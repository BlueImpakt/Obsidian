---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.06 Les connexions sur Make.txt"
---

# 2.06 Les connexions sur Make

## Resume
- Introduction aux types de connexions sur Make : principalement trois méthodes existent pour connecter ses outils préférés, dont OAuth qui permet une connexion directe sans manipulation de clé.
- Démonstration du flux OAuth classique : « Sign in with Google » propose automatiquement les autorisations d'accès nécessaires (lecture de fichiers), l'utilisateur validant simplement pour établir la connexion instantanément.
- Présentation de la méthode par clé API : chercher dans les réglages de l'outil une section Integration, Developer ou API Keys pour générer un nouveau jeton d'authentification (token), une méthode alternative à OAuth.
- Mise en garde de sécurité importante : ne jamais laisser visible une clé API dans un tutoriel ou une démonstration publique, car n'importe qui pourrait l'utiliser pour accéder au compte sans limite.
- Démonstration pratique de connexion à Make lui-même via clé API personnelle : accéder aux paramètres, section token API, créer et copier le token, puis le coller dans Make pour finaliser la connexion.
- Présentation du panneau centralisé des connexions Make, listant toutes les connexions établies. Précaution notée : certaines connexions peuvent nécessiter une réautorisation périodique du fait d'une durée de validité limitée.

## Concepts cles
- trois types principaux de connexions sur Make (dont OAuth)
- flux OAuth classique via Sign in with Google
- méthode par clé API (Integration/Developer/API Keys)
- mise en garde de sécurité sur l'exposition publique de clés API
- connexion à Make via son propre token API
- panneau centralisé des connexions
- durée de validité limitée nécessitant réautorisation

## Outils mentionnes
- Make
- Google

## Tips techniques
- Ne jamais exposer une clé API réelle dans un tutoriel public : la révoquer immédiatement après démonstration ou utiliser une clé factice

## Cas d'usage reels
- [[]]
