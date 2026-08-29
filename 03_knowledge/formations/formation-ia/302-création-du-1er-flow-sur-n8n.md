---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.02 Création du 1er flow sur N8N.txt"
---

# 3.02 Création du 1er flow sur N8N

## Resume
- Introduction à la création du premier workflow N8n : réglage préalable du thème en light (clair) plutôt que dark, une préférence personnelle de l'auteur pour améliorer la visibilité pédagogique de la démonstration.
- Démonstration de l'ajout de la première étape via raccourci clavier : identification des triggers, éléments fonctionnant comme sur Make en se déclenchant dès qu'un événement spécifique se produit.
- Présentation des trois panneaux de l'interface d'un node : panneau input à gauche, panneau central pour l'action (exemple « create a draft »), et panneau output à droite, la logique de base de construction sur N8n.
- Présentation des variables d'exécution disponibles : ID de l'exécution, mode, accès test, Resume URL (utile pour le node Wait qui sera vu plus tard, permettant de mettre en pause un workflow).
- Présentation de la variable $workflow donnant l'ID du workflow, utile pour le débogage en identifiant précisément d'où provient une exécution. Introduction du panneau central de visualisation des données entrantes/sortantes.
- Démonstration du renommage d'une action dans le panneau central (« créer un brouillon »), avec présentation d'une fenêtre permettant de mieux visualiser et organiser les données selon différents modes d'affichage.
- Explication de l'intérêt d'un affichage adapté pour les tables avec beaucoup d'éléments, et possibilité de redimensionner les valeurs affichées pour mieux gérer les longs textes dans l'output.
- Explication cruciale d'une option de traitement par lot : sans l'activer, 10 contacts trouvés dans Airtable déclenchent l'envoi de 10 messages séparés. En cochant l'option, un seul message est envoyé avec tous les contacts en destinataires.
- Introduction d'une option importante concernant les résultats vides : si une recherche Airtable ne retourne aucun contact correspondant, l'outil peut par défaut renvoyer une réponse vide plutôt que de bloquer le workflow.
- Confirmation de l'importance d'activer cette option pour toujours obtenir une réponse (même vide) permettant de poursuivre le flow, particulièrement crucial quand l'étape suivante dépend du résultat de la recherche.
- Comparaison entre version cloud et self-hosted pour la connexion (Sign in with Google), avec renvoi vers une vidéo dédiée au self-hosting de N8n pour plus de détails sur cette configuration alternative.
- Panorama des actions disponibles pour les brouillons Gmail : Create a draft, Delete a draft, Get a draft, Get many draft, illustrant la richesse des opérations CRUD possibles sur ce type d'objet.
- Démonstration pratique de création d'une variable personnalisée dans N8n : définir un nom (prénom) et sa valeur (Théo), puis sauvegarder pour rendre cette variable réutilisable dans les workflows.
- Distinction technique importante : $VARS.prenom écrit simplement est une valeur texte statique, tandis que l'usage des doubles crochets courbes (accolades) signale une valeur dynamique, un concept similaire à ce qui existe sur Make.
- Explication de la navigation dans un JSON reçu via la notation par point pour creuser dans les objets, illustrée par la construction d'un message personnalisé (« Salut Théo ») utilisant la variable dynamique plutôt qu'un texte statique.
- Présentation de Execute Step comme méthode de test recommandée : plutôt que de déclencher l'intégralité du workflow, cette option permet de tester uniquement l'étape en cours de construction, plus efficace pour le débogage progressif.
- Explication technique sur le Thread ID : lors d'une nouvelle conversation (pas une réponse), les ID restent identiques puisqu'aucune adresse n'a encore été contactée, contrairement à une réponse qui aurait des identifiants distincts.
- Conclusion de la leçon avec annonce d'un point important oublié à propos de l'opération de création de draft, dont les particularités seront précisées juste après pour compléter la démonstration.
- Précision importante sur une fonctionnalité présente sur Telegram, WhatsApp et Gmail mais absente sur Discord : un avertissement à bien garder en tête et penser à désactiver selon la plateforme utilisée.

## Concepts cles
- réglage du thème light pour la démonstration
- ajout de première étape via raccourci clavier (triggers)
- structure à trois panneaux (input/action centrale/output)
- variables d'exécution (ID, mode, Resume URL pour le node Wait)
- variable $workflow pour le débogage
- renommage d'action et options de visualisation des données
- adaptation de l'affichage pour tables volumineuses et longs textes
- option de traitement groupé (un seul message pour plusieurs contacts)
- gestion des résultats vides d'une recherche
- importance de toujours obtenir une réponse pour poursuivre le flow
- différence de connexion cloud vs self-hosted (renvoi à vidéo dédiée)
- panorama des actions CRUD pour les brouillons (Gmail)
- création pratique d'une variable personnalisée dans N8n
- distinction valeur texte statique vs valeur dynamique (accolades)
- navigation JSON par notation point pour construire un message dynamique
- Execute Step pour tester une seule étape (méthode de débogage recommandée)
- logique du Thread ID selon nouvelle conversation vs réponse
- annonce d'un point complémentaire important sur la création de draft
- différence de fonctionnalité selon plateforme (Discord vs Telegram/WhatsApp/Gmail)

## Outils mentionnes
- n8n
- Airtable
- Google
- Gmail
- Make
- Discord
- Telegram
- WhatsApp

## Tips techniques
- Activer l'option de traitement groupé pour envoyer un seul message à plusieurs destinataires plutôt qu'un message par contact individuel
- Toujours activer l'option de réponse vide par défaut quand une étape suivante dépend du résultat, pour éviter un blocage du workflow
- Utiliser les doubles accolades pour signaler une valeur dynamique dans N8n, contrairement à une simple référence texte statique
- Utiliser Execute Step pour tester une seule étape à la fois plutôt que de déclencher l'ensemble du workflow, pour un débogage plus efficace
- Vérifier la disponibilité d'une fonctionnalité spécifique selon la plateforme (absente sur Discord, présente sur Telegram/WhatsApp/Gmail)

## Cas d'usage reels
- [[]]
