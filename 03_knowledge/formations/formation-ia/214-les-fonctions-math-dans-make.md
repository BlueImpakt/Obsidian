---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.14 Les fonctions “math” dans Make.txt"
---

# 2.14 Les fonctions “math” dans Make

## Resume
- Introduction aux fonctions mathématiques de Make, avec un aparté personnel amusant : l'auteur explique une petite brûlure oculaire causée par de la cire de bougie lors d'une fête au Portugal, affectant temporairement son apparence à l'écran.
- Présentation de la première fonction mathématique : Average (moyenne), accessible dans l'onglet Math, permettant de calculer la moyenne d'un Array de valeurs numériques.
- Introduction de la deuxième fonction mathématique : Ceiling (arrondi supérieur), accessible dans le même onglet Math, permettant d'arrondir une valeur décimale vers le chiffre entier supérieur.
- Démonstration de Ceiling avec l'exemple 1,3 devenant 2, et introduction de la fonction inverse Floor qui arrondit systématiquement vers le chiffre entier inférieur plutôt que supérieur.
- Explication de la fonction Truncate : elle fonctionne en se basant sur la position du point décimal, un exemple avec Truncate de 1 illustrant qu'elle supprime tout ce qui se trouve après une position définie relative à ce point.
- Démonstration détaillée de Truncate avec valeurs positives et négatives : Truncate(+1) garde 123.2 (supprime 569 après la première décimale), Truncate(-1) garde 120 (annule aussi le chiffre avant le point).
- Poursuite de la démonstration Truncate avec -2 (annule deux chiffres avant le point) et +2 (conserve deux décimales après le point), illustrant la symétrie du comportement selon le signe du paramètre.
- Conclusion sur Truncate : à comprendre comme un outil de raccourcissement de valeur numérique, agissant soit sur les décimales soit sur les chiffres entiers selon le signe du paramètre fourni.
- Démonstration de la fonction Round (arrondi standard) : 1,24 devient 2, tandis que 2,8 devient 3, illustrant l'arrondi mathématique classique. Introduction de la fonction valeur absolue (Abs), oubliée précédemment dans la présentation.
- Présentation honnête des fonctions d'écart-type (rarement utilisées par l'auteur mais expliquées quand même) : S pour l'écart-type d'échantillon, P pour celui de la population totale d'une étude statistique.
- Présentation de la fonction Format Number, permettant de mettre en forme un chiffre (exemple : 14587,25) selon un format d'affichage défini, avec démonstration pratique malgré un petit glitch technique en cours de route.
- Mention des opérateurs de comparaison (plus grand, plus grand ou égal, etc.) utilisés principalement dans les conditions, puis présentation de la fonction Modulo qui garde le reste d'une division.
- Conclusion du module fonctions mathématiques, avec ajout tardif d'un point important oublié : l'importance des parenthèses dans Make, particulièrement significative dans le contexte des valeurs numériques.

## Concepts cles
- introduction aux fonctions mathématiques de Make
- fonction Average (moyenne) dans l'onglet Math
- fonction Ceiling (arrondi vers le supérieur)
- Ceiling (1,3 → 2) et fonction inverse Floor (arrondi inférieur)
- fonction Truncate basée sur la position du point décimal
- comportement de Truncate avec paramètres positifs et négatifs
- comportement symétrique de Truncate selon le signe (-2 vs +2)
- synthèse de Truncate comme outil de raccourcissement numérique
- fonction Round (arrondi standard)
- fonction valeur absolue (Abs)
- fonctions d'écart-type S (échantillon) et P (population totale)
- fonction Format Number pour la mise en forme de chiffres
- opérateurs de comparaison pour conditions
- fonction Modulo (reste de division)
- importance des parenthèses dans les calculs Make (point ajouté tardivement)

## Outils mentionnes
- Make

## Tips techniques
-

## Cas d'usage reels
- [[]]
