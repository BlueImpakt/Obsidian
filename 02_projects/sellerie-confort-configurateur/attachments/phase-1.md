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

| # | Poste | j | Livrable attendu | État au 15/10 |
|---|---|---|---|---|
| 1 | Audit du fonctionnement actuel et de la structure de données | 1,00 | Fonctionnement de `mkl_pc`, stockage, faisabilité du regroupement par famille | **Fait pour le regroupement (15/10)** : lot et famille testés sur la 1.7.6, voir §7. Lecture de `payment.php` et `active-plugins.php` faite (§8). Fichier public régénéré, 9 fiches atypiques listées, conclusion en fin de §10 (« Compléments poste 1 »). **Poste 1 clos** ; reste le test de la 2.0.0, optionnel (paquet non disponible, voir §7). |
| 2 | Clone local complet (données et médias), isolé de la production | 0,40 | Site local isolé, sans donnée personnelle | **Fait** : 345 produits, 15 121 médias, Divi, catégories, « Ma Moto », options APF. Reste cosmétique (3 médias en erreur, menus du pied de page). |
| 3 | Tests de rendu matières/couleurs, comparés aux photos réelles | 0,60 | Comparaison au rendu réel (SSIM/ΔE) sur un échantillon | **Fait (15/10)** : générateur couleur + texture, validé sur 5 modèles, voir §6. Couleur : faisable (ΔE ≈ 2,5). Matières unies : rendu correct. **Matières texturées : la recette de Valérie est retrouvée** (texture maître 1920 × 1280 par matière, découpée par le masque de chaque zone) ; régénération à l'aveugle exacte au pixel pour une partie des matières, voir §10. Surpiqûres = couleur unie. |
| 4 | Tests broderies / logos / nid d'abeille | 1,00 | Verdict de faisabilité chiffré par type de broderie | **En cours.** Nid d'abeille : le calque se pose sur sa photo d'origine, le transfert vers le rendu du configurateur n'est pas résolu. Logos : aucun essai consigné ; cas d'usage identifié, retirer le logo incrusté dans la photo de fond d'une forme de selle réutilisée (Tiger 900 avec GS) ou en poser un autre. |
| 5 | Estimation du temps de généralisation au catalogue | 0,30 | Temps pour passer de l'échantillon aux 46 configurations | **Données prêtes** (46 configurations, 302 couches distinctes, ≈ 10 900 images). Poste 3 et regroupement faits (§6, §7) ; dépend encore du poste 4. |
| 6 | Rapport de synthèse, chiffrage Phase 2, plan d'action avec calendrier | 0,70 | Rapport remis à Valérie | **Charpente existante** (Phase 2 : 14 à 24 j, plafond 16 j). À finaliser en dernier. |

## 2. Offert dans la Phase 1

| Volet | Livrable attendu | État au 15/10 |
|---|---|---|
| Audit des tâches manuelles automatisables | Liste des tâches avec temps et coût estimés (rappels, emailing, bons de commande) | **Pas commencé.** Source : CR de la réunion du 07/10. |
| Diagnostic de la perte de panier | Diagnostic avec préconisation (cookies, sauvegarde de session) | **Pistes** : `payment.php` écartée (§8, équivalent au modèle actuel) ; restent 447 tâches planifiées en échec, cron à vérifier, tous les plugins chargés sur panier et paiement (§8), absence de cookies. Préconisation à rédiger. |
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
