---
tags: [sellerie-confort, phase-1]
created: 2026-10-15
client: sellerie-confort
projet: sellerie-confort-configurateur
---

# Phase 1 : audit technique

Suivi de la Phase 1 poste par poste, d'après le devis I-26-10-2 signé. Ce qu'on savait avant de commencer est dans [[pre-phase-1]].

Projet : [[sellerie-confort-configurateur]] · Client : [[sellerie-confort]]

**Cadre** : 1 400 € HT = 4 j × 350 €, délai de 10 jours calendaires du 14/10 au **24/10/2026**. Solde de 700 € à la remise du rapport.

## 1. Les 6 postes du devis (4,00 j)

| #   | Poste                                                                 | j    | Livrable attendu                                                              | État au 15/10                                                                                                                                                                                                                                                                                                                                                                                             |
| --- | --------------------------------------------------------------------- | ---- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Audit du fonctionnement actuel et de la structure de données          | 1,00 | Fonctionnement de `mkl_pc`, stockage, faisabilité du regroupement par famille | **Fait pour le regroupement (15/10)** : lot et famille testés sur la 1.7.6, voir §7. Lecture de `payment.php` et `active-plugins.php` faite (§8). Fichier public régénéré, 9 fiches atypiques listées, conclusion en fin de §10 (« Compléments poste 1 »). **Poste 1 clos** ; reste le test de la 2.0.0, optionnel (paquet non disponible, voir §7).                                                      |
| 2   | Clone local complet (données et médias), isolé de la production       | 0,40 | Site local isolé, sans donnée personnelle                                     | **Fait** : 345 produits, 15 121 médias, Divi, catégories, « Ma Moto », options APF. Reste cosmétique (3 médias en erreur, menus du pied de page).                                                                                                                                                                                                                                                         |
| 3   | Tests de rendu matières/couleurs, comparés aux photos réelles         | 0,60 | Comparaison au rendu réel (SSIM/ΔE) sur un échantillon                        | **Fait (15/10)** : générateur couleur + texture, validé sur 5 modèles, voir §6. Couleur : faisable (ΔE ≈ 2,5). Matières unies : rendu correct. **Matières texturées : la recette de Valérie est retrouvée** (texture maître 1920 × 1280 par matière, découpée par le masque de chaque zone) ; régénération à l'aveugle exacte au pixel pour une partie des matières, voir §10. Surpiqûres = couleur unie. |
| 4   | Tests broderies / logos / nid d'abeille                               | 1,00 | Verdict de faisabilité chiffré par type de broderie                           | **En cours.** Nid d'abeille : le calque se pose sur sa photo d'origine, le transfert vers le rendu du configurateur n'est pas résolu. Logos : aucun essai consigné ; cas d'usage identifié, retirer le logo incrusté dans la photo de fond d'une forme de selle réutilisée (Tiger 900 avec GS) ou en poser un autre.                                                                                      |
| 5   | Estimation du temps de généralisation au catalogue                    | 0,30 | Temps pour passer de l'échantillon aux 46 configurations                      | **Données prêtes** (46 configurations, 302 couches distinctes, ≈ 10 900 images). Poste 3 et regroupement faits (§6, §7) ; dépend encore du poste 4.                                                                                                                                                                                                                                                       |
| 6   | Rapport de synthèse, chiffrage Phase 2, plan d'action avec calendrier | 0,70 | Rapport remis à Valérie                                                       | **Charpente existante** (Phase 2 : 14 à 24 j, plafond 16 j). À finaliser en dernier.                                                                                                                                                                                                                                                                                                                      |

## 2. Offert dans la Phase 1

| Volet | Livrable attendu | État au 15/10 |
|---|---|---|
| Audit des tâches manuelles automatisables | Liste des tâches avec temps et coût estimés (rappels, emailing, bons de commande) | **En cours (17/10), voir §25** : fiche d'habillage (bouton « Habillage », maquette A4) et courriel « En fabrication » au clic sur l'étiquette retenus ; courriels après commande déjà en place, note de suivi DPD automatique (vérifié dans le code). Source : CR de la réunion du 07/10. |
| Diagnostic de la perte de panier | Diagnostic avec préconisation (cookies, sauvegarde de session) | **Fait le 17/10, sans accès prod ni dev** : `Phase 1/diagnostic-panier-perdu.md`. **Causes confirmées dans le code :**<br>1. **Payline** renvoie vers « Commande reçue » avant la banque, et WooCommerce y vide le panier : tout paiement abandonné, annulé ou refusé laisse un panier vide.<br>2. **Cofidis** renomme la session du client avant sa redirection.<br>3. Panier sans compte gardé **2 jours** seulement.<br>**Écartés** : Alma, Complianz, `payment.php`, script du thème. **Préconisations** : ne pas vider le panier avant paiement, restaurer au retour de la banque, sessions de 30 jours, relance e-mail, lien de sauvegarde de configuration (refonte). |
| État des lieux du suivi statistique | État des lieux avec outil de parcours utilisateur recommandé | **Pas commencé.** |
| Chiffrage de la refonte complète et d'une maintenance mensuelle | Fourchette de jours et de coût | **Charpente faite** (Phase 3 : 26 à 43 j). Maintenance à chiffrer à part. |

## 3. Les regroupements envisagés (étape 2)

Une **configuration** = tout le contenu du configurateur d'une fiche : la liste des calques (zones : Bec, Assises, Liserés…), pour chaque calque la liste de ses choix (nom, ordre, image par angle, vignette, choix par défaut) et les angles. Elle est stockée **une fois par produit**, en copie indépendante. Aujourd'hui : 345 fiches, 345 copies, dont 46 distinctes.

| # | Regroupement | Aujourd'hui | Cible |
|---|---|---|---|
| A | **Jeux de choix partagés** | Chaque calque de chaque fiche porte sa propre copie de la liste (noms, ordre, vignettes) | 3 jeux définis une fois : 37 matières, 26 surpiqûres, 44 liserés. Chaque calque est rattaché à un jeu selon son type. |
| B | **Familles de matières** | Liste plate de 37, 26 ou 44 entrées | Familles de la page « Matières et couleurs » du site, reprises : **Noirs (9), Gris (8), Bleus (7), Rouges (5), Orangés / Jaunes (7), Verts (4), Autres couleurs (6)**. À valider avec Valérie. |
| C | **Configurations identiques** | 345 fiches, chacune avec sa copie | **46 configurations** à maintenir (dont une partagée par 117 fiches), 17 produits isolés. Une modification faite une fois s'applique à toutes les fiches du groupe. |
| D | **Nettoyage préalable** | 5 gabarits de noms de calques, 27 jeux de noms au lieu de 3, 34 calques atypiques (dont CFMOTO 800 NK), la faute « gris tonnerrre » dans 57 calques | Un nom par zone, un jeu de noms par type. Condition de A et C. |
| E | **Images** | Déjà réutilisées : 66 % des images sont partagées, jusqu'à 117 fiches pour une même image | Les fichiers ne bougent pas. Seule la configuration qui les référence change. |

**Constat du 15/10 sur B** : les galeries de la page « Matières » utilisent les **mêmes images de patch** que les vignettes du configurateur (mêmes identifiants de médiathèque, par exemple 690 et 693). Sur la Z900 (export du produit 39477), les 37 matières et les 44 liserés sont tous dans les familles de la page, et 24 surpiqûres sur 26. Le rattachement des familles aux choix se fait donc par l'identifiant de la vignette, sans saisie. À confirmer sur les 345 fiches.

**Réutilisation volontaire de formes de selle** (précisé par Melvin le 15/10) : une fiche qui reprend les visuels d'un autre modèle (Tiger 900 avec GS) n'est pas une erreur de copie. La forme de selle est la bonne, la configuration a été réutilisée pour ne pas créer un nouveau modèle de selle. Le seul défaut est le **logo d'origine incrusté dans la photo de fond**. C'est un cas d'usage direct des tests logos du poste 4 : retirer le logo, ou en poser un autre. Conséquence de conception : le logo doit être un calque séparé de la photo de fond.

**Limite** : l'appartenance à un groupe de C reste à vérifier modèle par modèle (même forme de selle, logo mis à part).

## 4. Gestion par Valérie : avant / après

| | Aujourd'hui | Cible |
|---|---|---|
| Ajouter une matière | Une image par calque de chaque modèle, saisie une par une dans l'éditeur du plugin, facturée par VIMAWEB | Déclarée une fois dans un écran « Matières » (patch, nom, famille, ordre, actif) |
| Retirer ou désactiver une matière | Passe par VIMAWEB (outil de purge) | Un geste, répercuté partout |
| Ajouter un modèle (≈ 1 semaine) | Calques importés, puis chaque matière ajoutée à la main sur chaque calque | Calques déposés en lot, type par calque, matières rattachées seules (par nom de fichier), aperçu, publication |
| Retrouver un fichier | Médiathèque WordPress, dossiers et catégories mal rangés | Nom de fichier normalisé `Selle-{Marque}-{Modèle}-{zone}_{NN}_{Matière}.png`. Le rattachement se fait par le nom : le rangement dans la médiathèque ne conditionne plus rien. |
| Photos et Photoshop | Manuel chez elle | Inchangé |

**Limite** : le regroupement supprime la saisie, pas la production des images. L'image d'une matière sur un calque reste propre à la découpe du modèle. Pour qu'« ajouter une couleur » devienne simple, il faut le rattachement par nom de fichier ou la génération des images (étape 1, testée au poste 3).

## 5. Flux de production d'une fiche et ce qu'on en sait

| Étape | Qui / où | État de nos connaissances |
|---|---|---|
| Photos de patch (échantillon physique) | Photographiées par ARTEO ou VIMAWEB, ajoutées à la médiathèque (JPG 750 × 750, dossier `2022/05`) | **Confirmé par Valérie (15/10).** |
| Photos de la selle sous plusieurs angles | Valérie, chez elle | Compte rendu du 07/10. |
| Découpe des calques (zones) | Valérie (chez elle), Photoshop | Compte rendu du 07/10. **Outil confirmé par les fichiers** : 12 400 PNG sur 12 931 portent la signature Adobe Photoshop pour Windows (version « CC » de 2022-2023, puis « 25.1 » pour les fiches de 12/2024 à 02/2025, soit deux installations). Les patchs ont été retouchés dans Photoshop CC le 12/05/2022. Gabarit ou action : inconnus. |
| Image « matière sur zone » | Patch collé au calque | **Recette : inconnue.** Observation sur les images (Z900, une zone) : la texture du patch est reprise à plus petite échelle, sans déformation de perspective visible, découpée par le masque de la zone. L'éclairage est dans un calque séparé « Ombres et éclairage ». **Lecture des métadonnées** : 10 823 PNG sur 12 931 (84 %) descendent d'un **même document Photoshop source**. Signal d'une production à partir d'un gabarit unique, à confirmer. Les 3 autres documents sources (460 à 874 fichiers) semblent correspondre à des jeux du simulateur de broderie : noms `r6-assise-…`, `f900xr-assise-…` et `assises-…` (à rapprocher du dossier `images-nid-abeille`). |
| Import dans WordPress, puis ajout des choix | Valérie, éditeur du plugin dans la fiche produit | L'éditeur propose : ajouter un choix par son nom, choisir l'image par angle dans la médiathèque, **copier / coller** des choix entre calques, regrouper des choix, réordonner, import / export par produit. Sa pratique exacte est inconnue. |

**Premier essai de reconstitution de la recette (15/10, Z900, zone « Assises arrière », 37 matières, masque identique pour toutes)**  (deux itérations) :

| Mesure | Résultat |
|---|---|
| **Couleur** : moyenne du patch → couleur de l'image de zone, régression linéaire par canal, validée en laissant chaque matière de côté | **ΔE médian 2,5, maximum 6,4** sur 37 matières. La couleur se déduit du patch. Les moins bien prédites : Gris fiber argent (6,4), Marron (5,3), Citron (5,2), Gris souris (5,0). |
| **Échelle de la texture** : « Quadrillé » seul | Isotrope, ≈ **0,30** (228 × 224 px pour un patch de 750). Corrélation 0,42 seulement. Ma première lecture « échelle non uniforme » était fausse. |
| **Texture des autres matières** | Corrélation ≈ 0 avec leur patch, à 0,26–0,34 d'échelle, pour les 8 autres matières à forte énergie de texture (fiber, marron, strié, rouge prune…). **La texture de l'image de zone n'est pas retrouvée par simple échelle et décalage du patch.** |
| Lecture de l'écart | Soit la texture vient d'une source plus grande ou orientée autrement que la vignette de 750 px, soit chaque patch a été placé et retravaillé à la main. Les deux restent à départager. |

**Ce que ça veut dire** : on ne reconstitue pas la recette de Valérie, et on n'en a pas besoin. Pour les matières unies (28 sur 37 ont une énergie de texture < 6 niveaux sur 255), la couleur du patch suffit à produire l'image à ΔE ≈ 3. Pour les 9 matières texturées, il faudra un rendu de texture jugé à l'œil (statistiques de texture, pas SSIM pixel à pixel), à comparer aux vraies images. C'est la suite du poste 3. Scripts : `Phase 1/scripts/recette_couleur_texture.py` et `recette_decalages.py`. Limite : une zone d'un modèle (Z900, Assises arrière).

**Pas de nouveau mail à Valérie (décision de Melvin, 15/10)** : les inconnues (qui, quel gabarit, quelle action, PSD d'origine, pratique dans l'éditeur) se déduisent des fichiers, ou deviennent des hypothèses écrites dans le rapport. Méthode : reproduire une image de zone à partir du patch et du masque, et mesurer l'écart avec l'image réelle (c'est le poste 3).

## 6. Poste 3 : tests de rendu matières/couleurs (fait le 15/10)

**Question** : peut-on produire l'image « matière X sur zone Y du modèle Z » à partir du seul patch et du masque de la zone, assez proche de l'image existante du configurateur ?

**Méthode** (scripts `Phase 1/scripts/poste3_*.py` et `recette_*.py`) :
- couleur de l'image de zone = fonction linéaire (par canal) de la couleur moyenne du patch, apprise sur la **Z900** (37 matières par zone) ;
- texture = détail haute fréquence du patch, à l'échelle 0,30, avec un gain appris (≈ 1,5) ;
- masque = celui de la zone du modèle (donné, découpé par Valérie) ;
- test sur **4 modèles jamais vus** : Honda CB 500 F, BMW S 1000 XR, KTM 125/390 Duke, Triumph 900 Tiger. Formes de zone distinctes de la Z900 (IoU des masques entre 0,0 et 0,64).

| Mesure | Résultat |
|---|---|
| Couleur moyenne de la zone, écart ΔE | **médiane 2,1 à 3,0** selon la zone et le modèle, maximum ≈ 6 sur les matières. Liserés : maximum 12 pour quelques couleurs (à identifier). |
| Texture, énergie générée / réelle | 0,97 à 1,05 (Z900, Honda, BMW) ; **0,82 à 0,90** (KTM, Triumph) |
| Écart pixel à pixel (inclut le décalage de texture, donc pessimiste) | ΔE médian 3,6 à 3,8 |
| **Rendu complet** de la selle (4 combinaisons par modèle) | ΔE médian **2,8 à 4,4**, SSIM **0,87 à 0,96** |
| Surpiqûres | Modèle linéaire en échec (ΔE 22,6) : ce sont des **couleurs unies saturées** (ex. bleu égyptien : patch 36/54/112, calque 34/27/223). Une valeur de couleur par fil suffit. |

Planches réel (gauche) / généré (droite), 4 combinaisons : ![[poste3-rendu-honda-cb500f.jpg]] ![[poste3-rendu-ktm-duke.jpg]]

**Verdict** :
- **Faisable pour la couleur et pour les matières unies** (28 sur 37). **Pour les matières texturées, ce générateur est insuffisant** : voir la correction au §9.
- **Un nouveau modèle ne demande que les masques** des zones (découpe de Valérie). Les images de chaque matière se génèrent ensuite, de l'ordre de la seconde par image.
- **Une nouvelle matière ne demande que son patch** (et une couleur pour un fil de surpiqûre).

**Limites** :
- La référence est l'image **existante du configurateur**, pas une photo de selle physique.
- Les masques sont ceux des vrais calques : le test ne couvre pas leur production.
- La texture générée n'est pas alignée pixel à pixel sur la réelle (recette d'origine non retrouvée, §5) : jugée par statistiques et à l'œil.
- Matières brillantes ou chromées (ΔE max 12 sur les liserés) : à lister et à garder en photo.
- Un modèle appris (Z900) et quatre testés ; pas de test sur les 46 configurations.
- Le patch a été photographié par ARTEO ou VIMAWEB : sa fidélité à la matière réelle n'est pas vérifiée.

## 7. Poste 1 : tests de regroupement lot / famille (fait le 15/10, plugin actuel 1.7.6)

### Données (345 fiches, clé d'identité = identifiant de la vignette, pas le nom)

| Type de calque | Calques à choix | Listes distinctes | Liste canonique |
|---|---|---|---|
| Assises (avant, arrière) | 470 | 8 | 37 choix, 449 calques (96 %) |
| Bandeaux | 344 | 4 | 37 choix, 336 calques (98 %) |
| Bandes latérales | 335 | 3 | 37 choix, 332 calques (99 %) |
| Bec | 351 | 5 | 37 choix, 337 calques (96 %) |
| Dosseret | 64 | 1 | 37 choix, 64 calques |
| Liserés | 337 | 1 | 44 choix, 337 calques |
| Surpiqûres | 341 | 3 | 26 choix, 335 calques (98 %) |

- **336 produits sur 345 (97 %)** n'ont que des listes canoniques. Les 9 autres ont au moins un calque à liste atypique (41 à 47 choix, dont CFMOTO 800 NK) ; liste exacte à établir.
- **Recomposition exacte** : 2 190 calques sur 2 242 (98 %), 79 704 choix. Nom, identifiant, ordre, disponibilité, description et nombre d'images se retrouvent à l'identique à partir du jeu partagé et de l'image du produit. Seul écart : le **choix par défaut** (1 446 cas), un réglage par produit et par calque.
- Dans les listes canoniques, aucun nom ne s'écarte de la règle « préfixe du calque + nom du jeu » : les variantes de noms (27 jeux comptés au 14/10) sont dans les listes atypiques. Par identité de patch, il n'y a que **3 jeux**.

### Essais sur le plugin actuel (site local, mu-plugin de test, filtre `mkl_pc/db/get`, rien d'écrit dans les produits)

| Essai | Résultat |
|---|---|
| **Lot** : renommer une matière une seule fois dans le jeu partagé | Visible sur **337 fiches sur 345**, 0 méta de produit modifiée |
| **Famille** : ranger les choix en groupes selon la page « Matières » | **57 groupes natifs** sur la Z900, 292 choix rattachés ; le front affiche les familles en têtes de liste (« LES NOIRS »…) |
| Familles de la page | Noirs, Gris, Bleus, Rouges, Orangés/Jaunes, Verts, Autres. 2 fils de surpiqûre sans famille (classés « Autres ») |

**Conclusion** : le regroupement par lot et par famille est **possible sur la 1.7.6**, sans fork, avec un petit plugin sur le filtre de lecture. Les groupes de choix sont natifs.

**Reste à faire en Phase 2** (non testé) : l'écriture (stocker le jeu une seule fois, pas seulement le composer à la lecture), les écrans « Matières » et « Modèles » pour Valérie, la régénération du fichier de configuration public, et le comportement des commandes passées (les identifiants de choix sont conservés).

### Plugin 2.0.0
Non testé. Il n'est pas nécessaire pour prouver le regroupement. Son intérêt serait de remplacer le petit plugin par les configurateurs globaux natifs, avec migration automatique des données. Le paquet 2.0.0 n'est pas disponible a priori (licences chez VIMAWEB) : s'il est publié sur le dépôt officiel WordPress.org, il faudra ton accord pour le télécharger. Un retour arrière est possible : l'instantané de la base est dans `clone-fichiers/snapshots/`.

## 8. Poste 1 : lecture des deux derniers fichiers sur mesure (15/10, lecture seule)

| Fichier | Ce qu'il fait | À retenir |
|---|---|---|
| `mu-plugins/active-plugins.php` (ARTEO, « development plugin ») | Sur le **front uniquement** (hors `/wp-admin/`), retire des plugins de la liste active selon l'adresse : accueil, boutique `/selles-de-moto/`, produits `/selle-de-moto/`, matières, FAQ, infos de paiement, contact. Chemins et adresses écrits en dur. | **Le configurateur et APF restent actifs sur les fiches produits** : le regroupement n'est pas gêné. **Panier, commande et compte ne correspondent à aucune règle : tous les plugins s'y chargent**, ce qui peut les alourdir (piste performance et panier perdu). Tout plugin ajouté sera chargé partout tant qu'il n'est pas listé. Un changement d'adresse en refonte désactiverait ce filtrage sans prévenir. Le plugin signalé comme compromis n'est retiré que des pages listées, pas des autres. |
| `Divi Child/woocommerce/checkout/payment.php` | Surcharge du modèle de paiement WooCommerce : ajoute un bloc de texte sur la caution (échange standard, carte virtuelle ou organisme de financement) | **Différence avec le modèle 10.9.0 : seulement le bloc de texte et un attribut `aria-label` manquant.** Fonctionnellement équivalent : la piste « modèle obsolète = panier perdu » est **écartée**. Le texte contient un **« (X €) » littéral** : un montant jamais remplacé, visible par le client à la commande. |

Autres surcharges du thème enfant : modèles de facture PDF (`pdf/facture-sellerie-confort`), hors configurateur et hors périmètre.

## 9. Poste 3 : correction sur les matières texturées (15/10, soir) : REMPLACÉE par le §10 (j'avais comparé de mauvais fichiers)

**Remarque de Melvin** : le résultat sur les matières texturées n'est pas bon, et Valérie applique chaque patch proprement. Il a raison. Le test du §6 était **déterministe** (régression linéaire pour la couleur, répétition du patch pour la texture, aucun modèle génératif), mais sa recette pour la texture était mauvaise.

| Constat | Mesure |
|---|---|
| Le relief visible dans les calques n'est **pas dans le patch** | Photos de patch lisses, de 35 à 52 Ko (par exemple `Fiber-black.jpg`). Le tressage « fiber », le grain du cuir, le strié n'y apparaissent pas (planche `essais-poste3/textures-zoom-assises.png`). |
| La texture n'est pas un recalage du patch | Recherche avec rotation libre, étirement x/y et 8 symétries : meilleure corrélation **0,30**, sur l'échelle limite de la grille. Seul le « Quadrillé » dépasse le bruit. |
| Le relief n'est pas un calque commun posé à la même place | Corrélation pixel à pixel entre matières : seulement { antidérapant, Enduro, charbon, galaxy } (0,75 à 0,85) et { Petronas, azur } (0,95). Les autres matières ont chacune leur propre relief. |
| Aucune source haute résolution dans la médiathèque | Rien de plus grand que les patchs. Les textures sources sont donc chez Valérie (fichiers Photoshop ou photos d'origine). |

**Conclusion** : sa méthode est automatisable, mais elle part de **textures sources** que nous n'avons pas. Le patch web ne suffit pas. Nous ne pouvons pas la rejouer à partir de la médiathèque.

**Ce qui marche sans ses fichiers : reporter la texture réelle déjà rendue.** Pour une matière existante, l'image d'une zone d'un modèle déjà fait contient sa texture exacte. On en prend un carré dans le masque et on le répète sur la zone d'un autre modèle (déterministe, aucun modèle génératif). Essai Z900 → KTM Duke, zone « Assises arrière », 22 matières texturées (planche `essais-poste3/exemplaire-z900-vers-ktm.png`) :
- à l'œil, tissage, perforé, strié, quadrillé et cuir sont fidèles à l'image réelle du KTM ;
- écart de couleur moyen ≤ 2,5 sur 255 ;
- l'énergie de texture du report va de 0,58 à 1,04 de la réelle (le carré d'exemplaire est petit : à affiner).
- Attention : pour 7 matières, le KTM utilise déjà **les mêmes fichiers** que la Z900 (énergie et couleur identiques). Ces cas sont triviaux.

