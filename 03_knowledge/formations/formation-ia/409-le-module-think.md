---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.09 Le module Think.txt"
---

# 4.09 Le module Think

## Resume
- Introduction au node Think, issu du Think Tool développé par Anthropic (créateurs de Claude), permettant à un agent de marquer une pause de réflexion structurée avant de résoudre une situation complexe.
- Démonstration d'un agent exemple illustrant le fonctionnement du ThinkToolNode, qui invite l'agent à réfléchir explicitement avant de formuler sa réponse finale.
- Exemple concret de raisonnement structuré produit par le Think Node (analyse de ce qui fait un bon hook narratif) avant transmission de la réponse finale au modèle principal.
- Configuration pratique du Think Tool sans paramètre spécifique, laissant l'agent réfléchir librement, testée sur une question ouverte sur les tâches du jour.
- Extension du prompt pour demander explicitement à l'agent de calculer, via le Think Tool et l'outil Get Task, les tâches réellement réalisables dans le temps disponible.
- Observation du processus de réflexion approfondie de l'agent qui évalue les différentes tâches récupérées pour construire une vue d'ensemble cohérente avant de répondre.
- Résultat de la première itération jugé trop volumineux, avec affinage du prompt en ajoutant une contrainte de temps précise (fin à 18h, 10 minutes par tâche) pour un calcul plus réaliste.

## Concepts cles
- introduction au node Think (Think Tool d'Anthropic pour Claude)
- démonstration du ThinkToolNode invitant l'agent à réfléchir avant de répondre
- exemple concret de raisonnement structuré via le Think Node (bon hook narratif)
- configuration pratique du Think Tool laissant l'agent réfléchir librement
- extension du prompt pour calculer les tâches réalisables via Think + Get Task
- observation du processus de réflexion approfondie pour construire une vue d'ensemble
- affinage du prompt avec contrainte de temps précise pour un calcul réaliste

## Outils mentionnes
- n8n
- Anthropic
- Claude
- OpenAI

## Tips techniques
- Combiner le Think Tool avec un outil de récupération de données (Get Task) pour permettre un calcul contextuel des tâches réalisables
- Ajouter des contraintes de temps précises (heure de fin, durée par tâche) dans le prompt pour obtenir un calcul de faisabilité réaliste

## Cas d'usage reels
- [[]]
