---
tags: [project, encours, esprit-docker]
created: 2026-08-29
statut: encours
client: esprit-docker
body_synced: 2026-11-05
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
- SEO / perf / a11y (2026-10-31) : corrections SEO du 28/10 + correctifs performance (hero rendu serveur, images via `images.esprit-docker.com`, WebP, cache statique 30 j) et accessibilité déployés en prod (commit `9c86356`) ; vérifié en ligne : 301 apex → www, sitemap 200, JSON-LD présent. Depuis le 2026-11-02, transformations d'images Cloudflare activées (photos produit en AVIF, ~20× plus légères ; 404 sur logo/photos d'ambiance de l'accueil corrigé, `d5e247f`). LCP non remesuré.
- Avis (2026-10-31) : la ligne « ★★★★★ 4,9/5 · 239 évaluations Vinted » (`ba5d513`) a été retirée le 2026-11-02 : Vinted est masqué du site (aucun lien, `avisVinted.ts` supprimé, URL retirée des données structurées, `179db63`, vérifié en ligne). Fondu, onglet « Avis » et page `/avis` conçus, en attente d'une collecte d'avis propres.
- Modèle Steppe, ex-L'Essentielle (2026-10-31) : 21 photos en ligne (7 coloris × face/profil/dos ; script `scripts/essentiel-import-photos.mjs`, Orange Terracotta pour ce modèle, Orange Corail écartée côté serveur) ; bloc « Nouveau Docker » en tête de `/collection` déployé (commit `89fca47`, vérifié en ligne). Animations de la page Collection prêtes en local, non déployées. Redirection 301 steppe → origine en prod (2026-11-02).
- Section `/guides` en MDX livrée (2026-11-02, commit `120692f`, brouillons exclus, sitemap conditionnel), durcie contre un guide mal formé (404) ; guide « porter une casquette docker » publié et en ligne (`4dc44ad`, au sitemap, IndexNow envoyé)
- Provenance des ventes (2026-11-02, commit `1094ebf`) : compteur anonyme mois × canal × page (option B, rien envoyé à Mollie), migration SQL appliquée sur Neon ; 73 méta descriptions uniques et onglets Livraison/Entretien dans le HTML. Lot SEO/GEO groupé en prod le 2026-11-02 (`58f1097` : À propos/FAQ, flux Merchant 73 produits, redirection Steppe → Origine) ; IndexNow envoyé, sitemap soumis, Search Console (propriété Domaine validée) et Bing Webmaster Tools branchés. Point zéro GEO : marque citée 2 fois sur 30, seulement à la question contenant son nom. Positions Google : n°1 sur la marque seule.
- Search Console (2026-11-05) : seule « esprit docker » fait apparaître le site (11 affichages, 6 clics, position 1), aucune page ne cible les recherches à volume (« casquette sans visière », « marin », « docker ») ; titres des 73 fiches (« Casquette docker … ») et H1/intro de la Collection faits et commités (non encore déployés, accord requis), 2 guides (dont « bonnet docker ») en brief
- Merchant Center (2026-11-05) : flux lu chaque nuit depuis le site ; 8 casquettes approuvées, 65 en visibilité limitée (examen des photos), 0 refusée ; 3 premiers clics Google Shopping
- CNIL (2026-11-05) : le compteur anonyme de ventes par canal est probablement hors exemption (outil d'auto-évaluation CNIL 07/2025)

## Décisions techniques
- **Stack** : Next.js (App Router), déploiement Cloudflare Pages (`@cloudflare/next-on-pages`, wrangler)
- **Stockage images** : Cloudflare R2 (`@aws-sdk/client-s3` en client S3-compatible)
- **Base de données** : Neon (PostgreSQL serverless, `@neondatabase/serverless`)
- **UI** : Base UI (`@base-ui/react`), Tailwind, GSAP pour les animations
- **PDF** : `pdf-lib` (probablement génération de factures/documents)
- **Traitement visuel produit** : pipeline de scripts Node custom (pas un service tiers) pour préparer/corriger les photos produit avant mise en ligne
- **Avis** : Vinted masqué du site (2026-11-02) : plus aucune note, mention ni lien Vinted (sameAs inclus), pas de reproduction des avis (CGU : copie interdite sans accord écrit). Collecte future : formulaire maison (Brevo + Neon) plutôt que Trustpilot gratuit ; Google Business Profile probablement inéligible (100 % en ligne).
- **Positionnement de marque** : Morgane personnalise des casquettes de base (jamais « fabrique ») ; logo brodé à Bordeaux (« Sud-Ouest » pour éviter la répétition), atelier à Gauriaguet, base fabriquée en Asie ; nom de Morgane public.

## Blocages / risques
- Next.js non patché : `@cloudflare/next-on-pages` plafonne à Next 15.5.2, les correctifs de sécurité commencent à 15.5.15.
- CNIL : le compteur anonyme de ventes par canal est probablement hors exemption.
- Merchant Center : 65 produits sur 73 en visibilité limitée (examen des photos).

## Next actions
- [ ] Valider avec Morgane le texte du carousel « Composez votre docker » (8 slides, 1080x1350) avant construction des visuels
- [ ] Appliquer les corrections du score `/ig-profile` (31/100) côté Instagram : champ nom, bio FR non tronquée, 3 posts épinglés, highlights, Stories
- [ ] Remplir les 8 champs `À CONFIRMER` de `~/.claude/instagram/voice.md` (tutoiement/vouvoiement, mots interdits, ton, positions de marque) à partir des premiers Reels tournés
- [ ] Search Console : suivre l'indexation (propriété Domaine validée, sitemap soumis) ; rédiger le référencement des recherches à volume
- [ ] Remesurer le LCP mobile (accueil, fiche, collection) après activation des transformations d'images Cloudflare
- [ ] Mise à jour de sécurité Next.js bloquée : `next-on-pages` plafonne à 15.5.2, correctifs à partir de 15.5.15 — trouver une voie (migration adaptateur Cloudflare)
- [ ] Référencement : stratégie mots-clés (« casquette docker brodée », « casquette marin »…), concurrents FR, pages/contenus à créer, maillage, sources de backlinks
- [ ] Avis : collecter les avis propres du site (e-mail Brevo quelques jours après livraison → formulaire → table Neon → modération admin) pour alimenter le fondu, l'onglet « Avis » et la page `/avis` déjà conçus (spec `docs/superpowers/specs/2026-10-31-avis-vinted-design.md`)
- [ ] L'Essentielle : valider la mise en corbeille R2 des PNG d'origine et versions intermédiaires inutilisées (`corbeille/produits/l-essentiel/…`) ; retirer le dos partagé en double sur Orange Terracotta si confirmé
- [ ] Mettre à jour le skill `set-image-espritdocker` (slugs avec tirets, cas sujet plus large que la cible : cible forcée + ombre atténuée avant recadrage) — accord Melvin en attente
- [ ] Steppe vert : récupérer les bons fichiers photo auprès de Melvin (le zip Photoroom (1) est identique à l'ancien) puis relancer `--remplacer`
- [ ] Déployer les correctifs Atelier mobile (« 66 combinaisons » centré, pastilles espacées)
- [ ] seo-geo : vérifier le compte DataForSEO (401, compte non vérifié) ; facultatif, le premier rechargement est de 50 USD
- [ ] Search Console : activer l'API sur le projet Google Cloud `seo-geo-513517` (collecte GSC en 403), ajouter l'adresse Blue Impakt en Complet, décommenter `GSC_SERVICE_ACCOUNT_JSON` dans `seo-geo/.env` si ce n'est pas fait
- [ ] Chantier marque pour les moteurs (marque citée 2 fois sur 30, seulement quand son nom est dans la question) : indexation, fiche d'établissement Google, mentions externes (Instagram, annuaires), JSON-LD Organization
- [ ] Annuaires : vérifier l'inscription Créateurs Français et LesCréatrices.fr et le compte Pinterest (alignés sur la phrase de marque le 2026-11-02, inscription effective non confirmée)
- [ ] Aligner la phrase de marque dans `PageAccueil.tsx` (« Assemblé à la main à Bordeaux », « Pose et finition main à Bordeaux », « …dans le Sud-Ouest à Bordeaux »)
- [ ] Merchant Center : 65 produits en visibilité limitée (examen des photos) — suivre l'approbation, corriger le flux/photos si besoin
- [ ] CNIL : trancher pour le compteur de ventes par canal (validation juriste, consentement ou retrait) avant tout autre client — probablement hors exemption
- [ ] Guides (casquette marin, bonnet docker, casquette sans visière) : envoyer à Morgane les 10 questions distinctes des 3 `a-valider.md`, puis remplacer les marqueurs, passer chaque guide en `brouillon: false` et redéployer
- [ ] Cohérence « Asie » : À propos et FAQ disent encore la casquette de base « fabriquée industriellement en Chine » (profil : jamais plus précis qu'« Asie ») et les descriptions produit en base disent « brodé dans le Sud-Ouest… » ; à aligner

## Journal
- 2026-11-02 : SEO/GEO en prod sur `master` (e749994, 6 min Cloudflare, vérifié, IndexNow 19 URL HTTP 202) ; GEO manuel 0 citation sur 30 (ChatGPT, Perplexity, Gemini) ; flux Merchant Center 73 produits (`feat/flux-merchant`, 8609d8b) et pages `/a-propos` + `/faq` (`feat/pages-a-propos-faq`, 125cf8d) prêts, non déployés ; réponses de Morgane intégrées, guide prêt à publier
- 2026-11-02 : Phrase de marque corrigée (logo brodé à Bordeaux, bijou cousu à la main en Gironde) dans JSON-LD, layout, méta accueil et /collection, commit dee8675 sur feat/pages-a-propos-faq ; reste PageAccueil.tsx et les profils externes
- 2026-11-02 : GEO manuel : série Perplexity jugée non fiable (10 questions dans une seule conversation), remesure question par question en navigateur intégré en cours ; `feat/pages-a-propos-faq` fusionnée en avance rapide dans `feat/seo-geo-attribution-guides` (43 tests verts), non déployée ; Merchant Center : retours 14 jours et livraison (Colissimo dès 100 €, Mondial Relay) corrigés
- 2026-11-02 : Bing Webmaster Tools branché (import Search Console, sitemap soumis à la main, accueil indexé) ; Merchant Center : retours, livraison et flux de 73 produits importés, en attente d'examen Google ; GEO manuel remesuré question par question (ChatGPT fait, Gemini en cours)
- 2026-11-02 : Morgane personnalise des casquettes de base (jamais « fabrique ») : formules corrigées dans les documents annuaires, profil et plan d'entité ; lieu de marque = « Bordeaux » par défaut, « Sud-Ouest » pour éviter la répétition.
- 2026-11-02 : GEO manuel final (question par question, sans compte) : marque citée 2 fois sur 30, seulement à la q10 contenant son nom ; redirection 301 steppe → origine testée (`2bb3abe`, branche `fix/redirection-steppe`), déploiement groupé avec À propos/FAQ et flux Merchant en attente du feu vert.
- 2026-11-02 : Lot groupé en prod (`58f1097` : À propos/FAQ, flux Merchant 73 produits, redirection Steppe → Origine), vérifié, IndexNow envoyé, sitemap soumis à la Search Console ; Merchant Center lit désormais le flux du site chaque nuit (flux manuel supprimé), approbation à vérifier le 5/11.
- 2026-11-02 : Guide « porter une casquette docker » publié et poussé sur `master` (`4dc44ad`) ; atelier à Gauriaguet, logo brodé à Bordeaux, base fabriquée en Asie ; décision : plus aucun lien Vinted (sameAs inclus), à confirmer.
- 2026-11-02 : Vinted masqué du site (boutique toujours active mais invisible des clients, aucun lien) : note « ancienne boutique » et `avisVinted.ts` supprimés, URL retirée des données structurées (`179db63`), vérifié en ligne (0 mention) ; guide `/guides/porter-casquette-docker` en ligne, au sitemap, IndexNow envoyé ; nom de Morgane public, annuaires/Instagram/Pinterest alignés sur la phrase de marque (`36c690f`)
- 2026-11-02 : Transformations d'images Cloudflare activées (variable via `.env.production`, `aba44d1`) : photos produit en AVIF (~20× plus légères) mais logo et photos d'ambiance de l'accueil en 404 (slash en trop), corrigé et poussé (`d5e247f`), revérification en cours ; indexation demandée dans Search Console pour `/a-propos`, `/faq` et le guide
- 2026-11-05 : Search Console : seule « esprit docker » fait apparaître le site (11 affichages, 6 clics, position 1), aucune page ne cible les recherches à volume (« casquette sans visière », « marin », « docker ») ; chantier lancé : titres des 73 fiches (« Casquette docker … ») et H1/intro de la Collection faits et commités, 2 guides (dont « bonnet docker ») en brief
- 2026-11-05 : Merchant Center : 8 casquettes approuvées, 65 en visibilité limitée (examen des photos), 0 refusée ; 3 premiers clics Google Shopping ; point CNIL ouvert : le compteur anonyme de ventes par canal est probablement hors exemption (outil d'auto-évaluation CNIL 07/2025)
- 2026-11-05 : FAQ et À propos corrigées (bonnet docker pas en maille) ; audits des briefs marin et bonnet rendus (affirmation « laine = bonnet » contredite par les données), corrections lancées
- 2026-11-05 : 3 guides en brouillon rédigés (casquette marin, bonnet docker, casquette sans visière) après correction des briefs ; 54 tests et build OK sur feat/recherches-volume, rien poussé, guides masqués en attendant les réponses de Morgane
- 2026-11-05 : Titres/descriptions des 73 fiches (« Casquette docker … »), H1 + intro de /collection et réponse bonnet docker en FAQ en production (`master` e0fab3e, fast-forward de 4 commits), vérifié en ligne, IndexNow 23 URL (HTTP 200) ; 3 guides toujours en 404 et hors sitemap tant que Morgane n'a pas répondu (10 questions)

## Liens
- Client : [[esprit-docker]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
- Repo / deployment : https://github.com/espritdocker/esprit-docker (Cloudflare Pages, R2, Neon)
