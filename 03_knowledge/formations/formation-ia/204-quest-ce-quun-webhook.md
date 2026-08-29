---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.04 Qu’est-ce qu’un Webhook.txt"
---

# 2.04 Qu’est-ce qu’un Webhook

## Resume
- Introduction aux Webhooks, présentés comme un élément important de l'automatisation, avec une comparaison directe visant à clarifier leur différence avec les Call API vus précédemment.
- Définition précise d'un webhook : une requête HTTP automatiquement envoyée dès qu'une condition est remplie dans une application (exemple : ajout d'un tag à un utilisateur dans un CRM), déclenchant une notification instantanée.
- Précision sur l'implémentation des webhooks dans Make et N8n : chacun propose des modules personnalisables avec une approche différente. Dès réception d'un événement par le webhook, l'ensemble du scénario est déclenché.
- Exemples concrets d'outils utilisant des webhooks : ActiveCampaign (envoi d'emails) déclenche un événement dès qu'un contact effectue une action spécifique, illustrant l'usage courant de ce mécanisme dans le marketing.
- Transition vers une démonstration pratique dans ClickFunnels, un outil de tunnels de vente, pour illustrer concrètement le fonctionnement d'un webhook dans une interface réelle.
- Démonstration de la création d'un webhook dans ClickFunnels : définir un nouvel endpoint, le point d'arrivée qui va recevoir les données envoyées par le déclencheur.
- Configuration pratique du webhook : nommage explicite (« Nouvelle commande »), destination définie vers Make, et sélection des événements précis qui déclencheront cette transmission de données.
- Clarification terminologique : le webhook désigne le type de transmission de données, tandis que l'endpoint est l'URL précise qui recevra ces données (exemple : dès création d'une commande, l'URL configurée sera atteinte).
- Démonstration de la connexion pratique entre ClickFunnels et Make : générer l'URL du webhook dans Make, la copier, puis la coller dans le champ endpoint de ClickFunnels pour établir la liaison entre les deux outils.
- Démonstration du déclenchement de test via Run Once dans Make : le scénario attend une donnée entrante après configuration, illustrant le mécanisme de test manuel avant mise en production réelle.
- Introduction du concept de bundle : ce que Make reçoit du webhook est un bundle contenant toutes les informations envoyées, correspondant en réalité à du JSON bien formaté, faisant le lien avec le module JSON précédemment étudié.
- Mise en garde sur la gestion de forte volumétrie : envoyer un événement à une large base (exemple 40 000 personnes) simultanément peut générer un afflux massif de requêtes, un point d'attention crucial pour les webhooks à fort volume.
- Choix entre traitement parallèle ou séquentiel des requêtes selon la fiabilité de l'API réceptrice : l'auteur recommande d'attendre les réponses avec des outils marketing anciens dont les API sont moins robustes que celles de référence comme Google Sheets.
- Présentation du panneau de gestion des webhooks : statut actif/inactif, association aux scénarios (navigation directe possible), détail du webhook, et file d'attente (queue) des messages en attente de traitement.
- Information technique importante : Make ne stocke les webhooks que trois jours, au-delà desquels ils peuvent disparaître s'ils ne sont pas traités, un point de vigilance à connaître absolument. Mention également des logs d'historique disponibles.

## Concepts cles
- introduction aux Webhooks et distinction avec les Call API
- définition d'un webhook (requête HTTP automatique conditionnelle)
- modules webhook personnalisables sur Make et N8n (approches différentes)
- exemple concret : ActiveCampaign et déclenchement d'événements webhook
- démonstration pratique de webhook dans ClickFunnels
- création d'un endpoint webhook dans ClickFunnels
- nommage et configuration d'événements spécifiques pour un webhook
- distinction webhook (type de transmission) vs endpoint (URL de destination)
- liaison pratique entre outils via copie d'URL de webhook
- test manuel via Run Once avant mise en production
- bundle Make comme JSON formaté reçu du webhook
- gestion de forte volumétrie de requêtes webhook simultanées
- choix parallèle vs séquentiel selon la fiabilité de l'API cible
- panneau de gestion des webhooks (statut, scénarios liés, queue)
- limite de rétention des webhooks Make (3 jours)

## Outils mentionnes
- Make
- n8n
- ActiveCampaign
- ClickFunnels
- Google Sheets

## Tips techniques
- Copier l'URL générée par le module webhook de l'outil récepteur et la coller dans l'endpoint de l'outil émetteur pour établir la connexion
- Privilégier un traitement séquentiel (attendre les réponses) avec des API peu fiables ou anciennes plutôt que le traitement parallèle par défaut
- Attention : Make ne conserve les webhooks non traités que 3 jours avant de les perdre définitivement

## Cas d'usage reels
- [[]]
