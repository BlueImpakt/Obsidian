---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.06 Première Automatisation sur N8N.txt"
---

# 3.06 Première Automatisation sur N8N

## Resume
- Introduction à la construction de la première automatisation avancée avec N8n, présentée délibérément à ce stade pour alterner théorie et pratique et rendre l'apprentissage plus digeste.
- Présentation de Calendly comme exemple de base : configuration de durée, localisation avec lien Google Meet automatique, définition d'horaires de travail synchronisés avec le calendrier existant.
- Généralisation du cas d'usage Calendly comme page de réservation type, utilisable par tout coach, formateur ou responsable d'entreprise pour permettre à des prospects de prendre rendez-vous facilement.
- Configuration du trigger Calendly dans N8n : choix entre Personal Access Token ou OAuth pour l'authentification, sélection du déclencheur « On Event Created » qui se déclenche dès qu'un nouvel événement est créé.
- Démonstration de création d'une application sur Calendly Developer (interface séparée nécessitant un compte dédié), avec nommage de l'application pour préparer l'intégration OAuth avec N8n.
- Configuration de l'environnement sandbox et de la Redirect URI (fournie par Calendly), suivie de la récupération du Client ID et Client Secret nécessaires à la connexion OAuth.
- Test pratique de réservation via le formulaire Calendly avec des données fictives, rencontrant un souci d'affichage d'un champ budget potentiellement lié à une restriction du plan gratuit versus premium.
- Finalisation de la réservation test et confirmation de la réception de l'information côté N8n, validant le bon fonctionnement du déclencheur configuré précédemment.
- Objectif suivant : insérer les résultats du formulaire de réservation dans une page Notion plutôt que Google Sheets déjà largement utilisé, pour varier les exemples et montrer d'autres intégrations.
- Création d'une base de données Notion type CRM basique en français, avec champs date, nom, contact, lien Google Meet, et budget (type select), illustrant la structuration d'un CRM minimal.
- Finalisation de la base de données Notion avec ajout automatique de vues et de pages de test, obtenant un CRM opérationnel prêt à être rendu accessible pour l'intégration N8n.
- Configuration de l'intégration Notion : définition d'un logo optionnel, récupération du jeton secret (token) et définition des accès (tout visible) pour connecter N8n à la base de données.
- Insertion du token dans N8n et connexion réussie donnant accès à toutes les bases de données Notion partagées, avec un léger délai d'attente nécessaire pour la synchronisation.
- Démonstration de partage explicite de la base de données spécifique avec l'intégration N8n créée (nommée « test2 »), une étape nécessaire pour que N8n puisse y accéder concrètement.
- Démonstration de création d'une nouvelle page dans la base Notion sélectionnée : renseignement du nom de l'invité et exploration des propriétés disponibles (budget, contact, date, lien Google Meet).
- Accès au JSON complet provenant de Calendly, permettant de creuser dans les données via la notation par point pour explorer les quatre options de premier niveau disponibles.
- Détail des quatre options de premier niveau du JSON Calendly : Created at, Created by, Event, et Payload, avec démonstration de l'accès au deuxième niveau via ajout d'un point supplémentaire.
- Recommandation d'utiliser le clavier plutôt que la souris pour une navigation plus rapide et propre, avec introduction d'une bonne pratique essentielle sur la référence par défaut à l'étape précédente en JSON.
- Démonstration d'ajout de ligne dans Google Sheets avec sélection du document via ID plutôt que menu déroulant, une méthode que l'auteur trouve plus simple et directe.
- Test de l'ajout du nom Jean Dupont, mais rencontre d'un problème : la valeur attendue n'est pas retrouvée, révélant un bug de référence de données à investiguer dans le chunk suivant.
- Explication clé du bug : le JSON fait maintenant référence à Google Sheets (dernière étape) et non plus à Calendly, rendant la valeur dynamique invalide. Bonne pratique fondamentale : ne jamais utiliser $json seul sauf nécessité absolue.
- Explication approfondie : le JSON change à chaque ajout de node intermédiaire, cassant les références. La solution est de nommer explicitement le module source cible plutôt que d'utiliser la référence générique.
- Exemple pratique de définition de valeur remplie (1000€) et découverte d'un Array imbriqué dans la structure de questions/réponses de Calendly, illustrant la complexité de certaines structures de données.
- Recommandation pratique : toujours privilégier Calendly Trigger comme référence et ajouter les éléments intermédiaires par copier-coller des valeurs, plutôt que par manipulation directe risquée.
- Explication cruciale sur le drag and drop : il utilise par défaut la nomenclature JSON générique (donc fragile), contrairement au copier-coller manuel qui préserve la référence explicite et robuste au module source.
- Manipulation d'une date/heure spécifique (7 juillet 12h30) avec option de définir une timezone statique ou dynamique, en appliquant la même bonne pratique de référence explicite précédemment enseignée.
- Recherche en direct de l'emplacement exact de la timezone dans la structure de données (finalement trouvée sous Time Zone plutôt que Schedule Event), illustrant le processus d'exploration itérative d'une structure JSON complexe.
- Finalisation du remplissage des champs de la page Notion (Join URL formaté correctement, nom du client), avec vérification que tous les éléments nécessaires (lien Google Meet, budget) sont bien récupérés.
- Possibilité de récupérer également le lien Calendly pour du tracking supplémentaire si besoin, puis exécution du step qui enregistre effectivement le rendez-vous dans la base de données Notion.
- Récupération de l'adresse email en naviguant dans le Payload via notation par point, puis validation finale que le rendez-vous avec Jean Dupont a bien été enregistré correctement, sans oubli cette fois.

