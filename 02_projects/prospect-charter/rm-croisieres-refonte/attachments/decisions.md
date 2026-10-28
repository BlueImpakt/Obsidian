# Décisions prises sans Melvin (28/10/2026)

Melvin a délégué la validation de la planche (« pour celui-ci, passe tout seul la validation 1 ; travaille en autonomie »). Chaque ligne : décision, raison, **coût si elle est fausse**.

## Idée et design

- **Idée : « Une semaine RM se choisit par sa route. »** Le premier écran montre, nuit par nuit, les itinéraires que RM publie déjà (Tour de la Martinique, Grenadines depuis le Marin, Grenadines depuis Saint-Vincent), à côté d'une photo de leur flotte. Raison : deux bases aux deux bouts du parcours, itinéraires et cartes déjà produits par RM ; Punch Croisières (même port) occupe le registre « carnet de voyage illustré », pas celui-ci. *Coût si faux* : premier écran à refaire (hero seul, le reste ne dépend pas de l'idée).
- **Palette tirée des cartes de RM** (mer #1E3D58, îles #C7936E) et **Bodoni Moda + Albert Sans** (Didone en écho au logo). *Coût* : jetons à changer dans `maquette/tokens.css`, une heure.
- **Hero : Liberta (Sunreef 50) au mouillage**, 4 048 px, page « Liberta » du site. Autres candidates : Take It Easy en route (6 912 px), marina de Blue Lagoon (4 288 px), rocher du Diamant (4 032 px). *Coût* : une ligne dans `research/process_photos.py`.
- **FR par défaut, EN au bouton de l'en-tête** : gérants et clientèle francophones, site actuel en EN/FR. Textes EN traduits par nous (l'anglais du site actuel est une traduction automatique). *Coût* : aucune relecture native de l'anglais.

## Faits et prix

- **Seconde grille de tarifs lue comme 2027.** Le site publie deux grilles sans année ; les prix de RM chez 12knots le confirment (Manureva 9 900 € du 09/01 au 15/05/2027). *Coût si faux* : prix de 2027 décalés d'un an sur les fiches.
- **Prix d'une semaine au prorata des nuits**, bornes de période incluses : 11 prix recalculés à l'euro près, identiques à ceux de RM chez 12knots (`tests/prix.test.mjs`). *Coût* : aucun tant que RM garde cette règle.
- **Frais de fin de séjour de 680 €** (administration 260, ménage 300, gaz et consommables 120) ajoutés au total, **2 330 € pour Liberta**, relevés chez 12knots ; le site dit seulement « forfait nettoyage obligatoire, selon la taille ». Marqués « à confirmer ». *Coût* : total faux de quelques centaines d'euros.
- **Semaines du samedi au samedi** (grille de RM chez 12knots), avec « Partir un autre jour » en repli. Marqué « à confirmer ». *Coût* : sélecteur à adapter si les départs sont libres.
- **Semaines complètes affichées** pour Manureva, Le Dumbea et Estella, d'après 12knots le 28/10/2026 (flux Booking Manager). Elles vieillissent dès le lendemain. *Coût* : une semaine affichée complète qui ne l'est plus ; à dire au gérant comme « exemple de ce que montrerait le planning branché ».
- **CGV du site comme référence** (30/30/40, annulation à 180 et 90 jours) malgré les conditions publiées chez les agences (50 %, J-45). *Coût* : échéancier faux si les agences ont raison ; question n° 1 au gérant.
- **Skipper 250 €/jour, hôtesse 200 €/jour** (site), comptés 7 jours par semaine (à confirmer) ; 280 et 220 € chez les agences. *Coût* : total faux de 210 à 420 € par semaine.
- **22 bateaux** (fiches du site), pas 24 (accueil) ni 39 (12knots). *Coût* : flotte incomplète si des bateaux n'ont pas de fiche.
- **Liberta** : nom pris de la visite 3D et de l'ancienne page (la fiche dit « SUNREEF 50 – 2020 »), caution affichée 2 000 € (fiche) malgré 7 000 / 10 000 € ailleurs. *Coût* : caution sous-estimée affichée au client.
- **Manureva affiché Lagoon 46** (titre et longueur 13,99 m) malgré l'adresse « lagoon-42 » ; **La Gloria affiché Lagoon 42** (titre) malgré l'adresse « lagoon-46 » ; doutes visibles sur la fiche (« À confirmer avec RM »). *Coût* : modèle faux sur une fiche.
- **« CB » lu comme cabines** (12 passagers pour 6 CB sur les Lagoon 42 : cohérent). *Coût* : nombre de cabines faux sur les cartes.

