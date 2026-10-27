---
tags: [project-doc, sabinas-watersport]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: GitHub/sabina-watersport-refonte/docs/08-message-accroche.md
---
# Message d'accroche à Sabina (allemand)

À envoyer avec le lien de la maquette hébergée. Lien de démo actuel : https://sabinas-concept-x7k2m9.vercel.app/ (Vercel, offre gratuite). `?lang=de` ouvre la maquette directement en allemand ; `#konzept` ouvre l'écran « ce qui change pour vous ».

Vérifié avec `ig-human` : 0 tic d'écriture IA, 0 caractère invisible, 0 tiret cadratin. Le score « voix » de l'outil compte des contractions et des pronoms anglais : il ne s'applique pas à l'allemand.

## WhatsApp (court, au +30 697 259 3276)

```
Hallo Sabina,

ich heiße Melvin Perrottet und baue mit meiner Agentur Blue Impakt Websites und Buchungsabläufe. Ihre drei Seiten habe ich mir angesehen. Daraus ist ein Entwurf geworden: eine Website statt drei, mit Ihren Fotos, Ihren Preisen und Ihren 479 Google-Bewertungen direkt neben dem Buchungsbutton.

Am besten auf dem Handy öffnen: https://sabinas-concept-x7k2m9.vercel.app/?lang=de

Gefällt er Ihnen? Dann zeige ich Ihnen in 15 Minuten, wie er bis zur Saison 2027 online gehen kann. Ich schreibe auf Deutsch, Englisch geht genauso gut.

Viele Grüße
Melvin
```

## WhatsApp, variante EN (déjà en contact, « on s'est parlé la semaine dernière »)

```
Hi Sabina, it's Melvin, we spoke last week.

While browsing your websites I noticed you run three URLs, and the design is starting to show its age. I work as a freelance web developer, so I took the liberty of building you a small mockup: one site instead of three, with your photos, your prices and your Google reviews.

It's not just a redesign. Behind it there is a complete setup that makes it work: a fast, modern site built with Astro; a simple dashboard (Sanity) where you change texts, prices and photos from your phone, updated in all languages at once; hosting and spam protection on Cloudflare; and secure online payment by card through Stripe, straight to your own account. On top of that, automations: each request lands on your WhatsApp with all the details, you confirm with one tap, the guest receives a secure payment link, then a reminder the day before and a review request the day after.

If you'd like to keep your three existing domain names for your Google ranking, you can: they would all redirect to the one site.

This is only a mockup, and it is meant to evolve with your needs and your feedback.

Best opened on your phone:
https://sabinas-concept-x7k2m9.vercel.app/?lang=en

If you like it, we could talk about getting you a new site in time for next season 🙂 One that turns more of your visitors into bookings.

Melvin
```

## E-mail (à info@dolphin-tours-rhodos.com ou sabine.kuehl@web.de)

**Betreff :** Ein Entwurf für sabinas-watersport.com

```
Hallo Sabina, hallo Roland,

ich heiße Melvin Perrottet und baue mit meiner Agentur Blue Impakt Websites und Buchungsabläufe für kleine Anbieter. Beim Vergleichen von Bootstouren an der Ostküste von Rhodos bin ich auf Ihre Seiten gestoßen. 479 Google-Bewertungen mit 5,0 Sternen hat in Lardos sonst niemand. Das ist selten.

Drei Dinge sind mir aufgefallen. Sie pflegen drei Websites, und keine zeigt das ganze Angebot. Ihre Bewertungen sieht man nirgends, nur ein Tripadvisor-Logo. Und das Anfrageformular fragt weder nach Datum noch nach Personenzahl, also braucht jeder Gast mehrere Nachrichten, bevor er bucht.

Daraus habe ich einen Entwurf gebaut, mit Ihren Fotos und Ihren echten Preisen. Am besten auf dem Handy öffnen: https://sabinas-concept-x7k2m9.vercel.app/?lang=de

Was sich für Sie im Alltag ändert, steht hier: https://sabinas-concept-x7k2m9.vercel.app/?lang=de#konzept
Ein Beispiel: Sie ändern einen Preis einmal am Handy, und er stimmt sofort in allen Sprachen.

Wenn Sie mögen, zeige ich Ihnen das in einem kurzen Gespräch von 15 Minuten, auf Deutsch oder Englisch. Ziel wäre, dass alles vor den ersten Buchungen 2027 online ist.

Viele Grüße
Melvin Perrottet
Blue Impakt
```

## E-mail de relance, variante EN courte (après le WhatsApp)

**Subject:** A mockup of your new website

```
Hello Sabina,

Just in case you missed my WhatsApp message: I'm a freelance web developer, and I took the liberty of building you a small mockup. One site instead of three, with your photos, your prices and your Google reviews.

See it here (best on your phone):
https://sabinas-concept-x7k2m9.vercel.app/?lang=en

Behind it, a complete setup:
- A fast, modern site (Astro), built to be found on Google in three languages
- An editor (Sanity) to change your texts, prices and photos yourself
- Online booking with secure card payment (Stripe), straight to your own account
- Automations: request on WhatsApp, confirmation emails, reminders and review requests, linked to your calendar
- Hosting and security (Cloudflare), with backups
- Visitor statistics, monitoring and maintenance

You can keep your three domain names for your Google ranking: they would all redirect to the one site.

It's only a mockup, meant to evolve with your needs and feedback. When would you have 10 minutes to discuss it? 🙂 As a freelancer, my rates are also well below those of a web agency.

Best regards,
Melvin Perrottet
Blue Impakt
```

## Traduction FR (pour toi, ne pas envoyer)

**WhatsApp** : Bonjour Sabina, je suis Melvin Perrottet, je fais des sites et des parcours de réservation avec mon agence Blue Impakt. J'ai regardé vos trois sites et j'en ai fait une maquette : un site au lieu de trois, avec vos photos, vos prix et vos 479 avis Google juste à côté du bouton de réservation. À ouvrir sur le téléphone (le lien s'ouvre directement en allemand). Si elle vous plaît, je vous montre en 15 minutes comment la mettre en ligne pour la saison 2027. J'écris en allemand, l'anglais va très bien aussi.

**E-mail** : même trame, avec les 3 constats (3 sites dont aucun n'a toute l'offre ; avis invisibles ; formulaire sans date ni nombre de personnes), le lien vers l'écran concept et l'exemple du prix modifié une fois pour toutes les langues.

## Avant d'envoyer
- [x] Maquette hébergée (Vercel) et lien mis à jour dans les messages
- [ ] Remplir `PITCH_CONTACT` (e-mail / WhatsApp de Melvin) en haut de `maquette/app.js` : sans ça, la page concept n'affiche aucun bouton pour te répondre
- [ ] Reconfirmer le chiffre « 479 avis Google 5,0 » le jour de l'envoi
- [ ] Choisir un seul canal pour le premier contact (WhatsApp **ou** e-mail), relance par l'autre à J+4
