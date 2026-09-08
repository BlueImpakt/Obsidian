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
- [ ] Signaler à NAECO l'exposition en clair de la clé maître JSONbin + mot de passe éditeur dans leur `CLAUDE.md`, recommander de les déplacer vers un gestionnaire de secrets (variable d'environnement, coffre-fort partagé) et de les faire tourner par précaution
- [ ] Câbler les fichiers média réels dans les slots `pilier-1..3`, `team-*`, `carnet-1..5`, `approche-1..3` quand NAECO les fournit
- [ ] Vérifier dans un vrai navigateur le feel des animations scroll (Hero/Manifeste/résurgence migrés vers Motion, sticky-scroll Carnet de bord et Approche) — le pane d'automation gèle `ScrollTimeline`
- [ ] Vérifier en prod (naecoexpedition.org) que l'éditeur JSONbin fonctionne toujours (connexion + test de sauvegarde) après hard-refresh, suite au déploiement de la refonte
- [ ] Trancher la lisibilité au repos des 3 Piliers sans média/hover (options proposées : P1 rendre le contenu visible d'emblée, P2 revenir à 3 cartes distinctes)
- [ ] Retirer `snapshots/naecoexpedition.org_2026-09-03.html` de `master` si préférence de le garder uniquement sur la branche `backup/pre-refonte` (actuellement accessible en prod, `noindex,nofollow`, inoffensif mais superflu)
- [ ] Diagnostic jonctions Hero→Mission / Carnet→Expédition repris avec la technique d'aplat opaque (commits `f523ddb`, `4a180f7`) après échec du correctif root-cause `f719d3f` ; même technique étendue à Constat→Carnet et aux bandes latérales sans voile d'Expédition 2026 (commit `efcc2f2`) — non confirmé visuellement (preview gelée, fenêtre en arrière-plan), à valider par Melvin après hard-refresh
- [ ] Jonction haute Piliers → Approche — appliquer la même technique d'aplat `#0f2536` que Hero → Mission (démarré en fin de session, à vérifier)
- [ ] Équipe — synchroniser/nettoyer la liste JSONbin `naeco_v5` (retirer le doublon "Marion Fritsch", ajouter le contenu réel du bloc Bureau) avant de considérer la restructuration des cartes Équipe terminée
- [ ] "Constat" renommé en "Contexte" et cartes "Notre action" (75% transparence au survol) faits côté code — reste le Save via l'éditeur JSONbin pour que ce soit visible en ligne
- [ ] Cartes Équipe/Partenaires — reprendre la police et la couleur des anciennes cartes équipe pour les nouvelles, harmoniser l'espace réservé au nom entre toutes les cartes, rendre la partie basse (bandeau du nom) transparente à 50%
- [ ] Regrouper « Notre manifeste » et « Suivre les aventures NAECO » dans une même section (design via skill ui-ux-pro-max, word reveal sur le texte du manifeste, vidéo "drone sunset" en fond) — devient la dernière section du site, retirer la section Contact

## Journal
- **Archive** : historique détaillé du 2026-08-29 au 2026-09-05 (refonte animée Phases 1+2, mise en prod du 09-04, vidéos de fond Mission/Constat/Carnet/Expédition) condensé dans [[journal-archive-2026-08]] — détail commit par commit dans l'historique git du repo.

- 2026-09-07 : Tous les commits locaux de [[naeco-site]] en attente poussés sur `origin/master` (26 commits d'un coup, dont `22ce4a4` vidéo "posidonie poisson", `354fadd` Approche sticky/fondu/voile, `f523ddb`/`4a180f7`/`efcc2f2` jonctions, `e022b28`, et toute la saga vidéos de fond / restructuration Équipe du 05). `.claude/launch.json` ajouté au repo. `more/` (vidéo source `NAECO (1080p).mp4` 791 Mo + logo) ajouté au `.gitignore` — trop lourd pour GitHub (rejet >100 Mo) ; Git LFS ou stockage externe si besoin de le versionner un jour.
- 2026-09-07 (suite) : Vidéo longue de la section Mission remplacée par `teaser_mare_nostrum`, bug corrigé (clic sur le bloc vidéo hors mode édition ouvrait le panneau d'édition — `.img-area-overlay` en `pointer-events:none` hors édition) — commit+push `ff7178b`. **Incident** : ce commit a embarqué par erreur les modifs de couleur d'eyebrow (`var(--g1)`→turquoise) d'une session parallèle qui éditait `index.html` en même temps — non écrites par cette session, mais poussées avec elle sur `master`, à valider avec Melvin.
- 2026-09-07 (suite) : Titres de section (eyebrows) repassés en turquoise `#3DC1B3` (10 règles CSS), puis les sections à fond ivoire clair (Équipe, Co-fondateurs, Bureau, Équipe expédition 2025, Partenaires, Personnalités qui soutiennent) restaurées en vert foncé `#12796d` sur retour de Melvin pour garder le contraste — rien commité.
- 2026-09-07 (suite) : Tentative de lissage de la bande ivoire visible entre la vidéo de fond et le fond clair de la section Équipe (voile `.equipe`/`::before` repassé en rampe continue) — retour de Melvin : la frontière reste visible, pas résolu.
- 2026-09-07 (suite) : Nouvelle approche pour la bande de la section Équipe — fondu en alpha directement sur la vidéo (`mask-image`, `transparent`→opaque sur ~46vh) au lieu d'un simple voile ivoire par-dessus, supprime le bord net. Retour de Melvin : dégradé bon mais masque désormais le haut de la vidéo. Correctif (option retenue par Melvin) : `translateY` vidéo 14vh→26vh + `mask` raccourci 46vh→16vh + `::before` réduit 78vh→60vh. Rendu non capturé côté agent (preview gelée), à confirmer visuellement par Melvin.
- 2026-09-07 (suite) : Section Constat — chiffres clés repositionnés en diagonale (1 % à gauche, 10 % au centre, +20 % à droite) via CSS (`align-items` par `.figure` + `padding-left/right`). Taille réduite en deux itérations (`clamp(72px,16vw,190px)` → `clamp(56px,10vw,120px)` → `clamp(44px,7.5vw,88px)`) et espacement vertical augmenté jusqu'à `44vh` desktop / `36vh` mobile, sur retours successifs de Melvin.
- 2026-09-07 (suite) : Section Expédition 2026 compactée pour tenir sur un écran 1366×768 zoom 100% sans scroll (paddings/gaps réduits sur `.expedition`/`.exp-teaser`/`.exp-body`/`.exp-facts`/`.exp-chev`), libellé « Trois gestes, une même vague » retiré (liste Observer/Pister/Transmettre conservée sans intitulé). Vérifié : 815px/642px/640px de hauteur sur 1440×900, 1366×700, 1280×640. Nouvelle demande reçue en fin de session (pas encore traitée) : renommer la section « Constat » en « Contexte » et, sur « Notre action », faire passer les 2 cartes non survolées à 75% de transparence quand une carte est en grand au survol (mécanisme de survol existant, à ne pas toucher).
- 2026-09-07 (suite) : Section Partenaires — badges remplacés par des cartes (`.ptnr-card`, même gabarit que les cartes équipe, sans flip/swap au curseur), 5 partenaires principaux affichés + bouton « Découvrir tous les partenaires » vers `/partenaires`. Bug corrigé : une liste JSONbin vide `[]` passait le garde `!== undefined` et écrasait le fallback par défaut — remplacé par une garde sensible à la longueur (`pick()`) pour partenaires/soutiens/cofond/bureau/team.
- 2026-09-07 (suite) : Nouvelle page `l-association.html` créée (route `/l-association`, remplace « Mission » dans le header/footer de `index.html`, `expeditions.html`, `mobilite.html`, `campagne-oceanographique.html`, `partenaires.html`) — clone léger reprenant les sections « Notre approche » et « Équipe » à l'identique de la landing (même transition entre les deux) ; sections conservées inchangées sur la landing. Bloc « Personnalités qui soutiennent le projet » ajouté sur `partenaires.html` (6 cartes, même bin JSONbin `soutiens` que la landing) — retour de Melvin : mauvais emplacement, ce bloc doit être sur la landing, pas sur `partenaires.html` (correction pas encore faite).
- 2026-09-07 (suite) : Demande traitée — section « Notre action », cartes non survolées estompées au survol (recul en taille + opacité réduite) ; « Constat » renommé en « Contexte » en HTML (Save via l'éditeur JSONbin encore nécessaire pour être visible en ligne). Bug découvert par ce changement : `opacity` sur `.volet` combinée au `backdrop-filter` du même élément isole la carte en couche composite sous Chromium et fait disparaître l'image de fond — corrigé en retirant l'`opacity` et en assombrissant le voile + le texte à la place (`.volet::after` + `.volet-in`), vérifié une première fois avec de vraies images sur le site en ligne. Retour de Melvin ensuite : images toujours signalées absentes ; dernière capture analysée montrait en fait le fichier local (`file:///...`), pas le site en ligne — diagnostic interrompu avant résolution confirmée par la limite de session.
- 2026-09-07 (suite) : Diagnostic images de piliers absentes conclu — elles n'existent que dans le `localStorage` de Brave, jamais poussées dans JSONbin, donc écrasées dès qu'un chargement réussi recharge le contenu depuis JSONbin. Pas de fix possible côté agent sans re-upload manuel via l'éditeur + Save ; Melvin a choisi d'attendre la mise en ligne pour juger du rendu plutôt que de creuser plus loin. Section Expédition 2026 : label « 3 gestes, une même vague » restauré et renommé « 3 actions, une même vague » avec 3 nouveaux items (surveillance chaîne trophique/mégafaune, étude pollutions anthropiques, surveillance biodiversité/refuges) — toujours piloté par JSONbin (Save requis), tient toujours dans un écran sans scroll.
- 2026-09-07 (suite) : Bloc « Personnalités qui soutiennent » retiré de la landing page (corrige le mauvais emplacement signalé la veille — le bloc reste sur `partenaires.html`), bouton « Découvrir tous les partenaires » recentré. Décision : le panneau d'édition « Personnalités soutien » est laissé en l'état pour l'instant, à retravailler plus tard. Sur `partenaires.html`, la section « Personnalités qui soutiennent » redesignée via le skill ui-ux-pro-max (Minimalism & Swiss) : cartes blanches + liseré corail 2px, rôle repassé en gris pour respecter le contraste WCAG (échec à 3.4:1 en corail → 5.43:1 en gris), monogramme d'initiales, grille responsive `auto-fill` (reflow 3/2/1). Nouvelle demande reçue en fin de session (pas encore traitée) : appliquer le même skill au design des cartes partenaires et des cartes équipe.

- 2026-09-08 : Demande en attente traitée — cartes Partenaires + Équipe + Soutiens redesignées via le skill ui-ux-pro-max (Minimalism & Swiss) : famille de cartes claires unifiée sur les 3 pages (surface blanche, filet corail 2px en tête, monogramme marine, échelle typo commune, hover discret coupé sous reduced-motion), flip conservé sur les cartes Équipe (face avant blanche, dos ivoire chaud). Nouvelle demande reçue en fin de session (pas encore traitée) : reprendre la police/couleur des anciennes cartes équipe pour les nouvelles (équipe + partenaires), harmoniser l'espace du nom entre cartes, rendre le bandeau du nom transparent à 50%. Par ailleurs, autre demande en attente reçue en parallèle : regrouper « Notre manifeste » et « Suivre les aventures NAECO » en une même section (design ui-ux-pro-max, word reveal sur le manifeste, vidéo "drone sunset" en fond), en dernière position du site, avec suppression de la section Contact.

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-site (Cloudflare Pages)
