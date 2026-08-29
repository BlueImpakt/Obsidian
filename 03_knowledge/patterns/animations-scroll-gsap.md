---
tags: [pattern, code, validé]
created: 2026-08-29
type: code
---

# animations-scroll-gsap

## Contexte

Un client veut une landing page avec des animations au scroll qui donnent une
sensation "premium" (comme les sites primés Awwwards/Framer) — transitions de
section, hero animé, révélation de texte progressive. Plutôt que de recréer ces
effets depuis une description visuelle (résultat toujours approximatif), on
scrape le vrai code source d'un site de référence pour en extraire les valeurs
exactes (timings, easing, seuils de déclenchement). Méthode générale :
[[reverse-engineering-site-reference]].

Construit et validé dans un bac à sable local (repo `Scrap landing page`,
`C:/Users/LENOVO/Documents/Scrap landing page`, pas encore rattaché à un projet
client livré) à partir de deux sources :

- **cantor8.io** — Webflow + GSAP 3.15 / ScrollTrigger + Lenis 1.3.23 + Splide.
  Code réel récupéré (`sources/cantor8/`), analyse dans `ANALYSIS.md` /
  `SECTIONS.md`, port fonctionnel dans `sources/cantor8/local-demo/`.
- **ClearPath** (template Framer, `github.com/charlesDabard/4myfellows`) —
  reconstruit en page statique autonome avec Lenis + GSAP ScrollTrigger.
  `sources/4myfellows/` : `app.js` (249 l., ~20 effets), `styles.css` (tokens),
  tous les assets rapatriés (26 images, polices Inter + Crimson Text, vendor
  GSAP/ScrollTrigger/Lenis).

## Stack de référence

```
react-three-fiber (scène 3D)  →  Lenis (smooth scroll)  →  GSAP + ScrollTrigger
(sync scroll ↔ animation)  →  modèles .glb compressés Draco/meshopt
```

Setup Lenis + GSAP **identique** sur les deux sites (= pattern standard, à
reprendre tel quel) :

```js
gsap.registerPlugin(ScrollTrigger);
gsap.ticker.lagSmoothing(0);
const lenis = new Lenis({ autoRaf: false, lerp: 0.1 }); // cantor8: anchors:true, allowNestedScroll:true
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000)); // GSAP ticker pilote Lenis, PAS lenis.raf seul
```

## Catalogue d'effets — cantor8.io

Détail complet dans `sources/cantor8/SECTIONS.md` (chaque effet pointe vers sa
ligne dans le HTML source).

| Effet | Technique | Dépendance |
|---|---|---|
| **pixel-dissolve** (transition inter-sections, ×3) | ScrollTrigger `scrub` sur grille de `<div>` | gsap + ScrollTrigger |
| Dessin progressif diagramme SVG (CTA final) + pulses infinis | ScrollTrigger `once`, `strokeDashoffset` | gsap + ScrollTrigger |
| Hero "réseau circulaire" (~130 nœuds, physique ressort + vent) | Canvas 2D + `requestAnimationFrame` (⚠️ pas WebGL malgré le nom `webgl-circle.js`) | vanilla |
| Pulse SVG "circuit" (×2 sections) | rAF manuel + `getBoundingClientRect` → `progress` → `strokeDashoffset` | vanilla |
| Carousel produits horizontal piloté au scroll vertical | scroll listener + rAF + `lerp` 0.14, `scale` 0.7→1 selon distance au bord | vanilla |
| Header clair/foncé selon section visible | `IntersectionObserver` sur `[data-section="light"]`, fondu logo 120 ms | vanilla |
| Line-reveal nav/boutons (hover) | CSS pur, `transition 950ms cubic-bezier(.16,1,.3,1)`, `translateY(-100%)` | CSS |
| Flèche bouton qui traverse (hover) | CSS `translate(±24px)` + fade | CSS |
| Flicker carré avant tags | CSS `@keyframes` 1.2 s, 4 paliers opacity/brightness | CSS |
| Carousel news (mobile only) | Splide, `perPage` dégressif 3.5→1, barre de progression custom | @splidejs/splide |

→ **Seuls 2 effets utilisent réellement GSAP/ScrollTrigger** (pixel-dissolve +
CTA final). Tout le reste est vanilla JS/CSS — utile pour alléger le bundle.

### pixel-dissolve — mécanique exacte

Script commun `sources/cantor8/html/index.html:915-1204` (garde
`window.__cantorPixelInit`). Repris dans `local-demo/js/pixel-transition.js`.

- Grille fixe **25 colonnes × 6 lignes** de `.pixel`, `position:absolute;
  bottom:0` de la section, taille de case recalculée au resize.
- Motif généré une fois via **PRNG à seed fixe** (`seededRandom(100+idx)`, LCG
  simple → déterministe, reproductible à chaque reload). Densité croissante vers
  le bas (34→70 %), 2 dernières lignes actives à 100 %.
- Chaque case active : 55 % couleur `to`, 27 % `from`, 18 % `accent` (cyan
  `#6FE3FF`) → mosaïque, pas bicolore.
- `ScrollTrigger.create({ trigger, endTrigger: target, start:'bottom bottom',
  end:'top top', onUpdate })` → un `progress` 0→1 découpé en 2 phases via
  `REVEAL_RATIO = 0.5` : phase 1 = apparition des pixels (`revealOrder`),
  phase 2 = bascule vers `to` uniforme (`blackOrder`, ordre différent).
