---
tags: [formation, millenium]
module: Formation IA
section: "Agents de Productivité"
source_transcript: "6.01 Agent Inbox Zero.txt"
---

# 6.01 Agent Inbox Zero

## Resume
- Introduction à la construction de l'agent Inbox Zero, destiné à trier automatiquement les emails et effectuer diverses tâches, avec référence à des statistiques sur le temps perdu par les cadres dirigeants sur leurs emails.
- Recommandation d'analyser ses propres emails pour identifier les catégories réelles reçues, illustrée par l'exemple personnel de l'auteur (demandes de support de deux types).
- Poursuite de l'identification des catégories d'emails personnels : demandes pour la chaîne YouTube et partenariats sponsorisés, illustrant la diversité des types à distinguer.
- Finalisation de la liste des cinq types d'emails identifiés : support, prospection, newsletters/comptes, collaborateurs, une base pour construire la classification de l'agent.
- Explication du mécanisme de déclenchement Gmail : plutôt qu'un déclenchement instantané, N8n interroge périodiquement (poll time) pour vérifier l'arrivée de nouveaux emails.
- Démonstration de connexion simple au compte Gmail via l'option cloud, avec mention d'une vidéo alternative pour les instances auto-hébergées de N8n.
- Vérification en direct de la boîte Gmail connectée, avec nettoyage des emails de test non pertinents et conservation d'exemples de newsletters pour la démonstration.
- Démonstration d'utilisation d'expressions pour nettoyer le contenu HTML des emails, supprimant les balises pour ne conserver que le texte brut exploitable par l'agent.
- Choix méthodologique de configuration du Text Classifier avec plusieurs catégories définies, une étape clé nécessitant un bon mapping des types d'emails identifiés.
- Démonstration de définition précise des catégories du classifieur (support/aide no-code, demande de facture client) avec formulations descriptives détaillées.
- Recommandation d'utiliser les adresses email des collaborateurs (plutôt que des critères de contenu) pour un tri fiable et limitant le risque d'erreur, avec catégorie transactionnelle distincte.
- Démonstration de configuration d'un second Text Classifier récupérant le contenu édité, avec classification binaire simplifiée (factures vs support/autre demande).
- Configuration du message système et du contenu utilisateur pour l'étape de traitement suivante, une structure de prompt classique à deux niveaux.
- Précision technique sur l'échappement des caractères spéciaux (précédés d'un slash inversé) nécessaire avant l'envoi du contenu vers Telegram, avec choix du modèle OpenAI.
- Sélection du modèle GPT-4.1 mini pour l'agent, avec réflexion sur l'alternative d'un agent IA complet, avant envoi d'un résumé de newsletter vers un chat Telegram spécifique.
- Démonstration d'ajout du bot Telegram créé au channel dédié via les droits Administrator, une étape technique nécessaire pour permettre l'envoi de messages automatisés.
- Test du workflow de filtrage vers la branche newsletter, avec traitement du résumé de contenu par le modèle, un processus prenant du temps selon le volume de contenu à traiter.
- Ajout d'une contrainte de longueur maximale (4000 caractères, balises incluses) dans le prompt de résumé, une précision importante pour respecter les limites de Telegram.
- Répétition d'instructions de formatage (échappement des caractères spéciaux) pour forcer le modèle à respecter la contrainte, un exemple de débogage itératif par répétition de consigne.
- Décision de changer de modèle face à un résultat persistant insatisfaisant, en passant à un AI Agent avec configuration Define Below plutôt que le nœud LLM simple utilisé initialement.
- Confirmation d'amélioration du résultat avec le nouveau modèle, l'agent analysant correctement la structure de la newsletter avant l'envoi du message texte configuré.
- Correction d'un oubli de configuration : activation du Parse Mode en Markdown V2, résolvant les problèmes d'affichage de codification dans le résumé de newsletter envoyé.
- Rappel de l'objectif de l'agent (alerter, pas distraire) avec présentation optionnelle de la catégorisation Gmail via ajout de labels sur les emails traités.
- Démonstration de création de sous-labels Gmail hiérarchiques (Prospection > YouTube, Prospection > Business, Autre) pour une classification structurée des emails.
- Configuration d'actions complémentaires Gmail après traitement : marquer un message comme lu, ou le retirer de l'inbox via suppression de label, complétant le cycle de traitement automatisé.
- Fin de la première partie (traitement des newsletters entrantes), avec transition vers le traitement des emails urgents nécessitant un channel Telegram dédié.
- Justification de la préférence pour Telegram plutôt que Slack : absence de limite sur le nombre de messages et meilleure expérience mobile pour les échanges en déplacement.
- Explication de l'usage d'un channel dédié permettant à plusieurs personnes d'être averties simultanément, avec possibilité de personnalisation visuelle de l'apparence du bot.
- Configuration de l'agent d'alerte urgente avec possibilité d'utiliser un modèle différent, potentiellement moins coûteux, adapté à ce cas d'usage spécifique de détection d'urgence.
- Précision sur la configuration du nouveau channel dédié aux alertes urgentes, avec chat ID distinct nécessitant la répétition de la configuration du déclencheur Telegram.
- Test pratique d'envoi d'un email fictif contenant un lien suspect (« meta.com ») pour vérifier la capacité de l'agent à détecter ce type de contenu potentiellement frauduleux.
- Résolution d'un incident mineur : l'email test s'était retrouvé en spam, nécessitant de le marquer comme « Not Spam » avant de poursuivre le test.
- Confirmation de la bonne catégorisation de l'email test comme urgent par l'agent, validant le fonctionnement de la classification automatisée.
- Résultat impressionnant : l'agent identifie de lui-même que le lien contenu dans l'email semble suspect et frauduleux, une capacité d'analyse avancée intégrée.
- Explication de la nécessité de distinguer les identifiants JSON entre les deux branches parallèles (newsletter et urgent) pour éviter toute confusion dans le routage des labels Gmail.
- Finalisation du traitement des emails urgents avec marquage comme important, avant transition vers le traitement d'une nouvelle catégorie : les factures.

