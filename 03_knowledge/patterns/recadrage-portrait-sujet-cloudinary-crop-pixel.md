---
tags: [pattern, code, validé]
created: 2026-09-29
type: code
---

# recadrage-portrait-sujet-cloudinary-crop-pixel

## Contexte

Lecteur d'animation [[naeco-carte]] : photos de baleines (48 photos V24, paysage
4:3 / 3:2) affichées dans une boîte `.ap-box` qui passe en **portrait 3:4 sous
600px** (`@media (max-width:600px)`). Un `object-fit:cover` d'une photo paysage
dans cette boîte zoome et décale : sujet coupé ou hors cadre. Objectif : sujet
**centré au max** sur mobile, sans perte de qualité, sans letterbox.

Ordre des essais (chacun a échoué avant le suivant) : `g_auto` → `g_xy_center` avec
coordonnées lues à l'œil → **crop pixel exact + détection + vérification visuelle**.

## Comment ça marche

### 1. Pourquoi `g_auto` ne suffit pas
`c_fill,g_auto,ar_3:4` rate les sujets petits / peu contrastés (dos de baleine sur
mer, souffle, contre-jour) : cadre vide ou sujet coupé sur ~10 photos sur 48. Bon
pour un premier jet global, pas pour un centrage fiable. **Ne pas refaire le test.**

### 2. `g_xy_center` : pièges
- `x_0.30,y_0.62` (fractions) → **400** ("Requested 2400000x3200000"). Il faut des
  **pixels**, donc les dimensions réelles : `.../fl_getinfo/<chemin>.jpg` → JSON
  `input.width/height`.
- Sur une photo paysage, la hauteur est déjà "pleine" dans un cadre 3:4 : **seul x
  compte**, y est ignoré. Ne pas perdre de temps à raffiner y.
- Le point donné est bien le centre de la fenêtre → si le résultat est décalé,
  l'erreur vient de la lecture du sujet, pas de Cloudinary.

### 3. Crop pixel déterministe (méthode retenue)
Calculer soi-même la fenêtre 3:4 puis `c_crop` + `c_scale` : contrôle total.
```python
if W/H > 0.75:                      # paysage : hauteur pleine, on ne joue que sur x
    cw, ch = round(H*0.75), H
    left = clamp(round(cx*W - cw/2), 0, W-cw); top = 0
else:                               # déjà plus étroit que 3:4 : largeur pleine, on joue sur y
    cw, ch = W, round(W/0.75)
    left = 0; top = clamp(round(cy*H - ch/2), 0, H-ch)
url = f"{BASE}/c_crop,x_{left},y_{top},w_{cw},h_{ch}/c_scale,w_1200/f_auto,q_auto/{path}"
```
Le crop sortant est **exactement** au ratio de la boîte → `object-fit:cover` devient
un no-op côté navigateur (pas de second recadrage).

### 4. Trouver le centre du sujet : détection + ROI manuelle
Détection auto seule = fausse (bateaux, 2e baleine lointaine, reflets). Recette :
1. **ROI dessinée à la main** par photo (fractions x0,x1,y0,y1) autour du sujet,
   excluant les distracteurs.
2. Image réduite à 1000px, **anomalie par rapport à la médiane de sa ligne**
   (retire le dégradé horizontal mer/ciel), flou box 5px.
3. Seuil = 99e percentile de l'anomalie **hors ROI** ; masse cumulée dans la ROI,
   bbox entre 3 % et 97 % → centre = `cx`.
Marche pour dos/souffle contrastés ; échoue sur les sujets très faibles (S01, S07,
L22 : bbox dégénérée) → corriger à l'œil.

### 5. Boucle de vérification (indispensable)
- Planche par lot de 6, **grille à 10 %** avec étiquettes (pas 25/50/75 : erreurs
  de ±10 % → sujet visiblement décalé), tuiles ≥ 640px de large.
- Overlay : jaune = ROI, rouge = détection, **vert = fenêtre de crop finale**.
- Planche finale des 48 crops avec **ligne rouge verticale au centre** → l'écart
  se voit d'un coup d'œil ; itérer sur les 2-3 photos décalées.
- Centrer sur le **centroïde visuel du sujet entier** (corps + souffle), pas sur la
  tête ni le souffle seul.

### 6. Photos aériennes verticales : rotation
Drone top-down (baleine horizontale, 4:3) : plutôt que de rogner une tranche
verticale (tête/queue perdues), `a_-90,c_fill,ar_3:4,w_1200,f_auto,q_auto`
(rotation gauche ; 4:3 tourné ≈ 3:4 exact) → baleine entière, verticale, sans
recadrage. `a_-90` = anti-horaire, `a_90` = horaire.

### 7. Câblage dans le lecteur
Deuxième pool `photosByDurMobile` (mêmes 24 long + 24 short, mêmes indices) dans la
banque ; helper qui choisit le pool selon `matchMedia('(max-width:600px)')` ;
`buildAnimSequence` utilise ce pool partout (tirage, file anti-répétition,
détection de clé de pool). Desktop inchangé (`photosByDur`, crop 16:9).

## Pièges rencontrés
- **Cache de planche périmé** : les fichiers cache étaient nommés par nom d'image
  (`rorqual-V24-11.jpg`), j'avais supprimé `L11.jpg` (inexistant) → la planche
  montrait encore l'ancien rendu. Toujours supprimer le fichier réellement
  utilisé, et vérifier que la planche a bien changé.
- **Le problème de précision venait de la méthode, pas du modèle** : lecture sur
  planche réduite + grille grossière → erreurs. Passer à un modèle plus gros n'était
  pas nécessaire ; la boucle fermée (détection + overlay + ligne centrale) a suffi.
- ffmpeg/libx264 exige largeur et hauteur **paires** (675×900 refusé → 720×960).

## Limites
- Photos paysage : **centrage vertical impossible** (hauteur pleine) sans zoomer de
  15-20 % (option non appliquée).
- Sujet plus large que le cadre portrait (baleine entière sur S20/S23) : centrage
  sur le corps, extrémités coupées.
- Sujet quasi invisible dans l'original (contre-jour, très lointain : L02, L19, S18) :
  aucun recadrage ne le sauve.

## Cas d'usage réels
- [[naeco-carte]] — lecteur d'animation rorqual V24, commits `97213c9` (crop mobile
  g_auto), `00516ce` (crops pixel recentrés + L11-L14 en rotation).
- Complémentaire de [[sync-image-audio-beat-detection-librosa]] (même lecteur).
