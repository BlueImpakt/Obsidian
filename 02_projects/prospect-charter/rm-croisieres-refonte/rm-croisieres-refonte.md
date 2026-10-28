---
tags: [project, encours, rm-croisieres]
created: 2026-10-28
statut: encours
client: rm-croisieres
parent: prospect-charter
---

# rm-croisieres-refonte

## Objectifs du projet
- Proposer à RM Croisières (Le Marin et Saint-Vincent, 22 bateaux à la semaine) une refonte de rmcroisieres.com autour de ses vrais prix, de ses itinéraires et de son planning Booking Manager, avec une demande de réservation complète qui garde RM maître de la confirmation.

## Livrables
- [[rm-01-reservation]] : organisation réelle de la réservation, Booking Manager, barèmes, questions à poser — **à lire en premier**
- **Maquette cliquable** : `C:\Users\LENOVO\Documents\GitHub\rm-croisieres-refonte\maquette\` (git local, sans remote ; serveur local port 4178, `.claude/launch.json`). Idée : « Choisissez la route, puis le bateau » (itinéraires de RM nuit par nuit au premier écran). Accueil, flotte, 22 fiches, demande en 3 étapes (semaines du samedi, prorata des nuits identique à 12knots, frais, échéancier des CGV, mode agence), vue bureau, page concept. FR + EN.
- Docs du repo : `DESIGN.md`, `docs/decisions.md` (décisions prises seul, avec leur coût si fausses), `docs/hypotheses.md`, `docs/faits.md`, `docs/photos.md`, revues `docs/revues/`.

## État actuel
- 2026-10-28 : maquette construite en autonomie (validation 1 déléguée par Melvin), revues passées, passe de corrections faite ; porte qualité complète et dossier d'envoi en cours.

## Décisions techniques
- Demande + calendrier, pas de paiement en ligne en phase 1 ; phase 2 : widget ou API Booking Manager.
- Grilles des fiches lues 2026 / 2027 (confirmé par 12knots) ; prorata des nuits ; frais de 680 € et samedis repris de 12knots, marqués « à confirmer ».
- Photos du site uniquement, jamais agrandies ; aucune retouche IA (petites photos signalées : Dlokoko 259 px, An tu plezi 465 px, Take It Easy 600 px, Pantagonia / Affligem / Rev'anou 697 px avec filigrane d'un autre site).

## Blocages / risques
- Barèmes contradictoires site / agences : l'échéancier affiché suit le site.
- Semaines complètes relevées le 28/10 : périment vite.
- Aucun email de gérant ; `PITCH_CONTACT` vide dans `maquette/concept.js`.

## Next actions
- [ ] Relire la maquette sur iPhone (Safari, portrait et paysage, VoiceOver sur l'accueil et la demande)
- [ ] Remplir `PITCH_CONTACT` (maquette/concept.js) et `PITCH_LIEN_PAGE` dans les messages
- [ ] Décider des photos à refaire (Nano Banana) ou à demander en HD
- [ ] Choisir le canal du premier contact (téléphone, formulaire, contact@)

## Journal
- 2026-10-28 : relevé du site, étude de réservation (Booking Manager, 12knots, barèmes), tunnels concurrents de Martinique, références premium (Y.CO, Moorings, Belmond) ; maquette construite, revues (textes, code, accessibilité, personas) et passe de corrections.

## Liens
- Projet parent : [[prospect-charter]]
- Client : [[rm-croisieres]]
- Patterns utilisés : [[stack-creation-site-web]]
- Repo : `C:\Users\LENOVO\Documents\GitHub\rm-croisieres-refonte` (local) — site actuel : rmcroisieres.com
