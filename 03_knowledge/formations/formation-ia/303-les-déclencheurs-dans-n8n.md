---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.03 Les déclencheurs dans N8N.txt"
---

# 3.03 Les déclencheurs dans N8N

## Resume
- Introduction aux déclencheurs sur N8n, présentés comme un élément fondamental de l'automatisation : le principe consiste à définir ce qui va initier le processus une fois qu'on se retire de la chaîne manuelle.
- Présentation de la catégorie des déclencheurs applicatifs, distinguée par deux types : les triggers (comparés à une gâchette de pistolet) qui réagissent instantanément à un événement.
- Distinction visuelle des types de déclencheurs (webhook en rouge) et présentation des triggers poll : contrairement au webhook passif, N8n va lui-même activement chercher l'information à intervalle régulier.
- Présentation de déclencheurs spécifiques à N8n : appel d'un scénario depuis un autre scénario, et le Mailhook (processus basé sur IMAP scannant la boîte mail) même s'il ne porte pas ce nom exact dans l'interface.
- Présentation du trigger manuel, essentiel et fréquemment utilisé lors des phases de test des automatisations, permettant de déclencher volontairement un scénario sans attendre l'événement réel.
- Astuce pratique de raccourci clavier : Ctrl+Entrée (Windows) ou Cmd+Entrée (Mac) permet de lancer le workflow sans avoir à cliquer sur un bouton, un gain de temps précieux lors des tests répétés.
- Explication du comportement du trigger manuel : N8n le considère par défaut comme inactif, car son unique méthode d'activation nécessite une action volontaire de l'utilisateur (clic sur Execute Workflow).
- Précision sur le type de méthode HTTP par défaut d'un webhook (GET), alors que la grande majorité des cas d'usage réels nécessitent plutôt une requête POST, envoyée par une autre application vers l'URL du webhook.
- Fonctionnalité appréciée de N8n : le PATH généré automatiquement (chaîne de caractères unique) peut être renommé pour plus de lisibilité, un avantage non disponible sur certaines plateformes concurrentes.
- Présentation du principe inverse au webhook : c'est N8n lui-même qui initie l'action à intervalle défini (jours, heures, minutes, secondes, semaines), plutôt que d'attendre passivement une sollicitation externe.
- Présentation des options de récurrence mensuelle (choix du jour du mois) et possibilité d'empiler plusieurs règles simultanément, avec introduction d'une dernière typologie de déclenchement particulièrement importante.
- Introduction du CRON, particulièrement utile pour les répétitions du type « toutes les X heures ». Recommandation de l'outil externe crontab.guru pour comprendre et construire facilement des expressions CRON valides.
- Démonstration pratique de collage d'une expression CRON directement dans l'interface N8n, illustrant la simplicité d'intégration une fois l'expression construite via l'outil externe recommandé.
- Exemple concret d'expression CRON déclenchant toutes les 6 heures, illustrant la flexibilité offerte par cette syntaxe. Transition vers la présentation des déclencheurs de type On The App Event.
- Mise en garde importante : l'icône éclair sur un trigger ne signifie pas systématiquement qu'il s'agit d'un webhook. Il faut connaître les spécificités de chaque application (exemple : ActiveCampaign envoie effectivement des webhooks).
- Précision sur l'origine des webhooks : ils peuvent être générés par le public (contact), l'admin, ou le système/API, avec possibilité de filtrer sur un ou plusieurs types d'origine pour affiner le déclenchement.
- Explication du mécanisme d'intégration automatique : N8n se charge lui-même de connecter le webhook via le compte utilisateur, nécessitant une URL de compte spécifique et une clé API (équivalente à un mot de passe).
- Illustration du principe de polling avec Airtable : contrairement au webhook, c'est N8n qui va activement chercher les données à intervalle régulier, réutilisant notamment l'expression CRON présentée précédemment.
- Conclusion sur les deux types fondamentaux de déclencheurs présents dans toutes les applications intégrées à N8n : webhook (passif) et poll (actif), illustré également avec l'exemple de Bubble.
- Exemple concret de trigger de type poll (« page updated on database ») où N8n va chercher activement l'information, confirmant les deux typologies présentées. Introduction des déclencheurs spécifiques à N8n comme les formulaires.
- Présentation d'un déclencheur particulièrement puissant : Chat Message Receive, très utile notamment pour les agents IA, permettant de recevoir des messages de chat comme point d'entrée d'une automatisation.
- Présentation de l'Email Trigger, équivalent du Mailhook vu sur Make : connexion via nom d'utilisateur et mot de passe Gmail, avec recommandation de consulter la documentation ou l'assistant intégré pour la configuration.
- Précision sur les avantages spécifiques de Gmail (plus d'actions natives disponibles) tout en confirmant que d'autres fournisseurs email peuvent aussi utiliser ce trigger. Introduction de l'Error Trigger pour déclencher un scénario en cas d'erreur d'un autre.
- Introduction du MCP dans N8n (approfondi plus tard) : il permet de rendre disponibles toutes ses automatisations directement en tant que serveur MCP, le framework développé par Anthropic pour connecter les LLM aux outils.

## Concepts cles
- introduction aux déclencheurs comme fondement de l'automatisation
- déclencheurs applicatifs de type trigger (analogie pistolet)
- triggers Poll (recherche active) vs webhook (passif)
- déclencheur inter-scénarios et Mailhook basé sur IMAP
- trigger manuel pour les phases de test
- raccourci clavier pour lancer le workflow (Ctrl/Cmd+Entrée)
- comportement par défaut inactif du trigger manuel
- type de méthode HTTP par défaut (GET) vs usage réel majoritaire (POST)
- renommage du PATH webhook (avantage compétitif de N8n)
- principe du polling actif (N8n initie l'action) vs webhook passif
- récurrence mensuelle et empilement de règles multiples
- CRON pour récurrences complexes
- outil crontab.guru pour construire des expressions CRON
- intégration pratique d'une expression CRON dans N8n
- exemple CRON toutes les 6 heures
- introduction des déclencheurs On The App Event
- mise en garde : l'icône éclair ne garantit pas un type webhook
- filtrage par origine du webhook (public/admin/système)
- intégration automatique du webhook via URL de compte et clé API
- polling Airtable avec réutilisation de l'expression CRON
- synthèse des deux types fondamentaux de déclencheurs applicatifs
- exemple de poll trigger et transition vers les formulaires N8n
- déclencheur Chat Message Receive (puissant pour agents IA)
- Email Trigger (équivalent Mailhook) via connexion Gmail
- Gmail favorisé nativement, introduction de l'Error Trigger
- MCP dans N8n pour exposer ses automatisations comme serveur

## Outils mentionnes
- n8n
- crontab.guru
- ActiveCampaign
- Airtable
- Bubble
- Gmail
- Anthropic

## Tips techniques
- Utiliser systématiquement le trigger manuel pendant les phases de test d'un workflow avant de le connecter à un vrai déclencheur
- Utiliser Ctrl+Entrée (Windows) ou Cmd+Entrée (Mac) pour lancer rapidement un workflow sans cliquer manuellement
- Renommer le PATH généré automatiquement du webhook pour plus de lisibilité et de facilité de maintenance
- Utiliser crontab.guru pour construire et valider une expression CRON avant de l'utiliser dans N8n
- Ne pas se fier uniquement à l'icône éclair pour identifier un trigger webhook : vérifier la documentation spécifique de chaque application

## Cas d'usage reels
- [[]]
