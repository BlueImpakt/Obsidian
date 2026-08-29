---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.07 Les filtres dans Make.txt"
---

# 2.07 Les filtres dans Make

## Resume
- Introduction au fonctionnement des filtres sur Make : accessible via une icône en forme de clé à molette entre deux actions liées, permettant notamment de délier deux actions d'un scénario.
- Introduction à la configuration d'un filtre (Setup a Filter) : l'auteur compare brièvement avec l'approche de N8n qu'il préfère, tout en montrant la méthode spécifique à Make pour nommer et créer un filtre.
- Démonstration concrète de filtre appliqué à un formulaire Google Forms à choix multiples : sélectionner une valeur spécifique parmi les réponses possibles pour filtrer le passage des données.
- Présentation des premiers opérateurs génériques de filtre : existence de valeur (vide = n'existe pas, rempli = existe), constituant la base commune à tous les types de données avant les opérateurs spécifiques par type.
- Présentation des opérateurs de texte : equal to (égal), not equal to (différent), contains (contient une partie du texte), avec variante insensible à la casse (majuscule/minuscule ignorée).
- Suite des opérateurs de texte (ne commence pas par, ne termine pas par, matches patterns pour des motifs personnalisés) et introduction des opérateurs numériques (égal, différent, supérieur, inférieur).
- Détail des opérateurs numériques et de date/heure : égal, différent, supérieur, inférieur, supérieur ou égal, inférieur ou égal, applicables aux comparaisons chiffrées et temporelles.
- Configuration d'un filtre simple (valeur égale à une réponse spécifique) et introduction de la combinaison de filtres multiples via les opérateurs logiques AND et OR pour affiner les conditions de passage.
- Vérification pratique du fonctionnement du filtre : le chiffre 1 indique qu'une réponse Google Forms a été enregistrée et correspond bien au critère filtré (« intelligence artificielle »), confirmant la validation.
- Explication de l'arrêt du scénario en cas d'échec du filtre (indicateur 0) : aucune donnée n'ayant passé le filtre, le processus s'interrompt à cette étape, illustrant le mécanisme de blocage conditionnel.
- Ajout d'une troisième option de réponse (« Productivité ») au formulaire, publication de la mise à jour, puis test avec les trois options désormais disponibles pour enrichir la logique de filtrage.
- Démonstration de la logique OR : la réponse « Productivité » passe le filtre car elle correspond à l'un des critères définis, contrairement à « no code ». Présentation d'une approche alternative avec « not equal to » (exclusion) pour définir la même logique inversement.
- Piège logique identifié : combiner « not equal to » avec OR sur plusieurs valeurs échoue systématiquement (une valeur n'étant jamais égale à toutes les autres simultanément), la bonne approche étant d'utiliser AND dans ce cas précis.
- Reprise pédagogique du problème logique OR/AND : l'auteur explique pourquoi la réponse « productivité » échoue avec la combinaison de conditions choisie, chaque condition étant validée individuellement mais pas ensemble selon l'opérateur logique appliqué.
- Validation finale de la logique correcte : « intelligence artificielle » n'étant égale ni à « no code » ni à « productivité », les deux conditions sont validées et la réponse passe le filtre, illustré par la métaphore d'un unique garde filtrant l'accès.

## Concepts cles
- accès aux filtres via l'icône clé à molette entre actions
- configuration d'un filtre Make (comparaison avec préférence N8n)
- filtre appliqué à un formulaire à choix multiples (Google Forms)
- opérateurs génériques d'existence de valeur (vide/rempli)
- opérateurs de texte (equal, not equal, contains, insensible à la casse)
- opérateurs de texte avancés (patterns) et introduction des opérateurs numériques
- opérateurs numériques et de date/heure complets
- combinaison de filtres via opérateurs logiques AND/OR
- vérification pratique du fonctionnement d'un filtre (indicateur 1/0)
- arrêt du scénario en cas d'échec du filtre (indicateur 0)
- ajout d'une nouvelle option de réponse pour enrichir le filtrage
- logique OR pour valider un filtre
- approche alternative par exclusion (not equal to)
- piège logique OR vs AND pour les exclusions multiples
- reprise pédagogique du piège logique OR pour clarifier
- validation de la logique correcte (métaphore du garde filtrant)

## Outils mentionnes
- Make
- n8n
- Google Forms

## Tips techniques
- Utiliser AND (et non OR) pour combiner plusieurs conditions d'exclusion 'not equal to', sinon la logique échoue systématiquement

## Cas d'usage reels
- [[]]
