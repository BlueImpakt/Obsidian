---
tags: [project-doc, sabinas-watersport]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: GitHub/sabina-watersport-refonte/docs/01-audit-contenu.md
---

↩ [[sabinas-watersport-refonte]]

# Audit de contenu — Sabinas Watersport Rhodos (3 sites)

Relevé du 21/10/2026. Sources : crawl curl des 2 sites Jimdo Creator (46 URL + pages légales), HTML de dolphin-tours-rhodos.com récupéré en curl (il a répondu 200 ce jour-là) et recoupé avec le relevé navigateur `research/dolphin-tours-rhodos.md`. HTML bruts : `research/raw/{sw,cat,dol}/`, textes extraits : `research/text/`, images originales : `research/raw/img/`.

Abréviations : **SW** = sabinas-watersport.com · **CAT** = catamaran-yachtsailing-rhodos.com · **DOL** = dolphin-tours-rhodos.com

> **Point clé** : les « Click pictures below for prices 2026 » ne renvoient **pas à des grilles tarifaires en image**. Ce sont des photos cliquables qui mènent aux pages où les prix sont **écrits en texte**. Les 47 images uniques des 3 sites ont été vérifiées : aucune ne contient de grille de prix. Tous les tarifs ci-dessous sont donc retranscrits depuis le texte HTML.

---

## 1. Structure des sites

### SW — sabinas-watersport.com (Jimdo Creator, 23 URL dans le sitemap)
Le menu contient 3 arbres de langue en parallèle. Les pages FR et DE sont servies avec `lang="en-US"`.

