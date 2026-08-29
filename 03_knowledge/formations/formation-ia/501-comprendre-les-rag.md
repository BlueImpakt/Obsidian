---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.01 Comprendre les RAG.txt"
---

# 5.01 Comprendre les RAG

## Resume
- Introduction détaillée au concept de RAG (Retrieval Augmented Generation), un concept majeur de l'automatisation IA permettant de créer des bases de connaissances pour enrichir les capacités de l'IA.
- Explication du problème d'obsolescence des connaissances des LLM : entraînés sur des données antérieures à une date donnée, ils restent limités sans recherche internet activée, un problème résolu par les RAG.
- Explication de la limite des LLM sans RAG : capacité à généraliser mais risque de réponses floues ou fausses en l'absence de suffisamment de matière, et absence d'accès natif aux documents personnels de l'utilisateur.
- Explication du fait que les LLM sont entraînés sur des données disponibles publiquement sur internet, ce qui explique la reproduction de styles issus d'œuvres protégées par le droit d'auteur dans certains générateurs d'images.
- Décomposition de l'acronyme RAG (Retrieval Augmented Generation) : retrouver l'information pertinente, l'enrichir, puis générer la réponse finale, un processus en trois temps.
- Métaphore de la grande pièce contenant tous les mots (espace vectoriel) : dès qu'une question est posée, un embedding est créé pour identifier les éléments les plus pertinents dans cet espace.
- Explication du processus d'enrichissement contextuel : le système regarde le contexte environnant (phrases avant/après) pour enrichir la réponse avant sa génération finale.
- Présentation de la diversité des sources documentaires exploitables par un RAG : PDF, pages web, drives, audios/vidéos transcrits en texte, images décrites, couvrant quasiment tout type de contenu.
- Illustration du mécanisme de sélection des éléments pertinents pour construire une réponse RAG : identifier plusieurs candidats proches, les combiner pour enrichir puis générer la réponse finale.
- Explication de la proximité spatiale des vecteurs sémantiquement liés dans l'espace vectoriel : chaque bout de texte est représenté sous forme de séquence de nombres selon son sens.
- Explication du processus de tokenisation transformant un texte (« le chat dort sur le canapé ») en coordonnées vectorielles capturant son aspect sémantique.
- Explication de la recherche par plus proches voisins (nearest neighbors) : calcul de distance entre le vecteur de la requête et tous les vecteurs existants pour retourner les 5 résultats les plus proches.
- Justification pédagogique de l'approfondissement technique avant la pratique, avec mention du modèle d'embedding le plus commun disponible au moment de l'enregistrement.
- Présentation de la technique de reranking : récupérer 10 candidats au lieu de 3, puis recalculer leur pertinence pour ne retenir finalement que les 3 plus pertinents, améliorant la qualité de réponse.
- Présentation de l'usage des métadonnées pour enrichir le contexte : possibilité d'ajouter des métadonnées comme un numéro de chapitre lors de la vectorisation d'éléments d'un livre dans N8n.
- Description du workflow RAG complet : déclenchement via webhook/chat, vectorisation de la question, recherche vectorielle (Pinecone ou Supabase) pour obtenir les 5 meilleurs résultats.
- Justification du découpage en petits morceaux de texte pour faciliter le processus d'embedding, chaque morceau étant placé avec des coordonnées précises dans l'espace vectoriel.
- Description visuelle du processus complet : la question vectorisée arrive dans l'espace vectoriel, identifie les points les plus proches dans la base de données, puis les fait travailler ensemble pour la réponse.
- Transition vers la pratique avec NotebookLM, outil créé par Google permettant de construire des RAG simplement, équivalent accessible du RAG que l'on construit dans N8n.
- Démonstration d'upload d'une source dans NotebookLM (le livre L'Almanach de Naval Ravikant), avec possibilité d'ajouter d'autres sources complémentaires comme des vidéos YouTube.
- Démonstration de sélection des sources à inclure dans la réponse et test d'interaction conversationnelle directe avec le contenu (« les pensées du cerveau de Naval ») via NotebookLM.
- Test pratique de traduction en français d'un extrait de citation de Naval Ravikant sur l'importance de savoir vendre ET construire, avec traçabilité de la source citée.
- Observation de la traçabilité forte de NotebookLM : le système montre clairement quelle source (PDF vs podcast Joe Rogan) a été utilisée pour construire chaque partie de la réponse.
- Exemple d'extraction précise depuis une source spécifique (transcript du podcast Joe Rogan Experience filtré), illustrant la granularité de traçabilité offerte par l'outil.
- Confirmation de la flexibilité des sources ajoutables à NotebookLM (MP3, Google Docs, Google Slides), permettant de construire facilement une base de connaissances sans s'en rendre compte.
- Introduction des limites de NotebookLM justifiant le passage à l'automatisation via API : besoin d'ajouter des sources en continu automatiquement plutôt que manuellement à chaque fois.
- Confirmation de la création réussie d'un Vector Store personnalisé (« Naval's mind ») en uploadant des fichiers, un processus qui sera reproduit de manière programmatique avec N8n.
- Démonstration de connexion d'un assistant OpenAI configuré avec des fichiers uploadés, accessible également via l'API pour des interactions programmatiques automatisées.
- Observation en direct sur le support multilingue récent de la fonctionnalité présentée, initialement limitée à l'anglais mais désormais étendue à d'autres langues.

