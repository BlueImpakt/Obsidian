---
tags: [formation, millenium]
module: Formation IA
section: "Devenir un pro de n8n"
source_transcript: "3.32 Data Tables  Paul.txt"
---

# 3.32 Data Tables | Paul

## Resume
- Sommaire de la présentation des Data Tables N8n : introduction, utilité, comparaison avec Sheets/Excel, avantages et limitations de ces derniers, présentation d'Airtable, puis introduction de PostgreSQL.
- Présentation du besoin de stockage persistant : les workflows N8n traitent bien les données en temps réel, mais posent question dès qu'il s'agit de les stocker durablement pour un usage ultérieur.
- Inconvénients de solutions externes comme Google Sheets : lenteur due au contact réseau nécessaire, dépendance à la validité des credentials et au fait que personne d'autre ne modifie la table simultanément.
- Avantage majeur des Data Tables natives N8n : stockage directement sur la machine ou le serveur hébergeant N8n, offrant une vitesse quasi instantanée, avec pour seule limite la taille maximale de la table.
- Démonstration de création d'une Data Table : accessible depuis l'onglet dédié sur l'accueil N8n, avec possibilité de créer depuis zéro ou d'importer des données existantes.
- Explication du système d'ID automatique des Data Tables : généré automatiquement et incrémenté en permanence, même après suppression d'entrées, un identifiant toujours unique et croissant.
- Démonstration pratique de saisie de données (Paul, Marie) avec édition par double-clic, et ajout d'une valeur booléenne (VIP) illustrant les trois états possibles : vrai, faux, ou nul (non renseigné).
- Précision sur les règles de nommage des colonnes : les underscores sont autorisés (mais pas en début de nom), les espaces ne le sont pas, avec des instructions claires fournies par l'interface.
- Démonstration de la sélection de dates via un calendrier intégré pratique, ou possibilité d'utiliser un bouton « now » pour insérer automatiquement la date et l'heure actuelles.
- Précision sur la saisie manuelle dans une Data Table : possibilité d'utiliser un point décimal pour d'autres types de valeurs, mais uniquement les formats compatibles avec la colonne concernée sont acceptés.
- Introduction aux opérations CRUD permettant de travailler avec n'importe quelle Data Table, un principe fondamental applicable à toute interaction avec une base de données, pas uniquement spécifique à N8n.
- Détail des cinq opérations CRUD disponibles : DELETE (supprimer des lignes), GET (lire), INSERT (créer), UPDATE (actualiser), et UPSERT (combinaison update/insert), avec options conditionnelles IF ROW EXISTS/DOES NOT EXIST.
- Introduction du filtrage de données via les onglets Any Conditions et All Conditions, permettant de filtrer les contacts avant même qu'ils n'arrivent dans le workflow.
- Explication d'All Conditions (logique ET) : toutes les conditions doivent être remplies simultanément pour qu'une ligne soit retenue, illustré par l'exemple d'un filtre sur le statut VIP.
- Démonstration pratique de filtrage combiné (VIP ET âge) : Marie (VIP) apparaît seule avec la condition ET stricte, mais Paul apparaît aussi avec une condition OU plus souple sur l'âge.
- Conclusion de la démonstration des filtres, avec annonce d'un exercice pratique à venir pour consolider la compréhension via un cas d'usage concret applicable en situation réelle.
- Démonstration de l'import de données depuis un fichier CSV pour créer rapidement une Data Table préremplie, une alternative pratique à la saisie manuelle pour l'exercice à venir.
- Confirmation que le CSV contient déjà les titres de colonnes appropriés, facilitant la création automatique de la structure de table sans configuration manuelle supplémentaire.
- Présentation de l'exercice pratique : simuler le traitement d'une commande client pour un produit spécifique, avec la table de données fraîchement importée servant de base au scénario.
- Détail du scénario : réception d'un webhook contenant le produit demandé, la quantité souhaitée et le nom du client, posant les bases du workflow de traitement de commande.
- Définition des conditions métier à vérifier : stock suffisant disponible, et produit non périmé (au moins 30 jours restants avant péremption), des règles business essentielles à valider.
- Démonstration pratique de vérification du stock via un node IF, comparant la valeur du webhook au stock disponible pour déterminer si la commande peut être honorée.
- Configuration du second filtre de vérification : contrôle de la date de péremption via une expression dynamique comparant la date actuelle au seuil de péremption défini.
- Test du scénario avec un produit dont la péremption est lointaine (2027), confirmant le bon fonctionnement du filtre de validation qui laisse passer les produits valides.
- Ajout d'une notification en cas de produit périmé, et introduction d'une dernière vérification booléenne du statut « en vente » du produit avant de finaliser le traitement de la commande.
- Présentation de la fonctionnalité Dry Run sur les opérations d'écriture : permet de simuler une exécution sans réellement modifier les données, une sécurité précieuse pour éviter d'endommager accidentellement une base.
- Confirmation que le Dry Run n'exécute effectivement rien, un outil précieux pour tester en toute sécurité avant de passer à la configuration réelle de l'opération de mise à jour du stock.
- Finalisation de l'opération de mise à jour (calcul mathématique simple pour décrémenter le stock), avec possibilité d'ajouter un message de confirmation de commande complétée envoyé au client.
- Résolution d'un oubli de désactivation du Dry Run, avec exécution réelle finale confirmant la mise à jour effective du stock (passant à 47), validant le workflow complet de bout en bout.
- Conclusion sur l'intérêt d'une source de vérité unique et intégrée pour tous les processus utilisant les mêmes données, ouvrant la voie à de nombreux autres projets d'intelligence artificielle intéressants à explorer.
- Introduction d'un cas d'usage avancé particulièrement intéressant : les agents IA de N8n peuvent travailler directement avec les nodes Data Tables, notamment via des valeurs booléennes pour des décisions de continuité de workflow.

