---
tags: [formation, millenium]
module: Formation IA
section: "Maîtriser la suite Google AI"
source_transcript: "0.45 Google AI Studio.txt"
---

# 0.45 Google AI Studio

## Resume
- Sommaire de la présentation de Google AI Studio : introduction, Playground Gemini, modèles pour code et chat, génération d'images et vidéos, visualisation et coûts des modèles, comparaison Gemini Pro vs Flash, coûts de génération d'images, modèles inférieurs pour tâches basiques, audio natif et text-to-speech, instructions système et clé API, outils avancés.
- Introduction à Google AI Studio, décrit comme un playground permettant de s'amuser avec l'ensemble des applications Google, un mélange de plusieurs outils réunis en un seul endroit, comparable dans l'esprit au Playground de ChatGPT présenté précédemment.
- Présentation des modèles disponibles dans Google AI Studio : Gemini 3 Pro, Nano Banana Pro, avec anticipation de futures versions (Gemini 3.5 ou 4). Présentation des modèles dédiés au code, raisonnement et chat, avec un appel à l'action pour construire des applications directement avec Gemini, détaillé plus tard dans la partie « build ».
- Détail des coûts d'utilisation par tokens : environ 2$ pour 1 million de tokens en entrée texte, 12$ pour 1 million en sortie. Pour les images, la tarification diffère : 120$ pour 1 million de tokens en entrée, mais 0,134$ par image générée en sortie, illustrant un modèle de facturation hybride entre tokens et unités.
- Détail des coûts des modèles audio : Native Audio avec une meilleure qualité sonore en sortie (12$/million tokens), et Gemini Pro Text-to-Speech avec 20$/million tokens en sortie contre seulement 1$/million en entrée, illustrant la différence de coût entre ce qu'on envoie et ce qui est généré.
- Démonstration de la création d'instructions système personnalisées (exemple : « Shorts Expert »), rédigées via Gemini ou Claude, réutilisables ensuite dans AI Studio. Présentation du champ clé API, permettant de connecter sa propre clé pour lever les restrictions et accéder à tous les modèles.
- Présentation de la fonctionnalité URL Context, qui permet au modèle d'explorer automatiquement le contenu autour d'une URL fournie. Présentation des réglages Top P et Output Length (longueur de sortie), avec une limite maximale de 65 000 tokens en réponse.
- Présentation des Stop Sequences et des filtres de modération configurables : harcèlement, discours haineux, contenu sexuellement explicite, contenu dangereux, chaque catégorie pouvant être ajustée selon le seuil de tolérance souhaité.
- Démonstration comparative en direct entre les modèles Flash et Pro sur une question liée au TDAH : l'auteur note que la différence n'est pas très marquée entre ces deux modèles proches, mais qu'elle deviendrait significative avec un modèle de moindre qualité.
- Les deux réponses comparées (chunking, fragmentation, externalisation de la mémoire de travail) sont jugées globalement similaires en qualité. L'auteur propose de refaire le test avec un modèle nettement moins performant pour visualiser une différence plus nette, ce dernier terminant en seulement 10 secondes.
- Conclusion de la comparaison : la qualité n'est clairement pas la même avec un modèle inférieur. Transition vers la partie considérée comme la plus intéressante de Google AI Studio : la partie « Build », qui sera abordée en plusieurs étapes en commençant par la galerie d'exemples.
- Présentation de la navigation de la partie Build : galerie, mes apps, FAQ. La galerie contient des exemples d'outils créés avec différents modèles Google, notamment des créations utilisant VO, le modèle de génération vidéo de Google.
- Mention d'une interface MCP permettant d'améliorer ses propres interfaces créées. Définition centrale de la partie Build : elle permet de construire des mini-applications, sans prétendre être l'endroit idéal pour créer une application ultime et complète.
- Avantage clé de la partie Build : une intégration très facilitée avec l'écosystème Gemini et les clés API, l'application générée utilisant directement le modèle 2.5 Flash avec des instructions système et sa propre clé API si nécessaire.
- Bref aparté technique sur un léger scintillement d'écran (probablement lié à Google), résolu par un rafraîchissement de page. L'auteur annonce vouloir passer rapidement en revue plusieurs exemples de la galerie sans s'attarder longuement sur chacun.
- Rappel du principe méthodologique central de l'auteur (« cheval de bataille ») appliqué à la création d'applications : réfléchir en deux temps, d'abord générer le meilleur prompt possible, puis utiliser ce prompt pour construire l'application, plutôt qu'une demande vague qui donnerait un résultat médiocre.
- Démonstration concrète : générer un prompt spécialisé pour créer une mini-application de todo list avec coach de productivité, structurée selon le modèle goal/project/tasks, sans base de données (stockage local), en détaillant les spécifications le plus précisément possible.
- Suite de la spécification détaillée de l'application : options Multi-Select, structure de sortie précisant l'identification de l'ICP, les Apollo Search Keywords, et une matrice de huit critères notés, illustrant le niveau de détail nécessaire pour un bon résultat.
- L'auteur affine le rendu visuel de l'application par itérations successives : le fond généré ne correspond pas exactement à sa demande mais s'en inspire, puis il ajuste les textes explicatifs jugés illisibles en raison d'une couleur trop bleue.
- Finalisation de l'application : remplacement du logo par celui de Millenium (via un lien d'image externe car le stockage direct n'était pas possible) et ajustement du sous-titre à plusieurs reprises jusqu'à obtenir un résultat satisfaisant.
- Bilan de la création : seulement 4-5 prompts ont suffi une fois la bonne base posée. Présentation des options finales : télécharger le fichier de l'application, la publier sur GitHub, ou surtout la déployer directement depuis Google AI Studio, décrit comme le véritable avantage de l'outil.
- Démonstration du processus de déploiement avec un nom de domaine personnalisé (millenium.cx) : configuration des DNS records, avec une hésitation de l'auteur qui annule par précaution pour ne pas modifier son URL de production existante.
- L'auteur supprime un déploiement test pour éviter tout conflit, puis confirme que le processus de déploiement final est très simple à condition d'avoir un bon point de départ, que ce soit au niveau du design ou des spécifications techniques.

