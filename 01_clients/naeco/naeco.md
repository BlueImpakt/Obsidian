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

## Liens
- Projets : [[naeco-site]], [[naeco-carte]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
