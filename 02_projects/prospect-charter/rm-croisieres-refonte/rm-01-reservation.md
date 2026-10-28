---
tags: [rm-croisieres, prospection]
created: 2026-10-28
projet: rm-croisieres-refonte
---

# rm-01-reservation

Projet : [[rm-croisieres-refonte]] · Client : [[rm-croisieres]] · Parent : [[prospect-charter]] · Source : repo `rm-croisieres-refonte`, `docs/etudes/2026-10-28-rm-croisieres-reservation.md` (copie dans `attachments/`) ; tunnels concurrents de Martinique : repo `prospection-charter`, `docs/etudes/2026-10-28-rm-croisieres-tunnels-concurrents.md`.

## L'essentiel
- **Les prix existent** : chaque fiche publie une grille à la semaine sur 5 saisons, plus la caution. Il manque le total, les frais, l'année des grilles et les disponibilités.
- **Le planning est déjà dans Booking Manager** (MMK, depuis mars 2023) : 12knots et BeBlue affichent les semaines libres et réservées de RM. Le site de RM n'en montre rien.
- **Semaines du samedi au samedi**, prix au prorata des nuits quand une semaine chevauche deux saisons (vérifié sur 11 prix de 12knots), **680 € de frais de fin de séjour** (260 administration + 300 ménage + 120 gaz et consommables ; 2 330 € pour Liberta).
- **Deux barèmes contradictoires** : site 30 / 30 / 40 % et annulation à 180 et 90 jours ; agences 50 %, solde et annulation totale à 45 jours. Skipper 250 €/jour sur le site, 280 € chez les agences.
- **Bateaux de propriétaires** : plusieurs sociétés domiciliées chez RM Services Nautiques et un GIE ; Liberta est aussi vendu par son propriétaire (Blue Ocean Sailing, SamBoat « Thierry »). RM vend sous « RM Croisieres », « Roberto » (SamBoat, Click&Boat) et en anonyme (BeBlue, Sailogy, GlobeSailor).
- **Marché au Marin** : seul Dream Yacht vend vraiment en ligne (dispos, total, 30 %). Onze loueurs locaux sur treize s'arrêtent à un formulaire. À Saint-Vincent, personne ne vend en ligne.

## Principe retenu pour la maquette
Calendrier « libre / complet » par bateau et par semaine (samedi-samedi), puis demande pré-remplie avec total et échéancier des CGV ; RM confirme, envoie le contrat et la demande d'acompte. Pas de réservation immédiate en phase 1 (ventes parallèles des propriétaires, barèmes non tranchés, aucun encaissement en ligne connu). Phase 2 : brancher le widget ou l'API de Booking Manager.

## Questions à poser à RM
1. Quel barème fait foi : site ou agences ?
2. Booking Manager est-il la source unique du planning, semaines propriétaires et SamBoat comprises ? API ou widget inclus dans l'abonnement ?
3. Part des réservations directes ; commissions versées aux agences.
4. Comment la carte est-elle encaissée aujourd'hui ?
5. Frais de fin de séjour : 680 € partout ?
6. Skipper et hôtesse : 250 / 200 € ou 280 / 220 € ?
7. Aller simple Le Marin ↔ Blue Lagoon possible ? Qui gère la clearance ?
8. Les propriétaires vendent-ils leurs semaines eux-mêmes ?
9. Départs le samedi seulement ? Quels bateaux partent de Blue Lagoon ?
10. Origine de la clientèle.
11. Flotte réelle : 21 fiches, 24 annoncés, 39 chez 12knots ?
