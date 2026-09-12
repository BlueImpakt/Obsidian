---
tags: [project, archive, naeco]
created: 2026-09-12
---

# naeco-carte — Journal archive (2026-08-29 → 2026-09-10)

Entrées condensées du Journal de [[naeco-carte]] pour garder la fiche principale lisible. Détail complet dans l'historique git du repo `NAECOEXPEDITION/naeco-carte` ; les bugs réutilisables sont documentés dans `03_knowledge/troubleshooting.md`.

## 2026-08-29
Repo analysé, fiche créée. Pattern "JSONbin comme source de vérité + garde-fous stricts anti-écrasement" noté comme réutilisable → [[jsonbin-source-de-verite]].

## 2026-08-31
Bug de race condition résolu (tracés d'expédition qui revenaient à leur position initiale en cours d'édition) — fix par flag `localDirty`, déployé (commit `4bc0499`). Détail dans `03_knowledge/troubleshooting.md`.

## 2026-09-07
Commit `aa64cd8` poussé (`.gitignore`/`CLAUDE.md`, règles Graphify).

## 2026-09-09 — Tracking live du catamaran
Brainstorm puis spec puis plan (6 tâches TDD) pour le suivi en direct du catamaran pendant l'expédition 2026 : téléphone à bord → Worker Cloudflare `naeco-track` (D1) → carte affiche marqueur + tracé qui s'allonge. Les 6 tâches livrées et testées (43/43 tests verts), poussé en prod sur demande explicite de Melvin. Worker déployé par Melvin côté Cloudflare (login interactif requis, hors capacité agent) — **tracking live opérationnel en prod**, testé de bout en bout avec le vrai téléphone. Bug de flash/saccade de la carte en mode Live découvert au test réel et corrigé (conflit `transition:transform` avec les transforms Leaflet).

## 2026-09-10
Rebranding "Catamaran NAECO" → "Expédition Point Zéro" partout (popup, export GPX). Filtres d'en-tête désactivés par défaut, panneau "Banque de données" masqué, bug du traceur Live invisible au chargement corrigé. Formulaire "Site d'étude" refondu (protocole/date/expédition/médias), icône du marqueur bateau remplacée (voilier + cap rotatif, choisi parmi 5 options visuelles présentées au client). Rattrapage du tracé live manquant : les points du début d'expédition, non trackés, réinjectés à partir d'un tracé déjà connu ailleurs dans la base plutôt que ré-estimés.

Nouvelle campagne **STARECORSICA (2026-2029)** ajoutée ; champ "association" rendu obligatoire sur observations/escales/sites — les 18 entrées antérieures à cette règle rattachées automatiquement à STARECORSICA. Charte graphique NAECO appliquée à la carte (header, logo, couleurs, tracés). Bug "trace qui disparaît à l'ouverture de l'éditeur" signalé, corrigé, puis re-signalé — recatégorisé le lendemain en faux positif de cache navigateur. Bug de flash/saccade à l'ouverture (repaint GPU, cf. `03_knowledge/troubleshooting.md`) et bug mobile (boutons inatteignables sous 375px) diagnostiqués et corrigés en fin de journée, pas encore poussés à la clôture.

## Liens
- Fiche principale : [[naeco-carte]]
