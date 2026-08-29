---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.03 Les déclencheurs dans Make.txt"
---

# 2.03 Les déclencheurs dans Make

## Resume
- Introduction aux déclencheurs sur Make, présentés comme un élément crucial car ils initient toute la séquence d'automatisation. Deux types principaux à approfondir : les déclencheurs instantanés en premier.
- Explication des événements déclencheurs disponibles selon les outils (nouvel abonné, désabonnement newsletter, action spécifique dans un CRM), permettant de définir précisément les événements souhaités pour déclencher une alerte.
- Transition vers le second type majoritaire de déclencheurs : les déclencheurs non instantanés, illustrés par l'exemple d'aller chercher des pages dans Notion ou Airtable, sans notification immédiate en temps réel.
- Démonstration pratique avec Airtable : configuration d'un déclencheur qui envoie un signal dès qu'un nouvel utilisateur apparaît dans une feuille de ventes ou de contacts sélectionnée.
- Configuration détaillée du déclencheur : définition d'un champ spécifique et choix du point de départ (à partir de maintenant ou d'une date spécifique définie), offrant une granularité de contrôle sur le démarrage.
- Explication des intervalles réguliers de déclenchement (toutes les 5, 10 minutes, etc.) et précision importante : chaque déclenchement consomme une opération facturée, même si aucune nouvelle donnée n'est disponible.
- Démonstration du scheduling avancé sur Make : définir des fenêtres horaires précises (ex: 14h-15h40), des jours spécifiques (mardi, lundi, jeudi) et des mois particuliers (février, avril), permettant un contrôle très granulaire du déclenchement.
- Exemple pratique d'optimisation : exclure les mois d'été (vacances) et définir des horaires d'ouverture précis, avec déclenchement toutes les 15 minutes uniquement pendant ces créneaux, permettant d'économiser des opérations inutilisées.
- Présentation des options de récurrence : jour du mois spécifique, jour de la semaine (chaque lundi), chaque jour à une heure fixe, ou déclenchement unique (Once) à une date précise, couvrant tous les cas de figure temporels.

## Concepts cles
- importance des déclencheurs comme point de départ
- déclencheurs instantanés (premier type)
- personnalisation des événements déclencheurs selon l'outil (CRM, newsletter)
- déclencheurs non instantanés (majorité des cas, exemple Notion/Airtable)
- exemple pratique de déclencheur Airtable (nouvel utilisateur)
- configuration du point de départ du déclencheur (maintenant ou date spécifique)
- intervalles réguliers de déclenchement consommant une opération à chaque fois
- scheduling avancé (fenêtre horaire, jours, mois spécifiques)
- optimisation par exclusion de périodes (économie d'opérations)
- options de récurrence complètes (mois, semaine, jour, unique)

## Outils mentionnes
- Make
- Notion
- Airtable

## Tips techniques
- Attention : chaque déclenchement à intervalle régulier consomme une opération facturée, même sans nouvelle donnée disponible
- Définir des horaires d'ouverture précis pour les déclencheurs récurrents afin d'économiser des opérations en dehors des créneaux utiles

## Cas d'usage reels
- [[]]
