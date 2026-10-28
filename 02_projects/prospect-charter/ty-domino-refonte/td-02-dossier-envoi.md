---
tags: [project, encours, ty-domino]
created: 2026-10-28
projet: ty-domino-refonte
parent: ty-domino-refonte
genere_par: maquette-outils/envoi
---

# td-02-dossier-envoi

Projet : [[ty-domino-refonte]] · Client : [[ty-domino]] · Parent : [[prospect-charter]] · Source : outil `maquette-outils/envoi`, config `envoi/exemples/envoi.json`

Dossier d'envoi de la maquette Ty Domino : vidéo, avant/après, chiffres, page privée et messages. **Tout est en brouillon** : rien n'est publié ni envoyé, Melvin relit et envoie lui-même. Langue du gérant : **FR**.

## À faire avant le premier envoi
- [ ] Remplacer `PITCH_CONTACT` (email + téléphone de Melvin) dans les messages et la page privée
- [ ] Héberger la page privée et la maquette en lien privé, puis remplacer `PITCH_LIEN_PAGE` (aucun lien traçant, aucun pixel)
- [ ] Trancher l'offre « prix pilote contre étude de cas » (marquée **À CONFIRMER PAR MELVIN** sur la page)
- [ ] Choisir la date de J0 (proposée : 03/11/2026) et relire chaque message
- [ ] Facultatif : enregistrer la voix sur le script minuté ([[td-sous-titres-fr.srt]]), déposer `voix-melvin-fr.wav` à côté de la config, relancer `py -I envoi.py video --sans-capture`
- [ ] Le lien e-mail de la page contact actuelle pointe vers info@monsite.fr : écrire à tydomino@gmail.com (mentions légales et pied de page).
- [ ] Vérifier à la main le widget Bookeo de la page Réservation actuelle avant le premier échange (docs/etudes/2026-10-28-ty-domino-reservation.md).
- [ ] Remplir PITCH_CONTACT et le lien de la page privée dans les messages avant l’envoi.


