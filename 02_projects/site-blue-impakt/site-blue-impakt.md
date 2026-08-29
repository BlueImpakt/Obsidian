---
tags: [project, encours]
created: 2026-08-29
statut: encours
client: blue-impakt
---

# site-blue-impakt

## Objectifs du projet
- Site vitrine Blue Impakt : présenter l'offre (automatisations, agents IA, dev web/no-code, conseil stratégique) pour associations environnementales et entreprises à impact

## Livrables
- Site statique (`index.html`) avec positionnement "L'IA au service de l'environnement et de l'humain"

## État actuel
- Site existant et déployé (Cloudflare Pages, projet Wrangler `blue-impakt`)
- Contient une section hero animée (GSAP), photo de profil (Melvin Perrottet)

## Décisions techniques
- Stack : HTML/CSS/JS statique, pas de framework — assets servis directement (`[assets] directory = "."` dans `wrangler.toml`)
- Déploiement : Cloudflare Pages via Wrangler
- Polices : Google Fonts (DM Serif Display, DM Sans, Fragment Mono)

## Blocages / risques
-

## Next actions
- [ ]

## Journal
- 2026-08-29 : Repo identifié (`github.com/BlueImpakt/Site-web`), fiche projet créée dans le vault, positionnement ICP mis à jour dans CLAUDE.md à partir du contenu réel du site

## Liens
- Client : [[blue-impakt]]
- Patterns utilisés :
- Repo / deployment : https://github.com/BlueImpakt/Site-web (Cloudflare Pages, projet `blue-impakt`)