## Concepts cles
- plan de présentation de Google AI Studio
- Google AI Studio comme playground unifié
- comparaison avec le Playground ChatGPT
- panorama des modèles disponibles (Gemini 3 Pro, Nano Banana Pro)
- fonctionnalité de construction d'applications avec Gemini
- tarification par tokens (texte)
- tarification par image générée
- coûts Native Audio vs Text-to-Speech
- asymétrie de coût entrée/sortie
- instructions système personnalisées réutilisables
- clé API personnelle pour lever les restrictions
- URL Context pour explorer une page web
- réglages Top P et longueur de sortie (max 65000 tokens)
- Stop Sequences
- filtres de modération configurables (harcèlement, haine, contenu explicite, dangereux)
- comparaison Flash vs Pro peu significative entre modèles proches
- comparaison avec un modèle de moindre qualité
- rapidité accrue mais qualité moindre
- conclusion sur la différence de qualité entre modèles
- transition vers la partie Build
- navigation de la partie Build (galerie, apps, FAQ)
- exemples utilisant VO (modèle vidéo Google)
- interface MCP pour améliorer les interfaces créées
- Build = création de mini-applications, pas d'applications complètes
- intégration facilitée avec Gemini et clés API
- usage du modèle 2.5 Flash par défaut dans les apps générées
- parcours rapide de plusieurs exemples de la galerie
- principe des deux temps appliqué à la création d'applications
- risque d'un prompt vague donnant un résultat médiocre
- exemple concret : todo list avec coach de productivité
- structure goal/project/tasks sans base de données
- structure de sortie détaillée (ICP, matrice 8 critères)
- niveau de détail nécessaire dans les spécifications
- itérations d'ajustement visuel (fond, lisibilité du texte)
- remplacement de logo via lien externe
- processus itératif jusqu'au résultat final
- 4-5 prompts suffisants avec une bonne base
- déploiement direct comme avantage clé
- déploiement avec domaine personnalisé
- configuration des DNS records
- suppression pour éviter les conflits de déploiement
- simplicité du déploiement final avec un bon point de départ

## Outils mentionnes
- Google AI Studio
- ChatGPT
- Gemini
- Nano Banana
- Claude
- VO
- Apollo
- GitHub

## Tips techniques
- Rédiger les instructions système via Gemini ou Claude avant de les copier dans AI Studio pour un résultat plus abouti
- Toujours générer le meilleur prompt possible avant de construire une application plutôt que de demander directement un résultat vague
- Poser une bonne base de spécifications dès le départ permet de finaliser une application en seulement 4-5 prompts

## Cas d'usage reels
- [[]]
