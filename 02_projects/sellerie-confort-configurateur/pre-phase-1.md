---
tags: [sellerie-confort, pre-phase-1]
created: 2026-10-14
client: sellerie-confort
projet: sellerie-confort-configurateur
---

# Pré-phase 1 : contexte et reconnaissance

Le **contexte** de la mission : cadre contractuel, histoire, besoin, façon de travailler de Valérie, site et hébergement existants, constats hors périmètre. Les analyses et les tests de l'audit sont dans [[phase-1]], la préparation de la suite dans [[prepa-phase-2]]. Reconnaissance menée à partir de lectures publiques, du contrat signé, de la console OVH et des échanges avec Valérie ; rien n'a été modifié, ni chez OVH ni chez o2switch, ni sur le site.

Note réorganisée le 20/10 (contexte ici, analyses dans [[phase-1]]) : correspondance des anciens numéros dans [[phase-1]], annexe C.

Détails : [[2026-10-14-sellerie-confort-hebergement-acces]] · Projet : [[sellerie-confort-configurateur]] · Client : [[sellerie-confort]]

## 1. Cadre contractuel (signé le 13/10/2026)

| Point | Valeur |
|---|---|
| Documents | Contrat Phase 1 signé, devis **I-26-10-2** signé, facture émise, **acompte 700 € versé** |
| Prix | **1 400 € HT** = 4 j × 350 €, TVA non applicable (art. 293 B CGI) |
| Paiement | 50 % à la signature (700 €), solde 50 % (700 €) à la remise du rapport |
| Durée | **4 j de travail effectif** sur **10 jours calendaires** à partir de l'accès effectif. Prolongée si retard imputable au client |
| Échéance probable | **~23-24/10/2026** si l'accès date du 13 ou 14/10 : à confirmer par mail |
| Résiliation | Préavis écrit de 5 jours ; jours non faits non dus |
| Livrables | Propriété du client après paiement complet |

### Poste par poste (devis I-26-10-2)

| Poste | Jours |
|---|---|
| Audit du fonctionnement actuel et de la structure de données (plugin, stockage, faisabilité du regroupement par famille) | 1,00 |
| Clone local complet (données et médias), isolé de la production | 0,40 |
| Tests de rendu matières/couleurs, comparés aux photos réelles | 0,60 |
| Tests broderies / logos / **nid d'abeille** (zones à géométrie complexe, dosseret) | 1,00 |
| Estimation du temps de généralisation au catalogue | 0,30 |
| Rapport de synthèse, chiffrage Phase 2, plan d'action avec calendrier | 0,70 |
| **Total** | **4,00** |

### Offert dans la Phase 1
- Audit des tâches manuelles automatisables (temps et coût estimés)
- Diagnostic de la **perte de panier**, avec préconisation (cookies, sauvegarde de session)
- État des lieux du **suivi statistique**, avec outil de parcours utilisateur recommandé
- **Chiffrage de la refonte complète du site et d'une maintenance mensuelle**

### Phase 2
- Devis distinct, taux **350 €/j**, forfait jour
- **Plafond 7 000 € HT** ; 1 400 € de Phase 1 déduits, soit un solde max de **5 600 € HT**
- Si le temps dépasse l'estimation, le surplus est à ma charge. Tout ce qui est hors périmètre convenu passe par avenant
- La remise du rapport n'engage aucune des parties à conclure la Phase 2

### Limites et engagements
- Les tests sont des **essais de faisabilité** sur un échantillon. Engagement sur leur réalisation et la fidélité de leur restitution, **pas sur un rendu identique à une photographie** (art. 1, art. 7)
- **Accès** : compte administrateur WordPress temporaire, nominatif, révocable. Extension complémentaire possible avec autorisation. Jamais d'accès direct à la base de données
- **Production intacte**, sauf l'extension d'export temporaire, avec **accord écrit préalable** (un mail suffit), désinstallée dès l'export fait
- **Clone local isolé**, sans clients, commandes, paiements, comptes utilisateurs ni messages de formulaires ; si ces données se retrouvent dans l'export, suspendre, supprimer sans délai, informer le client. Environnement détruit à la fin de la Phase 1 sauf accord écrit
- **Outils d'IA tiers** (art. 4) : échantillon de photos et textures uniquement, aucune donnée personnelle, services privilégiés qui n'entraînent pas leurs modèles sur les contenus, usage commercial vérifié, photos et textures restent la propriété du client
- Je n'interviens ni sur l'hébergement, ni sur la maintenance, ni sur les outils du site (art. 2). Le client prévient son webmaster

