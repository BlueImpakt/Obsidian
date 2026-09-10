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
- 2026-08-29 : Repos identifiés (`NAECOEXPEDITION/naeco-site`, `NAECOEXPEDITION/naeco-carte`), fiche client créée
- 2026-08-31 : Bug de race condition résolu sur [[naeco-carte]] (tracés d'expédition écrasés pendant l'édition), déployé. Détails dans la fiche projet et `03_knowledge/troubleshooting.md`.
- 2026-09-01 : Nouvelle page `/expeditions` livrée sur [[naeco-site]] (Point Zéro 2026 + les 4 expéditions précédentes), contenu extrait du Notion officiel de l'expédition. Détails dans la fiche projet.
- 2026-09-02 : Grosse journée [[naeco-site]] — refonte animée Phases 1 (Hero + Manifeste) et 2 (Constat Méditerranée, Carnet de bord, 3 Piliers, Équipe en cartes flip) implémentées et mergées sur `master` (pas encore déployées). Nouvelle spec reçue pour refondre la section « Notre Approche ». Détails complets dans la fiche projet.
- 2026-09-03 : Section « Notre Approche » de [[naeco-site]] refondue (composant sticky-scroll « Parcours à 3 temps ») et mergée sur `master`, Phase 1 migrée vers la lib Motion, transition sombre→clair du site étalée sur 4 zones. Ordre des sections verrouillé côté code (l'équipe ne peut plus le réorganiser via l'éditeur) et couleur source de la section Mission ajustée (`#102746`). Toujours pas déployé en prod. Détails dans la fiche projet.
- 2026-09-03 (suite) : Section « Expédition 2026 » animée, réglages fins de la couleur de fond Mission (résolue par échantillonnage de la photo Hero, `#0b2842`→`#142A4A`) et rampe de dégradé homogénéisée sur toute la zone bleue du site. Demande de fin de session (copie de sauvegarde du site + commit/push) interrompue par la limite de session, à reprendre. Toujours pas déployé en prod. Détails dans la fiche projet.
- 2026-09-04 : **Refonte animée de [[naeco-site]] déployée en production** sur naecoexpedition.org (39 commits), après sauvegarde de l'ancienne version sur une branche `backup/pre-refonte`. À confirmer côté Melvin : l'éditeur JSONbin fonctionne toujours en prod. Détails dans la fiche projet.
- 2026-09-04 (suite) : Vidéos de fond « voile-vers-marine » posées sur [[naeco-site]] (Mission, Constat câblées avec de vraies vidéos ; Expédition/Piliers restent à faire). Deux bugs corrigés en cours de route : bande vidéo visible entre sections courtes (fix `sticky`→`absolute`) et vidéos tronquées par les transformations Cloudinary à la volée (fix : fichiers pré-encodés). Détails dans la fiche projet.
- 2026-09-05 : Vidéos Expédition/Piliers câblées sur [[naeco-site]] (toutes les sections « cœur de plongée » ont désormais leur vidéo), cartes Piliers rendues translucides. Détails dans la fiche projet.
- 2026-09-05 (suite) : Fond vidéo de la section Mission changé pour "Intro, baleine, solastalgie" sur [[naeco-site]], bloc citation retiré. Bug signalé (bande sans voile après "Notre approche") — fix tenté non concluant, toujours visible selon Melvin. Détails dans la fiche projet.
- 2026-09-05 (suite) : Bug de la bande sans voile finalement résolu (vraie cause : bord de raccord entre deux dégradés CSS rastérisés séparément, pas la rampe du voile). Longue saga de repositionnement de la vidéo de fond Mission close (bug de débordement sticky sur la Stats bar résolu en l'absorbant dans la section + `overflow: clip`). Vidéo de fond ajoutée à la section Équipe (sticky, transparence, fix débordement). Restructuration des cartes Équipe démarrée (nouveau bloc Bureau), à finaliser par Melvin côté JSONbin. Détails dans la fiche projet.

- 2026-09-07 : Tous les commits en attente poussés en remote — [[naeco-site]] (26 commits d'un coup, toute la saga vidéos de fond + restructuration Équipe du 05) et [[naeco-carte]] (`.gitignore`/`CLAUDE.md` graphify, `aa64cd8`). Vidéo source NAECO de 791 Mo exclue du versioning (`.gitignore`, trop lourde pour GitHub).
- 2026-09-07 (suite) : Sur [[naeco-site]] — vidéo Mission remplacée (`teaser_mare_nostrum`) + bug de clic hors édition corrigé (commit `ff7178b`), couleur des titres de section ajustée (turquoise partout, vert foncé restauré sur fonds ivoire clairs pour le contraste), tentative de lissage de la bande ivoire visible section Équipe non concluante. Détails dans la fiche projet.
- 2026-09-08 : Sur [[naeco-site]] — refonte nav + section finale commitée et poussée en remote (commit `20a281c`, 6 fichiers, +5441/−126) : nav « Mission » → « L'association » sur tout le site + nouvelles pages `l-association.html` et `partenaires.html`, section Contact supprimée et newsletter fusionnée avec « Notre manifeste » (dernière section, fond vidéo drone sunset), « Constat » renommé « Contexte », Expédition 2026 compactée, cartes Partenaires en portrait 3/4, cartes Équipe/Partenaires harmonisées (police + or #FFC83A des anciennes cartes, bandeau du nom translucide 50 %). [[naeco-carte]] : rien à pousser (working tree clean). Détails dans la fiche projet.
- 2026-09-08 (suite) : Facture NAECO (26-06-2) réévaluée de 500 € à 2 500 €, cohérence vérifiée.
- 2026-09-08 (suite) : Déclaration URSSAF juin 2026 mise à jour avec le nouveau CA — d'abord aligné sur la facture (2 500 €, cotisations 320 € + 55 € + 5 € = 380 €), puis révisé à **3 500 €** (cotisations sociales 448 €, versement libératoire IR 77 €, CFP 7 €, total 532 €, aucun arrondi), document reconstruit proprement (police unique, cellules alignées) après un souci de rendu pdf2htmlEX (polices mixtes, chiffres débordant des cases) sur l'export PDF brut.
- 2026-09-08 (suite) : Sur [[naeco-site]] — root cause identifiée du bug images vides en prod (logo + section « Notre action ») : `applyData()` ne réhydrate pas les inputs cachés, ce qui fait écraser les images stockées par `saveAll()` au premier chargement. Correctif pas encore appliqué. Détails dans la fiche projet.
- 2026-09-08 (suite) : Sur [[naeco-site]] — section « Notre approche » retirée de la landing page ; correction apportée ensuite (c'est « L'équipe », pas « Partenaires », qui devait être retirée en plus — « Partenaires » restaurée, nav/footer repointés) — pas encore commité. Vidéo de fond du manifeste finalisée (upload Cloudinary) et couleur du word-reveal passée en corail. Câblage en dur des 4 images Cloudinary confirmé fait. Détails dans la fiche projet.
- 2026-09-09 : Accès Notion NAECO connecté côté claude.ai — workspace « QG — Espace de travail de ML Cipriani » exploré (bases Projets, Ressources, MAJ contenus, Documentation Association, Accès Comptes, Contact). Plaquette NAECO 2025 introuvable dans le workspace (recherche mot-clé exact, 0 résultat) ni sur Drive (non connecté). Sur [[naeco-carte]] : plan d'implémentation du tracking live catamaran produit (6 tâches TDD) et exécution démarrée — Task 1 (core Worker) et Task 2 (export GPX) terminées et testées, Task 3 (routeur Worker) en cours. Détails dans la fiche projet.
- 2026-09-09 (suite) : Sur [[naeco-carte]] — les 6 tâches du plan tracking live catamaran terminées (43/43 tests verts), code et carte poussés en prod sur demande explicite de Melvin ; il reste à Melvin de déployer le Worker `naeco-track` côté Cloudflare (login interactif requis). Sur [[naeco-site]] — chiffres statsbar mis à jour (5 expéditions & documentaires réalisés au lieu de 4). Détails dans les fiches projet.
- 2026-09-09 (suite) : **Tracking live catamaran opérationnel en prod** sur [[naeco-carte]] — Worker `naeco-track` déployé par Melvin, testé de bout en bout, premiers points reçus du téléphone. Custom domain abandonné (zone Cloudflare pas dans le bon compte), carte pointée sur l'URL `.workers.dev`. Bug de flash/saccade découvert au test réel puis corrigé et déployé. Détails dans la fiche projet.
- 2026-09-10 : Sur [[naeco-carte]] — rebranding "Catamaran NAECO" → "Expédition Point Zéro" (popup, note signal, export GPX) et filtres d'en-tête désactivés par défaut au chargement (légende Expéditions synchronisée avec le filtre), les deux poussés en prod. Détails dans la fiche projet.
- 2026-09-10 (suite) : Sur [[naeco-carte]] — panneau "Banque de données" masqué, bug du traceur Live invisible au chargement corrigé, formulaire "Site d'étude" refondu (protocole/date-heure/expédition/description/médias), icône du marqueur bateau remplacée par un voilier avec cap rotatif, rattrapage du tracé live manquant injecté dans D1. Détails dans la fiche projet.
- 2026-09-10 (suite) : Sur [[naeco-carte]] — champs Escales enrichis (case "Autre" + "Événement associé"), refonte de la légende/traces (sélection radio stricte, Point Zéro devient le tracker live, section "EXPÉDITION NAECO" + nouvelle "CAMPAGNE OCÉANOGRAPHIQUE STARESO"), nouvelle campagne STARECORSICA (2026-2029) ajoutée, association obligatoire sur observations/escales/sites — anciens marqueurs sans association rattachés automatiquement à STARECORSICA. Détails dans la fiche projet.
- 2026-09-10 (suite) : Sur [[naeco-carte]] — charte graphique NAECO appliquée à la carte (header clair, logo, badges recolorés, tracés ivoire), fix du bug de disparition de la trace Point Zéro en mode présentation, filtre "Expédition/campagne" ajouté dans l'éditeur, couleurs AMP/PELAGOS fixées, fenêtre légende bicolore. Détails dans la fiche projet.

## Liens
- Projets : [[naeco-site]], [[naeco-carte]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
