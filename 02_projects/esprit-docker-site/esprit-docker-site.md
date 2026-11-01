---
tags: [project, encours, esprit-docker]
created: 2026-08-29
statut: encours
client: esprit-docker
body_synced: 2026-10-31
---

# esprit-docker-site

## Objectifs du projet
- Site e-commerce Next.js pour la vente de chapeaux (marque "Esprit Docker")
- Gros travail de gestion de catalogue produit : variantes visuelles (face/profil, couleurs type "sakura"), détourage/ombres, cohérence des visuels

## Livrables
- Site en production : [www.esprit-docker.com](https://www.esprit-docker.com)
- Pipeline de traitement d'images produit (scripts internes) : export pour Photoroom, correction d'ombres/reflets, feathering, dédoublonnage de variantes, audit de résolutions

## État actuel
- Site en production, légal à jour (mentions légales/CGU/CGV datées du 25 août 2026)
- Pipeline d'assets produit très développé (plusieurs dizaines de scripts `.mjs` de retouche/correction d'images) — probablement le vrai savoir-faire technique du projet
- Mail "colis expédié" (Brevo) en place depuis le 2026-09-02 : déclenché par le webhook Sendcloud, verrou anti-doublon `commandes.suivi_email_envoye_at` (migration faite sur Neon prod)
- Graphify actif sur le repo (1108 nœuds / 1673 edges) ; `.claude/settings.local.json` gitignored
- Volet Instagram en cours (2026-10-05) : `voice.md` des skills ig-* complété, `/ig-profile` 31/100, carousel « Composez votre docker » (8 slides) rédigé, à valider avant construction
- SEO / perf / a11y (2026-10-31) : corrections SEO du 28/10 + correctifs performance (hero rendu serveur, images via `images.esprit-docker.com`, WebP, cache statique 30 j) et accessibilité déployés en prod (commit `9c86356`) ; vérifié en ligne : 301 apex → www, sitemap 200, JSON-LD présent. LCP non remesuré après déploiement. Étape suivante : référencement (Search Console, mots-clés, contenu).
- Avis (2026-10-31) : ligne « ★★★★★ 4,9/5 · 239 évaluations Vinted » sous le bouton d'achat de toutes les fiches (commit `ba5d513`, en ligne) ; aucun texte d'avis Vinted repris (CGU Vinted). Fondu, onglet « Avis » et page `/avis` conçus, en attente d'une collecte d'avis propres.
- Modèle Steppe, ex-L'Essentielle (2026-10-31) : 21 photos en ligne (7 coloris × face/profil/dos ; script `scripts/essentiel-import-photos.mjs`, Orange Terracotta pour ce modèle, Orange Corail écartée côté serveur) ; bloc « Nouveau Docker » en tête de `/collection` déployé (commit `89fca47`, vérifié en ligne). Animations de la page Collection prêtes en local, non déployées.

## Décisions techniques
- **Stack** : Next.js (App Router), déploiement Cloudflare Pages (`@cloudflare/next-on-pages`, wrangler)
- **Stockage images** : Cloudflare R2 (`@aws-sdk/client-s3` en client S3-compatible)
- **Base de données** : Neon (PostgreSQL serverless, `@neondatabase/serverless`)
- **UI** : Base UI (`@base-ui/react`), Tailwind, GSAP pour les animations
- **PDF** : `pdf-lib` (probablement génération de factures/documents)
- **Traitement visuel produit** : pipeline de scripts Node custom (pas un service tiers) pour préparer/corriger les photos produit avant mise en ligne
- **Avis** : pas de reproduction des avis Vinted (CGU : copie interdite sans accord écrit) ni de lien vers le profil Vinted (prix différents) ; note de boutique seule, présentée comme note vendeur et jamais dans le JSON-LD Product. Collecte future : formulaire maison (Brevo + Neon) plutôt que Trustpilot gratuit ; Google Business Profile probablement inéligible (100 % en ligne).

## Blocages / risques
- Next.js non patché : `@cloudflare/next-on-pages` plafonne à Next 15.5.2, les correctifs de sécurité commencent à 15.5.15.
- Transformations d'images Cloudflare non activées : les variantes responsives des photos produit ne sont pas générées à la volée.

