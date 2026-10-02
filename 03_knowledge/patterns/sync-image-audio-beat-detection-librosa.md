---
tags: [pattern, code, validé]
created: 2026-09-21
type: code
---

# sync-image-audio-beat-detection-librosa

## Contexte

Lecteur d'animation plein écran [[naeco-carte]] (observation rorqual) : défilement
rapide de photos calé sur un extrait audio réel (Woodkid, "Run Boy Run"). Le
premier jet était un motif de durées tapé à la main (blocs 0.4s/0.9s ajustés par
essais-erreurs, vérifiés en exportant des vidéos ffmpeg à chaque itération) — ça
"sonnait juste" à peu près, mais avec un décalage systématique perceptible et
aucune garantie que les coupes tombent vraiment sur les transitoires du morceau.

Remplacé par une détection de beat réelle (librosa) : le motif rythmique reste
choisi à la main (nombre de coupes courtes/longues par "phrase"), mais les
**timestamps** de chaque coupe viennent de l'analyse audio, pas d'une constante.

## Comment ça marche

### 1. Détection tempo + beats (dynamic programming, pas d'heuristique maison)
```python
import librosa
y, sr = librosa.load(audio_path, sr=None, mono=True)
onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=128)
tempo, beat_frames = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, hop_length=128, trim=False)
beat_times = librosa.frames_to_time(beat_frames, sr=sr, hop_length=128)
```
Un script maison (STFT + autocorrélation + seuil de pic) donnait déjà un tempo
correct à ~3 BPM près, mais librosa (beat-tracker à programmation dynamique,
Ellis 2007) est plus robuste et ne saute jamais un temps même dans un passage
faible. **madmom a été écarté** : dernier build 2018, incompatible Python
3.14 / numpy 2.x sur ce poste — ne pas perdre de temps à forcer l'install sur
un environnement récent, aller direct à librosa.

### 2. Corriger le décalage pic vs attaque réelle (~20-40ms)
Le beat-tracker pointe le **pic d'énergie** de chaque coup, pas son **attaque**
(le son a un temps de montée). Symptôme perçu : "l'image arrive en retard sur le
beat". Fix : recaler chaque beat sur l'onset backtracké le plus proche (walk-back
jusqu'au minimum d'énergie précédent = la vraie attaque) :
```python
onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr,
                                     hop_length=128, backtrack=True, units="frames")
onset_times = librosa.frames_to_time(onsets, sr=sr, hop_length=128)
# puis, pour chaque beat, chercher l'onset backtracké le plus proche
# dans une fenêtre de ±80ms et le substituer au beat
```
Décalage moyen mesuré sur ce cas : ~22ms (jusqu'à 40-50ms sur certains coups).
Sensible à l'oreille — ne pas sauter cette étape.

### 3. Motif rythmique manuel appliqué sur la vraie grille de beats
Le motif ("phrase" de 16 beats / 13 images : 10 coupes d'1 beat + 3 coupes de
2 beats fusionnés) reste une décision artistique humaine, mais consomme les
**vrais timestamps** plutôt que des constantes 0.4s/0.9s :
```python
PATTERN = [1]*6 + [2] + [1]*4 + [2]*2   # nb de beats consommés par slot
bi = 0
for span in PATTERN * N_PHRASES:
    t0, t1 = beats[bi], beats[bi + span]
    slots.append((t0, t1))
    bi += span
```
Résultat : durées ~0.43-0.47s (au lieu d'un fixe 0.45s) et ~0.87-0.91s — la
variation suit les micro-fluctuations réelles du tempo du morceau.

### 4. Piège ffmpeg : images sources hétérogènes → perte de frames silencieuse
Symptôme signalé par l'utilisateur : "il n'y a qu'une image fixe", incohérent
avec le CSV, rendu différent PC/téléphone. Cause réelle : les images sources
(tailles et pixel formats JPEG différents — 800×533 en 4:4:4, 800×366, un
en 4:2:0...) forcent le filtre `scale+crop` de ffmpeg à **reconfigurer tout
le graphe de filtres à chaque changement d'image**, ce qui fait perdre presque
toutes les frames (12 frames encodées pour 5.4s attendues). Le fichier de sortie
garde pourtant une métadonnée de durée correcte (héritée de la piste audio), donc
`ffprobe -show_entries format=duration` ne détecte rien d'anormal — seul un
`grep "Reconfiguring filter graph"` dans le log ffmpeg, ou un contrôle de
diversité des frames décodées, révèle le bug.

**Fix** : normaliser toutes les images (même taille, même format pixel) *avant*
de les donner au concat demuxer :
```python
from PIL import Image, ImageOps
def cover_resize(im, w, h):
    im = ImageOps.exif_transpose(im)
    sw, sh = im.size
    scale = max(w/sw, h/sh)
    im = im.resize((round(sw*scale), round(sh*scale)), Image.LANCZOS)
    left, top = (im.width-w)//2, (im.height-h)//2
    return im.crop((left, top, left+w, top+h))
# sauvegarder en JPEG quality=92, subsampling=0 (4:4:4) pour TOUTES les images
```
Après normalisation : plus aucun "Reconfiguring filter graph" dans le log,
durée réelle = durée attendue, diversité de frames confirmée par échantillonnage
(hash des frames extraites à intervalle régulier).

### 5. Vérification — ne jamais se fier à un seul contrôle
- `ffprobe -show_entries format=duration` seul est **insuffisant** (peut mentir,
  cf. piège ci-dessus).
- `ffprobe -count_frames -select_streams v:0` s'est lui aussi révélé **peu
  fiable** sur ce pipeline (a donné une durée de 1.84s sur un fichier confirmé
  correct par ailleurs — probablement un bug/quirk de cette requête précise avec
  des fichiers issus du concat demuxer).
- Le contrôle qui marche vraiment : décoder plusieurs frames à intervalle
  régulier (`-vf "select='not(mod(n\,50))'"`) et comparer leurs hash MD5 —
  confirme une vraie diversité d'images sur toute la durée, pas seulement au
  début.

## Code / config

```
Stack : Python (librosa, numpy/scipy, Pillow), ffmpeg (concat demuxer + libx264)
Détection : librosa.beat.beat_track + librosa.onset.onset_detect(backtrack=True)
Normalisation images : Pillow (cover-resize + crop, subsampling=0 uniforme)
Rendu vérif : ffmpeg -f concat -safe 0 -i list.txt -i audio.wav -vf fps=25 ...
```

## Quand le réutiliser

Tout projet où des images doivent défiler en synchro précise avec un morceau
réel (pas un métronome généré) : lecteurs d'animation, générateurs de reels/
contenu social calé sur musique, tout pipeline ffmpeg photo→vidéo avec des
images sources hétérogènes en taille/format (le piège de l'étape 4 n'est pas
spécifique à l'audio-sync, il touche **tout** slideshow ffmpeg avec des JPEG
de tailles/subsampling variés).

## Cas d'usage réels
- [[naeco-carte]] — lecteur d'animation plein écran, observation rorqual (33
  photos réelles, motif 16 beats/13 images × 16 phrases, séquence complète en
  CSV : `sync-image-audio-beat-detection-librosa-sequence.csv`)
