---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.03 Le node Sentiment Analysis, Text Classifier.txt"
---

# 4.03 Le node Sentiment Analysis, Text Classifier

## Resume
- Introduction au module Text Classifier et Sentiment Analysis, avec démonstration de configuration du nœud Sentiment Analysis à partir d'un chat de test, en définissant le texte à analyser.
- Démonstration de connexion du texte analysé provenant du nœud précédent (message du chat), illustrant comment chaîner les données entre nœuds successifs.
- Configuration de branchements conditionnels selon le sentiment détecté (positif → classification, négatif → redirection vers un autre agent IA), une logique de routage automatisé.
- Test pratique de détection de sarcasme : un message ironique sur des livreurs en retard est correctement identifié comme sarcastique par l'analyse de sentiment, démontrant la finesse de détection.
- Exemple de réponse positive générée en cas de sentiment détecté favorable, illustrant l'usage du routage conditionnel pour adapter la réponse selon le ton du message reçu.
- Explication de la granularité offerte par l'analyse de sentiment : elle porte sur la manière dont un message est dit plutôt que sur son contenu brut, avec accès au prompt système sous-jacent modifiable.
- Présentation des métriques additionnelles disponibles en sortie du Sentiment Analysis avancé : force (strength) et confiance (confidence), toutes deux notées sur une échelle de 0 à 1.
- Démonstration de définition de plusieurs catégories de classification (facturation, support, général) pour le Text Classifier, avec la catégorie « reste » servant de fourre-tout.
- Test pratique du Text Classifier configuré avec les catégories support client, facturation, aide générale, en déclenchant une demande type pour observer le résultat de classification.
- Explication de l'importance de bien configurer à la fois le titre et la description détaillée de chaque catégorie du Text Classifier, la description précise étant déterminante pour la bonne classification.
- Présentation du format JSON de réponse du Text Classifier, avec retour sur les options oubliées de Sentiment Analysis (Sentiment Categories, Include Detailed Results).

## Concepts cles
- introduction et configuration du nœud Sentiment Analysis via un chat de test
- démonstration de chaînage de données entre nœuds successifs (chat vers analyse)
- configuration de branchements conditionnels selon le sentiment détecté
- test pratique de détection de sarcasme réussie
- exemple de réponse adaptée au sentiment positif détecté
- granularité de l'analyse de sentiment (comment le message est dit vs contenu) et prompt système modifiable
- métriques additionnelles du Sentiment Analysis : force et confiance (échelle 0-1)
- démonstration de définition de catégories multiples pour le Text Classifier
- test pratique du Text Classifier avec catégories multiples
- importance de la description détaillée des catégories pour une classification précise
- format JSON de réponse et options complémentaires de Sentiment Analysis

## Outils mentionnes
- n8n

## Tips techniques
- Toujours rédiger une description précise et détaillée pour chaque catégorie du Text Classifier, pas seulement un titre court, pour maximiser la précision

## Cas d'usage reels
- [[]]
