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

## Journal
- 2026-08-29 : Repo analysé, fiche créée. Pattern "JSONbin comme source de vérité + garde-fous stricts anti-écrasement" à retenir — potentiellement réutilisable pour d'autres sites à contenu live-éditable.
- 2026-08-31 : Bug résolu — tracés d'expédition qui revenaient à leur position initiale en cours d'édition (race condition entre le `fetch` JSONbin `/latest` au chargement et une édition démarrée avant sa réponse). Fix par flag `localDirty` (`index.html:545-547`, `index.html:2620-2627`), déployé (commit `4bc0499`). Voir [[jsonbin-source-de-verite]] et `03_knowledge/troubleshooting.md`. Identité git du repo corrigée (`melvin.perrottet@blue-impakt.org`) — à vérifier si l'amend+force-push du commit `4bc0499` (mauvaise adresse) a bien été fait.

- 2026-09-07 : Commit `aa64cd8` poussé — `.gitignore` (ignore `graphify-out/` + `.claude/settings.local.json`) et `CLAUDE.md` (règles graphify).

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-carte