## Concepts cles
- introduction pédagogique alternant théorie et pratique avancée
- présentation de Calendly (durée, lien Meet, synchronisation calendrier)
- généralisation du cas d'usage page de réservation (coach, formateur)
- configuration du trigger Calendly (Personal Access Token vs OAuth)
- création d'application sur Calendly Developer (interface séparée)
- configuration sandbox, Redirect URI, Client ID/Secret pour OAuth
- test pratique de formulaire Calendly avec limite potentielle de plan
- validation de la réception du trigger Calendly côté N8n
- choix de Notion pour varier les intégrations démontrées
- création d'un CRM basique dans Notion (champs date/nom/contact/budget)
- finalisation du CRM Notion avec vues et pages de test
- configuration du jeton secret et des accès pour l'intégration Notion
- connexion réussie donnant accès aux bases de données Notion
- partage explicite d'une base de données spécifique avec l'intégration N8n
- création d'une nouvelle page Notion avec renseignement des propriétés
- exploration du JSON complet Calendly via notation par point
- quatre options de premier niveau du JSON Calendly (Created at/by, Event, Payload)
- recommandation d'usage du clavier
- introduction d'une bonne pratique JSON essentielle
- sélection de document Google Sheets via ID plutôt que menu déroulant
- bug de référence de donnée non retrouvée (mise en place du problème)
- bonne pratique fondamentale : ne jamais utiliser $json seul (référence l'étape précédente immédiate)
- solution : nommer explicitement le module source plutôt que référence générique
- exemple pratique et découverte d'un Array imbriqué dans Calendly
- recommandation : Calendly Trigger comme référence stable + copier-coller
- drag and drop utilise JSON générique fragile vs copier-coller robuste
- gestion de date/heure avec timezone dynamique (application de la bonne pratique)
- exploration itérative en direct pour localiser un champ dans le JSON
- finalisation des champs Notion (Join URL, nom client)
- enregistrement final dans Notion avec possibilité de tracking Calendly
- validation finale de l'enregistrement complet avec email récupéré

## Outils mentionnes
- n8n
- Calendly
- Google Meet
- Notion
- Google Sheets

## Tips techniques
- Partager explicitement chaque base de données Notion avec l'intégration créée, sinon N8n n'y aura pas accès
- Privilégier la navigation au clavier plutôt qu'à la souris pour une construction plus rapide et propre des expressions dynamiques
- Ne jamais utiliser la référence $json seule sauf nécessité absolue : elle pointe toujours vers l'étape immédiatement précédente, source de bugs
- Toujours nommer explicitement le module source d'une donnée plutôt que d'utiliser la référence générique $json qui casse en cas d'ajout de node
- Préférer le copier-coller de valeurs plutôt que le drag and drop, ce dernier utilisant par défaut une référence JSON générique fragile

## Cas d'usage reels
- [[]]
