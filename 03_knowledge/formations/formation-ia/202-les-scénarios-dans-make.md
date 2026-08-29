---
tags: [formation, millenium]
module: Formation IA
section: "Les bases de Make"
source_transcript: "2.02 Les scénarios dans Make.txt"
---

# 2.02 Les scénarios dans Make

## Resume
- Introduction aux scénarios Make : chaque automatisation créée constitue un scénario, pouvant prendre différentes formes, être organisé dans des dossiers, avec pour objectif de comprendre leur structure générale.
- Exemples concrets d'organisation de scénarios personnels de l'auteur : lead magnets (ressources offertes contre abonnement newsletter), notifications, achats, scraping, support client, webinaires, illustrant une structuration thématique claire.
- Rappel que Make reste l'outil secondaire de l'auteur (N8n étant le primaire). Présentation de la structure de la liste des scénarios : chaque scénario affiche une prévisualisation des outils utilisés.
- Démonstration de la fonction de recherche des scénarios : possible de chercher par outil spécifique utilisé (exemple : IFTTT), sans nécessité que le nom de l'outil apparaisse dans le titre du scénario pour être trouvé.
- Présentation de deux méthodes pour catégoriser les scénarios : déplacer vers un dossier (Move to Folder) après création du dossier concerné, ou simplement les glisser-déposer (drag and drop) directement dans l'interface.
- Conseil de nomenclature pour les scénarios : structurer les noms par type (« formulaire », « produit ») en précisant les outils impliqués (Sheets, CRM), créant une convention de nommage cohérente et facile à suivre.
- Mention de l'utilité de la nomenclature structurée dans les grandes organisations avec de nombreux collaborateurs. Introduction du canvas Make : possibilité de zoomer, dézoomer et se déplacer librement sur l'espace de travail.
- Point crucial sur la sauvegarde : contrairement à d'autres outils, Make ne sauvegarde pas automatiquement le travail, il faut sauvegarder manuellement via le bouton dédié, une différence importante à ne pas oublier.
- Présentation des scénarios input et output : possibilité d'ajouter des variables fixes qui restent constantes tout au long du scénario, liées à l'input initial et conservées directement dans le workflow.
- Introduction aux paramètres avancés du scénario, avec avertissement de complexité croissante à venir. Premier paramètre présenté : le Sequential Processing, une notion importante à bien comprendre.
- Explication du Sequential Processing : les automatisations peuvent s'exécuter séquentiellement (une action après l'autre) ou en parallèle (plusieurs exécutions simultanées), l'option forçant l'ordre séquentiel étant utile dans certains contextes précis.
- Illustration concrète du risque d'échec temporaire d'API : si l'API Google Sheets tombe en panne pendant une minute au moment d'un formulaire soumis, la donnée pourrait être perdue sans mécanisme de protection adéquat.
- Explication de l'option Enable Data Loss : permet, en cas d'arrêt de flux, d'accepter une perte de données au profit de la continuité du scénario, plutôt que de bloquer complètement l'exécution en cas de manque d'espace d'exécution.
- Explication du cas d'usage pour désactiver l'auto-commit : principalement pour les workflows utilisant des modules ACID, qui garantissent qu'un déclencheur ne s'active que si toutes les conditions exactes sont intégralement remplies.
- Présentation du réglage de tolérance aux erreurs consécutives : définir un seuil (ex: 10 erreurs) après lequel le scénario se désactive automatiquement, un mécanisme de protection contre les échecs répétés non contrôlés.
- Présentation de la fonctionnalité de notes contextuelles dans un scénario, particulièrement utile pour collaborer en équipe ou expliquer une automatisation vendue à un client, avec navigation directe vers l'élément commenté.

## Concepts cles
- définition des scénarios Make comme automatisations individuelles
- exemples concrets d'organisation thématique des scénarios
- structure d'affichage de la liste des scénarios (prévisualisation des outils)
- recherche de scénarios par outil utilisé (indépendamment du titre)
- catégorisation par dossier (déplacement ou drag and drop)
- convention de nomenclature des scénarios (type + outils impliqués)
- utilité de la nomenclature en contexte d'équipe
- navigation dans le canvas Make (zoom, déplacement)
- absence de sauvegarde automatique sur Make (sauvegarde manuelle obligatoire)
- variables fixes input/output du scénario
- introduction du Sequential Processing (paramètre avancé)
- exécution séquentielle vs parallèle (Sequential Processing)
- risque de perte de données lors d'une panne API temporaire (exemple Google Sheets)
- option Enable Data Loss (compromis continuité vs perte de données)
- modules ACID et désactivation de l'auto-commit
- seuil d'erreurs consécutives avant désactivation automatique
- notes contextuelles pour la collaboration ou la vente client

## Outils mentionnes
- Make
- n8n
- IFTTT
- Google Sheets

## Tips techniques
- Utiliser la recherche par outil pour retrouver un scénario, même si le nom de l'outil n'apparaît pas dans son titre
- Adopter une convention de nommage systématique pour les scénarios (type + outils impliqués) pour faciliter leur recherche future
- Toujours sauvegarder manuellement son scénario Make, l'outil ne sauvegardant jamais automatiquement
- Configurer un seuil de tolérance aux erreurs consécutives pour désactiver automatiquement un scénario défaillant
- Ajouter des notes contextuelles dans les scénarios complexes destinés à être partagés en équipe ou vendus à un client

## Cas d'usage reels
- [[]]