## Concepts cles
- introduction détaillée au concept de RAG pour enrichir les capacités de l'IA
- problème d'obsolescence des connaissances des LLM résolu par les RAG
- limite des LLM sans RAG (réponses floues/fausses, pas d'accès aux documents personnels)
- explication de la reproduction de styles d'œuvres protégées par les LLM entraînés sur internet
- décomposition de l'acronyme RAG (retrouver, enrichir, générer)
- métaphore de l'espace vectoriel comme grande pièce contenant tous les mots
- processus d'enrichissement contextuel via le contexte environnant du texte trouvé
- diversité des sources documentaires exploitables par un RAG (PDF, audio, vidéo, image)
- illustration du mécanisme de sélection des éléments pertinents pour la réponse RAG
- proximité spatiale des vecteurs sémantiquement liés dans l'espace vectoriel
- explication du processus de tokenisation transformant du texte en coordonnées vectorielles
- explication de la recherche par plus proches voisins (nearest neighbors)
- justification pédagogique de l'approfondissement technique, mention du modèle d'embedding commun
- technique de reranking (10 candidats recalculés vers 3 retenus)
- usage des métadonnées pour enrichir le contexte (exemple chapitre de livre)
- description du workflow RAG complet (déclenchement, vectorisation, recherche via Pinecone/Supabase)
- justification du découpage en petits morceaux pour faciliter l'embedding
- description visuelle complète du processus de recherche vectorielle et génération
- transition pratique vers NotebookLM (équivalent accessible du RAG N8n)
- démonstration d'upload de source dans NotebookLM (livre Naval Ravikant)
- démonstration d'interaction conversationnelle avec les sources via NotebookLM
- test pratique de traduction avec traçabilité de la source citée
- observation de la traçabilité forte des sources utilisées par NotebookLM
- exemple d'extraction précise et traçable depuis une source spécifique (podcast)
- flexibilité des sources ajoutables à NotebookLM (MP3, Google Docs/Slides)
- limites de NotebookLM justifiant l'automatisation via API pour l'ajout continu de sources
- confirmation de création d'un Vector Store personnalisé via upload de fichiers
- démonstration de connexion d'un assistant OpenAI accessible via API
- observation du support multilingue récent d'une fonctionnalité

## Outils mentionnes
- n8n
- Pinecone
- Supabase
- NotebookLM
- Google
- YouTube
- Google Docs
- Google Slides
- OpenAI

## Tips techniques
- Utiliser une technique de reranking : récupérer un nombre plus large de candidats puis recalculer leur pertinence pour ne garder que les meilleurs
- Ajouter des métadonnées contextuelles (chapitre, source, date) lors de la vectorisation pour enrichir la pertinence des résultats de recherche RAG
- Passer à une automatisation via API dès que le besoin d'enrichissement continu de sources dépasse l'usage manuel ponctuel de NotebookLM

## Cas d'usage reels
- [[]]
