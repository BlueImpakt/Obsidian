---
tags: [rm-croisieres, prospection]
created: 2026-10-28
projet: rm-croisieres-refonte
---

# rm-03-note-relecture

Projet : [[rm-croisieres-refonte]] · Client : [[rm-croisieres]] · Source : repo `rm-croisieres-refonte`, `docs/note-relecture.md`


Maquette locale : lancer le serveur `rm-maquette` (`.claude/launch.json`, port 4178), puis http://localhost:4178/. Page pour le gérant : `concept.html`. Rien n'est déployé ni envoyé.

## L'idée
**« Choisissez la route, puis le bateau. »** Le premier écran trace, nuit par nuit, les itinéraires que RM publie déjà, un bouton par route à son nom complet (Tour de la Martinique, Grenadines depuis le Marin, Grenadines depuis Saint-Vincent), dans les couleurs de leurs propres cartes (marine #1E3D58, sable #C7936E), à côté de Liberta au mouillage. Bodoni Moda (écho au logo) et Albert Sans.

## Sourcé
- 22 bateaux, noms, modèles, cabines, passagers, longueurs, cautions, tarifs à la semaine par saison : fiches de rmcroisieres.com (`docs/faits.md`, chaque valeur avec son URL). La porte qualité vérifie 151 faits en FR et en EN.
- Itinéraires, conditions de location (paiement 30/30/40, annulation, météo), services et leurs prix : pages du site.
- Prix d'une semaine au prorata des nuits : 11 prix recalculés à l'euro près, identiques à ceux de RM chez 12knots.
- Photos : toutes du site, jamais agrandies.

## Supposé ou tiré d'ailleurs (marqué « à confirmer » ou « exemple »)
- Frais de fin de séjour 680 € (2 330 € pour Liberta), samedi comme jour de départ, semaines complètes de Manureva, Le Dumbea et Estella : 12knots, 28/10/2026.
- Année des deux grilles de tarifs (2026, 2027), skipper facturé 7 jours, rachat de franchise de 3 % avec skipper (minimum 260 €).
- Délai de réponse « sous 24 h », lien WhatsApp sur le mobile du site, demandes et messages automatiques de la vue bureau, lien de paiement, copie de chaque message à l'agence.
- **Choix « 1 semaine / 2 semaines » du tunnel : ni sourcé ni marqué.** Le site ne publie que des tarifs à la semaine et des idées de croisière de 8 et 10 jours (question plus bas).
- Détail complet : `docs/hypotheses.md`.

## Manque
- Photos HD : Dlokoko (259 px), An tu plezi (465 px, bandes noires rognées), Take It Easy (600 px), Pantagonia, Affligem et Rev'anou (697 px, même photo avec le filigrane d'un autre site), Le Gaspésien (768 px), Manureva et Lily (854 px, même rendu du chantier). Aucune retouche par IA : à toi de décider (Nano Banana) ou à demander à RM.
- Tes coordonnées : `PITCH_CONTACT` vide dans `maquette/concept.js`, `PITCH_LIEN_PAGE` dans les messages.
- Réponses de RM : barème qui fait foi (site 30/30/40 ou agences 50 % à J-45), Booking Manager comme planning unique, frais, tarifs skipper, bateaux de Blue Lagoon, départs le samedi, durées possibles (semaine seule, deux semaines, croisière de dix jours ?).
- Aucun email de gérant publié : le premier message part par le formulaire du site, contact@rmcroisieres.com ou le téléphone.

