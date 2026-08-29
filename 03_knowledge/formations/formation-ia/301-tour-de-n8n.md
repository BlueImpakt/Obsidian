---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.01 Tour de N8N.txt"
---

# 3.01 Tour de N8N

## Resume
- Présentation de N8n comme le meilleur outil d'automatisation selon l'auteur, potentiellement rebutant au premier abord mais paradoxalement plus accessible que Make une fois maîtrisé, une opinion que certains utilisateurs des deux outils pourraient nuancer.
- Présentation de l'essai gratuit de 14 jours sur la version cloud N8n, recommandée pour débuter car certains aspects sont simplifiés, avant de basculer vers l'auto-hébergement plus rentable une fois plus expérimenté.
- Démonstration pratique de l'inscription : lancement de l'essai gratuit, réponses aux questions de profilage (taille d'entreprise « juste moi », équipe « IT » car l'auteur fait un peu de tout).
- Fin du processus d'inscription : possibilité d'inviter des membres ou de passer cette étape, création automatique de l'espace de travail, rendant l'utilisateur immédiatement prêt à automatiser.
- Tour d'horizon de l'interface : présentation des workflows et critique UX sur le bouton Create Credential jugé peu intuitif, l'auteur préférant une séparation plus claire entre les fonctionnalités.
- Explication du runtime (temps de traitement des automatisations) et des trois options de création disponibles (workflow, credential, project), avec réitération de la critique sur cette organisation jugée redondante.
- Présentation du canvas interactif de N8n, similaire à Make en termes de flexibilité de navigation, avec démonstration de l'usage d'une souris Logitech MX Master 3 pour naviguer via la molette.
- Présentation de fonctionnalités pratiques : synchronisation de la sélection avec le canvas et pop-out panel permettant d'afficher un panneau flottant (utile pour visualiser les logs différemment).
- Comparaison avec l'expérience d'outils comme Bubble pour les utilisateurs familiers de ce type d'interface. Présentation du menu contextuel de workflow : dupliquer, télécharger, renommer.
- Présentation des réglages avancés : Execution Order (recommandation d'utiliser la V1) et Error Workflow permettant de déclencher un workflow dédié à la gestion d'erreurs en cas de bug sur le scénario principal.
- Présentation de la définition de la time zone, essentielle pour la manipulation des dates (comme vu précédemment sur Make), avec options de sauvegarde des exécutions échouées et réussies en production.
- Mention de fonctionnalités cachées intéressantes, transition vers la présentation des autres sections de l'interface : l'éditeur, les exécutions, et les évaluations (permettant de mesurer la performance d'un workflow).
- Présentation de l'Admin Panel : permet de gérer plusieurs instances tournant simultanément, gérer son plan d'abonnement, et accepter les nodes développés par la communauté N8n.
- Mise en garde sur les nodes communautaires : il faut apprendre à identifier les bons et à bien les catégoriser, car certains sont mal optimisés et alourdissent le scénario, N8n étant facturé au scénario et non à l'opération.
- Présentation des templates et des variables globales définies « en dur » au niveau de l'instance N8n, permettant leur réutilisation cohérente à travers plusieurs workflows différents.
- Présentation de l'assistant IA intégré à N8n, jugé bien plus pertinent que celui de Make (qualifié de « complètement nul » par l'auteur), capable de répondre efficacement à des questions d'aide sur l'outil.
- Importance de la documentation et de l'usage des notes dans les workflows, particulièrement crucial pour le travail collaboratif ou avec des clients, afin qu'ils puissent facilement comprendre la logique du scénario.
- Démonstration pratique de la fonctionnalité de copier-coller de notes entre nodes, permettant de dupliquer facilement une note contextuelle (exemple avec un node Notion) sur d'autres éléments du workflow.

## Concepts cles
- N8n jugé plus accessible que Make une fois maîtrisé (opinion personnelle)
- essai gratuit 14 jours (version cloud), transition vers auto-hébergement
- démonstration pratique du processus d'inscription N8n
- finalisation de l'inscription et création automatique de l'espace
- présentation de l'interface avec critique UX (bouton Create Credential)
- runtime et options de création (workflow/credential/project)
- canvas interactif N8n (navigation similaire à Make)
- fonctionnalités canvas (sync sélection, pop-out panel pour logs)
- comparaison avec Bubble
- menu contextuel de workflow (dupliquer, télécharger, renommer)
- réglage Execution Order (recommandation V1)
- Error Workflow pour la gestion centralisée des erreurs
- définition de time zone
- options de sauvegarde des exécutions (échouées/réussies)
- sections de l'interface (éditeur, exécutions, évaluations)
- Admin Panel (gestion multi-instances, plan, nodes communautaires)
- mise en garde sur la qualité variable des nodes communautaires
- facturation N8n au scénario (pas à l'opération)
- variables globales définies en dur, réutilisables sur plusieurs workflows
- assistant IA intégré N8n jugé supérieur à celui de Make
- importance de la documentation via notes pour le travail collaboratif/client
- démonstration pratique du copier-coller de notes entre nodes

## Outils mentionnes
- n8n
- Make
- Bubble
- Notion

## Tips techniques
- Débuter sur la version cloud N8n (essai 14 jours) avant de basculer vers l'auto-hébergement une fois plus expérimenté
- Utiliser l'Execution Order en version V1 (recommandation de l'auteur)
- Trier soigneusement les nodes communautaires : certains sont mal optimisés et alourdissent inutilement le scénario
- Toujours bien documenter ses workflows avec des notes, surtout dans un contexte collaboratif ou client

## Cas d'usage reels
- [[]]
