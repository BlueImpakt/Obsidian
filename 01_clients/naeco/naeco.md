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
- 2026-09-16 (suite) : Sur [[naeco-site]] — logo partenaire STARESO récupéré (Drive), recadré, intégré (Cloudinary) et vérifié en live ; rien commité. Liste des 5 prochains partenaires à intégrer transmise par le client (Agence de l'Eau, Le Fonds Vert, FDVA, Fonds HLD, La MAIF Ajaccio). Détails dans la fiche projet.
- 2026-09-17 : Sur [[naeco-carte]] — migration des 43 images Drive vers Cloudinary lancée (risque de perte d'accès au Drive), 42/43 migrées, 1 lien cassé encore à trancher avant de patcher la carte. Détails dans la fiche projet.
- 2026-09-17 (suite) : Sur [[naeco-carte]] — migration des 43 images Drive vers Cloudinary terminée et patchée en live (43/43, dernier lien cassé résolu, bug de saisie Galéria corrigé au passage). Détails dans la fiche projet.
- 2026-09-17 (suite) : Sur [[naeco-carte]] — 9 nouvelles observations mégafaune Point Zéro extraites de 4 GPX client, payload de sync préparé (27 obs au total), publication en attente (client doit exécuter la commande lui-même, mot de passe non partagé). Détails dans la fiche projet.
- 2026-09-17 (suite) : Sur [[naeco-carte]] — publication des 9 observations Point Zéro confirmée (27 au total), puis corrigée sur demande du client (espèces/nombre d'individus). Détails dans la fiche projet.
- 2026-09-17 (suite) : Sur [[naeco-carte]] — 2 nouvelles photos ajoutées à l'escale Porto via Cloudinary (6 → 8 photos). Détails dans la fiche projet.
- 2026-09-17 (suite) : Sur [[naeco-site]] — commit `d7254cd` poussé en prod (renommage « 3 gestes » + CTA déplacé, statsbar 4→5, refonte hero, reformulations de copie). Détails dans la fiche projet.
- 2026-09-18 (suite) : Sur [[naeco-carte]] — 4 nouvelles icônes SVG espèces (raie, dauphin, baleine, tortue) dessinées et intégrées, bug du picker éditeur corrigé au passage, déployé ; photos ajoutées aux 2 observations « dauphins bleu et blanc » Point Zéro. Détails dans la fiche projet.
- 2026-09-19 : Sur [[naeco-carte]] — blocage photos rorqual/globicéphale/plongée levé (fichiers fournis via dossiers locaux), photos assignées aux observations correspondantes et à la fiche « Plongée scientifique 30M », poussées en direct. Détails dans la fiche projet.
- 2026-09-19 (suite) : Sur [[naeco-site]] — icône Instagram ajoutée au header (7 pages), header/logo uniformisé sur les 6 sous-pages, carte DRAJES supprimée (landing repassée à 5 partenaires), texte Vision NAECO intégré et nouvelle page "Programme & Projets" démarrée. Détails dans la fiche projet.
- 2026-09-19 (suite) : Sur [[naeco-site]] — couleur STARESO reconfirmée, tortue HLD recolorée au survol, système hover 2 images ajouté sur le logo FDVA (rendu signalé "pas propre" par le client, non résolu). Détails dans la fiche projet.
- 2026-09-19 (suite) : Sur [[naeco-site]] — hover FDVA "pas propre" résolu (cache navigateur, fix cache-busting déployé, confirmation client en attente) ; page "Programme & Projets" finalisée (Vision en hero + CTA Expéditions/Mobilité) et déployée ; footer refondu sur les 8 pages (réseaux sociaux, nav, contact). Détails dans la fiche projet.
- 2026-09-20 : Sur [[naeco-carte]] — conception et plan validés pour une animation son+image "rorqual" (lecteur plein écran synchronisé sur un extrait Woodkid, droits musicaux réglés côté client), spec et plan d'implémentation commités, exécution démarrée. Détails dans la fiche projet.
- 2026-09-20 (suite) : Sur [[naeco-carte]] — Tasks 1-5 de l'animation rorqual implémentées et vérifiées (overlay, moteur audio, popup), motif rythmique corrigé (108,2s), audio réel Woodkid branché et testé, démo montrée au client. Reste en attente : ~100 photos rorqual et confirmation client pour la publication finale (Task 6). Détails dans la fiche projet.
- 2026-09-20 (suite) : Sur [[naeco-carte]] — animation rorqual déployée en prod (Task 6 terminée, patch JSONbin appliqué), désync perçu diagnostiqué (contention navigateur au chargement, pas un bug audio), motif rythmique finalisé par exports vidéo ffmpeg (`(A,B,C,C,C)×3 + C`), 33 vraies photos intégrées, lecteur rendu responsive mobile. Détails dans la fiche projet.

## Liens
- Projets : [[naeco-site]], [[naeco-carte]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
