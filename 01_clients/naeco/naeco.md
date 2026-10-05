---
tags: [client, actif, p2, environnement, france]
created: 2026-08-29
statut: actif
priorite: p2
secteur: environnement
localisation: france
---

# naeco

## Relationnel
- **Association** : NAECO — "Mobiliser l'art et la science pour l'océan"
- **Activité** : expéditions à la voile, créations artistiques, sensibilisation ; documentation de la biodiversité marine (ex. expédition 2022 "The Pelagos Sanctuary", collaboration STARESO)

## Historique des échanges
-

## Décisions prises
-

## Besoins identifiés
- Site vitrine de l'association
- Carte interactive des expéditions/observations/données scientifiques (Pelagos, escales, sites d'étude)

## Devis / propositions
-

## Next actions
- [ ]

## Journal
- 2026-09-19 (suite) : Sur [[naeco-site]] — couleur STARESO reconfirmée, tortue HLD recolorée au survol, système hover 2 images ajouté sur le logo FDVA (rendu signalé "pas propre" par le client, non résolu). Détails dans la fiche projet.
- 2026-09-19 (suite) : Sur [[naeco-site]] — hover FDVA "pas propre" résolu (cache navigateur, fix cache-busting déployé, confirmation client en attente) ; page "Programme & Projets" finalisée (Vision en hero + CTA Expéditions/Mobilité) et déployée ; footer refondu sur les 8 pages (réseaux sociaux, nav, contact). Détails dans la fiche projet.
- 2026-09-20 : Sur [[naeco-carte]] — conception et plan validés pour une animation son+image "rorqual" (lecteur plein écran synchronisé sur un extrait Woodkid, droits musicaux réglés côté client), spec et plan d'implémentation commités, exécution démarrée. Détails dans la fiche projet.
- 2026-09-20 (suite) : Sur [[naeco-carte]] — Tasks 1-5 de l'animation rorqual implémentées et vérifiées (overlay, moteur audio, popup), motif rythmique corrigé (108,2s), audio réel Woodkid branché et testé, démo montrée au client. Reste en attente : ~100 photos rorqual et confirmation client pour la publication finale (Task 6). Détails dans la fiche projet.
- 2026-09-20 (suite) : Sur [[naeco-carte]] — animation rorqual déployée en prod (Task 6 terminée, patch JSONbin appliqué), désync perçu diagnostiqué (contention navigateur au chargement, pas un bug audio), motif rythmique finalisé par exports vidéo ffmpeg (`(A,B,C,C,C)×3 + C`), 33 vraies photos intégrées, lecteur rendu responsive mobile. Détails dans la fiche projet.
- 2026-09-23 : Sur [[naeco-carte]] — incident de perte de données JSONbin (cause : plan d'implémentation obsolète prescrivant un écrasement brut du bin), restauré et corrigé, sauvegarde committée. 6 nouveaux sites d'étude publiés. Sécurité : rotation de la clé maître JSONbin à faire (secret partagé avec [[naeco-site]]). Détails dans la fiche projet.
- 2026-09-23 (suite) : Sur [[naeco-carte]] — stockage Cloudinary des animations rorqual/globicéphales entièrement réorganisé et nettoyé (74 fichiers orphelins supprimés), animation globicéphales reconstruite depuis zéro et branchée à son observation. Détails dans la fiche projet.
- 2026-09-23 (suite) : Sur [[naeco-site]] — refonte de l'éditeur v2 (tous textes/police/taille/couleur éditables sur les 8 pages) lancée : design et plan 1 validés et commités, exécution démarrée, bloquée en attente d'un `.dev.vars` client. Détails dans la fiche projet.
- 2026-09-28 : Sur [[naeco-site]] — Plan 1 de l'éditeur v2 livré, testé et déployé en prod ; incident de sécurité JSONbin résolu (migration des bins vers le compte actuel, clé/mot de passe régénérés, anciens bins supprimés) ; incident de déploiement `.dev.vars` exposé puis corrigé. Sur [[naeco-carte]] — migré vers le nouveau bin, redéployé et vérifié en prod. Détails dans les fiches projet.
- 2026-09-29 : Sur [[naeco-site]] — page mobilité retravaillée (6 capsules Instagram, nouveau texte d'intro, design critique appliquée, remerciement DRAJES de Corse), déployé. Sur [[naeco-carte]] — animation rorqual reprise (version 45s en ligne pour rorqual et globicéphale, 48 nouvelles photos Cloudinary), et 90 points GPS parasites nettoyés sur le tracé live. Détails dans les fiches projet.
- 2026-10-02 : Sur [[naeco-site]] — bug page Partenaires corrigé (fetch JSONbin obsolète écrasait les catégories), hauteur du voile hero réduite de 50%, texte abaissé, virgule retirée après "Méditerranée" dans le HTML, tout déployé. Détails dans la fiche projet.
- 2026-10-02 (suite) : Sur [[naeco-site]] — lockup NAECO × STARESO ajouté sous l'eyebrow "Expédition 2026" (logo STARESO officiel, animation d'apparition échelonnée), déployé. Sur [[naeco-carte]] — recadrage mobile portrait de l'animation rorqual repris en méthode pixel-précise après échec du crop automatique, déployé ; déplacement d'une photo long→short en attente de déploiement. Détails dans les fiches projet.
- 2026-10-02 (suite) : Sur [[naeco-site]] — lockup "NAECO × STARESO" ajouté et animé dans le teaser expédition, logo STARESO au repos corrigé, déployé. Sur [[naeco-carte]] — recadrage mobile portrait V24 finalisé (méthode documentée), pool rorqual ajusté (L06/S04), nouveau dossier Cloudinary V35 globicéphale créé en préparation d'une vidéo pas encore produite. Détails dans les fiches projet.
- 2026-10-04 : Sur [[naeco-carte]] — banque V35 globicéphale branchée, animations rorqual (1min) et globi (1min20) ralenties de 25 % en ligne desktop + mobile (`40e2477`) ; nettoyage Cloudinary réversible (77 assets déplacés dans `_a_supprimer`).
- 2026-10-05 : Sur [[naeco-carte]] — expédition point zéro terminée (badge live retiré, `99d7266`), bouton play des liens `?anim=` recentré (`85b8af0`). Sur [[naeco-site]] — bug « 2 vidéos seulement » sur Mobilité corrigé (état localStorage périmé, `59205fd`) puis même risque purgé sur index et l-association (`99aa007`).

## Liens
- Projets : [[naeco-site]], [[naeco-carte]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
