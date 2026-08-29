---
tags: [checklist, formation, millenium]
---

# Ajouter une leçon au RAG Millenium (et l'exporter vers le vault)

Processus pour intégrer une nouvelle vidéo/leçon (masterclass, cours, etc.) au pipeline RAG du
projet `C:\Users\LENOVO\Documents\Millenium`, jusqu'à sa synthèse dans ce vault
(`03_knowledge/formations/`). À suivre **dans l'ordre**, sans sauter d'étape — chaque étape a
un garde-fou pour une raison précise (voir les incidents passés du projet).

⚠️ Ce projet est parfois travaillé en parallèle par plusieurs sessions Claude Code sur la même
base (`chunks_db.sqlite`, `tella_mapping.csv`). Toujours lancer `check_duplicates.py` avant ET
après toute écriture.

## 0. Pré-requis

```bash
cd C:\Users\LENOVO\Documents\Millenium
python check_duplicates.py
```

Doit afficher "OK : aucun doublon detecte" avant de commencer. Si ce n'est pas le cas, ne pas
continuer — investiguer d'abord.

## 1. Récupérer le transcript

Selon la source :
- **Leçon hébergée sur Tella** (cas standard de la plateforme Millenium) : utiliser
  `scrape_tella.py` avec le titre exact de la leçon présent dans `tella_mapping.csv`.
- **Autre source** (ex. un replay Circle.so d'un masterclass live, comme celui d'Alexis Buhaj) :
  la vidéo peut avoir un endpoint de transcript natif différent (ex.
  `academy.theyo.co/media_transcripts/<id>.vtt`) — l'inspecter via les requêtes réseau de la
  page. Télécharger le VTT brut.

**Vérifier le titre exact** : la colonne `titre`/le nom de fichier doit être le nom EXACT de la
leçon tel qu'affiché sur la plateforme — un espace, un accent ou une majuscule différente crée
un doublon silencieux en base.

## 2. Mettre le transcript au bon format

Le script de chunking attend un format précis, tête + corps :

```
Categorie: <Nom du module, ex. Masterclass>
Section: <Nom de la section>
Lecon: <Titre exact de la leçon>
---

[MM:SS] Premier segment de texte (une phrase ou un groupe de phrases cohérent)
[MM:SS] Segment suivant
...
```

