---
tags: [project, encours, naeco]
created: 2026-08-29
statut: encours
client: naeco
---

# naeco-carte

## Objectifs du projet
- Carte interactive des expéditions NAECO : tracés de navigation, observations scientifiques, données Pelagos, escales, sites d'étude

## Livrables
- Page "Carte interactive" (`index.html`), données dans `naeco_data.json`
- Exemple de donnée : expédition 2022 "The Pelagos Sanctuary" (Sanctuaire Pelagos, biodiversité pélagique/cétacés, collab STARESO, tracé GPS complet, vidéo YouTube embarquée)

## État actuel
- En production, déploiement Cloudflare Pages + config Netlify présente (`netlify.toml`) — à clarifier laquelle est la plateforme réellement utilisée

## Décisions techniques
- **Stack** : HTML unique + JSON de données, pas de framework
- **Données live** : synchronisées via **JSONbin** (bin distinct de naeco-site), contient `expeditions`, `observations`, `pelagosData`, `stats`, `general`, `escales`, `sitesEtude`
- **Règles de travail strictes (définies par le client dans son propre CLAUDE.md)** :
  - Ne **jamais** `git push` sans instruction explicite ("déploie")
  - Attendre validation ("ok"/"tu peux coder") avant d'implémenter un contenu discuté
  - Chercher des sources officielles avant tout contenu réglementaire/scientifique (réglementation AMP, UICN, espèces)
  - Toujours lire JSONbin avant modif de contenu — ne jamais écraser depuis le HTML
  - Ne jamais réécrire les `coords` des expéditions depuis le HTML — les récupérer depuis JSONbin telles quelles
  - Ne jamais pousser les données complètes vers JSONbin — patcher uniquement les champs modifiés
- ⚠️ Clé JSONbin non recopiée ici (voir repo client)

## Blocages / risques
- `sync.sh` a un bug de path connu côté client — déploiement à faire manuellement (`git add/commit/push`)

## Next actions
- [ ] Vérifier si le commit `4bc0499` a bien été amendé (mauvaise adresse email) + force-pushé sur `main`
- [ ] Custom domain `track.naecoexpedition.org` (optionnel) — la zone Cloudflare vue par `wrangler` ne correspond pas au bon compte, à refaire proprement si souhaité ; le Worker tourne déjà sur son URL `.workers.dev`, aucun impact fonctionnel
- [ ] Pousser le commit en attente (header mobile responsive `a75b2f2`)
- [ ] Créer une clé JSONbin restreinte en lecture seule (dashboard JSONbin.io) et déployer un proxy Cloudflare Worker pour l'écriture (comme `naeco-track`) — corrige le mot de passe éditeur et la clé JSONbin actuellement en clair dans `index.html`

## Journal
- **Archive** : historique détaillé du 2026-08-29 au 2026-09-10 (setup JSONbin, tracking live catamaran, refonte légende/charte graphique) condensé dans [[journal-archive-2026-08]] — détail commit par commit dans l'historique git du repo.