## Concepts cles
- introduction à l'agent Inbox Zero de tri automatique d'emails
- recommandation d'analyser ses propres catégories d'emails réelles avant de construire l'agent
- identification de catégories d'emails (YouTube, partenariats sponsorisés)
- finalisation de la liste des cinq types d'emails identifiés pour la classification
- explication du mécanisme de polling Gmail (poll time) plutôt que déclenchement instantané
- démonstration de connexion Gmail via cloud (alternative auto-hébergée mentionnée)
- vérification en direct de la boîte Gmail et nettoyage des emails de test
- démonstration de nettoyage du contenu HTML des emails (suppression de balises)
- configuration du Text Classifier avec catégories définies (importance du mapping)
- démonstration de définition précise des catégories (support, demande de facture)
- recommandation d'utiliser les adresses email des collaborateurs pour un tri fiable
- démonstration d'un second Text Classifier avec classification binaire simplifiée
- configuration du message système et contenu utilisateur pour le traitement
- précision technique sur l'échappement des caractères spéciaux avant envoi Telegram
- sélection du modèle GPT-4.1 mini et envoi de résumé vers Telegram
- démonstration d'ajout du bot Telegram au channel via droits Administrator
- test du workflow de filtrage et résumé de contenu newsletter
- ajout d'une contrainte de longueur maximale (4000 caractères) pour respecter Telegram
- débogage itératif par répétition de consigne de formatage
- décision de changer de modèle (AI Agent Define Below) face à un résultat insatisfaisant
- confirmation d'amélioration du résultat avec le changement de modèle
- correction d'un oubli de configuration : Parse Mode Markdown V2
- rappel de l'objectif d'alerte non-distrayante et présentation de la catégorisation via labels Gmail
- démonstration de sous-labels Gmail hiérarchiques pour classification structurée
- configuration d'actions complémentaires (marquer comme lu, retirer de l'inbox)
- transition vers le traitement des emails urgents (nouveau channel Telegram)
- justification de la préférence Telegram vs Slack (pas de limite, meilleure UX mobile)
- usage d'un channel dédié pour alerter simultanément plusieurs personnes
- configuration de l'agent d'alerte urgente avec modèle potentiellement moins coûteux
- précision sur la configuration du chat ID distinct pour le channel d'alertes urgentes
- test pratique de détection de lien suspect via email fictif
- résolution d'un incident : email test classé en spam à corriger
- confirmation de la bonne catégorisation d'un email comme urgent
- résultat impressionnant : détection autonome d'un lien frauduleux par l'agent
- nécessité de distinguer les identifiants JSON entre branches parallèles
- finalisation du traitement des emails urgents et transition vers les factures

## Outils mentionnes
- n8n
- Gmail
- Telegram
- OpenAI
- Slack

## Tips techniques
- Analyser d'abord ses propres emails reçus pour identifier les catégories réelles avant de construire un agent de tri automatique
- Utiliser les adresses email connues des collaborateurs comme critère de tri plutôt que l'analyse de contenu, pour limiter le risque d'erreur
- Toujours échapper les caractères spéciaux (précédés d'un slash inversé) avant d'envoyer du contenu formaté vers Telegram
- Préciser explicitement une limite de caractères (incluant les balises) dans le prompt de résumé, pour respecter les contraintes de la plateforme de destination
- Répéter et reformuler une instruction plusieurs fois si le modèle ne la respecte pas du premier coup, une technique de débogage de prompt courante
- Changer de type de nœud (AI Agent plutôt que LLM simple) si un modèle persiste à ne pas respecter une contrainte de formatage précise
- Toujours vérifier l'activation du Parse Mode Markdown V2 sur Telegram pour éviter les problèmes d'affichage de codification dans les messages formatés
- Utiliser un modèle moins coûteux pour la détection d'urgence, une tâche généralement plus simple que la génération de contenu
- Bien distinguer les identifiants JSON entre différentes branches parallèles d'un workflow pour éviter toute ambiguïté de routage

## Cas d'usage reels
- [[]]