| Besoin | Méthode | État |
|---|---|---|
| **Nouveau modèle**, matières existantes | Masques des zones + texture réelle reportée depuis un modèle déjà fait | **Faisable**, jugé à l'œil |
| **Nouvelle matière unie** | Couleur du patch (ΔE ≈ 2,5) | **Faisable** |
| **Nouvelle matière texturée** | Il faut sa texture source (photo haute résolution, comme celle que Valérie applique aujourd'hui) | **Pas faisable depuis le patch web seul** ; à écrire comme précondition dans le rapport |

**Limites** : une zone, deux modèles ; carré d'exemplaire petit, donc répétition visible possible sur de grandes zones ; pas encore de chiffrage SSIM (le report n'est pas aligné pixel à pixel, par construction).

**Compléments (15/10, soir)** : deux tests de plus pour savoir si le patch web est la source de la texture du calque.
- **Relief calculé à partir du patch** (dérivées à 4 angles, laplacien, inverse, échelles 0,20 à 0,42, 4 rotations, décalage libre) : corrélation 0,01 à 0,05 sur les 8 matières texturées ; seul le « Quadrillé » reste à 0,38 (0,17 à 0,32 avec les dérivées). Ce n'est donc pas un effet d'estampage (emboss) appliqué au patch.
- **Spectre de texture** (insensible au recadrage) : aucune échelle commune. Les meilleures échelles vont de 0,23 à 0,99 selon la matière, et à l'échelle 0,30 la corrélation est faible ou négative pour la plupart. Si le même patch avait reçu la même transformation, on attendrait une échelle commune.

**Lecture prudente** : pour les matières texturées testées, le patch web donne la **couleur** et la **famille de matière** (même tissage de base pour le « Quadrillé »), mais **pas le relief** du calque. Que ce soit une autre photo, une autre résolution ou un autre traitement, nous ne le savons pas : aucun test sur ces fichiers ne le tranche. Observation utile pour le rapport : sur la page « Matières » du site, une matière comme « Fiber blanc » apparaît lisse, alors que le configurateur la montre tressée.

**Recherche de sources de texture dans la médiathèque (15/10, soir)** : liste publique (API REST) = **15 123 médias**, 15 120 téléchargés, 1 invalide, 2 en erreur ; **4,98 Go d'originaux**, tous des images (PNG 12 933, JPEG 2 010, WebP 176, AVIF 3, HEIC 1), identifiants de 15 à 222 392. Le rapport système de la prod du 14/10 en compte **15 185** : 62 de plus que la liste publique (hypothèse : pièces jointes liées à des contenus non publics). Hors calques, 2 365 images ; les plus grandes (374 de 2 000 px et plus, planche `essais-poste3/planche-grandes-photos.jpg`, 96 vérifiées) sont des **photos de selles ou de motos**, aucun gros plan d'étoffe. Les noms évoquant une matière (`avant-assises-arriere-*`, `couture-*`, `bande-*`) sont des jeux du simulateur nid d'abeille. **Aucune source de texture n'est visible dans la partie publique de la médiathèque.** La part non publique (62 fichiers) n'est pas examinée.

## 10. Poste 3 : correction décisive, la texture est sur WordPress (15/10, soir)

**Cause de mon erreur** : j'avais comparé les calques aux **patchs du nuancier (750 px, 2022/05)**, que le configurateur utilise comme vignettes. Ce ne sont pas les fichiers que Valérie applique. Capture de Melvin : `Fiber-Blanc.jpg`, **171 × 171 px**, téléversé le 11/03/2025 par Valérie Cenizo, rattaché à la fiche BMW F 900 XR ; il montre le tressage. Les paragraphes « relief absent du patch » des §6 à §9 concernaient les mauvais fichiers.

| Constat | Mesure |
|---|---|
| Petites images de matière de Valérie | **93 fichiers de 171 × 171 px** (2024/12 et 2025/03), 50 noms de matière retrouvés |
| Échelle par rapport aux calques | **1,00** (meilleure échelle 0,995 à 1,005 sur 7 matières) : même résolution que le calque |
| La petite image est un extrait exact des calques | Corrélation **0,999 à 1,000** par recherche de gabarit dans les calques de **dizaines de modèles** (Yamaha FJR, TDM, Suzuki Hayabusa, BMW S1000R, Kawasaki Z900…) |
| Une même texture posée aux mêmes coordonnées | Calques de 60 modèles pour « Fiber blanc » : **837 paires sur 837 identiques au pixel près** là où les zones se recouvrent (MAE 0,00) |

**La recette de Valérie est donc** : une **texture maître de 1920 × 1280 par matière**, découpée (masque d'écrêtage) par le masque de chaque zone de chaque modèle. Les 12 400 PNG qui descendent d'un même document Photoshop (§5) vont dans le même sens.

### Régénération à l'aveugle (modèles mis de côté, jamais utilisés pour la reconstitution)

Texture maître reconstituée par la réunion des calques de 37 modèles (207 fichiers par matière, **69 % du canevas**), testée sur 6 modèles mis de côté (BMW R 1150 RT, Dorsoduro 750, Honda CTX, KTM Duke, Suzuki GSX-S, Yamaha MT-09 Tracer ; 34 à 40 zones par matière).

| Matière | Pixels des zones couverts | Pixels identiques | Écart moyen (0-255) | Conflits entre modèles |
|---|---|---|---|---|
| Fiber blanc | **100 %** | **100 %** | **0,00** | 0 % |
| Noir perforé | **100 %** | **100 %** | **0,00** | 0 % |
| Marron | 100 % | 99,8 % | 0,10 | 2,4 % |
| Noir quadrillé | 100 % | 73,9 % | 2,44 | 40 % |
| Rouge vif | 100 % | 69,7 % | 1,84 | 47 % |
| Gris fiber argent | 100 % | 66,5 % | 3,53 | 51 % |
| Noir strié | 100 % | 63,1 % | 3,85 | 57 % |
| Violet | 100 % | 58,8 % | **27,54** | 24 % |

**Lecture** : les zones de modèles jamais vus sont **entièrement couvertes** par la texture reconstituée, et pour 3 matières sur 8 le résultat est **identique au pixel près**. Pour les autres, des modèles d'époques différentes ne portent pas exactement la même version de la texture (conflits de 24 à 57 % des pixels). L'écart moyen reste de 2 à 4 niveaux sur 255, sauf le Violet (27,5), où une variante de couleur différente existe.

### Ce que ça change

| Besoin | Méthode | État |
|---|---|---|
| **Nouveau modèle**, matières existantes | Texture maître de la matière découpée par les masques du modèle | **Faisable, exact au pixel pour une partie des matières** ; versions à départager pour les autres |
| **Nouvelle matière** (unie ou texturée) | Sa petite image de 171 × 171 px, **répétée à l'échelle 1** | **Faisable** : à l'œil, même tressage que le calque ; MAE 4,1, ΔE 2,2, SSIM 0,72 sur 27 matières (6 texturées : MAE 10, ΔE 4,6, SSIM 0,44). Idéal : sa texture maître, comme Valérie. |
| **Surpiqûres** | Couleur unie par fil | Faisable |

**Reste à faire** : classer les variantes de texture par époque et prendre la plus récente par défaut (explique les conflits) ; vérifier la couverture sur les 43 modèles ; couture du raccord quand on répète une tuile de 171 px.

**Ce que ça annule** : la précondition « il faut les textures de travail de Valérie » du §9 devient « sa petite image 171 × 171 suffit pour une nouvelle matière ». Il n'est donc pas nécessaire de rephotographier les matières existantes.

### Glossaire : la texture maître (terme de travail, pas un nom trouvé dans ses fichiers)

La **texture maître** d'une matière est **une seule grande image**, de la taille du canevas (1920 × 1280 px), qui contient le motif de la matière (tressage du « Fiber blanc », grain du « Violet »…) sur toute sa surface. Un **calque de zone** est cette image **vue à travers le masque de la zone** : la forme découpée de la zone garde la texture, le reste est transparent. C'est le principe d'un masque d'écrêtage dans Photoshop.

```
texture maître          masque de la zone         calque (PNG du site)
(toute l'image)    ×    (forme de l'assise)   =   (texture visible
                                                   seulement dans la forme)
```

**Pourquoi elle existe** : les calques « Fiber blanc » de 60 modèles sont identiques au pixel près là où leurs zones se recouvrent, et la petite image de 171 × 171 px se retrouve telle quelle (corrélation 0,999) dans les calques de dizaines de modèles : c'est un recadrage de cette grande texture.

| Objet | Taille | Rôle |
|---|---|---|
| Patch du nuancier (2022/05) | 750 × 750 | Vignette du choix dans le configurateur et sur la page Matières. **Pas la texture appliquée.** |
| Petite image de Valérie (2024/12, 2025/03) | 171 × 171 | Un **extrait** de la texture maître, à l'échelle 1 |
| Texture maître | 1920 × 1280 | L'image complète de la matière, sur tout le canevas |
| Calque d'une zone (PNG du site) | 1920 × 1280 | Texture maître **× masque** d'une zone d'un modèle |

**Ce que nous avons** : pas son fichier de texture maître. Nous l'avons **reconstituée** en assemblant les morceaux visibles dans les calques existants : environ 69 % du canevas avec 37 modèles, ce qui suffit à couvrir 100 % des zones des modèles testés, mais pas à livrer une image complète.

**Ce que ça permet** : pour un nouveau modèle, on applique ses masques à la texture maître de chaque matière. Pour une nouvelle matière, il faut sa texture maître, ou à défaut sa petite image de 171 px répétée à l'échelle 1.

### Versions de la texture maître par matière (15/10, soir, zones de surface, 39 matières)

Méthode : calques regroupés en versions (mêmes pixels là où les zones se recouvrent, tolérance 4 niveaux), versions datées par le dossier d'envoi, test à l'aveugle sur 6 modèles mis de côté. Liserés et surpiqûres écartés : ce sont des lignes fines, sans recouvrement suffisant pour comparer (version non déterminable, couleur unie).

| Cas | Matières | Nombre | Identiques avec la version récente | Identiques avec la bonne version |
|---|---|---|---|---|
| **Une seule version** | Blanc, Bleu azur, Bleu égyptien, Bleu MT Violet, Bleu Petronas, Citron, Fiber blanc, Jaune colza, Marron, Noir fiber black, Noir perforé, Rouge Bordeaux, Rouge griotte, Vert pin | **14** | **100 %** | 100 % |
| **Une version dominante** (97,6 % des fichiers) | Bleu océan, Rouge prune, Vert primaire, Violet | **4** | **100 %** | 100 % |
| **Deux versions réelles** (≈ 56 % récente / ≈ 42 % ancienne) | Gris brume argent, Gris fiber anthracite, Gris fiber argent, Gris tonnerre, Marron foncé, Noir Enduro, Noir quadrillé, Noir strié, Orange poterie, Rouge vif, Sable, Vert pistache, Bleu Yam, Gris macadam, Gris souris, Noir antidérapant, Noir carbone, Noir charbon, Noir diamant, Noir galaxy, Orange | **21** | 66,8 à 97,6 % | **99,4 à 99,7 %** |

**Lecture** : le partage 56,5 % / 42 % est le même pour les 21 matières, donc il suit des **groupes de modèles** et non des matières : ces 21 matières ont été refaites en 2023/01, et les modèles d'avant gardent l'ancienne version. Pour **un nouveau modèle**, la version récente est la règle naturelle. Il reste à confirmer que les derniers modèles l'utilisent (c'est le cas des fichiers de 2023/01 à 2023/12). Les 3 matières à 8 versions comptent surtout des variantes isolées d'un fichier.

### Correspondance matière / petite image de 171 px, par le contenu et non par le nom

Recherche du gabarit dans le calque de la plus grande zone de la Z900 (Bandeaux), 50 petites images :

| Matière du configurateur | Petite image | Corrélation |
|---|---|---|
| Noir fiber black | `Fiber-black.jpg` | 0,96 |
| Noir quadrillé | `Quadrille.jpg` | 0,79 |
| Gris tonnerre | `Gris-tonnerre.jpg` | 0,65 |
| Bleu MT Violet | `Bleu-MT-Bleu-Violet.jpg` | 0,88 |
| Rouge Bordeaux | `Bordeaux.jpg` | 0,76 |
| Rouge prune | `Prune.jpg` | 0,78 |
| **Vert pin** | **`Pin.jpg`** (distinct de `Vert-Primaire.jpg`, qui correspond à « Vert primaire ») | 0,84 |
| Noir Enduro | `Enduro-Noir.jpg` | 0,56 |
| Noir antidérapant | pas de fichier propre ; même famille de texture que Enduro, charbon et galaxy (0,5) | ambigu |
| Bleu Yam | aucune correspondance fiable | 0,38 |

Les noms de fichiers diffèrent donc des noms du configurateur (mots inversés ou raccourcis). Pour 7 de ces 10 matières, la petite image existe ; pour 2 elle est ambiguë (famille de texture commune) ; pour 1 elle n'est pas trouvée. Deux fausses correspondances de la méthode (Bleu azur → Blanc, Marron → Sable) viennent de matières à peu de relief : la corrélation sous 0,6 n'est pas fiable pour elles, le nom suffit.

### Les 39 matières : réel contre texture maître contre vignette (15/10, soir)

Pour chaque matière, quatre colonnes : **réel** (extrait de 140 × 100 px du calque PNG de la zone d'un modèle mis de côté, c'est-à-dire ce que le configurateur empile), **texture maître** de la version récente construite sans ce modèle, **vignette** du nuancier (patch de 750 px, 2022/05, celle que référence le configurateur), **petite image de 171 px** de Valérie (2024/12 et 2025/03) répétée à l'échelle 1. Planches : `essais-poste3/planches-v2-*/` (script `poste3_planche_39_v2.py`).

| Modèle mis de côté | Matières identiques à 99 % ou plus | Moyenne de pixels identiques |
|---|---|---|
| KTM Duke | **39 sur 39** | 100 % |
| Honda CTX | **39 sur 39** | 100 % |
| Yamaha MT-09 Tracer | **39 sur 39** | 100 % |
| BMW R 1150 RT | 18 sur 39 | 83,7 % |
| Suzuki GSX-S 2 Parts | 18 sur 39 | 83,7 % |
| Dorsoduro 750 | 16 sur 37 | 82,8 % |

**Lecture** : les trois modèles qui utilisent la version récente sont retrouvés à l'identique pour **les 39 matières**. Les trois autres portent l'ancienne version pour les 21 matières refaites en 2023/01 : les 18 matières à une seule version restent identiques, les autres montrent un écart moyen de 1,6 à 5 niveaux sur 255. La **vignette du nuancier** ne reproduit ni le relief ni la couleur exacte (image lissée, avec dégradé d'éclairage). La **petite image de 171 px** donne le bon grain et la bonne couleur : sur 36 matières sur 39 (il manque Bleu Yam, Noir antidérapant, Noir diamant), écart moyen médian de **4,8** sur 255 (KTM Duke) et 5,0 (BMW R 1150 RT), sans être identique au pixel (la phase de la tuile n'est pas celle du modèle).

KTM Duke (version récente, 39 sur 39) : ![[poste3-planche-ktm-duke-1.jpg]]

BMW R 1150 RT (ancienne version, 18 sur 39) : ![[poste3-planche-bmw-r1150rt-2.jpg]]

Les planches complètes sont `poste3-planche-ktm-duke-{1,2,3}.jpg` et `poste3-planche-bmw-r1150rt-{1,2,3}.jpg` dans les pièces jointes.

### Selles entières : réel contre texture maître (15/10, soir)

Rendu complet de la selle : calques réels empilés (photo de base, zones, ombres) contre les mêmes calques dont les **zones de surface** (assises, bandes, bandeaux, bec, dosseret) sont régénérées avec la texture maître construite **sans ce modèle**. Liserés et surpiqûres restent réels (lignes fines, couleur unie). Deux combinaisons par modèle, avec zoom sur les assises. Script : `poste3_selles.py`, images : `essais-poste3/selles/`.

| Modèle (mis de côté) | Version utilisée par le modèle | Combinaison 1 : pixels de surface identiques | Combinaison 2 |
|---|---|---|---|
| KTM Duke | récente | **100 %** (écart 0,00) | **100 %** |
| Honda CTX | récente | **100 %** | **100 %** |
| BMW R 1150 RT | ancienne | 77,6 % (écart 2,6/255) | 61,6 % (écart 4,1/255) |
| Suzuki GSX-S 2 Parts | ancienne | 80,0 % (écart 2,3/255) | 65,5 % (écart 3,7/255) |

**Lecture** : à l'échelle de la selle, les deux rendus sont indiscernables, y compris pour les modèles qui portent l'ancienne version. Au zoom, les différences apparaissent sur le grain (par exemple le tressage « Gris fiber argent » est plus fin sur la version récente). La règle de version par modèle les supprime.

![[poste3-selle-ktm-duke.jpg]]
![[poste3-selle-bmw-r1150rt.jpg]]

Autres : `poste3-selle-honda-ctx.jpg`, `poste3-selle-suzuki-gsxs.jpg`. Les choix de la combinaison sont ceux dont le nom contient le mot demandé en premier (par exemple « violet » a retenu « Bleu MT Violet »).


### Inventaire des 37 matières : vignettes et versions de texture (15/10, soir)

Deux notions à ne pas confondre :

- **Vignette** : la petite image du choix. Il en existe deux générations. L'**ancienne** (nuancier, 2022/05, mesurée à 750 × 750 sur les exemples) sert à la fois sur la page « Matières » et dans le configurateur des fiches standard. La **nouvelle** (171 × 171 px, téléversée par Valérie en 2024/12 puis 2025/03) sert dans les fiches nid d'abeille (F 900 XR, R6) et n'est pas sur la page Matières.
- **Texture des calques** : la version de l'image appliquée sur la selle. Les 21 matières refaites en 2023/01 existent en version **récente** et **ancienne** ; les modèles d'avant 2023/01 gardent l'ancienne.

