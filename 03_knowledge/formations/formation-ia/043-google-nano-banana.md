---
tags: [formation, millenium]
module: Formation IA
section: "Maîtriser la suite Google AI"
source_transcript: "0.43 Google Nano Banana.txt"
---

# 0.43 Google Nano Banana

## Resume
- Introduction à Nano Banana Pro, présenté comme le meilleur modèle de génération d'images de Google, devenu la référence de référence depuis plusieurs mois pour la création d'infographies et d'images en général.
- Explication du concept de FPS (Frame Per Second, images par seconde) appliqué à la vidéo : un nombre élevé pour capturer du mouvement rapide (sport), un nombre plus faible (24-30 images/seconde) suffisant pour une personne qui parle simplement.
- Discussion sur la ressemblance stylistique des générations d'images avec certains studios connus (allusion à Miyazaki/Ghibli) : l'auteur nuance l'idée reçue d'un simple entraînement direct sur des œuvres protégées, évoquant plutôt l'influence d'extraits et compilations largement diffusés sur YouTube.
- L'auteur souligne la disponibilité continue du modèle (traitement 24h/24) et introduit les premières règles à connaître avant de rédiger un prompt : sur les photos de personnes ordinaires, il n'y a généralement pas de problématique particulière de génération.
- Présentation d'une instruction de base réutilisable en anglais pour transformer un prompt simple en JSON prompt structuré pour Nano Banana Images, incluant une structure détaillée avec prompt et prompt négatif.
- Exemple concret d'application du style : demander explicitement des « dessins Pixar » pour garantir la cohérence stylistique entre plusieurs images, plutôt qu'un style de dessin animé générique. Recommandation d'utiliser des descriptions séparées par des virgules (style, éclairage, composition) plutôt que de longues phrases.
- Explication du concept de bokeh (effet de flou d'arrière-plan couramment utilisé par les créateurs YouTube) comme élément stylistique à intégrer dans le prompt pour un rendu photographique professionnel.
- Méthodologie en trois étapes pour construire un prompt efficace : clarifier d'abord l'objectif visuel, puis construire le prompt textuel, et enfin obtenir le JSON complet structuré. L'auteur propose de partager son prompt template pour ceux qui le souhaitent.
- Démonstration d'un prompt écrit de façon informelle et random (scène de pluie à 21h avec reflet de lumière dans une flaque), que le JsonBuilder va automatiquement transformer en prompt structuré très précis, illustrant l'intérêt de cet outil de traduction.
- Règle importante rappelée : ne jamais partager le contexte entre deux images différentes, toujours recommencer une nouvelle génération. Résultat obtenu : image en 1536x1024 malgré l'absence de taille spécifiée, avec possibilité d'affiner davantage (exemple : rendu noir et blanc).
- Astuce pratique de raccourci clavier pour ouvrir une nouvelle discussion (Command/Control + Shift + O), utile pour respecter la règle de non-partage de contexte entre générations d'images sur Nano Banana.
- Démonstration d'une nouvelle génération d'image avec un prompt descriptif détaillé (petit restaurant de rue éclairé à la lanterne, personnes âgées jouant aux cartes). L'auteur relance une tentative dans une nouvelle discussion en mode Pro, anticipant un résultat de meilleure qualité.
- Évaluation critique du résultat obtenu : jugé « mid » (moyen) car l'ambiance n'est pas assez nocturne malgré la demande. L'auteur reformule en insistant explicitement sur le fait que l'image et l'atmosphère doivent impérativement être de nuit, illustrant l'importance d'insister sur des critères non respectés.
- Clarification : Nano Banana est en réalité directement intégré dans Gemini, donc le même outil. L'auteur explique qu'on peut ouvrir deux discussions séparées, ou créer sa propre Gem dédiée à la génération d'images comme alternative organisationnelle.
- Résultat partiellement raté (image scindée en deux involontairement) mais dont l'esthétique se rapproche de ce que l'auteur recherchait. Il relance une nouvelle tentative, estimant que le problème ne vient probablement pas directement du prompt lui-même.
- Introduction de termes techniques cinématographiques dans le prompt : style IMAX, fort contraste, Anamorphic Flare (effet large avec reflets bleus ou ambrés typiques du format anamorphique), donnant un rendu jugé très satisfaisant, comparable à un écran de cinéma en haute résolution.
- Nouvelle méthode présentée : identifier un style de miniature très propre pour pouvoir le réutiliser, en s'inspirant d'un créateur YouTube apprécié par l'auteur (Callaway) et en copiant l'URL d'une de ses vidéos aux miniatures particulièrement réussies.
- Démonstration de reverse engineering d'une miniature existante : définir un rôle (« meilleur prompt engineer du monde spécialisé en analyse et génération d'images avec Nano Banana Pro »), puis coller l'image de la miniature pour que le modèle en décrive précisément la composition.
- Une fois la description obtenue, l'auteur demande la transformation en JSON prompt adaptable à n'importe quelle nouvelle thématique, sans se cadrer sur le compte spécifique, pour obtenir un template flexible mais fidèle au design initial identifié.
- Exemple concret de brief personnalisé intégrant des logos spécifiques (dont N8N) et une courbe symbolisant la monétisation réussie de l'activité. L'auteur définit un rôle de « meilleur JSON prompt engineer pour Nano Banana Pro » en remplissant des variables de brief pour générer un prompt sur-mesure référençant explicitement les logos mentionnés.
- Retour sur Gemini pour une nouvelle approche : fournir quatre images de référence (dont une image de base type miniature) plutôt qu'un simple prompt textuel, pour orienter la génération de manière plus visuelle et précise.
- Présentation d'un outil complémentaire : l'extension Brand Fetch sur Raycast (lanceur d'applications disponible sur Mac et Windows), permettant de récupérer facilement des logos de marques via l'App Store de Raycast.
- Démonstration pratique de Brand Fetch : taper « BR » suivi du nom d'une marque (ex: Claude) dans Raycast permet de sauvegarder ou copier directement le logo dans le presse-papier, pour l'intégrer ensuite dans une génération d'image.
- Suite de la démonstration avec le logo OpenAI : l'auteur anticipe le besoin d'une version sombre du logo (car fond blanc par défaut) et choisit spécifiquement le format PNG pour pouvoir l'ouvrir et le copier facilement dans le navigateur.
- L'auteur active le mode Pro pour générer une miniature complète, en espérant que le modèle ne refuse pas de traiter une image le représentant en tant que personnalité publique (contrainte de modération potentielle sur les visages).
- Le modèle traite le JSON prompt fourni, clarifie et adapte automatiquement certains éléments avant génération. L'auteur est satisfait du résultat bien qu'imparfait niveau ressemblance faciale, jugeant la miniature globalement réussie et esthétique.
- Analyse du résultat : le fond a bien été conservé mais manque de détail avec un léger effet de bavure, jugé acceptable. Démonstration d'une modification demandée : ajuster la grille de fond avec des points type canevas à une opacité de 0,5.
- Mise en garde importante : ne pas passer par un outil comme Claude pour repartir de zéro à chaque itération de visage risque de dégrader progressivement la ressemblance, le rendu final pouvant finir par ne plus du tout correspondre à l'original souhaité.
- L'auteur note qu'un résultat propre peut être obtenu facilement sans sur-préciser chaque détail du template, le texte généré étant naturellement cohérent et bien cadré. Objectif suivant : remplacer les quadrillages de l'image par une image fournie en superposition.
- L'auteur note que ChatGPT est parfois moins réactif à la génération d'images directe, nécessitant de préciser explicitement « génère l'image », alors qu'ici (sur Nano Banana/Gemini) le modèle a bien compris malgré des instructions minimales.
- Bilan positif : le modèle a bien respecté la consigne pour le visage, avec un seul écart notable sur le format (marges légèrement mangées, format 1280x720 non respecté précisément) et l'oubli d'un élément (une chaise) à retirer via une instruction complémentaire.
- L'auteur relance une demande de retrait d'un élément non désiré (une chaise) qui n'avait pas été pris en compte initialement. Résultat final jugé assez créatif malgré un léger écart sur l'ambiance nocturne demandée précédemment, illustrant l'itération progressive nécessaire pour affiner un rendu.

## Concepts cles
- Nano Banana Pro comme référence Google en génération d'images
- FPS (Frame Per Second) et son influence sur le rendu
- nuance sur l'origine du style visuel des modèles (Miyazaki)
- influence des contenus largement diffusés en ligne
- disponibilité continue du modèle
- règles de base avant de prompter
- instruction de base pour générer des JSON prompts
- structure prompt/prompt négatif
- référence stylistique explicite (Pixar) pour la cohérence
- descriptions courtes séparées par virgules plutôt que phrases longues
- effet bokeh comme élément stylistique de prompt
- méthodologie en trois étapes (objectif, prompt, JSON)
- JsonBuilder transformant un prompt informel en prompt structuré
- règle : ne jamais partager le contexte entre deux images
- taille par défaut générée (1536x1024)
- raccourci clavier pour nouvelle discussion (Cmd/Ctrl+Shift+O)
- prompt descriptif détaillé (scène de rue)
- génération en mode Pro dans une nouvelle discussion
- insistance explicite sur un critère non respecté (nuit)
- Nano Banana intégré nativement dans Gemini
- organisation via Gem dédiée ou discussions séparées
- résultat partiellement raté mais esthétique proche de l'objectif
- vocabulaire cinématographique (IMAX, Anamorphic Flare)
- rendu haute résolution façon écran de cinéma
- méthode d'inspiration à partir d'un créateur de référence
- copie d'URL vidéo comme point de départ
- reverse engineering d'une miniature existante
- rôle expert pour l'analyse d'image
- transformation en JSON prompt adaptable et réutilisable
- template flexible fidèle au design initial
- brief personnalisé avec logos et symboles spécifiques
- variables de brief pour un prompt sur-mesure
- utilisation de plusieurs images de référence (4 images)
- extension Brand Fetch sur Raycast pour récupérer des logos
- recherche de logo via raccourci 'BR' dans Raycast
- choix du format PNG pour la compatibilité
- anticipation de la couleur de fond nécessaire
- mode Pro pour la génération de miniature complète
- contrainte potentielle liée aux personnalités publiques
- adaptation automatique du JSON prompt par le modèle
- compromis entre ressemblance et qualité esthétique
- ajustement fin post-génération (opacité de grille)
- risque de dégradation de ressemblance en repartant de zéro à chaque itération
- résultat cohérent sans sur-précision du template
- remplacement de zones par superposition d'image
- différence de réactivité ChatGPT vs Nano Banana pour la génération directe
- respect global de la consigne avec écarts mineurs (format, élément oublié)
- itération progressive pour affiner le rendu final

## Outils mentionnes
- Nano Banana
- Gemini
- YouTube
- n8n
- Raycast
- Brand Fetch
- Claude
- OpenAI
- ChatGPT

## Tips techniques
- Utiliser une instruction de conversion en JSON prompt structuré plutôt que de rédiger un prompt libre directement
- Utiliser des descriptions courtes séparées par des virgules (style, éclairage, composition) plutôt que des phrases longues
- Clarifier d'abord l'objectif visuel avant de rédiger le prompt textuel, puis seulement générer le JSON structuré
- Ne jamais partager le contexte d'une image avec une autre génération : toujours recommencer une nouvelle conversation
- Utiliser le raccourci Cmd/Ctrl+Shift+O pour ouvrir rapidement une nouvelle discussion et éviter le partage de contexte
- Insister explicitement et de façon répétée sur un critère visuel non respecté (ex: heure de la journée) pour forcer sa prise en compte
- Utiliser du vocabulaire cinématographique précis (IMAX, Anamorphic Flare) pour obtenir un rendu visuel de qualité cinéma
- S'inspirer d'un créateur dont les miniatures sont reconnues comme références visuelles pour bâtir son propre style
- Faire décrire une image existante par un modèle pour en extraire un prompt réutilisable (reverse engineering)
- Générer un JSON prompt adaptable à n'importe quel sujet à partir d'un design de référence, pour le réutiliser en template
- Utiliser l'extension Brand Fetch sur Raycast pour récupérer rapidement le logo officiel d'une marque connue
- Éviter de repartir de zéro à chaque itération de visage pour ne pas dégrader progressivement la ressemblance
- Préciser explicitement 'génère l'image' sur ChatGPT si le modèle n'exécute pas la génération automatiquement
- Préciser explicitement le format exact en pixels (ex: 1280x720) si le rendu final doit être strictement respecté

## Cas d'usage reels
- [[]]
