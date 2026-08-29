---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.15 Les fonctions conditionnelles sur Make • Partie 1.txt"
---

# 2.15 Les fonctions conditionnelles sur Make • Partie 1

## Resume
- Introduction aux fonctions conditionnelles sur Make, présentées comme simples mais nécessitant une logique structurelle particulière. La condition principale abordée : la fonction IF.
- Démonstration de l'imbrication de conditions IF successives : chaque branche fausse peut contenir un nouveau IF avec sa propre condition (exemple : « si 2 est supérieur à 1 »), créant une chaîne de vérifications en cascade.
- Démonstration pratique dans Make avec un JSON réutilisé de session précédente : création d'une condition IF accessible via les fonctions générales (et non mathématiques) de l'interface.
- Résultat du test : la condition (2 égale 2) est appliquée sur les 10 valeurs de l'Array, retournant vrai pour chacune, illustrant l'application automatique d'une condition sur un ensemble de données.
- Poursuite de l'imbrication : au lieu de mettre « faux » directement, on peut y placer une nouvelle condition IF (réutilisant la valeur dynamique définie précédemment), permettant une structure de décision en cascade plus élaborée.
- Explication de l'imbrication multiple de conditions pour construire des processus décisionnels complexes : chaque niveau peut contenir sa propre condition, créant un arbre de décision structuré et flexible.
- Astuce pratique très utilisée par l'auteur : utiliser des guillemets vides comme valeur par défaut pour gérer les inscriptions sans prénom renseigné, préférant garder le mot « prénom » plutôt qu'un champ vide.
- Introduction d'une troisième voie de transformation : le Switch, particulièrement utile pour établir une valeur de correspondance à partir d'une valeur définie, un mécanisme différent des simples conditions IF.
- Démonstration du fonctionnement du Switch : il identifie une valeur dans une liste (exemple « Ramos ») et sort la correspondance associée, avec possibilité de définir autant de paires valeur/correspondance que nécessaire.
- Explication de la structure imbriquée d'objets complexes (exemple CRMContact) : un objet peut contenir des listes identifiables par crochets, chaque élément de la liste étant lui-même un objet avec ses propres propriétés.
- Démonstration des fonctions Omit (exclure un champ, exemple : faire disparaître le code postal) et Pick (opposé : conserver uniquement le champ sélectionné), deux fonctions complémentaires pour manipuler la structure de données.
- Introduction de la fonction Get, similaire à Pick mais différente dans son fonctionnement : elle s'applique aussi bien aux Arrays qu'aux objets, avec une exécution légèrement différente selon le type ciblé.
- Exemple pratique d'usage avancé de Get avec un opérateur numérique : récupérer un élément spécifique de liste en ajoutant un nombre à chaque itération, une stratégie utile pour parcourir séquentiellement des enregistrements.
- Différence clé entre Get et Pick : Get permet de creuser aussi profondément que nécessaire dans les niveaux d'imbrication (exemple : récupérer le code postal depuis une adresse), une flexibilité que Pick n'offre pas.

## Concepts cles
- introduction à la fonction conditionnelle IF
- imbrication de conditions IF successives en cascade
- localisation de la fonction IF dans les fonctions générales
- application automatique d'une condition sur toutes les valeurs d'un Array
- imbrication d'une condition IF à la place d'une valeur fausse
- arbre de décision complexe via imbrication multiple de conditions
- astuce des guillemets vides comme valeur par défaut pour champs manquants
- fonction Switch pour établir des correspondances de valeurs
- mécanisme de correspondance valeur/résultat du Switch
- structure imbriquée d'objets complexes avec listes internes (CRMContact)
- fonctions Omit (exclure) et Pick (conserver uniquement)
- fonction Get (similaire à Pick mais applicable Arrays et objets)
- usage avancé de Get avec incrémentation numérique pour parcourir une liste
- différence clé Get (creuse en profondeur) vs Pick (surface uniquement)

## Outils mentionnes
- Make

## Tips techniques
- Utiliser une condition IF avec valeur par défaut pour gérer élégamment les champs manquants (ex: prénom non renseigné dans un formulaire)
- Combiner Get avec un opérateur numérique incrémental pour parcourir séquentiellement les éléments d'une liste dans une automatisation
- Utiliser Get plutôt que Pick lorsqu'il faut accéder à une valeur profondément imbriquée dans plusieurs niveaux d'objets

## Cas d'usage reels
- [[]]
