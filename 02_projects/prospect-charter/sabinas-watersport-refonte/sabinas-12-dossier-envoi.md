---
tags: [project, encours, sabinas-watersport]
created: 2026-11-01
projet: sabinas-watersport-refonte
parent: sabinas-watersport-refonte
genere_par: maquette-outils/envoi
---

# sabinas-12-dossier-envoi

Projet : [[sabinas-watersport-refonte]] · Client : [[sabinas-watersport]] · Parent : [[prospect-charter]] · Source : outil `maquette-outils/envoi`, config `envoi/exemples/envoi.json`

Dossier d'envoi de la maquette Sabinas Watersport Rhodos : vidéo, avant/après, chiffres, page privée et messages. **Tout est en brouillon** : rien n'est envoyé ; seule la page privée est en ligne, en lien non référencé, Melvin relit et envoie lui-même. Langue du gérant : **EN**.

## À faire avant le premier envoi
- [x] Coordonnées de Melvin dans les messages et la page privée (email, téléphone, WhatsApp)
- [x] Page privée et maquette hébergées en lien privé, non référencé : https://sabinas-xuygcn.vercel.app/p/ (aucun lien traçant, aucun pixel)
- [ ] Trancher l'offre « prix pilote contre étude de cas » (marquée **À CONFIRMER PAR MELVIN** sur la page)
- [ ] Choisir la date de J0 (proposée : 03/11/2026) et relire chaque message
- [ ] Facultatif : enregistrer la voix sur le script minuté ([[sabinas-sous-titres-en.srt]]), déposer `voix-melvin-en.wav` à côté de la config, relancer `py -I envoi.py video --sans-capture`
- [ ] Melvin a déjà échangé avec Sabina (docs/08, variante « we spoke last week ») : le J0 « froid » de l'outil est à adapter en message de suite, en anglais.
- [ ] J+8 : aucun détail d'avis vérifié, à écrire à la main ou à sauter.
- [ ] Avis Google (510) relevés sur Wanderlog le 31/10 : à relever à la main sur Google le jour de l'envoi.
- [ ] Le lien de la maquette v2 expire 7 jours après J0 : changer J0 oblige à republier (envoi.py publier --j0 …).


