---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.12 Fonctions de dates dans N8N.txt"
---

# 3.12 Fonctions de dates dans N8N

## Resume
- Introduction aux fonctions de dates sur N8n, avec avertissement que certaines fonctions vont surprendre. Présentation préalable importante du formatage Luxon, une bibliothèque de référence à bien assimiler.
- Présentation du formatage Luxon des dates : différents codes de lettres répétées (tttt pour temps+timezone, ffff pour date complète, dddd pour date écrite entière) permettent de personnaliser précisément l'affichage.
- Démonstration pratique de manipulation de date avec un exemple personnel (anniversaire de la mère de l'auteur, 19 juillet 2025), en utilisant ToDateAndTime pour convertir une string en date exploitable.
- Explication de la codification des jours (2 ou 4 chiffres) et des mois (M majuscule, distinct de m minuscule qui désigne les minutes), une nuance de casse essentielle à respecter dans Luxon.
- Présentation des dates complètes (dddd) et de la date avec heure (ffff, probablement pour « full »), ainsi que l'option de conversion au format Unix Timestamp.
- Démonstration de l'ajout combiné de plusieurs unités temporelles en une seule opération (exemple : 6 jours + 6 mois simultanément), une approche jugée plus simple et lisible par l'auteur.
- Présentation de la fonction DiffTo pour calculer la différence entre deux dates (exemple : 15,5 jours ou 22 000 minutes jusqu'à un anniversaire), avec possibilité de choisir l'unité de mesure du résultat.
- Introduction de la fonction EndOf, permettant d'arrondir une date vers la fin d'une unité choisie (exemple : fin de journée), une fonctionnalité pratique pour définir des bornes temporelles.
- Démonstration détaillée d'EndOf sur différentes unités : fin de journée (23h59min59s), fin de mois (31 juillet), fin d'année (31 décembre), fin d'heure, avec introduction de StartOf pour l'arrondi vers le début.
- Présentation de la fonction Set pour modifier des composantes spécifiques d'une date (exemple : fixer l'heure à midi), permettant des ajustements précis et ciblés d'une date/heure.
- Présentation de SetLocal, permettant d'adapter la structure de date selon différents pays/langues (ordre mois/jour/année inversé), ainsi que la définition de la timezone (exemple : Europe/Lisbonne).
- Explication de ToLocal : définit une date par rapport au fuseau horaire de l'utilisateur, avec démonstration de conversion d'une date texte (2025-07-19) vers ce format local personnalisé.
- Confirmation du décalage horaire observé (5 heures d'écart avec une timezone de référence), validant le fonctionnement de ToLocal, avant de poursuivre avec d'autres opérateurs de date importants.
- Présentation de ToUTC : ramène une date au fuseau horaire de Greenwich (référence 0), quelle que soit la timezone d'origine, très utile pour standardiser des dates issues de sources multiples.
- Distinction entre Compare/Diff2 (différence entre deux dates spécifiées) et Diff2Now (raccourci calculant automatiquement par rapport à maintenant, évitant de devoir spécifier explicitement « now »).
- Débogage en direct d'un problème de récupération de valeur, résolu en identifiant un symbole dollar manquant, illustrant le processus itératif de correction lors de la manipulation de dates.
- Démonstration d'IsBetween : vérifie si une date se situe entre deux bornes (exemple : le 19 juillet n'est pas entre le 1er et le 18 juillet, donc faux). Introduction de ToISO pour formater au standard ISO.
- Clarification du comportement par défaut vs ToISO explicite : le système peut deviner le format attendu, mais ToISO garantit la conformité même quand une valeur manque ou que le format initial est incorrect.
- Démonstration finale de ToDateTime combiné à ToISO pour transformer une valeur (16h32) au format ISO correct, avec annonce que la liste de fonctions touche bientôt à sa fin.
- Présentation des fonctions d'extraction de composants individuels d'une date : Day (jour), Extract (déjà vu), Hour (heure, retournant 0 par défaut si non spécifiée dans la date d'origine).
- Présentation d'IsInLeapYear (année bissextile) : 2024 est vraie (bissextile), 2025 est fausse, une fonction utile pour des calculs calendaires précis liés aux années bissextiles.
- Présentation des options d'extraction avancées via InLocal : jour de la semaine (samedi identifié), format court (WeekdayShort), et numéro de semaine, offrant une granularité complète de personnalisation.
- Mention des Quarters (trimestres) et rappel des fonctions IsEmpty/IsNotEmpty déjà vues, ainsi que la possibilité de savoir si une date tombe un week-end, complétant le panorama des fonctions de date.

## Concepts cles
- introduction aux fonctions de dates N8n basées sur Luxon
- codes de formatage Luxon (tttt, ffff, dddd)
- démonstration pratique avec ToDateAndTime (exemple personnel)
- nuance de casse M (mois) vs m (minutes) dans Luxon
- formats dddd et ffff (full date), conversion Unix Timestamp
- combinaison de plusieurs unités temporelles en une opération
- fonction DiffTo pour calculer un écart entre deux dates
- fonction EndOf pour arrondir vers la fin d'une unité de temps
- exemples multiples d'EndOf et introduction de StartOf
- fonction Set pour modifier des composantes spécifiques de date
- fonction SetLocal (adaptation régionale et timezone)
- fonction ToLocal pour ajuster une date au fuseau horaire personnel
- validation du décalage horaire via ToLocal
- fonction ToUTC pour standardiser une date sur Greenwich
- distinction Diff2 (deux dates) vs Diff2Now (raccourci vs maintenant)
- débogage en direct (symbole dollar manquant)
- fonction IsBetween et introduction de ToISO
- utilité de ToISO explicite pour garantir la conformité de format
- combinaison ToDateTime + ToISO pour formatage correct
- extraction de composants individuels (Day, Hour)
- fonction IsInLeapYear (validation année bissextile)
- options d'extraction avancées via InLocal (jour semaine, numéro semaine)
- fonction Quarters et vérification de week-end

## Outils mentionnes
- n8n

## Tips techniques
- Attention à la casse : M majuscule désigne le mois, m minuscule désigne les minutes dans le formatage de date Luxon
- Utiliser ToUTC pour standardiser des dates issues de sources ou timezones multiples avant traitement

## Cas d'usage reels
- [[]]
