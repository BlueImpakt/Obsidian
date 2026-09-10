---
tags: [project, encours, naeco]
created: 2026-08-29
statut: encours
client: naeco
---

# naeco-carte

## Objectifs du projet
- Carte interactive des expéditions NAECO : tracés de navigation, observations scientifiques, données Pelagos, escales, sites d'étude

## Livrables
- Page "Carte interactive" (`index.html`), données dans `naeco_data.json`
- Exemple de donnée : expédition 2022 "The Pelagos Sanctuary" (Sanctuaire Pelagos, biodiversité pélagique/cétacés, collab STARESO, tracé GPS complet, vidéo YouTube embarquée)

## État actuel
- En production, déploiement Cloudflare Pages + config Netlify présente (`netlify.toml`) — à clarifier laquelle est la plateforme réellement utilisée

## Décisions techniques
- **Stack** : HTML unique + JSON de données, pas de framework
- **Données live** : synchronisées via **JSONbin** (bin distinct de naeco-site), contient `expeditions`, `observations`, `pelagosData`, `stats`, `general`, `escales`, `sitesEtude`
- **Règles de travail strictes (définies par le client dans son propre CLAUDE.md)** :
  - Ne **jamais** `git push` sans instruction explicite ("déploie")
  - Attendre validation ("ok"/"tu peux coder") avant d'implémenter un contenu discuté
  - Chercher des sources officielles avant tout contenu réglementaire/scientifique (réglementation AMP, UICN, espèces)
  - Toujours lire JSONbin avant modif de contenu — ne jamais écraser depuis le HTML
  - Ne jamais réécrire les `coords` des expéditions depuis le HTML — les récupérer depuis JSONbin telles quelles
  - Ne jamais pousser les données complètes vers JSONbin — patcher uniquement les champs modifiés
- ⚠️ Clé JSONbin non recopiée ici (voir repo client)

## Blocages / risques
- `sync.sh` a un bug de path connu côté client — déploiement à faire manuellement (`git add/commit/push`)

## Next actions
- [ ] Vérifier si le commit `4bc0499` a bien été amendé (mauvaise adresse email) + force-pushé sur `main`
- [ ] Custom domain `track.naecoexpedition.org` (optionnel) — la zone Cloudflare vue par `wrangler` ne correspond pas au bon compte, à refaire proprement si souhaité ; le Worker tourne déjà sur son URL `.workers.dev`, aucun impact fonctionnel
- [ ] Dessiner le vrai tracé de STARECORSICA (2026-2029) via l'onglet Expéditions de l'éditeur (bouton « Tracer le tracé ») — actuellement un tracé placeholder (2 points)

## Journal
- 2026-08-29 : Repo analysé, fiche créée. Pattern "JSONbin comme source de vérité + garde-fous stricts anti-écrasement" à retenir — potentiellement réutilisable pour d'autres sites à contenu live-éditable.
- 2026-08-31 : Bug résolu — tracés d'expédition qui revenaient à leur position initiale en cours d'édition (race condition entre le `fetch` JSONbin `/latest` au chargement et une édition démarrée avant sa réponse). Fix par flag `localDirty` (`index.html:545-547`, `index.html:2620-2627`), déployé (commit `4bc0499`). Voir [[jsonbin-source-de-verite]] et `03_knowledge/troubleshooting.md`. Identité git du repo corrigée (`melvin.perrottet@blue-impakt.org`) — à vérifier si l'amend+force-push du commit `4bc0499` (mauvaise adresse) a bien été fait.

