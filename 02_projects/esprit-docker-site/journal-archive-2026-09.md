# Archive Journal — esprit-docker-site

Entrées archivées automatiquement (seuil `## Journal` > 15, voir CLAUDE.md). Historique complet, ordre chronologique.

---

- 2026-09-02 : Fix mail de suivi colis Sendcloud (voir [[esprit-docker]] pour le détail du diagnostic) — ajout d'une note "vérifiez vos spams" dans `emailCommande.ts` et `succes/page.tsx`. Commit `944dca9` sur `master`.
- 2026-09-02 : Path B implémenté pour le mail "colis expédié" (voir [[esprit-docker]] pour le diagnostic complet) — `emailExpedition.ts` (envoi Brevo, même charte que la confirmation) + hook dans le webhook Sendcloud + colonne `commandes.suivi_email_envoye_at` (verrou anti-doublon). Migration exécutée et vérifiée sur Neon prod (projet `esprit-docker`, branche `production`). Commit+push `20a6fc6` sur `master`.
- 2026-09-04 : Graphify (graphe de code tree-sitter, voir `03_knowledge/outils.md`) installé et activé — 1108 nœuds/1673 edges, nudge `/graphify` actif en session. `.claude/settings.json` renommé en `.claude/settings.local.json` + gitignored (le hook contient un chemin `graphify.exe` propre à la machine de Melvin, à ne jamais committer).
