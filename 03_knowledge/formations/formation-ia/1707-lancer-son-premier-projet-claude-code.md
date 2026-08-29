---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.07 Lancer son premier projet Claude Code.txt"
---

# 17.07 Lancer son premier projet Claude Code

## Resume
- Sommaire du module lancer son premier projet Claude Code : introduction, terminal environments, Claude vs GPT, interface Codex, utiliser Conductor, project boilerplate setup.
- Introduction pratique au lancement du premier projet réel, avec première décision importante à prendre : choisir l'écosystème de build parmi plusieurs options disponibles.
- Comparaison Claude vs GPT pour le développement : GPT jugé plus autonome sur certaines tâches précises quand l'objectif est clair, avec mention de l'excellence de l'application Codex native.
- Nuance sur les forces respectives : Codex excelle comme exécutant précis sans fioritures, tandis que Claude est meilleur pour définir la direction globale et la réflexion stratégique d'un projet.
- Présentation de Conductor, outil gratuit de personnalisation permettant de configurer les modèles utilisés (par défaut Opus 4.7) et d'ajuster le niveau d'effort du modèle.
- Analyse stratégique des investissements massifs des acteurs IA pour attirer les utilisateurs dans leur écosystème fermé, limitant l'interopérabilité avec des outils tiers ; présentation des options de personnalisation d'apparence.
- Démonstration de création automatique d'un repository GitHub depuis Conductor, avec présentation de l'interface (projets à gauche avec leurs branches, terminal à droite).
- Démonstration de l'ajout automatique de skills par défaut dans le projet (exemple : Email Best Practices lié à Resend), consultables dans l'onglet Cloud Skills.
- Présentation des deux fichiers de référence du projet : CLAUDE.md expliquant la marche à suivre, et le README expliquant l'objectif (visible aussi sur GitHub), avant de lancer une session de brainstorming.
- Mention de l'outil Aqua Voice utilisé pour la dictée vocale, ainsi que la génération d'images via un outil dénommé « TIO Cloud », des outils complémentaires pour accélérer le workflow créatif.
- Poursuite de la description ajoutée au projet, avec annonce de la conception hors caméra de l'interface, une étape volontairement effectuée en réel pour créer le réflexe chez les apprenants.
- Suite de la définition du produit en brainstorming : spécification des formats de miniature (16:9 pour YouTube, 9:16 pour les shorts), confirmation de l'absence de version gratuite, et choix du style de reformulation par prompt système.
- Présentation de la stack technique choisie pour le projet (nom de code « TomMaker ») : TanStack Start avec Vite et React 19, Convex pour la base de données, BetterAuth, Polar pour paiements, Resend pour emails, ShadCN et Tailwind pour le design.
- Correction en direct du plan initial : rejet des modèles proposés (OpenAI GPT Image, Gemini 2.5 Flash Image) jugés pas assez récents, avec formulation d'un feedback direct à l'IA pour ajuster le choix des modèles.
- Correction technique précise sur le format d'image généré (1536x1024 incorrect pour du 16:9), avec demande explicite de correction du ratio et des paramètres qualité par défaut sur « high ».
- Démonstration de connexion à Convex depuis le terminal : ouverture de l'URL d'authentification, création de compte ou connexion, nommage de l'appareil, confirmation via navigateur.
- Recommandation de sécurité sur la gestion des variables d'environnement : toujours vérifier et remplacer les clés API sensibles (ex : SK ANT) plutôt que de les envoyer telles quelles sans vérification.
- Démonstration de création d'une clé API sur une plateforme IA (Get API Key), avec nommage explicite de la clé (ex : « SumMaker ») et possibilité de créer des workspaces séparés.
- Suite de la configuration des clés API : ajout de la clé, précision qu'il s'agit d'un test non fonctionnel, puis récupération d'une clé API complémentaire depuis Google AI Studio.
- Démonstration rapide de création d'une clé secrète supplémentaire (nommée « SumMaker »), poursuivant la configuration multi-provider du projet.
- Confirmation de l'envoi réussi des variables d'environnement (OpenAI Key, Google API Key, Anthropic API Key, admin email) vers le projet, avant lancement effectif de l'application via la commande de développement.
- Démonstration de déploiement des fonctions pour tester l'application en local (localhost), avec gestion automatique du remplacement d'un ancien serveur de développement encore actif.
- Démonstration de création de compte de test dans l'application (email et mot de passe), avec mention que l'intégration Google Auth sera traitée dans une vidéo séparée ; premier constat du design encore imparfait à ce stade.

## Concepts cles
- plan de présentation du module de lancement d'un premier projet Claude Code
- introduction pratique au lancement du premier projet : choix de l'écosystème de build
- comparaison Claude vs GPT : autonomie de GPT sur tâches précises
- nuance : Codex exécutant précis vs Claude meilleur en direction stratégique
- présentation de Conductor (outil gratuit de configuration de modèles)
- analyse des investissements pour attirer vers un écosystème fermé, personnalisation d'apparence
- démonstration de création automatique de repository GitHub via Conductor
- démonstration d'ajout de skills par défaut (Email Best Practices, Resend)
- présentation des fichiers CLAUDE.md et README comme documents de référence
- mention des outils Aqua Voice (dictée) et TIO Cloud (génération d'images)
- annonce de la conception de l'interface hors caméra pour créer un réflexe pratique
- spécification produit : formats de miniature (16:9/9:16), absence de version gratuite
- stack technique complète du projet (TanStack, Convex, BetterAuth, Polar, Resend, ShadCN)
- correction en direct des modèles proposés (jugés pas assez récents)
- correction technique précise du ratio d'image (16:9) et paramètres qualité
- démonstration de connexion à Convex via terminal et navigateur
- recommandation de sécurité sur la vérification des variables d'environnement (clés API)
- démonstration de création de clé API nommée avec workspaces séparés
- suite de configuration des clés API et récupération de clé Google AI Studio
- démonstration de création d'une clé secrète supplémentaire nommée
- confirmation d'envoi des variables d'environnement multi-provider et lancement de l'app
- démonstration de déploiement local et remplacement automatique d'un ancien serveur
- démonstration de création de compte de test et constat du design imparfait initial

## Outils mentionnes
- Claude Code
- Codex
- Conductor
- Claude
- GPT
- Opus
- GitHub
- Resend
- Aqua Voice
- TanStack
- Vite
- React
- Convex
- BetterAuth
- Polar
- ShadCN
- Tailwind CSS
- OpenAI
- Gemini
- Google AI Studio
- Google
- Anthropic

## Tips techniques
- Formuler un feedback direct et précis à l'IA quand les modèles proposés par défaut ne correspondent pas aux attentes de fraîcheur/qualité
- Vérifier précisément les dimensions générées par l'IA (ratio d'image) et corriger explicitement si elles ne correspondent pas au format attendu
- Toujours vérifier et remplacer manuellement les clés API sensibles dans les variables d'environnement, ne jamais les envoyer sans contrôle

## Cas d'usage reels
- [[]]
