---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.11 Les Bundles dans Make.txt"
---

# 2.11 Les Bundles dans Make

## Resume
- Introduction aux structures de données et bundles dans Make, illustrée par un exemple concret d'email : connexion à Gmail via Watch Emails, avec possibilité de définir un dossier spécifique ou de scanner l'inbox complète avec filtrage.
- Analyse de deux bundles récupérés (exemple d'une facture Framer) : chaque email correspond à un bundle distinct, illustrant comment Make structure automatiquement chaque élément de données individuel dans un bundle séparé.
- Explication clé sur l'universalité de la structure de bundle : ce n'est pas propre à un email spécifique ni même à un compte Gmail particulier, mais une structure commune à absolument tous les emails envoyés via Gmail.
- Explication de la raison d'être des Arrays par défaut : comme un email peut avoir plusieurs pièces jointes, ce champ est obligatoirement un Array, contrairement aux champs uniques par nature (date d'envoi, taille, thread) qui n'en nécessitent pas.
- Démonstration visuelle de la structure avec deux pièces jointes numérotées 1 et 2 dans un email, illustrant concrètement comment plusieurs éléments d'un même type sont organisés au sein d'un Array.
- Importance de comprendre cette structure pour la sauvegarde de variables : un champ simple comme le sujet (subject) se sauvegarde facilement, contrairement à des données multiples nécessitant une gestion différente.
- Résolution d'un petit souci technique lors du test, révélant que deux variables distinctes sont définies pour deux emails différents (un reçu Framer et une réponse à une question), illustrant la gestion de plusieurs bundles simultanés.
- Nouvelle démonstration après relance du scénario : le bundle est dupliqué mais correctement traité, illustrant le comportement cohérent du système face à plusieurs occurrences de données similaires.
- Explication de la notation entre crochets dans un Array : elle définit précisément de quelle pièce jointe on parle (la première, la deuxième, etc.), un mécanisme d'indexation essentiel pour cibler un élément spécifique.
- Précision sur le comportement par défaut : sans indexation spécifiée, le système prend automatiquement le premier élément. Pour cibler un élément précis, il faut indiquer son numéro entre crochets (1 pour la première pièce jointe, 2 pour la seconde).
- Mise en garde importante : tenter de sauvegarder plusieurs valeurs d'un Array dans une seule variable sans gestion appropriée ne fonctionnera pas correctement, une seule valeur étant effectivement enregistrée malgré l'intention initiale.

## Concepts cles
- introduction aux bundles via l'exemple de Watch Emails (Gmail)
- structure d'un bundle correspondant à un élément de données individuel (exemple email)
- universalité de la structure de bundle pour tous les emails Gmail
- Arrays obligatoires pour les champs à cardinalité multiple (pièces jointes)
- numérotation visuelle des éléments d'un Array (exemple pièces jointes)
- sauvegarde simple d'un champ unique (sujet) vs champ multiple
- gestion de plusieurs bundles distincts simultanément
- comportement cohérent face à des bundles dupliqués
- notation entre crochets pour indexer un élément spécifique d'un Array
- comportement par défaut (premier élément) vs indexation manuelle
- limite de la sauvegarde directe de plusieurs valeurs d'un Array

## Outils mentionnes
- Make
- Gmail
- Framer

## Tips techniques
- Spécifier explicitement le numéro entre crochets pour cibler un élément précis d'un Array, sinon le premier est pris par défaut
- Ne pas tenter de sauvegarder directement plusieurs valeurs d'un Array dans une seule variable : utiliser un itérateur ou agrégateur à la place

## Cas d'usage reels
- [[]]
