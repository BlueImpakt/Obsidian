---
tags: [sellerie-confort, phase-2]
created: 2026-10-20
client: sellerie-confort
projet: sellerie-confort-configurateur
---

# Préparation de la Phase 2

Ce qu'il faut décider et préparer avant de lancer la Phase 2 : chiffrage, environnements, hébergement, cadre RGPD. Le contexte est dans [[pre-phase-1]], les résultats de l'audit dans [[phase-1]].

Projet : [[sellerie-confort-configurateur]] · Client : [[sellerie-confort]]

## 1. Chiffrage (version du 20/10)

> **Révisé le 04/11** : à la réunion avec VIMAWEB et Valérie, demande d'un configurateur indépendant du plugin et d'APF. Nouveau chiffrage et options au §3. Le tableau ci-dessous reste la base « plugin conservé » (option B du §3).

Taux 350 € HT par jour, TVA non applicable (art. 293 B du CGI). Document Word : `sellerieconfort-refonte/Phase 1/chiffrage-phases-1-2-3-fourchette.docx` (et version à montant fixe `chiffrage-phases-1-2-3.docx`).

### Phase 2 : refonte du configurateur

| Lot | Durée | Détail |
|---|---|---|
| Environnements dev et préprod | 1 j | Copie exacte du site sur l'hébergement, données clients comprises (encadrées par une clause RGPD au contrat), neutralisée : fermée au public, paiements en test, courriels et tâches automatiques coupés. Préprod refaite juste avant la mise en ligne |
| Configurateur en version 2.0.0 | 1,5 j | Mise à jour sur les 345 fiches. Test : commandes passées intactes, retour arrière possible |
| Données du catalogue | 3 j | Les 345 fiches regroupées en 46 configurations, noms corrigés, familles validées avec Valérie. Test : chaque fiche affiche les mêmes choix qu'avant |
| Configurateur intégré, fiche produit, panier | 3 j | Nouvelle interface sur toutes les fiches configurables, nouvelle fiche produit, panier récapitulatif. Test : prix et panier corrects sur chaque modèle |
| Design | 1 j | Finitions ordinateur et mobile. Test sur les modèles les plus différents |
| Broderies et nid d'abeille | 3 j | Logos et 26 couleurs de fil sur tous les modèles concernés, nid d'abeille facultatif. Test : logo bien placé et bonne couleur dans la commande |
| Écran de gestion des matières | 2,5 j | Ajout, retrait et classement des matières par Valérie, répercutés sur tout le catalogue. Formation |
| Recette en préprod et mise en production | 2,5 j | Contrôle automatique des 345 fiches, commandes test (Payline, Alma, Cofidis, échange standard) vérifiées par Valérie. Mise en production avec retour arrière |
| **Total** | **17,5 j** | **6 125 € HT** à payer (Phase 1 déduite) |

Plafond contractuel : 7 000 € HT avec la Phase 1, soit 16 j de Phase 2. Avec l'écran de gestion, dépassement de 1,5 j ; sans lui, 15 j (5 250 € HT). Au-dessus du plafond, on resserre le périmètre (écran de gestion ou nid d'abeille en option), on n'absorbe pas.

### Phase 3 : refonte complète du site (configurateur fait en Phase 2)

| Lot | Durée | Détail |
|---|---|---|
| Thème sur mesure à la place de Divi | 3 à 3,5 j | Système de design, modèles de pages, listes de produits. Test : rendu identique sur ordinateur et mobile |
| Marques, modèles, recherche « Ma moto » | 3 à 3,5 j | 27 marques, 448 modèles, sélecteur « Ma moto » réécrit. Test : chaque moto mène aux bonnes selles |
| Pages de contenu | 2,5 à 3 j | Accueil, Matières et couleurs, FAQ, livraison et échange standard, contact, mentions légales |
| Panier, paiement, livraison | 2 à 2,5 j | Alma, Cofidis, Payline, DPD sur le nouveau thème. Test : une commande par moyen de paiement |
| Compte client, courriels, factures | 1,5 à 2 j | Espace client, gabarits des courriels de commande, factures PDF |
| Automatisations | 3 à 3,5 j | Fiche d'habillage, courriel « En fabrication », relances de configuration et de panier, écran « Échanges standard » et relances caution, demande d'avis. Test : chaque courriel et chaque relance sur commandes test |
| SEO, vitesse, accessibilité, RGPD | 2 j | Redirections 301, réglage du cache, politique de confidentialité, cookies. Test : aucune page perdue dans Google |
| Recette, migration, mise en production | 3 j | Tests complets en préprod, bascule, prise en main par Valérie |
| **Total** | **20 à 23 j** | **7 000 à 8 050 € HT** |

