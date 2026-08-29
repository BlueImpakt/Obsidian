---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.11 Audit et sécurité.txt"
---

# 17.11 Audit et sécurité

## Resume
- Sommaire du module audit et sécurité : introduction à l'audit, installation de Trail of Bits, ajout de skills complémentaires, configuration des outils, lancement de l'audit complet.
- Introduction à l'audit de sécurité via installation d'un plugin marketplace (Trail of Bits/skills), une société spécialisée dans l'audit de sécurité fournissant ce plugin pour Claude.
- Démonstration d'installation de skills complémentaires (verification loop) via commande directe ou déclenchement automatique, illustrant la flexibilité d'installation des outils d'audit.
- Installation réussie des skills Convex pour l'audit, avec constat que les skills TanStack ne sont pas trouvés automatiquement, nécessitant une recherche manuelle du repository.
- Résolution du problème d'installation manquante en demandant à l'IA de chercher directement le repository des skills TanStack sur le web, avant de lancer la phase d'audit complète.
- Lancement de la phase d'audit complète analysant toutes les parties du code pour détecter d'éventuels problèmes de sécurité liés à la base de données, avec invitation à ne pas perdre de temps pendant l'exécution.
- Démonstration d'achat de nom de domaine (11,25€ pour un an) avant configuration ultérieure dans Resend, une étape technique concrète du déploiement de l'infrastructure email.
- Démonstration de création de projet Vercel lié directement à un repository GitHub existant, une étape d'intégration continue reliant le code source au déploiement.
- Explication du concept de déploiement : republier en ligne une nouvelle version accessible à tous les utilisateurs, visible dans l'historique des déploiements (exemple initial commit sur la branche master).
- Démonstration de modification des enregistrements DNS pour lier le domaine acheté au projet Resend, avec choix stratégique du .com plutôt que du .io initialement configuré.
- Vérification et ajout d'un enregistrement DMARC manquant dans la configuration DNS via Vercel, une étape de sécurisation email souvent oubliée.
- Confirmation de la reconnaissance automatique du provider (Vercel) et rapidité de propagation DNS, avec transition vers la vérification des résultats de l'audit de sécurité lancé précédemment.
- Résultats concrets de l'audit de sécurité : détection d'une faille permettant de modifier la quantité de crédits sans contrôle, et d'un problème d'accès non autorisé aux URLs signées de fichiers stockés.
- Lancement d'un second scan d'audit pour vérification approfondie, avec incident mineur de détection des plugins Trail of Bits (annonce initiale erronée de zéro plugin installé).
- Confirmation de 4 plugins correctement installés, avec planification de trois sprints de correction des erreurs détectées avant réévaluation finale du résultat.
- Application des corrections identifiées : ajout de 5 variables manquantes détectées par l'audit, avec vérification directe dans l'environnement de développement Convex.
- Anecdote de confusion personnelle liée à la multiplicité des comptes gérés (sandbox oubliée), illustrant le défi organisationnel réel de gérer plusieurs environnements en parallèle.
- Démonstration de remplissage des informations business requises (Software SaaS, Thumbnail Generator, modèle Subscription) pour finaliser la configuration du dashboard de paiement.
- Mise en garde sur la récupération de clés API via CLI dans le flow de conversation, jugée risquée ; distinction entre le Polar organization token et le webhook secret, deux éléments séparés à générer.
- Détection automatique d'une variable manquante (Better Auth URL) après déploiement, résolue par l'ajout automatique de l'URL de production Convex, avec récapitulatif final du déploiement.
- Démonstration de création d'un nouveau projet nommé « Thumbbreaker » avec ouverture automatique d'une nouvelle URL dédiée à la sélection et configuration des services du projet.
- Configuration des paramètres externes du projet (email de support, domaine hello@thumbbreaker.com) avec précision sur l'usage destiné aux utilisateurs externes plutôt qu'internes.
- Configuration finale de l'authentification Google (Client ID et Client Secret) confirmée avec succès, une étape technique complétant l'intégration OAuth de l'application.

## Concepts cles
- plan de présentation du module audit et sécurité
- introduction à l'audit de sécurité via le plugin Trail of Bits
- démonstration d'installation de skills complémentaires (verification loop)
- installation des skills Convex et échec de recherche automatique des skills TanStack
- résolution par recherche web directe du repository de skills manquant
- lancement de la phase d'audit complète de sécurité (base de données incluse)
- démonstration d'achat de domaine (11,25€/an) avant configuration Resend
- démonstration de création de projet Vercel lié à GitHub
- explication du concept de déploiement et historique visible dans Vercel
- modification des enregistrements DNS pour lier domaine et Resend (choix .com vs .io)
- ajout d'un enregistrement DMARC manquant via Vercel
- confirmation de propagation DNS rapide et transition vers les résultats de l'audit
- résultats concrets de l'audit : failles sur crédits modifiables et URLs de storage exposées
- lancement d'un second scan d'audit avec incident mineur de détection de plugins
- confirmation de 4 plugins installés et planification de sprints de correction
- application des corrections : 5 variables manquantes ajoutées, vérification Convex
- anecdote de confusion personnelle liée à la multiplicité des comptes/environnements
- démonstration de remplissage des informations business pour le dashboard de paiement
- mise en garde sur la récupération de clés API via CLI, distinction token vs webhook secret
- détection et correction automatique d'une variable manquante (Better Auth URL)
- démonstration de création de projet nommé avec URL dédiée aux services
- configuration des paramètres externes du projet (email de support, sous-domaine)
- configuration finale réussie de l'authentification Google OAuth (Client ID/Secret)

## Outils mentionnes
- Trail of Bits
- Claude
- Convex
- TanStack
- Resend
- Vercel
- GitHub
- Polar
- BetterAuth
- Google

## Tips techniques
- Demander à l'IA de chercher directement sur le web un repository de skills manquant plutôt que d'abandonner l'installation
- Toujours vérifier la présence de l'enregistrement DMARC en plus des autres enregistrements DNS, souvent oublié mais important pour la sécurité email
- Toujours vérifier via audit que les quantités sensibles (crédits) ne sont pas modifiables côté client sans contrôle serveur
- Éviter de faire récupérer des clés API sensibles via CLI dans le flux de conversation avec l'IA, pour limiter les risques d'exposition

## Cas d'usage reels
- [[]]
