---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.06 Configurer Postgres en tant que memoire.txt"
---

# 5.06 Configurer Postgres en tant que memoire

## Resume
- Introduction au module d'ajout de mémoire Postgres à un agent IA, en remplacement de la mémoire simple native de N8n qui pose problème dès qu'il faut stocker beaucoup de données.
- Présentation de PostgreSQL comme standard ultime des bases de données relationnelles, technologie open source existant depuis plus de 30 ans, sur laquelle Supabase s'appuie.
- Explication de la structuration relationnelle des données en SQL, avec distinction par rapport aux bases de données NoSQL, un format moins traditionnel mais également répandu.
- Explication du positionnement de Supabase : reprendre le cœur de PostgreSQL et y ajouter des surcouches facilitant l'intégration pour les développeurs.
- Démonstration de sélection du nœud Postgres Chat Memory dans N8n, avec nécessité de configurer les credentials de connexion à la base de données Postgres au préalable.
- Recommandation de nommage clair des credentials Supabase (nom du projet), avec récupération des détails de connexion directement depuis l'interface Supabase (composant Connect).
- Détail des composants de connexion à récupérer : Port, Database (type de base), et nom d'utilisateur, tous nécessaires pour configurer la connexion Postgres dans N8n.
- Démonstration de récupération du nom d'utilisateur (format postgres.xxx) et du mot de passe du projet Supabase pour compléter la configuration des credentials.
- Démonstration de recréation d'un projet Supabase de test (template Postgres) avec choix de région (France) et mot de passe à conserver précieusement pour la suite.
- Explication de la nécessité de laisser le champ table name par défaut (sans pré-créer la table) pour permettre à N8n de créer automatiquement la structure adaptée.
- Test pratique confirmant la création de la table N8N Chat Histories dans Supabase après un premier message, avec un session ID identifiant unique de chaque conversation.
- Explication du mécanisme de récupération de mémoire basé sur le dernier message de chat et l'identifiant de session en cours, chaque nouvelle session ouvrant un nouvel enregistrement.

## Concepts cles
- introduction à la mémoire Postgres en remplacement de la mémoire simple limitée de N8n
- présentation de PostgreSQL comme standard ultime des bases relationnelles (30 ans, open source)
- distinction entre bases de données SQL relationnelles et NoSQL
- positionnement de Supabase comme surcouche facilitatrice sur PostgreSQL
- démonstration de sélection et configuration initiale du nœud Postgres Chat Memory
- recommandation de nommage clair des credentials et récupération via composant Connect
- détail des composants de connexion Postgres à récupérer (port, database, utilisateur)
- démonstration de récupération du nom d'utilisateur et mot de passe Supabase
- démonstration de création de projet Supabase avec choix de région
- nécessité de laisser le nom de table par défaut pour création automatique par N8n
- test pratique confirmant la création de table avec session ID unique par conversation
- explication du mécanisme de récupération de mémoire par session ID

## Outils mentionnes
- n8n
- Postgres
- Supabase

## Tips techniques
- Nommer clairement les credentials Supabase avec le nom du projet associé, pour faciliter l'identification lors de la gestion de plusieurs connexions
- Conserver précieusement le mot de passe de base de données Supabase généré à la création, il est essentiel pour la connexion ultérieure
- Laisser le champ de nom de table par défaut sans le pré-créer manuellement, N8n se charge de créer automatiquement la structure adaptée

## Cas d'usage reels
- [[]]
