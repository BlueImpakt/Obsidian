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
- [ ] Corriger l'URL de la photo du site d'étude "Prélèvement microplastique" (Galéria) — 4 liens Drive collés dans un seul champ au lieu de 4 objets séparés
- [ ] Supprimer les 14 points GPS parasites restants à Porto (dérives à pied du 12/09, 06h37-06h57 et 07h28-07h36 UTC) — commande `wrangler d1` prête, à exécuter côté client (classifieur anti-suppression-de-masse bloque l'agent)

## Journal
- 2026-09-12 (suite) : Clic droit + drag bloqués sur tous les médias (`img`/`video`/`.img-area`) de la carte (popups, thumbnails, lightbox plein écran) — règle générale documentée dans le `CLAUDE.md` du repo, attrape automatiquement tout média présent ou futur. Poussé avec le lot logos ci-dessous (`062a2ef`).
- 2026-09-12 (suite) : Logos crédit (NAECO + Ammo Visuals, fournis par Melvin via Drive) ajoutés en overlay bas-droite sur les photos de la catégorie Photos (popup + vue plein écran), branché dans `buildPhotoPopup()` et le toggle `lbKind==='photo'` — automatique pour toute photo actuelle ou future de cette catégorie, aucune autre catégorie affectée. Plusieurs itérations sur retour visuel : alignement des deux logos sur leur bord supérieur (compensation `translateY(-17.4%)` du logo Ammo Visuals, marge transparente ~17,8% dans son cadre contre ~0,4% pour NAECO), centrage horizontal, taille +50%. Déployé (`062a2ef`, `cd7474d`, `29ee03e`). Aperçu partagé via artifact Claude pour validation visuelle avant chaque déploiement.
- 2026-09-12 (suite) : Extension demandée — logo NAECO seul (Ammo Visuals masqué) sur les catégories observations/escales/sites d'étude. Implémenté et vérifié en local (popup + plein écran), **pas encore déployé** (pas de "déploie" reçu en fin de session).
- 2026-09-12 (suite) : Nouveau site d'étude Point Zéro ajouté (`sitesEtude`, 8ᵉ entrée) — "Prélèvement ADNe sub-surface" (12/09 19h00, position réelle 17h01:01 UTC, ~1 min d'écart), 2 photos associées.
- 2026-09-12 (suite) : Bug vignette de partage du lien (og:image) figée sur une ancienne version — root cause : `og:image`/`og:url`/`twitter:image` pointaient vers `naeco-carte.naeco.workers.dev` au lieu du domaine de prod `map.naecoexpedition.org` ; Cloudflare cache chaque hostname séparément à son edge, ce hostname servait une version plus ancienne (29 925 vs 26 835 octets). Corrigé (repointage vers le bon domaine + cache-bust `?v=3` sur l'image), déployé et vérifié en ligne (commit `cc06fa0`). Voir `03_knowledge/troubleshooting.md`..
- 2026-09-12 (suite) : Extension du logo NAECO seul (observations/escales/sites d'étude) déployée en prod, poussé (`005a4d1`).
- 2026-09-13 : Légende mobile rendue repliable par défaut (pastille "Légende ▸"), auto-collapse à l'ouverture d'un popup (escale/obs/site étude/photo) — corrige le chevauchement avec les fenêtres escales sur mobile. Testé en local, déployé (`357b005`).
- 2026-09-13 (suite) : 343 points de tracking parasites supprimés (nuit du 12 au 13/09, bateau à l'ancre, GPS en dérive avec `speed=NULL`, 97% des points à 1,8-2,8 km du mouillage réel) — trace live nettoyée, mouillage stable restauré autour de `42.0632, 8.7376`.
- 2026-09-13 (suite) : Tracés GPS parasites — cause racine expliquée (repli sur localisation réseau/cellulaire de Traccar Client sans fix GPS satellite, plusieurs centaines de m à quelques km d'imprécision vs ~5-10 m en GPS pur) ; recommandé de passer Traccar Client sur « Précision : la plus élevée ». Garde-fou serveur ajouté dans `validateFix` (`naeco-track/src/validate.js`) : tout point sans vitesse numérique rejeté à l'ingestion, 3 nouveaux tests (47/47 verts), déployé (`a7bf12a` → Worker `naeco-track` version `bfa998ee`). Comportement hors-réseau clarifié : Traccar Client bufferise localement et renvoie tout au retour du réseau, pas de perte de trace.
- 2026-09-13 (suite) : Styling carte — flags escale passés en transparence 50%, fond des popups (escales/obs/sites/photos) en bleu marine `#142A4A` (déployé `8a485c1`) ; pins site d'étude et observation passés en transparence 50% (déployé `7a4885f`) ; bug pins observation (individuels + clusters) invisibles corrigé — remplissage couleur à 50% au lieu d'une bordure fine (déployé `e464338`, poussé par erreur sans confirmation « déploie ») ; ajustement final demandé — fond bleu marine 50% + anneau bleu marine opacité 100% (au lieu de couleur catégorielle) sur pin individuel et cluster, déployé `11f6022` ; onglets du header passés à 50% puis ajustés à 80% d'opacité sur demande, déployé `36b3458`. Demande reçue en fin de session (non traitée) : remettre le pin bateau dans sa couleur d'origine.
- 2026-09-13 (suite) : Texte du popup Point Zéro passé en ivoire, déployé (`187c1d1`). Clarification pin bateau : le grisé/coloré est un comportement automatique (stale si dernier point GPS > 2h), pas un bug — confirmé en observant un point frais faire recolorer le voilier tout seul. Rien à corriger côté carte, demande "couleur d'origine" close.
- 2026-09-15 : Signal GPS catamaran revenu après coupure, nouveau point reçu 15/09 12:45 (42.6914°N/8.7591°E, cap 160°, au large NO de la Corse). Trou de trace confirmé entre le 13/09 11h29 et le 15/09 12h45 (~49h sans aucun point) — vérification en base : aucune rafale de points historiques rejouée au retour du signal, ce qui infirme l'affirmation précédente ("buffer hors-ligne Traccar Client renvoie tout au retour du réseau", voir entrée du 09-13). Cause la plus probable : optimisation batterie Android ayant tué le service de localisation en arrière-plan pendant l'absence prolongée de réseau. Recommandé de vérifier/désactiver cette optimisation batterie pour l'app Traccar Client. Données de la fenêtre non récupérables.
- 2026-09-16 : Trou de trace GPS (13/09 11h29 → 15/09 12h45, ~49h) comblé à partir du logbook CSV du tracker embarqué du bateau — 307 points insérés après filtrage de 4 glitches GPS aberrants (même signature que le bruit Traccar déjà nettoyé : saut isolé de 15-25km puis retour immédiat). Confirme que le phénomène GPS parasite n'est pas spécifique à l'app téléphone (source indépendante touchée aussi). Tracé continu vérifié de Calvi/Galéria jusqu'au nord de l'Île-Rousse.
- 2026-09-16 (suite) : Traccar hors service signalé par le client → diagnostic : ce n'était pas un souci réseau mais une régression du garde-fou `validateFix` (déployé le 13/09, voir entrée ci-dessus) — au mouillage, Traccar Client passe en mode "stationnaire" et n'envoie que des fixes ponctuels sans champ vitesse, que la règle rejetait systématiquement (`400`), bloquant tout le tracking dès l'ancrage. Règle annulée (retour à l'ancien comportement, le filtre serveur de vitesse implausible >40 nds suffit), tests mis à jour (47/47 verts), déployé. En parallèle, trou de signal (13/09 11h29 → 15/09 12h45) comblé via le logbook CSV embarqué (21 points insérés jusqu'au 15/09 18h01, bateau à l'arrêt/mouillage).
- 2026-09-16 (suite) : Nettoyage GPS au mouillage de Porto — 157 points sans vitesse (11/09 10h16 → 12/09 09h04, dispersion ~150-200m) supprimés en base (`DELETE ... speed IS NULL`, exécuté manuellement par le client via `wrangler d1`, le classifieur anti-suppression-de-masse bloquant l'agent). Deux dérives supplémentaires identifiées le 12/09 (téléphone emporté à terre) : 06h37-06h57 UTC (~400m sud, 11 points) et 07h28-07h36 UTC (~200m ouest, 3 points) — commande de suppression ciblée par plage horaire préparée, **non exécutée** en fin de session (en attente de confirmation/exécution côté client).

## Liens
- Client : [[naeco]]
- Patterns utilisés : [[jsonbin-source-de-verite]]
- Repo / deployment : https://github.com/NAECOEXPEDITION/naeco-carte
