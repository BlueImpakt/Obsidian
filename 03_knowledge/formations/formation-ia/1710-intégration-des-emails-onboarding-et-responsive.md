---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.10 Intégration des emails, onboarding et responsive.txt"
---

# 17.10 Intégration des emails, onboarding et responsive

## Resume
- Sommaire du module intégration des emails, onboarding et responsive : project updates, email integration strategy, onboarding workflow, implementing onboarding, copywriting skills, execution and next steps.
- Mise à jour de l'avancement du projet : mise en place de la capacité à mentionner des mots-clés dans les prompts, une fonctionnalité jugée particulièrement utile pour la génération d'images.
- Instruction de configuration d'une séquence d'onboarding pour les nouveaux utilisateurs : overlay masquant le fond avec pop-ups contextualisées guidant les premières étapes d'usage de l'application.
- Utilisation d'un skill spécialisé (Onboarding Specialist) avec vérification systématique préalable de son contenu, révélant une anomalie amusante (texte en polonais détecté dans le skill).
- Bilan de configuration des emails automatiques (7 emails créés) avec estimation que 80% du travail était correct d'emblée, le reste nécessitant des ajustements successifs, avant configuration de Resend en production.
- Poursuite du travail sur le design des 7 emails refactorisés, avec upload d'une miniature dans Convex, actuellement stockée en statique en attendant une meilleure solution.
- Correction d'un problème de cohérence visuelle (excès de rouge perturbant le call-to-action), avec référence au design system Millenium pour recadrer l'IA vers la charte graphique établie.
- Reconnaissance d'un moment de frustration face à une IA tournant en rond, avec deux options possibles : reset la session ou insister, l'auteur ayant choisi d'insister dans ce cas.
- Présentation de React Email comme librairie d'affichage des emails, avec relance du localhost pour prévisualisation ; précision que le travail sur les emails reste secondaire en importance globale.
- Aperçu du canevas d'email final avec changement de nom de projet en cours de route (« Thumbbreaker »), une référence ludique à une émission télévisée pour enfants.
- Exemple de copywriting créatif pour la séquence d'emails (« un visage humain change tout ») illustrant l'insight que les meilleures miniatures YouTube comportent un visage humain expressif, un défi pour les modèles de génération d'images.
- Configuration de l'étape d'upload d'assets dans l'onboarding : demander la signature visuelle de l'utilisateur (logo, background, photo brute) que l'IA analysera pour en extraire ce dont elle a besoin.
- Exemple de copywriting différenciant pour l'onboarding : mise en avant du coût élevé en crédits des outils concurrents (10-12 crédits par tentative) versus le système de reformulation de prompt optimisé du produit.
- Résolution d'un bug lié à un conflit entre deux instances localhost ouvertes simultanément (une pour l'app principale, une pour tester les emails), causant une confusion corrigée par la suite.
- Identification de deux problèmes visuels lors du test d'onboarding (icône croix superposée, manque d'opacité) notés immédiatement pour correction dans la liste de feedback.
- Test complet réussi de l'étape d'onboarding en une seule tentative (« one shot ») : upload logo, police custom, description de miniature, résultat qualifié de niveau masterclass par l'auteur.
- Identification d'un problème d'expérience de chargement trop brutal (transition sans état intermédiaire) après login, avec latence perceptible sur l'affichage initial des crédits (zéro puis mise à jour).
- Réflexion sur l'importance de consacrer du temps à peaufiner minutieusement l'application plutôt que de se concentrer uniquement sur le code brut, illustrée par un test de création d'un nouveau compte de vérification.
- Satisfaction croissante face à la cohérence globale émergente du produit, avec précision que le logo actuellement affiché n'est encore qu'un placeholder temporaire.
- Instruction créative pour le menu utilisateur multi-personnes, façon design iPhone « Liquid Glass », en laissant l'IA réfléchir à la meilleure approche pour switcher entre les personnes et rendre le menu déployable.
- Recherche d'un skill spécialisé pour ajouter des fonctionnalités PWA (Progressive Web App) et notifications push, une approche pragmatique consistant à chercher un skill existant avant de développer soi-même.
- Identification de deux problèmes de mise en page (absence de padding, éléments non fusionnés visuellement) après test sur simulateur, illustrant le processus continu de raffinement responsive.
- Test précis sur preset iPhone (390x844) révélant des bordures collées problématiques, avec instructions détaillées de réorganisation de la disposition des éléments (largeur, alignement).
- Instructions précises d'alignement d'éléments d'interface (cercles, icône avatar vs icône menu) pour garantir une cohérence visuelle de taille entre tous les éléments comparables.
- Rappel de la discipline de vérification systématique de chaque changement, avec satisfaction sur le comportement flottant du menu mobile obtenu, correspondant précisément à l'attente.
- Délégation créative à l'IA pour trouver un mot plus court remplaçant « personne » (trop long sur desktop), tout en gardant le contrôle sur les exigences précises d'alignement des icônes.
- Introduction à la configuration des variables d'environnement pour stocker les clés API, avec explication des deux options possibles : fichier env.local (local uniquement) ou configuration serveur.
- Démonstration de mise à jour de la clé API Resend dans les variables d'environnement via une simple requête à l'IA, illustrant la simplicité de gestion des credentials avec Claude Code.
- Recommandation de sécurité pour le tracking d'emails : utiliser un sous-domaine de tracking discret plutôt que des noms évidents comme « track » ou « t », désormais bien identifiés par les filtres anti-spam.