## Concepts cles
- plan de présentation des Data Tables N8n
- besoin de stockage persistant au-delà du traitement en temps réel
- inconvénients de Google Sheets externe (lenteur, dépendance credentials)
- avantage de vitesse des Data Tables natives (vs solution externe)
- démonstration pratique de création d'une Data Table
- système d'ID auto-incrémenté et unique des Data Tables
- saisie de données et démonstration de valeur booléenne (vrai/faux/nul)
- règles de nommage des colonnes (underscores autorisés, pas d'espaces)
- sélection de dates via calendrier intégré ou bouton 'now'
- contraintes de saisie manuelle selon le type de colonne
- introduction aux opérations CRUD (principe fondamental des bases de données)
- cinq opérations CRUD détaillées (DELETE, GET, INSERT, UPDATE, UPSERT)
- filtrage via Any Conditions / All Conditions avant traitement
- logique ET d'All Conditions (toutes les conditions requises)
- démonstration pratique de filtres combinés (ET vs OU)
- annonce d'un exercice pratique consolidant les filtres
- import de données via fichier CSV pour créer une table préremplie
- import CSV avec titres de colonnes déjà présents
- présentation de l'exercice pratique de traitement de commande
- structure du webhook de commande (produit, quantité, client)
- conditions métier : stock suffisant et péremption (30 jours minimum)
- vérification du stock via node IF (comparaison avec le webhook)
- vérification de la date de péremption via expression dynamique
- test de validation avec produit à péremption lointaine
- notification de péremption et vérification finale du statut de vente
- fonctionnalité Dry Run pour simuler sans risque de modification
- confirmation du fonctionnement sûr du Dry Run
- finalisation de la mise à jour de stock avec confirmation client
- validation finale du workflow avec Dry Run désactivé (stock à 47)
- avantage d'une source de vérité unique et intégrée
- intégration des Data Tables avec les agents IA de N8n

## Outils mentionnes
- n8n
- Google Sheets

## Tips techniques
- Importer un fichier CSV pour créer rapidement une Data Table préremplie plutôt que de saisir manuellement chaque ligne
- Utiliser le Dry Run pour tester une opération d'écriture sur une Data Table sans risquer de modifier réellement les données

## Cas d'usage reels
- [[]]
