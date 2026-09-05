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
- **Étude de cas "Ramen" — Jesse Zhou**
  (`jesse-zhou.medium.com/jesses-ramen-case-study-77bae77ab5f0`) — walkthrough
  d'un portfolio 3D immersif (Three.js + GSAP + Lenis). Modèle de *structure de
  projet* (organisation de scène, chargement, sync caméra/scroll) à lire avant de
  chiffrer, pas du code à copier. Détail technique scrollpath :
  [[animations-scroll-gsap]].

**Pistes projet pour ces outils** (non validées — opportunités / upsells)
- **[[naeco-carte]]** — *scrollpath* : mode cinématique, caméra qui survole le
  tracé d'expédition (points de contrôle = escales Pelagos / sites STARESO),
  progression = scroll dans le récit.
- **[[naeco-site]]** — *scrollpath* + *Blender connector* + *Sketchfab* : hero
  avec le voilier NAECO (modélisé sous Blender, spécifique donc absent de
  Sketchfab) qui suit la route Pelagos au scroll ; scène peuplée d'assets CC0
  (bouée, dauphin — travail cétacés). *Étude Ramen* = blueprint avant chiffrage.
- **[[esprit-docker-site]]** — *Blender connector* + *Sketchfab* + *scrollpath* :
  visualiseur 3D de chapeau (nettoyage/décimation de scans clients sous Blender,
  tête de mannequin CC0 en placeholder), caméra qui orbite face → profil → dos au
  scroll. *CodePen* : hover-zoom produit / spin 360°.
- **[[site-blue-impakt]]** — *CodePen* : Pen de text/grid-reveal récupéré en View
  Source, réadapté avec Motion sur la grille Müller-Brockmann (refonte en cours).
  *Étude Ramen* = référence si page "démo capacité agence".
- **[[km0-circuit-court]]** — *Sketchfab* : assets low-poly CC0 (cageots,
  légumes, étal) pour les illustrations de la landing.

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

## Graphify (Graphify-Labs)

**Repo** : GitHub Graphify-Labs, Apache-2.0, package PyPI `graphifyy` (double-y).

Parsing AST local via tree-sitter → construit un knowledge graph du code d'un
projet ; Claude interroge le graphe (`graphify query`/`explain`/`path`) au lieu
de grep/lire tous les fichiers. Parsing du code 100 % local et gratuit (rien ne
sort de la machine — bon point pour la confidentialité des repos clients sous
NDA) ; seul le traitement docs/PDF/images consomme des tokens de la session.

**Installation** (portée globale, testée) : `winget install astral-sh.uv` →
`uv tool install graphifyy` → `graphify install` (enregistre `/graphify`
globalement) → `graphify claude install` (active le nudge souple par projet).
Deux mécanismes distincts à ne pas confondre : construire/mettre à jour le
graphe (`/graphify .`, une fois puis rebuild seulement si le code change —
`graphify hook install` peut l'automatiser sur `commit`/`checkout`) vs.
l'utiliser en session (automatique une fois `graphify claude install` fait sur
le projet, hook `PreToolUse` qui suggère `graphify query` avant une lecture
brute — mode souple, pas bloquant).

**Décision d'usage (2026-09-04)** : le ROI dépend de la taille et surtout de la
*durée de vie* du codebase — rentable seulement si le même projet est
réinterrogé sur de nombreuses sessions. Retenu pour **[[km0-circuit-court]]**
(produit propre, code qui vit des mois/années). Pas retenu pour les missions
Blue Impakt courtes (sites vitrines, automatisations ponctuelles) : monter et
maintenir le graphe coûte plus cher que ce qu'il économise. Risques notés :
graphe périmé si pas remis à jour (`graphify update .`), `graphify-out/` à
garder en `.gitignore` (pas d'intérêt à le committer en solo).

**Installation réelle (2026-09-04)** : finalement étendue aux 5 repos de
`C:\Users\LENOVO\Documents\GitHub` plutôt qu'à KM0 seul — **esprit-docker**
(1108 nœuds, 1673 edges), **KM0** (1319 nœuds, 2761 edges), **naeco-carte** et
**[[naeco-site]]** (4 nœuds chacun — repos quasi sans code réel, gain jugé
négligeable mais nudge laissé actif sur demande). **Site-web** exclu : page
statique sans JS, extraction à 0 nœud, nudge désinstallé après coup. Piège
rencontré : `graphify claude uninstall` supprime le **skill global**
(`/graphify`), pas seulement le nudge du projet visé, puisque l'install est
globale et partagée — un seul fichier skill pour tous les projets. Fix
appliqué en parallèle sur les 4 repos actifs : le hook `PreToolUse` que
`graphify claude install` écrit dans `.claude/settings.json` contient un
chemin absolu propre à la machine (`.../graphify.exe`) — renommé en
`.claude/settings.local.json` (+ `.gitignore`) pour ne jamais le committer et
casser le hook chez un collaborateur qui clone le repo.
