---
tags: [project, encours, rm-croisieres]
created: 2026-10-28
statut: encours
client: rm-croisieres
parent: prospect-charter
body_synced: 2026-10-28
---

# rm-croisieres-refonte

## Objectifs du projet
- Proposer à RM Croisières (Le Marin et Saint-Vincent, 22 bateaux à la semaine) une refonte de rmcroisieres.com autour de ses vrais prix, de ses itinéraires et de son planning Booking Manager, avec une demande de réservation complète qui garde RM maître de la confirmation.

## Livrables
- [[rm-01-reservation]] : organisation réelle de la réservation, Booking Manager, barèmes, questions à poser — **à lire en premier**
- **Maquette cliquable** : `C:\Users\LENOVO\Documents\GitHub\rm-croisieres-refonte\maquette\` (git local, sans remote ; serveur local port 4178, `.claude/launch.json`). Idée : « Choisissez la route, puis le bateau » (itinéraires de RM nuit par nuit au premier écran). Accueil, flotte, 22 fiches, demande en 3 étapes (semaines du samedi, prorata des nuits identique à 12knots, frais, échéancier des CGV, mode agence), vue bureau, page concept. FR + EN.
- Docs du repo : `DESIGN.md`, `docs/decisions.md` (décisions prises seul, avec leur coût si fausses), `docs/hypotheses.md`, `docs/faits.md`, `docs/photos.md`, revues `docs/revues/`.
- [[rm-03-note-relecture]] : note de relecture (sourcé, supposé, manquant, décisions et leur coût, mesures, contrôle iPhone) ; `attachments/` : DESIGN.md, decisions.md, hypotheses.md, étude de réservation
- [[rm-02-dossier-envoi]] — dossier d'envoi : vidéo, avant/après, chiffres, page privée, messages J0 à J+15 (brouillons)

## État actuel
- 2026-10-28 (soir) : maquette refaite après les retours de Melvin : hero plein écran (catamaran sur banc de sable, zoom lent), pages Croisières et Qui sommes-nous, en-tête et prix regroupés, prix des fiches françaises, équipement de 5 bateaux, demande WhatsApp. Porte au vert (n° 26, puis contrôles ciblés) ; Lighthouse à remesurer machine libre. Dossier d'envoi régénéré. Lire [[rm-03-note-relecture]].
- 2026-10-28 (suite) : audit de couverture du site (`docs/revues/couverture-site.md`) puis ajouts : prix FR vérifiés, équipement, jeux aquatiques, pages Croisières et Qui sommes-nous, WhatsApp prérempli ; porte complète finale sur 8 pages et dossier d'envoi à refaire une fois les modifications terminées.
- 2026-10-28 (midi) : hero en photo HD fournie par Melvin, plein écran, titre « Choisissez votre cap et votre bateau » ; accueil : hero → visites 3D → Lagoon 43 → flotte (Liberta, Manureva, Yurelle, Sea Naaps, Bieckert, Madelon) ; dernière porte PASS sur a77f3cd, passe « première lecture » non encore commitée ; dossier d'envoi et vidéo à refaire quand Melvin aura fini ses retours.

## Décisions techniques
- Demande + calendrier, pas de paiement en ligne en phase 1 ; phase 2 : widget ou API Booking Manager.
- Grilles des fiches lues 2026 / 2027 (confirmé par 12knots) ; prorata des nuits ; frais de 680 € et samedis repris de 12knots, marqués « à confirmer ».
- Photos du site uniquement, jamais agrandies ; aucune retouche IA (petites photos signalées : Dlokoko 259 px, An tu plezi 465 px, Take It Easy 600 px, Pantagonia / Affligem / Rev'anou 697 px avec filigrane d'un autre site).
- Bouton principal « Réserver » (FR) / « Request » (EN), RM confirme ensuite ; demande WhatsApp préremplie marquée « exemple » (risque : hors planning si RM ne gère pas WhatsApp) ; prix FR retenus sauf écarts justifiés, affichés « à confirmer ».
- Hero : photo HD fournie par Melvin avec dézoom de ×1,5 à ×1,8 sur 10 s (légère perte de netteté au début du mouvement acceptée, jamais agrandie au repos) ; numéro « Appelez le bureau » en bas à droite de la photo, sans fond.

## Blocages / risques
- Barèmes contradictoires site / agences : l'échéancier affiché suit le site.
- Semaines complètes relevées le 28/10 : périment vite.
- Aucun email de gérant ; `PITCH_CONTACT` vide dans `maquette/concept.js`.
- Le site ne fixe ni durée minimale ni prix d'un jour supplémentaire ; rachat de franchise contradictoire (260 € FR, 160 € EN) : questions pour le gérant.

## Next actions
- [ ] Relire la maquette sur iPhone (Safari, portrait et paysage, VoiceOver sur l'accueil et la demande)
- [ ] Remplir `PITCH_CONTACT` (maquette/concept.js) et `PITCH_LIEN_PAGE` dans les messages
- [ ] Décider des photos à refaire (Nano Banana) ou à demander en HD
- [ ] Choisir le canal du premier contact (téléphone, formulaire, contact@)

## Journal
- 2026-10-28 (soir) : série de retours de Melvin appliqués (hero, pages, en-tête, cartes, textes, WhatsApp, durée, franchise), audit de couverture du site, skill maquette-prospect enrichi, proposition de session pour faire évoluer Sabina.
- 2026-10-28 : choix de durée « 1 semaine / du … au … » (5 nuits min.) sur la fiche et le tunnel, « N au plus sur ce bateau » retiré, franchise skipper 160 € min. ; porte n° 14 à 16 au vert.
- 2026-10-28 : passe de vitesse mobile (dictionnaires par page, logo, photos 900 px, polices après la photo, préchargement flotte), Finish-Gate HOLD corrigé (carte An tu plezi, acompte avant coordonnées, copie à l'agence), retours de Melvin sur les textes et les sources, porte n° 12 PASS, dossier d'envoi régénéré.
- 2026-10-28 : revues (textes, code, accessibilité, personas, impeccable, Vercel, Finish-Gate, deux aveugles), passes de corrections, porte qualité n° 6, dossier d'envoi généré (vidéo 57 s, J0 à J+15) ; skill maquette-prospect mis à jour.
- 2026-10-28 : relevé du site, étude de réservation (Booking Manager, 12knots, barèmes), tunnels concurrents de Martinique, références premium (Y.CO, Moorings, Belmond) ; maquette construite, revues (textes, code, accessibilité, personas) et passe de corrections.
- 2026-10-28 : prix corrigés d'après les fiches FR (écarts vérifiés un par un), bloc « À bord » sur 5 fiches, bouton « Réserver » (110ec3b), demande WhatsApp préremplie (exemple), pages Croisières et Qui sommes-nous ajoutées, hero réduit aux Grenadines depuis Saint-Vincent, légende du récif corrigée (a874a95), prix des options regroupés dans « Prix et conditions ».
- 2026-10-28 : hero refait sur la photo HD de Melvin (dézoom ×1,5-1,8, titre « Choisissez votre cap et votre bateau », boutons croisières / flotte, numéro du bureau en bas à droite), sections Lagoon 43 et visites 3D ajoutées, flotte de l'accueil revue (Yurelle, Sea Naaps) ; porte PASS 9/9 (a77f3cd, accueil 2,3 s mobile), puis passe « première lecture » (hero plein écran, visites 3D en 2e) en attente du verdict de la porte.

## Liens
- Projet parent : [[prospect-charter]]
- Client : [[rm-croisieres]]
- Patterns utilisés : [[stack-creation-site-web]]
- Repo : `C:\Users\LENOVO\Documents\GitHub\rm-croisieres-refonte` (local) — site actuel : rmcroisieres.com
