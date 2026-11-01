# DESIGN.md · Sabinas Watersport Rhodos

Système visuel de la maquette `maquette/`. Écrit le 31/10/2026, après coup : la v1 (21/10) avait son système dans l'en-tête de `styles.css`, Melvin l'a validé en direct. Ce document le fixe, ajoute ce que le skill `maquette-prospect` exige (hero plein écran, en-tête, prix à un seul endroit) et respecte `invariants-luxe.md`. Les jetons vivent dans le bloc `:root` de `maquette/styles.css` ; la porte qualité compare la page à ce fichier (contrôle « système visuel », avertissement).

## L'idée

**La journée tient en quatre escales, de notre plage au Blue Lagoon.** Stafilia → Cave Island → Lindos → Blue Lagoon : seul ce loueur part de Stafilia Beach et passe sous l'Acropole avant le lagon. Elle est visible dès le premier écran (légende-programme sous les boutons du hero), puis dans la fiche (« Your day, stop by stop ») et sur la carte du point de départ (OpenStreetMap).

## Ce qui vient de Sabina

- **Palette** : l'eau turquoise du lagon (photos de Sabina), le bleu profond de la mer au large, le blanc chaulé de Lindos, l'or du logo Dolphin Tours. Pas de noir : la journée se passe en pleine lumière.
- **Typographies** : GFS Didot (Didot grecque, Greek Font Society) pour les titres et l'accroche du client ; Commissioner (dessinée par un typographe grec) pour l'interface. Repli système : Didot, Bodoni 72, Georgia ; Segoe UI, system-ui.
- **Photos** : celles de Sabina, hétérogènes (drone, téléphone, appareil) : même recadrage 4:3 dans une rangée, jamais agrandies, petites sources affichées à leur taille.

## Couleurs

| Jeton | Valeur | Usage |
|---|---|---|
| `--ink` | #0f2433 | texte, fond du pied de page |
| `--sea` | #0b4f6c | titres, surfaces fortes, focus |
| `--lagoon` | #1aa7a5 | icônes, décor |
| `--lagoon-ink` | #0f7d7b | turquoise lisible pour du texte (AA) |
| `--foam` | #f6f9f9 | fond de page |
| `--stone` | #e8eeec | sections alternées |
| `--line` | #cfdcda | filets |
| `--muted` | #4c6170 | texte secondaire |
| `--field` | #7d8f99 | bordure des champs (3:1) |
| `--gold` | #e9a93b | bouton principal (texte #2a1c05) |
| `--wa` | #25d366 | WhatsApp (texte #06311a) |
| `--white` | #ffffff | cartes, texte sur photo |
| `--danger` | #b3261e | erreurs |

Sur la photo du hero : texte #ffffff, accent italique #bff3ef, accroche #eef7f8, légende #dceff1, voile rgb(10, 30, 44) de 0 à 86 % d'opacité. Badges « À confirmer » / « Exemple » : texte #6b4a0a sur #fbe9c6. Pied de page : #c9d6dd, #9fb2bd. Survol du bouton or : #f0b54d. Autres valeurs héritées de la v1 et tolérées : #d6e6ec, #dfe9ee, #eaf3f3, #a86b00, #a8b6bd, #b9c4c9, #2bb3b4, #0e6b8a.

## Typographie