- Si la source est un VTT brut (cues très courts, un par sous-titre), il faut **fusionner les
  cues consécutives en segments de taille phrase** (couper sur `.`/`!`/`?` ou après ~40 mots),
  en gardant le timestamp du **premier** cue de chaque segment fusionné. Convertir
  `HH:MM:SS.mmm` en minutes totales `MM:SS` (au-delà de 59 minutes, continuer en 3+ chiffres,
  ex. `122:21` — c'est juste une étiquette, pas une contrainte de format stricte).
- Placer le fichier dans `transcripts/<module-slug>/<sous-dossier-existant>/<Titre exact>.txt`
  — regarder la convention déjà en place pour ce module (ex. `transcripts/masterclass/masterclass/`).
- ⚠️ Écrire le fichier avec un outil qui garantit l'UTF-8 (Write, pas un heredoc bash) si le
  titre contient des caractères spéciaux (ex. « • ») — un heredoc peut les corrompre
  silencieusement.

```bash
python check_duplicates.py   # doit rester OK après l'ajout du fichier
```

## 3. Chunker (découpage sémantique)

```bash
python .claude/skills/docx-millenium/scripts/chunk_transcripts.py
```

Idempotent (`UNIQUE(transcript_file, chunk_num)`, erreurs d'intégrité ignorées) — traite en
réalité **tous** les fichiers de `transcripts/` à chaque run, pas juste le nouveau, donc c'est
lent (recalcule les embeddings de détection de frontières pour tout). **Lancer en arrière-plan**
plutôt qu'en avant-plan avec un timeout court. Le script ne fait qu'un seul `commit()` à la fin
— une interruption en cours de route ne sauvegarde rien.

Noter le nombre de nouveaux chunks insérés et leur plage d'`id` (affiché en fin de run, ou
requêter `SELECT MIN(id), MAX(id) FROM chunks WHERE status='pending'`).

## 4. Exporter les chunks en attente

```bash
python .claude/skills/docx-millenium/scripts/list_pending_chunks.py --limit <N> --out batch.json
```

`<N>` = nombre de chunks obtenu à l'étape 3.

## 5. Enrichir (résumé/concepts/outils/tips/cas d'usage/type)

Pour chaque chunk du batch, produire un objet :

```json
{
  "id": <id du chunk>,
  "resume": "1-3 phrases résumant précisément CE chunk",
  "concepts": ["concept 1", "concept 2"],
  "outils": ["Outil A"],
  "tips_techniques": ["Conseil actionnable si présent"],
  "cas_d_usage": ["Exemple concret d'usage si présent"],
  "type_contenu": "theorie|demonstration_pratique|anecdote|chiffre_cle"
}
```

**⚠️ Point critique — bug de décalage d'ID (déjà rencontré 2 fois sur ce projet) :**
Sur un transcript long (50+ chunks) avec un style de parole très fluide ("du coup", "en fait",
"voilà" en continu), il est très facile de perdre l'alignement exact entre l'`id` et son
`texte_brut` en composant les résumés à la volée depuis la mémoire d'une lecture précédente —
le contenu glisse d'un id vers le suivant (ou le précédent) sans s'en rendre compte, souvent à
partir d'un point précis puis en cascade sur le reste du batch.

**Méthode qui fonctionne, à suivre strictement pour tout batch de plus de ~15 chunks :**
1. Ne jamais composer un résumé "de mémoire" à partir d'une lecture large faite plus tôt.
2. Traiter par lots de 10 id maximum.
3. Pour chaque lot, **re-requêter la base** juste avant de rédiger, avec un marqueur explicite
   par id (`###ID=<id>###\n<texte_brut>\n###END###`), et rédiger immédiatement en regardant ce
   texte, jamais en scrollant vers un extrait lu plus haut.
4. Ne jamais réutiliser un résumé déjà écrit pour un id voisin, même si le sujet semble continu
   — chaque id a son propre texte, distinct.

## 6. Vérifier AVANT d'appliquer (obligatoire, jamais sauter)

```bash
python3 -c "
import json, sqlite3
enriched = json.load(open('batch_enrichi.json', encoding='utf-8'))
conn = sqlite3.connect('chunks_db.sqlite')
cur = conn.cursor()
merged = []
for item in enriched:
    cur.execute('SELECT texte_brut FROM chunks WHERE id=?', (item['id'],))
    merged.append({'id': item['id'], 'texte_brut': cur.fetchone()[0], 'resume': item['resume']})
json.dump(merged, open('for_verify.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
"
python verify_enrichment.py for_verify.json
```

- **0 décalage** ou uniquement des scores bas (<25) sur des id isolés (pas de série contiguë) →
  probablement des faux positifs (vocabulaire partagé entre chunks voisins/thématiquement
  proches) — mais **vérifier quand même chacun manuellement** en comparant le résumé au
  `texte_brut` exact de son id avant de conclure.
- **Série contiguë de décalages avec scores croissants (30+)** → vrai bug. Reprendre l'étape 5
  pour la plage concernée en repartant de zéro (étape 6.4 ci-dessus), jamais en essayant de
  "patcher" un décalage en place (ça introduit presque toujours un nouveau décalage ailleurs).
- Recommencer la vérification jusqu'à obtenir un état propre.

## 7. Appliquer à la base

```bash
python .claude/skills/docx-millenium/scripts/apply_enrichment.py for_verify.json
```

⚠️ Si erreur `no such column: cas_d_usage` (ou une autre colonne) : la base principale
(`chunks_db.sqlite` à la racine) peut être en retard sur le schéma par rapport à la copie de dev
utilisée par le skill (`.claude/skills/docx-millenium/chunks_db.sqlite`). Vérifier avec
`PRAGMA table_info(chunks)` sur les deux, et ajouter la colonne manquante sur la base principale
avec `ALTER TABLE chunks ADD COLUMN <nom> TEXT` (non destructif) avant de relancer.

```bash
python check_duplicates.py   # doit rester OK après l'écriture
```

## 8. Exporter la synthèse vers le vault

```bash
python export_millenium_notes.py --module "<Nom du module, ex. Masterclass>"
```

Génère/actualise `03_knowledge/formations/<module-slug>/<lecon-slug>.md` (une note légère par
leçon : résumé, concepts, outils, tips — jamais le texte brut complet, pour rester dans l'esprit
"index léger" du vault) et régénère `_index.md` du module.

## 9. Committer et pousser le vault

```bash
cd "C:\Users\LENOVO\Documents\Obsidian\BLUE IMPAKT"
git add -A && git commit -m "Add <titre leçon> synthesis note" && git push
```

## Pour interroger le RAG ensuite

Utiliser le skill `millenium-rag` (ou `query_rag.py` directement depuis
`C:\Users\LENOVO\Documents\Millenium`) — recherche fine sur les 6600+ chunks bruts, plus précise
que les notes de synthèse du vault quand une question pointue le nécessite.
