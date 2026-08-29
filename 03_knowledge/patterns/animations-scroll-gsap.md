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
exactes (timings, easing, seuils de déclenchement).

Construit et validé dans un bac à sable local (repo "Scrap landing page", pas
encore rattaché à un projet client livré) à partir de deux sources : cantor8.io
(Webflow + GSAP/ScrollTrigger + Lenis) et le template Framer 4myfellows/ClearPath.

## Comment ça marche

**Méthode de scraping** : toujours récupérer le vrai code (HTML/CSS/JS), jamais
recréer depuis une capture d'écran ou une description — un scrape révèle les
valeurs exactes (durées, stagger, opacité de départ) qu'une interprétation
visuelle ne peut que deviner. Vérifier la licence/le poids des assets avant de
les rapatrier.

**Rapatriement local zéro dépendance réseau** : télécharger images/SVG, fichiers
de police, et les librairies JS/CSS (GSAP, ScrollTrigger, Lenis) puis réécrire
tous les chemins — permet de tester offline et d'éviter tout appel vers le site
source.

**Sandbox avec contenu placeholder** : ne jamais reproduire intégralement un
site commercial tiers (contenu, marque, textes, logo) même à usage interne —
porter uniquement la structure et les animations, avec du contenu bidon.

Deux effets documentés et prêts à réutiliser :

- **reveal-words** — révélation mot par mot d'un texte au scroll, pilotée par
  GSAP ScrollTrigger en mode `scrub`. Paramètres validés : opacité de départ
  `0.12`, `stagger: 0.08`, `duration: 0.4`.
- **pixel-dissolve** — transition entre sections par grille de pixels générée
  par PRNG à seed fixe, pilotée par ScrollTrigger. Point d'attention : le
  conteneur de la transition doit être le **premier enfant de la section
  cible** (pas de la section précédente), avec un `margin-top` pour l'ancrage —
  sinon le placement DOM casse silencieusement l'effet.

## Code / config

```js
// reveal-words — squelette
gsap.from(".reveal-word", {
  opacity: 0.12,
  stagger: 0.08,
  duration: 0.4,
  scrollTrigger: {
    trigger: ".reveal-section",
    start: "top 80%",
    end: "bottom 60%",
    scrub: true,
  },
});
```

## Cas d'usage réels
- Repo "Scrap landing page" — bac à sable local (`local-demo/`), animations
  portées et vérifiées visuellement, pas encore intégrées à un site client livré
