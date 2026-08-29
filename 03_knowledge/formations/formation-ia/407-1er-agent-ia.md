---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.07 1er agent IA.txt"
---

# 4.07 1er agent IA

## Resume
- Introduction au premier agent IA construit de A à Z, avec présentation d'un mapping visuel préalable du flow à construire, une approche différente et plus complète que les vidéos précédentes.
- Présentation de la structure de l'agent avec trois actions (deux de lecture, une d'écriture dans la base de données), l'email étant délégué à un agent dédié séparé.
- Explication du choix du trigger « On Channel Post » plutôt que « On Message » sur Telegram, permettant de créer différents channels pour différents cas d'usage distincts.
- Démonstration de création d'un nouveau bot Telegram (nommé « Teyo Formation Bot ») avec génération du token d'accès permettant de connecter le bot au workflow N8n.
- Ajout du bot créé à un channel Telegram spécifique, avec précision importante qu'un seul trigger peut être configuré par bot, une limite à connaître pour l'architecture du système.
- Démonstration de configuration des permissions du bot dans le channel (gestion des messages, stories, etc.), une étape effectuée partiellement hors caméra pour protéger la confidentialité des contacts.
- Finalisation des permissions du bot (gestion des vidéos chat activée), avec confirmation de la présence multiple possible de plusieurs bots dans un même channel Telegram.
- Test pratique de déclenchement du workflow via l'envoi de messages Telegram simples (« salut », « c'est cool »), confirmant l'enregistrement correct des messages transmis à l'agent IA.
- Configuration de la mémoire de l'agent IA avec recommandation de définir une clé d'identification unique pour stocker l'ID spécifique de chaque interaction, plutôt que d'utiliser le nœud de chat connecté par défaut.
- Transition vers la connexion des outils externes de l'agent, en commençant par Google Calendar, une étape clé pour donner à l'agent des capacités d'action réelles.
- Démonstration de connexion des credentials Google Calendar API via authentification Google simplifiée (Sign in with Google) pour donner à l'agent l'accès à la création d'événements.
- Présentation des actions disponibles pour Google Calendar (créer, supprimer, obtenir un événement, obtenir plusieurs), avec recommandation d'utiliser « Get Many » pour récupérer tous les événements d'un calendrier.
- Recommandation méthodologique clé : tester chaque étape individuellement au fur et à mesure de la construction de l'agent, plutôt que d'attendre la fin complète pour tout tester d'un coup.
- Insistance sur l'importance d'une nomenclature claire et cohérente des nœuds et outils (ex : « Get Events » ou « Obtenir événements »), essentielle pour que l'agent comprenne correctement quel outil utiliser.
- Premier test complet de l'agent via l'envoi d'un message Telegram (« donne-moi mes événements de la journée »), une étape de validation en conditions réelles du workflow construit.
- Débogage en direct d'un bug de déclenchement (l'automatisation semble passée en arrière-plan), illustrant les aléas fréquents rencontrés lors des premiers tests d'un nouvel agent.
- Identification de la cause réelle du bug : accès non accordé à tous les calendriers de l'utilisateur, nécessitant une reconfiguration des accès pour chaque calendrier concerné.
- Explication de la nomenclature FromAI (« Defined automatically by the model ») : l'IA choisit dynamiquement certaines valeurs (comme l'ID de calendrier) selon le contexte de la requête utilisateur.
- Démonstration de configuration de consignes précises pour l'agent, associant des mots-clés (« voyages », « événements ») à des identifiants de calendrier spécifiques pour un routage correct.
- Clarification en direct d'une confusion entre l'ID du chat et l'ID de l'utilisateur (le sender), deux identifiants distincts mais souvent confondus lors de la configuration.
- Diagnostic via les logs d'un problème de date incorrecte transmise à l'outil Get Events, révélant que l'agent n'avait pas connaissance de la date actuelle, un point à corriger dans la configuration.
- Confirmation du bon fonctionnement final : l'agent récupère correctement les événements du jour et envoie le message attendu, avant transition vers la connexion de l'outil Notion pour la gestion des tâches.
- Diagnostic d'un problème d'accès Notion : la base de données de tâches n'avait pas été partagée avec l'intégration API, une cause fréquente de dysfonctionnement lors de la connexion Notion.
- Poursuite du débogage de la connexion Notion, avec découverte que le problème venait de la gestion des connexions internes multiples, nécessitant de recréer l'intégration correcte.
- Configuration réussie de la récupération des tâches Notion (Get Many, Return All), avec recommandation de simplifier la réponse pour éviter de surcharger l'agent en données inutiles.
- Configuration du filtrage de tâches Notion, avec choix entre construction manuelle du filtre ou délégation à l'IA via JSON, en sélectionnant une propriété spécifique de la base de données.
- Test du flux complet (réveil de l'agent, récupération des tâches, reformulation, envoi de message) révélant qu'aucune tâche n'a été trouvée, nécessitant un retour aux logs pour diagnostiquer.
- Méthode de débogage par suppression progressive des filtres pour isoler le problème : suppression du filtre révélant une réponse vide, confirmant que le filtre construit était en cause.
- Confirmation que le filtre initial ne fonctionnait pas correctement, avec recommandation de reconstruire le filtre manuellement en analysant précisément la structure des données retournées.
- Présentation d'une alternative de filtrage via JSON laissant le modèle gérer la logique, avec recommandation d'ajouter du contexte explicite pour guider l'agent sur la manière de filtrer correctement.
- Validation du fonctionnement après correction : récapitulatif de la journée obtenu avec succès, incluant les leçons du jour, avec observation qu'un contenu non désiré peut être filtré via le prompt.
- Amélioration itérative de la réponse de l'agent : demande d'ajout de liens cliquables pour chaque tâche, permettant d'ouvrir directement la page Notion correspondante depuis le message reçu.
- Observation du temps de traitement de l'agent (environ 30-45 secondes) qui interroge successivement Notion et le calendrier avant de composer et envoyer sa réponse finale via message.

## Concepts cles
- introduction à la construction complète d'un premier agent IA (mapping préalable)
- structure de l'agent : deux actions de lecture, une d'écriture en base de données
- choix du trigger 'On Channel Post' Telegram pour différents cas d'usage
- démonstration de création d'un bot Telegram avec génération de token
- ajout du bot au channel avec limite d'un trigger par bot
- configuration des permissions du bot dans le channel Telegram
- finalisation des permissions et possibilité de plusieurs bots par channel
- test pratique de déclenchement via messages Telegram simples
- configuration de la mémoire d'agent avec clé d'identification unique par interaction
- transition vers la connexion d'outils externes (Google Calendar)
- démonstration de connexion des credentials Google Calendar via authentification simplifiée
- recommandation d'utiliser Get Many pour récupérer tous les événements du calendrier
- recommandation méthodologique : tester chaque étape individuellement pendant la construction
- importance de la nomenclature claire des nœuds pour la compréhension de l'agent
- premier test complet de l'agent via message Telegram réel
- débogage en direct d'un bug de déclenchement (automatisation en arrière-plan)
- identification de la cause du bug : accès manquant à tous les calendriers
- explication de la nomenclature FromAI pour le choix dynamique de valeurs par l'IA
- démonstration de consignes associant mots-clés à identifiants de calendrier
- clarification de la distinction entre ID du chat et ID de l'utilisateur
- diagnostic via logs d'un problème de date incorrecte transmise à l'agent
- confirmation du bon fonctionnement final et transition vers l'outil Notion
- diagnostic : base de données Notion non partagée avec l'intégration API
- poursuite du débogage de connexion Notion (gestion des connexions multiples)
- configuration réussie de récupération des tâches Notion avec simplification recommandée
- configuration du filtrage de tâches Notion (manuel vs délégué à l'IA via JSON)
- test du flux complet révélant un problème de filtre (aucune tâche trouvée)
- méthode de débogage par suppression progressive des filtres pour isoler le problème
- recommandation de reconstruction manuelle du filtre après analyse de la structure des données
- alternative de filtrage via JSON délégué au modèle avec contexte explicite
- validation du fonctionnement après correction et possibilité d'affiner le prompt
- amélioration itérative : ajout de liens cliquables Notion dans la réponse de l'agent
- observation du temps de traitement multi-sources de l'agent (30-45 secondes)

## Outils mentionnes
- n8n
- Telegram
- Google Calendar
- Notion

## Tips techniques
- Définir une clé d'identification unique explicite pour la mémoire de l'agent plutôt que de se reposer sur la connexion par défaut du nœud de chat
- Utiliser l'action Get Many pour récupérer l'ensemble des événements d'un calendrier plutôt que des requêtes individuelles
- Tester chaque étape d'un agent IA individuellement au fur et à mesure de sa construction, plutôt que d'attendre la fin pour tout tester en une fois
- Adopter une nomenclature claire et explicite pour chaque nœud et outil d'un agent, essentielle à sa capacité de choisir le bon outil
- Toujours vérifier que l'accès est accordé à TOUS les calendriers pertinents, pas seulement le calendrier principal, lors de la configuration Google Calendar
- Consulter systématiquement les logs pour diagnostiquer pourquoi un agent transmet une valeur incorrecte (comme une date) à un outil connecté
- Toujours vérifier que la base de données Notion concernée a été explicitement partagée avec l'intégration API utilisée, une cause fréquente d'échec silencieux
- Simplifier systématiquement la réponse d'un nœud de récupération de données volumineuses pour éviter de surcharger inutilement l'agent en tokens
- Supprimer progressivement les filtres d'un nœud pour isoler la source d'un problème de retour vide, une méthode de débogage systématique
- Analyser précisément la structure brute des données retournées avant de reconstruire manuellement un filtre défaillant
- Ajouter du contexte explicite dans le prompt de l'agent pour guider précisément la logique de filtrage attendue, plutôt que de laisser le modèle deviner
- Demander explicitement à l'agent d'inclure des liens cliquables vers les ressources sources (Notion, calendrier) pour faciliter l'action de l'utilisateur

## Cas d'usage reels
- [[]]
