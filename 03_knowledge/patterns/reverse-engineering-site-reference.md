---
tags: [pattern, workflow, validé]
created: 2026-08-29
type: workflow
---

# reverse-engineering-site-reference

## Contexte

Un client (ou soi-même) montre un site qui inspire — un effet de scroll, un hero
animé, un layout. Recréer "à l'œil" depuis une capture ou une description donne
toujours un résultat approximatif : les timings, easings et seuils de
déclenchement sont invisibles de l'extérieur. La méthode consiste à récupérer le
**vrai code** du site de référence et à en extraire les valeurs exactes, puis à
porter uniquement la technique (jamais le contenu) dans un bac à sable local.

Formalisé dans le repo `Scrap landing page`
(`C:/Users/LENOVO/Documents/Scrap landing page/CLAUDE.md` +
`notes-office-hour-landing-3d.md`), appliqué à cantor8.io et au template Framer
ClearPath — cf. [[animations-scroll-gsap]] pour le résultat.

## Comment ça marche

### Règle d'or

**Ne jamais recréer un design à partir d'une simple description.** Si le code
n'est pas récupérable, le dire au client au lieu de deviner.

### Étapes

1. **Identifier la stack** avant de coder — Wappalyzer (ou équivalent) :
   framework JS, builder (Webflow/Framer), librairies d'animation, versions.
   Dit si l'effet visé est faisable avec les outils déjà maîtrisés.
2. **Récupérer le code réel**, par ordre de préférence :
   - repo GitHub du projet s'il existe (`gh` CLI pour cloner/lire) — donne la
     logique d'animation, pas seulement le rendu ;
   - export CodePen (`View Source`) pour une démo isolée ;
   - `view-source:` + fetch direct des fichiers JS/CSS (marche sur les sites
     Webflow : les scripts sont dans des `.txt`/`.js` accessibles) ;
   - Firecrawl pour un scrape propre en HTML/Markdown (mieux qu'un DOM brut plein
     de classes générées à donner à un LLM) ;
   - inspecteur navigateur en dernier recours — donne le DOM post-JS (structure
     + style), pas le code source des devs.
3. **Analyser et documenter** — un fichier `ANALYSIS.md` (stack détectée, design
   tokens, composants clés) + un `SECTIONS.md` (chaque animation → sa ligne dans
   le source, params exacts : durée, stagger, easing, `start`/`end`
   ScrollTrigger). Repérer le **code mort** (classes absentes du DOM, warnings
   console) pour ne pas le porter.
4. **Rapatrier les assets en local, zéro dépendance réseau** — images, SVG,
   polices `.woff2`, et les librairies vendor (GSAP, ScrollTrigger, Lenis) ;
   réécrire tous les chemins. Permet de tester offline et de ne jamais rappeler
   le site source.
5. **Porter dans un bac à sable avec contenu placeholder** — ne jamais
   reproduire intégralement un site commercial tiers (contenu, marque, textes,
   logo), même en interne. Porter la structure + les animations, avec du contenu
   bidon. Découper en modules JS courts par effet (un fichier par animation).
6. **Vérifier avant intégration** :
   - **licences** — polices payantes (ex. PP Neue Montreal), modèles 3D
     Sketchfab (exiger CC0 ou usage commercial libre) ;
   - **poids** — `.glb` compressés Draco/meshopt, taille des `.woff2` ;
   - **mobile** — prévoir un fallback (scroll natif si Lenis rame sur bas de
     gamme, lazy-load de la scène 3D après le premier paint, moins de
     particules). Souvent la source le fait déjà : bon exemple à suivre.

### Outils du workflow

Voir [[outils]] pour le détail : Wappalyzer, Firecrawl, `gh` CLI, `yt-dlp` +
MCP youtube-knowledge (transformer un tuto vidéo en base interrogeable),
Agent-Reach (lecture multi-plateformes sans clés API), Vowen (dictée vocale
locale pour les prompts longs), DeepSeek en pré-filtre (résumer un gros
repo/une longue vidéo avant de passer l'essentiel à Claude — à réserver aux
volumes peu critiques, un résumé tiers perd des détails).

## Code / config

```
Scrap landing page/
  CLAUDE.md                     # règles projet (stack, "jamais depuis une description")
  notes-office-hour-landing-3d.md
  sources/
    <site>/
      html/ css/ js/            # code réel récupéré, brut
      ANALYSIS.md               # stack + tokens + composants
      SECTIONS.md               # chaque anim → ligne source + params exacts
      local-demo/               # port modulaire, contenu placeholder, offline
```

## Cas d'usage réels

- **cantor8.io** → `sources/cantor8/` : stack Webflow + GSAP 3.15 + Lenis 1.3.23
  + Splide identifiée, pixel-dissolve et hero canvas 2D documentés au pixel près,
  port fonctionnel dans `local-demo/`.
- **ClearPath** (`github.com/charlesDabard/4myfellows`) → `sources/4myfellows/` :
  template Framer reconstruit en page statique autonome, ~20 effets GSAP avec
  valeurs du template, 100 % des assets localisés (26 images, Inter +
  Crimson Text, vendor GSAP/Lenis).
- Aucun encore livré à un client — base de composants réutilisable.
