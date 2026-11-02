# Archive Journal — esprit-docker-site

Entrées archivées automatiquement (seuil `## Journal` > 15, voir CLAUDE.md). Historique complet, ordre chronologique.

---

- 2026-10-05 : voice.md des skills ig-* complété depuis le profil Instagram (lu dans Chrome, lecture seule) ; langue FR, CTA `DOCKER`. `/ig-profile` : 31/100. Carousel « Composez votre docker » (8 slides) rédigé, à valider avant construction.
- 2026-10-28 : Audit SEO (Lighthouse SEO 100, mais apex/www en double, pas de canonical ni JSON-LD, sitemap 500 intermittente) ; corrections écrites dans le repo (301 apex → www, canonicals, JSON-LD Product/Organization, sitemap à repli, noindex zones privées, titres « casquette docker ») — tsc OK, non commitées ni déployées.
- 2026-10-31 : Audit perf/a11y (LCP mobile : accueil 3,5 s, fiche 2,7 s, collection 5,0 s) et correctifs (hero rendu serveur, images via images.esprit-docker.com, WebP, cache 30 j, a11y) ; flou du hero adouci (2 s → 4 s). Tout déployé avec les corrections SEO du 28/10 : commit 9c86356, vérifié en ligne (301 apex → www, sitemap 200, JSON-LD).
- 2026-10-31 : Avis Vinted : recopie des textes abandonnée (CGU Vinted : pas de reproduction sans accord écrit) ; ligne « ★★★★★ 4,9/5 · 239 évaluations Vinted » ajoutée sous le bouton d'achat de toutes les fiches (src/lib/avisVinted.ts), déployée (ba5d513) et vérifiée desktop + mobile. Spec avis (fondu, onglet, page /avis) gardée pour une collecte d'avis propres.
- 2026-10-31 : Nouveau modèle L'Essentielle : photos des 4 coloris normalisées au format catalogue (WebP ~180 Ko au lieu de PNG 2,8 Mo) + dos, publiées en R2/Neon ; Orange Corail remplacé par « Orange Terracotta » pour ce modèle ; bloc « Nouvelle collection » en tête de /collection et masquage des couleurs non proposées codés, vérifiés en local, non déployés.
- 2026-10-31 : L'Essentielle : 21 photos (7 couleurs × face/profil/dos, vrais dos partout) en ligne, transparence reconstruite depuis les PNG à fond blanc, script `scripts/essentiel-import-photos.mjs` ; en-tête du bloc « Nouvelle collection » refait (« NOUVELLE » / « COLLECTION » en diagonale 45° de chaque côté de la carte), vérifié desktop, non déployé.
- 2026-10-31 : Modèle L'Essentielle renommé « Steppe » (Orange Corail écartée côté serveur), bloc « Nouveau Docker » de /collection finalisé et déployé (89fca47, vérifié en ligne) ; descriptions des 13 modèles mises à jour ; animations de la page Collection prêtes, non déployées.
- 2026-10-31 : Section « Nouveau docker » Steppe sur l'accueil, finitions fiche produit (logo, note Vinted, bouton retour), prix minimum corrigé, Steppe/Terracotta retirés de l'Atelier — déployé (`0be017b`, `c37a609`, `a01e609`) ; correctifs Atelier mobile prêts en local
