---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.02 Choisir sa base de données  back-end.txt"
---

# 17.02 Choisir sa base de données / back-end

## Resume
- Sommaire du module choisir sa base de données/back-end : introduction, fonctionnement de Supabase, limitations de Supabase, découverte de Convex, avantages du realtime natif.
- Introduction à la comparaison Supabase vs Convex : explication du choix évolutif de l'auteur de Supabase vers Convex, avec présentation de Supabase comme base de données Postgres standard.
- Présentation de l'opposition SQL vs NoSQL : Firebase illustrant les bases NoSQL sans structure fixe de lignes/colonnes, organisées plutôt en documents indépendants.
- Présentation des solutions de stockage de fichiers comme AWS S3 ou Cloudflare, permettant de stocker et charger des documents depuis une base de données, distinctes des Edge Functions déclenchées à la demande.
- Synthèse des cinq forces de Supabase (retour instantané temps réel), avec ajout de la base de données vectorisée (Vector Database) et des Cronjobs pour déclencher des actions programmées.
- Présentation de Convex comme base de données nativement temps réel par définition, un positionnement différenciant clairement affiché par l'entreprise elle-même dans sa comparaison avec Supabase.
- Explication de la différence d'approche du temps réel : Supabase déclenche le realtime à la demande selon le besoin, tandis que Convex l'intègre par défaut dans toute l'application dès sa conception.
- Honnêteté sur le choix personnel de l'auteur : bien que tous ses projets restent sur Supabase par habitude, il recommande Convex pour quiconque partirait de zéro aujourd'hui.
- Précision technique sur l'appariement de Convex avec TypeScript pour l'inférence de schéma, avec nuance que Supabase reste pertinent pour les usages nécessitant beaucoup de SQL.
- Présentation de l'écosystème d'intégrations autour de Convex (notifications Expo pour app mobile, Brevo, Polar), une architecture pensée selon la trajectoire technique adoptée.

## Concepts cles
- plan de présentation du module de choix de base de données/back-end
- introduction à la comparaison Supabase vs Convex (évolution de l'auteur)
- opposition SQL vs NoSQL (Firebase comme exemple NoSQL)
- solutions de stockage de fichiers (AWS S3, Cloudflare) et introduction des Edge Functions
- synthèse des cinq forces de Supabase (dont Vector Database et Cronjobs)
- présentation de Convex comme base de données nativement temps réel
- différence d'approche du temps réel : Supabase à la demande vs Convex par défaut
- honnêteté : usage personnel de Supabase par habitude, mais recommandation de Convex pour repartir de zéro
- appariement de Convex avec TypeScript et pertinence de Supabase pour usage SQL intensif
- écosystème d'intégrations Convex (Expo, Brevo, Polar)

## Outils mentionnes
- Supabase
- Convex
- Postgres
- Firebase
- AWS
- Cloudflare
- TypeScript
- SQL
- Expo
- Brevo
- Polar

## Tips techniques
-

## Cas d'usage reels
- [[]]
