---
tags: [prepa-reunion, sellerie-confort]
created: 2026-10-06
client: sellerie-confort
---

# 2026-10-07-sellerie-confort

## Objectif de la réunion
- **Obtenir la signature** de la Phase 1 (devis I-26-08-1, 1 600 € HT, 4 j) et du contrat mis à jour
- **Fixer le démarrage** : date, accès WordPress admin, qui les crée
- **Comprendre le flux réel de fabrication** des images (outil, temps, fréquence) : c'est le gain à chiffrer pour la Phase 2
- Faire valider la direction et le niveau de réalisme attendu des rendus IA
- Support visuel : [[sellerie-confort-reunion-2026-10-07.excalidraw]] (6 blocs à parcourir dans l'ordre)

![[sellerie-confort-reunion-2026-10-07.excalidraw]]

## Contexte / passif
- Fiches : [[sellerie-confort]] · [[sellerie-confort-configurateur]]
- Contact : Valérie Cenizo, co-gérante. Fait elle-même le contenu et a les accès WordPress. VIMAWEB = maintenance, ARTEO Conseil = créateur du site
- Début août : maquettes vues et validées (seule remarque : le beige). 7 août : elle demande de simplifier l'ajout de couleurs/matières et d'afficher les logos sur la selle, et demande un prix
- Phase 1 pas démarrée. Contrat du 07/08 jamais signé, **version mise à jour le 06/10** (clone sélectif sans clients/commandes, outils d'IA tiers, durée, Phase 2 sur devis en forfait jour). Dates laissées en blanc
- Audit externe passif du site fait le 06/10 (détails dans le projet)

### Chiffres à citer (vérifiés sur les fichiers publics, à présenter comme des estimations)
- **≈ 220 images par selle** (≈ 294 pour les selles en 2 parties) : 37 matières × 4 zones + 44 liserés + 26 surpiqûres + 2 fixes
- **345 fiches configurables** sur 1 520 produits, soit ≈ **83 000 images ≈ 35 Go**
- Une seule vue ("Face") par selle ; structure quasi identique d'une fiche à l'autre (3 gabarits sur 45 fiches vérifiées)
- La fiche phare BMW GS LC est une copie (`...-copie`) : illustration de la duplication manuelle
- Le Carbone vient d'être supprimé : géré par une fenêtre d'information (plugin `sc-notice-carbone`), pas par le configurateur

### À ne pas citer
- Les chiffres du `.xlsx` (35 749 produits : faux) ; Payline (non détecté) ; migration headless Next.js/MedusaJS (hors sujet)
- Aucun chiffre de Phase 2 demain (il vient du rapport)

## Points à aborder
Ordre conseillé, avec le schéma Excalidraw :

1. **Accroche (5 min), bloc 1 « Aujourd'hui ».** Reformuler avec ses mots : un fichier par zone, par matière et par modèle. Montrer la capture de la médiathèque (`attachments/usine-a-gaz-mediatheque-f900xr.png`) et les chiffres. Faire valider : « c'est bien ça ? »
2. **Son flux réel (15 min).** Voir les questions ci-dessous. Noter les chiffres : temps par modèle, fréquence, outils
3. **La cible (10 min), bloc 2 « Demain ».** 3 étapes + broderies. Insister : les étapes 1 et 2 vont ensemble (la 2 seule simplifie la saisie, la 1 supprime la fabrication). Étape 1 optionnelle, les photos actuelles sont gardées. Puis **montrer les maquettes** comme vision cible, hors Phase 1, sans engagement
4. **Phase 1 (10 min), bloc 3.** 6 briques, 4 jours, livrable = rapport. Dire ce qu'elle obtient : un oui/non/avec limites sur chaque brique, et un chiffrage ferme de la Phase 2 en forfait jour
5. **Cadre (10 min), blocs 4 et 5.** Accès temporaires, clone sélectif sans données clients, rien touché en ligne, échantillon de photos envoyé à des outils d'IA. Rôles VIMAWEB/ARTEO
6. **Démarrage (5 min), blocs 5 et 6.** Date, accès, interlocuteur côté webmaster, modèles échantillons. Signature si possible

### Positionnement technique (pour moi, pas à détailler)
- Pas de « l'IA va tout faire » : **compositing déterministe en piste principale** (masques déjà présents dans les PNG, texture, ombrage de la photo de base), IA en renfort (masques de nouveaux modèles, retrait/ajout de logos)
- Matières brillantes/chromées/pailletées (liserés) : garder les photos, système hybride
- Broderies : réponse nette en fin de Phase 1 ; plusieurs couleurs combinables imposent un rendu à la volée, un autre ordre de difficulté que les matières
- Étape 2 = couche sur-mesure autour du plugin tiers (aucun référentiel de matières global aujourd'hui : l'ID de « Gris tonnerre » change selon la couche), donc dépendance à VIMAWEB pour la mise en prod : à clarifier

### Objections probables
| Objection | Réponse |
|---|---|
| « Pourquoi payer avant d'avoir le devis complet ? » | La Phase 1 est ce qui rend le devis ferme : on teste sur votre matière avant de s'engager. 1 600 € déduits de la Phase 2 |
| « L'IA ne vaudra jamais une vraie photo » | Exact, on ne le promet pas. Photos actuelles conservées, étape 1 optionnelle, on mesure l'écart en Phase 1 |
| « Et VIMAWEB ? » | Travail sur une copie locale, jamais en ligne. Il est informé. Qui met en prod en Phase 2 : à décider ensemble |
| « Combien pour la suite ? » | Forfait jour chiffré à l'issue de la Phase 1, pas avant |
| « On pourrait tout refaire à neuf ? » | Possible plus tard, mais ce n'est pas l'objectif : on restructure le configurateur existant d'abord |

## Questions à poser
**Priorité 1 (changent le chiffrage)**
- Combien de temps prend l'ajout d'**un nouveau modèle**, et d'**une nouvelle matière** ? À quelle fréquence ?
- Comment sont fabriqués les ~220 PNG : quel outil (Photoshop ?), qui le fait, avec quelles sources ? **Existe-t-il des PSD ou des découpes d'origine ?**
- Plusieurs motos partagent-elles la même forme de selle ou chaque fiche est-elle unique ?
- D'où viennent les photos de patchs (matière posée sur la selle, photographiée) ? Les textures existent-elles en scan ou en fichier à part ?
- Les 9 motifs de broderie existent-ils en fichiers vectoriels ou de broderie ? Le client doit-il voir **plusieurs couleurs** sur la selle ?

**Priorité 2 (cadre et démarrage)**
- Quand les accès WordPress, et qui les crée ? Où est hébergé le site, qui valide une modification avant la mise en ligne ?
- Quel est le rôle exact de VIMAWEB et d'ARTEO ? Qui a installé et paramétré le plugin de configuration (version Pro, import en masse) ? Qui a écrit `sc-notice-carbone` ?
- Quels modèles servent d'échantillon (BMW GS LC ?) ?
- Qui tranche sur le niveau de réalisme d'un rendu ? Est-elle à l'aise avec des images générées par IA en vente ?
- Les fiches `-copie` / `-2`, `-3` sont-elles à garder ? Des modèles obsolètes ?

**Priorité 3 (suite du projet)**
- Budget et calendrier visés pour la Phase 2 ? Refonte visuelle de tout le site souhaitée ?
- La vue unique suffit-elle, ou plusieurs angles à terme ?
- Reçoit-elle la photo de patchs physiques dont elle parlait dans son mail (la capture de la médiathèque n'est pas forcément cette photo) ?

## À avoir avec moi
- Contrat Word mis à jour (+ PDF), devis I-26-08-1
- Schéma Excalidraw ouvert et zoomé sur le bloc 1
- Capture médiathèque F 900 XR
- Maquettes : `npx serve -l 5190 sellerieconfort-refonte` dans le repo `sellerie-confort` (page d'accueil, BMW, fiche produit, configurateur, matières, panier)
- **Avant de montrer les maquettes** : traiter la remarque sur le beige, et corriger le bug de `index.html` (un extrait de JavaScript s'affiche tel quel)

## Sortie de réunion (ce qu'il faut avoir obtenu)
- Contrat signé, ou date de signature fixée
- Date de démarrage de la Phase 1 et personne chargée de créer les accès
- Réponses aux questions de priorité 1, ou la manière de les obtenir (visite du poste de travail, échantillons)
- Choix des modèles échantillons
- Réaction de Valérie aux maquettes et à l'idée de rendu IA, pour le CR

## Liens
- Client : [[sellerie-confort]]
- Projet : [[sellerie-confort-configurateur]]
- Repo : https://github.com/BlueImpakt/sellerie-confort