Réserve interne : ces montants sont au-dessous de l'estimation détaillée (Phase 3 : 29 à 46 j ; automatisations seules : 6 à 8,5 j, voir [[phase-1]] §25). Périmètre à tenir serré, surtout « Ma moto » et automatisations.

## 2. Environnements, mise en production, hébergement, RGPD

Déplacé de [[phase-1]] §23 le 20/10 (rédigé le 17/10).

### Copie locale complète ou préprod ?
- **Une copie locale complète** (toutes les extensions et réglages de la prod) couvre environ 80 % des risques : conflits d'extensions et de scripts, test des 345 fiches, commande jusqu'à sa création, affichage dans l'admin, mises à jour du plugin. Elle ne couvre pas : cache LiteSpeed, retour du paiement Payline (adresse locale non joignable), courriels, vitesse réelle.
  - Conditions : **export anonymisé** (sans clients, commandes ni clés de paiement, art. 2 du contrat) avec l'accord écrit de Valérie ; ne pas faire tourner l'extension signalée comme compromise.
- **Une préprod n'est pas obligatoirement chez le même hébergeur**, mais c'est le plus fiable : les risques restants viennent du serveur (LiteSpeed, PHP, pare-feu o2switch, courriels, paiement). Sur o2switch, une copie sur sous-domaine ne coûte presque rien ; l'hébergement est géré par VIMAWEB, donc à passer par Valérie.
- Ordre proposé : copie locale complète anonymisée d'abord, puis courte vérification en préprod (cache, paiement test, courriels).

