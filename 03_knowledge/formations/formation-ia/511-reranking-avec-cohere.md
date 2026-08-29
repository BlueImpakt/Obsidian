---
tags: [formation, millenium]
module: Formation IA
section: "Construire ses RAG"
source_transcript: "5.11 Reranking avec Cohere.txt"
---

# 5.11 Reranking avec Cohere

## Resume
- Introduction au reranking via le node CohereRanking de N8n, second mécanisme d'amélioration des résultats RAG au-delà du filtrage par métadonnées.
- Explication du principe du reranking : Cohere analyse et compare les dix résultats vectoriels obtenus à la question posée, pas seulement sémantiquement mais de manière plus fine.
- Détail du mécanisme de scoring du reranking : Cohere attribue un score de pertinence à chaque morceau puis les réorganise, avec option de ne transmettre que les meilleurs plutôt que tous dans l'ordre initial.
- Exemple avant/après illustrant le reranking : aucun filtrage initial par document, la recherche vectorielle ramène tout, puis le reranking ne conserve que la crème de la crème des résultats.
- Démonstration de récupération de la clé API Cohere et d'ajout simple du reranking dans un nœud existant, une intégration facile même sur un RAG naïf déjà en place.
- Test comparatif avec la même question posée précédemment (« qu'est-ce qu'un webhook ? ») pour observer si le reranking modifie l'ordre de présentation des résultats identiques.
- Présentation du prix de Cohere : 1000 requêtes gratuites, puis un coût très faible (dixième de centime pour moins de 100 chunks), un service très accessible pour améliorer un RAG.
- Observation positive du reranking : il peut révéler des résultats inattendus dans des catégories de documents non envisagées initialement mais complémentaires à la réponse recherchée.
- Mise en garde sur une limite du reranking seul : il peut privilégier un document très précis mais obsolète (2023 vs 2026) sans contexte de date, d'où l'intérêt de combiner avec un filtre par date.
- Exemple d'usage avancé des metadata tags pour le contrôle d'accès multi-tenant/multi-rôle, illustré par un agent RAG d'entreprise où certains documents sont réservés à certains rôles.
- Conclusion du module reranking : recommandation forte d'explorer cette technique facile à ajouter à tout agent RAG existant, avec mise à disposition du workflow pour expérimentation personnelle.

## Concepts cles
- introduction au reranking via le node CohereRanking de N8n
- explication du principe du reranking Cohere (comparaison fine au-delà du sémantique)
- détail du mécanisme de scoring et réorganisation du reranking Cohere
- exemple avant/après illustrant le principe du reranking (crème de la crème)
- démonstration de récupération de clé API Cohere et intégration facile
- test comparatif avec la même question pour observer l'effet du reranking sur l'ordre
- prix de Cohere : 1000 requêtes gratuites puis coût très faible
- observation positive : le reranking révèle des résultats inattendus et complémentaires
- limite du reranking seul : privilégier un document précis mais obsolète sans filtre de date
- exemple d'usage des metadata tags pour contrôle d'accès multi-tenant/multi-rôle
- conclusion : recommandation d'ajouter facilement le reranking à un RAG existant

## Outils mentionnes
- n8n
- Cohere

## Tips techniques
- Combiner le reranking avec un filtre de métadonnées par date pour éviter que des documents précis mais obsolètes ne soient privilégiés
- Utiliser les metadata tags pour implémenter un contrôle d'accès multi-tenant/multi-rôle dans un RAG d'entreprise partagé
- Toujours tester l'ajout du reranking sur un RAG existant, une amélioration facile à intégrer avec un potentiel gain de pertinence significatif

## Cas d'usage reels
- [[]]
