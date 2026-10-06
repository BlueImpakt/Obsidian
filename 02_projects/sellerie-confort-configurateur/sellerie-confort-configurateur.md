---
tags: [project, encours, sellerie-confort]
created: 2026-10-06
statut: encours
client: sellerie-confort
---

# sellerie-confort-configurateur

## Objectifs du projet
- Simplifier la gestion du **configurateur de selles** de sellerieconfort.com (« usine à gaz » selon la cliente) : ajouter une couleur, une matière ou un modèle ne doit plus imposer de tout reshooter et de tout re-saisir selle par selle, zone par zone
- Mutualiser les matières par famille couleur/matière entre modèles (aujourd'hui rien n'est partagé)
- Alléger l'ergonomie côté client final (listes de choix trop longues)
- Afficher les **logos / broderies choisis directement sur la selle** (suivi d'angle et de relief, ex. dosseret)
- Périmètre Blue Impakt : **design + restructuration de la base du configurateur**. VIMAWEB (maintenance) et ARTEO Conseil (créateur du site) restent en place, contacts à limiter au strict nécessaire

## Livrables
- **Phase 1 — audit technique : 1 600 € HT** (4 j × 400 €, art. 293 B CGI, paiement comptant, déduit de la Phase 2 si suite). Devis I-26-08-1. Rapport de synthèse : compréhension du problème, résultats des tests, estimation de généralisation au catalogue, faisabilité, chiffrage Phase 2 + calendrier
  - 0,6 j audit plugin et stockage · 0,4 j clone local · 1 j tests matières/couleurs · 1 j tests broderies · 0,3 j estimation généralisation · 0,7 j rapport + chiffrage
- **Phase 2** (à chiffrer après Phase 1) : étape 1 patchs IA (optionnelle), étape 2 backend (regroupement par famille), étape 3 frontend/ergonomie, + broderies
- Maquettes HTML de refonte (déjà montrées début août, direction validée, seul le beige à changer) : démonstration uniquement, **pas un engagement contractuel**

## État actuel
- **Pré-signature.** Contrat Phase 1 (projet du 07/08/2026) ni discuté ni signé : dates et durée de 20 jours dépassées, mention des congés caduque → à réécrire avant signature, nouvelle période à fixer avec la cliente
- **Réunion client le 2026-10-07** : convaincre de travailler avec Blue Impakt, fixer la période, obtenir les accès
- Audit externe passif du site réalisé le 2026-10-06 (voir Décisions techniques). Pas d'accès admin, rien testé sur le site
- Aucun accès WordPress, aucun clone local à ce jour

## Décisions techniques
- **Pile détectée** (front uniquement) : WordPress + WooCommerce 11.1.0, thème Divi, LiteSpeed. Configurateur = plugin **Product Configurator for WooCommerce** v1.7.5 (`mkl_pc`), config stockée en fichiers JS dans `wp-content/uploads/mkl_product_configurations/product_configuration_{ID}.js`. Options de commande (gel, chauffage, hauteur) = autre plugin, **Advanced Product Fields** (`wapf`) : deux systèmes distincts
- **Structure des données** : couches d'images PNG 1920×1280 (~350 Ko) superposées, **une image pleine résolution par choix et par selle**, une seule vue. BMW GS LC (produit 19633) : 8 couches, 220 images ; certaines selles 10 couches, 294 images. Les fiches ont été dupliquées puis adaptées (noms de couche copiés d'une autre moto)
- **Volumes** (sitemaps du 2026-10-06) : 27 marques, 448 catégories modèle, 1 520 URL produits dont 345 « configurable » → estimation **76 000 à 100 000 images, 25 à 35 Go** (à valider : les 345 fiches n'ont probablement pas toutes la même structure)
- **Chiffres à ne pas citer** : colonne « Nb produits » du `structure_migration_catalog.xlsx` (35 749, fausse) ; Hyosung en trop (28 marques au lieu de 27) ; Payline/Monext non détecté (le site utilise Alma, Cofidis, DPD)
- **Hors périmètre** : la recommandation Next.js + MedusaJS de `AUDIT_RAPPORT.md` et le plan de migration SEO/redirections 301 ne sont pas l'objectif. Le projet réel restructure le configurateur WooCommerce existant
- **Cadre contractuel** : accès admin WP temporaire, nominatif, révocable ; clone local du site, tous les tests sur le clone, jamais sur la prod ; aucun accès direct à la base ni aux données clients/commandes/paiements ; plugin d'export/clone installé avec accord ; outils payants et API à la charge de Blue Impakt ; propriété des livrables au client après paiement ; résiliation préavis 5 j
- **Pistes IA pour les patchs/broderies** (recherche, **rien testé**) : Mira-Scene (3D depuis image unique) **écarté** (maillages trop approximatifs, pas de retexturage réaliste, lourd en GPU). Retenu à tester : segmentation (SAM / SAM 3) + retexturage 2D avec préservation des ombres et lumières, ou édition générative (FLUX.1 Kontext [pro] meilleur candidat, Nano Banana Pro/2 en face-à-face, GPT Image 2 plan B, Qwen-Image-Edit en local). Outils SaaS de recolor (Photoroom, Claid, GoStudio) : bons pour un prototype, peu contrôlables. Le rendu ne sera jamais identique à 100 % à une photo, l'étape 1 reste optionnelle et ne remplace pas les photos existantes

## Blocages / risques
- Contrat non signé, période de Phase 1 à renégocier ; pas de décompte tant que les accès ne sont pas fournis
- Dépendance aux accès WordPress côté cliente (Valérie Cenizo les a) ; rôle exact de VIMAWEB et ARTEO à clarifier, ainsi que l'auteur du plugin sur-mesure `sc-notice-carbone`
- Hypothèse non vérifiée : homogénéité de structure des 345 fiches configurables
- Acceptabilité côté cliente d'images générées par IA en vente, et critère de validation du réalisme (qui tranche) non définis
- Photos sources (patchs physiques retouchés) : existence de fichiers haute résolution ou PSD hors site inconnue
- Fichiers parasites du repo : `script_scraping_sellerie.py.py` (doublon) ; `index.html` des maquettes contient un extrait de JS affiché tel quel ; prix des maquettes fictifs (250 €, 285 €)

## Next actions
- [ ] Réunion du 2026-10-07 avec Valérie Cenizo : convaincre, fixer la nouvelle période de Phase 1, décider quoi montrer des maquettes
- [ ] Réécrire le contrat Phase 1 (dates, durée de 20 jours, congés) puis faire signer le devis I-26-08-1 à 1 600 € HT
- [ ] Obtenir l'accès WordPress admin temporaire et démarrer le décompte de la période
- [ ] Cloner le site en local (données + médias) et auditer le plugin `mkl_pc` et son stockage (fichiers JS + base)
- [ ] Choisir les modèles/coloris échantillons (BMW GS LC ?) et lancer les tests matières/couleurs puis broderies
- [ ] Estimer la généralisation au catalogue à partir du volume réel (345 fiches configurables à vérifier)
- [ ] Rédiger le rapport de synthèse, chiffrer la Phase 2 et le calendrier

## Journal
- 2026-10-06 : Repo `BlueImpakt/sellerie-confort` cloné en local. Contexte consolidé dans `RAPPORT_CONTEXTE_PROJET.md` : audit externe passif du site (pile, structure du configurateur, volumes) et corrections des incohérences de `AUDIT_RAPPORT.md` et du `.xlsx`. Fiche projet créée, questions pour la réunion du 07/10 listées dans le rapport.

## Liens
- Client : [[sellerie-confort]]
- Patterns utilisés :
- Repo / deployment : https://github.com/BlueImpakt/sellerie-confort (local : `C:\Users\LENOVO\Documents\GitHub\sellerie-confort`) · site client : https://sellerieconfort.com
- Docs clés dans le repo : `sellerieconfort-refonte/RAPPORT_CONTEXTE_PROJET.md` (contexte, mails, questions réunion), `sellerieconfort-refonte/AUDIT_RAPPORT.md`, `Contrat_Phase1_SellerieConfort_BlueImpakt.docx`, `DEVIS-I-26-08-1-SELLERIE-CONFORT-S.A.R.L_.pdf`
