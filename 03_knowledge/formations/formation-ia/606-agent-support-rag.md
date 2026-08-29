---
tags: [formation, millenium]
module: Formation IA
section: "Agents de Productivité"
source_transcript: "6.06 Agent Support RAG.txt"
---

# 6.06 Agent Support RAG

## Resume
- Introduction à la création d'un RAG intelligent combinant scraping et gestion de base vectorielle, avec deux outils essentiels : Firecrawl et Supabase.
- Présentation du modèle de prix Firecrawl : outil payant avec 500 crédits gratuits puis jusqu'à 3000 crédits par mois, plus une tarification par tokens API.
- Démarrage du crawling de la base d'informations de Framer, outil de création de sites web choisi comme cas d'usage pour cette démonstration.
- Configuration d'une limite de crawling à 50 pages, avec récupération d'une URL de suivi car le processus de crawling prend du temps.
- Précision sur la gestion des crédits épuisés : possibilité de récupérer un crawling précédent déjà effectué sans en relancer un nouveau.
- Résultat du crawling : récupération des neuf pages de premier niveau (getStarted, Accessibility, Account, CMS, etc.) de la documentation Framer.
- Exploration du deuxième niveau de crawling, récupération des questions et sous-pages à l'intérieur de la première page (ex : getStarted).
- Passage au troisième niveau où le contenu réel des articles apparaît, avec choix entre récupérer uniquement le niveau 1 ou aller plus en profondeur.
- Récupération du contenu au format Markdown avec les différentes URL associées, incluant le contenu détaillé d'articles comme Layout Grids.
- Utilisation du nœud Split Out pour filtrer et séparer les nombreux éléments et liens récupérés en éléments individuels traitables.
- Résultat du filtrage : 36 éléments conservés sur 49 (13 retirés), chacun contenant le contenu d'un article utilisable pour le RAG.
- Présentation d'une méthode alternative avec un ancien workflow : crawling simple du premier niveau puis extraction du Markdown transformé en JSON string via un nœud de code.
- Ajout d'une propriété de filtrage pour ne garder que les éléments contenant le mot 'article', avec configuration de la donnée envoyée dans le nœud de code.
- Utilisation de Claude pour générer directement le code du nœud de filtrage, à partir des données JSON d'entrée fournies en exemple.
- Test du code généré via un second nœud de code temporaire, en redirigeant temporairement le flux de données pour validation.
- Conseil général : en cas de difficulté avec le code, ne pas hésiter à faire appel à Claude ou une autre IA pour aider, l'objectif étant de montrer la pratique et le raisonnement.
- Présentation de deux approches de scraping : une voie économe en crédits Firecrawl, ou un processus manuel de récupération du HTML brut d'une URL.
- Présentation de la version simple de Firecrawl pour scraper une seule URL (scrape a URL and get its content), sans crawling multi-pages.
- Retour sur le workflow de crawling précédent pour poursuivre la démonstration de la partie la plus intéressante à venir.
- Introduction à la création d'une base de données vectorielle sur Supabase, avec choix d'un modèle d'embedding, recommandation de toujours privilégier celui de ChatGPT.
- Configuration des métadonnées à indexer : description (OGDescription simplifiée) et titre (Title) pour chaque article dans la base vectorielle.
- Confirmation de l'ajout des 36 articles courts dans le VectorStore, avec vérification visuelle du contenu correctement inséré.
- Configuration d'un Chat Trigger et d'un agent IA avec instructions system prompt : 'Tu es un expert connecté à un RAG enrichi à mon savoir'.
- Connexion du Vector Store Supabase à l'agent IA en tant qu'outil, utilisant la fonction Retrieve Document pour la recherche dans le RAG.
- Amélioration des résultats via le re-ranking avec Cohere, à activer directement dans la configuration de la base de données documents.
- Explication de l'intérêt des métadonnées : certaines données liées à une URL ne ressortent pas forcément dans les réponses sans elles pour donner du contexte.
- Premier test du RAG en conditions réelles : question sur l'ajout d'un nom de domaine Google sur Framer, réponse rapide via recherche dans le Vector Store.
- Démonstration de la capacité du RAG à croiser plusieurs articles différents pour enrichir sa réponse, illustrant la puissance du système.
- Mention d'une alternative moins chère au crawler utilisé (Website Content Crawler) pour éviter de multiplier les abonnements payants.
- Dernière étape pour rendre le workflow actif en production : activer le workflow une fois les structures d'embedding classiques en place.
- Astuce (hack) de personnalisation visuelle du chat intégré, accessible via une option de configuration spécifique.
- Utilisation d'un prompt demandant à l'IA de jouer un expert en design inspiré de Notion et Linear pour générer un style visuel soigné pour le chatbot N8N.
- Objectif de rendre le chatbot partageable directement aux utilisateurs, clients ou prospects, pour interagir en autonomie sans intervention humaine.
- Attente prudente du résultat du design généré, avec inquiétude que le style soit trop chargé (too much) et nécessite un ajustement.
- Application en direct du nouveau design généré sur le chat existant, avec incertitude assumée sur le résultat final avant test.
- Test final du chatbot avec une question sur le layout grid Framer, retournant un guide structuré avec instructions détaillées (clic sur logo Framer, propriétés).
- Conclusion enthousiaste sur l'intelligence du système RAG créé, avec invitation à tester et réutiliser le template associé à la vidéo.

