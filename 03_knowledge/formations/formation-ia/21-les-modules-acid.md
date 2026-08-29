---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.1 Les modules ACID.txt"
---

# 2.1 Les modules ACID

## Resume
- Introduction aux modules ACID, illustrés via l'exemple d'Airtable (obtenir des enregistrements/lignes dans une base de données), un type de module garantissant l'intégrité complète des conditions avant déclenchement.
- Comparaison rapide entre Google Sheets (navigation facile, écriture simple) et Airtable (plus structuré), l'auteur annonçant qu'il approfondira Airtable plus tard tout en présentant brièvement les deux options.
- Digression enthousiaste sur Telegram, décrit comme gratuit et extraordinaire (« WhatsApp en un milliard de fois mieux »), avec démonstration de la création d'un bot Telegram pour l'envoi de messages automatisés.
- Détail pratique de la création du bot Telegram : nom libre mais devant se terminer par « bot » pour l'identifiant technique, puis récupération du token d'authentification nécessaire à la connexion.
- Exemple de traitement par lots de 16 éléments (villes préférées : Tokyo, Lisbonne, Porto, Bali, Singapour, etc.), traités par groupes de 5, illustrant la mécanique de pagination lors d'une recherche.
- Constat que ce traitement a consommé 16 opérations distinctes pour une simple recherche (search), amenant l'auteur à recommander l'usage du module Watch plutôt que Search pour économiser des opérations dans certains cas.
- Configuration du module Watch avec un champ jour/heure spécifique, sélection du champ ciblé (ville), limitation possible à une vue Airtable spécifique, et définition d'une limite de résultats retournés (exemple : 10).
- Confirmation de l'économie d'opérations obtenue avec le module ACID/Watch : une seule ligne modifiée traitée en une seule opération, évitant d'avoir à filtrer systématiquement l'ensemble de la base de données à chaque exécution.

## Concepts cles
- introduction aux modules ACID via l'exemple Airtable
- comparaison rapide Google Sheets vs Airtable (simplicité vs structure)
- éloge de Telegram et création d'un bot pour l'automatisation
- configuration technique d'un bot Telegram (nom se terminant par 'bot', token)
- traitement par lots de 5 sur 16 éléments (pagination)
- Watch préférable à Search pour économiser des opérations
- configuration du module Watch (champ ciblé, vue, limite de résultats)
- économie confirmée d'opérations grâce aux modules ACID/Watch

## Outils mentionnes
- Airtable
- Google Sheets
- Telegram
- WhatsApp
- Make

## Tips techniques
- Le nom technique d'un bot Telegram doit obligatoirement se terminer par 'bot' pour être accepté
- Privilégier le module Watch plutôt que Search quand c'est possible, pour économiser significativement des opérations

## Cas d'usage reels
- [[]]
