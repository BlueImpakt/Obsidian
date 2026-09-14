---
tags: [project, encours, blue-impakt]
created: 2026-08-29
statut: encours
client: blue-impakt
---

# km0-circuit-court

## Objectifs du projet
- Produit propre Blue Impakt (pas un projet client) : plateforme de circuit court mettant en relation producteurs locaux et consommateurs
- Principes fondateurs : 0% de commission sur les ventes (modèle SaaS/abonnement fixe ou participatif), zéro friction producteur, API-first

## Livrables
- **Phase 1 — Web-First (en cours)** : appli web responsive, carte interactive (Mapbox/Leaflet), gestion de stock producteur, Click & Collect avec paiement Stripe (capture différée au poids réel)
- **Phase 2 — Mobile (futur)** : app mobile (React Native ou Flutter) consommant la même API — backend inchangé

## État actuel
- Backend API REST en développement actif (NestJS)
- Admin/facturation déjà réfléchis concrètement (voir captures abonnements/TVA dans `ADMIN/` du repo — mensuel/annuel, option producteur)
- Paiements : Stripe (côté appli) + Mollie (côté abonnements/facturation ADMIN)

## Décisions techniques
- **Stack backend** : Node.js 20+, NestJS 10 (TypeScript), PostgreSQL 15+, Prisma 5, JWT (passport-jwt), Swagger sur `/docs`
- **Paiement** : Stripe (Payment Intents, capture manuelle) pour les commandes ; Mollie pour la facturation/abonnements
- **Frontend** : Vite + TypeScript (dossier `frontend/`), déploiement Vercel (`frontend/vercel.json`)
- **Séparation stricte** : le backend ne sait pas qui l'appelle (web ou mobile) — jamais de logique front dans le backend
- **Sync Notion** : scripts (`scripts/sync_notion.py`, `patch_notion_categories.py`) pour synchroniser du contenu/catégories depuis Notion

## Blocages / risques
-

## Next actions
- [ ]

## Journal
- 2026-08-29 : Repo identifié (`github.com/BlueImpakt/KM0`), fiche projet créée. Découverte importante : Blue Impakt n'est pas qu'une activité de service (auto/no-code/consulting) mais développe aussi son propre produit SaaS.
- 2026-09-04 : Graphify (graphe de code tree-sitter, voir `03_knowledge/outils.md`) installé et activé — 1319 nœuds/2761 edges, nudge `/graphify` actif en session. C'était la cible initiale de l'outil (projet long-vivant, sessions répétées).

## Liens
- Repo / deployment : https://github.com/BlueImpakt/KM0 (backend NestJS + frontend Vite/Vercel)
- Patterns utilisés :
