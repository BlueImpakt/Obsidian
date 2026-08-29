---
tags: [formation, millenium]
module: Formation IA
section: "Agents de Productivité"
source_transcript: "6.02 Agent Inbox Zero • Partie 2.txt"
---

# 6.02 Agent Inbox Zero • Partie 2

## Resume
- Introduction à la deuxième partie de l'agent Inbox Zero : connexion à Google Drive pour l'upload de fichiers, avec renvoi vers un tutoriel séparé sur la connexion Gmail via Google Cloud Platform.
- Test de récupération de données à partir d'une fausse entreprise (Acme Corp) et recherche d'un modèle de facture vide pour tester le traitement automatisé de factures.
- Recherche d'un exemple de facture au format PDF (via Invoice Generator) pour créer un cas de test réaliste destiné à valider le traitement automatisé des factures.
- Démonstration de génération d'une facture de test réaliste (adresse, échéance à 14 jours, montant de 1000$) via un générateur en ligne pour valider le pipeline de traitement.
- Configuration de l'option Include Other Input Fields sur le trigger email, essentielle pour permettre le téléchargement des documents joints reçus.
- Débogage d'une erreur d'exécution après réception d'un email test, révélant un champ obligatoire non rempli, illustrant le processus itératif de mise au point du workflow.
- Démonstration de récupération de la pièce jointe (Attachment 0) et configuration de l'upload de fichier vers Google Drive avec le bon nom de ressource.
- Constat que la pièce jointe binaire n'a pas été correctement récupérée dans un premier essai, nécessitant de recommencer l'envoi de l'email de test.
- Second essai réussi avec recréation d'une facture de test et envoi correct, en veillant bien à conserver la pièce jointe lors de l'exécution du workflow.
- Conclusion sur l'utilité de cette automatisation simple pour sauvegarder facilement les factures reçues, avec introduction d'une extension possible : transmettre la facture au comptable.
- Démonstration de configuration d'un envoi d'email automatique au comptable avec la facture en pièce jointe, incluant le numéro de facture récupéré dans l'objet du message.
- Explication de l'utilité du scan automatique des documents pour permettre à l'agent de traiter et récupérer les données directement depuis le compte Google Drive connecté.
- Configuration de la classification des demandes de prospection (YouTube) réutilisant le même modèle et le contenu sauvegardé précédemment pour la catégorisation.
- Configuration de l'extraction de champs spécifiques (budget de l'opération, nom du contact) à partir du contenu email pour enrichir automatiquement une base de données de prospection.
- Finalisation des champs d'extraction (budget, entreprise, type d'opportunité comme affiliation/sponsoring) pour enrichir automatiquement un Google Sheet de suivi.
- Exemple pratique de génération automatique de proposition de collaboration pour un YouTubeur, basée sur une rémunération en affiliation, illustrant la génération de réponses commerciales.
- Envoi de la proposition générée (20% de commission) avec annonce d'une méthode plus avancée à venir plus tard dans la formation pour ce type de génération.
- Configuration d'une logique de filtre pour réponse automatique conditionnelle : enregistrer systématiquement toute opportunité mais ne répondre automatiquement que dans certains cas spécifiques.
- Configuration d'un agent répondant automatiquement par la négative aux demandes d'affiliation, avec prompt précis définissant son rôle d'assistant email et son contexte.
- Démonstration finale du déclenchement de l'agent ayant accès aux emails, capable de composer et envoyer directement une réponse à la bonne personne via Gmail.
- Conclusion sur le gain de temps réalisé par l'agent, avec rappel important de toujours retirer les mentions d'attribution automatique (Append) après un test, une bonne pratique systématique.

## Concepts cles
- introduction à la partie 2 : connexion Google Drive et renvoi vers tutoriel Gmail/GCP
- test de récupération de données via une fausse entreprise et modèle de facture vide
- recherche d'un exemple de facture PDF via Invoice Generator pour test réaliste
- démonstration de génération de facture de test réaliste
- configuration de l'option Include Other Input Fields pour télécharger les pièces jointes
- débogage d'une erreur d'exécution révélant un champ obligatoire manquant
- démonstration de récupération de pièce jointe et upload vers Google Drive
- constat d'échec de récupération de pièce jointe binaire nécessitant un nouvel essai
- second essai réussi de test avec pièce jointe correctement conservée
- conclusion sur l'utilité de la sauvegarde automatique de factures, extension vers le comptable
- démonstration de configuration d'envoi automatique de facture au comptable
- explication de l'utilité du scan automatique de documents pour récupération de données
- configuration de classification des demandes de prospection YouTube
- configuration d'extraction de champs spécifiques (budget, contact) pour enrichissement
- finalisation des champs d'extraction pour enrichissement automatique de Google Sheet
- exemple pratique de génération automatique de proposition de collaboration (affiliation)
- envoi de la proposition générée avec annonce d'une méthode avancée future
- logique de filtre pour réponse automatique conditionnelle selon le type d'opportunité
- configuration d'un agent de réponse négative automatique aux demandes d'affiliation
- démonstration finale de déclenchement d'agent envoyant une réponse via Gmail
- conclusion sur le gain de temps et rappel de retirer les mentions d'attribution automatique

## Outils mentionnes
- n8n
- Google Drive
- Google Cloud Platform
- Invoice Generator
- Google Sheets
- Gmail

## Tips techniques
- Utiliser un générateur de factures en ligne (Invoice Generator) pour créer rapidement des cas de test PDF réalistes
- Toujours activer l'option Include Other Input Fields sur un trigger email pour permettre le téléchargement des pièces jointes reçues
- Toujours retirer les mentions d'attribution automatique générées par les agents IA avant l'usage réel en production

## Cas d'usage reels
- [[]]
