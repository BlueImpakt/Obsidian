# Sabinas Watersport : tunnels de réservation des concurrents du sud-est de Rhodes (31/10/2026)

Question posée : comment réserve-t-on, écran par écran, chez les opérateurs de sorties en bateau de Lindos, Lardos, Kiotari, Haraki, Pefkos et Kolymbia, et sur les plateformes où ils vendent ? Le principe retenu pour Sabina (demande sans paiement immédiat, réponse humaine, WhatsApp pré-rédigé, cf. `2026-10-31-sabinas-reservation.md`) est-il en retard ?

## Méthode et limites

- **Outil** : Playwright Python 1.61 (Chromium), viewport 390 × 844, user-agent iPhone, langue en-GB. Le 1440 n'a pas été rejoué : le mobile suffisait à répondre.
- **Relevé** : tous les faits datent du **31/10/2026**.
- **Captures** : `research/tunnels-rhodes/<concurrent>-<étape>-390.png` (70 fichiers, 28 Mo). Les textes bruts sont dans `research/tunnels-rhodes/txt/` et les scripts dans `research/tunnels-rhodes/scripts/`.
- **Règles respectées** : aucun clic sur « Book now », « Add to cart », « Checkout », « Book and pay », « Send message », « Request a Quote » ou « Envoyer ». Aucune donnée personnelle saisie. Les seuls réglages faits sont des dates, des quantités ou des options, tous restés locaux. Cookies refusés quand un refus existait (« Only essential », « Only necessary », « Decline »). Le bandeau GetMyBoat ne propose que « Close » : il n'a pas été cliqué.
- **Limite n° 1, la saison est finie.** Beaucoup de calendriers sont fermés jusqu'en 2027, et plusieurs fiches sont « sold out » ou « no offers ». Quand l'écran suivant le calendrier n'a pas pu être atteint, c'est écrit « non vu ».
- **Limite n° 2, anti-robots.** Viator renvoie HTTP 403. Expedia et Travelocity renvoient 429 avec la page « Bot or Not? ». GetYourGuide a fonctionné pour une recherche et une fiche, puis a répondu 403. Aucun contournement n'a été tenté.

## 1. Tableau comparatif

Lecture des colonnes :
- « Gestes » : nombre de taps depuis la fiche du produit jusqu'au bouton final, que je n'ai pas cliqué.
- « Prix avant coord. » : le total est-il visible avant de donner ses coordonnées ?
- « Date et pers. d'abord » : la date et le nombre de personnes sont-ils demandés avant l'identité ?