| Famille | Matière | Vignette page + configurateur (ancienne) | Nouvelle vignette (171 px) | Texture des calques |
|---|---|---|---|---|
| Noirs | Noir antidérapant | `Anti-derapant.jpg` (2022/05) | **aucune** | récente + ancienne (68 fichiers anciens) |
| Noirs | Noir charbon | `Noir-charbon.jpg` (2022/05) | `Noir-Charbon.jpg` (2025/03) | récente + ancienne (67 fichiers anciens) |
| Noirs | Noir Enduro | `Enduro-noir.jpg` (2022/05) | `Enduro-Noir.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Noirs | Noir fiber black | `Fiber-black.jpg` (2022/05) | `Fiber-black.jpg` (2025/03) | une seule version |
| Noirs | Noir galaxy | `Noir-galaxy.jpg` (2022/05) | `Noir-Galaxy.jpg` (2025/03) | récente + ancienne (67 fichiers anciens) |
| Noirs | Noir perforé | `Noir-perfore.jpg` (2022/05) | `Noir-perfore.jpg` (2025/03) | une seule version |
| Noirs | Noir quadrillé | `Quadrille.jpg` (2022/05) | `Quadrille.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Noirs | Noir strié | `Noir-strie.jpg` (2022/05) | `Noir-strie.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Gris | Gris brume argent | `Gris-Brume-argent.jpg` (2022/05) | `Gris-Brume-Argent.jpg` (2025/03) | récente + ancienne (72 fichiers anciens) |
| Gris | Gris fiber anthracite | `Gris-Fiber-Anthracite.jpg` (2022/05) | `Gris-Fiber-Anthracite.jpg` (2025/03) | récente + ancienne (72 fichiers anciens) |
| Gris | Gris fiber argent | `Gris-Fiber-Argent.jpg` (2022/05) | `Gris-Fiber-Argent.jpg` (2025/03) | récente + ancienne (72 fichiers anciens) |
| Gris | Gris macadam | `Gris-Macadam.jpg` (2022/05) | `Gris-macadam.jpg` (2025/03) | récente + ancienne (67 fichiers anciens) |
| Gris | Gris souris | `Gris-Souris.jpg` (2022/05) | `Gris-Souris.jpg` (2024/12) | récente + ancienne (67 fichiers anciens) |
| Gris | Gris tonnerre | `Gris-Tonnerre.jpg` (2022/05) | `Gris-tonnerre.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Bleus | Bleu azur | `Bleu-Azur.jpg` (2022/05) | `Bleu-Azur.jpg` (2025/03) | une seule version |
| Bleus | Bleu MT Violet | `Bleu-MT-Bleu-violet.jpg` (2022/05) | `Bleu-MT-Bleu-Violet.jpg` (2025/03) | une seule version |
| Bleus | Bleu océan | `Bleu-Ocean.jpg` (2022/05) | `Bleu-Ocean.jpg` (2025/03) | récente (variantes isolées) |
| Bleus | Bleu Petronas | `Bleu-Petronas.jpg` (2022/08) | `Bleu-Petronas.jpg` (2025/03) | une seule version |
| Bleus | Bleu Yam | `Yam.jpg` (2022/05) | **aucune** | récente + ancienne (67 fichiers anciens) |
| Bleus | Bleu Égyptien | `Bleu-Egyptien.jpg` (2022/05) | `Bleu-Egyptien.jpg` (2025/03) | une seule version |
| Rouges | Rouge Bordeaux | `Bordeau.jpg` (2022/05) | `Bordeaux.jpg` (2025/03) | une seule version |
| Rouges | Rouge griotte | `Rouge-griotte.jpg` (2022/05) | `Rouge-Griotte.jpg` (2025/03) | une seule version |
| Rouges | Rouge prune | `Prune.jpg` (2022/05) | `Prune.jpg` (2024/12) | récente (variantes isolées) |
| Rouges | Rouge vif | `Rouge-vif.jpg` (2022/05) | `Rouge-Vif.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Orangés / Jaunes | Citron | `Citron.jpg` (2022/05) | `Citron.jpg` (2025/03) | une seule version |
| Orangés / Jaunes | Jaune colza | `Jaune-colza.jpg` (2022/05) | `Jaune-Colza.jpg` (2025/03) | une seule version |
| Orangés / Jaunes | Orange | `Orange.jpg` (2022/05) | `Orange.jpg` (2025/03) | récente + ancienne (67 fichiers anciens) |
| Orangés / Jaunes | Orange poterie | `Orange-poterie.jpg` (2022/05) | `Orange-Poterie.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Orangés / Jaunes | Sable | `Sable.jpg` (2022/05) | `Sable.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Verts | Vert pin | `Pin.jpg` (2022/05) | `Pin.jpg` (2024/12) | une seule version |
| Verts | Vert pistache | `Vert-pistache.jpg` (2022/05) | `Vert-Pistache.jpg` (2025/03) | récente + ancienne (71 fichiers anciens) |
| Verts | Vert primaire | `Vert-primaire.jpg` (2022/05) | `Vert-Primaire.jpg` (2025/03) | récente (variantes isolées) |
| Autres couleurs... | Blanc | `Blanc.jpg` (2022/05) | `Blanc.jpg` (2025/03) | une seule version |
| Autres couleurs... | Fiber blanc | `Fiber-blanc.jpg` (2022/05) | `Fiber-Blanc.jpg` (2025/03) | une seule version |
| Autres couleurs... | Marron | `Marron.jpg` (2022/05) | `Marron.jpg` (2024/12) | une seule version |
| Autres couleurs... | Marron foncé | `Marron-fonce.jpg` (2022/05) | `Marron-Fonce.jpg` (2024/12) | récente + ancienne (71 fichiers anciens) |
| Autres couleurs... | Violet | `Violet.jpg` (2022/05) | `Violet.jpg` (2025/03) | récente (variantes isolées) |
| (hors page) | Noir carbone | absente de la page | à vérifier | récente + ancienne (67 fichiers anciens) |
| (hors page) | Noir diamant | absente de la page | à vérifier | récente + ancienne (67 fichiers anciens) |

**Chiffres** : les 37 matières de la page ont toutes une vignette ancienne (page et configurateur sont identiques) ; **35 sur 37 ont une nouvelle vignette 171 px** (il manque Noir antidérapant et Bleu Yam) ; **14 ont une seule version de texture**, **21 ont une récente et une ancienne** (19 de la page, plus Noir carbone et Noir diamant, absents de la page) ; Bleu océan, Rouge prune, Vert primaire et Violet ont 4 versions mais 97,6 % des fichiers sur une seule.

**Si le nouveau configurateur n'utilise que les versions récentes** : toutes les matières ont une version courante, donc c'est faisable. Trois précautions : (1) les modèles d'avant 2023/01 changeraient légèrement (écart moyen de 2 à 5 niveaux sur 255, indiscernable à l'échelle de la selle, visible au zoom) ; (2) pour les 21 matières, la version récente couvre **61,0 %** du canevas contre **69,2 %** pour la réunion des deux : des zones qui n'existent que sur d'anciens modèles seraient à compléter ; (3) que la récente soit la version voulue par Valérie n'est pas vérifié.

### 750 px ou 171 px : quelle source pour reproduire une matière (15/10, soir)

**Le 171 × 171 reproduit mieux, et ce n'est pas une question de résolution.** La vignette de 750 px est une photo du tissu retouchée pour la page web : lissée, avec un dégradé d'éclairage, sans le relief. La petite image de 171 px est un **extrait de la vraie texture, à l'échelle où elle est appliquée**.

| | Vignette du nuancier (750 px, 2022/05) | Petite image de Valérie (171 px, 2024/12 et 2025/03) |
|---|---|---|
| **Relief** | Absent (corrélation ≈ 0,03 avec le calque) | Présent : même tressage ou grain que le calque |
| **Échelle par rapport au calque** | Sans rapport | **1,00** |
| **Couleur** | Correcte en moyenne (ΔE ≈ 2,5), éclairage inégal | Correcte (ΔE ≈ 2,2) |
| **Rendu répété sur une zone** | Mauvais pour les matières texturées | Proche du réel : écart moyen 4,8 (KTM Duke) et 5,0 (BMW R 1150 RT) sur 255 |

**Ce que 171 px ne règle pas** : la répétition (une tuile se répète 4 à 5 fois sur une zone de 700 px, raccords non traités) et les textures irrégulières (Violet, Marron), qui montrent le plus d'écart après répétition.

| Rang | Source | Fidélité |
|---|---|---|
| 1 | Texture maître (1920 × 1280, sans répétition) | Identique au pixel avec la bonne version |
| 2 | Petite image 171 px, répétée | Proche à l'œil, raccords à traiter |
| 3 | Vignette 750 px du nuancier | Couleur seulement |

**Pour une nouvelle matière** : il faut une image **à l'échelle 1:1, plus grande que la plus grande zone** (environ 800 × 500 px au minimum, idéalement 1920 × 1280), prise en lumière rasante. Une photo de 750 px prise de loin et lissée ne convient pas ; une image de 171 px à la bonne échelle suffit déjà pour un résultat acceptable.

## 11. Poste 3 : synthèse et clôture (15/10, soir)

**Poste 3 terminé.** La recette de Valérie est retrouvée, validée à l'aveugle sur des modèles jamais utilisés, et les cas sans source complète ont une méthode mesurée.

| Question | Réponse | Mesure |
|---|---|---|
| Recette de Valérie | Une **texture maître** de 1920 × 1280 par matière, découpée par le masque de chaque zone de chaque modèle | 837 paires de calques sur 837 identiques au pixel (Fiber blanc, 60 modèles) |
| Nouveau modèle, matières existantes | Texture maître × masques du modèle | **39 matières sur 39 identiques** sur 3 modèles à la version récente ; 18 sur 39 sur les 3 modèles à l'ancienne version, **99,4 % ou plus avec la bonne version** |
| Selle entière | Rendu empilé identique à l'échelle de la selle | 100 % des pixels de surface (KTM Duke, Honda CTX) ; 62 à 80 % avec l'ancienne version |
| Nouvelle matière unie | Couleur du patch | ΔE ≈ 2,5 |
| Nouvelle matière texturée | Sa petite image de 171 px à l'échelle 1, avec raccord (voir ci-dessous) | Écart moyen 4,8 à 5,0 sur 255, même grain à l'œil |
| Surpiqûres, liserés | Couleur unie par fil | Aucune version à gérer |

### Raccords de la petite image (modèle de test : KTM Duke, 8 matières texturées)

Repère : une visibilité du raccord ≤ 1,2 correspond à une couture invisible (1,0 = aussi lisse que l'intérieur de la tuile). Méthode A : recadrage sur un nombre entier de périodes. Méthode B : fondu par décalage.

| Matière | Période (px) | Raccord brut / A / B | Écart au réel brut / A / B | Méthode retenue |
|---|---|---|---|---|
| Fiber blanc | 27 × 51 | 1,77 / **0,35** / 1,21 | 12,6 / **6,0** / 12,3 | A |
| Noir strié | 12 × 36 | 1,25 / **0,47** / 1,23 | 10,2 / **2,8** / 10,8 | A |
| Noir perforé | 20 × 29 | 0,99 / **0,44** / 1,36 | 4,8 / **0,9** / 4,6 | A |
| Gris fiber argent | 14 × 41 | 0,60 / 0,66 / 0,92 | 15,1 / 20,1 / 15,1 | brut (raccord déjà invisible) |
| Gris fiber anthracite | 23 × 11 | 0,92 / 0,88 / 1,09 | 10,3 / 10,4 / 10,2 | brut |
| Noir quadrillé | 34 × 10 | 2,05 / 2,00 / **0,75** | 12,3 / 14,9 / 12,9 | B |
| Violet | non périodique | 1,34 / – / **1,10** | 14,2 / – / 13,9 | B |
| Marron | non périodique | 1,31 / – / **0,94** | 7,8 / – / 7,6 | B |

**Constat utile** : les tissages réguliers (perforé, strié, Fiber blanc) sont des motifs **strictement périodiques**. Une cellule unité suffit à régénérer leur texture maître, avec un écart de 0,9 sur 255 pour le Noir perforé. Les cuirs (Violet, Marron) sont irréguliers : le fondu suffit pour cacher les raccords.

### Règles à retenir pour la Phase 2

1. **Version de texture par modèle** : enregistrée une fois pour chaque modèle existant ; version récente par défaut pour un nouveau modèle.
2. **Une nouvelle matière** : couleur seule si elle est unie ; sa petite image 171 px (ou mieux, une image 1:1 de 800 × 500 px ou plus, en lumière rasante) si elle est texturée.
3. **Liserés et surpiqûres** : une valeur de couleur par fil.
4. **Raccords** : A pour les tissages périodiques, B pour les cuirs, brut sinon.

### Limites

- Régénération à l'aveugle sur 6 modèles et 39 matières ; raccords testés sur un seul modèle (8 matières).
- Fidélité mesurée par rapport aux images existantes de Valérie, pas à une photo de l'étoffe.
- Pas de nouvelle matière réelle testée : la méthode est validée sur les existantes, avec leur petite image.
- Le choix de la version « récente » comme défaut n'est pas confirmé par Valérie.
- Les matières sans petite image (Noir antidérapant, Bleu Yam, Noir diamant) n'ont que le patch du nuancier pour une nouvelle utilisation.

### Scripts (dossier `Phase 1/scripts/`)

`poste3_versions_texture.py`, `poste3_texture_maitre.py`, `poste3_planche_39_v2.py`, `poste3_selles.py`, `poste3_raccords_tuile.py`, `poste3_inventaire_matieres.py`, `poste3_tuile_171.py`, `poste3_correspondance_contenu.py`. Résultats : `Phase 1/essais-poste3/`.

### Compléments poste 1 : fichier public, fiches atypiques, clôture (15/10, nuit, site local)

**Le fichier de configuration public reprend les données composées.** Le fichier `uploads/mkl_product_configurations/product_configuration_39477.js` (celui que charge le visiteur) est supprimé puis régénéré par le plugin dans quatre états (mu-plugin de test, produit pilote Z900) :

| État | Taille | Groupes | Choix | Choix renommés |
|---|---|---|---|---|
| Normal (mode off) | 156 545 octets | 0 | 294 | 0 |
| Famille | 166 795 octets (+ 6,5 %) | **57** | 292 rattachés + 57 en-têtes | 0 |
| Lot (un seul renommage) | 156 612 octets | 0 | 294 | **7** (un par calque concerné) |
| Retour au mode normal, régénéré | 156 545 octets | 0 | 294 | 0 |

Le retour à l'état normal redonne **exactement** la taille d'origine. Le site local est remis en mode normal (`sc_test_mode` sur `off`).

**Les 9 fiches atypiques** (calque dont la liste ne reprend pas la liste canonique de son type) :

| Fiches | Ce qui diffère | Traitement envisagé |
|---|---|---|
| **5 sportives** : CFMOTO 800 NK, Yamaha R1, Yamaha R6, Kawasaki ZX-6R, Suzuki GSXR 600 | 44 à 45 choix par calque (7 calques), **aucune vignette en commun** avec le jeu canonique : autre génération du jeu. 28 noms sur 37 en commun, avec des variantes d'orthographe (« bordeau », « grisbrume »). Il manque Citron, Marron, Gris brume argent, Gris tonnerre, Bleu MT Violet sous leur nom habituel. | Rapprocher par nom (28/37) puis par contenu pour le reste ; ou les laisser en jeu propre au début |
| **2 nid d'abeille** : Yamaha MT-09, Suzuki GSX-S 8S/8R | **Jeu canonique + 4 choix** (Alcantara, Rose brillant, Rouge brillant, Vert brillant) : 37 sur 37 en commun, mêmes vignettes | Jeu canonique avec 4 matières optionnelles par fiche |
| **BMW F 900 XR ou R** | 43 à 47 choix, 28 noms sur 37 en commun, **fautes de frappe** (« alcanatara », « asssies marron fonce ») et autres vignettes ; surpiqûres : 34 choix | Normaliser les noms, puis rapprocher |
| **Honda Goldwing 1800** | Un seul calque : « Coutures assises (si option choisie) », 26 choix dont 5 fils différents | Variante du jeu des surpiqûres |

Liste complète : `Phase 1/essais-poste3/poste1-fiches-atypiques.json`. Les 336 autres fiches reprennent exactement les listes canoniques.

### Conclusion du poste 1 pour le rapport

- **Le regroupement par lot et par famille est faisable sur le plugin actuel (1.7.6), sans fork** : un petit plugin sur le filtre `mkl_pc/db/get`, des groupes de choix natifs pour les familles.
- **Périmètre** : 336 fiches sur 345 (97 %) se recomposent exactement à partir de 3 jeux partagés. Les 9 autres se traitent par exception (tableau ci-dessus).
- **Vérifié en local** : lecture par l'API du plugin, rendu du front, régénération du fichier public, retour à l'état d'origine à l'octet près.
- **Reste pour la Phase 2** : écriture du jeu partagé (stocker une fois, pas seulement composer à la lecture) ; écrans « Matières » et « Modèles » pour Valérie ; version de la texture par groupe de modèles (§10) ; fiches atypiques ; comportement des commandes passées (identifiants de choix conservés, à vérifier en recette).
- **Plugin 2.0.0** : non testé ; non nécessaire pour conclure. Il remplacerait le petit plugin par les configurateurs globaux natifs (migration automatique à tester sur copie avant toute mise à jour).
- **Limites** : le plugin `Sync MKL…` de VIMAWEB (dev seulement) n'a pas été lu ; les liserés et surpiqûres n'ont pas de version de texture déterminable ; test sur la copie locale reconstruite, pas sur la production.

### Décision sur les raccords après examen visuel (Melvin, 15/10, soir)

Constat de Melvin sur la planche : seuls le Violet et le Marron (cuirs) fonctionnent avec le fondu ; pour le reste, le recadrage sur périodes entières donne un meilleur résultat visuel. Vérifié au zoom ×4 sur la jonction entre tuiles (`essais-poste3/raccords/zoom-jonction.png`) :

| Matière | Brut | A (périodes entières) | B (fondu) |
|---|---|---|---|
| Fiber blanc | couture nette | **sans couture** | légère cassure |
| Noir strié | léger saut | **sans couture** | léger saut |
| Gris fiber argent | rayures verticales propres au tissage | idem | idem |
| **Noir quadrillé** | couture | **couture encore visible** | continu, motif un peu brouillé |

Règle retenue : **cuirs → fondu (B)** ; **tissages réguliers (perforé, strié, Fiber blanc) → recadrage (A)** ; Fiber argent et anthracite → brut. **Noir quadrillé : cas à part**, aucune des deux méthodes n'est parfaite ; à traiter si nécessaire par un assemblage de morceaux (« quilting »), non testé. Mon choix de B pour le quadrillé dans le tableau de la §11 se fondait sur la mesure de couture et ne tient pas compte du brouillage du motif.

**Le raccord ne s'applique que sans texture maître** : nouvelle matière dont on n'a que la petite image de 171 px. Avec une photo plein cadre (1920 × 1280 ou plus, à l'échelle 1:1), il n'y a rien à répéter, donc aucun raccord.

## 12. Poste 3 : compléments (15/10, soir) : cas sans texture maître, zone non couverte, photo d'une texture maître, raccords

### L'idée en langage simple

Valérie a, pour chaque matière, **un grand rouleau de tissu** (la texture maître) et, pour chaque modèle, des **gabarits** (la forme de l'assise, du bec, des bandeaux). Elle pose le gabarit sur le tissu et découpe : c'est le calque. Le même rouleau sert pour tous les modèles. Nous n'avons pas le rouleau lui-même : nous l'avons **reconstitué en recollant les morceaux déjà découpés** dans les calques de tous les modèles.

### Comment la texture maître a été construite

Elle est construite avec les **calques finis** des modèles existants (chaque pixel est copié d'un calque), **pas** avec la petite image de 171 px. La petite image a servi à comprendre qu'une grande texture partagée existe : on la retrouve pixel pour pixel (corrélation 0,999) dans les calques de dizaines de modèles, donc c'est un extrait de cette grande texture.

```
petite image 171 px  ← extrait de →  texture maître (grande image)
                                      reconstituée depuis les calques finis
