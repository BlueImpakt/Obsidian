---
tags: [project-doc, sabinas-watersport]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: GitHub/sabina-watersport-refonte/docs/03-walkthrough-cro.md
---

↩ [[sabinas-watersport-refonte]]

# 03 — Walkthrough cognitif CRO : Sabinas Watersport Rhodos (existant)

> **Ce document est une simulation qualitative, pas une preuve statistique.** Les réactions des personas sont des hypothèses fortes, construites sur l'ordre réel des blocs, le texte réel et le rendu mobile réel des pages. Il faut les confirmer avec des données : analytics, demandes reçues par formulaire/WhatsApp, et 3 à 5 tests utilisateurs. Elles servent à argumenter la refonte et à cadrer la maquette, pas à prédire un taux de conversion.

**Relevé effectué le 21/10/2026.**
- Récupération HTML (curl, user-agent iPhone) des 3 sites. dolphin-tours-rhodos.com a répondu en 200 avec un UA mobile ; voir aussi `research/dolphin-tours-rhodos.md`.
- Rendu dans le navigateur intégré en viewport mobile (375×812, équivalent iPhone), cookies non essentiels refusés : c'est le choix le plus probable sur mobile et le plus défavorable au site.
- Positions verticales mesurées dans le DOM : 1 écran ≈ 812 px.
- Les personas sont placés **en pleine saison (juillet)**. Le sunset cruise n'est proposé que de fin mai à mi-septembre, et Sabina n'est sur place que de mai à octobre.

---

## 1. Ce que le visiteur rencontre réellement (cartographie)

### 1.1 Trois sites, une seule entreprise

| Domaine | Ce que Google promet (title) | Ce qu'on trouve | CMS |
|---|---|---|---|
| sabinas-watersport.com | Title de ~300 caractères bourré de mots-clés : « Private Catamaran Daytrip, Boat tours /Sailboat /Snorkel Trip / Watersports Lardos Rhodes / Hilton/ Domes Aulus Rhodes/ Amoh Pefkos/ Lindos Imperial / Mayia resort Kiotari » | Hub généraliste : sports nautiques, speedboat, voilier. Les prix catamaran renvoient vers l'autre domaine. | Jimdo Creator |
| catamaran-yachtsailing-rhodos.com | « Best Catamaran tour experience in Rhodes - exclusive & private boat cruise » | Mono-produit catamaran : journée privée, demi-privée, sunset | Jimdo Creator |
| dolphin-tours-rhodos.com | « Exclusive Boat tours & Catamaran cruises in Rhodes » | Les mêmes bateaux, une 3e marque, et l'avertissement « NO specific dolphin watching tours! » | Jimdo Dolphin |

Les noms des hôtels (Aulus, Lindos Imperial, Mayia Kiotari…) servent d'aimant SEO dans les titles. **Aucune page ne reprend ce lien hôtel → plage une fois le visiteur arrivé.** La pertinence est promise dans Google, puis abandonnée sur la page.

### 1.2 Home sabinas-watersport.com, ordre réel sur mobile (~4,6 écrans)

