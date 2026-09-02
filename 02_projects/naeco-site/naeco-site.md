---
tags: [project, encours, naeco]
created: 2026-08-29
statut: encours
client: naeco
---

# naeco-site

## Objectifs du projet
- Site vitrine NAECO : "Mobiliser l'art et la science pour l'océan"
- Présenter les expéditions à la voile, créations artistiques, actions de sensibilisation

## Livrables
- Site public : https://naeco-site.naeco.workers.dev
- Pages : accueil, campagne océanographique, mobilité

## État actuel
- Site en production, déployé sur Cloudflare Pages (auto-déploiement au push `main`)

## Décisions techniques
- **Stack** : fichier HTML unique (`index.html`), pas de framework
- **Contenu live-éditable** : un éditeur en ligne (raccourci Ctrl+Shift+E, protégé par mot de passe — voir gestionnaire de secrets du client, pas stocké ici) permet à l'équipe NAECO de modifier textes/images/liens/couleurs sans toucher au code. Les changements sont synchronisés vers **JSONbin** (bin privé) avec debounce ~600ms.
- **Règle de travail critique** : toujours lancer `check-remote.sh` en début de session pour récupérer l'état actuel du contenu depuis JSONbin avant toute modification — sinon risque d'écraser des changements faits par l'équipe via l'éditeur
- **Déploiement** : `sync.sh "description"` → commit + push → Cloudflare Pages redéploie automatiquement
- ⚠️ Le repo client contient une clé maître JSONbin et un mot de passe éditeur en clair dans son propre `CLAUDE.md` — **volontairement non recopiés ici**, à récupérer directement depuis le repo/le client si besoin

## Blocages / risques
- Repo GitHub source de vérité ambigu : le `CLAUDE.md` du projet référence `melp-cloud/naeco-site`, alors que le clone a été fait depuis `NAECOEXPEDITION/naeco-site` — à clarifier lequel est le remote actif avant de pousser du code
- 🔴 **Sécurité** : clé maître JSONbin + mot de passe éditeur stockés en clair dans le `CLAUDE.md` du repo client (pas juste référencés — la valeur elle-même). Si le repo fuite ou si l'accès change de mains, ces secrets sont exposés tels quels.

## Next actions
- [ ] Signaler à NAECO l'exposition en clair de la clé maître JSONbin + mot de passe éditeur dans leur `CLAUDE.md`, recommander de les déplacer vers un gestionnaire de secrets (variable d'environnement, coffre-fort partagé) et de les faire tourner par précaution

