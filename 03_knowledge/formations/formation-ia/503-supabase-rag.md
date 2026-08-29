---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.03 Supabase RAG.txt"
---

# 5.03 Supabase RAG

## Resume
- Introduction à la construction d'un RAG plus avancé via Supabase, avec organisation méthodique du travail (renommage et duplication des workflows simple/compliqué).
- Anecdote sur l'origine du nom Supabase, conçu pour concurrencer Firebase (propriété de Google), ce dernier étant critiqué pour avoir historiquement abandonné plusieurs produits utilisés par des startups.
- Exemple de structure de données typée dans Supabase : un type utilisateur avec identifiant unique, nom (String), statut actif (boolean), email (String), illustrant la rigueur du typage.
- Présentation des avantages de Supabase au-delà de la base Postgres : authentification facilitée intégrée, une surcouche pratique ajoutée par rapport à une base Postgres classique.
- Présentation du dernier avantage majeur de Supabase : la Realtime Database, une base de données en temps réel très utilisée pour les applications nécessitant des mises à jour instantanées.
- Mise en garde sur la limite de performance de la flexibilité : au-delà d'un certain volume de données, le système commence à ralentir, un compromis à connaître.
- Anecdote sur la découverte d'Airtable il y a près de 10 ans, un outil ayant compris le besoin de typage de données plus riche que du simple texte ou nombre non structuré.
- Présentation des types de colonnes riches disponibles dans Airtable (pièces jointes, cases à cocher, sélections multiples, dates) et des formules de type Vlookup entre bases connectées.
- Précision sur la limite de scalabilité d'Airtable : plafonné à 100 000 enregistrements par base, un outil pensé pour des applications d'entreprise, pas pour des millions d'utilisateurs.
- Explication de la philosophie open source de Supabase, permettant de self-hoster sa propre instance sur un serveur (exemple via Railway), un avantage majeur sur des solutions fermées.
- Démonstration de création d'un nouveau projet Supabase avec définition du mot de passe et sélection de la région (Europe), une étape de configuration initiale standard.
- Démonstration de création de colonnes dans Supabase, jugée moins intuitive qu'Airtable mais rapidement compréhensible, avec définition d'une colonne de type texte.
- Présentation des templates de démarrage Supabase, avec choix du template Langchain permettant de vectoriser directement les éléments à intégrer dans la base.
- Débogage en direct d'une erreur de syntaxe SQL liée à la valeur 1536 (dimension d'embedding), illustrant les aléas techniques fréquents lors de la configuration initiale.
- Confirmation de la réussite de la requête SQL de création de table (« Success, no rows returned »), avec apparition de la table « documents » dans la base de données.
- Explication de la structure de la table documents : trois colonnes (content, metadata, embedding) correspondant au contenu scanné, aux données additionnelles, et à la traduction vectorisée du texte.
- Démonstration de sélection de la table documents et reconnexion de l'embedding avec Mistral, avec ajout du nœud Supabase VectorStore configuré pour ajouter des documents.
- Nettoyage des données superflues du JSON reçu via le module Extract From File, pour ne conserver que les éléments réellement utiles avant vectorisation.
- Contrainte technique importante : impossible de configurer la taille de dimension d'embedding avec Mistral pour ce cas d'usage, nécessitant de basculer vers OpenAI et de choisir précisément les dimensions.
- Observation d'une légère différence de nombre d'entrées (moins quatre) attribuée aux métadonnées, avec vérification dans le Table Editor de Supabase confirmant le résultat attendu.
- Vérification du contenu complet du livre vectorisé avec des métadonnées simplifiées, et visualisation des embeddings sous forme de vecteurs dans la base de données Supabase.
- Test final réussi du RAG via Supabase : requête sur le concept de jugement et accountability, retournant les quatre meilleurs résultats du VectorStore, validant le pipeline complet.

## Concepts cles
- introduction au RAG avancé via Supabase avec organisation méthodique des workflows
- anecdote sur l'origine de Supabase (concurrent de Firebase de Google)
- exemple de structure de données typée dans Supabase (identifiant, string, boolean)
- avantages de Supabase : authentification facilitée intégrée sur base Postgres
- présentation de la Realtime Database de Supabase pour applications temps réel
- mise en garde sur la limite de performance liée au volume de données
- anecdote sur la découverte d'Airtable et son innovation en typage de données
- présentation des types de colonnes riches Airtable et formules type Vlookup
- limite de scalabilité d'Airtable (100 000 enregistrements max par base)
- philosophie open source de Supabase permettant le self-hosting (exemple Railway)
- démonstration de création d'un nouveau projet Supabase (région Europe)
- démonstration de création de colonnes Supabase (moins intuitif qu'Airtable)
- présentation des templates de démarrage Supabase (choix du template Langchain)
- débogage en direct d'une erreur de syntaxe SQL liée à la dimension d'embedding
- confirmation de la création réussie de la table documents
- explication de la structure de table documents (content, metadata, embedding)
- démonstration de connexion embedding Mistral et ajout du Supabase VectorStore
- nettoyage des données superflues via le module Extract From File
- contrainte technique : basculer vers OpenAI pour contrôler les dimensions d'embedding
- observation et vérification du résultat dans le Table Editor Supabase
- vérification du contenu vectorisé et visualisation des embeddings dans Supabase
- test final réussi du RAG Supabase validant le pipeline complet

## Outils mentionnes
- n8n
- Supabase
- Firebase
- Google
- Postgres
- Airtable
- Railway
- Langchain
- Mistral
- OpenAI

## Tips techniques
- Dupliquer et renommer clairement ses workflows (simple vs avancé) pour garder une trace organisée de la progression de complexité
- Utiliser le module Extract From File pour nettoyer et extraire uniquement les éléments utiles d'un fichier avant vectorisation
- Basculer vers OpenAI si le contrôle précis des dimensions d'embedding est nécessaire, Mistral ne permettant pas cette configuration

## Cas d'usage reels
- [[]]