| EN | DE | FR |
|---|---|---|
| `/` (accueil EN) | `/de-katamaran-tagestour-bootstouren-wassersport/` | `/fr-excursions-en-bateau-sports-nautiques/` |
| `/our-boat-trips-watersports-english/catamaran-daycruise-private-boat-trips/` (arborescence différente des autres pages EN) | `…/katamaran-tagestour-private-boot-trips/` | `…/excursion-en-catamaran-tour-coucher-de-soleil/` |
| `/en-boat-trips-watersports/sailboat-tour-yachtsailing/` | `…/yachtsegeln-segeltour/` | `…/excursion-en-voilier-tout-la-jounee/` (faute dans l'URL) |
| `/en-boat-trips-watersports/private-boat-tour/` | `…/private-bootstour/` | `…/tour-prive-en-bateau/` |
| `/en-boat-trips-watersports/watersports-prices/` | `…/wassersport-preise/` | `…/sports-nautiques-et-tarifs/` |
| `/en-boat-trips-watersports/booking-request/` | `…/buchungsanfrage/` | `…/demande-de-réservation/` |
| `/en-boat-trips-watersports/about-us/` | `…/über-uns/` | `…/à-propos-de-nous/` |
| `/en-boat-trips-watersports/deposit-payment/` | — | — |

Il y a aussi `/about/`. C'est la boîte « Impressum » de Jimdo, qui contient l'adresse et l'e-mail mais aucune information légale.

### CAT — catamaran-yachtsailing-rhodos.com (Jimdo Creator, 18 URL)
| EN | DE | FR |
|---|---|---|
| `/` (accueil = page « Our trips » EN) | `/info-auf-deutsch/unsere-touren/` | `/fr-notre-excursions/` |
| `/info-in-english/` (About us) | `/info-auf-deutsch/` (Über uns) | — |
| `…/catamaran-photos-info/` | `…/katamaran-fotos-info/` | `…/catamaran-photos-info/` |
| `…/rates-2026-catamaran-private-tour/` | `…/preise-2026-katamaran-private-tour/` | `…/tarifs-2026-catamaran-tour-prive/` (contient aussi le sunset) |
| `…/romantic-catamaran-sunset-cruise/` | `…/romantic-catamaran-sunset-tour/` | — |
| `…/booking-request/` | `…/buchungsanfrage/` | `…/demande-de-réservation/` |
| `…/deposit-payment/` | — | — |

### DOL — dolphin-tours-rhodos.com (Jimdo **Dolphin**, 4 URL, EN uniquement)
Pages : Home, Prices, Contact & Location, About us. Pages légales : Imprint, Privacy, Withdrawal.

**Constat** : le même catalogue est réparti sur 3 domaines et 7 « sites » de langue. SW ne contient aucune info sur le catamaran : ses 3 pages catamaran (EN/DE/FR) se limitent à une photo qui renvoie vers CAT.

---

## 2. Catalogue complet des offres et tarifs 2026

Point de départ commun : **station Sabinas Watersport, Stafilia Beach, 85109 Lardos** (entre Lindos et Kiotari). Tous les bateaux ont un skipper, donc aucun permis n'est demandé pour les tours.

### 2.1 Catamaran — Journée privée « Day Cruise to Blue Lagoon » (CAT, DOL)
- **Bateau** : Fountaine Pajot Lavezzi 40 « **THOI** » (le site écrit « Fountain Pajot »). 40 pieds, 4 cabines doubles, 2 WC, carré vitré avec cuisine, espace extérieur ombragé, grand filet avant à environ 1 m au-dessus de l'eau.
- **Durée et horaires** : 6 h, **10:30 – 16:30**.
- **Prix (privatisation)** :

| Nombre de personnes | Prix |
|---|---|
| jusqu'à 4 | **950 €** |
| jusqu'à 6 | **1 050 €** |
| jusqu'à 8 | **1 150 €** |

- **Capacité** : 8 personnes maximum.
- **Inclus (page Rates)** : catamaran privé, capitaine professionnel, hôte/hôtesse, diesel, annexe (« dinghi ») pour le transfert plage, snack d'accueil, déjeuner fraîchement préparé (l'accueil précise « fresh, organic & local », style méditerranéen), vin blanc, bières, softs, jus et eau plate à volonté, masques de snorkeling, SUP, jouets aquatiques.
- **Itinéraire** : départ Sabinas Watersport → « Cave Island », île volcanique avec tunnel naturel (dauphins et tortues possibles entre l'île et le cap de Lindos) → port naturel de Lindos (arrêt photo sur l'Acropole) → **Blue Lagoon** (baignade et snorkeling près du petit récif) → déjeuner servi à l'arrière sous l'ombre → retour, détente dans le filet avant.
- **Options** : repas végétarien ou végan sur demande (**mentionné en FR uniquement**).
- **Public visé** : couples, familles avec jeunes enfants (FR : « enfants de tous âges »), groupes, lune de miel, anniversaires, mariages.

### 2.2 Catamaran — Journée semi-privée « Half-private Tour » (CAT uniquement)
- 6 h (mêmes horaires et même programme), **160 € par personne**, groupe mixte de **8 personnes maximum**, « all services included as described above ».
- **Absente de DOL**, qui ne propose que la formule privée, et **absente de SW**.

### 2.3 Catamaran — Sunset Cruise privée (CAT)
- **Durée et horaires** : 3 h, **17:00 – 20:00**.
- **Saison** : EN « end of May until mid of September » ; DE et FR « de mai à mi-septembre » (**incohérence**).

| Nombre de personnes | Prix |
|---|---|
| jusqu'à 2 | **450 €** |
| jusqu'à 4 | **500 €** |
| jusqu'à 6 | **550 €** |
| jusqu'à 8 | **600 €** |

- **Inclus** : catamaran privé, capitaine, diesel, annexe pour le transfert, fruits frais, vin blanc, bière, softs, jus, eau plate, arrêt baignade au Blue Lagoon, coucher de soleil au retour. Le texte d'accroche parle de « Prosecco », qui n'apparaît pas dans la liste des inclusions.
- **Absente de DOL** (aucune mention du sunset). Côté SW, elle n'apparaît que dans les titres de menu.