## Journal
- 2026-08-29 : Repo analysé, fiche projet créée. Pattern JSONbin + éditeur live noté comme knowledge réutilisable.
- 2026-09-01 : Guide de charte graphique complété (polices DM Sans/Inter/Space Mono/Caveat). Couleurs des 3 pages alignées sur la charte NAECO — Bleu Marine `#142A4A` / Ivoire `#F4EEE4`, ratio 60‑30‑10 strict (fond ivoire, cartes+header blancs, accent de pôle par page). Commit+push demandé en fin de session — à confirmer que le check-remote.sh a bien été respecté (voir Next actions daily note du jour).
- 2026-09-01 : Nouvelle page `/expeditions` créée à partir du contenu Notion « Présentation Expédition Point Zéro » (+ sous-page Planning). Contenu : Point Zéro 2026 en page complète (accroche, manifeste, itinéraire, 3 piliers science/art/transmission, partenaires) + « Le sillage » (les 4 expéditions précédentes 2022-2025, vidéos reprises de [[naeco-carte]]). Section `#expedition` de la landing transformée en teaser vers cette page ; onglet menu « Expéditions » redirigé vers `/expeditions` sur les 3 pages du site. Bug de scroll cassé (`overflow-x:hidden` sur `<body>`) corrigé. Patch appliqué au JSONbin en suivant la procédure `CLAUDE.md` du repo (la landing rendait encore du contenu 2025 avant patch).
- 2026-09-01 : Refonte forme éditoriale (style Swiss/magazine, skill `ui-ux-pro-max`) de `expeditions.html` — grille rail+colonne, rail numéroté 01→06, drop cap, pull-quote, trio de chiffres sans fond, palette/fonts du skill ignorées au profit de la charte NAECO verrouillée. Même langage repris sur le teaser `#expedition` de la landing (forme seulement, contenu et liaison JSONbin intactes, tous les `data-id` conservés). Commit+push (`3b75f8c`) sur `NAECOEXPEDITION/naeco-site` après `check-remote.sh` ; 2 fichiers, +382/−342.
- 2026-09-02 : Section HERO retravaillée (crop du bas de l'image, `height` fixe 620px pour supprimer le gap avec la barre de chiffres, `background-position: center top`), bouton « Expédition 2026 » retiré du hero. Barre de chiffres animée (count-up 1,4s au scroll, une fois, désactivée si `prefers-reduced-motion`). Bloc upload vidéo ajouté sous le manifeste/citation de la section Mission (`<video autoplay muted loop playsinline>`, placeholder en attendant le fichier). Commit+push (`237d022`) sur `NAECOEXPEDITION/naeco-site`, 1 fichier +132/−4.
- 2026-09-02 : Brief de refonte éditoriale reçu (abandon du style landing SaaS/puces/définitions dictionnaire, place centrale aux médias photo/vidéo sous-marine, effets de scroll sur le hero — zoom arrière + fondu + flou vidéo de fond, section manifeste en text-reveal au scroll). Le brief supposait une migration React/Next.js/Tailwind/Framer Motion — **décision tranchée : non**, l'architecture HTML statique + éditeur JSONbin (Ctrl+Shift+E) reste en place pour ne pas casser le workflow d'édition de l'équipe NAECO. Animations ajoutées avec **Motion** (lib vanilla JS, ex-Motion One, API `scroll()`/`inView()`/springs compatible Framer Motion mais sans React). Maquettes visuelles (mockups Hero + aperçu scroll, vraie palette/polices) lancées pour trancher les registres d'animation — session interrompue avant le retour des maquettes.
- 2026-09-02 : Retour des 3 maquettes (registres A/B/C) — direction **A** retenue : lumière→profondeur→résurgence. Image Hero conservée telle quelle (haut clair avec header, bas bleu foncé) ; les sections suivantes s'assombrissent progressivement jusqu'au point le plus profond (`#142A4A`, chiffres qui comptent) avant de remonter vers du clair, en une seule descente continue depuis le Hero jusqu'à la résurgence finale.
- 2026-09-02 : Effets de scroll du brief mappés aux valeurs déjà scrapées (pattern [[animations-scroll-gsap]], bac à sable `Scrap landing page` — cantor8/ClearPath) : intro Hero (media fade 1.4-2s, nav stagger 0.08, titre split mots blur+y), zoom/flou vidéo au scroll (scale 1→1.18 scrub), manifeste text-reveal mot à mot (`splitWords`, stagger 0.08, scrub), scroll horizontal + parallaxe pour la galerie Expéditions. Priorité affichée par Melvin : terminer cette refonte avant d'explorer les pistes 3D/scrollpath notées en knowledge (upsells, pas engagées sur ce projet).
- 2026-09-02 : Méthode d'implémentation des animations précisée après inspection du code existant (IntersectionObserver + compteur rAF déjà en place, aucune lib chargée) : JS vanilla en extension de l'infra actuelle retenu pour le Hero/Manifeste (zéro nouvelle dépendance) plutôt que la lib Motion ou GSAP ; GSAP réservé pour plus tard, pour le scroll horizontal du Carnet de bord (Expéditions). Brief de refonte resserré finalisé (5 transformations, scope figé) et input de brainstorming post-refonte préparé pour arbitrer les pistes neuves parkées (voilier 3D scrollpath, médias générés, nouveaux graphiques) une fois la refonte livrée et déployée.
- 2026-09-02 : Spec design Hero + Manifeste (skill brainstorming) finalisée et commitée, non poussée — `docs/superpowers/specs/2026-09-02-hero-manifeste-anime-design.md` sur `master` (repo n'a pas de workflow de branches). Direction « plongée » registre A choisie parmi 3 maquettes visuelles (A lumière→profondeur→résurgence, B contemplatif, C émerveillement lumineux). Spec détaillée : Hero (nouveau `.hero-bg` isolé du contenu, entrée staggerée, scroll zoom/flou/gradient marine), Manifeste (`mh` en Fraunces text-reveal mot à mot avec re-split via MutationObserver sur édition JSONbin, bascule fond ivoire→`#142A4A`), intégration (1 `<style>` + 1 `<script>` vanilla ~80 lignes), `prefers-reduced-motion`, 7 critères de réussite, gouvernance assets générés, roadmap Phases 2-3.
- 2026-09-02 : Brainstorm sur le périmètre neuf parké tranché. **Piste Hero 3D voilier (scrollpath Pelagos)** : hors périmètre de cette refonte (contredit la décision « Hero intouché », coût ~2 semaines, jamais fait chez Blue Impakt) — spec séparée possible plus tard sous condition d'un spike jetable Three.js validant le FPS mobile avant modélisation Blender. **Convergence avec [[naeco-carte]]** : en attente de la piste voilier ; si elle se fait, isoler un module partagé `pelagos-path.js` (courbe + tangente), pas de framework 3D maison avant deux consommateurs réels. **Médias générés IA** : règle de gouvernance adoptée dès maintenant (dernier recours, jamais preuve documentaire scientifique, usage texture/transition basse opacité, taggé dans un manifeste d'assets), rien à produire sur cette livraison. Transition vers le plan d'implémentation (skill writing-plans) démarrée en fin de session.
- 2026-09-02 : Plan d'implémentation Hero+Manifeste rédigé (skill writing-plans, 8 tâches — police Fraunces, calque `.hero-bg`, entrée staggerée, plongée au scroll, restyle Manifeste, `splitWords`+`MutationObserver`, bascule fond+éclairage mot à mot, passe critères de réussite) et sauvegardé dans `docs/superpowers/plans/2026-09-02-hero-manifeste-anime.md`, commité sur `master` (non poussé). Exécution démarrée en mode inline (skill executing-plans) : tâche 1 « police Fraunces + flag `html.js` + token `--font-serif` » en cours.

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-site (Cloudflare Pages)
