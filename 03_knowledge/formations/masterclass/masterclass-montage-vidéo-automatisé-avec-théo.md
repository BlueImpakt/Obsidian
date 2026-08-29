---
tags: [formation, millenium]
module: Masterclass
section: "Masterclass"
source_transcript: "Masterclass Montage Vidéo Automatisé avec Théo.txt"
---

# Masterclass Montage Vidéo Automatisé avec Théo

## Resume
- Introduction à la masterclass sur le montage vidéo automatisé, sommaire des sujets (pourquoi automatiser, principes, analyse Gemini, transcription, outils, bonnes pratiques).
- Ouverture sur le sujet très attendu de l'automatisation du montage vidéo, présenté comme l'une des tâches les plus chronophages.
- Explication de l'économie du volume imposée par les algorithmes des plateformes, justifiant l'intérêt de l'automatisation pour produire davantage de contenu.
- Précision que l'automatisation vise particulièrement le format où chacun a son '80-20', YouTube restant plus complexe malgré des vidéos déjà automatisées avec l'IA.
- Explication du défi principal de l'automatisation : les coupes (cuts), avec plus de risques d'erreurs sur un long discours (exemple d'un rush de 48 minutes réduit à 20).
- Objectif de partage complet du skill de montage automatisé, avec recommandation de le comprendre en profondeur plutôt que de le copier aveuglément.
- Conseil de format pour les réseaux verticaux : attention à la place des boutons d'interaction sur le côté droit en bas, préparation d'une carte éditoriale de layout.
- Précision que la méthode fonctionne aussi pour les vlogs, nécessitant d'abord une analyse de tous les rushs par Gemini, puis la préparation d'assets visuels complémentaires.
- Explication technique fondamentale : une vidéo est un assemblage de frames (images) collées les unes aux autres, base de la logique de montage automatisé.
- Présentation de HyperFrame, moteur graphique de rendu (librairie de skills, templates, ressources, documentation) permettant de créer transitions et effets animés.
- Conseil technique pour le placement précis des effets sonores : découper strictement au début et à la fin du pic, en indiquant explicitement sa position pour un bon placement sur la timeline.
- Gestion des répétitions et hésitations ('euh euh euh') dans la transcription, avec préférence personnelle contre l'usage d'un prompteur pour les éviter.
- Présentation d'un mécanisme de validation intégré au skill, garantissant qu'aucun élément n'est envoyé sans vérification préalable.
- Présentation de l'interface de review façon outil de montage vidéo, où l'utilisateur indique les points de coupe et l'agent exécute via FFmpeg.
- Deuxième étape clé : rechercher des ressources d'illustration (YouTube, Twitter, tweets animés, vidéos de tweets) pour appuyer visuellement le discours.
- Présentation d'Epidemic Sound (bibliothèque de sons abordable) utilisé via un MCP permettant à Claude de trouver directement la bonne musique selon la scène.
- Récapitulatif de la stack d'outils : Epidemic Sound pour le son, Simple Icons pour les icônes, FFmpeg pour la coupe/mix, Postiz pour la publication sur les réseaux.
- Limite technique importante : Gemini échantillonne à une frame par seconde, pouvant manquer un flash de moins de 0,5 seconde ; attention aux balises vidéo.
- Précision que Postiz est open source, installable sur son propre serveur (Railway ou autre), et permet de publier sur toutes les plateformes sociales.
- Explication du rôle central de HyperFrame pour le motion design et la structuration des éléments d'interface, avec suggestion de soutenir le projet sur GitHub.
- Présentation du toolkit HyperFrame : rendu en 4K, timeline d'édition intégrée, cheat sheet de commandes pour faciliter l'interaction.
- Exemple d'utilisation personnalisée d'un template existant (police et interface adaptées), avec alternative disponible pour amplifier certains mots à l'écran.
- Recommandation de décrire en langage naturel le comportement d'animation souhaité (mot qui grossit, phrase entière, animation mot par mot) pour customiser à partir de HyperFrame.
- Présentation des 8 modules du système : Audio Pipeline, B-Roll Sourcing, Cut Pipeline, Design System, Gemini Judge, Hyperframe Ref, Master Engine, Soundcraft.
- Détail du fonctionnement de Gemini Judge (extraction et vérification de frames via MCP) et de la Cut Pipeline (transcription Eleven Labs, détection de silences/répétitions).
- Configuration technique requise : clés API nécessaires dans le fichier .env local pour Gemini, ElevenLabs, et potentiellement le MCP Epidemic Sound.
- Démonstration de recherche du MCP YouTube Knowledge sur le GitHub de Teo Bouancheau, ressource complémentaire pour le pipeline.
- Explication du dérushage automatique (nettoyage du rush avant montage) via un skill complémentaire nommé Video Use, faisant la différence sur la qualité finale.
- Fonctionnalités du skill Video Use : suppression des filler words et ajout de sous-titres, principalement utilisé pour nettoyer les mots de remplissage.
- Seul processus resté manuel dans le pipeline : la recherche de B-rolls pertinents sur YouTube (ex : rechercher une vidéo de 2 minutes correspondant au sujet).
- Présentation de Claude Tag : Claude devient un employé disponible 24h/24, mentionnable comme un collègue sur Slack pour réaliser des tâches (ex : sortir les ventes de mai, refaire une présentation).
- Théorie de la troisième interface de l'IA : après le chatbot web, puis l'application interagissant avec l'ordinateur, l'IA s'immisce désormais directement dans les outils utilisés.
- Méthode pédagogique de partir d'un état fini du skill pour expliquer comment le modifier, plutôt que de le présenter comme magique, avec premier retour sur la visibilité du présentateur.
- Revue détaillée élément par élément du montage généré, avec identification précise d'un écran noir jugé problématique à corriger.
- Validation globale positive d'une V2 avec corrections mineures : une faute d'orthographe (Andrei Karpathy) et un problème d'animation sur un chiffre à deux parties.
- Correction précise demandée : reformater '24 heures sur 24' en '24x24' avec un temps d'affichage plus long, et rechercher une image d'Andrei Karpathy.
- Démonstration de gain de temps : aller chercher soi-même une image (5 secondes) plutôt que de tout déléguer, en notant que cette étape reste automatisable.
- Présentation de Claude Tag : Claude s'immisce dans les chats Slack après ouverture des accès (drive, documents) pour réaliser des tâches déléguées.
- Répétition de la théorie de la troisième interface de l'IA : chatbot web, puis application interagissant avec l'ordinateur, puis IA immiscée directement dans les outils.
- Vérification du respect des zones d'interface natives TikTok/Instagram (icônes, nom de profil, commentaires) pour éviter les superpositions gênantes.
- Démonstration en direct de modification de police (trop grosse) vers une police avec empattement, en se rendant directement sur le projet.
- Objectif pédagogique : montrer qu'avec peu de changements on obtient un résultat totalement différent, le système n'étant pas limité au style personnel du présentateur.
- Exemple de prompt de style détaillé : police Europa Grotesque, privilégier la capitalisation lowercase plutôt que majuscules pour un meilleur rendu.
- Conseil d'explorer les composants UI disponibles comme source d'inspiration pour trouver des idées d'interface, de fond et de structure.
- Exemple de prompt de style néomorphique détaillé : blanc sur blanc crème cassé, texte alternant noir avec touches de bleu-violet.
- Idée expérimentale non garantie : diviser l'écran en trois avec une partie supérieure dédiée à la caméra pour tester un nouveau format visuel.
- Récapitulatif complet du style signature défini : crème cassé, Europa Grotesque lowercase, touches bleu-violet rares, néomorphisme minimal, zéro effet, fade up doux.
- Troisième répétition de la présentation de Claude Tag, l'immixtion de Claude dans les channels Slack après ouverture des accès aux outils.
- Troisième répétition de la théorie de la troisième interface de l'IA (chatbot, application, immixtion dans les outils).
- Démonstration pratique manuelle d'insertion d'image via l'éditeur iOS natif : identifier la zone, copier-coller directement l'image au bon endroit.

## Concepts cles
- introduction à la masterclass montage vidéo automatisé (sommaire des sujets)
- ouverture : le montage vidéo comme tâche particulièrement chronophage
- explication de l'économie du volume imposée par les algorithmes des plateformes
- précision : YouTube reste plus complexe pour l'automatisation malgré des essais réussis
- explication du défi principal des coupes (cuts) sur un long discours
- objectif de partage complet du skill avec recommandation de le comprendre en profondeur
- conseil de format vertical (attention aux boutons d'interaction)
- adaptation de la méthode aux vlogs (analyse Gemini puis assets)
- explication technique : une vidéo est un assemblage de frames
- présentation de HyperFrame (moteur graphique de rendu)
- conseil technique de découpage précis pour le placement des effets sonores
- gestion des répétitions et hésitations dans la transcription (sans prompteur)
- présentation d'un mécanisme de validation intégré au skill
- présentation de l'interface de review avec exécution des coupes via FFmpeg
- étape de recherche de ressources d'illustration (YouTube, Twitter, tweets animés)
- présentation d'Epidemic Sound utilisé via MCP pour Claude
- récapitulatif de la stack d'outils (Epidemic Sound, Simple Icons, FFmpeg, Postiz)
- limite technique : Gemini échantillonne à 1 frame/seconde (risque de manquer un flash court)
- précision : Postiz est open source et compatible avec toutes les plateformes
- explication du rôle central de HyperFrame pour le motion et la structuration
- présentation du toolkit HyperFrame (rendu 4K, timeline, cheat sheet)
- exemple de personnalisation d'un template existant (police, interface adaptée)
- recommandation de décrire en langage naturel le comportement d'animation souhaité
- présentation des 8 modules du système de montage automatisé
- détail du fonctionnement de Gemini Judge et de la Cut Pipeline
- configuration technique requise : clés API dans le fichier .env local
- démonstration de recherche du MCP YouTube Knowledge sur GitHub
- explication du dérushage automatique via le skill complémentaire Video Use
- fonctionnalités du skill Video Use (filler words, sous-titres)
- seul processus manuel du pipeline : la recherche de B-rolls pertinents
- présentation de Claude Tag (Claude mentionnable comme un collègue sur Slack)
- théorie de la troisième interface de l'IA (immiscée dans les outils existants)
- méthode pédagogique : partir d'un état fini pour expliquer les modifications
- revue détaillée élément par élément avec identification d'un écran noir problématique
- validation d'une V2 avec corrections mineures (orthographe, animation de chiffre)
- correction précise de formatage de texte et recherche d'image
- démonstration : chercher soi-même une image plutôt que tout déléguer (automatisable)
- présentation de Claude Tag (immixtion dans Slack après ouverture des accès)
- répétition de la théorie de la troisième interface de l'IA
- vérification du respect des zones d'interface natives TikTok/Instagram
- démonstration en direct de modification de police vers une police avec empattement
- objectif pédagogique : peu de changements suffisent pour un style totalement différent
- exemple de prompt de style détaillé (police Europa Grotesque, lowercase)
- conseil d'explorer les composants UI comme source d'inspiration
- exemple de prompt de style néomorphique détaillé (blanc crème, touches bleu-violet)
- idée expérimentale de division d'écran en trois avec zone caméra
- récapitulatif complet du style signature défini (design system personnel)
- troisième répétition de la présentation de Claude Tag
- troisième répétition de la théorie de la troisième interface de l'IA
- démonstration pratique manuelle d'insertion d'image via l'éditeur iOS

## Outils mentionnes
- Gemini
- YouTube
- HyperFrame
- FFmpeg
- Twitter
- Epidemic Sound
- Claude
- Simple Icons
- Postiz
- Railway
- GitHub
- Eleven Labs
- Slack
- TikTok
- Instagram

## Tips techniques
- Comprendre en profondeur un skill/workflow partagé avant de le réutiliser, pour pouvoir l'adapter facilement si l'output souhaité doit changer
- Toujours vérifier l'espace occupé par les boutons d'interaction natifs sur le côté droit lors du montage de vidéos verticales pour réseaux sociaux
- Découper strictement le début et la fin d'un pic audio et indiquer explicitement sa position, pour garantir un bon placement automatique sur la timeline
- Intégrer systématiquement une étape de validation dans un skill d'automatisation avant tout envoi final, pour éviter les erreurs non contrôlées
- Systématiquement rechercher des ressources d'illustration externes (tweets animés, extraits vidéo) pour appuyer visuellement chaque point du discours
- Garder en tête que Gemini échantillonne à une frame par seconde et peut manquer un flash de moins de 0,5 seconde lors de l'analyse vidéo
- Décrire précisément en langage naturel le comportement d'animation souhaité (grossissement, apparition mot par mot, transition) pour customiser un template HyperFrame
- Configurer toutes les clés API nécessaires (Gemini, ElevenLabs, Epidemic Sound) dans un fichier .env local avant de lancer le pipeline de montage automatisé
- Mentionner Claude directement dans Slack comme un collègue pour lui déléguer des tâches autonomes (analyses, retravail de documents)
- Partir toujours d'un résultat déjà généré (état fini) pour expliquer comment le modifier point par point, plutôt que de présenter un skill comme une boîte magique
- Toujours vérifier que le montage respecte les zones d'interface natives des réseaux sociaux (icônes, nom de profil) pour éviter toute superposition gênante
- Privilégier systématiquement l'écriture en lowercase plutôt qu'en majuscules dans les designs de texte animé, le rendu étant meilleur
- Explorer une bibliothèque de composants UI existants comme source d'inspiration pour trouver des idées de structure et de fond, même sans les copier tels quels

## Cas d'usage reels
- [[]]
