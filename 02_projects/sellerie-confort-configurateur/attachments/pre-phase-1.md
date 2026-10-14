---
tags: [sellerie-confort, pre-phase-1]
created: 2026-10-14
client: sellerie-confort
projet: sellerie-confort-configurateur
---

# Pré-phase 1 : reconnaissance

Ce qu'on sait **avant** de toucher au clone et aux tests de la Phase 1. Reconnaissance menée le 14/10/2026 à partir de lectures publiques, du contrat signé et de la console OVH. Rien n'a été modifié, ni chez OVH ni chez o2switch, ni sur le site.

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

## 3. Le besoin, en bref

- Ajouter ou retirer une **matière** aujourd'hui : un fichier par zone, par matière et par modèle, saisis un par un, et c'est **VIMAWEB qui facture chaque demande**. Nouvelles matières en stock bloquées depuis longtemps
- **Nid d'abeille** = une broderie, seulement sur quelques modèles tout préparés ; ils veulent l'ajouter au configurateur
- Ajout d'un modèle ≈ **1 semaine**. Photos et Photoshop restent manuels (ça marche bien) ; on automatise l'ajout des matières sur chaque calque et le classement par famille
- Principe d'ergonomie : tout sur **une seule page**
- Priorité broderies : basse pour Valérie, haute pour moi (vrai plus du configurateur)

## 4. Ce qu'on sait du site (lecture publique)

| Sujet | Valeur |
|---|---|
| Pile | WordPress, WooCommerce 11.1.0, Divi, LiteSpeed |
| Configurateur | `mkl_pc` (Product Configurator for WooCommerce) 1.7.5, images en couches PNG |
| Options de commande | `wapf` (Advanced Product Fields Extended) 3.2.1, système distinct |
| Paiement / livraison | Alma, Cofidis, DPD. Payline/Monext non détecté |
| Prix | Woo Discount Rules |
| Plugin sur mesure | `sc-notice-carbone` (auteur à confirmer) |
| Catalogue | 1 520 produits, **345 configurables**, 27 marques, 448 catégories modèle |
| Images | 220 à 294 par selle, **≈ 83 000 images** (estimation). L'extrapolation « ≈ 35 Go » est **fausse** : les uploads réels font **15,06 Go** au total (voir §9). Nombre de fichiers uniques à recompter sur le clone |
| Jeux de matières | **3 jeux réutilisables : 37 matières, 26 surpiqûres, 44 liserés** ; 337 fiches sur la même logique, 8 atypiques dont CFMOTO 800 NK |
| Données incohérentes | Faute « gris tonnerrre » copiée dans 57 couches ; noms de couche copiés d'autres modèles ; 5 gabarits de noms |

### Hypothèse technique à trancher
Le plugin `mkl_pc` n'a sans doute pas de notion de famille ni de jeu partagé. Quatre pistes, de la plus légère à la plus lourde : étendre via API/hooks ; couche à côté qui génère les données attendues ; forker le plugin ; configurateur maison branché sur WooCommerce. **Tout se refait en restant sur WordPress** : WordPress n'est pas le facteur limitant, c'est le plugin et la façon dont il est monté.

## 5. Hébergement et accès (reconnaissance du 14/10)

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
| Accord écrit pour le plugin d'export | **À obtenir avant le 17/10** |
| Date de départ du délai (10 j) | À confirmer par mail |
| Information de VIMAWEB | Valérie d'accord, pas encore faite. Risque : licences, mise en production, hostilité |
| Temps de reconnaissance | À consigner : il consomme le délai calendaire, à décider s'il compte dans les 4 jours |
| Stratégie tarifaire Phase 2 | Interne uniquement, voir [[2026-10-07-sellerie-confort-cr-interne]] |
| Cible Phase 2 | Calendrier et chiffrage seulement après audit |

## 7. Échéances

| Date | Quoi |
|---|---|
| **17/10/2026** | Départ en congés de Valérie : accord écrit et accès avant |
| **~23-24/10/2026** | Fin du délai de 10 jours (à confirmer) |
| **Début novembre** | Rencontre du client avec une agence web |
| **Avril 2027** | Renouvellement du plan OVH |
| **17/06/2027** | Expiration du domaine |

