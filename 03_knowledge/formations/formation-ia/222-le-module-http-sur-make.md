---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.22 Le module HTTP sur Make.txt"
---

# 2.22 Le module HTTP sur Make

## Resume
- Introduction au module HTTP sur Make, similaire à celui de N8n, permettant d'effectuer une requête auprès d'un serveur spécifique pour obtenir ou envoyer des données, une fonctionnalité déjà partiellement abordée précédemment.
- Présentation des différentes options du module HTTP, avec retour vers la documentation API de Todoist déjà utilisée précédemment comme exemple de référence pour construire une requête HTTP concrète.
- Justification du choix de Todoist comme exemple : une structure simple d'application todo, avec des tâches organisées en listes, disposant de dates d'échéance et de descriptions, idéale pour un exemple pédagogique.
- Configuration du type de contenu (JSON) dans la requête HTTP, avec le champ « Content » identifié comme seul élément requis par l'API pour créer une nouvelle tâche, illustrant la simplicité minimale requise.
- Identification de l'élément manquant : l'authentification, configurée via le champ Authorization, avec deux possibilités principales, dont l'usage d'un token, un élément généralement situé au même endroit dans toutes les API.
- Démonstration de récupération de la clé API depuis les réglages (section Intégration/Développeur) puis intégration après le mot « Bearer », confirmant le schéma d'authentification déjà présenté dans un module précédent.
- Confirmation du succès de la requête HTTP : la réponse contient bien le User ID et les données de la tâche créée (« faire bouillir l'eau des pâtes »), validant l'ensemble du processus de création via l'API.
- Démonstration de la création d'une sous-tâche liée à la tâche précédente, avec passage de la valeur récupérée de l'étape 1 (ID de la tâche parente) vers l'étape 2 via une virgule dans l'objet JSON.
- Présentation des critères optionnels disponibles pour affiner une tâche (ordre dans la liste, date d'échéance, durée), avec focus sur le champ Parent ID essentiel pour lier une sous-tâche à sa tâche parente.
- Explication d'une fonctionnalité commune de Make : quand un module n'a pas encore de données à tester, il demande d'exécuter un module unique pour générer les données test préalablement, un mécanisme standard de test.
- Test réussi du flow complet : création d'une tâche principale (« mettre les pâtes dans l'eau ») suivie de sa sous-tâche (« s'assurer que l'eau frémit »), validant l'enchaînement complet du scénario.
- Transition vers la récupération de données (GET) : ajouter un slash suivi de la valeur souhaitée pour cibler précisément un élément spécifique dans la base de données Todoist via l'endpoint approprié.
- Démonstration de récupération d'un projet spécifique (plutôt que des tâches) via l'endpoint Projects, en spécifiant le Project ID nécessaire pour cibler précisément l'élément souhaité, plutôt que d'obtenir tous les projets.
- Débogage en direct d'un problème de récupération de projet, avec tentative d'ajout d'une étape Parse Response pour résoudre l'erreur rencontrée, illustrant le processus itératif de résolution de bug en configuration API.
- Résolution d'une erreur « Task not found » identifiée comme un oubli du paramètre projet : une fois corrigé, la requête aboutit et retourne bien le projet lié à la première tâche créée (projet égal à Inbox).
- Introduction des Query Parameters, à distinguer du body de la requête : ces paramètres se définissent directement dans l'URL de la requête plutôt que dans le corps envoyé, illustré via l'exemple « get tasks ».
- Test complet du flow avec ajout de Parse Response, révélant qu'à chaque relance manuelle, une nouvelle tâche était recréée, un comportement important à comprendre pour éviter les doublons lors des tests.
- Observation d'une limite de pagination API : bien que 63 éléments existent au total, l'API filtre par lots de 50, illustrant l'importance de bien gérer la pagination pour récupérer l'intégralité des données.
- Conclusion sur l'intérêt majeur du module HTTP : permettre d'aller chercher des données d'une API même sans intégration native disponible sur Make, un usage extrêmement fréquent illustré par l'exemple personnel de l'outil FalAI.

## Concepts cles
- introduction au module HTTP sur Make (similaire N8n)
- retour à la documentation Todoist pour construire une requête HTTP
- Todoist choisi comme exemple pour sa structure simple
- champ Content comme seul élément requis pour créer une tâche
- configuration de l'Authorization avec token
- récupération et intégration de la clé API avec préfixe Bearer
- validation du succès de la requête HTTP (création de tâche confirmée)
- création d'une sous-tâche liée avec passage de valeur entre étapes
- champ Parent ID pour lier une sous-tâche
- mécanisme 'run this module only' pour générer des données de test
- validation du flow complet tâche + sous-tâche
- construction d'un endpoint GET pour cibler un élément précis
- récupération ciblée d'un projet spécifique via Project ID
- débogage en direct avec Parse Response
- résolution d'erreur 'Task not found' (paramètre projet manquant)
- distinction Query Parameters (URL) vs body de requête
- comportement de création de doublons lors de tests répétés manuellement
- limite de pagination API (filtrage par 50 malgré 63 éléments)
- module HTTP pour pallier l'absence d'intégration native
- exemple d'usage personnel (FalAI)

## Outils mentionnes
- Make
- n8n
- Todoist
- FalAI

## Tips techniques
- Attention : relancer manuellement un module de création recrée systématiquement une nouvelle entrée, générant des doublons de test
- Utiliser le module HTTP générique pour connecter n'importe quelle API même sans intégration native disponible sur Make

## Cas d'usage reels
- [[]]