## Tunnel

- **Demande, pas de réservation immédiate** : RM vend aussi via Booking Manager et des agences, des propriétaires vendent leurs semaines (Liberta), aucun outil d'encaissement en ligne connu. Recommandation de l'étude : calendrier + demande. *Coût* : tunnel jugé timide si RM voulait payer en ligne tout de suite.
- **Délai de réponse « sous 24 h, du lundi au samedi »**, marqué « exemple » (aucun délai publié ; horaires réels 9 h-17 h du lundi au samedi). *Coût* : promesse à ajuster.
- **WhatsApp sur le mobile du site (+596 696 72 25 44)**, marqué « exemple » : aucun WhatsApp publié. *Coût* : lien vers un numéro qui n'utilise peut-être pas WhatsApp.
- **Mode agence** dans l'étape 3 (case « Je réserve pour un client »), lien de paiement au titulaire de la carte. *Coût* : aucun si RM ne travaille pas avec des conciergeries ; le parcours reste discret.
- **Expérience du chef de bord demandée** en coque nue (CGV art. 7 : fiche d'expérience, skipper imposable). *Coût* : un champ de plus à l'étape 2.

## Photos

- **Photo principale = celle que le site met en avant** pour chaque bateau (carte de la flotte), sauf Liberta : vue au mouillage 4 048 px de la page Liberta au lieu de la photo de la fiche (2 048 px), même bateau. *Coût* : une photo de carte différente de celle du site actuel.
- **Petites photos montrées à leur taille** : Dlokoko (259 px) dans un cadre réduit ; An tu plezi rognée de ses bandes noires d'export (465 px) ; fiches à photo de moins de 790 px en mosaïque « taille réelle ». Aucune photo refaite par IA : c'est à Melvin de décider (Nano Banana) ou à RM de fournir des originaux. *Coût* : cartes moins pleines pour Dlokoko et An tu plezi.
- **Galeries rattachées par page d'origine** : Liberta (page Liberta + vignette 3D), Take It Easy (page Take It Easy + photo « TAKE IT EASY » sur la coque), Manureva (page Manureva), Le Dumbea (bandeau « Lagoon 43 » de l'accueil), Madelon (page Oceanis 40.1), Le Gaspésien et Ola 2 (vignettes des visites 3D). *Coût* : une photo attribuée au mauvais bateau d'un même modèle (Lagoon 43 : Le Dumbea ou Kayo).
- **Pas d'harmonisation** : le diagnostic ne signale aucune dominante à corriger ; seuls les profils couleur (Display P3, Adobe RGB) sont convertis en sRGB.

## Après les revues (28/10/2026)