## 2. Historique commercial

| Date | Fait |
|---|---|
| Début août 2026 | Maquettes envoyées |
| 07/08 | Retour client : « on aime beaucoup sauf le beige » ; demande d'ajout de matière plus simple, logos sur la selle, et prix |
| 07/08 | Devis I-26-08-1 à **1 600 € HT** (4 j × 400 €), contrat jamais signé |
| 07/10 | Réunion ~2 h avec Valérie : besoin confirmé, maquettes très appréciées, nouvelle offre orale à **1 400 €** (350 €/j) |
| 08/10 | Devis I-26-10-1 (1 400 €), maquettes envoyées |
| 13/10 | Contrat réécrit, clause de plafond ajoutée, devis I-26-10-2, **signature des deux** |
| 14/10 | Facture émise, acompte versé, accès admin WordPress reçus |

Contexte client : année difficile, très peu de commandes ; 15 000 € déjà investis dans le site il y a deux ans, pas satisfaits. Une agence web les rencontre **début novembre**. Valérie en congés **à partir du 17/10**.

## 3. Le besoin et la façon de travailler de Valérie

- Ajouter ou retirer une **matière** aujourd'hui : un fichier par zone, par matière et par modèle, saisis un par un, et c'est **VIMAWEB qui facture chaque demande**. Nouvelles matières en stock bloquées depuis longtemps
- **Nid d'abeille** = une broderie, seulement sur quelques modèles tout préparés ; ils veulent l'ajouter au configurateur
- Ajout d'un modèle ≈ **1 semaine**. Photos et Photoshop restent manuels (ça marche bien) ; on automatise l'ajout des matières sur chaque calque et le classement par famille
- Principe d'ergonomie : tout sur **une seule page**
- Priorité broderies : basse pour Valérie, haute pour moi (vrai plus du configurateur)

### 3.1 Vocabulaire : une « configuration »

Une **configuration** = tout le contenu du configurateur d'une fiche : la liste des calques (zones : Bec, Assises, Liserés…), pour chaque calque la liste de ses choix (nom, ordre, image par angle, vignette, choix par défaut) et les angles. Elle est stockée **une fois par produit**, en copie indépendante. Aujourd'hui : 345 fiches, 345 copies, dont 46 distinctes.

### 3.2 Gestion par Valérie : aujourd'hui et cible visée

| | Aujourd'hui | Cible |
|---|---|---|
| Ajouter une matière | Une image par calque de chaque modèle, saisie une par une dans l'éditeur du plugin, facturée par VIMAWEB | Déclarée une fois dans un écran « Matières » (patch, nom, famille, ordre, actif) |
| Retirer ou désactiver une matière | Passe par VIMAWEB (outil de purge) | Un geste, répercuté partout |
| Ajouter un modèle (≈ 1 semaine) | Calques importés, puis chaque matière ajoutée à la main sur chaque calque | Calques déposés en lot, type par calque, matières rattachées seules (par nom de fichier), aperçu, publication |
| Retrouver un fichier | Médiathèque WordPress, dossiers et catégories mal rangés | Nom de fichier normalisé `Selle-{Marque}-{Modèle}-{zone}_{NN}_{Matière}.png`. Le rattachement se fait par le nom : le rangement dans la médiathèque ne conditionne plus rien. |
| Photos et Photoshop | Manuel chez elle | Inchangé |

### 3.3 Flux de production d'une fiche

