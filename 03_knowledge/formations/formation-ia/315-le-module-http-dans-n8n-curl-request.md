---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.15 Le module HTTP dans N8N  Curl Request.txt"
---

# 3.15 Le module HTTP dans N8N / Curl Request

## Resume
- Transition vers la construction de vraies automatisations sur N8n, en commençant par l'API Todoist (gratuite, sans besoin de paiement), un exemple accessible pour débuter concrètement la pratique.
- Recherche de la documentation développeur Todoist REST API, avec une petite hésitation face à plusieurs versions disponibles avant de sélectionner la bonne référence à utiliser pour la suite.
- Découverte de Curl Requests bien construites dans la documentation Todoist, l'auteur cherchant spécifiquement un exemple de requête pour obtenir la liste des tâches à illustrer.
- Construction manuelle de l'appel API sans Curl Request disponible : utilisation du node HTTP en méthode GET, avec mention de la fonctionnalité Import Curl abordée plus tard dans la formation.
- Rencontre d'une erreur d'authentification lors du premier test, résolue en configurant l'authentification via l'option Generic (plutôt que Predefined Credential Type) pour définir manuellement les identifiants.
- Explication de la nécessité de vérifier le mode d'authentification spécifique à chaque API, certaines ayant des méthodes customisées différentes du standard, la documentation étant la meilleure source d'information.
- Objectif pédagogique clarifié : construire la connexion de manière manuelle et customisée plutôt que d'utiliser une méthode prédéfinie, en configurant explicitement le Bearer Token identifié dans la documentation.
- Recherche d'un exemple supplémentaire dans la documentation pour illustrer davantage le pattern d'authentification, confirmant une structure similaire à travers différents endpoints de l'API.
- Validation du succès de l'authentification : récupération réussie des listes personnelles de l'utilisateur (perso, inbox, TikTok, YouTube) grâce au token du compte, confirmant le bon fonctionnement de la connexion.
- Exploration des propriétés retournées par l'API Todoist pour un projet : nom, date de dernière mise à jour, style de vue (probablement liste, kanban, etc.), format string, illustrant la richesse des métadonnées disponibles.
- Observation d'une limitation spécifique d'un ancien projet (impossibilité d'assigner des tâches). Transition vers l'objectif suivant : ajouter une nouvelle tâche à un projet via l'endpoint Create Task de l'API.
- Configuration de l'URL ciblant l'endpoint TASH pour créer une tâche, avec réutilisation de l'authentification Bearer déjà configurée, mais constat que cela ne suffit pas seul pour créer effectivement la tâche.
- Identification de la cause de l'échec : des arguments requis manquent. La documentation API précise généralement les champs obligatoires nécessaires pour qu'un appel API réussisse effectivement.
- Démonstration de deux méthodes équivalentes pour envoyer une donnée (Content = « acheter des olives ») : soit via un formulaire simple, soit via un JSON explicitement construit, les deux produisant le même résultat.
- Construction du JSON complet pour ajouter une tâche à un projet spécifique (liste perso identifiée comme résultat 1 dans la structure de données récupérée précédemment).
- Configuration du champ Project ID (type String) en allant chercher dynamiquement la valeur via les fonctions déjà maîtrisées, illustrant l'application pratique des connaissances acquises précédemment.
- Précision que la nomenclature de nommage des étapes est libre (pas de convention obligatoire), l'auteur nommant son module « post task dans projet » selon sa propre logique personnelle.
- Renommage en français des étapes (« Obtenir projet », « Créer tâche dans projet ») pour plus de clarté personnelle, en préparation de la création effective d'une nouvelle tâche liée au Project ID récupéré.
- Sélection du premier résultat (index 0, correspondant au projet perso) via indexation simple plutôt que via les fonctions Filter/Find plus complexes, choix pédagogique pour ne pas surcharger la démonstration du module HTTP.
- Vérification sur Todoist : les tâches créées précédemment n'appartenaient à aucun projet spécifique (par défaut dans Inbox), préparant le test de la nouvelle configuration avec Project ID correctement défini.
- Confirmation du succès : la nouvelle tâche (« faire une mousse au chocolat ») est bien créée dans le projet perso spécifié, validant la création programmatique complète d'une tâche liée à un projet.
- Constat qu'il n'y a pas de couleur sur les tâches (uniquement sur les projets), avec exploration d'une fonctionnalité alternative : ajouter un Array de labels pour tester cette possibilité de catégorisation.
- Débogage en direct du système de priorité de Todoist : découverte par tâtonnement que la priorité varie de 0 à 3 (0 étant probablement 'aucune priorité'), un test itératif pour comprendre l'échelle exacte.
- Confirmation du bon fonctionnement de la date d'échéance (19 juillet), illustrant comment interpréter et utiliser correctement les différentes valeurs de l'API. Introduction de l'objectif suivant : créer une sous-tâche.
- Démonstration de création de sous-tâche : dupliquer le module de création de tâche existant, puis remplacer la référence au Project ID par la valeur de la tâche parente (Parent Task) pour créer le lien hiérarchique.
- Validation de la création réussie de la sous-tâche, avec transition vers la démonstration de sa modification puis de sa suppression, illustrant le cycle de vie complet d'une tâche via l'API.
- Configuration de la modification de sous-tâche en utilisant dynamiquement l'identifiant de la sous-tâche créée précédemment, permettant de cibler précisément l'élément à modifier via son contenu.
- Rencontre opportune d'un souci technique servant de prétexte pour introduire le module Wait, présenté comme très utile pour créer des pauses entre deux nodes d'un scénario, un point détaillé par la suite.
- Configuration d'une pause de 5 secondes via le module Wait entre la création de tâche et l'étape suivante, illustrant un problème de référence de données (JSON ID) causé par l'ajout de ce nouveau node intermédiaire.
- Explication du comportement du module Wait : il est vide et sert uniquement à faire transiter la donnée, une caractéristique utile notamment pour certaines API nécessitant un délai avant traitement suivant.
- Conclusion enthousiaste sur la puissance de l'automatisation via les modules HTTP, avec annonce d'un futur exemple supplémentaire dans une vidéo dédiée pour approfondir davantage ces concepts.

## Concepts cles
- transition vers la pratique avec l'API Todoist (gratuite)
- recherche et sélection de la bonne version de documentation Todoist
- découverte de Curl Requests dans la documentation Todoist
- construction manuelle de l'appel API (GET), mention d'Import Curl
- résolution d'erreur d'authentification via option Generic
- nécessité de vérifier le mode d'authentification spécifique à chaque API
- approche manuelle et customisée de configuration d'authentification (Bearer Token)
- confirmation du pattern d'authentification similaire à travers les endpoints
- validation du succès de l'authentification (listes récupérées)
- exploration des propriétés d'un projet Todoist (nom, mise à jour, vue)
- transition vers la création d'une tâche via endpoint Create Task
- configuration de l'endpoint de création avec authentification réutilisée
- nécessité de vérifier les arguments requis dans la documentation API
- deux méthodes équivalentes pour envoyer une donnée (formulaire vs JSON)
- construction du JSON pour ajouter une tâche à un projet ciblé
- configuration dynamique du Project ID via fonctions apprises
- liberté de nomenclature pour le nommage des étapes
- renommage en français pour clarté personnelle des étapes
- choix pédagogique de simplicité (indexation directe vs fonctions complexes)
- vérification de l'affectation de projet par défaut (Inbox)
- validation du succès de création de tâche liée à un projet
- test de la fonctionnalité Array of Labels sur une tâche
- débogage itératif pour comprendre l'échelle de priorité Todoist (0-3)
- validation de la date d'échéance et transition vers les sous-tâches
- création d'une sous-tâche via duplication et référence à la tâche parente
- validation de sous-tâche et transition vers modification/suppression
- modification dynamique d'une sous-tâche via son identifiant
- introduction opportune du module Wait (pauses entre nodes)
- configuration de pause 5 secondes et problème de référence causé par l'ajout de node
- fonctionnement du module Wait (transit de données, délai pour API)
- conclusion sur la puissance de l'automatisation HTTP

## Outils mentionnes
- n8n
- Todoist

## Tips techniques
- Toujours vérifier dans la documentation API quels champs sont obligatoires avant de construire une requête de création

## Cas d'usage reels
- [[]]
