---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.23 Historique des executions sur N8N.txt"
---

# 3.23 Historique des executions sur N8N

## Resume
- Introduction à l'historique des exécutions sur N8n, en complément de la gestion des erreurs vue précédemment, pour comprendre tout ce qu'il y a à savoir sur le suivi des exécutions passées.
- Présentation d'Execution Data (Highlighted Data) : une fonctionnalité de sauvegarde similaire à Set Field, mais spécifiquement conçue pour marquer des données importantes à retrouver facilement dans l'historique.
- Présentation des statuts d'exécution filtrable : erreur, annulée, en file d'attente, en cours, réussie, ou en attente d'une étape, ainsi que le filtrage par tags pour une recherche facilitée.
- Démonstration pratique du Highlighted Data pour rechercher facilement une exécution spécifique (exemple : retrouver une exécution par un ID utilisateur précis), une fonctionnalité de recherche puissante.
- Présentation des informations affichées pour chaque exécution : date d'exécution, statut de réussite, et runtime (temps d'exécution total), des données essentielles pour le suivi de performance.
- Présentation de deux options de reprise après erreur : réessayer avec le workflow actuellement sauvegardé, ou avec le workflow original tel qu'il était au moment exact de l'erreur (si des modifications ont été faites entre-temps).

## Concepts cles
- introduction à l'historique des exécutions (complément à la gestion d'erreurs)
- fonctionnalité Execution Data/Highlighted Data pour marquer des données importantes
- statuts d'exécution filtrables et filtrage par tags
- démonstration pratique de recherche via Highlighted Data (ID utilisateur)
- informations affichées par exécution (date, statut, runtime)
- deux options de reprise après erreur (workflow actuel vs original)

## Outils mentionnes
- n8n

## Tips techniques
- Choisir de réessayer avec le workflow original (au moment de l'erreur) plutôt que l'actuel si des modifications ont été apportées entre-temps

## Cas d'usage reels
- [[]]
