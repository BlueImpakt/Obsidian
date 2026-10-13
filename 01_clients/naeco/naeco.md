---
tags: [client, actif, p2, environnement, france]
created: 2026-08-29
statut: actif
priorite: p2
secteur: environnement
localisation: france
body_synced: 2026-10-13
---

# naeco

## Relationnel
- **Association** : NAECO — "Mobiliser l'art et la science pour l'océan"
- **Activité** : expéditions à la voile, créations artistiques, sensibilisation ; documentation de la biodiversité marine (ex. expédition 2022 "The Pelagos Sanctuary", collaboration STARESO)

## Historique des échanges
-

## Décisions prises
- 2026-10-13 : retours client Mobilité tranchés — logos partenaires en fin de page, navigation inchangée.
- 2026-10-04 : animations rorqual/globicéphale ralenties de 25 % (desktop + mobile).

## Besoins identifiés
- Site vitrine de l'association
- Carte interactive des expéditions/observations/données scientifiques (Pelagos, escales, sites d'étude)

## Devis / propositions
-

## Next actions
- [ ] Déployer `mobilite.html` (retours client implémentés en local le 2026-10-13, non déployé) ([[naeco-site]])

## Journal
- 2026-09-23 (suite) : Sur [[naeco-carte]] — stockage Cloudinary des animations rorqual/globicéphales entièrement réorganisé et nettoyé (74 fichiers orphelins supprimés), animation globicéphales reconstruite depuis zéro et branchée à son observation. Détails dans la fiche projet.
- 2026-09-23 (suite) : Sur [[naeco-site]] — refonte de l'éditeur v2 (tous textes/police/taille/couleur éditables sur les 8 pages) lancée : design et plan 1 validés et commités, exécution démarrée, bloquée en attente d'un `.dev.vars` client. Détails dans la fiche projet.
- 2026-09-23 (suite) : Sur [[naeco-carte]] — animation rorqual/globicéphale en 1 min 31 mise en ligne (`0a1aeef`), liens de partage `?anim=` avec écran d'accueil ▶ (`cc6a87e`).
- 2026-09-28 : Sur [[naeco-site]] — Plan 1 de l'éditeur v2 livré, testé et déployé en prod ; incident de sécurité JSONbin résolu (migration des bins vers le compte actuel, clé/mot de passe régénérés, anciens bins supprimés) ; incident de déploiement `.dev.vars` exposé puis corrigé. Sur [[naeco-carte]] — migré vers le nouveau bin, redéployé et vérifié en prod. Détails dans les fiches projet.
- 2026-09-29 : Sur [[naeco-site]] — page mobilité retravaillée (6 capsules Instagram, nouveau texte d'intro, design critique appliquée, remerciement DRAJES de Corse), déployé. Sur [[naeco-carte]] — animation rorqual reprise (version 45s en ligne pour rorqual et globicéphale, 48 nouvelles photos Cloudinary), et 90 points GPS parasites nettoyés sur le tracé live. Détails dans les fiches projet.
- 2026-10-02 : Sur [[naeco-site]] — bug page Partenaires corrigé (fetch JSONbin obsolète écrasait les catégories), hauteur du voile hero réduite de 50%, texte abaissé, virgule retirée après "Méditerranée" dans le HTML, tout déployé. Détails dans la fiche projet.
- 2026-10-02 (suite) : Sur [[naeco-site]] — lockup NAECO × STARESO ajouté sous l'eyebrow "Expédition 2026" (logo STARESO officiel, animation d'apparition échelonnée), déployé. Sur [[naeco-carte]] — recadrage mobile portrait de l'animation rorqual repris en méthode pixel-précise après échec du crop automatique, déployé ; déplacement d'une photo long→short en attente de déploiement. Détails dans les fiches projet.
- 2026-10-02 (suite) : Sur [[naeco-site]] — lockup "NAECO × STARESO" ajouté et animé dans le teaser expédition, logo STARESO au repos corrigé, déployé. Sur [[naeco-carte]] — recadrage mobile portrait V24 finalisé (méthode documentée), pool rorqual ajusté (L06/S04), nouveau dossier Cloudinary V35 globicéphale créé en préparation d'une vidéo pas encore produite. Détails dans les fiches projet.
- 2026-10-04 : Sur [[naeco-carte]] — banque V35 globicéphale branchée, animations rorqual (1min) et globi (1min20) ralenties de 25 % en ligne desktop + mobile (`40e2477`) ; nettoyage Cloudinary réversible (77 assets déplacés dans `_a_supprimer`).
- 2026-10-05 : Sur [[naeco-carte]] — expédition point zéro terminée (badge live retiré, `99d7266`), bouton play des liens `?anim=` recentré (`85b8af0`). Sur [[naeco-site]] — bug « 2 vidéos seulement » sur Mobilité corrigé (état localStorage périmé, `59205fd`) puis même risque purgé sur index et l-association (`99aa007`).
- 2026-10-08 : Sur [[naeco-carte]] — Rotation de clé JSONbin confirmée en prod, ancien bin compromis supprimé, clé et mot de passe historiques retirés des fichiers de doc/plan des deux repos (naeco-carte, naeco-site), poussé.
- 2026-10-12 : Sur [[naeco-carte]] — audit des fiches AMP : contours et règles de 15+ AMP recalés sur les textes officiels, Maddalena + 4 AMP sardes + Capo Spartivento ajoutées (23 AMP), drone « à vérifier » plutôt qu'« interdit » sans source, badge dérivé de l'UICN ; déployé (`03b9d80`).
- 2026-10-13 : Sur [[naeco-site]] — page Mobilité branchée sur l'éditeur v2, retours client Notion analysés
- 2026-10-13 : Sur [[naeco-site]] — retours Mobilité tranchés (logos partenaires en fin de page, nav inchangée), implémentation démarrée
- 2026-10-13 : Sur [[naeco-site]] — retours client Mobilité implémentés dans `mobilite.html` (local, non déployé).

## Liens
- Projets : [[naeco-site]], [[naeco-carte]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
