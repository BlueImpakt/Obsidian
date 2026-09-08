---
tags: [project, archive, naeco]
created: 2026-09-08
---

# naeco-site — Journal archive (2026-08-29 → 2026-09-05)

Entrées condensées du Journal de [[naeco-site]] pour garder la fiche principale lisible. Détail complet (valeurs CSS exactes, commits, itérations) dans l'historique git du repo `NAECOEXPEDITION/naeco-site` ; les bugs réutilisables sont documentés dans `03_knowledge/troubleshooting.md` et les patterns concernés.

## 2026-08-29
Repo analysé, fiche créée. Pattern JSONbin + éditeur live identifié comme knowledge réutilisable → [[jsonbin-source-de-verite]].

## 2026-09-01
Guide de charte graphique complété (polices, couleurs `#142A4A`/`#F4EEE4`). Page `/expeditions` créée à partir du Notion officiel (Point Zéro 2026 + rétrospective 4 expéditions, vidéos reprises de [[naeco-carte]]). Refonte éditoriale (rail numéroté, drop cap, pull-quote) appliquée à `/expeditions` et au teaser landing. Commit `3b75f8c`.

## 2026-09-02 — Refonte animée, Phase 1 (Hero + Manifeste)
Brief de refonte reçu en React/Next/Tailwind/Framer Motion — **refusé** : architecture HTML statique + éditeur JSONbin conservée pour ne pas casser le workflow d'édition NAECO, animations ajoutées avec **Motion** (vanilla, API façon Framer Motion). 3 maquettes proposées, direction **A** (lumière→profondeur→résurgence) retenue. Hero 3D voilier écarté du périmètre (hors scope, ~2 semaines) — piste parkée, gouvernance médias IA actée en même temps.

Spec + plan écrits et exécutés (8 tâches) : Hero + Manifeste livrés et mergés sur `master`. Bug découvert et corrigé en cours de route : l'ordre des sections est piloté par `sectionOrder` dans **JSONbin** (pas le HTML) — cassait l'effet de "plongée continue" (fix : ordre forcé côté code). Incident de pollution JSONbin par un `saveAll()` de test corrigé + garde-fou ajouté pour que ça ne se reproduise pas.

## 2026-09-02 — Phase 2 (Constat, Carnet de bord, Piliers, Équipe/Partenaires)
Design figé, bascule complète sur la lib **Motion** pour toute la phase. Chiffres `#constat` retravaillés après désaccord du client sur la source initiale — résolu en redemandant directement les 3 vrais chiffres à Melvin plutôt que d'essayer de justifier les précédents. Les 4 sections livrées et mergées sur `master`. Fin de journée : décision de ne pas pousser en prod tout de suite (~39 commits d'avance), snapshot de sauvegarde proposé.

## 2026-09-03
Section « Notre Approche » refondue en composant sticky-scroll « Parcours à 3 temps » (ancien bloc dictionnaire supprimé). Phase 1 migrée de rAF vanilla vers `Motion.scroll`. Ordre des sections **verrouillé définitivement** côté code (l'équipe ne peut plus le réorganiser via l'éditeur). Couleur de fond Mission ajustée par échantillonnage réel de la photo Hero (`#0b2842`→`#142A4A`) après plusieurs essais sous le seuil de perception humaine. Section Expédition 2026 animée.

Snapshot de sauvegarde de la prod créé et committé en local (pas encore poussé — décision de déploiement en attente de Melvin : ne rien pousser / pousser juste une branche de backup / tout pousser).

Audit du code demandé par Melvin et fait : verdict solide, 7 points d'amélioration remontés (pacing trop long sans médias réels, bug `splitWords` sur texte en gras, dérive specs/code, fond no-JS incohérent, CSS mort, perf mineure, commits jamais poussés donc jamais vus en ligne).

## 2026-09-04 — Mise en prod + vidéos de fond
**Refonte complète poussée en production** sur naecoexpedition.org (39 commits), après sauvegarde de l'ancienne version sur la branche `backup/pre-refonte`.

Brainstorm vidéos de fond marin (Constat/Expédition/Piliers) : mécanisme **« voile-vers-marine »** retenu (chaque section fond vers le marine à ses bords) — remplace le fondu croisé initialement validé, plus robuste sur mobile et sur des vidéos découpées d'une même source. Spec et plan écrits et implémentés : les 4 sections « cœur de plongée » (Mission, Constat, Carnet de bord, Expédition) câblées avec leurs vidéos Cloudinary au fil de la journée.

Deux bugs trouvés et corrigés, documentés dans `03_knowledge/troubleshooting.md` : troncature vidéo via URL de transformation Cloudinary à la volée (fix : pré-encoder et uploader sans transformation), et débordement du calque vidéo `sticky` en fin de section courte (fix : `position: absolute` pour les sections courtes, `sticky` réservé aux sections hautes). Graphify installé sur le repo (4 nœuds, gain jugé négligeable mais laissé actif).

## 2026-09-05
Vidéo Expédition 2026 basculée sur une nouvelle source, Piliers récupère l'ancienne. Toutes les sections « cœur de plongée » ont désormais leur vidéo. Cartes Piliers rendues translucides (voile allégé). Carnet de bord : champ lieu retiré des vignettes, bug JSONbin corrigé au passage (écrasait les éditions HTML avec d'anciennes valeurs).

Longue série de corrections sur les jonctions entre sections (Hero→Mission, Carnet→Expédition, bande sans voile après "Notre approche") — cause réelle trouvée après plusieurs fausses pistes : un filet d'1px dû à la rastérisation indépendante de deux dégradés CSS voisins, pas un problème d'opacité de voile (détail dans `03_knowledge/troubleshooting.md`). Section "Notre approche" passée en sticky, fondu de jonction ajouté. Vidéo de fond ajoutée à la section Équipe. Restructuration des cartes Équipe démarrée (nouveau bloc "Bureau") — **non finalisée** : JSONbin `naeco_v5` a encore un doublon "Marion Fritsch" à nettoyer, resté en Next actions de la fiche principale.

## Liens
- Fiche principale : [[naeco-site]]
