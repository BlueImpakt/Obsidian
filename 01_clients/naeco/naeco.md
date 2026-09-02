---
tags: [client, actif, p2, environnement, france]
created: 2026-08-29
statut: actif
priorite: p2
secteur: environnement
localisation: france
---

# naeco

## Relationnel
- **Association** : NAECO — "Mobiliser l'art et la science pour l'océan"
- **Activité** : expéditions à la voile, créations artistiques, sensibilisation ; documentation de la biodiversité marine (ex. expédition 2022 "The Pelagos Sanctuary", collaboration STARESO)

## Historique des échanges
-

## Décisions prises
-

## Besoins identifiés
- Site vitrine de l'association
- Carte interactive des expéditions/observations/données scientifiques (Pelagos, escales, sites d'étude)

## Devis / propositions
-

## Next actions
- [ ]

## Journal
- 2026-08-29 : Repos identifiés (`NAECOEXPEDITION/naeco-site`, `NAECOEXPEDITION/naeco-carte`), fiche client créée
- 2026-08-31 : Bug de race condition résolu sur [[naeco-carte]] (tracés d'expédition écrasés pendant l'édition), déployé. Détails dans la fiche projet et `03_knowledge/troubleshooting.md`.
- 2026-09-01 : Nouvelle page `/expeditions` livrée sur [[naeco-site]] (Point Zéro 2026 + les 4 expéditions précédentes), contenu extrait du Notion officiel de l'expédition. Détails dans la fiche projet.
- 2026-09-02 : Grosse journée [[naeco-site]] — refonte animée Phases 1 (Hero + Manifeste) et 2 (Constat Méditerranée, Carnet de bord, 3 Piliers, Équipe en cartes flip) implémentées et mergées sur `master` (pas encore déployées). Nouvelle spec reçue pour refondre la section « Notre Approche ». Détails complets dans la fiche projet.

## Liens
- Projets : [[naeco-site]], [[naeco-carte]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
