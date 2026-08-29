---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.13 Prompt Engineering, Presets, Bug Fix.txt"
---

# 17.13 Prompt Engineering, Presets, Bug Fix

## Resume
- Sommaire du module prompt engineering, presets et bug fix : introduction et workflow, importance des branches, liste des correctifs, gestion des erreurs, optimisations UI, fonctionnalités avancées, lancement des tâches.
- Règle absolue de workflow Git : ne jamais travailler directement sur la branche master (version en production), toujours créer une nouvelle branche même pour des corrections mineures.
- Lancement autonome de l'IA sur la liste complète des défauts identifiés, avec méthode de validation systématique après exécution avant de passer à l'étape suivante (prompt engineering).
- Introduction de la fonctionnalité de presets personnalisables : ajout de la possibilité pour les utilisateurs (et l'admin) de créer leurs propres presets, testée d'abord en tant qu'administrateur.
- Démonstration de la simplicité d'un prompt de correction fonctionnelle (ajout de la réinitialisation de mot de passe manquante), illustrant l'accessibilité de ce type de correction même sans expertise technique.
- Instruction de développement d'une nouvelle fonctionnalité majeure : permettre aux utilisateurs de créer leurs propres presets personnalisés, avec explication à venir sur le logo affiché.
- Instruction d'implémentation structurée et sécurisée de la fonctionnalité, avec demande explicite d'utiliser des skills de vérification de sécurité côté base de données.
- Détection d'un bug de logique métier : un preset non activé par l'utilisateur (cinématographique) apparaît quand même dans les générations, révélant un défaut de filtrage à corriger.
- Réflexion business sur la protection de la propriété intellectuelle du style visuel : justifier l'abonnement en évitant que les utilisateurs puissent simplement extraire le prompt et le réutiliser gratuitement ailleurs (NanoBanana).
- Brainstorming demandé à l'IA sur la mise en place d'un système Bring Your Own Key permettant à certains utilisateurs d'utiliser leurs propres clés API, une réflexion produit avancée.
- Technique d'exploration en parallèle : lancer l'IA sur plusieurs directions différentes simultanément pour gagner du temps, en acceptant que certaines pistes puissent être abandonnées en cours de route.
- Démonstration du preset personnel de l'auteur (« preset Théo ») basé sur la color science Fujifilm, reconnue pour son rendu cinématographique caractéristique, chargé depuis l'admin.
- Validation finale enthousiaste du résultat qualifié de masterclass, avec instruction de commit, push et déploiement de la version preview sur Vercel avant fusion avec la branche principale.
- Rappel de la bonne pratique SaaS : passer en revue systématiquement tous les cas utilisateur avant de merger avec la branche principale et de pousser une nouvelle version (0.02) en production.

## Concepts cles
- plan de présentation du module prompt engineering, presets et bug fix
- règle absolue : ne jamais travailler directement sur master, toujours créer une branche
- lancement autonome de l'IA sur une liste de défauts avec validation post-exécution
- introduction de la fonctionnalité de presets personnalisables (test admin d'abord)
- démonstration de la simplicité d'un prompt de correction fonctionnelle (reset password)
- instruction de développement de la fonctionnalité de presets utilisateurs personnalisés
- instruction d'implémentation structurée avec vérification de sécurité via skills
- détection d'un bug de logique métier : preset non activé apparaissant quand même
- réflexion business sur la protection de la propriété intellectuelle du style visuel (prompt)
- brainstorming sur système Bring Your Own Key pour clés API personnalisées
- technique d'exploration parallèle de plusieurs directions simultanées
- démonstration du preset personnel basé sur la color science Fujifilm
- validation finale et déploiement de version preview Vercel avant fusion
- bonne pratique SaaS : revue systématique des cas utilisateur avant merge en production

## Outils mentionnes
- Git
- Vercel

## Tips techniques
- Ne jamais travailler directement sur la branche master en production, toujours créer une nouvelle branche, même pour des corrections mineures
- Laisser l'IA travailler en autonomie sur une liste complète de corrections, puis valider systématiquement chaque point avant de passer à l'étape suivante
- Tester une nouvelle fonctionnalité côté admin avant de la déployer pour les utilisateurs finaux
- Demander explicitement à l'IA d'utiliser des skills de vérification de sécurité lors de l'implémentation de fonctionnalités touchant à la base de données
- Protéger la valeur ajoutée d'un abonnement en empêchant l'extraction facile des prompts propriétaires, pour éviter le contournement gratuit du service
- Explorer plusieurs directions simultanément avec l'IA pour gagner du temps, en acceptant que certaines pistes soient finalement abandonnées
- Toujours déployer une version preview avant de fusionner avec la branche principale, pour valider visuellement le résultat en conditions réelles
- Toujours passer en revue systématiquement tous les cas utilisateur possibles avant de merger et déployer une nouvelle version en production

## Cas d'usage reels
- [[]]
