---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.02 Construire son 1er RAG.txt"
---

# 5.02 Construire son 1er RAG

## Resume
- Introduction à la construction du premier agent RAG dans N8n, retranscrivant directement ce qui a été fait sur la plateforme OpenAI, avec configuration d'une entrée sous forme de chat.
- Démonstration de connexion à l'assistant Naval créé précédemment via le compte OpenAI connecté, permettant d'interroger directement le contenu vectorisé.
- Résultat impressionnant de conceptualisation générée à partir d'un simple prompt (portabilité des savoirs, capital intellectuel comme nouvelle monnaie), illustrant la puissance du RAG bien configuré.
- Mise en garde contre le sur-engineering : pour de nombreux usages simples, une base de données vectorielle complexe (Supabase, etc.) est excessive par rapport aux besoins réels.
- Démonstration de configuration de base d'un agent RAG simple dans N8n : ajout d'un modèle (OpenAI), d'une mémoire simple, puis introduction du VectorStore comme outil connecté.
- Exemple de consigne de prompt pour forcer l'usage du VectorStore : instruction explicite d'utiliser le VectorStore pour enrichir la réponse, et de répondre honnêtement en cas d'absence d'information trouvée.
- Constat qu'un agent sans VectorStore connecté répond de manière générale basée sur ses connaissances d'entraînement plutôt que sur un contenu spécifique réellement vectorisé.
- Ajout effectif de l'outil Simple Vector Store, avec présentation des différentes catégories de Vector Stores disponibles dans N8n (MongoDB, Pinecone, Postgres, Supabase, Simple).
- Configuration de la description du VectorStore (« toutes les connaissances de Naval ») et paramétrage du nombre de meilleurs résultats à retourner par la recherche.
- Explication de l'option d'inclusion des métadonnées permettant de donner du contexte supplémentaire à chaque bout de texte vectorisé et stocké dans le VectorStore.
- Explication du rôle de l'embedding dans le processus RAG : transformer la question de l'utilisateur en vecteur pour en extraire les résultats les plus pertinents du VectorStore.
- Test du chat sollicitant effectivement le VectorStore, avec réponse honnête de l'agent indiquant qu'il n'a pas trouvé d'informations précises sur le concept recherché dans la base vectorisée.
- Analyse détaillée de l'input et de l'output du processus : la requête sur le concept Learn to Build/Learn to Sell est d'abord recherchée dans la mémoire de l'agent.
- Poursuite de l'analyse : l'agent détecte une interaction précédente en mémoire, sollicite le chat avec les instructions appropriées, et enrichit sa réponse à partir de cette mémoire.
- Observation technique du flux entre Mistral (interrogation du VectorStore vide) et OpenAI (réutilisation du résultat), illustrant l'articulation entre plusieurs modèles dans le pipeline RAG.
- Confirmation de la mise à jour de la mémoire avec le dernier échange, avant transition vers l'étape cruciale d'envoi des données dans le VectorStore pour pouvoir ensuite les retrouver.
- Démonstration de récupération d'un fichier (livre) via requête HTTP programmatique, un rappel que ces requêtes fonctionnent de manière identique en navigateur ou en code.
- Configuration de l'ajout de documents dans le VectorStore, avec paramétrage du batch size à 200, précisant que ce chiffre concerne le traitement par lots et non le découpage du texte.
- Configuration du modèle d'embedding (Mistral) et du Default Data Loader pour charger les documents depuis un fichier binaire, avec sélection du format de données approprié.
- Explication du chevauchement de texte (overlap) dans le découpage : conserver les 200 caractères précédents pour donner davantage de contexte et éviter une séparation trop abrupte entre chunks.
- Test d'exécution du workflow d'indexation : les données sont envoyées au Default Data Loader, deux batchs d'embeddings sont générés, confirmant le bon fonctionnement du pipeline d'ingestion.
- Confirmation de la vectorisation réussie de 390 items en deux batchs (200 puis 190), démontrant le fonctionnement automatique du traitement par lots du batch size configuré.
- Test avancé du RAG fonctionnel : question sur la relation entre l'auteur du livre (Eric Jorgensen) et Naval Ravikant, avec réponse correcte issue de la recherche vectorielle réussie.

## Concepts cles
- introduction à la construction du premier agent RAG dans N8n (retranscription depuis OpenAI)
- démonstration de connexion à l'assistant personnalisé via compte OpenAI
- résultat impressionnant de conceptualisation générée par le RAG
- mise en garde contre le sur-engineering d'une base vectorielle complexe pour des besoins simples
- démonstration de configuration de base d'un agent RAG simple (modèle, mémoire, VectorStore)
- consigne de prompt forçant l'usage du VectorStore et l'honnêteté en cas d'absence de réponse
- constat : un agent sans VectorStore répond sur ses connaissances générales, pas un contenu spécifique
- ajout du Simple Vector Store et présentation des catégories disponibles
- configuration de la description et du nombre de résultats retournés du VectorStore
- explication de l'option d'inclusion des métadonnées pour contexte supplémentaire
- explication du rôle de l'embedding dans l'extraction des résultats pertinents
- test du VectorStore avec réponse honnête d'absence d'information trouvée
- analyse détaillée de l'input/output et de la recherche en mémoire
- poursuite de l'analyse : détection de mémoire précédente enrichissant la réponse
- observation de l'articulation entre plusieurs modèles (Mistral et OpenAI) dans le pipeline RAG
- transition vers l'étape d'envoi de données dans le VectorStore (indexation)
- démonstration de récupération de fichier via requête HTTP programmatique
- configuration du batch size à 200 pour l'ajout de documents (distinct du découpage de texte)
- configuration du modèle d'embedding Mistral et du Default Data Loader
- explication du chevauchement de texte (overlap) pour éviter une séparation abrupte
- test d'exécution confirmant le bon fonctionnement du pipeline d'ingestion (2 batchs)
- confirmation de vectorisation réussie en deux batchs (390 items : 200+190)
- test avancé du RAG fonctionnel sur une relation entre auteur et sujet

## Outils mentionnes
- n8n
- OpenAI
- Supabase
- MongoDB
- Pinecone
- Postgres
- Mistral

## Tips techniques
- Éviter d'utiliser une base de données vectorielle complexe (Supabase, etc.) pour des besoins RAG simples, souvent overkill par rapport au besoin réel
- Instruire explicitement l'agent RAG de répondre qu'il ne connaît pas la réponse si elle n'est pas trouvée dans le VectorStore, plutôt que d'halluciner
- Configurer un chevauchement (overlap) entre les chunks de texte pour préserver le contexte et éviter une séparation trop abrupte du contenu

## Cas d'usage reels
- [[]]