## Next actions
- [ ] Valider avec Morgane le texte du carousel « Composez votre docker » (8 slides, 1080x1350) avant construction des visuels
- [ ] Appliquer les corrections du score `/ig-profile` (31/100) côté Instagram : champ nom, bio FR non tronquée, 3 posts épinglés, highlights, Stories
- [ ] Remplir les 8 champs `À CONFIRMER` de `~/.claude/instagram/voice.md` (tutoiement/vouvoiement, mots interdits, ton, positions de marque) à partir des premiers Reels tournés
- [ ] Search Console : créer la propriété Domaine `esprit-docker.com` avec le compte Google Esprit Docker (TXT dans Cloudflare), ajouter Melvin en propriétaire, soumettre `https://www.esprit-docker.com/sitemap.xml` ; suivre l'indexation
- [ ] Vérifier que `images.esprit-docker.com` sert bien les images en prod, puis remesurer le LCP mobile (accueil, fiche, collection) après le déploiement du 31/10
- [ ] Mise à jour de sécurité Next.js bloquée : `next-on-pages` plafonne à 15.5.2, correctifs à partir de 15.5.15 — trouver une voie (migration adaptateur Cloudflare)
- [ ] Référencement : stratégie mots-clés (« casquette docker brodée », « casquette marin »…), concurrents FR, pages/contenus à créer, maillage, sources de backlinks
- [ ] Avis : collecter les avis propres du site (e-mail Brevo quelques jours après livraison → formulaire → table Neon → modération admin) pour alimenter le fondu, l'onglet « Avis » et la page `/avis` déjà conçus (spec `docs/superpowers/specs/2026-10-31-avis-vinted-design.md`)
- [ ] Google Shopping : répondre à la session dédiée (état des comptes Merchant Center / Search Console), puis flux produits automatique depuis Neon
- [ ] Mettre à jour la note Vinted affichée (`src/lib/avisVinted.ts`) de temps en temps
- [ ] L'Essentielle : valider la mise en corbeille R2 des PNG d'origine et versions intermédiaires inutilisées (`corbeille/produits/l-essentiel/…`) ; retirer le dos partagé en double sur Orange Terracotta si confirmé
- [ ] L'Essentielle : redirection de l'ancienne adresse `/l-essentiel/…` / `/l-essentielle/…` (404) vers `/collection/steppe` si des liens ont été partagés
- [ ] Mettre à jour le skill `set-image-espritdocker` (slugs avec tirets, cas sujet plus large que la cible : cible forcée + ombre atténuée avant recadrage) — accord Melvin en attente
- [ ] Steppe vert : récupérer les bons fichiers photo auprès de Melvin (le zip Photoroom (1) est identique à l'ancien) puis relancer `--remplacer`
- [ ] Déployer les correctifs Atelier mobile (« 66 combinaisons » centré, pastilles espacées)

## Journal
- 2026-08-29 : Repo identifié et analysé (`github.com/espritdocker/esprit-docker`), fiche projet créée
- 2026-09-02 : Fix mail de suivi colis Sendcloud (voir [[esprit-docker]] pour le détail du diagnostic) — ajout d'une note "vérifiez vos spams" dans `emailCommande.ts` et `succes/page.tsx`. Commit `944dca9` sur `master`.
- 2026-09-02 : Path B implémenté pour le mail "colis expédié" (voir [[esprit-docker]] pour le diagnostic complet) — `emailExpedition.ts` (envoi Brevo, même charte que la confirmation) + hook dans le webhook Sendcloud + colonne `commandes.suivi_email_envoye_at` (verrou anti-doublon). Migration exécutée et vérifiée sur Neon prod (projet `esprit-docker`, branche `production`). Commit+push `20a6fc6` sur `master`.
- 2026-09-04 : Graphify (graphe de code tree-sitter, voir `03_knowledge/outils.md`) installé et activé — 1108 nœuds/1673 edges, nudge `/graphify` actif en session. `.claude/settings.json` renommé en `.claude/settings.local.json` + gitignored (le hook contient un chemin `graphify.exe` propre à la machine de Melvin, à ne jamais committer).
- 2026-10-05 : voice.md des skills ig-* complété depuis le profil Instagram (lu dans Chrome, lecture seule) ; langue FR, CTA `DOCKER`. `/ig-profile` : 31/100. Carousel « Composez votre docker » (8 slides) rédigé, à valider avant construction.
- 2026-10-28 : Audit SEO (Lighthouse SEO 100, mais apex/www en double, pas de canonical ni JSON-LD, sitemap 500 intermittente) ; corrections écrites dans le repo (301 apex → www, canonicals, JSON-LD Product/Organization, sitemap à repli, noindex zones privées, titres « casquette docker ») — tsc OK, non commitées ni déployées.
- 2026-10-31 : Audit perf/a11y (LCP mobile : accueil 3,5 s, fiche 2,7 s, collection 5,0 s) et correctifs (hero rendu serveur, images via images.esprit-docker.com, WebP, cache 30 j, a11y) ; flou du hero adouci (2 s → 4 s). Tout déployé avec les corrections SEO du 28/10 : commit 9c86356, vérifié en ligne (301 apex → www, sitemap 200, JSON-LD).
- 2026-10-31 : Avis Vinted : recopie des textes abandonnée (CGU Vinted : pas de reproduction sans accord écrit) ; ligne « ★★★★★ 4,9/5 · 239 évaluations Vinted » ajoutée sous le bouton d'achat de toutes les fiches (src/lib/avisVinted.ts), déployée (ba5d513) et vérifiée desktop + mobile. Spec avis (fondu, onglet, page /avis) gardée pour une collecte d'avis propres.
- 2026-10-31 : Nouveau modèle L'Essentielle : photos des 4 coloris normalisées au format catalogue (WebP ~180 Ko au lieu de PNG 2,8 Mo) + dos, publiées en R2/Neon ; Orange Corail remplacé par « Orange Terracotta » pour ce modèle ; bloc « Nouvelle collection » en tête de /collection et masquage des couleurs non proposées codés, vérifiés en local, non déployés.
- 2026-10-31 : L'Essentielle : 21 photos (7 couleurs × face/profil/dos, vrais dos partout) en ligne, transparence reconstruite depuis les PNG à fond blanc, script `scripts/essentiel-import-photos.mjs` ; en-tête du bloc « Nouvelle collection » refait (« NOUVELLE » / « COLLECTION » en diagonale 45° de chaque côté de la carte), vérifié desktop, non déployé.
- 2026-10-31 : Modèle L'Essentielle renommé « Steppe » (Orange Corail écartée côté serveur), bloc « Nouveau Docker » de /collection finalisé et déployé (89fca47, vérifié en ligne) ; descriptions des 13 modèles mises à jour ; animations de la page Collection prêtes, non déployées.
- 2026-10-31 : Section « Nouveau docker » Steppe sur l'accueil, finitions fiche produit (logo, note Vinted, bouton retour), prix minimum corrigé, Steppe/Terracotta retirés de l'Atelier — déployé (`0be017b`, `c37a609`, `a01e609`) ; correctifs Atelier mobile prêts en local

## Liens
- Client : [[esprit-docker]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
- Repo / deployment : https://github.com/espritdocker/esprit-docker (Cloudflare Pages, R2, Neon)