- 2026-09-11 : Bug "création de site d'étude cassée" corrigé — cause : les polygones AMP/Pelagos et les markers Leaflet font `stopPropagation()` sur leur clic (pour ouvrir leur fiche), ce qui empêchait le clic de placement d'atteindre son handler. Fix : listener en phase de capture sur `document`, actif seulement pendant un placement réel. Poussé (`7bc57e6`). Effet de bord découvert : 16 sites d'étude vides dans le JSONbin (tentatives précédentes silencieusement ratées à cause du même bug) — supprimés, ne restent que les 4 vrais sites Point Zéro.
- 2026-09-11 (suite) : Bug photo escale Ajaccio (fenêtre noire) corrigé — le champ `photo` contenait un lien de partage Google Drive collé tel quel dans une balise `<img>` (échoue silencieusement). Fonction `gdriveImg()` ajoutée pour convertir ce format vers l'URL image directe `lh3.googleusercontent.com/d/ID`, appliquée partout où une photo est affichée (obs, escale, expédition, sites d'étude). Commit `b209418`, **pas encore poussé**.
- 2026-09-11 (suite) : Nouveau site d'étude Point Zéro ajouté dans JSONbin (`sitesEtude`, 5ᵉ entrée) — « Prélèvement microplastique », au large de Galéria (42.12585, 8.60099), 11/09/2026 09:00 (position réelle 07:00:07 UTC), protocole filet Manta identique à l'entrée du 10/09 à Calcatoggio.
- 2026-09-11 (suite) : Commit `b209418` (fix photo Google Drive escale Ajaccio) poussé sur `main`. Nouvelle demande client : galerie multi-images — possibilité d'ajouter plusieurs photos et d'ouvrir une fenêtre galerie (80% écran, navigation flèches gauche/droite) au clic sur une image.
- 2026-09-11 (suite) : Galerie plein écran multi-photos implémentée — clic sur une photo (site d'étude/observation/escale) ouvre une visionneuse 80vw/80vh, navigation flèches gauche/droite + clavier, compteur ; champ `photo` unique des escales migré vers `media[]` (multi-photos, migration transparente à la sauvegarde). Poussé (`20cfcba`). Nouvelle demande client : marqueurs photo indépendants des observations — icône « pin goutte » retenue parmi 4 styles proposés en visuel ; reste à implémenter (onglet « Photo » dans l'éditeur, clic carte pour placer, URL comme escales, multi-photos, réutilisation de la galerie plein écran).
- 2026-09-11 (suite) : Marqueurs photo indépendants des observations implémentés — nouvel onglet « Photo » dans l'éditeur (pin goutte violet, clic sur la carte pour placer, position + reverse-géocodage auto, plusieurs photos, galerie plein écran réutilisée). ⚠️ Découverte en testant : le fichier synchronise en direct chaque modif vers un JSONbin de **production** (clé en dur) — clics de test poussés par erreur puis restaurés avec validation explicite de Melvin avant chaque push correctif. Poussé (`8a72672`). Formulaire simplifié ensuite sur retour client — retrait des champs "Expédition associée" et "Description" (plus utilisés), popup carte n'affiche plus que la ou les photos (plus de lieu/titre), champ "Nom" devient un repère interne éditeur uniquement. Poussé (`af145a4`).
- 2026-09-11 (suite) : Faille de sécurité identifiée — mot de passe éditeur (`EDIT_PWD`) et clé JSONbin (accès complet lecture/écriture aux données de production) tous deux en clair dans `index.html`, lisibles via "Afficher le code source" (contourne même le mot de passe). Décision : restreindre la clé JSONbin publique en lecture seule + proxy Cloudflare Worker (même pattern que `naeco-track`) qui détient la vraie clé d'écriture côté serveur ; UI et mot de passe éditeur inchangés côté utilisateur. Reste à faire côté Melvin : créer la clé JSONbin read-only (dashboard JSONbin.io) + déployer le Worker (code à préparer côté Claude).
- 2026-09-11 (suite) : Root cause du flash de légende (fix probabiliste `8118cbd`, jamais résolu) diagnostiquée précisément à partir d'une vidéo client — le calque `.lp` isolé par `contain:layout style paint` se présentait à ses bornes périmées (largeur du panneau **vide**, 34px = `border+padding×2+border`) car une animation `stroke-dashoffset` (`dash-flow`) **morte** — propriété SVG appliquée par erreur à une `<div>`, le trait est en réalité un `background-image` — forçait un repaint continu du calque. Corrigé (retrait du `contain` mal posé), poussé avec le fix Photos (`8a72672`). Second flash découvert sur la carte elle-même (bande de tuiles rastérisées périmées, 23% des frames, colonne fixe x=798→1168) — même cause : `.exp-dash` (la trace pointillée) partage son unique `<svg>` avec le polygone Pelagos (`fill-opacity:0.15`), et `stroke-dashoffset` n'a pas de fast-path compositeur → tout le calque SVG overlay est re-rasterisé en continu (~60/s mesurés). Animation passée à `steps(8)` (~5,7 repaints/s), vérifié visuellement, poussé (`af145a4..6f98227`).

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-carte
