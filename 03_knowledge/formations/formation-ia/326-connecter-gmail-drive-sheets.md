---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.26 Connecter Gmail  Drive  Sheets.txt"
---

# 3.26 Connecter Gmail / Drive / Sheets

## Resume
- Introduction à la connexion des comptes Google (Gmail, Drive, Sheets) via credentials personnalisés, avec plusieurs méthodes possibles présentées, dont une approche plus avancée développée dans ce module.
- Démonstration d'un cas où le bouton standard « se connecter à Google » n'est plus disponible, nécessitant une méthode de connexion alternative via configuration manuelle.
- Démonstration de création d'un projet Google Cloud Console, première étape nécessaire pour configurer une connexion Google personnalisée avancée avec ses propres identifiants.
- Activation de l'API Google Drive sur le projet Cloud Console créé, une étape indispensable pour autoriser l'accès programmatique aux services Google souhaités.
- Recommandation d'activer également l'API Google Slides en prévision d'usages futurs, pour avoir une configuration clé en main dès qu'on interagit avec l'ensemble de la suite Google.
- Poursuite de la configuration du projet Google Cloud Console : ajout d'une adresse de contact, validation des étapes successives, puis configuration de l'autorisation d'instance dans les paramètres avancés.
- Configuration des Redirect URLs en copiant l'URL fournie par N8n, puis génération du Client ID et Client Secret nécessaires pour finaliser la connexion OAuth personnalisée.
- Validation de la connexion réussie à Google Drive, avec extension de la même procédure pour connecter également Google Sheets en créant un compte de connexion similaire.

## Concepts cles
- introduction à la connexion Google via credentials personnalisés
- méthode de connexion alternative quand le bouton standard est indisponible
- création d'un projet Google Cloud Console (première étape)
- activation de l'API Google Drive sur le projet Cloud Console
- activation préventive de l'API Google Slides pour usage futur
- configuration finale du projet Google Cloud Console (adresse contact, autorisation instance)
- configuration des Redirect URLs et génération Client ID/Secret
- validation de la connexion Drive et extension à Google Sheets

## Outils mentionnes
- n8n
- Gmail
- Google Drive
- Google Sheets
- Google Cloud Console

## Tips techniques
- Activer par anticipation toutes les API Google susceptibles d'être utilisées, pour avoir une configuration clé en main

## Cas d'usage reels
- [[]]