| Étape | Qui / où | État de nos connaissances |
|---|---|---|
| Photos de patch (échantillon physique) | Photographiées par ARTEO ou VIMAWEB, ajoutées à la médiathèque (JPG 750 × 750, dossier `2022/05`) | **Confirmé par Valérie (15/10).** |
| Photos de la selle sous plusieurs angles | Valérie, chez elle | Compte rendu du 07/10. |
| Découpe des calques (zones) | Valérie (chez elle), Photoshop | Compte rendu du 07/10. **Outil confirmé par les fichiers** : 12 400 PNG sur 12 931 portent la signature Adobe Photoshop pour Windows (version « CC » de 2022-2023, puis « 25.1 » pour les fiches de 12/2024 à 02/2025, soit deux installations). Les patchs ont été retouchés dans Photoshop CC le 12/05/2022. Gabarit ou action : inconnus. |
| Image « matière sur zone » | Patch collé au calque | **Recette retrouvée depuis** (texture maître découpée par le masque de la zone, [[phase-1]] §5.3). Constat initial : Observation sur les images (Z900, une zone) : la texture du patch est reprise à plus petite échelle, sans déformation de perspective visible, découpée par le masque de la zone. L'éclairage est dans un calque séparé « Ombres et éclairage ». **Lecture des métadonnées** : 10 823 PNG sur 12 931 (84 %) descendent d'un **même document Photoshop source**. Signal d'une production à partir d'un gabarit unique, à confirmer. Les 3 autres documents sources (460 à 874 fichiers) semblent correspondre à des jeux du simulateur de broderie : noms `r6-assise-…`, `f900xr-assise-…` et `assises-…` (à rapprocher du dossier `images-nid-abeille`). |
| Import dans WordPress, puis ajout des choix | Valérie, éditeur du plugin dans la fiche produit | L'éditeur propose : ajouter un choix par son nom, choisir l'image par angle dans la médiathèque, **copier / coller** des choix entre calques, regrouper des choix, réordonner, import / export par produit. Sa pratique exacte est inconnue. |

### 3.4 Appel du 16/10 : ce que Valérie a dit

*Notes de Melvin, appel téléphonique ; certains points sont donnés « probablement » ou « je ne suis pas sûr ».*
- Les images de matières sont faites à partir de **petites images (vignettes) répétées** pour « patcher » les calques. Pas de textures maîtres photographiées au départ. C'est **Samuel**, le premier développeur, qui l'a fait il y a environ **13 ans**, pour quasiment toutes les matières.
- Il n'y a **pas eu de nouvelle matière depuis plusieurs années** (à confirmer). Une matière « ajoutée en 2025 » n'a pas été photographiée en 2025 : les dates relevées dans les fichiers sont des dates de téléversement, pas de prise de vue. Pourquoi certaines matières existent en 750 px et d'autres en 171 px reste inexpliqué.
- **Pas de PSD, seulement des PNG.**
- **Ajouter une selle** : Produits → Démarrer le configurateur → Contenu, puis ajout des images **une à une**, par calque et par matière, pour chaque selle.
- Elle **crée les calques dans Photoshop**, ce qui lui prend beaucoup de temps. Elle a **de nombreuses nouvelles selles** qu'elle ne peut pas ajouter : ce ne sont pas des modèles duplicables, il faudrait refaire tous les calques.
- Une fois les calques faits, elle doit **payer VIMAWEB pour « faire entrer » la selle**, parce que VIMAWEB crée les matières. Ce point n'est pas compris : à clarifier (voir ci-dessous).
- Demande : **automatiser la création des calques**.

### 3.5 Questions posées à Valérie et réponses

**Reste à demander à Valérie**
- Ce que VIMAWEB facture exactement et pourquoi.
- Combien de nouvelles selles en attente, et photos de ces selles disponibles (cadrage identique aux selles actuelles ?).
- Où sont les vignettes d'origine de Samuel, et pourquoi 750 px pour certaines matières et 171 px pour d'autres.

