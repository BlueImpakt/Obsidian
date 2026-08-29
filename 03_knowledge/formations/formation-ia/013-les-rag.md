---
tags: [formation, millenium]
module: Formation IA
section: "Les Fondamentaux IA"
source_transcript: "0.13 Les RAG.txt"
---

# 0.13 Les RAG

## Resume
- Introduction au RAG (Retrieval Augmented Generation), concept central de l'automatisation IA permettant de créer des bases de connaissances pour améliorer la pertinence des réponses. Constat de départ : plus on apporte de contexte à une IA, plus les réponses sont satisfaisantes. Les LLM (ChatGPT, Claude) ont des données d'entraînement figées à une date de cutoff.
- Explique la première limite fondamentale des LLM : leurs données d'entraînement sont figées (cutoff), les rendant obsolètes sans recherche internet active. Solution : apporter des données supplémentaires sur lesquelles le modèle peut se baser, pour éviter des réponses hors-contexte.
- L'IA généraliste peut donner des résultats flous ou faux si elle manque de matière spécifique. Introduit la deuxième limite : les LLM n'ont pas accès aux documents privés d'un utilisateur ou d'une entreprise.
- Les LLM ne connaissent que ce qui est public sur Internet (biais visibles : styles d'œuvres copyrightées dans les images générées, Claude s'appuyant beaucoup sur Reddit). Sans données confidentielles fournies, réponses génériques et peu personnalisées — d'où la création du RAG, qui permet de nourrir les LLM d'une base de connaissances propre incluant des documents solides comme les SOP.
- L'acronyme RAG est décomposé : Retrieve (retrouver), Augment (enrichir), Generate (générer). Lors d'une requête, l'agent va piocher dans une base de connaissances vectorisée. Introduit le concept de vectorisation : transformer les données en petits fragments répartis dans un espace, car les LLM raisonnent par probabilités sur le mot suivant.
- Décrit le mécanisme de recherche par similarité sémantique : lors d'une question, un embedding est créé pour repérer les éléments les plus proches sémantiquement dans l'espace vectoriel (exemple : la zone autour du mot "chat"), puis le prompt est enrichi avec les passages trouvés avant de générer la réponse.
- Détaille trois cas d'usage concrets du RAG : le support client (réponses à des questions spécifiques), l'assistant documentaire (recherche rapide dans de très longs manuels de 150+ pages), et la base de connaissances d'entreprise alimentée collectivement — avantage clé : l'information est sourcée et validée puisque c'est l'utilisateur qui choisit ce qu'il met dans la base.
- Démarre la description du processus technique : ingestion de documents de tout type (PDF, pages web, drives, audio/vidéo transcrits en texte, images décrites). Introduit le chunking (découpage d'un texte de 180 pages en petits fragments) et l'embedding (encodage numérique entre -1 et 1 : plus les valeurs sont proches, plus elles sont proches dans l'espace).
- Explique la mécanique de récupération lors d'une requête : une nouvelle requête utilisateur crée elle-même un embedding placé dans le même espace vectoriel pour identifier les éléments les plus proches, qui servent de base à la réponse générée. Premier exemple de proximité sémantique (dog/cat/animal, king/queen/prince).
- Poursuit les exemples de proximité sémantique (car/bus/train ; apple/banana/orange/fruit), puis explique que chaque fragment de texte devient un point dans un espace à 1536 dimensions. Des mots proches sémantiquement (chat/félin) ont des coordonnées proches car le système capture le sens profond, pas seulement l'orthographe. Introduit la tokenisation avec l'exemple 'le chat dort sur le canapé'.
- Détaille la tokenisation et la transformation en coordonnées vectorielles. Les phrases de sens similaire obtiennent des vecteurs proches. Introduit les deux méthodes principales de calcul de similarité : le cosinus et la distance euclidienne, illustrées par une requête exemple 'Où est-ce qu'il dort l'animal ?'.
- Illustre la recherche vectorielle : la requête devient un vecteur, on calcule la distance avec tous les vecteurs existants, et les 5 résultats les plus proches sont retournés. La cosine similarity est la méthode la plus utilisée (angle entre vecteurs), la distance euclidienne existe aussi mais est moins représentée.
- Compare les modèles d'embedding OpenAI : le modèle 'large' (3072 dimensions) offre une précision supérieure mais coûte plus cher, tandis que le modèle 'small' (1536 dimensions) convient à la grande majorité des cas d'usage. Introduit Cohere, utile pour le re-ranking (réorganisation des résultats retrouvés).
- Explique le re-ranking en détail : au lieu de récupérer directement 3 éléments, on en récupère 10, on évalue leur pertinence par rapport à la question, puis on ne retient que les 3 plus pertinents pour composer la réponse — ce qui améliore la précision finale. Introduit les bases de données vectorielles (Pinecone, Supabase), indispensables face au volume de vecteurs à traiter.
- Le filtrage de métadonnées (ex: associer un chapitre à un fragment vectorisé d'un livre dans n8n) apporte du contexte additionnel à la recherche. Aborde l'optimisation d'index pour les gros volumes et les mises à jour en temps réel. Décrit le workflow d'ingestion RAG dans n8n : sources → découpage en fragments de 500-1000 tokens → vectorisation → stockage dans Supabase.
- Décrit le processus côté requête : déclenchement (webhook ou chat), vectorisation de la question, récupération des 5 meilleurs résultats via recherche vectorielle (Pinecone/Supabase), assemblage du contexte, génération de la réponse par le LLM, puis re-ranking final (Cohere) pour affiner un premier tri vectoriel souvent imprécis.
- Décrit visuellement le pipeline complet : un texte est splitté en petits bouts représentés par des points ayant des coordonnées précises dans un espace vectoriel, stockés avec leurs coordonnées et métadonnées associées. Lorsqu'un utilisateur pose une question, un nouveau vecteur 'Retriever' se positionne dans cet espace pour identifier les voisins les plus proches.
- Conclut l'explication schématique de la recherche vectorielle, puis redétaille le re-ranking : au lieu de ne récupérer que 3 éléments, le système en récupère une dizaine, évalue la pertinence de chacun par rapport à la question, puis ne retient que les 3 plus pertinents pour composer la réponse finale (Cohere cité comme outil).
- Transition vers la démonstration pratique avec Notebook LM, outil créé par Google permettant de créer facilement un RAG (équivalent conceptuel à un RAG construit dans n8n, mais accessible directement via l'interface Google). Début de la démo : recherche et téléchargement du PDF de l'Almanach de Naval Ravikant pour l'utiliser comme source.
- Démonstration pas à pas de l'ajout de sources dans Notebook LM : upload du PDF de l'Almanach via 'Choose File', puis ajout d'une vidéo YouTube (podcast de Naval Ravikant avec Joe Rogan) en copiant l'URL. Le RAG Notebook LM accepte jusqu'à 300 sources (podcasts, sites web, vidéos).
- Démonstration concrète d'une requête dans Notebook LM : la question 'Qu'est-ce que Naval dit sur learn to build, learn to sell ?' obtient une réponse quasi instantanée et complète, citant la citation exacte de Naval Ravikant, illustrant la rapidité et la pertinence de la recherche vectorielle en pratique.
- Montre une fonctionnalité clé de Notebook LM : chaque réponse est accompagnée de notes de bas de page (citations numérotées) indiquant précisément l'endroit dans le document source où l'information a été trouvée.
- Le système sait cibler une source spécifique selon la question posée (ex: une question sur le podcast Joe Rogan va chercher dans le contexte de cette source précise). Illustre une requête plus large et donc plus longue à traiter, nécessitant plus de recherche pour identifier ce qui est pertinent.
- Le système explore le contexte du podcast (transcript filtré), cherchant les passages les plus pertinents sur des thèmes comme la richesse et le bonheur, en citant la source précise (Joe Rogan Experience).
- Récapitule la richesse des formats de sources acceptés par Notebook LM (tweets, MP3, Google Docs, Google Slides) pour construire une base de connaissances. Introduit la limite principale de cette approche manuelle : il faut systématiquement ajouter soi-même chaque nouvelle source.
- Pour automatiser l'enrichissement continu de la base sans intervention manuelle, on utilise les API plutôt que Notebook LM. Présente une seconde façon de créer un RAG : la plateforme OpenAI (Playground), via la fonctionnalité 'Assistants'. Démonstration d'un assistant personnalisé 'Naval' avec un prompt de base, le modèle 4.1 et la fonctionnalité 'file search'.
- Détaille le Vector Store créé dans OpenAI en uploadant des fichiers (toutes les notes prises sur Naval Ravikant, appelées 'Naval's mind'), permettant d'interagir avec l'ensemble du contenu produit par cette personne. Ce processus manuel dans le Playground est identique à celui qui sera automatisé programmatiquement avec n8n.
- Montre l'accès à l'assistant OpenAI également possible via l'API. Récapitule les deux façons de créer un RAG : soit un 'RAG miniature' avec upload manuel de fichiers + accès API (OpenAI), soit un outil comme Notebook LM plus simple pour ajouter des sources. Introduit le 'hack' du podcast génératif de Notebook LM pour synthétiser de gros volumes de données ('deep dive conversation').
- Démonstration de la génération de podcast audio dans Notebook LM, découverte en direct que d'autres langues sont désormais supportées (Settings > Output language). Le podcast généré est personnalisable et des notes peuvent devenir des sources. Notebook LM est qualifié de meilleur outil pour étudier un contenu interactivement. Conclusion : pas d'API disponible pour Notebook LM contrairement à OpenAI.

## Concepts cles
- RAG comme base de connaissances
- importance du contexte pour la pertinence
- date de cutoff des LLM
- chatbots d'entreprise
- bases de connaissances
- limite de cutoff des LLM
- apport de données supplémentaires
- limite d'accès aux documents privés
- biais des LLM issus de données publiques
- RAG pour nourrir de données propres
- SOP comme source de référence
- décomposition de l'acronyme RAG
- vectorisation des données
- raisonnement probabiliste des LLM
- embedding de la requête
- recherche par proximité sémantique dans l'espace vectoriel
- cas d'usage : support client, assistant documentaire, base de connaissances d'entreprise
- fiabilité par sourçage manuel du contenu
- support client
- assistant documentaire pour manuels longs
- base de connaissances d'entreprise collaborative
- ingestion multi-format de documents
- chunking
- embedding
- encodage numérique entre -1 et 1
- mécanique de récupération par requête vectorisée
- proximité sémantique dans l'espace
- espace vectoriel à 1536 dimensions
- capture du sens profond vs orthographe
- tokenisation
- tokenisation et coordonnées vectorielles
- cosinus vs distance euclidienne
- recherche vectorielle top-5
- cosine similarity comme méthode dominante
- modèles d'embedding OpenAI (small vs large)
- Cohere et re-ranking
- re-ranking (10 → 3)
- bases de données vectorielles
- filtrage de métadonnées
- mise à jour d'index en temps réel
- workflow d'ingestion RAG dans n8n (500-1000 tokens/fragment)
- vectorisation d'un livre avec métadonnées de chapitre
- pipeline complet de requête RAG
- re-ranking comme étape finale
- schéma du pipeline vectoriel complet
- vecteur 'Retriever'
- re-ranking (rappel détaillé)
- Notebook LM comme outil de création de RAG simplifié
- upload de sources multiples dans Notebook LM
- limite de 300 sources
- rapidité et pertinence de la recherche vectorielle en pratique
- citations sourcées avec notes de bas de page
- ciblage de source selon la question
- impact de la largeur de la question sur le temps de traitement
- filtrage de transcript par thème
- richesse des formats de sources acceptés
- limite : ajout manuel systématique
- automatisation de l'enrichissement via API
- OpenAI Assistants comme mécanisme de RAG
- fonctionnalité 'file search'
- Vector Store OpenAI
- équivalence Playground manuel / automatisation n8n
- accès API à l'assistant OpenAI
- récapitulatif des deux méthodes de RAG
- hack : podcast génératif Notebook LM
- génération de podcast multilingue
- personnalisation du contenu du podcast
- limite : pas d'API pour Notebook LM

## Outils mentionnes
- ChatGPT
- Claude
- Reddit
- OpenAI (embeddings)
- Cohere
- Pinecone
- Supabase
- n8n
- Notebook LM
- Google
- Raycast (Mac uniquement)
- Google Docs
- Google Slides
- OpenAI Platform / Playground
- OpenAI Assistants (file search)
- GPT-4.1
- OpenAI Vector Store
- OpenAI API

## Tips techniques
- Transcrire audios et vidéos en texte et décrire les images avant de les intégrer dans le pipeline RAG
- Le modèle d'embedding 'small' suffit pour la grande majorité des cas d'usage, pas besoin du 'large' plus coûteux sauf besoin de précision accrue
- Récupérer davantage de résultats que nécessaire (ex: 10) puis les re-classer par pertinence pour n'en garder que les meilleurs (ex: 3), plutôt que de se limiter au premier tri vectoriel brut
- Ajouter des métadonnées riches (ex: numéro de chapitre) aux fragments vectorisés pour affiner la recherche
- Découper le texte en fragments de 500 à 1000 tokens avant vectorisation
- Utiliser la fonctionnalité 'file search' des Assistants OpenAI pour créer un RAG directement dans le Playground, sans passer par n8n
- Utiliser la fonctionnalité 'deep dive conversation' de Notebook LM (génération de podcast) pour synthétiser de gros volumes de données à digérer
- Changer la langue de sortie du podcast Notebook LM via Settings > Output language si le contenu généré est en anglais par défaut

## Cas d'usage reels
- [[]]
