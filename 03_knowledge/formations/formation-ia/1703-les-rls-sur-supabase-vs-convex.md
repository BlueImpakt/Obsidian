---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.03 Les RLS sur Supabase vs Convex.txt"
---

# 17.03 Les RLS sur Supabase vs Convex

## Resume
- Sommaire du module RLS sur Supabase vs Convex : introduction, comprendre les RLS, le concept de RLS, définir une policy, pièges à éviter, utiliser les Edge Functions, Supabase vs Convex, conclusion.
- Introduction à l'explication des RLS (Row Level Security) sur Supabase, pourquoi cet outil peut être plus risqué qu'un backend comme Convex, et comment sécuriser totalement son usage.
- Nuance importante : les RLS ne sont pas difficiles à configurer, surtout à l'ère de l'IA et de Claude Code, mais Supabase peut présenter des failles de sécurité par défaut si les Row Level Security ne sont pas correctement configurées.
- Explication de la définition d'une policy RLS : nom, table concernée, et type d'interaction visé (ex : SELECT), la structure de base pour sécuriser l'accès aux données.
- Distinction entre l'interaction utilisateur directe avec la base de données (RLS) et les Edge Functions, qui s'exécutent côté serveur et sont donc structurellement plus sécurisées.
- Règle stricte de vérification systématique des RLS à chaque déploiement en production, pour éviter tout risque de fuite de données (data leak), une pratique critique de sécurité.
- Alternative recommandée pour ceux ne voulant pas se soucier des RLS : Convex, avec zéro accès direct à la base de données ; précision sur l'ancien vendor locking de Convex désormais résolu grâce à son passage en open source.

## Concepts cles
- plan de présentation du module RLS Supabase vs Convex
- introduction aux RLS Supabase et risques comparés à Convex
- nuance : RLS pas difficiles avec l'IA, mais failles de sécurité par défaut sur Supabase
- structure de définition d'une policy RLS (nom, table, type d'interaction)
- distinction entre interaction directe utilisateur (RLS) et Edge Functions côté serveur
- règle stricte : vérifier systématiquement les RLS à chaque déploiement en production
- alternative Convex sans accès direct à la DB, résolution du vendor locking (open source)

## Outils mentionnes
- Supabase
- Convex
- Claude Code

## Tips techniques
- Toujours configurer explicitement les Row Level Security sur Supabase, faute de quoi l'application reste vulnérable par défaut
- Vérifier systématiquement les Row Level Security à chaque déploiement en production, sans exception, pour prévenir tout risque de fuite de données

## Cas d'usage reels
- [[]]