- Titre du hero : GFS Didot 400, `clamp(2.15rem, 4.2vw + 1rem, 4.75rem)`, interligne 1,02, 15 caractères de large au plus, italique turquoise pour le lieu.
- Titres de section (`.h2`) : GFS Didot 400, 1.875rem, couleur `--sea`.
- Sous-titres (`.h3`, cartes, tableaux) : GFS Didot 400, 1.6rem / 1.55rem / 1.5rem.
- Accroche du client dans l'en-tête : GFS Didot italique 1.15rem ; signature du hero (numéro) : GFS Didot italique 1.15rem.
- Texte courant : Commissioner 400, 1rem, interligne 1,55 ; chapeau 1.125rem.
- Petits textes : 0.8125rem (libellés, méta), 0.92rem (boutons de l'en-tête, cartes) ; capitales espacées seulement pour les sur-titres et le sous-titre du logo.
- Chiffres : tabulaires (`font-variant-numeric: tabular-nums lining-nums`).

Tailles en usage : 0.6rem, 0.62rem, 0.68rem, 0.7rem, 0.72rem, 0.75rem, 0.76rem, 0.78rem, 0.8rem, 0.8125rem, 0.82rem, 0.85rem, 0.86rem, 0.88rem, 0.9rem, 0.92rem, 0.93rem, 0.95rem, 0.98rem, 1rem, 1.02rem, 1.05rem, 1.1rem, 1.125rem, 1.15rem, 1.2rem, 1.25rem, 1.3rem, 1.35rem, 1.375rem, 1.4rem, 1.45rem, 1.5rem, 1.55rem, 1.6rem, 1.875rem, 1.9rem, 2rem, 2.2rem, 2.6rem, 4.5rem, 16px.

## Espacements

Gouttière 16 px (sécurité des encoches comprise), sections 56 à 72 px, cartes 18 px de marge intérieure, largeur de contenu 1 180 px. Barre d'action du téléphone 72 px, en-tête 60 px.

## Rayons

`--r-s` 10px (champs, encadrés), `--r-m` 18px (cartes, tableaux), 999px (boutons, pastilles de langue), 50% (icônes rondes), 12px et 14px (vignettes de la v1), 4px (badges), 6px et 8px (focus, lien d'évitement), 34px (téléphone de la démo), 0 (photo des cartes, collée au bord).

## Ombres

Rares, seulement sous ce qui flotte : `0 30px 60px -30px rgba(15,36,51,.6)` (feuille de demande), `0 24px 50px -32px rgba(15,36,51,.6)`, `0 -20px 60px -20px rgba(0,0,0,.35)` (barre du téléphone), `0 6px 18px -8px rgba(233,169,59,.9)` (bouton or), `0 0 0 3px rgba(11,79,108,.35)` (focus des champs). Les cartes n'ont pas d'ombre : un filet `--line`.

## Mouvement

- Hero : la photo zoome lentement (10 s, au plus ×1,08 et jamais au-delà de la taille du fichier chargé) ; titre, accroche, boutons, légende et signature montent en cascade (opacité + translation 22 px, 0,9 s, décalés de 0,15 s).
- Titres de section : montent à l'entrée dans l'écran (même geste), filet de sécurité à 4 s.
- Jamais en mouvement réduit ni sous `navigator.webdriver` (captures de la porte et de la vidéo) ; `?anim` les force. Pas de `clip-path` sur du texte (anneau de focus).
- Feuille de demande : glisse du bas sur téléphone, fondu sur ordinateur (Motion 11).

## Règles fixes (invariants et préférences de Melvin)

- Le hero occupe tout le premier écran, texte posé sur la photo, **aucune pastille ni badge sur une photo**, deux boutons au plus, numéro du bureau en signature.
- En-tête translucide (blanc 70 %, flou), accroche du client entre logo et menu, menu dans l'ordre des sections, bouton « Request », langues dans l'en-tête (dans le panneau du menu sous 1 000 px).
- Cartes en grille régulière (1, 2 puis 3 colonnes), photo pleine au même recadrage 4:3, prix « dès … » sur la carte.
- Tous les prix dans « Prix et conditions », une seule fois ; ailleurs, un « dès … » ou un total calculé et un lien vers le tableau.
- Une seule forme de fiche : galerie défilante de 5 éléments au plus, vidéo au centre (choix de Melvin sur Sabina, 21/10).
- Fond clair et une seule couleur d'accent (l'or) pour l'action.

## Ce qui reste libre, et pourquoi ce choix

- Titres en serif : la Didot grecque relie la marque à Lindos ; la v1 l'avait, Melvin l'a gardée.
- 3 cartes par rangée à 1 440 px : les photos des cartes font au moins 960 px (le catamaran, photo mise en avant par Sabina, fait 960 px : 2 colonnes l'agrandiraient).
- Pas de recherche dans le hero : la barre du téléphone et le bouton de l'en-tête ouvrent la demande.
- Alignement strict plutôt que chevauchements : les photos de Sabina n'ont ni la même lumière ni le même photographe.