## Décisions prises à ta place (coût si elles sont fausses)
1. **Validation de la planche passée seul** (à ta demande) : idée de la route et hero Liberta. *Coût* : premier écran à refaire (le reste ne dépend pas de l'idée).
2. **Demande + calendrier, pas de paiement en ligne** : planning déjà dans Booking Manager, propriétaires qui vendent en parallèle, barèmes contradictoires. *Coût* : tunnel jugé timide si RM veut encaisser en ligne tout de suite.
3. **CGV du site comme référence** malgré les conditions publiées chez les agences. *Coût* : échéancier faux si les agences ont raison (question n° 1 au gérant).
4. **Frais de 680 € inclus dans le total**, repris de 12knots. *Coût* : total faux de quelques centaines d'euros.
5. **Contradictions du site laissées visibles** sur les fiches (« À confirmer avec RM ») : Manureva 46/42, La Gloria, Rev'anou, caution de Liberta, tarif de Sol. *Coût* : le gérant peut trouver ça intrusif ; c'est aussi la preuve qu'on a lu son site.

Toutes les décisions : `docs/decisions.md`.

## Mesures (porte qualité n° 12 du 28/10/2026)
- **Porte qualité : tout passe (9 contrôles sur 9).** Tests (21), débordement (216 vues), photos jamais agrandies (1 208 + 264 en galerie), états ouverts (120 parcours), console, faits (151 × 2 langues), tunnel (client sur téléphone : 8 gestes, 3 étapes ; agence : 14 gestes), système visuel.
- **Affichage sur téléphone en vrai bridage** (seuil 4 s) : accueil 2,6 s (4,4 avant cette passe), flotte 3,9 s (7,0), fiche 3,6 s (4,4). Gains : un dictionnaire de traduction par page au lieu de sept, logo à sa taille, version 900 px des grandes photos (qualité 95), données compactées, première photo de la flotte préchargée, polices chargées après la grande photo (repli Didot ou Bodoni 72 sur iPhone le temps du chargement). Mesures sur le serveur local, sans compression : en ligne, ce sera plus rapide. Accessibilité et bonnes pratiques Lighthouse : 100 partout.
- **Avant / après, accueil sur téléphone** : 7,9 Mo et 7,0 s d'affichage pour rmcroisieres.com, 579 Ko pour la maquette (13,6 fois plus légère).
- **Comparaison à l'aveugle** (juge neuf, Y.CO, The Moorings, Belmond) : 2e sur le premier écran et la fiche derrière Belmond, 1re sur le tunnel à 1 440 px (`docs/revues/aveugle-2.md`). L'écart tient surtout aux photos de RM.

## Revues
- **Après ta relecture du premier écran (28/10)** : boutons de route au nom complet, plus aucune mention de rmcroisieres.com comme source dans les pages (badges « exemple » et « à confirmer » seuls), nombre d'avis masqué sous 50, accroches reprises (« Vingt-deux bateaux, une expérience hors du temps », « Arriver plus tôt, repartir plus tard », « Ils ont navigué avec RM »…), compliment du J0 réécrit.
- **Finish-Gate (HOLD, rendu après la première note) corrigé** : carte d'An tu plezi vide, premier acompte sous le bouton d'envoi sur téléphone, parcours agence sans copie à l'agence.
Textes, code, animations, accessibilité, personas, impeccable, règles Vercel, comparaison à l'aveugle (Y.CO, The Moorings, Belmond), Finish-Gate : `docs/revues/`. Une passe de corrections a suivi, puis une reprise du premier écran et de la fiche après chaque comparaison à l'aveugle, puis les bloquants du Finish-Gate (fourchette de prix de l'accueil, fiches à petite photo). Restent à ta décision : les photos (doublons, filigrane, petites sources) et le lien entre la route et les bateaux (on ignore quels bateaux partent de Saint-Vincent).

## Dossier d'envoi
`sortie/envoi/` (hors git) et la note [[rm-02-dossier-envoi]] du vault : vidéo de 57 s (verticale et paysage, sous-titres), couverture, avant/après (accueil et fiche Manureva), page privée, brouillons J0, J+3 (WhatsApp sur le mobile du site), J+8, J+15. Rien n'est envoyé. Aucun email de gérant publié : canal à choisir (formulaire, contact@rmcroisieres.com, téléphone).

## Contrôle sur ton iPhone (5 minutes)
Safari, en portrait puis en paysage :
1. Accueil : changer de route, faire défiler les escales.
2. Une fiche (Liberta) : ouvrir la galerie, parcourir toutes les photos, fermer.
3. « Choisir ma semaine » : choisir une semaine, puis « Demander Liberta pour cette semaine ».
4. Étapes 2 et 3 jusqu'à l'écran de fin (données fictives).
5. VoiceOver sur l'accueil et sur la demande : la route, le choix de la semaine, les erreurs.
