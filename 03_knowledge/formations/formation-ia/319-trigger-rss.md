---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.19 Trigger RSS.txt"
---

# 3.19 Trigger RSS

## Resume
- Introduction au node RSS (Feed Trigger), présenté comme non essentiel mais potentiellement utile, avec distinction entre deux variantes : RSS Read notamment, dont la différence sera précisée.
- Exemples concrets de flux RSS disponibles sur des blogs personnels (Justin Welch, Austin Kleon), illustrant que même des sites peu connus pour leur RSS en disposent souvent, parfois de façon cachée.
- Élargissement du concept : les flux RSS existent pour YouTube, les newsletters, les articles de blog, illustré par la newsletter IA connue « The Rundown » qui utilise ce système.
- Démonstration de la structure JSON d'un flux RSS : dernier article publié, image descriptive, et liste d'items successifs, illustrant la facilité d'accès structuré à ces données.
- Confirmation que le HTML complet de l'article (mise en forme, bordures, images, espacements) est retranscrit directement dans le flux RSS, offrant un accès riche au contenu original.
- Justification pédagogique de ce module : très probable que les utilisateurs intégrant l'IA dans leurs automatisations aient besoin d'utiliser le RSS, un outil hybride entre articles et blogs.
- Présentation d'un outil payant couvrant chaînes YouTube et newsletters, et introduction de Kill The Newsletter, une alternative gratuite qui génère un flux RSS à partir du nom d'une newsletter.
- Démonstration pratique d'inscription à une newsletter via l'adresse générée par Kill The Newsletter, permettant de recevoir automatiquement le contenu directement dans son automatisation N8n.
- Confirmation de la possibilité de multiplier les triggers RSS sur N8n pour suivre plusieurs sources simultanément (exemple : blog N8n en plus), sans limite pratique significative de nombre.
- Démonstration de création d'un nouveau Google Sheet dédié pour organiser et centraliser les flux RSS suivis (utilisation du raccourci sheets.new pour créer rapidement un nouveau document).
- Configuration de la feuille RSS Feed dans Google Sheets pour centraliser les différentes publications suivies, avec humour sur le nombre cumulé de Google Sheets créés au fil de la formation.
- Retour au workflow pour sélectionner le RSS Feed configuré et vérifier la connexion à la feuille Google Sheets, avec exécution de test pour valider la configuration.
- Introduction de RSS Read comme alternative permettant de lire spécifiquement à la demande un flux RSS défini dans la feuille de centralisation, obtenant le même type de résultat que le trigger classique.
- Confirmation de la flexibilité de l'approche : qu'on utilise un trigger unique par source ou une référence centralisée dans Google Sheets, on peut y regrouper newsletters, chaînes YouTube et autres sources.
- Démonstration d'ajout du flux RSS de la propre chaîne YouTube de l'auteur (affichage des 20 dernières vidéos publiées), avec configuration au format XML pour l'intégration dans le système.
- Explication de la structure résultante en deux lignes distinctes (une pour l'email, une pour les vidéos), permettant de suivre facilement l'arrivée de nouvelles vidéos via Google Sheets à mesure qu'elles sont publiées.

## Concepts cles
- introduction au node RSS avec distinction RSS Read vs autre variante
- exemples de flux RSS sur des blogs personnels (souvent cachés)
- diversité des sources RSS (YouTube, newsletters, blogs)
- structure JSON d'un flux RSS (items, image, article)
- richesse du contenu HTML retranscrit dans le flux RSS
- justification pédagogique de l'utilité du RSS pour l'automatisation IA
- Kill The Newsletter comme alternative gratuite pour créer un flux RSS de newsletter
- démonstration pratique d'inscription via Kill The Newsletter
- possibilité de multiplier les triggers RSS sans limite pratique
- création rapide de Google Sheet via raccourci sheets.new
- configuration de la feuille de centralisation des flux RSS
- test de connexion entre RSS Feed configuré et Google Sheets
- RSS Read comme alternative pour lecture à la demande
- flexibilité entre trigger unique et référence centralisée dans Google Sheets
- exemple d'ajout du flux RSS d'une chaîne YouTube personnelle
- structure en deux lignes distinctes pour suivre les nouvelles publications

## Outils mentionnes
- n8n
- Kill The Newsletter
- Google Sheets
- YouTube

## Tips techniques
- Utiliser Kill The Newsletter (gratuit) pour transformer n'importe quelle newsletter email en flux RSS exploitable
- Utiliser le raccourci sheets.new pour créer instantanément un nouveau Google Sheet sans passer par le menu

## Cas d'usage reels
- [[]]