| # | Opérateur (base) · produit testé | Canal et outil | Gestes jusqu'au bouton final | Prix avant coord. | Date et pers. d'abord | Paiement | Annulation, météo | Humain | Fin, délai annoncé |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Water Sports Rodos – Action / South Rhodes Boat Rental** (Lardos) · sortie privée en SeaRay 260 avec skipper | Direct, rentaboat-rhodes.com : widget WordPress non identifié, SDK PayPal (`intent=authorize`) | 6 taps, puis 7 champs de coordonnées, puis « Next » (récapitulatif et paiement non vus) | **Non** : aucun prix dans le tunnel privé | Date et créneau oui ; le nombre de personnes est demandé avec les coordonnées | FAQ : « full amount or a deposit online, or pay locally » ; PayPal ou carte | Météo : l'équipe propose des alternatives ou rembourse. Annulation client : non vu | Téléphone, WhatsApp, e-mail | Non vu |
| 1 bis | idem · activités nautiques (jet-ski, bouées) | Direct, watersports-rodos.com : **Booknetic**, 6 étapes | 2 taps jusqu'au calendrier, puis rien (mai 2027 fermé) | Oui, prix sur chaque carte | Activité, puis date et heure, puis coordonnées | « Online payment is disabled for bookings including parasailing » ; moyen de paiement non vu | Changement gratuit sur la plage | Téléphone, WhatsApp | « Thank you for your request! » (lu dans le code, pas à l'écran) |
| 2 | **Lindos Water Sports / Lindos Rental Boats** (Lindos) · Nireus, Karnic avec skipper | Direct, thelindoswatersports.com : **Turitop** intégré | **Impasse** : le widget affiche « Not available! Booking system will be activated soon » | Prix par heure ou forfait sur la carte | – | Annonce « Secure Your Booking For Just €35 », sans moyen de le faire | Non vu | Téléphone ; bouton WhatsApp flottant (lien non relevé) | – |
| 3 | **Glass Bottom Boat Melani** (Lindos) · croisière partagée de 3 h | Direct, glassbottomboatmelani.com : **FareHarbor** | 2 taps (date, quantité), puis contact et carte **sur la même page**, puis « Book and pay » | **Oui**, 75,82 € pour 2 adultes, « Includes taxes and fees » | Oui | **Total en ligne** (carte, Stripe), alors que le site annonce « €10 per Person » | 100 % ou avoir à J-1 ; 100 % si l'opérateur annule pour la météo | Téléphone, WhatsApp | « Instant confirmation » |
| 4 | **L&A Yachting** (Lindos) · speedboat Axopar privé 2 h | Musement/TUI (« Instant confirmation »). **Le compte Rezdy est fermé** | Fiche « sold out » | £397 « from » | – | Non vu | 100 % à J-1 | Non vu | – |
| 5 | **Summer Breeze Lindos Cruises** (Vlicha) · croisière partagée de 3 h | GetYourGuide et Musement | GYG : 1 tap jusqu'au calendrier, **aucune date ouverte**. Musement : « sold out » | 55 €/pers. (GYG), £46 (Musement) | Oui (GYG : participants et date dans le même bloc) | GYG : « Reserve now and pay later » | 100 % à J-1 (GYG et Musement) | Non vu | – |
| 6 | **Royal Yachts Partnership** (Lindos) · **voilier privé** de 3 h ou 5 h 30 | Musement/TUI | 2 taps (date pré-remplie au 1er nov. 2026, option), puis + groupe, puis « Add to cart » ou « Checkout » | **Oui, par groupe** : £506 (demi-journée), £827 (journée) | Oui | Non vu (après le panier) | **70 % à J-30, 50 % à J-7** | Non vu | « Instant confirmation » |
| 7 | **Kolymbia Sea Lines** (Kolymbia) · catamaran Lagoon 44 partagé | Musement/TUI | 4 taps (date, heure, billets), puis « Add to cart » ou « Checkout » | Oui, £55/pers. | Oui | Non vu | 100 % à J-1 | Chat Musement | « Instant confirmation » |
| 8 | **Boat Cruises Rhodes** (Nikolaos, Lardos) · **catamaran Lucia 40 privé**, 10 h | Click&Boat | 1 tap, puis la fiche « Contact Nikolaos » (date et message), puis « Send message » | **Non** sans date ; **aucune date ouverte** jusqu'à fin 2027 | Date seulement | Non vu | 100 % à J-1 (hors frais de service) | Messagerie Click&Boat | Non vu |
| 9 | **Rhodes Rent a Boat** (Rhodes-ville, revendeur) · Rhodes–Lindos privé en speedboat Jost | Direct, rhodesrentaboat.com : **WhatsApp pré-rédigé par produit** | **1 tap** jusqu'à WhatsApp | **Oui**, « FROM 1 390 € » | Non : c'est au client de les écrire dans WhatsApp | Aucun en ligne | Météo : « the operator reschedules during your stay or refunds » | WhatsApp, téléphone, formulaire | « usually within a few hours », « fast reply » |
| 10 | **Aegean Dream Boats** (Haraki) · location sans permis | Direct, Carrd : **Google Form** | 1 tap, puis 7 champs, puis « Envoyer » | Oui, dans l'en-tête du formulaire (75 € pour 1 h, 320 € la journée) | Non : le nom vient en premier | Aucun | Non vu | WhatsApp | Non vu |
| 11 | **Gin Tonic Lindos Sailing** (Lindos) · voile semi-privée ou privée | CheckYeti et GetMyBoat | CheckYeti : « currently no offers available » | – | – | – | Non vu | – | – |
| 12 | **Rhodes Sea Lines** (Kiotari, Lardos, Lindos) · bateau rapide | CheckYeti et GYG | CheckYeti : « no offers » ; GYG : 403 | – | – | – | Non vu | – | – |
| 13 | **Simons Watersports** (Lardos) · **catamaran privé**, demi-journée | Travelocity/Expedia (Viator) | **Non rejoué** (429) | – | – | – | – | – | – |
| 14 | **Dream Boats** (New Marina) · privé vers Lindos | Expedia | **Non rejoué** (429, « Bot or Not? ») | – | – | – | – | – | – |
| 15 | **Watersport Center Kiotari** | Aucun site trouvé | **Non rejoué** | – | – | – | – | – | – |

