---
tags: [project, encours, rm-croisieres]
created: 2026-10-28
projet: rm-croisieres-refonte
parent: rm-croisieres-refonte
genere_par: maquette-outils/envoi
---

# rm-02-dossier-envoi

Projet : [[rm-croisieres-refonte]] · Client : [[rm-croisieres]] · Parent : [[prospect-charter]] · Source : outil `maquette-outils/envoi`, config `envoi/exemples/envoi.json`

Dossier d'envoi de la maquette RM Croisières : vidéo, avant/après, chiffres, page privée et messages. **Tout est en brouillon** : rien n'est publié ni envoyé, Melvin relit et envoie lui-même. Langue du gérant : **FR**.

## À faire avant le premier envoi
- [ ] Remplacer `PITCH_CONTACT` (email + téléphone de Melvin) dans les messages et la page privée
- [ ] Héberger la page privée et la maquette en lien privé, puis remplacer `PITCH_LIEN_PAGE` (aucun lien traçant, aucun pixel)
- [ ] Trancher l'offre « prix pilote contre étude de cas » (marquée **À CONFIRMER PAR MELVIN** sur la page)
- [ ] Choisir la date de J0 (proposée : 03/11/2026) et relire chaque message
- [ ] Facultatif : enregistrer la voix sur le script minuté ([[rm-sous-titres-fr.srt]]), déposer `voix-melvin-fr.wav` à côté de la config, relancer `py -I envoi.py video --sans-capture`
- [ ] Aucun email publié par RM : le J0 part par le formulaire du site, par contact@rmcroisieres.com (mentions légales) ou par téléphone (+596 696 72 25 44). À choisir par Melvin.
- [ ] Remplir PITCH_CONTACT dans maquette/concept.js et PITCH_LIEN_PAGE dans les messages avant l'envoi.