## Pièces
| Pièce | Fichier |
|---|---|
| Vidéo verticale (téléphone, WhatsApp), 69 s, version légère | [[sabinas-video-vertical-en-leger.mp4]] |
| Vidéo 16:9 (ordinateur), version légère | [[sabinas-video-paysage-en-leger.mp4]] |
| Couverture avec bouton lecture (à mettre dans l'email, cliquable vers la page) | [[sabinas-couverture-video-en.jpg]] |
| Avant/après téléphone, premier écran | [[sabinas-accueil-telephone-ecran.jpg]] |
| Avant/après téléphone, page entière | [[sabinas-accueil-telephone-page.jpg]] |
| Avant/après ordinateur, premier écran | [[sabinas-accueil-ordinateur-ecran.jpg]] |
| Avant/après ordinateur, page entière | [[sabinas-accueil-ordinateur-page.jpg]] |
| Avant/après à curseur (HTML autonome) | [[sabinas-avant-apres.html]] |
| Fiche chiffres | [[sabinas-fiche-chiffres.png]] |
| Page privée (HTML, à côté des vidéos) | [[sabinas-page-privee.html]] |
| Brouillon J0 en HTML (image cliquable) | [[sabinas-email-j0.html]] |
| Sous-titres / script de la voix | [[sabinas-sous-titres-en.srt]] |

![[sabinas-couverture-video-en.jpg]]

## Calendrier
| Jalon | Date proposée | Canal | État |
|---|---|---|---|
| J0 | mar. 03/11/2026 | email | brouillon prêt |
| J+3 | ven. 06/11/2026 | WhatsApp | brouillon prêt |
| J+8 | mer. 11/11/2026 | email | à ne pas envoyer : aucun détail d'avis dans la config : J+8 à écrire à la main |
| J+15 | mer. 18/11/2026 | email | brouillon prêt |

## Messages

### J0, email à info@dolphin-tours-rhodos.com
Objet : Sabinas Watersport Rhodos: your website, seen from a phone
```
Hello Sabina,

I’m Melvin, a sailing enthusiast and web designer: I sail, and I rebuild websites for people who make their living from the sea.
5.0 out of 5 from 510 reviews on Google, and 4.9 on Tripadvisor: your guests clearly love the day.
Your trips are spread over three websites, none of them shows those reviews, and the request form asks for neither a date nor a number of guests.
I turned that into a mock-up, on my own initiative and with no commitment: a one-minute video, below.
[IMAGE: sabinas-couverture-video-en.jpg, linked to https://sabinas-xuygcn.vercel.app/p/]
Would you have 15 minutes this week to look at it together?
If this is not for you, just reply “stop” and I won’t write again.

Melvin Perrottet, Blue Impakt
melvin.perrottet@blue-impakt.org · +33 6 36 81 72 74 · WhatsApp : https://wa.me/33636817274
```

### J+3, WhatsApp au +49 176 3170 7126

```
Hello Sabina, it’s Melvin from Blue Impakt. I emailed you on 03 November about your website on phones.
Here is your home page before and after, on the same screen: [IMAGE: sabinas-accueil-telephone-ecran.jpg]
15 minutes this week? Otherwise, a “stop” is enough.
```

### J+8, email
Objet : Sabinas Watersport Rhodos: a detail from your reviews
```
Hello Sabina,

A detail from your reviews: 
In the mock-up, a guest’s request reaches you complete and priced, and you confirm it in two taps, deposit link included. It is at the end of the video: https://sabinas-xuygcn.vercel.app/p/
15 minutes this week or next?
A “stop” is enough and I won’t write again.

Melvin Perrottet, Blue Impakt
melvin.perrottet@blue-impakt.org · +33 6 36 81 72 74 · WhatsApp : https://wa.me/33636817274
```

### J+15, email
Objet : Sabinas Watersport Rhodos: closing on my side
```
Hello Sabina,

Without a reply, I am closing this on my side.
The video stays online at the same address, if you would like to show it to your team: https://sabinas-xuygcn.vercel.app/p/
Have a good season,

Melvin Perrottet, Blue Impakt
```

Règles appliquées : J0 de 5 à 7 lignes, une seule question, une ligne « stop », « de ma propre initiative, sans engagement », ni prix ni technologies, aucun pixel ni lien traçant (CNIL), pas de tiret cadratin. Fait flatteur : 5.0 / 5, 510 avis Google, relevé : 31/10/2026 (docs/faits.md).

## Chiffres
Mesures : Lighthouse 12.8.2, mobile profile (simulated slow 4G), median of 3 runs, home page · 31/10/2026 · source : avant : sortie/avant/lhr-1..3.json (envoi/mesurer_avant.sh) ; demande actuelle : formulaire libre à 4 champs, docs/01-audit-contenu.md §7 ; après : porte qualité n° 11 (sortie/porte-11/resultat.json) ; 3 étapes : contrôle tunnel ; 2 gestes : vue #bureau (« Read the request » puis « Confirm and send the 150 € link »)

- **3 steps to book from a phone, price shown upfront · 2 taps at the office: review, then send the payment link Fast booking, simple to run** : Today: a free form with name, phone, email and message; trip, date and number of guests are settled by message.
- **Performance 34 → 79 · Accessibility 75 → 100 · Search visibility 92 → 100 scores out of 100** : Lighthouse scores of the home page: current site, then mock-up.
- **3 → 1 one website for all your trips and prices** : Today: sabinas-watersport.com, catamaran-yachtsailing-rhodos.com and dolphin-tours-rhodos.com each show part of the trips and prices.

**Ne pas citer :**
- Affichage mobile : le site actuel est déjà adapté au téléphone
- Poids de page (« 3,5× plus légère ») : parle peu au gérant (Melvin, 28/10/2026) ; reste dans la note interne
- Nombre de gestes du tunnel : 8 gestes paraît beaucoup (Melvin, 28/10/2026) : citer les étapes
- Premier affichage (FCP) : souvent plus rapide sur un vieux site sans polices ni CSS : se retourne contre nous
- LCP du site actuel : trop instable en labo (4 à 14 s selon le passage) pour un chiffre-choc
- « Site 100 % accessible » : Lighthouse ne fait que le contrôle automatique : dire « contrôle automatique »

## Vidéo : déroulé et sous-titres
69 s, 1080×1920 et 1920×1080, sans musique, sous-titres incrustés, aucune voix de synthèse. Piste « voix de Melvin » facultative (voir plus haut). Les versions maîtresses (≈ 20 Mo) restent dans la sortie de l'outil ; le vault garde les versions légères (≈ 8 Mo, même image, assez légères pour WhatsApp).

| Début (s) | Sous-titre |
|---|---|
| 0,0 | Your site today, on a phone. |
| 1,8 | Three websites, and none of them shows all your trips. |
| 5,6 | The mock-up: your drone photo, full screen. |
| 8,3 | Your day in four stops, from your beach to the Blue Lagoon. |
| 11,9 | All your trips on one page, each with its starting price. |
| 15,5 | Every price once, in one table, with your terms. |
| 20,7 | Each trip has its page: photos, video, the day stop by stop. |
| 24,3 | Stafilia, Cave Island, Lindos, the Blue Lagoon. |
| 30,0 | The price for the group, worked out live. |
| 32,6 | Then a date: only days in season can be picked. |
| 35,4 | Name and WhatsApp. Nothing to pay at this stage. |
| 39,0 | Deposit, weather and cancellation, shown before sending. |
| 42,7 | Sent. The guest knows what happens next, and when. |
| 46,9 | Your side: the request arrives complete and priced. |
| 51,1 | You read the message, already written in the guest’s language. |
| 54,9 | Second tap: the deposit link goes out. Nothing leaves without you. |
| 58,9 | Strong wind forecast? You decide, then the guests are told. |
| 63,4 | Private prototype: your photos, your prices. |
| 66,0 | Next step: 15 minutes together. |

## Liens
- Projet parent : [[sabinas-watersport-refonte]]
- Maquette locale : http://127.0.0.1:4186/ · site actuel : https://www.sabinas-watersport.com/
