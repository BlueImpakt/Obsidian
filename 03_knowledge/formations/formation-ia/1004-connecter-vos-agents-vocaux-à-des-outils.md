---
tags: [formation, millenium]
module: Formation IA
section: "Agents Vocaux"
source_transcript: "10.04 Connecter vos agents vocaux à des outils.txt"
---

# 10.04 Connecter vos agents vocaux à des outils

## Resume
- Sommaire du module connexion d'outils aux agents vocaux : Knowledge Base Setup, Custom Functions, configuration d'outils externes, intégration serveur MCP, test d'agent en direct, et bonnes pratiques de conclusion.
- Configuration quasi complète de l'agent, il reste deux aspects à paramétrer : les outils et la knowledge base, cette dernière étant une sorte de RAG que Retell génère automatiquement pour alimenter l'agent de façon très simple.
- Une fois l'information vectorisée et ajoutée à la knowledge base (exemple « Clinique Martin »), l'agent y accède directement, ce qui permet de concentrer le prompt sur le comportement plutôt que sur les données brutes.
- Présentation des deux façons de connecter un outil externe à l'agent vocal : les webhooks/custom functions (appel direct déclenchant un workflow), ou le standard MCP où N8n agit comme serveur MCP et non comme client.
- Présentation des outils par défaut disponibles : terminer/raccrocher un appel, transférer un appel, et un outil calendrier natif via call.com permettant de vérifier une disponibilité et de prendre rendez-vous directement.
- Configuration pratique d'un outil personnalisé : récupération de l'URL de production, préférence pour la méthode POST plutôt que GET (méthode par défaut retenue), puis attribution d'un nom à l'outil (ex : vérifier calendrier).
- Ajout des paramètres avancés de l'outil : headers pour l'identification (compte, clé API), query parameters selon le service ciblé, et corps de requête en JSON pour transmettre des données à un autre workflow N8n.
- Point d'attention sur le mode de réponse de l'outil : choisir entre déclencher seulement le workflow ou attendre sa réponse complète via l'option « When Last Node Finishes », qui attend l'exécution intégrale avant de renvoyer le résultat.
- Configuration d'un outil MCP nommé « MCP N8N Calendrier » via l'URL du MCP Server Trigger préalablement créé dans N8n, utilisé ici pour permettre à l'agent de créer un événement dans Google Calendar.
- Recommandation de bien décrire chaque outil connecté (fonction exacte, données à envoyer), le serveur MCP étant présenté comme un outil très puissant permettant d'exploiter toutes les capacités end-to-end et de le connecter facilement à plusieurs agents.
- Test pratique en conditions réelles de l'agent configuré : un appelant fictif (Paul) demande les horaires, vérifie une disponibilité, puis prend rendez-vous le lendemain à 14h en confirmant son nom complet.
- Conclusion du module : les compétences acquises permettent de créer, personnaliser et rendre utiles des agents vocaux capables d'utiliser des outils et de communiquer avec les systèmes existants des clients, avec annonce des tests LLM et simulations à venir.

## Concepts cles
- plan de présentation de la connexion d'outils aux agents vocaux
- knowledge base Retell comme RAG généré automatiquement
- vectorisation de la knowledge base pour alléger le prompt
- deux méthodes de connexion d'outils : webhook/custom function vs MCP (N8n en serveur)
- outils par défaut (fin d'appel, transfert, calendrier call.com)
- configuration d'un outil custom (URL production, méthode POST)
- paramètres avancés d'un outil (headers, query parameters, JSON)
- option 'When Last Node Finishes' pour attendre la réponse complète du workflow
- configuration d'un outil MCP nommé pour créer des événements Google Calendar
- importance de la description précise des outils MCP
- MCP comme outil puissant réutilisable entre agents
- test pratique de bout en bout de l'agent (prise de rendez-vous)
- conclusion du module et annonce des tests LLM/simulations à venir

## Outils mentionnes
- Retell AI
- n8n
- call.com
- Google Calendar

## Tips techniques
- Déléguer les données factuelles à la knowledge base plutôt qu'au prompt, pour garder ce dernier concentré sur le comportement de l'agent
- Préférer la méthode POST à GET pour la configuration des outils personnalisés d'un agent vocal
- Toujours bien décrire précisément un outil MCP (fonction, données à envoyer) pour que l'agent l'utilise correctement

## Cas d'usage reels
- [[]]
