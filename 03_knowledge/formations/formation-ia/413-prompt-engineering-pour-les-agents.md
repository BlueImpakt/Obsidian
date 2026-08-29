---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.13 Prompt engineering pour les agents.txt"
---

# 4.13 Prompt engineering pour les agents

## Resume
- Introduction au module prompt engineering pour les agents, avec présentation d'un document exhaustif et d'une version mindmap complémentaire pour faciliter la compréhension de la stratégie globale.
- Principe clé de prompting mécanique pour agents : donner un maximum de ressources avec un minimum de mots, en énumérant des situations distinctes plutôt qu'un gros paragraphe descriptif.
- Méthode d'isolement du type d'action à tester (obtenir événements du jour/mois/année) pour valider systématiquement chaque variante face à des cas d'usage multiples (plusieurs calendriers).
- Recommandation du version control de prompt, empruntée au vocabulaire développeur : créer des points d'étape systématiques pour retester l'ensemble à chaque ajout de modification.
- Méthode de construction progressive du prompt à partir de zéro : démarrer avec le prompt le plus simple possible pour l'étape 1, le tester intensivement avant d'ajouter de la complexité.
- Mise en garde contre une croyance erronée fréquente : connecter un outil (ex : Airtable) à un agent ne garantit pas automatiquement qu'il sache l'utiliser correctement sans instructions explicites.
- Métaphore du karting sans rails : contrairement à une automatisation classique avec garde-fous (arrêt si étape A échoue), un agent IA n'a pas ces protections natives, il faut les construire soi-même.
- Recommandation professionnelle : plus il y a de documentation autour d'un agent, plus cela décharge de responsabilité dans un cadre où l'on doit rendre des comptes ; introduction des trois frameworks de prompting.
- Présentation du framework court de prompting, adapté aux nœuds LLM simples (pas les agents complexes) pour des tâches basiques ne nécessitant pas une structure élaborée.
- Recommandation de privilégier un modèle peu coûteux (open source ou Gemini en version légère) plutôt que des modèles premium onéreux pour les tâches simples ne nécessitant pas de raisonnement complexe.
- Présentation des quatre parties du framework court de prompting : objectif/rôle, instructions détaillées, exemples, et variables.
- Exemple concret de définition du rôle (« tu es un excellent copywriter ») suivi d'instructions détaillées avec conditions explicites de type « fais ceci, ne fais pas cela ».
- Présentation de la partie exemples du framework court (illustration du résultat souhaité), suivie de la partie variables référençant les outputs des champs précédents (ex : date du jour).
- Précision sur l'usage des variables référençant des données d'étapes précédentes (ex : json.output), complétant la structure simple du framework court avant transition vers un framework plus long.
- Exemple de framework plus étoffé avec objectifs chiffrés explicites (ex : open rate espéré supérieur à 50%) et instructions de ton précises (clair mais drôle par petites touches).
- Présentation de la spécification de sortie dans le framework étoffé : demander explicitement un format JSON avec exemple de structure attendue précisée dans le prompt.
- Démonstration de définition d'exemples réussis dans le prompt (objets ayant bien fonctionné) combinée à des instructions de style d'écriture précises (net, précis, oral).
- Introduction du framework long avec ajout du SOP (Standard Operating Procedure) définissant l'ordre précis des tâches à exécuter, notamment quand plusieurs sous-agents sont impliqués.
- Distinction claire entre le SOP (ordre des étapes à suivre) et les instructions (consignes détaillées de comportement), deux éléments complémentaires mais distincts du prompt long.
- Astuce (hack) pour créer un SOP efficace : enregistrer une vidéo explicative en s'adressant comme à un collègue, puis utiliser un outil comme MacWhisper pour transcrire ce contenu explicatif.
- Détail de la méthode d'enregistrement vidéo pour créer un SOP : parler naturellement comme à un collaborateur, puis utiliser l'outil MacWhisper pour transcrire automatiquement le contenu.
- Recommandation de préciser les propriétés des outils utilisés (ex : filtrage par date) et d'adopter un format cohérent en camelCase pour nommer les actions (ex : sendEmail).
- Présentation d'options de fallback en cas d'échec (« zappe l'info », « réessaye », « appelle un humain ») avec transition vers les concepts fondamentaux distinguant workflows et agents.
- Recommandation pour la mise en production : structurer rigoureusement les prompts et les optimiser pour minimiser le nombre de tâches, une exigence de fiabilité renforcée par rapport à la phase de test.
- Présentation du chaînage de prompts (chain of prompts) : conditionner une action sur le résultat d'une étape précédente (ex : agir selon les plages horaires du calendrier avant de consulter les tâches Notion).
- Recommandation forte d'ajouter systématiquement un format de sortie JSON structuré dans le prompt, avec définition explicite des variables de sortie attendues.
- Recommandation d'utiliser le formatage Markdown (H2 pour rôle/objectif/contexte/SOP, H3 pour chaque outil) pour structurer visuellement un prompt long et complexe.
- Recommandation d'utiliser des paramètres facilement compréhensibles (pas de syntaxe inventée obscure), avec bonnes pratiques de gestion d'erreurs (fallback et messages d'erreur clairs).
- Recommandation d'utiliser les outils à API bien documentée (Notion, Airtable, Google Calendar, Drive, Docs, Sheets) tout en restant très explicite sur l'action précise attendue de chaque outil.
- Annonce d'exemples pratiques concrets tirés d'un document mis à disposition, illustrant les différents éléments de prompt engineering déjà présentés dans le module.
- Exemple de structuration d'un SOP par étapes séquentielles avec sous-étapes conditionnelles (2.1, 2.a), une logique similaire à des instructions if-then appliquées directement au prompt.
- Exemple complet d'arborescence de prompt recommandée : un agent coordinateur événementiel aidant une utilisatrice (Laura) via Google Workspace et Notion, analysant le type d'événement à organiser.
- Conclusion du module prompt engineering : recommandation de précision accrue du SOP et nécessité de synchroniser systématiquement les informations entre tous les outils utilisés.

## Concepts cles
- introduction au prompt engineering pour agents (document exhaustif + mindmap)
- principe clé : énumérer des situations distinctes plutôt qu'un paragraphe descriptif
- méthode d'isolement du type d'action pour valider systématiquement chaque variante
- recommandation du version control de prompt (retester après chaque ajout)
- méthode de construction progressive du prompt à partir de zéro (simplicité d'abord)
- mise en garde : connecter un outil ne garantit pas son utilisation correcte sans instructions
- métaphore du karting sans rails : absence de garde-fous natifs dans un agent IA
- importance de la documentation pour décharger la responsabilité en contexte professionnel
- présentation du framework court de prompting pour nœuds LLM simples
- recommandation de modèle peu coûteux pour les tâches simples (open source, Gemini léger)
- présentation des quatre parties du framework court (objectif, instructions, exemples, variables)
- exemple concret de définition de rôle et instructions conditionnelles précises
- présentation des parties exemples et variables du framework court
- usage de variables référençant des données d'étapes précédentes
- exemple de framework étoffé avec objectifs chiffrés et ton précis
- présentation de la spécification de sortie (format JSON avec exemple structuré)
- démonstration d'exemples réussis combinés à des instructions de style d'écriture
- introduction du SOP (Standard Operating Procedure) définissant l'ordre des tâches
- distinction claire entre SOP (ordre) et instructions (consignes de comportement)
- astuce : enregistrer une vidéo explicative pour créer un SOP via transcription
- détail de la méthode d'enregistrement vidéo et transcription via MacWhisper
- recommandation de format camelCase pour nommer les actions des outils
- présentation d'options de fallback en cas d'échec et transition vers workflows vs agents
- recommandation de structuration rigoureuse des prompts pour la mise en production
- présentation du chaînage de prompts conditionné sur le résultat d'une étape précédente
- recommandation d'ajouter systématiquement un format de sortie JSON structuré
- recommandation de formatage Markdown hiérarchisé (H2/H3) pour structurer un prompt long
- recommandation de paramètres compréhensibles et gestion d'erreurs avec messages clairs
- recommandation d'outils à API bien documentée et d'instructions explicites d'action
- annonce d'exemples pratiques concrets tirés d'un document de référence
- exemple de SOP structuré avec sous-étapes conditionnelles (logique if-then dans le prompt)
- exemple complet d'arborescence de prompt (coordinateur événementiel)
- conclusion : précision du SOP et synchronisation systématique entre outils

## Outils mentionnes
- n8n
- Airtable
- Gemini
- MacWhisper
- Notion
- Google Calendar
- Google Drive
- Google Docs
- Google Sheets
- Google Workspace

## Tips techniques
- Structurer un prompt d'agent en énumérant des situations distinctes courtes plutôt qu'en rédigeant un gros paragraphe descriptif ambigu
- Isoler et tester systématiquement chaque type d'action possible (jour/mois/année) plutôt que de valider uniquement le cas le plus simple
- Pratiquer le version control de prompt : créer des points d'étape systématiques et retester l'ensemble à chaque modification ajoutée
- Démarrer la construction d'un prompt d'agent avec la version la plus simple possible, la tester intensivement, avant d'ajouter progressivement de la complexité
- Ne jamais présumer qu'un agent saura utiliser correctement un outil connecté sans instructions explicites précises sur son usage attendu
- Construire soi-même des garde-fous explicites dans un agent IA (contrairement à une automatisation classique), qui n'en possède pas nativement
- Documenter systématiquement les agents dans un cadre professionnel, la documentation servant de protection de responsabilité
- Utiliser un modèle peu coûteux (open source ou version légère) pour les tâches simples, réservant les modèles premium aux besoins de raisonnement complexe
- Formuler les instructions d'un prompt avec des conditions explicites du type 'fais ceci, ne fais pas cela' pour un cadrage précis
- Intégrer des objectifs chiffrés explicites (ex : taux d'ouverture cible) dans le prompt pour orienter concrètement la génération
- Spécifier explicitement le format de sortie attendu (JSON avec exemple structuré) dans le prompt pour garantir une réponse exploitable
- Bien distinguer le SOP (ordre séquentiel des étapes) des instructions (consignes de comportement détaillées) dans un prompt d'agent complexe
- Enregistrer une vidéo explicative orale (comme à un collègue) puis la transcrire via un outil comme MacWhisper pour générer rapidement un SOP détaillé
- Adopter un format cohérent (camelCase) pour nommer les actions des outils dans un prompt d'agent, pour une meilleure clarté structurelle
- Prévoir des options de fallback explicites (zapper, réessayer, escalader vers un humain) dans le prompt d'un agent en cas d'échec d'une étape
- Optimiser les prompts pour minimiser le nombre de tâches lors du passage en production, une rigueur supérieure à la phase de test
- Utiliser le chaînage de prompts pour conditionner une action sur le résultat d'une étape précédente, plutôt que des instructions indépendantes
- Toujours définir un format de sortie JSON structuré avec variables explicites dans le prompt d'un agent, pour un résultat exploitable
- Structurer un prompt long avec du formatage Markdown hiérarchisé (H2 pour les sections principales, H3 pour le détail de chaque outil)
- Éviter toute syntaxe inventée obscure dans les paramètres d'un prompt, et toujours prévoir des messages d'erreur clairs en cas de fallback
- Rester très explicite sur l'action précise attendue même avec des outils à API bien documentée (Notion, Airtable, Google Workspace)
- Structurer un SOP avec des sous-étapes conditionnelles numérotées (2.1, 2.a) pour intégrer une logique if-then directement dans le prompt
- Toujours exiger explicitement dans le SOP la synchronisation des informations entre tous les outils utilisés par un agent

## Cas d'usage reels
- [[]]