**Repère : le catamaran de Sabina (Lavezzi 40) tel que les plateformes le vendent aujourd'hui**

| Canal | Mode | Gestes | Prix affiché | Annulation affichée | Calendrier |
|---|---|---|---|---|---|
| **Pelago** (fournisseur « Sabinas Watersport Rhodos ») | **« Instant confirmation »** | 3 taps (disponibilités, date, « Select »), réglage des personnes, puis « Book now » ou « Add to cart » | **1 277,70 € pour le groupe** (le total ne change pas de 1 à 4 personnes, 8 au maximum) | « Free cancellation », sans délai visible | **Tous les jours ouverts du 31/10/2026 à janvier 2027**, à « 1.3K » |
| **Booking.com** (même intitulé que la fiche Viator 113856P1) | Billet daté | Date (1er novembre présélectionné), créneau de 10 h 30, personnes, ticket « Group (max. 8 people) », puis « Next » | **1 250 €**, « Includes taxes and charges » | En tête : « Free cancellation… up to 24 hours » ; sur le billet : **« Non-refundable »** | Dates ouvertes dès le 1/11/2026 |
| **Click&Boat** (profil « Sabine ») | **Demande** : message pré-rempli « There will be [number of people] of us… » | 1 tap, puis « Send message » | « From £1,077 » (encart d'une autre fiche) | **70 % à J-30** | Aucune date ouverte jusqu'en janvier 2028 |
| **GetMyBoat** | **Demande** (« Request a Quote ») | La barre date, durée et invités est déjà remplie | « $1,602 /day Estimated Rate » ; la description dit 1 250 € avec un **acompte de 350 €** | « Free cancellation up to 14 days » | Non vu |

## 2. Fiches courtes

**1. Water Sports Rodos – Action / South Rhodes Boat Rental (Lardos, plage Lothiarica).** C'est le voisin direct de Sabina.
- Deux tunnels :
  - les activités passent par **Booknetic** (étapes lues dans le DOM : Activities, Extra services, Date & Time, Contact information, My Booking Cart, Confirm Details) ;
  - les bateaux passent par **rentaboat-rhodes.com**.
- Sur rentaboat-rhodes.com, le parcours d'une sortie privée avec skipper est :
  1. « Book Online » ;
  2. « Private Boat Trips » ;
  3. choix de la sortie (coucher de soleil de 2 h en SeaRay 260, ou journée) ;
  4. extras (glacière offerte, transfert gratuit Lardos/Pefkos/Lindos, vin 50 €, champagne 120 €, GoPro 20 €) ;
  5. **calendrier réel**, avec des jours ouverts barrés de vert à partir du 16/04/2027 ;
  6. créneau (18:00-20:00) ;
  7. « Customer Information » : prénom, nom, téléphone, e-mail, commentaires, hôtel, nombre de passagers.
- Je me suis arrêté sur « Next ». **Aucun prix n'est affiché dans le tunnel privé.** La FAQ promet « Instant Booking » et le choix entre paiement total, acompte en ligne ou paiement sur place.
- Météo : « may cancel/change your reservation and provide alternative options or refund your money ».
- URLs : https://www.rentaboat-rhodes.com/book-now/ · https://www.watersports-rodos.com/bookings/
- Captures : `rentaboat-3-widget` à `rentaboat-8-apres-creneau`, `wsrodos-2-service-choisi`, `wsrodos-3-etape2`, `wsrodos-3b-mai-2027`.

**2. Lindos Water Sports / Lindos Rental Boats (Lindos, plage Pallas).**
- Chaque bateau annonce « Secure Your Booking For Just €35 ». Sous chaque carte, l'iframe **Turitop** affiche « Not available! Booking system will be activated soon », avec une adresse Hotmail.
- Le tunnel est donc une impasse ; seuls restent le téléphone et une bulle WhatsApp.
- Prix : Nireus 110 €/h ou 450 € les 6 h ; Karnic 115 ch avec skipper 100 €/h ou 450 € les 6 h.
- URL : https://thelindoswatersports.com/boat-rental
- Captures : `lindosws-1-flotte`, `lindosws-2-carte-karnic`, `lindosws-3-widget-turitop`.

**3. Glass Bottom Boat Melani (Lindos).**
- C'est le seul tunnel direct complet du lot. Le calendrier **FareHarbor** saute à la première date ouverte (12/05/2027, 14 h). Une seule page réunit quantités, total TTC, contact (nom, téléphone, e-mail), carte et conditions, puis « Book and pay ».
- Paiement intégral. Le site annonce pourtant « Secure Your Booking for €10 per Person ».
- Annulation : « full refund or credit if canceled at least 24 hours before… in the event of cancellation by operators due to weather ».
- URL : https://fareharbor.com/embeds/book/glassbottomboatmelani/items/733716/
- Captures : `melani-1-fareharbor`, `melani-3-deux-adultes`, `melani-3-deux-adultes-long`.

**4. L&A Yachting (Lindos).**
- `layachting.rezdy.com` affiche « This account has been canceled ».
- Le speedboat privé de 2 h se vend sur Musement/TUI : « Instant confirmation », « Private Tour », £397, **sold out**, 100 % à J-1.
- URLs : https://layachting.rezdy.com/ · https://www.musement.com/uk/rhodes/gems-of-lindos-2-hour-private-boat-trip-1-511878/
- Captures : `layachting-accueil`, `musement-layachting-1-fiche`.

**5. Summer Breeze Lindos Cruises (Vlicha).**
- Sur GYG : 1 060 avis, 4,7, 55 €/pers., « Reserve now and pay later », 24 h. Calendrier : **aucune date ouverte** dans les mois chargés, à partir d'octobre 2026.
- Sur Musement : « sold out ». Fournisseur : « Summer Breeze Lindos Cruises IKE ».
- URLs : https://www.getyourguide.com/en-gb/lindos-l46233/lindos-all-inclusive-3-hour-swimming-cruise-t627773/ · https://www.musement.com/uk/rhodes/swim-and-snorkel-boat-cruise-in-lindos-area-480535/
- Captures : `gyg-summerbreeze-1-fiche`, `gyg-summerbreeze-2-widget`, `gyg-summerbreeze-3-calendrier`, `musement-summerbreeze-1-fiche`.

**6. Royal Yachts Partnership (voilier privé, Lindos).**
- Musement : « Instant confirmation », « Private Tour ».
- **Prix par groupe** : £506 (option de 3 h, 16 h) et £827 (journée). Une date du 1er novembre 2026 est proposée hors saison.
- Annulation : 70 % à J-30, 50 % à J-7.
- C'est l'exemple le plus proche d'un **bateau privé vendu en réservation immédiate** dans la zone.
- URL : https://www.musement.com/uk/rhodes/private-bay-to-bay-sailing-day-trip-from-lindos-445648/
- Captures : `musement-baytobay-1-fiche`, `musement-baytobay-2-dispo`.

**7. Kolymbia Sea Lines (catamaran partagé « Summer Vibes »).**
- Musement : date (mai 2027 ouvert), heure (10 h ou 13 h), billets à £55, total, puis « Add to cart » ou « Checkout ».
- 24 h. « No extra fees ».
- URL : https://www.musement.com/uk/rhodes/catamaran-cruise-from-kolymbia-harbour-with-drinks-523257/
- Captures : `musement-kolymbia-4-calendrier` à `-6-date-choisie`.

**8. Boat Cruises Rhodes (catamaran Lucia 40, Lardos).**
- C'est le concurrent direct sur le catamaran privé : 10 h, 5 h, coucher de soleil.
- Sur Click&Boat, « Check availability » ouvre « Contact Nikolaos » (date et message), puis « Send message ». Aucune date n'est ouverte jusqu'au 31/12/2027 et aucun prix n'apparaît sans date.
- 100 % à J-1.
- URL : https://www.clickandboat.com/uk/activities/lardos/lindos-by-sea-10-hour-private-sailing-tour-on-luxury-catamaran-7611
- Captures : `cnb-bcr-1-fiche`, `cnb-bcr-2-contact`.

**9. Rhodes Rent a Boat (Mandraki).**
- C'est un revendeur : « We confirm availability with the operator, usually within a few hours ».
- Chaque fiche porte « Book on WhatsApp ». Le message est rédigé avec le nom du produit : « Hi! I'd like to book: Rhodes to Lindos: Full-Day Private Cruise — Speedboat Jost. Please send me availability and price. »
- Prix affiché : 1 390 €. Pas de date ni de nombre de personnes dans le lien.
- URL : https://rhodesrentaboat.com/tour-detail/rhodes-to-lindos-full-day-private-cruise-speedboat-jost
- Captures : `rhodesrentaboat-3-fiche-lindos`, `rhodesrentaboat-4-bouton-whatsapp`.

**10. Aegean Dream Boats (Haraki).**
- « BOOK NOW » ouvre un Google Form : nom, date, heure, téléphone ou WhatsApp, personnes (5 par bateau), durée, notes.
- Les tarifs figurent dans l'en-tête du formulaire. Pas de paiement.
- URLs : https://aegeandreamboats.carrd.co/ · https://forms.gle/Mbh75dRF8ffSfEbG9
- Captures : `aegeandreamboats-1-accueil`, `aegean-form-2-googleform`.

**11-12. Gin Tonic Lindos Sailing et Rhodes Sea Lines.**
- Leurs pages CheckYeti affichent « currently no offers available ».
- La page CheckYeti « Boat Trips Lindos » ne propose plus que des offres « nearby » (Fethiye).
- URLs : https://www.checkyeti.com/en/p/4043/gin-tonic-lindos-sailing · https://www.checkyeti.com/en/p/2389/rhodes-sea-lines · https://www.checkyeti.com/en/boat-tours/greece/lindos/boat-tours
- Captures : `checkyeti-gintonic-1`, `checkyeti-rhodessealines-1`, `checkyeti-lindos-1`.

**Sabina sur les plateformes.**
- Les fiches et leurs URLs :
  - Pelago : https://www.pelago.com/en-GB/activity/pdpge4slk-private-catamaran-daytrip-lindos-rhodos-with-lunch-and-drinks-rhodes/
  - Booking.com : https://www.booking.com/attractions/gr/preyirndn3o3-private-catamaran-daytrip-lindos-rhodos-with-lunch-and-drinks.html
  - Click&Boat : https://www.clickandboat.com/uk/activities/lardos/white-blue-and-divine-a-full-day-on-a-catamaran-22144
  - GetMyBoat : https://www.getmyboat.com/trips/5Yrydkma/
- Captures : `pelago-1-fiche`, `pelago-3-date-choisie`, `pelago-4-option`, `pelago-5-quatre-personnes`, `booking-sabina-1-fiche` à `-3-total`, `cnb-sabina-1-fiche` à `-3-dates`, `getmyboat-1-fiche`, `getmyboat-2-parametres`.
- **Quatre politiques d'annulation différentes pour le même bateau** : 24 h, « non-refundable », 70 % à J-30, 14 jours. Pelago et Booking.com acceptent aussi des dates en novembre-janvier, hors saison.

## 3. Non rejoués

| Concurrent | Raison |
|---|---|
| Simons Watersports (catamaran privé, Lardos) | Pas de site trouvé. Les fiches Travelocity et Expedia renvoient HTTP 429. Viator renvoie 403 |
| Dream Boats (privé vers Lindos) | Expedia renvoie 429 avec la page anti-robot « Bot or Not? » |
| Watersport Center Kiotari | Aucun site trouvé (Greeka : réservation sur place) |
| Gin Tonic, Rhodes Sea Lines | Aucune offre en ligne sur CheckYeti au relevé ; GetYourGuide renvoie 403 à la deuxième visite |
| Fiche Viator de Sabina (113856P1) | HTTP 403. Couverte indirectement par Pelago et Booking.com |
| Unlimited Adrenaline (agence, « Private Boat Tour to Lindos ») | La fiche redirige vers l'accueil : produit retiré, écarté |

## 4. Conclusion

**Quelqu'un vend-il un catamaran ou un bateau privé en réservation immédiate, avec calendrier et paiement en ligne ?**
- **Oui, mais seulement sur les plateformes, et Sabina la première.**
  - Son catamaran est en « Instant confirmation » sur Pelago à 1 277,70 € le groupe, et sur Booking.com à 1 250 €. Le calendrier y est ouvert tous les jours jusqu'en janvier, donc ses disponibilités affichées ne sont pas réelles.
  - Royal Yachts (voilier privé, Lindos) et L&A Yachting (speedboat privé) font de même sur Musement/TUI, avec un prix par groupe.
- **En direct, personne ne le fait pour un catamaran.**
  - Le concurrent catamaran Boat Cruises Rhodes reste sur demande, via Click&Boat.
  - Le seul tunnel direct avec calendrier réel pour une sortie privée est celui de South Rhodes Boat Rental (speedboat SeaRay 260, Lardos). Il ne montre aucun prix et l'étape de paiement n'a pas été vue.
  - Le seul tunnel direct payé en entier est celui de Melani, sur une croisière partagée à 38 €.
  - Lindos Water Sports promet un acompte de 35 €, mais son widget est désactivé.

**Le principe de Sabina est-il en retard ?**
- **Non, il est au niveau du direct, et au-dessus de la plupart.**
  - Ailleurs, on trouve un Google Form, un WhatsApp sans date, un widget en panne, ou un tunnel sans prix.
  - Une demande qui prend sortie, date et personnes au premier écran, avec le total, est déjà meilleure que tout ce qui existe en direct dans la zone.
- **Le seul écart est face aux plateformes.** Elles affichent « Instant confirmation » et un délai d'annulation en une ligne. Le client qui compare voit le même bateau confirmé sur-le-champ, mais 300 € plus cher. La demande directe doit donc compenser avec un délai de réponse chiffré et le prix direct bien visible.

**À emprunter :**
1. **Un total par groupe, écrit « pour le bateau, jusqu'à 8 personnes »**, comme Pelago (« Total EUR 1,277.7 », inchangé de 1 à 4 personnes) et Booking.com (« Group (max. 8 people) · € 1,250 »). Il faut aussi rappeler l'écart avec le prix direct.
2. **Une phrase d'annulation et de météo sous le bouton**, sur le modèle de FareHarbor chez Melani : remboursement ou avoir à J-1, remboursement si l'opérateur annule pour la météo. **Une seule politique sur tous les canaux**, au lieu des quatre relevées chez Sabina.
3. **Un WhatsApp pré-rédigé qui nomme la sortie**, comme Rhodes Rent a Boat (« I'd like to book: … Speedboat Jost »). Le lien de Sabina doit aussi porter la date et le nombre de personnes choisis, ce que personne ne fait. Il faut l'accompagner d'une promesse chiffrée, du type « usually within a few hours ».
4. **Un calendrier qui grise les jours fermés**, comme celui de South Rhodes Boat Rental (jours ouverts marqués de vert à partir du 16/04/2027). Même en mode demande, ça évite les demandes pour des jours où Sabina ne sort pas. C'est l'inverse des plateformes, qui acceptent des réservations en hiver.
5. **Le choix entre acompte et solde**, à proposer dans l'argumentaire, pas dans la maquette. South Rhodes Boat Rental laisse le choix entre paiement total, acompte en ligne ou paiement sur place. Sabina affiche elle-même un acompte de 350 € sur GetMyBoat, contre 150 € fixes en direct : à harmoniser avec elle.
