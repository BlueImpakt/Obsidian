# DESIGN.md : RM Croisières, maquette de refonte

Système visuel écrit avant le code (28/10/2026). Chaque page et chaque agent le respectent ; la porte qualité signale toute valeur hors système. Les jetons vivent dans `maquette/tokens.css` (bloc `:root`), qui fait foi.

## L'idée

**Une semaine RM se choisit par sa route.** RM publie déjà, nuit par nuit, les croisières que son équipage conseille (Tour de la Martinique, Grenadines depuis le Marin, Grenadines depuis Saint-Vincent) et les dessine sur ses propres cartes, bleu marine et îles couleur sable. Le premier écran montre cette route tracée nuit après nuit, à côté d'une vraie photo de leur flotte au mouillage ; le bateau vient ensuite, choisi pour la route.

Pourquoi c'est propre à RM : deux bases aux deux bouts du parcours (Le Marin, Blue Lagoon à Saint-Vincent), des itinéraires écrits par leur équipage, des cartes à eux. Un loueur de chaîne vend « un Lagoon 42 » ; RM vend « Estella » et une route.

## Couleurs

Tirées des cartes de RM (`site/33-Rm-croisieres-refonte-visuels-.jpg` : mer #1E3D58, îles #C7936E) et de la coque blanche.

| Jeton | Valeur | Rôle |
|---|---|---|
| `--marine` | #1E3D58 | Panneau de route, pied de page, boutons principaux. La mer des cartes RM. |
| `--encre` | #10202F | Texte courant et titres sur fond clair. |
| `--sable` | #C7936E | Les escales et le tracé de la route, filets fins. Jamais un fond de bouton, jamais du texte sur blanc (contraste 2,6:1). |
| `--coque` | #FFFFFF | Fond des pages. |
| `--ecume` | #EDF2F4 | Fond des bandes secondaires (tarifs, services). |
| `--lagon` | #13777A | Liens, focus, état choisi. 5,2:1 sur blanc. |
| `--brume` | #5B6B78 | Texte secondaire sur blanc (5,5:1). |
| `--trait` | #C9D3DA | Bordures de champs et séparateurs. |
| `--alerte` | #A23B2A | Erreurs de formulaire uniquement. |
| `--aconfirmer` | #8A5A12 | Mention « à confirmer » / « exemple ». |

Sur `--marine` : texte #FFFFFF, secondaire `--blanc-78` rgba(255,255,255,0.78), filets `--blanc-40` rgba(255,255,255,0.4), `--blanc-25` rgba(255,255,255,0.25) et `--blanc-20` rgba(255,255,255,0.2), sable pour les escales. Bouton sur photo : `--blanc-94` rgba(255,255,255,0.94). Fonds de mention : `--fond-aconfirmer` #FBF6EE, `--fond-alerte` #FBEFEC.

## Typographie

- **Bodoni Moda** (Google Fonts, axes opsz et wght, italique) : noms des bateaux, titres, escales de la route en italique. Le Didone fait écho au logo R⚓M et aux noms peints sur les coques.
- **Albert Sans** (Google Fonts, 400, 500, 600) : texte courant, interface, chiffres (`font-variant-numeric: tabular-nums` dans les tarifs).
- Pas de capitales espacées pour les étiquettes ; pas de police à chasse fixe.

Échelle (px), téléphone puis ordinateur :

| Jeton | Téléphone | Ordinateur | Usage |
|---|---|---|---|
| `--t-xs` | 13px | 13px | mentions, sources |
| `--t-s` | 15px | 15px | légendes, aides de champ |
| `--t-m` | 17px | 17px | texte courant (interligne 1,55) |
| `--t-l` | 20px | 21px | intertitres d'interface, prix |
| `--t-xl` | 26px | 30px | titres de section |
| `--t-2xl` | 34px | 44px | nom du bateau en fiche |
| `--t-3xl` | 36px | 68px | grands titres |
| `--t-hero` | 36px | 56px (44px de 768 à 1279) | titre du premier écran |

Bodoni : graisse 500 en titre, 400 italique pour les escales, `letter-spacing: -0.01em` au-delà de 34px. Lignes de texte : 68 caractères au plus.

## Espacements

Pas de 4 : 4, 8, 12, 16, 24, 32, 48, 64, 96 px (`--s-1` à `--s-9`). Gouttière de page 16px sur téléphone, 32px dès 768px, 64px dès 1280px ; contenu limité à 1200px (texte 680px).

## Rayons

| Jeton | Valeur | Usage |
|---|---|---|
| `--r-photo` | 6px | photos des cartes et des fiches |
| `--r-champ` | 4px | champs, boutons |
| `--r-pastille` | 999px | choix de route, filtres |
| `--r-panneau` | 12px | panneau du formulaire, fenêtre de la galerie |

## Ombres

Deux seulement, pour ce qui flotte :
- `--ombre-barre` : `0 -6px 20px rgba(16,32,47,0.12)` (barre d'action mobile)
- `--ombre-panneau` : `0 18px 48px rgba(16,32,47,0.22)` (galerie, menu, panneau de demande)
- `--ombre-escale` : `0 0 0 1px #C7936E` (anneau des escales de la route)

Les cartes n'ont pas d'ombre : la photo pleine fait la carte.

## Mouvement

- **Un seul moment orchestré** : au chargement, la route du premier écran se trace (trait 1,4 s, escales qui apparaissent une à une, 60 ms d'écart). Changer d'itinéraire retrace la route (0,9 s).
- Réponses aux gestes : 160 à 220 ms, `cubic-bezier(.2,.7,.2,1)` ; ouverture de la galerie en fondu 200 ms.
- `prefers-reduced-motion` : route affichée d'emblée, aucune transition au-delà de l'opacité.

## Composition

- **Téléphone d'abord (390 px)** : photo pleine largeur (56 % de la hauteur), puis le panneau marine de la route, défilable à l'horizontale, escales en italique ; barre d'action fixe en bas (« Demander une semaine », WhatsApp, appel).
- **Ordinateur (1 440 px)** : premier écran en deux parties, photo à gauche (7/12), panneau marine de la route à droite (5/12), escales en échelle verticale.
- **Cartes de la flotte** : photo pleine au format 4:3, nom du bateau en Bodoni, modèle et année, cabines et passagers, prix « dès … la semaine ». Une photo plus petite que son cadre n'est jamais étirée : le cadre se réduit à sa taille.
- **Fiche** : une seule forme, mosaïque 1 + 2 ; pour un bateau à une seule photo, les caractéristiques prennent la place des deux petites photos.
- Alignement à gauche partout ; seul l'écran de fin de demande est centré.

## Principes

1. La route avant le bateau, le bateau avant l'option.
2. Le prix de la semaine, les options choisies et l'échéancier des CGV sont visibles avant toute coordonnée.
3. Tout chiffre vient du site de RM (source dans `research/flotte.json`) ou porte la mention « à confirmer ».
4. Le sable trace, le marine porte, le blanc respire : pas de quatrième couleur de fond.
5. Aucune photo affichée plus grande que son fichier.
