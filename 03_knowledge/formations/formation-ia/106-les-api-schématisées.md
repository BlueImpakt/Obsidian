---
tags: [formation, millenium]
module: Formation IA
section: "Comprendre l'Automatisation"
source_transcript: "1.06 Les API Schématisées.txt"
---

# 1.06 Les API Schématisées

## Resume
- Introduction à une présentation schématisée et approfondie du fonctionnement d'une API via une carte visuelle détaillée, en partant du principe de deux applications souhaitant échanger une donnée.
- Explication du concept de requête via un exemple concret (Google Forms) : chaque fois qu'on envoie ou demande des données à une API spécifique, cela constitue une requête, point de départ du schéma présenté.
- Explication de la structure d'URL d'une API : distinction entre l'URL classique du site web (monapp.com) et celle de l'application/API (préfixée de « app » ou incluant une version comme V2), une structure commune à la majorité des applications.
- Démonstration de la construction d'une requête via un outil comme N8n ou Make : l'adresse de base est complétée par un endpoint spécifique ajouté après le mot « api » dans l'URL, ciblant la ressource souhaitée.
- Introduction de la terminologie simplifiée « rows » pour désigner les enregistrements/lignes, puis présentation du concept de type d'action associé à un endpoint, dont GET (obtenir des données) est le premier exemple présenté.
- Poursuite de la présentation des types d'action : possibilité de filtrer via une query, puis introduction de POST, l'action utilisée pour envoyer ou créer une nouvelle donnée, en complément de GET.
- Explication du chevauchement possible entre actions : PUT/PATCH servent à modifier ou remplacer une ligne, mais POST peut parfois aussi servir à cette fin selon la conception de l'endpoint, celui-ci pouvant décider lui-même du comportement approprié.
- Introduction de la notion de sécurité des données API : bien qu'une base de données soit partagée, chaque utilisateur ne peut accéder qu'à ses propres données (exemple d'un spreadsheet personnel), grâce à un système d'individualisation des accès.
- Présentation du mode de connexion OAuth : un système facilitant la connexion via son propre compte utilisateur, similaire au processus de validation qu'on connaît lors d'une authentification classique.
- Explication de l'authentification par mot de passe intégrée dans le header de la requête, aux côtés d'autres informations techniques que le header peut contenir pour accompagner la requête API.
- Explication du header « Content-Type: application/json » : il indique au service destinataire (exemple Google Sheets) le format de langage utilisé pour la communication, une analogie faite avec le fait de préciser dans quelle langue on va parler.
- Démonstration pratique d'ajout d'une nouvelle ligne dans un Google Sheets via API, l'auteur précisant que même un tableur simple comme Google Sheets peut fonctionner comme une véritable base de données dans ce contexte.
- Suite de la démonstration : définition d'un champ statut avec des valeurs prédéfinies (Gold, Silver, Bronze), avec avertissement sur un piège potentiel concernant un autre champ à venir (revenu).
- Explication de l'usage des guillemets dans le JSON pour catégoriser le type de valeur (texte vs chiffre) : sans guillemets, l'API ne peut pas distinguer un texte d'un nombre, illustrant l'importance de cette convention syntaxique.
- Explication du type booléen en JSON : les valeurs true/false s'écrivent sans guillemets car il n'existe que deux réponses possibles (vrai ou faux), une convention qui facilite grandement le traitement automatisé de ces données.
- Illustration pratique de l'envoi d'une donnée booléenne dans une requête, avec précision que la colonne d'exemple était fictive à but pédagogique. Une fois la requête envoyée, une nouvelle ligne est ajoutée à la base de données.
- Présentation d'une alternative au JSON : l'envoi sous forme de FormData, souvent via des interfaces visuelles facilitant la création de lignes, où chaque composante de la donnée (nom, etc.) est envoyée séparément selon le logiciel utilisé.
- Mise en garde sur les erreurs de format possibles : un statut attendant un mot précis (ex: « gold ») échouera si mal orthographié (« golde »), le système renvoyant alors une erreur de non-conformité avec le paramétrage attendu.

## Concepts cles
- présentation schématisée détaillée du fonctionnement API
- concept de requête illustré par un exemple (Google Forms)
- structure d'URL distinguant site web et application/API (préfixe 'app', versions V2)
- construction d'une requête via N8n/Make avec ajout d'endpoint
- terminologie 'rows' pour les enregistrements
- GET comme premier type d'action
- POST pour envoyer/créer une donnée
- filtrage via query
- chevauchement possible entre POST et PUT/PATCH selon l'endpoint
- individualisation des accès aux données API (sécurité par utilisateur)
- OAuth comme mode de connexion via compte utilisateur
- authentification par mot de passe intégrée au header
- header Content-Type application/json (analogie linguistique)
- Google Sheets utilisé comme base de données via API
- exemple de champ statut avec valeurs prédéfinies (Gold/Silver/Bronze)
- rôle des guillemets pour distinguer texte et nombre en JSON
- type booléen en JSON (true/false sans guillemets)
- exemple pratique d'envoi de donnée booléenne pour ajouter une ligne
- FormData comme alternative au JSON pour l'envoi de données
- erreurs de format courantes (orthographe non conforme)

## Outils mentionnes
- Google Forms
- n8n
- Make
- Google Sheets

## Tips techniques
- Vérifier attentivement l'orthographe exacte attendue par un champ à valeurs prédéfinies pour éviter les erreurs de requête

## Cas d'usage reels
- [[]]
