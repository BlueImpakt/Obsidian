---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.11 Node Human in the Loop.txt"
---

# 4.11 Node Human in the Loop

## Resume
- Introduction au node Human in the Loop : nécessité d'intégrer une validation humaine dans certains processus d'agents IA pour des actions importantes ne devant pas être laissées en autonomie totale.
- Présentation du schéma type d'un workflow Human in the Loop : déclencheur périodique, agent IA utilisant un modèle, avec intégration d'une étape de validation humaine à un point clé.
- Explication du mécanisme de boucle de validation : en cas de refus, l'élément repasse par la boucle Human in the Loop, avec démonstration de configuration d'un trigger Telegram pour ce workflow.
- Recommandation de renommer le bot Telegram utilisé (ex : « Teio Contenu ») pour identifier clairement son usage spécifique parmi plusieurs bots gérés en parallèle.
- Démonstration pratique de test d'un message d'exemple (« écrit un post LinkedIn ») avant configuration de l'agent IA correspondant via l'option Define Below.
- Exemple de prompt de rôle pour un agent Ghostwriter LinkedIn : structure hook/hold/body/CTA, ton persuasif avec humour léger, sans hashtags, transformant une idée reçue en post percutant.
- Configuration des options de validation Human in the Loop (Approve Only vs Approve and Disapprove), avec récupération de la valeur générée par l'agent pour l'afficher dans le message de validation.
- Référence au livre L'Almanach de Naval Ravikant utilisé comme source d'inspiration pour le contenu généré, avec observation que le message de validation est initialement vide car dépendant de la génération en cours.
- Explication du mécanisme technique du formulaire de validation Human in the Loop : un webhook N8n qui se déclenche au clic pour confirmer ou refuser l'action proposée par l'agent.
- Test complet du workflow sur un concept concret (« learn to build, learn to sell ») : l'agent génère le post et une réponse de validation apparaît pour confirmation.
- Formulation d'un prompt de retravail pour un agent de validation : demander explicitement de retravailler le post selon des critères précis en cas d'insatisfaction du résultat initial.
- Configuration de l'agent de retravail avec modèle Anthropic, réutilisation de la même mémoire et des mêmes outils que l'agent de création initial, une architecture cohérente.
- Démonstration de récupération du résultat du premier agent de création via expression (item.json.output) pour l'injecter dans le prompt de l'agent de retravail.
- Relance du test complet avec un nouveau concept LinkedIn (« learn to build, learn to sell »), illustrant le cycle itératif de génération et validation en conditions réelles.
- Démonstration volontaire d'un rejet de validation (« pas OK ») sur un critère personnel (séparation vie pro/perso), pour illustrer pédagogiquement le fonctionnement du refus dans le workflow.
- Répétition du cycle complet avec un nouveau concept, incluant un nouveau rejet de validation, illustrant la robustesse et la répétabilité du système de boucle Human in the Loop.
- Démonstration de transmission du texte de retour ('idée du post') vers l'agent de création via Execute Workflow, complétant le cycle de feedback dans le système de validation.
- Exemple de rejet argumenté d'un post évoquant Naval Ravikant sur le choix entre techniques et commercial, illustrant un critère de validation subjectif conduisant à une nouvelle itération via l'agent de validation.
- Configuration d'un champ de formulaire requis demandant la raison précise du rejet (« que souhaiterais-tu changer au poste ? »), une amélioration pour affiner le feedback donné à l'agent.
- Exemple concret de feedback structuré fourni via le formulaire (« le hook n'est pas assez clickbait »), démontrant la précision attendue pour guider efficacement la réécriture par l'agent.
- Configuration d'une condition logique (égal à « OK ») déterminant le branchement vers la validation finale ou vers une nouvelle itération de retravail selon la réponse reçue.

## Concepts cles
- introduction au Human in the Loop pour validation humaine d'actions importantes
- présentation du schéma type d'un workflow Human in the Loop
- mécanisme de boucle de validation en cas de refus, démonstration trigger Telegram
- recommandation de renommer les bots Telegram pour identifier clairement leur usage
- démonstration de test d'un message d'exemple avant configuration de l'agent
- exemple de prompt de rôle Ghostwriter LinkedIn (structure hook/hold/body/CTA)
- configuration des options de validation Human in the Loop (Approve/Disapprove)
- référence au livre L'Almanach de Naval Ravikant comme source de contenu
- mécanisme technique du formulaire de validation via webhook N8n
- test complet du workflow de validation sur un concept concret
- formulation d'un prompt de retravail selon des critères précis
- configuration cohérente de l'agent de retravail (même modèle, mémoire, outils)
- démonstration de récupération du résultat du premier agent via expression
- relance du test complet avec un nouveau concept illustrant le cycle itératif
- démonstration pédagogique volontaire d'un refus de validation
- répétition du cycle complet illustrant la robustesse de la boucle de validation
- démonstration de transmission du feedback vers l'agent de création via Execute Workflow
- exemple de rejet argumenté illustrant un critère de validation subjectif
- configuration d'un champ de formulaire requis demandant la raison du rejet
- exemple concret de feedback structuré et précis pour guider la réécriture
- configuration d'une condition logique de branchement selon la réponse de validation

## Outils mentionnes
- n8n
- Telegram
- Anthropic

## Tips techniques
- Renommer chaque bot Telegram selon son usage spécifique pour faciliter l'identification quand plusieurs bots sont gérés en parallèle
- Structurer un prompt de rédaction LinkedIn selon le schéma hook/hold/body/CTA avec consignes de ton précises (humour léger, pas de hashtags)
- Formuler un prompt de retravail explicite précisant les critères d'insatisfaction, pour permettre à l'agent de corriger le contenu
- Rendre obligatoire la saisie de la raison précise du rejet dans un formulaire de validation, pour fournir un feedback exploitable à l'agent
- Fournir un feedback précis et actionnable (ex : 'le hook n'est pas assez clickbait') plutôt qu'une critique vague, pour guider efficacement la réécriture

## Cas d'usage reels
- [[]]