### 2.4 Voilier — journée « Yachtsailing Sailboat Daytrip to Blue Lagoon » (SW, DOL)
- **Bateau** : voilier monocoque, **modèle et nom non indiqués**. WC à bord, grand bain de soleil à l'avant, taud à l'arrière, 2 « balcony seats » au-dessus de l'eau. Les passagers peuvent participer à la manœuvre.
- **Durée** : 6 h, **horaires non indiqués**.
- **Prix** :
  - **Privé** : **750 € pour 2 personnes**, puis **+25 € par personne supplémentaire**.
  - **Partagé** : **150 € par personne**, groupe de **6 personnes maximum**.
- **Inclus** : yacht, diesel, capitaine, déjeuner (« light lunch ») et boissons (vin blanc, bière, softs, eau), masques de snorkeling. **La version DE ajoute le stand up paddle**, absent en EN, FR et DOL.
- **Itinéraire** : côte est de Rhodes et Lindos → Blue Lagoon (baignade et snorkel) → retour le long de Pefkos jusqu'à Lardos. Dauphins possibles.
- **Disponibilité** : « until 25th September 2026 » (EN et DE). Pas mentionnée en FR ni sur DOL.
- **Variantes annoncées sans prix** : la page EN parle de « sunset cruise or private Sail Training », la page FR de « coucher de soleil ». Aucun tarif voilier-sunset n'existe nulle part.
- **FR** : pas de formule partagée, ajoute « optimal 2-4 P », et la liste des inclusions est dupliquée (doublon tronqué).

### 2.5 Speedboat / Motoryacht — « Tour Deluxe extra » 4 h (SW, DOL)
- Nom : « Perfect Mood Trip to Lindos », privé (les clients et le skipper seuls à bord).
- **Prix** : **640 € par bateau pour 2 personnes**, **+20 € par personne supplémentaire**, **8 personnes maximum**. Le texte parle de « price per **Motoryacht** ».
- **Inclus** : fruits frais, déjeuner léger, toutes les boissons, équipement complet de snorkeling, paddleboard.
- **Itinéraire** : Blue Lagoon, Grand Canyon, Rockwall Caves, cliff jumping, dauphins possibles à Cave Island, criques isolées, Lindos.
- **Public** : couples, familles avec enfants **y compris bébés**, amis. Groupes sur demande.
- Prolongeable jusqu'à 6 h (« flexible in time and content »), **prix de l'extension non indiqué**.

### 2.6 Speedboat — « Tour Deluxe » 2,5 h (SW uniquement)
- **Prix** : **400 € par speedboat pour 2 personnes**, **+20 € par personne supplémentaire**, **4 personnes maximum**.
- **Inclus** : équipement de snorkeling complet et bouteilles d'eau. Même itinéraire, en version courte.
- **Absent de DOL.**
- Les capacités (8 contre 4) et les mentions « Motoryacht » / « Speedboat » laissent penser à **2 bateaux différents**. Ce n'est expliqué nulle part et aucun modèle n'est nommé.

### 2.7 Sports nautiques — « Watersports & Prices 2026 » (SW, en EN, DE et FR)
| Activité | Détail | Prix |
|---|---|---|
| Windsurf : cours débutant | 1 h, 1 personne | 55 € |
| Windsurf : cours de 3 h | libellé « 3-hour course **1 hour** 1 pers. » (erreur en EN et DE, correct en FR) | 135 € |
| Windsurf : cours de base de 8 h | 1 personne | 280 € |
| Licence windsurf WWS | frais | 40 € |
| Location planche et voile | 1 h | 30 € |
| Engins tractés (Sofa, Ringos, Flyer, Banana) | 10 min par personne | 20 € |
| Ski nautique / wakeboard : cours débutant | 40 min maximum | 70 € |
| Ski nautique / wakeboard : remise à niveau | 25 min maximum | 55 € |
| Tour de bi-ski | 10 min maximum | 40 € |
| Tour de mono-ski | 10 min maximum | 50 € |
| Jetski 110 ch, 1 ou 2 personnes | 15 min | « 45 / 50 € » (probablement 1 pers. / 2 pers., **non explicité**) |
| Stand up paddle avec initiation | 1 h par personne | 20 € |
| Kayak simple ou double | 1 h | 15 € (sans distinction simple/double) |
| Cours de voile privé sur yacht | 4 h, cours particulier (FR : « débutants ou avancés ») | 480 € |

