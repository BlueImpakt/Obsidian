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
- **Sécurité accès données (depuis 2026-09-11)** : plus aucune clé JSONbin côté client. Lecture ET écriture passent exclusivement par un proxy Cloudflare Worker (`/api/data`, `/api/sync`, `/api/login`) qui détient seul les secrets (`JB_MASTER_KEY`, `EDIT_PASSWORD`, via `wrangler secret put`) ; même pattern que `naeco-track`
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
- [ ] Activer le versioning JSONbin sur le bin naeco-carte (aucun retour arrière possible actuellement en cas d'écrasement)
- [ ] Vérifier si le commit `4bc0499` a bien été amendé (mauvaise adresse email) + force-pushé sur `main`
- [ ] Custom domain `track.naecoexpedition.org` (optionnel) — la zone Cloudflare vue par `wrangler` ne correspond pas au bon compte, à refaire proprement si souhaité ; le Worker tourne déjà sur son URL `.workers.dev`, aucun impact fonctionnel
- [ ] Pousser le commit en attente (header mobile responsive `a75b2f2`)
- [ ] Supprimer les 14 points GPS parasites restants à Porto (dérives à pied du 12/09, 06h37-06h57 et 07h28-07h36 UTC) — commande `wrangler d1` prête, à exécuter côté client (classifieur anti-suppression-de-masse bloque l'agent)
- [ ] Migrer le logo NAECO (`PHOTO_LOGO_NAECO`, même bloc que le logo Ammo Visuals) de Google Drive vers Cloudinary
- [ ] Déployer la migration du logo Ammo Visuals vers Cloudinary (changement local uniquement pour l'instant)

## Journal
- 2026-09-17 (suite) : 2 nouvelles photos (Google Drive) uploadées vers Cloudinary et ajoutées à l'escale Porto (6 → 8 photos), vérifié côté serveur.
- 2026-09-17 (suite) : 2 photos supplémentaires assignées aux 2 observations « Saut de raie mobula » (1 photo par observation) sur Cloudinary — données rechargées avant application pour ne pas écraser les 4 observations mégafaune ajoutées entre-temps, 27 observations et escale Porto (8 médias) préservées, vérifié en direct.
- 2026-09-18 : Logo Ammo Visuals (overlay photos, lightbox + carte, `index.html:544` et `:2635`) migré de Google Drive vers Cloudinary (`ammo-visuals-logo.png`, PNG transparent 1599×1600), 2 références mises à jour dans le code, fichier local fourni au client. Changement local uniquement, pas encore déployé. Migration du logo NAECO (`PHOTO_LOGO_NAECO`, même bloc) repérée comme risque similaire, pas encore traitée.
- 2026-09-18 (suite) : 4 nouvelles icônes SVG dessinées à la main (raie, dauphin, baleine, tortue), même style trait fin que les 5 existantes (pas de lib externe). Intégrées dans `obsIcon()` (marqueurs carte), `_phSvgs` (header popup), `_obsCardIcon` (cards éditeur). Bug corrigé au passage : le picker d'émojis de l'éditeur affichait encore les anciens émojis génériques pour les espèces ayant une icône dédiée — lookup factorisé dans `_obsSvgFor()`, nouveau `_pickerIcon()` branché sur le picker. Émoji 🪁 ajouté à `EMJS` pour la raie (aucun unicode dédié). Testé visuellement en local, déployé (2 commits sur `main`).
- 2026-09-18 (suite) : Photos ajoutées aux 2 observations Point Zéro « dauphins bleu et blanc » (1 photo par obs, upload Cloudinary + push `/api/sync`), vérifié en ligne. Photos rorqual (5), globicéphale (2) et plongée scientifique (2) reçues inline dans le chat plutôt qu'en pièce jointe — aucun fichier exploitable, redemandées au client.
- 2026-09-19 : Blocage photos rorqual/globicéphale/plongée (envoyées inline la veille, aucun fichier récupérable) levé — client a fourni les fichiers via dossiers locaux (`rorqual`, `globi`, `plongée` dans Téléchargements). Photos assignées : rorqual commun (2 obs — `DSC_5621` 2 individus, `DSC_5472` aileron + montagnes), globicéphale (1 obs — `DSC_5724`, ailerons au soleil couchant), plongée scientifique 30M (2 photos, galerie complète). Uploadées Cloudinary, poussées en direct (`/api/sync`), vérifié sur `map.naecoexpedition.org`. Reste sans photo côté Point Zéro : 2 raies Mobula et 1 tortue Caouanne.
- 2026-09-20 : Conception et plan validés pour une animation son+image "rorqual" (lecteur plein écran 80%, horloge Web Audio API sans dérive, ~100 photos mélangées aléatoirement, synchronisées sur un extrait de "Run Boy Run" de Woodkid en WAV, tempo réduit à 50% soit 0.4s/1s par photo) — droits musicaux réglés côté client, spec commitée (`docs/superpowers/specs/2026-09-20-rorqual-anim-player-design.md`), plan d'implémentation commité en 6 tâches (`docs/superpowers/plans/2026-09-20-rorqual-anim-player.md`). Exécution démarrée en mode inline : Task 1 (modèle de données `ANIM_BANKS`) en cours.
- 2026-09-20 (suite) : Tasks 1-5 du plan animation rorqual implémentées et vérifiées (modèle de données `ANIM_BANKS`, overlay UI plein écran 80%, moteur de lecture Web Audio avec pause/reprise exacte, Échap + pause auto si onglet en arrière-plan, point d'entrée dans la popup observation), commitées. Motif rythmique corrigé sur demande client en séquence positionnelle fixe (1s intro + 16×(6×0.4s/1×0.9s/4×0.4s/2×0.9s) = 108,2s), spec mise à jour. Fichier audio réel `Run Boy Run NAECO WAV.wav` (124s, l'outro après 108,2s garde la dernière photo figée) uploadé sur Cloudinary et branché dans `ANIM_BANKS.rorqual.audio`, vérifié en lecture réelle. Démo montrée au client en direct dans le navigateur. Reste en attente : les ~100 vraies photos rorqual (placeholder Cloudinary utilisé pour les tests) et Task 6 (écriture JSONbin de prod) toujours en pause, confirmation explicite du client requise avant envoi.
- 2026-09-20 (suite) : Animation rorqual déployée en ligne (photos placeholder + vrai son Run Boy Run) puis patch JSONbin de production appliqué (`anim:"rorqual"` sur les 2 observations réelles) — Task 6 terminée, carte "Voir l'animation" visible en prod. Désync son/image perçu par le client diagnostiqué : pas un bug d'horloge audio mais une contention du thread principal au chargement de la carte (1-4 img/s pendant ~19s, puis 60fps stable) ; anti-répétition consécutive de photos ajoutée à l'algorithme.
- 2026-09-20 (suite) : Motif rythmique de l'animation rorqual finalisé par itérations d'exports vidéo ffmpeg (calage son/image vérifié hors rendu navigateur, méthode désormais systématique pour ce type de réglage) — motif final `(A,B,C,C,C)×3 + C`, intro 1s, ~115,8s, poussé en prod. 33 vraies photos rorqual intégrées (remplacent les 5 placeholders), réparties en deux banques par durée de slot (5 dédiées aux slots 0,9s, 28 aux slots 0,4s). Lecteur rendu responsive mobile (ratio 3:4 sous 600px, 16:9 préservé desktop), poussé en prod. Reste en placeholder : l'image d'intro (1s, toujours la même à chaque lecture).
- 2026-09-21 : Calage son/image de l'animation rorqual passé sur `librosa` (beat-tracker MIR standard, programmation dynamique) au lieu du script maison — tempo détecté 132.51 BPM, motif manuel conservé (6 courtes/1 longue/4 courtes/2 longues ×8 phrases) mais chaque coupe calée sur le vrai timestamp de battement. Deux bugs trouvés et corrigés : (1) décalage systématique de ~22-35ms entre le pic d'énergie détecté et l'attaque réelle du son (corrigé par backtracking d'onset librosa, intro 0.981s → 0.946s), (2) images figées en aval causées par des formats/tailles pixel hétérogènes entre photos forçant ffmpeg à reconfigurer son filter graph à chaque changement (perte massive de frames) — fix par pré-normalisation de toutes les images à la même taille/format avant assemblage. Séquence complète rendue sur l'audio entier (124.03s, 208 images réparties sur 16 phrases), calage confirmé bon par le client sur les rendus finaux. Reste à faire : intégrer cette séquence complète dans `index.html` (jusqu'ici testée en rendu vidéo ffmpeg hors navigateur).
- 2026-09-21 (suite) : Méthode de calage `librosa` documentée dans `03_knowledge/patterns/sync-image-audio-beat-detection-librosa.md` (détection tempo/beats, correction du décalage pic/attaque, piège ffmpeg filter graph, méthode de vérification par hash de frames) + CSV complet de la séquence (209 lignes) en pattern réutilisable, tags `#pattern #code #validé`.
- 2026-09-21 (suite) : Séquence complète librosa intégrée dans `index.html` et poussée en prod (`18d1f1a`) — 207 durées de slots calées sur les vrais battements détectés, intro/outro fixes (coucher de soleil 0.95s → 16 phrases de vraies photos → lune figée 5.3s, images "OCEAN" fournies par le client recadrées pour retirer les bandes blanches Canva), crédit logo NAECO en position fixe affiché uniquement sur les vraies photos (masqué sur intro/outro). Nouveau piège ffmpeg au passage : `-shortest` ne se fie pas toujours à la vraie fin du flux vidéo si la durée est absente des métadonnées d'entrée (`N/A` sur un concat) — remplacé par une durée `-t` explicite pour forcer la coupe.
- 2026-09-21 (suite) : 3 ajustements visuels poussés en prod sur demande client — crédit logo agrandi de 100% (`a587cd7`), outro recadré + `object-position: 60%` pour garder la lune visible sur desktop (16:9) sans couper le logo (`5805975`), fond du lecteur à 50% d'opacité pour laisser la carte visible en transparence + vignette intro sur la carte d'accès + pause au clavier uniquement (barre espace, bouton retiré) (`91a4aeb`).
- 2026-09-21 (suite) : Bug de blocage au chargement (carte figée sur le splash screen, reproductible uniquement sur Brave en navigation normale) diagnostiqué et corrigé — cause réelle : `localStorage` obsolète propre au profil Brave (les Shields, piste initiale, ont été écartés), fix = `localStorage.clear()`. Documenté dans `03_knowledge/troubleshooting.md`. Écran de chargement du lecteur harmonisé avec le splash de la carte (logo NAECO + barres d'onde), poussé (`c11590f`).

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-carte
