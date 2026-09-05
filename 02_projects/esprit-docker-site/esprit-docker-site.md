---
tags: [project, encours, esprit-docker]
created: 2026-08-29
statut: encours
client: esprit-docker
---

# esprit-docker-site

## Objectifs du projet
- Site e-commerce Next.js pour la vente de chapeaux (marque "Esprit Docker")
- Gros travail de gestion de catalogue produit : variantes visuelles (face/profil, couleurs type "sakura"), détourage/ombres, cohérence des visuels

## Livrables
- Site en production : [www.esprit-docker.com](https://www.esprit-docker.com)
- Pipeline de traitement d'images produit (scripts internes) : export pour Photoroom, correction d'ombres/reflets, feathering, dédoublonnage de variantes, audit de résolutions

## État actuel
- Site en production, légal à jour (mentions légales/CGU/CGV datées du 25 août 2026)
- Pipeline d'assets produit très développé (plusieurs dizaines de scripts `.mjs` de retouche/correction d'images) — probablement le vrai savoir-faire technique du projet

## Décisions techniques
- **Stack** : Next.js (App Router), déploiement Cloudflare Pages (`@cloudflare/next-on-pages`, wrangler)
- **Stockage images** : Cloudflare R2 (`@aws-sdk/client-s3` en client S3-compatible)
- **Base de données** : Neon (PostgreSQL serverless, `@neondatabase/serverless`)
- **UI** : Base UI (`@base-ui/react`), Tailwind, GSAP pour les animations
- **PDF** : `pdf-lib` (probablement génération de factures/documents)
- **Traitement visuel produit** : pipeline de scripts Node custom (pas un service tiers) pour préparer/corriger les photos produit avant mise en ligne

## Blocages / risques
-

## Next actions
- [ ]

## Journal
- 2026-08-29 : Repo identifié et analysé (`github.com/espritdocker/esprit-docker`), fiche projet créée
- 2026-09-02 : Fix mail de suivi colis Sendcloud (voir [[esprit-docker]] pour le détail du diagnostic) — ajout d'une note "vérifiez vos spams" dans `emailCommande.ts` et `succes/page.tsx`. Commit `944dca9` sur `master`.
- 2026-09-02 : Path B implémenté pour le mail "colis expédié" (voir [[esprit-docker]] pour le diagnostic complet) — `emailExpedition.ts` (envoi Brevo, même charte que la confirmation) + hook dans le webhook Sendcloud + colonne `commandes.suivi_email_envoye_at` (verrou anti-doublon). Migration exécutée et vérifiée sur Neon prod (projet `esprit-docker`, branche `production`). Commit+push `20a6fc6` sur `master`.
- 2026-09-04 : Graphify (graphe de code tree-sitter, voir `03_knowledge/outils.md`) installé et activé — 1108 nœuds/1673 edges, nudge `/graphify` actif en session. `.claude/settings.json` renommé en `.claude/settings.local.json` + gitignored (le hook contient un chemin `graphify.exe` propre à la machine de Melvin, à ne jamais committer).

## Liens
- Client : [[esprit-docker]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
- Repo / deployment : https://github.com/espritdocker/esprit-docker (Cloudflare Pages, R2, Neon)
