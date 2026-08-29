---
tags: [formation, millenium]
module: Formation IA
section: "Comprendre l'Automatisation"
source_transcript: "1.08 Comprendre les documentations API.txt"
---

# 1.08 Comprendre les documentations API

## Resume
- Introduction à la documentation API, décrite comme le mode d'emploi permettant de comprendre le fonctionnement d'une API et d'envoyer correctement les données aux bons endroits, avec présentation d'un exemple visuel type.
- Justification du choix de l'exemple (Todoist) : c'est une des API les plus simples et compréhensibles pour débuter. L'auteur invite les utilisateurs déjà familiers avec la documentation API à passer cette vidéo, réservée aux débutants.
- Démonstration de navigation dans la documentation Todoist : identification de la version d'API pertinente (V2 plutôt que V1), illustrant l'importance de bien repérer la version documentée avant utilisation.
- Introduction du concept de Curl Request retrouvé dans la documentation : un élément qui sera particulièrement important à comprendre plus tard pour l'usage avec N8n, l'auteur annonçant un futur rappel pédagogique sur ce sujet.
- Explication de la structure d'URL Todoist utilisée par des outils comme Make ou N8n pour obtenir des informations : api.todoist.com/REST/V2, illustrant concrètement la structure d'adresse d'API vue précédemment.
- Identification de l'endpoint « project » visant à obtenir les détails des projets de l'utilisateur, avec introduction du header d'authentification permettant de garantir que ce sont bien les projets appartenant à l'utilisateur qui sont retournés.
- Recherche en direct par l'auteur (assumant ne pas connaître la réponse à l'avance) sur la signification du préfixe « Bearer » devant un token : un schéma d'authentification standard, illustré avec l'outil Raycast sur Mac.
- Conclusion sur cet endpoint simple : aucune donnée à envoyer ni filtrage nécessaire, l'objectif étant uniquement d'obtenir tous les projets. La réponse attendue prend la forme d'un Array contenant plusieurs objets séparés par des virgules.
- Transition vers un endpoint plus complexe nécessitant l'envoi de données : Todoist impose sa propre nomenclature pour structurer les tâches (contenu de la tâche et autres champs spécifiques attendus).
- Retour concret sur les booléens (true/false) dans le contexte des tâches Todoist, présentation des champs ordre, priorité, projet lié, et introduction du concept d'ID unique permettant de créer des bases de données relationnelles.
- Astuce pratique pour retrouver un identifiant unique (Project ID) : souvent visible directement dans l'URL de la plateforme (exemple donné avec LinkedIn), un raccourci utile pour éviter de fouiller dans la documentation.
- L'auteur choisit volontairement de ne pas surcharger d'informations à ce stade, annonçant un approfondissement futur. Présentation du panel d'actions disponibles sur les projets, incluant close/reopen une tâche.
- Démonstration de la création d'un nouveau projet via une requête de type POST, en précisant que seuls les types de données listés dans la documentation seront acceptés par l'API, les autres étant simplement ignorés.
- Explication du champ nom obligatoire pour la création de projet, et présentation de la fonctionnalité de projets indentés (projet enfant rattaché à un projet parent existant), ainsi que la définition de la couleur d'icône du projet.
- L'auteur fait le lien entre les actions listées dans la documentation Todoist et celles disponibles sur Make/N8n : ce sont exactement les mêmes actions retranscrites dans l'interface de ces outils d'automatisation.
- Observation sur l'évolution des pratiques API : POST est de plus en plus utilisé même pour des modifications, au détriment de PUT et PATCH jugés de moins en moins employés. Exemple de mise à jour de nom de projet et d'archivage.
- Conclusion pédagogique : la pratique reste essentielle pour vraiment maîtriser, mais cette introduction permet désormais d'aborder n'importe quelle documentation API pour comprendre comment codifier ses requêtes correctement.

## Concepts cles
- documentation API comme mode d'emploi essentiel
- choix de Todoist comme exemple d'API simple pour débutants
- identification de la version d'API pertinente dans la documentation
- introduction du concept de Curl Request (approfondi plus tard avec N8n)
- structure concrète de l'URL API Todoist (api.todoist.com/REST/V2)
- endpoint 'project' et header d'authentification associé
- Bearer comme schéma d'authentification standard
- endpoint simple de récupération sans filtrage (réponse en Array d'objets)
- nomenclature spécifique imposée par l'API pour l'envoi de données (tâches)
- champs de tâche Todoist (ordre, priorité, projet)
- ID unique pour bases de données relationnelles
- astuce : retrouver un ID unique directement dans l'URL de la plateforme
- panorama des actions disponibles (close/reopen task)
- création via POST avec types de données strictement définis
- projets indentés (projet enfant/parent)
- définition de la couleur d'icône
- correspondance directe entre documentation API et actions disponibles sur Make/N8n
- tendance : POST remplace progressivement PUT/PATCH pour les modifications
- conclusion : la documentation API comme mode d'emploi général réutilisable

## Outils mentionnes
- Todoist
- n8n
- Make
- Raycast
- LinkedIn

## Tips techniques
- Chercher un identifiant unique (Project ID, etc.) directement dans l'URL de la plateforme plutôt que dans la documentation

## Cas d'usage reels
- [[]]
