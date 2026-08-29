---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.07 Agent de Newsletter avec X.txt"
---

# 5.07 Agent de Newsletter avec X

## Resume
- Introduction à la création d'un agent de newsletter entièrement automatisé, générant quotidiennement du contenu de bout en bout de manière autonome.
- Réflexion sur l'adaptabilité thématique de l'agent newsletter à tout domaine, avec opportunité business d'aller chercher des professionnels (avocats, entrepreneurs) ayant besoin de ce flux d'informations.
- Démonstration de construction du workflow newsletter dans N8n avec déclencheur quotidien programmé à 5h du matin, première étape de collecte et simplification de données.
- Démonstration de connexion d'un outil HTTP pour scraper des données sur X (Twitter), avec précision que HappyFile n'est pas encore directement disponible pour ce cas d'usage.
- Ajout d'outils complémentaires pour la newsletter : scraping Reddit sur l'intelligence artificielle via HTTP, et Perplexity Deep Research pour approfondir un sujet spécifique.
- Réflexion en direct sur le problème de volume de données du flux RSS, avec décision d'ajouter une étape RSS Read dédiée pour mieux gérer la collecte.
- Décision de combiner ou d'empiler les éléments récupérés (12 items au total) plutôt que de les traiter séparément, malgré un léger bug rencontré en cours de configuration.
- Choix d'un nettoyage complet du contenu via code personnalisé plutôt que via des outils de conversion Markdown standards, pour ne conserver que le texte utile de chaque élément.
- Débogage en direct du nœud de code de nettoyage (Clean Content) rencontrant un bug, illustrant le processus itératif de correction lors de la construction du workflow.
- Correction du code de nettoyage pour retirer un formatage indésirable (notamment sur les apostrophes), illustrant l'affinage itératif nécessaire pour un résultat propre.
- Validation finale du nettoyage des données après plusieurs itérations et rafraîchissements, confirmant que les données sont désormais propres et réutilisables pour la suite du workflow.
- Recommandation méthodologique clé : s'inspirer de la structure d'une newsletter appréciée (pas son contenu) pour cadrer le format de la newsletter générée automatiquement.
- Spécification détaillée de structure de newsletter : 4-5 sujets par jour, sommaire en début, infos en bref à la fin, et mention d'outils tendance devenus viraux.
- Configuration du prompt système intégrant le contenu des newsletters du jour et la date du jour comme variables contextuelles pour la génération automatique.
- Introduction du premier outil connecté à l'agent newsletter, nommé « Xradar », permettant d'obtenir les tendances (top trends) actuelles sur la plateforme X.
- Démonstration d'enrichissement de l'outil X via la documentation Live Search de l'API OpenAI, une ressource utilisée pour construire la requête adéquate.
- Instruction de concision pour l'outil et régénération de la requête curl suite à un problème d'import dans N8n, une résolution technique nécessaire au bon fonctionnement.
- Configuration des seuils de filtrage sur X (View Count minimum 50 000) avec choix de modèle dynamique et mise en garde sur le coût de l'API X, jugé relativement élevé.
- Réutilisation d'un guide de configuration rapide précédemment créé (filtres globaux, config niche) pour accélérer la mise en place des paramètres de l'outil de recherche.
- Transition vers la configuration de l'outil Perplexity Deep Research pour effectuer des recherches plus poussées, avec définition du prompt système correspondant.
- Sélection d'un scraper Reddit facturé au résultat plutôt qu'un abonnement, une préférence méthodologique pour les outils accessibles sans engagement récurrent.
- Configuration de la limite de posts et recommandation d'utiliser un exemple simple pour indiquer à l'agent de récupérer les posts du jour sur des subreddits spécifiques.
- Configuration détaillée du scraper Reddit (subreddit Artificial Intelligence, skip comments/community) avec exemple concret d'URL de subreddit à insérer.
- Analyse des logs du workflow complet : Anthropic identifie les comptes à cibler, Xradar retourne des données, puis Anthropic reformate le contenu reçu en plusieurs passes.
- Étape finale de publication : création automatique d'un document Google Docs via l'action « Create a document », nécessitant une connexion au compte Google déjà expliquée précédemment.

## Concepts cles
- introduction à l'agent de newsletter entièrement automatisé quotidien
- réflexion sur l'adaptabilité thématique et opportunité business de l'agent newsletter
- démonstration de construction avec déclencheur quotidien à 5h du matin
- démonstration de connexion HTTP pour scraper des données sur X
- ajout d'outils complémentaires (Reddit IA, Perplexity Deep Research)
- réflexion sur la gestion du volume de données RSS et ajout d'une étape dédiée
- décision d'empiler les éléments récupérés (12 items au total)
- choix d'un nettoyage complet via code personnalisé plutôt qu'outils standards
- débogage en direct du nœud de code de nettoyage rencontrant un bug
- correction du code de nettoyage pour retirer le formatage indésirable (apostrophes)
- validation finale du nettoyage des données après itérations
- recommandation méthodologique : s'inspirer de la structure (pas du contenu) d'une newsletter existante
- spécification détaillée de structure de newsletter (4-5 sujets, sommaire, tendances)
- configuration du prompt système avec variables contextuelles (contenu du jour, date)
- introduction de l'outil Xradar pour obtenir les top trends de X
- démonstration d'enrichissement via la documentation Live Search de l'API OpenAI
- instruction de concision et régénération de curl suite à un problème d'import
- configuration des seuils de filtrage X et mise en garde sur le coût de l'API
- réutilisation d'un guide de configuration rapide précédemment créé
- transition vers la configuration de Perplexity Deep Research
- préférence méthodologique pour les outils facturés au résultat plutôt qu'à l'abonnement
- configuration de la limite de posts et exemple pour cibler les posts du jour
- configuration détaillée du scraper Reddit (subreddit AI, skip comments)
- analyse des logs du workflow complet multi-étapes (Anthropic, Xradar)
- étape finale de publication automatique dans Google Docs

## Outils mentionnes
- n8n
- Perplexity
- Reddit
- OpenAI
- Anthropic
- Google Docs

## Tips techniques
- Privilégier un code de nettoyage personnalisé plutôt que les outils de conversion standards quand un contrôle plus fin du résultat est nécessaire
- S'inspirer de la structure d'une newsletter existante appréciée, jamais de son contenu, pour cadrer le format de sa propre newsletter automatisée
- Surveiller attentivement le coût de l'API X, jugé relativement élevé, lors de la configuration de scraping de tendances
- Privilégier les outils tiers facturés au résultat plutôt qu'à l'abonnement récurrent, une approche plus flexible pour des besoins ponctuels

## Cas d'usage reels
- [[]]
