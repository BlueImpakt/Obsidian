---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.04 Le node Information Extractor.txt"
---

# 4.04 Le node Information Extractor

## Resume
- Introduction au module Information Extractor : contrairement à l'agent IA conçu pour la flexibilité, ce module vise à extraire des données précises et structurées à partir d'un texte.
- Démonstration pratique d'extraction sur un article de blog copié-collé, avec présentation des trois méthodes de définition d'attributs : JSON, schéma, ou attributs séparés.
- Démonstration de définition d'un attribut « conclusion » pour extraire spécifiquement la section conclusion complète de l'article de blog analysé.
- Explication de la distinction entre attributs obligatoires (ex : conclusion, toujours présente) et attributs optionnels (ex : email, pas toujours présent), une flexibilité utile pour l'extraction de données variées.
- Confirmation que toutes les données définies (conclusion complète et email) ont été parfaitement extraites de l'article de blog, avec rappel de la possibilité alternative de définir un exemple JSON.
- Explication de la possibilité de préciser un format spécifique pour chaque attribut extrait (texte vs numérique), illustrée par des exemples comme date de publication ou valeur vie client.
- Démonstration d'exécution d'un workflow d'analyse complète de site web (Execute Workflow), plus lourd en ressources, permettant d'extraire des informations structurées (nom, tagline) automatiquement.

## Concepts cles
- introduction à l'Information Extractor (extraction précise vs flexibilité de l'agent IA)
- démonstration d'extraction avec trois méthodes de définition d'attributs (JSON, schéma, séparés)
- démonstration d'extraction d'un attribut spécifique (conclusion de l'article)
- distinction entre attributs obligatoires et optionnels dans l'extraction
- confirmation d'extraction complète et réussie des données définies
- précision du format d'attribut extrait (texte vs numérique)
- démonstration d'analyse complète de site web via Execute Workflow

## Outils mentionnes
- n8n

## Tips techniques
- Définir certains attributs d'extraction comme optionnels (ex : email) quand leur présence n'est pas garantie dans tous les textes traités
- Préciser explicitement le format attendu (texte, numérique, date) pour chaque attribut extrait par l'Information Extractor

## Cas d'usage reels
- [[]]