## Concepts cles
- plan de présentation du module intégration emails/onboarding/responsive
- mise à jour projet : fonctionnalité de mots-clés dans les prompts
- instruction de configuration d'une séquence d'onboarding avec overlay contextualisé
- usage d'un skill spécialisé avec vérification préalable systématique du contenu
- bilan de configuration des 7 emails automatiques (80% correct d'emblée) et passage Resend en production
- refactorisation du design des emails et upload de miniature dans Convex
- correction de cohérence visuelle (excès de rouge) via référence au design system
- gestion de la frustration face à une IA tournant en rond (reset vs insister)
- présentation de React Email et relativisation de l'importance du travail sur les emails
- aperçu du canevas email final avec changement de nom de projet (Thumbbreaker)
- exemple de copywriting créatif basé sur l'insight du visage humain expressif (miniatures YouTube)
- configuration de l'étape d'upload d'assets dans l'onboarding
- exemple de copywriting différenciant comparant le coût en crédits des concurrents
- résolution d'un bug de conflit entre deux instances localhost simultanées
- identification de problèmes visuels en test d'onboarding (icône, opacité)
- test complet réussi de l'onboarding en une seule tentative (one shot)
- identification d'un problème de transition de chargement trop brutale post-login
- importance du peaufinage minutieux au-delà du code brut fonctionnel
- satisfaction face à la cohérence globale émergente (logo encore placeholder)
- instruction créative pour un menu iPhone-esque (Liquid Glass) avec réflexion déléguée à l'IA
- recherche pragmatique d'un skill PWA existant plutôt que développement manuel
- identification de problèmes de mise en page responsive (padding, fusion visuelle)
- test précis sur preset iPhone (390x844) et instructions de réorganisation
- instructions précises d'alignement et de cohérence de taille entre éléments comparables
- rappel de la discipline de vérification systématique et satisfaction sur le menu flottant mobile
- délégation créative à l'IA pour un choix de mot plus court, contrôle gardé sur l'alignement
- introduction aux variables d'environnement pour stocker les clés API (local vs serveur)
- démonstration de mise à jour de clé API Resend via requête simple à l'IA
- recommandation de sous-domaine de tracking discret pour éviter la détection anti-spam

## Outils mentionnes
- Resend
- Convex
- React Email
- YouTube
- Claude Code

## Tips techniques
- Configurer une séquence d'onboarding avec overlay et pop-ups contextualisées pour guider les nouveaux utilisateurs dès la création de compte
- Toujours vérifier le contenu d'un skill avant de l'utiliser, pour détecter d'éventuelles anomalies (comme du texte dans une langue inattendue)
- Référencer explicitement le design system établi quand l'IA dévie de la charte graphique, plutôt que de décrire les corrections au cas par cas
- Face à une IA qui tourne en rond sur une tâche, choisir entre réinitialiser la session ou insister avec des instructions plus précises
- Comparer explicitement le coût en crédits/tentatives des concurrents dans le copywriting d'onboarding pour valoriser l'efficacité du système propre
- Éviter d'ouvrir plusieurs instances localhost simultanément sur un même projet, source de conflits et de confusion difficile à diagnostiquer
- Consacrer du temps significatif au peaufinage détaillé de l'expérience utilisateur, pas seulement au fonctionnement technique brut du code
- Décrire une intention visuelle de haut niveau (référence design connue) et laisser l'IA proposer la meilleure implémentation technique concrète
- Chercher systématiquement un skill existant pour une fonctionnalité standard (PWA, notifications push) avant d'envisager un développement manuel
- Tester systématiquement sur des presets d'appareils précis (ex : 390x844 pour iPhone) pour détecter les problèmes de responsive réels
- Toujours tout vérifier systématiquement après chaque modification, même les éléments qui semblaient déjà fonctionnels
- Déléguer les choix créatifs mineurs (formulation de texte court) à l'IA plutôt que de les faire soi-même, tout en gardant le contrôle sur les exigences structurelles
- Utiliser un nom de sous-domaine de tracking discret et non évident (éviter 'track' ou 't'), désormais facilement repérés par les filtres anti-spam

## Cas d'usage reels
- [[]]
