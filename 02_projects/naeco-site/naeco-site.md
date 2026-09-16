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
- **Refonte animée (Phases 1+2 + Approche) déployée en prod le 2026-09-04** (`git push origin master`, 39 commits) — vérifié en ligne (marqueurs `resurgence`/`exp-badge`/`piliers-volets`/`flip-inner` présents, ~213 Ko)

## Décisions techniques
- **Stack** : fichier HTML unique (`index.html`), pas de framework
- **Contenu live-éditable** : un éditeur en ligne (raccourci Ctrl+Shift+E, protégé par mot de passe — voir gestionnaire de secrets du client, pas stocké ici) permet à l'équipe NAECO de modifier textes/images/liens/couleurs sans toucher au code. Les changements sont synchronisés vers **JSONbin** (bin privé) avec debounce ~600ms.
- **Règle de travail critique** : toujours lancer `check-remote.sh` en début de session pour récupérer l'état actuel du contenu depuis JSONbin avant toute modification — sinon risque d'écraser des changements faits par l'équipe via l'éditeur
- **Déploiement** : `sync.sh "description"` → commit + push → Cloudflare Pages redéploie automatiquement
- ⚠️ Le repo client contient une clé maître JSONbin et un mot de passe éditeur en clair dans son propre `CLAUDE.md` — **volontairement non recopiés ici**, à récupérer directement depuis le repo/le client si besoin
- **Ordre des sections verrouillé côté code** (2026-09-03) : l'équipe NAECO ne peut plus réorganiser les sections via l'éditeur (drag désactivé, `sectionOrder` plus lu/écrit dans le bin, `arrange()` fait foi)
- **Vidéos de fond Cloudinary** (2026-09-04) : toujours livrer des fichiers pré-encodés (2 résolutions desktop/mobile), jamais d'URL de transformation à la volée (`f_auto,q_auto,w_...`) — sur ce compte, ces URLs tronquent la durée des vidéos livrées (bug vécu : un film de 23 min ressortait à 4,5s)

## Blocages / risques
- Repo GitHub source de vérité ambigu : le `CLAUDE.md` du projet référence `melp-cloud/naeco-site`, alors que le clone a été fait depuis `NAECOEXPEDITION/naeco-site` — à clarifier lequel est le remote actif avant de pousser du code
- 🔴 **Sécurité** : clé maître JSONbin + mot de passe éditeur stockés en clair dans le `CLAUDE.md` du repo client (pas juste référencés — la valeur elle-même). Si le repo fuite ou si l'accès change de mains, ces secrets sont exposés tels quels.

