---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.14 Faire une requête HTTP.txt"
---

# 3.14 Faire une requête HTTP

## Resume
- Introduction au node HTTP sur N8n, décrit comme le pendant du webhook mais plus complet : capable à la fois de récupérer et d'envoyer des données, contrairement au webhook limité à la réception.
- Explication de la différence entre navigation web classique (rendering visuel dans le navigateur) et une requête GET directe qui obtiendrait le même contenu brut sans la mise en forme visuelle.
- Présentation de la structure d'URL des API (exemple api.notion.com) et méthode pour trouver la documentation officielle d'une API via une simple recherche du nom de service suivi de « documentation ».
- Rappel de la distinction entre paramètres du body (pour POST, envoyer des données) et Query Parameters (pour GET, filtrer une demande), une notion fondamentale déjà abordée mais réaffirmée ici.
- Conclusion de l'introduction au node HTTP : les données récupérées sont réutilisables dans les nodes suivants du workflow, avec recommandation à venir sur les bonnes pratiques d'usage.

## Concepts cles
- node HTTP comme pendant complet du webhook (envoi et réception)
- différence entre rendering navigateur et requête GET brute
- méthode de recherche de documentation API (nom + 'documentation')
- rappel body (POST) vs Query Parameters (GET, filtrage)
- conclusion : réutilisation des données HTTP dans les nodes suivants

## Outils mentionnes
- n8n
- Notion

## Tips techniques
- Chercher '[nom du service] documentation API' pour trouver rapidement la documentation officielle d'un service

## Cas d'usage reels
- [[]]
