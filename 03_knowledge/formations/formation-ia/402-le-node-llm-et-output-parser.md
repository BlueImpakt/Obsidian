---
tags: [formation, millenium]
module: Formation IA
section: "L'IA dans n8n"
source_transcript: "4.02 Le node LLM et Output Parser.txt"
---

# 4.02 Le node LLM et Output Parser

## Resume
- Introduction au module sur le node LLM (Basic LLM Chain) avec démonstration de sa configuration par défaut, incluant la possibilité d'accéder publiquement à un chat de prévisualisation via une URL.
- Démonstration pratique d'une erreur de configuration révélée dans les logs, illustrant l'utilité du panneau de logs pour diagnostiquer les échanges avec le chat de prévisualisation.
- Analyse détaillée du log d'erreur (session ID, message envoyé, valeur du chat input) avec possibilité de modifier certains éléments directement depuis la vue agrandie du log.
- Test pratique du LLM (Claude via Anthropic) répondant à une question météo : le modèle indique correctement ne pas avoir accès aux conditions météorologiques en temps réel, une limite native attendue.
- Clarification sur le choix entre Basic LLM Chain et agent IA : la Chain convient pour des questions simples sans besoin d'outils externes, l'agent IA étant nécessaire pour aller chercher des informations via des outils spécifiques.
- Démonstration pratique de génération de script vidéo avec consignes structurées (hook des premières secondes, CTA, éléments augmentant le watchtime) via la Basic LLM Chain.
- Test pratique de génération avec contrainte de durée (45 secondes) illustrant le prompting de base pour obtenir un script de contenu court calibré.
- Exemple de contenu généré (comparaison Claude/GPT sur sécurité, analyse, cohérence) avec introduction de l'Output Parser pour structurer la réponse selon un format défini.
- Démonstration de définition d'un champ de performance noté sur 100 dans l'output structuré, avec option autofix format et choix du modèle (Anthropic) pour le traitement.
- Mise en garde explicite contre une mauvaise pratique observée, avec démonstration du Structured Output Parser forçant le LLM à répondre dans un format spécifique prédéfini.
- Configuration d'une boucle d'auto-amélioration : le prompt demande au modèle d'atteindre un score de performance de 100% en réévaluant et réécrivant le script précédemment noté (87%).
- Astuce d'optimisation de workflow : dupliquer et reconnecter les nœuds Structured Output Parser et modèles plutôt que de les recréer à chaque fois, un gain de temps pratique.
- Résultat final de la boucle d'amélioration : un script sur un combattant de MMA obtenant un score de performance de 100%, illustrant l'efficacité de la relecture/correction automatisée par un second passage.

## Concepts cles
- introduction à la configuration du Basic LLM Chain et accès public via URL
- démonstration d'utilisation des logs pour diagnostiquer une erreur de configuration
- analyse détaillée d'un log d'erreur avec modification directe possible
- test pratique révélant la limite native du LLM sur les données météo temps réel
- critère de choix Basic LLM Chain (simple) vs agent IA (accès outils)
- démonstration de génération de script vidéo structuré (hook, CTA, watchtime)
- test pratique de prompting de base avec contrainte de durée
- introduction de l'Output Parser pour structurer la réponse selon un format
- démonstration de champ de performance noté sur 100 dans l'output structuré
- démonstration du Structured Output Parser forçant un format de réponse spécifique
- configuration d'une boucle d'auto-amélioration itérative basée sur un score de performance
- astuce d'optimisation : dupliquer les nœuds plutôt que les recréer
- résultat final : script optimisé à 100% via relecture/correction automatisée

## Outils mentionnes
- n8n
- Claude
- Anthropic
- GPT

## Tips techniques
- Consulter systématiquement les logs du chat de prévisualisation pour diagnostiquer précisément la cause d'une erreur de configuration
- Configurer une boucle d'auto-amélioration où le modèle réécrit son propre contenu en visant un score de performance cible plus élevé
- Dupliquer et reconnecter les nœuds existants (Output Parser, modèles) plutôt que de les recréer manuellement à chaque usage, pour gagner du temps

## Cas d'usage reels
- [[]]
