---
tags: [rm-croisieres, prospection]
created: 2026-10-28
projet: rm-croisieres-refonte
---

# rm-03-note-relecture

Projet : [[rm-croisieres-refonte]] · Client : [[rm-croisieres]] · Source : repo `rm-croisieres-refonte`, `docs/note-relecture.md`


Maquette locale : lancer le serveur `rm-maquette` (`.claude/launch.json`, port 4178), puis http://localhost:4178/. Page pour le gérant : `concept.html`. Rien n'est déployé ni envoyé.

## L'idée
**« Choisissez votre cap et votre bateau. »** Le premier écran est la photo plein cadre d'un catamaran au bord d'un banc de sable (version HD que tu as fournie d'une image du diaporama de RM), avec un zoom lent de 10 s. Le titre est posé dessus. À droite, une carte translucide déroule nuit par nuit « 8 jours, Les Grenadines depuis Saint-Vincent », la route que RM publie déjà. Palette tirée des cartes de RM (marine #1E3D58, sable #C7936E), Bodoni Moda (écho au logo) et Albert Sans.

## Pages
- **Accueil** : hero, visites 3D des quatre bateaux (liens Matterport du site), nouveauté Lagoon 43, la flotte (vraies photos de RM en première rangée), prix et conditions (tableau des options), propriétaires.
- **Croisières** : les quatre idées de croisière nuit par nuit (dont le Sud de la Martinique) et les deux bases.
- **Qui sommes-nous** : l'équipe au ponton, l'arrivée racontée (lits faits, clim allumée, courses livrées), sécurité, propriétaires.
- **La flotte, 22 fiches, la demande en 3 étapes, la vue bureau, la page concept.** En-tête : La flotte, Croisières, Prix et conditions, Qui sommes-nous, avec l'accroche du site « Location de bateaux Martinique ».

## Sourcé
- 22 bateaux, noms, modèles, cabines, passagers, longueurs, cautions, tarifs par saison : fiches de rmcroisieres.com (`docs/faits.md`). Fiches françaises et anglaises comparées une par une : grille 2026 de Dlokoko, Sol et Madelon 2027 repris de la française. La porte vérifie 152 faits en FR et en EN.
- Itinéraires, conditions de location (paiement, annulation, météo, 21 ans, ni nuit ni solitaire, retard), services et leurs prix, jeux aquatiques, ravitaillement, inclus et sécurité : pages du site.
- Équipement détaillé de Manureva, Estella, Take It Easy, Liberta et Madelon : leurs anciennes pages encore en ligne (2023), marqué « à confirmer ».
- Prix d'une semaine au prorata des nuits : 11 prix identiques à ceux de RM chez 12knots.

## Supposé ou tiré d'ailleurs (« à confirmer » ou « exemple »)
- Frais de fin de séjour 680 € (2 330 € pour Liberta), départ le samedi, semaines complètes : 12knots, 28/10/2026.
- Durée « 1 semaine » ou « du … au … », 5 nuits au moins (ton choix), prix au prorata des nuits.
- Rachat de franchise avec skipper : 3 %, minimum 160 € (le site dit aussi 260 € et une caution ramenée à 1 000 €).
- Délai de réponse « sous 24 h », WhatsApp (demande pré-rédigée vers le mobile du site), vue bureau et messages automatiques, copie à l'agence.
- Détail : `docs/hypotheses.md`.

## Manque
- Photos HD : Dlokoko (259 px), An tu plezi (465 px), Take It Easy (600 px), Pantagonia, Affligem et Rev'anou (697 px, filigrane d'un autre site), Le Gaspésien (768 px), Manureva et Lily (854 px, rendu du chantier). Lagoon 43, Yurelle, Manureva : images de synthèse du chantier. **Hero : un original plus grand que 2 000 px** (au moins 3 000) rendrait le zoom marqué sur un écran de 1 920 px (×1,06 aujourd'hui).
- Photo « récif en cœur » du chapitre Grenadines depuis le Marin : un monocoque, lieu non confirmé (côte de type méditerranéen).
- Tes coordonnées : `PITCH_CONTACT` vide dans `maquette/concept.js`, `PITCH_LIEN_PAGE` dans les messages.
- Réponses de RM : barème qui fait foi (site 30/30/40 ou agences 50 % à J-45), Booking Manager comme planning unique, durées possibles et minimum, prix d'un jour en plus, minimum du rachat de franchise, bateaux de Blue Lagoon, WhatsApp.
- Aucun email de gérant publié : premier message par le formulaire, contact@rmcroisieres.com, le téléphone, ou WhatsApp (brouillon dans `docs/envoi-whatsapp.md`).

## Décisions prises à ta place (coût si elles sont fausses)
1. **Demande + calendrier, pas de paiement en ligne** : planning déjà dans Booking Manager, propriétaires qui vendent en parallèle. *Coût* : tunnel jugé timide si RM veut encaisser tout de suite.
2. **CGV du site comme référence** malgré les conditions des agences. *Coût* : échéancier faux si les agences ont raison (question n° 1 au gérant).
3. **Frais de 680 € inclus dans le total** (12knots). *Coût* : total faux de quelques centaines d'euros.
4. **Fiche française d'abord quand les deux langues diffèrent**, sauf confirmation tierce (Manureva 11 600 € pour les fêtes, comme chez 12knots). *Coût* : 100 à 900 € d'écart sur une semaine si RM tient l'autre version.
5. **Zoom borné à la taille du fichier** : aucune photo agrandie, même pendant le mouvement. *Coût* : zoom discret sur grand écran tant que l'original n'est pas plus grand.

Toutes les décisions : `docs/decisions.md`.

## Mesures
- **Porte qualité n° 26** (dernière passe complète sur machine libre) : 9 contrôles, tout au vert sauf l'agrandissement passager du dézoom, corrigé depuis (portes 27 à 31 au vert sur les photos). Tests (23), débordement (232 vues), photos jamais agrandies (1 336 + 264 en galerie), états ouverts (128 parcours), console, faits (152 × 2 langues), tunnel (client sur téléphone : 8 gestes, 3 étapes ; agence : 14 gestes), système visuel.
- **Lighthouse** : vert dans la porte n° 26 (téléphone en vrai bridage sous 4 s). Les relances du soir (portes 32 à 36) sont « incertaines » : machine chargée par d'autres sessions (indice 508 à 530 pour un minimum de 1 000). **À remesurer machine libre** : `py -I porte_qualite.py gate.json --seulement lighthouse`.
- **Avant / après, accueil sur téléphone** : 7,9 Mo et 7,0 s d'affichage pour rmcroisieres.com, environ 590 Ko pour la maquette.
- **Comparaison à l'aveugle** (Y.CO, The Moorings, Belmond), faite avant la refonte du hero : 2e derrière Belmond sur le premier écran et la fiche, 1re sur le tunnel (`docs/revues/aveugle-2.md`). À refaire avec le nouveau hero.

## Revues
Textes, code, animations, accessibilité, personas, impeccable, règles Vercel, Finish-Gate, deux comparaisons à l'aveugle, audit de couverture du site (`docs/revues/couverture-site.md`). Puis tes retours du 28/10 : sources retirées des pages, avis sous 50 masqués, accroches, durée, prix des fiches françaises, deux pages, en-tête, hero plein écran, cartes, WhatsApp, numéro du bureau en signature.

## Dossier d'envoi
`sortie/envoi-final-2/` (hors git) et la note [[rm-02-dossier-envoi]] du vault : vidéo (verticale et paysage, sous-titres), couverture, avant/après, page privée, brouillons J0 à J+15. Rien n'est envoyé.

## Contrôle sur ton iPhone (5 minutes)
Safari, en portrait puis en paysage :
1. Accueil : le zoom, le titre sur la photo, faire défiler les escales, ouvrir une visite 3D.
2. Une fiche (Liberta) : ouvrir la galerie, parcourir toutes les photos, fermer ; le bloc « À bord ».
3. « Votre semaine » : une semaine, puis « Du … au … » ; « Envoyer cette demande sur WhatsApp ».
4. La demande jusqu'à l'écran de fin (données fictives), avec un jeu aquatique.
5. VoiceOver sur l'accueil et sur la demande.
