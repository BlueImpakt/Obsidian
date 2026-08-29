---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.18 Les fonctions de dates dans Make.txt"
---

# 2.18 Les fonctions de dates dans Make

## Resume
- Introduction aux fonctions de dates sur Make, l'auteur précisant avoir préparé cette partie hors caméra en raison de sa nature répétitive, mais promettant de tout expliquer en détail par la suite.
- Présentation des principaux transformateurs de dates, Add et Set, et de la fonction Now qui retourne la date actuelle au format ISO avec le fuseau horaire approprié.
- Contexte historique du format de date standardisé : créé pour résoudre le chaos des formats de date variés utilisés partout, structuré en année/mois/jour/heure à la seconde près pour garantir une cohérence universelle.
- Démonstration pratique de la fonction Now, retournant l'heure actuelle correspondant à la localisation, avec une petite nuance apportée sur la précision exacte de cette heure affichée.
- Présentation de la fonction Add pour les dates : permet d'ajouter ou de soustraire des minutes (et autres unités), accessible via ce que l'auteur appelle les « transformateurs » de dates dans l'interface Make.
- Explication du mécanisme de soustraction via l'opérateur moins : la fonction d'ajout de minutes peut aussi en retirer si le chiffre fourni est négatif, une convention standard en programmation reprise dans Make.
- Démonstration en série de plusieurs opérations de dates : soustraction de 10 minutes, 2 heures, puis 4 heures sur des éléments successifs, illustrant la variété des unités manipulables.
- Poursuite de la démonstration avec ajout de 6 mois puis 1 an, confirmant que toutes les unités de temps (minutes à années) peuvent être ajoutées ou soustraites. Introduction des fonctions Set, distinctes des fonctions Add.
- Explication du fonctionnement de Set : elle réinitialise une composante spécifique de la date/heure actuelle (seconde de la minute, minute de l'heure, heure du jour, jour de la semaine, mois de l'année) à une valeur définie.
- Démonstration pratique combinant plusieurs fonctions de date testées ensemble, avec observation de l'heure affichée en format GMT (16h05 pour 17h05 réel), soulignant l'importance de comprendre le décalage de fuseau horaire.
- Analyse détaillée du résultat des tests précédents, avec vérification des minutes soustraites et confirmation du décalage horaire GMT constaté dans l'environnement de travail de l'auteur.
- Poursuite de l'analyse des résultats : soustraction de 2 heures (16h05 devient 14h05) et de 4 jours, l'auteur rappelant systématiquement que l'heure affichée dans Make est en GMT et non dans le fuseau horaire personnel de l'utilisateur.
- Suite de l'analyse des résultats de Set : vérification de l'heure (12), du jour (lundi 23 juin), du mois (novembre 2025) et de l'année (2077 !), avec une touche d'humour sur la longévité espérée de l'auteur.
- Recommandation pédagogique d'exercices pratiques personnels pour bien assimiler les fonctions de dates. Introduction de Format Date, permettant de formater une date selon des critères spécifiques et personnalisables.
- Présentation de la codification de format de date standard (Y pour année, avec 2 ou 4 chiffres possibles), et démonstration avec un convertisseur externe pour valider visuellement le résultat obtenu (20 mars confirmé).

## Concepts cles
- introduction aux fonctions de dates de Make
- fonctions Add et Set pour les dates
- fonction Now (format ISO avec fuseau horaire)
- origine et structure du format de date standardisé (ISO)
- démonstration pratique de la fonction Now
- fonction Add pour manipuler les dates (ajout/soustraction)
- convention de soustraction via valeur négative (standard programmatique)
- démonstration de soustractions successives sur plusieurs unités de temps
- ajout de mois et années
- introduction des fonctions Set (distinctes de Add)
- mécanisme de Set (réinitialisation d'une composante temporelle précise)
- décalage entre heure GMT affichée et heure locale réelle
- analyse de résultats de tests de dates avec décalage GMT
- rappel récurrent : heure Make en GMT, pas fuseau personnel
- exemple humoristique de résultat Set avec année future (2077)
- recommandation d'exercices pratiques
- introduction de Format Date
- codification de format de date (Y=année) et validation via convertisseur

## Outils mentionnes
- Make

## Tips techniques
- Toujours se souvenir que l'heure affichée par défaut dans Make est en GMT, pas dans son propre fuseau horaire
- S'exercer soi-même avec les fonctions Add/Set/Format Date sur des exemples personnels pour bien les assimiler

## Cas d'usage reels
- [[]]
