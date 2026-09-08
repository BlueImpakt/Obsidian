---
tags: [project, encours, blue-impakt]
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
- Refonte (2026-08-31) : charte graphique d'origine conservée à l'identique (navy `#07111D`, dégradés bleu→vert, DM Serif Display, cartes arrondies, glows) — seule la discipline de grille modulaire Müller-Brockmann (12 col, baseline 8px, gouttières 24, marges 64) et Motion (remplace GSAP/ScrollTrigger, Lenis conservé) s'appliquent en dessous. Fichier unique `index.html` conservé.

## Blocages / risques
-

## Next actions
- [ ] Exécuter le plan de refonte (10 tâches, subagent-driven-development) sur la branche `refonte-swiss-grid`
- [ ] Trancher au merge : suppression ou archivage des fichiers `preview-v*.html` dans `docs/`

## Journal
- 2026-08-29 : Repo identifié (`github.com/BlueImpakt/Site-web`), fiche projet créée dans le vault, positionnement ICP mis à jour dans CLAUDE.md à partir du contenu réel du site
- 2026-08-31 : Refonte lancée — skills `muller-brockmann-grid-systems` + `motion` installés en global, brainstorming (4 maquettes : V2 Swiss pur, V3, V2b alternance sombre/clair, écartées), tranché sur V4 (charte d'origine + grille dessous). Spec (`docs/superpowers/specs/2026-08-31-refonte-grille-muller-brockmann-design.md`) et plan (`docs/superpowers/plans/2026-08-31-refonte-grille-muller-brockmann.md`) écrits et commités sur branche `refonte-swiss-grid` (repo local `C:\Users\LENOVO\Documents\GitHub\Site-web`), `main` intact. Exécution en 10 tâches (subagent-driven-development) lancée.

## Liens
- Client : [[blue-impakt]]
- Patterns utilisés : `muller-brockmann-grid-systems`, `motion`
- Repo / deployment : https://github.com/BlueImpakt/Site-web (Cloudflare Pages, projet `blue-impakt`) — branche de travail `refonte-swiss-grid`
