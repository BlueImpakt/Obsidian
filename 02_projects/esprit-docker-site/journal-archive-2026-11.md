# Archive Journal — esprit-docker-site

Entrées archivées automatiquement (seuil `## Journal` > 15, voir CLAUDE.md). Historique complet, ordre chronologique.

---

- 2026-11-02 : Outil SEO/GEO `seo-geo` cadré avec Esprit Docker en pilote (spec + 2 plans) ; côté site, provenance des ventes (tâches 1 à 3) validée en relecture, section `/guides` en cours ; migration à passer avant déploiement, point CNIL à trancher
- 2026-11-02 : Section `/guides` en MDX livrée (commit 120692f, brouillons exclus, sitemap conditionnel), vérifiée dans le navigateur ; durcissement en cours contre un guide mal formé.
- 2026-11-02 : Revue finale branche attribution + /guides : défaut critique Safari < 16.4 (lookbehind regex) corrigé en vague finale ; « Steppe » = modèle Origine déjà au sitemap ; consentement CNIL (provenance) à trancher avant déploiement
- 2026-11-02 : Vague finale de corrections de la revue de branche terminée (lookbehind regex supprimé pour Safari < 16.4, 28 tests verts, build propre), non poussée ; reste migration SQL provenance et point CNIL avant déploiement
- 2026-11-02 : pilote de l'outil seo-geo sur Esprit Docker : audit technique rangé (images mobile lourdes, même méta sur les 13 fiches, Livraison/Entretien invisibles dans le HTML initial), brief du guide « porter-casquette-docker » audité et corrigé, rédaction à venir
- 2026-11-02 : Provenance des ventes passée en compteur anonyme (option B, exemption CNIL, rien envoyé à Mollie, opposition dans « Gérer mes cookies », textes légaux réécrits ; commit 1094ebf) ; migration SQL appliquée sur Neon avec compte de lecture seule `seo_geo_lecture` ; point zéro GEO : Claude ne cite Esprit Docker dans aucune des 32 réponses, mesure sur Sonnet 5.5 (~1,70 $/mois) ; 73 méta descriptions uniques et onglets Livraison/Entretien dans le HTML ; premier guide « porter une casquette docker » en brouillon ; branches non déployées
- 2026-11-02 : Search Console : propriété Domaine validée en DNS, compte de service `seo-geo` créé et ajouté, clé rangée hors repo ; collecte GSC en 403 tant que l'API n'est pas activée sur le projet `seo-geo-513517`. Positions Google mesurées : n°1 sur la marque seule, absent du top 10 sur 21 autres mots-clés.