| Écran | Contenu |
|---|---|
| 0 | **Modale cookies plein écran** (EN), qui masque tout. Trois boutons de même poids : Accept all / Accept only selected / Reject all. |
| 1 | Burger menu (21 entrées EN+DE+FR dans un seul menu déroulant) · photo : Sabina dans la boutique de location, avec un sticker émoji « pouce » et « WELCOME » en orange italique · « Welcome 2026 at SABINAS WATERSPORT RHODOS » · 4 lignes d'offres en bleu italique · « * * * * * * * » · paragraphe d'accroche. **Aucun bouton, aucun prix, aucun avis.** |
| 1→2 | « Click Pictures below for Prices 2026 » · bouton noir « Booking request », juste sous la ligne de flottaison · 4 photos sans prix superposé (« Catamaran trip prices click photo », « Sailboat cruise click photo », « Boat tour prices click photo », « Watersports prices click photo »). La 1re photo fait **changer de domaine** sans prévenir. |
| 2→3 | Logo TripAdvisor (sans note ni nombre d'avis) · bloc répété « Exclusive and private… » + 2e « Booking request » · **3 grands blocs gris « Youtube content is not displayed due to your cookie settings »** · une vidéo Facebook |
| 3→4 | Footer « Info & Booking » : adresse, « next to Aulus Lindos Rhodes Resort », email, puis **2 numéros différents** (WhatsApp +49 allemand, mobile +30 grec) **en texte brut, sans lien `tel:` ni `wa.me`** · carte Google bloquée par les cookies · boutons de partage LinkedIn/Xing |

### 1.3 Home catamaran-yachtsailing-rhodos.com, ordre réel sur mobile (~8,2 écrans)

| Écran | Contenu |
|---|---|
| 0 | **Modale cookies en allemand** (« Diese Website verwendet Cookies… ») sur la version anglaise du site |
| 1 (0–812) | Photo du rocher de Lindos (le catamaran y est minuscule) · logo flou · H1 « Exclusive & luxury Catamaran Day tour & Sunset cruise in Rhodos/Rhodes » · « catamaran-yachtsailing-rhodos.com » · « Our trips » · « English / Deutsch / Francais > menue » · début d'une belle photo de catamaran dans l'eau turquoise. **Ni prix ni CTA.** |
| 2 (812–1624) | « Day Cruise to Blue Lagoon » · **Private Tour 6 h, from 950 €** · inclus · bouton violet « Rates private tour 2026 » (y≈1244) · **Half-private Tour 6 h, 160 €/pers, max 8** (y≈1368) · début de « Tour Info » |
| 3 (1624–2436) | Longue prose sur l'itinéraire (Cave Island, Lindos, Blue Lagoon, déjeuner, filet avant) |
| 4 (2436–3248) | « Contact: » email + téléphone en gras, non cliquables (y≈2617) · « Booking request » · « The perfect frame for your honeymoon, birthday, wedding… » · **Private Catamaran Sunset cruise** (y≈2942) **sans prix** · bouton « Booking request - Private Catamaran Sunset cruise » |
| 5–6 | Galerie de 3 photos · logo TripAdvisor qui pointe vers **tripadvisor.de (page d'accueil, pas la fiche)** · widget Powr.io bloqué · **4 blocs gris YouTube** (y≈4544 →) |
| 7–8 | « Info & Location » · WhatsApp +49 et mobile +30 en texte brut (y≈5918) · faute de frappe « www.dolphin-tours-rhodos.**con** » · carte bloquée |

Sous-pages clés :
- **Rates 2026** : 950 / 1 050 / 1 150 € selon le nombre de personnes, mais **pas de demi-privé** (incohérent avec la home), puis un formulaire.
- **Sunset** : privé uniquement, 3 h, 17h–20h, 450 € (2 pers.) → 600 € (8 pers.), « only available from end of May until mid of September ».
- **Booking request** : formulaire **Nom / E-mail / Mobile / Message**. Pas de date, pas de choix d'activité, pas de nombre de personnes. Mention « Es gilt die Privacy Policy » en allemand sur les pages EN et FR. Aucun délai de réponse annoncé.
- **Deposit payment** : une photo et un bouton PayPal. **Aucun montant d'acompte, aucune condition d'annulation, aucune politique météo** n'est écrit sur aucun des 3 sites.
- **About** : Sabine & Roland, Allemands, sur place depuis 2007, Sabine ex-manager de centres nautiques 5–6★ aux Maldives, Roland « Captain RYA Offshore ». **C'est le meilleur actif de confiance de l'entreprise, et il est enterré dans « About us ».**
- **Version FR** : le menu catamaran FR n'a **pas de page sunset dédiée** (les prix sunset sont dans « Tarifs 2026 »). Traduction automatique visible : « dériveur pour le transfert à terre » pour *dinghy*, « Excursion en voilier tout la jounee ». Pas de version italienne.

### 1.4 dolphin-tours-rhodos.com
C'est le template le plus propre : vraie photo drone en hero, téléphone dans l'en-tête. Mais **le numéro de l'en-tête pointe vers la page d'accueil (`href="/"`) au lieu d'appeler.** Les boutons « Prices & Book… » mènent à une page Prices, puis à une page Contact **sans formulaire**, avec carte bloquée et un seul vrai lien `wa.me` (le seul des 3 sites). Le nom de domaine promet des dauphins que la page dément aussitôt.

### 1.5 Constats techniques transverses
- **0 lien `tel:`** sur les 3 sites. **1 seul lien WhatsApp** cliquable (page Contact de dolphin-tours).
- Après refus des cookies, **7 à 8 blocs gris** d'avertissement remplacent les vidéos et les cartes. Sur mobile, ils occupent l'équivalent de 1,5 à 2 écrans.
- Images sans `alt` et nommées `image.jpg`. Galerie catamaran datée de 2017 (horodatage des fichiers).
- Aucune note ni aucun nombre d'avis affiché nulle part. Pourtant, une recherche montre que le catamaran privé est distribué ailleurs avec des avis très positifs : fiche Expedia/Travelocity affichant **9,8/10**, Click&Boat **4,9/5**. Chiffres à revérifier avant usage.
- Incohérences d'adresse : « next to Aulus Lindos Rhodes Resort » (footers) contre « next to Lindian Village Resort » (Imprint dolphin).

---

## 2. Persona 1 : Jens & Katrin, couple allemand, anniversaire de mariage

```
PERSONA PROFILE
Nom :              Katrin (41, F) tient le téléphone ; Jens (43, M) lit par-dessus l'épaule
Nationalité :      Allemande (Munich), anglais correct, préfère lire en allemand
Situation :        10 ans de mariage, séjour à l'Aulus Lindos (adults only), J-2 avant l'anniversaire
SEARCH CONTEXT
Requête Google :   "catamaran Rhodes private"
Source :           Google organique, 1er résultat naturel → catamaran-yachtsailing-rhodos.com
Vus avant :        2 annonces Google Ads de grosses flottes à Rhodes-ville, une fiche GetYourGuide
Device :           iPhone 14, 22h30, wifi de l'hôtel, sur le balcon
PSYCHOLOGY
Familiarité :      Faible avec la région, moyenne avec les excursions en bateau
Urgence :          Élevée : veut une réponse ce soir ou demain matin pour après-demain
Peurs :            Bateau bondé, « privé » qui ne l'est pas, pas de réponse à temps, paiement à un inconnu
Déclencheurs :     Prix clair TTC, conditions écrites, avis, interlocuteur identifiable (allemand = bonus)
Style de décision: Rapide si les cases sont cochées, sinon passe au suivant
Attachement :      Sécure (Katrin) : fait confiance si les bases sont là
GOAL
Succès :           Un catamaran privé confirmé pour après-demain, journée ou coucher de soleil
Seuil de contact : Prix + « dispo après-demain ? » réglable en 1 message WhatsApp
```

### Phase 0 : avant l'arrivée
> « Bon, c'est notre anniversaire après-demain, il nous faut un truc spécial. Pas un bateau de 60 personnes avec de la musique à fond. Un catamaran juste pour nous deux, un verre de vin, la baignade. Le budget n'est pas le problème, le problème c'est que c'est dans deux jours. Je veux savoir ce soir si c'est possible. »

**Contrat de pertinence :** en 3 secondes, la page doit dire *catamaran privé + près de Lindos + prix + réservable rapidement*.

### Phase 1 : test des 5 secondes
Ce qui s'affiche d'abord est la **modale cookies en allemand**. Pour Katrin, c'est presque un bon signe (« ah, c'est allemand ? »). Après le clic sur « Reject all », elle voit le rocher de Lindos et un H1 en blanc sur photo.

| Question | Réponse | Verdict |
|---|---|---|
| Qu'est-ce que c'est ? | « Catamaran de luxe à Rhodes. » | OUI, le H1 est explicite |
| Est-ce pour moi ? | « Privé ? Le H1 dit "exclusive & luxury", pas "private". Près de mon hôtel ? Aucune idée. » | PARTIEL |
| Que dois-je faire ? | Aucun bouton. Seulement « English / Deutsch / Francais > menue ». | **NON : constat critique** |

### Phase 2 : défilement

**Écran 1, hero**
> « Joli, Lindos. Mais où est le bateau ? Ah, ce petit point blanc. "English / Deutsch / Francais > menue"… il faut ouvrir le menu pour l'allemand ? Pas grave, on lit l'anglais. On descend. »

```
ANALYSTE — Écran 1
État émotionnel : curieuse
Delta confiance : = (la langue DE du bandeau cookies rassure un peu, le logo flou et la photo sans bateau neutralisent)
LIFT :            Clarté OK, Pertinence partielle (« private » absent du H1), Urgence nulle
Cialdini actifs : aucun
Cialdini manquants : Preuve sociale (note), Unité (« wir sind Deutsche », totalement absent)
Fogg :            M haute | A moyenne | Prompt visible : NON
CTA atteignable : NON
Technique :       modale cookies en DE sur une page EN ; logo pixellisé
```

**Écran 2, offre et prix**
> « Ah voilà : "Private Tour 6 hours, from 950 €". Déjeuner bio, boissons, paddle, tout compris. OK, c'est cher mais c'est clair, et c'est privé. "Half-private 160 € par personne"… non, on veut être seuls. "From 950" : c'est pour combien de personnes ? On est deux. Je clique sur "Rates". »

```
ANALYSTE — Écran 2
État émotionnel : rassurée
Delta confiance : ↑ prix public, contenu de la prestation détaillé
LIFT :            Proposition de valeur ↑ (tout inclus), Anxiété ↓ partielle
Cialdini actifs : Autorité légère (détail du service)
Cialdini manquants : Preuve sociale, Rareté (aucune notion de disponibilité)
Fogg :            M haute | A moyenne | Prompt : oui (« Rates private tour 2026 »), mais il mène à plus d'info, pas à une réservation
CTA atteignable : un bouton d'info, pas un bouton de réservation
```

**Page Rates 2026 (premier clic)**
> « 950 € jusqu'à 4 personnes, OK, on est deux, c'est 950. 10h30–16h30. Et maintenant ? Un formulaire : nom, email, téléphone, message. Pas de date ? Je dois écrire "après-demain, 2 personnes, anniversaire" dans le message ? Et elle répond quand ? Ce soir ? Dans trois jours ? Et le sunset dont parlait la page, il coûte combien ? Pas ici. »

```
ANALYSTE — Rates
État émotionnel : hésitante
Delta confiance : ↓ formulaire générique, aucun délai de réponse, aucune disponibilité
LIFT :            Anxiété ↑↑ (« aurai-je une réponse à temps ? »), Urgence non exploitée
Cialdini manquants : Engagement (aucun petit pas : choisir une date, un créneau)
Fogg :            M haute | A FAIBLE (tout doit être rédigé à la main) | Prompt : bouton envoyer
Technique :       mention « Es gilt die Privacy Policy » en allemand ; erreurs de validation en allemand
```

**Retour home, écran 4 : le sunset**
> « "Private Catamaran Sunset cruise… glass of Prosecco"… ça, c'est exactement notre anniversaire ! Combien ? Pas de prix. Encore un bouton "Booking request". Je ne vais pas envoyer deux formulaires. Il y a un téléphone en gras, mais je ne peux pas cliquer dessus. Et appeler à 22h30 un numéro grec… non. »

**Écrans 5 à 8**
> « Des photos… un logo TripAdvisor, je tape dessus : ça m'envoie sur la page d'accueil de TripAdvisor ?! Où sont les avis ? Puis quatre cases grises "Youtube content is not displayed"… ça fait site cassé. Tout en bas, un WhatsApp… avec un numéro allemand, +49 ? C'est qui, en fait ? Je dois le copier dans WhatsApp à la main. »

```
ANALYSTE — Écrans 5–8
État émotionnel : frustrée puis méfiante
Delta confiance : ↓↓ lien TripAdvisor vers la home (signal de site abandonné), blocs gris, numéro +49 inexpliqué
LIFT :            Anxiété ↑, Distraction ↑ (partage LinkedIn, Powr bloqué)
Cialdini manquants : Preuve sociale (ici elle se retourne contre le site), Sympathie (aucun visage de Sabine/Roland sur la home), Unité (des Allemands depuis 2007, et le +49 deviendrait un atout au lieu d'une source de doute)
Fogg :            M en baisse | A faible | Prompt : WhatsApp présent mais non cliquable
CTA atteignable : NON
```

### Phase 3 : verdict
> « Le bateau a l'air super et le prix est honnête. Mais je ne sais pas s'ils ont de la place après-demain, je ne sais pas qui va me répondre ni quand, et je n'ai pas un seul avis sous les yeux. GetYourGuide, lui, me dit "disponible jeudi, annulation gratuite" en deux clics. Je vais faire une capture d'écran du prix, envoyer un WhatsApp à moitié par principe… et réserver l'autre en attendant. »

```
VERDICT — Persona 1
Confiance : 5/10 · Clarté : 7/10 · Pertinence : 8/10
Contacterait : PEUT-ÊTRE (WhatsApp tapé à la main, en parallèle d'une réservation OTA ; risque élevé de perte)
Forces :      1. Prix public du privé + détail du tout-inclus (LIFT Valeur)
              2. Positionnement occasion spéciale explicite (LIFT Pertinence)
              3. Cookies en DE : un signal Unité accidentel
Faiblesses :  1. Aucune disponibilité ni délai de réponse alors que l'urgence est forte (Fogg Ability, LIFT Anxiété)
              2. Aucun avis visible ; lien TripAdvisor cassé (Cialdini Preuve sociale)
              3. WhatsApp et téléphone non cliquables, en bas de page (Fogg Prompt)
Presque partie : page Rates, devant un formulaire sans date ni délai de réponse
Plus engagée :  écran 2, « Private Tour 6 hours from 950 € – all included »
```

**Ce qui l'aurait convertie :**
- un bouton WhatsApp collant qui pré-remplit « Private catamaran, [date], 2 pers., anniversary » ;
- « Antwort meist innerhalb von 2 Stunden » ;
- un mini-calendrier ou au moins « dernières dispos cette semaine » ;
- le prix du sunset à côté de celui de la journée ;
- « Abfahrt: Stafilia Beach, direkt neben dem Aulus » : le point de départ est **à côté de son hôtel**, et c'est enterré dans le footer de la page Booking ;
- une photo de Sabine & Roland avec « seit 2007 ».

---

## 3. Persona 2 : la famille Whitfield, britannique, 2 enfants (8 et 12 ans)

```
PERSONA PROFILE
Nom :              Claire (39, F) planifie ; Mark (41) valide le budget ; Ollie (12) veut de l'adrénaline ; Maisie (8) nage moyennement
Nationalité :      Britannique (Leeds)
Situation :        All-inclusive au Mayia/Kiotari, jour 4 sur 10, cherche « un truc à faire » une demi-journée
SEARCH CONTEXT
Requête Google :   "snorkelling trip Kiotari kids" puis "watersports Lardos"
Source :           Google organique → sabinas-watersport.com (le title cite « Mayia resort Kiotari »)
Vus avant :        Prospectus du rep TUI à l'hôtel (excursion bateau en groupe ~45 £/adulte), avis TripAdvisor d'un concurrent
Device :           Samsung milieu de gamme, 4G roaming, au bord de la piscine, en plein soleil
PSYCHOLOGY
Familiarité :      Faible (région), moyenne (activités nautiques)
Urgence :          Jours : cette semaine
Peurs :            Sécurité des enfants (gilets, âge minimum, mer agitée), coût caché, payer pour 4 et s'ennuyer
Déclencheurs :     Prix par personne/enfant, gilets fournis, moniteurs qualifiés, avis de familles, « kids from 6 »
Style de décision: Chercheuse méthodique, compare 3 options avant d'en parler à Mark
Attachement :      Anxieux (Claire) : a besoin d'être rassurée à chaque étape
GOAL
Succès :           Une demi-journée snorkeling/sport nautique sûre pour 4, budget ≈ 150–250 £
Seuil de contact : Prix total famille connu + « safe for an 8-year-old » écrit noir sur blanc
```

### Phase 0
> « Les enfants s'ennuient à la piscine. Ollie veut faire du jet-ski, Maisie veut voir des poissons. Il me faut un truc pas trop loin, pas hors de prix, et surtout sûr. Maisie ne nage pas encore super bien. Si je dois appeler quelqu'un pour savoir le prix, je laisse tomber : le rep de l'hôtel a un prospectus avec des prix. »

**Contrat de pertinence :** « watersports / snorkelling », « près de Kiotari », « enfants OK », un prix visible.

### Phase 1 : test des 5 secondes
Modale cookies plein écran → « Reject all ». Ensuite : photo d'une femme en débardeur fluo dans une boutique de location, un émoji pouce et « WELCOME » orange en italique.

| Question | Réponse | Verdict |
|---|---|---|
| Qu'est-ce que c'est ? | « Une école de sports nautiques ? Il y a aussi catamaran, speedboat, voilier… » | PARTIEL : 4 offres en vrac, aucune hiérarchie |
| Est-ce pour moi ? | « Rien sur les enfants, rien sur Kiotari dans ce que je vois. » | **NON** |
| Que dois-je faire ? | Aucun bouton visible | **NON : constat critique** |

### Phase 2

**Écran 1**
> « Bon, ça a l'air d'une petite affaire familiale, plutôt sympa. "Real, genuine, enthusiastic", OK. Mais c'est où, par rapport à nous ? Et combien ? On descend. »

```
ANALYSTE — Écran 1
État émotionnel : curieuse, prudente
Delta confiance : ↑ légère (Sympathie : une vraie personne) / ↓ (esthétique amateur, émoji, italique bleu)
LIFT :            Pertinence ↓ (aucun lien Kiotari ni famille), Clarté ↓ (4 offres sans hiérarchie)
Cialdini actifs : Sympathie (photo de Sabina), sans légende pour dire qui elle est
Cialdini manquants : Autorité (certifications, depuis 2007), Preuve sociale
Fogg :            M moyenne | A faible | Prompt : NON
CTA atteignable : NON (le premier « Booking request » est juste sous la ligne de flottaison)
```

**Écran 2 : « Click Pictures below for Prices 2026 »**
> « Il faut cliquer sur des photos pour voir les prix ? Bateau à voile… speedboat… le gamin sur les skis. "Watersports prices click photo". J'y vais. »

```
ANALYSTE — Écran 2
État émotionnel : légèrement agacée
LIFT :            Clarté ↓ (le prix est caché derrière une interaction sans indice visuel), Distraction ↑ (le lien catamaran change de domaine)
Fogg :            A ↓ (chaque prix coûte un clic plus un chargement en 4G roaming)
Technique :       aucune étiquette de prix ni de durée sur les vignettes ; zones tactiles = images entières, sans affordance de bouton
```

**Page Watersports & Prices**
> « Enfin des prix, en texte. Banane / ringo 20 € les 10 minutes par personne : ça fait 80 € pour 10 minutes à quatre… Jet-ski 45 € le quart d'heure. Ski nautique 70 €. Paddle 20 € de l'heure, kayak 15 €. OK, ça c'est raisonnable pour Ollie. Mais le snorkeling ? Rien ici. Et l'âge minimum pour le jet-ski ? Les gilets ? Il y a un moniteur ? Le ski, oui ("neoprene west"…), le reste, rien. »

```
ANALYSTE — Watersports Prices
État émotionnel : partagée (prix OK, sécurité absente)
Delta confiance : ↑ prix lisibles / ↓ aucune info sécurité, aucun âge minimum
LIFT :            Anxiété ↑↑ (peur n°1 non traitée), Valeur ↑
Cialdini manquants : Autorité (Sabina instructrice windsurf/voile/ski, Roland RYA Offshore : c'est sur une autre page), Preuve sociale (« families love… »)
Fogg :            M moyenne | A moyenne | Prompt : aucun bouton de réservation sur la page, seulement le bloc générique en bas
```

**Page Private Boat Tour (recherche du snorkeling)**
> « "Private Speedboat & Motoryacht Tour Deluxe"… speedboat avec Maisie ? "families with children (including babies)", ah, ça c'est rassurant. 2,5 heures, 400 € pour 2, plus 20 € par personne, max 4 : 440 € pour nous quatre. Le 4 heures, 640 € + 40 €. Pour du snorkeling ? Le rep de l'hôtel fait 45 £ par adulte. Et "cliff jumping" : Ollie va adorer, moi je vais faire une crise cardiaque. Il n'y a rien entre 80 € de banane et 440 € de bateau privé ? »

```
ANALYSTE — Private Boat Tour
État émotionnel : découragée
Delta confiance : ↑ « including babies », « 100% positive feedback » / ↓ écart de prix brutal, aucune option partagée pour familles
LIFT :            Valeur ↓ pour ce segment (le privé est un luxe qu'elle n'a pas cherché), Pertinence ↓
Cialdini actifs : Preuve sociale déclarative (« 100% positive feedback »), invérifiable
Fogg :            M ↓ | A moyenne | Prompt : « Booking request »
```

> Le voilier partagé (150 €/pers, 6 h, déjeuner compris), soit 600 € pour 4, existe mais se trouve sur une **3e page**, et rien n'indique un tarif enfant.

**Retour home, écrans 3–4**
> « Trois cases grises "YouTube"… une carte qui ne s'affiche pas. "Between Lindos and Kiotari, next to Aulus". C'est à combien en voiture ? On n'a pas de voiture. Il y a un transfert ? Rien. »

### Phase 3 : verdict
> « Ça a l'air d'être des gens bien, compétents. Mais je n'ai toujours pas de réponse à "est-ce que Maisie peut faire du snorkeling en sécurité, et combien ça coûte pour nous quatre ?". J'ai trois onglets, un prospectus du rep sur la table, et lui dit "children 4-11 half price, life jackets provided, hotel pickup". Désolée Sabina. »

```
VERDICT — Persona 2
Confiance : 6/10 · Clarté : 4/10 · Pertinence : 4/10
Contacterait : NON (au mieux, Ollie y va seul en jet-ski s'ils passent devant la plage)
Forces :      1. Prix des sports nautiques publiés en texte (LIFT Clarté sur la page dédiée)
              2. « including babies » / « families with children » (LIFT Anxiété ↓)
              3. Petite structure humaine, visible (Cialdini Sympathie)
Faiblesses :  1. Zéro information de sécurité (gilets, âges, encadrement, météo) : peur n°1 non traitée (LIFT Anxiété)
              2. Pas de produit snorkeling famille à prix intermédiaire ; trou entre 80 € et 440 € (LIFT Valeur/Pertinence)
              3. Prix cachés derrière des photos, sur 3 pages et 2 domaines (Fogg Ability)
Presque partie : page Private Boat Tour, devant « 400 € + 20 €/pers » et « cliff jumping »
Plus engagée :  page Watersports Prices (prix lisibles, activités pour Ollie)
```

**Ce qui l'aurait convertie :**
- une entrée « Familles » sur la home ;
- un bloc sécurité standard sur chaque fiche : gilets fournis toutes tailles, âge minimum par activité, moniteurs certifiés (avec les diplômes de Sabina et Roland), annulation météo gratuite ;
- un prix « famille de 4 » calculé ;
- un snorkeling partagé ou semi-privé, avec tarif enfant ;
- « 10 min en voiture de Kiotari, taxi ≈ X € » ou une solution de transfert ;
- 2 ou 3 avis de familles britanniques.

---

## 4. Persona 3 : Léa & Marco, jeune couple franco-italien, comparateur GetYourGuide

```
PERSONA PROFILE
Nom :              Léa (28, F, Lyon), Marco (30, M, Turin)
Situation :        Location à Pefkos, 7 jours, budget serré mais « une soirée spéciale » prévue
SEARCH CONTEXT
Requête :          GetYourGuide "sunset cruise Lindos" → a repéré l'opérateur, puis Google "sabinas watersport sunset cruise"
Source :           Recherche de marque (veut « éviter la commission de GYG »)
Vus avant :        Fiches GYG/Expedia : sunset partagé 1h30–2h à Lindos autour de 45–60 €/pers, « free cancellation 24h », 4,7★ (1 200 avis), photos de clients
Device :           iPhone 13 de Léa, 18h, terrasse d'un café
PSYCHOLOGY
Familiarité :      Moyenne (habitués des OTA)
Urgence :          Jours (cette semaine)
Peurs :            Payer plus cher qu'en OTA, arnaque au paiement direct, pas de recours si annulation
Déclencheurs :     Prix ≤ OTA ou avantage clair à réserver en direct, avis, annulation gratuite, paiement sécurisé
Style de décision: Chercheuse, compare onglet contre onglet
Attachement :      Évitant (Marco) : veut les faits, déteste le blabla ; Léa, entre sécure et anxieuse
GOAL
Succès :           Un sunset à 2, ambiance romantique, dans la limite de ~150 € pour deux
Seuil de contact : « Pourquoi en direct ? » + prix + annulation écrits
```

### Phase 0
> « Sur GYG, on a vu des couchers de soleil à Lindos autour de 50 € par personne. Marco dit qu'en réservant en direct, on paie moins et l'argent va au skipper, pas à la plateforme. OK, mais si le site fait peur, on reste sur GYG : là-bas au moins, on peut annuler. »

**Contrat de pertinence :** prix du sunset + comparaison implicite avec l'OTA + garanties équivalentes.

### Phase 1 : test des 5 secondes (arrivée sur sabinas-watersport.com via la marque)
Modale cookies → photo de Sabina dans la boutique. Liste « Exclusive Catamaran Day tour & Sunset Cruise ».

| Question | Réponse | Verdict |
|---|---|---|
| Qu'est-ce que c'est ? | « Le centre nautique de Sabina, OK. » | OUI |
| Est-ce pour moi ? | « "Sunset Cruise" cité, mais aucun prix. » | PARTIEL |
| Que dois-je faire ? | « Le menu ? Il y a FR, cool. » | PARTIEL (via menu) |

### Phase 2

**Menu burger**
> « 21 lignes… EN, DE, FR. "FR – Excursion en Catamaran / Tour Coucher de soleil". Allez. Hmm, "Excursion en voilier tout la jounee" : traduction un peu automatique. Pas d'italien pour Marco, tant pis. »

**Page FR catamaran → clic photo → bascule sur catamaran-yachtsailing-rhodos.com**
> « Attends, on a changé de site ? L'URL n'est plus la même. C'est la même entreprise ? Le bandeau cookies est maintenant en allemand. Bizarre. »

```
ANALYSTE — Changement de domaine
État émotionnel : méfiante
Delta confiance : ↓↓ (rupture de marque, de domaine et de langue en un seul clic : pour une persona qui a peur des arnaques, c'est le pire moment pour ça)
LIFT :            Anxiété ↑, Clarté ↓
Cialdini manquants : Cohérence (même marque, même URL)
```

**Home catamaran, écran 4 : sunset**
> « "Private Catamaran Sunset cruise… glass of wine or Prosecco"… c'est joli. Combien ? Rien. Je clique… page anglaise : 450 € jusqu'à 2 personnes. QUATRE CENT CINQUANTE ?! Sur GYG c'est 50 € par tête. Ah, c'est privé : tout le bateau pour nous. Bon, c'est 225 € par personne. Il n'existe pas en partagé ? Pour la journée, il y a un "half-private" à 160 €, mais pour le sunset, rien. »

```
ANALYSTE — Page Sunset
État émotionnel : choquée, puis calculatrice
Delta confiance : = (prix honnête mais hors budget)
LIFT :            Valeur : le privé n'est pas expliqué comme une valeur (8 couchettes, 3 h, Blue Lagoon, boissons) face à une offre partagée de 1h30 ; pas d'ancrage comparatif
                  Pertinence ↓ : aucune offre au niveau de prix du segment
Cialdini manquants : Contraste (comparer « 225 €/pers, privé, 3 h, Blue Lagoon » avec « 50 € partagé à 40 personnes »), Rareté (« seulement de fin mai à mi-septembre » est écrit, mais comme une contrainte, pas comme un argument)
Fogg :            M ↓↓ | A moyenne | Prompt : « Booking request »
```

**Recherche de garanties (Booking request, Deposit payment)**
> « Formulaire : nom, email, portable, message. "Es gilt die Privacy Policy"… sur la page FR aussi ? "Deposit payment" : une photo et un bouton PayPal. Combien d'acompte ? Remboursé s'il y a du vent ? Rien n'est écrit. Sur GYG, c'est "annulation gratuite jusqu'à 24h avant", en vert, en gros. »

```
ANALYSTE — Réservation et acompte
État émotionnel : méfiante (Marco : « on ferme »)
Delta confiance : ↓↓ aucune condition écrite, mélange de langues
LIFT :            Anxiété maximale : paiement direct à un inconnu, sans politique d'annulation
Cialdini manquants : Preuve sociale (rien n'est visible, alors qu'il existe 9,8/10 sur une OTA : le direct paraît MOINS crédible que l'OTA qui vend le même bateau), Autorité (paiement sécurisé, mentions légales complètes)
Fogg :            M basse | A faible | Prompt : bouton PayPal sans contexte
```

### Phase 3 : verdict
> « Les photos sont belles et le privé à 450 €, c'est sans doute une bonne affaire pour 6 personnes. Pour nous deux, non. Et même si on voulait, je ne vois pas pourquoi réserver ici plutôt que sur GYG : pas d'avis, pas d'annulation, pas de calendrier, trois sites différents. On retourne sur GYG. Ou alors on prend le "half-private" en journée à 160 €… mais je n'ai pas envie d'écrire un email pour ça. »

```
VERDICT — Persona 3
Confiance : 3/10 · Clarté : 5/10 · Pertinence : 3/10
Contacterait : NON (retour OTA)
Forces :      1. Prix publiés, tout inclus détaillé (LIFT Valeur)
              2. Version FR existante (LIFT Pertinence, partiellement)
              3. Visuels du catamaran convaincants (photo drone)
Faiblesses :  1. Aucune raison de réserver en direct plutôt qu'en OTA : ni prix, ni avantage, ni garantie (LIFT Valeur/Anxiété)
              2. Aucune condition d'annulation ni d'acompte écrite (LIFT Anxiété)
              3. Rupture de domaine et de langue au moment du choix (Cialdini Cohérence)
Presque partie : page Sunset, devant « 450 € up to 2 persons »
Plus engagée :  home catamaran écran 4 (texte sunset au Prosecco)
```

**Ce qui l'aurait convertie :**
- un sunset semi-privé (par exemple 6–8 places, prix par personne) ou un « coucher de soleil à partager » ;
- un bloc « Pourquoi réserver en direct » : meilleur prix garanti par rapport aux OTA, échange direct avec Sabina, petit groupe ;
- l'annulation météo gratuite et le montant d'acompte écrits ;
- les avis importés : TripAdvisor, Google et la note OTA ;
- le prix par personne affiché à côté du prix bateau (« 450 € pour 2 = 225 €/pers ») ;
- un site, un domaine, une langue cohérente du bandeau cookies jusqu'au formulaire.

---

## 5. Matrice comparative des 3 personas

| Dimension | P1 Couple DE (premium, urgent) | P2 Famille UK (prix, sécurité) | P3 Couple FR/IT (comparateur OTA) |
|---|---|---|---|
| Domaine d'arrivée | catamaran | watersport | watersport → catamaran |
| Ce que la page sert bien | Offre privée, prix | Prix sports nautiques (page dédiée) | Beauté du produit |
| Bloquant n°1 | Disponibilité / délai de réponse | Sécurité enfants non traitée | Pas de raison de réserver en direct |
| Bloquant n°2 | Avis absents | Trou de gamme 80 € → 440 € | Annulation et acompte non écrits |
| Moment d'abandon | Formulaire sans date | Prix du speedboat privé | Prix du sunset privé |
| Probabilité de contact | Moyenne (WhatsApp, à la main) | Faible | Très faible |
| Levier Cialdini prioritaire | Unité (couple allemand) + Preuve sociale | Autorité (diplômes, sécurité) | Preuve sociale + Contraste |
| Position Fogg | M haute, **A faible** → facilitateur | M moyenne, A faible → étincelle + facilitateur | M faible, A faible → étincelle d'abord |

**Arbitrage stratégique.** Aujourd'hui, le site sert (mal) le segment premium privé, le plus rentable. Il perd sans combat les familles et les comparateurs d'OTA. La refonte n'a pas à tout ouvrir à tout le monde, mais elle doit :
1. faire convertir le segment premium **sans friction**, car c'est lui qui paie le site ;
2. offrir aux deux autres segments une porte d'entrée claire : sports nautiques à l'unité et semi-privé par personne, plutôt que de les renvoyer vers l'OTA ou le rep de l'hôtel.

La décision de créer ou non un sunset semi-privé appartient à Sabina. C'est une question de produit, pas de site, mais le walkthrough montre que c'est là qu'elle perd le segment 25–35 ans.

---

## 6. Top 10 des frictions, classées par impact sur la conversion

| # | Friction | Où | Personas touchés | Framework |
|---|---|---|---|---|
| 1 | **Aucun CTA de contact cliquable et persistant** : 0 lien `tel:`, WhatsApp en texte brut tout en bas, numéro de l'en-tête dolphin qui renvoie vers la home | 3 sites, tous écrans | P1, P2, P3 | Fogg Ability + Prompt |
| 2 | **Formulaire sans date, activité ni nombre de personnes, et sans délai de réponse annoncé.** Pour une demande urgente, l'issue est incertaine. | Booking request ×3 | P1 (critique), P3 | Fogg Ability, LIFT Anxiété |
| 3 | **Zéro preuve sociale visible** : logos TripAdvisor sans note, lien catamaran vers la home tripadvisor.de, alors qu'il existe des notes de 9,8/10 et 4,9/5 ailleurs | 3 sites | P1, P2, P3 | Cialdini Preuve sociale |
| 4 | **Conditions d'acompte, d'annulation et de météo absentes** ; page Deposit = photo + bouton PayPal | Deposit payment ×2 | P3 (critique), P1 | LIFT Anxiété |
| 5 | **3 domaines, 3 marques** : bascule de domaine non annoncée au clic « Catamaran prices », contenus dupliqués, incohérences (demi-privé absent de Rates, « .con », adresse Aulus/Lindian Village) | Navigation inter-sites | P3, P2 | LIFT Clarté, Cialdini Cohérence |
| 6 | **Hero sans promesse ni CTA** : photo de boutique et émoji sur le hub, rocher de Lindos sans bateau visible sur le site catamaran ; aucun prix ni bouton dans le 1er écran | Écran 1 des homes | P1, P2, P3 | Test des 5 s, LIFT Clarté/Pertinence |
| 7 | **Prix cachés ou dispersés** : « click photo » sans étiquette, prix sunset absent de la home, total famille à calculer soi-même, pas de prix par personne sur le privé | Home watersport, home catamaran | P2, P3, P1 | Fogg Ability, LIFT Clarté |
| 8 | **Sécurité et adéquation enfants non traitées** : âges minimums, gilets, encadrement, diplômes (enterrés dans About) | Fiches activités | P2 (critique) | LIFT Anxiété, Cialdini Autorité |
| 9 | **Le meilleur atout de confiance est caché** : Sabine & Roland, allemands, depuis 2007, Maldives, RYA ; départ « à côté de l'Aulus » | About, footer | P1 (Unité), P2 (Autorité) | Cialdini Unité/Autorité/Sympathie |
| 10 | **Bruit technique et linguistique** : modale cookies plein écran (en DE sur EN), 7 à 8 blocs gris YouTube/Maps après refus, mentions en allemand sur pages EN/FR, traduction automatique FR, menu de 21 entrées multilingues, boutons de partage LinkedIn/Xing | 3 sites | P2, P3 | LIFT Distraction, Clarté |

---

## 7. Les 10 exigences de la maquette (cahier des charges)

Chaque exigence est testable : la maquette passe ou échoue.

1. **Barre d'action mobile collante, sur toutes les pages.** WhatsApp (`wa.me` avec message pré-rempli : activité + date + nb pers.) + Appeler (`tel:`) + Réserver. Visible dès le 1er écran, jamais à plus d'un pouce.
   *Corrige les frictions 1 et 2 · Fogg Prompt/Ability.*

2. **Hero = test des 5 s réussi.** Photo du catamaran (ou de l'activité) en mer, promesse « Private catamaran & boat trips from Stafilia Beach, Lindos – since 2007 », note agrégée (★ + nombre d'avis) et 2 CTA (« See trips & prices » / WhatsApp), tout cela au-dessus de 812 px.
   *Frictions 6 et 3.*

3. **Un seul site, une seule marque, une langue cohérente.** Domaine principal unique, les 2 autres redirigés en 301 vers les fiches correspondantes. EN/DE/FR via un sélecteur de langue, pas un menu triple. Bandeau cookies, formulaires, messages d'erreur et mentions dans la langue de la page. Traductions FR relues par un humain.
   *Frictions 5 et 10.*

4. **Home en « catalogue » à cartes produit**, chacune avec photo, durée, privé/partagé, capacité et **prix « dès » en texte** (ex. « Sunset privé · 3 h · dès 450 € / 2 pers. »). Entrées par intention : *Occasion spéciale / En famille / Sensations / Petit budget (partagé)*.
   *Frictions 7 et 6 · LIFT Pertinence.*

5. **Fiche activité standardisée, toujours dans le même ordre** :
   - prix (total et par personne) ;
   - durée et horaires ;
   - inclus / non inclus ;
   - itinéraire en 4 puces ;
   - **bloc « Pour qui / sécurité »** : âge minimum, gilets toutes tailles, skipper certifié, nb max ;
   - point de départ et accès ;
   - avis liés au produit ;
   - FAQ ;
   - CTA collant.

   *Frictions 7 et 8.*

6. **Réservation en 3 étapes maximum avec date réelle.**
   1. Activité + date (calendrier, jours indisponibles grisés si possible) + adultes/enfants (âges) ;
   2. Coordonnées (nom, email, WhatsApp) ;
   3. Récapitulatif avec prix calculé, montant de l'acompte et conditions.

   Message de confirmation « Sabina vous répond sous X h », plus un email automatique. *Option : paiement de l'acompte en ligne (Stripe/PayPal) directement à l'étape 3.*

   *Friction 2 · Fogg Ability, Cialdini Engagement.*

7. **Conditions écrites, visibles avant la demande** : acompte (montant ou %), annulation, politique météo (« report ou remboursement si la mer est trop agitée »), moyens de paiement. Résumé en 3 pictos sur chaque fiche et au récapitulatif, page détaillée en lien.
   *Friction 4 · LIFT Anxiété.*

8. **Preuve sociale réelle et vérifiable** : note TripAdvisor/Google (widget natif ou extrait daté, avec lien vers la vraie fiche), 3 à 6 avis courts segmentés (couple, famille, anniversaire) sur la home et sur chaque fiche. Pas de « 100 % positive feedback » non sourcé. Aucun widget qui disparaît quand on refuse les cookies.
   *Friction 3.*

9. **Bloc « Qui on est » sur la home + avantages du direct.** Photo de Sabine & Roland, « depuis 2007 », Maldives / RYA Offshore, « on parle DE/EN ». Encart « Pourquoi réserver en direct » (meilleur prix garanti par rapport aux OTA, contact direct, flexibilité). Point de départ « à côté de l'Aulus, 10 min de Lindos / Kiotari » avec carte statique cliquable (image + lien Google Maps, sans dépendre des cookies).
   *Frictions 9 et 5 · Cialdini Unité/Autorité/Sympathie.*

10. **Socle technique « zéro bruit ».**
    - Bandeau cookies non bloquant (bannière basse, pas de modale plein écran).
    - Vidéos en façade : image + bouton play chargés seulement au clic, jamais de bloc gris.
    - Images optimisées avec `alt` descriptif ; LCP < 2,5 s en 4G.
    - Zones tactiles ≥ 44 px.
    - Suppression des boutons de partage LinkedIn/Xing.
    - Mentions légales complètes et cohérentes.
    - Données structurées `LocalBusiness` + `Product`/`Offer` avec prix.
    - Suivi des clics WhatsApp, `tel:` et des envois de formulaire comme conversions.

    *Friction 10 · LIFT Distraction, et mesure du résultat de la refonte.*

---

## 8. Hypothèses à valider après mise en ligne
- **Le WhatsApp pré-rempli fait plus que doubler les contacts entrants par rapport au formulaire actuel.** À mesurer : clics `wa.me` + formulaires / sessions, sur 4 semaines avant/après.
- **Afficher la note et 3 avis sur la home réduit le taux de rebond mobile du 1er écran.**
- **Une offre partagée (sunset ou snorkeling) récupère le segment 25–35 ans et familles sans cannibaliser le privé.** Il s'agit d'une décision produit à prendre avec Sabina, testable sur une saison.
- **Le segment germanophone convertit mieux quand « Deutsche Gastgeber seit 2007 » apparaît sur le 1er écran de la version DE.**

Sources externes consultées pour le cadre de comparaison OTA, à revérifier avant toute citation commerciale :
- [Expedia : sunset cruise partagé à Lindos](https://www.expedia.com/things-to-do/lindos-sunset-cruise-with-unlimited-drinks.a48813359.activity-details)
- [Travelocity : catamaran privé Lindos](https://www.travelocity.com/things-to-do/private-catamaran-daytrip-lindos-rhodos-with-lunch-and-drinks.a3065829.activity-details)
- [Click&Boat : Lavezzi 40 Lardos](https://clickandboat.com/uk/boat-hire/lardos/catamaran/fountaine-pajot-catamaran-lavezzi-40-wp424j)
