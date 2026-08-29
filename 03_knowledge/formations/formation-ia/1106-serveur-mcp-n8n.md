---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un expert de n8n"
source_transcript: "11.06 Serveur MCP n8n.txt"
---

# 11.06 Serveur MCP n8n

## Resume
- Sommaire du module Serveur MCP N8n : introduction au MCP, MCP Server Trigger dans N8n, Instance Level MCP, ses bénéfices, comment l'utiliser, connexion via OAuth, et lister les workflows N8n.
- Renvoi vers une vidéo complémentaire de la formation IA expliquant en profondeur le concept de MCP (architecture, usage) et des exemples spécifiques d'utilisation du MCP Server Trigger dans N8n.
- Présentation de l'Instance Level MCP : alternative permettant d'utiliser N8n comme serveur MCP au niveau global de l'instance, donnant accès à l'agent à tous les workflows existants et exécutables, plutôt qu'à des outils isolés configurés un par un.
- Démonstration de la configuration de l'Instance Level MCP : accès à la liste des workflows autorisés à être exécutés via ce point d'entrée, et visualisation des clients actuellement connectés.
- Démonstration pratique de connexion d'un outil (Claude) au serveur Instance Level MCP configuré précédemment, en renseignant l'adresse du serveur côté client.
- Étape de connexion via OAuth : ouverture d'une fenêtre d'approbation, validation de la connexion, puis retour à Claude désormais connecté à l'instance N8n via MCP, prêt à recevoir des requêtes.
- Consultation des permissions accordées au connecteur N8n : trois actions possibles répertoriées, dont la recherche des détails d'un workflow et la liste des workflows disponibles, visibles dans les paramètres de connecteurs.
- Test pratique : demande à l'assistant connecté de lister les workflows (statut inactif visible) puis d'exécuter le workflow « data tables », l'agent vérifiant d'abord les détails du workflow avant de procéder à l'exécution.
- Explication de l'activation/désactivation de l'accès MCP par workflow individuel : identifiable via un petit logo, modifiable via l'option « Remove MCP access » soit depuis la liste des workflows, soit directement à l'intérieur du workflow.
- Présentation d'une alternative dans VS Code : extensions type Kilo Code ou Cline permettant d'intégrer des agents IA directement dans l'environnement de développement, avec préférence personnelle pour Kilo Code.
- Explication de la configuration nécessaire pour connecter un serveur MCP depuis VS Code : modification d'un fichier de configuration des serveurs MCP indiquant l'URL du serveur Instance Level MCP N8n et un token d'accès.
- Confirmation de la connexion réussie de l'instance N8n en MCP à plusieurs agents, avec transition vers l'exposé des limites intrinsèques du serveur MCP natif de N8n, notamment sur la visibilité des exécutions.
- Illustration concrète de la première limite : un workflow planifié quotidiennement échoue, mais l'agent connecté via MCP natif ne peut pas accéder à l'historique d'exécution, obligeant à copier-coller manuellement l'erreur pour la faire déboguer.
- Deuxième limite majeure de l'Instance Level MCP : impossible de créer, modifier ou supprimer des workflows via cette interface, l'agent ne pouvant utiliser que ce qui existe déjà, sans capacité de création nouvelle. Démonstration à venir avec un petit workflow test.
- Confirmation de l'exécution réussie du workflow test (réception d'un email), mais échec de la demande d'élimination du workflow via MCP, l'API ne proposant aucune fonction de suppression, avec présentation d'une solution alternative.
- Présentation de l'alternative via l'API N8n classique : accès complet pour modifier credentials, tables de données, projets, étiquettes, utilisateurs, variables, et surtout workflows et exécutions, avec possibilité de tout créer, modifier ou éliminer.
- Introduction de l'outil n8n-mcp (disponible sur GitHub) qui fournit à l'agent la documentation des nœuds existants, des cas d'usage réels, et l'accès à l'API pour effectuer directement des modifications sur l'instance.
- Modalités de connexion à n8n-mcp : fenêtre de configuration simple, mais limite pratique de 100 appels d'outils par jour en usage gratuit, rapidement insuffisante pour un usage sérieux, nécessitant l'option suivante.
- Présentation des deux modes d'installation de n8n-mcp : configuration basique (documentation et exemples de nœuds uniquement) ou configuration avancée donnant accès à l'API pour effectuer des modifications réelles sur l'instance N8n.
- Incident illustratif majeur : lors d'une demande de suppression du workflow TestMCP, l'agent a supprimé par erreur un autre workflow (MCPExample) à la place, soulignant la nécessité impérative de rester vigilant avec ce type de serveur.
- Démonstration réussie de modification de workflow via l'agent : ajout automatique d'un trigger au workflow test MCP, transformant une exécution ponctuelle en tâche s'exécutant automatiquement chaque jour.

## Concepts cles
- plan de présentation du module Serveur MCP N8n
- renvoi vers vidéo complémentaire sur le concept de MCP
- Instance Level MCP : accès global à tous les workflows de l'instance
- configuration de l'Instance Level MCP (liste des workflows autorisés, clients connectés)
- connexion pratique d'un client (Claude) au serveur Instance Level MCP
- approbation de connexion via OAuth pour lier Claude à N8n
- permissions du connecteur N8n (recherche workflows, détails)
- test pratique de listing et exécution d'un workflow via MCP
- activation/désactivation de l'accès MCP par workflow (logo, option dédiée)
- alternative VS Code : extensions Kilo Code / Cline comme agents IA de développement
- configuration fichier MCP servers avec URL et token d'accès
- limites du serveur MCP natif N8n (visibilité des exécutions)
- limite pratique : pas d'accès à l'historique d'exécution via MCP natif
- limite : pas de création/modification/suppression de workflow via MCP natif
- confirmation de l'absence de fonction de suppression via MCP API N8n
- alternative via l'API N8n classique (accès complet CRUD)
- outil n8n-mcp (GitHub) : documentation des nœuds + accès API
- limite de 100 appels d'outils/jour de n8n-mcp en usage gratuit
- deux modes d'installation n8n-mcp (documentation seule vs accès API)
- incident réel : suppression accidentelle d'un mauvais workflow par l'agent
- démonstration réussie de modification autonome d'un workflow (ajout de trigger)

## Outils mentionnes
- n8n
- Claude
- VS Code
- Kilo Code
- Cline
- n8n-mcp

## Tips techniques
- Toujours vérifier attentivement les actions destructrices (suppression) proposées par un agent connecté à un serveur MCP avant de les approuver

## Cas d'usage reels
- [[]]
