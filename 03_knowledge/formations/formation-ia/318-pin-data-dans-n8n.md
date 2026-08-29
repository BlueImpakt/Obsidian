---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.18 Pin Data dans N8N.txt"
---

# 3.18 Pin Data dans N8N

## Resume
- Introduction à Pin Data, une fonctionnalité extrêmement importante lors de l'usage de services externes : elle permet de mémoriser l'output reçu pour éviter de le récupérer à nouveau à chaque test.
- Astuce pratique : copier les données JSON, demander à une IA de les modifier selon un besoin spécifique, puis les remettre dans l'Edit Output, illustrant une utilisation créative combinant Pin Data et IA.
- Limite pratique rencontrée : un workflow trop lourd dépasse la taille maximale autorisée pour la modification, une astuce étant de tronquer le JSON à un seul élément pour contourner cette limite technique.

## Concepts cles
- introduction à Pin Data pour mémoriser l'output d'un service externe
- astuce combinant copie JSON + modification IA + Edit Output
- limite de taille pour la modification de JSON (astuce : tronquer à un élément)

## Outils mentionnes
- n8n

## Tips techniques
- Copier les données JSON pinnées, les faire modifier par une IA selon un besoin précis, puis les réinjecter via Edit Output
- En cas de dépassement de taille maximale du JSON, le tronquer à un seul élément représentatif pour pouvoir le modifier

## Cas d'usage reels
- [[]]
