# Archive Journal — esprit-docker-site

Entrées archivées automatiquement (seuil `## Journal` > 15, voir CLAUDE.md). Historique complet, ordre chronologique.

---

- 2026-10-05 : voice.md des skills ig-* complété depuis le profil Instagram (lu dans Chrome, lecture seule) ; langue FR, CTA `DOCKER`. `/ig-profile` : 31/100. Carousel « Composez votre docker » (8 slides) rédigé, à valider avant construction.
- 2026-10-28 : Audit SEO (Lighthouse SEO 100, mais apex/www en double, pas de canonical ni JSON-LD, sitemap 500 intermittente) ; corrections écrites dans le repo (301 apex → www, canonicals, JSON-LD Product/Organization, sitemap à repli, noindex zones privées, titres « casquette docker ») — tsc OK, non commitées ni déployées.
- 2026-10-31 : Audit perf/a11y (LCP mobile : accueil 3,5 s, fiche 2,7 s, collection 5,0 s) et correctifs (hero rendu serveur, images via images.esprit-docker.com, WebP, cache 30 j, a11y) ; flou du hero adouci (2 s → 4 s). Tout déployé avec les corrections SEO du 28/10 : commit 9c86356, vérifié en ligne (301 apex → www, sitemap 200, JSON-LD).
