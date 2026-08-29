---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.08 Fonctions de texte dans N8N • Partie 1.txt"
---

# 3.08 Fonctions de texte dans N8N • Partie 1

## Resume
- Introduction aux fonctions de texte sur N8n basées sur JavaScript, une approche plus proche du code que Make, tout en poursuivant un objectif similaire de manipulation textuelle des données.
- Présentation d'une structure de données avec entreprise et plusieurs contacts associés, visualisée sous forme d'arborescence pour mieux comprendre l'imbrication des différents éléments (contact 0, contact 1, etc.).
- Démonstration de navigation par points pour atteindre une valeur profondément imbriquée (compagnie.name), illustrant la méthode fondamentale de récupération d'information dans N8n.
- Test de la fonction Contains : « TechCorp Solution » ne contient pas « patate » (faux) mais contiendrait « Corp » (vrai), avec retour booléen affiché explicitement dans l'interface pour validation.
- Astuce de raccourci clavier pour créer des crochets (Shift+Option+parenthèse sur Mac) nécessaires pour cibler un élément précis d'une liste de contacts par son index (contact[0]).
- Cas d'usage très utile : séparer un email de son nom de domaine via Split, technique également applicable pour extraire des éléments individuels d'une liste de tags multiples.
- Démonstration de StartWith et EndWith : tester si un texte commence ou termine par une chaîne spécifique (exemple : « .com »), avec avertissement sur l'importance de bien gérer les parenthèses dans la syntaxe.
- Explication du problème d'ambiguïté des guillemets imbriqués : quand une string contient elle-même des guillemets, le système ne peut pas identifier clairement les limites de la chaîne visée.
- Solution au problème des guillemets imbriqués : utiliser des apostrophes pour délimiter le texte contenant des guillemets, ou inversement des guillemets si le texte contient des apostrophes.
- Démonstration de Replace All : remplacer « Marie » par « Claude » dans un texte, avec précision qu'un remplaçant doit obligatoirement être défini pour que la fonction s'exécute correctement.
- Cas d'usage concret de Replace All pour normaliser des réponses de formulaire mal orthographiées ou abrégées (exemple : remplacer « TCS » par « TechCorp Solution »), une technique de nettoyage de données très utile.
- Démonstration de la fonction Length, simplement le nombre de caractères d'un texte, avec exemple de calcul additionné (8+9+1 espace = 18 caractères au total).
- Présentation de l'encodage utile pour d'anciennes API nécessitant l'encodage combiné du mot de passe et du nom d'utilisateur au format Base64, une pratique parfois encore requise avec certains systèmes legacy.
- Démonstration de la fonction Concat pour combiner deux textes (exemple : compléter « Marie » mal renseigné en « Marie-Agnès » en concaténant le nom complet manquant à la valeur existante).
- Présentation d'Extract Domain, utile pour extraire uniquement le nom de domaine d'une URL (exemple : youtube.com), fonctionnant précisément avec une vraie URL mais échouant sur du texte non conforme.
- Présentation d'Extract URL Path : extrait la portion du chemin après le domaine (exemple : /video/theo à partir de youtube.com/video/theo), complétant les fonctions d'analyse d'URL disponibles.
- Explication du système hexadécimal (0-9 puis A-F) comme moyen d'encoder des valeurs numériques au-delà de 9 sans utiliser deux chiffres, une base de conversion couramment rencontrée en informatique.
- Introduction de la fonction Quote, utilisée occasionnellement : elle permet d'entourer une valeur de guillemets automatiquement, un usage utile bien que peu fréquent dans les cas d'usage courants.

## Concepts cles
- fonctions de texte N8n basées sur JavaScript (plus proche du code que Make)
- visualisation d'une structure de données en arborescence (entreprise + contacts)
- navigation par points pour atteindre une valeur profondément imbriquée
- test de la fonction Contains avec retour booléen
- raccourci clavier Mac pour créer des crochets (index de liste)
- Split pour séparer email/domaine ou extraire des tags individuels
- fonctions StartWith et EndWith (avec avertissement sur les parenthèses)
- problème d'ambiguïté des guillemets imbriqués dans une string
- solution : alterner apostrophes et guillemets pour éviter les conflits
- fonction Replace All (remplaçant obligatoire)
- cas d'usage de Replace All pour normaliser des abréviations dans les formulaires
- fonction Length (compte de caractères)
- encodage Base64 pour d'anciennes API (mot de passe/utilisateur)
- fonction Concat pour combiner et compléter un texte partiel
- fonction Extract Domain (nécessite une URL valide)
- fonction Extract URL Path (portion après le domaine)
- explication du système hexadécimal (0-9 puis A-F)
- fonction Quote (encadrement de guillemets, usage occasionnel)

## Outils mentionnes
- n8n
- Make

## Tips techniques
- Utiliser Shift+Option+parenthèse sur Mac pour créer facilement des crochets nécessaires à l'indexation d'une liste
- Utiliser Split pour séparer efficacement un email de son domaine, ou pour extraire des éléments individuels d'une liste de tags
- Utiliser des apostrophes pour délimiter du texte contenant des guillemets, et inversement, pour éviter les conflits de syntaxe
- Utiliser Replace All pour normaliser automatiquement les abréviations ou fautes courantes dans les réponses de formulaire

## Cas d'usage reels
- [[]]
