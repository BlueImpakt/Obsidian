---
tags: [formation, millenium]
module: Formation IA
section: "Comprendre l'Automatisation"
source_transcript: "1.04 Comment va se passer la formation.txt"
---

# 1.04 Comment va se passer la formation?

## Resume
- Introduction au déroulement pratique de la formation : recommandation d'utiliser un double écran, avec la vidéo placée dans un coin (bas à droite par exemple) pendant que l'outil pratiqué reste visible à côté, pour suivre efficacement les démonstrations.
- L'auteur affirme avoir la formule la plus simple à retenir pour obtenir des résultats suffisamment bons, et met en garde contre les prétendus « prompts magiques » vendus par certains, rappelant qu'il existe en réalité différentes formes légitimes de prompts.
- Présentation d'une ressource de référence recommandée : un document intitulé « Prompt Engineering » concentrant l'essentiel à savoir pour créer de bons prompts, disponible en anglais, que l'auteur a partiellement traduit et adapté avec des exemples.
- Introduction technique au contenu du document de référence : présentation de la LLM Output Configuration, incluant les contrôles d'échantillonnage (température, Top K, Top P) et la manière dont ces paramètres sont combinés dans le processus de génération.
- Complément sur le Top K sampling : une méthode définissant les probabilités des tokens les plus probables, distincte et antérieure conceptuellement au Top P (nucleus sampling) déjà présenté précédemment, offrant plus de flexibilité dans la sélection.
- Explication de la limite du Top K sampling : évite les non-sens totaux en restant sur des tokens probables, mais peut se révéler trop restrictif. C'est pour compenser cette rigidité que le Top P (nucleus sampling) est souvent préféré, offrant plus de flexibilité.
- Analogie du stagiaire pour expliquer l'imperfection des LLM : sans aucune instruction, le résultat est quasiment nul ; à l'inverse, un excès de détails sur chaque étape à suivre peut aussi générer des complications imprévues.
- Confession personnelle de l'auteur : il lui arrive occasionnellement de mal formuler ses prompts après de longues heures de travail intense, sans le recommander. Règle générale rappelée : plus un prompt est clair, plus il est facile pour le LLM de produire un bon résultat.
- Définition du Zero-Shot Prompting selon le document de référence : le prompt le plus simple, ne fournissant aucun exemple, juste une description directe de la tâche (question, début d'histoire, instructions).
- Mention d'un outil de test recommandé par le document source : Vertex AI Studio (Google), offrant un playground pour tester différentes techniques de prompting directement en pratique.
- Introduction du One-Shot et Few-Shot Prompting : contrairement au Zero-Shot, on fournit un (ou plusieurs) exemple(s) que le modèle va pouvoir imiter pour mieux compléter la tâche demandée.
- Exemple concret de Few-Shot Prompting appliqué à la commande de pizza : le modèle répond en JSON structuré avec taille, type et liste d'ingrédients (Array), illustrant concrètement le format de sortie structuré obtenu.
- Application pratique du Few-Shot pour créer des posts LinkedIn performants : identifier des templates de posts viraux existants, puis demander à ChatGPT ou Claude d'analyser leur structure pour s'en inspirer dans la génération.
- Introduction du System Prompting : définir un contexte global et un objectif pour le LLM, spécifier un format de sortie, établir des contraintes et un rôle — une structure qui se rapproche progressivement de celle enseignée par l'auteur (rôle/contexte/action/conditions).
- Précision sur le System Prompting : il définit la vision d'ensemble (big picture) et l'action attendue du modèle (traduire, classifier, etc.), se distinguant du contextual prompting par sa portée plus générale.
- Présentation du Role Prompting : demander au modèle d'incarner un métier, un rôle ou une identité spécifique, particulièrement utile en usage professionnel, un composant décrit comme fondateur dans la structure de prompt globale.
- Détail des variantes de rôle possibles : ton (contrarien, confrontationnel, descriptif, direct, formel, humoristique) ou expertise spécifique (expert en sciences de la vie, en copywriting, en scripts YouTube).
- Recommandation d'orienter explicitement le rôle dans le prompt : sans définition de rôle, le modèle répond selon la moyenne perçue des attentes générales, alors qu'un rôle bien défini permet d'obtenir une expertise ciblée et pertinente.
- Introduction du Step-Back Prompting : une technique améliorant la performance en posant d'abord une question générale liée à la tâche avant d'aborder la question spécifique, permettant de mieux ancrer le contexte.
- Illustration pratique du Step-Back Prompting : après avoir établi le contexte général via une première question, on revient au prompt original enrichi de ce contexte préalablement obtenu pour affiner la réponse finale.
- Introduction du problème des LLM avec les tâches mathématiques et de la solution du chain of thought : découper le raisonnement en plusieurs étapes plutôt que de demander directement la réponse finale, illustré par un exemple d'âge relatif.
- Démonstration de l'ajout de l'instruction « pense étape par étape » à un problème mathématique simple (âge relatif), une modification minime mais déterminante pour améliorer la précision du raisonnement du modèle.
- Confirmation de l'efficacité du chain of thought : un ajout minimal (« pense étape par étape ») suffit à déclencher un raisonnement structuré, particulièrement recommandé pour tout raisonnement complexe ou mathématique.
- Démonstration en direct montrant l'importance de l'outil de recherche (search) pour obtenir des chiffres précis et actualisés : sans cet outil activé, le modèle risque de donner des données incorrectes ou obsolètes.
- Présentation de la technique de self-consistency : envoyer le même prompt plusieurs fois avec une température élevée, puis retenir la réponse la plus fréquente parmi les résultats générés, au prix d'un coût plus élevé mais avec une meilleure cohérence.
- Illustration d'un exemple de classification de priorité de bug : évaluation basée sur des critères comme l'urgence, la criticité, et l'impact personnel, permettant d'orienter une décision structurée sur l'importance à accorder.
- Illustration du principe d'exploration par arbre de raisonnement (tree of thoughts) : tester plusieurs branches, éliminer celles qui ne correspondent pas, continuer à explorer les branches restantes jusqu'à converger vers la meilleure réponse finale.
- Conclusion sur le document de référence Prompt Engineering : l'auteur invite à approfondir soi-même le reste du contenu, en annonçant que la formation se concentrera sur un framework de prompt unique et suffisant, sans surcharger l'apprenant de théorie.

## Concepts cles
- recommandation d'usage d'un double écran pour suivre la formation
- mise en garde contre les 'prompts magiques' commerciaux
- existence de différentes formes légitimes de prompts
- document de référence 'Prompt Engineering' (source anglaise traduite)
- LLM Output Configuration (température, Top K, Top P)
- Top K sampling comme complément au Top P (nucleus sampling)
- limite restrictive du Top K compensée par le Top P
- analogie du stagiaire pour illustrer l'équilibre du niveau de détail d'un prompt
- règle générale : clarté du prompt facilite le traitement par le LLM
- définition du Zero-Shot Prompting (aucun exemple fourni)
- Vertex AI Studio comme playground de test recommandé
- One-Shot et Few-Shot Prompting (fourniture d'exemples à imiter)
- exemple concret de sortie JSON structurée via Few-Shot (commande pizza)
- application Few-Shot pour créer des posts LinkedIn viraux
- System Prompting (contexte, objectif, format, contraintes, rôle)
- distinction System Prompting vs Contextual Prompting
- Role Prompting comme composant fondateur du prompt
- variantes de rôle : ton vs expertise spécifique
- importance de définir explicitement un rôle pour obtenir une expertise ciblée
- Step-Back Prompting (question générale avant question spécifique)
- illustration pratique du Step-Back Prompting en deux temps
- difficulté des LLM avec les mathématiques
- solution via découpage en étapes (chain of thought)
- ajout de l'instruction 'pense étape par étape' comme levier de précision
- efficacité confirmée du chain of thought pour raisonnements complexes
- importance de l'activation de la recherche pour des chiffres précis
- technique de self-consistency (envois multiples, réponse majoritaire)
- exemple de classification de priorité selon critères multiples
- arbre de raisonnement (tree of thoughts) avec élimination progressive de branches
- conclusion : focalisation sur un framework de prompt unique et suffisant

## Outils mentionnes
- Vertex AI Studio
- ChatGPT
- Claude
- LinkedIn

## Tips techniques
- Utiliser un double écran avec la vidéo en petit format à côté de l'outil pratiqué pour suivre efficacement une formation pratique
- Consulter le document de référence 'Prompt Engineering' comme base théorique solide sur le prompting
- Toujours privilégier la clarté maximale du prompt, même sous fatigue ou pression de temps
- Analyser des posts LinkedIn viraux existants et les fournir en exemple au LLM pour améliorer la qualité du contenu généré
- Toujours définir un rôle explicite dans le prompt pour obtenir une réponse d'expertise ciblée plutôt qu'une réponse générique
- Ajouter systématiquement 'pense étape par étape' pour les problèmes de raisonnement ou mathématiques
- Déclencher systématiquement le chain of thought pour tout raisonnement mathématique ou logique complexe
- Utiliser la self-consistency (plusieurs envois du même prompt à température élevée) pour des réponses plus fiables, au prix d'un coût plus élevé

## Cas d'usage reels
- [[]]
