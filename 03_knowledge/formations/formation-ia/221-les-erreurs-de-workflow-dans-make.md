---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.21 Les erreurs de workflow dans make.txt"
---

# 2.21 Les erreurs de workflow dans make

## Resume
- Introduction à la gestion des erreurs sur Make, illustrée par un scénario existant intégrant des error handlers (gestionnaires d'erreurs), des modules dédiés à la prise en compte et la résolution automatique des erreurs.
- Exemple concret d'erreur récurrente : un module WebinarJam générant fréquemment des erreurs liées au rate limit de l'API (limite du nombre de requêtes autorisées par minute/seconde), un problème courant avec les outils marketing anciens.
- Autres causes d'erreurs courantes : envoi de trop de données simultanément, ou service tiers en panne (down). Astuce pratique : consulter les pages status.[nomdoutil].com (exemple ClickUp) pour vérifier si un incident est en cours.
- Précision sur la rareté des pannes de service (une à deux fois par an maximum), mais importance de savoir gérer ce cas. Introduction du concept d'Error Handler avec un focus sur le plus utilisé : le Module Break.
- Explication du paramétrage du Module Break : configurer 5 tentatives espacées de 15 minutes chacune (soit 1h15 de filet de sécurité), une durée jugée suffisante car les pannes d'API dépassent rarement cette fenêtre.
- Confirmation du fonctionnement de Break : il arrête l'exécution et la relance automatiquement après le délai défini, pour le nombre de tentatives configuré, un mécanisme de retry automatique paramétrable.
- Présentation de l'Error Handler Resume : permet de renvoyer manuellement des données spécifiques en cas de bug ciblé (exemple : un nom vide qui bloque le processus), en corrigeant directement l'élément problématique.
- Démonstration d'un fallback manuel : en cas d'erreur, l'utilisateur peut ajouter manuellement les valeurs nécessaires (exemple : un lien de secours fiable comme teio.link.live) pour permettre au scénario de continuer.

## Concepts cles
- introduction aux error handlers pour la gestion d'erreurs
- exemple concret de rate limit API (WebinarJam)
- astuce : consulter les pages status.[outil].com en cas de panne suspectée
- rareté des pannes mais nécessité de gestion
- introduction du Module Break
- configuration recommandée du Module Break (5 tentatives, 15min d'intervalle)
- mécanisme de retry automatique via Break
- Error Handler Resume pour corriger manuellement une donnée bloquante
- fallback manuel avec valeur de secours prédéfinie

## Outils mentionnes
- Make
- WebinarJam
- ClickUp

## Tips techniques
- Consulter la page status.[nom_outil].com pour vérifier si une panne de service tiers explique une erreur d'automatisation
- Configurer le Module Break avec 5 tentatives espacées de 15 minutes (1h15 total) comme filet de sécurité standard contre les pannes temporaires
- Prévoir une valeur de secours fiable (ex: un lien alternatif) à utiliser manuellement en cas d'erreur via un fallback

## Cas d'usage reels
- [[]]
