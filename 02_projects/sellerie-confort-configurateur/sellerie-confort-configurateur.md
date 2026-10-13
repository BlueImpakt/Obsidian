---
tags: [project, encours, sellerie-confort]
created: 2026-10-06
statut: encours
client: sellerie-confort
body_synced: 2026-10-13
---

# sellerie-confort-configurateur

## Objectifs du projet
- Simplifier la gestion du **configurateur de selles** de sellerieconfort.com (« usine à gaz » selon la cliente) : ajouter une couleur, une matière ou un modèle ne doit plus imposer de tout reshooter et de tout re-saisir selle par selle, zone par zone
- Mutualiser les matières par famille couleur/matière entre modèles (aujourd'hui rien n'est partagé)
- Alléger l'ergonomie côté client final (listes de choix trop longues)
- Afficher les **logos / broderies choisis directement sur la selle** (suivi d'angle et de relief, ex. dosseret)
- Périmètre Blue Impakt : **design + restructuration de la base du configurateur**. VIMAWEB (maintenance) et ARTEO Conseil (créateur du site) restent en place, contacts à limiter au strict nécessaire

## Livrables
- **Phase 1 — audit technique : 1 400 € HT** (4 j × 350 €, art. 293 B CGI, acompte 50 % (700 €) après signature, solde à la remise du rapport ; déduit de la Phase 2 si suite). Devis I-26-10-1 du 08/10 (I-26-10-2, acompte 50/50, présent à côté ; I-26-08-1 à 1 600 € obsolète). Rapport de synthèse : compréhension du problème, résultats des tests, estimation de généralisation au catalogue, faisabilité, chiffrage Phase 2 + calendrier
  - 0,6 j audit plugin et stockage · 0,4 j clone local · 1 j tests matières/couleurs · 1 j tests broderies · 0,3 j estimation généralisation · 0,7 j rapport + chiffrage
  - **Phase 1 élargie, offerte** (réunion du 07/10) : audit des automatisations (rappels, emailing, bons de commande), suivi statistique du parcours utilisateur, panier perdu (pas de cookies, mail de relance à envisager) ; chiffrage de la refonte complète + maintenance mensuelle inclus
- **Phase 2** (à chiffrer après Phase 1) : étape 1 patchs IA (optionnelle), étape 2 backend (regroupement par famille), étape 3 frontend/ergonomie, + broderies ; fourchette annoncée 4 000 à 7 000 € (viser 5 500 €), à chiffrer en jours réels après l'audit, taux 350 €/j
- Maquettes HTML de refonte (déjà montrées début août, direction validée, seul le beige à changer) : démonstration uniquement, **pas un engagement contractuel** ; refonte complète des 6 maquettes le 07/10, très appréciées, en ligne sur Netlify (08/10)

## État actuel
- **Pré-signature, Phase 1 acceptée oralement.** Réunion du 07/10 tenue (~2 h avec Valérie Cenizo) : besoin confirmé, maquettes très appréciées ; **rien n'est signé**, contrat et démarrage dépendent de l'accord de son mari. Nouvelle offre orale : Phase 1 à 1 400 € HT. CR : [[2026-10-07-sellerie-confort-cr-interne]] · [[2026-10-07-sellerie-confort-cr-client]]
- Contrat Phase 1 réécrit le 13/10 (Word + PDF, 1 400 € HT, acompte 50 %) ; devis I-26-10-1 et I-26-10-2 à aligner avec la référence citée dans le contrat. Mail de CR parti avec un placeholder de créneaux à compléter
- Valérie en congés à partir du 17/10 : contrat signé + accès WordPress admin à obtenir avant, rapport livré pendant ses congés. Concurrence : une agence web les rencontre début novembre
- Audit externe passif du site (06/10, hébergement et DNS le 13/10) : pas d'accès admin, rien testé sur le site, aucun clone local à ce jour. Maquettes en ligne sur Netlify depuis le 08/10

## Décisions techniques
- **Pile détectée** (front uniquement) : WordPress + WooCommerce 11.1.0, thème Divi, LiteSpeed. Configurateur = plugin **Product Configurator for WooCommerce** v1.7.5 (`mkl_pc`), config stockée en fichiers JS dans `wp-content/uploads/mkl_product_configurations/product_configuration_{ID}.js`. Options de commande (gel, chauffage, hauteur) = autre plugin, **Advanced Product Fields** (`wapf`) : deux systèmes distincts
- **Structure des données** : couches d'images PNG 1920×1280 (~350 Ko) superposées, **une image pleine résolution par choix et par selle**, une seule vue. BMW GS LC (produit 19633) : 8 couches, 220 images ; certaines selles 10 couches, 294 images. Les fiches ont été dupliquées puis adaptées (noms de couche copiés d'une autre moto)
- **Volumes** (sitemaps du 2026-10-06) : 27 marques, 448 catégories modèle, 1 520 URL produits dont 345 « configurable » → estimation **76 000 à 100 000 images, 25 à 35 Go** (à valider : les 345 fiches n'ont probablement pas toutes la même structure)
- **Chiffres à ne pas citer** : colonne « Nb produits » du `structure_migration_catalog.xlsx` (35 749, fausse) ; Hyosung en trop (28 marques au lieu de 27) ; Payline/Monext non détecté (le site utilise Alma, Cofidis, DPD)
- **Hors périmètre** : la recommandation Next.js + MedusaJS de `AUDIT_RAPPORT.md` et le plan de migration SEO/redirections 301 ne sont pas l'objectif. Le projet réel restructure le configurateur WooCommerce existant
- **Cadre contractuel** : accès admin WP temporaire, nominatif, révocable ; clone local du site, tous les tests sur le clone, jamais sur la prod ; aucun accès direct à la base ni aux données clients/commandes/paiements ; plugin d'export/clone installé avec accord ; outils payants et API à la charge de Blue Impakt ; propriété des livrables au client après paiement ; résiliation préavis 5 j
- **Décision (2026-10-06) : compositing déterministe en piste principale pour les matières**, IA en renfort. Les masques existent déjà (canal alpha des PNG actuels) ; Python (NumPy, OpenCV, pyvips), texture + ombrage de la photo de base, mesure SSIM/ΔE (`scikit-image`) contre les photos réelles. IA pour les masques de nouveaux modèles (SAM) et le retrait/ajout de logos (LaMa, FLUX Kontext). Matières brillantes/chromées : garder les photos. À valider en Phase 1, rien testé. Variante à chiffrer en Phase 2 : composer côté navigateur au lieu de stocker 83 000 fichiers (remplace le rendu du plugin, beaucoup plus lourd)
- **Décisions de facturation (2026-10-06)** : Phase 2 en **forfait jour chiffré grâce à la Phase 1**, 1 600 € déduits. Clone **sélectif** sans clients ni commandes. Maquettes remontrées comme vision cible, hors Phase 1
- **Contrat Phase 1 mis à jour le 2026-10-06** (Word + PDF dans le repo) : livrable défini, plugin d'export temporaire avec accord écrit, clone sélectif et destruction en fin de phase, nouvel article outils d'IA/services tiers, 4 j de travail sur 20 j calendaires, Phase 2 sur devis, signature datée en blanc. Ajouts du même jour : Phase 2 au **même taux de 400 €/jour**, remboursement des jours non effectués en cas de résiliation après paiement intégral (art. 9), lieu de signature laissé en blanc (réunion au domicile de la cliente). Contrat et devis déplacés dans `sellerieconfort-refonte/` du repo
- **Pistes IA pour les patchs/broderies** (recherche, **rien testé**) : Mira-Scene (3D depuis image unique) **écarté** (maillages trop approximatifs, pas de retexturage réaliste, lourd en GPU). Retenu à tester : segmentation (SAM / SAM 3) + retexturage 2D avec préservation des ombres et lumières, ou édition générative (FLUX.1 Kontext [pro] meilleur candidat, Nano Banana Pro/2 en face-à-face, GPT Image 2 plan B, Qwen-Image-Edit en local). Outils SaaS de recolor (Photoroom, Claid, GoStudio) : bons pour un prototype, peu contrôlables. Le rendu ne sera jamais identique à 100 % à une photo, l'étape 1 reste optionnelle et ne remplace pas les photos existantes
- **Décision (2026-10-07, réunion)** : les étapes 1 et 2 du flux d'ajout d'un modèle (photos sous plusieurs angles, calques Photoshop) restent manuelles chez Valérie ; on automatise l'ajout des matières par calque et le classement par familles. Le nid d'abeille est une broderie : son test est inclus dans les tests broderies de l'audit. Ergonomie : tout sur une seule page, conservé
- **Hébergement (13/10, lecture publique)** : o2switch (LiteSpeed), DNS OVH, mail Google Workspace ; staging probablement faisable chez o2switch. WordPress conservé pour la refonte (moins cher et moins risqué que du from scratch) — hypothèse à confirmer par l'audit

## Blocages / risques
- Contrat non signé : démarrage et signature suspendus à l'accord du mari de Valérie ; pas de décompte tant que les accès ne sont pas fournis ; contrat et accès WordPress admin à obtenir avant ses congés (17/10)
- Dépendance aux accès WordPress côté cliente (Valérie Cenizo les a) ; rôle exact de VIMAWEB et ARTEO à clarifier, ainsi que l'auteur du plugin sur-mesure `sc-notice-carbone`
- Mise en production en Phase 2 : à décider avec la cliente (moi, VIMAWEB ou hybride). Mon engagement du 07/08 de ne pas toucher à la logique technique du site est à reformuler. Voir [[2026-10-07-sellerie-confort]] pour les limites techniques Phase 1/2 et la compatibilité avec le code existant
- Hypothèse d'homogénéité des 345 fiches **levée le 08/10** : 337 fiches sur 345 suivent la même logique (3 jeux réutilisables), 8 atypiques (dont CFMOTO 800 NK)
- Acceptabilité côté cliente d'images générées par IA en vente, et critère de validation du réalisme (qui tranche) non définis
- Photos sources (patchs physiques retouchés) : existence de fichiers haute résolution ou PSD hors site inconnue
- Fichiers parasites du repo : `script_scraping_sellerie.py.py` (doublon) ; `index.html` des maquettes contient un extrait de JS affiché tel quel ; prix des maquettes fictifs (250 €, 285 €)
- **VIMAWEB** détient les licences des plugins (`mkl_pc`, `wapf`, Divi) et a les mêmes accès WordPress que Valérie : elle est d'accord pour les reprendre à son nom ; procédure (transfert éditeur ou rachat) à confirmer plugin par plugin ; Valérie doit l'informer de la collaboration si elle donne suite
- Hébergement o2switch (LiteSpeed), DNS et domaine chez OVH (expire le 17/06/2027), email Google Workspace : titulaires des comptes inconnus, à demander à Valérie avant de contacter VIMAWEB ; accès serveur, version PHP et staging non vérifiables depuis le site public
- Concurrence : une agence web les rencontre début novembre — démarrer vite pour ne pas perdre la place

## Next actions
- [ ] Obtenir avant le 17/10 le contrat Phase 1 signé (devis I-26-10-1, 1 400 € HT) et l'accès WordPress admin ; envoyer à Valérie les 2 créneaux de rattrapage (placeholder resté dans le mail de CR) ; régénérer le devis dans Henrri
- [ ] Obtenir l'accès WordPress admin temporaire et démarrer le décompte de la période
- [ ] Cloner le site en local (données + médias) et auditer le plugin `mkl_pc` et son stockage (fichiers JS + base)
- [ ] Choisir les modèles/coloris échantillons (BMW GS LC ?) et lancer les tests matières/couleurs puis broderies
- [ ] Rédiger le rapport de synthèse, chiffrer la Phase 2 et le calendrier
- [ ] Demander à Valérie qui est titulaire des comptes o2switch, OVH et Google avant de contacter VIMAWEB ; vérifier que le contrat cite bien le devis I-26-10-2
- [ ] Licences des plugins : préparer avec Valérie la reprise à son nom (`mkl_pc`, `wapf`, Divi) si VIMAWEB bloque ; Valérie informe VIMAWEB de la collaboration si elle donne suite
- [ ] Dans l'audit : vérifier ce que permet `mkl_pc` (familles de matières, broderies, options) et cadrer le périmètre de l'audit offert pour tenir dans les 4 jours

## Journal
- 2026-10-06 : Repo `BlueImpakt/sellerie-confort` cloné en local. Contexte consolidé dans `RAPPORT_CONTEXTE_PROJET.md` : audit externe passif du site (pile, structure du configurateur, volumes) et corrections des incohérences de `AUDIT_RAPPORT.md` et du `.xlsx`. Fiche projet créée, questions pour la réunion du 07/10 listées dans le rapport.
- 2026-10-06 (suite) : Audit du configurateur public (fiche BMW GS LC + 45 fiches échantillon + poids de 60 images) : structure homogène (3 gabarits : 220 / 294 / cas particuliers), ≈ 240 images par fiche en moyenne, ≈ 83 000 images ≈ 35 Go ; matières sans identité globale (IDs différents selon la couche) ; broderies = champs de formulaire (plugin `wapf`), logo BMW incrusté dans la photo de fond ; l'hypothèse « fiches hétérogènes » du rapport est levée. Contrat Phase 1 mis à jour. Réunion du 07/10 préparée : [[2026-10-07-sellerie-confort]] + schéma Excalidraw.
- 2026-10-07 : **Refonte complète des 6 maquettes** (`sellerieconfort-refonte/Maquette/`) : accueil, liste des selles (BMW), fiche produit, matières, configurateur, panier. Design commun (thème + en-tête/pied identiques, bleu du logo, fond blanc, Zilla Slab + Archivo, fil de couture), animations Motion 14 en local (hors ligne), vrai logo, données réelles (catalogue 27 marques / 441 modèles / 12 produits, 389 couches du configurateur R6). **Aucun texte inventé** : tout vient des anciens fichiers ou du site réel. **Parcours de démonstration** : accueil → recherche « R6 » → fiche Yamaha R6 → configurateur → panier. **Configurateur testé** : 8 zones personnalisables (249 tests automatiques + 39 tests de clics réels, et vérification manuelle), familles de matières, annuler/refaire, comparer, partage, broderies, options, ajout au panier. Valeurs alignées sur la page réelle de la R6 : réf. YAMAHAR6, « Délai de 1 mois », 225 € (265 € barré), uniquement « Modification ». Lancer : `Maquette/lancer-maquettes.bat`. Originaux rangés dans `Maquette/_originaux/`.
- 2026-10-08 : Analyse du catalogue complet (345 fiches configurables) : 337 sur la même logique (3 jeux réutilisables : 37 matières, 44 liserés, 26 surpiqures), 8 fiches atypiques (dont CFMOTO 800 NK) ; ≈ 2 254 couches, ≈ 83 000 images. Maquettes, contrat et schéma Excalidraw commités/poussés (`fd2fdc7`).
- 2026-10-08 : Maquettes mises en ligne sur Netlify (`https://maquettes-sellerie-confort-bi.netlify.app`, équipe BlueImpakt, public sans mot de passe) car jointes à un mail elles perdent leurs `assets/`. Pages, CSS, JS, Motion, logo, données et images vérifiés. Panneau du configurateur sans barre de défilement en bureau (sous-agent du 07/10 : 76 contrôles, tests 249 et 39 verts) : déjà dans le fichier publié (vérifié le 13/10, seules les réécritures d'URL Netlify diffèrent) ; restent un vide à 1440×900 à l'étape 1 et un défilement masqué mais présent en mobile.
- 2026-10-13 : Après la réunion du 07/10, Valérie OK pour la Phase 1. Contrat réécrit (Word + PDF) : **1 400 € HT (4 j × 350 €)**, devis **I-26-10-1** du 08/10, acompte 50 % (700 €) facturé après signature, solde 50 % à la remise du rapport ; chiffrage de la refonte complète + maintenance mensuelle et audit automatisations/panier/suivi inclus sans supplément ; taux Phase 2 à 350 €. Départ en congés de Valérie le 17/10 : le rapport sera livré pendant ses congés, il faut contrat signé + accès WP avant. Hébergeur identifié par lectures publiques : o2switch (LiteSpeed), DNS chez OVH, mail Google Workspace, domaine expire le 17/06/2027. Analyse WordPress : refonte (thème, plugin configurateur, familles en base) faisable sans quitter WordPress, moins chère et moins risquée que du from scratch ; synthèse ajoutée à la note interne du CR. Mail de CR parti avec un placeholder de créneaux non rempli (rattrapage à envoyer).
- 2026-10-13 (suite) : Notes CR interne/client déplacées dans le dossier refonte (nouvelle référence). Contrat Phase 1 retouché côté Melvin (docx/pdf) et nouveau devis I-26-10-2 (acompte 50/50) présent à côté de I-26-10-1 : référence du devis dans le contrat à vérifier. Titulaires des comptes o2switch/OVH/Google inconnus.
- 2026-10-13 (suite) : Clause de plafonnement Phase 2 ajoutée au contrat (Art. 6) : 7 000 € HT max pour le périmètre défini après l'audit, dépassement de temps à la charge du prestataire, hors périmètre par avenant ; 1 400 € de Phase 1 déduits (solde max 5 600 € HT, 16 j). Si le contrat est déjà signé, avenant nécessaire.

## Liens
- Réunion : [[2026-10-07-sellerie-confort]] (prépa) · CR : [[2026-10-07-sellerie-confort-cr-interne]] · [[2026-10-07-sellerie-confort-cr-client]] · schéma [[sellerie-confort-reunion-2026-10-07.excalidraw]]
- Client : [[sellerie-confort]]
- Patterns utilisés :
- Repo / deployment : https://github.com/BlueImpakt/sellerie-confort (local : `C:\Users\LENOVO\Documents\GitHub\sellerie-confort`) · site client : https://sellerieconfort.com
- Docs clés dans le repo : `sellerieconfort-refonte/RAPPORT_CONTEXTE_PROJET.md` (contexte, mails, questions réunion), `sellerieconfort-refonte/AUDIT_RAPPORT.md`, `Contrat_Phase1_SellerieConfort_BlueImpakt.docx`, `DEVIS-I-26-08-1-SELLERIE-CONFORT-S.A.R.L_.pdf`

