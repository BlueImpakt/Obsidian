---
tags: [formation, millenium]
module: Formation IA
section: "Comprendre l'Automatisation"
source_transcript: "1.03 Installer N8N avec Railway,.txt"
---

# 1.03 Installer N8N avec Railway,

## Resume
- Introduction à l'installation de N8n en open source, précédée d'une explication du concept d'open source lui-même, indispensable pour comprendre l'installation sur un serveur personnel.
- Explication du modèle d'achat unique et de ses limites économiques : rentable au début mais rapidement perdant sur le long terme, un modèle plus courant sur les applications mobiles que sur les SaaS (services hébergés sur Internet).
- Introduction du modèle freemium (exemple Adobe avec plus de 5000 utilisateurs mentionnés) puis présentation du dernier modèle principal à connaître : l'open source, en excluant volontairement les sous-modèles secondaires comme l'affiliation.
- Anecdote personnelle sur l'évolution de la perception de l'open source : historiquement perçu comme des alternatives « cheap » et dégradées aux outils propriétaires, une nouvelle génération d'outils open source (dont N8n) est devenue aussi bonne, voire meilleure, que les alternatives payantes.
- Explication de la différence fondamentale entre cloud et open source : le cloud implique un abonnement en échange d'une responsabilité du fournisseur envers l'utilisateur (maintenance, disponibilité, support).
- Analyse des avantages/inconvénients du modèle cloud : simplicité d'usage mais coût plus élevé, contrairement au modèle open source qui fonctionne selon une logique différente (auto-hébergement, gratuité du logiciel).
- Précision sur la responsabilité en self-hosting : N8n met à disposition l'image de l'outil sans garantie de support si quelque chose ne fonctionne pas, considérant que l'utilisateur non-payant assume l'entière responsabilité de son installation.
- Présentation d'Elestio, outil personnel de l'auteur (15$/mois) permettant d'accéder facilement à de nombreuses applications open source auto-hébergées, illustré par des exemples comme Ghost, reflétant sa philosophie d'appréciation de l'open source.
- Analogie pédagogique : une image d'installation open source est comparable à un fichier .dmg (Mac) ou .exe (Windows) mais pour le web. Présentation des options d'hébergement possibles (DigitalOcean, Railway) pour déployer ce type d'image.
- Démonstration du déploiement de template sur Railway : offre de 30 jours d'essai ou 5 dollars de crédit gratuit, avec N8n identifié comme l'instance la plus installée, aux côtés d'autres options comme Typebot.
- Démonstration pratique de l'installation de N8n sur Railway, avec passage nécessaire par un plan payant Hobby suite à des limitations de plans gratuits, et gestion d'un petit bug technique rencontré en cours de route.
- Précision sur l'évolution des conditions d'essai Railway (changement des modalités par rapport à avant) : nécessité d'ajouter une carte bancaire pour lancer le plan, puis sélection du template N8n pour lancer l'installation.
- Détail des ressources techniques allouées : 8 Go de mémoire et 8 CPU par container, puis démonstration du déploiement effectif du template incluant l'installation automatique d'une base de données nécessaire.
- Recommandation importante lors de la configuration : activer l'option de workflow history sur 24 heures, utile notamment pour le scraping d'emails. L'instance N8n se lance ensuite avec une gestion relativement simple et accessible.
- Avantage de centraliser l'architecture sur une plateforme comme Railway : possibilité de visualiser et gérer tous les éléments installés au même endroit, avec un déploiement automatique via Docker en arrière-plan.
- Présentation d'options avancées pour les utilisateurs techniques : possibilité de chercher des modèles directement, avec recommandation d'augmenter la capacité serveur pour éviter des temps de réponse trop longs, et mention de serveurs MCP disponibles également.
- Présentation d'une alternative d'installation via un service VPS dédié : sélection de l'application N8n, choix d'un emplacement géographique (exemple : France), configuration d'un mot de passe serveur, illustrant une méthode alternative à Railway.
- Détail tarifaire de cette alternative VPS : environ 6,99€ sur un engagement de 24 mois (prix plus élevé sur engagements plus courts). L'auteur note que cette solution simple devient moins intéressante à mesure que l'usage d'automatisation augmente en intensité.
- Comparaison de benchmarks de modèles par catégorie : sur l'édition d'images, un modèle domine largement avec 8 millions de votes, un écart très net par rapport aux concurrents selon les classements observés.
- Confirmation de la domination de VO3 sur les catégories texte-vers-vidéo et image-vers-vidéo dans les benchmarks. Mention d'un autre outil (Copilot) dont les données de classement datent d'environ 120 jours, donc potentiellement obsolètes.
- Retour d'expérience de l'auteur confirmant que Claude reste globalement le meilleur sur la plupart des tâches quotidiennes (sans nécessiter systématiquement la version Pro), suivi de Gemini (bon mais avec de gros défauts en coding) et de GPT-5 jugé moyen selon les vrais benchmarks.
- Mise en garde méthodologique sur les benchmarks : un score de proximité élevé ne garantit pas forcément une meilleure intelligence pratique, les benchmarks pouvant être orientés pour valoriser certains aspects. L'auteur introduit un critère complémentaire essentiel : le coût par tâche.
- Présentation d'une fonctionnalité pratique sur N8n : changer de modèle en un clic, voire de façon dynamique selon le contexte des réponses. Introduction d'un tableau comparatif des prix par modèle selon le nombre de tokens en entrée.
- Chiffres de tarification Claude : Opus coûte 15$ par million de tokens en entrée et 75$ en sortie (très cher), tandis que Sonnet (largement utilisé par l'auteur) offre un contexte d'1 million de tokens pour 3$ en entrée et 15$ en sortie, un rapport qualité/prix bien plus favorable.
- Poursuite de la comparaison tarifaire sur d'autres modèles : Qwen 3 et Mistral Medium (environ 0,40€), jugés honnêtes en rapport qualité-prix. L'auteur recommande systématiquement de comparer les prix avant de choisir un modèle pour un usage donné.

## Concepts cles
- nécessité de comprendre l'open source avant l'installation de N8n
- limites économiques du modèle d'achat unique
- distinction SaaS vs applications mobiles
- modèle freemium (exemple Adobe)
- focus sur les modèles principaux (open source)
- évolution de la perception de l'open source (de dégradé à compétitif)
- différence fondamentale cloud (responsabilité fournisseur) vs open source
- avantages/inconvénients comparés cloud (simple mais cher) vs open source
- absence de garantie de support en self-hosting gratuit
- Elestio comme solution d'hébergement simplifié (15$/mois)
- analogie image d'installation web = fichier .dmg/.exe
- options d'hébergement (DigitalOcean, Railway)
- essai gratuit Railway (30 jours ou 5$ de crédit)
- N8n comme instance la plus populaire
- passage obligatoire par un plan Hobby payant
- gestion d'un bug d'installation
- évolution des conditions d'essai Railway (carte requise)
- ressources allouées (8Go RAM, 8 CPU)
- installation automatique de base de données
- activation recommandée du workflow history (24h)
- centralisation de la gestion via Railway (Docker)
- options avancées (recherche de modèles, serveurs MCP)
- recommandation d'augmenter la capacité serveur
- alternative d'installation via VPS dédié
- choix de la localisation géographique du serveur
- tarification VPS selon durée d'engagement (6,99€/24 mois)
- limite de la solution simple face à un usage intensif
- domination nette d'un modèle sur l'édition d'images (8 millions de votes)
- domination de VO3 sur texte-vers-vidéo et image-vers-vidéo
- obsolescence potentielle des données de classement (120 jours)
- classement personnel Claude > Gemini > GPT-5 (usage quotidien)
- limite des benchmarks (orientation possible)
- introduction du critère coût par tâche
- changement de modèle dynamique sur N8n
- tableau comparatif de prix par tokens
- tarification Claude Opus (15$/75$ par million de tokens)
- tarification Claude Sonnet (3$/15$, contexte 1M tokens)
- tarification Qwen 3 et Mistral Medium
- recommandation de comparaison systématique des prix

## Outils mentionnes
- n8n
- Adobe
- Elestio
- Ghost
- DigitalOcean
- Railway
- Typebot
- Docker
- VO3
- Claude
- Gemini
- GPT-5
- Qwen
- Mistral

## Tips techniques
- Utiliser un service comme Elestio pour simplifier l'auto-hébergement de multiples outils open source
- Toujours activer le workflow history sur 24h lors de l'installation N8n, particulièrement utile pour les workflows de scraping d'emails
- Ne jamais se fier uniquement aux scores de benchmarks : toujours considérer aussi le coût réel par tâche
- Configurer un changement de modèle dynamique sur N8n selon le contexte plutôt que de rester figé sur un seul modèle
- Toujours comparer les prix de plusieurs modèles avant de faire un choix, en fonction de l'usage spécifique visé

## Cas d'usage reels
- [[]]
