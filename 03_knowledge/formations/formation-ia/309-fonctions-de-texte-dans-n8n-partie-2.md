---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.09 Fonctions de texte dans N8N • Partie 2.txt"
---

# 3.09 Fonctions de texte dans N8N • Partie 2

## Resume
- Introduction de la partie 2 des fonctions texte, divisée pour éviter une vidéo trop longue (40 minutes). Reprise avec un texte simple (« Bonjour ») pour continuer l'exploration de la liste des fonctions disponibles.
- Explication du formatage Markdown : structure des titres via des dièses (# pour H1, le plus gros titre), un espace suivi du texte, permettant un formatage automatique de la hiérarchie du contenu.
- Présentation d'éléments Markdown avancés : tables, blocs de code (fence code block), notes de pied de page (footnote), et heading ID (identifiants personnalisés pour naviguer directement vers une section précise.
- Démonstration de la fonction RemoveMarkdown : sans elle, les indicateurs de syntaxe (comme les dièses) restent visibles dans le texte final, rendant le contenu parasité par ces symboles techniques.
- Exploration détaillée d'une structure JSON contenant beaucoup d'espaces blancs et de valeurs sans tags identifiés, illustrant la complexité potentielle des données brutes à traiter.
- Démonstration de la fonction Replace avec un seul argument : sans remplaçant défini, elle affiche « undefined » à la place du caractère supprimé, illustrant l'importance de toujours spécifier les deux paramètres.
- Présentation d'une fonction très utile pour les francophones : suppression des accents (exemple « bonne année » devient « bonne annee »), utile quand certaines API ne supportent pas les caractères accentués.
- Démonstration détaillée de la fonction Slice avec indexation précise : retenir les positions 1 et 2 en excluant la position 3, illustrant le fonctionnement du découpage par indices numérotés.
- Poursuite de l'explication de Slice avec un second exemple d'indexation (retirer les deux premiers, garder 3 et 4), illustrant deux façons différentes de calculer les positions incluses/exclues.
- Rappel de la fonction Split (déjà vue) et introduction de Substring, similaire dans son objectif d'extraction d'un fragment de texte à une position donnée, une fonction complémentaire à Slice.
- Confirmation du fonctionnement de Substring et transition vers ToJSONString, l'auteur encourageant à consulter la documentation intégrée disponible pour approfondir chaque fonction.
- Explication de ToJSONString : formate et ajoute les guillemets nécessaires pour qu'une valeur soit prête à être utilisée dans une string, avec démonstration corrective sur un problème d'apostrophe.
- Rappel de Trim et présentation de TrimEnd, qui retire uniquement les espaces blancs en fin de texte, tandis que les espaces au début seraient conservés, illustrant la précision de cette fonction ciblée.
- Confirmation de TrimStart (équivalent en début de texte) et présentation des fonctions URLDecode/URLEncode, déjà vues sur Make, permettant d'encoder ou décoder les caractères spéciaux d'une URL.
- Démonstration détaillée d'IndexOf (position d'un caractère dans une chaîne) avec explication de l'indexation à partir de 0, illustrant précisément comment localiser une lettre spécifique dans un mot.
- Poursuite de la démonstration IndexOf avec plusieurs exemples de position de lettres différentes, précisant que la fonction retourne par défaut la première occurrence trouvée en cas de doublon.
- Introduction de la fonction Match, spécifique car elle permet de travailler avec des expressions régulières (regex), avec renvoi vers un outil externe pour apprendre à composer ces expressions.
- Recommandation pragmatique forte : plutôt que d'apprendre le regex par cœur en 2025-2027, il est bien plus efficace d'utiliser l'IA pour générer les expressions régulières nécessaires directement.
- Démonstration pratique de génération de regex via l'outil Raycast sur Mac : demander « écris le regex pour identifier les mots avec des majuscules » puis insérer directement le résultat généré.
- Correction itérative du regex généré : un problème identifié avec un accent est signalé à l'IA, qui met à jour automatiquement l'expression pour corriger ce cas non pris en compte initialement.
- Analyse du résultat du regex corrigé avec indexation précise des lettres correspondantes, l'auteur encourageant l'expérimentation personnelle avec des textes de test pour bien comprendre le comportement du regex.
- Présentation de la fonction IsDomain, validant si une chaîne est un domaine valide : « https://teio.co » est jugé faux (le préfixe https n'est pas reconnu comme partie du domaine), contrairement au domaine seul.
- Précision technique sur la validation d'URL : un minimum de deux lettres est requis pour être reconnu comme extension de domaine valide, illustrant les règles précises de validation utilisées par la fonction.
- Présentation de la fonction IsEmail : valide qu'une chaîne de caractères correspond à un format d'email correct (exemple : hello@teio.co identifié comme valide), rejetant les formats incorrects.
- Détail des règles de validation IsEmail : retirer le @ ou une lettre invalide fausse l'identification, tandis qu'un format minimal (mot + @ + extension de 2 lettres) est correctement reconnu comme email valide.
- Présentation de la fonction IsNumeric : valide les caractères numériques accompagnés d'opérateurs (+ ou -) et de décimales, une fonction utile pour vérifier la conformité d'une valeur avant traitement mathématique.
- Présentation des fonctions de casse : suppression de toutes les majuscules, SentenceCase (majuscule uniquement sur le premier mot de la phrase), et ToTitleCase (majuscule sur chaque mot important).
- Présentation d'Uppercase (tout en majuscules) et introduction de ParseJSON, permettant d'identifier et transformer une chaîne de texte structurée en véritable objet JSON exploitable.
- Démonstration pratique de ParseJSON : à partir d'une string au format JSON, extraction d'un objet contenant des valeurs spécifiques (nom, prénom), transformant du texte brut en structure de données exploitable.
- Présentation de ToBoolean : transforme une valeur en véritable booléen (true/false réel plutôt qu'une string), avec précision que toute valeur non reconnue est convertie par défaut en true.

## Concepts cles
- poursuite pédagogique de la liste des fonctions texte (partie 2)
- formatage Markdown des titres (dièses pour hiérarchie H1-H6)
- éléments Markdown avancés (tables, code block, footnote, heading ID)
- fonction RemoveMarkdown pour nettoyer les indicateurs de syntaxe
- exploration de structure JSON complexe avec espaces blancs
- comportement de Replace sans remplaçant défini (undefined)
- fonction de suppression d'accents (utile pour compatibilité API)
- démonstration détaillée de Slice avec indices précis
- exemples multiples d'indexation avec Slice
- rappel Split et présentation de Substring
- transition vers ToJSONString, recommandation de consulter la documentation intégrée
- fonction ToJSONString pour préparer une valeur à l'insertion dans une string
- fonction TrimEnd (suppression d'espaces en fin de texte uniquement)
- TrimStart et fonctions URLDecode/URLEncode
- fonction IndexOf pour localiser la position d'un caractère
- comportement d'IndexOf sur des occurrences multiples (première trouvée)
- fonction Match pour les expressions régulières (regex)
- recommandation d'utiliser l'IA plutôt que d'apprendre le regex manuellement
- démonstration pratique de génération de regex via Raycast
- correction itérative d'un regex généré par IA (gestion des accents)
- encouragement à l'expérimentation personnelle du regex
- fonction IsDomain (validation de format domaine, sans préfixe https)
- règle de validation d'URL (minimum deux lettres pour l'extension)
- fonction IsEmail (validation de format email)
- règles précises de validation d'IsEmail
- fonction IsNumeric (validation de format numérique avec opérateurs et décimales)
- fonctions de casse (SentenceCase, ToTitleCase)
- Uppercase et introduction de ParseJSON
- démonstration pratique de ParseJSON pour extraire des valeurs structurées
- fonction ToBoolean (conversion en booléen réel, défaut true)

## Outils mentionnes
- n8n
- Raycast

## Tips techniques
- Utiliser RemoveMarkdown pour retirer proprement les indicateurs de syntaxe Markdown (dièses, etc.) d'un texte final
- Utiliser la fonction de suppression d'accents pour garantir la compatibilité avec des API qui ne supportent pas les caractères accentués
- Consulter systématiquement la documentation intégrée de N8n pour approfondir chaque fonction texte disponible
- Générer les expressions régulières (regex) via l'IA plutôt que de les apprendre manuellement, une compétence devenue obsolète à maîtriser soi-même
- Utiliser Raycast pour générer rapidement des expressions régulières via IA directement depuis le clavier
- S'exercer personnellement avec des textes de test pour comprendre le comportement concret d'un regex avant de l'utiliser en production

## Cas d'usage reels
- [[]]
