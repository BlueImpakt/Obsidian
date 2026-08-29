---
tags: [project, encours, naeco]
created: 2026-08-29
statut: encours
client: naeco
---

# naeco-site

## Objectifs du projet
- Site vitrine NAECO : "Mobiliser l'art et la science pour l'océan"
- Présenter les expéditions à la voile, créations artistiques, actions de sensibilisation

## Livrables
- Site public : https://naeco-site.naeco.workers.dev
- Pages : accueil, campagne océanographique, mobilité

## État actuel
- Site en production, déployé sur Cloudflare Pages (auto-déploiement au push `main`)

## Décisions techniques
- **Stack** : fichier HTML unique (`index.html`), pas de framework
- **Contenu live-éditable** : un éditeur en ligne (raccourci Ctrl+Shift+E, protégé par mot de passe — voir gestionnaire de secrets du client, pas stocké ici) permet à l'équipe NAECO de modifier textes/images/liens/couleurs sans toucher au code. Les changements sont synchronisés vers **JSONbin** (bin privé) avec debounce ~600ms.
- **Règle de travail critique** : toujours lancer `check-remote.sh` en début de session pour récupérer l'état actuel du contenu depuis JSONbin avant toute modification — sinon risque d'écraser des changements faits par l'équipe via l'éditeur
- **Déploiement** : `sync.sh "description"` → commit + push → Cloudflare Pages redéploie automatiquement
- ⚠️ Le repo client contient une clé maître JSONbin et un mot de passe éditeur en clair dans son propre `CLAUDE.md` — **volontairement non recopiés ici**, à récupérer directement depuis le repo/le client si besoin

## Blocages / risques
- Repo GitHub source de vérité ambigu : le `CLAUDE.md` du projet référence `melp-cloud/naeco-site`, alors que le clone a été fait depuis `NAECOEXPEDITION/naeco-site` — à clarifier lequel est le remote actif avant de pousser du code
- 🔴 **Sécurité** : clé maître JSONbin + mot de passe éditeur stockés en clair dans le `CLAUDE.md` du repo client (pas juste référencés — la valeur elle-même). Si le repo fuite ou si l'accès change de mains, ces secrets sont exposés tels quels.

## Next actions
- [ ] Signaler à NAECO l'exposition en clair de la clé maître JSONbin + mot de passe éditeur dans leur `CLAUDE.md`, recommander de les déplacer vers un gestionnaire de secrets (variable d'environnement, coffre-fort partagé) et de les faire tourner par précaution

## Journal
- 2026-08-29 : Repo analysé, fiche projet créée. Pattern JSONbin + éditeur live noté comme knowledge réutilisable.

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-site (Cloudflare Pages)
