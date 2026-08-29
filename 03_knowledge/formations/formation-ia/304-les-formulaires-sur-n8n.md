---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.04 Les formulaires sur N8N.txt"
---

# 3.04 Les formulaires sur N8N

## Resume
- Introduction aux formulaires sur N8n, décrits comme particulièrement puissants : présentation de la distinction entre formulaires de test et formulaires de production dans l'interface.
- Configuration de base d'un formulaire de démonstration : authentification, titre et description, avant d'aborder la section Form Elements où se construit le contenu réel du formulaire.
- Critique mineure d'ergonomie sur l'utilisation d'espace dans l'interface. Démonstration de la définition d'un champ de formulaire (prénom) parmi les nombreux types disponibles (custom, HTML, date, etc.).
- Démonstration pratique de remplissage du formulaire avec des exemples ludiques (prénom Kilian, nom Mbappé), et astuce d'utilisation de la touche Tab pour naviguer rapidement entre les champs successifs.
- Explication de la différence entre champ email et champ texte simple : un champ texte accepterait n'importe quelle saisie même invalide, tandis qu'un champ email valide le format avant transmission à une API d'envoi.
- Démonstration d'un champ caché dans un formulaire N8n : un champ « programme » (valeur « AI Pro ») invisible pour le remplissant mais inséré automatiquement comme s'il avait été écrit, utile pour segmenter les soumissions.
- Explication de l'usage combiné : le champ caché permet de filtrer dynamiquement les valeurs selon le programme lié (exemple Bootcampia), avec démonstration de l'ajout d'un champ de sélection numérique pour l'âge.
- Remplissage pratique du formulaire de test avec des exemples concrets (âge 40 ans, métier indépendant), illustrant l'utilisation typique du formulaire en conditions réelles.
- Confirmation de la soumission du formulaire test avec rappel qu'il ne doit pas être mis en production, et visualisation automatique de la réponse enregistrée au format output, prête à être réutilisée dans les modules suivants.
- Rappel important : il faut toujours exécuter le formulaire pour l'activer. Présentation de l'option de personnalisation du label du bouton, initialement « Submit » par défaut, personnalisable selon le besoin.
- Présentation des options avancées : Ignore Bots (filtre anti-bot), Form Path (personnalisation de l'URL du formulaire, similaire aux webhooks), et Form Response pour définir la réponse retournée.
- Présentation de l'option Workflow Timezone permettant de choisir si le fuseau horaire doit apparaître dans le champ Submitted At, ainsi que l'introduction du Form Styling pour personnaliser l'apparence visuelle du formulaire.
- Astuce astucieuse : utiliser Claude ou ChatGPT pour générer du CSS personnalisé en demandant un style spécifique (exemple : « style Notion ») afin de personnaliser rapidement l'apparence d'un formulaire N8n.
- Poursuite de la démonstration du hack de personnalisation par IA, l'auteur encourageant à ne pas hésiter à déléguer ce type de tâche technique à l'IA plutôt que de coder soi-même le CSS.
- Démonstration finale du hack : copier le CSS généré par l'IA et le coller dans le champ de style du formulaire, obtenant instantanément un style personnalisé (façon Notion) adaptable à volonté.
- Présentation d'une option de timing de réponse : choisir de répondre dès la soumission du formulaire, ou seulement une fois le workflow entièrement terminé, une option pratique pour certains cas de traitement asynchrone.
- Découverte d'une fonctionnalité peu connue mais extraordinaire de N8n : personnaliser dynamiquement les questions suivantes selon les réponses déjà soumises (exemple : demander le chiffre d'affaires seulement si l'utilisateur est indépendant).
- Démonstration pratique de formulaire multi-étapes avec question personnalisée insolite (prénom du chien), illustrant concrètement la puissance des formulaires N8n pour créer des parcours conditionnels et engageants.
- Récapitulatif des champs collectés par le formulaire construit (prénom, nom, email, attente du programme, âge, métier actuel), préparant la structuration en vue de l'enregistrement dans une base de données.
- Construction de la structure de la table de données (email, métier actuel, attente) et démonstration de la connexion vers Google Sheets pour enregistrer automatiquement la réponse de formulaire.
- Confirmation de l'enregistrement de la demande avec les données récupérées, introduction du concept clé de champs d'expression dynamiques, différenciés des champs fixes classiques.
- Explication de la récupération dynamique de la valeur du champ prénom depuis le module précédent (identifié par $json), un mécanisme jugé très important pour comprendre la circulation des données entre modules.
- Astuce technique de raccourci clavier pour créer des accolades (crochets courbes) sur Windows via Alt + parenthèse, indispensable pour manipuler les expressions dynamiques dans N8n.
- Test final du flow multi-étapes avec un nouvel exemple (Jean, artisan, 28 ans) : validation du bon fonctionnement global malgré un petit souci d'affichage initial de la réponse, finalement résolu.

## Concepts cles
- introduction aux formulaires N8n (test vs production)
- configuration de base d'un formulaire (titre, description, authentification)
- types de champs de formulaire disponibles (custom, HTML, date)
- astuce touche Tab pour naviguer entre champs de formulaire
- différence entre champ email (validation) et champ texte simple
- champ caché pour segmenter automatiquement les soumissions (invisible à l'utilisateur)
- filtrage dynamique via champ caché + champ numérique (âge)
- remplissage pratique d'un formulaire de test
- confirmation de soumission test et réutilisation des données output
- nécessité d'exécuter le formulaire pour l'activer
- personnalisation du label du bouton
- options Ignore Bots et Form Path personnalisable
- option Workflow Timezone et introduction du Form Styling
- astuce d'utiliser Claude/ChatGPT pour générer du CSS personnalisé de formulaire
- encouragement à déléguer la personnalisation CSS à l'IA
- copier-coller du CSS généré par IA dans le champ de style
- option de timing de réponse (immédiat vs après fin du workflow)
- personnalisation dynamique des questions suivantes selon réponses précédentes
- exemple concret de formulaire multi-étapes avec question personnalisée
- récapitulatif des champs collectés avant enregistrement
- structuration de la table et connexion à Google Sheets
- introduction des champs d'expression dynamiques (vs fixes)
- récupération dynamique via $json du module précédent
- raccourci clavier Windows pour créer des accolades (Alt+parenthèse)
- test final validant le flow multi-étapes complet

## Outils mentionnes
- n8n
- Claude
- ChatGPT
- Google Sheets

## Tips techniques
- Utiliser la touche Tab pour naviguer rapidement entre les champs lors de la configuration d'un formulaire
- Utiliser un champ de type email plutôt que texte pour garantir la validité du format avant transmission à une API
- Utiliser un champ caché pour taguer automatiquement les soumissions de formulaire par programme/source sans que l'utilisateur le voie
- Toujours exécuter le formulaire N8n avant de le tester, sinon il reste inactif
- Demander à Claude ou ChatGPT de générer le CSS de personnalisation d'un formulaire en décrivant simplement le style visuel souhaité
- Utiliser la personnalisation dynamique des questions de formulaire selon les réponses déjà données pour un parcours plus pertinent
- Sur Windows, utiliser Alt+parenthèse pour créer facilement des accolades nécessaires aux expressions dynamiques N8n

## Cas d'usage reels
- [[]]
