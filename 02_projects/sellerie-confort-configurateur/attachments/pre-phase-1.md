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
| Accord écrit pour le plugin d'export | **Obtenu par mail de Valérie** : installation temporaire de l'extension nécessaire à la copie technique, « conformément au contrat ». **Conditions** : aucune donnée personnelle ni commande exportée ; extension désinstallée dès l'export terminé. **Non utilisé à ce jour** (le public suffit, voir §9) : en réserve |
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
- **Essai 1 (échec, constaté par Melvin)** : pose rigide (échelle + translation) du motif sur le rendu du configurateur, meilleur IoU 0,34, échelle ≈ 0,405. **Le motif ne suit pas la courbure de la selle.** Cause : le motif n'est pas dessiné sur le rendu du configurateur. Script `scripts/register_nid_abeille.js` : à ne pas réutiliser tel quel.
- **Diagnostic (confirmé)** : le PNG 5712 × 4284 est dessiné sur la **photo** de la selle finie (cadrage d'origine d'un smartphone, redimensionnée à 2560 de large puis recadrée par le site). Superposé à la photo `z-900-nid-d-abeil.jpg-vert-kawa-scaled.jpg` avec échelle = 2560 / 5712 ≈ 0,448 et décalage vertical ≈ -100 px, les alvéoles coïncident avec la vraie broderie (résidu de 10 à 20 px à affiner). Les 3 zones du motif = panneau avant (grande zone), liseré haut du panneau avant, assise arrière.
- **Conséquence** : le nid d'abeille n'existe aujourd'hui dans aucune couche du configurateur ; il est montré par des photos de selles réelles. Le configurateur affiche un autre point de vue (rendu), il faut donc un **passage photo → rendu par panneau** (transformation projective par panneau, puis éventuellement maillage). C'est le vrai travail de la Phase 2 sur les broderies.
- **Références disponibles dans `clone-fichiers/wp-content/uploads`** : 7 photos Z900 avec nid d'abeille (`2025/01/z-900-nid-d-abeil*`), et d'autres modèles (Z650, BMW R1200/1250 GS, Hornet 750, Aprilia RS 660, MT-07…) : vérité terrain pour le test inter-modèles.
- **Essais de déformation vers le rendu propre (noir et azur)** : (v1) normalisation radiale par zone : échec ; (v2) correspondance colonne par colonne entre les bords haut et bas du motif et du panneau : **le panneau avant suit la courbure, les alvéoles sont lisibles, mais elles sont étirées (×2,7 en largeur) et l'assise arrière est inutilisable** ; (v3) repère de l'axe principal : pire (cisaillement). Conclusion : une correspondance **par contours seuls ne suffit pas** ; il faut soit des points de contrôle placés à la main (maillage), soit une génération paramétrique du motif suivant la surface. Fichiers `essais/warp-v*`, script `scripts/warp_nid_abeille_v2.js`. À présenter comme **faisabilité partielle**, pas comme résultat publiable.
- **Essai v4 : maillage à points de contrôle (thin-plate spline), 17 points avant + 16 arrière, fait à la main sur la photo et le rendu** : **résultat exploitable comme démonstration** (alvéoles hexagonales en perspective sur le panneau avant, le liseré haut, le bec et l'assise arrière, découpées par les masques des couches, sur compo noir et compo azur). Défauts : alvéoles étirées en bas du panneau avant, bord irrégulier de l'assise arrière, quelques fragments au bec. Points : `scripts/tps_points_avant.json`, `tps_points_arriere.json` ; script `scripts/tps_nid_abeille.js` ; images `essais/maillage-tps-*.png`. Coût réel : relever ~30 points par modèle, c'est le temps de travail à chiffrer par modèle en Phase 2 (ou à automatiser par détection de contours des panneaux).
- **Essai v5 : génération procédurale** (Melvin : le maillage n'est « pas propre ») : réseau d'hexagones réguliers (pointe en haut, allongés) dessiné dans le repère de la selle (surface réglée entre bord haut et bord bas relevés à la main), traits de largeur constante, cellules retenues seulement si leur centre tombe dans l'empreinte du motif de Valérie, découpe par les masques de couches. **Plus propre** : pas de lignes déchirées ni de fragments, perspective suivie. Défauts : cellules entières seulement donc couverture irrégulière au bord, pas de relief (ombres) sur les traits, arrière peu couvert, paramètres de densité réglés à l'œil (15 colonnes × 4,4 rangées devant, 11 × 3 derrière). Fichiers `essais/procedural-*.png`, `scripts/proc_nid_abeille.js`. C'est la voie qui généralise : un modèle = 2 courbes de bord + 2 réglages de densité.
- **CORRECTION (la plus importante) : le calque se pose presque tel quel.** Melvin avait raison : « le calque du nid d'abeille sans la selle » et « le calque de la selle sans le nid d'abeille » se superposent. Avec **échelle = 1920 / 5712 ≈ 0,336 et décalage vertical ≈ -100 px**, sans aucune déformation, 93 % des pixels du motif tombent sur la selle de la Z900 et le rendu est le meilleur de tous les essais (`essais/CALQUE-SIMPLE-noir-motif-blanc.png`, `...-azur-...`). Le PNG 5712 × 4284 (4:3) est simplement un canevas plus haut que celui du configurateur (1920 × 1280, 3:2). Mes essais précédents (déformation radiale, maillage, génération procédurale) partaient d'un diagnostic **faux** (« autre point de vue ») : ils sont à considérer comme des impasses, pas comme la voie à suivre. Mon premier calage (IoU 0,34, échelle 0,405) utilisait une mauvaise métrique. Reste à affiner : échelle/décalage fin (quelques pixels), épaisseur des traits à l'échelle réduite, recoloration par coloris de fil.
- **Hypothèse de Melvin validée : le calque a été dessiné sur la photo `z-900-nid-d-abeil.jpg-vert-kawa-scaled.jpg`.** Les 6 variantes de `2025/01` (rouge, argent, vert primaire, grioote et blanc, etc.) sont la même prise de vue avec des fils de couleurs différentes ; **aucune version brute (sans broderie) n'est dans le clone**. Reconstitution : calage du calque sur la photo par corrélation avec le vert des fils (échelle ≈ 0,462 du cadre 5712, décalage (-17,5 ; -138) dans le cadre 2560 × 1626), puis effacement des fils par diffusion. **Résultat : le calque (bleu azur, blanc) se pose proprement sur la base, en suivant la courbure** (`essais/RESULTAT-calque-*-sur-base-effacee.png`, base `BASE-photo-vert-kawa-broderie-effacee.png`). Défauts : bords bosselés où la broderie touchait la jonction avec le carbone, coutures vertes d'origine encore visibles. **À demander à Valérie : la photo brute d'origine (5712 × 4284) sans broderie**, avec laquelle ces défauts disparaissent. Le simulateur de Valérie = photo brute + un PNG de broderie par coloris de fil.
- **Essai v6 (échec) : génération à partir des seuls masques de couches** (coordonnées harmoniques `u,v` du panneau, réseau hexagonal dans ce repère, éclairage de la couche « Ombres et éclairage »). Les masques de panneaux sont déjà là pour chaque modèle (donc pas besoin de SAM). Mais le repère harmonique n'est **pas isométrique** : les cellules passent de minuscules à énormes et deviennent des polygones irréguliers (`essais/warp-v6-noir-ECHEC-*.png`). Il faut un vrai **dépliage** (LSCM / ARAP, ex. UV unwrap de Blender ou `libigl`) pour garder une taille de cellule constante. À ne pas refaire à la main en JavaScript.
- **Outillage installé le 14/10 (accord explicite de Melvin)** : Python 3.14 (déjà présent), environnement isolé `C:\Users\LENOVO\ai-tools\sellerie-venv` : NumPy, SciPy, OpenCV, scikit-image, PyTorch **CPU** (pas de GPU NVIDIA, AMD Radeon 740M), transformers, libigl. Modèle de profondeur : **Depth Anything V2 Small** (HF `depth-anything/Depth-Anything-V2-Small-hf`). Une autre installation existe dans `Documents\Depth-Anything-V2` (autre session).
- **Essai v7 : dépliage à pas constant** (masques des couches + profondeur Depth Anything + dépliage). (a) LSCM maison à bord libre : **échec** (solution non unique, échelles de 0,01 à 149) ; (b) **MDS à repères sur distances géodésiques** (quasi isométrique) : **le panneau avant donne un réseau à cellules de taille régulière qui épouse la selle** (`essais/AUTO-depliage-*.png`), sans aucun relevé manuel. Défauts : lignes un peu ondulées, fissures aux bords, orientation des cellules non pilotée, **assise arrière ratée** (domaine assise arrière + dosseret : lignes déformées sur le logo). Meilleur résultat automatique à ce jour, mais **pas au niveau d'un calque dessiné** ; la profondeur seule n'est pas la limite (même résultat à relief nul). Piste suivante : contraindre l'orientation du réseau, traiter chaque panneau séparément, lisser le champ.
- **Reprise à zéro (Opus, 14/10 soir), dossier `Phase 1/opus-nid-abeille/`** :
  - **Calage exact du PNG sur la photo** par distance de chamfer sur les vrais fils : `sx=0,4790 sy=0,4786 dx=-79,9 dy=-174,7` (cadre 2560 × 1626), écart moyen **0,01 px**, 100 % des pixels sur les fils, identique sur la photo rouge. **Mon calage précédent (0,462) avait 3,7 % d'erreur d'échelle** : il explique une partie des décalages des essais antérieurs.
  - **Les photos `2025/01` (vert Kawa, rouge, argent, grioote…) sont toutes la même prise de vue**, recadrée et recolorée (simulateur de Valérie). Aucune n'offre un autre point de vue.
  - **Chaîne de transfert validée** (photo effacée → autre photo effacée, correspondance dense RoMa, sans voir la broderie) : 99,2 % du motif à ≤ 3 px des vrais fils, écart moyen 0,1 px. Valide la chaîne, pas la robustesse au changement de point de vue (le cas test est une homographie).
  - **RoMa (correspondance dense, état de l'art) échoue entre photo et rendu** : certitude moyenne 0,005 (contre 0,35 photo/photo), correspondances incohérentes. Cause : écart d'apparence + **les deux pièces (avant, arrière) sont posées différemment à chaque prise de vue**, aucune transformation globale possible.
  - **Méthode retenue : SAM (segmentation par pièce) + recalage par silhouette (homographie ECC + spline TPS sur le contour) pièce par pièce, puis rendu depuis le PNG pleine résolution avec les couleurs/textures d'origine et l'ombrage du rendu.** IoU silhouette 0,973 (avant) et 0,982 (arrière). **Variante 1 (silhouette) = meilleur résultat automatique de la journée**, proche de la disposition réelle (`resultats/V1-*`, comparaison `resultats/COMPARAISON-reference-V1-V2.jpg`). Variante 2 (surface d'assise seule) : cellules étirées, liseré perdu.
  - Limites : correspondance par contour, pas par surface 3D ; aucune vérité terrain sur le rendu (jugement visuel) ; un seul modèle. Outils ajoutés : `kornia` (LoFTR), `romatch` (RoMa + DINOv2), SAM via transformers (`facebook/sam-vit-base`), poids en cache `~/.cache`.
- Fichiers déposés par Melvin dans `essais/` : `Z900 nid abeille gris.png` est une vignette 400 × 400 (trop petite pour mesurer) ; `Z900 nid abeille vert.htm` est une **page d'admin WordPress enregistrée** (médiathèque), pas une image : à ne pas utiliser.

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


## 11. Clone local (construit le 14/10, soir)

### Fichiers : `Phase 1/clone-fichiers/`

| Dossier | Contenu | Rôle |
|---|---|---|
| `00-master/` | 4 archives UpdraftPlus (`plugins`, `themes`, `mu-plugins`, `others`) + `SHA256SUMS.txt` | Original, **lecture seule** |
| `01-lecture/` | Code extrait (26 499 fichiers, 396 Mo) | Lecture |
| `02-essai/` | Copie identique | À casser |
| `03-reserve/` | Copie identique | Référence |
| `wp-content/uploads/` | Médias téléchargés à l'identique (+ `manifeste-medias.csv`) | Source des images du site local |

Contrôles faits sur les archives, sans les extraire : **aucune base de données, aucun `wp-config.php`, aucun téléversement**. Fichiers signalés : `plugins/woo-payline-caution/.env` (4 variables d'URL, pas de clé), `wpayline_caution__debug.log` (29 Ko, aucune adresse e-mail, téléphone ni IBAN détectés), `error_log` du plugin DPD (27 Mo, 134 909 lignes : le plugin journalise sans fin, constat de santé). Les journaux ne sont pas dans les copies de travail. Le dossier `wpvivid_staging` vient de notre essai WPvivid, pas de la prod.

Inventaire des plugins (38 dossiers) : le plugin compromis y figure sous `wp-logo-showcase-responsive-slider-slider` (106 fichiers) ; dossiers d'origine locale : `sc-export-pdf-factures`, `sc-notice-carbone`, `sc-order-note`, `purge-bandeaux-noir-diamant`. `mu-plugins` : `active-plugins.php` (ARTEO), `fix-wapf-preview.php`, `InitUmbrella.php`.

### Site local : `sellerie-confort.local`

| Élément | Valeur |
|---|---|
| Outil | Local (WP Engine), site `sellerie-confort`, dossier `C:\Users\LENOVO\Local Sites\sellerie-confort` |
| Environnement | WordPress **7.1.3**, PHP **8.2.29** (prod : 8.3.35), nginx, base sur le port 10005 |
| Thème | Divi Child (Divi 4.27.8) |
| Plugins actifs | WooCommerce 11.2.1, Product Configurator 1.7.6, APF Extended 3.2.1 |
| Exclus | Plugin compromis, WP Umbrella, CleanTalk, LiteSpeed Cache, UpdraftPlus, WP Tiger |
| Repère visuel | Barre d'admin **rouge** + « LOCAL » (`mu-plugins/env-local-banner.php`) |
| Compte admin | `Mel` (local, sans lien avec les sites du client) |
| Produits | 345 recréés depuis les fichiers publics avec leurs identifiants d'origine (`reconstruction/donnees/`, scripts `build_products.php`) |
| Pièces jointes | Insérées avec leurs identifiants d'origine (`build_attachments.php`) |
| Orchestration | `scripts/pipeline_reconstruction.ps1`, journal `reconstruction/pipeline.log` |

Le site local n'est branché sur aucune des quatre copies : son code a été **copié depuis `01-lecture`** (empreinte du fichier principal du configurateur identique). Instantané de la base à prendre une fois la reconstruction terminée.

### Règle d'accès
Sites du client (prod, dev, préprod) : connexion à l'admin sur autorisation explicite, cas par cas. WordPress local : accès libre (décision de Melvin du 14/10/2026). Mémoire et `CLAUDE.md` du dépôt à jour.

### Outils et scripts (dans `Phase 1/scripts/`)
`sample_configs.py`, `compare_export.py`, `download_media.py`, `inspect_archives.py`, `check_flagged.py`, `extract_master.py`, `fetch_products_data.py`, `build_products.php`, `build_attachments.php`, `pipeline_reconstruction.ps1`.


## 12. Lecture du code sur mesure (14/10, soir, depuis `01-lecture`)

Lecture seule, rien exécuté. Plugins et correctifs écrits pour ce site.

| Fichier | Auteur (en-tête) | Fonction | À retenir |
|---|---|---|---|
| `plugins/purge-bandeaux-noir-diamant/` (1 628 lignes) | « Vous » | **Outil d'administration** (Outils → `sc-pc-tools`) : 1) retire un choix de couleur/matière (`Noir diamant`) de toutes les structures du configurateur, avec dry-run puis exécution, sauvegarde et CSV ; 2) pose l'étiquette « Configurable » sur les produits configurables ; 3) purge des méta de cache | Voir ci-dessous |
| `plugins/sc-notice-carbone/` | Sellerie Confort | Fenêtre modale d'information sur la suppression de la finition Carbone | Aucun lien avec la logique du configurateur |
| `plugins/sc-order-note/` | Vimaweb | Colonne « Notes » dans la liste des commandes | Hors configurateur |
| `plugins/sc-export-pdf-factures/` | Vimaweb | Export ZIP de factures PDF par plage de dates | Données personnelles : hors périmètre |
| `mu-plugins/fix-wapf-preview.php` | `vw_` (Vimaweb) | Contournement d'un bogue d'APF Pro 2.7.5 (aperçu dans l'éditeur) | APF Pro est désormais **inactif** (Extended 3.2.1 actif) : correctif probablement caduc |
| `mu-plugins/active-plugins.php` | ARTEO Digital | Filtre la liste des extensions actives | À lire avant toute activation en local |

### Ce que le plugin de purge explique
1. **Les 1,1 Go de `postmeta`** : à chaque exécution réelle, pour chaque méta du configurateur modifiée, il ajoute une **copie complète « avant »** sous la clé `<clé d'origine>_backup_bandeaux_purge_<meta_id>`. Dix ou douze exécutions sur 345 produits suffisent à expliquer le gros du poids : **hypothèse forte, à confirmer avec les données** (le décompte des clés `*_backup_bandeaux_purge_*`). Piste d'allègement : base de 1,47 Go à environ 0,4 Go.
2. **L'étiquette « Configurable » n'existe pas** : la fonction de pose n'a jamais été exécutée. Ce n'est donc pas un indicateur fiable de produits configurables.
3. **Les dates de modification ne sont pas des dates d'édition** : l'outil fait un `wp_update_post` sur chaque produit traité. Le « modifié le 13/10 » de plusieurs centaines de produits vient très probablement de là. À ne pas utiliser pour dater des changements de contenu (conclusion corrigée sur dev, voir §9).
4. **Fiabilité** : l'outil manipule des tableaux sérialisés ligne à ligne, avec des suppressions de méta et de cache par motif `LIKE`. C'est du code de maintenance en production non revu : à signaler comme risque dans le rapport.

## 13. Rendu du configurateur en local (14/10, soir)

Page de test : `http://sellerie-confort.local/product/modele-selle-configurable-triumph-tiger-01/` (produit 16319). Comparaison du HTML public de la prod et du site local.

| Élément | Prod | Local, état initial | Local, après alignement |
|---|---|---|---|
| Thème du configurateur | `clean` | `float` (défaut) | **`clean`** |
| Fermeture après ajout au panier / après un choix | oui / oui | non / non | **oui / oui** |
| Image du choix actif dans la couche | oui | non | **oui** |
| Devise et format | `€`, virgule décimale | `$`, point | **`€`, virgule** |
| Messages | en français | en anglais | **en français** (paquets de langue copiés) |
| Bouton | « Configurer » | « Configure » | **« Configurer »** |

Deux pièges rencontrés : WooCommerce était en mode **« bientôt disponible »** (le site local n'affichait pas les produits : `woocommerce_coming_soon` passé à `no`), et les réglages du configurateur sont dans l'option `mkl_pc__settings`, absente d'une base neuve (reproduits depuis l'objet public `PC_config`). Script : `Phase 1/scripts/set_prod_like_settings.php`.

### Ce qui reste différent
- **Page autour du configurateur** : la prod utilise des modèles **Divi Theme Builder** (en-tête, pied de page, fiche produit : 131 sections contre 24 en local), stockés en base, donc absents.
- **Options de commande** (gel, chauffage, hauteur, mode de commande) : ce sont des groupes de champs APF (`wapf_product`, 38 en prod) stockés en base, donc **absents**. À reconstruire depuis le HTML public si besoin.
- Classes du bouton : celles du thème local (`primary button btn btn-primary wp-element-button`) contre `button` en prod. Cosmétique.
- Réglages secondaires du configurateur non exposés au public (prix dans le configurateur, nom des angles) : défauts.

## 14. Référence du front, options de commande, charpente de chiffrage (14/10, soir)

### A. Référence du front existant
Captures publiques, bureau (1440) et mobile (390), pages entières : `Phase 1/reference-front/{desktop,mobile}/` (12 pages, + fiche produit avec configurateur ouvert). Script : `scripts/capture_reference.mjs`. Aucun clone nécessaire : c'est le public.

| Constat sur la fiche produit actuelle | |
|---|---|
| Structure | Fiche Divi : étiquette « Configurable », photo, prix (barré 250 € → **210 € TTC**), bloc Cofidis 3x/4x, puis formulaire APF **sous** le configurateur |
| Le configurateur | **Plein écran séparé** (liste des 6 couches à gauche, selle à droite, « Valider la configuration », « Reset ») : ce n'est donc pas « tout sur une page » |
| Parasites à l'ouverture | Fenêtre « Information importante » (Carbone) + bannière cookies |
| Prix | Le public renvoie 250 € (prix de base) ; le 210 € vient de **Discount Rules** : le local affiche 250 € |
| Page oubliée en ligne | `xx__ma-moto-php-shortcode__archive-backup` (page d'archive de code, publiée) |

### B. Options de commande (APF), 4 fiches publiques
Détail : `Phase 1/reconstruction/options-apf-echantillon.json`. Script : `scripts/inventory_options.py`.

| Groupe | Champs | Fiches |
|---|---|---|
| **Communs** (groupes `59570`, `4659`) | Modèle de ma moto*, Année*, Taille pilote*, Poids pilote*, Poids passager, Commentaires, **Type de commande*** (2 choix), **Hauteur d'assise pilote*** (3), **Option gel** (4), Options de selle, Informations complémentaires, **Broderies*** (oui/non) | 4 sur 4 (12 champs) |
| **Par modèle** (groupes `858`, `1132`, `p_<id>`) | Broderie dosseret*, Motif de broderie (3), **Couleurs de broderie (26)**, Motif bandes / dosseret, Précisions couleurs, Autres couleurs | 1 à 2 sur 4, conditionnels |

Surcoûts relevés : hauteur ±2 cm **+10 €**, gel avant / arrière **+35 €**, deux assises **+70 €**. 12 à 17 champs par fiche, **règles conditionnelles** (la broderie ouvre le motif, qui ouvre les couleurs). Sur 38 groupes au total, un socle commun et des groupes propres à chaque modèle.

### C. Charpente de chiffrage (ordres de grandeur, à valider)
Taux 350 €/j. Volumes : 345 fiches = **46 configurations**, 302 couches distinctes, 27 marques, 448 modèles, 15 pages, 1 526 produits, 34 plugins actifs.

**Phase 2 : simulateur + parcours de commande (page produit unique)**

| Poste | j |
|---|---|
| Design de la page unique, mobile compris (maquette R6) | 1 à 2 |
| Nettoyage des données (27 jeux de noms, 34 couches atypiques) et regroupement en 46 configurations | 3 à 5 |
| Configurateur 2.0 ou plugin sur crochets, essais de migration, retour arrière | 2 à 4 |
| Page : configurateur **intégré** + options + infos client sur une seule page | 4 à 6 |
| Broderies / nid d'abeille (selon les tests) | 2 à 4 |
| Recette, staging, mise en production | 2 à 3 |
| **Total** | **14 à 24 j (≈ 4 900 à 8 400 €)** |

Plafond contractuel : **7 000 € HT**, soit **16 j** après déduction des 1 400 € de Phase 1. La page produit unique relève du « simulateur et parcours de commande » : elle est **dans** le plafond. Au-dessus de 16 j : resserrer (broderies en option), pas absorber.

**Phase 3 : refonte complète sous WordPress**

| Poste | j |
|---|---|
| Thème sur mesure à la place de Divi (système de design, en-tête, pied, modèles) | 6 à 10 |
| Marques, catégories modèle, recherche « Ma moto » | 5 à 8 |
| Pages de contenu (Matières, FAQ, Infos, Contact, légal) | 3 à 5 |
| Panier et paiement (Alma, Cofidis, Payline, caution échange standard, DPD) | 4 à 7 |
| Compte client, e-mails, factures PDF | 2 à 4 |
| SEO (301), performance, accessibilité, RGPD | 3 à 5 |
| Recette, migration, mise en production, formation | 3 à 4 |
| **Total** | **26 à 43 j (≈ 9 100 à 15 000 €)** |

La cible interne de **≈ 5 000 € (14 j)** est très inférieure. Leviers : conserver Divi et ne refaire que les modèles (≈ −10 à −15 j), migrer un socle de pages, découper en lots. **Maintenance** (cible 450 €/mois) : chiffrage à part, avec périmètre et exclusions.

**Pour rendre le chiffrage ferme** : décision Divi conservé ou non ; résultats des tests matières et broderies ; périmètre des pages ; inventaire des 38 groupes APF (4 fiches sur 38 faites).

## 15. Reconstruction terminée, front Divi, instantanés (14/10, 20 h 40)

### Bilan de la reconstruction locale
| Élément | Résultat |
|---|---|
| Produits | **345 sur 345** publiés, identifiants d'origine conservés |
| Médias téléchargés (API REST publique, mêmes chemins) | **15 120 sur 15 123** (5,33 Go) ; 1 fichier invalide (`2026/08/SELLE-MANDELLO-1-scaled.jpg`, id 187710) ; 2 en erreur HTTP (`BMW-R-1200RT-surpiqures_25/26`, ids 2803 et 2804) |
| Pièces jointes enregistrées | **15 121** (avec leurs identifiants d'origine) |
| Images d'un produit testé (16319) | **220 sur 220** présentes, servies en HTTP 200 |
| Page produit locale | HTTP 200, bouton « Configurer », thème `clean` |
| Utilisateurs en base locale | 1 (compte `Mel`), aucune donnée personnelle |

### Front de référence : exports Divi reçus (3 fichiers, `Phase 1/divi-export/`, ignoré par Git)
| Fichier | Contenu | Inspection |
|---|---|---|
| `Modeledivithemebuilder.json` (17 Mo) | **23 modèles** Theme Builder : site par défaut (en-tête 31066), Boutique, **13 modèles propres à des marques** (Aprilia, BMW, Ducati, Honda, Kawasaki, KTM, Suzuki, Triumph, Yamaha, CFMoto, Zontes, Voge, Moto Guzzi, Indian, Kymco, Honda Hornet), toutes les catégories, tous les produits, produits avec l'étiquette « Selle configurable », 404 | Aucune clé sensible ; une seule adresse e-mail (`contact@sellerieconfort.com`, 63 occurrences : coordonnées du magasin) |
| `Options du thème Divi.json` | Réglages Divi (logo, palette, navigation) | Aucune clé d'API |
| `Configurations personnalisées Divi.json` | Personnalisation (couleurs, polices, tailles) | Aucune clé sensible |

Les deux fichiers d'options sont **appliqués** au site local par script (`scripts/import_divi_options.php` : 96 réglages et 221 réglages de personnalisation ; palette `#111111 | #ffffff | #1a428a | #426ca9 | #d02c30…` ; logo d'origine). Le Theme Builder s'importe **dans l'interface** (Divi → Theme Builder → portabilité → importer), le gestionnaire d'import procédant par étapes avec jetons de page.

À noter pour la refonte : **13 modèles dupliqués par marque** (même mise en page, répétée) ; une seule gestion centralisée suffirait dans une refonte.

### Instantanés (dans `Phase 1/clone-fichiers/snapshots/`)
| Fichier | Contenu |
|---|---|
| `db-apres-reconstruction-2026-10-14.sql` (+ `.sha256`) | Base du site local après reconstruction (≈ 70 Mo), point de retour avant le test de la 2.0.0 |
| `site-local-code-hors-uploads-2026-10-14.zip` | `wp-content` du site local sans `uploads` |

### Front Divi importé en local (14/10, 21 h 30)
Import du Theme Builder **par les vrais appels AJAX de Divi** (`scripts/import_divi_via_http.php`) : l'import en ligne de commande vidait les modules (le contexte `admin-ajax` charge les modules, pas la ligne de commande). Résultat : **23 modèles**, 1 en-tête global, 22 corps ; le modèle par défaut est défini.

| Élément | État local |
|---|---|
| En-tête (logo, menu principal à 7 entrées dont 29 marques) | Reconstruit depuis le HTML public |
| Fiche produit : bandeau, titre, prix, bouton « Configurer », « Caractéristiques », images, pied de page (coordonnées, horaires) | **Présents**, fidèles à la prod |
| Image principale des produits | 345 posées (via l'API REST publique) |
| Réglages et personnalisation Divi | Appliqués (palette, logo) |
| Pages (accueil, FAQ, matières, contact…) | **Absentes** (contenu en base) : export WordPress « Pages » à faire |
| Menus du pied de page | Non retrouvés dans le HTML public |
| Options de commande APF (gel, hauteur, broderies…) | Absentes (groupes en base) |
| Menu rapide (Mon compte, Panier) | Créé ; liaison au module à reprendre |

Pièges rencontrés : (1) les modules **globaux** de la bibliothèque Divi ne sont pas dans l'export du Theme Builder : références retirées, contenu inline conservé (`scripts/strip_global_modules.php`) ; (2) les menus de la prod ont des identifiants qui n'existent pas en local (`relink_menus.php`) ; (3) WooCommerce était en mode « bientôt disponible ».

### Pages importées en local (14/10, 21 h 50)
Export WordPress « Pages » déposé par Melvin (15 pages, 1 auteur, aucune donnée personnelle ; seules coordonnées : contact@sellerieconfort.com et deux adresses d'ARTEO dans les mentions légales). Importé par script (`scripts/import_pages_wxr.php`) avec les identifiants d'origine ; pages WooCommerce (boutique 791, panier 792, commande 793, compte 794, CGV 17922), accueil (29) et URL des produits `/selle-de-moto/<produit>/` alignés sur la prod.

L'accueil local reproduit le contenu de la prod. Écarts : le **sélecteur « Ma Moto »** (code PHP sur mesure, dont une page d'archive `XX__Ma Moto Php ShortCode__ARCHIVE Backup` reste publiée en prod), des images de bibliothèque absentes, le curseur de produits (plugin Product Slider à activer), les options de commande APF et les menus du pied de page.

### Enseignement du clone du front, pour le chiffrage (14/10, soir)
Reproduire en local le front « tel qu'il est » a demandé plusieurs heures de travail, alors que le code, les données publiques et les médias étaient déjà disponibles. Ce que l'exercice a révélé de la **dette du front**, à reporter dans la Phase 3 :

| Constat | Conséquence pour la refonte |
|---|---|
| **23 modèles** Theme Builder, dont **13 dupliqués par marque** (même mise en page répétée) | Un seul modèle paramétré suffit : gain de maintenance, mais à reconstruire |
| **Modules globaux** de la bibliothèque Divi référencés par les mises en page, absents de l'export du Theme Builder | Dépendance cachée : une migration casse l'en-tête sans prévenir |
| **Menus, widgets, pages, groupes d'options (APF), catégories** stockés en base, non récupérables depuis les fichiers | Un clone « par fichiers » ne rend pas le site ; la base filtrée est nécessaire pour une copie fidèle |
| Sélecteur **« Ma Moto »** en PHP hors plugin, page d'archive du code encore publiée | Fonction centrale du parcours sans propriétaire ni documentation |
| Export du Theme Builder **inutilisable en ligne de commande** (modules non chargés) | Toute automatisation de migration doit passer par le contexte administrateur de Divi |

Chiffrage : ces points justifient une fourchette large pour la Phase 3 (**26 à 43 j**) et plaident pour **documenter avant de migrer** (inventaire des modèles, des menus, des groupes d'options et des fonctions sur mesure).

### Catégories, sélecteur « Ma Moto », options de commande (14/10, 22 h)
| Élément | Résultat local |
|---|---|
| Catégories de produits | **501 recréées** depuis l'API REST publique, identifiants d'origine conservés ; étiquettes : 41 ; **345 produits rattachés** (`scripts/build_categories.php`) |
| URL | Alignées sur la prod : `/selle-de-moto/<produit>/` et `/selles-de-moto/marque/<marque>/<modèle>/` (« marque » est une **catégorie parente**, socle `selles-de-moto`) |
| Sélecteur « Ma Moto » | **Fonctionne** : le shortcode `wpd-product-categories` est dans `functions.php` du thème enfant et lit les catégories, qui manquaient |
| Theme Builder | Ré-importé après les catégories (les conditions d'affichage par marque sont rattachées aux termes) |
| Options de commande (APF) | Reconstruites **par produit** depuis le HTML public (méta `_wapf_fieldgroup`, 12 à 19 champs, règles conditionnelles, surcoûts) ; approximation : les groupes globaux d'origine et leurs règles d'application ne sont pas reproduits (`scripts/build_apf_fields.php`) |

Constats de données : la fiche **« Selle TRIUMPH Tiger 900 – Configurable »** (id 17377) affiche des visuels **BMW GS** ; la fiche 16319 (Triumph 900 Tiger 1993-1998) porte les images de la **Yamaha TDM 900**. Des fiches utilisent les images d'un autre modèle.

Pièges : le vidage des règles d'URL doit se faire dans un **second processus** (WooCommerce enregistre les types de contenu avant la mise à jour de l'option) ; les menus de la prod ont des identifiants absents en local (menus et emplacements réaffectés : `relink_menus.php`, `assign_locations.php`).
