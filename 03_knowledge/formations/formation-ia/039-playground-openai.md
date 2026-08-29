---
tags: [formation, millenium]
module: Formation IA
section: "Maîtriser ChatGPT"
source_transcript: "0.39 Playground OpenAI.txt"
---

# 0.39 Playground OpenAI

## Resume
- Introduction au Playground d'OpenAI, décrit comme la face cachée de ChatGPT : une interface visuelle dédiée à ceux qui construisent avec l'API, permettant de tester différents paramètres et configurations avant de les intégrer dans du code.
- Démonstration rapide de la création d'une réponse de modèle dans le Playground, avec un aperçu d'une Curl Request (requête HTTP en ligne de commande), sujet qui sera détaillé plus longuement dans un module ultérieur dédié.
- L'auteur justifie l'usage de l'API OpenAI plutôt que de créer son propre modèle : la complexité de développement d'un modèle est trop élevée, et utiliser l'API garantit de rester à jour avec toutes les nouveautés sans avoir à refaire l'architecture à chaque évolution majeure.
- Présentation de la représentation API des GPT : chaque GPT configuré pour un objectif spécifique a son équivalent côté API. Introduction des concepts de threads (une discussion complète) et de messages (un aller-retour simple entre l'utilisateur et le LLM).
- Présentation de la fonctionnalité Imagination du Playground pour définir la génération d'images : format carré, choix de la qualité, niveau de modération, et fond transparent ou opaque, permettant de préconfigurer le modèle pour des tâches spécifiques.
- Suite de la configuration dans le Playground (fonctionnant sous GPT-4) : définition des instructions du modèle, ajout de fichiers, et définition de fonctions au format JSON pour appeler des API externes. Possibilité également de définir le format de sortie attendu (JSON structuré).
- Introduction à la création d'assistants dans le Playground, illustrée par un exemple personnel : un assistant nommé « Naval » avec pour instruction d'incarner le cerveau de Naval Ravikant et de générer des idées innovantes sur un script reçu, en utilisant le modèle O3 mini.
- Démonstration de l'appel à l'assistant créé : accès direct à l'assistant, possibilité d'édition, puis test en mode thread avec une question sur ce que Naval dit à propos de « learn to build ».
- L'assistant répond en s'appuyant sur des ressources du VectorStore associé (indiqué par le préfixe « VS »), générant une réponse structurée façon mini-article basée sur la base de connaissance vectorisée qui lui a été fournie.

## Concepts cles
- Playground OpenAI comme face cachée de ChatGPT
- interface visuelle dédiée aux développeurs API
- création de réponse de modèle
- aperçu des Curl Requests
- complexité de créer son propre modèle
- avantage de rester à jour via l'API OpenAI
- représentation API des GPT
- threads et messages
- paramètres de génération d'images (format, qualité, modération, fond)
- instructions du modèle et fichiers
- fonctions JSON pour appeler des API externes
- format de sortie JSON
- création d'assistants persistants
- exemple d'assistant personnalisé (Naval)
- appel et test d'un assistant en mode thread
- VectorStore comme base de connaissance de l'assistant
- réponse générée à partir de contenu vectorisé

## Outils mentionnes
- OpenAI
- ChatGPT

## Tips techniques
-

## Cas d'usage reels
- [[]]
