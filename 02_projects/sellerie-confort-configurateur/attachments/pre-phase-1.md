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
8. **Point bloquant pour l'export** : savoir où sont stockées les **commandes** (HPOS ou anciennes tables `wp_posts`). Avec le stockage historique, un filtre par table ne suffit pas à les exclure. À lire dans WooCommerce → Réglages → Avancé → Fonctionnalités → « Stockage des données de commande ». **Relevé du 14/10 sur dev** : stockage **hérité** (`wp_posts`), HPOS non activé, bloqué par deux extensions déclarées incompatibles (Custom Order Statuses for WooCommerce, Shipping Method Description), avec des commandes non synchronisées. **Prod à relever** : elle utilise une autre extension de statuts (Tyche 3.0.1), donc le résultat peut différer.
