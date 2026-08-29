---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.3 Automatiser les tâches restantes avec PhantomBuster.txt"
---

# 3.3 Automatiser les tâches restantes avec PhantomBuster

## Resume
- Introduction à Phantom Buster, un autre outil important (entreprise française) permettant d'automatiser diverses tâches, présenté directement via une visite de son site officiel.
- Limite d'Apify pour l'action LinkedIn : il permet de récupérer des informations disponibles mais ne peut pas déclencher d'actions directes (comme reprogrammer un contact ajouté), une distinction importante avec PhantomBuster.
- Introduction du cas d'usage engagement LinkedIn : au-delà de créer des posts, la croissance sur LinkedIn passe aussi par l'engagement actif avec le contenu d'autres personnes.
- Observation que les influenceurs LinkedIn actifs mettent souvent en place des stratégies d'automatisation de commentaires bien placés, générant énormément d'engagement sur leur propre profil par ricochet.
- Exemple chiffré personnel de l'auteur : un simple commentaire humoristique a généré 18 420 impressions, illustrant comment un commentaire bien placé peut être vu par des milliers de personnes.
- Explication des deux avantages de cette stratégie de commentaires ciblés : elle rend visible auprès d'une nouvelle audience et s'inscrit dans la philosophie d'optimisation prônée tout au long de la formation.
- Présentation des actions disponibles sur PhantomBuster : accepter automatiquement des invitations LinkedIn, visiter des profils, exporter ses connexions, scraper des pages d'entreprise ou des profils.
- Explication technique du fonctionnement de PhantomBuster : il utilise le cookie de session de l'utilisateur pour interagir en son nom, automatisant un processus normalement manuel.
- Explication du risque de détection et de blocage par LinkedIn si le comportement automatisé est trop mécanique. PhantomBuster contourne ce risque en simulant un comportement humain réaliste avec des pauses entre actions.
- Démonstration pratique de configuration : installation d'une extension de détection automatique, connexion à un fichier source (Google Sheets recommandé plutôt que CSV) et sélection de la colonne source.
- Précision technique : le fichier Google Sheets source doit être rendu publiquement accessible (partage « anyone with the link ») pour que le robot puisse y accéder correctement.
- Précision de limite recommandée : environ 80 commentaires par jour maximum, au-delà de quoi il faudrait rafraîchir la session plus fréquemment pour paraître suffisamment actif sur la plateforme.
- Recommandation de montée en charge progressive : commencer avec 2-3 commentaires par jour puis augmenter graduellement (4-5, 6-7, 8-9) pour donner l'impression d'un engouement naturel plutôt que d'un comportement robotique.
- Mise en garde sur la détection facile par LinkedIn d'un comportement suspect. Recommandation de ne même pas approcher la limite théorique de 80, en restant très progressif dans l'augmentation.
- Présentation des options de fréquence de déclenchement (une, deux, trois fois par jour ou mode avancé), avec recommandation personnelle de 4-5 exécutions quotidiennes comme bon compromis.
- Présentation des paramètres avancés : options de proxy PhantomBuster, requêtes HTTP, webhooks (notification de fin de processus), et gestion de fichiers (combinaison ou suppression de fichiers).

## Concepts cles
- introduction à Phantom Buster (entreprise française d'automatisation)
- limite d'Apify : récupération de données uniquement, pas d'actions directes
- importance de l'engagement actif pour la croissance LinkedIn
- stratégie d'automatisation de commentaires bien placés (générateur d'engagement)
- exemple chiffré : 18 420 impressions sur un simple commentaire
- double avantage des commentaires ciblés (visibilité + optimisation)
- panorama des actions PhantomBuster (invitations, profils, export)
- mécanisme technique : utilisation du cookie de session pour automatiser
- simulation de comportement humain par PhantomBuster (pauses réalistes)
- configuration pratique (extension, source Google Sheets recommandée)
- nécessité de partage public du Google Sheets source
- limite recommandée de 80 commentaires par jour
- stratégie de montée en charge progressive pour paraître naturel
- recommandation de rester bien en-dessous de la limite théorique de 80
- recommandation de fréquence (4-5 fois par jour)
- paramètres avancés (proxys, webhooks, gestion de fichiers)

## Outils mentionnes
- PhantomBuster
- Apify
- LinkedIn
- Google Sheets

## Tips techniques
- Privilégier Google Sheets plutôt qu'un fichier CSV comme source pour PhantomBuster, pour une meilleure fiabilité
- Rendre le Google Sheets source publiquement accessible via le lien, sinon PhantomBuster ne peut pas y accéder
- Augmenter progressivement le volume de commentaires automatisés (2-3 puis 4-5 etc.) pour paraître naturel aux yeux de LinkedIn
- Configurer PhantomBuster pour s'exécuter 4-5 fois par jour, un compromis recommandé entre naturel et efficacité

## Cas d'usage reels
- [[]]
