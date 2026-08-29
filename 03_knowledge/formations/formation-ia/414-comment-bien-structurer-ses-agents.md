---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.14 Comment bien structurer ses agents.txt"
---

# 4.14 Comment bien structurer ses agents

## Resume
- Introduction au module de structuration des agents : présentation de cinq façons différentes d'organiser des agents dans N8n selon la complexité du besoin.
- Présentation de la structure séquentielle : agent 1 écrit l'objet d'email, agent 2 écrit le corps, agent 3 évalue les deux, une architecture adaptée aux processus linéaires.
- Précision qu'un agent au sein d'une structure séquentielle reste un véritable agent (pas un simple node LLM) et peut avoir accès à des outils externes comme Google Sheets.
- Présentation de la structure combinée pour analyser plusieurs éléments simultanément (ex : email combinant plusieurs analyses), illustrée par un exemple de rédaction de post LinkedIn stylisé.
- Présentation de la structure conditionnelle basée sur classification : un agent classifieur détermine lequel des agents spécialisés (agent 1 ou agent 2) sera déclenché selon le contenu identifié.
- Application concrète de la structure conditionnelle pour classifier des demandes et rediriger vers des agents spécialisés : service client, tri d'emails, gestion de tickets, modération de contenu.
- Critère de décision pour utiliser la structure conditionnelle : nécessaire dès que les scénarios deviennent complexes et qu'on a besoin de plus de granularité dans l'interaction de l'agent.
- Présentation de la structure hiérarchique manager/sous-agents : le manager (agent 3) supervise les résultats des agents 1 et 2 mais ne peut pas revenir en arrière, d'où l'importance de bien structurer cette hiérarchie.
- Transition vers la démonstration pratique dans N8n de toutes les structures d'agents présentées théoriquement, en commençant par la succession d'agents en chaîne.
- Démonstration de configuration d'un second agent (corps de l'email) puis d'un troisième agent de validation utilisant un modèle moins coûteux car sa tâche est plus simple.
- Démonstration de configuration de l'exécution conditionnelle : un Text Classifier en amont détermine vers quel agent spécialisé router la demande selon le type identifié.
- Configuration d'une boucle de validation via node IF : si l'agent validateur est satisfait, le workflow continue, sinon il redemande à l'agent constructeur avec le feedback précis à corriger.
- Présentation de la structure hiérarchique via sous-workflows dédiés : déclenchement d'un nouvel agent avec son propre modèle et outils, renvoyant l'information à l'agent appelant.
- Démonstration de création et de nommage d'un sous-agent spécialisé (« agent calendrier ») directement rappelable et connecté à l'agent principal.
- Avantage clé de la structuration en sous-agents : le prompt spécifique (ex : identifiant unique de calendrier) reste localisé sur le sous-agent, évitant un prompt principal trop long et facilitant la maintenance.

## Concepts cles
- introduction aux cinq façons d'organiser des agents dans N8n
- structure séquentielle : agents spécialisés en chaîne (objet, corps, évaluation)
- précision : un agent en structure séquentielle reste un véritable agent avec outils
- structure combinée pour analyser plusieurs éléments simultanément
- structure conditionnelle : classification déterminant l'agent spécialisé à déclencher
- applications concrètes de la classification conditionnelle (service client, tri emails, tickets)
- critère de décision : structure conditionnelle pour scénarios complexes
- structure hiérarchique manager/sous-agents avec limite de non-retour en arrière
- transition vers la démonstration pratique des structures d'agents dans N8n
- démonstration de configuration séquentielle avec modèle économique pour la validation
- démonstration de configuration de l'exécution conditionnelle via Text Classifier
- configuration d'une boucle de validation conditionnelle avec feedback de correction
- structure hiérarchique via sous-workflows dédiés avec retour d'information
- démonstration de création et nommage d'un sous-agent spécialisé (agent calendrier)
- avantage de la structuration en sous-agents : prompt localisé facilitant la maintenance

## Outils mentionnes
- n8n
- Google Sheets

## Tips techniques
- Réserver la structure conditionnelle (classification + redirection) aux scénarios suffisamment complexes nécessitant une granularité d'interaction fine
- Utiliser un modèle moins coûteux pour l'agent de validation dans une chaîne séquentielle, sa tâche étant plus simple que la génération
- Localiser les prompts spécifiques (identifiants, détails techniques) sur des sous-agents dédiés plutôt que de surcharger le prompt principal

## Cas d'usage reels
- [[]]