## 8. Constats à porter au rapport (sans y toucher en Phase 1)

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

## 9. Site Health prod et dev (relevés du 14/10, lecture seule)

Textes bruts : `sellerieconfort-refonte/site-health-prod-2026-10-14.txt` et `site-health-dev-2026-10-14.txt` (repo `sellerie-confort`).

### Production : ce que ça donne

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

### Dev : ce qui le distingue

| Sujet | Valeur |
|---|---|
| Nature | Préproduction créée avec **WP Tiger** (o2switch), dossier `myTiger-Preprod`, compte cPanel nommé `sellerieconfort` |
| Retard | Configurateur 1.5.13 (prod 1.7.6), WooCommerce 10.5.2 (prod 11.2.1), WordPress 6.9.1 (prod 7.1.3), 1 071 utilisateurs (prod 2 890) |
| Plugins absents de la prod | **`SC - Sync MKL Product Configurator (templates par tag modèle)`** (Vimaweb, 1.0.1), **Zakeke Interactive Product Designer** 4.2.0, TranslatePress, ACF Pro (non activé), Autoptimize, WP File Manager |
| WP_DEBUG | `true` avec journal actif (sur dev seulement) |

### À retenir

1. **Dev est écarté comme source de clone** : données personnelles présentes (art. 2) et trop ancien. Source retenue : la production, avec filtre de tables.
2. **Le clone est léger** : 17,87 Go dont 15,06 Go d'uploads. Mon estimation « 25 à 35 Go » de médias du configurateur était **trop haute** (≈ 83 000 images × 350 Ko). Soit les fichiers sont plus petits, soit **partagés entre fiches** (produits dupliqués qui pointent vers les mêmes médias). À mesurer sur le clone, en comptant les fichiers uniques.
3. **VIMAWEB a déjà prototypé sur dev un plugin « templates par tag modèle » pour le configurateur.** Il n'est pas en production. C'est exactement le terrain de l'étape 2 (regroupement) : **à lire avant tout chiffrage**, et à aborder avec tact (ils ont déjà essayé quelque chose, ce qui contredit l'idée d'un refus pur et simple d'améliorer l'existant).
4. **Zakeke** (personnalisation produit : logos, texte) est installé sur dev, pas en prod : à vérifier si c'est un essai pour les logos sur la selle, et s'il y a un abonnement en cours. Recoupe notre volet broderies.
5. **Product Configurator 2.0.0** existe : lire le changelog avant de conclure sur les limites de `mkl_pc` (la 2.0 peut changer la donne sur les jeux partagés).
6. **Payline est bien en production** (le rapport d'audit avait raison), à côté d'Alma et Cofidis. `Woo Payline Caution` porte la caution de l'échange standard.
7. **Serveur confortable** pour la suite : PHP 8.3, 2 Go de mémoire, Imagick disponible, `time_limit` 600 s. Export/import et traitement d'images côté serveur sont envisageables.
8. **Point bloquant pour l'export** : savoir où sont stockées les **commandes** (HPOS ou anciennes tables `wp_posts`). Avec le stockage historique, un filtre par table ne suffit pas à les exclure. À lire dans WooCommerce → Réglages → Avancé → Fonctionnalités → « Stockage des données de commande ». **Relevé du 14/10 sur dev** : stockage **hérité** (`wp_posts`), HPOS non activé, bloqué par deux extensions déclarées incompatibles (Custom Order Statuses for WooCommerce, Shipping Method Description), avec des commandes non synchronisées. **Prod relevée le 14/10 : stockage hérité aussi** (`wp_posts`), HPOS bloqué par une seule extension incompatible (Shipping Method Description for WooCommerce), commandes non synchronisées. **Conséquence : un filtre par table ne suffit pas à exclure les commandes.** Les données personnelles se trouvent aussi dans les fichiers (factures PDF, dossiers `woocommerce_uploads`, `wpforms`, logs). Méthode d'export à choisir en conséquence, avec un contrôle final (recherche de `_billing_`, `_shipping_` dans l'export). Options : export WordPress natif (produits et médias seulement, rien à installer sur la prod) ou WP Migrate avec exclusion de types de contenu (peut-être une fonction payante, à vérifier à l'écran).

### Rapport système WooCommerce de la prod (14/10, 2 exports dans `Phase 1/`)

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

#### Tables à exclure d'un export (préfixe `SC_`)
`users`, `usermeta` (garder la structure, créer un admin local), `comments`, `commentmeta`, `woocommerce_order_items`, `woocommerce_order_itemmeta`, `woocommerce_sessions`, `woocommerce_payment_tokens*`, `wc_orders*`, `wc_order_*`, `wc_customer_lookup`, `wcpdf_*`, `wpforms_entries*`, `wpforms_payment*`, `wc_cofidispayment_*`, `alma_business_data`, `cleantalk_*`, `pimwick_gift_card*`, `wdr_order_*` ; **et** les articles de type `shop_order` et `shop_order_refund` avec leurs `postmeta`.

### Lecture du code de `mkl_pc` 1.7.6 (14/10, plugin lu sans être exécuté)

Version lue : **1.7.6**, celle de la prod (la 2.0.0 reste à lire). Fichiers clés : `inc/db.php`, `inc/cache.php`.

| Sujet | Ce que fait le plugin |
|---|---|
| **Stockage** | Par produit, en méta WooCommerce : `_mkl_product_configurator_layers`, `_angles`, `_content`, `_last_updated`, plus `_mkl_pc__is_configurable` et `_mkl_pc__variable_configuration_mode`. Tableaux PHP sérialisés dans `SC_postmeta` |
| **Forme du contenu** | Liste de couches ; chaque couche a des `choices[]` ; chaque choix a des `images[]` avec `image {id, url}` et `thumbnail {id, url}`. L'URL est stockée **dans** la donnée, avec l'ID de la pièce jointe |
| **Fichier JS public** | Simple **cache généré** de ces données (`PC.productData.prod_{ID}`), régénéré à la demande si 404, à la sauvegarde des réglages WooCommerce et à chaque purge totale de LiteSpeed (d'où les dates vers 4 h) |
| **Partage entre produits** | **Aucune notion de jeu, de famille ou de bibliothèque partagée.** Seul partage natif : mode `share_layers_config` des produits variables (couches communes, choix par variation) |
| **Rattachement par nom de fichier** | Le plugin contient déjà une résolution d'image par **nom de fichier** (`scan_product_images`, `_find_image_id`), utilisée après une migration |
| **Import/Export** | Section native par produit |
| **Sauvegarde** | La migration (`update.php`) ajoute une méta `_mkl_product_configurator_content__backup` : peut expliquer une partie du 1,1 Go de `postmeta`, à vérifier |

#### Points d'extension (sans toucher au cœur du plugin)

| Crochet | Usage possible |
|---|---|
| Filtre **`mkl_pc/db/get`** | Lecture : reconstruire `content` à la volée à partir d'un jeu de matières partagé |
| Filtre `mkl_product_configurator_content_data` | Idem, au niveau du contenu |
| Filtre `mkl_product_configurator/data/set/{component}` et `.../set/choice` | Écriture : normaliser ou compléter avant enregistrement |
| Actions `mkl_pc_before_save_product_configuration`, `mkl_pc_saved_product_configuration` | Déclencher une synchronisation après sauvegarde |
| Filtre `mkl_pc_get_configurator_data` | Modifier ce qui part dans le fichier JS |
| Filtre `mkl_pc_db_fields` | Ajouter des champs (famille, groupe) |
| Filtre `mkl_product_configurator_admin_menu` | Ajouter un onglet dans l'éditeur du configurateur |
| Méthode `DB::update_choice()` | Mise à jour programmatique d'un choix |

#### Conclusion technique provisoire

- **L'option 1 (étendre via crochets) est viable** pour l'étape 2 : un petit plugin peut lire un jeu partagé (37, 26, 44 matières) et composer le contenu de chaque produit, sans forker.
- **Nuance importante** : un jeu partagé peut partager les **noms, ordres, prix, vignettes**, mais l'**image d'une matière sur une couche d'un modèle reste propre à ce modèle** (c'est la découpe). La partie lourde reste donc l'étape 1 (produire ces images), pas l'étape 2.
- **Piste à tester** : rattacher les images **par convention de nom** (`{modèle}-{zone}-{matière}`), comme le plugin sait déjà le faire. Ça remplacerait la saisie manuelle une par une.
- **À vérifier** : le poids réel de `postmeta` (sauvegardes ?) et le mode réellement utilisé par les produits Sellerie Confort. (La 2.0.0 est lue : voir ci-dessous.)

### Changelog de `mkl_pc` 2.0.0 (publiée le 12/10/2026, il y a 2 jours)

Sources : `readme.txt` du dépôt officiel (trunk), page du plugin sur WordPress.org. Prérequis : WordPress 6.0+, PHP 7.4+, testé jusqu'à 7.1. La prod (WP 7.1.3, PHP 8.3) est compatible.

| Nouveauté | Contenu | Pertinence |
|---|---|---|
| **Configurateurs globaux** | Une configuration commune, rangée dans « Product Configurator > Global configurators », **assignable par produit ou par catégorie** (sous-catégories incluses). « Make local copy » détache un produit | **Forte** : c'est la notion de jeu partagé qui manquait |
| **Couches globales** | Toute couche peut devenir globale (« Make Global ») et être importée dans d'autres produits ; « Edit original » propage ; « Disconnect » rend une copie locale | **Forte**, même remarque |
| **Méta de configuration par couche** | Réglage « Configuration meta data » : une méta par couche, au lieu d'une méta unique | Utile pour exports, factures, ERP |
| **Commandes** | Une commande affiche l'**image et les noms enregistrés à l'achat**, plus ceux de la configuration actuelle | **Protège l'historique** quand on restructure |
| **Ordre des couches** | L'ordre d'empilement est enregistré avec la configuration | |
| **Performance** | Section dédiée ; option « n'afficher que les images visibles » ; purge optionnelle des configurations avec LiteSpeed | À regarder pour le panier et le temps de chargement |
| Autres | Thème « EV », configurateur 3D (glTF/GLB) | Hors sujet |

#### Ce que ça change
1. **La fonction de partage existe désormais nativement**, mais elle partage une **couche ou une configuration entière avec ses images**. Les sources ne disent rien du partage des images entre produits. Chez Sellerie Confort, l'image d'une matière sur une couche est la **découpe propre au modèle** : un partage « global » ne s'applique donc directement qu'aux couches dont l'image est identique d'un modèle à l'autre. À tester sur échantillon avant d'en faire la solution.
2. **Mise à jour = migration de données.** La notice de mise à jour dit : « Configurator data moves to a new storage format, converted automatically. » Le changelog, lui, ne parle ni de migration ni de rupture. **Ne rien mettre à jour en production** avant d'avoir testé sur une copie, d'autant que les plugins de VIMAWEB et le plugin « Purge + Tag » s'appuient sur l'ancien stockage.
3. **Publiée le 12/10** : très récente. Mieux vaut attendre une ou deux versions correctives avant de la recommander pour la prod.
4. **L'historique des commandes** : en 1.7.6, une commande peut être rendue à partir de la configuration *actuelle*. Restructurer les données avant la 2.0 peut donc altérer l'affichage des commandes passées. Argument pour mettre à jour d'abord, sur staging, puis restructurer.
5. **Le rattachement par nom de fichier** reste pertinent, notamment pour produire les couches de chaque modèle sans saisie manuelle.

#### Arbre de décision provisoire (étape 2)

| Si les tests montrent que… | Alors |
|---|---|
| Une couche globale peut recevoir une image par modèle (ou des masques) | Utiliser les couches/configurateurs globaux de la 2.0, avec un petit outil d'import par nom |
| Les images sont forcément distinctes par modèle | Petit plugin sur les crochets (filtre `mkl_pc/db/get` ou équivalent 2.0) qui compose les choix depuis un jeu partagé, images rattachées par nom |
| Un rendu « masque + texture » est retenu (tests Phase 1) | Le jeu partagé porte les textures ; une couche par modèle porte le masque. Peu d'images, front-end à adapter |

## 10. Matériel de test reçu et premiers constats (14/10, après-midi)

Règle posée par Melvin : **aucune connexion à l'admin WordPress sans son autorisation explicite.** Tout ce qui suit vient de fichiers qu'il a déposés ou d'images publiques téléchargées avec son accord. Fichiers dans `sellerieconfort-refonte/Phase 1/` (repo `sellerie-confort`).

### Nid d'abeille : fichiers de Valérie (`nid_d_abeille_z900_simulateur.zip`)
| Point | Constat |
|---|---|
| Contenu | **Z900 uniquement**, 11 PNG, un par coloris : alcantara, antidérapant, blanc, bleu azur, bleu égyptien, bleu océan, bleu petronas, bleu sirius, bleu yam, carbone, charbon |
| Format | RGBA, **5712 × 4284** (4:3), contre 1920 × 1280 (3:2) pour les couches du site |
| Contenu réel | Seulement les **arêtes des alvéoles** (0,76 % de pixels opaques), en perspective, sur 3 zones. Géométrie **identique** d'un coloris à l'autre |
| Coloris absents des 37 matières du site | **alcantara, carbone, bleu sirius** (à confirmer : nouvelles matières en stock ?) |

### Exports admin du configurateur (4 produits, faits par Melvin)
Produits 16319 (Triumph Tiger 01, couche nommée « Yamaha TDM 900 »), 17258 (BMW S1000 XR), 17773 (BMW S1000 R), **39477 (Kawasaki Z900 : 10 couches, 294 images)**. L'export natif de `mkl_pc` donne en plus du fichier public les **IDs de pièces jointes**, les dimensions et les vignettes : de quoi recompter les fichiers uniques sans clone. Aucun choix « nid d'abeille » dans la Z900 actuelle. Toutes les images : 1920 × 1280.

### Images Z900 (public, téléchargées avec accord, 26 fichiers, 11 Mo)
`z900-images/sources/` (3 coloris : noir antidérapant, bleu azur, blanc + fond et ombre) ; recomposition dans `z900-images/essais/`.

### Recalage du motif sur la Z900 (essai)
- Recherche automatique (échelle + translation) : **meilleure solution IoU 0,34**, échelle ≈ **0,405**, décalage ≈ (-180, -196) px. Script : `scripts/register_nid_abeille.js`.
- Incrustation visuellement plausible (même perspective), mais **non validée** : des alvéoles débordent du bord de la selle ; découpées par les masques des couches (comportement du configurateur), la zone avant est bien remplie, la zone arrière est surtout coupée. Il manque une référence (capture du simulateur avec le motif posé).
- **Test transfert inter-modèles impossible pour l'instant** : un seul modèle fourni. À porter au rapport comme « non démontré » avec marge de risque sur le chiffrage des broderies.

### Données chiffrées nouvelles
- Échantillon public (39 fiches) : 9 246 références pour **3 596 fichiers uniques** ; 1 762 identifiants partagés par au moins 2 produits (jusqu'à 13). Confirme que les « 83 000 images » sont des références.

### À faire (en attente de Melvin)
- Envoyer le mail groupé : brouillon `Phase 1/mail-valerie-brouillon.md` (accord export, date de départ du délai, information VIMAWEB, second modèle, capture du simulateur, coloris absents).
- Vérifier côté médiathèque l'absence de `.psd` (filtre MIME), à faire par Melvin ou avec son accord explicite.

### Échantillon de 39 fiches configurables (14/10, fichiers publics, lecture seule)

Méthode : 40 fiches tirées à intervalles réguliers parmi les 345 « configurable » du sitemap (1 timeout), fichier de config public lu en mémoire, rien d'autre que le résumé conservé. Résumé et script : `sellerieconfort-refonte/Phase 1/` (`echantillon-configs-publics-2026-10-14.json`, `scripts/sample_configs.py`).

| Mesure | Résultat |
|---|---|
| Type de produit | **39 sur 39 « simple »**, config chargée dans la page (pas de variations) |
| Couches par produit | 8 (28 produits), 10 (9), 9 (1), 7 (1) |
| Jeux de choix par couche | 37 (matières, 174 couches), 44 (liserés, 39), 26 (surpiqûres, 39), 1 (couches fixes, 78) |
| Références d'images | 9 246 pour 39 produits, soit ≈ 237 par produit |
| Images **uniques** | **3 596** (≈ 2,6 références par image) |
| Images utilisées par plusieurs produits | **1 762 sur 3 596 (49 %)**, jusqu'à **13 produits** pour une même image |
| Couches avec choix | 252, dont **98 distinctes** par liste d'images |
| Configurations complètes | **15 distinctes sur 39 produits**, le plus gros groupe en compte **13 identiques** |
| Poids du fichier de config | ≈ 127 Ko en moyenne |
| Jeux de noms de matières | 6 variantes (au lieu de 3 attendus) : fautes de frappe et copies |

#### Ce que ça corrige et ce que ça apporte
1. **Je corrige l'audit d'octobre** (« rien n'est partagé entre modèles ») : les **images sont déjà réutilisées** entre produits quand la forme de selle est la même (jusqu'à 13). La duplication est dans la **configuration de chaque produit** (JSON copié), pas dans les fichiers.
2. **Le nombre d'images à produire est bien plus faible que 83 000** : 83 000 est un nombre de références. Le chiffrage de l'étape 1 doit porter sur les **couches distinctes**, donc sur les formes de selle, pas sur les fiches.
3. **Les couches et configurateurs globaux de la 2.0 deviennent très plausibles** : un groupe de produits identiques (jusqu'à 13) est exactement un « configurateur global » à assigner par catégorie. Sur l'échantillon, 252 couches se réduisent à 98, et 39 configurations à 15.
4. **Pas de variations** : tous les produits sont simples, donc le mode `share_layers_config` n'est pas utilisé.
5. **Prudence** : échantillon de 39 sur 345 (11 %), tiré par ordre alphabétique des URL. La proportion de doublons sur l'ensemble reste à confirmer sur les 345 (≈ 700 requêtes publiques, quelques minutes).
6. **Un écart à expliquer** : les 345 fichiers de config publics pèsent ≈ 44 Mo (345 × 127 Ko), alors que `SC_postmeta` fait **1 101 Mo**. La config visible n'en explique que 4 %. Reste ≈ 1 Go à identifier (sauvegardes `__backup`, métas de plugins, résidus d'anciens plugins ?). Piste d'allègement de la base (1,47 Go) et de performance, à documenter dans le rapport. Non visible depuis l'extérieur : nécessite les données.
7. **Export WordPress natif par catégorie : impossible pour les produits.** Le filtre de catégorie n'existe que pour les articles. L'export « tous les produits » (1 595, avec 1,1 Go de métadonnées) renvoie `ERR_INVALID_RESPONSE`. Ne pas le relancer sans filtre de dates restreint.
8. **Ce que le fichier public contient et ne contient pas** (contrôle sur le produit 16319). Présents : `layers` (couches : nom, type, ordre, nombre de choix), `content` (choix : nom, ordre, image par angle, vignette, valeur par défaut, disponibilité), `angles`, `product_info`. **Absents** : champs d'administration (libellés internes, drapeaux « masqué », prix additionnels), sauvegardes, date de dernière modification, produits non publiés ou hors sitemap. Les **images sont les fichiers d'origine** (PNG 1920 × 1280, 85 à 613 Ko), sans dégradation.
9. **Conséquences** : l'admin affiche **1 593 produits : 1 526 publiés, 66 brouillons, 1 privé, 1 en corbeille**. Les 66 brouillons et le privé ne sont **pas visibles** dans le public. Le fichier public suffit pour chiffrer ce que voit le client. Il ne suffit pas pour un **inventaire contractuel** : le compte de 345 fiches vient d'un motif de slug (« configurable »), pas d'un drapeau, donc des produits configurables peuvent échapper (les 376 « autres slugs »). À recouper par l'admin : filtre sur l'étiquette « Configurable » (posée par le plugin « Purge + Tag ») et export de contrôle de quelques produits via l'onglet Import/Export du configurateur.
10. **Convention de nom des images** : `Selle-{Marque}-{Modèle}-{zone}_{NN}_{Matière}.png`, par exemple `Selle-Yamaha-TDM-900-bec_00_Noir-Antiderapant.png`. L'indice `_NN` est un ordre à vérifier : il rend le rattachement par nom réaliste.
11. **Comparaison export admin / fichier public sur 4 produits (14/10, 16h41-16h47)** : produits 16319 (8 couches, 220 choix), 17773 (10 couches, 294 choix), 17258 (9 couches, 257 choix), 39477 (10 couches, 294 choix). Résultat : **identiques** sur les quatre. Mêmes couches, mêmes choix, mêmes **identifiants d'image à 100 %** (220, 294 et 257 sur 220, 294 et 257), mêmes champs. Seule différence : `display_mode` est présent sur toutes les couches dans l'export et sur une seule dans le public. Aucun choix masqué ou indisponible (`available` vrai partout), aucun prix additionnel, aucun libellé interne : **le fichier public est fidèle pour les produits publiés**. Une seule vue (« Face »). Fichiers : `Phase 1/configurator-data--product-*.json`. Script : `Phase 1/scripts/` (comparaison).
12. **Conséquence** : l'analyse des 345 fiches publiques est fiable pour le chiffrage. L'écart restant concerne ce que le public ne montre pas par nature : **66 brouillons** et 1 produit privé, et d'éventuels produits configurables hors du motif de slug. Les prix ne dépendent pas des choix (aucun `extra_price`) : un jeu partagé n'a pas de tarif à porter.

### Analyse des 345 fiches « configurable » publiques (14/10, 16h45-17h01, 0 erreur)

Même méthode que l'échantillon, sur l'ensemble des 345 fichiers de config publics. Résumé : `Phase 1/analyse-345-fiches-publiques-2026-10-14.json`. Script : `Phase 1/scripts/sample_configs.py`.

| Mesure | Résultat |
|---|---|
| Produits | **345 simples**, aucune variation |
| Couches par produit | 8 (238), 10 (91), 9 (9), 7 (7) |
| Références d'images | **83 034** |
| Images uniques | **10 937** (10 935 noms de fichier), soit ≈ 7,6 références par image |
| Images partagées entre produits | **7 243 sur 10 937 (66 %)**, jusqu'à **117 produits** pour une même image |
| Couches avec choix | **2 254**, dont **302 distinctes** par liste d'images (13 %) |
| Configurations complètes distinctes | **46 pour 345 produits** |
| Taille des groupes de produits identiques | 117, 41, 26, 20, 19, 12, 11, 9, 9, 7, 5, 5… ; **17 produits isolés** |
| Jeux de choix | 37 matières (1 521 couches), 44 liserés (357), 26 surpiqûres (338), 1 choix fixe (689), **atypiques : 34 couches** (41, 45, 46, 36, 40 ou 27 choix) |
| Jeux de noms distincts | **27** au lieu de 3 attendus (fautes de frappe, copies, orthographes) |
| Poids moyen du fichier de config | ≈ 129 Ko |

#### Ce que ça change
1. **Le vrai volume est ≈ 10 900 images, pas 83 000** (83 000 = références).
2. **345 fiches se ramènent à 46 configurations** : c'est le nombre d'objets à maintenir si on regroupe. 17 sont des produits isolés, à traiter un par un. Le plus gros groupe (117 produits) ne demande qu'un seul « configurateur global » en 2.0.
3. **302 couches distinctes** : c'est la bonne unité de chiffrage pour les images de l'étape 1.
4. **Nettoyage préalable** : 27 jeux de noms à ramener à 3 et 34 couches atypiques à examiner (dont CFMOTO).
5. **Borne haute** : les 46 groupes sont des identités exactes. Une couche en plus ou une image différente sépare deux fiches presque identiques, donc le nombre réel de familles sera inférieur après nettoyage.
6. **Limites** : analyse des produits publiés repérés par le motif de slug (345 sur 1 526 publiés). Restent à examiner les 66 brouillons et d'éventuels configurables hors motif.
