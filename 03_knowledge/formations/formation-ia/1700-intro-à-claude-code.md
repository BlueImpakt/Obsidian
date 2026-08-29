---
tags: [formation, millenium]
module: Formation IA
section: "Claude Code"
source_transcript: "17.00 Intro à Claude Code.txt"
---

# 17.00 Intro à Claude Code

## Resume
- Sommaire du module Introduction à Claude Code : introduction, Boris Czerny, objectif de l'outil, raisonnement et évolution, capacités autonomes, nouvelle ère du développement, transformation d'Anthropic.
- Présentation de Boris Czerny, ingénieur chez Anthropic et créateur de Claude Code, précédemment employé chez Meta jusqu'en août 2024, un parcours éclairant sur la genèse de l'outil.
- Explication de la genèse de Claude Code : partant de tests sur l'accès du modèle à un écosystème fermé d'actions, avec une structure initialement très linéaire similaire aux approches précédentes.
- Constat de l'écosystème né autour de Claude jusqu'à Opus 4.1, qui a défini une nouvelle méta du développement permettant à des non-développeurs de créer sans écrire une ligne de code.
- Présentation de l'écosystème Claude (Claude, Claude Code, Claude Cowork, Claude Platform), avec description de Claude comme « thinking partner » dépassant le simple chatbot classique.
- Éloge du confort de codage directement dans le terminal, jugé supérieur à l'expérience en application classique, avec mention que cette perception pourrait évoluer avec les futures améliorations de Claude.
- Description de la sensation psychologique de proximité directe permise par l'absence d'interface dans le terminal, une abstraction devenue inutile grâce aux capacités actuelles des LLM.
- Comparaison de l'IDE à un Google Doc pour développeurs, avec prédiction que les IDE ont quasiment vocation à disparaître face à l'usage croissant du terminal via l'IA.
- Présentation des deux modes d'interaction avec Claude Code depuis un IDE : terminal intégré directement dans l'IDE, ou usage alterné entre les deux selon les besoins, une pratique personnelle de l'auteur.
- Mention historique de Cursor comme pionnier du VS Code avec IA intégrée, suivi d'Antigravity (Google) ; précision que Claude Code est aussi disponible sur web (claude.ai) et iOS, avec préférence personnelle limitée pour ces versions.
- Affirmation forte du potentiel de multiplication de productivité par 10 grâce à Claude Code pour des usages professionnels réellement alignés sur des objectifs concrets, un gain jugé pleinement rentable.
- Présentation des outils fondamentaux de Claude Code : WRITE (écriture), EDIT (modification), BASH (exécution de commandes), puis GLOB, GREP et WebFetch pour la recherche d'informations.
- Introduction à la structuration d'un projet avec Claude Code : le fichier CLAUDE.md agit comme le « cerveau » du projet, définissant la structure de l'application et les règles à tester systématiquement.
- Explication de la distinction entre modes de fonctionnement selon le contexte : laisser Claude Code travailler en autonomie prolongée sans validation constante pour une première version, versus un mode plus supervisé.
- Présentation du système de skills de Claude Code : un skill nommé (ex : « deploy ») avec une description déclenchant automatiquement une action (déploiement) lorsque l'utilisateur utilise un mot-clé spécifique.
- Présentation des scripts comme bouts de code déclenchés automatiquement selon le besoin, avec recommandation de garder les scripts légers plutôt que denses pour une meilleure lisibilité et maintenance.
- Explication de l'accès du MCP à un large éventail d'actions, avec évolution vers l'intégration croissante des CLI (Command Line Interface), dont Claude Code est lui-même un exemple.
- Présentation des trois primitives fondamentales du MCP : les tools (outils actionnables comme créer, demander) et les ressources à lire pour comprendre un contexte (ex : structure de Notion).
- Explication de la fonctionnalité de compactage de contexte de Claude Code, comparée à la compression d'un fichier zip, permettant de libérer de la place dans la fenêtre contextuelle en cours de session.
- Recommandation de bien cloisonner et normer ses sessions Claude Code : l'accumulation progressive de contexte au fil d'une session peut réduire la pertinence des réponses si mal gérée.
- Présentation des slash commandes de Claude Code (comme /help), ainsi que des différents modes de fonctionnement dont le Plan Mode, recommandé en priorité pour planifier avant d'exécuter.
- Introduction à la notion de sous-agent dans Claude Code : face à une tâche volumineuse, l'outil délègue progressivement à des sous-agents plutôt que de tout exécuter lui-même, une capacité amenée à s'améliorer avec les futurs modèles.

## Concepts cles
- plan de présentation du module Introduction à Claude Code
- présentation de Boris Czerny (créateur de Claude Code, ex-Meta)
- genèse de Claude Code : tests d'accès du modèle à un écosystème d'actions
- nouvelle méta du développement permettant aux non-développeurs de créer sans code
- présentation de l'écosystème Claude (Code, Cowork, Platform) comme thinking partner
- éloge du confort de codage en terminal, supérieur à l'application classique
- sensation psychologique de proximité directe permise par l'absence d'interface
- comparaison IDE/Google Doc et prédiction de disparition progressive des IDE
- deux modes d'interaction avec Claude Code depuis un IDE (terminal ou usage alterné)
- historique de Cursor/Antigravity et disponibilité de Claude Code sur web/iOS
- affirmation de multiplication de productivité par 10 avec Claude Code
- présentation des outils fondamentaux de Claude Code (WRITE, EDIT, BASH, GLOB, GREP, WebFetch)
- structuration de projet : CLAUDE.md comme cerveau du projet avec règles de test
- distinction entre mode autonome prolongé et mode supervisé selon le contexte
- présentation du système de skills de Claude Code (nom, description, déclencheur)
- présentation des scripts automatiques et recommandation de légèreté
- accès du MCP à un large éventail d'actions et intégration croissante des CLI
- présentation des trois primitives fondamentales du MCP (tools, ressources)
- fonctionnalité de compactage de contexte (analogie avec un zip)
- recommandation de cloisonner et normer les sessions Claude Code pour préserver la pertinence
- présentation des slash commandes et du Plan Mode (planifier avant exécuter)
- introduction à la notion de délégation à des sous-agents dans Claude Code

## Outils mentionnes
- Claude Code
- Claude
- Opus
- Google Doc
- Cursor
- Antigravity
- MCP
- Notion

## Tips techniques
- Utiliser le fichier CLAUDE.md comme document central définissant la structure et les règles obligatoires de test du projet pour l'IA
- Garder les scripts déclenchés par Claude Code légers et non denses, plutôt que de tout concentrer dans un seul script complexe
- Utiliser la fonctionnalité de compactage de Claude Code pour libérer de l'espace contextuel lors de sessions longues, comme on compresserait un fichier
- Cloisonner et normer clairement les sessions Claude Code par sujet, pour éviter que l'accumulation de contexte ne dégrade la pertinence des réponses
- Toujours commencer par le Plan Mode de Claude Code pour planifier avant d'exécuter, plutôt que de foncer directement dans l'action

## Cas d'usage reels
- [[]]
