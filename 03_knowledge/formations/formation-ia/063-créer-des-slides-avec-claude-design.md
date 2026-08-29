---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un expert sur Claude"
source_transcript: "0.63 Créer des slides avec Claude Design.txt"
---

# 0.63 Créer des slides avec Claude Design

## Resume
- Sommaire de la vidéo sur Claude Design : introduction, concept et philosophie, stratégie de design itératif, mise en place d'un design system, configuration et génération.
- Introduction à Claude Design : présentation de ses capacités et de ce qu'il peut potentiellement remplacer. L'auteur précise qu'au moment de l'enregistrement, l'outil est encore en Research Preview, donc en phase de test limitée.
- Contexte de Claude Design présenté comme une extension naturelle des capacités de codage croissantes de Claude, décrit comme une sorte de « Figma inversé » par rapport à l'outil de design traditionnel bien connu des designers.
- Explication de la démarche inversée de Claude par rapport à Figma : alors que Figma construit d'abord visuellement l'interface (layers, composants) avant de la transposer en code, Claude part de la démarche inverse en générant directement du code pour produire le design.
- Application du principe d'itération au design : plutôt que de chercher le prompt parfait dès le premier essai (comme pour une miniature), il est plus efficace de procéder par itérations successives en précisant progressivement le style souhaité, plutôt que de tout formaliser d'un coup.
- Démonstration pratique : l'auteur ajoute un design system existant (le sien, qu'il partage en ressource complémentaire) pour créer un slide deck basé sur cette identité visuelle prédéfinie, illustrant l'intérêt de réutiliser une base cohérente.
- Présentation de la bibliothèque d'exemples disponibles : fichiers récents, designs personnels, et exemples fournis, incluant des interfaces plates ou des mini-animations (text streaming, cartes à effet iridescent, loader animé façon globe).
- Démonstration du choix typographique pour le design system : sélection d'une police au style « Grotesque » puis import d'une seconde police (Manier Heavy Italic) pour compléter l'identité visuelle du projet.
- Finalisation de l'import des polices, puis nommage du design system (« Millenium Design System ») et ajout du code copier-coller correspondant, illustrant la précision technique possible dans la configuration.
- Revue détaillée des paramètres du design system généré : ombres et lueurs (Shadows/Glows), familles typographiques, échelle de tailles de texte, petits labels, couleur de succès modifiée — l'auteur validant la plupart des choix par défaut proposés.
- Suite de la revue : cartes (8 pixels de rayon), badges et pills avec effet de reflet, champs de saisie avec coins nets (sharp) à 8 pixels — l'auteur validant globalement la cohérence esthétique proposée automatiquement.
- Une fois le design system finalisé, il peut être publié et partagé. Présentation des options complémentaires : variation de modèle, ajout de fichiers, dictée vocale pour discuter, bien que l'auteur souligne que ce ne sont pas les fonctionnalités les plus importantes.
- Courte séquence de navigation où l'auteur cherche parmi plusieurs designs enregistrés lequel correspond au bon projet à utiliser pour la suite de la démonstration.
- Le design est retrouvé, renommé « Millenium DS » puis publié et défini comme modèle par défaut, permettant ensuite de déclencher facilement de nouveaux designs basés sur cette identité visuelle réutilisable.
- Démonstration de la création d'un projet de présentation : sélection du type (présentation), lancement de la création, et possibilité de générer un slide deck à partir d'une présentation existante ou d'un contenu brut fourni.
- Choix du modèle sous-jacent (Opus 4.7 ou 4.6 selon préférence) et ajout de fichiers de référence et d'images pour donner du contexte. L'exemple choisi porte sur Dario Amodei, fondateur de Claude, pour illustrer une présentation thématique complète.
- Présentation d'un outil complémentaire pratique, Dropover, permettant de créer des petits « shelves » temporaires pour glisser-déposer facilement des images (logos, visuels) avant de les intégrer à la présentation en cours de construction.
- Poursuite de la collecte d'assets visuels : récupération du logo OpenAI en version blanche pour compléter la présentation, illustrant la démarche méthodique de rassemblement de ressources graphiques avant génération.
- Suite de la collecte d'images, avec possibilité d'en ajouter autant que nécessaire. L'auteur note un ralentissement technique passager, sans que cela n'affecte la faisabilité de l'upload de multiples fichiers organisés en dossier.
- Claude pose systématiquement des questions de cadrage avant de générer la présentation : durée souhaitée (15-20 minutes), public cible, style narratif (cinématique, storytelling, dramatique, ton « strict Millenium » avec accent Anthropic), et angle principal de l'histoire (opposition Sam Altman vs Dario Amodei).
- Claude auto-répond à certaines questions en s'appuyant sur le script fourni et met à jour sa liste de tâches (todos) en fonction des fichiers reçus. L'auteur recommande d'envoyer un maximum de contenu, y compris en passant par Claude Code pour préparer le matériel en amont.
- Analyse du résultat généré : mise en page variée et lisible, mais l'auteur note des répétitions de formes visuelles, expliquées par un manque d'images fournies initialement dans le processus de génération.
- Identification du problème principal : un manque d'assets visuels disponibles pour enrichir la présentation. L'auteur montre comment ajouter davantage d'images dans la bibliothèque pour pallier ce manque (exemple : recherche d'images supplémentaires de Sam Altman).
- Démonstration du workflow d'édition par commentaire : sélectionner un élément indésirable (« la lune de miel ne dure pas »), écrire un simple commentaire « supprime », envoyer à Claude qui traite la modification en arrière-plan sans intervention manuelle supplémentaire, avec possibilité d'annoter via dessin.
- Confirmation du bon fonctionnement du workflow de commentaires : l'élément a été supprimé et la nouvelle image intégrée avec succès. L'auteur juge le résultat final exceptionnel, avec possibilité de continuer à affiner des détails précis (ex: couleur d'un élément).
- Conclusion pratique : la seule chose vraiment nécessaire en amont est une bonne bibliothèque d'assets, l'outil se débrouillant ensuite automatiquement pour appliquer les modifications. L'outil est décrit comme un mélange entre prompting intelligent et commentaires successifs, bien au-delà d'un simple outil de prompt.
- Révélation technique importante : le résultat visible n'est pas un fichier PowerPoint propriétaire (.pptx) mais un rendu HTML. L'export en PDF fonctionne différemment de ce qu'on pourrait attendre d'un outil de présentation classique.
- Explication approfondie du mécanisme technique : l'outil ne fonctionne pas comme une surcouche visuelle classique, mais interagit directement avec le HTML via un système d'envoi et de réception de prompts, combiné à une logique de gestion d'assets exploitable.
- Conclusion de la démonstration Claude Design avant transition vers un autre cas d'usage (site web) : présentation des options de partage et collaboration (accès en visualisation/commentaire/édition via lien copiable) et duplication rapide du projet, y compris en tant que template réutilisable.

## Concepts cles
- plan de présentation de Claude Design
- Claude Design encore en phase Research Preview
- Claude Design comme 'Figma inversé'
- démarche inversée de Claude par rapport à Figma (code d'abord vs visuel d'abord)
- itérations successives plutôt qu'un prompt parfait dès le départ
- utilisation d'un design system existant comme base
- bibliothèque d'exemples et d'animations disponibles
- import de polices personnalisées (Grotesque, Manier Heavy Italic)
- nommage et configuration du design system via code
- revue des paramètres visuels du design system généré
- validation des composants UI générés (cartes, badges, inputs)
- publication et partage du design system
- options complémentaires (dictée vocale, fichiers)
- navigation entre plusieurs designs enregistrés
- renommage, publication et définition par défaut du design system
- création d'un projet de présentation à partir d'un contenu existant
- choix du modèle sous-jacent (Opus)
- ajout de fichiers de contexte thématique
- outil Dropover pour organiser les glisser-déposer d'images
- collecte de logos de marques (version blanche pour compatibilité)
- upload multiple de fichiers organisés en dossier
- questions de cadrage systématiques avant génération (durée, public, style, angle narratif)
- auto-résolution de questions via le script fourni
- todos mis à jour automatiquement
- répétitions visuelles dues à un manque d'images initiales
- ajout d'assets supplémentaires pour enrichir visuellement
- édition par commentaire textuel traité en arrière-plan
- annotation par dessin
- validation du workflow de commentaires (suppression + ajout d'image)
- importance clé d'une bonne bibliothèque d'assets en amont
- mix entre prompting intelligent et commentaires itératifs
- rendu HTML plutôt que fichier PowerPoint propriétaire
- particularité de l'export PDF
- mécanisme technique d'interaction directe avec le HTML via prompts
- options de partage et collaboration (lien, commentaire, édition)
- duplication en tant que template réutilisable

## Outils mentionnes
- Claude
- Claude Design
- Figma
- Dropover
- Claude Code

## Tips techniques
- Procéder par itérations successives sur le design plutôt que de chercher le prompt parfait dès le premier essai
- Définir un design system comme modèle par défaut pour gagner du temps sur les futurs projets de présentation
- Utiliser Dropover pour organiser temporairement des images à glisser-déposer avant de les intégrer dans un projet
- Laisser Claude poser des questions de cadrage précises (durée, public, angle) avant de lancer la génération d'une présentation
- Envoyer un maximum de contenu et de contexte à Claude avant génération, quitte à préparer le matériel via Claude Code
- Éditer une présentation via de simples commentaires textuels traités automatiquement en arrière-plan plutôt qu'en modifiant manuellement
- Préparer une bonne bibliothèque d'assets en amont plutôt qu'un prompt parfait : c'est ce qui compte le plus

## Cas d'usage reels
- [[]]
