---
tags: [knowledge]
---

# Outils découverts

Une entrée par outil : ce que c'est, pourquoi il est utile, comment il s'intègre au workflow Blue Impakt.

## batirup-skills (Alexis Buhaj)

**Repo** : `github.com/alexisbhj/batirup-skills`

Source des skills Claude Code installés dans ce setup : `good-night`, `agent-clear`
(hook `SessionStart`), `transcribe` (Whisper local). Vu dans la masterclass
[[masterclass-claude-code-obsidian-alexis]] — contient un README d'installation et
un `CLAUDE-generique.md` (template de constitution vault, volontairement générique,
à adapter). À retourner voir si les skills évoluent côté upstream (mises à jour,
nouveaux skills ajoutés par Alexis).

## Boîte à outils — landing pages / animation / scraping

Inventaire issu de `Scrap landing page/notes-office-hour-landing-3d.md` (office
hour Claude Code). Workflow associé : [[reverse-engineering-site-reference]].

**Analyse & scraping de sites de référence**
- **Wappalyzer** — détecte la stack d'un site (framework, CMS, librairies
  d'animation) depuis le code chargé. À lancer avant de reproduire un effet.
- **Firecrawl** — scrape une page et la rend en Markdown/HTML propre, plus
  exploitable par un LLM qu'un DOM brut. L'inspecteur navigateur ne donne que le
  DOM post-JS ; pour la logique d'animation, chercher le repo GitHub.
- **`gh` CLI** — cloner/lire un repo, gérer PR/issues depuis le terminal.
  Claude Code s'en sert pour récupérer le code d'un template directement.
- **CodePen** — démos HTML/CSS/JS isolées (effets scroll, layouts). Point de
  départ visuel : récupérer le code via *View Source* / *Export*, jamais demander
  à Claude de recréer d'après le rendu.

**3D & scroll**
- **react-three-fiber** (pmndrs) — wrapper React déclaratif pour Three.js.
  Standard actuel pour la 3D dans un site React/Next.
- **Lenis** (darkroomengineering) — smooth scroll inertiel, se combine avec GSAP
  ScrollTrigger via le `gsap.ticker` (pas `lenis.raf` seul). Prévoir un fallback
  scroll natif sur mobile bas de gamme.
- **Scrollpath** — terme générique : définir une trajectoire (courbe
  Catmull-Rom/Bézier) pour animer objet 3D ou caméra le long du scroll.
- **Sketchfab** — modèles 3D `.glb`/`.gltf`. Exiger licence CC0 / usage
  commercial libre pour un client ; compresser Draco avant intégration.
- **Blender connector** (tuto Anthropic) — piloter Blender par le langage pour
  produire ses propres assets 3D.

**Récupération & analyse de vidéos**
- **yt-dlp** — télécharge vidéos (YouTube + autres) : références, tutos, assets.
- **MCP youtube-knowledge** — interroge le contenu d'une vidéo (transcription,
  résumé, recherche). Combiné à yt-dlp : transforme un tuto en base interrogeable.

**Productivité autour de Claude**
- **Vowen** (vowen.ai) — dictée vocale locale (Whisper open-source), Mac/Windows,
  écrit là où est le curseur (prompt Claude Code inclus). Utile pour instructions
  longues ; local donc OK pour contenu sensible.
- **DeepSeek en pré-filtre** — modèle bon marché pour trier/résumer un gros
  volume (repo, logs, longue vidéo) avant de passer l'essentiel à Claude.
  Réserver aux volumes peu critiques : un résumé tiers perd des détails.
- **Agent-Reach** (Panniantong) — CLI open-source donnant à un agent un accès
  lecture/recherche unifié multi-plateformes (X, Reddit, YouTube, GitHub,
  Bilibili, XiaoHongShu) sans clés API ; route vers les bons outils existants,
  `agent-reach doctor` indique le chemin actif.
