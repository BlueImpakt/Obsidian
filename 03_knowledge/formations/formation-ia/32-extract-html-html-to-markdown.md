---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.2 Extract HTML  HTML to Markdown.txt"
---

# 3.2 Extract HTML / HTML to Markdown

## Resume
- Introduction au node ExtractHTML, directement lié au module RSS précédent : une fois un feed récupéré, ce node permet d'en extraire le contenu utile de manière structurée.
- Démonstration du contenu HTML brut d'un flux RSS et présentation des différentes méthodes disponibles pour le nettoyer et n'en récupérer que le texte utile, sans le bruit de la mise en forme.
- Présentation des options avancées d'ExtractHTML : possibilité de styliser une table HTML personnalisée et de capitaliser les en-têtes, mais focus principal sur l'extraction de contenu HTML pur, l'usage le plus courant.
- Configuration de l'extraction au format Text pour tous les éléments, puis introduction des CSS Selectors, permettant d'indiquer précisément quelle structure HTML cibler pour l'extraction.
- Exemple de sélecteur CSS pour cibler les paragraphes (balise P), avec renvoi vers une ressource externe pour approfondir la connaissance des différents sélecteurs HTML (classe, type, balise de base).
- Présentation des sélecteurs les plus utiles : H1 à H5 (titres), P (paragraphes/texte), et A (ancres/liens), particulièrement importants pour extraire le contenu structuré d'une page web.
- Démonstration pratique de filtrage : combiner H1 à H6 et P pour extraire tout le texte structuré, retourné sous forme de liste, avec ajout d'une seconde valeur ciblant spécifiquement les liens.
- Constat que le retour en simple bloc de texte n'est pas idéal quand il y a plusieurs éléments distincts, illustrant la nécessité d'un format en Array plutôt qu'en texte concaténé.
- Confirmation du résultat correct avec plusieurs éléments de texte distincts bien séparés, ainsi que la récupération de tous les liens associés avec leurs attributs (no opener, no referrer, no follow).
- Explication des attributs de tracking de liens (référent = origine du clic), permettant de suivre l'origine du trafic, ainsi que la présentation du style et de la target (destination) de chaque lien.
- Recommandation d'utiliser le node Aggregate pour combiner toutes les valeurs récupérées dans l'Array, avec transition vers la présentation du node HTML to Markdown, très pratique.
- Démonstration du fonctionnement du Markdown avec un exemple pratique sur Google Docs (peu utilisé par l'auteur), montrant la modification automatique du texte via la syntaxe dièse (#).
- Illustration de la hiérarchie des titres Markdown (# à ####) : plus le nombre de dièses augmente, plus le texte devient petit, une convention visuelle standard du langage Markdown.
- Petit souci technique avec l'affichage sur Google Docs (version beta du markdown selon l'auteur), mais confirmation que les fondamentaux du Markdown restent applicables via le module dédié dans N8n.
- Démonstration de la configuration du module HTML to Markdown : connexion du contenu HTML source, définition d'une Destination Key pour spécifier où stocker le résultat converti en sortie.
- Présentation d'options supplémentaires du module, dont la possibilité de placer les URLs à la fin du texte converti, une personnalisation utile selon le format de sortie souhaité.
- Résolution d'un petit souci de duplication d'étape, avec exécution finale du module de conversion Markdown confirmant la bonne transformation du contenu HTML en texte formaté.
- Conclusion de la présentation du module Markdown, avant de poursuivre avec l'étape suivante consécutive au module HTML, clôturant cette section pratique sur l'extraction et la conversion.

## Concepts cles
- introduction à ExtractHTML (lié au module RSS précédent)
- méthodes de nettoyage du HTML brut pour extraire le texte utile
- options avancées ExtractHTML (table stylisée) vs extraction principale de contenu
- configuration au format Text et introduction des CSS Selectors
- sélecteur CSS pour paragraphes (P) et ressource pour approfondir
- sélecteurs clés H1-H5, P et A (ancres/liens)
- combinaison de sélecteurs pour extraire texte et liens séparément
- nécessité du format Array plutôt que bloc de texte unique
- résultat correct avec textes séparés et attributs de liens (nofollow, etc.)
- attributs de tracking de liens (référent, style, target)
- node Aggregate pour combiner les valeurs, introduction de HTML to Markdown
- démonstration du Markdown appliqué à Google Docs
- hiérarchie visuelle des titres Markdown selon le nombre de dièses
- limite de la prise en charge Markdown sur Google Docs vs module N8n
- configuration du module HTML to Markdown (Content, Destination Key)
- option de positionnement des URLs à la fin de la conversion Markdown
- exécution finale et validation de la conversion Markdown
- conclusion de la section Markdown avant l'étape suivante

## Outils mentionnes
- n8n
- Google Docs

## Tips techniques
- Consulter une ressource dédiée aux sélecteurs HTML pour maîtriser les différents types (classe, type, balise) selon le besoin

## Cas d'usage reels
- [[]]
