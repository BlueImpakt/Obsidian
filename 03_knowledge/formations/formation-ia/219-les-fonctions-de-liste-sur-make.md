---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.19 Les fonctions de Liste sur Make.txt"
---

# 2.19 Les fonctions de Liste sur Make

## Resume
- Introduction à la fonction Join pour les Arrays : elle permet de rassembler plusieurs éléments d'une liste en une seule chaîne, marquant la transition vers les fonctions dédiées aux Arrays après variables, math, texte et dates.
- Démonstration pratique de Join : récupération des nombres d'un Array et assemblage en une chaîne séparée par des points, illustrant concrètement l'usage de cette fonction pour formater une liste.
- Présentation de la fonction Length appliquée aux Arrays (par opposition au texte) : elle détermine le nombre d'éléments présents dans une liste donnée, une information souvent utile pour des logiques conditionnelles.
- Présentation de la fonction Slice : elle permet de découper un Array de façon similaire au découpage de texte (Substring), en extrayant une portion précise d'une liste de valeurs.
- Introduction de la fonction Merge, nécessaire pour combiner deux Arrays à la suite l'un de l'autre, une simple concaténation textuelle n'étant pas suffisante car elle serait interprétée comme une string.
- Démonstration de Array Contains (adaptation de la fonction Contains vue pour le texte) : vérifier si une valeur spécifique (exemple : 12) existe dans une liste de nombres, retournant un booléen vrai/faux.
- Démonstration de la fonction Add appliquée aux Arrays : ajouter une nouvelle valeur (exemple : 13) à une liste existante, une opération simple d'enrichissement de données au sein d'un Array.
- Présentation de la fonction Shuffle, permettant de mélanger aléatoirement les éléments d'un Array, avec un cas d'usage concret : générer des questions de quiz dans un ordre aléatoire.
- Présentation de deux fonctions utiles : Sort (trier un Array selon une propriété spécifique, jugée très utile) et Reverse (inverser l'ordre séquentiel des éléments d'une liste).
- Présentation rapide de Last (récupérer le dernier élément d'une liste) et introduction de Flatten, une fonction rarement utilisée que l'auteur explique brièvement sans nécessairement la démontrer en détail.
- Démonstration pratique de la détection de doublons dans un Array : identification d'une valeur répétée (12) considérée comme doublon, avec test supplémentaire ajoutant d'autres valeurs dupliquées (13, 78) pour vérifier le comportement.
- Confirmation du fonctionnement des fonctions Distinct et Duplicates : les doublons identifiés (deux fois 12, deux fois 78) sont bien réduits à une seule occurrence chacun, validant l'efficacité de ces fonctions de nettoyage.
- Transition vers les informations de plan/quota : nombre d'opérations consommées, identifiant et nom d'équipe, quantité de données restantes dans le plan, identifiant d'organisation, informations de gestion de compte.

## Concepts cles
- introduction de la fonction Join pour les Arrays
- démonstration pratique de Join (séparation par point)
- fonction Length appliquée aux Arrays (nombre d'éléments)
- fonction Slice pour découper un Array (analogue à Substring)
- fonction Merge pour combiner deux Arrays
- fonction Array Contains (vérification d'existence dans une liste)
- fonction Add pour ajouter un élément à un Array
- fonction Shuffle et cas d'usage (quiz aléatoire)
- fonctions Sort (tri par propriété) et Reverse (inversion d'ordre)
- fonctions Last et Flatten (usage rare)
- détection pratique de doublons dans un Array
- validation des fonctions Distinct et Duplicates pour le nettoyage de listes
- informations de suivi de plan et de quota (opérations, données restantes)

## Outils mentionnes
- Make

## Tips techniques
- Utiliser Merge (et non une simple concaténation textuelle) pour combiner correctement deux Arrays
- Utiliser Shuffle pour mélanger aléatoirement une liste, utile par exemple pour l'ordre de questions d'un quiz

## Cas d'usage reels
- [[]]
