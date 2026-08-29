---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.04 Transcrire avec Whisper.txt"
---

# 5.04 Transcrire avec Whisper

## Resume
- Introduction au module de transcription via OpenAI (Whisper) : plan en deux temps, d'abord transcrire un épisode de podcast, puis transcrire une vidéo Instagram.
- Présentation du format XML de flux podcast comme équivalent ancien du JSON, contenant l'image, le résumé et les métadonnées lisibles par les lecteurs de podcast.
- Démonstration de filtrage de 318 épisodes de podcast pour ne conserver que ceux dont la durée est inférieure à un seuil défini (1000 unités), afin de trouver un épisode court adapté au test.
- Explication de la conversion de la durée en minutes (division par 60) pour identifier un épisode court (5 minutes) adapté à une transcription de démonstration rapide.
- Exemple d'usage stratégique : enrichir un agent expert en neurosciences avec le contenu d'Andrew Huberman, en utilisant la fonction Transcribe a Recording d'OpenAI.
- Confirmation du bon fonctionnement de la transcription complète des 5 minutes de podcast, avec texte généré réutilisable, notamment pour créer des résumés de podcast.
- Mention de la possibilité de diviser un fichier audio volumineux en plusieurs petits fichiers pour les gros contenus, avant transition vers la transcription de vidéos Instagram.
- Présentation du nœud HappyFile pour scraper du contenu Instagram sans installation complexe, avec configuration via l'action « Run an actor ».
- Configuration du scraping avec un nom d'utilisateur Instagram spécifique (créateur RPN/Roberto Nixon) et limitation du nombre de reels scrapés par profil (limité à 1 pour la démo).
- Configuration de l'option Wait For Finish avec paramétrage du timeout maximal (60 secondes par défaut), une valeur ajustable selon les besoins de traitement.
- Démonstration de téléchargement effectif d'une vidéo Instagram (3,68 Mbps, taille typique légère d'un reel) suivi de sa transcription via l'outil OpenAI Transcribe.
- Conclusion sur l'utilité de la transcription vidéo pour analyser les patterns de storytelling de créateurs influents dans une niche donnée, en vue d'améliorer son propre contenu.

## Concepts cles
- introduction à la transcription OpenAI Whisper (podcast puis vidéo Instagram)
- présentation du format XML de flux podcast (équivalent ancien du JSON)
- démonstration de filtrage d'épisodes par durée (318 épisodes filtrés)
- explication de la conversion de durée en minutes pour sélection d'épisode court
- exemple stratégique d'enrichissement d'agent expert via transcription de contenu spécialisé
- confirmation de transcription complète réutilisable pour résumés de podcast
- mention de la division de fichiers audio volumineux et transition vers Instagram
- présentation du nœud HappyFile pour scraper Instagram (Run an actor)
- configuration de scraping Instagram avec limitation du nombre de reels
- configuration du timeout Wait For Finish (60 secondes par défaut)
- démonstration de téléchargement et transcription d'une vidéo Instagram (3,68 Mbps)
- conclusion sur l'utilité de la transcription pour analyser les patterns de storytelling

## Outils mentionnes
- n8n
- OpenAI
- Whisper
- HappyFile
- Instagram

## Tips techniques
- Enrichir un agent expert avec le contenu transcrit de figures reconnues du domaine visé, pour améliorer la précision de ses réponses

## Cas d'usage reels
- [[]]
