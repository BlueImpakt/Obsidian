---
tags: [formation, millenium]
module: Formation IA
section: "Comprendre l'Automatisation"
source_transcript: "1.05 Comprendre le fonctionnement des API.txt"
---

# 1.05 Comprendre le fonctionnement des API

## Resume
- Introduction au cours sur les API, conçue pour les débutants complets, avec renvoi vers une vidéo bonus plus approfondie pour ceux souhaitant aller plus loin sur le sujet.
- Introduction aux principes fondamentaux des API : tous les outils quotidiens en possèdent une, permettant de comprendre comment une information transite d'une application A vers une application B.
- Explication de l'intérêt commercial d'ouvrir une API : Facebook/Meta a intérêt à ouvrir son API aux CRM car cela permet aux entreprises utilisant leurs publicités payantes de récupérer directement les informations collectées via les formulaires publicitaires.
- Illustration de l'omniprésence des API dans les applications de messagerie quotidiennes (Facebook, WhatsApp, Telegram) : ce sont des API qui permettent de charger les messages et le contenu en temps réel entre les serveurs et l'application utilisateur.
- Introduction du JSON comme moyen universel de transfert d'information entre services. Analogie avec l'accusé de réception postal : le système de réponse API confirme que la requête a bien été reçue et traitée, comme une signature de facteur.
- Introduction du concept d'endpoints : une API n'est pas un bloc unique mais comporte plusieurs points de terminaison (adresses précises), chacun correspondant à une fonction spécifique.
- Exemples concrets d'endpoints : un endpoint « commandes » (ou « orders ») pour gérer les commandes d'une entreprise, un endpoint « produit » (ou « product ») pour modifier une fiche produit, illustrant la logique de nommage par fonction.
- Introduction du format JSON : un objet est délimité par des accolades, contenant des paires clé-valeur (exemple : ville, température, ciel), chaque valeur étant entourée de guillemets, formant la base de toute structure JSON.
- Description du fonctionnement côté serveur : constamment à l'écoute, il reçoit la demande via l'API, va chercher les informations dans la bonne base de données puis prépare et envoie la réponse correspondante.
- Illustration de la rapidité et de l'échelle des requêtes API : un simple clic produit une réponse en une seconde, un processus répété des milliards de fois par jour, constituant la base de toute automatisation où chaque action correspond à un appel API.
- Exemple concret de réponse API dans un contexte de paiement : validation si suffisamment d'argent disponible, ou refus avec message d'erreur si fonds insuffisants ou paiement non validé, illustrant la logique conditionnelle des réponses API.
- Synthèse essentielle sur les API : elles sont un intermédiaire entre logiciels, chaque requête devant cibler un endpoint précis pour être correctement interprétée, illustré notamment par le cas sensible des paiements en ligne nécessitant une précision absolue.

## Concepts cles
- introduction aux API pour débutants (renvoi à une vidéo bonus approfondie)
- fondamentaux des API pour la transmission d'information entre applications
- intérêt commercial de l'ouverture d'API (exemple Facebook/Meta)
- omniprésence des API dans les messageries (WhatsApp, Telegram)
- JSON comme format universel de transfert
- analogie de l'accusé de réception postal pour la réponse API
- endpoints comme points de terminaison précis d'une API
- exemples concrets d'endpoints nommés par fonction (commandes, produits)
- structure de base du JSON (objet, clé-valeur, accolades)
- fonctionnement côté serveur (écoute, recherche, réponse)
- échelle massive des requêtes API quotidiennes
- les API comme base de toute automatisation
- exemple de réponse API conditionnelle (validation/refus de paiement)
- synthèse : l'API comme intermédiaire logiciel ciblant des endpoints précis

## Outils mentionnes
- Facebook
- Meta
- WhatsApp
- Telegram

## Tips techniques
-

## Cas d'usage reels
- [[]]
