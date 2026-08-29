---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.16 Le module HTTP dans N8N  Wait.txt"
---

# 3.16 Le module HTTP dans N8N / Wait

## Resume
- Introduction à un cas d'usage combinant les modules HTTP et Wait, avec présentation d'un nouvel outil (détaillé plus tard) qui servira à illustrer concrètement l'ensemble des modules à venir.
- Clarification juridique importante sur le scraping : légal car portant sur des données publiquement accessibles, qu'elles soient collectées manuellement (10 heures) ou automatiquement, la légalité restant identique.
- Mise en garde importante sur le scraping international : ne pas copier aveuglément les pratiques américaines (comme l'usage d'Apollo), car les règles juridiques diffèrent selon les pays, notamment pour le scraping de leads.
- Exemple concret de données scrapables légalement : liste de restaurants parisiens avec numéros de téléphone professionnels, des données publiques et non personnelles donc autorisées au scraping.
- Présentation d'Apify identifiant automatiquement des listes répétées pour les catégoriser en tableaux structurés : horaires, adresses, notes, nombre d'avis, prix moyen, type de restaurant, images, tags.
- Présentation d'un outil complémentaire fonctionnant hors ligne (probablement une extension), permettant de rechercher par mot-clé ou localisation sans connexion active au moment de l'utilisation.
- Panorama des cas d'usage sans limite du scraping : identifier les meilleurs contenus TikTok/YouTube/Instagram, trouver des restaurants à contacter, ou analyser les meilleurs produits Amazon.
- Présentation d'un autre outil de scraping spécialisé (Idealista, pour le marché immobilier au Portugal/Espagne) à 19$/mois, avec préférence de l'auteur pour un paiement au résultat ou à l'usage plutôt qu'un abonnement fixe.
- Clarification sur les données personnelles vs professionnelles dans le contexte légal du scraping : si les données ne sont pas liées à un individu spécifique, le scraping reste autorisé, avec renvoi vers un article de référence.
- Démonstration pratique du scraping en direct via Google Maps, récupérant 5 restaurants avec leurs informations (Inca Paisa, Chili Flushing, Moon Chinese Restaurant, etc.).
- Panorama des données récupérées : numéro de téléphone, réseaux sociaux, notes moyennes de chaque restaurant, avec possibilité d'enrichissement supplémentaire des leads via des informations liées.
- Lancement effectif du scraping de 5 restaurants, introduisant le cas d'usage concret justifiant l'utilité du module Wait, dont la nécessité sera expliquée dans la suite du raisonnement.
- Explication clé du besoin du module Wait : la réponse de lancement du scraping est immédiate mais les données réelles ne sont pas encore disponibles, elles doivent être récupérées après un délai de traitement.
- Présentation de l'alternative : récupérer directement le dataset via son identifiant unique, en explorant l'endpoint Dataset Items de l'API Apify pour accéder aux résultats du scraping.
- Décomposition de la structure d'URL pour accéder aux éléments du dataset : base de l'URL, endpoint « dataset », puis « item » pour cibler les éléments spécifiques du jeu de données scrapé.
- Présentation de l'authentification par token directement intégré dans l'URL (paramètre token=), et perspective d'automatiser la récupération du dataset ID généré dynamiquement à l'étape précédente.
- Confirmation du cas d'usage idéal du module Wait : attendre que le scraping se génère avant d'aller chercher dynamiquement les résultats, car ceux-ci ne sont jamais renvoyés instantanément.
- Configuration des paramètres de recherche du scraper : langue des résultats (français), localisation ciblée (Paris, France), première étape de personnalisation de la requête de scraping.
- Suite de la configuration : nombre d'endroits à scraper (5), option de récupération d'images (désactivée), et option d'enrichissement des leads trouvés (désactivée pour cet exemple simple).
- Configuration finale des mots-clés de recherche multiples (restaurant, hôtel, etc.) sous forme d'Array, permettant de scraper plusieurs types d'établissements en une seule requête paramétrée.
- Confirmation que le scraping s'est terminé (délai d'attente respecté), permettant de récupérer avec succès toutes les données ciblées grâce au dataset ID transmis dynamiquement.
- Recommandation de « pinner » (épingler) les données pour éviter de devoir réexécuter le workflow à chaque test, une fonctionnalité qui sera approfondie plus tard. Préparation de la création d'un spreadsheet.
- Configuration de la connexion Google Sheets pour enregistrer les données scrapées : sélection de l'identifiant unique du document et association des colonnes correspondant aux champs récupérés.
- Exemple concret de données enregistrées : ville (Vincennes), note moyenne (Total Score), URL (Hôtel Saint-Louis), téléphone, illustrant le résultat final structuré dans la feuille de calcul.
- Poursuite du test complet du workflow : le scraping se termine avec 10 résultats obtenus, illustrant le fonctionnement de bout en bout de l'automatisation avec un volume de données plus important.
- Récupération réussie des 10 éléments du dataset, avec identification d'un souci de formatage sur le champ téléphone nécessitant une conversion explicite au format texte pour un affichage correct.

## Concepts cles
- introduction à un cas d'usage réel combinant HTTP et Wait
- clarification juridique : le scraping de données publiques est légal
- mise en garde sur les différences juridiques internationales du scraping (US vs autres pays)
- exemple concret de données légalement scrapables (restaurants, contacts pro)
- catégorisation automatique de données scrapées par Apify
- outil de scraping fonctionnant hors ligne
- panorama des cas d'usage variés du scraping (réseaux sociaux, e-commerce)
- outil Idealista (immobilier Portugal/Espagne) et préférence pour tarification à l'usage
- distinction données personnelles vs professionnelles pour le scraping légal
- démonstration pratique de scraping via Google Maps
- richesse des données scrapées (contact, réseaux sociaux, notes)
- lancement du scraping justifiant l'usage du module Wait
- nécessité du module Wait : réponse immédiate mais données pas encore prêtes
- récupération directe via l'identifiant de dataset (endpoint Dataset Items)
- structure d'URL pour accéder aux éléments d'un dataset Apify
- authentification par token dans l'URL et récupération dynamique du dataset ID
- cas d'usage confirmé du module Wait pour le scraping
- configuration des paramètres de langue et localisation du scraper
- configuration du nombre d'endroits et options d'enrichissement
- configuration de mots-clés multiples via Array
- validation du succès de récupération après attente du scraping
- recommandation d'épingler (pin) les données pour éviter la réexécution
- configuration de la connexion Google Sheets pour les données scrapées
- exemple concret de données enregistrées dans Google Sheets
- test complet du workflow avec 10 résultats
- résolution d'un problème de formatage du champ téléphone (conversion en texte)

## Outils mentionnes
- n8n
- Apollo
- Apify
- Idealista
- Google Maps
- Google Sheets

## Tips techniques
- Ne pas copier les pratiques de scraping américaines sans vérifier les règles juridiques applicables dans son propre pays
- Privilégier des outils de scraping facturés au résultat/usage plutôt qu'à l'abonnement fixe quand c'est possible
- Comprendre qu'une réponse de lancement de scraping immédiate ne signifie pas que les données sont déjà disponibles : prévoir un délai
- Épingler (pin) les données de test pour éviter de devoir relancer un scraping coûteux à chaque test de workflow
- Convertir explicitement en format texte les numéros de téléphone récupérés pour éviter les problèmes de formatage automatique

## Cas d'usage reels
- [[]]
