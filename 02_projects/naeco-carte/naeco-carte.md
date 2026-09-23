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
- [ ] Activer le versioning JSONbin sur le bin naeco-carte (aucun retour arrière possible actuellement en cas d'écrasement — cause aggravante confirmée lors de l'incident de perte de données du 2026-09-23)
- [ ] Vérifier si le commit `4bc0499` a bien été amendé (mauvaise adresse email) + force-pushé sur `main`
- [ ] Custom domain `track.naecoexpedition.org` (optionnel) — la zone Cloudflare vue par `wrangler` ne correspond pas au bon compte, à refaire proprement si souhaité ; le Worker tourne déjà sur son URL `.workers.dev`, aucun impact fonctionnel
- [ ] Pousser le commit en attente (header mobile responsive `a75b2f2`)
- [ ] Supprimer les 14 points GPS parasites restants à Porto (dérives à pied du 12/09, 06h37-06h57 et 07h28-07h36 UTC) — commande `wrangler d1` prête, à exécuter côté client (classifieur anti-suppression-de-masse bloque l'agent)
- [ ] Migrer le logo NAECO (`PHOTO_LOGO_NAECO`, même bloc que le logo Ammo Visuals) de Google Drive vers Cloudinary
- [ ] Déployer la migration du logo Ammo Visuals vers Cloudinary (changement local uniquement pour l'instant)
- [ ] Régénérer la master key JSONbin (fuite historique dans `check-remote.sh`, découverte le 2026-09-23) puis `wrangler secret put JB_MASTER_KEY` sur naeco-carte ET naeco-site (secret partagé, même compte JSONbin)
- [ ] Ajouter un espace au-dessus du texte "VOIR LE FILM PHOTOGRAPHIQUE (2min)" de la vignette animation pour le décaler d'une ligne (demande client interrompue en fin de session du 2026-09-23, pas encore faite)
- [ ] Décider du sort des 5 photos globicéphales encore en portrait non pivotées (P1033286, P1033357, P1033382, P1033393, P1033394)
- [ ] Supprimer `naeco-carte-migration-test/` et `samples/` sur Cloudinary si confirmé inutile (proposé au client le 2026-09-23, pas encore confirmé)

## Journal
- 2026-09-21 (suite) : Méthode de calage `librosa` documentée dans `03_knowledge/patterns/sync-image-audio-beat-detection-librosa.md` (détection tempo/beats, correction du décalage pic/attaque, piège ffmpeg filter graph, méthode de vérification par hash de frames) + CSV complet de la séquence (209 lignes) en pattern réutilisable, tags `#pattern #code #validé`.
- 2026-09-21 (suite) : Séquence complète librosa intégrée dans `index.html` et poussée en prod (`18d1f1a`) — 207 durées de slots calées sur les vrais battements détectés, intro/outro fixes (coucher de soleil 0.95s → 16 phrases de vraies photos → lune figée 5.3s, images "OCEAN" fournies par le client recadrées pour retirer les bandes blanches Canva), crédit logo NAECO en position fixe affiché uniquement sur les vraies photos (masqué sur intro/outro). Nouveau piège ffmpeg au passage : `-shortest` ne se fie pas toujours à la vraie fin du flux vidéo si la durée est absente des métadonnées d'entrée (`N/A` sur un concat) — remplacé par une durée `-t` explicite pour forcer la coupe.
- 2026-09-21 (suite) : 3 ajustements visuels poussés en prod sur demande client — crédit logo agrandi de 100% (`a587cd7`), outro recadré + `object-position: 60%` pour garder la lune visible sur desktop (16:9) sans couper le logo (`5805975`), fond du lecteur à 50% d'opacité pour laisser la carte visible en transparence + vignette intro sur la carte d'accès + pause au clavier uniquement (barre espace, bouton retiré) (`91a4aeb`).
- 2026-09-21 (suite) : Bug de blocage au chargement (carte figée sur le splash screen, reproductible uniquement sur Brave en navigation normale) diagnostiqué et corrigé — cause réelle : `localStorage` obsolète propre au profil Brave (les Shields, piste initiale, ont été écartés), fix = `localStorage.clear()`. Documenté dans `03_knowledge/troubleshooting.md`. Écran de chargement du lecteur harmonisé avec le splash de la carte (logo NAECO + barres d'onde), poussé (`c11590f`).
- 2026-09-21 (suite) : diagnostic du blocage au chargement (Brave) affiné — le `localStorage` obsolète (`nobs`) documenté précédemment n'était qu'un symptôme corrélé, pas la cause réelle. Vraie cause trouvée : `buildObsPopup()` référençait `ANIM_BANKS` avant sa déclaration ~800 lignes plus loin dans `index.html` ; `renderObservations()` s'exécutait dès le chargement et plantait sur ce marqueur si l'observation rorqual (avec `anim` défini) était visible dès la première passe, bloquant tout le script derrière (donc le splash ne se cachait jamais). Fix par garde défensive, poussé (`94b3252`), testé en simulant exactement la condition de crash. Documenté dans `03_knowledge/troubleshooting.md`.
- 2026-09-21 (suite) : écran de chargement du lecteur d'animation harmonisé avec le splash de la carte (fond ivoire, logo NAECO foncé, icône cassée en haut à gauche retirée, texte vignette "Voir le film photographique (2min)" sur 3 lignes centrées), poussé (`64f5c80`).
- 2026-09-21 (suite) : montage de la vidéo animation « globicéphales » démarré sur demande client (42 photos fournies via Google Drive, même rythme que l'animation rorqual, intro/outro coucher de soleil/lune identiques, crédit logo NAECO) — en cours, pas encore poussé en prod.
- 2026-09-21 (suite) : upload des 44 photos globicéphales vers Cloudinary (2000px, résolution web), montage vidéo de la séquence (120.03s, gabarit rorqual) démarré ; preview qualité 800×450 jugée dégradée par le client — clarifié que ce rendu vidéo local (ffmpeg) ne sert qu'à valider le rythme et n'a aucun rapport avec la qualité vue en prod (l'animation affiche les photos sources en direct, pas un export vidéo), vérification qualité mise en pause sur demande client. Migration complète des photos de l'animation rorqual vers Cloudinary : 14 photos "drone 2025" ajoutées au pool 0,4s (`rorqual/short/drone/2025`), 5 photos "souffle" migrées de Drive vers Cloudinary (pool 0,9s, `rorqual/long/souffle`), 28 photos restantes du pool 0,4s d'origine migrées aussi (`rorqual/short/photos`) — plus aucune dépendance Google Drive pour cette animation, poussé (`f89348a`). Anciens dossiers Cloudinary plats orphelins (`rorqual/drone/2025`, `rorqual/souffle`), non supprimables sans clé API Cloudinary.
- 2026-09-21 (suite) : tracker Cloudflare Web Analytics créé pour `map.naecoexpedition.org` (sous-domaine non éligible à l'auto-injection Cloudflare) — snippet JS ajouté manuellement avant `</body>` dans `index.html`, poussé (`64f5c80..d1310e7`), déploiement auto via Cloudflare Workers Builds.
- 2026-09-23 : Incident de perte de données JSONbin découvert et résolu — toutes les clés sauf `observations` avaient disparu (expeditions, escales, sitesEtude, photos, pelagosData, stats, general). Cause trouvée : un plan d'implémentation obsolète (`docs/superpowers/plans/2026-09-20-rorqual-anim-player.md`, Task 6 Step 5) prescrivait un `PUT` brut vers JSONbin en croyant à tort patcher uniquement le champ `observations` — JSONbin ne fusionne pas par champ sur un PUT, ça remplace tout le bin. Restauré depuis une sauvegarde du 17/09 fusionnée avec les 29 observations courantes. Correctifs commités et poussés (`e6b2e4d`) : clé maître JSONbin en clair retirée de `check-remote.sh`, `CLAUDE.md` du repo mis à jour (fin de la doctrine "PUT brut avec clé maître", tout passe par `/api/sync`), avertissement ajouté au plan fautif. Sécurité : la clé maître JSONbin ayant fuité doit être régénérée — elle est partagée avec [[naeco-site]] (même compte JSONbin), donc `wrangler secret put JB_MASTER_KEY` à refaire sur les deux repos une fois la nouvelle clé générée (pas encore fait). Sauvegarde complète post-restauration committée et poussée (`backups/jsonbin_backup_2026-09-23.json`, `b06f58a`).
- 2026-09-23 (suite) : 6 nouveaux sites d'étude créés sur l'expédition Point Zéro (19-20/09, réutilisation des titres/contenus/photos de protocoles existants) — 2× "Prélèvement ADNe sub-surface", 2× "Filet Manta"/microplastique, 2× "Caméra sous-marine" (50M et 100M), positionnés sur le GPS réel du bateau au plus proche de chaque horaire (écart max 88s). 15 sites d'étude au total en ligne.
- 2026-09-23 (suite) : Écriture JSONbin sans mot de passe en clair fiabilisée — bug trouvé après une longue session de debug (mot de passe systématiquement refusé malgré confirmation manuelle) : `curl.exe` corrompt les guillemets d'un payload JSON passé depuis PowerShell, un bug connu de passage d'arguments aux binaires natifs, sans rapport avec le mot de passe lui-même. Fix : `Invoke-RestMethod` (natif PowerShell) à la place de `curl.exe` pour tout appel `/api/login`/`/api/sync`. Écriture directe désormais possible sans repasser par le terminal du client à chaque fois (mot de passe lu depuis la variable d'environnement `NAECO_EDIT_PASSWORD`, jamais dans le chat). Documenté dans `03_knowledge/troubleshooting.md`.
- 2026-09-23 (suite) : Réorganisation complète du stockage Cloudinary du "film photographique" (animations rorqual + globicéphales) — arborescence `naeco-carte/{rorqual,globilocephale}/{long,short}/...`, ajout de 16 photos "drone 2026" et de photos supplémentaires (souffle, photoantoine) au pool rorqual, renommage `short/photos` → `short/photoeditammo`, 74 fichiers orphelins nettoyés via le script de nettoyage (pattern documenté dans [[secrets-api-terminal-sans-clair]]). Animation globicéphales entièrement reconstruite (dossiers réorganisés depuis zéro, 93 photos au total réparties long/short, dont 2 lots drone) et branchée à l'observation "Globicéphale" (`anim: globicephale`) — poussé (`3cd12fa`, `f2ab700`, `cae265c`, `4b1dcb9`). Les 3 photos drone 2025 portrait (DJI-55/56/57) réintégrées pivotées en paysage.

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-carte
