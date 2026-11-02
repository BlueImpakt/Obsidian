---
tags: [project, encours, esprit-docker]
created: 2026-08-29
statut: encours
client: esprit-docker
body_synced: 2026-11-02
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
- Section `/guides` en MDX livrée (2026-11-02, commit `120692f`, brouillons exclus, sitemap conditionnel), durcie contre un guide mal formé (404) ; premier guide « porter une casquette docker » en brouillon
- Provenance des ventes (2026-11-02, commit `1094ebf`) : compteur anonyme mois × canal × page (option B, exemption CNIL, rien envoyé à Mollie), migration SQL déjà appliquée sur Neon ; 73 méta descriptions uniques et onglets Livraison/Entretien dans le HTML ; branches `feat/seo-geo-attribution-guides` et `feat/outil-seo-geo` non déployées, non poussées. Point zéro GEO : la marque n'est citée dans aucune des 32 réponses de Claude

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
- [ ] Mettre à jour la note Vinted affichée (`src/lib/avisVinted.ts`) de temps en temps
- [ ] L'Essentielle : valider la mise en corbeille R2 des PNG d'origine et versions intermédiaires inutilisées (`corbeille/produits/l-essentiel/…`) ; retirer le dos partagé en double sur Orange Terracotta si confirmé
- [ ] L'Essentielle : redirection de l'ancienne adresse `/l-essentiel/…` / `/l-essentielle/…` (404) vers `/collection/steppe` si des liens ont été partagés
- [ ] Mettre à jour le skill `set-image-espritdocker` (slugs avec tirets, cas sujet plus large que la cible : cible forcée + ombre atténuée avant recadrage) — accord Melvin en attente
- [ ] Steppe vert : récupérer les bons fichiers photo auprès de Melvin (le zip Photoroom (1) est identique à l'ancien) puis relancer `--remplacer`
- [ ] Déployer les correctifs Atelier mobile (« 66 combinaisons » centré, pastilles espacées)
- [ ] seo-geo : vérifier le compte DataForSEO (401, compte non vérifié) ; facultatif, le premier rechargement est de 50 USD
- [ ] Search Console : cliquer sur « Valider » (TXT DNS déjà en place), ajouter l'adresse Blue Impakt en Complet, créer le projet Google Cloud et le compte de service (clé dans `C:\Users\LENOVO\secrets\gsc-seo-geo.json`), l'ajouter en Restreint, décommenter `GSC_SERVICE_ACCOUNT_JSON` dans `seo-geo/.env`
- [ ] Chantier marque pour les moteurs (Claude ne cite Esprit Docker dans aucune des 32 réponses) : indexation, fiche d'établissement Google, mentions externes (Vinted, Instagram, annuaires), JSON-LD Organization
- [ ] Annuaires : inscrire Créateurs Français et LesCréatrices.fr, créer le compte Pinterest (rien inscrit à ce jour)
- [ ] Aligner la phrase de marque dans `PageAccueil.tsx` (« Assemblé à la main à Bordeaux », « Pose et finition main à Bordeaux », « …dans le Sud-Ouest à Bordeaux ») une fois la modification en cours terminée, puis sur Instagram, annuaires et Merchant Center
- [ ] Poser à Morgane : qui fabrique les casquettes de base et où ; accepte-t-elle que son nom soit public
- [ ] Merchant Center : vérifier l'approbation des 73 produits vers le jeudi 5/11 (tâche programmée à 10 h), corriger le flux si refus
- [ ] Vérifier en ligne `/guides/porter-casquette-docker` puis `npm run indexnow` pour le guide
- [ ] Retirer l'URL Vinted de `PROFILS_MARQUE` (`src/lib/seo.ts:21`) et du test `seo.test.ts`, si Melvin confirme ; vérifier la formule « ancienne boutique » de la note Vinted

## Journal
- 2026-11-02 : Outil SEO/GEO `seo-geo` cadré avec Esprit Docker en pilote (spec + 2 plans) ; côté site, provenance des ventes (tâches 1 à 3) validée en relecture, section `/guides` en cours ; migration à passer avant déploiement, point CNIL à trancher
- 2026-11-02 : Section `/guides` en MDX livrée (commit 120692f, brouillons exclus, sitemap conditionnel), vérifiée dans le navigateur ; durcissement en cours contre un guide mal formé.
- 2026-11-02 : Revue finale branche attribution + /guides : défaut critique Safari < 16.4 (lookbehind regex) corrigé en vague finale ; « Steppe » = modèle Origine déjà au sitemap ; consentement CNIL (provenance) à trancher avant déploiement
- 2026-11-02 : Vague finale de corrections de la revue de branche terminée (lookbehind regex supprimé pour Safari < 16.4, 28 tests verts, build propre), non poussée ; reste migration SQL provenance et point CNIL avant déploiement
- 2026-11-02 : pilote de l'outil seo-geo sur Esprit Docker : audit technique rangé (images mobile lourdes, même méta sur les 13 fiches, Livraison/Entretien invisibles dans le HTML initial), brief du guide « porter-casquette-docker » audité et corrigé, rédaction à venir
- 2026-11-02 : Provenance des ventes passée en compteur anonyme (option B, exemption CNIL, rien envoyé à Mollie, opposition dans « Gérer mes cookies », textes légaux réécrits ; commit 1094ebf) ; migration SQL appliquée sur Neon avec compte de lecture seule `seo_geo_lecture` ; point zéro GEO : Claude ne cite Esprit Docker dans aucune des 32 réponses, mesure sur Sonnet 5.5 (~1,70 $/mois) ; 73 méta descriptions uniques et onglets Livraison/Entretien dans le HTML ; premier guide « porter une casquette docker » en brouillon ; branches non déployées
- 2026-11-02 : Search Console : propriété Domaine validée en DNS, compte de service `seo-geo` créé et ajouté, clé rangée hors repo ; collecte GSC en 403 tant que l'API n'est pas activée sur le projet `seo-geo-513517`. Positions Google mesurées : n°1 sur la marque seule, absent du top 10 sur 21 autres mots-clés.
- 2026-11-02 : SEO/GEO en prod sur `master` (e749994, 6 min Cloudflare, vérifié, IndexNow 19 URL HTTP 202) ; GEO manuel 0 citation sur 30 (ChatGPT, Perplexity, Gemini) ; flux Merchant Center 73 produits (`feat/flux-merchant`, 8609d8b) et pages `/a-propos` + `/faq` (`feat/pages-a-propos-faq`, 125cf8d) prêts, non déployés ; réponses de Morgane intégrées, guide prêt à publier
- 2026-11-02 : Phrase de marque corrigée (logo brodé à Bordeaux, bijou cousu à la main en Gironde) dans JSON-LD, layout, méta accueil et /collection, commit dee8675 sur feat/pages-a-propos-faq ; reste PageAccueil.tsx et les profils externes
- 2026-11-02 : GEO manuel : série Perplexity jugée non fiable (10 questions dans une seule conversation), remesure question par question en navigateur intégré en cours ; `feat/pages-a-propos-faq` fusionnée en avance rapide dans `feat/seo-geo-attribution-guides` (43 tests verts), non déployée ; Merchant Center : retours 14 jours et livraison (Colissimo dès 100 €, Mondial Relay) corrigés
- 2026-11-02 : Bing Webmaster Tools branché (import Search Console, sitemap soumis à la main, accueil indexé) ; Merchant Center : retours, livraison et flux de 73 produits importés, en attente d'examen Google ; GEO manuel remesuré question par question (ChatGPT fait, Gemini en cours)
- 2026-11-02 : Morgane personnalise des casquettes de base (jamais « fabrique ») : formules corrigées dans les documents annuaires, profil et plan d'entité ; lieu de marque = « Bordeaux » par défaut, « Sud-Ouest » pour éviter la répétition.
- 2026-11-02 : GEO manuel final (question par question, sans compte) : marque citée 2 fois sur 30, seulement à la q10 contenant son nom ; redirection 301 steppe → origine testée (`2bb3abe`, branche `fix/redirection-steppe`), déploiement groupé avec À propos/FAQ et flux Merchant en attente du feu vert.
- 2026-11-02 : Lot groupé en prod (`58f1097` : À propos/FAQ, flux Merchant 73 produits, redirection Steppe → Origine), vérifié, IndexNow envoyé, sitemap soumis à la Search Console ; Merchant Center lit désormais le flux du site chaque nuit (flux manuel supprimé), approbation à vérifier le 5/11.
- 2026-11-02 : Guide « porter une casquette docker » publié et poussé sur `master` (`4dc44ad`) ; atelier à Gauriaguet, logo brodé à Bordeaux, base fabriquée en Asie ; décision : plus aucun lien Vinted (sameAs inclus), à confirmer.

## Liens
- Client : [[esprit-docker]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
- Repo / deployment : https://github.com/espritdocker/esprit-docker (Cloudflare Pages, R2, Neon)
