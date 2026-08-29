---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.05 Analyser ses documents via OCR.txt"
---

# 5.05 Analyser ses documents via OCR

## Resume
- Introduction à l'OCR (Optical Character Recognition), technologie de reconnaissance de caractères manuscrits ou textuels par machine learning à partir d'analyse d'images.
- Démonstration des limites de la sélection de texte native dans une image (certains éléments comme une quantité numérique ne sont pas sélectionnables), justifiant le recours à l'OCR.
- Présentation de la performance élevée (environ 95%) d'un outil OCR capable de traiter textes, images, tableaux et équations mathématiques, fonctionnant aussi bien en français qu'en anglais.
- Démonstration de configuration d'un formulaire d'upload d'image dans N8n, avec champ de type fichier accepté pour tous les formats sans restriction.
- Test pratique d'upload d'une image contenant un identifiant à extraire, un cas d'usage concret illustrant la limite des méthodes classiques face à ce besoin.
- Présentation des deux modes d'OCR disponibles : OCR sur PDF (uploadé) ou sur images, avec focus initial sur le traitement des images.
- Démonstration de configuration simple du token d'API pour activer l'OCR, avec test de validation via Execute Step confirmant le bon fonctionnement de la connexion.
- Présentation du modèle spécifique Mistral OCR Latest utilisé pour le traitement OCR, avec configuration JSON définissant le modèle à appliquer sur l'image uploadée.
- Explication du processus d'encodage d'image en base64 nécessaire pour l'API OCR, avec récupération du format via une requête curl importée.
- Démonstration de conversion de données binaires en chaîne base64 via l'option Move File to a Base64 String, avec attention particulière à la cohérence du nom du champ d'entrée.
- Débogage d'une erreur de configuration liée au mode expression non activé, avec démonstration de récupération de l'image encodée via le module Extract From File.
- Configuration du type MIME de l'image et alternative via Set Fields pour conserver l'extension de fichier appropriée (ex : image.png) dans le pipeline de traitement OCR.
- Test réussi d'extraction OCR sur une image de demande de devis : l'intégralité du texte est extraite avec succès, confirmant le bon fonctionnement du pipeline de reconnaissance.
- Démonstration d'extraction d'un numéro de dossier spécifique à partir du texte OCR, réutilisable pour transmission automatique via un canal WhatsApp ou autre.
- Transition vers une approche alternative pour l'OCR sans encodage manuel : upload direct des fichiers via une structure en trois étapes distinctes.
- Présentation du cas d'usage d'enrichissement de PDF uploadé, avec référence à la documentation API en trois étapes pour traiter ce type de fichier.
- Démonstration de la première étape d'upload de fichier (une facture) via requête curl, permettant ensuite d'obtenir une URL de fichier utilisable pour l'appel OCR.
- Démonstration de la deuxième étape (deuxième appel API) pour obtenir l'URL du fichier uploadé, réalisée simplement via import d'une requête curl dans le nœud HTTP.
- Confirmation de l'obtention d'une URL d'accès direct au fichier uploadé, avant introduction de la dernière étape : l'envoi de cette URL au service OCR Mistral.
- Démonstration de configuration de la requête finale vers Mistral OCR via curl importé, en conservant uniquement l'authentification Bearer avec l'API Mistral.
- Configuration des champs de sortie structurés de l'OCR (produits séparés par virgule, montant en format string pour flexibilité de manipulation), finalisant le pipeline d'extraction de facture.

## Concepts cles
- introduction à l'OCR (reconnaissance de caractères par machine learning)
- démonstration des limites de sélection de texte native justifiant l'OCR
- performance OCR élevée (~95%) sur textes, tableaux, équations, multilingue
- démonstration de configuration d'un formulaire d'upload d'image sans restriction de format
- test pratique d'upload d'image avec identifiant à extraire (cas d'usage concret)
- présentation des deux modes d'OCR (PDF uploadé vs images)
- démonstration de configuration du token API OCR et validation
- présentation du modèle Mistral OCR Latest pour le traitement des images
- explication du processus d'encodage d'image en base64 via requête curl
- démonstration de conversion binaire vers base64 (cohérence du nom de champ)
- débogage d'une erreur de mode expression et récupération via Extract From File
- configuration du type MIME et conservation de l'extension de fichier via Set Fields
- test réussi d'extraction OCR complète sur une demande de devis
- démonstration d'extraction d'un numéro de dossier réutilisable via WhatsApp
- transition vers l'approche OCR sans encodage manuel (upload direct en 3 étapes)
- présentation du cas d'usage d'enrichissement de PDF via documentation API
- démonstration de la première étape d'upload de fichier via curl (obtention d'URL)
- démonstration de la deuxième étape API pour obtenir l'URL du fichier via curl
- confirmation d'obtention d'URL de fichier et transition vers l'envoi à Mistral
- démonstration de configuration finale de la requête OCR Mistral (authentification Bearer)
- configuration des champs de sortie structurés OCR (produits, montant en string)

## Outils mentionnes
- n8n
- Mistral
- WhatsApp

## Tips techniques
- Veiller à ce que le nom du champ d'entrée (ex : 'image') soit identique entre les nœuds lors de la conversion base64, sous peine d'échec
- Vérifier systématiquement que le mode expression est bien activé lors de la manipulation de chaînes de caractères encodées longues
- Conserver certains champs numériques (comme un montant) au format string en sortie OCR pour garder plus de flexibilité de manipulation ultérieure

## Cas d'usage reels
- [[]]
