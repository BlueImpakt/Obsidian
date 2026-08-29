---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.17 Split in Batches  Loop over items.txt"
---

# 3.17 Split in Batches / Loop over items

## Resume
- Introduction à la fonction Loop Over Items : elle traite l'information élément par élément individuellement, contrairement au comportement par défaut de N8n qui traite des flows successifs pour l'ensemble des données.
- Cas d'usage de Loop Over Items : utile avec de grands volumes de données pour suivre précisément quels éléments passent ou échouent, ou pour respecter les limites de débit (rate limit) de certaines API.
- Confirmation de l'importance majeure de ce module dans la construction de workflows avancés, un élément que l'utilisateur va utiliser très fréquemment dans ses automatisations futures.
- Préparation d'une démonstration avec une deuxième feuille de calcul similaire, pour illustrer concrètement la différence de comportement avec et sans l'usage de Loop Over Items.
- Renommage de la feuille de test (Sheet2) et augmentation significative du volume de données scrapées (500 au lieu de 5) pour bien visualiser l'intérêt du traitement en boucle sur un grand volume.
- Reprise du processus de scraping Google Maps déjà vu (déclenchement, attente, récupération du dataset), avec ajustement de la requête pour ce nouveau volume de test plus important.
- Conseil méthodologique important : toujours tester d'abord avec 1 élément avant de monter graduellement, plutôt que de lancer directement 500 éléments qui consommeraient inutilement beaucoup de crédits en cas d'erreur.
- Observation du temps de traitement plus long pour un volume important : les valeurs mettent du temps à être retournées car le système doit traiter l'ensemble des données avant de répondre.
- Débogage d'un problème de référence de champ (« title » non trouvé via Google Sheets), avec rappel de la bonne pratique : toujours utiliser les marqueurs de node spécifiques plutôt que la référence JSON générique.
- Poursuite du débogage en explorant le schéma de la requête HTTP originale pour retrouver le bon nom de champ (C-Title finalement identifié), illustrant l'importance de vérifier le schéma source.
- Configuration successive des champs à récupérer (rue, code postal, ville, score total, URL, téléphone) depuis le dataset scrapé, avec suggestion d'utiliser ToString pour certains champs sensibles au formatage.
- Lancement d'un test à plus grande échelle (250 recherches générant 500 éléments), avec observation en direct du crawling en cours pour comprendre le comportement du système à cette échelle.
- Explication du fonctionnement de Loop Over Items : par défaut le flow continue vers « Done », mais il faut spécifiquement configurer la branche « Loop » (marquée « Replace Me ») pour créer la boucle de traitement.
- Recommandation cruciale de sécurité : toujours tester avec Execute Once avant de lancer une boucle complète, car sinon l'opération se répète pour tous les 500 éléments, un risque de traitement incontrôlable.
- Démonstration d'Execute Once pour charger les valeurs de Loop Over Items et pouvoir explorer un élément spécifique de la boucle sans déclencher le traitement complet.
- Explication du mécanisme de séparation des éléments dans la boucle : sur 500 éléments, 499 restent en liste d'attente pendant qu'un seul est traité, le suivant ne démarrant qu'une fois le précédent terminé (traitement séquentiel).
- Démonstration de la bonne pratique de référence via item.json dans le contexte de Loop Over Items, pour récupérer successivement les différents champs (titre, rue, code postal, ville, score, site web).
- Application de ReplaceAll pour nettoyer le format du numéro de téléphone. Introduction de l'ajout d'un filtre conditionnel dans la boucle pour ne traiter que les éléments répondant à certains critères.
- Configuration du filtre dans la boucle avec le critère « Total Score supérieur à 4 », illustrant comment appliquer une condition de qualité pour ne conserver que les meilleurs éléments traités.
- Validation du filtre : l'élément « kept » (conservé) confirme le passage du critère, avec transition vers la création d'une tâche à partir des éléments filtrés et conservés dans la boucle.
- Ajout d'une notification finale une fois le traitement terminé : création d'un brouillon Gmail avec un message confirmant que le processus est terminé, illustrant la clôture propre d'un workflow en boucle.
- Test complet du workflow en réexécutant l'ensemble : le processus va vite car il réutilise les éléments déjà scrapés précédemment, illustrant l'efficacité de la boucle sur des données déjà en cache.
- Anecdote personnelle sur la possibilité de reconnaître un restaurant dans les résultats scrapés, puis identification d'un problème : seulement 13 éléments sur 500 sont passés avec succès, nécessitant investigation.
- Résolution du problème via les options Always Output Data et Continue Workflow, permettant de gérer les cas où l'étape précédente n'a pas envoyé de données, sans bloquer l'ensemble du traitement en boucle.
- Confirmation que la boucle continue correctement au-delà de 13 éléments cette fois (grâce à la correction précédente) jusqu'à traiter l'intégralité des 500 éléments prévus.
- Identification d'une erreur de trop de requêtes simultanées, illustrant un cas d'usage supplémentaire de Loop Over Items : éviter de saturer une API en envoyant 5000 requêtes d'un coup, avec risque d'échec partiel.
- Explication cruciale sur la logique de boucle : un élément « faux » ne doit pas interrompre le flow entier, sinon le premier élément non conforme arrêterait tout le traitement des éléments suivants dans la boucle.