## Next actions
- [ ] Sécuriser la clé API Cloudinary (actuellement en clair) — Melvin doit la fournir pour déterminer la bonne méthode de stockage
- [ ] Signaler à NAECO l'exposition en clair de la clé maître JSONbin + mot de passe éditeur dans leur `CLAUDE.md`, recommander de les déplacer vers un gestionnaire de secrets (variable d'environnement, coffre-fort partagé) et de les faire tourner par précaution
- [ ] Câbler les fichiers média réels dans les slots `pilier-1..3`, `team-*`, `carnet-1..5`, `approche-1..3` quand NAECO les fournit
- [ ] Vérifier dans un vrai navigateur le feel des animations scroll (Hero/Manifeste/résurgence migrés vers Motion, sticky-scroll Carnet de bord et Approche) — le pane d'automation gèle `ScrollTimeline`
- [ ] Vérifier en prod (naecoexpedition.org) que l'éditeur JSONbin fonctionne toujours (connexion + test de sauvegarde) après hard-refresh, suite au déploiement de la refonte
- [ ] Trancher la lisibilité au repos des 3 Piliers sans média/hover (options proposées : P1 rendre le contenu visible d'emblée, P2 revenir à 3 cartes distinctes)
- [ ] Retirer `snapshots/naecoexpedition.org_2026-09-03.html` de `master` si préférence de le garder uniquement sur la branche `backup/pre-refonte` (actuellement accessible en prod, `noindex,nofollow`, inoffensif mais superflu)
- [ ] Diagnostic jonctions Hero→Mission / Carnet→Expédition repris avec la technique d'aplat opaque (commits `f523ddb`, `4a180f7`) après échec du correctif root-cause `f719d3f` ; même technique étendue à Constat→Carnet et aux bandes latérales sans voile d'Expédition 2026 (commit `efcc2f2`) — non confirmé visuellement (preview gelée, fenêtre en arrière-plan), à valider par Melvin après hard-refresh
- [ ] Jonction haute Piliers → Approche — appliquer la même technique d'aplat `#0f2536` que Hero → Mission (démarré en fin de session, à vérifier)
- [ ] Équipe — synchroniser/nettoyer la liste JSONbin `naeco_v5` (retirer le doublon "Marion Fritsch", ajouter le contenu réel du bloc Bureau) avant de considérer la restructuration des cartes Équipe terminée
- [ ] Renommer la section "Constat" en "Contexte" ; section "Notre action" — au survol d'une carte elle passe en grand (existant, ne pas toucher), les 2 autres cartes passent à 75% de transparence
- [ ] Passer le bin JSONbin `naeco-site` (`6a176fbc21f9ee59d2931d83`) en lecture publique (dashboard → Privacy → Public), déployer les 6 fichiers traités par l'option D (`campagne-oceanographique.html`, `expeditions.html`, `partenaires.html`, `mobilite.html`, `l-association.html`, `index.html`), régénérer la Master Key JSONbin (l'ancienne reste exposée dans l'historique git/`snapshots/`/caches de déploiement), supprimer l'Access Key read-only devenue inutile
- [ ] Corriger la bande sombre à la jonction dégradé → Partenaires — retirer/ajuster le `margin-bottom: -100vh` du fond vidéo sticky de `.expedition` (~lignes 870-878), résidu de l'ancienne galerie Carnet de bord
- [ ] Pusher le commit `ffda241` (implémentation complète de l'alignement charte graphique sur les 8 pages) une fois validé par Melvin
- [ ] Designer la page `/agir-ensemble.html` (stub créé, header/footer + hero « Page en préparation »)
- [ ] Vérifier le contraste du texte blanc « Actus, expéditions & récits océaniques. Sans spam. » sur fond ivoire de la section manifeste — lisibilité dépendante des zones de la vidéo en fond
- [ ] Créer la page "programme" sur naeco-site pour y intégrer le texte Vision NAECO ("Un monde où la connaissance, la compréhension et l'émerveillement nourrissent l'engagement et la protection du vivant.") — "Programme" n'est actuellement qu'un menu déroulant (Expéditions/Mobilité/Campagne Océanographique), pas une page
- [ ] Pusher/déployer la fusion du bloc carte interactive dans la bande dégradée (entre Expédition 2026 et Partenaires) — implémenté et vérifié, rien commité
- [ ] Intégrer les logos des 3 partenaires restants (FDVA, Fonds HLD, La MAIF Ajaccio) dès qu'ils sont récupérables depuis Drive — Agence de l'Eau et Le Fonds Vert déjà traités (Cloudinary + intégrés)
- [ ] Commiter/pousser (`sync.sh`) les logos partenaires déjà intégrés (STARESO, Agence de l'Eau, Le Fonds Vert) dans `index.html`/`partenaires.html`, idéalement groupé avec les prochains logos traités
- [ ] Commiter/pousser (`sync.sh`) la restructuration `/partenaires` (4 catégories) + la refonte responsive de la section Partenaires landing (cartes carrées 100vh, gabarit mobile/desktop unifié) — rien commité

## Journal
- 2026-09-08 (suite) : Section carte interactive agrandie pour remplir l'écran à 100% de zoom (desktop ≥861px) — `.wrap` élargi à 1400px, marges réduites, titre repassé sur une seule ligne (`min(2.3vw,26px)`), `.map-frame` en `max(440px, 100vh - var(--nav-h) - 104px)`, hauteur de section vérifiée à 863px sur 1440×900. Lien header « Actions » renommé « Programme » sur les 7 pages (desktop + mobile), sous-menu déroulant inchangé.
- 2026-09-09 : Tous les commits locaux pending poussés (commit `34cc839`, 7 fichiers) — section carte plein écran + titre 1 ligne, nav « Actions »→« Programme », retouches manifeste/copie, plus 4 commits antérieurs (charte graphique, compteurs stats). `master` synchro avec `origin/master`, working tree clean. Demande reçue juste après traitée à la reprise de session : « 3 actions => 3 gestes » — libellé renommé « 3 gestes, une même vague », bouton « Découvrir nos expéditions » déplacé de la fiche technique vers la colonne droite sous la liste des 3 gestes ; vérifié en DOM à 1440px, non commité.
- 2026-09-09 (suite) : Dérive du texte du HERO au dézoom diagnostiquée — `.hero` a une hauteur fixe (620px) mais une largeur fluide, `.hero-bg` en `background-size:cover` recadre l'image dès que le ratio du bloc change au dézoom, les textes calés en `transform:translateY(...)` restent à une distance absolue du haut du bloc → dérive entre fond et texte. 3 options proposées, **option 1 retenue** : remplacer la hauteur fixe par `aspect-ratio` (= ratio de l'image) et repositionner les textes en `top:%` plutôt qu'en `translateY` absolu — `cover` ne recadre alors plus jamais.
- 2026-09-09 (suite) : **Option 1 implémentée** — `.hero` passé en `height: 44vw; max-height: 900px; container-type: size` (ratio constant visible), textes (`naeco`/tagline/boutons) recalés en `position: absolute; top: 80%/88%/93%` (point fixe de l'image) au lieu de `translateY` absolu, `h1`/`h2` en `translateY(3cqh)`, mobile réaffirmé en `position: static`. Vérifié : position de « naeco » stable à exactement 80% de la hauteur du hero à 1280px et 1920px (avant : dérive de ~235px sur cette plage) ; rendu à 1440px identique à l'avant, animations scroll OK, mobile inchangé, console propre. Limite connue et acceptée : au-delà de ~2045px de large CSS, le plafond `max-height:900px` s'active et une légère dérive réapparaît. Confirmé qu'aucune autre section (Mission, Constat, Piliers, Bascules, Partenaires, cartes équipe) n'a besoin du même traitement — leurs fonds image sont soit en flux normal derrière du texte (pas de calage au pixel), soit en `background-position:center` (recentrage auto).
- 2026-09-09 (suite) : Statsbar — 1ʳᵉ colonne, chiffre `4` → `5`, libellé « Expéditions réalisées » → « Expéditions & documentaires réalisés » (accord « réalisés » retenu par l'agent, à confirmer par Melvin s'il préfère « réalisées »). Compteur animé vérifié.
- 2026-09-11 : Bandeau rouge « Site en chantier » (`#D6362A`, Space Mono 700, style eyebrow) ajouté dans le header entre le logo et les liens, sur les 7 pages live (index, l-association, agir-ensemble, partenaires, expeditions, mobilite, campagne-oceanographique). Vérifié desktop + mobile, aucun chevauchement avec la nav. Rien commité
- 2026-09-12 : Clic droit + drag bloqués sur tous les médias (`img`/`video`) des 7 pages du site (bloc identique inséré avant `</body>` sur chaque page), en complément du même traitement sur [[naeco-carte]] — règle générale documentée comme obligatoire dans le `CLAUDE.md` du repo pour toute page future. Poussé et déployé (`b7c643c`).
- 2026-09-12 (suite) : Bandeau « Site en chantier » réimplémenté à l'identique sur les 7 pages — la version du 11/09 n'avait jamais été commitée et a été perdue entre les deux sessions. Vérifié desktop + mobile de nouveau. **Toujours rien commité** — voir Next actions.
- 2026-09-12 (suite) : Texte du bandeau finalisé sur demande — « Site en chantier » → **« 🚧 Site en travaux »**. Committé et poussé sur `master` (`a18c6a0`).
- 2026-09-15 : Section Mission (`index.html`) mise à jour avec le nouveau texte mission NAECO ("Mobiliser l'art et la science pour explorer, comprendre et protéger l'océan en inspirant un engagement durable."), titre `mh` conservé. Raison d'être NAECO ajoutée en intro de `l-association.html` (`.assoc-lead`) — le `<h1>` au-dessus répète désormais le début du texte, pas encore tranché si à reformuler. Texte Vision NAECO ("Un monde où la connaissance, la compréhension et l'émerveillement nourrissent l'engagement et la protection du vivant.") en attente : pas de page "programme" sur le site pour l'accueillir, « Programme » dans le header n'est qu'un menu déroulant (Expéditions/Mobilité/Campagne Océanographique).
- 2026-09-16 (suite) : Bloc carte interactive (eyebrow + titre + iframe) fusionné dans la bande dégradée `.resurgence`, repositionnée entre "Expédition 2026" et "Partenaires" — une seule section `<section class="carte resurgence" id="carte">` ([index.html:2881](https://github.com/NAECOEXPEDITION/naeco-site)), ancien div `.resurgence` vide supprimé. CSS : `.resurgence` passée en `min-height` (au lieu de `height` fixe), eyebrow/titre repassés en ivoire clair (portion sombre du dégradé), jonctions `::before`/`::after` en `z-index:1`. JS : ordre verrouillé des sections (`ORDER`) met désormais `carte` entre `expedition` et `partenaires`, logique de repositionnement manuel de `.resurgence` supprimée (devenue inutile, `data-section-id="carte"` porté nativement). Vérifié via DOM/styles calculés (ordre, gradient, couleurs, aucune erreur console) — pas de capture visuelle possible (fenêtre navigateur masquée côté outil). **Rien commité/déployé.**
- 2026-09-16 (suite) : Logo partenaire STARESO récupéré depuis Google Drive (dossier "Logos partenaires", partagé le jour même — indexation Drive progressive diagnostiquée pour expliquer l'absence initiale de plusieurs fichiers), recadré (cadre noir retiré), uploadé sur Cloudinary (`naeco-site/logo-stareso`, preset `ml_default`), intégré dans `index.html:3369` et `partenaires.html:365` (entrée `STARESO Calvi`) — vérifié en live (image chargée, 600×309). Rien commité/déployé. Liste des 5 partenaires à ajouter ensuite communiquée par le client en fin de session : Agence de l'Eau, Le Fonds Vert, FDVA, Fonds HLD, La MAIF Ajaccio.
- 2026-09-16 (suite) : Liste définitive des 5 partenaires à afficher en landing reçue du client — landing (`index.html:3368`) et `partenaires.html:364` réordonnés/complétés : Agence de l'Eau Rhône-Méd., Le Fonds Vert, FDVA, Fonds HLD, La MAIF Ajaccio (anciens partenaires type Ville d'Ajaccio/STARESO conservés, toujours visibles sur `/partenaires`). Logos Agence de l'Eau (`logo-agence-eau.png`, 600×600) et Le Fonds Vert (`logo-fonds-vert.png`, 479×351, recadré depuis `Logo fonds vert.jpg` trouvé dans le dossier Drive `more/`) uploadés sur Cloudinary et intégrés dans `index.html:3369` et `partenaires.html:365` — vérifié en live. Restent en initiales : FDVA, Fonds HLD, La MAIF Ajaccio. Rien commité/déployé.
- 2026-09-16 (suite) : Sur [[naeco-site]] — page `/partenaires` restructurée en 4 catégories (Partenaire scientifique, Soutiens institutionnels & financiers, Partenaires logistiques & opérationnels, Partenaires éducatifs & d'engagement citoyen), ancienne liste plate remplacée, `STARESO Calvi` renommé `STARESO`. Section Partenaires de la landing retravaillée sur plusieurs itérations : cartes redimensionnées puis rendues responsives en hauteur (exactement `100vh − nav`, sans scrollbar), cartes passées en format carré (logo + espace nom dédié en dessous), alignement/centrage et taille de police ajustés. Audit `ui-ux-pro-max` : bug trouvé et corrigé — le gabarit mobile héritait par erreur du template cartes équipe (photo portrait, nom en script doré superposé), désormais unifié avec le desktop (tuile carrée + nom DM Sans ivoire) sur tous les viewports. Rien commité/déployé.
- 2026-09-16 (suite) : Sur [[naeco-site]] — dossier Drive NAECO "SPONSORS PNG / V2" confirmé accessible (connecteur Google Drive) — sous-dossier V2 vide au moment de la vérification, dossier parent contient ~19 logos sponsors/partenaires (Agence de l'eau, FDVA, Pangaea, Icape Planète Bleue, Collectivité de Corse, Biocoop, Sailcoop, CCIC, RFAE, HLD, etc.).

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-site (Cloudflare Pages)