```

### Les 30,7 % non couverts : du vide

La texture maître couvre **69,2 %** du canevas de 1920 × 1280. Ce qui reste a été classé pixel par pixel avec les photos de base et les ombres de tous les modèles (planche `essais-poste3/zone-non-couverte.png`).

| Contenu du canevas | Part |
|---|---|
| Couvert par la texture maître (silhouette des 43 modèles réunis) | 69,2 % |
| **Fond vide hors silhouette** (marges autour des selles) | 30,6 % |
| Petits trous à l'intérieur de la silhouette (63 trous, le plus grand de 1 305 px) | 0,2 % |
| Partie de selle non texturée | ≈ 0 % |

La boîte englobante de toutes les selles tient dans x 25 → 1901, y 55 → 1218. **Aucune selle n'apparaît dans les 30 %**, ce qui corrige le risque que j'avais noté (§10). Le risque restant est étroit : un modèle photographié avec un **cadrage très différent** de ceux d'aujourd'hui. Les 0,2 % de trous fins se comblent par interpolation des voisins.

### Les cas où il n'y a pas de texture maître

| # | Cas | Pourquoi | Conséquence |
|---|---|---|---|
| 1 | **Une nouvelle matière** | Aucun calque existant ne la porte, donc rien à assembler | Photo plein cadre (voir plus bas), ou à défaut sa petite image répétée avec raccord |
| 2 | Une partie du canevas jamais utilisée | 30,6 % de vide, sans selle | Aucune action tant que le cadrage de prise de vue reste le même |
| 3 | Les matières réservées aux liserés (« Argent brillant », « Rouge brillant », « L'argent Chrome », « Vert brillant »…) | Trop glissantes pour les assises ; le jeu des liserés compte 44 choix contre 37 pour les surfaces | Pas de texture maître et pas besoin : fines lignes de couleur unie |

Les 39 matières de surface analysées ont toutes une texture maître reconstituée.

### Le raccord : seulement sans texture maître

Pour remplir une zone de 700 px avec une image de 171 px, on la répète comme un carrelage. Entre deux carreaux, une **couture** apparaît si les bords ne s'ajustent pas. Le raccord est la façon de la faire disparaître.

| Situation | Raccord ? |
|---|---|
| Matière existante (texture maître 1920 × 1280) | **Non** : on découpe dans une grande image, rien n'est répété |
| Nouvelle matière avec une **photo plein cadre** (1920 × 1280 ou plus, échelle 1:1) | **Non** : c'est une vraie texture maître |
| Nouvelle matière avec **seulement sa petite image de 171 px** | **Oui** |

Colonnes de la planche des raccords (`essais-poste3/raccords/raccords-Selle-KTM-Duke.jpg`, carré de 342 px, soit environ 2 × 2 tuiles) : **réel** = extrait du vrai calque du KTM Duke (référence) ; **plain** = la petite image répétée telle quelle ; **A** = recadrée sur un nombre entier de périodes puis répétée ; **B** = fondue avec une copie d'elle-même décalée de moitié puis répétée. Chiffres : « raccord » = visibilité de la couture (1,0 invisible) ; « écart » = écart moyen au réel sur 255, sensible à la phase du motif, donc secondaire devant le jugement visuel.

### Photographier une texture maître pour une nouvelle matière

C'est la meilleure solution pour une nouvelle matière texturée : même procédé que Valérie, aucune répétition, donc aucun raccord.

| Point | Consigne |
|---|---|
| Taille | Image d'au moins **1920 × 1280 px**, l'étoffe remplit tout le cadre, sans pli |
| Échelle | Même taille de tissage à l'écran que les matières existantes (voir ci-dessous) |
| Prise de vue | De face, à plat, lumière rasante (≈ 15 à 30° au-dessus de la surface), sans flash |
| Lumière | Même direction pour toutes les matières |
| Couleur | Charte grise dans le cadre, balance des blancs fixée |

**Calibrer l'échelle** : photographier d'abord une matière déjà connue (par exemple le Fiber blanc) avec le même réglage, comparer son tissage à sa texture maître reconstituée pour obtenir l'agrandissement, puis photographier les nouvelles matières au même réglage.

**Valider avant de s'engager** : photographier deux matières connues (Fiber blanc et Violet), construire leurs calques avec la photo et les comparer à ceux de Valérie. Si l'écart est du même ordre que celui des matières existantes entre elles, le protocole est bon.

**Non testé** : le temps de prise de vue, et le smartphone (probablement suffisant).

### Test sur selles : réel, texture maître, raccord (15/10, soir)

Trois rendus de la même selle, deux combinaisons par modèle (script `poste3_selles_raccord.py`, images `essais-poste3/selles-raccord/`) :
- **réel** : les calques du modèle ;
- **texture maître** : zones de surface régénérées avec la texture maître construite sans ce modèle ;
- **raccord** : zones de surface remplies avec la **petite image de 171 px** répétée, méthode retenue par matière (A pour les tissages réguliers, B pour les cuirs, brut sinon ; Noir quadrillé forcé sur A). La tuile est posée à un décalage fixe, sans jamais regarder le réel.

| Modèle | Combinaison | Texture maître : pixels identiques (écart moyen sur 255) | Raccord : écart moyen sur 255 |
|---|---|---|---|
| KTM Duke (version récente) | 1 | **100 %** (0,00) | 11,9 |
| KTM Duke | 2 | **100 %** (0,00) | 10,7 |
| BMW R 1150 RT (ancienne version) | 1 | 77,6 % (2,6) | 11,5 |
| BMW R 1150 RT | 2 | 69,0 % (3,4) | 10,7 |

**Lecture** : à l'échelle de la selle, les trois rendus sont indiscernables. Au zoom sur les assises, la **texture maître** est la plus proche du réel ; le **raccord** garde le bon tissage et la bonne couleur mais avec un grain légèrement différent, et des jonctions verticales visibles sur le Noir quadrillé. L'écart moyen du raccord (≈ 11 sur 255) est environ 3 à 4 fois celui de la texture maître sur une ancienne version, et il vient surtout du décalage des motifs. C'est un plan B correct pour une nouvelle matière sans texture maître, pas un équivalent.

![[poste3-selle-raccord-ktm-duke.jpg]]
![[poste3-selle-raccord-bmw-r1150rt.jpg]]

**Précision sur le Noir quadrillé (15/10, soir)** : le Noir quadrillé est une matière existante, donc il a sa texture maître et ne demande **aucun raccord**. Il n'a servi que de **cas d'essai** du plan B (une matière à motif irrégulier). La seule limite qui en ressort concerne une **nouvelle matière** de même genre, livrée avec sa seule petite image de 171 px : le raccord ne serait pas parfait. Ce n'est pas un point à traiter pour le catalogue actuel.

### Copie du site local avec le regroupement en place (15/10, nuit)

Pour garder `sellerie-confort.local` fidèle à la production, le regroupement par famille est mis en place sur **une copie séparée** : même plugin (**Product Configurator 1.7.6, non modifié**), même thème, mêmes données de départ.

| Élément | Valeur |
|---|---|
| Adresse | `http://127.0.0.1:8090` (serveur PHP intégré, accessible seulement depuis ce poste) |
| Dossier | `C:\Users\LENOVO\sellerie-confort-regroupement\public` (cœur WordPress, plugins, thème, mu-plugins copiés) |
| Base | `sc_regroupement`, copie des 52 tables (345 produits), **séparée** de la base `local` |
| Médias | Dossiers `2022` à `2026` reliés au site local d'origine (jonctions), **aucune duplication** de 5 Go ; le dossier du fichier de configuration public est propre à la copie (pas de pollution du site d'origine) |
| Regroupement | mu-plugin `sc-regroupement-test.php` en mode **`famille` sur toutes les fiches** (option `sc_test_mode`) : 7 familles en en-têtes de liste, 57 groupes sur la Z900, fichier public de 162 107 octets contre 156 545 à l'origine |
| Repère visuel | Barre d'administration rouge et mention « COPIE REGROUPEMENT » |
| Lancement | `Phase 1/scripts/copie_regroupement_lancer.ps1` (le site Local d'origine doit être démarré : sa base héberge aussi `sc_regroupement`) |

Vérifications : page produit en HTTP 200, groupes affichés dans le configurateur (en-têtes « LES NOIRS », « LES GRIS »…), fichier public d'origine du site local resté à 156 545 octets.

**Ce que la copie n'est pas** : le jeu partagé n'est pas encore stocké une seule fois (la composition se fait à la lecture) et aucun écran de gestion n'existe pour Valérie. Les 9 fiches atypiques restent telles quelles.

### Quelles images demain : originales ou générées ? (15/10, nuit)

Règle proposée pour la Phase 2 : **les images d'origine ne sont jamais remplacées**. On génère seulement ce qui n'existe pas encore. Un même configurateur mélange donc images d'origine (matières historiques) et images générées (ajouts).

| Cas | Images utilisées | Pourquoi |
|---|---|---|
| **Ancien modèle, matières existantes** | **Originales**, inchangées | Déjà faites par Valérie et validées. Les régénérer n'apporte rien : au mieux identique, au pire une autre version. |
| **Nouveau modèle, matières existantes** | **Générées** (masques du modèle × texture maître) | Les images n'existent pas encore. C'est le gain de temps de Valérie. |
| **Ancien modèle, nouvelle matière** | **Générées**, pour la nouvelle matière seulement | La matière n'existe sur aucun calque : il faut une image par zone de chaque modèle. |
| **Nouveau modèle, nouvelle matière** | **Générées** | Idem |

**Pourquoi ne pas régénérer l'existant**
- Pas de gain : pour 18 matières sur 39, la régénération est identique à l'original au pixel près.
- Risque de version : pour 21 matières, les modèles d'avant 2023/01 portent une version plus ancienne de la texture ; la version récente les changerait.
- Risque d'écart visuel sur les matières texturées, que le test à l'aveugle n'écarte pas entièrement.

**Volume pour une nouvelle matière** : une image par zone de surface de chaque modèle. Les 345 fiches ne portent que 302 listes d'images distinctes et beaucoup de modèles partagent leurs masques ; le nombre réel de fichiers est de l'ordre de la centaine ou de quelques centaines, **à chiffrer**.

**À trancher**
- L'écart acceptable pour mélanger images d'origine et générées dans une même fiche (aujourd'hui : ΔE médian de 2 à 3 pour la couleur).
- La validation par Valérie, matière par matière, avec une planche de comparaison, avant publication (recommandée).


## 13. Poste 3 : points de clôture (15/10, soir)

Les photos de matières réelles (validation d'une texture maître photographiée) sont **reportées à la Phase 2** : Melvin n'a pas les matières avec lui.

### Version de texture par modèle (43 modèles, 21 matières à deux versions)

Chaque zone de surface de ces matières est comparée à la texture maître récente (pixels identiques). Fichier : `Phase 1/essais-poste3/version-par-modele.csv`.

| Version utilisée | Nombre | Modèles |
|---|---|---|
| **Récente** (≥ 95 % des zones identiques à la texture récente) | 23 | KTM Duke, Piaggio MP3, Suzuki GSX S 1000, Honda Goldwing 1500, Honda Goldwing 1800, Honda Goldwing 1800 2Parts, Honda CB 650 R, Honda CBF, Honda CBR 1000 F, Honda CBR 900 2Parts, Honda CTX, Honda Integra, Suzuki Hayabusa, Suzuki SV 2Parts, Yamaha MT 07 2Parts, Yamaha MT 09 Tracer, Yamaha MT 09 Tracer 2Parts, Yamaha TDM 850, Yamaha TDM 900, Yamaha FJR 1300 2001, Yamaha FJR 1300 2005, Yamaha FZ8 2Parts, Yamaha T Max |
| **Ancienne** (≤ 15 % identiques ; 9,5 % correspond aux 2 matières sur 21 qui n'ont pas changé) | 18 | BMW R 1200RT, Dorsoduro 750, Ducati Diavel, Piaggio MP3 av 2014, BMW C650 GT, BMW GS LC, BMW K 1600 GTL, BMW R 1150 RT, BMW R 1200 RT LC, BMW S 1000 R, BMW S 1000 R 2Parts, BMW XR 1000, Kawasaki Z 750 1000 2Parts, Kawasaki Z 900, Suzuki GSX S 2Parts, BMW R 1200 GS, Suzuki GSR 600, Honda VFR VTEC |
| **Mixte** | 2 | Honda Africa Twin, Honda Shadow (77 % et 87 % de zones récentes) |

**Tendance par époque d'envoi** (dossier d'upload) : jusqu'à 2023/06, 3 modèles récents sur 21 ; **depuis 2023/07, 20 sur 22** ; **depuis 2023/10, 10 sur 10**. Cela appuie la règle « version récente par défaut pour un nouveau modèle », sans la confirmer avec Valérie (pas de mail).

### Liserés : la couleur se déduit de la vignette, avec une exception métallique

Correction de ce que j'avais écrit au §12 : les liserés ne sont **pas** de fines lignes. Le calque d'un liseré couvre une surface médiane de **≈ 16 000 px**, avec une couleur presque unie (écart-type médian 4,3 à 5,3 sur 255).

| Mesure (Z900 et KTM Duke, 44 liserés, un choix laissé de côté) | Résultat |
|---|---|
| ΔE médian de la couleur déduite de la vignette | **2,8 à 2,9** |
| Part des liserés à ΔE ≤ 5 / ≤ 10 | **93 %** / **98 %** |
| Moins bien déduits | Or pailleté (12,1 à 12,5), Or (6,9 à 7,1), Gris souris (5,5), Gris fiber argent (5,0), Marron (4,7 à 4,8) |
| Les plus texturés | Or pailleté, Gris argent chromé, Or, Gris fiber argent (écart-type 15 à 26) |

**Règle** : liserés unis → couleur de la vignette ; liserés métalliques ou pailletés (Or pailleté, Or, Argent chromé, Gris fiber argent) → on garde leurs fichiers actuels (ils ont une vraie texture, pas de texture maître construite pour eux).

### Démonstration dans le vrai configurateur local

Procédure testée sur le KTM Duke (produit 10169), site local uniquement :

1. génération des 6 calques de surface de « Violet » depuis la texture maître et les masques du modèle (identiques à 100 % aux originaux, couverts à 100 %) ;
2. enregistrement comme nouvelles pièces jointes ;
3. retrait puis recréation du choix « Violet » avec ces images ;
4. le plugin a **régénéré lui-même** son fichier de configuration public avec les 6 nouvelles images ;
5. dans l'interface, la sélection « Assises avant : Violet » affiche le calque `Selle-KTM-Duke-assise-av_38_Violet-MAITRE.png` sur la selle.

Le site local a été **remis dans son état d'origine** (configuration restaurée, pièces jointes de démonstration supprimées). Scripts : `poste3_demo_generer.py`, `poste3_demo_enregistrer.php`. Ce que ça prouve : le chemin « générer les images puis les enregistrer dans le plugin » fonctionne ; il reste à construire l'outil qui le fait en un geste (Phase 2).

### Points restants du poste 3

| Point | Statut |
|---|---|
| Photo plein cadre d'une matière réelle (Fiber blanc, Violet) | **Phase 2** (matières non disponibles) |
| « Version récente » comme défaut | Appuyée par la tendance par époque ; **non confirmée** par Valérie |
| Raccord pour une nouvelle matière sans texture maître | Plan B décrit (§11 et §12) |

### Test de la 2.0.0 sur la copie « regroupement » (15/10, nuit)

**Procédure** (copie `127.0.0.1:8090` uniquement, jamais le site local d'origine ni la production) :
1. Instantané de la base de la copie : base `sc_regroupement_v1_7_6` (52 tables, 345 produits).
2. Sauvegarde des fichiers du plugin 1.7.6 : `sellerie-confort-regroupement\_sauvegarde\`.
3. Mise à jour par WP-CLI depuis le dépôt officiel (`downloads.wordpress.org/plugin/product-configurator-for-woocommerce.2.0.0.zip`).
4. Mesure de l'état des données avant et après (`scripts/etat_configurateur.php`, résultats dans `essais-v2/`).

| Mesure | 1.7.6 (avant) | 2.0.0 (après) |
|---|---|---|
| Fiches configurables | 345 | 345 |
| Clés de méta et nombre de lignes | 5 clés × 345 | identiques |
| Poids des données (contenu) | 56 801 838 octets | **identique** |
| Lecture par l'API du plugin (Z900) | 10 calques, 351 choix, 57 groupes | **identique** |
| Filtre `mkl_pc/db/get` (regroupement) | présent | **présent** |
| Fichier de configuration public | 162 107 octets, 57 groupes | 162 492 octets, 57 groupes, **plus un fichier `.json`** |
| Front : choix rendus et en-têtes de famille | 292 / 57 | 292 / 57 |
| Erreurs du navigateur | 12 adresses numériques `0.0.66.x` | **les mêmes sur le site local 1.7.6** : bruit préexistant |
| Administration de la fiche | fonctionne | fonctionne ; nouveautés « Configurator source », « Configurator type », « Global Layers » |

**Ce que fait la migration** (lecture de `inc/update.php` de la 2.0.0) : elle ajoute deux réglages par défaut (`fe_3d_use_draco_loader`, `purge_with_page_cache`) et reprend le mode d'enregistrement des images de configuration (`save_images`). **Elle ne convertit aucune donnée de produit.** Les deux types de contenu `mkl_global_layer` et `mkl_pc_global_config` sont créés mais vides.

**Correction** : la notice du dépôt (« les données passent à un nouveau format, converties automatiquement ») m'avait fait écrire qu'un retour arrière exigerait de restaurer la base. Pour cette mise à jour, **ce n'est pas le cas** : le retour arrière consiste à remettre les fichiers de la 1.7.6, l'option `mkl_pc__settings` et l'option `mkl_pc_version`. L'instantané de la base reste une précaution. Ce qu'une **première sauvegarde faite dans l'éditeur 2.0** écrit dans les fiches n'est pas testé.

**Non testé** : l'usage des configurateurs et couches globaux ; l'enregistrement dans l'éditeur ; des commandes factices ; l'outil « Purge + Tag » (inactif dans la copie) ; les performances ; la compatibilité du thème personnalisé ; les fonctions 3D.

**Conséquence pour le plan** : la 2.0.0 est compatible avec le regroupement testé sur la 1.7.6 (même filtre, mêmes données, même rendu). Le passage en production reste à décider avec Valérie et ne dépend pas du regroupement.


## 14. Passer sur la 2.0.0 et écran de gestion : tests sur la copie et prototype (16/10)

Tout ce qui suit a été fait **sur la copie « regroupement »** (`127.0.0.1:8090`), jamais sur le site local d'origine ni sur la production. Les commandes sont des commandes factices, supprimées à la fin.

### 14.1 Test des commandes passées (1.7.6 contre 2.0.0)

Méthode : commandes créées par le **vrai chemin du plugin** (ajout au panier puis création de commande WooCommerce), l'une avec les fichiers de la **1.7.6** (sauvegarde remise temporairement), l'autre avec la **2.0.0** ; puis modification du catalogue de la fiche Z900 ; relecture. Scripts : `scripts/poste1_test_commandes*.php|ps1`, journaux dans `essais-v2/`.

| Ce qu'on relit | Modification du catalogue | 1.7.6 | 2.0.0 |
|---|---|---|---|
| **Page de la commande dans l'administration** (ligne « Configuration ») | renommage, retrait d'un choix, renumérotage des identifiants | identique | identique |
| **« Commander à nouveau »** (la configuration est reconstruite) | renommage d'une matière | **le nom change** | **identique** |
| idem | retrait d'un choix | **le choix et son image sont perdus** | **identique** |
| idem | renumérotage des couches et des choix | **la couche et le choix sont perdus** | **identique** |

Lecture :
- La commande enregistre déjà, sous les deux versions, le nom, la couche et l'identifiant d'image au moment de l'achat : l'affichage dans l'administration ne bouge pas.
- Ce que la 1.7.6 ne protège pas, c'est la **reconstruction** d'une configuration à partir d'une commande (« Commander à nouveau »), qui relit le catalogue **actuel**. La 2.0.0 s'appuie sur les données enregistrées.
- **La protection vaut aussi pour les commandes passées sous 1.7.6** : leurs lignes contenaient déjà le nom, la couche et l'image ; la 2.0.0 s'en sert. Une mise à jour protège donc l'historique existant, sans migration.
- Limites : commandes factices sur une copie, une fiche. Les vraies commandes (5 437) restent hors périmètre ; courriels, factures PDF et bons de commande non testés.

### 14.2 Configurateurs globaux sur la copie

| Mesure | Résultat |
|---|---|
| Configurations distinctes parmi les 345 fiches | **55** (empreinte du contenu, des couches et des angles) |
| Configurateurs globaux créés | **55**, 345 fiches rattachées, 0 erreur |
| Lecture après rattachement, données locales conservées | **345 / 345 identiques** à la référence |
| Lecture après **purge des données locales** de chaque fiche | **345 / 345 identiques** : la lecture passe bien par le global |
| Modification faite **une fois** dans le global G06 | visible sur **19 fiches sur 19**, retour à l'identique à l'annulation |
| Écriture par `DB::set()` en ligne de commande | **abîme le global** (contenu écrit par morceaux sans l'index de finalisation, lecture impossible) : réparé depuis la sauvegarde. Écrire au format bloc JSON utilisé à la création, ou passer par l'éditeur du navigateur. |

À retenir : le natif partage bien les fiches, mais **n'offre rien pour agir sur les 55 configurateurs à la fois**.

### 14.3 L'écran de gestion : ce que le natif ne fait pas

| Besoin | Natif 2.0.0 | Écran de gestion |
|---|---|---|
| Une configuration partagée par plusieurs fiches | Oui (configurateur global) | Non nécessaire |
| Modifier une fois pour tout un groupe | Oui (« Edit original ») | Non nécessaire |
| Commandes passées protégées | Oui | Non nécessaire |
| **Renommer une matière partout** | Non : 55 configurateurs à ouvrir | **Oui** |
| **Désactiver une matière partout** | Non | **Oui** |
| **Familles de matières** (7, issues de la page « Matières ») | À recréer à la main dans chacun des 55 | **Oui**, définies une fois |
| **Ajouter une matière à tous les modèles** (images comprises) | Non : une image par zone et par configurateur, à la main | **Oui**, génération par lots |
| Vue d'ensemble : où est utilisée telle matière | Non | **Oui** |

### 14.4 Le prototype : plugin « Gestion du configurateur »

Dossier : `Phase 1/plugin-gestion/sc-gestion-configurateur/` (un seul fichier PHP), tests dans `plugin-gestion/tests/`, notice `plugin-gestion/README.md`. Menu « Configurateur SC » dans l'administration, droit `manage_woocommerce`.

| Écran | Fonction | Résultat des tests |
|---|---|---|
| **Matières et couleurs** | Catalogue des matières (par nom normalisé), filtres matières / fils de surpiqûre et par famille, renommage, famille, activation, nombre de fiches concernées | **19 / 19** : affichage, enregistrement, effet côté visiteur (renommage sur 7 couches, matière masquée, matière déplacée de famille), retour à l'état initial |
| **Modèles et calques** | Les 55 configurateurs globaux, leurs fiches, leurs couches, listes atypiques, liens vers l'édition native | affichage vérifié, aucune erreur |
| **Ajouter une matière** | Nom, famille, matière unie (couleur) ou texturée (petite image) ; une image par zone et par configurateur, générée à partir du masque ; barre de progression ; annulation | matière unie **18 / 18**, matière texturée **14 / 14** (voir 14.5) |

Principe : renommages, activations et familles sont appliqués **à la lecture** (aucune donnée de fiche réécrite). Seul l'ajout d'une matière écrit, dans les configurateurs globaux, avec une sauvegarde par configurateur et une annulation. L'éditeur d'administration du plugin ne reçoit jamais de données composées.

### 14.5 Ajout d'une matière : résultats et qualité des images générées

**Fonctionnement mesuré** : 55 configurateurs traités, **304 images** de 1920 × 1280 générées en **170 à 190 s** (environ 0,6 s par image), vignette incluse, matière visible côté visiteur sur toutes les zones concernées, familles toujours en groupes natifs (56), annulation : 350 noms avant, 350 après, matière disparue, comparaison de lecture **345 / 345** à la référence à la fin de tous les essais.

**Qualité** : même zone (« Assises Fiber blanc », Z900), image générée à partir d'une petite image 171 px, comparée à l'image réelle de la boutique.

| Entrée fournie | Masque | Écart moyen | Couleur moyenne | Énergie de texture (générée / réelle) | Aspect |
|---|---|---|---|---|---|
| **Carré 171 px de la vraie matière**, raccords atténués | identique (IoU 1,000) | 13,5 / 255 | **identique** | 11,5 / 12,9 | quasi indiscernable ; un fin trait vertical subsiste à certains raccords |
| Même carré, sans atténuation | identique | 14,0 / 255 | identique | 13,0 / 12,9 | raccords visibles tous les 171 px |
| **Vignette rééchantillonnée depuis un JPG de 750 px** (ombrée), raccords atténués | identique | 11,8 / 255 | **+4 niveaux (plus clair)** | 6,5 / 12,9 | grain adouci, teinte un peu claire |

Lecture :
- **La qualité dépend surtout de l'image fournie**, pas du moteur : un vrai carré de la matière à l'échelle 1 donne le même rendu que l'image réelle (masque, couleur) ; une vignette ombrée ou rééchantillonnée donne une matière plus lisse et un peu plus claire.
- L'option « Atténuer les raccords » (cochée par défaut) retire l'éclairage lent de la petite image puis fond la tuile avec sa version décalée. Elle supprime le quadrillage dû à l'éclairage ; il reste, sur certains motifs, un trait fin au raccord. Elle adoucit légèrement le grain (énergie 11,5 au lieu de 13,0).
- Planches : `attachments/gestion-qualite-generee-vs-reelle-vraie-tuile.png` et `gestion-qualite-generee-vs-reelle-entree-degradee.png` (à gauche générée, à droite réelle).
- Pour une matière à fort relief (cuir, carbone), ce traitement ne remplace pas la texture maître de la boutique : la décision est à prendre matière par matière (voir §12).

### 14.6 Défauts trouvés en test, corrigés

| Défaut | Cause | Correction |
|---|---|---|
| Une fiche rendue illisible après écriture en ligne de commande | `DB::set()` écrit en morceaux sans index | Écriture au format bloc JSON ; réparation depuis la sauvegarde |
| Caractères accentués abîmés (`é` devenu `u00e9`) après une annulation | Sauvegarde enregistrée sans `wp_slash` | Sauvegarde et écriture avec `wp_slash` ; global réparé, 345 / 345 vérifié |
| « Violet » mélangeant matière et fil de surpiqûre | Identité sans distinction de type | Préfixe `fil-` pour les fils |
| Catalogue gonflé (152 puis 231 identités) | Préfixes de zone non retirés | Liste de préfixes dans `decouper()` |
| Écran d'administration du plugin recevant des données composées | Filtre appliqué aussi à l'éditeur | Garde : composition seulement côté visiteur (`fe=1`) |
| Page d'administration inaccessible sur la copie | Routeur ne traitant pas `wp-admin/` | Routeur corrigé |

### 14.7 Limites et suite

- Prototype validé **sur une copie uniquement** : aucune recette sur préproduction, aucune compatibilité vérifiée avec le thème Divi personnalisé ni avec l'enregistrement dans l'éditeur 2.0.
- Un seul ajout suivi à la fois ; catalogue reconstruit à la demande (~15 s) ; fiches à liste atypique laissées telles quelles si moins de la moitié des matières sont reconnues.
- L'hébergement (VIMAWEB) reste à traiter : l'installation du plugin et le passage en 2.0.0 en production sont des décisions de Phase 2, hors périmètre de la Phase 1.
- **Pour la Phase 2** : recette de l'ajout de matière sur une vraie préproduction ; fournir à Valérie un protocole pour la petite image (vrai carré à l'échelle réelle, sans ombre) ; chiffrer l'écran de gestion (le prototype couvre déjà les trois écrans, reste l'ergonomie et la recette).


### 14.8 Nouvelles matières : carré répété ou texture maître, et quelle photo demander à Valérie (16/10)

**Ce qui est utilisé aujourd'hui**
- **En production** (Product Configurator, 1.7.6) : aucune image n'est générée ni répétée. Le plugin affiche des images de 1920 × 1280 px préparées hors du site (une par matière, zone et modèle, par exemple `Selle-Kawasaki-Z-900-assise-av_37_Fiber-Blanc.png`) et téléversées à la main, à partir de textures maîtres et de masques. **Correction après l'appel du 16/10 (voir 14.9)** : selon Valérie, ces images ont été faites à partir de petites images de matière répétées (par Samuel, il y a environ 13 ans) ; la « texture maître » des §11 à 13 est une reconstitution équivalente, pas un fichier d'origine. La petite vignette de la matière ne sert qu'à choisir.
- **Dans le prototype de gestion** (copie locale seulement) : le carré de 171 px fourni est **répété en carrelage** sur le cadre, puis découpé par le masque de chaque zone. Il ne sait pas lire une grande photo comme texture maître.

**Deux façons d'apporter une nouvelle matière**

| | Petit carré répété (prototype) | Large bout de matière = texture maître |
|---|---|---|
| Principe | Un carré de 171 px répété en carrelage | La photo, mise à l'échelle, remplit le cadre |
| Raccords et répétition | Possibles ; atténuées par un fondu, un trait fin peut rester | **Aucun** |
| Matière nécessaire | Quelques centimètres | Un bout couvrant la plus grande zone à l'échelle |
| État | Fait et testé (§14.5) | **À construire** (choix de zone, mise à l'échelle) |

Logique proposée pour la Phase 2 : si la photo couvre la plus grande zone à l'échelle, utiliser la texture maître ; sinon prendre le plus grand carré propre et le répéter avec le fondu. Une texture maître donne le même résultat pour tous les modèles : le découpage par les masques fournit les 304 images.

**Taille du bout de matière**
- Mesure : sur la Z900, la zone « Assises » occupe **844 × 555 px** dans le cadre de 1920 × 1280. Il suffit de couvrir la plus grande zone : les autres zones (bandeaux, liserés, bandes) peuvent prendre d'autres morceaux de la même photo, à la même échelle. Seule la Z900 est mesurée ; les autres modèles restent à vérifier.
- En centimètres, il faut une **cote réelle** d'une selle (longueur ou largeur d'assise). Exemple, à titre d'hypothèse non mesurée : si 844 px valent 40 cm, cela fait environ 21 px/cm, soit un bout d'environ 40 × 26 cm au minimum, 50 × 35 cm avec de la marge.
- Un échantillon de fournisseur de 10 × 10 cm ne suffit pas pour une texture maître ; il suffit pour le carré répété.

**Photographier la matière**
- Avec un téléphone récent (environ 4000 × 3000 px), un bout de 50 × 35 cm photographié en plein cadre donne environ 80 px/cm, soit environ 4 fois le détail nécessaire (hypothèse de 21 px/cm) : l'image sera réduite, il n'y a pas de manque de détail.
- Les vraies limites : netteté (trépied), appareil bien à plat (sans perspective), cadrer large et n'utiliser que le centre (déformation des bords), lumière douce et régulière sans reflet (les matières brillantes ou métallisées sont les plus difficiles).
- Si le bout est trop grand : scanner à plat (A4 ou A3), ou plusieurs photos assemblées (non testé).
- L'**échelle** reste à fixer : une règle visible dans la photo, ou un réglage avec aperçu sur une selle. Le prototype ne gère que l'échelle 1.

**Non testé** : aucune photo réelle prise au téléphone, aucune texture maître construite par le plugin, mesure de la plus grande zone sur les autres modèles, calibrage px/cm avec une cote réelle.

## 15. Voie A : habiller le plugin sur la copie, ce que ça donne (16/10)

Test sur la copie (`http://127.0.0.1:8090`, base `sc_regroupement`, plugin `mkl_pc` **2.0.0** actif, familles déjà dans les données). Fichiers : `Phase 1/habillage-configurateur/` (`sc-habillage-configurateur.php`, `habillage.css`, `habillage.js`, `habillage-familles.js`), polices dans `Maquette/assets/fonts/`. Rien en ligne.

### Ce qui fonctionne (vérifié à l'écran et par script)

| Élément de la maquette | Résultat |
|---|---|
| Configurateur **dans la fiche produit**, à la place du bouton plein écran | Oui : shortcode natif `[mkl_configurator]` injecté sur la fiche, bouton masqué, pleine largeur (1200 px centré) malgré la colonne étroite de Divi |
| Selle à gauche, panneau de 470 px à droite, pied sous les deux | Oui (grille CSS) |
| Couleurs et polices de la maquette (bleu `#1b478a`, Zilla Slab, Archivo, fil de couture pointillé) | Oui |
| Liste des zones, grille de vignettes à 4 colonnes, matière active entourée en pointillé | Oui |
| **Familles en onglets avec compteurs** (Noirs 8, Gris 6, Bleus 6, Rouges 4, Orangés/Jaunes 5, Verts 3, Autres 5) | Oui, à partir des groupes natifs |
| **Annuler / Refaire / Tout réinitialiser** | Oui (testé : choix → 1/8, annuler → 0/8, refaire → 1/8, réinitialiser → 0/8) |
| **Comparer** (maintenir pour voir la configuration d'origine) | Écrit ; non testé à la souris |
| **Partager** : lien avec la configuration dans l'adresse, rechargé à l'ouverture | Oui (testé : un lien à 3 zones en Violet les applique et le compteur affiche 3/8) |
| Compteur « n / 8 zones personnalisées », étiquette de la matière choisie | Oui |
| Noms de matières raccourcis (sans le préfixe de zone) | Écrit ; non vérifié visuellement |
| **Champs d'options** (broderies, hauteur d'assise, gel, infos client) de même largeur et de même style | Oui, mais **sous** le configurateur, pas dans le panneau |
| Mobile (une colonne, sans débordement horizontal) | Oui ; le panneau garde une hauteur fixe |
| Ajout au panier | Bouton du plugin restylé (bleu) ; **non testé** jusqu'au panier |

Le plugin se pilote par des événements souris complets (un `.click()` seul ne suffit pas) ; il expose aussi `reset_configuration` et `select_choice`.

### Ce qui n'est pas fait (reste de la maquette)

1. **Étapes Broderies, Options, Informations dans le panneau** : les champs APF restent en dessous. Les déplacer dans le panneau garde à faire : règles conditionnelles, champs obligatoires, navigation entre étapes.
2. **Total combiné** avec les surcoûts APF (+10 €, +35 €…) : le plugin affiche le prix de base, APF les surcoûts à part.
3. **Récapitulatif** en tiroir : non fait.
4. **Mobile en feuille qui se déplie par le bas** : non fait ; seule la mise en une colonne l'est.
5. Quelques finitions au pixel (vignettes, espacements) : à comparer à la maquette.

### Lecture

La voie A donne **la structure, le style et les outils de la maquette** pour le choix des matières, avec peu de code (un mu-plugin, ≈ 16 Ko de CSS, ≈ 8 Ko de JavaScript). Elle ne donne pas encore **le parcours en quatre étapes** : c'est là que se concentre le reste de l'effort, et la voie B (interface maison branchée sur le plugin) devient plus pertinente si ce parcours est un impératif.

### Réserves

- Testé sur la **2.0.0** (version de la copie), pas sur la 1.7.6 de la prod ; la structure du configurateur intégré est la même sur les deux d'après l'inspection.
- Un seul produit (KTM Duke), un seul navigateur (celui de l'application), taille mobile émulée.
- Les pages de test ont été supprimées ; les fichiers sont dans un mu-plugin de la copie, pas sur le site local principal.


### 14.9 Appel avec Valérie (16/10) : ce qu'elle a dit et ce que ça change

**Ce que Valérie a dit** (notes de Melvin, appel téléphonique ; certains points sont donnés « probablement » ou « je ne suis pas sûr »)
- Les images de matières sont faites à partir de **petites images (vignettes) répétées** pour « patcher » les calques. Pas de textures maîtres photographiées au départ. C'est **Samuel**, le premier développeur, qui l'a fait il y a environ **13 ans**, pour quasiment toutes les matières.
- Il n'y a **pas eu de nouvelle matière depuis plusieurs années** (à confirmer). Une matière « ajoutée en 2025 » n'a pas été photographiée en 2025 : les dates relevées dans les fichiers sont des dates de téléversement, pas de prise de vue. Pourquoi certaines matières existent en 750 px et d'autres en 171 px reste inexpliqué.
- **Pas de PSD, seulement des PNG.**
- **Ajouter une selle** : Produits → Démarrer le configurateur → Contenu, puis ajout des images **une à une**, par calque et par matière, pour chaque selle.
- Elle **crée les calques dans Photoshop**, ce qui lui prend beaucoup de temps. Elle a **de nombreuses nouvelles selles** qu'elle ne peut pas ajouter : ce ne sont pas des modèles duplicables, il faudrait refaire tous les calques.
- Une fois les calques faits, elle doit **payer VIMAWEB pour « faire entrer » la selle**, parce que VIMAWEB crée les matières. Ce point n'est pas compris : à clarifier (voir ci-dessous).
- Demande : **automatiser la création des calques**.

**Mesure faite après l'appel** : la vraie texture du Fiber blanc (assise Z900) est-elle une répétition littérale d'une tuile de 171 px ? (`plugin-gestion/tests/periode_reelle.py`, écart moyen absolu entre l'image et elle-même décalée, sur 255)

| Décalage | Écart | Lecture |
|---|---|---|
| 171 px à l'horizontale, à la verticale, en diagonale | 14 à 15 | **pas de répétition à 171 px** (même niveau qu'un décalage au hasard) |
| **51 px à la verticale** (et 102 px) | **0,0** | superposition **exacte au pixel** : répétition littérale d'une cellule de 51 px de haut |
| 27 px à l'horizontale | 1,8 | quasi exacte (cellule d'environ 27 px de large) |

Lecture :
- Valérie a raison sur le fond : la texture est bien une **répétition**, mais d'une **petite cellule de tissage** (environ 27 × 51 px pour le Fiber blanc), et non du carré de 171 px. Le carré de 171 px est un extrait de cette surface, et ne contient pas un nombre entier de cellules (171 / 51 = 3,35).
- C'est pourquoi le prototype, qui répète le carré de 171 px tel quel, s'écarte de 12 à 14 niveaux et fait apparaître des raccords. En détectant la cellule (autocorrélation) et en répétant **la cellule**, on doit retrouver la texture réelle quasiment au pixel près pour les tissages réguliers : c'est la méthode A du §11 (écart de 6,0 contre 12,6 pour le Fiber blanc, 0,9 pour le Noir perforé).
- Pour les cuirs irréguliers (Violet, Marron), il n'y a pas de cellule ; le fondu reste le meilleur recours.
- Le prototype doit donc passer du « carré de 171 px répété » à la « cellule détectée répétée ». Cela ne demande aucune photo plein cadre. Mesure faite sur une seule matière ; à étendre aux 8 matières texturées du §11.

**Ce que ça change pour la Phase 2**
1. **La matière n'est plus le goulot** : peu de nouvelles matières, et leur ajout est couvert par l'écran de gestion (§14.4) avec la cellule répétée.
2. **Le goulot est la création des calques d'une nouvelle selle.** Une image de zone est la texture de la matière découpée par le masque de la zone (identique au pixel sur 39 matières et 3 modèles, §11) : créer les calques d'un nouveau modèle revient à produire les **masques de zones** (assise, bec, bandeaux, liserés, bandes) et le fond photo/ombres, puis à générer toutes les images de matières par calcul.
3. **La saisie image par image disparaît** : configurateur global (2.0.0) et génération par lots, déjà testés sur la copie.
4. **Dépendance à VIMAWEB** : à clarifier avec Valérie ce que VIMAWEB fait au juste quand elle le paie (création des matières dans le plugin ? plugin sur mesure ?). L'écran de gestion supprimerait ce besoin pour les matières.

**Automatiser les calques : outils envisagés (non testés ici)**
- **Segmentation des zones** : SAM 2 (Segment Anything) avec un clic par zone, ou GroundingDINO + SAM avec des consignes écrites ; contrôle et correction à la main. Hypothèse la plus réaliste : semi-automatique (cinq clics par selle, au lieu de dessiner tous les calques).
- **Ombres et volume** : estimation de profondeur ou de normales (MoGe-2, déjà utilisée pour le nid d'abeille) pour conserver le relief ; sinon reprendre le calque d'ombres du modèle le plus proche.
- **Assemblage** : Python (NumPy, OpenCV, pyvips), déterministe, comme pour les matières ; pas de génération d'image par IA pour les calques de matière.
- **Validation sans risque** : refaire les masques de 5 à 10 selles **existantes** avec l'outil et mesurer l'écart (IoU) avec les masques de Valérie, qui servent de vérité terrain.

**Reste à demander à Valérie**
- Ce que VIMAWEB facture exactement et pourquoi.
- Combien de nouvelles selles en attente, et photos de ces selles disponibles (cadrage identique aux selles actuelles ?).
- Où sont les vignettes d'origine de Samuel, et pourquoi 750 px pour certaines matières et 171 px pour d'autres.

**Précisions reçues après l'appel (16/10)**
- **VIMAWEB** : Valérie le paie à chaque nouvelle selle, mais on ne sait pas ce qu'il fait derrière. Ce qui est sûr : **c'est elle qui découpe les calques et ajoute les patchs un à un**. Précisé ensuite dans le même appel : voir « Rôle de VIMAWEB » plus bas (l'hypothèse sur le plugin `Sync MKL…` n'est pas retenue).
- **Selles en attente** : plusieurs. Elles sont prises **globalement sous le même angle et à la même distance, mais pas au centimètre près**. Conséquences : les masques d'une nouvelle selle ne sont pas réutilisables d'un modèle à l'autre (segmentation à refaire pour chaque selle) ; l'échelle de la texture par rapport à la selle varie légèrement d'une photo à l'autre (de quelques pour cent, à mesurer sur les modèles existants avant de décider d'un réglage d'échelle).
- **Vignettes d'origine de Samuel** : a priori sur l'ancien hébergement **OVH** (69 Go non inventoriés). L'inventaire de ces 69 Go est le moyen de retrouver les sources et d'expliquer 750 px contre 171 px ; il demande l'accès à l'hébergement (hors périmètre tant que Melvin ne l'a pas décidé).

**Essai SAM sur une selle existante (Kawasaki Z900, 16/10, CPU, modèle `facebook/sam-vit-base` déjà présent en cache, aucun téléchargement)** : un clic par zone placé au point le plus intérieur du masque réel (simule l'opérateur), comparé aux masques de Valérie (canal alpha des images de zones). Script : `plugin-gestion/tests/essai_sam_selle.py`, planche : `attachments/gestion-essai-sam-z900.png` (vert = masque de Valérie, rouge = SAM, point jaune = clic). Temps : environ 10 s pour l'image, moins d'une seconde par zone.

| Zone | IoU (masque choisi par SAM) | Meilleur des 3 propositions |
|---|---|---|
| Dosseret | **0,96** | 0,96 |
| Bec | **0,94** | 0,94 |
| Assises avant | 0,34 | 0,75 |
| Bandeaux | 0,43 | 0,43 |
| Assises arrière | 0,23 | 0,46 |
| Bandes latérales | 0,18 | 0,79 |
| Liserés | 0,03 | 0,23 |
| Surpiqûres | 0,00 | 0,00 |
| **Moyenne** | **0,39** | **0,57** |

Lecture :
- **Un clic suffit pour les zones nettement délimitées** (bec, dosseret : 0,94 à 0,96) et pour la silhouette d'ensemble.
- **Il ne suffit pas** pour les zones séparées par une simple couture sur un cuir de même couleur (assises, bandeaux, bandes latérales) : SAM renvoie souvent la selle entière ou une zone voisine. Les liserés (fines lignes) et les surpiqûres (741 px) ne sont pas trouvés.
- Ajouter des clics négatifs dans les autres zones n'a **pas** amélioré le résultat (moyenne 0,29 au lieu de 0,39 ; le bec baisse de 0,94 à 0,40).
- Cas difficile : selle noire sur noir. Le masque de Valérie exclut aussi le logo brodé, ce qui pénalise un peu l'IoU.
- **Conclusion** : SAM seul, dans cette version, ne suffit pas pour produire les calques. Pistes à tester, par ordre de promesse : (1) **partir des masques du modèle existant le plus proche** et les recaler sur la nouvelle selle (même angle et même distance, au centimètre près seulement) en s'appuyant sur la silhouette, puis affiner les bords avec SAM ou les contours ; (2) un modèle SAM plus grand (vit-large ou SAM 2.1) avec boîtes englobantes au lieu de points ; (3) détection des coutures par contours pour les liserés et surpiqûres. Rien de cela n'est testé.

**Rôle de VIMAWEB (précisé par Melvin après l'appel, 16/10 ; rapporté de mémoire, à confirmer avec Valérie)**
- Il y a **deux opérations distinctes**, faites par deux personnes :
  1. **VIMAWEB (payé à chaque nouvelle selle)** : Valérie lui remet le **calque** (la forme de la zone) ; il y applique les **couleurs et matières** et fournit les images « matière X sur zone Y ». C'est la fabrication des images de zones.
  2. **Valérie** : dans Produits → Démarrer le configurateur → Contenu, elle ajoute **une par une** les matières, et associe à chaque choix l'image de zone (« photo du calque ») et la vignette de la matière. C'est ce qui relie la matière au calque.
- Cela correspond aux données : chaque choix du configurateur porte deux images distinctes, l'**image de zone** (1920 × 1280, fabriquée) et la **vignette** (le petit carré cliquable, fourni par Valérie).
- **Conséquence** : l'opération 1, celle que paie Valérie à VIMAWEB, est exactement ce que le poste 3 reproduit par calcul (texture + masque) et que l'écran de gestion automatise ; l'opération 2 est la saisie image par image que les configurateurs globaux 2.0 et la génération par lots suppriment. Reste à la charge de Valérie la **découpe des calques** (masques de zones), que l'essai SAM ne remplace pas encore.
- Non établi : comment VIMAWEB applique les couleurs (outil, script Photoshop, travail manuel), à quel prix et avec quelle qualité par rapport à notre génération.
- **Précisions de Melvin (16/10)** : VIMAWEB applique les couleurs **par du code** (traitement automatique, pas de travail manuel). Valérie paie **60 € par selle** ; Melvin juge ce montant sans importance pour le chiffrage. Cela rejoint la mesure du §14.9 : une texture répétée d'une cellule exacte est la signature d'un traitement par programme ; le prototype de gestion refait la même opération. Le code de VIMAWEB (hérité de Samuel ?) pourrait donner la recette exacte (cellule, répétition, couleur), mais le demander à VIMAWEB n'est pas dans le périmètre sans décision de Melvin.

**Selles « nid d'abeille » déjà configurables (précisé par Melvin, 16/10) et vérification sur la copie**
- Valérie a découpé le calque du nid d'abeille dans Photoshop et l'a envoyé à VIMAWEB, qui y a appliqué les couleurs par code. Exemple : BMW F 900 XR / R, où l'on change la couleur du nid d'abeille dans « Configurer ma selle ». Le nid d'abeille y est **imposé** (par défaut, non retirable). Il ne couvre qu'**une partie de l'assise**, ce qui empêche d'automatiser avec un script qui l'appliquerait à toute l'assise.
- Décision envisagée par Melvin : **continuer avec des patchs, mais rendre le nid d'abeille facultatif** (mettre ou retirer) au lieu d'obligatoire. (Message coupé à « Avec les calques, je… » : suite à reprendre.)
- **Vérification sur la copie (fiche F 900 XR, produit 32182)** : la couche « Couture Nid d'abeille » est une couche simple comme les autres ; ses réglages « Exiger un choix », « Sélection par défaut » et « L'utilisateur peut désélectionner » sont **vides**, donc le plugin sélectionne par défaut le premier choix et ne permet pas de le retirer. Le plugin offre nativement les réglages « Ne rien sélectionner par défaut » (`select_nothing`) et « L'utilisateur peut désélectionner le choix » (`can_deselect`) : **rendre le nid d'abeille facultatif est un réglage de la couche, sans développement**.
- **Pas de trou sous le nid d'abeille** : l'image de la couche Assises est opaque (99,7 %) à l'endroit du nid d'abeille, lequel est une image semi-transparente (alpha moyen 123) posée par-dessus. Retirer la couche laisse donc une assise unie, sans zone vide.
- À noter : les images de cette selle (2025/03) dépassent 1920 px de large (le nid d'abeille s'étend jusqu'à x = 4251 px) : les selles récentes n'ont pas toutes le cadre de 1920 × 1280 des plus anciennes. À vérifier avant d'appliquer l'hypothèse d'échelle unique.
- Non testé : le rendu du front avec le réglage modifié sur la fiche d'origine, et le comportement sur les autres selles à nid d'abeille (F 900 XR, GSX-S 8S/8R).

**Apprentissage (16/10, site local) : le nid d'abeille peut être retiré dans la version configurable, sur la fiche MT-09 (produit 59286)**
- **Fiches nid d'abeille configurables du site** : 3 fiches au nom explicite (BMW F 900 XR / R, Yamaha MT-09 2024, Suzuki GSX-S 8S/8R). La **MT-09 (produit 59286, 320 €)** a 10 couches dont « Couture nid d'abeille » : **27 coloris**, images en 1920 × 1280, toutes présentes dans le clone (`2024/12/`). Leurs noms de fichier sont trompeurs : 2 en `couture-nid-abeille-*` (noir, blanc), les 25 autres en `assises-*` (`assises-azur.png`…). C'est cette fiche qui a fourni la maille de la forme A (`formes.json`).
- **Retirer le nid d'abeille est possible et sans trou** : sans la couche, il reste les zones de surface (Assises, Avant assise arrière, Bandes, Bandeaux, Bec, Bec arrière, Couture). Vérifié sur une copie locale (produit 222762, la fiche 59286 n'est pas modifiée) : la selle s'affiche, les choix de couleur fonctionnent, l'assise change bien de couleur sans motif dessous.
- **Nid d'abeille facultatif = un onglet, pas du développement** : la couche est ré-ajoutée sur la copie sous le nom « Nid d'abeille » (en dernier), avec les 27 coloris et leurs vignettes, **rien de sélectionné par défaut** (`default_selection = select_nothing`) et **désélectionnable** (`can_deselect`). Le rendu avec le coloris Rouge vif est correct. Désélection : confirmée en déclenchant l'événement du plugin ; un vrai clic dans le navigateur de test ne l'a pas fait reculer (clic mal ciblé ou comportement réel : à revérifier à la main).
- **Le calque « Noir antidérapant » qui reste est dégradé** : les calques de la fiche (2024/12) ne sont **pas** la texture maître de Valérie. Luminosité 44 contre 29 pour la texture maître (version récente, 2023), grain plus gros, taches horizontales répétées (raccords de tuile). Écart moyen de 17 niveaux et 9 % de pixels identiques à la texture maître, **pour les 6 zones** de la fiche : c'est donc la matière entière qui est une version à part, pas seulement l'assise.
- **Correction appliquée sur la copie** : on garde le masque de chaque calque (canal alpha) et on remplace les couleurs par la texture maître de Noir antidérapant (`poste3_reappliquer_texture_maitre.py`) ; les ~3 % de pixels hors texture reconstituée sont complétés par la même texture décalée. 5 zones refaites (Assises, Avant assise arrière, Bandes, Bandeaux, Bec), rendu uniforme sans taches ; la selle est plus sombre, c'est le vrai niveau de la texture maître. Le choix « Bec arrière Noir antidérapant » pointe vers `assises-anthracite-2.png`, une image **anthracite** (luminosité 59) : fichier probablement erroné, non touché.
- **Autre défaut trouvé** : le calque d'ombres de cette fiche contient le logo « CB 125 R » (copié d'une fiche Honda), visible sur le rendu : à retirer, comme pour les logos incrustés (voir Poste 4).
- **Outils** (dans `Phase 1/scripts/`) : `creer_selle_sans_nid_local.php` (copie sans nid, option `onglet` pour le rendre facultatif), `remplacer_image_choix_local.php` (remplace l'image d'un choix), `poste3_reappliquer_texture_maitre.py`. Résultats : `Phase 1/essais-poste3/mt09-texture-maitre/`. Tout est limité au site local `sellerie-confort.local`.
- **Pour la production** (non fait, hors périmètre sans décision de Melvin) : rendre le nid d'abeille facultatif sur les fiches de Valérie = cocher « Ne rien sélectionner par défaut » et « Peut désélectionner » sur la couche ; corriger la matière Noir antidérapant demande de remplacer les 6 images de chaque fiche concernée.

Planche des calques détourés par SAM sur la Z900 : `attachments/gestion-essai-sam-z900-calques.png` (une ligne par zone : masque choisi par SAM, meilleure des 3 propositions, masque réel de Valérie). Constat visuel : l'assise avant et les bandes latérales ressortent comme la selle entière ou des morceaux troués ; le bec et le dosseret sont propres (mais le logo brodé du dosseret est perçu comme un trou) ; les liserés et les surpiqûres ne sont pas trouvés.

**Calques automatiques : essai d'un modèle entraîné sur les calques de Valérie (16/10, CPU, aucun téléchargement)**
- **Jeu de données** : les **55 configurations distinctes** (les 55 configurateurs globaux, chacun regroupant des fiches à calques identiques) plutôt que les 345 fiches : photo de base + un masque par zone (canal alpha des images de couches), découpage **par configuration** (44 entraînement, 11 test jamais vues). 54 images en 1920 × 1280, 1 en 5712 × 4284 (BMW F 900 XR). Les noms de zones diffèrent d'une configuration à l'autre (bandes séparées du dosseret ou non, assise unique ou avant/arrière) : 11 classes. Le nid d'abeille n'existe que dans 2 configurations. Scripts : `plugin-gestion/tests/dump_jeu_segmentation.php`, `construire_jeu_segmentation.py`, `essai_dinov2_zones.py`.
- **Modèle** : DINOv2-small gelé (déjà en cache) + une petite tête apprise, 300 époques sur processeur (quelques minutes). Aucune déformation d'image, aucun réglage.

| Classe (configurations de test où elle existe) | IoU |
|---|---|
| Assise avant / arrière (2 et 1) | 0,94 / 0,94 |
| Bec (11) | 0,81 |
| Assise unique (10) | 0,75 |
| Bandes et dosseret (8) | 0,69 |
| Bandeaux (11) | 0,68 |
| Bandes (3) | 0,68 |
| Dosseret (1) | 0,00 |
| Liserés (10) | 0,00 |
| Surpiqûres (10) | 0,00 |
| **Moyenne de toutes les classes** | **0,51** ; **≈ 0,78** sans les trois classes à zéro |

- Lecture : sur des selles **jamais vues**, le modèle place les grandes zones au bon endroit (bec, assises, bandeaux, bandes), avec des contours en escalier (le modèle voit par blocs de 14 px) et quelques confusions entre zones voisines. Il ne trouve **ni les liserés ni les surpiqûres** (lignes de quelques pixels) ni le dosseret isolé (1 seule configuration de test). Comparaison avec SAM un clic par zone (moyenne 0,39 sur la Z900) **non équivalente** : autre protocole, autres selles, SAM sans entraînement.
- Limites : peu d'exemples (44), très peu de configurations de test par classe (1 à 11), perte d'entraînement proche de zéro (apprentissage par cœur probable), une seule exécution. Les contours sont à affiner (SAM, contours d'image) et les lignes fines demandent une autre méthode.
- Planche : `attachments/gestion-essai-dinov2-zones.png` (photo de base, masques réels, masques prédits ; trois selles de test). Sur une des selles, la photo de base est une silhouette grise sans texture.
- Suite envisagée : Mask2Former (ou SegFormer) entraîné sur GPU loué avec déformations d'image, puis affinage des contours par SAM ; lignes fines (liserés, surpiqûres) par détection de contours. Rien de cela n'est testé.

### 14.10 Les trois jeux de choix et l'écran « Matières et couleurs » en quatre onglets (17/10)

**Pourquoi 78 matières et 153 surpiqûres s'affichaient.** L'écran comptait les **noms distincts** sur les 55 configurateurs globaux, pas les couleurs réelles. Les fautes, les listes atypiques et mes essais l'ont gonflé. Les chiffres de la note pré-phase-1 (jeux de choix par couche : 37, 44, 26) sont les bons.

**Les trois jeux standard** (repérés par la taille des listes, sur les 55 configurateurs) :

| Jeu | Choix | Couches | Contenu |
|---|---|---|---|
| **Matières** | 37 | 174 (assises, bec, bandeaux, bandes, dosseret) | Noirs, gris, bleus, rouges, orange, jaune, verts, marrons, blanc, Fiber blanc, violet |
| **Liserés** | 44 | 50 | Les 37 matières + 7 finitions brillantes (gris argent brillant, gris argent chromé, rouge brillant, or, or pailleté, vert brillant, rose brillant) |
| **Surpiqûres (fils)** | 26 | 51 | Palette de fils, **identique aux 26 « Couleurs broderie »** des options de commande (mêmes noms : « Argent et Brume », « Bleu égyptien et Yam »…) |

Un quatrième type : les **couches fixes** (1 choix, 78 couches), qui ne sont pas un jeu à choisir.

**Écran de gestion (prototype, copie `127.0.0.1:8090`)** : quatre onglets **Matières 37 · Liserés 44 · Surpiqûres 26 · À vérifier 183**. Une matière appartient à un jeu si elle figure dans une liste de la taille standard du jeu ; sinon elle va dans « À vérifier » avec sa raison :

| Raison | Nombre |
|---|---|
| Nid d'abeille nommé autrement (« Couture nid d'abeille X », « Nid d'abeille X ») | 52 |
| Petites pointes (couche de la Yamaha R6, 44 choix, 5 fiches) | 44 |
| Variante ou faute (« bordeau », « bleu sirius », « Surpiques bleu azur »…) | 64 |
| Broderie de logo (mes calques d'essai, présents dans un configurateur de la copie) | 22 |
| Doublon probable (« Gris tonnerrre ») | 1 |

(Une première version annonçait 86 « variantes ou fautes » : 22 étaient mes choix de logos.)

**Propreté des trois jeux (vérifiée)** : Liserés et Surpiqûres n'ont **ni doublon ni faute** et une seule composition de liste partout. Matières : deux défauts dans les données, **« Gris tonnerrre »** (trois r) dans les **66 listes « Assises »** (les 159 autres écrivent « Gris tonnerre ») et **« orange poterie »** en minuscule dans 66 listes. Corrigés sur la copie par le mécanisme de l'écran (renommage), le doublon héritant de la famille « Les Gris ». **Vignettes** : dans les listes standard chaque matière n'a **qu'une seule vignette** (nuancier 2022/05, 750 × 750) ; les « plusieurs vignettes » venaient des autres listes (nid d'abeille, images de 171 px), et le compteur ne les prend plus en compte.

**Rattachement du nid d'abeille et des logos à la palette de 26 fils : fait sur la copie (17/10, après accord de Melvin).**
- **Constat de départ** : seules **2 fiches** ont une couche de nid d'abeille dédiée : **Yamaha MT-09** (59286, 27 choix) et **BMW F 900 XR / R** (32182, 29 choix, liste ancienne et désordonnée). La **Suzuki GSX-S 8S/8R** (59650) n'a pas de couche dédiée : sa couche « Couture » est déjà la liste standard de 26 fils. La MT-09 couvre les **26 fils au complet** (+ le cas Égyptien/Yam) ; la F 900 XR n'a aucun gris et a **7 couleurs hors palette**.
- **Ce que « rattacher » change** : une couleur de nid d'abeille prend l'**identité du fil** (nom, famille, activation communs). Les **images restent distinctes** (un PNG coloré par fiche) et les **listes par fiche ne changent pas** : aucune fiche ne se met à offrir les 26 couleurs.
- **Résultat (écran, copie)** : **Surpiqûres 26 (+11 supplémentaires)**, À vérifier 131 (183 avant : les 52 noms de nid d'abeille n'y sont plus). Les 27 et 29 choix des deux fiches sont **tous conservés** après composition (vérifié), maintenant classés en familles (Les Noirs, Les Gris…) comme les autres listes de fils.
- **Fusionnés avec un fil de la palette (synonymes)** : citron → Jaune citron ; bordeau et Rouge Bordeaux → Bordeaux ; Gris brume argent → Argent et Brume. Le reste du nid d'abeille correspond déjà à un fil par son nom.
- **Les 11 couleurs supplémentaires (rien n'est perdu)**, rangées sous l'onglet Surpiqûres, après les 26 :
  - **7 hors palette**, F 900 XR uniquement : bleu petronas, bleu sirius, marron foncé, marron clair, rose clair, prune, violet ;
  - **2 calques distincts, variantes du fil « Bleu égyptien et Yam »** : « bleu égyptien » et « bleu yam » gardent chacun leur calque et héritent la famille et l'activation du fil (désactiver le fil les masque) ;
  - **2 noms ambigus, non rattachés** tant que Valérie n'a pas répondu : « blanc et fiber blanc » (Fiber blanc est une texture, pas un fil) et « rouge vif-brillant » (Rouge vif ou Rouge brillant ?).
- **Logos** : la couleur du fil d'un logo est déjà **la médiane du calque « Couture » du modèle** (jeu Surpiqûres), donc les logos reposent sur la palette. Le rattachement : `scripts/exporter_palette_fils.php` exporte les 26 fils du catalogue (`palette_fils.json`) et `export_configurateur.py` les lit avec `FILS=palette` (par défaut, les 4 fils d'essai ; non lancé sur les 26 : 26 couleurs × 5 logos × 2 emplacements par modèle). Les 22 choix de mon prototype restent dans « À vérifier » (« Broderie de logo (essai) »).
- **Broderie, champ d'options de commande « Couleurs broderie »** (26 pastilles, hors configurateur) : mêmes noms que les 26 fils, mais **toujours pas relié** : renommer un fil ne le suit pas. Il faut une passerelle (le plugin remplit les libellés du champ depuis le catalogue) : environ 1 j, **non faite**.
- **À trancher avec Valérie** : (1) les 7 couleurs de la F 900 XR sont-elles encore vendues ? (2) « Égyptien et Yam » : garder deux calques (retenu pour l'instant) ou un seul ? (3) « rouge vif-brillant » : quel rouge ? (4) « blanc et fiber blanc » : un seul calque pour les deux ? La F 900 XR a aussi un doublon (« bleu yam » deux fois).
- **Bascule technique** : les clés du catalogue passent par `SC_Gestion::rattacher()` (palette, synonymes, variantes, noms à confirmer en constantes de la classe). Si le jeu de 26 change, la constante `PALETTE` est à mettre à jour.

Code : `Phase 1/plugin-gestion/sc-gestion-configurateur/` (README à jour). Aucun changement en production.

## 16. Divi contre modèle PHP pour la fiche produit : mesure Lighthouse (16/10)

Test sur la copie (`http://127.0.0.1:8090`, produit KTM Duke 10169), 3 passages par cas, médiane. Fichiers : `Phase 1/habillage-configurateur/test-divi/` (`sc-fiche-produit.php`, `sc-test-fiche-php.php`, `mesure.mjs`, `mesure.log`). Le modèle PHP et le script viennent de la branche `claude/gallant-cray-219vp6` (non fusionnée) ; deux corrections : le gabarit PHP est rangé dans `mu-plugins/sc-habillage/` (à la racine, WordPress le chargeait comme extension et plantait), et le script appelle Lighthouse par Node (le lancement par `npx` échoue sous Windows).

- **A** : fiche actuelle, rendue par le modèle Theme Builder de Divi (`/?p=10169`).
- **B** : même fiche, rendue par un modèle PHP qui reprend la maquette (fil d'Ariane, titre, tag, référence, prix, configurateur en ligne) (`/?p=10169&sc_php=1`). L'en-tête et le pied de page restent ceux de Divi dans les deux cas.

| Version | Profil | Score | LCP (s) | TBT (ms) | CLS | Poids (Ko) | Requêtes | CSS inutilisé (Ko) | JS inutilisé (Ko) |
|---|---|---|---|---|---|---|---|---|---|
| A Theme Builder | mobile | 30 | 31,88 | 1 324 | 0,039 | 15 332 | 142 | 262 | 416 |
| A Theme Builder | bureau | 57 | 5,09 | 242 | 0,010 | 15 332 | 142 | 256 | 416 |
| B modèle PHP | mobile | 33 | 13,62 | 1 057 | 0,025 | 12 456 | 130 | 255 | 425 |
| B modèle PHP | bureau | 62 | 2,52 | 246 | 0,023 | 12 456 | 130 | 273 | 426 |

### Ce que contient le poids de la page (premier passage de chaque cas)

| Type | A : requêtes, poids | B : requêtes, poids |
|---|---|---|
| **Images** | 68, **12,45 Mo (83 %)** | 58, **9,69 Mo (80 %)** |
| Scripts | 43, 1,09 Mo | 43, 1,09 Mo |
| Polices | 9, 0,74 Mo | 7, 0,74 Mo |
| Feuilles de style | 18, 0,32 Mo | 18, 0,32 Mo |
| Document HTML | 0,37 Mo | 0,32 Mo |

### Lecture

1. **Le poids vient des images, pas de Divi** : 80 à 83 % du transfert, soit près de 10 à 12 Mo. L'image PNG la plus lourde pèse 1,3 Mo ; les calques du configurateur dominent la page dans les deux versions.
2. **Le gain de B (environ 2,9 Mo, 12 requêtes, +3 à +5 points de score) vient du contenu**, pas du mécanisme : la fiche A affiche en plus des images (galerie, blocs de réassurance) et des champs d'options que B ne contient pas. Ce n'est donc **pas un gain de « quitter Divi »**.
3. **Scripts et feuilles de style sont identiques** (43 scripts, 1,09 Mo ; 18 feuilles, 0,32 Mo) : B garde l'en-tête et le pied de page de Divi, donc le JavaScript de Divi reste chargé. Ce test **ne mesure pas** ce que coûterait ou gagnerait un thème entièrement sans Divi.
4. **Les valeurs absolues sont mauvaises dans les deux cas** (score mobile 30 et 33 ; LCP 14 à 32 s) : serveur PHP local à un seul processus, limitation réseau de Lighthouse, aucun cache ni CDN. À lire en **relatif**, pas comme des valeurs de production.

**Conséquence pour la question « sortir de Divi »** : le levier de performance n'est pas Divi mais **le chargement des images du configurateur** (n'afficher que les calques visibles, formats plus légers, chargement différé). Un modèle PHP seul n'allège pas la page de façon significative.

### Limites

- Une fiche, une machine, serveur local ; B n'a ni champs d'options ni blocs de réassurance (comparaison à contenu inégal).
- Pas de test d'un thème sans Divi.
- La mesure n'a pas isolé le coût propre de l'habillage (même fichiers chargés en A et B).

**Calques automatiques : Mask2Former sur GPU (Kaggle, T4 ×2, 16/10)** : même jeu (44 configurations d'entraînement, 11 de test jamais vues), même mesure que l'essai DINOv2. Modèle de départ `facebook/mask2former-swin-tiny-coco-instance`, 150 époques en 28 minutes, avec déformations d'images (symétrie, zoom, décalage, luminosité). Notebook : `plugin-gestion/tests/entrainer_mask2former.ipynb`. Le jeu de données a été envoyé sur le compte Kaggle de Melvin en **dataset privé**.

| Classe (configurations de test concernées) | DINOv2 gelé | **Mask2Former** |
|---|---|---|
| Assise unique (10) | 0,75 | **0,86** |
| Assise avant / arrière (2 / 1) | 0,94 / 0,94 | **0,95 / 0,99** |
| Bandeaux (11) | 0,68 | **0,95** |
| Bec (11) | 0,81 | **0,89** |
| Bandes et dosseret (8) | 0,69 | **0,81** |
| Bandes (3) | 0,68 | 0,60 |
| **Liserés (10)** | 0,00 | **0,71** |
| Surpiqûres (10) | 0,00 | 0,12 |
| Dosseret (1) | 0,00 | 0,00 |
| **IoU moyen** | 0,51 | **0,72** |

- IoU par configuration : de 0,45 à 0,86 (une seule sous 0,5 : 0,446 et 0,474 pour deux configurations).
- Lecture : sur des selles jamais vues, les grandes zones sont retrouvées à 0,86 à 0,99 et **les liserés, qui échappaient à SAM et à DINOv2, passent à 0,71**. Reste faible : les **surpiqûres** (0,12, lignes de quelques pixels) et le **dosseret isolé** (0,00, une seule configuration de test, donc pas concluant). Les bandes sont à 0,60 sur 3 configurations seulement.
- Comparaison avec SAM (0,39 à un clic par zone, Z900 seule) : autre protocole, à titre indicatif.
- Limites : 11 configurations de test, une seule exécution (pas de répétition, pas de réglage), 55 images au total ; les chiffres par classe reposent sur 1 à 11 configurations ; l'IoU à 0,5 de seuil ne dit pas la précision du contour au pixel près (nécessaire pour un calque de production). Aucun contrôle visuel des masques prédits n'est encore fait pour ce modèle.
- Suite envisagée : contrôle visuel des masques ; affinage des contours (SAM ou détection de contours) ; surpiqûres par détection de lignes ; plus de configurations par classe ; mesure de l'écart de contour en pixels face aux calques de Valérie.

**Calques automatiques : SegFormer-B0 sur cette machine (processeur, 16/10)** : même jeu et même mesure. Poids de départ `nvidia/mit-b0` (téléchargé, officiel NVIDIA, environ 14 Mo), 60 époques en 1 h 01 min sur processeur, déformations d'images, perte BCE pondérée + Dice. Script : `plugin-gestion/tests/essai_segformer_b0.py`.

| Modèle | IoU moyen (11 configurations de test) | Liserés | Surpiqûres | Bandeaux | Assise unique |
|---|---|---|---|---|---|
| DINOv2 gelé + tête (CPU, quelques minutes) | 0,51 | 0,00 | 0,00 | 0,68 | 0,75 |
| **SegFormer-B0** (CPU, 1 h) | **0,64** | 0,62 | 0,08 | 0,74 | 0,76 |
| **Mask2Former** (GPU Kaggle, 28 min) | **0,72** | 0,71 | 0,12 | 0,95 | 0,86 |

- Lecture : SegFormer-B0, entraîné entièrement sur cette machine, trouve déjà les liserés (0,62) et fait mieux que DINOv2 ; Mask2Former reste devant, surtout sur les bandeaux (0,95 contre 0,74). Dans les trois cas, les surpiqûres (lignes de quelques pixels) et le dosseret isolé (une seule configuration de test) échouent.
- Les deux configurations les plus difficiles sont les mêmes pour tous les modèles (G222649 et G222674).
- Limites : une exécution par modèle, 11 configurations de test, réglages non optimisés (SegFormer-B0 n'a pas été entraîné aussi longtemps que Mask2Former).
- Conséquence : un GPU n'est pas indispensable pour un résultat utile (0,64 sur processeur), mais Mask2Former donne un net avantage pour les grandes zones.

### Captures A et B (16/10)

Captures bureau (1440 px) de la copie, produit KTM Duke : `Phase 1/habillage-configurateur/test-divi/captures/A-divi-bureau.png` et `B-php-bureau.png`.

- **A (Divi)** : en-tête et bandeau de fil d'Ariane de Divi, photo du produit, texte d'avertissement, prix, puis le configurateur habillé (outils, compteur, zones, pied avec prix et bouton bleu), puis les champs d'options et le total, tous à la même largeur.
- **B (modèle PHP)** : fil d'Ariane, titre, tag « Délai de 1 mois », prix, configurateur habillé et pied, puis le pied de page. Plus proche de la maquette, mais **sans** les champs d'options, la description ni la photo produit.
- **Défaut corrigé en cours de test** : sur A, le configurateur et les options étaient décalés vers la droite et coupés au bord (la colonne Divi n'est pas centrée dans la fenêtre). Corrigé par un alignement calculé en JavaScript (`habillage.js`), le CSS seul ne suffisait pas.

## 17. Voie B : l'interface de la maquette branchée sur le plugin (16/10)

**Question posée** : la maquette `configurateur-maquette-r6.html` peut-elle servir d'interface réelle, avec le panier du site qui fonctionne derrière ? **Réponse : oui, sur la copie, pour une fiche (KTM Duke 10169), de la sélection des matières jusqu'à l'ajout au panier.**

### Ce qui a été fait
- La page de la maquette (HTML, CSS, JavaScript) est reprise **telle quelle** (scène, barre d'outils, 4 étapes, familles de matières, récapitulatif, partage, annuler/refaire, comparer, mobile). Un script (`Phase 1/maquette-branchee/build.py`) l'assemble en gabarit WordPress avec quelques remplacements ciblés. Activation par `?sc_maq=1` sur la fiche, uniquement sur la copie (mu-plugin `sc-maquette.php`).
- **Données du plugin** : les calques, leurs choix, les images et l'ordre d'empilement viennent du plugin (`mkl_pc('db')->get`), le choix d'origine est celui du plugin (vérifié : les 8 zones ont le même choix par défaut que le configurateur actuel). Les motifs de broderie, les 26 couleurs, les hauteurs, le gel et le prix viennent des champs APF du produit.
- **Panier** : le configurateur du plugin et le formulaire WooCommerce (champs APF) sont présents dans la page mais masqués. Au clic sur « Ajouter au panier », la maquette recopie les matières dans le plugin, les champs dans APF, puis déclenche le bouton du plugin : c'est le chemin actuel de la fiche, rien n'est contourné.

### Test automatisé (Chrome, `test-parcours.mjs`)
Parcours : matière (Fiber black sur assises avant), broderie dosseret « Duke plein et contour », couleur Bleu azur, hauteur abaissée, gel assise avant, 5 informations, récapitulatif, ajout au panier, lecture du panier.
- Total affiché dans la maquette : **290,00 €** = 245 + 10 + 35. Panier WooCommerce : **290,00 €**, avec les 8 lignes de configuration (Fiber black, etc.) et tous les champs APF (broderie, motif, couleur, hauteur, gel, modèle, année, taille, poids, commentaire).
- Aucune erreur JavaScript, aucune matière non classée après réglage des règles de familles.
- Captures : `poste3-voieB-1-matieres.png`, `-2-broderies.png`, `-3-recap.png`, `-4-mobile.png`, `-5-panier.png` (même dossier).

### Trouvailles
- **Le script du thème enfant bloque l'ajout au panier** : `Divi Child/js/custom-single-product.js` empêche le bouton « Ajouter au panier » tant qu'on n'a pas cliqué « Configurer ma selle », et plante (`prix-base` absent) sur une page qui n'est pas la fiche Divi. Le gabarit retire donc les scripts et styles du thème, des CDN (Bootstrap, html2canvas) et la galerie WooCommerce. En refonte, ce script disparaît de toute façon.
- **Les noms de matières du plugin sont irréguliers** (« Gris tonnerrre » avec trois r, « Assises Citron », « Assises Marron » sans « clair ») : les familles de la maquette reposent sur des règles de reconnaissance de noms, trois règles ajoutées. Sur le site réel, les **groupes natifs du plugin 2.0.0** (déjà présents dans les données de la copie : « Les Noirs », etc.) évitent cette dépendance aux noms : à décider en phase 2.
- Les miniatures de matières de la copie n'existent pas en 150×150 (tailles non générées) : repli sur l'image d'origine dans l'adaptateur. Sans effet en production.
- Défaut de la copie, hors sujet : les champs APF « image-swatch » du formulaire masqué appellent `http://16657`… (identifiant de média pris pour une adresse) : trois requêtes en erreur, invisibles.

### Ce qui reste pour que ce soit la vraie interface
1. **Étape manquante : « Type de commande »** (Modification, ou Échange standard +15 € avec caution) : champ obligatoire d'APF, absent de la maquette. Le pont choisit « Modification » par défaut, ce qui est faux pour un client qui veut l'échange standard. À ajouter dans la maquette (étape Options ou Infos).
2. **Fiche-modèle** : les libellés APF sont repérés par leur texte (« Broderie Dosseret », « Motif de broderie »…), valable pour la Duke. Les produits avec « Bandes » ou d'autres intitulés demandent une table de correspondance par produit (ou des noms de champs normalisés dans APF, c'est un choix de Valérie).
3. **Champ « Broderies » en double** (oui/non, obligatoire) en plus de « Broderie Dosseret » : le pont répond pareil aux deux, à clarifier avec Valérie.
4. **Parcours cible** (décision de Melvin, 16/10) : le configurateur (matières, broderies, options, infos perso, tout dans la page) puis la **fiche produit récapitulative** (options choisies, prix, livraison). Pas encore fait : aujourd'hui l'ajout au panier ramène sur la fiche.
5. **En-tête et pied de page du site** : la page de test n'en a pas (la maquette les a). À brancher via Divi Theme Builder (en-tête/pied globaux) ou un gabarit PHP.
6. **Poids et vitesse** : le plugin charge ses propres calques en plus de ceux de la maquette (mêmes fichiers, donc cache navigateur). À mesurer au Lighthouse, ou à éviter en appelant l'ajout au panier de WooCommerce directement.
7. Champs de la maquette non reliés : « Bandes » (le motif n'existe pas pour la Duke, case masquée), prix barré.

### Fichiers
`Phase 1/maquette-branchee/` : `build.py` (assemblage et déploiement sur la copie), `sc-maquette.php` (adaptateur de données, bascule `?sc_maq=1`), `test-parcours.mjs`, `apf_dump.php`, `captures/`. Le dossier généré `sc-maquette/` est reconstruit par `build.py`.

## 18. Voie B : les logos brodés (option A) branchés dans la maquette (16/10)

**Résultat : sur la Z900 (produit 39477, site Local principal, plugin 1.7.6), l'étape Broderies de la maquette pilote les calques « Broderie dosseret » et « Broderie bande latérale » du prototype ; on voit le logo sur la selle, et le panier garde le logo et le fil.**

### Fonctionnement
- Le gabarit détecte les calques dont le nom contient « broderie ». Un choix de calque = « Logo - fil couleur » (image déjà découpée et ombrée). Ces calques ne sont plus des zones de l'étape Matières : ils deviennent l'étape Broderies.
- **Dosseret / Bandes** : les cases d'emplacement choisissent le calque. Décochées : choix d'origine du plugin (logo d'origine sur le dosseret, aucune broderie sur les bandes). Cochées : tuiles de logos (Yeux, Aile Honda, Yamaha, Electrocardiogramme, Alpinestar, + « Sans broderie » sur le dosseret), puis **une couleur de fil** (4 fils : blanc, rouge vif, vert brillant, jaune citron). L'aperçu change en direct, « Comparer » revient au logo d'origine.
- **Panier** : le pont active les deux calques du plugin (la ligne « Broderie dosseret : Yeux - fil rouge vif » apparaît dans « Configuration » du panier), et remplit aussi les champs APF « Broderie Dosseret », « Motif de broderie » (option au nom le plus proche du logo, sinon la première), « Couleurs broderie ».
- Test automatisé `test-logos.mjs` : logo Yeux rouge sur le dosseret, Yamaha rouge sur les bandes, comparaison, 4 infos, ajout au panier : **panier correct** (logos, fils, champs APF, infos). Test de non-régression sur la copie (Duke, plugin 2.0.0) : toujours bon. Captures : `poste3-voieB-6-logos-z900.png`, `poste3-voieB-7-logos-panier.png`.

### Corrections faites en route
- **Plugin 1.7.6, formulaire du panier** : avec `force_form`, le plugin envoie son propre formulaire, **sans les champs APF** (le panier était refusé : « Error adding product to cart », champs obligatoires absents). Le pont recopie les champs APF dans ce formulaire avant l'envoi. En 2.0.0 le plugin envoie le formulaire WooCommerce : sans effet.
- Le gabarit n'affichait pas les messages WooCommerce : ils sont maintenant repris en message en haut de page.
- Le retrait des styles et scripts du thème retirait aussi ceux du plugin (chemin `/themes/` présent dans `inc/themes/clean`) : limité à `/wp-content/themes/`, et au domaine du site (le site principal est en `sellerie-confort.local`).
- Modal Bootstrap du thème enfant et marqueurs PhotoSwipe masqués.

### Limites et décisions à prendre
1. **Seulement 4 fils**, contre 26 couleurs dans APF : le prototype n'a que 4 fils par logo. Pour les 26, soit 26 images par logo et par emplacement (**5 logos × 26 × 2 emplacements = 260 images 1920×1280**), soit **l'option B** (logo recoloré en direct dans la page). Option B : l'interface s'y prêterait très bien (une couleur libre, aperçu immédiat), mais l'enregistrement du choix dans le panier reste à faire (noté dans §Logos brodés de `pre-phase-1.md`).
2. **Une seule couleur par logo** : la maquette permet plusieurs couleurs de broderie (champ « Couleurs broderie » d'APF, avec précisions). Avec le calque, c'est une couleur ; un logo multicolore demande un calque par combinaison ou l'option B avec zones.
3. **Les logos du prototype ne sont pas ceux d'APF pour la Z900** : APF propose 12 motifs (Z 900, Z du Z 900, Griffe Monster, Logo Akrapovic, Pattes de chat, Red-Bull, K de Kawasaki, Punisher, Fox...), le prototype en fait 5 (dont Aile Honda et Yamaha, qui servent de test). Seuls Yeux, Electrocardiogramme et Alpinestar se recoupent ; pour Aile Honda et Yamaha, le champ APF reçoit la première option : **à rendre cohérent avec la liste réelle des motifs de Valérie**.
4. Les vignettes de logos (fil blanc sur fond gris) sont peu contrastées dans la tuile : une vignette dédiée par logo améliorerait la lecture.
5. Sur le site principal, le champ APF « Poids passager » et « Commentaires » existent avec d'autres identifiants que sur la copie : le pont les repère par libellé, donc sans effet.

### Fichiers
`Phase 1/maquette-branchee/` : `build.py` (options `--deploy` pour la copie 8090, `--local` pour le site principal `sellerie-confort.local`), `sc-maquette.php`, `test-logos.mjs`, `test-parcours.mjs`. Aperçu : `http://sellerie-confort.local/?p=39477&sc_maq=1`. Le mu-plugin `sc-maquette` est installé sur le site principal et sur la copie, sans effet hors `?sc_maq=1`.

## 19. Apprentissages de la session « voie B » (16/10)

**1. On peut coder la maquette dans le site réel sans casser le plugin.**
- Le plugin n'est pas modifié : l'interface de la maquette s'appuie dessus. Il garde son rôle (calques, choix, prix, panier) et la maquette ne fait que le piloter, par les mêmes clics que ceux d'un visiteur. Un seul gabarit (mu-plugin `sc-maquette`), activé par `?sc_maq=1` ; hors de ce paramètre, le site est inchangé.
- Vérifié sur **deux versions** du plugin : 2.0.0 (copie, Duke) et **1.7.6, la version actuellement en production** (site principal, Z900). Il n'y a donc pas besoin de la 2.0.0 pour avoir l'interface de la maquette.
- Rien dans le plugin, APF ou Divi ne limite l'affichage. Seuls obstacles rencontrés : le script de Divi Child qui bloque le bouton, retiré de ce gabarit, et le formulaire de la 1.7.6 sans les champs APF (recopiés par le pont).
- Le panier reste celui de WooCommerce : le total, la ligne « Configuration » et les champs APF sont les mêmes qu'aujourd'hui.

**2. La broderie logo fonctionne dans cette interface.**
- Les calques « Broderie dosseret / bande » du prototype (option A) se choisissent par logo et par fil dans l'étape Broderies, avec aperçu en direct, comparaison et panier correct (logo, fil, champs APF).
- Limites connues : 4 fils (pas 26), une couleur par logo, logos du prototype différents des 12 motifs d'APF. Pour 26 fils sans 260 images : option B, dont il reste à enregistrer le choix dans le panier.

**3. Pièges à retenir**
- Une image « transparente » faite à la main avait un pixel non nul : la lueur de survol (`drop-shadow`) la rendait visible sur toute la selle (voile violet). Utiliser un vrai GIF 1×1 transparent, et **tester le survol**, pas seulement l'affichage fixe.
- Filtrer les scripts du thème par leur chemin `/wp-content/themes/` (et non `/themes/`, qui attrape `inc/themes/clean` du plugin), et par le domaine du site (pas une adresse en dur).
- Les noms de matières du plugin sont irréguliers (fautes, « Marron » sans « clair ») : les familles par règles de noms demandent des ajustements ; les groupes natifs du plugin 2.0.0 sont plus sûrs.
- Les captures de la fenêtre de l'application peuvent être gelées (fenêtre masquée) : tester avec Chrome et puppeteer (`test-parcours.mjs`, `test-logos.mjs`).

**4. Conséquence pour la suite (Phase 2)**
- La refonte du configurateur peut se faire **au-dessus du plugin existant**, sans réécrire le moteur de calques ni le panier : le travail porte sur l'interface, la correspondance des champs APF par produit, le champ « Type de commande », la fiche récapitulative et l'en-tête/pied du site.
- Reste à mesurer : poids et vitesse de la page (le plugin masqué charge ses calques en plus de ceux de l'interface).

**Calques automatiques : Mask2Former version 2 (Swin-base, image 1152 × 768 prévue, Kaggle, 16/10 soir)** : 100 époques en 52 min, même jeu et même découpage test que la version 1. **IoU moyen 0,64, contre 0,72 pour la version 1 (Swin-tiny, 768 × 512)** : le modèle plus gros n'a pas amélioré le résultat.
- Classes lues sur la capture : bandes et dosseret 0,82 (v1 : 0,81), bandeaux 0,82 (v1 : 0,95), bec 0,79 (v1 : 0,89), liserés 0,65 (v1 : 0,71), bandes 0,59, surpiqûres 0,13, dosseret 0,00, assise arrière 0,98. (Les premières lignes, assise unique et assise avant, n'étaient pas lisibles sur la capture.)
- Par configuration : de 0,37 à 0,81. **G222689 passe de 0,86 (v1) à 0,37** ; G222649 et G222674 restent les plus faibles (0,37 et 0,42).
- Réserve : on n'a pas vérifié que la version 2 a bien lu le dataset à 1152 × 768 (le dataset d'origine à 768 × 512 était aussi rattaché au notebook, et le temps d'entraînement est plus court que prévu pour cette taille).
- **Lecture** : trois modèles très différents (DINOv2 gelé 0,51, SegFormer-B0 0,64, Mask2Former Swin-base 0,64, Swin-tiny 0,72) restent dans une même fourchette, et une seule selle de test peut faire varier le score de 0,5 point. Avec 11 configurations de test et une exécution par modèle, **l'écart entre 0,64 et 0,72 n'est pas fiable** : le facteur limitant est le petit nombre de formes de selles (55), pas la taille du modèle. Ne pas conclure qu'un modèle est meilleur sans validation croisée sur les 55.
- Conséquence pour le plan : plus de calcul sur le même jeu n'apporte rien de démontré. Le scénario retenu reste **semi-automatique** (proposition du modèle, correction par Valérie), à valider par la mesure du temps de retouche.

## 20. Voie B : les 4 chantiers restants faits, test de bout en bout (16/10)

**Objectif : savoir si l'approche tient pour la Phase 2. Réponse : oui sur tous les cas testés, sans réglage par produit.**

### Ce qui a été construit
1. **Champ « Type de commande »** (Modification, ou Échange standard +15 €) : nouvelle rubrique de l'étape Options, prix inclus dans le total, récapitulatif, lien de partage, envoi dans APF. Le texte d'information est celui du champ APF (réel). Rubrique masquée quand le produit n'a qu'un seul choix (Z900 : Modification seule). Capture `poste3-voieB-8-options-type-commande.png`.
2. **Correspondance des champs APF produit par produit** : fini la table par libellé. Un champ APF reçoit un **rôle** d'après son type et son libellé (modèle, année, taille, poids, hauteur, gel, type de commande, couleurs, motifs, emplacements, oui/non broderie…), calculé à chaque chargement (`sc_maq_role`). Les champs qui ne reçoivent aucun rôle (chauffage, accoudoirs, dosseret passager…) sont **affichés tels quels dans l'étape Options**, avec leur prix, et envoyés à APF (`sc_maq_extra`). Capture `-9-options-chauffage.png`.
   - **Mesure sur les 344 produits configurables de la copie** (`couverture_champs.php`) : **tous les champs obligatoires sont reconnus (0 non reconnu)** ; 141 produits utilisent des cases « Dosseret / Bandeau central » (2023) et 193 un oui/non par emplacement ; 79 produits ont des champs supplémentaires gérés de façon générique. Les libellés varient (« Motif Bandeau central » ×87, « Motif Bandes » ×19, « Hauteur de selle » ×14, « Modèle ABS »…) sans que ça gêne.
   - Piège rencontré : deux champs APF peuvent porter **le même libellé** (« Broderies » : cases d'emplacements et oui/non) ; le tableau est donc indexé par **identifiant de champ**, pas par libellé.
3. **Fiche récapitulative** (`?sc_recap=1`) : après l'ajout au panier, WooCommerce renvoie sur la fiche du produit, qui affiche la dernière ligne du panier : aperçu de la selle configurée, matières avec vignettes, broderies (y compris logos), options, informations, **total**, délai de fabrication, livraison, mode d'envoi selon le type de commande. Boutons : Voir mon panier, **Modifier ma configuration** (retour au configurateur avec les choix et les informations gardés dans la session du navigateur), Continuer mes achats. Les phrases de délai, de port et d'envoi sont celles de la page Panier du site actuel. Captures `-10-`, `-11-` et `-12-` (mobile).
4. **En-tête et pied de page du site** : ceux de la maquette (logo, navigation, Mon compte, Panier avec le **nombre d'articles réel**, pied de page), avec les adresses réelles du site (accueil, boutique, matières et couleurs, contact, compte, panier) sur le configurateur et sur la fiche récapitulative.

### Tests de bout en bout (Chrome, scripts `test-parcours.mjs`, `test-logos.mjs`, `test-produits.mjs`)
- **Duke** (copie, 2.0.0) et **Z900** (site principal, 1.7.6) : parcours complet jusqu'à la fiche récapitulative puis le panier, totaux identiques partout (290 €, 245 €), logos compris.
- **4 autres modèles sans aucun réglage** : Yamaha FJR 1300 (cases d'emplacements, motif dosseret et bandeau central, échange standard : 280 €), BMW R 1200 RT (chauffage et top case obligatoires, hauteur supplémentaire : 330 €), Honda Goldwing 1500 (dosseret pilote, chauffage, accoudoirs : 645 €), Honda Africa Twin (dosseret et bandeau central : 270 €). Panier et fiche récapitulative corrects pour chacun.
- Aucune erreur JavaScript, aucune alerte PHP.

### Ce qui reste (Phase 2)
- **Champs supplémentaires** : rendu générique simple (cases et boutons) ; les champs conditionnels d'APF (visibles selon une autre réponse) sont affichés sans condition, donc facultatifs à l'écran. Une vraie règle de conditions est à écrire pour les 79 produits concernés.
- **Plusieurs motifs de même rôle** (ex. « Motif Assise avant » et « Motif Assise arrière ») : traités comme champs supplémentaires, avec vignette ; une interface dédiée par emplacement serait plus claire.
- **Modifier depuis la fiche récapitulative** ajoute une seconde ligne au panier (le plugin sait modifier une ligne existante : à brancher).
- **26 fils pour les logos** (option A : 4 fils seulement) ; **les logos du prototype** à caler sur les motifs réels de chaque modèle.
- **Poids de la page** (calques du plugin masqué en plus de ceux de l'interface) et **mesure Lighthouse** de la page du configurateur.
- Pied de page et menu : textes de la maquette (« Maquette de refonte — design non définitif ») à remplacer ; le lien « Configurateur » du menu renvoie à la boutique faute de page générique.
- Aucun paiement n'a été effectué : la fiche s'arrête au panier.

### Fichiers
`Phase 1/maquette-branchee/` : `build.py`, `sc-maquette.php` (rôles, champs supplémentaires, redirection, adresses), `recap.php` (fiche récapitulative), `couverture_champs.php`, `test-parcours.mjs`, `test-logos.mjs`, `test-produits.mjs`, `captures/`.

## 21. Logos brodés sur le plugin 2.0.0 (17/10)

- Les calques « Broderie dosseret » (22 choix) et « Broderie bande laterale » (21 choix) et l'ombre sans logo d'origine sont ajoutés à la **Z900 de la copie** (produit 39477, `127.0.0.1:8090`, plugin 2.0.0), par `Phase 1/maquette-branchee/import_logos_copie.php`.
- Différence avec le site principal (1.7.6) : la 2.0.0 découpe les données en morceaux ; l'écriture passe donc par son API (`mkl_pc('db')->set`) et non par les métadonnées directes. Relecture vérifiée par l'API. Sauvegarde de la configuration d'origine dans `export-configurateur/kawasaki-z-900/sauvegarde-copie-39477/` ; retour arrière : `wp eval-file import_logos_copie.php 39477 <dossier> restaurer`.
- **Vérifié** : configurateur natif de la 2.0.0 (les deux calques apparaissent avec leurs choix), interface de la maquette (`?sc_maq=1` : logo et fil, comparaison), fiche récapitulative et panier (lignes « Broderie dosseret : Yeux - fil rouge vif », « Broderie bande laterale : Yamaha - fil rouge vif » et champs APF). Test `SC_BASE=http://127.0.0.1:8090 SC_TAG=logos20 node test-logos.mjs`. Capture `poste3-voieB-13-logos-z900-plugin20.png`.
- Conclusion : les logos brodés (option A) fonctionnent de la même façon en 1.7.6 et en 2.0.0.

## 22. Parcours : pas de fiche récapitulative, le panier récapitule (décision de Melvin, 17/10)

- **Décision** : après le configurateur, l'ajout au panier mène **directement au panier**, qui sert de récapitulatif (matières, broderies, options, infos, prix). La fiche récapitulative du §20 est retirée (fichier mis de côté : `Phase 1/maquette-branchee/_abandon/recap.php`).
- **Référencement** (contexte de la décision) : remplacer la fiche produit par l'interface ferait perdre le contenu indexé (texte, photos, prix, données produit). Recommandation : la fiche produit reste la page référencée, avec un bouton « Configurer ma selle » ; le configurateur est une étape à part (adresse propre, canonique vers la fiche ou noindex). Parcours : fiche produit → configurateur → panier.
- Fait sur la copie et le site local : redirection de l'ajout vers le panier (`woocommerce_add_to_cart_redirect` → page panier) ; tests rejoués (Duke, BMW R 1200 RT) : arrivée sur « Panier de commande » avec toutes les lignes, totaux corrects.
- À prévoir en Phase 2 : le panier doit être à la hauteur de ce rôle (maquette `panier.html` : vignette de la selle configurée, lignes lisibles, lien « Modifier » qui rouvre le configurateur sur la ligne au lieu d'en ajouter une).

## 23. Mise en production sans casser : environnements et passage dev → préprod → prod (17/10)

### Ce qui manque pour confirmer qu'on peut mettre la maquette en prod
Acquis : l'interface pilote le plugin sans le modifier (1.7.6 et 2.0.0), panier WooCommerce correct, 6 modèles de bout en bout, 344 fiches sur 344 avec leurs champs obligatoires reconnus, retour arrière par simple désactivation. À valider, par ordre d'importance :
1. **Un environnement identique à la prod** : le site local n'a que 4 extensions actives. Risques : cache et optimisation LiteSpeed (fusion ou report des scripts) qui casseraient le pont ; le gabarit retire les scripts externes, donc aussi bandeau cookies, statistiques et peut-être des scripts de paiement : il faut une liste de scripts à garder.
2. **Une commande complète**, pas seulement le panier : paiement Payline en mode test, courriels, affichage de la commande dans l'admin vérifié par Valérie (c'est elle qui fabrique à partir de ça).
3. **Le catalogue entier** : test automatique sur les ~345 fiches configurables.
4. **Conditions APF** des 79 fiches à champs supplémentaires (affichés sans condition aujourd'hui).
5. **« Modifier » qui double la ligne du panier** : brancher la modification de ligne du plugin.
6. **Navigateurs et poids** : Safari iPhone, Firefox, Lighthouse du configurateur, calques chargés deux fois.
7. **Fragilité aux mises à jour du plugin** (le pont s'appuie sur sa structure HTML) : figer la version, rejouer les tests avant chaque mise à jour.
8. **Référencement** : voir §22 (la fiche produit reste la page référencée, configurateur à part, canonique ou noindex).
9. **Textes de maquette** à remplacer (pied de page « Maquette de refonte… », libellé « Configurateur »), validation par Valérie.

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

**Calques automatiques : SAM 3 sans entraînement (Kaggle T4, 17/10)** : `facebook/sam3` (848 M de paramètres, accès accordé par Meta le 17/10), aucune selle de Valérie vue à l'entraînement, donc mesure sur les **55 configurations**. Une demande par zone, quatre façons : un clic au point le plus intérieur de la zone, une boîte autour de la zone (rectangle de l'opérateur), clic + boîte, texte (« motorcycle seat », « piping », « stitching »…, meilleur masque retenu : borne haute). Notebook : `plugin-gestion/tests/essai_sam3_zeroshot.ipynb` (installation de SAM 3 sans rétrograder NumPy).

| Zone (configurations) | Clic, choix de SAM | Clic, meilleur des 3 | **Boîte** | Clic + boîte | Texte (meilleur) |
|---|---|---|---|---|---|
| Bec (54) | 0,72 | 0,86 | **0,89** | 0,89 | 0,16 |
| Dosseret (12) | 0,23 | 0,67 | **0,94** | 0,94 | 0,29 |
| Assise avant (18) | 0,31 | 0,61 | **0,81** | 0,81 | 0,25 |
| Assise arrière (16) | 0,45 | 0,79 | **0,79** | 0,79 | 0,34 |
| Assise unique (39) | 0,42 | 0,49 | 0,55 | 0,56 | 0,33 |
| Bandes (25) | 0,31 | 0,68 | 0,52 | 0,57 | 0,16 |
| Bandes et dosseret (28) | 0,10 | 0,31 | 0,48 | 0,60 | 0,16 |
| Bandeaux (54) | 0,36 | 0,50 | 0,29 | 0,40 | 0,13 |
| Liserés (51) | 0,26 | 0,28 | 0,06 | 0,05 | 0,34 |
| Surpiqûres (51) | 0,01 | 0,01 | 0,01 | 0,01 | 0,09 |
| **Moyenne (55)** | 0,33 | 0,47 | 0,44 | 0,47 | 0,21 |
| Moyenne (11 configurations de test des modèles entraînés) | 0,32 | 0,43 | 0,39 | 0,42 | 0,20 |

- **Lecture** : sans aucun entraînement, une **boîte** suffit pour les **zones compactes et bien délimitées** : bec 0,89, dosseret 0,94, assise avant 0,81, assise arrière 0,79 (au niveau de Mask2Former entraîné, voire au-dessus pour le dosseret). En revanche, SAM 3 échoue sur les **zones allongées qui entourent la selle** (bandeaux 0,29 à 0,50, bandes et dosseret 0,48 à 0,60) : leur boîte couvre presque toute la selle. Les **lignes** (liserés, surpiqûres) restent hors d'atteinte (au mieux 0,34 pour les liserés, par le texte).
- « Meilleur des 3 » suppose qu'un opérateur choisisse parmi les trois propositions de SAM, ce qui est réaliste dans un outil interactif.
- **Comparaison** sur les 11 mêmes configurations de test : SAM 3 sans entraînement 0,43 au mieux, contre **0,72 pour Mask2Former entraîné** sur les 44 autres. Les deux sont complémentaires : Mask2Former place mieux les grandes zones et les bandeaux, SAM 3 détoure mieux les zones compactes à partir d'une boîte.
- Limites : une exécution, prompts non réglés (une seule boîte ou un seul clic par zone), contours non examinés au pixel près ; affiner SAM 3 sur les calques n'est pas testé (848 M de paramètres : un GPU T4 ne suffit probablement pas sans gel partiel du modèle).
- **Conséquence pour la Phase 2** : un outil semi-automatique réaliste combinerait (1) Mask2Former pour proposer toutes les zones, (2) SAM 3 pour redétourer les zones compactes à partir des boîtes de Mask2Former ou d'un rectangle tracé par Valérie, (3) une sélection des coutures pour les liserés et surpiqûres (elles suivent les bords des zones à 99 % et 78 %), (4) la correction manuelle du reste. La mesure décisive reste le temps de retouche par selle, face au détourage actuel dans Photoshop.

### 14.10 Calques automatiques : conclusion (décision de Melvin, 17/10)

**Décision** : on arrête les essais. Aucun des modèles testés ne produit des calques utilisables sans reprise : le détourage manuel de Valérie reste la référence.

| Approche testée (16-17/10) | Données | Résultat (IoU, 1 = identique au calque de Valérie) |
|---|---|---|
| SAM 1 (vit-base), un clic par zone | Z900 | 0,39 |
| DINOv2 gelé + tête apprise | 44 selles apprises, 11 testées | 0,51 |
| SegFormer-B0 entraîné (processeur) | idem | 0,64 |
| Mask2Former Swin-tiny entraîné (GPU Kaggle) | idem | **0,72** (meilleur) |
| Mask2Former Swin-base, image plus grande | idem | 0,64 |
| SAM 3 sans entraînement, une boîte par zone | 55 selles | 0,44 (0,43 sur les 11 de test) |

Ce que montrent les chiffres :
- Les **zones compactes** (bec, dosseret, assises séparées) sont bien détourées : 0,8 à 0,99 selon le modèle, et SAM 3 y arrive sans entraînement à partir d'une simple boîte.
- Les **zones qui entourent la selle** (bandeaux, bandes) sont instables : 0,3 à 0,95 selon le modèle et l'essai.
- Les **lignes fines** échouent partout : surpiqûres 0,00 à 0,13, liserés 0,00 à 0,71.
- **Aucun essai ne dépasse 0,72 en moyenne**, et les écarts entre essais (une même selle de 0,86 à 0,37) montrent que le facteur limitant est le **petit nombre de formes de selles (55)**, plus que le modèle. Les zones sont aussi des **choix de conception** de Valérie, que la photo ne dicte pas toujours.

Ce qui n'a pas été testé (à mentionner honnêtement dans le rapport) : SAM 3 réentraîné sur les calques (trop lourd pour un GPU gratuit), la combinaison Mask2Former + SAM 3, la validation croisée sur les 55, la mesure du temps de retouche d'une proposition par rapport au détourage complet. Ces pistes pourraient réduire le travail de Valérie dans un outil semi-automatique, mais **rien ne démontre aujourd'hui un gain** : elles ne sont pas retenues pour la Phase 2.

Conséquence pour la Phase 2 : la **découpe des calques reste manuelle** chez Valérie (comme décidé en réunion le 07/10 pour les étapes 1 et 2 du flux d'ajout d'un modèle). L'automatisation porte sur ce qui suit la découpe et que les essais ont validé : génération des images de matières à partir des calques (poste 3, écran de gestion §14.4-14.5), configurateurs globaux 2.0 (§14.2), suppression de la saisie image par image et de l'intervention payante de VIMAWEB pour les couleurs.

Traces : scripts et notebooks dans `Phase 1/plugin-gestion/tests/` (`essai_sam_selle.py`, `essai_dinov2_zones.py`, `essai_segformer_b0.py`, `entrainer_mask2former*.ipynb`, `essai_sam3_zeroshot.ipynb`, `essai_sam21_zeroshot.ipynb` non lancé) ; jeu de données (55 configurations) hors dépôt dans `sellerie-confort-regroupement/_jeu_segmentation*`, copie privée sur le compte Kaggle de Melvin.

## 24. Fiche produit au design de la maquette : configurable et non configurable (17/10)

**Décision de Melvin** : le configurateur ne peut pas être refait sans la fiche produit, sinon les options et les infos perso sont demandées deux fois. Deux fiches au même design (maquette « Fiche produit ») :
- **Selle configurable** : contenu d'origine **sans** options, broderies ni infos perso (elles sont dans le configurateur). Zone d'achat : prix, délai, bouton **« Configurer ma selle »** vers le configurateur, avertissement d'origine sur les couleurs par défaut.
- **Produit non configurable** : contenu d'origine **avec** ses options et infos perso (champs APF) sur la fiche, **ajout au panier direct** (une étape de moins). Seule la forme change.
- Parcours : fiche → configurateur → panier (selle configurable) ; fiche → panier (non configurable).

**Fait sur la copie** (`?sc_fiche=1`, `Phase 1/maquette-branchee/fiche.php`, styles `assets/fiche.css` tirés de la maquette) :
- Contenu réel : photos (principale + galerie avec vignettes), titre, référence, prix et prix barré, fil d'Ariane par catégories, résumé et description si présents, catégories et étiquettes, produits similaires de WooCommerce, garanties ; textes de modification, délai et livraison repris du site (fiche et page panier).
- Non configurable : le formulaire WooCommerce et ses champs APF sont dans la colonne principale, restylés en cartes d'options ; la boîte d'achat affiche le total en direct et déclenche l'ajout ; les conditions APF (champs qui apparaissent selon une réponse) restent gérées par APF lui-même.
- Le fil d'Ariane du configurateur ramène à la fiche.
- **Test** (`test-fiches.mjs`) : fiche configurable (bouton vers le configurateur, aucun champ d'option) ; fiche non configurable (hauteur, gel, infos, échange standard : total 340 € = 245 + 10 + 70 + 15, identique au panier, toutes les lignes APF dans le panier). Captures `poste3-voieB-14` à `-16`.
- **Limite du test** : les deux sites locaux ne contiennent **aucun produit non configurable** (copie construite à partir des fiches configurables publiques). Le cas a été testé sur un produit de **TEST** créé sur la copie (`creer_produit_test.php`, réf. `TEST-NON-CONFIG`, photos et champs APF de la Duke). À vérifier sur de vrais produits non configurables (en stock, carte cadeau, accessoires) dans la copie complète.

**À noter** : la base locale a changé de port (10005 → 10006) après le redémarrage de Local ; `wp-config.php` et `lancer.ps1` de la copie sont mis à jour.

### Correction du §24 (17/10) : produit de test non configurable
- **Erreur** : le premier produit de test reprenait les champs APF de la Duke (configurable), donc des **broderies en option**, qui n'existent pas sur une selle non configurable. Le gabarit, lui, affiche bien les champs propres à chaque produit (la maquette ne sert qu'au design) ; c'est le contenu du test qui était inventé.
- **Corrigé** : le produit de test recopie maintenant la **fiche publique de prod « Selle confort moto Yamaha R6 »** (non configurable, lue le 17/10) : prix 265 → 225 €, caractéristiques (la broderie fait partie du modèle : « Logo Yamaha en blanc et r6 en blanc »), catégorie, étiquettes, champs hauteur, gel, informations et type de commande « Modification » seul, avec son texte. Photo : celle de la R6 configurable de la copie.
- **Fiche non configurable ajustée au contenu d'origine** : « Délai de 1 mois » (selle fabriquée sur commande ; l'état du stock seulement pour la catégorie « En stock »), caractéristiques et « Ce modèle de selle est disponible : Modification » dans la boîte d'achat (sous le bouton, qui reste visible), « Prix de base (sans options) », accordéon « Modification, délai et livraison ».
- Test : hauteur -2 cm, gel 2 assises, infos, Modification : **305 €** (225 + 10 + 70), identique au panier. Non reproduit : les mensualités Cofidis de la fiche d'origine (extension de paiement absente des copies).

## 25. Automatisations : fiche d'habillage et courriel « En fabrication » (17/10)

Volet offert « Audit des tâches manuelles automatisables ». Sources : code des extensions de la prod lu dans le clone (lecture seule), une commande de Melvin (juin-juillet 2026) pour les courriels reçus, captures de Melvin dans l'admin. Aucune commande client consultée.

### Ce que le site produit déjà à partir d'une commande

| Document | Outil | Contenu | Production |
|---|---|---|---|
| Bon de livraison (« bon de commande » pour Valérie, à confirmer) | WooCommerce PDF Invoices & Packing Slips, modèle maison du thème enfant (`woocommerce/pdf/facture-sellerie-confort/`) | Client, livraison, paiement, selle, **délai de fabrication** (ajout VIMAWEB du 30/05/25), toutes les lignes de la commande (configuration + champs APF), « Caractéristiques selle » | Contenu automatique ; création automatique ou au clic : réglage en base, **à vérifier** |
| Variante « avec étiquette » | Idem (`packing-slip-avec-etiquette.php`) | Le bon + un encadré « Étiquette de suivi de fabrication » par selle | Idem ; laquelle des deux est utilisée : à demander |
| **Étiquette de production** (colonne « Etiquettes prod ») | `product-manufacturing-label` : extension d'étiquettes d'expédition modifiée | N° de commande, client, date, moto + année, selle chauffante, gel, TP / Pi / Pa (taille et poids pilote, poids passager), hauteur, type de commande | **Un clic par commande**, imprimante d'étiquettes (à confirmer) ; marque la commande « imprimée » (`_printed`) |
| Facture | WCPDF, modèle maison | Comptable | Selon réglages |

**L'étiquette sert à la base et à la mousse** (identification, morphologie, gel) : elle ne lit que les champs APF, donc **aucune matière ni couleur** ; broderie, motif et commentaires sont **masqués exprès** (`hideproductfieldstab`). L'habillage (matières, liserés, surpiqûres, broderie) est aujourd'hui recopié **à la main** sur une fiche interne, que nous n'avons pas vue.

### Fiche d'habillage : bouton « Habillage » (retenu par Melvin)

![[sellerie-confort-fiche-habillage-maquette.png]]

Maquette A4 (données fictives, selle KTM Duke composée à partir des calques publics) : ![[sellerie-confort-fiche-habillage-maquette.pdf]]. Source : `Phase 1/fiche-habillage/` (`maquette-fiche-habillage.html`, `composer_visuel_duke.py`).

- **Bouton « Habillage »** à côté de « Etiquette » dans la liste des commandes, + action groupée (imprimer les fiches des commandes cochées). **A4**, imprimante couleur ; l'étiquette reste sur l'imprimante d'étiquettes. Travailler par lot (toutes les étiquettes, puis toutes les fiches) : Chrome garde la dernière imprimante.
- **Contenu** : en-tête (n°, date, client, échange standard, délai, broderie, gel) ; **image de la selle configurée** ; **pilote et moto** (moto et année, taille, poids pilote et passager, hauteur) ; options ; **habillage** zone par zone (pastille couleur, case « Coupé ») ; **broderie** avec **vignette du motif**, fil, case « Brodé » ; **commentaires en entier** (client, informations complémentaires, note interne `_sc_order_note`) ; suivi atelier (coupe, couture, broderie, contrôle).
- **Règles** : la fiche lit **tous** les champs de la commande (un champ inconnu va dans « Autres informations ») ; les cadres de commentaires restent **imprimés même vides**, pour écrire à la main.
- **Image** : `mkl_pc` superpose déjà les calques choisis en une image (`save_image`, `merge`, REST `mkl_pc/v1/merge/…`). En 1.7.6, l'image est recalculée depuis la configuration actuelle (une matière retirée peut la changer) ; la 2.0.0 fige image et noms à l'achat.
- **Montage** : mu-plugin à part, l'extension de VIMAWEB n'est pas modifiée. **Charge : 1,25 à 1,5 j.**
- **À obtenir** : photo de la fiche manuelle actuelle (ordre des rubriques), confirmation de l'imprimante d'étiquettes et de la présence d'une imprimante couleur.

### Courriels après commande : ce qui existe déjà

Courriels reçus pour une commande de Melvin (n° 153844) : compte créé, commande reçue (avec pièce jointe), justificatif de paiement (9 juin) ; **« Note ajoutée à votre commande »** puis **« Commande expédiée »** (23 juillet) ; courriels DPD (livraison, arrivée en relais) ; commande terminée (25 juillet).

**La note de suivi DPD est automatique, pas manuelle** (vérifié dans le code) : texte « Cher client, vous pouvez suivre la livraison de votre colis DPD en cliquant sur ce lien : https://my.dpd.fr/<n° de colis> » = extension **DPD France 6.0.1** (`dpd-woocommerce`), tâche planifiée **horaire** `dpd_schedule_status_update` en mode « lien de suivi par numéro de colis » (`ScheduledActions.php`, lien `my.dpd.fr/`) : elle ajoute une **note client** (`add_order_note($note, 1)`, d'où le courriel « Note ajoutée ») puis passe la commande au statut d'expédition (d'où « Expédiée »). L'action groupée manuelle de l'extension produirait un lien `dpd.fr/tracex_…`, absent ici. Conséquence : la tâche DPD tournait en juillet 2026 ; elle n'est probablement pas parmi les 447 tâches en échec.

**Ce qui manque** : rien entre la commande et l'expédition (**6 semaines de silence** sur cet exemple, pendant la fabrication). Inutile d'ajouter le lien DPD à nos courriels : DPD et sa note le font déjà.

### Courriel « En fabrication » au clic sur l'étiquette (retenu par Melvin)

- Déclencheur : le clic sur **« Etiquette »** (la commande passe `_printed = yes` par l'appel `mark_order_as_printed`) → statut « En fabrication » → courriel au client « Votre selle est en fabrication », avec le délai (règle du bon de livraison : « En stock » ou étiquette « délai de … » du produit).
- Montage : statut maison (vérifier d'abord la liste existante dans Custom Order Status) + classe de courriel WooCommerce (`woocommerce_email_classes`, modifiable par Valérie dans Réglages › E-mails) ; désactiver le courriel générique de Custom Order Status pour éviter les doublons.
- Option : courriel à mi-délai (« votre selle avance, livraison prévue vers le … »).
- **Charge : 0,25 à 0,5 j.**
- À capturer dans l'admin de la prod avant de coder : statuts personnalisés existants, courriels actifs (Réglages › E-mails).

### Autres pistes listées (à chiffrer avec les volumes de Valérie)
Échange standard : relances client J+7 / J+10 et alerte J+12 pour la caution (le contrôle des 10 jours est désactivé dans `woo-payline-caution`), 1 à 1,5 j · panier perdu : lien de reprise et relance, 1,5 à 2,5 j · demande d'avis après livraison, 0,25 à 0,5 j · envoi mensuel des factures au comptable, 0,25 à 0,5 j. Retirée : « notes de commande préremplies » (supposition sans fondement ; la colonne « Notes » est une note interne libre).

## 25. Revue design et textes des fiches et du configurateur (17/10)

- **Méthode** (choix de Melvin : A + B + C) : skills `design-critique` et `ux-copy` en direct, puis trois agents en parallèle sur un brief commun (aucun texte inventé, aucun fichier modifié) : **UI Designer** (design visuel), **UX Researcher** (parcours d'achat et reformulations), **UI Finish-Gate Reviewer** (finition et accessibilité, pages ouvertes dans Chrome, axe-core). Verdict du contrôle final : **HOLD**, 4 bloquants.
- **Bloquants corrigés** : police, couleurs et focus clavier écrasés par le CSS en ligne de Divi (la feuille du thème est maintenant chargée après) ; type de commande et hauteur **cochés à la place du client** (plus de choix par défaut, blocage à la validation avec message) ; selle rognée dans l'aperçu.
- **Autres corrections** : zones nommées, familles sur une rangée, étapes nommées, sélection nette, cibles de 44 px, boîte d'achat non coupée, délai cohérent (« Fabrication sur commande », Goldwing 3 mois), modalités visibles, fil d'Ariane commun fiche/configurateur, textes reformulés **sans information nouvelle**.
- **Restent** : aperçu de la Duke (logo incrusté dans la photo de base : il faut une photo sans broderie) ; fautes des textes APF et du contenu produit (à corriger par Valérie) ; « 45 jours » contre « 1 mois » (au client) ; panier à refaire ; conditions APF des champs supplémentaires.
- Tests rejoués après corrections : Duke, BMW R 1200 RT, FJR 1300, Z900 (2.0.0), fiche configurable et non configurable : paniers et totaux identiques.
- Détail et tableau complet : `Phase 1/maquette-branchee/revue-design/revue-synthese.md` (brief des agents : `brief-revue.md`, revue A : `revue-A-claude.md`, script appliqué : `appliquer_revue.py`). Captures `poste3-voieB-17` à `-19`.

### Compléments du 17/10 (suite) : courriels, panier perdu, avis, caution

**Courriels automatiques actuels.** Gabarits **WooCommerce** (réglables dans WooCommerce › Réglages › E-mails), envoyés par l'extension **WP Mail SMTP** (le service d'envoi réglé est en base : à lire dans les en-têtes d'un courriel reçu, « Afficher l'original »). S'y ajoutent les courriels d'extensions : note de suivi DPD, statut « Expédiée » (Custom Order Status), « Prélèvement de la caution » (`woo-payline-caution`), cartes cadeaux, notifications WPForms. **Aucun outil d'emailing commercial** (lettre d'information, promotions) n'est installé. L'« emailing à la main » du CR du 07/10 désigne probablement les courriels écrits par Valérie (dont la relance de retour de selle, confirmée par Melvin) : à lui demander.

**Cartes cadeaux : piste retirée.** Version gratuite de PW Gift Cards : pas de date d'expiration (fonction de la version Pro, `set_expiration_date` vide), donc rien à rappeler.

**Avis clients** : J+15 **après la livraison** (passage en « Terminée » par DPD), lien vers la fiche Google. Aucune extension d'avis installée. 0,25 à 0,5 j.

**Configuration perdue, panier perdu : deux problèmes.**
- **Configuration perdue avant le panier** : le configurateur `mkl_pc` n'enregistre rien (aucune sauvegarde navigateur dans son code ; module payant « Save your design » chez l'éditeur). Rechargement, retour arrière ou onglet fermé = tout est perdu.
- **Panier perdu après l'ajout** : piste trouvée en lecture publique de la prod (en-têtes seulement). Les fiches produit sont servies par le **cache serveur o2switch** (`x-lsadc-cache: hit`, « PowerBoost », en plus de LiteSpeed Cache, `max-age` 7 jours), **même quand la requête porte les cookies de panier WooCommerce** (`woocommerce_items_in_cart`, `wp_woocommerce_session_*`) : un client qui a un panier reçoit la même page en cache que tout le monde (compteur de panier, messages, jetons de sécurité figés jusqu'à 7 jours). La page panier, elle, n'est pas en cache. **Hypothèse à vérifier** par un test de visiteur (Melvin ou Valérie : ajouter au panier, revenir sur une fiche et sur l'accueil, regarder le compteur et le panier) puis, si confirmé, exclure les visiteurs ayant un panier du cache o2switch (réglage serveur, à faire par le titulaire de l'hébergement).

**Prototype fait sur la copie (17/10)** : `Phase 1/relance-panier/` (mu-plugin `sc-relance.php`, README, test `test-relance.mjs`, captures). **16 vérifications sur 16** :
1. Configuration en cours **sauvegardée dans le navigateur** (adresse `#z=…` de la maquette + infos pilote, 30 jours) et **remise au retour** avec le message « Votre configuration du … est retrouvée » et « Recommencer à zéro ».
2. **« Recevoir par e-mail »** dans le **récapitulatif seulement** (à côté de « Partager » ; l'encadré de l'étape 4, à côté du panier, est retiré pour ne pas inciter à remettre l'achat à plus tard) : adresse + même schéma que le panier (décision de Melvin) : mention en petit « Si vous ne commandez pas, nous pourrons vous envoyer deux rappels (24 h et 72 h après) » et case **« Je ne veux pas de rappel »** (vérifié : cochée, aucun rappel) ; courriel au gabarit WooCommerce avec **image de la selle**, choix, total et bouton **« Reprendre ma configuration »** qui rouvre configuration **et** infos sur un autre appareil ; **rappels à 24 h et 72 h** ; désinscription en un clic dans chaque message.
3. **Capture au paiement** : mention et case « Je ne veux pas de rappel » sous le champ e-mail ; copie du panier ; relances à 1 h, 24 h, 72 h ; **lien de reprise du panier vérifié dans un autre navigateur** (selle et options retrouvées).
4. **Arrêt** dès qu'une commande payée existe avec la même adresse (vérifié), ou au clic de désinscription. Suivi dans WooCommerce › Relances. Sur le local, les courriels sont écrits dans `wp-content/sc-courriels/` (aucun envoi).

![[sellerie-confort-relance-formulaire.png]]
![[sellerie-confort-relance-courriel.png]]

Charge pour la prod : environ **2 à 2,5 j** (adaptation au configurateur retenu, textes avec Valérie, RGPD, tests d'envoi réel et de paiement), en plus du diagnostic du cache (0,25 à 0,5 j).

### Échange standard : retour de selle et caution

**Aujourd'hui (code de `woo-payline-caution`, Vimaweb)** : aucune alerte. Seuls repères :
- colonne **« Caution »** de la liste des commandes : bouton **« Prélever (n) »** pour chaque commande en échange standard payée par Payline, **dès le premier jour** (la mention « En attente » avant 10 jours est commentée dans le code) ; « Terminée » quand toutes les selles sont reçues ou les cautions prélevées ;
- fenêtre par selle : **« Selle reçue »** ou **« Prélever »** (débit immédiat de la carte enregistrée chez Payline, `do_immediate_wallet_payment`, puis commande séparée « caution payée » et courriel « Prélèvement de la caution ») ; montant par produit, puis catégorie, puis défaut ;
- **Cofidis : pas de bouton** (exclu dans le code). **Alma** : pas exclu, mais sans carte enregistrée chez Payline le prélèvement échoue (« Impossible de récupérer les informations du portefeuille »). **Carte virtuelle** (e-carte à usage unique ou courte durée) : le débit ultérieur échoue.
- Valérie parcourt la liste, calcule les délais de tête et écrit les relances à la main.

**Relance voulue par Melvin** : J+7 après la livraison, avec avertissement sur la caution. **Attention** : DPD passe la commande en « Terminée » à la livraison (courriel « terminée » 1 à 2 jours après la livraison sur l'exemple de Melvin) ; la condition « sauf si Terminée » bloquerait toutes les relances. Condition proposée : **selle non reçue et caution non prélevée** (données que l'extension tient par selle). Suite : 2ᵉ relance à J+14, résumé quotidien « Cautions à traiter » à Valérie, **prélèvement toujours validé par Valérie**. 1 à 1,5 j.

**Simplifier la gestion : deux voies**

| Voie | Contenu | Pour | Contre | Charge |
|---|---|---|---|---|
| A. Liste des commandes actuelle, enrichie | Colonne « Retour selle » : jours depuis la livraison, pastille verte / orange / rouge, relances envoyées ; vue filtrée « Échanges standard à traiter » ; action groupée « Selle reçue » | Rien de nouveau à apprendre | Mélangé aux autres commandes ; les cas sans carte (Alma, Cofidis) restent hors outil | 0,5 à 0,75 j |
| B. **Écran « Échanges standard »** (WooCommerce › Échanges standard) | Une ligne par selle à récupérer : commande, client, date de livraison, J+, relances, moyen de paiement (carte enregistrée ou non), montant ; boutons Selle reçue / Prélever / Relancer / Envoyer un lien de paiement ; historique. **Gère aussi les relances de caution des clients sans carte prélevable** (paiement en 3-4 fois Alma ou Cofidis, carte virtuelle) : relance du retour de selle puis, à défaut, lien de paiement de la caution et relances de ce lien (demande de Melvin, 17/10) | Tout au même endroit, y compris les cas sans carte ; base des relances automatiques | Un écran de plus à maintenir | 1 à 1,5 j |

**Recommandation : B**, en gardant le bouton « Selle reçue » dans la liste des commandes. Les deux voies partagent les relances (1 à 1,5 j ci-dessus).

**Caution impossible à prélever (paiement en 3-4 fois, carte virtuelle) : solutions**

| Solution | Principe | Pour | Contre |
|---|---|---|---|
| 1. Empreinte de carte séparée | Pour un échange standard payé avec Alma ou Cofidis : enregistrement d'une carte chez Payline (portefeuille, sans débit) à la fin de la commande | Même fonctionnement qu'aujourd'hui ensuite | Une étape de plus pour le client ; carte virtuelle toujours refusée ; carte expirée possible |
| 2. **Consigne encaissée puis remboursée** (modèle des pièces auto) | La caution est payée à la commande, remboursée au retour de l'ancienne selle (remboursement déclenché par « Selle reçue ») | Aucun risque d'impayé, marche avec toute carte, y compris virtuelle | Le client avance 200 à 400 € ; financement par Alma/Cofidis à vérifier ; possible frein à la vente |
| 3. Pré-autorisation | Blocage du montant sur la carte | Pas de débit | Validité d'environ 7 jours, trop courte avec un mois de fabrication |
| 4. Mandat SEPA | Mandat de prélèvement signé à la commande | Indépendant de la carte et du financement | Nouveau prestataire ou option Payline, contestation possible 8 semaines |
| 5. Lien de paiement à J+14 | Si pas de retour et pas de carte : lien de paiement envoyé (depuis l'écran B) | Simple, peu de développement | Aucune garantie : repose sur la bonne foi, recours sinon |
| 6. Règle commerciale | Échange standard réservé au paiement comptant par carte (Alma, Cofidis masqués pour ce type de commande) | 0,25 j, risque supprimé | Ventes financées perdues ou à basculer en « Modification » |

Proposition : court terme **6 ou 5** ; moyen terme **1** ou **2** selon les chiffres. À demander à Valérie : part des échanges standard payés en plusieurs fois, nombre de selles non renvoyées par an et montant perdu, ce qu'elle fait aujourd'hui quand le paiement est passé par Cofidis, délai réel accordé (10 jours après réception ?), moment du passage en « Terminée », texte de sa relance actuelle.

### Ajustements demandés par Melvin après la revue (17/10)
- **Zones** : les 8 pastilles sur 2 rangées de 4 (une rangée débordait et masquait Liserés et Surpiqûres).
- **Broderies** : **couleurs et commentaire sous chaque emplacement** (dosseret, puis bandes), au lieu d'une palette commune en bas ; **5 motifs par ligne** (vignettes plus petites). Sur la Z900 (logos en calques), chaque emplacement a son fil (ex. dosseret rouge vif, bandes blanc). APF n'ayant qu'un champ « Couleurs broderie », on y coche l'union des couleurs et le détail par emplacement va dans « Autres couleurs / Précisions couleurs » (ex. « Dosseret : Gris souris (commentaire) ; Bandes : Gris macadam (commentaire) »). Vérifié au panier (FJR 1300, Z900).
- Motifs APF sans image sur la copie (médias absents) : le nom du motif s'affiche à la place.
- **Tout tient dans l'écran à 100 %** (demande de Melvin) : zones sur une seule rangée (une colonne par zone, nom court dessous), **toutes les familles visibles** (puces compactes sur 3 lignes au lieu d'une rangée qui défilait), en-tête « Matières & couleurs » masqué (le nom est dans l'onglet), mention « rendu non contractuel » déplacée dans le récapitulatif. Mesuré sans défilement dans le panneau en 1920×960 et 1440×790 ; sur un écran de 1366×650, le configurateur dépasse encore de 50 px.
- **Survol de la selle** : vignette avec la matière de la zone, son nom et « Cliquer pour modifier », et la pastille de la zone mise en évidence dans le panneau ; le clic sur la selle choisit la zone (déjà présent dans la maquette, rendu visible).
- **Logos brodés : les 26 couleurs de fil et plusieurs couleurs possibles** (demande de Melvin) : la palette des logos est maintenant celle des surpiqûres (= champ APF « Couleurs broderie », 26 couleurs) au lieu des 4 fils du prototype, avec choix multiple. **Aperçu** : si le logo n'existe pas en image dans la couleur choisie (seuls blanc, rouge vif, vert brillant, jaune citron existent), la page recolore l'image en fil blanc avec la première couleur choisie (canvas, découpe et relief conservés). **Panier** : APF reçoit toutes les couleurs (« Couleurs broderie » et détail par emplacement) ; la ligne du plugin indique le logo dans le fil le plus proche disponible (ex. « Yeux - fil blanc ») : à terme, un calque par logo sans couleur figée (option B) éviterait cette ambiguïté.
- « **Sans broderie** » est maintenant la première tuile des motifs du dosseret.
- **Tout le bloc blanc tient dans la fenêtre à 100 %** (demande de Melvin) : la hauteur du configurateur est calculée sur la fenêtre réelle (barre d'administration, en-tête et titre compris) au lieu de valeurs fixes ; puces de familles plus compactes et panneau un peu plus large sur grand écran (2 lignes de familles en 1920 px, 3 en 1440 px) ; compteur « zones personnalisées » abrégé sous 1600 px. Mesuré sans défilement : 1920×880, 1920×950, 1440×760 ; en dessous de 1366×640, le configurateur garde une hauteur minimale de 500 px.

**Aujourd'hui, sans carte prélevable (Alma, Cofidis, carte virtuelle)** : rien dans le site. L'extension n'a ni lien de paiement ni courriel pour ce cas (vérifié dans son code : Cofidis exclu, Alma sans portefeuille Payline, aucun lien `order-pay` ni envoi). Ce que fait Valérie (lien de paiement depuis l'espace Payline/Monext, virement, chèque, appel) n'est pas visible : **à lui demander**.

**Commander plus tard ? (question de Melvin, 17/10)** Risque réel si le bouton est à côté de « Ajouter au panier ». Fait sur la copie : bouton seulement dans le récapitulatif ; **proposition au départ** « Vous partez ? Gardez votre selle » (une fois par visite, client engagé, ni envoi ni clic panier ; souris qui sort par le haut sur ordinateur, 60 s d'inactivité sur téléphone ; pas de piège sur le bouton retour) ; **bilan** dans WooCommerce › Relances (envois et commandes par origine, délai moyen avant commande) pour décider après quelques semaines de garder, déplacer ou retirer le bouton.
- **Survol de la selle corrigé** : la carte des zones était calculée sur le seul coin haut-gauche des images réelles (1920×1280, la maquette utilisait des images de 640×427), d'où des zones annoncées au mauvais endroit. L'image entière est maintenant prise en compte, et les zones fines (liserés, surpiqûres) ne « captent » plus la souris à 2 px quand une grande zone est exactement dessous. Testé point par point : Duke, Z900 et BMW R 1200 RT, toutes les zones reconnues.
- **Familles de matières en tuiles uniformes** (4 par ligne) : aperçu des 3 premières matières de la famille, nom court (premier mot du nom réel : Noirs, Gris, Bleus, Rouges, Oranges, Verts, Blancs ; nom complet en infobulle) et nombre de matières. **Tout le bloc blanc tient dans la fenêtre** mesuré à la taille d'écran de Melvin (1536×766 avec affichage Windows à 125 %) et en 1440×760.