**Précisions reçues après l'appel (16/10)**
- **VIMAWEB** : Valérie le paie à chaque nouvelle selle, mais on ne sait pas ce qu'il fait derrière. Ce qui est sûr : **c'est elle qui découpe les calques et ajoute les patchs un à un**. Précisé ensuite dans le même appel : voir « Rôle de VIMAWEB » plus bas (l'hypothèse sur le plugin `Sync MKL…` n'est pas retenue).
- **Selles en attente** : plusieurs. Elles sont prises **globalement sous le même angle et à la même distance, mais pas au centimètre près**. Conséquences : les masques d'une nouvelle selle ne sont pas réutilisables d'un modèle à l'autre (segmentation à refaire pour chaque selle) ; l'échelle de la texture par rapport à la selle varie légèrement d'une photo à l'autre (de quelques pour cent, à mesurer sur les modèles existants avant de décider d'un réglage d'échelle).
- **Vignettes d'origine de Samuel** : a priori sur l'ancien hébergement **OVH** (69 Go non inventoriés). L'inventaire de ces 69 Go est le moyen de retrouver les sources et d'expliquer 750 px contre 171 px ; il demande l'accès à l'hébergement (hors périmètre tant que Melvin ne l'a pas décidé).

### 3.6 Rôle de VIMAWEB

*Précisé par Melvin après l'appel (16/10), rapporté de mémoire, à confirmer avec Valérie.*
- Il y a **deux opérations distinctes**, faites par deux personnes :
  1. **VIMAWEB (payé à chaque nouvelle selle)** : Valérie lui remet le **calque** (la forme de la zone) ; il y applique les **couleurs et matières** et fournit les images « matière X sur zone Y ». C'est la fabrication des images de zones.
  2. **Valérie** : dans Produits → Démarrer le configurateur → Contenu, elle ajoute **une par une** les matières, et associe à chaque choix l'image de zone (« photo du calque ») et la vignette de la matière. C'est ce qui relie la matière au calque.
- Cela correspond aux données : chaque choix du configurateur porte deux images distinctes, l'**image de zone** (1920 × 1280, fabriquée) et la **vignette** (le petit carré cliquable, fourni par Valérie).
- **Conséquence** : l'opération 1, celle que paie Valérie à VIMAWEB, est exactement ce que le poste 3 reproduit par calcul (texture + masque) et que l'écran de gestion automatise ; l'opération 2 est la saisie image par image que les configurateurs globaux 2.0 et la génération par lots suppriment. Reste à la charge de Valérie la **découpe des calques** (masques de zones), que l'essai SAM ne remplace pas encore.
- Non établi : comment VIMAWEB applique les couleurs (outil, script Photoshop, travail manuel), à quel prix et avec quelle qualité par rapport à notre génération.
- **Précisions de Melvin (16/10)** : VIMAWEB applique les couleurs **par du code** (traitement automatique, pas de travail manuel). Valérie paie **60 € par selle** ; Melvin juge ce montant sans importance pour le chiffrage. Cela rejoint la mesure de [[phase-1]] §5.10 : une texture répétée d'une cellule exacte est la signature d'un traitement par programme ; le prototype de gestion refait la même opération. Le code de VIMAWEB (hérité de Samuel ?) pourrait donner la recette exacte (cellule, répétition, couleur), mais le demander à VIMAWEB n'est pas dans le périmètre sans décision de Melvin.

## 4. Le site existant

| Sujet | Valeur |
|---|---|
| Pile | WordPress, WooCommerce 11.1.0, Divi, LiteSpeed |
| Configurateur | `mkl_pc` (Product Configurator for WooCommerce) 1.7.5, images en couches PNG |
| Options de commande | `wapf` (Advanced Product Fields Extended) 3.2.1, système distinct |
| Paiement / livraison | Alma, Cofidis, DPD. Payline/Monext non détecté |
| Prix | Woo Discount Rules |
| Plugin sur mesure | `sc-notice-carbone` (auteur à confirmer) |
| Catalogue | 1 520 produits, **345 configurables**, 27 marques, 448 catégories modèle |
| Images | 220 à 294 par selle, **≈ 83 000 images** (estimation). L'extrapolation « ≈ 35 Go » est **fausse** : les uploads réels font **15,06 Go** au total (voir §4.1). Nombre de fichiers uniques à recompter sur le clone |
| Jeux de matières | **3 jeux réutilisables : 37 matières, 26 surpiqûres, 44 liserés** ; 337 fiches sur la même logique, 8 atypiques dont CFMOTO 800 NK |
| Données incohérentes | Faute « gris tonnerrre » copiée dans 57 couches ; noms de couche copiés d'autres modèles ; 5 gabarits de noms |

### Hypothèse technique à trancher (réponse : [[phase-1]] §3.1 et §3.9)
Le plugin `mkl_pc` n'a sans doute pas de notion de famille ni de jeu partagé. Quatre pistes, de la plus légère à la plus lourde : étendre via API/hooks ; couche à côté qui génère les données attendues ; forker le plugin ; configurateur maison branché sur WooCommerce. **Tout se refait en restant sur WordPress** : WordPress n'est pas le facteur limitant, c'est le plugin et la façon dont il est monté.

### 4.1 Site Health prod et dev, rapport système WooCommerce (14/10, lecture seule)

Textes bruts : `sellerieconfort-refonte/site-health-prod-2026-10-14.txt` et `site-health-dev-2026-10-14.txt` (repo `sellerie-confort`).

#### Production

| Sujet | Valeur |
|---|---|
| WordPress / WooCommerce / Divi | 7.1.3 / 11.2.1 / 4.27.8 (dernière 4.27.9) |
| Configurateur | **Product Configurator 1.7.6** (dernière : **2.0.0**, version majeure non installée) |
| Options de commande | Advanced Product Fields **Extended** 3.2.1 (`wapf`). La version Pro 2.7.5 est inactive |
| Paiement / livraison | **Alma 6.7.0**, **Payline 1.4.8** (Monext, présent), Cofidis, DPD, + Woo Payline Caution (Vimaweb) |
| Serveur | PHP **8.3.35**, MariaDB 11.4.13, mémoire 2 Go, upload 512 Mo, `time_limit` 600 s, Imagick 7.1 |
| Cache | LiteSpeed Cache 7.9.1 (seul), drop-in `advanced-cache.php` |
| Données | **2 890 utilisateurs**, **2 241 entrées de formulaire** : données personnelles à exclure du clone |
| Tailles | Total **17,87 Go** : uploads **15,06 Go**, base **1,47 Go**, plugins 299 Mo, thème 61 Mo |
| Mises à jour | Auto désactivées sur presque tout (sauf WPForms). Rien de très en retard, sauf le configurateur (2.0.0 disponible) |
| Plugins sur mesure | `SC Notice Carbone` (en-tête : « Sellerie Confort »), `Notes de commande`, `SC - Export PDF Factures`, `Woo Payline Caution` (Vimaweb), `Purge + Tag « Configurable »` 1.2.0 (auteur « Vous ») |
| mu-plugins | `Active Plugins` (ARTEO Digital), `fix-wapf-preview.php` (auteur inconnu), WP Umbrella |

#### Dev : ce qui le distingue

| Sujet | Valeur |
|---|---|
| Nature | Préproduction créée avec **WP Tiger** (o2switch), dossier `myTiger-Preprod`, compte cPanel nommé `sellerieconfort` |
| Retard | Configurateur 1.5.13 (prod 1.7.6), WooCommerce 10.5.2 (prod 11.2.1), WordPress 6.9.1 (prod 7.1.3), 1 071 utilisateurs (prod 2 890) |
| Plugins absents de la prod | **`SC - Sync MKL Product Configurator (templates par tag modèle)`** (Vimaweb, 1.0.1), **Zakeke Interactive Product Designer** 4.2.0, TranslatePress, ACF Pro (non activé), Autoptimize, WP File Manager |
| WP_DEBUG | `true` avec journal actif (sur dev seulement) |

#### À retenir

1. **Dev est écarté comme source de clone** : données personnelles présentes (art. 2) et trop ancien. Source retenue : la production, avec filtre de tables.
2. **Le clone est léger** : 17,87 Go dont 15,06 Go d'uploads. Mon estimation « 25 à 35 Go » de médias du configurateur était **trop haute** (≈ 83 000 images × 350 Ko). Soit les fichiers sont plus petits, soit **partagés entre fiches** (produits dupliqués qui pointent vers les mêmes médias). À mesurer sur le clone, en comptant les fichiers uniques.
3. **VIMAWEB a déjà prototypé sur dev un plugin « templates par tag modèle » pour le configurateur.** Il n'est pas en production. C'est exactement le terrain de l'étape 2 (regroupement) : **à lire avant tout chiffrage**, et à aborder avec tact (ils ont déjà essayé quelque chose, ce qui contredit l'idée d'un refus pur et simple d'améliorer l'existant).
4. **Zakeke** (personnalisation produit : logos, texte) est installé sur dev, pas en prod : à vérifier si c'est un essai pour les logos sur la selle, et s'il y a un abonnement en cours. Recoupe notre volet broderies.
5. **Product Configurator 2.0.0** existe : lire le changelog avant de conclure sur les limites de `mkl_pc` (la 2.0 peut changer la donne sur les jeux partagés).
6. **Payline est bien en production** (le rapport d'audit avait raison), à côté d'Alma et Cofidis. `Woo Payline Caution` porte la caution de l'échange standard.
7. **Serveur confortable** pour la suite : PHP 8.3, 2 Go de mémoire, Imagick disponible, `time_limit` 600 s. Export/import et traitement d'images côté serveur sont envisageables.
8. **Point bloquant pour l'export** : savoir où sont stockées les **commandes** (HPOS ou anciennes tables `wp_posts`). Avec le stockage historique, un filtre par table ne suffit pas à les exclure. À lire dans WooCommerce → Réglages → Avancé → Fonctionnalités → « Stockage des données de commande ». **Relevé du 14/10 sur dev** : stockage **hérité** (`wp_posts`), HPOS non activé, bloqué par deux extensions déclarées incompatibles (Custom Order Statuses for WooCommerce, Shipping Method Description), avec des commandes non synchronisées. **Prod relevée le 14/10 : stockage hérité aussi** (`wp_posts`), HPOS bloqué par une seule extension incompatible (Shipping Method Description for WooCommerce), commandes non synchronisées. **Conséquence : un filtre par table ne suffit pas à exclure les commandes.** Les données personnelles se trouvent aussi dans les fichiers (factures PDF, dossiers `woocommerce_uploads`, `wpforms`, logs). Méthode d'export à choisir en conséquence, avec un contrôle final (recherche de `_billing_`, `_shipping_` dans l'export). Options : export WordPress natif (produits et médias seulement, rien à installer sur la prod) ou WP Migrate avec exclusion de types de contenu (peut-être une fonction payante, à vérifier à l'écran).

#### Rapport système WooCommerce de la prod (2 exports dans `Phase 1/`)

Deux fichiers `SystemStatusReport_sellerieconfort.com_…` : identiques sauf les compteurs d'Action Scheduler (le second est le plus récent).

| Constat | Valeur | Ce que ça change |
|---|---|---|
| **Préfixe de tables** | **`SC_`** (pas `wp_`) | À utiliser dans tout filtre ou toute requête |
| **Où est la config du configurateur** | Aucune table `mkl_` : elle est dans **`SC_postmeta`** (**1 101 Mo** sur 1 363 Mo de base, soit 81 %) | Impossible d'exclure `postmeta` pour éviter les commandes : elle contient aussi ce qu'on veut garder. Confirme qu'il faut filtrer par type de contenu |
| **Commandes** | **5 437** `shop_order` + 51 remboursements dans `SC_posts` ; `wc_orders*` quasi vides ; HPOS désactivé, synchro désactivée | Les commandes et leurs métadonnées sont dans les mêmes tables que les produits |
| **Produits** | 1 595 produits, 42 variations, 38 groupes `wapf_product` | |
| **Médiathèque** | **15 185 pièces jointes** au total | Contredit l'estimation de ≈ 83 000 images : ce chiffre compte des **références**, pas des fichiers. Fichiers uniques ≤ 15 185. À rapprocher des 15,06 Go d'uploads |
| **Autres contenus** | 2 609 révisions, 1 311 entrées `seopress_404` | Bruit à ne pas exporter |
| **Restes d'anciens plugins** | Tables `bwg_*` (Photo Gallery), `ngg_*` (NextGEN), `yoast_*`, `berocket_*`, `mainwp_wpvivid_*` | Plusieurs générations de site se sont empilées |
| **Surcharge de modèle obsolète** | `Divi Child/woocommerce/checkout/payment.php` en version **9.8.0** contre 10.9.0 | Risque sur le tunnel de paiement. Piste pour le panier perdu |
| **Tâches planifiées en échec** | **447** échouées (de 07/08 à 12/10), 7 335 terminées | À identifier : quel hook, quel plugin |
| **Cron WordPress** | « – » | Possiblement désactivé côté WordPress (cron serveur ?), à vérifier |
| **Cache objet externe** | Aucun | |
| **Journal WooCommerce** | 30 jours, 11 Mo | |

### 4.2 Front existant (captures publiques)
Captures publiques, bureau (1440) et mobile (390), pages entières : `Phase 1/reference-front/{desktop,mobile}/` (12 pages, + fiche produit avec configurateur ouvert). Script : `scripts/capture_reference.mjs`. Aucun clone nécessaire : c'est le public.

| Constat sur la fiche produit actuelle | |
|---|---|
| Structure | Fiche Divi : étiquette « Configurable », photo, prix (barré 250 € → **210 € TTC**), bloc Cofidis 3x/4x, puis formulaire APF **sous** le configurateur |
| Le configurateur | **Plein écran séparé** (liste des 6 couches à gauche, selle à droite, « Valider la configuration », « Reset ») : ce n'est donc pas « tout sur une page » |
| Parasites à l'ouverture | Fenêtre « Information importante » (Carbone) + bannière cookies |
| Prix | Le public renvoie 250 € (prix de base) ; le 210 € vient de **Discount Rules** : le local affiche 250 € |
| Page oubliée en ligne | `xx__ma-moto-php-shortcode__archive-backup` (page d'archive de code, publiée) |

### 4.3 Options de commande (APF) existantes
Détail : `Phase 1/reconstruction/options-apf-echantillon.json`. Script : `scripts/inventory_options.py`.

| Groupe | Champs | Fiches |
|---|---|---|
| **Communs** (groupes `59570`, `4659`) | Modèle de ma moto*, Année*, Taille pilote*, Poids pilote*, Poids passager, Commentaires, **Type de commande*** (2 choix), **Hauteur d'assise pilote*** (3), **Option gel** (4), Options de selle, Informations complémentaires, **Broderies*** (oui/non) | 4 sur 4 (12 champs) |
| **Par modèle** (groupes `858`, `1132`, `p_<id>`) | Broderie dosseret*, Motif de broderie (3), **Couleurs de broderie (26)**, Motif bandes / dosseret, Précisions couleurs, Autres couleurs | 1 à 2 sur 4, conditionnels |

Surcoûts relevés : hauteur ±2 cm **+10 €**, gel avant / arrière **+35 €**, deux assises **+70 €**. 12 à 17 champs par fiche, **règles conditionnelles** (la broderie ouvre le motif, qui ouvre les couleurs). Sur 38 groupes au total, un socle commun et des groupes propres à chaque modèle.

## 5. Hébergement et accès

| Élément | Où | Titulaire |
|---|---|---|
| Domaines `sellerieconfort.com` / `.fr` / `sellerie-confort.com` | OVH | Valérie |
| Zone DNS | OVH | Valérie |
| **Site en vente** | **o2switch** (`109.234.165.168`) | **VIMAWEB** (confirmé par Valérie) |
| `dev.sellerieconfort.com` | o2switch (`109.234.165.38`) | Probablement VIMAWEB, à confirmer |
| Ancien hébergement (créé 17/06/2013, 69 Go, PHP 7.2) | OVH | Valérie |
| Hébergement performance « sellerz » | OVH | Valérie, rôle inconnu |
| Boîtes mail (`mail.`, `smtp.`) | OVH | Valérie |
| Réception mail (MX) | Google Workspace | À confirmer |
| Licences des plugins | — | **VIMAWEB** |

- `dev` = copie WordPress de la boutique, `noindex`, **sans mot de passe**, contenu figé vers **juin 2026** (pages de mars 2025), fichiers régénérés les 5 et 17/09 : quelqu'un y a travaillé
- L'ancien hébergement OVH sert encore l'ancien site (Sam-Web, PHP 7.2) quand on l'interroge directement ; `dev2022` = WordPress « Site en construction »
- **Accès obtenus** : compte nominatif sur la **prod** et sur **dev**. Accès OVH : hors contrat, inutile en Phase 1. **o2switch : non fourni, non nécessaire en Phase 1**

## 6. Décisions et points ouverts

| Sujet | État |
|---|---|
| Source du clone | **Production avec filtre de tables**, accord écrit de Valérie. Dev écarté : 1 071 utilisateurs et 151 entrées de formulaire (données personnelles, art. 2) et versions plus anciennes |
| Accord écrit pour le plugin d'export | **Obtenu par mail de Valérie** : installation temporaire de l'extension nécessaire à la copie technique, « conformément au contrat ». **Conditions** : aucune donnée personnelle ni commande exportée ; extension désinstallée dès l'export terminé. **Non utilisé à ce jour** (le public suffit, voir [[phase-1]] §4.2) : en réserve |
| Date de départ du délai (10 j) | **14/10/2026** (précisé par Melvin) : fin du délai le **24/10/2026**. À tracer par mail à Valérie |
| Information de VIMAWEB | **Faite** (précisé par Melvin le 14/10). Pas de contact direct de notre part. Risques qui restent : licences, mise en production, réaction |
| Temps de reconnaissance | À consigner : il consomme le délai calendaire, à décider s'il compte dans les 4 jours |
| Stratégie tarifaire Phase 2 | Interne uniquement, voir [[2026-10-07-sellerie-confort-cr-interne]] |
| Cible Phase 2 | Calendrier et chiffrage seulement après audit |

## 7. Échéances

| Date | Quoi |
|---|---|
| **17/10/2026** | Départ en congés de Valérie : accord écrit et accès avant |
| **24/10/2026** | Fin du délai de 10 jours (départ le 14/10) |
| **Début novembre** | Rencontre du client avec une agence web |
| **Avril 2027** | Renouvellement du plan OVH |
| **17/06/2027** | Expiration du domaine |

## 8. Constats hors périmètre, à porter au rapport

- PHP 7.2 sur un hébergement OVH actif, avec l'ancien site (compte, panier) joignable directement
- 69 Go non inventoriés sur un plan de 2013 : sources d'origine, WordPress 2022, sauvegardes ?
- Deux offres OVH actives, dont une dédiée ; **boîtes mail sur ce plan** : ne pas résilier sans migration
- `dev` public sans mot de passe, copie ancienne de la boutique
- Domaines secondaires : redirections et SEO à auditer
- **ALERTE SÉCURITÉ (constatée et confirmée le 14/10 vers 16h29)** : l'admin de la prod affiche l'avertissement officiel « Important Notice from the WordPress.org Plugins Team » : plusieurs plugins de l'auteur « essentialplugin » ont téléchargé du code depuis `analytics.essentialplugin.com` et installé une porte dérobée dans un fichier `wp-comments-posts.php`, utilisée pour injecter du code dans `wp-config.php` (liens spam cachés, redirections, pages injectées, SEO « black-hat »). La mise à jour forcée « ne peut pas confirmer » l'élimination complète. Plugin concerné ici : **WP Logo Showcase Responsive Slider and Carousel** (éditeur *Essential Plugin*), compromis après rachat (activée le 05/04/2026). Ce plugin est **actif sur la prod en 3.8.7.1** (version de mise à jour forcée, qui ne nettoie pas le reste) et sur dev en **3.8.7** (non mise à jour). La compromission n'est **pas établie** : il faut inspecter les fichiers. Contrôle passif fait : page d'accueil et page matières identiques pour un visiteur et pour un robot Googlebot (pas de camouflage visible, non concluant).
  - À faire par le titulaire de l'hébergement (VIMAWEB) : chercher `wp-comments-posts.php` à la racine, vérifier `wp-config.php`, la liste des administrateurs, les pages inconnues, supprimer le plugin, changer les mots de passe (admin, base, FTP/cPanel) et les clés de sécurité, restaurer au besoin depuis une sauvegarde saine.
  - **Décision de Melvin (14/10)** : sujet **hors périmètre** (hébergement et maintenance, art. 2 ; c'est le sujet de VIMAWEB). **Pas de prise de contact avec VIMAWEB**, rien n'est touché tant que ça ne gêne pas la mission.
  - Garde-fous qui restent : ne rien supprimer ni modifier sur la prod (art. 2 et 7), **ne cloner ni les fichiers ni les plugins** de la prod, ne pas exécuter ce plugin en local.
  - Redevient un sujet de mission si : un compte administrateur inconnu apparaît (le compte nominatif est concerné), un export ou un test est perturbé par du contenu injecté, le site est signalé par un moteur de recherche ou un navigateur, ou un résultat de l'audit en dépend (performance, panier perdu). À signaler à ce moment-là.
  - Constat à reporter dans le rapport comme **point de sécurité observé**, sans investigation de notre part.
