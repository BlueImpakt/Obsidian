---
tags: [formation, millenium]
module: Formation Productivite
section: "Aller plus loin"
source_transcript: "28. Se creer un Assistant Business.txt"
---

# 28. Se creer un Assistant Business

## Resume
- Introduction à la création d'un assistant personnel business, complémentaire à l'automatisation du service client vue précédemment, focalisé sur les alertes récurrentes.
- Rappel de Pushcut pour les notifications iOS, avec mention de l'application mobile Make comme alternative multi-plateforme similaire.
- Présentation de la création de multiples notifications dans Pushcut, chacune associée à une webhook URL dédiée.
- Explication de l'ajout de textes et titres dynamiques déclenchant l'action de notification, utilisé principalement pour les alertes de vente.
- Introduction de LogSnag comme alternative payante (quelques euros) pour ceux souhaitant aller plus loin dans l'analyse au-delà de la simple alerte.
- Présentation de LogSnag comme véritable centre de notification dédié au business, capable d'afficher une suite d'événements (facturation, etc.).
- Nuance que LogSnag est surtout utile en cas de volume important d'événements, offrant une vue d'ensemble simple sur l'activité business.
- Présentation des fonctionnalités de graphiques (charts) et d'insights disponibles dans LogSnag pour analyser l'activité.
- Présentation des options de filtrage par email et des KPI disponibles, avec application mobile dédiée pour les notifications LogSnag.
- Démonstration de l'accès à l'application LogSnag sur Mac avec masquage des données de confidentialité des utilisateurs inscrits.
- Présentation des multiples points d'entrée de la newsletter suivis (lead magnet productivité, toolbox, édito), chacun tracé séparément.
- Confirmation de l'organisation en channels distincts, avec projet d'ajouter à terme les ventes et le service client comme channels supplémentaires.
- Avantage clé de LogSnag par rapport à Pushcut : la possibilité de créer des graphiques (charts) d'analyse visuelle des données.
- Exemple concret de données chiffrées suivies au fil des jours : 14 inscrits un jour, 8 le lendemain, 2 le jour même, ventilées par channel.
- Transition vers l'explication technique de l'envoi des données à LogSnag, nécessitant un point d'origine centralisé (souvent un webhook Make).
- Démonstration de création d'un webhook Make à insérer dans le formulaire, première étape de la chaîne de collecte de données.
- Configuration de l'insertion de l'adresse webhook copiée dans le formulaire, avant retour dans Make pour ajouter le module suivant.
- Ajout du module LogSnag dans Make (extension communautaire non officielle), avec configuration du nom du projet correspondant à l'organisation.
- Configuration du type d'événement lié au webhook d'un formulaire spécifique (formation Flutter Flow gratuite), avec test de soumission en direct.
- Poursuite du test de soumission du formulaire pour valider la réception correcte des données dans le webhook Make.
- Confirmation de la réception du webhook après un nouveau test, avec réajustement du module pour accélérer le processus de configuration.
- Analyse du payload reçu contenant email et titre du formulaire, avec configuration du champ sign up en dur pour catégoriser l'événement.
- Configuration du module create event LogSnag avec mapping du projet, channel newsletter, et type d'événement précis (formation Flutter Flow gratuite).
- Finalisation de la configuration avec description (email), icône emoji automatiquement récupérée, et activation de la notification associée.
- Confirmation du succès du test : l'événement newsletter apparaît bien dans LogSnag avec l'adresse email correctement associée.
- Conclusion sur l'intérêt de LogSnag comme centre de notification avec graphiques d'analyse business, avec présentation des deux options possibles.
- Distinction finale entre Pushcut (notifications simples sans analyse, 15€/an) et LogSnag (analyse approfondie), à choisir selon le besoin.
- Démonstration de l'alternative via l'application mobile Make (Send a Push Notification) équivalente à Pushcut, nécessitant l'application installée.

## Concepts cles
- introduction à l'assistant personnel business (alertes récurrentes)
- rappel de Pushcut (iOS) et alternative Make mobile multi-plateforme
- présentation de la création de multiples notifications avec webhook URL
- explication de l'ajout de textes dynamiques pour les alertes de vente
- introduction de LogSnag comme alternative payante pour l'analyse avancée
- présentation de LogSnag comme centre de notification dédié au business
- nuance : LogSnag utile surtout pour un volume important d'événements
- présentation des fonctionnalités de charts et insights de LogSnag
- présentation du filtrage par email et des KPI (application mobile)
- démonstration de l'application LogSnag sur Mac (confidentialité masquée)
- présentation des multiples points d'entrée de newsletter suivis séparément
- confirmation de l'organisation en channels distincts (extension future ventes, support)
- avantage clé de LogSnag vs Pushcut : graphiques d'analyse visuelle
- exemple concret de données chiffrées suivies quotidiennement par channel
- transition vers l'explication technique d'envoi des données via webhook
- démonstration de création d'un webhook Make pour le formulaire
- configuration de l'insertion de l'adresse webhook dans le formulaire
- ajout du module communautaire LogSnag dans Make
- configuration du type d'événement lié au webhook d'un formulaire spécifique
- poursuite du test de soumission validant la réception du webhook
- confirmation de la réception du webhook après nouveau test
- analyse du payload reçu et configuration du champ sign up en dur
- configuration du module create event LogSnag avec mapping précis
- finalisation avec description email, icône emoji et notification activée
- confirmation du succès du test avec événement newsletter visible dans LogSnag
- conclusion sur LogSnag comme centre de notification avec graphiques
- distinction finale Pushcut (15€/an, simple) vs LogSnag (analyse approfondie)
- démonstration de l'alternative Make mobile (Send a Push Notification)

## Outils mentionnes
- Pushcut
- Make
- LogSnag

## Tips techniques
- Tracer séparément chaque point d'entrée d'acquisition (lead magnet, toolbox, édito) pour identifier précisément l'origine de chaque conversion
- Associer une icône emoji automatiquement récupérée à chaque type d'événement LogSnag, pour une identification visuelle rapide dans le flux

## Cas d'usage reels
- [[]]
