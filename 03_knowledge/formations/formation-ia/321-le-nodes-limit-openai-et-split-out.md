---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.21 Le Nodes Limit, OpenAI et Split Out.txt"
---

# 3.21 Le Nodes Limit, OpenAI et Split Out

## Resume
- Introduction à la première automatisation intégrant l'IA, présentée délibérément à ce moment pour introduire un nouveau module utile tout en construisant un cas d'usage pratique complet.
- Démonstration de configuration d'une clé API OpenAI : sélection de l'organisation (optionnelle mais utile si plusieurs), création d'une nouvelle clé API nommée explicitement (« N8N Formation »).
- Choix du modèle OpenAI (GPT-4o ou 4.1 mini) et construction du prompt demandant d'extraire les trois idées principales d'une newsletter, une tâche concrète illustrant l'usage de l'IA sur du contenu RSS.
- Poursuite de la construction du prompt avec définition du contenu, puis digression pédagogique pour illustrer un autre concept via le feed RSS précédemment récupéré.
- Introduction du concept de Limit : un flux RSS peut contenir plusieurs éléments simultanément (exemple 5 newsletters), nécessitant de limiter le traitement au premier élément pour la démonstration.
- Sélection de la valeur HTML1 sous forme d'Array (identifiable par les crochets), avec identification de plusieurs éléments vides (positions 2, 12, 14) à nettoyer avant traitement.
- Application de la fonction Compact pour supprimer les éléments vides identifiés, puis utilisation de Join pour rassembler tous les éléments restants en une seule chaîne de texte exploitable.
- Construction de l'instruction de format de sortie JSON pour le prompt IA, définissant explicitement la structure attendue avec un premier champ « titre de la newsletter » comme premier élément.
- Poursuite de la construction du JSON de sortie : ajout d'un résumé exhaustif de la newsletter en format string, puis début de construction d'un Array pour structurer plusieurs idées identifiées.
- Détail de la structure de chaque idée dans l'Array : titre de l'idée, index numérique (1, 2, 3...) et résumé de l'idée, une structure répétée pour chaque élément identifié par l'IA.
- Construction d'un second Array dédié aux propositions de contenu TikTok, avec structure similaire d'objets multiples incluant un titre pour chaque idée de vidéo.
- Rappel de l'importance du bon formatage JSON, avec ajout du script complet pour chaque TikTok et d'un index numérique pour ordonner les différentes propositions générées.
- Validation du résultat complet généré : titre de la newsletter (« l'IA révolutionne la fertilité »), résumé, trois idées structurées, et trois scripts TikTok correspondants, illustrant l'aboutissement du pipeline complet.

## Concepts cles
- introduction à la première automatisation IA (nouveau module intégré)
- configuration d'une clé API OpenAI (nommage explicite)
- choix de modèle OpenAI et prompt d'extraction d'idées de newsletter
- poursuite de la construction du prompt avec digression pédagogique
- introduction du node Limit pour traiter un seul élément parmi plusieurs
- identification d'éléments vides dans un Array à nettoyer
- application de Compact puis Join pour nettoyer et assembler le texte
- construction du format de sortie JSON attendu dans le prompt
- poursuite de la construction JSON (résumé + début d'Array d'idées)
- structure détaillée de chaque idée dans l'Array (titre, index, résumé)
- construction d'un Array de propositions de contenu TikTok
- ajout du script complet et de l'index pour chaque proposition TikTok
- validation du résultat complet (newsletter → idées → scripts TikTok)

## Outils mentionnes
- n8n
- OpenAI

## Tips techniques
- Définir explicitement la structure JSON de sortie attendue dans le prompt pour garantir un format exploitable par les étapes suivantes

## Cas d'usage reels
- [[]]
