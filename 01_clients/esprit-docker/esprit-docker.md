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

## Journal
- 2026-09-02 : Vérif de la dernière piste Sendcloud faite — aucune case "permission de l'intégration" n'existe sur ce type d'intégration API (les "3 endroits" de la doc Sendcloud valent pour les intégrations plugin type Shopify, pas pour une intégration API brute). Config panel donc intégralement correcte des deux côtés (toggle global, templates, pays, webhook) et pourtant 0 email en 30 jours — cause probablement hors de contrôle (limitation d'offre ou colis API non branchés au moteur d'email côté serveur Sendcloud). **Path B (Brevo) implémenté et déployé** : voir [[esprit-docker-site]] pour le détail technique. Melvin devra faire le test end-to-end lui-même (commande + paiement + marquage expédiée + annulation Sendcloud = actions sortantes que l'agent ne déclenche pas). Confusion réglée en passant : les expéditions test "Test Kunde" du 27/08 venaient d'un script d'une session Claude Code antérieure avec accès à un `.env` local (clés API Sendcloud), pas de cette session.
- 2026-09-04 : Sur [[esprit-docker-site]] — Graphify (graphe de code tree-sitter, voir `03_knowledge/outils.md`) installé et activé — 1108 nœuds/1673 edges, nudge `/graphify` actif en session. Détails dans la fiche projet.
- 2026-10-05 : Sur [[esprit-docker-site]] — profil Instagram @esprit_docker audité (31/100 : pas d'épinglés ni highlights, bio tronquée en anglais, dernier post il y a 32 jours) ; voice.md des skills ig-* renseigné (FR, CTA mot-clé `DOCKER`) ; carousel « Composez votre docker » rédigé, en attente de validation.
- 2026-10-28 : Sur [[esprit-docker-site]] — audit SEO et corrections écrites (301 apex → www, canonicals, JSON-LD, sitemap), non déployées.
- 2026-10-31 : Sur [[esprit-docker-site]] — corrections SEO, performance et accessibilité déployées en prod (commit 9c86356) ; prochaine étape : référencement (Search Console sur le compte Google du client, mots-clés, contenu).
- 2026-10-31 : Sur [[esprit-docker-site]] — note Vinted (4,9/5 · 239 évaluations) affichée sous le bouton d'achat de toutes les fiches, sans recopier d'avis (CGU Vinted) ; prochaine étape : collecter ses propres avis après livraison.
- 2026-10-31 : Sur [[esprit-docker-site]] — modèle L'Essentielle mis en ligne (photos normalisées, couleur Orange Terracotta) ; bloc « Nouvelle collection » prêt, en attente de déploiement.
- 2026-10-31 : Sur [[esprit-docker-site]] — 21 photos L'Essentielle (7 couleurs, 3 vues) en ligne ; en-tête « NOUVELLE / COLLECTION » en diagonale refait, en attente de déploiement.
- 2026-10-31 : Sur [[esprit-docker-site]] — modèle Steppe (ex-L'Essentielle) en ligne, bloc « Nouveau Docker » sur /collection déployé (89fca47).
- 2026-10-31 : Sur [[esprit-docker-site]] — section Steppe sur l'accueil, finitions fiche produit, Atelier sans Steppe, déployé (`a01e609`)
- 2026-11-02 : Sur [[esprit-docker-site]] — outil SEO/GEO cadré avec ce site en pilote ; provenance des ventes et section guides en cours de construction
- 2026-11-02 : Sur [[esprit-docker-site]] — section `/guides` en MDX livrée et vérifiée (brouillons non indexés).
- 2026-11-02 : Sur [[esprit-docker-site]] — revue finale attribution/guides : bug Safari ancien corrigé, CNIL (provenance) à trancher avant déploiement
- 2026-11-02 : Sur [[esprit-docker-site]] — corrections finales de la revue de branche (compatibilité Safari), prêt à déployer après migration SQL et point CNIL
- 2026-11-02 : Sur [[esprit-docker-site]] — audit technique SEO/GEO du pilote seo-geo rangé, premier guide en cours de brief

## Liens
- Projets : [[esprit-docker-site]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
