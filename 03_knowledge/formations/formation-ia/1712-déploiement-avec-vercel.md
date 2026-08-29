---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.12 Déploiement avec Vercel.txt"
---

# 17.12 Déploiement avec Vercel

## Resume
- Sommaire du module déploiement avec Vercel : introduction au déploiement, automatisation, configuration des variables, importance des pull requests, vérification et débogage.
- Instruction complète de mise en production : dernier commit vérifié sans secret ni fichier .env, push de la branche, création de pull request vers la branche principale, puis déploiement Vercel.
- Auto-dérision de l'auteur sur son propre niveau de flemme technique face à l'exécution via interface plutôt que terminal, une décision pédagogique pour rendre le processus visible aux apprenants.
- Démonstration du processus automatisé complet : push de branche sur GitHub, création et merge de pull request, mise à jour du master local, puis ajout des variables d'environnement.
- Explication pédagogique de l'intérêt d'une pull request par rapport à un simple git merge direct : introduction d'une étape de revue et de contrôle avant intégration dans la branche principale.
- Confirmation du déploiement final réussi malgré quelques erreurs mineures auto-corrigées par l'IA, avec vérification complète : pas de secret exposé, variables Vercel synchronisées, application en ligne.
- Vérification en direct de l'application déployée (Thumbbreaker) via le navigateur, avec constat qu'un setup Polar reste à finaliser (variables manquantes) sur la page de pricing.
- Test grandeur nature de l'application déployée : import d'assets d'une personne réelle (Reynald) et d'une police custom pour valider l'expérience utilisateur complète en production.
- Exemple concret de prompt de génération testé en production : miniature avec une personne tenant un logo en métal brossé, texte « trilliard » en arrière-plan, scène en studio avec éclairage spécifique.
- Poursuite de l'affinage du prompt de test (reflets, texte, ambiance studio bleu) avant lancement de la génération en attente de résultat, avec vérification que tous les assets sont bien pris en compte.
- Résultat convaincant obtenu en production (image générée avec le chiffre « milliard » affiché correctement), avec identification simultanée d'une erreur mineure à corriger notée dans le suivi.
- Test de la fonctionnalité d'itération sur une génération existante, avec ajout de nouvelles corrections à la liste (couleur rouge sur certains éléments) et démonstration de la copie de prompt.

## Concepts cles
- plan de présentation du module de déploiement avec Vercel
- instruction complète de mise en production (commit sans secret, PR, déploiement)
- choix pédagogique d'exécution via interface plutôt que terminal (visibilité pour les apprenants)
- démonstration du processus automatisé complet de déploiement (push, PR, merge, variables)
- explication de l'intérêt d'une pull request vs merge direct
- confirmation du déploiement final réussi avec auto-correction et vérifications de sécurité
- vérification en direct de l'application déployée et setup Polar restant à finaliser
- test grandeur nature en production avec assets réels et police custom
- exemple concret de prompt de génération testé en production (mise en scène détaillée)
- affinage du prompt de test avant lancement de la génération
- résultat convaincant obtenu en production avec erreur mineure identifiée
- test de la fonctionnalité d'itération et démonstration de copie de prompt

## Outils mentionnes
- Vercel
- GitHub
- Git
- Polar

## Tips techniques
- Toujours vérifier l'absence de secrets ou fichiers .env dans un commit avant tout push et déploiement en production

## Cas d'usage reels
- [[]]