## Pièces
| Pièce | Fichier |
|---|---|
| Vidéo verticale (téléphone, WhatsApp), 63 s, version légère | [[td-video-vertical-fr-leger.mp4]] |
| Vidéo 16:9 (ordinateur), version légère | [[td-video-paysage-fr-leger.mp4]] |
| Couverture avec bouton lecture (à mettre dans l'email, cliquable vers la page) | [[td-couverture-video-fr.jpg]] |
| Avant/après téléphone, premier écran | [[td-accueil-telephone-ecran.jpg]] |
| Avant/après téléphone, page entière | [[td-accueil-telephone-page.jpg]] |
| Avant/après ordinateur, premier écran | [[td-accueil-ordinateur-ecran.jpg]] |
| Avant/après ordinateur, page entière | [[td-accueil-ordinateur-page.jpg]] |
| Avant/après à curseur (HTML autonome) | [[td-avant-apres.html]] |
| Fiche chiffres | [[td-fiche-chiffres.png]] |
| Page privée (HTML, à côté des vidéos) | [[td-page-privee.html]] |
| Brouillon J0 en HTML (image cliquable) | [[td-email-j0.html]] |
| Sous-titres / script de la voix | [[td-sous-titres-fr.srt]] |

![[td-couverture-video-fr.jpg]]

## Calendrier
| Jalon | Date proposée | Canal | État |
|---|---|---|---|
| J0 | mar. 03/11/2026 | email | brouillon prêt |
| J+3 | ven. 06/11/2026 | WhatsApp | brouillon prêt |
| J+8 | mer. 11/11/2026 | email | brouillon prêt |
| J+15 | mer. 18/11/2026 | email | brouillon prêt |

## Messages

### J0, email à tydomino@gmail.com
Objet : Ty Domino : votre site, vu depuis un téléphone
```
Bonjour Bruno Desporte,

Je m’appelle Melvin, passionné de voile et web designer : je navigue, et je refais des sites pour ceux qui vivent de la mer.
Votre programme est déjà écrit étape par étape, de l’îlet Madame à l’îlet Chancel, et vos passagers parlent tous du calme, de la voile et du repas.
4,9 sur 394 avis Google, mais votre page contact envoie les e-mails vers info@monsite.fr, l’adresse du modèle Wix, et pour réserver il faut remplir un formulaire puis attendre la réponse.
J’en ai fait une maquette, de ma propre initiative et sans engagement : une minute de vidéo, ci-dessous.
[IMAGE : td-couverture-video-fr.jpg, cliquable vers PITCH_LIEN_PAGE]
Auriez-vous 15 minutes cette semaine pour la regarder ensemble ?
Si le sujet ne vous intéresse pas, répondez « stop » et je ne vous écrirai plus.

Melvin Perrottet, Blue Impakt
PITCH_CONTACT
```

### J+3, WhatsApp au +596 696 22 44 29

```
Bonjour Bruno Desporte, Melvin de Blue Impakt. Je vous ai écrit le 03/11 au sujet de votre site sur téléphone.
Voici l’avant/après de votre page d’accueil, sur le même écran : [IMAGE : td-accueil-telephone-ecran.jpg]
15 minutes cette semaine ? Sinon, un « stop » suffit.
```

### J+8, email
Objet : Ty Domino : un détail tiré de vos avis
```
Bonjour Bruno Desporte,

Un détail tiré de vos avis : au Robert, aucun catamaran à voile en petit comité ne se réserve en ligne aujourd’hui : celui qui le fera le premier captera les clients qui réservent le soir, depuis leur location.
Dans la maquette, la veille de chaque sortie, le client reçoit automatiquement l’heure, le ponton, le parking et la façon de reconnaître votre agent. Vous le voyez à la fin de la vidéo : PITCH_LIEN_PAGE
15 minutes cette semaine ou la suivante ?
Un « stop » suffit pour ne plus recevoir de message.

Melvin Perrottet, Blue Impakt
PITCH_CONTACT
```

### J+15, email
Objet : Ty Domino : je clos de mon côté
```
Bonjour Bruno Desporte,

Sans réponse de votre part, je clos le sujet de mon côté.
La vidéo reste en ligne à la même adresse, si vous voulez la montrer à votre équipe : PITCH_LIEN_PAGE
Bonne saison,

Melvin Perrottet, Blue Impakt
```

Règles appliquées : J0 de 5 à 7 lignes, une ligne de présentation juste après la salutation, une seule question, une ligne « stop », « de ma propre initiative, sans engagement », ni prix ni technologies, aucun pixel ni lien traçant (CNIL), pas de tiret cadratin. Fait flatteur : 4.9 / 5, 394 avis Google, relevé : 28/10/2026 (docs/etudes/2026-10-28-ty-domino-reservation.md).

## Chiffres
Mesures : Lighthouse 12.8.2, profil mobile (4G lente simulée), page d’accueil · 28/10/2026 · source : ty-domino-refonte/sortie/porte-7/resultat.json et sortie/lighthouse-avant/

- **Performance 61 → 75 · Accessibilité 83 → 100 · Référencement 92 → 100 notes sur 100** : Notes Lighthouse de la page d’accueil : site actuel, puis maquette.

**Ne pas citer :**
- Étapes de la demande : 3 étapes (plus de 3) ou parcours actuel non décrit (« demande » du côté avant)
- Affichage mobile : le site actuel est déjà adapté au téléphone
- Poids de page (« 3,5× plus légère ») : parle peu au gérant (Melvin, 28/10/2026) ; reste dans la note interne
- Nombre de gestes du tunnel : 8 gestes paraît beaucoup (Melvin, 28/10/2026) : citer les étapes
- Premier affichage (FCP) : souvent plus rapide sur un vieux site sans polices ni CSS : se retourne contre nous
- LCP du site actuel : trop instable en labo (4 à 14 s selon le passage) pour un chiffre-choc
- « Site 100 % accessible » : Lighthouse ne fait que le contrôle automatique : dire « contrôle automatique »

## Vidéo : déroulé et sous-titres
63 s, 1080×1920 et 1920×1080, sans musique, sous-titres incrustés, aucune voix de synthèse. Piste « voix de Melvin » facultative (voir plus haut). Les versions maîtresses (≈ 20 Mo) restent dans la sortie de l'outil ; le vault garde les versions légères (≈ 8 Mo, même image, assez légères pour WhatsApp).

| Début (s) | Sous-titre |
|---|---|
| 0,0 | Voici ty-domino.fr, ouvert sur un téléphone. |
| 3,0 | Pour réserver : un formulaire, puis attendre la réponse. |
| 6,8 | Dès le premier écran : le bateau, le prix, et la route du jour. |
| 11,1 | Au près le matin, vent arrière au retour : la journée sur la carte de la baie. |
| 15,9 | Une place à bord, ou le bateau entier : le prix sur chaque carte. |
| 20,9 | Le client choisit sa date : il voit les places restantes et le total. |
| 26,7 | Ses coordonnées, et c’est tout. |
| 32,7 | Avant de payer : vos conditions d’annulation et de météo, mot pour mot. |
| 37,1 | L’acompte de 50 % est payé : la sortie est réservée. |
| 41,2 | De votre côté : les réservations arrivent payées, les places se mettent à jour. |
| 46,0 | Un appel ou un message WhatsApp ? Vous l’ajoutez en trois champs. |
| 51,8 | Et la météo reste votre décision : un geste prévient tous les passagers du jour. |
| 55,5 | Vos photos, vos prix, vos conditions de vente. |
| 59,0 | Prochain pas : 15 minutes ensemble, si cela vous parle. |

## Liens
- Projet parent : [[ty-domino-refonte]]
- Maquette locale : http://localhost:4183/ · site actuel : https://www.ty-domino.fr/
