---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.1 Les métadonnées dans les RAG.txt"
---

# 5.1 Les métadonnées dans les RAG

## Resume
- Sommaire du module RAG avancé et métadonnées : introduction, techniques d'optimisation, limites du RAG naïf, les trois couches du RAG, mise en œuvre du filtrage, implémentation pratique.
- Explication de la limite du RAG naïf : une simple comparaison vectorielle sémantique peut ramener des concepts proches mais non pertinents, ralentissant et confondant le LLM final.
- Présentation du premier mécanisme d'amélioration : le filtre de métadonnées appliqué avant la recherche vectorielle, avec possibilité d'utiliser FromAI pour laisser l'agent choisir ses catégories de filtre.
- Présentation de la technique de metadata filtering par classification préalable des documents entrants : attribuer une catégorie ou un titre à chaque document lors de son ingestion dans le VectorStore.
- Explication du terme « naïf » appliqué au RAG classique : l'agent assume naïvement que toute l'information récupérée est pertinente, alors qu'un filtrage préalable améliore la pertinence.
- Démonstration de configuration de filtres de métadonnées (Category, DocTitle) dans les options du Default Data Loader, avec valeur dynamique fournie par un agent.
- Précision que le VectorStore doit être préparé pour recevoir les filtres configurés, avec un setup similaire à celui déjà réalisé précédemment pour un VectorStore classique.
- Démonstration de sélection du projet et de la fonction MatchDocuments dans Supabase, une fonction par défaut nécessaire pour la recherche vectorielle avec filtres.
- Test du workflow Advanced RAG complet : trois documents N8n traités par l'agent, chacun recevant automatiquement une catégorie et un titre en métadonnées.
- Constat que les métadonnées par défaut sont peu informatives et quasi identiques pour tous les chunks, justifiant l'intérêt d'un enrichissement personnalisé des métadonnées.
- Observation des résultats enrichis contenant désormais une métadonnée de catégorie précise (ex : webhooks), démontrant la valeur ajoutée du filtrage par métadonnées.
- Configuration d'un agent de recherche (retrieval) utilisant le VectorStore Supabase avec description précise de l'outil (recherche de documents N8n) pour orienter son usage.
- Réflexion sur les limites du filtrage strict par document : une question sur les webhooks pourrait être liée à l'authentification ou aux agents IA, des connexions perdues par un filtre trop restrictif.
- Identification du risque de manque de contexte lors de l'analyse chunk par chunk, avec proposition d'envoyer le document complet en plus du chunk pour un meilleur choix de subtopic, au prix de tokens supplémentaires.

## Concepts cles
- plan de présentation du module RAG avancé et métadonnées
- explication de la limite du RAG naïf (résultats sémantiquement proches mais non pertinents)
- premier mécanisme : filtre de métadonnées appliqué avant la recherche vectorielle (via FromAI)
- technique de classification préalable des documents lors de l'ingestion
- explication du terme 'naïf' appliqué au RAG classique (pertinence non garantie)
- démonstration de configuration de filtres de métadonnées dans le Default Data Loader
- préparation du VectorStore pour recevoir les filtres de métadonnées configurés
- démonstration de sélection de la fonction MatchDocuments dans Supabase
- test du workflow Advanced RAG complet (catégorisation automatique de documents)
- constat de la pauvreté des métadonnées par défaut (justifiant l'enrichissement personnalisé)
- observation des résultats enrichis avec catégorie précise (exemple webhooks)
- configuration d'un agent de retrieval avec description précise de l'outil VectorStore
- réflexion sur les limites du filtrage strict (connexions perdues entre concepts liés)
- risque de manque de contexte chunk par chunk, solution d'envoi du document complet

## Outils mentionnes
- n8n
- Supabase

## Tips techniques
- Appliquer un filtre de métadonnées avant la recherche vectorielle pour éliminer le bruit sémantique, plutôt que de filtrer après coup
- Envoyer le document complet en complément du chunk isolé à l'agent si le contexte insuffisant nuit à la précision, en acceptant le coût en tokens

## Cas d'usage reels
- [[]]
