# RM Croisières : comment la réservation est organisée aujourd'hui (28/10/2026)

Prospect rmcroisieres.com (Le Marin, Martinique, et Blue Lagoon, Saint-Vincent). La question : quel tunnel proposer dans la maquette de refonte, à partir de ce que RM fait réellement aujourd'hui, de ses conditions publiées et de la façon dont sa flotte est déjà vendue ailleurs.

Méthode :
- site lu en entier le 28/10/2026 (extraction de 120 pages, cache dans `research/extraction/_cache/` de ce dépôt) ;
- captures Playwright en 1440 et en 390 px (accueil FR et EN, Booking, fiche Manureva, conditions) dans `C:\Users\LENOVO\AppData\Local\Temp\claude\rm-etude\part1\captures\`, hors dépôt ;
- prix chez les tiers repris de l'étude des plateformes (lot C, même jour) : `prospection-charter/docs/etudes/2026-10-28-tunnels-concurrents-martinique/C-plateformes.md`.

Rien n'a été saisi ni envoyé. Le bandeau cookies a été refusé (Google Maps) ou ignoré (rmcroisieres.com).

> **Correction du brief.** « Aucun prix » est faux. Les 21 fiches bateaux de la flotte affichent une **grille de prix à la semaine par saison, plus la caution** (exemple : [fiche Manureva](https://www.rmcroisieres.com/bateau/manureva-lagoon-42-haut-de-gamme-2019/), capture `rm-fiche-manureva-390.png`). Ce qui manque : l'année des saisons, les frais obligatoires, un total, et tout lien entre la grille et la demande.

---

## 1. Comment on réserve aujourd'hui

### Le parcours

1. Fiche bateau : tableau « Tarifs à la Semaine* », puis « Caution », « (*) hors options », et un lien « Demander un devis ». Ce lien pointe vers `https://www.rmcroisieres.com/reservation` **sans le nom du bateau** : le client doit le choisir de nouveau dans le formulaire ([fiche Manureva](https://www.rmcroisieres.com/bateau/manureva-lagoon-42-haut-de-gamme-2019/)).
2. Page [Réservation](https://www.rmcroisieres.com/reservation/) (titre « réservation et demande de devis »), formulaire WPForms. Champs :

| Champ | Type | Obligatoire |
|---|---|---|
| Nom et Prénom | texte | oui |
| Email | email (filtre anti-spam sur certains domaines) | oui |
| Numéro de téléphone | texte | oui |
| Nombre de passagers | **texte libre** | non |
| Dates souhaitées | **texte libre** (pas de sélecteur de date) | non |
| Vous êtes intéressés par | liste de 21 bateaux | non |
| Vous souhaitez | cases : Skipper, Hôtesse, « Possibilité de rachat d'assurance », Kayak, Paddle, Équipement de pêche | non |
| Message | zone de texte | **oui** |

   Bouton « Envoyer la demande de réservation ». Promesse : « Nous vous répondrons dans les plus brefs délais » (pas de délai chiffré). Pas de champ base de départ (Le Marin ou Blue Lagoon), ni durée, ni coque nue / skipper explicite, ni expérience du chef de bord.
3. Ensuite : non visible. Contrat, acomptes et caution sont décrits dans les conditions (§3), sans outil en ligne.

### Liens et contacts

- **Lien cassé confirmé** : sur l'accueil FR et EN, le bouton « Rentrons en contact » pointe vers `http://reservation/` ([accueil EN](https://www.rmcroisieres.com/), [accueil FR](https://www.rmcroisieres.com/fr/)), contrôle Playwright du 28/10. Les liens « Booking » et « Contact Us » du menu marchent (`/reservation-2/`, `/contact-us/`).
- La page [Booking](https://www.rmcroisieres.com/reservation/) a dépassé 45 s de chargement (`networkidle`) aux deux essais Playwright du 28/10 ; la capture a été prise quand même.
- Téléphone : +596 696 722 544, « du lundi au samedi de 9h à 17h » (pied de page de toutes les pages ; Google Maps : « Ouvre à 08:30 »).
- Email : publié seulement dans les mentions légales, rmservicesnautiques@live.fr ([mentions légales](https://www.rmcroisieres.com/politique-de-confidentialite-mentions-legales/)).
- **WhatsApp : aucun lien** (aucun `wa.me` ni `whatsapp` dans le code des pages, contrôle du 28/10). Pas de chat.
- Facebook et Instagram en pied de page.
- Formulaire [Nous contacter](https://www.rmcroisieres.com/nous-contacter/) : nom, prénom, email, téléphone, message.
- [Devenir propriétaire](https://www.rmcroisieres.com/devenir-proprietaire/) : défiscalisation outre-mer (art. 244 quater W du CGI, « au moins 35 % »), et « vous pouvez devenir membre de notre Groupement d'Intérêt Économique qui vous facilitera la gestion de vos locations ».

---

## 2. Ce qui est vendu

| Point | Ce que dit RM | Source |
|---|---|---|
| Formules | Location « avec ou sans équipage ». Skipper : **250 € TTC / jour** + nourriture du skipper. Hôtesse : **200 € TTC / jour** + nourriture (« ce tarif peut varier en fonction de votre base de départ ») | [Skipper et hôtesse](https://www.rmcroisieres.com/skipper-et-hotesse/) |
| Skipper chez les tiers | 280 € / jour, hôtesse ou cuisinier 220 € / jour (RM sur 12knots) : **écart avec le site** | [12knots, page RM](https://12knots.com/fr/review/rm-croisieres/) |
| Équipage complet | Sunreef 50 « Liberta » présenté « luxe crewed », barrable sans skipper « pour les marins expérimentés » ou avec (cabine équipage) | [fiche Liberta](https://www.rmcroisieres.com/catamaran-sunreef-50-luxe-crewed-liberta/) |
| Cabine | Non trouvé | — |
| Durée | Prix **à la semaine uniquement**. Itinéraires types de 8 jours (Grenadines). Journée, week-end : non trouvé | fiches bateaux ; [Au départ de Saint-Vincent](https://www.rmcroisieres.com/au-depart-de-saint-vincent/) |
| Jour de rotation | Non écrit sur le site. Chez 12knots, la grille de RM est découpée en semaines **samedi-samedi** (ex. 09.01 → 15.05.2027, 16 → 23.01.2027) | [12knots Take it Easy](https://12knots.com/en/yacht-charter/lagoon-450-premium-ac-take-it-easy-49945-bs-le-marin/) |
| Check-in / check-out | Embarquement **18h00** le 1er jour, mise en main le lendemain matin ; débarquement **10h00**. Mise en main anticipée (départ le 1er soir, du lundi au samedi selon planning) : **125 €**. Débarquement différé à 16h : **300 €** | [Formalités](https://www.rmcroisieres.com/formalites-administratives-et-sanitaires/) |
| Bases | Le Marin ; Blue Lagoon (baie de Calliaqua, 15 min de l'aéroport Argyle SVD), « sans jour de transit depuis la Martinique » | [page Blue Lagoon](https://www.rmcroisieres.com/au-depart-de-bequia/) |
| One-way Le Marin ↔ Blue Lagoon | Non trouvé (ni prix ni mention) | — |
| Caution | Par fiche : 2 000 € (Sunreef 50) à 6 000 € (Lagoon 46, 450, Elba 45) ; 5 000 € sur la plupart ; 3 000 à 4 000 € sur les monocoques. Versée « par MasterCard, Visa ou espèces en euros » à la prise en charge (CGV art. 6). **Incohérences** : Sunreef 50 à 2 000 € sur la fiche actuelle, 7 000 € sur l'ancienne page, 10 000 € chez 12knots | fiches ; [ancienne page Liberta EN](https://www.rmcroisieres.com/catamaran-sunreef-50-luxe-crewed-liberta-2/) ; lot C §10 |
| Rachat de franchise | Deux versions sur le site : « minimum 260 €, franchise résiduelle 2 000 € » ; et « 1 000 € de caution seulement ». Obligatoire avec skipper : **3 % de la location** (« 160 € minimum » sur l'une des pages). Chez les tiers : « damage waiver » 3 % ou 380 € | [Formalités](https://www.rmcroisieres.com/formalites-administratives-et-sanitaires/) ; [Qui sommes-nous](https://www.rmcroisieres.com/qui-sommes-nous/) ; lot C §10 |
| Frais de fin de séjour | « Le forfait nettoyage est obligatoire et le tarif varie selon la taille du bateau » (montant non publié sur le site). **Chez les tiers : 680 € fixes** (administration 260 + ménage 300 + consommables/gaz 120) | [Qui sommes-nous](https://www.rmcroisieres.com/qui-sommes-nous/) ; [12knots Take it Easy](https://12knots.com/en/yacht-charter/lagoon-450-premium-ac-take-it-easy-49945-bs-le-marin/) |
| Linge, nettoyage en plus | Jeu de linge : 40 € par cabine double, 20 € la pointe avant ; nettoyage supplémentaire 250 € | [La vie à bord](https://www.rmcroisieres.com/la-vie-a-bord/) |
| Carburant | Bateau livré avec les pleins (eau, gasoil, gaz, essence HB), à rendre pleins (CGV art. 9) | [CGV](https://www.rmcroisieres.com/condition-location/) |
| Jouets | Kayak, paddle, matériel de pêche, filet + gilet enfant : 150 € chacun « la croisière » | [Jeux aquatiques](https://www.rmcroisieres.com/location-de-jeux-aquatiques/) |
| Avitaillement | Renvoi vers des tiers : application Paradise Foods, Appro-Zagaya, sailshop.fr. Chez 12knots : option avitaillement de RM | [Ravitaillement](https://www.rmcroisieres.com/ravitaillement/) ; [Qui sommes-nous](https://www.rmcroisieres.com/qui-sommes-nous/) |
| Transferts | Aéroport → marina : **65 €** de 1 à 5 passagers, **13 € / pers.** à partir de 6, payés au chauffeur. Chez les tiers : 150 € | [Transfert](https://www.rmcroisieres.com/transfert-aeroport-marina/) ; lot C §10 |
| Taxes, clearance Grenadines | Le chef de bord passe au bureau le lendemain de l'arrivée pour les papiers et les « formalités douanières » (bureau 7h30-16h30). CGV art. 7 : le locataire acquitte les taxes douanières de chaque État visité. **Montants non trouvés** chez RM (Sunsail publie 35 € de clearance par adulte et 25 à 75 € de mouillage par nuit : lot B) | [Formalités](https://www.rmcroisieres.com/formalites-administratives-et-sanitaires/) ; [CGV](https://www.rmcroisieres.com/condition-location/) |
| Permis / CV pour la coque nue | Aucun permis exigé par écrit. Locataire de **21 ans minimum** ; le chef de bord remplit une **fiche d'expérience nautique** ; RM peut refuser le bateau et imposer un skipper payant « nonobstant les références, brevets et permis présentés » ; navigation solitaire et de nuit interdites ; côte au vent de la Martinique interdite (CGV art. 7) | [CGV](https://www.rmcroisieres.com/condition-location/) |

### Grille de prix publiée sur le site (semaine, hors options et hors frais)

Saisons communes à toutes les fiches, **sans année**, répétées deux fois (le second cycle correspond vraisemblablement à la saison suivante) : 08/01-15/05, 15/05-20/08, 20/08-01/11, 01/11-20/12, 20/12-07/01. Relevé du 28/10/2026, fiches FR liées depuis [Tous nos catamarans](https://www.rmcroisieres.com/tous-nos-catamarans/) et [Tous nos monocoques](https://www.rmcroisieres.com/tous-nos-monocoques/).

| Bateau (fiche) | 08/01-15/05 | 15/05-20/08 | 20/08-01/11 | 01/11-20/12 | 20/12-07/01 | Caution |
|---|---|---|---|---|---|---|
| Lagoon 42 Haut de Gamme : Sol, Estella, Pantagonia, Le Gaspésien, Rev'Anou (+ Affligem, fiche EN) | 7 800 € | 5 700 € | 4 800 € | 5 900 € | 8 700 € | 5 000 € |
| Lagoon 42 « La Gloria » | 6 900 € | 4 900 € | 3 900 € | 4 900 € | 7 000 € | 5 000 € |
| Lagoon 43 « Le Dumbea » (2025), Lagoon 43 « Kayo » (fiche EN) | 8 500 € | 7 000 € | 6 700 € | 7 400 € | 10 400 € | 5 000 € |
| Lagoon 450 « Take it Easy » (2017) | 8 500 € | 7 000 € | 6 700 € | 7 400 € | 10 400 € | 6 000 € |
| Lagoon 46 « Manureva » (2019), « Lily » (2020) | 9 900 € | 7 300 € | 6 900 € | 7 700 € | 11 500 € | 6 000 € |
| Elba 45 « Ola 2 » (2023) | 9 900 € | 7 300 € | 6 900 € | 7 100 € | 11 600 € | 6 000 € |
| Lagoon 46 « Dlokoko » | 10 500 € | 8 000 € | 7 200 € | 8 500 € | 14 000 € | 6 000 € |
| Sunreef 50 (2020) | 19 900 € | 17 500 € | 17 500 € | 18 400 € | 27 300 € | 2 000 € |
| Bali Catspace 40 « An ti plezi », « Yurelle » | 6 400 € | 4 900 € | 4 000 € | 4 500 € | 7 000 € | 5 000 € |
| Aquila 32 « Sea Naaps » / Aquila 28 « Cap Antilles » | 7 100 € / 4 200 € toute l'année | | | | | 5 000 € |
| Beneteau 46.1 « Bieckert » | 5 800 € | 5 000 € | 4 200 € | 5 000 € | 7 500 € | 5 000 € |
| Beneteau Oceanis 40.1 « Madelon » | 4 800 € | 3 900 € | 3 100 € | 3 900 € | 5 500 € | 4 000 € |
| Dufour 39 « Rothko » | 3 800 € | 3 600 € | 2 800 € | 3 700 € | 4 800 € | 5 000 € |

Défauts relevés sur ces fiches :
- **Fiche Lagoon 43 « Kayo » FR : cases de prix vides** (« € » seul) ; la version EN est remplie.
- **Le Dumbea FR** : 10 400 € sur la ligne « 01/11 au 20/12 » du second cycle, contre 7 400 € sur la version EN (coquille probable).
- **Manureva** : URL `manureva-lagoon-42-…` alors que la fiche titre « Lagoon 46 » ; 11 500 € (FR) contre 11 600 € (EN) aux fêtes.
- **Sol EN** : 8 700 € au lieu de 7 800 € sur le second cycle haute saison.
- D'anciennes pages (« Weekly Rates », `catamaran-…-2/`) restent en ligne avec d'autres prix (Manureva 9 300 €, Take it Easy 8 000 €, Liberta 17 500 € en haute saison) : à supprimer ou rediriger.
- Le « Deux Océans – Bali 5.4 » apparaît dans la liste du formulaire mais n'a pas de fiche.
- Flotte : l'accueil annonce « 24 voiliers » ; 21 noms sont listés. 12knots annonce **39 bateaux** pour RM (31 catamarans, 5 voiliers, 3 bateaux à moteur, [page RM](https://12knots.com/fr/review/rm-croisieres/)) et Booking Manager « 13 catamarans et 3 voiliers » en mars 2023 ([actualité BM](https://www7.booking-manager.com/en/news/rm-croisieres-blue-lagoon-st-vincent-le-marin-martinique-n1714.html)).

**Ces prix sont identiques à ceux que RM diffuse chez les agences** (Manureva 9 900 €, Take it Easy et Dumbea 8 500 €, Lagoon 42 Premium 7 800 € en haute saison chez 12knots, Click&Boat, Sailogy : lot C §10). La maquette peut donc les reprendre tels quels, en ajoutant les 680 € de frais vus chez les tiers.

---

## 3. Conditions de location (CGV publiées)

Source : [Condition Location](https://www.rmcroisieres.com/condition-location/) (FR) et [Rental conditions](https://www.rmcroisieres.com/rental-conditions/) (EN), identiques sur ces points. Pas de PDF, pas de date de version.

- **Paiement (art. 4)** :
  - réservation à plus de 3 mois du départ : **30 % à la réservation, 30 % à J-3 mois, solde à J-1 mois** ;
  - de 1 à 3 mois : **50 % à la réservation, solde à J-1 mois** ;
  - à moins d'un mois : **100 %** ;
  - retard de paiement : RM peut annuler sans remboursement.
- **Moyens de paiement (art. 4)** : **Visa, MasterCard, chèque français, virement** ; pas de chèque à moins d'un mois ; espèces en euros jusqu'à 50 % du total. Comment la carte est encaissée (lien, terminal, VAD) : **non trouvé**. Aucun paiement en ligne sur le site.
- **Annulation par le client (art. 2)** :
  - à plus de 180 jours : acomptes remboursés **moins 300 €** de frais de gestion ;
  - de 180 à 90 jours : **50 %** des acomptes remboursés, moins 300 € ;
  - à 90 jours et moins : **aucun remboursement** ;
  - « le montant de la location restera acquis au loueur […] quel que soit le motif » ;
  - **assurance annulation** possible, « au bénéfice et aux frais » du locataire (le formulaire propose une case « Possibilité de rachat d'assurance »).
- **Annulation par RM (art. 3)** : bateau équivalent sous 48 h ou remboursement au prorata, sans dommages-intérêts. Panne de confort (générateur, clim, dessalinisateur) : aucune indemnité.
- **Météo et cyclones (art. 7 et 8)** : pas de sortie annoncée force 7 et plus ; en cas de dépression, tempête tropicale ou cyclone, rejoindre la marina ou le « trou à cyclone » ; « le mauvais temps ne saurait être invoqué » pour un retour en retard (pénalité : double du prix quotidien par jour de retard). **Aucune clause d'annulation ou de report liée à la saison cyclonique** (non trouvé).
- **Prise en charge (art. 6)** : location soldée, contrat signé, caution versée, inventaire signé, passeports et liste d'équipage fournis. Place de port gratuite le premier et le dernier jour.
- **Caution (art. 8 et 10)** : rendue « au plus tard dans un délai d'un mois », encaissable sans préavis en cas de dommage.
- Régate : franchise et caution doublées, préautorisation carte 7 jours avant.

**Contradiction avec ce que RM publie chez les agences.** Sur 12knots, les conditions de RM sont : **acompte 50 %, solde à J-45**, 50 % retenus à plus de 46 jours, 100 % à 45 jours et moins, option de 3 jours sans paiement ([12knots, Take it Easy](https://12knots.com/en/yacht-charter/lagoon-450-premium-ac-take-it-easy-49945-bs-le-marin/), « Payment & Cancellation », relevé du 28/10). Deux barèmes coexistent : celui du site (30/30/40, 180/90 jours) et celui du flux B2B (50/50, J-45). À trancher avec RM avant de les afficher.

---

## 4. Planning et intermédiaires

### Booking Manager (MMK) : confirmé

- « RM Croisieres from Martinique joined Booking Manager to offer 13 Catamarans and 3 Sailing Yachts […] now available for distribution and real-time bookings », 17/03/2023 ([booking-manager.com](https://www7.booking-manager.com/en/news/rm-croisieres-blue-lagoon-st-vincent-le-marin-martinique-n1714.html)).
- 12knots et BeBlue affichent exactement les mêmes semaines réservées pour Manureva (26/12/2026 → 06/03/2027, et 03 → 10/04/2027) et les mêmes libellés de frais : un flux commun, cohérent avec Booking Manager (lot C §11).
- Indice d'un ancien flux Sedna (URL 12knots en `-sed…`), non confirmé. Nausys, YachtSys : aucune trace.
- Booking Manager propose une **API REST** et un **widget de recherche** que le loueur peut intégrer à son propre site (« a great way to implement online bookings on your website ») : [API](https://portal.booking-manager.com/en/products/rest-api.html), [offre loueurs](https://www.booking-manager.com/en/products/charter-operators.html). Conditions d'accès et prix : non trouvés (formulaire de contact).

### Où la flotte est vendue (détail et URLs : lot C §10)

| Canal | Nom affiché | Ce qu'on y voit |
|---|---|---|
| 12knots | **RM Croisieres** (page loueur) | grille semaine par semaine, statut Available / Booked, frais 680 €, conditions 50 % / J-45, note **3,5 sur 3 avis** (deux négatifs de 2025 sur l'entretien) |
| Borrow A Boat (ex-Zizoo) | **RM Croisieres**, « partenaire depuis 2016 » | Take it Easy 16-23/01/2027 : 8 500 €, 9 300 € TTC au total ; annonces Estella, Lorena, Liberta retirées |
| Sailica | « operated by RM Croisieres » | Lorena, sans prix |
| SamBoat, Click&Boat | « **Roberto** », compte pro | Dumbea, Lagoon 42/46/450, Elba 45 ; frais différents sur Click&Boat (570 €) ; calendrier SamBoat qui ne colle pas avec 12knots |
| BeBlue, Sailogy, GlobeSailor | loueur masqué | mêmes grilles et mêmes frais que RM |

### Prix relevés chez les tiers (« prix relevé chez <agence> », 28/10/2026, par semaine, hors 680 € de frais sauf mention)

| Bateau | Agence | Période | Prix | Attribution |
|---|---|---|---|---|
| Manureva (Lagoon 46) | 12knots | 09/01 → 15/05/2027 | 9 900 € (complet du 26/12 au 06/03) | certaine |
| Manureva | 12knots | 15/05 → 21/08/2027 ; 21/08 → 30/10/2027 ; fêtes 2026-27 | 7 300 € ; 6 900 € ; 11 600 € | certaine |
| Manureva | BeBlue | 06/03 → 15/05/2027 | 9 900 € (9 702 € après −2 %) | probable |
| Take it Easy (Lagoon 450) | 12knots | 16 → 23/01/2027 | 8 500 €, disponible | certaine |
| Take it Easy | Borrow A Boat | 16 → 23/01/2027 | 8 500 €, **9 300 € TTC** tout compris | certaine |
| Le Dumbea (Lagoon 43) | 12knots | 09/01 → 15/05/2027 ; 15/05 → 21/08/2027 | 8 500 € (16-23/01 complet) ; 7 000 € | certaine |
| Le Dumbea | SamBoat (« Roberto ») | 20 → 27/03/2027 | 9 180 € total (8 500 + 680) | probable forte |
| Estella (Lagoon 42) | 12knots | nov. → mi-déc. 2026 ; 26/12 → 02/01 | 5 900 € ; 8 700 € (grille arrêtée au 09/01/2027) | certaine |
| Lagoon 42 Premium (sans nom) | Click&Boat (« Roberto ») | 16 → 23/01/2027 | 7 800 € ; total 8 508 € (7 j) ou 9 633 € (8 j facturés) | probable |
| Lagoon 42 (sans nom) | Sailogy | 16 → 23/01/2027 | 7 800 €, 8 480 € au total | probable |
| Lagoon 42 2018 (sans nom) | GlobeSailor | 16 → 23/01/2027 | 6 900 € − 276 € = 6 624 € hors frais | probable |
| Elba 45 | Click&Boat ; Sailogy | 07/01 → 15/05 ; 16 → 23/01/2027 | 9 900 € ; 9 900 € | probable |
| Lagoon 46 Luxe (Dlokoko) | Click&Boat | 07/01 → 15/05 | 10 500 € | probable |
| Aquila 32 (Sea Naaps) | Sailogy | 16 → 23/01/2027 | 7 140 € | probable forte |
| Liberta (Sunreef 50) | 12knots | — | aucune grille affichée ; frais 2 330 €, caution 10 000 € | certaine |
| Liberta | SamBoat (« Thierry ») | 07/01 → 30/04 ; 01/05 → 30/06 | 16 600 € ; 13 800 € + skipper et hôtesse obligatoires | non attribuable à RM sur cette annonce |
| Lorena (Lagoon 450) | Sailica | — | prix non trouvé | certaine |

### Structure : des bateaux de propriétaires

Registre des entreprises ([recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr/search?q=RM%20SERVICES%20NAUTIQUES&code_postal=97290), 28/10/2026) :
- **RM CROISIERE** (nom commercial RM CROISIERES), SARL créée en 2013, NAF 77.21Z, gérants Frédéric Bonniol, Patrick Letupe, Roberto Maxera, adresse « chez Mr Roberto Maxera, Capitainerie du Marin ».
- **GROUPEMENT RM CROISIERES** (SIREN 847 686 342), **GIE** créé en 2019, administrateur Roberto Maxera, « c/o RM Services Nautiques ». C'est l'entité nommée dans les [mentions légales](https://www.rmcroisieres.com/politique-de-confidentialite-mentions-legales/), et le GIE dont parle la page Devenir propriétaire.
- Domiciliées « c/o RM Services Nautiques, Marina du Marin » : **RM CROISIERES TOO** (2019), **RM CROISIERES FIVE** (2023), **BLUE OCEAN SAILING** (2019, gérant Thierry Proust), **RM LOCATION** (2015). TAOTE CROISIERES (2019) sort aussi sur la recherche « Maxera » au Marin.

Lecture (à confirmer avec RM) : une société par bateau ou par propriétaire, regroupées dans un GIE géré par RM. Blue Ocean Sailing (Thierry Proust) vend aussi « son » Sunreef 50 Liberta sur blueoceansailing.fr et sur SamBoat sous « Thierry » : un propriétaire peut donc commercialiser son bateau en parallèle de RM. Conséquence directe pour le tunnel : **le planning n'appartient pas qu'à RM**, les semaines propriétaire et les ventes directes des propriétaires doivent remonter dans Booking Manager pour qu'un calendrier en ligne soit fiable.

---

## 5. Réputation et clientèle

- **Google** : 4,3 ([fiche Google Maps](https://www.google.com/maps/place/RM+CROISIERES/@14.4693096,-60.8642649,17z), 28/10/2026), 20 avis à l'audit du 23/10. Le texte des avis n'est pas lisible sans compte (« affichage limité de Google Maps ») : **avis récurrents non trouvés**.
- **12knots** : 3,5 sur 3 avis, dont deux de 2025 sur l'entretien (pompe de cale, climatisation, foc, frigo, batterie), un de 2020 positif ([page RM](https://12knots.com/fr/review/rm-croisieres/)).
- **TripAdvisor** : non trouvé.
- Office de tourisme : fiche [martinique.org](https://www.martinique.org/en/things-to-do/water-sports-and-activities/rm-croisieres).
- **Part de clientèle FR / US / autres : non trouvée.** Indices indirects seulement :
  - le site s'ouvre en anglais (racine en EN, français sous `/fr/`), et l'image d'accueil s'appelle `home-page-carousel-usa.jpg` ;
  - « des clients qui viennent du monde entier » ([Qui sommes-nous](https://www.rmcroisieres.com/qui-sommes-nous/)) ;
  - diffusion chez des agences italienne (BeBlue), britannique (Borrow A Boat), internationales (12knots, Sailogy) et françaises (SamBoat, Click&Boat, GlobeSailor).

---

## 6. Conclusion : quel tunnel pour la maquette

| Option | Pour | Contre | Verdict |
|---|---|---|---|
| **Demande sans calendrier** (formulaire structuré) | Aucune intégration ; c'est le standard local (11 loueurs locaux sur 13, lot A) | Ne fait pas mieux que la page actuelle ; le client ne sait pas si sa semaine est libre, alors que 12knots le lui dit | Insuffisant pour RM |
| **Réservation immédiate avec acompte** | C'est ce que fait Dream Yacht au Marin (acompte 30 %, lot B) | Suppose un planning unique et à jour ; or des propriétaires vendent en parallèle (Liberta), SamBoat diverge déjà du flux ; deux barèmes d'acompte contradictoires ; aucun outil d'encaissement en ligne connu | Pas en phase 1 |
| **Calendrier de disponibilités + demande** | Le planning existe déjà dans Booking Manager (dispo semaine par semaine, prix, frais) ; un outil du marché suffit, comme Misterbooking chez Alternative et ACM (lot A) ; le bureau garde la main sur le contrat et l'acompte | Dépend de l'accès API ou widget Booking Manager (conditions non publiques) | **Recommandé** |

**Recommandation de principe** : calendrier « libre / complet » par bateau et par semaine (samedi-samedi), alimenté par Booking Manager, puis **demande de réservation pré-remplie** (bateau, base, semaine, formule coque nue / skipper / hôtesse, passagers, options, expérience du chef de bord) avec **total affiché** (location + 680 € de frais + options, caution à part) et **échéancier d'acompte** calculé selon la date. RM confirme, envoie le contrat et l'appel d'acompte. Ajouter WhatsApp et un délai de réponse chiffré.

Dans la maquette, avant d'avoir l'accès Booking Manager :
- calendrier marqué « exemple » ou « disponibilités indicatives » ;
- prix : grille du site, et pour les totaux « prix relevé chez 12knots » ;
- conditions : afficher le barème du site, avec la mention « à confirmer » tant que le barème 50 % / J-45 diffusé chez les agences n'est pas tranché.

Phase suivante seulement : option ferme de 3 à 7 jours (comme l'option de 3 jours que RM accorde déjà via 12knots), puis acompte en ligne, si RM veut et si le planning est jugé fiable.

---

## 7. Questions à poser à RM

1. Quel barème fait foi : site (30/30/40, annulation à 180/90 jours) ou agences (50 %, solde et annulation à J-45) ?
2. Booking Manager est-il la source unique du planning, y compris pour les semaines propriétaires et les ventes SamBoat / Click&Boat ? Accès API ou widget inclus dans votre abonnement ?
3. Part des réservations directes et commissions versées aux agences (SamBoat : 20 % d'après son aide).
4. Comment encaissez-vous la carte aujourd'hui (terminal, lien VAD, banque) ?
5. Montant exact des frais obligatoires (680 € partout ?) et du forfait ménage par taille de bateau.
6. Tarifs skipper et hôtesse : 250 / 200 € (site) ou 280 / 220 € (agences) ?
7. One-way Le Marin ↔ Blue Lagoon : possible ? À quel prix ? Qui gère la clearance ?
8. Les propriétaires gardent-ils le droit de vendre leurs semaines eux-mêmes (cas Liberta) ?
9. Vous travaillez en semaine samedi-samedi uniquement, ou départs libres hors haute saison ?
10. Origine de la clientèle (FR, US, Canada, Europe).
11. Quelle est la flotte réelle : 21 fiches, 24 annoncés, 39 chez 12knots ?
