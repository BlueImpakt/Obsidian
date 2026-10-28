---
tags: [project, encours, jicky-marine]
created: 2026-10-28
projet: jicky-marine-refonte
parent: jicky-marine-refonte
genere_par: maquette-outils/envoi
---

# jicky-02-dossier-envoi

Projet : [[jicky-marine-refonte]] · Client : [[jicky-marine]] · Parent : [[prospect-charter]] · Source : outil `maquette-outils/envoi`, config `envoi/exemples/jicky.json`

Dossier d'envoi de la maquette Jicky Marine : vidéo, avant/après, chiffres, page privée et messages. **Tout est en brouillon** : rien n'est envoyé ; seule la page privée est en ligne, en lien non référencé, Melvin relit et envoie lui-même. Langue du gérant : **FR**.

## À faire avant le premier envoi
- [ ] Remplacer `PITCH_CONTACT` (email + téléphone de Melvin) dans les messages et la page privée
- [x] Page privée et maquette hébergées en lien privé, non référencé : https://jicky-marine-ltdnit.vercel.app/p/ (aucun lien traçant, aucun pixel)
- [ ] Trancher l'offre « prix pilote contre étude de cas » (marquée **À CONFIRMER PAR MELVIN** sur la page)
- [ ] Choisir la date de J0 (proposée : 03/11/2026) et relire chaque message
- [ ] Facultatif : enregistrer la voix sur le script minuté ([[jicky-sous-titres-fr.srt]]), déposer `voix-melvin-fr.wav` à côté de la config, relancer `py -I envoi.py video --sans-capture`
- [ ] Chiffres : mesurés le 27/10 sur le commit 3e6b647 ; repasser la porte qualité avant l'envoi et relancer `chiffres` avec son resultat.json si la maquette a changé.


