---
tags: [formation, millenium]
module: Formation Productivite
section: "Aller plus loin"
source_transcript: "25. Automatiser le Service Client.txt"
---

# 25. Automatiser le Service Client

## Resume
- Introduction à la construction d'un chatbot de support client automatisé, avec alerte automatique en cas de nouvelle demande à traiter.
- Présentation de Tally comme premier outil utilisé pour le chatbot, avec transparence sur le fait que ce n'est pas une recommandation sponsorisée.
- Précision que le plan gratuit de Tally est largement suffisant pour l'exemple démontré, un bon exemple de pricing accessible.
- Démonstration de la création d'un formulaire de contact affiché sous forme de chatbot interactif dans Tally.
- Présentation des logiques et intégrations disponibles avec Make, l'intégration étant réalisée directement du côté de Make.
- Démonstration de configuration d'un nouveau scénario Make recherchant l'action Tally pour créer la connexion.
- Configuration du module watch webhooks blocks event dans Make, avec création de connexion via la clé API récupérée dans Tally.
- Sélection du formulaire de contact Tally créé, avec précision que ce canal contact concerne les non-clients, généralement peu traités en priorité.
- Récupération et rafraîchissement du bloc ID nécessaire à la reconnaissance du formulaire côté Make, puis sauvegarde de la configuration.
- Configuration du lien avec Notion via le module create database items, en sélectionnant la base de données cible pour stocker les demandes.
- Configuration des propriétés de la base de données support Notion : tag (à traiter plus tard), email, et created time pour horodater chaque demande.
- Ajout d'un champ texte réponse, avec réflexion sur la gestion des réponses vidéo (upload cloud avec URL directe ou méthode alternative).
- Configuration du statut du ticket avec les valeurs open (à traiter) et closed (dupliqué avec coche pour marquer comme traité).
- Ajout d'un indicateur visuel (emoji fire) pour les tickets urgents nécessitant une prise en charge, complétant la structure des champs.
- Configuration d'un filtre pour identifier les demandes déjà traitées (check), avant recherche de la valeur correspondante dans la base de données.
- Configuration de la requête de recherche dans la base de données support, avec mapping des champs message et email pour retrouver l'entrée précise.
- Finalisation des champs de base (date de création, réponse, tags reportés à plus tard) et confirmation de l'objectif d'envoyer les données vers Notion.
- Introduction de Pushcut, un outil d'envoi de notifications sur iPhone habituellement utilisé pour les ventes, réutilisé ici pour alerter des nouvelles questions.
- Démonstration de la création d'une nouvelle notification Pushcut dédiée aux alertes de support client.
- Explication du choix de sons distinctifs pour différencier les notifications importantes (support) des notifications classiques (WhatsApp, Instagram).
- Configuration du device cible (iPhone spécifiquement) pour la notification, avec possibilité de gérer plusieurs appareils (iPad, iPhone).
- Configuration des paramètres avancés (titre, texte de la notification), avec idée d'inclure directement l'URL Notion pour ouvrir la fiche concernée.
- Configuration dynamique du titre et du texte de la notification à partir de l'email et du message reçus, complétant la structure de l'alerte.
- Sauvegarde de la configuration et lancement d'un premier test en soumettant une question réelle via le formulaire de contact.
- Saisie en direct d'une question test dans le formulaire de contact concernant la possibilité de paiement en plusieurs fois.
- Poursuite de la saisie de la question test dans le formulaire de contact du chatbot.
- Soumission du formulaire avec identité test, suivie d'un test d'exécution du scénario révélant un souci de données manquantes.
- Correction du problème identifié en réajustant les noms de groupes de données (groupe 1, groupe 2) dans Make et Pushcut de manière cohérente.
- Second test avec une nouvelle question, incluant un marqueur distinctif (plus un) pour vérifier que c'est bien cette nouvelle donnée qui est traitée.
- Confirmation du succès du test avec réception effective de la notification vibrante sur iPhone, et vérification de l'entrée créée dans Notion.
- Transition vers le déclenchement de la réponse email automatique, l'objectif étant de tout automatiser à partir de Notion directement.
- Démonstration de création d'un nouveau scénario Make avec Notion comme déclencheur, via le module watch database items.
- Configuration du module de watch sur la base de données support, avant ajout d'un module Gmail pour l'envoi de l'email de réponse.
- Configuration de l'adresse email destinataire récupérée depuis les données Notion, avant mise en place d'un filtre de déclenchement.
- Configuration d'un filtre déclenchant l'envoi uniquement si la propriété envoyer est cochée (égale true) dans Notion.
- Configuration de l'email de réponse : adresse dynamique, sujet fixe et début de rédaction du contenu de l'email automatique.
- Introduction de la possibilité d'utiliser des balises HTML pour la mise en forme de l'email, via un éditeur HTML dédié simple d'utilisation.
- Rédaction du contenu de l'email avec insertion dynamique de la question posée par le client au sein du message de réponse.
- Ajustement de la formulation pour un ton plus naturel malgré l'aspect robotisé assumé, l'objectif restant le gain de temps global.
- Finalisation du template d'email avec signature personnalisée, une structure simple copiable directement pour d'autres usages.
- Ajustement humoristique de la formulation type de l'email pour ne pas exagérer sur le côté systématique, avant finalisation du template.
- Ajout de la signature personnelle au template, avant retour dans Make pour insérer la réponse dynamique dans le contenu de l'email.
- Suggestion d'ajouter un paragraphe supplémentaire avec un lien URL de fichier, pour enrichir l'email de réponse si nécessaire.
- Réflexion sur la nécessité d'ajouter une condition pour gérer les cas où le fichier serait vide, simplification retenue pour l'exemple pédagogique.
- Sauvegarde de la configuration finale et test de la question soumise avec rédaction directe de la réponse dans Notion.
- Confirmation du succès complet du processus : exécution du scénario envoyant effectivement l'email de réponse automatique au destinataire.
- Bilan du gain de temps obtenu (deux clics au lieu de la gestion manuelle complète des emails), avec piste d'amélioration future pour lier automatiquement le lien de l'email.