- À `progress ≈ 1` : classe `.is-solid` fige l'aplat (évite le recalcul
  hors-écran). `onEnterBack`/`onLeaveBack` rejouent à l'envers.
- ⚠️ **Placement DOM** : le conteneur `.pixel-transition` doit être le **premier
  enfant de la section cible** (pas de la précédente), avec un `margin-top`
  négatif pour l'ancrage — sinon l'effet casse silencieusement.
- Pas de shader ni canvas → portable tel quel en React sans dépendance.

## Catalogue d'effets — ClearPath (`sources/4myfellows/app.js`)

Tous en GSAP + ScrollTrigger. Valeurs exactes du template original.

| Effet | Params clés |
|---|---|
| **Intro timeline** (au load) | `media` `opacity` 1.4–2 s `power2.out` ; nav `stagger 0.08` ; titre split en mots `y:54, blur(10px), stagger:0.07` |
| **reveal-words** (texte mot à mot au scroll) | `opacity 0→1, stagger 0.08, duration 0.4, scrub:true`, `start "top 82%" end "bottom 45%"` |
| Split mots réutilisable | `splitWords(el, cls)` → `<span class="w">` par mot |
| Image sticky qui zoome | `scale 1→1.18, ease:none, scrub`, trigger `.intro` |
| Toggle "Balance" (knob + track + label) | timeline `paused`, `flip.play()/reverse()` sur `ScrollTrigger` `start "22% top"` |
| Bascule before/after (blur) | `scrub` timeline, `autoAlpha` + `y:±40` + `blur(6px)` |
| Nav claire sur fonds sombres | `ScrollTrigger.create({ onToggle })` → `nav.classList.toggle("nav--light")` sur `.intro-media`, `.quote`, `.footer` |
| Reveals génériques | `[data-reveal]` → `y:28, autoAlpha:0, duration:1, power3.out, once:true, start "top 88%"` ; delay via `data-reveal="0.2"` |
| Parallaxes | `.card-media img` `y:-170→0 scrub` ; `[data-float]` `y:±amt` (`data-float="60"`) ; `.quote-bg` `-23%→0%` ; `.waves svg` `x:-1400 scrub:1.2` |
| Odomètre gros chiffre (How It Works) | `hiw-strip` translaté `y:-(n-1)*h, duration:0.9, power4.inOut` sur `ScrollTrigger` par step |
| SVG dessiné (tortillon citation, ellipse pricing, `hero-lines`) | `strokeDasharray/offset = getTotalLength()`, `scrub` ou `once` + `power2.inOut` |
| Compteurs | `gsap.to({n:0}, {n:end, duration:1.6, onUpdate})` `once:true` |
| Pricing mensuel/annuel | `gsap.to({n}, ...)` interpole le prix à chaque toggle |
| FAQ accordéon | classes `.is-open`, `ScrollTrigger.refresh()` après 550 ms |
| `prefers-reduced-motion` | branche `reduce` : pose juste `opacity:1`, aucune timeline |
| Refresh post-load | `document.fonts.ready.then(ScrollTrigger.refresh)` + `window load` |

### Design tokens ClearPath (`styles.css`)

```css
:root{
  --white:#fff; --ink:#2e3231; --gray:#535956; --green:#7fa69b; --mist:#949e9b; --bg:#fafafa;
  --serif:"Crimson Text",Georgia,serif;   /* OFL, libre */
  --sans:"Inter",-apple-system,sans-serif; /* OFL, libre */
  --ease:cubic-bezier(.44,0,.56,1);
}
```

Bouton signature : pastille `border-radius:999px`, 2 points `::before/::after` qui
"sautent" d'un côté à l'autre au hover via `transition padding .45s var(--ease)`.

## Polices & licences (à vérifier avant tout usage client)

| Police | Site | Licence |
|---|---|---|
| PP Neue Montreal | cantor8 (corps + titres) | **Payante** (Pangram Pangram) — ne pas auto-héberger sans droits ; prévoir un substitut libre |
| Fragment Mono | cantor8 (labels canvas / UI technique) | OFL (Google Fonts) — libre |
| Inter | ClearPath (sans) | OFL — libre |
| Crimson Text | ClearPath (serif, titres display) | OFL — libre |

## Code / config

```js
// reveal-words — squelette (ClearPath, valeurs template original)
document.querySelectorAll("[data-words]").forEach((el) => {
  splitWords(el, "w"); // wrap chaque mot dans <span class="w">
  gsap.to(el.querySelectorAll(".w"), {
    opacity: 1, ease: "none", stagger: 0.08, duration: 0.4,
    scrollTrigger: { trigger: el, start: "top 82%", end: "bottom 45%", scrub: true },
  });
});
```

## Cas d'usage réels

- Repo `Scrap landing page` — bac à sable local. `sources/cantor8/local-demo/`
  (index + 7 modules JS : hero-circle, pixel-transition, products-drift,
  header-theme, line-reveal, cta-lines, init) et `sources/4myfellows/` (page
  ClearPath autonome) portés et vérifiés visuellement. **Pas encore intégrés à un
  site client livré.**
- Next action ouverte : décider si ClearPath sert de base à un prochain site
  client (cf. daily 2026-08-29).