## Pièces
| Pièce | Fichier |
|---|---|
| Vidéo verticale (téléphone, WhatsApp), 74 s, version légère | [[jicky-video-vertical-fr-leger.mp4]] |
| Vidéo 16:9 (ordinateur), version légère | [[jicky-video-paysage-fr-leger.mp4]] |
| Couverture avec bouton lecture (à mettre dans l'email, cliquable vers la page) | [[jicky-couverture-video-fr.jpg]] |
| Avant/après téléphone, premier écran | [[jicky-accueil-telephone-ecran.jpg]] |
| Avant/après téléphone, page entière | [[jicky-accueil-telephone-page.jpg]] |
| Avant/après ordinateur, premier écran | [[jicky-accueil-ordinateur-ecran.jpg]] |
| Avant/après ordinateur, page entière | [[jicky-accueil-ordinateur-page.jpg]] |
| Avant/après à curseur (HTML autonome) | [[jicky-avant-apres.html]] |
| Fiche chiffres | [[jicky-fiche-chiffres.png]] |
| Page privée (HTML, à côté des vidéos) | [[jicky-page-privee.html]] |
| Brouillon J0 en HTML (image cliquable) | [[jicky-email-j0.html]] |
| Sous-titres / script de la voix | [[jicky-sous-titres-fr.srt]] |

![[jicky-couverture-video-fr.jpg]]

## Calendrier
| Jalon | Date proposée | Canal | État |
|---|---|---|---|
| J0 | mar. 03/11/2026 | email | brouillon prêt |
| J+3 | ven. 06/11/2026 | WhatsApp | à ne pas envoyer : aucun numéro WhatsApp pro public (au plus, un appel au bureau) |
| J+8 | mer. 11/11/2026 | email | brouillon prêt |
| J+15 | mer. 18/11/2026 | email | brouillon prêt |

## Messages

### J0, email à info@jickymarine.com
Objet : Jicky Marine : votre site, vu depuis un téléphone
```
Bonjour,

4,6 sur 5 et 75 avis sur Tripadvisor : vos clients y citent vos équipages par leur prénom.
Une flotte de 18 bateaux depuis 2004 à St Barth, mais votre site est illisible sur mobile et chaque réservation passe par un échange d'emails, là où les agences encaissent en ligne.
J’en ai fait une maquette, de ma propre initiative et sans engagement : une minute de vidéo, ci-dessous.
[IMAGE : jicky-couverture-video-fr.jpg, cliquable vers https://jicky-marine-ltdnit.vercel.app/p/]
Auriez-vous 15 minutes cette semaine pour la regarder ensemble ?
Si le sujet ne vous intéresse pas, répondez « stop » et je ne vous écrirai plus.

Melvin Perrottet, Blue Impakt
PITCH_CONTACT
```

### J+3, WhatsApp 
**aucun numéro WhatsApp pro public (au plus, un appel au bureau)**
```
Bonjour, Melvin de Blue Impakt. Je vous ai écrit le 03/11 au sujet de votre site sur téléphone.
Voici l’avant/après de votre page d’accueil, sur le même écran : [IMAGE : jicky-accueil-telephone-ecran.jpg]
15 minutes cette semaine ? Sinon, un « stop » suffit.
```

### J+8, email
Objet : Jicky Marine : un détail tiré de vos avis
```
Bonjour,

Un détail tiré de vos avis : en novembre 2025, un client a salué le bateau et l’équipage, mais regretté des instructions d’arrivée incomplètes : le bateau n’accoste qu’une fois tout le groupe sur le ponton, le parking est rare, l’agent difficile à reconnaître.
Dans la maquette, la veille de chaque sortie, le client reçoit automatiquement l’heure, le ponton, le parking et la façon de reconnaître votre agent. Vous le voyez à la fin de la vidéo : https://jicky-marine-ltdnit.vercel.app/p/
15 minutes cette semaine ou la suivante ?
Un « stop » suffit pour ne plus recevoir de message.

Melvin Perrottet, Blue Impakt
PITCH_CONTACT
```

### J+15, email
Objet : Jicky Marine : je clos de mon côté
```
Bonjour,

Sans réponse de votre part, je clos le sujet de mon côté.
La vidéo reste en ligne à la même adresse, si vous voulez la montrer à votre équipe : https://jicky-marine-ltdnit.vercel.app/p/
Bonne saison,

Melvin Perrottet, Blue Impakt
```

Règles appliquées : J0 de 5 à 7 lignes, une seule question, une ligne « stop », « de ma propre initiative, sans engagement », ni prix ni technologies, aucun pixel ni lien traçant (CNIL), pas de tiret cadratin. Fait flatteur : 4.6 / 5, 75 avis Tripadvisor, relevé : 25/10/2026 (jicky-marine-refonte/docs/avis-clients.md).

## Chiffres
Mesures : Lighthouse 12.8.2, profil mobile (4G lente simulée), médiane de 3 passages, page d’accueil · 27/10/2026 · source : jicky-marine-refonte/docs/revues/web-quality.md, tableaux A et B (commit 3e6b647) ; référencement de la maquette sans son noindex de prototype (66 avec) ; demande actuelle : CGV art. 3.2 (prospection-charter/docs/etudes/2026-10-25-jicky-marine-paiement.md) ; 3 étapes : porte qualité, contrôle tunnel

- **3 étapes pour demander une sortie, depuis le téléphone** : Aujourd’hui : un email au bureau, qui répond par un récapitulatif et un lien de paiement.
- **Performance 75 → 96* · Accessibilité 60 → 100 · Référencement 82 → 100 notes sur 100** : Notes Lighthouse de la page d’accueil : site actuel, puis maquette. * Performance : objectif une fois le site optimisé et en ligne.
- **Téléphone affichage pensé pour l’écran** : Le site actuel n’a pas de réglage pour téléphone : il s’y affiche en version bureau rétrécie.

**Ne pas citer :**
- Poids de page (« 3,5× plus légère ») : parle peu au gérant (Melvin, 28/10/2026) ; reste dans la note interne
- Nombre de gestes du tunnel : 8 gestes paraît beaucoup (Melvin, 28/10/2026) : citer les étapes
- Premier affichage (FCP) : souvent plus rapide sur un vieux site sans polices ni CSS : se retourne contre nous
- LCP du site actuel : trop instable en labo (4 à 14 s selon le passage) pour un chiffre-choc
- « Site 100 % accessible » : Lighthouse ne fait que le contrôle automatique : dire « contrôle automatique »

## Vidéo : déroulé et sous-titres
74 s, 1080×1920 et 1920×1080, sans musique, sous-titres incrustés, aucune voix de synthèse. Piste « voix de Melvin » facultative (voir plus haut). Les versions maîtresses (≈ 20 Mo) restent dans la sortie de l'outil ; le vault garde les versions légères (≈ 8 Mo, même image, assez légères pour WhatsApp).

| Début (s) | Sous-titre |
|---|---|
| 0,0 | Votre site, sur un téléphone. |
| 1,8 | Le texte est trop petit pour être lu sans zoomer. |
| 5,4 | La maquette, vos photos en grand. |
| 7,5 | Votre note dès le premier écran : 4,6 sur 5, 75 avis. |
| 10,7 | Vos 18 bateaux côte à côte, à l’échelle, du 37 au 90 pieds. |
| 15,4 | Puis vos 18 bateaux, chacun avec son prix de départ. |
| 18,6 | Toute la flotte sur une page, à filtrer par sortie, destination et invités. |
| 24,4 | Chaque bateau a sa fiche : photos, détails, prix. |
| 27,7 | Les tarifs par sortie, horaires et destinations compris. |
| 31,3 | Le client choisit sa sortie et sa date : le prix s’affiche aussitôt. |
| 36,4 | Puis le nombre d’invités et le déjeuner. |
| 40,4 | Enfin ses coordonnées. Rien à payer à ce stade. |
| 44,0 | La demande arrive à votre bureau, complète. |
| 46,6 | Côté bureau : le bateau, la date, les invités et le prix, déjà calculé. |
| 51,8 | Vous relisez le message. Rien ne part sans vous. |
| 55,2 | Un tap : la confirmation part avec le lien de paiement Up2pay. |
| 60,7 | La veille, le client recevra l’heure, le ponton, le parking et comment reconnaître votre agent. |
| 66,4 | Ce qui avait manqué à un client en novembre 2025. |
| 69,3 | Prototype privé : vos photos, vos tarifs. |
| 71,8 | Prochain pas : 15 minutes ensemble. |

## Liens
- Projet parent : [[jicky-marine-refonte]]
- Maquette locale : http://localhost:4173/ · site actuel : https://www.jickymarine.com/
