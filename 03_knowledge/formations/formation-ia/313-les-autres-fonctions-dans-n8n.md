---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.13 Les autres fonctions dans N8N.txt"
---

# 3.13 Les autres fonctions dans N8N

## Resume
- Introduction de la dernière partie sur les fonctions N8n : les fonctions d'objet, distinctes des fonctions d'Array (liste), une section jugée moins captivante mais essentielle à la compréhension globale.
- Présentation de la structure d'un objet via un exemple de liste d'achats : distinction entre Keys (clés), Values (valeurs), et objet (l'ensemble structuré combinant ces éléments).
- Explication de la limite de Get avec plusieurs objets : quand un objet unique existe, la fonction sait quoi retourner, mais avec plusieurs objets similaires, l'ambiguïté se pose. Confirmation que les fonctions numériques et texte s'appliquent normalement selon le type détecté.
- Présentation des fonctions Keys (retourne les clés d'un objet, exemple : Product, Amount, Date) et Values (retourne les valeurs correspondantes, exemple : Entreprise, 3500, 2024), utiles pour manipuler des propriétés complexes.
- Cas d'usage concret de Values pour extraire une série de montants (2000, 3500) en vue d'opérations mathématiques ultérieures comme la multiplication. Introduction d'IsEmpty/IsNotEmpty pour les objets.
- Démonstration de HasField : vérifie si un objet contient une clé spécifique (exemple : « Amount » existe mais un mauvais nom de champ ne fonctionne pas), utile pour valider la structure avant traitement.
- Introduction de KeepFieldContaining : filtre un objet selon les valeurs plutôt que les clés (exemple : filtrer par la valeur 3500), retournant un objet réduit aux champs correspondants.
- Démonstration pratique de KeepFieldContaining avec une valeur textuelle (« Enterprise License ») : le système retourne un nouvel objet ne contenant que la clé correspondant à cette valeur trouvée.
- Démonstration de la fonction Compact pour les objets : supprime automatiquement les champs vides (exemple : profession non renseignée), ne conservant que les valeurs réellement remplies.
- Reprise d'un exemple simple après un souci d'affichage, puis présentation de RemoveField, permettant de supprimer un champ spécifique d'un objet (exemple : retirer la date non nécessaire).
- Présentation de ToJSONString pour formater correctement un objet en JSON valide, et URLEncode, particulièrement utile pour encoder des éléments destinés à des paramètres de requête (query parameters).
- Transition vers les fonctions booléennes, peu nombreuses : possibilité de transformer un booléen en nombre ou en autre format, complétant le panorama exhaustif des types de données manipulables sur N8n.

## Concepts cles
- introduction aux fonctions d'objet (distinctes des Arrays)
- structure fondamentale d'un objet (Keys, Values)
- limite de Get avec objets multiples (ambiguïté)
- fonctions Keys et Values pour un objet
- cas d'usage de Values pour extraction en vue de calculs
- fonction HasField pour valider l'existence d'une clé
- fonction KeepFieldContaining (filtrage par valeur plutôt que par clé)
- exemple pratique de KeepFieldContaining sur valeur textuelle
- fonction Compact pour objets (suppression des champs vides)
- fonction RemoveField pour supprimer un champ ciblé
- ToJSONString et URLEncode pour objets (utile pour query parameters)
- fonctions booléennes (peu nombreuses, conversion en nombre)

## Outils mentionnes
- n8n

## Tips techniques
- Utiliser Compact sur un objet pour supprimer automatiquement les champs vides avant enregistrement ou traitement

## Cas d'usage reels
- [[]]
