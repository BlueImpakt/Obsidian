---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.09 Les variables sur Make.txt"
---

# 2.09 Les variables sur Make

## Resume
- Introduction aux variables sur Make, décrites comme essentielles car présentes dans chaque module : un identifiant unique associé à un module contenant des données réutilisables ailleurs dans le scénario.
- Exemple illustratif de deux modules successifs (prénom d'un côté, lien de connexion privée de l'autre) partageant des variables entre eux, montrant comment une donnée générée par un module peut être réutilisée dans un module ultérieur.
- Démonstration de la création d'une variable personnalisée : accessible depuis une étape spécifique du scénario, pouvant être de différents types et nommée librement selon le besoin.
- Explication de l'icône « Set » pour déposer une variable dans un conteneur, et de « Get » pour la récupérer, deux fonctions symétriques permettant de définir puis réutiliser une donnée nommée librement.
- Exemple concret : définition d'une variable représentant le jour du jour actuel, récupérable ensuite à n'importe quel endroit du scénario, illustrant la portabilité des variables une fois créées.
- Présentation d'une utilisation avancée des variables via la fonction Map, illustrée par le choix dynamique d'un modèle LLM (Claude étant un exemple parmi plusieurs modèles de puissance variable disponibles).
- Explication de l'intérêt de la dynamisation via Map : rendre un paramètre (comme le nom du modèle) variable selon la réponse plutôt que fixe, en sélectionnant la case Map pour connecter cette valeur dynamiquement.
- Exemple d'application pratique de la dynamisation : éviter de devoir mettre à jour manuellement une date de webinaire à chaque récurrence, en allant chercher cette valeur dynamiquement via l'option Map depuis une source précédente.
- Poursuite de l'exemple du webinaire : récupérer automatiquement le prochain élément futur (première occurrence à venir) plutôt que de mettre à jour manuellement chaque semaine, une recherche dynamique de l'élément pertinent.
- L'auteur reconnaît que l'exemple simple présenté n'a pas d'intérêt direct en soi, mais annonce vouloir illustrer des cas d'usage concrets où cette dynamisation devient très utile, avec un premier exemple de définition de modèle LLM (Anthropic).
- Démonstration de configuration d'un appel LLM avec instructions dynamiques : choix du modèle, nombre de tokens maximal, et prompt personnalisé (« génère un post LinkedIn en te basant sur ce topic ») utilisant un ID récupéré depuis Google Sheets.
- Précision technique importante : la numérotation des modules dans Make suit l'ordre de création (et non l'ordre visuel dans le flow), un point clé pour naviguer efficacement dans un scénario complexe.
- Test en direct du scénario complet : exécution jusqu'à l'étape 4, avec génération d'un prompt et enregistrement automatique sur Google Sheets, illustrant l'exécution en temps réel du pipeline construit.
- Résultat concret de la génération : un post LinkedIn complet sur le thème des œufs et de la nutrition (« pourquoi les œufs ont besoin de plus de place dans votre nutrition »), illustrant l'aboutissement du prompt dynamique configuré.
- Introduction de l'étape suivante du scénario : router le contenu généré vers différents sous-scénarios via des filtres, avec l'exemple d'une colonne supplémentaire dédiée au style de contenu à appliquer.
- Démonstration d'une condition de filtre basée sur l'identité d'un auteur (Andrew Huberman ou Tony Robbins) : si validée, un nouveau message est envoyé à Claude demandant de réécrire le post LinkedIn dans le style de l'auteur en question, en réutilisant la variable de modèle définie précédemment.
- Démonstration de récupération de la variable contenant le post généré précédemment, pour l'insérer dans une nouvelle requête via une variable nommée (thisLinkedInPost), illustrant l'enchaînement de variables entre étapes.
- Configuration du prompt de réécriture stylisée (« comme s'il était écrit par [auteur] »), avec un filtre inversé exigeant que l'auteur soit précisément Andrew Huberman ou Tony Robbins pour déclencher cette réécriture.
- Vérification du bon fonctionnement : le modèle correctement transmis à Claude génère un post LinkedIn (« Pourquoi devenir un bon orateur ? ») qui est ensuite enregistré directement dans Google Sheets, validant le pipeline complet.
- Explication du chemin emprunté par le routeur : puisque l'auteur défini n'était pas vide, c'est la première voie qui a été empruntée par le scénario, confirmant la logique de sélection de branche selon les données présentes.
- Confirmation que le filtre valide correctement l'existence d'un auteur non vide, déclenchant la réécriture du prompt dans le style de Tony Robbins spécifiquement, illustrant le bon fonctionnement de la condition.
- Clarification importante sur le fonctionnement des routeurs : contrairement à l'idée reçue, Make ne traite pas toutes les branches simultanément mais séquentiellement selon un ordre défini, modifiable en cliquant sur le routeur pour réorganiser les routes.
- Illustration concrète de l'ordre d'exécution séquentiel des étapes du routeur : d'abord l'étape numéro 12, puis 15, puis 13, démontrant que l'ordre suit une logique précise et non un traitement parallèle instantané.
- Poursuite de la démonstration : bien que le scénario semble se diviser en plusieurs voies visuellement, l'exécution reste en réalité séquentielle. Une troisième route sans condition (fallback) est mentionnée, servant de voie par défaut.
- Ajout d'un module spécifique nommé POST permettant d'enregistrer le contenu généré précédemment (le post façon Tony Robbins, plus énergique) dans une variable pour une réutilisation ultérieure dans le scénario.
- Conseil d'optimisation important : plutôt que de dupliquer l'enregistrement sur chaque branche du routeur, laisser une seule voie sans filtre en dernière position pour récupérer la valeur de la variable, évitant ainsi les répétitions inutiles.
- Synthèse sur l'usage de Get/Set Variable : utile pour enregistrer des valeurs brutes, combiner des valeurs, ou les récupérer ultérieurement, avec la règle stricte que le nom utilisé dans Get doit correspondre exactement à celui défini dans Set.
- Test en direct avec une valeur « personne » comme auteur, déclenchant simultanément les deux branches pour observer le comportement du scénario avec ce cas de test particulier.
- Analyse du résultat du test : la métaphore du « gardien de la porte » illustre qu'une branche a été bloquée (condition non remplie pour Andrew Huberman) tandis que l'autre, sans gardien, a laissé passer la donnée sans restriction.

## Concepts cles
- définition des variables Make (identifiant unique par module)
- exemple de partage de variables entre modules successifs
- création pratique d'une variable personnalisée
- fonctions Set (déposer) et Get (récupérer) une variable
- exemple concret de variable réutilisable à tout endroit du scénario
- fonction Map pour rendre un paramètre dynamique (exemple choix de modèle LLM)
- intérêt de rendre un paramètre dynamique plutôt que fixe via Map
- exemple pratique : date de webinaire dynamisée pour éviter mise à jour manuelle
- récupération automatique du prochain élément futur pertinent
- annonce de cas d'usage concrets pour la dynamisation de variables
- configuration LLM avec prompt dynamique basé sur Google Sheets
- numérotation des modules par ordre de création, pas visuel
- test en direct du pipeline complet jusqu'à l'étape de génération
- exemple de résultat généré : post LinkedIn sur la nutrition
- routage post-génération vers différents sous-scénarios selon le style
- condition de filtre par auteur déclenchant une réécriture stylisée
- insertion d'une variable de post généré dans une nouvelle requête
- filtre inversé exigeant un auteur précis pour la réécriture
- validation du pipeline complet (modèle transmis, contenu généré, enregistré)
- logique de sélection de branche selon la présence de données
- validation de la condition d'existence déclenchant une réécriture ciblée
- traitement séquentiel des routes (pas simultané), ordre modifiable
- exemple concret d'ordre d'exécution séquentiel (12 → 15 → 13)
- route sans condition (fallback) parmi les branches séquentielles
- module POST pour sauvegarder un contenu généré dans une variable
- optimisation : voie unique sans filtre en dernière position pour éviter la duplication
- synthèse usage Get/Set Variable
- règle de correspondance exacte des noms
- test en direct avec un cas limite (auteur = personne)
- métaphore du gardien de la porte pour illustrer le filtrage sélectif

## Outils mentionnes
- Make
- Claude
- Anthropic
- Google Sheets

## Tips techniques
- Utiliser la fonction Map pour rendre un paramètre dynamique plutôt que de le fixer manuellement à chaque scénario
- Dynamiser une date récurrente (webinaire) via Map plutôt que de la mettre à jour manuellement à chaque occurrence
- Se souvenir que la numérotation des modules Make suit l'ordre de création, pas leur position visuelle dans le scénario
- Se rappeler que Make traite les routes d'un routeur séquentiellement selon un ordre défini, pas en parallèle simultané
- Placer une voie sans filtre en dernière position d'un routeur pour centraliser l'enregistrement final plutôt que de le dupliquer sur chaque branche
- Toujours utiliser exactement le même nom entre Set Variable et Get Variable pour que la récupération fonctionne

## Cas d'usage reels
- [[]]
