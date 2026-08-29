---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.1 Fonctions math dans N8N.txt"
---

# 3.1 Fonctions math dans N8N

## Resume
- Introduction aux fonctions mathématiques sur N8n : rappel que sans guillemets, une valeur texte n'est pas comprise, tandis que les nombres se manipulent différemment via des fonctions dédiées.
- Présentation d'un hack important pour N8n et de la fonction IsEven (chiffre pair ou impair) : retourne vrai pour un nombre pair (ex: 12), faux pour un nombre impair.
- Présentation de la fonction Absolute (valeur absolue), puis introduction de Ceiling et Floor : arrondi supérieur ou inférieur d'un chiffre décimal, avec exemples chiffrés concrets.
- Présentation du formatage numérique par défaut (style américain) et personnalisable via les paramètres de locale, avec accès à une liste de codes de langue/pays pour adapter le formatage régional.
- Exploration des codes de locale disponibles (allemand, français, portugais brésilien) : la langue est notée en minuscule, le pays en majuscule (exemple : FR-CA pour le Canada francophone).
- Démonstration comparative de formatage régional des nombres : FR-FR utilise l'espace comme séparateur de milliers, le portugais brésilien utilise la virgule, illustrant les différences culturelles de formatage.
- Présentation d'IsInteger : identifie si un nombre est entier (sans décimale), avec exemple montrant que retirer une décimale valide (« ,1 ») rend la valeur reconnue comme entière. Rappel de la fonction Round pour l'arrondi standard.
- Précision sur le paramètre de précision de Round : définir 2, 3 ou 4 pour obtenir respectivement 2, 3 ou 4 décimales dans le résultat arrondi, une flexibilité utile selon le niveau de précision requis.
- Présentation du format ISO 8601 et du Unix Timestamp (déjà vu dans le module Make), permettant de convertir des nombres en dates lisibles via un convertisseur dédié.
- Présentation de ToDateAndTime et astuce de conversion (multiplier par 1000 plutôt que rajouter trois zéros), puis introduction de ToLocalString, transformant une valeur numérique en format texte régional.
- Conclusion des fonctions numériques avec ToString (conversion en texte manipulable via les fonctions de string vues précédemment), la section ayant été plus rapide car comportant moins de fonctions au total.

## Concepts cles
- introduction aux fonctions mathématiques N8n (distinction string/nombre)
- hack important N8n et fonction IsEven
- fonctions Absolute, Ceiling et Floor pour les décimaux
- formatage numérique via locales (défaut américain, personnalisable)
- codification des locales (langue minuscule, pays majuscule)
- comparaison de formatage numérique régional (FR vs BR)
- fonction IsInteger et rappel de Round
- paramètre de précision décimale de Round (2, 3, 4 décimales)
- format ISO 8601 et Unix Timestamp (conversion nombre-date)
- ToDateAndTime et ToLocalString (astuce de multiplication par 1000)
- conclusion des fonctions numériques avec ToString

## Outils mentionnes
- n8n

## Tips techniques
- Multiplier par 1000 plutôt que d'ajouter manuellement trois zéros pour convertir un timestamp Unix en millisecondes

## Cas d'usage reels
- [[]]
