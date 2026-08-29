---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un expert de n8n"
source_transcript: "11.04 Tests de performance  Evaluation.txt"
---

# 11.04 Tests de performance / Evaluation

## Resume
- Sommaire du module évaluation : introduction aux évaluations, pourquoi évaluer les agents IA, le risque de la production, la distinction tester vs valider, et la mise en œuvre concrète via l'onglet évaluation de N8n.
- Constat que les personnes minutieuses vérifient plus que le simple fonctionnement technique visuel (nodes verts, information qui circule correctement) d'un workflow, allant au-delà de la validation superficielle.
- Définition de l'évaluation comme moyen de rendre objective et chiffrée la performance d'un agent ou système, plutôt qu'une appréciation subjective, permettant de comparer objectivement différentes versions entre elles.
- Lien entre évaluation et coût : réduire le nombre de tokens, envoyer des documents plus courts, demander des réponses plus concises ou utiliser un modèle sans temps de réflexion sont des leviers directs pour réduire le coût selon la performance visée.
- Utilité de l'évaluation pour repérer précocement une dégradation de performance de l'agent avant qu'elle ne s'aggrave ; rappel que le choix du modèle est lié au prix, à la quantité de tokens consommés et au résultat attendu, un arbitrage à faire sciemment.
- Présentation de l'onglet d'évaluation natif de N8n qui facilite la visualisation des résultats, tout en précisant que cette fonctionnalité pourrait être reproduite manuellement en dehors de N8n avec un autre outil.
- Présentation du cas pratique support client utilisé pour la démo d'évaluation : deux Data Tables, l'une pour vérifier l'état d'une commande (exemples fictifs), l'autre pour consulter les règles et politiques de retour produit.
- Présentation du prompt de l'agent testé, incluant règles de réponse et règles de catégorisation (un des aspects évalués pour les agents catégoriseurs), avec usage d'un structured output pour structurer la réponse.
- Présentation d'un jeu d'évaluation volontairement court (pour la démo) avec recommandation forte d'utiliser un jeu de test bien plus large en production (vingtaine à cinquantaine d'exemples) pour couvrir davantage de cas.
- Exemple concret de cas d'évaluation : une requête sur un numéro de commande spécifique doit renvoyer les détails exacts connus de cette commande (statut de livraison), sans utilisation d'outil supplémentaire dans ce cas précis.
- Rappel du coût induit par l'évaluation elle-même : chaque exécution consomme un appel LLM, potentiellement doublé par un second LLM chargé d'évaluer les résultats, nécessitant d'arbitrer selon l'importance réelle du workflow concerné.
- Démonstration de la configuration du trigger d'évaluation connecté à l'EvalDataset : un test rapide confirme que le premier item du dataset (exemple commande 1234) est bien récupéré et affiché.
- Ajout de l'output node dans l'onglet évaluation, chargé d'enregistrer les réponses réelles obtenues face au dataset, une étape nécessaire après avoir vérifié que le trigger fonctionne correctement.
- Explication du mécanisme de branchement conditionnel (type if node) qui distingue une exécution réelle d'une exécution d'évaluation, chacune suivant une branche dédiée du workflow selon le contexte de déclenchement.
- Configuration de l'output en récupérant la colonne de réponse attendue du dataset et en y copiant le résultat réellement obtenu de l'agent, pour permettre la comparaison entre attendu et obtenu.
- Alternative possible : sauter l'étape automatisée et évaluer manuellement les réponses contre les attentes ; présentation des sept métriques disponibles pour l'évaluation automatisée, chacune correspondant à un critère différent.
- Présentation de la métrique String Similarity, adaptée à la vérification de catégorisation : score de 0 à 1 mesurant la similarité (nombre de changements nécessaires) entre la réponse obtenue et la réponse attendue fournie.
- Démonstration d'une évaluation combinant plusieurs métriques simultanément (trois sur les cinq disponibles), l'outil permettant de choisir librement le nombre et le type de critères à évaluer en parallèle.
- Précision sur la métrique d'utilisation des outils : possibilité de lister plusieurs outils attendus séparés par des virgules, illustré par un cas de retour de commande nécessitant à la fois la révision de commande et les politiques de retour.
- Présentation de la métrique par prompt LLM évaluant sur une échelle de 1 à 5 la ressemblance de la réponse ; ce prompt d'évaluation peut lui-même être généré via ChatGPT ou Gemini selon la préférence de l'utilisateur.
- Précision sur les limites d'exécution parallèle des évaluations selon le plan N8n : une seule exécution séquentielle en Community/Pro, trois à cinq en parallèle en Business/Enterprise, ou limite modifiable via variables d'environnement en self-hosted.
- Résultat chiffré d'une première évaluation révélant un problème : score de 0,43 sur l'utilisation des outils, signifiant que la moitié des cas n'utilisent pas les outils comme attendu, malgré un bon score de correctness global.
- Investigation du score faible d'utilisation d'outils (0,43) : la première exécution des tests affiche 0%, avec possibilité de cliquer directement sur le test pour accéder à l'exécution détaillée et diagnostiquer le problème.
- Après correction, constat d'amélioration : le score d'utilisation d'outils passe de 0,43 à 1 (usage systématique correct), avec recommandation de ne pas se limiter à une seule exécution pour valider une amélioration.
- Constat de scores mitigés sur une évaluation particulière (100% sur certains critères, 50% sur un autre), affectant la correctness globale de la réponse, illustré par le cas concret de la commande 5678 à retourner.
- Diagnostic de la piste d'amélioration : ajuster le modèle ou le prompt pour préciser que face à un numéro de commande combiné à une demande de retour, l'agent doit utiliser les deux outils simultanément, en enrichissant le prompt en conséquence.
- Confirmation que la correction du prompt a résolu l'erreur identifiée, avec meilleure garantie d'éviter ce type de problème en production, illustrant le procédé itératif nécessaire à l'optimisation continue d'un agent.
- Insistance sur le procédé itératif indispensable pour garantir des résultats fiables en production et un workflow digne de confiance pour le client, avec recommandation de ne modifier qu'un seul élément à la fois lors de chaque itération.
- Précision sur une limitation de plan N8n : impossible de lancer l'évaluation avec custom metrics (graphiques de résultats) sur plusieurs workflows simultanément, message « limit reached » affiché au-delà d'un workflow évalué à la fois.
- Astuce technique de prompt engineering pour éviter une erreur de syntaxe : lorsqu'un outil n'est pas utilisé, il faut garder une portion de string spécifique dans le prompt, sinon les doubles crochets d'une expression restent ouverts et cassent la syntaxe.
- Recommandation d'intégrer aussi les Guardrails et la conformité RGPD dans l'évaluation d'un agent, une couche de vérification supplémentaire à ajouter une fois les règles de sécurité et de conformité déjà en place.

