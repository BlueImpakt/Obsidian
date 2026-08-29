---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.08 Les routeurs dans Make.txt"
---

# 2.08 Les routeurs dans Make

## Resume
- Introduction aux routeurs (routers) sur Make, un élément important permettant de créer des branches multiples dans le flow selon différentes conditions, en reprenant l'exemple du scénario de formulaire déjà construit.
- Démonstration de la configuration d'un routeur : selon la condition remplie, la donnée est envoyée vers une branche ou une autre. Exemple d'exclusion de la valeur « no code » pour filtrer vers une branche spécifique.
- Exemple concret d'action déclenchée par branche : lorsque l'option est « intelligence artificielle », un email est envoyé automatiquement via Gmail vers une adresse support pour traiter le dossier d'inscription.
- Introduction du concept de fallback : la route qui capture tous les cas ne remplissant aucune des conditions définies précédemment, une route de secours optionnelle configurable manuellement ou automatiquement.
- Configuration pratique d'une seconde route pour la valeur « productivité », illustrant la construction progressive de multiples branches avec une identification claire de la route fallback restante.
- Test en direct du routeur : soumission d'une nouvelle réponse au formulaire (Théo Maréchal, intelligence artificielle), vérification que le filtre laisse bien passer la donnée et l'enregistre sur Google Sheets comme attendu.
- Comparaison critique entre Make et N8n sur les routeurs : l'auteur préfère l'approche N8n qui permet de rejoindre deux voies différentes, évitant d'avoir à recréer systématiquement les branches des deux côtés comme sur Make.

## Concepts cles
- introduction aux routeurs pour créer des branches conditionnelles
- configuration pratique d'un routeur avec conditions d'exclusion
- exemple concret : envoi d'email Gmail selon la branche déclenchée
- concept de route fallback (capture des cas non couverts)
- configuration pratique d'une seconde branche de routeur
- test en direct de la logique de routage complète
- comparaison Make vs N8n sur la gestion des routeurs (préférence N8n)

## Outils mentionnes
- Make
- Gmail
- Google Sheets
- n8n

## Tips techniques
-

## Cas d'usage reels
- [[]]
