---
tags: [project, encours, prospection]
created: 2026-10-25
statut: encours
client: aucun
body_synced: 2026-10-27
---

# prospect-charter

## Objectifs du projet
- Prospecter les loueurs de bateaux et opérateurs d'excursions (Caraïbes d'abord) avec un agent qui découvre, audite et classe les sites, puis transformer les meilleurs prospects en refontes / automatisations Blue Impakt.
- Réutiliser le boilerplate « opérateur nautique » né de [[sabinas-watersport-refonte]] sur chaque prospect.

## Sous-projets
- [[sabinas-watersport-refonte]] — Sabinas Watersport Rhodos (Rhodes, Grèce) : premier dossier complet, maquette v1, base du boilerplate et repère de calibrage (douleur ≈ 8).
- [[jicky-marine-refonte]] — Jicky Marine (Saint-Barthélemy) : n°1 du top 50, étude paiement / réservation faite le 2026-10-25.
- [[rm-croisieres-refonte]] — RM Croisières (Le Marin, Martinique, et Saint-Vincent) : maquette de refonte construite en autonomie le 2026-10-28 (route nuit par nuit, calendrier Booking Manager, demande avec total).

## Livrables
- Agent : skill `/prospect-charter` + sous-agent `site-auditor`, scripts Python (découverte Apify Google Maps, filtrage, fusion, top 50).
- Résultats au 2026-10-25 : 126 prospects retenus (34 refontes, 76 améliorations, 16 créations), 115 écartés ; `resultats/top50-prioritaires.csv` classé par score de priorité.
- Zones : Martinique, Saint-Martin, Saint-Barthélemy terminées ; BVI, Antigua, Sint Maarten en cours ; Guadeloupe et 17 autres à faire.
- Outils communs maquettes : `C:\Users\LENOVO\Documents\GitHub\maquette-outils` (extraction, photos, porte-qualite, envoi), chacun avec README et tests ; prompt de lancement dans le skill `maquette-prospect`.

## État actuel
- 2026-10-25 : prospect n°1 (Jicky Marine) étudié en détail ; l'offre type « réservation et paiement en ligne » est à adapter au cas par cas (moyens de paiement déjà en place, territoire, organisation du bureau).
- 2026-10-27 : top 50 requalifié avec budget (registre français : fort +6, moyen +3, faible −15) et agence (−10 ; 35 sites signés par une agence sur les 126 prospects) — Taxi Cap (budget faible + agence Pixell), RM Croisières et 7 prospects avec agence sortis ; poids modifiables dans `scripts/top50.py`, méthode dans `resultats/top50-methode.md` (cf720ee).

## Décisions techniques
- Deux notes par prospect : note de tri (le site est-il à refaire ?) et douleur (ce que la présence web coûte à l'entreprise) ; top 50 par score de priorité (douleur, gamme, moyens, closing, ticket).
- **Stripe ne prend pas les entreprises de Saint-Barthélemy** (ni Polynésie, Nouvelle-Calédonie, Wallis-et-Futuna, Saint-Pierre-et-Miquelon) ; Martinique, Guadeloupe et Saint-Martin oui. Sint Maarten (partie néerlandaise) non plus. À vérifier pour chaque prospect avant de proposer un paiement en ligne.
- Passage à l'échelle (27/10) : on réutilise la méthode (`maquette-prospect`), les leçons CRO et les garde-fous, jamais le design ; direction visuelle, parcours de réservation et argumentaire sont conçus pour chaque client.
- Process maquette (27/10) : deux validations de Melvin seulement (planche codée avant de coder la suite, puis maquette finie avec note de relecture et dossier d'envoi, porte qualité au vert) ; entre les deux la session décide seule et note chaque décision ; l'outil d'envoi ne produit que des brouillons, Melvin envoie ; aucun pixel ni lien traçant (CNIL) ; un sous-projet vault par maquette.
- Porte qualité : photo « agrandie » jugée en pixels CSS pour PASS/FAIL ; photos sous la résolution iPhone listées « à demander en HD » sans bloquer.

## Blocages / risques
- L'audit lit le HTML sans JavaScript : widgets de réservation parfois ratés (CaptainJo, Nautitan corrigés le 2026-10-24) ; les moyens de paiement réels sont souvent dans les CGV, pas sur la page d'accueil.

## Next actions
- [ ] Préparer le premier contact avec Jicky Marine (voir [[jicky-marine-refonte]])
- [ ] Corriger le libellé « ticket élevé (semaine / plusieurs jours) » du top 50 pour Jicky Marine (location à la sortie, pas à la semaine)

## Journal
- 2026-10-25 : Projet parent créé ; Sabinas et Jicky Marine rangés en sous-projets.
- 2026-10-27 : Taxi Cap (3e du top 50) : CA 2021 102 k€ avec perte, site déjà fait par l'agence Pixell ; crible du top 50 : 31 prospects sans agence identifiée, 19 avec agence/prestataire.
- 2026-10-27 : Top 50 requalifié avec budget (registre : +6/+3/−15) et agence (−10, 35 sites signés sur 126) : Taxi Cap, RM Croisières et 7 prospects avec agence sortent, Star Voyage, Location Catamaran Martinique, Calypso, Kokoumdo montent (cf720ee, poussé).
- 2026-10-27 : Décision : passer à l'échelle sur d'autres refontes en réutilisant la méthode et les leçons Jicky/Sabina, avec un design, un parcours et un argumentaire propres à chaque client ; pistes retenues pour soigner la 1re maquette : dossier de faits sourcés vérifié par test et planche photos/direction à valider avant de coder.
- 2026-10-27 : Outillage maquettes à la chaîne livré dans `maquette-outils` (extraction du site prospect, harmonisation photos, dossier d'envoi vidéo/avant-après/brouillons, porte qualité PASS/FAIL avec tunnel et comparaison à l'aveugle ; 236 tests) et intégré au skill `maquette-prospect` avec un prompt de lancement ; process fixé à 2 validations de Melvin (planche, maquette finie), envois faits par Melvin, un sous-projet vault par maquette.
- 2026-10-27 : Maquette RM Croisières lancée avec le nouveau process (extraction en cours ; incohérence « Manureva » Lagoon 46 vs Lagoon 42 relevée).

## Liens
- Client : aucun (projet de prospection)
- Patterns utilisés : [[stack-creation-site-web]]
- Repo / deployment : github.com/BlueImpakt/prospect-charter (privé) — local `C:\Users\LENOVO\Documents\GitHub\prospection-charter`
