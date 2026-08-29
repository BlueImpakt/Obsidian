---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.1 Intégrer OpenRouter.txt"
---

# 4.1 Intégrer OpenRouter

## Resume
- Introduction à OpenRouter, un agrégateur permettant d'accéder à un large éventail de LLM (Anthropic, Azure, DeepSeek, etc.) via un point d'entrée unique.
- Justification de l'usage d'OpenRouter pour accéder à des modèles non natifs comme Perplexity, avec démonstration de configuration des credentials via le guide intégré.
- Présentation de l'option auto-top-up des crédits OpenRouter : rechargement automatique quand le solde descend sous un seuil défini (ex : recharge dès que le solde atteint 5).
- Aperçu de la diversité des modèles accessibles via OpenRouter : Mistral, Microsoft, Gemini de Google, Baidu, et bien d'autres fournisseurs internationaux.
- Exemple de sélection du modèle Perplexity Sonar Deep Research pour des recherches web, avec avertissement sur la nécessité de provisionner correctement son compte avant usage.
- Présentation des options de tri et de filtrage des providers OpenRouter (équilibré, par prix, par qualité, par latence) avec possibilité d'exclure certains providers pour raisons de confidentialité (ex : éviter la Chine/Alibaba).
- Présentation de la personnalisation des notifications OpenRouter, et de la possibilité de trier tous les modèles disponibles selon la longueur de contexte supportée.
- Recommandation de nommage explicite lors de l'ajout d'un modèle OpenRouter dans N8n (préfixe « OR » suivi du nom du modèle) pour identifier facilement sa provenance dans les workflows.
- Test pratique de recherche d'actualités récentes via le modèle Perplexity sollicité à travers OpenRouter, illustrant l'usage concret de recherche web en temps réel.
- Avis personnel sur Perplexity : interface client jugée supérieure à l'expérience via API, avec transition annoncée vers la suite du module sur les autres modèles disponibles.

## Concepts cles
- introduction à OpenRouter comme agrégateur d'accès à de multiples LLM
- justification d'OpenRouter pour accéder à Perplexity (modèle non natif)
- option auto-top-up des crédits OpenRouter (rechargement automatique)
- aperçu de la diversité des modèles accessibles via OpenRouter (Mistral, Baidu, etc.)
- exemple de sélection Perplexity Sonar Deep Research avec avertissement de provisionnement
- options de tri/filtrage des providers OpenRouter et exclusion pour confidentialité
- personnalisation des notifications et tri des modèles par longueur de contexte
- recommandation de nommage explicite des modèles OpenRouter (préfixe OR)
- test pratique de recherche d'actualités via Perplexity sollicité par OpenRouter
- avis personnel sur Perplexity (interface client vs API)

## Outils mentionnes
- n8n
- OpenRouter
- Anthropic
- Azure
- DeepSeek
- Perplexity
- Mistral
- Gemini
- Baidu
- Alibaba

## Tips techniques
- Activer l'auto-top-up des crédits OpenRouter pour éviter les interruptions de service liées à un solde insuffisant
- Exclure explicitement certains providers OpenRouter (ex : basés en Chine) si des considérations de confidentialité des données l'exigent
- Préfixer le nom des modèles OpenRouter ajoutés dans N8n (ex : 'OR Perplexity Sonar') pour identifier facilement leur provenance

## Cas d'usage reels
- [[]]