- 2026-09-07 : Commit `aa64cd8` poussé — `.gitignore` (ignore `graphify-out/` + `.claude/settings.local.json`) et `CLAUDE.md` (règles graphify).
- 2026-09-09 : Brainstorm (skill brainstorming) sur l'ajout du tracé live + suivi du catamaran pendant l'expédition 2026. Contraintes cadrées : connexion internet fiable à bord (Starlink/4G), position émise par un smartphone à bord via Traccar Client/OwnTracks (HTTP), trace conservée et rejouable (peu importe la fréquence de rafraîchissement). **Approche retenue** : Cloudflare Worker + D1 (même stack que le reste, gratuit) — le téléphone POST sa position au Worker (protocole OsmAnd), insertion dans D1, la carte interroge un endpoint `/track` pour afficher marqueur + tracé qui s'allonge avec le style `renderExpeditions()` existant ; en fin d'expédition, export D1 → tableau `coords` collé dans JSONbin comme une expédition normale.
- 2026-09-09 (suite) : Design finalisé et spec commitée (`docs/superpowers/specs/2026-09-09-live-tracking-catamaran-design.md`, dans `naeco-carte/`) — 4 briques : **Traccar Client** (émetteur, buffer offline), **Worker `naeco-track`** (`track.naecoexpedition.org`), **D1** (table `positions`, dédup `UNIQUE(device, ts)`), couche `lyr.live` (affichage). 3 endpoints : `/ingest` (POST OsmAnd + token, bornes lat/lon/ts, `INSERT OR IGNORE`), `/track?since=` (polling 60s, CORS restreint au domaine de la carte), `/track.gpx` (export/archivage). Réglage émetteur retenu : 120s / 100m / 15° (équilibre précision/batterie), filtre points aberrants >40 nœuds. Fin d'expé : script `freeze-expedition.mjs` (Douglas-Peucker) → patch ciblé JSONbin. **Intégration à `index.html` vérifiée dans le code** : quasi purement additive — `lyr.live:L.layerGroup()` s'ajoute à l'objet `lyr` existant (ligne 599), toggle via `toggleLayer()` déjà générique, style `dash-flow` et `leaflet-polylineDecorator` déjà chargés/utilisés par `renderExpeditions()`, marqueur catamaran sur le même pattern `L.divIcon` que les icônes existantes — aucune nouvelle dépendance. Code du Worker dans `naeco-track/` à la racine du repo `naeco-carte`. Passage au plan d'implémentation démarré (skill writing-plans) ; plan pas encore produit à la clôture de la session.
- 2026-09-09 (suite) : Plan d'implémentation produit (`docs/superpowers/plans/2026-09-09-live-tracking-catamaran.md`, 6 tâches TDD) et exécution démarrée en inline (feu vert Melvin pour coder direct sur `main`, commits par tâche, rien poussé) — **Task 1** (core Worker `naeco-track`) ✓ 20/20 tests, **Task 2** (export GPX) ✓ 24/24 tests, **Task 3** (routeur Worker) démarrée. Une constante de test erronée dans le plan corrigée au passage (timestamp ISO `2026-09-09` = `1788912000`, pas `1757376000`).
- 2026-09-09 (suite) : **Task 3** (routeur Worker) ✓ 39/39 tests. **Task 4** (scaffold déploiement + smoke D1) ✓ — D1 local + smoke d'intégration OK ; le `wrangler d1 create` distant reste une étape de déploiement (login Cloudflare requis), pas un blocage pour le code. **Task 5** (couche `lyr.live` dans la carte) démarrée.
- 2026-09-09 (suite) : **Task 5** (couche `lyr.live`) ✓ — vérifiée navigateur (polyline animée, marqueur orienté au cap, popup, append incrémental, note « pas de signal », toggle Live, masquage en mode édition). **Les 6 tâches du plan sont complètes, 43/43 tests verts.** Sur demande explicite de Melvin (« déploie maintenant » puis « débrouille-toi pour push toi-même »), poussé en prod sur `main` (`aa64cd8..fd005c0`) — Cloudflare Pages redéploie la carte automatiquement, bouton Live visible. Le Worker `naeco-track` reste à déployer par Melvin (`wrangler login` + `d1 create` + `secret put` + `deploy`, requiert son login Cloudflare interactif) — tant que ce n'est pas fait, le bouton Live affiche « mise à jour indisponible » (dégradation prévue). Config Traccar Client clarifiée avec Melvin : URL corrigée en `https://track.naecoexpedition.org/ingest?token=...` (il manquait `/ingest` + le token), fréquence réglée à 120s.
- 2026-09-09 (suite) : **Worker `naeco-track` déployé en prod** par Melvin (`wrangler login` + `d1 create` + `secret put INGEST_TOKEN` + `wrangler deploy`) → `https://naeco-track.contact-341.workers.dev`. Testé de bout en bout : `/ingest` rejette (401) sur mauvais token, accepte (200) et stocke sur bon token, `/track` renvoie le point, purge D1 remote OK. Custom domain `track.naecoexpedition.org` abandonné (« No zones match » — la zone n'est pas rattachée au compte Cloudflare que voit `wrangler`) ; carte pointée directement sur l'URL `.workers.dev` (commit `c657aff`), fonctionnellement équivalent. **Tracking live catamaran opérationnel en prod** — test réel avec le téléphone, positions reçues près d'Ajaccio. Bug de flash/saccade de la carte en mode Live découvert au test réel puis corrigé : `transition:transform` sur `.boat-marker` entrait en conflit avec les transforms Leaflet appliqués à chaque frame de pan/zoom ; retiré et déployé (`931b201`).
- 2026-09-10 : Renommé "Catamaran NAECO" en "Expédition Point Zéro" partout dans la carte (popup bateau, note signal, export GPX) — poussé (`5fed2e7`, `6472d8d`), 43/43 tests verts.
- 2026-09-10 (suite) : Tous les filtres d'en-tête (Expéditions, Observations, Escales, Sites d'étude, Live) désactivés par défaut au chargement — carte s'ouvre avec fond + Pelagos + AMP uniquement. Légende synchronisée : la section Expéditions n'apparaît que si la couche `routes` est active. Commité et poussé (`8ad0878`).
- 2026-09-10 (suite) : Panneau "Banque de données" masqué (`display:none`) — poussé (`3802a45`). Bug corrigé : le traceur Live ne s'affichait plus au chargement car la désactivation des filtres par défaut avait aussi éteint le bouton et la couche `lyr.live` — exception ajoutée pour Live comme pour les couches de fond, poussé (`ea94543`).
- 2026-09-10 (suite) : Refonte du formulaire "Site d'étude" — champs `Nom du protocole`, `Date/Heure`, `Expédition associée` (incluant "Expédition Point Zéro", le tracé du tracker live), `Description`, galerie `Médias` (photos/vidéos avec lecture vidéo lazy). Retiré : "Type de recherche" et "Profondeur". Vérifié navigateur (formulaire + popup + galerie), poussé avec les champs Escales ci-dessous (`0cd6767`).
- 2026-09-10 (suite) : Icône du marqueur bateau remplacée — voilier vu de profil, toujours droit, avec anneau pointillé et pastille de cap rotative (option D, choisie parmi 5 propositions visuelles). Poussé (`68bd519`).
- 2026-09-10 (suite) : Rattrapage du tracé live manquant (tracking démarré après le début de l'expédition) — 6 points injectés dans D1 (`cata2026`, horodatés 1h avant le premier point GPS réel) à partir de la boucle déjà connue dans JSONbin ("Nouvelle expédition (2026)"), raccord validé sans saut aberrant. 4 points parasites (tests près de Calvi) supprimés. Aucun déploiement nécessaire, la carte lit `/track` en direct.
- 2026-09-10 (suite) : Champs Escales — case "Autre" dans les types d'événement (si cochée, le label du flag sur la carte prend ce texte, prioritaire sur les types) + nouveau champ "Événement associé". `assocOptions()` — liste partagée (`— Aucun —` + expéditions + "Expédition Point Zéro" + **STARECORSICA**) — utilisée à la fois par "Événement associé" (Escales) et "Expédition associée" (Sites d'étude). Poussé avec la refonte Site d'étude, un seul commit (`0cd6767`).
- 2026-09-10 (suite) : Refonte légende/traces — sélection **radio stricte** (une seule trace visible à la fois, re-clic = aucune, défaut = Point Zéro). **Point Zéro (2026)** devient le tracker live lui-même (point rouge clignotant + badge "live"), le bouton d'en-tête Live est supprimé. Légende : "EXPÉDITIONS" renommé **"EXPÉDITION NAECO"** ; nouvelle section **"CAMPAGNE OCÉANOGRAPHIQUE STARESO"** entre les expéditions et Couches ; **STARECORSICA (2026-2029)** ajoutée comme nouvelle trace (catégorie `campagne`, tracé placeholder à dessiner via l'éditeur). Champ "expédition/campagne associée" rendu obligatoire sur observations/escales/sites, un marqueur n'est visible que si sa catégorie est active ET associée à la trace sélectionnée. Poussé (`8b08338`).
- 2026-09-10 (suite) : Les 18 observations + l'escale existantes (créées avant l'ajout du champ association) rattachées automatiquement à **STARECORSICA** via `normalizeAssoc()`. Poussé (`34c4a90`).

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-carte