## Concepts cles
- introduction à Loop Over Items (traitement individuel vs flow global)
- cas d'usage de Loop Over Items (suivi granulaire, respect des rate limits)
- importance majeure de Loop Over Items pour les workflows avancés
- préparation d'une démonstration comparative avec deuxième feuille
- augmentation du volume de test (500 éléments) pour illustrer Loop Over Items
- reprise du processus de scraping pour un volume plus important
- méthode de test progressif (1 puis montée graduelle)
- temps de traitement plus long avec un volume important de données
- rappel de bonne pratique : marqueurs de node spécifiques plutôt que JSON générique
- exploration du schéma HTTP Request pour retrouver un champ correct
- configuration successive de multiples champs depuis le dataset
- test à grande échelle en direct (250 recherches, 500 éléments)
- configuration de la branche Loop (vs Done) dans Loop Over Items
- recommandation critique : Execute Once avant de lancer une boucle complète
- usage d'Execute Once pour explorer un élément spécifique de la boucle
- mécanisme de traitement séquentiel un par un dans la boucle (liste d'attente)
- bonne pratique item.json pour récupérer les champs dans la boucle
- nettoyage de téléphone via ReplaceAll et introduction de filtre conditionnel dans la boucle
- filtre de qualité dans la boucle (Total Score > 4)
- validation du filtre et transition vers création de tâche
- notification finale par email à la fin du traitement en boucle
- test complet réutilisant les données déjà scrapées (rapidité)
- identification d'un problème de traitement partiel (13/500 seulement)
- résolution via Always Output Data et Continue Workflow pour gérer les données manquantes
- confirmation du bon fonctionnement de la boucle complète (500 éléments)
- cas d'usage supplémentaire de Loop Over Items (éviter la saturation d'API)
- logique cruciale : un élément faux ne doit pas interrompre toute la boucle

## Outils mentionnes
- n8n
- Google Sheets
- Apify
- Gmail

## Tips techniques
- Toujours tester une automatisation avec 1 seul élément avant de monter progressivement en volume, pour éviter de gaspiller des crédits sur une erreur
- Toujours utiliser Execute Once pour tester une boucle avant de la lancer sur l'ensemble des éléments, sous peine de traitement incontrôlable
- Activer Always Output Data et Continue Workflow pour qu'une boucle ne s'arrête pas complètement en cas de données manquantes sur un élément
- S'assurer qu'un élément ne remplissant pas un critère ne bloque pas l'intégralité du traitement des éléments suivants dans une boucle

## Cas d'usage reels
- [[]]
