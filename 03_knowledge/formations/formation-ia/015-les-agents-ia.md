---
tags: [formation, millenium]
module: Formation IA
section: "Les Fondamentaux IA"
source_transcript: "0.15 Les Agents IA.txt"
---

# 0.15 Les Agents IA

## Resume
- Introduction au fonctionnement des agents IA, basés sur les fonctions des LLM (notamment le reasoning) appliquées à des outils et des connexions rendues possibles par des technologies comme Longchain. Ce qui différencie un agent IA d'un LLM classique, c'est sa capacité à raisonner sur une demande puis à utiliser des outils/API à sa disposition. Exemple filé : réserver un restaurant, où l'agent doit d'abord identifier les informations nécessaires (date, lieu, style, ambiance, nombre de personnes) avant d'agir.
- Détaille le déroulé concret du raisonnement d'un agent pour réserver un restaurant via l'API TripAdvisor et sa fonction Search Restaurants, en envoyant les critères en paramètres. Insiste sur l'importance de toujours fournir la date du jour car l'agent ne peut pas la déduire seul et l'API échouera sans cette information. Une fois les résultats obtenus, l'agent applique un raisonnement supplémentaire pour filtrer les options selon les contraintes de l'utilisateur (ex. restaurant végétarien).
- Décrit le processus en amont et en aval des interactions de l'agent avec les outils : analyse de la demande, identification de l'action à mener, puis recherche de l'outil adapté. Nouvel exemple : « Quel temps fait-il à Paris ? », où l'agent identifie Paris comme un lieu puis détermine l'intention (la météo) à partir du traitement déjà réalisé par le LLM sur les mots et leur position dans l'espace vectoriel.
- Poursuite de l'exemple météo : l'agent dispose d'une fenêtre contextuelle d'outils (email, calculette, API météo, etc.) et associe la demande à l'outil le plus pertinent par proximité sémantique. Il lit la description de l'outil, puis remplit les paramètres requis en reformatant la demande au format JSON (par exemple insérer 'Paris' dans le champ 'ville'). La requête est envoyée en texte à l'API, qui renvoie une réponse que l'agent reformule pour l'utilisateur.
- Récapitule le principe fondamental de décision des agents, en contraste avec les LLM classiques qui peuvent utiliser des connecteurs MCP mais restent différents des outils d'automatisation comme n8n où Longchain joue un rôle central. Longchain permet d'appliquer des actions à un LLM pour créer un processus agentique capable de raisonner sur plusieurs outils. La liste d'outils disponibles est perçue par l'agent comme du texte au format JSON (un array d'objets avec des propriétés nom et description).
- Explique le mécanisme d'exécution des outils : le LLM ne peut pas exécuter un outil lui-même, c'est Longchain qui intercepte sa demande d'action et l'exécute réellement dans un scénario automatisé. Reprend l'exemple météo pour montrer comment l'agent sélectionne l'action (météo API) et l'input (Paris) correspondant le mieux à la demande utilisateur, en se basant sur le nom et la description de l'outil.
- Longchain convertit la demande formatée en texte en appel API direct, récupère la réponse texte (ex. '15 degrés nuageux') puis l'agent transforme cette donnée brute en réponse naturelle pour l'utilisateur. Introduit la notion que chaque outil possède une fonction, des possibilités et des paramètres définis, illustrée par l'outil 'calculatrice' avec sa description et ses types de paramètres (texte, nombre, booléen).
- Précise qu'on peut définir autant de paramètres que nécessaire pour un outil, mais qu'un nombre trop élevé complique la lecture pour l'agent. Mentionne la possibilité de définir des métadonnées sur les outils. Une fois ce cadre en place, l'agent lit la description de chaque outil disponible et décide, via le reasoning, lesquels lui sont utiles pour répondre à la demande.
- Détaille le raisonnement invisible de l'agent lors de l'usage d'un outil (ex. calculatrice) : identifier l'outil nécessaire, déterminer les valeurs à y insérer, puis exécuter soit une fonction Python soit un appel API pour obtenir le résultat. Rappelle que de nombreux outils plus ou moins complexes peuvent être connectés (API, traitement de documents, bases de données), ce qui permet d'enrichir un LLM grâce à Longchain. Introduit la question suivante : ce qui différencie un agent qui a du contexte.
- Aborde la mémoire comme élément clé différenciant un agent contextualisé. Sans mémoire (ex. navigation privée), chaque interaction avec un LLM repart de zéro et l'IA ne peut pas se souvenir des échanges précédents. Pour créer des agents utiles, il faut donc conserver un minimum de contexte, ce que Longchain permet via trois types de support de mémoire.
- Présente les trois types de mémoire Longchain : la Conversation Buffer Memory (stocke tous les messages précédents, devient vite lourde), la Conversation Summary Memory (résume les anciens messages et garde les derniers complets, plus efficace pour les longues conversations), et la Conversation Buffer Window Memory (garde seulement les X derniers échanges, principalement utilisée sur n8n). Explique aussi qu'un identifiant unique est utilisé pour retrouver le contexte mémorisé, stocké soit dans l'outil, soit dans une base Postgres.
- Détaille le format technique de stockage des messages (JSON avec rôle humain/assistant et contenu), récupérés via un ID avant chaque décision de l'agent. Exemple concret avec ClickUp : associer la mémoire à l'ID unique d'une tâche permet à un agent créateur de scripts YouTube de modifier un script existant plutôt que de le recréer entièrement lors d'une nouvelle interaction, un comportement comparé à celui de Claude qui réécrit des passages plutôt que de tout refaire.
- Conclut sur la mémoire : une fois l'historique disponible, l'agent l'utilise pour décider de la suite, ce qui économise des tokens et améliore l'efficacité en gardant trace des interactions précédentes. Introduit ensuite les Vector Embeddings comme le fait de vectoriser des documents spécialisés pour aller y chercher des informations.
- Décrit le processus des Vector Embeddings : transformer le texte en liste de nombres, comparer les vecteurs similaires, indexer et stocker les documents vectorisés dans une base de données vectorielle (Pinecone ou Supabase). Lors d'une recherche, la question posée est comparée aux vecteurs de cette base spécifique (et non celle du LLM de base), pour renvoyer une réponse enrichie et pertinente à l'agent.
- Illustre la recherche vectorielle avec un exemple sur des documents automobiles : une question sur les moyens de transport terrestre permet de retrouver les passages pertinents. Mentionne l'intégration Longchain VectorStoreRetriever pour effectuer cette recherche, et renvoie vers d'autres leçons (Notebook LM, ajout de données sur ChatGPT) pour approfondir. Introduit ensuite la distinction entre workflow (séquence prédéfinie) et agent.
- Détaille ce qu'est un workflow (séquence d'étapes prédéfinies A, B, C... pouvant inclure une étape IA apportant de la cognitivité) versus un agent, qui offre plus de flexibilité, la capacité de brainstormer et de revenir en arrière contrairement à un workflow qui avance uniquement en avant. Exemple : un script de vente rédigé par un sous-agent rédacteur puis validé par un sous-agent validateur, coordonnés par un agent manager.
- Illustre le risque d'un workflow rigide : si l'agent validateur refuse le résultat, le processus peut se retrouver bloqué ou entrer dans une boucle sans fin en cas de tentative de correction automatique répétée.
- Montre comment un agent manager arbitre entre deux sous-agents et effectue des allers-retours adaptatifs : si le script de vente est noté 6/10 alors qu'il faut minimum 7, l'agent-manager redemande des modifications selon le feedback, permettant orchestration et adaptabilité. Cette flexibilité a une contrepartie : moins de contrôle. Conseille d'utiliser un workflow quand un contrôle factuel et précis est requis (ex. Google Docs formaté exactement), et un agent quand plus de flexibilité décisionnelle est souhaitée.
- Détaille les critères de choix : un workflow convient à un process métier fixe et bien défini nécessitant zéro erreur, car un agent peut planter (fenêtre contextuelle trop grande, perte de repère dans des itérations répétées). Un agent convient quand on veut de la flexibilité et de l'adaptation, comme un assistant de productivité capable de décider quoi faire face à une information manquante (ex. attribuer une liste par défaut dans ClickUp) plutôt que d'échouer comme le ferait un workflow non prévu pour ce cas. Évoque aussi des approches hybrides : agent appelant un sous-workflow au format de sortie strict (ex. une note), ou workflow appelant un agent à une étape spécifique.
- Poursuit l'exemple hybride : un sous-workflow renvoie un format de sortie strict et attendu (ex. 'note 2.7') plutôt qu'une réponse libre. Inversement, un workflow peut appeler un agent à une étape précise pour bénéficier de sa flexibilité (ex. 'comment améliorerais-tu ce truc'), puis reprendre le déroulé normal du workflow. Introduit ensuite l'orchestration multi-agents : spécialisation par domaine, avec des modes séquentiel, parallèle ou hiérarchique.
- Détaille les modes d'orchestration multi-agents : en parallèle (plusieurs agents travaillent simultanément puis un agent conclut ou fusionne les réponses), et hiérarchique (un agent-manager coordonne et distribue les tâches). La communication entre agents repose généralement sur une mémoire partagée et l'échange de messages, potentiellement sauvegardés en base de données. Exemple : agent manager coordonnant un agent recherche, un agent analyse et un agent rédaction pour produire un rapport, exécutables en séquentiel ou sous supervision hiérarchique.
- Précise que dans l'exemple recherche/analyse/rédaction, le mode parallèle n'est pas adapté car l'analyse dépend du résultat de la recherche — une structure hiérarchique avec agent-manager reste toutefois possible. Aborde ensuite comment les données circulent entre agents : texte simple (prompts, questions, réponses, instructions), objets structurés (JSON, XML — XML étant lié aux flux RSS), fichiers (binaires, images, PDF, audio) et métadonnées apportant du contexte sur les outils utilisables.
- Conclut sur le rôle central de Longchain : convertir les formats entre LLM et API (l'agent ne voyant que le texte final du processus). Aborde la gestion des erreurs (échec d'outil, API down, ressource introuvable) : un agent peut décider de tenter autre chose face à une erreur, contrairement à un scénario qui continue simplement avec l'erreur. Met en garde contre le fait de survaloriser les agents par effet de mode, alors que les scénarios/workflows restent parfois tout aussi, voire plus, efficaces. Clôt ce module introductif théorique sur les agents IA.

