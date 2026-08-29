---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.05 Création du 1er scénario dans Make.txt"
---

# 2.05 Création du 1er scénario dans Make

## Resume
- Introduction à la construction du premier scénario complet sur Make, composé d'un déclencheur et d'une action simples, en partant d'un exemple concret de formulaire.
- Exemple concret d'inscription à une académie via formulaire simple (prénom, nom, option choisie), tous les champs étant obligatoires, illustrant le déclenchement d'une action dès validation du formulaire.
- Recommandation pédagogique : utiliser des outils déjà connus pour faciliter l'apprentissage. Démonstration de la sélection du Form ID via un connecteur, avec deux méthodes de sélection possibles.
- Bonne pratique de test : pour les déclencheurs non-webhook, exécuter d'abord l'action réelle (remplir le formulaire) avant de tester la réception via Run Once, plutôt que de tester dans le vide sans donnée disponible.
- Rappel pédagogique reliant la structure de réponse reçue à la notion de JSON précédemment enseignée : un objet peut contenir un autre objet, potentiellement avec des arrays, cette structure imbriquée se retrouvant concrètement dans les données du formulaire.
- Analyse détaillée de la structure de données reçue : trois étapes/réponses différentes visibles, chacune étant un objet contenant un ID de question et une collection sous forme d'Array pour les réponses possibles.
- Identification précise des données pertinentes dans la structure JSON du bundle : parmi tous les champs disponibles (Answer, Text Answer, question ID), seules les valeurs réelles souhaitées (« Jean », « Dupont », « intelligence artificielle ») intéressent l'utilisateur pour construire l'action suivante.
- Démonstration de la connexion à Google Sheets et de la sélection du document cible, l'auteur recommandant de sélectionner par ID plutôt que par nom pour plus de simplicité et de fiabilité.
- Explication de la double nature de Google Sheets : à la fois tableur classique navigable cellule par cellule, et base de données où chaque ligne peut être considérée comme un enregistrement structuré.
- Confirmation de la terminologie : dans une logique programmatique d'automatisation, une ligne de Google Sheets est appelée un enregistrement (record). Le scénario est configuré pour créer automatiquement un nouvel enregistrement à chaque inscription.
- Explication du choix précis de la valeur la plus indentée dans la structure de données plutôt qu'une valeur générique : cela permet d'isoler exactement le mot de la réponse recherchée, évitant toute ambiguïté entre valeurs similaires.

## Concepts cles
- premier scénario simple (déclencheur + action)
- exemple concret : formulaire d'inscription académie (3 champs obligatoires)
- recommandation d'utiliser des outils connus pour apprendre
- sélection du Form ID via connecteur
- bonne pratique de test : réaliser l'action avant de tester le déclencheur
- structure JSON imbriquée retrouvée concrètement dans une réponse de formulaire
- analyse détaillée de la structure objet/Array d'une réponse de formulaire
- identification des valeurs pertinentes dans une structure JSON complexe
- sélection de document par ID plutôt que par nom (recommandation)
- double nature de Google Sheets (tableur et base de données)
- terminologie 'record' pour une ligne en logique programmatique
- choix de la valeur la plus indentée pour isoler précisément une donnée

## Outils mentionnes
- Make
- Google Sheets

## Tips techniques
- Pratiquer avec des outils qu'on connaît déjà pour faciliter l'apprentissage d'une nouvelle plateforme d'automatisation
- Réaliser l'action déclenchante réelle avant de lancer Run Once pour les déclencheurs non-webhook, sinon le test échoue faute de donnée
- Sélectionner un document Google Sheets par son ID plutôt que par son nom pour plus de fiabilité
- Choisir toujours la valeur la plus indentée/spécifique dans une structure de données imbriquée pour isoler précisément l'information recherchée

## Cas d'usage reels
- [[]]