### Dev, préprod, prod
- **Même chose côté serveur** (une copie du site sur un sous-domaine), **usage différent** : la **dev** sert à développer et peut s'éloigner de la prod ; la **préprod** est une copie **fraîche et fidèle** de la prod, refaite juste avant le test final. Une dev peut servir de préprod si on la recopie depuis la prod juste avant.
- **Plusieurs copies possibles** : l'offre o2switch permet a priori plusieurs sites et sous-domaines sur le même hébergement (dans la limite de l'espace disque) : à confirmer avec VIMAWEB.
- **Le site dev existant du client** : contenu et date de dernière copie inconnus (pas d'accès sans autorisation de Melvin) ; à demander à VIMAWEB. S'il peut être rafraîchi depuis la prod, il sert de préprod.
- Cible : **une dev à jour** pour travailler, **une préprod** pour le dernier test, puis **la prod**.

### Le passage d'un environnement à l'autre
**Règle** : **le code monte** (dev → préprod → prod : notre extension, fichiers, versions d'extensions) ; **les données descendent** (prod → préprod → dev : commandes, clients, produits, stocks). **Jamais la base de dev ou de préprod vers la prod** : elle effacerait les commandes et clients arrivés entre-temps.

**Dev → préprod**
1. Recréer la préprod comme copie fraîche de la prod (sous-domaine o2switch), fermée à Google et aux visiteurs, paiement en mode test, courriels bloqués.
2. Y appliquer la livraison **exactement comme on le fera en prod** : dépôt du code (mu-plugin, versionné dans git), puis scripts qui modifient des données (ex. calques de broderie, champs APF).
3. Tester : catalogue complet automatisé, commande test, validation de Valérie dans l'admin.
La préprod est la **répétition générale** de la mise en prod.

**Préprod → prod**
1. Sauvegarde complète de la prod (fichiers et base), à une heure creuse.
2. Même paquet de code, mêmes scripts qu'en préprod.
3. Vider le cache LiteSpeed.
4. Vérifier quelques fiches et une commande, puis surveiller.
5. **Retour arrière** : désactiver l'extension, ou l'interface fiche par fiche. Pas de restauration de la base (on perdrait les commandes passées depuis).

**Point délicat** : une partie de la configuration vit dans la base (calques du configurateur, champs APF, réglages) et ne « monte » pas avec le code. Elle se rejoue en prod par script (comme nos scripts d'import) ou à la main dans l'admin : tout changement de données passe donc par un script testé en préprod.

**Outils o2switch** : cPanel propose en général un outil de clonage (WP Toolkit ou Softaculous selon l'installation) et le déploiement git. Attention, « pousser vers le site en ligne » peut écraser la base : à n'utiliser que pour les fichiers. À confirmer avec VIMAWEB.

**Atout de notre approche** : l'interface tient dans une extension et s'active produit par produit ; mise en prod = déposer des fichiers et cocher des fiches ; retour arrière immédiat.

### Hébergement : piste « reprendre o2switch au nom de Valérie » (17/10, à valider avec Valérie et VIMAWEB)
**Problème** : sur l'hébergement de VIMAWEB, tout le chantier de la Phase 2 (dev, préprod) leur est visible. Moyens :
- WP Umbrella (journal d'activité, sur prod et dev) ;
- journaux d'accès o2switch ;
- connexions WordPress ;
- e-mail de création de compte ;
- `WP_DEBUG_LOG` actif sur dev.

**Ce qu'on sait** :
- Le dev a été créé avec **WP Tiger**, dans le dossier `myTiger-Preprod` du **compte cPanel `sellerieconfort`** : prod et dev vivent donc très probablement dans **un même compte o2switch, dédié au site**.
- Les deux adresses IP différentes (prod `109.234.165.168`, dev `109.234.165.38`) passent toutes deux par le frontal « PowerBoost » d'o2switch : elles ne prouvent pas deux serveurs.

**Piste** : avec l'accord de VIMAWEB, transférer ce compte à Valérie, qui devient titulaire et payeuse.
- **Cas 1, compte dédié (le plus probable)** : changement de titulaire par le support o2switch (le client n'a pas accès aux outils d'administration du serveur) ; procédure officielle non trouvée, à confirmer avec eux. Avantage majeur : **rien ne bouge** (même serveur, même IP, cache LiteSpeed, aucune migration, aucune coupure).
- **Cas 2, site logé dans un compte d'agence de VIMAWEB** : pas de cession possible. Valérie ouvre son abonnement o2switch, migration du site (o2switch aide gratuitement aux migrations entrantes), puis changement d'adresse IP dans le DNS, que Valérie contrôle déjà chez OVH.

**À régler dans les deux cas** :
- licences des plugins payants au nom de VIMAWEB (Divi, SEOPress Pro, configurateur…), à transférer ou racheter ;
- WP Umbrella à retirer, sauf si Valérie garde leur maintenance ;
- changement de tous les codes (cPanel, FTP, base, administrateurs), à l'occasion du traitement du plugin signalé comme compromis ;
- sort de dev et préprod.

**Intérêt** : Valérie titulaire peut créer un accès à Melvin et une préprod sur sous-domaine. VIMAWEB ne voit plus le chantier, sauf s'il reste en maintenance.

**Alternatives** :
- **Local + préprod sur un hébergement contrôlé par Melvin**, livraison en paquet (git, extension, scripts) : rien de visible avant la mise en production.
- **OVH au nom de Valérie** : elle y a déjà domaines, DNS, boîtes mail, l'ancien hébergement (PHP 7.2, à éteindre après migration des boîtes) et un plan « Performance » `sellerz` peut-être inutilisé. Cela implique une migration et des tests de performance (pas de cache LiteSpeed). Renouvellement OVH en avril 2027.
- **Recommandation** : si VIMAWEB accepte et que c'est le cas 1, reprendre o2switch est le plus simple et le moins risqué.

**Question à poser** (par Valérie, à VIMAWEB ou à o2switch) : « Le compte cPanel `sellerieconfort` est-il un abonnement dédié, et peut-on en transférer la titularité à Sellerie Confort ? »

### Environnement de dev de la Phase 2 : données clients, RGPD, neutralisation (décision de Melvin, 17/10)
**Retenu** : cadrer la RGPD dans le contrat de Phase 2, puis travailler sur une **copie exacte de la prod, en ligne sur o2switch** (préproduction WP Tiger), **neutralisée** à l'installation. C'est plus simple qu'une copie pseudonymisée.

**1. Cadrer la RGPD dans le contrat de Phase 2**
- Le contrat de Phase 1 (art. 2) interdit de consulter clients, commandes et paiements : la Phase 2 doit l'autoriser explicitement.
- Clause de **sous-traitance (art. 28 RGPD)** : Valérie responsable du traitement, Melvin (Blue Impakt) sous-traitant. À y fixer :
  - finalité (développement, tests, maintenance) ;
  - catégories de données (clients, commandes, comptes) ;
  - lieu de stockage et durée ;
  - mesures de sécurité ;
  - pas de sous-traitance ultérieure sans accord ;
  - suppression en fin de mission ;
  - alerte en cas de fuite.
- **Justifier l'usage de données réelles** (principe de minimisation, art. 5) : diagnostic de commandes réelles, tests sur l'historique des commandes (structure, champs, mise à jour du configurateur).
- **Vocabulaire** : une copie dont on remplace noms et e-mails mais garde les commandes est **pseudonymisée**, pas anonymisée : elle reste une donnée personnelle (art. 4). La pseudonymisation n'est plus nécessaire avec la clause ; elle reste une option pour une copie hors serveur.

**2. Dev en ligne sur o2switch, pas en local**
- **Pourquoi** : le local actuel est limité, mais pas par l'absence de données clients. Il est reconstruit à partir des pages publiques, n'a que 4 extensions actives sur 34 (sans LiteSpeed, CleanTalk, Payline, Alma, Cofidis, Complianz…) et n'a pas d'adresse publique (pas de retour bancaire, pas d'e-mails).
- **Données réelles nécessaires** pour très peu de tests : diagnostic d'une commande précise, et vérification finale en prod. Tout le reste (configurateur, catalogue, panier, commandes, paiements en mode test, e-mails, factures, historique, statistiques) se fait sans.
- **Mise en place** : VIMAWEB crée ou rafraîchit une préproduction avec **WP Tiger** (copie complète des fichiers et de la base, dans un sous-dossier ou sous-domaine du compte o2switch, comme le dev actuel `myTiger-Preprod`, aujourd'hui figé vers juin et en retard de versions).
  - WP Tiger copie tout, données clients comprises, sans option de pseudonymisation documentée (non vérifié dans la doc officielle).
  - **Ne jamais « pousser » la préprod vers la prod** : cela écraserait les commandes arrivées entre-temps.
- **Copie à garder sur l'hébergement plutôt que sur le poste de Melvin** : les données ne quittent pas le serveur. En local, il faudrait un disque chiffré, aucune copie ailleurs et la suppression en fin de mission (2 890 clients).
- **Visibilité** : la préprod WP Tiger est dans le compte de VIMAWEB, donc visible pour eux. Elle ne devient privée qu'avec la reprise du compte au nom de Valérie (sous-section précédente).

**3. Neutralisation de la copie : obligatoire, contrat ou pas**
Une copie exacte garde les clés de paiement de production, les vrais e-mails clients et les tâches planifiées. Sans neutralisation, le dev peut écrire aux clients, encaisser ou rembourser, et renseigner WP Umbrella. Un script, lancé une fois à chaque copie :
- coupure des e-mails sortants (ou redirection vers une adresse de test), y compris WP Mail SMTP ;
- moyens de paiement en mode test (Payline, Alma, Cofidis), clés de production retirées ;
- tâches planifiées et Action Scheduler désactivées (relances, synchronisations, exports) ;
- WP Umbrella désactivé ;
- site fermé aux moteurs et aux visiteurs (mot de passe, `noindex`) ;
- plugin signalé comme compromis non exécuté, et recherche du fichier `wp-comments-posts.php` dans la copie.

**À préparer par Melvin** : la clause RGPD de sous-traitance, le script de neutralisation, et la demande à VIMAWEB (envoyée par Valérie).

## 3. Configurateur indépendant (réunion VIMAWEB et Valérie du 04/11)

### Ce qui a été demandé
- Réunion à trois le 04/11 : a priori, pas de problème pour travailler avec VIMAWEB (la reprise de la maintenance, voir [[reprise-maintenance]], est donc à reconsidérer).
- VIMAWEB souhaite un **configurateur développé hors du plugin Product Configurator for WooCommerce (Marc Lacroix, « mklacroix »)**, y compris hors de la 2.0.0, pour ne pas risquer de casse liée au plugin.
- Décision de Melvin : **APF (Advanced Product Fields) est retiré aussi**, pour le même objectif d'indépendance.
- Plus de travail, mais plus de liberté.

### Ce qui dépend aujourd'hui du plugin et d'APF (relu dans `maquette-branchee/sc-maquette`)
- **Déjà indépendant** : l'interface (rendu des calques, étapes, récapitulatif, partage par lien).
- **Plugin** : données lues par `mkl_pc('db')->get('layers'|'content')` ; ajout au panier par un « pont » qui recopie la configuration dans le formulaire caché du plugin puis clique son bouton ; panier, commande, image de la configuration ; éditeur d'administration des calques utilisé par Valérie. L'écran de gestion (`sc-gestion-configurateur`) s'appuie sur le filtre interne `mkl_pc/db/get` et écrit dans `_mkl_product_configurator_content`.
- **APF** : toutes les options et informations de commande (hauteur, gel, chauffage, type de commande, options supplémentaires, champs de broderie, informations pilote), avec prix et conditions, par groupe de champs `_wapf_fieldgroup` sur chaque fiche. L'**étiquette de production** (code VIMAWEB) lit les champs APF.

### Chiffrage d'un configurateur indépendant (plugin et APF retirés)

| Lot | Durée | Détail |
|---|---|---|
| Environnements dev et préprod | 1 j | Inchangé |
| Modèle de données et migration | 3 à 4 j | Remplace « passage en 2.0.0 » et « données du catalogue » : les 46 configurations dans nos données WordPress (post_meta), les 345 fiches rattachées, images existantes réutilisées sans doublon |
| Configurateur branché sur nos données | 2 à 2,5 j | Le prototype, branché sur nos données au lieu du plugin |
| Panier et commande | 3,5 à 4,5 j | Nouveau : ajout au panier, contrôle des choix et du prix côté serveur, panier, commande, courriels, factures PDF, étiquette et fiche d'habillage, image de la configuration, affichage des anciennes commandes faites avec le plugin |
| Options (remplace APF) | 1,5 à 2 j | Options dans nos données (prix, conditions par modèle), migration des groupes de champs APF des 345 fiches |
| Fiche produit et design | 1,5 à 2 j | Inchangé ou presque |
| Broderies et nid d'abeille | 3 j | Inchangé |
| Écran de gestion devenu l'éditeur complet | 5 à 6,5 j | Matières, plus création d'une configuration, de ses calques, de ses angles et dépôt des images par choix (l'éditeur du plugin disparaît), plus gestion des options |
| Adaptations liées au retrait d'APF | 1 j | Panier, commande, courriels, factures et étiquette de production (code VIMAWEB) |
| Recette et mise en production | 3,5 à 4 j | Plus de parcours à tester, retrait du plugin et d'APF, vérification du code VIMAWEB qui en dépend |
| **Total** | **25 à 30,5 j** | **8 750 à 10 675 € HT**, plus 200 € HT d'outils (au lieu de 17,5 j et 6 125 € HT) |

- Plugin seul retiré, APF conservé : 21 à 25,5 j (7 350 à 8 925 € HT).
- Les commandes passées gardent les valeurs APF en texte : lisibles sans APF. Celles du plugin demandent un affichage de compatibilité.
- **Ce qui peut faire monter l'estimation** : des modules payants du plugin utilisés (prix par choix, conditions entre choix, plusieurs vues) à refaire. Inventaire des fonctions réellement utilisées à faire sur la copie locale pour resserrer la fourchette.
- Calendrier : livraison qui glisse vers janvier.

### Failles connues du plugin
- **CVE-2025-54674** : faille de type CSRF, gravité moyenne, versions jusqu'à 1.4.4 ([GitHub Advisory](https://github.com/advisories/GHSA-fpvv-xmjr-h8hp)).
- **CVE-2026-105872** : injection d'objet PHP, gravité haute, versions jusqu'à 1.7.5, publiée le 09/10/2026, **corrigée en 1.7.6** ([HOL Guard](https://hol.org/guard/security/cves/CVE-2026-105872-wordpress-product-configurator-for-woocommerce)).
- **La prod est en 1.7.6 : les deux sont corrigées.** Aucune faille ouverte connue à ce jour.

### Le risque de casse : réel ou prétexte ?
- **Fondé en partie** : l'approche « plugin conservé » se branche sur un mécanisme interne du plugin (filtre `mkl_pc/db/get`, format de données), qu'une mise à jour majeure peut casser (la 2.0.0 a beaucoup changé) ; plugin maintenu par un seul développeur ; faille sérieuse corrigée en octobre 2026 ; et c'est VIMAWEB qui applique les mises à jour, donc qui serait mis en cause. Vouloir une frontière nette les protège, c'est légitime.
- **Exagéré** : avec une préprod où les mises à jour sont testées, le risque est faible ; la plupart des boutiques WooCommerce tournent sur des extensions tierces ; ils gardent Divi et des dizaines d'extensions, l'exigence ne vise que le périmètre de Melvin.
- **Effet réel** : tout le risque et 40 à 75 % de travail en plus passent sur Melvin. Accepté au même prix, c'est là qu'il serait en difficulté.

### Options à présenter à Valérie
- **Option A, configurateur indépendant** (recommandée si le budget suit) : 25 à 30,5 j par avenant (changement de périmètre demandé le 04/11). Conditions :
  1. nouveau chiffrage validé par Valérie ;
  2. frontière écrite : configurateur et options = Blue Impakt, le reste = VIMAWEB, origine d'un incident établie par le journal des modifications et les empreintes des fichiers (protège aussi Melvin des effets de leurs mises à jour) ;
  3. calendrier ajusté ;
  4. garantie de 6 mois sur tout le configurateur, prise en compte dans le prix.
- **Option B, plugin conservé avec périmètre élargi** (si le surcoût est refusé) : plugin 2.0.0 et APF gardés, mais **dans le périmètre de Melvin** : VIMAWEB ne les met plus à jour, Melvin le fait après test en préprod. Le risque de casse lié aux mises à jour disparaît sans réécrire le configurateur. Chiffrage du §1 (17,5 j).

**Prochaines étapes** : inventaire des fonctions du plugin utilisées (pour resserrer la fourchette de l'option A) ; rédaction des deux options pour Valérie.

### Résultat de l'essai (04/11/2026)

Essai sur la copie locale, 5 fiches (Duke, Z 900, Africa Twin 1100, BMW F 900 XR nid d'abeille, Z 1000 SX), plugin et APF coupés. Compte rendu complet : `sellerieconfort-refonte/Phase 2/essai-independant/compte-rendu.md` (branche `essai-configurateur-independant`), journal du temps et captures dans le même dossier.

- **Possible** : configuration, panier, commande, administration, courriel, facture PDF et étiquette VIMAWEB fonctionnent sans le plugin ni APF, sans toucher au code de VIMAWEB. Prix identiques au site actuel (10/10). Attaques refusées. Prototype intact sans le cookie. Deux réserves pour la version complète (remède simple, à faire et tester) : anciennes commandes et paniers en cours qui contiennent des objets du plugin (erreur fatale possible une fois le plugin retiré) ; motif de broderie APF faux sur la Duke (le premier choix est imposé, défaut repris du prototype).
- **Temps mesuré** : ≈ 3 h 25 de construction par agents IA (4 h 22 d'horloge avec les relectures). Pas converti en jours : les rapports mesuré / papier (de moins de 1 % à 5 % selon les lots) montrent que l'écriture du code n'est pas le poste lourd. Le reste à faire est chiffré lot par lot ; recette, validations avec Valérie et intégration ne sont pas compressées.

| Lot | Papier | Révisé | Pourquoi |
|---|---|---|---|
| Environnements dev et préprod | 1 j | 1 j | Inchangé (essai en local seulement) |
| Modèle de données et migration | 3 à 4 j | 2 à 3 j | Format compatible, migration exacte sur 5 fiches ; reste le regroupement en 46 configurations partagées (non testé) et sa validation |
| Configurateur branché sur nos données | 2 à 2,5 j | 1 à 1,5 j | Front identique au prototype du premier coup ; reste le contrôle des 345 fiches et le branchement de la fiche produit (`fiche.php`, `?sc_fiche`) sur nos données (la fiche elle-même est au lot « Fiche produit et design ») |
| Panier et commande | 3,5 à 4,5 j | 2 à 3 j | Fait et testé sur 5 fiches ; restent anciennes commandes du plugin (objets du plugin stockés dans les lignes : classes de compatibilité ou migration des meta), paniers et sessions à la bascule, paiements réels, fiche d'habillage |
| Options (remplace APF) | 1,5 à 2 j | 1 à 1,5 j | Règles et prix validés ; reste la migration des 345 fiches et les chemins de prix non comparés |
| Fiche produit et design | 1,5 à 2 j | 1,5 à 2 j | Hors essai |
| Broderies et nid d'abeille | 3 j | 3 à 3,5 j | Hors essai (nid d'abeille généré) ; en plus, correspondance logo du calque ↔ motif APF sur toutes les configurations (fausse sur la Duke) et calques de broderie absents (BMW 32182) |
| Écran de gestion devenu l'éditeur complet | 5 à 6,5 j | 3,5 à 4,5 j | Éditeur, options et matières faits en version dépouillée ; pas d'angles à faire (un seul partout) ; restent création d'une configuration, ajout d'une matière, écrans finis, formation |
| Adaptations liées au retrait d'APF | 1 j | 0,5 j | Étiquette et factures compatibles sans changement ; reste l'inventaire du code VIMAWEB |
| Recette et mise en production | 3,5 à 4 j | 3,5 à 4 j | Inchangé : dépend de Valérie, des paiements réels et de la bascule en prod |
| Appropriation du code de l'essai (nouveau) | — | 1 à 1,5 j | Code écrit par des agents (≈ 5 300 lignes et ≈ 3 900 lignes de tests) : lecture et appropriation par Melvin, qui le garantit 6 mois |
| **Total** | **25 à 30,5 j** | **20 à 26 j** | **7 000 à 9 100 € HT** (+ 200 € HT d'outils), au lieu de 8 750 à 10 675 € HT |

- Écart avec l'option B (17,5 j) : 2,5 à 8,5 j (875 à 2 975 € HT). Plafond de 16 j dépassé dans tous les cas.
- Défauts existants trouvés en route (thème VIMAWEB `functions.php:912`, factures PDF qui décodent les entités, BMW 32182 impossible à mettre au panier par le prototype, donnée APF de la Z 1000 SX, erreur fatale de `sc-relance` avec un panier du plugin, motif de broderie imposé sur la Duke, broderie non dessinée sur la BMW 32182) : compte rendu §6.
