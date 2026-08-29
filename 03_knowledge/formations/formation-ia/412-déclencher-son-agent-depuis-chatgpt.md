---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.12 Déclencher son agent depuis ChatGPT.txt"
---

# 4.12 Déclencher son agent depuis ChatGPT

## Resume
- Introduction aux différents moyens de connecter et déclencher un agent IA, constat que peu de contenu existe sur ce sujet malgré la multiplication des agents.
- Présentation de l'intérêt d'utiliser ChatGPT comme porte d'entrée déclenchant un webhook, mécanisme transposable à d'autres outils comme Claude.
- Conseil de nommer explicitement le GPT créé (ex : AgentFacture) pour ensuite l'utiliser dans la génération du schéma de référence.
- Génération du schéma d'action avec correction en direct d'un oubli (URL du webhook non précisée) avant de continuer la configuration.
- Étape de création d'un nouveau GPT personnalisé nommé AgentFacture via l'onglet de configuration dédié.
- Configuration de l'action du GPT via le schéma copié (send invoice data), avec rappel de retirer le mode test avant la mise à jour finale.
- Présentation de l'accès à l'agent IA de facture créé, prêt à recevoir des factures à traiter en exemple.
- Démonstration pratique : téléchargement d'une facture exemple puis envoi de ses données via une instruction au GPT.
- Confirmation du succès du déclenchement du webhook avec envoi automatique des données extraites de la facture, vérification des informations (numéro, montant).
- Vérification détaillée des données extraites : produits scannés automatiquement avec TVA à 20% correctement identifiée sans avoir été explicitement demandée.
- Confirmation de la rapidité du traitement (5 secondes) : ChatGPT analyse une facture et extrait toutes les valeurs pour les envoyer directement dans le workflow.
- Qualification de cette capacité comme un vrai game changer, avec pistes d'amélioration possibles du GPT (ex : vérifier l'envoi du document lui-même).
- Présentation d'une voie alternative de déclenchement via Telegram, permettant d'avoir plusieurs points d'entrée pour le même agent.
- Confirmation de la possibilité d'avoir plusieurs triggers dans un même scénario N8N, avec ajout d'un nœud OpenAI pour analyser la donnée reçue via Telegram.
- Démonstration de manipulation de données en array (ex : liste de produits) avec la fonction Execute Steps pour conserver la structure.
- Conclusion de l'exemple avec mention des nœuds Merge pour fusionner des données similaires, résumant les possibilités de déclenchement d'agents IA.

## Concepts cles
- introduction aux différents moyens de connecter et déclencher un agent IA
- présentation de ChatGPT comme porte d'entrée déclenchant un webhook
- conseil de nommer explicitement le GPT créé pour référence
- génération du schéma d'action avec correction d'un oubli d'URL webhook
- étape de création d'un GPT personnalisé nommé AgentFacture
- configuration de l'action du GPT (retrait du mode test avant mise à jour)
- présentation de l'accès à l'agent IA de facture prêt à l'emploi
- démonstration pratique d'envoi d'une facture exemple au GPT
- confirmation du succès du déclenchement webhook avec vérification des données
- vérification détaillée : extraction automatique de la TVA sans demande explicite
- confirmation de la rapidité d'extraction de facture par ChatGPT (5 secondes)
- qualification de game changer avec pistes d'amélioration possibles
- présentation d'une voie alternative de déclenchement via Telegram
- confirmation de plusieurs triggers possibles dans un même scénario N8N
- démonstration de manipulation de données en array avec Execute Steps
- conclusion sur les nœuds Merge et les possibilités de déclenchement d'agents IA

## Outils mentionnes
- ChatGPT
- Claude
- Telegram
- N8N
- OpenAI

## Tips techniques
- Toujours nommer explicitement chaque GPT créé (ex : AgentFacture) selon sa fonction précise pour faciliter la maintenance
- Toujours retirer le mode test de la configuration d'action GPT avant la mise à jour finale, pour que le déclenchement fonctionne réellement
- Configurer plusieurs triggers différents (webhook, Telegram, etc.) dans un même scénario N8N pour déclencher le même agent via des canaux variés

## Cas d'usage reels
- [[]]