## Concepts cles
- plan de présentation du module évaluation des agents IA
- distinction entre fonctionnement technique visible et validation réelle de la qualité
- définition de l'évaluation : objectivation chiffrée de la performance
- leviers de réduction de coût liés à l'évaluation (tokens, longueur, modèle sans réflexion)
- détection précoce de dégradation via évaluation
- arbitrage modèle/prix/résultat attendu
- onglet d'évaluation natif N8n (reproductible manuellement hors N8n)
- cas pratique de démo : Data Tables commandes et politiques de retour
- prompt avec règles de catégorisation et structured output
- recommandation d'un jeu de test large en production (20-50 exemples)
- exemple de cas de test attendant une réponse précise sans outil
- coût de l'évaluation (double appel LLM possible : exécution + évaluation)
- configuration et test du trigger connecté à l'EvalDataset
- ajout de l'output node pour enregistrer les réponses réelles
- branchement conditionnel évaluation vs exécution réelle (if node)
- configuration de l'output : comparaison attendu vs obtenu
- alternative manuelle vs sept métriques d'évaluation automatisée
- métrique String Similarity (score 0-1 basé sur la similarité textuelle)
- évaluation multi-métriques simultanée (choix libre parmi cinq critères)
- métrique d'utilisation des outils (liste attendue séparée par virgules)
- métrique par prompt d'évaluation LLM (échelle 1-5), générable via ChatGPT/Gemini
- limites d'exécution parallèle des évaluations selon le plan N8n (self-hosted modifiable)
- résultat d'évaluation révélant un problème d'usage d'outils (score 0,43)
- diagnostic détaillé d'un test en échec via accès direct à l'exécution
- amélioration du score d'utilisation d'outils après correction (0,43 vers 1)
- recommandation de ne pas se fier à une seule exécution
- cas concret de score mitigé affectant la correctness (commande 5678)
- correction du prompt pour préciser l'usage combiné de deux outils
- validation de la correction et procédé itératif d'optimisation
- procédé itératif d'optimisation d'agent
- recommandation de ne changer qu'un seul élément par itération
- limitation de plan : un seul workflow évalué avec custom metrics à la fois
- astuce anti-erreur de syntaxe liée aux doubles crochets dans le prompt
- intégration des Guardrails et de la conformité RGPD dans l'évaluation

## Outils mentionnes
- n8n
- ChatGPT
- Gemini

## Tips techniques
- Réduire les tokens consommés (documents plus courts, réponses concises, modèle sans temps de réflexion) pour maîtriser le coût d'un agent IA
- Évaluer régulièrement un agent en production pour repérer une dégradation de performance avant qu'elle ne s'aggrave
- Utiliser un jeu de données d'évaluation d'au moins 20 à 50 exemples en production, jamais seulement 5 à 7 cas comme en démo
- Générer le prompt d'évaluation LLM lui-même via ChatGPT ou Gemini plutôt que de le rédiger entièrement à la main
- Ajuster la limite d'exécutions parallèles d'évaluation via les variables d'environnement en self-hosted pour accélérer les tests
- Ne jamais valider une amélioration d'agent sur une seule exécution de test, répéter pour confirmer la stabilité du résultat
- Préciser explicitement dans le prompt les cas où plusieurs outils doivent être utilisés simultanément, pour éviter les oublis de l'agent
- Ne modifier qu'un seul élément à la fois lors des itérations d'optimisation d'un agent, pour isoler clairement l'effet de chaque changement
- Toujours garder une portion de texte de secours dans le prompt pour éviter une rupture de syntaxe des doubles crochets quand un outil n'est pas utilisé
- Inclure la vérification des Guardrails et de la conformité RGPD comme critère d'évaluation additionnel d'un agent

## Cas d'usage reels
- [[]]
