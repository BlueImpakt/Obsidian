---
tags: [client, actif, p2, artisanat, france]
created: 2026-08-29
statut: actif
priorite: p2
secteur: artisanat
localisation: france
body_synced: 2026-10-05
---

# esprit-docker

## Relationnel
- **Contact** : Morgane Le Mouee — Entreprise Individuelle (micro-entrepreneur)
- **Activité** : Esprit Docker — chapellerie / site e-commerce de chapeaux (nom commercial "Esprit Docker", nom de code projet `esprit-chapellerie`)
- **Site** : [www.esprit-docker.com](https://www.esprit-docker.com)
- **Contact pro** : contact@esprit-docker.com

## Historique des échanges
- 2026-09-02 : Bug mail de suivi Sendcloud — 0 email de suivi envoyé en 30 jours côté Sendcloud (config panel correcte) ; le mail "point relais" reçu vient de Mondial Relay. Solution de repli (Brevo, webhook Sendcloud) implémentée et déployée, test end-to-end à faire par Melvin (voir [[esprit-docker-site]]).
- 2026-10-05 : Audit Instagram @esprit_docker (31/100), voice.md ig-* renseigné, carousel « Composez votre docker » rédigé en attente de validation.

## Décisions prises
- 2026-09-02 : Repli Brevo retenu pour l'email « expédié » (envoyé depuis le webhook Sendcloud, anti-doublon via `commandes.suivi_email_envoye_at`) — le mail de suivi natif Sendcloud n'est pas fiable (0 envoi en 30 jours).
- 2026-08-30 : Auth admin : retour à `ADMIN_PASSWORD` en Secret Cloudflare (série hash PBKDF2 revertée).
- 2026-10-05 : Instagram — CTA mot-clé `DOCKER`, voix FR.

## Besoins identifiés
- Site e-commerce Next.js pour vente de chapeaux, avec gestion avancée de variantes produit (photos par face/profil, motifs, détourage)

## Devis / propositions
-

## Next actions
- [ ] Test end-to-end du flux Brevo « expédié » (commande + paiement + marquage expédiée + annulation Sendcloud) — Melvin
- [ ] Valider le carousel Instagram « Composez votre docker »
- [ ] Ajouter `.claude/settings.local.json` au `.gitignore`
- [ ] Envoyer à Morgane [[referencement-google-ia]] et récupérer ses réponses (phrase de marque, nom et photo, année de création, comptes existants, questions du guide)

## Journal
- 2026-11-02 : Sur [[esprit-docker-site]] — Provenance des ventes passée en compteur anonyme (option B, exemption CNIL, rien envoyé à Mollie, opposition dans « Gérer mes cookies », textes légaux réécrits ; commit 1094ebf) ; migration SQL appliquée sur Neon avec compte de lecture seule `seo_geo_lecture` ; point zéro GEO : Claude ne cite Esprit Docker dans aucune des 32 réponses, mesure sur Sonnet 5.5 (~1,70 $/mois) ; 73 méta descriptions uniques et onglets Livraison/Entretien dans le HTML ; premier guide « porter une casquette docker » en brouillon ; branches non déployées
- 2026-11-02 : Sur [[esprit-docker-site]] — Search Console branchée à l'outil seo-geo (propriété Domaine validée, compte de service prêt, API à activer) ; positions Google : n°1 sur la marque, absent du top 10 ailleurs.
- 2026-11-02 : Sur [[esprit-docker-site]] — document [[referencement-google-ia]] : trace en langage simple de tout le travail SEO/GEO ; plan entité de marque codé sur la branche (`OnlineStore` + `sameAs`, descriptions à jour, IndexNow, commit e749994) ; compte Merchant Center créé.
- 2026-11-02 : Sur [[esprit-docker-site]] — SEO/GEO déployé en prod (IndexNow envoyé), GEO manuel 0 citation sur 30, flux Merchant Center et pages À propos/FAQ prêts non déployés, réponses de Morgane intégrées
- 2026-11-02 : Sur [[esprit-docker-site]] — phrase de marque corrigée (bijou cousu en Gironde) dans métas et JSON-LD, commit dee8675, non fusionné
- 2026-11-02 : Sur [[esprit-docker-site]] — Perplexity remesuré question par question, pages À propos/FAQ fusionnées (non déployées), retours et livraison Merchant Center alignés sur les CGV
- 2026-11-02 : Sur [[esprit-docker-site]] — Bing Webmaster Tools branché, Merchant Center corrigé et flux de 73 produits importé (examen Google en cours), GEO manuel remesuré (ChatGPT fait, Gemini en cours)
- 2026-11-02 : Sur [[esprit-docker-site]] — Morgane personnalise des casquettes de base (formules corrigées partout), « Bordeaux » par défaut pour la marque.
- 2026-11-02 : Sur [[esprit-docker-site]] — GEO manuel final : marque citée 2 fois sur 30 (uniquement quand son nom est dans la question) ; redirection steppe → origine testée, déploiement groupé en attente du feu vert.
- 2026-11-02 : Sur [[esprit-docker-site]] — lot SEO/GEO groupé en prod (À propos/FAQ, flux Merchant, redirection Steppe), Merchant Center lit le flux du site chaque nuit, guide « porter une casquette docker » publié.
- 2026-11-02 : Sur [[esprit-docker-site]] — Vinted masqué du site, guide publié et indexation demandée à Google, images allégées (AVIF) après correction du logo de l'accueil, textes d'annuaires alignés sur la phrase de marque
- 2026-11-05 : Sur [[esprit-docker-site]] — chantier mots-clés à volume lancé (titres des 73 fiches, Collection, guides) ; Merchant Center 8 approuvées / 65 en examen photos ; point CNIL sur le compteur de ventes à trancher
- 2026-11-05 : Sur [[esprit-docker-site]] — FAQ/À propos corrigées, audits des briefs marin et bonnet rendus, corrections en cours
- 2026-11-05 : Sur [[esprit-docker-site]] — 3 guides en brouillon rédigés (casquette marin, bonnet docker, casquette sans visière) après correction des briefs ; 54 tests et build OK sur feat/recherches-volume, rien poussé, guides masqués en attendant les réponses de Morgane
- 2026-11-05 : Sur [[esprit-docker-site]] — titres des fiches, page Collection et FAQ bonnet docker en production et vérifiés, IndexNow envoyé ; 3 guides en attente des réponses de Morgane (10 questions)

## Liens
- Projets : [[esprit-docker-site]]
- Trace du travail SEO/GEO (langage simple) : [[referencement-google-ia]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