- **Conditions annoncées** : windsurf avec moniteur, matériel et bateau d'accompagnement, 1 à 2 personnes par heure maximum. Ski nautique et wakeboard avec perche d'apprentissage, combinaison néoprène, gilet et eau inclus.
- **Absent de CAT et de DOL.**

### 2.8 Informations absentes des 3 sites (toutes langues)
- **Prix enfants** : aucun. Les prix sont par bateau ou par adulte, et aucun âge minimum n'est indiqué.
- **Politique d'annulation**, en particulier en cas de **météo** ou de **meltem** : rien.
- **Solde de paiement** (espèces, carte à bord ?) : rien.
- **Horaires** du voilier et du speedboat : non indiqués.
- **Âge et permis** pour le jetski : rien.
- **Langues parlées à bord** : non indiquées. On peut supposer DE et EN (équipe allemande), sans confirmation sur les sites.
- **Accès et parking** de la station : seulement « next to Aulus Lindos Rhodes Resort ».

---

## 3. Informations entreprise

- **Marques** : « Sabinas Watersport Rhodos » (centre nautique), « Catamaran Yachtsailing Rhodos » (située « @ Sabinas Watersport Rhodos ») et « Dolphin Tours Rhodos ». Selon DOL, cette dernière est une « cruise company » **créée en 2023** qui coopère avec Sabinas Watersport.
- **Équipe** : **Sabina / Sabine Kuehl** (de Kiel) et **Roland** (de Leipzig), Allemands. Ils se sont rencontrés en 2001 dans « un petit village d'Allemagne de l'Est ». Ils exploitent la station **depuis 2007**. CAT dit « 20 years ago », soit environ 2006.
  - **Sabina** : responsable de la station, monitrice de windsurf et de voile, monitrice de ski nautique et wakeboard. Elle a passé « many winters » comme manager de centres nautiques dans des resorts 5* et 6* aux **Maldives**.
  - **Roland** : capitaine du speedboat, **RYA Offshore** Captain, technicien de la station (« Mac Giver »). Il a dirigé auparavant son propre hôtel-restaurant dans l'Erzgebirge (DE).
- **Mission (CAT)** : « Joy and fulfillment… If you say "The Catamaran daycruise was the highlight of our vacation!" then we have achieved our goal ».
- **Flotte connue** :
  - catamaran Fountaine Pajot Lavezzi 40 « THOI » (8 passagers) ;
  - un voilier monocoque (non nommé, 6 passagers maximum) ;
  - une « Motoryacht » (8 passagers maximum) et un « Speedboat » (4 passagers maximum), sans modèle. Les photos montrent un bowrider blanc et bleu à taud, capable d'embarquer 6 à 8 personnes (assets S1/S2), un petit bowrider jaune et un open blanc à taud noir (photos de Roland à la barre).
  - matériel de sports nautiques : jetski 110 ch, windsurfs, ski, wake, SUP, kayaks, engins tractés.
- **Contacts** :
  - mobile **+30 697 259 3276** (aussi WhatsApp selon DOL) ;
  - WhatsApp **+49 176 31707126** ;
  - e-mail **sabine.kuehl@web.de** sur SW et CAT (adresse webmail personnelle, masquée par Cloudflare) ;
  - **info@dolphin-tours-rhodos.com** sur DOL.
