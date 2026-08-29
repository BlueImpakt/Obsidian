---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.17 Les fonctions “texte” dans Make.txt"
---

# 2.17 Les fonctions “texte” dans Make

## Resume
- Introduction aux fonctions texte de Make, nombreuses mais avec un rythme de présentation rapide, en commençant par la fonction Length permettant de mesurer la longueur d'une chaîne de caractères.
- Présentation de Capitalize (mettre une majuscule au premier mot, exemple : « Jérôme ») et introduction de Start Case, une fonction voisine mais différente qui sera détaillée dans la suite.
- Présentation de la fonction ASCII (probablement) permettant de rendre lisibles par les API et le traitement informatique certains caractères non standards, notamment des caractères tchèques ou croates.
- Démonstration pratique avec le mot « méditerranée » : la fonction retire tous les caractères spéciaux non supportés, illustrant concrètement l'utilité de la normalisation pour la compatibilité informatique.
- Présentation de la fonction Replace : remplacer un mot spécifique par un autre (exemple : « tigre » remplacé par « lion »), en spécifiant le mot cible dans le premier paramètre et le remplacement dans le second.
- Confirmation du fonctionnement de Replace et introduction de ReplaceEmojiCharacters, une fonction supprimant automatiquement les émojis d'un texte, utile pour nettoyer du contenu généré avec excès d'émojis.
- Présentation de la fonction Trim, utile pour nettoyer les espaces superflus dans les données de formulaires (par exemple des prénoms saisis avec des espaces indésirables), un problème qui peut fausser les filtres ultérieurs.
- Distinction entre Capitalize (majuscule uniquement en début de phrase) et une fonction opposée en minuscules. Transition vers la fonction Substring, comparée à un découpage précis d'une portion de texte.
- Démonstration de Substring avec l'exemple « anticonstitutionnellement » : pour extraire « constitutionnellement », il faut démarrer à l'index correct, avec la précision essentielle que la numérotation commence à 0 et non à 1.
- Correction d'une erreur en direct : oubli de la valeur de fin pour Substring, corrigée en définissant une position finale (20) pour obtenir le résultat souhaité, illustrant l'importance de définir les deux bornes.
- Présentation de fonctions peu utilisées mais utiles à connaître (recherche de position d'un caractère dans une chaîne), et introduction de ToBinary et ToString pour transformer un texte en valeur binaire.
- Démonstration de l'encodage URL avec des pourcentages (exemple « je supporte le PSG » transformé avec des caractères encodés comme %20), illustrant le processus d'encodage d'une chaîne de texte.
- Présentation de la fonction StripHTML : elle retire les balises HTML (exemple balise bold) d'un texte pour le rendre compatible avec des outils qui ne supportent pas le HTML brut, une fonction pratique et concrète.
- Introduction au Markdown, largement utilisé dans des outils comme Notion pour structurer du texte via de simples caractères plutôt que des clics d'interface, un format de mise en forme textuelle très répandu.
- Confirmation de l'utilité pratique de StripHTML, avec démonstration montrant la transformation de hashtags en titre de niveau 2 (H2), illustrant la conversion automatique de format lors du nettoyage HTML.
- Confirmation du fonctionnement de la fonction Contains renvoyant un booléen (True/False), puis transition vers la fonction Split, importante pour découper une chaîne de texte selon un séparateur défini.
- Mention transparente de fonctions de chiffrement (encryption) peu maîtrisées par l'auteur, dont Base64 utilisée occasionnellement pour l'encodage, sans prétendre à une expertise particulière sur ce sujet technique.

## Concepts cles
- introduction aux fonctions texte (dont Length)
- fonctions Capitalize et Start Case
- fonction de normalisation de caractères spéciaux (ex: tchèque, croate)
- démonstration pratique de suppression de caractères spéciaux
- fonction Replace (remplacement de mot)
- fonction ReplaceEmojiCharacters pour nettoyer les émojis
- fonction Trim pour nettoyer les espaces superflus
- distinction Capitalize vs minuscule
- introduction de Substring
- règle importante : indexation Substring commence à 0
- nécessité de définir les deux bornes (début/fin) pour Substring
- fonctions de position de caractère, ToBinary, ToString
- encodage URL avec caractères pourcentage (%20)
- fonction StripHTML pour retirer les balises HTML
- Markdown comme format de mise en forme textuelle (utilisé dans Notion)
- conversion automatique de hashtags en titre H2 via StripHTML
- fonction Contains (retour booléen) et introduction de Split
- fonctions de chiffrement (Base64) peu approfondies

## Outils mentionnes
- Make
- Notion

## Tips techniques
- Utiliser ReplaceEmojiCharacters pour nettoyer automatiquement un texte contenant trop d'émojis
- Utiliser Trim systématiquement sur les données de formulaires pour éviter que des espaces superflus faussent les filtres ultérieurs
- Se rappeler que l'indexation des caractères dans Substring commence à 0, pas à 1

## Cas d'usage reels
- [[]]
