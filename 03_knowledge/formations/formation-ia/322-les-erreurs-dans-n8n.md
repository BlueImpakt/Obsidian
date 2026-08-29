---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.22 Les erreurs dans N8N.txt"
---

# 3.22 Les erreurs dans N8N

## Resume
- Introduction à la gestion des erreurs sur N8n avec approche contre-intuitive : commencer par configurer le setup avant même de créer l'erreur elle-même, dans un workflow de test nommé « erreur x, y, z ».
- Démonstration de génération volontaire d'une erreur via un exemple d'API (Ocean) mal configurée, en utilisant une Curl Request de référence transformée en node HTTP pour illustrer un cas d'erreur réel.
- Nécessité d'activer un déclencheur permanent (Schedule Trigger, toutes les minutes) plutôt qu'un trigger manuel, car un workflow ne peut être activé qu'avec un déclencheur automatique réel.
- Présentation de deux méthodes pour être averti d'une erreur : journaliser l'erreur dans un Google Sheet ou une base Airtable, illustré par l'enregistrement dans une feuille RSS Feeds existante.
- Insistance sur l'importance de bien cataloguer les erreurs pour pouvoir les diagnostiquer précisément, sinon leur traçabilité devient difficile face à des sources d'erreurs multiples et diffuses.
- Présentation d'un hack très utile : Copy to Editor, qui permet de récupérer une exécution passée et d'épingler ses données directement dans l'éditeur pour faciliter le débogage et l'investigation.
- Configuration détaillée des champs à enregistrer lors d'une erreur : message brut reçu, code d'erreur, et message simple, formant une structure de log complète et exploitable.
- Ajout de l'ID du workflow et de l'ID d'exécution comme informations supplémentaires utiles pour retrouver facilement l'exécution concernée lors d'une investigation ultérieure.
- Exemple concret d'entrée de log complète : message d'erreur explicite (« API token is invalid »), avec le raw message complet pour une traçabilité exhaustive de l'incident enregistré.
- Recommandation d'ajouter une notification instantanée via la plateforme de messagerie préférée (Telegram, Slack, ClickUp Chat), l'auteur privilégiant personnellement Telegram pour ce type d'alerte.
- Explication du comportement en cas de succès : le flow continue normalement comme prévu, le node d'erreur ne se déclenchant que lorsque l'étape liée rencontre effectivement un problème.
- Validation finale du système d'erreur : un message précis (« erreur de workflow pour l'API Notion ») permet de savoir exactement où se situe le problème, bien plus utile qu'un message générique vague.

## Concepts cles
- approche contre-intuitive de gestion des erreurs (setup avant l'erreur elle-même)
- génération volontaire d'une erreur via API mal configurée
- nécessité d'un Schedule Trigger pour activer un workflow permanent
- méthodes de journalisation d'erreur (Google Sheet/Airtable)
- importance du catalogage précis des erreurs pour la traçabilité
- hack Copy to Editor pour déboguer via une exécution passée
- configuration des champs de log d'erreur (message brut, code, message)
- ajout de l'ID de workflow et d'exécution pour la traçabilité
- exemple concret de log d'erreur complet (token invalide)
- recommandation de notification instantanée via messagerie préférée
- comportement normal en cas de succès (flow continue sans interruption)
- validation d'un message d'erreur précis (vs message générique)

## Outils mentionnes
- n8n
- Google Sheets
- Telegram
- Slack
- ClickUp
- Notion

## Tips techniques
- Toujours cataloguer précisément chaque erreur (source, code, message) pour faciliter le diagnostic ultérieur
- Utiliser Copy to Editor pour récupérer les données d'une exécution passée et faciliter le débogage direct dans l'éditeur
- Configurer une notification instantanée via sa messagerie préférée (Telegram, Slack) en complément du log d'erreur

## Cas d'usage reels
- [[]]