## Pièces
| Pièce | Fichier |
|---|---|
| Vidéo verticale (téléphone, WhatsApp), 57 s, version légère | [[rm-video-vertical-fr-leger.mp4]] |
| Vidéo 16:9 (ordinateur), version légère | [[rm-video-paysage-fr-leger.mp4]] |
| Couverture avec bouton lecture (à mettre dans l'email, cliquable vers la page) | [[rm-couverture-video-fr.jpg]] |
| Avant/après téléphone, premier écran | [[rm-accueil-telephone-ecran.jpg]] |
| Avant/après téléphone, page entière | [[rm-accueil-telephone-page.jpg]] |
| Avant/après ordinateur, premier écran | [[rm-accueil-ordinateur-ecran.jpg]] |
| Avant/après ordinateur, page entière | [[rm-accueil-ordinateur-page.jpg]] |
| Avant/après à curseur (HTML autonome) | [[rm-avant-apres.html]] |
| Fiche chiffres | [[rm-fiche-chiffres.png]] |
| Page privée (HTML, à côté des vidéos) | [[rm-page-privee.html]] |
| Brouillon J0 en HTML (image cliquable) | [[rm-email-j0.html]] |
| Sous-titres / script de la voix | [[rm-sous-titres-fr.srt]] |

![[rm-couverture-video-fr.jpg]]

## Calendrier
| Jalon | Date proposée | Canal | État |
|---|---|---|---|
| J0 | mar. 03/11/2026 | email | brouillon prêt |
| J+3 | ven. 06/11/2026 | WhatsApp | brouillon prêt |
| J+8 | mer. 11/11/2026 | email | brouillon prêt |
| J+15 | mer. 18/11/2026 | email | brouillon prêt |

## Messages

### J0, email à (email à trouver)
Objet : RM Croisières : votre site, vu depuis un téléphone
```
Bonjour,

Votre équipage publie déjà ses itinéraires nuit par nuit, du Marin aux Grenadines, et chacun de vos bateaux porte un nom.
Vos 22 bateaux sont déjà proposés semaine par semaine chez 12knots, mais votre propre site ne montre aucune disponibilité, et le bouton « Rentrons en contact » de l'accueil mène à une page cassée.
J’en ai fait une maquette, de ma propre initiative et sans engagement : une minute de vidéo, ci-dessous.
[IMAGE : rm-couverture-video-fr.jpg, cliquable vers PITCH_LIEN_PAGE]
Auriez-vous 15 minutes cette semaine pour la regarder ensemble ?
Si le sujet ne vous intéresse pas, répondez « stop » et je ne vous écrirai plus.

Melvin Perrottet, Blue Impakt
PITCH_CONTACT
```

### J+3, WhatsApp au +596 696 72 25 44

```
Bonjour, Melvin de Blue Impakt. Je vous ai écrit le 03/11 au sujet de votre site sur téléphone.
Voici l’avant/après de votre page d’accueil, sur le même écran : [IMAGE : rm-accueil-telephone-ecran.jpg]
15 minutes cette semaine ? Sinon, un « stop » suffit.
```

### J+8, email
Objet : RM Croisières : un détail tiré de vos avis
```
Bonjour,

Un détail tiré de vos avis : chez 12knots, deux avis de 2025 parlent de l’entretien à bord (pompe de cale, climatisation) : une liste d’arrivée claire et un message la veille rassurent avant même l’embarquement.
Dans la maquette, la veille de chaque sortie, le client reçoit automatiquement l’heure, le ponton, le parking et la façon de reconnaître votre agent. Vous le voyez à la fin de la vidéo : PITCH_LIEN_PAGE
15 minutes cette semaine ou la suivante ?
Un « stop » suffit pour ne plus recevoir de message.

Melvin Perrottet, Blue Impakt
PITCH_CONTACT
```

### J+15, email
Objet : RM Croisières : je clos de mon côté
```
Bonjour,

Sans réponse de votre part, je clos le sujet de mon côté.
La maquette reste en ligne 30 jours à la même adresse, si vous voulez la montrer à votre équipe : PITCH_LIEN_PAGE
Bonne saison,

Melvin Perrottet, Blue Impakt
```

Règles appliquées : J0 de 5 à 7 lignes, une seule question, une ligne « stop », « de ma propre initiative, sans engagement », ni prix ni technologies, aucun pixel ni lien traçant (CNIL), pas de tiret cadratin. Fait flatteur : 4.3 / 5, 20 avis Google, relevé : 23/10/2026 (agent prospect-charter, resultats/prospects-charter-v2.csv).

## Chiffres
Mesures : Lighthouse 12.8.2, profil mobile (4G lente simulée), page d’accueil · 28/10/2026 · source : rm-croisieres-refonte/sortie/porte-6/resultat.json et sortie/lighthouse-avant/

- **8,8× plus légère sur téléphone** : Page d’accueil : 7,89 Mo aujourd’hui, 902 Ko pour la maquette.

**Ne pas citer :**
- Accessibilité : écart insuffisant ou maquette sous 90 (92 → 100)
- Affichage mobile : le site actuel est déjà adapté au téléphone
- Score « Performance » Lighthouse : écart trop faible et trop variable d'un passage à l'autre pour servir d'argument
- Premier affichage (FCP) : souvent plus rapide sur un vieux site sans polices ni CSS : se retourne contre nous
- LCP du site actuel : trop instable en labo (4 à 14 s selon le passage) pour un chiffre-choc
- « Site 100 % accessible » : Lighthouse ne fait que le contrôle automatique : dire « contrôle automatique »

## Vidéo : déroulé et sous-titres
57 s, 1080×1920 et 1920×1080, sans musique, sous-titres incrustés, aucune voix de synthèse. Piste « voix de Melvin » facultative (voir plus haut). Les versions maîtresses (≈ 20 Mo) restent dans la sortie de l'outil ; le vault garde les versions légères (≈ 8 Mo, même image, assez légères pour WhatsApp).

| Début (s) | Sous-titre |
|---|---|
| 0,0 | Voici rmcroisieres.com, ouvert sur un téléphone. |
| 2,6 | Les prix existent, mais seulement au fond de chaque fiche, sans total. |
| 6,6 | Sur la maquette : vos itinéraires, nuit par nuit, dès le premier écran. |
| 9,3 | Un geste pour voir les Grenadines depuis Blue Lagoon. |
| 11,8 | Puis vos bateaux, chacun par son nom, avec son prix de départ. |
| 16,3 | Chaque bateau a sa fiche : photos, caractéristiques, tarifs. |
| 22,4 | Le client choisit sa semaine : le prix s’affiche, frais compris. |
| 25,7 | Puis l’équipage : seul, avec skipper, ou skipper et hôtesse. |
| 28,8 | Le total et l’échéancier de vos conditions de location suivent chaque choix. |
| 30,3 | Enfin ses coordonnées. Rien à payer à ce stade. |
| 34,5 | La demande arrive à votre bureau, complète et chiffrée. |
| 39,0 | Côté bureau : la demande, le total, l’acompte, et une alerte si la semaine est déjà demandée. |
| 41,2 | Un geste : la confirmation et le lien d’acompte partent à votre nom. |
| 44,8 | Les rappels d’acompte et le message de la veille partent seuls, ou après votre relecture. |
| 50,7 | Un prototype privé, avec vos photos, vos tarifs et vos conditions. |
| 53,9 | Prochain pas : 15 minutes ensemble, si cela vous parle. |

## Liens
- Projet parent : [[rm-croisieres-refonte]]
- Maquette locale : http://localhost:4178/ · site actuel : https://www.rmcroisieres.com/