- **Réseaux** : Facebook `facebook.com/boattripsrhodes` · Instagram `@sabinas.watersport` (lien sur DOL uniquement) · TripAdvisor : fiche « Sabinas Watersport Rhodos » `d8323947`, avec un widget « TA_excellent » sur SW et CAT. Le lien TripAdvisor de CAT pointe vers `tripadvisor.de/` (page d'accueil, **lien cassé fonctionnellement**).
- **Saison** : sur place de mai à octobre, joignable en ligne toute l'année (DOL).
- **Mentions légales** :
  - SW et CAT : pas de page Impressum réelle. `/about/` affiche l'adresse et l'e-mail plus le bloc publicitaire Jimdo. Seul le footer « All copyrights reserved by Sabine Kuehl 2026 » identifie l'exploitante.
  - DOL : un « Imprint 2026 » existe, mais sans raison sociale.
  - **Aucune raison sociale, aucun n° AFM/TVA, aucun n° de licence** (EOT/MHTE, capitainerie, licence de bateau de tourisme) sur aucun des 3 sites.
  - **Privacy Policy** (SW, CAT) : texte Jimdo standard (Google Analytics 4, reCAPTCHA, statistiques Creator). Le responsable du traitement n'est pas identifié.
  - **Withdraw contract** : formulaire Jimdo standard « 14 jours », alors que le droit de rétractation ne s'applique pas à une prestation de loisirs à date fixe.

---

## 4. Parcours de réservation actuel

1. **Découverte** : sur SW, « Click pictures below for prices 2026 » mène à des photos. Pour le catamaran, le clic **quitte le site vers CAT**. Sur la page d'accueil FR, la vignette « Excursions privées en Bateau » pointe vers `maritime-excursion.com`, **domaine mort (DNS ne résout pas)**.
2. **Prix** : en texte, sur des pages différentes selon le produit et le domaine (voir §2).
3. **Demande de réservation**, le seul canal de « réservation » :
   - **Formulaire Jimdo SW** (EN, DE et FR, mais libellés des champs en anglais partout) : `Name`, `Mobile Number`, `Email` (champ texte, sans validation e-mail), `Message`, bouton « send ». Mention « Please fill out the fields marked with an asterisk ». La Privacy Policy mentionne reCAPTCHA.
   - **Formulaire Jimdo CAT** : `Name`, `E-Mail`, `Mobile number with area code` (ou « Phone with area code » sur la page Rates), `Message`. On le trouve sur les pages booking-request **et** en bas des pages Rates (EN, DE, FR). La mention RGPD est en allemand (« Es gilt die Privacy Policy ») sur les pages EN et FR.
   - **DOL** : pas de formulaire. Liens « Booking request » vers la page Contact (téléphone et WhatsApp `wa.me/4917631707126`).
   - **Aucun champ structuré** : ni date, ni produit, ni nombre d'adultes et d'enfants, ni hôtel. Tout passe par le message libre.
   - **Aucun calendrier de disponibilité**, aucun prix calculé en ligne.
4. **Échange manuel** par e-mail, téléphone ou WhatsApp avec Sabina.
5. **Acompte** :
   - pages « Deposit payment » sur **SW (EN uniquement)** et **CAT (EN uniquement)**, non liées depuis DE et FR ;
   - bouton **PayPal Hosted Button** à prix fixe, **150,00 € EUR** (vérifié via l'API PayPal `ncp/api/form-fields`) ;
     - SW, bouton `K6GU3EWMWGVS6` : « Deposit payment for Catamaran daycruise or sunset cruise, Sailboat cruise, Speedboat or Motoryacht tour » ;
     - CAT, bouton `QK73TVC6F342Y` : « Deposit private Catamaran daycruise or sunset cruise » ;
   - paiement par PayPal ou carte via PayPal (meta description de CAT : « Easy payment … by Paypal or Creditcard ») ;
   - **aucun texte sur la page** pour expliquer l'acompte : rien sur le montant restant dû, le moment ou le moyen de régler le solde, le remboursement ou l'annulation. La page SW n'affiche qu'une galerie de 5 photos, le bouton et les blocs habituels.
6. **Solde** : jamais mentionné.

---

## 5. Incohérences et erreurs relevées

### Entre sites
| Sujet | SW | CAT | DOL |
|---|---|---|---|
| Catamaran semi-privé 160 €/pers | absent | présent | **absent** |
| Sunset catamaran 450–600 € | menu seulement | présent | **absent** |
| Voilier privé et partagé | 750 € / +25 € / 150 €, partagé absent en FR | — | idem SW |
| Speedboat 2,5 h à 400 € | présent | — | **absent** |
| Sports nautiques | présent | — | absent |
| Inclusions voilier | DE : + SUP ; EN/FR : sans SUP | — | sans SUP |
| Repère d'adresse | « next to Aulus Lindos Rhodes Resort (and Glystra Beach) » | « next to Aulus Lindos Rhodes Resort » | Imprint : « next to **Lindian Village Resort** » ; footer : Aulus |
| E-mail | sabine.kuehl@web.de | sabine.kuehl@web.de | info@dolphin-tours-rhodos.com |
| Langues | EN, DE, FR | EN, DE, FR partiel (pas de page sunset dédiée, pas d'About, pas de deposit) | EN seul |
| Dauphins | « Dolphins maybe at Cave Island » | « with some luck… dolphins » | domaine « dolphin-tours » mais « NO specific dolphin watching tours! » |

### À l'intérieur d'un même site
- **Prénom** : « Sabina » sur SW, « Sabine » sur CAT (About).
- **Ancienneté** : « since 2007 » contre « 20 years ago » (CAT).
- **Saison du sunset** : « end of May » (EN) contre « May » (DE, FR).
- **Catamaran sur CAT** : l'accueil liste « fuel, captain, host/ess, lunch, all drinks, snorklemasks, paddleboard », la page Rates ajoute snack d'accueil, annexe et jouets aquatiques. L'accueil dit « toilet », la page Photos dit 2 WC.
- **Phrase tronquée en FR** : « … sur notre catamaran de 40 pieds dans » (phrase interrompue).
- **Capacité et unité du speedboat** : on lit « per Motoryacht » (8 personnes) puis « per Speedboat » (4 personnes) sans explication. DOL titre « Private Speedboat Excursion » mais facture « per Motoryacht ».
- **Erreur de libellé** : « 3-hour course 1 hour » (windsurf, EN et DE).
- **Jetski « 45 / 50 € »** et **kayak simple/double** : prix ambigus.
- **Lien Google Maps** des pages booking SW : requête « Sabinas+**Ratersport**+Rhodos » (faute de frappe).
- **Footer CAT** : « www.dolphin-tours-rhodos.**con** » (faute de frappe).
- **Coquilles** (échantillon) :
  - EN : « menue », « snorklemasks », « crystall », « paddelboard », « cayak », « Neoprenwest », « Individuell », « ar the 2 lofty balcony seats », « exteriour » ;
  - DE : « Sailttraining » ;
  - FR : « tout la jounee », « Demander de reservation », « vin blanche », « Vouz » ;
  - DOL : « Booking requesr », « spectaculur », « dinghi ».

---

## 6. Audit technique rapide

| Critère | SW | CAT | DOL |
|---|---|---|---|
| CMS | Jimdo Creator | Jimdo Creator | Jimdo Dolphin |
| Poids de l'accueil (HTML + CSS + JS + images, hors iframes et tiers chargés en JS) | **~1,3 Mo**, ~17 requêtes ; HTML 63 Ko | **~1,4 Mo**, ~13 requêtes ; HTML 146 Ko | ~0,84 Mo, ~5 requêtes ; HTML 45 Ko, mais un bundle JS de 759 Ko |
| Plus gros fichier | `google_map_placeholder.png` **716 Ko** (sur toutes les pages, à cause du bloc Maps dans le footer) | idem | renderer JS 759 Ko |
| Scripts dans le HTML | 28–29 balises `<script>`, GA4 `G-V5Z7BT48QN` + UA legacy | 26–28, GA4 `G-ZNNN13THTP` | 5 |
| Embeds | 3 YouTube + 1 vidéo Facebook + Google Maps sur **chaque page** (sidebar) | 4 YouTube + Maps + Powr.io + widget TripAdvisor sur chaque page | YouTube + Maps (consentement) |
| Consentement | YouTube et Maps bloqués avant consentement, mais **l'iframe vidéo Facebook est chargée directement** (`src=`, pas `data-src`), avant tout consentement | YouTube, Maps et Powr bloqués | OK |
| `<title>` | **150–400 caractères** : suffixe de site imposé « … / Watersports Lardos Rhodes / **Hilton / Domes Aulus Rhodes / Amoh Pefkos / Lindos Imperial / Mayia Kiotari** » (bourrage de mots-clés avec noms d'hôtels concurrents ou voisins), titre de l'accueil dupliqué | ~200 caractères : « Best Catamaran tour experience… » répété 2 fois sur l'accueil | courts : « Prices \| https://www.dolphin-tours-rhodos.com » (URL dans le titre) |
| Meta description | **16 pages sur 23 vides** (toutes les pages produits EN, DE et FR) | 18 sur 18 renseignées | 6 sur 7 |
| `lang` / hreflang | `lang="en-US"` sur **toutes** les pages, DE et FR compris ; **aucun hreflang** | idem | `lang="en"` ; pas de hreflang |
| OG / Twitter | présents (générés par Jimdo). **Même og:image partout** : photo de Sabina devant la cabane, 2592×1944 | présents ; og:image = baie de Lindos | présents ; og:image recadré 576 px |
| schema.org | **aucun** | **aucun** | 1 JSON-LD **avec `"@type":""` vide** (invalide) |
| sitemap.xml | OK, 23 URL | OK, 18 URL | OK, 4 URL |
| robots.txt | OK (Disallow /app/ et /j/, Crawl-Delay 5, AhrefsBot et MJ12bot bloqués) | idem | minimal, mal formé (« Allow: /User-agent: * » sur une seule ligne) |
| Alt des images | **~80 % vides** (8 sur 10 sur l'accueil). Le logo a pour alt le titre de site complet (bourrage) | idem (8 sur 10 vides) | 100 % vides |
| Viewport mobile | oui (`width=device-width, initial-scale=1`) | oui | oui |
| Images | originaux jusqu'à 6240×4160 (8,4 Mo pour la photo speedboat) servis via `srcset` jimcdn, donc acceptable côté rendu | idem, originaux 6000×4000 (7 Mo) | CDN Cloudflare `format=auto` |
| Contenu dupliqué | 3 pages catamaran sans contenu (photo et lien seulement) ; textes About repris sur 3 domaines | — | textes copiés depuis SW et CAT (duplicate content entre domaines) |
| Liens cassés | `maritime-excursion.com` (FR), lien TripAdvisor CAT vers la racine du site | | |

---

## 7. Synthèse des problèmes majeurs (contenu)
1. **Offre éclatée** sur 3 domaines et 7 arbres de langue. Aucun site ne présente le catalogue complet, et les prix diffèrent par omission : semi-privé, sunset et speedboat 2,5 h absents de DOL.
2. **Aucune condition de vente** : annulation, météo, solde, enfants, âge. Ce manque est critique pour une activité dépendante du vent.
3. **Acompte de 150 € fixe** via PayPal, quel que soit le produit (950 € ou 400 €), **sans aucune explication** sur la page, et accessible en EN uniquement.
4. **Réservation = formulaire libre à 4 champs** : pas de date, de produit, ni de nombre de personnes. Toute la qualification se fait à la main.
5. **Légal** : pas d'Impressum ni de raison sociale, AFM ou licence ; Privacy Jimdo générique ; vidéo Facebook chargée sans consentement.
6. **SEO** : titres bourrés de noms d'hôtels, `lang` faux sur DE et FR, pas de hreflang ni de schema (alors que `TouristTrip`, `LocalBusiness`, `Offer` s'y prêtent), 16 meta descriptions vides sur SW, alt vides.
7. **Confiance** : widget TripAdvisor « Excellent » présent, mais aucun avis client en texte sur les sites. La flotte (hors catamaran) n'est ni nommée ni décrite.