## Concepts cles
- introduction à la construction d'un chatbot de support client automatisé
- présentation de Tally (formulaire chatbot, transparence non sponsorisée)
- précision : le plan gratuit de Tally est largement suffisant
- démonstration de la création d'un formulaire de contact au format chatbot
- présentation de l'intégration Tally-Make côté Make
- démonstration de configuration d'un scénario Make avec l'action Tally
- configuration du module watch webhooks blocks event avec clé API Tally
- sélection du formulaire contact et précision de traitement des non-clients
- récupération du bloc ID et sauvegarde de la configuration Make
- configuration du lien Notion via create database items
- configuration des propriétés de la base support Notion (email, created time)
- ajout du champ réponse et réflexion sur la gestion des réponses vidéo
- configuration du statut de ticket (open, closed avec coche)
- ajout d'un indicateur visuel emoji pour les tickets urgents
- configuration d'un filtre pour identifier les demandes déjà traitées
- configuration de la requête de recherche (message, email) dans la base support
- finalisation des champs de base envoyés vers Notion
- introduction de Pushcut pour les notifications iPhone (nouvelles questions)
- démonstration de création d'une notification Pushcut dédiée au support
- explication du choix de sons distinctifs pour les notifications importantes
- configuration du device cible (iPhone) parmi plusieurs appareils possibles
- configuration des paramètres avancés avec idée d'inclure l'URL Notion
- configuration dynamique du titre et texte de notification (email, message)
- sauvegarde et lancement d'un premier test avec question réelle
- saisie en direct d'une question test (paiement en plusieurs fois)
- poursuite de la saisie de la question test
- soumission du formulaire et débogage d'un souci de données manquantes
- correction du problème en réajustant les noms de groupes de données
- second test avec marqueur distinctif pour valider le bon traitement de la donnée
- confirmation du succès du test avec notification reçue et entrée Notion vérifiée
- transition vers le déclenchement automatique de la réponse email depuis Notion
- démonstration de création d'un scénario Make déclenché par Notion
- configuration du watch sur la base support et ajout du module Gmail
- configuration de l'adresse email destinataire depuis Notion
- configuration du filtre déclenchant l'envoi si la propriété envoyer est cochée
- configuration de l'email de réponse (adresse dynamique, sujet fixe)
- introduction des balises HTML pour la mise en forme via un éditeur dédié
- rédaction de l'email avec insertion dynamique de la question du client
- ajustement de la formulation pour un ton plus naturel malgré l'aspect robotisé
- finalisation du template d'email avec signature personnalisée copiable
- ajustement humoristique de la formulation type de l'email
- ajout de la signature personnelle et insertion de la réponse dynamique
- suggestion d'ajout d'un paragraphe avec lien URL de fichier
- réflexion sur la gestion conditionnelle des cas de fichier vide
- sauvegarde de la configuration finale et test avec rédaction dans Notion
- confirmation du succès complet du processus d'envoi automatique
- bilan du gain de temps (deux clics) et piste d'amélioration future

## Outils mentionnes
- Tally
- Make
- Notion
- Pushcut
- WhatsApp
- Instagram
- Gmail

## Tips techniques
- Utiliser un indicateur visuel simple (emoji) pour signaler l'urgence d'un ticket support, facilitant le repérage rapide dans la base de données
- Configurer des sons de notification distinctifs pour les alertes vraiment importantes, afin de les différencier immédiatement des notifications classiques de réseaux sociaux
- Vérifier et aligner systématiquement les noms de champs entre les différentes plateformes connectées (Make, Pushcut), une source fréquente de bug silencieux
- Ajouter un marqueur distinctif temporaire dans les données de test, pour vérifier avec certitude que c'est bien la nouvelle donnée testée qui est traitée
- Utiliser une propriété booléenne (case à cocher) dans la base de données comme déclencheur explicite de l'envoi automatique, pour garder le contrôle manuel
- Utiliser un éditeur HTML dédié dans l'outil d'automatisation pour formater proprement le contenu d'un email automatique
- Prévoir une condition explicite pour gérer les champs optionnels (fichier vide) dans une automatisation, plutôt que de supposer leur présence systématique

## Cas d'usage reels
- [[]]