## Concepts cles
- introduction au RAG combinant scraping et base vectorielle (Firecrawl, Supabase)
- présentation du modèle de prix Firecrawl (500 crédits gratuits, jusqu'à 3000/mois)
- démarrage du crawling de la base d'informations de Framer
- configuration d'une limite de crawling et récupération d'une URL de suivi
- précision sur la récupération d'un crawling précédent en cas de crédits épuisés
- résultat du crawling : 9 pages de premier niveau récupérées
- exploration du deuxième niveau de crawling (sous-pages et questions)
- passage au troisième niveau de crawling (contenu réel des articles)
- récupération du contenu au format Markdown avec les URL associées
- utilisation du nœud Split Out pour séparer les éléments récupérés
- résultat du filtrage : 36 éléments conservés sur 49
- méthode alternative : crawling simple puis transformation en JSON string via nœud de code
- ajout d'une propriété de filtrage sur le mot 'article' dans le nœud de code
- utilisation de Claude pour générer le code du nœud de filtrage
- test du code généré via un second nœud de code temporaire
- conseil général de faire appel à l'IA en cas de difficulté avec le code
- présentation de deux approches de scraping (Firecrawl économe vs HTML manuel)
- présentation de la version simple Firecrawl pour une seule URL
- retour sur le workflow de crawling précédent pour poursuivre la démonstration
- création d'une base vectorielle Supabase avec modèle d'embedding recommandé (ChatGPT)
- configuration des métadonnées indexées (description et titre)
- confirmation de l'ajout des 36 articles dans le VectorStore
- configuration d'un Chat Trigger et d'un agent IA avec system prompt RAG
- connexion du Vector Store Supabase à l'agent IA (fonction Retrieve Document)
- amélioration des résultats via le re-ranking avec Cohere
- explication de l'intérêt des métadonnées pour donner du contexte aux réponses
- premier test du RAG en conditions réelles (question sur domaine Framer)
- démonstration de la capacité du RAG à croiser plusieurs articles
- mention d'une alternative moins chère au crawler (Website Content Crawler)
- dernière étape : activer le workflow en production
- astuce de personnalisation visuelle du chat intégré
- utilisation d'un prompt d'expert design inspiré de Notion et Linear
- objectif de rendre le chatbot partageable en autonomie aux utilisateurs
- attente prudente du design généré (risque de style trop chargé)
- application en direct du nouveau design sur le chat existant
- test final du chatbot avec une question sur le layout grid Framer
- conclusion sur l'intelligence du système RAG et invitation à réutiliser le template

## Outils mentionnes
- Firecrawl
- Supabase
- Framer
- N8N
- Claude
- ChatGPT
- Cohere
- Website Content Crawler
- Notion
- Linear

## Tips techniques
- Fournir un exemple de données JSON d'entrée à Claude pour lui faire générer directement le code du nœud de filtrage N8N correspondant
- Toujours faire appel à une IA (Claude) en cas de blocage sur du code N8N, l'important étant de comprendre le raisonnement plutôt que le code exact
- Toujours privilégier le modèle d'embedding de ChatGPT/OpenAI lors de la configuration d'une base de données vectorielle
- Activer le re-ranking via Cohere sur la base de données documents pour améliorer significativement la pertinence des résultats du RAG
- Explorer les options de personnalisation visuelle disponibles pour le widget de chat intégré, souvent méconnues
- Demander à l'IA de jouer le rôle d'un expert en design inspiré de références connues (Notion, Linear) pour générer un style visuel soigné

## Cas d'usage reels
- [[]]
