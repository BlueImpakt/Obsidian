---
tags: [formation, millenium]
module: Formation IA
section: "Comprendre l'Automatisation"
source_transcript: "1 Introduction.txt"
---

# 1 Introduction

## Resume
- Introduction au concept de RAG (Retrieval Augmented Generation), présenté comme un concept majeur de l'automatisation IA permettant de créer des bases de connaissances pour enrichir les capacités des LLM au-delà de leur entraînement initial.
- Explication du problème fondamental résolu par le RAG : les LLM sont entraînés sur des données figées à une date donnée et restent obsolètes sans recherche internet active, ne pouvant répondre à des questions sur des événements postérieurs à leur entraînement.
- Précision sur les limites des LLM : bien que capables de traiter l'information de manière générale, ils peuvent donner des résultats flous ou faux en l'absence de matière suffisante, et n'ont naturellement pas accès aux documents personnels de l'utilisateur.
- Rappel que les LLM ont été entraînés uniquement sur des données publiquement disponibles sur Internet, ce qui explique pourquoi certains générateurs d'images reproduisent des styles issus d'œuvres protégées par le droit d'auteur.
- Explication du fonctionnement du RAG via son acronyme : retrouver (Retrieval), enrichir (Augmented), générer (Generation) l'information. Lors d'une requête, le système va d'abord aller chercher des informations pertinentes avant de générer la réponse finale.
- Analogie de la grande pièce contenant tous les mots (espace vectoriel) : lors d'une question, le système crée un embedding pour localiser dans cet espace les éléments les plus pertinents par rapport à la requête posée.
- Détail du processus d'enrichissement contextuel : le système analyse les phrases avant et après l'élément pertinent trouvé pour enrichir la réponse avant de générer le résultat final, avec l'annonce d'une future cartographie visuelle du processus.
- Présentation des types de documents source utilisables pour un RAG : PDF, pages web, drives, audios transcrits, vidéos transcrites, et même des images une fois décrites textuellement, illustrant la grande diversité de formats compatibles.
- Illustration du processus de sélection des éléments pertinents dans l'espace vectoriel pour construire le début de la réponse, l'enrichir, puis générer la réponse finale, résumant le fonctionnement global du RAG.
- Explication de la proximité spatiale des éléments sémantiquement liés dans l'espace vectoriel : chaque bout de texte est représenté sous forme de séquence de nombres, permettant de visualiser des concepts proches comme physiquement proches dans cet espace.
- Démonstration concrète de tokenisation et vectorisation d'une phrase (« le chat dort sur le canapé ») : chaque mot obtient des coordonnées vectorielles numériques positionnées dans l'espace sémantique selon leur sens.
- Explication du calcul de recherche vectorielle : une requête est transformée en vecteur, puis on calcule la distance avec tous les vecteurs existants pour identifier les voisins les plus proches, généralement les cinq résultats les plus pertinents retournés.
- L'auteur assume la technicité de l'explication car il souhaite poser des fondements solides avant la pratique. Introduction des modèles d'embedding disponibles, en notant que le paysage évolue vite et que ce qu'il présente sera probablement déjà dépassé au moment du visionnage.
- Présentation d'une technique d'optimisation : plutôt que de récupérer directement les 3 résultats les plus proches, le système en récupère 10 puis effectue un recalcul de pertinence pour ne retenir que les 3 les plus pertinents au final, améliorant ainsi la qualité de la réponse.
- Présentation de l'usage des métadonnées pour enrichir le contexte : sur N8n, on peut associer des métadonnées (comme un numéro de chapitre pour un livre vectorisé) à chaque fragment, apportant un contexte supplémentaire utile lors de la recherche.
- Description du déclenchement pratique d'un RAG : une question arrive via un Webhook ou un chat, elle est vectorisée, puis une recherche vectorielle avec des outils comme Pinecone ou Supabase récupère les cinq meilleurs résultats correspondants.
- Explication du chunking (découpage en petits morceaux de texte) comme facilitateur du processus d'embedding : chaque fragment obtient des coordonnées précises qui déterminent sa position dans la zone vectorielle, non attribuée au hasard.
- Illustration concrète du processus complet : la question vectorisée est comparée aux vecteurs existants dans la base de données pour retrouver les points les plus proches, dont les données sont ensuite combinées pour construire la réponse finale.
- Transition vers la pratique avec Notebook LM, outil créé par Google permettant de construire simplement un RAG, équivalent à ce qu'on pourrait construire manuellement dans N8N mais accessible directement via l'interface Google.
- Démonstration d'upload de source dans Notebook LM : import d'un livre au format PDF (l'Almanach de Naval Ravikant) et possibilité d'ajouter d'autres types de sources comme des vidéos YouTube.
- Présentation de la sélection des sources actives dans la réponse générée, permettant d'interagir directement avec le contenu importé (exemple : dialoguer avec les idées de Naval Ravikant à partir de tout ce qu'il a écrit).
- Citation illustrative de Naval Ravikant (« If you can do both, you will be unstoppable ») liant apprentissage de la vente et de la construction, avec démonstration de la fonction de traduction en français directement dans l'outil.
- L'auteur souligne la puissance de l'interaction directe avec un PDF spécifique (contrairement au podcast Joe Rogan moins sollicité ici), illustrant comment construire la compétence combinée d'apprendre à bâtir et à vendre à partir des sources intégrées.
- Exemple concret d'extraction ciblée : recherche d'un passage sur la richesse et le bonheur, le système allant chercher spécifiquement dans le transcript du Joe Rogan Experience filtré par cette source précise.
- Confirmation de la flexibilité des sources acceptées par Notebook LM : fichiers MP3, Google Docs, Google Slides et bien d'autres, permettant de construire une base de connaissances complète. L'auteur souligne qu'on vient, sans s'en rendre compte, de créer un RAG fonctionnel.
- Introduction de la limite principale de cette approche manuelle : le besoin d'automatiser l'ajout et l'enrichissement continu des sources via des API, plutôt que d'être constamment devant Notebook LM pour ajouter du contenu manuellement.
- Transition vers la construction programmatique d'un RAG équivalent via N8n : l'auteur présente son propre Vector Store personnel (« Naval's mind ») créé en uploadant des fichiers, un processus qu'il va reproduire de manière automatisée.
- Explication du processus d'upload de fichiers liés à un assistant ou agent IA pour obtenir des réponses pertinentes, avec exemple de question posée sur la vraie richesse selon Naval, l'assistant étant également accessible via API.
- Note sur la disponibilité linguistique de l'outil : initialement limité à l'anglais, l'auteur signale une nouveauté récente permettant potentiellement d'autres langues, invitant à vérifier soi-même cette évolution au moment du visionnage.

## Concepts cles
- introduction au RAG (Retrieval Augmented Generation)
- obsolescence des connaissances figées des LLM sans recherche active
- limites de généralisation sans données suffisantes
- absence d'accès natif aux documents personnels
- entraînement limité aux données publiques disponibles
- reproduction de styles issus d'œuvres protégées
- fonctionnement du RAG selon son acronyme (retrouver/enrichir/générer)
- analogie de la grande pièce pour l'espace vectoriel
- création d'un embedding lors d'une requête
- enrichissement contextuel via phrases adjacentes
- diversité des formats source compatibles avec un RAG (PDF, audio, vidéo, image décrite)
- synthèse du processus complet de sélection et génération RAG
- représentation spatiale de la proximité sémantique dans l'espace vectoriel
- tokenisation et vectorisation d'une phrase exemple
- calcul de distance vectorielle pour trouver les voisins les plus proches
- retour des 5 résultats les plus proches
- évolution rapide des modèles d'embedding disponibles
- technique de récupération élargie puis reranking (10 → 3 résultats)
- métadonnées enrichissant le contexte (exemple : chapitre de livre)
- déclenchement d'un RAG via Webhook/chat
- outils de recherche vectorielle (Pinecone, Supabase)
- chunking comme facilitateur de l'embedding
- positionnement non aléatoire dans l'espace vectoriel
- synthèse visuelle du processus de recherche vectorielle
- Notebook LM comme équivalent simplifié d'un RAG construit sur N8N
- upload de source PDF et vidéo YouTube dans Notebook LM
- sélection des sources actives pour la génération de réponse
- citation de Naval sur vendre et construire
- fonction de traduction intégrée
- interaction sélective privilégiant une source sur une autre (PDF vs podcast)
- extraction ciblée filtrée par source spécifique (Joe Rogan Experience)
- diversité maximale des sources (MP3, Google Docs, Slides)
- création implicite d'un RAG via Notebook LM
- limite du RAG manuel : nécessité d'automatisation via API
- Vector Store personnel comme équivalent programmatique de Notebook LM
- liaison de fichiers à un assistant/agent IA accessible via API
- évolution de la disponibilité multilingue de l'outil

## Outils mentionnes
- n8n
- Pinecone
- Supabase
- Notebook LM
- Google
- Google Docs
- Google Slides

## Tips techniques
- Récupérer un nombre plus large de résultats puis les reclasser par pertinence, plutôt que de se limiter directement au top 3
- Ajouter des métadonnées (chapitre, section, date) à chaque fragment vectorisé pour enrichir le contexte de recherche

## Cas d'usage reels
- [[]]
