---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.11 Fonctions de listes dans N8N.txt"
---

# 3.11 Fonctions de listes dans N8N

## Resume
- Introduction aux fonctions de liste (Array) sur N8n, annoncée comme nombreuse et nécessitant de la concentration, débutant en douceur avec un exemple simple d'array de tags associés à un contact.
- Présentation des opérateurs disponibles pour les Arrays, dont plusieurs sont communs avec les fonctions texte mais adaptés au contexte de liste (exemple : Length pour compter le nombre d'éléments plutôt que de caractères).
- Distinction clé entre Contains et Includes : Contains vérifie une correspondance partielle (« fr » matche « France »), tandis qu'Includes nécessite une correspondance exacte de l'élément dans la liste.
- Introduction de la fonction Map, décrite comme très importante, illustrée avec un Array complet de contacts pour montrer comment appliquer une transformation à l'ensemble des éléments d'une liste.
- Explication de la syntaxe particulière de Map avec la notation « item => » : elle définit une transformation appliquée systématiquement à chaque élément de la liste, un concept clé de programmation fonctionnelle.
- Démonstration pratique de Map appliquant une opération à chaque contact (exemple : fonction Concat avec des guillemets), illustrant concrètement comment enrichir chaque élément d'une liste de manière homogène.
- Confirmation que Map fonctionne aussi sur les valeurs numériques : appliquer Round sur une extraction de salaires arrondit chaque valeur de la liste, illustrant la polyvalence de cette fonction puissante.
- Introduction pratique de la fonction Filter sur les Arrays : recherche des contacts avec un salaire inférieur à 50 000, illustrant le filtrage conditionnel appliqué à une liste d'objets.
- Confirmation du résultat de Filter (Sophie Bernard à 45 000€, inférieure au seuil de 50 000) : la fonction retient uniquement les éléments de l'Array correspondant au critère défini, une fonction très fréquemment utilisée.
- Présentation de la fonction Chunk : divise un Array en groupes de taille définie (exemple : chunk de 2 regroupe les éléments par paires), utile pour traiter de grandes listes par lots successifs.
- Préparation d'un exemple avec un Array de 3 valeurs auquel on ajoute une quatrième valeur vide, préparant la démonstration de la fonction suivante pour nettoyer ce type de données.
- Démonstration de Compact, qui retire les valeurs vides d'un Array, très utile pour nettoyer une liste. Introduction de Concat pour Arrays, permettant d'ajouter le contenu d'un Array à un autre.
- Introduction de la fonction Difference : calcule les valeurs distinctes entre deux Arrays, illustrée avec un exemple retirant un élément commun (« tech ») pour observer le résultat obtenu.
- Introduction de la fonction Find : retourne le premier élément d'une liste correspondant à des critères définis, démontrée avec l'exemple d'une liste de tags/contacts.
- Démonstration détaillée de Find avec des critères d'âge variables (supérieur à 35, puis à 45), illustrant comment le résultat change selon le seuil défini, retournant toujours le premier match trouvé.
- Présentation d'IndexOf pour Array : détermine la position d'une valeur spécifique dans la liste (exemple : « Premium » en position 1, « France » en position 2), utilisant l'indexation à partir de 0.
- Conclusion sur Intersect (intersection entre deux listes) et introduction d'IsEmpty/IsNotEmpty, permettant de vérifier si un Array contient ou non des éléments.
- Explication du fonctionnement d'IsEmpty (traduit littéralement « est vide ») : renvoie faux quand l'Array contient effectivement des valeurs, comme dans l'exemple avec trois éléments présents.
- Confirmation d'IsNotEmpty (vrai car trois éléments présents), puis introduction de Join permettant de réunir les valeurs d'un Array avec un séparateur personnalisable (exemple avec un « + »).
- Démonstration de la fonction Merge sur deux Arrays d'objets distincts (l'un avec nom/âge, l'autre avec ville de Berlin/pays), préparant une fusion complète de ces structures de données.
- Résultat de la fusion Merge : les quatre objets distincts (2+2) sont réunis en un seul objet combiné mélangeant toutes les valeurs, illustré par l'exemple de Nathan associé à ses différentes propriétés.
- Présentation de la fonction Pluck, comparable à Map mais spécifiquement conçue pour extraire une propriété précise de chaque objet d'une liste (exemple : tous les Last Name en une seule liste texte).
- L'auteur choisit délibérément de ne pas couvrir une fonction jugée trop complexe et rarement utilisée personnellement, puis introduit RenameKeys, pratique pour renommer les clés d'une structure de données.
- Rassurance sur la densité des fonctions présentées (nécessaire pour la complétude), puis démonstration de Reverse : inverse l'ordre des éléments, le premier (index 0) devenant le dernier et inversement.
- Présentation de Smart Join, similaire à Merge mais adaptée à un format de données parfois rencontré dans d'anciennes API (structure « Field/Age/Value » plutôt que le format standard clé-valeur).
- Cas d'usage concret de Smart Join avec les champs personnalisés (custom fields) retrouvés dans des outils comme ClickUp, où la structure field/valeur permet de gérer des noms de champs non prédéfinis.
- Présentation de SortToJSONString, transformant tous les éléments d'un Array en une unique string JSON, permettant ensuite de la manipuler comme n'importe quel texte avec les fonctions de string classiques.
- Démonstration de Splice, permettant d'ajouter ou retirer un élément à une position précise d'un Array (exemple : insérer « bonjour » à un emplacement spécifique de la liste).
- Présentation d'Union : fusionne deux Arrays en supprimant automatiquement les doublons (exemple : un élément présent dans les deux listes n'apparaît qu'une seule fois dans le résultat final).

## Concepts cles
- introduction aux fonctions Array (nombreuses, nécessitant attention)
- opérateurs Array communs avec le texte mais adaptés (Length)
- distinction Contains (partiel) vs Includes (exact) pour les Arrays
- introduction de la fonction Map (importante pour transformer une liste entière)
- syntaxe Map avec notation 'item =>' (transformation par élément)
- démonstration pratique de Map avec Concat sur chaque contact
- Map appliqué aux valeurs numériques (exemple Round sur salaires)
- fonction Filter sur Array avec condition numérique
- résultat pratique de Filter (extrêmement utile et fréquent)
- fonction Chunk pour diviser un Array en groupes
- préparation d'exemple avec une valeur vide ajoutée à un Array
- fonctions Compact (nettoyage valeurs vides) et Concat pour Arrays
- fonction Difference pour calculer les valeurs distinctes entre deux Arrays
- fonction Find pour retourner le premier élément correspondant
- comportement de Find selon différents seuils de critère
- fonction IndexOf pour Array (localisation de position)
- fonctions Intersect et IsEmpty/IsNotEmpty
- comportement d'IsEmpty selon le contenu de l'Array
- IsNotEmpty et fonction Join avec séparateur personnalisable
- préparation de Merge sur deux Arrays d'objets distincts
- résultat de fusion Merge combinant plusieurs objets en un
- fonction Pluck pour extraire une propriété spécifique de chaque objet
- fonction jugée trop complexe (non couverte) et introduction de RenameKeys
- fonction Reverse (inversion de l'ordre des éléments)
- fonction Smart Join pour format de données legacy (Field/Value)
- cas d'usage Smart Join pour champs personnalisés (ClickUp)
- fonction SortToJSONString (Array vers string JSON manipulable)
- fonction Splice pour ajout/retrait d'élément à position précise
- fonction Union (fusion avec suppression automatique des doublons)

## Outils mentionnes
- n8n
- ClickUp

## Tips techniques
- Utiliser Includes pour une correspondance exacte d'élément dans un Array, et Contains pour une correspondance partielle
- Utiliser Chunk pour diviser une grande liste en groupes de taille définie, utile pour un traitement par lots
- Utiliser Compact pour nettoyer automatiquement les valeurs vides d'un Array avant traitement

## Cas d'usage reels
- [[]]