## Concepts cles
- agent IA vs LLM classique
- reasoning
- réservation de restaurant (cas d'usage)
- utilisation d'outils et d'API par un agent
- appel d'API avec paramètres (Search Restaurants)
- nécessité de fournir un maximum de contexte
- filtrage des résultats selon les contraintes utilisateur
- identification d'action et d'intention
- exemple météo à Paris
- lien entre traitement LLM et détermination d'intention
- fenêtre contextuelle d'outils
- association demande-outil par similarité
- formatage JSON des paramètres d'appel API
- reformulation de la réponse API
- processus de décision agentique
- connecteurs MCP
- structuration JSON de la liste d'outils
- interception et exécution d'outil par Longchain
- sélection d'action et d'input par l'agent
- limite du LLM seul (pas d'exécution directe)
- conversion de format par Longchain
- transformation de données brutes en langage naturel
- paramètres d'un outil (texte, nombre, booléen)
- exemple calculatrice
- complexité liée au nombre de paramètres
- métadonnées d'outil
- sélection des outils nécessaires via reasoning
- exécution via fonction Python ou API
- diversité des outils connectables (documents, bases de données)
- enrichissement du LLM via Longchain
- mémoire d'un agent
- navigation privée et perte de contexte
- trois types de mémoire Longchain
- Conversation Buffer Memory
- Conversation Summary Memory
- Conversation Buffer Window Memory
- identifiant unique pour retrouver le contexte
- stockage mémoire (intégré ou Postgres)
- stockage JSON des messages (rôle + contenu)
- usage d'un ID de tâche ClickUp pour la mémoire contextuelle
- modification incrémentale plutôt que régénération complète
- économie de tokens grâce à la mémoire
- Vector Embeddings
- vectorisation de documents spécialisés
- transformation du texte en vecteurs
- comparaison de similarité vectorielle
- indexation et stockage de documents vectorisés
- base de données vectorielle dédiée vs base du LLM
- exemple recherche vectorielle sur documents automobiles
- VectorStoreRetriever
- distinction workflow vs agent (introduction)
- workflow = séquence prédéfinie
- étape IA dans un workflow
- flexibilité et retour en arrière d'un agent
- architecture agent manager + sous-agents (rédacteur/validateur)
- risque de boucle infinie dans un workflow rigide
- blocage en cas de refus du validateur
- arbitrage par agent-manager avec seuil de validation
- compromis flexibilité vs contrôle
- critère de choix workflow (contrôle strict) vs agent (flexibilité)
- agent qui plante (fenêtre contextuelle, itérations répétées)
- gestion d'information manquante par un agent vs échec d'un workflow
- approches hybrides agent+workflow
- sous-workflow à format de sortie strict
- format de sortie strict pour un sous-workflow
- appel d'un agent à une étape précise d'un workflow
- orchestration multi-agents par spécialisation
- mode séquentiel d'orchestration
- orchestration en parallèle
- orchestration hiérarchique avec agent-manager
- mémoire partagée entre agents
- exemple agent recherche/analyse/rédaction
- dépendance entre étapes empêchant le parallélisme
- formats de circulation des données (texte, JSON, XML, fichiers, métadonnées)
- XML et flux RSS
- conversion de formats par Longchain
- gestion des erreurs par un agent vs un scénario
- mise en garde contre le biais de hype envers les agents
- workflows parfois plus efficaces que les agents

## Outils mentionnes
- Longchain
- TripAdvisor (API)
- API météo
- n8n
- MCP
- Python
- Postgres
- ClickUp
- Claude
- Pinecone
- Supabase
- Notebook LM
- ChatGPT
- Google Docs

## Tips techniques
- Toujours transmettre la date du jour à l'agent, car sans cette information explicite l'API échouera par manque de paramètre
- Éviter de multiplier excessivement les paramètres d'un outil, car cela complique la lecture et la sélection par l'agent
- Utiliser la Conversation Summary Memory pour les longues conversations plutôt que la Buffer Memory, qui devient rapidement trop lourde
- Attribuer un identifiant unique à chaque contexte mémorisé pour pouvoir le retrouver facilement, surtout avec plusieurs agents actifs
- Associer la mémoire d'un agent à un identifiant unique (ex. ID de tâche ClickUp) pour qu'il modifie un contenu existant plutôt que de le regénérer entièrement à chaque demande
- Utiliser un workflow lorsque le contrôle doit être factuel et précis (ex. remplissage exact d'un document) ; utiliser un agent lorsque l'on souhaite plus de flexibilité dans le processus décisionnel
- Privilégier un workflow pour un processus métier fixe nécessitant une fiabilité totale et sans erreur possible
- Privilégier un agent pour un assistant de productivité si l'utilisateur lui-même est peu fiable/précis dans ses demandes, car l'agent peut combler les informations manquantes ou redemander

## Cas d'usage reels
- [[]]