- **Deux comparaisons à l'aveugle** (Y.CO, The Moorings, Belmond) : la maquette passe de 3e à 2e sur le premier écran et la fiche, 1re sur le tunnel à 1 440 px. Belmond (hôtellerie de luxe, film et photographie professionnels) reste devant sur le premier écran et la fiche. Ruling : montrer quand même, la différence tenant surtout aux photos de RM (sources moyennes, parfois de chantier), qu'on ne retouche pas sans toi. *Coût* : un premier écran moins « maison » que Belmond tant que les photos ne sont pas refaites.
- **La route ne filtre pas les bateaux** : on ne sait pas quels bateaux partent de Blue Lagoon ; filtrer serait inventer. *Coût* : le choix d'itinéraire reste une vitrine, sans effet sur la flotte (Finish-Gate, majeur).
- **Photos partagées et filigrane laissés tels quels** (Sol / Estella, Pantagonia / Affligem / Rev'anou, Manureva / Lily, Le Dumbea / Kayo) : à toi de décider (Nano Banana ou photos de RM). *Coût* : cartes voisines identiques dans la flotte.
- **Semaines : huit à la fois à partir du mois choisi**, en grille (fin du rail horizontal coupé, jugé « coupé au bord » à l'aveugle). *Coût* : un geste de plus pour un départ lointain (choisir le mois).
- **Fourchette « de … à … la semaine »** sur la fiche au lieu de « dès … » : la première semaine affichée n'est pas la moins chère. *Coût* : aucun.
- **Rachat de franchise de 3 % ajouté au total avec skipper** (« obligatoire si vous embauchez un skipper », page Formalités), minimum de 160 € (« 3 % de la location, 160 Euros minimum », pages Qui sommes-nous et Formalités en anglais ; la page Formalités en français dit « d'un minimum de 260 Euro » : contradiction, d'abord appliquée à 260 €, corrigée le 28/10). *Coût* : 100 € d'écart sur les petits bateaux si c'est 260 € qui fait foi si le minimum ne s'applique pas.

## Passe de vitesse et retours de Melvin (28/10/2026, après la note de relecture)

- **Polices chargées après la grande photo** (événement `load`) : sur téléphone lent, la photo garde la bande passante ; en attendant, les titres s'affichent en Didot ou Bodoni 72 (iPhone), Georgia ailleurs. *Coût* : un changement de police visible une fraction de seconde sur réseau lent.
- **Version 900 px des grandes photos** (qualité 95), en plus de 1 200 et 2 400 px : choisie par les téléphones Android et le profil mobile de Lighthouse ; les iPhone (DPR 3) gardent 1 200 px. Aucune photo agrandie. *Coût* : 62 fichiers de plus.
- **Un dictionnaire de traduction par page, logo à sa taille, données compactées, photos principales à part, première photo de la flotte préchargée.** *Coût* : si la période tarifaire change le bateau le moins cher, le test `photos.test.mjs` demande de relancer `node research/preload_flotte.mjs`.
- **Nombre d'avis masqué sous 50** (consigne de Melvin) : l'accueil et la page concept donnent la note seule (4,3 sur 5). *Coût* : aucun.
- **Accroches reprises** (consigne de Melvin : chaque accroche percutante, aucune évidence) : titre de la flotte « Vingt-deux bateaux, une expérience hors du temps », bases, prix, services, avis, propriétaires, page flotte, page concept. *Coût* : aucun ; textes encore à relire par un natif pour l'anglais.
- **Finish-Gate (HOLD) corrigé** : carte d'An tu plezi (petite photo entière dans son cadre, sans zoom au survol), premier acompte et lien « Détail du prix et échéancier » au-dessus des coordonnées sur téléphone, « personne qui paie » partout et copie de chaque message à l'agence (marquée exemple dans `hypotheses.md`). *Coût* : promesse de copie à l'agence à valider avec RM.

- **Boutons de route au nom complet** (consigne de Melvin) : « Tour de la Martinique », « Grenadines depuis le Marin », « Grenadines depuis Saint-Vincent ». Sur ordinateur, ils passent sur trois lignes : titre, boutons et échelle resserrés sous 900 px de haut pour garder l'itinéraire entier (vérifié à 1 280 × 720, 1 366 × 768, 1 440 × 900) ; le nom de la route n'est plus répété au-dessus de l'échelle (lu par les lecteurs d'écran). *Coût* : titre un peu plus petit sur portable.
- **Plus de mention de rmcroisieres.com comme source dans les pages** (consigne de Melvin) : liens « rmcroisieres.com » des bases, des services et de l'itinéraire, note et lien de la fiche, pied de page, lien 12knots du récapitulatif. Restent les badges « exemple » et « à confirmer ». *Coût* : aucun ; les sources sont dans `docs/faits.md`.
- **Durée : « 1 semaine » ou « du … au … », 5 nuits au moins** (consigne de Melvin), sur la fiche et dans le tunnel, à la place de « 1 ou 2 semaines » (non sourcé) et de « Partir un autre jour ». « 5 jours » compté comme 5 nuits entre les deux dates (`NUITS_MIN` dans `maquette/semaines.js`). Prix des dates libres : chaque nuit au septième du tarif de la semaine de sa période, marqué « à confirmer » ; skipper et hôtesse comptés au nombre de nuits. *Coût* : prix faux si RM facture autrement les séjours courts ; minimum à passer à 4 si « 5 jours » se compte comme RM (« 8 jours / 7 nuits »).
- **« 10 personnes au plus sur ce bateau » retiré** (consigne de Melvin) : la liste des personnes s'arrête déjà à la capacité du bateau. *Coût* : aucun.
- **Rachat de franchise avec skipper : minimum 160 €** au lieu de 260 € (voir plus haut).

