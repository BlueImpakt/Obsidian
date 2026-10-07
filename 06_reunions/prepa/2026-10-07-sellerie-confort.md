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
| Objection                                           | Réponse                                                                                                                  |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| « Pourquoi payer avant d'avoir le devis complet ? » | La Phase 1 est ce qui rend le devis ferme : on teste sur votre matière avant de s'engager. 1 600 € déduits de la Phase 2 |
| « L'IA ne vaudra jamais une vraie photo »           | Exact, on ne le promet pas. Photos actuelles conservées, étape 1 optionnelle, on mesure l'écart en Phase 1               |
| « Et VIMAWEB ? »                                    | Travail sur une copie locale, jamais en ligne. Il est informé. Qui met en prod en Phase 2 : à décider ensemble           |
| « Combien pour la suite ? »                         | Forfait jour chiffré à l'issue de la Phase 1, pas avant                                                                  |
| « On pourrait tout refaire à neuf ? »               | Possible plus tard, mais ce n'est pas l'objectif : on restructure le configurateur existant d'abord                      |

### Ce qui peut coincer (pour moi, en simple)
D'après l'audit du site public ; je n'ai pas vu l'admin. Les points « à vérifier » sont à trancher en Phase 1.

**Phase 1 (les tests)**
- **Copier le site :** il est très lourd (≈ 35 Go de photos). On n'en copie qu'une partie, assez pour tester
- **Les logiciels payants (à vérifier) :** certains outils du site demandent une licence liée à son adresse. Sur ma copie, ils peuvent refuser de marcher
- **Les matières brillantes ou pailletées :** plus difficiles à reproduire que les mates. Il faudra peut-être garder les photos
- **Les broderies :** le plus dur. Il faut effacer le logo déjà présent sur la photo, puis en dessiner un autre qui suit les courbes de la selle, en plusieurs couleurs possibles
- **Les tests ne prouvent pas tout :** ils disent « oui », « non » ou « oui avec des limites », mais ne livrent pas un système prêt à vendre

**Phase 2 (la construction)**
- **Le logiciel du configurateur n'est pas à moi :** s'il se met à jour, ce que j'ai ajouté peut ne plus marcher. Je travaille à côté de lui, sans le modifier, et je teste avant chaque mise à jour
- **Les photos sont très nombreuses (≈ 83 000) :** le site grossit, les sauvegardes aussi. On les compresse
- **Les anciennes commandes :** les couleurs choisies doivent garder les mêmes identifiants, sinon les anciens paniers et commandes s'embrouillent
- **Les broderies sont dans un autre formulaire :** ce que la cliente voit sur la selle doit correspondre à ce qu'elle commande
- **Le design :** les maquettes sont des pages à part. Il faudra les refaire à l'intérieur du site existant

### Le prestataire de maintenance (VIMAWEB) et la mise en ligne
- **Phase 1 : je n'ai pas besoin de lui.** Mais il surveille le site : un compte inconnu ou un nouvel outil peut déclencher une alerte. **Valérie le prévient avant** (article 2 du contrat)
- **Phase 2 :** il gère probablement l'hébergement et les sauvegardes. Il peut me ralentir ou me bloquer (refuser un accès, dire que mon travail a cassé le site). Son contrat de maintenance exclut peut-être les interventions d'un tiers
- **Le plus sûr :** que les accès à l'hébergement soient au nom de Valérie, pas au sien
- **Mise en ligne : rien ne m'oblige à passer par lui** si Valérie m'autorise par écrit. Trois options : (1) moi, avec les accès qu'elle me donne ; (2) lui, avec ma livraison et ma procédure ; (3) les deux : je teste sur une copie chez l'hébergeur, puis on met en ligne ensemble. Mon avis : 1 ou 3, lui toujours prévenu, sauvegarde avant, plan de retour
- **À redire autrement demain :** mon mail du 7 août promettait de ne pas toucher « à la logique technique du site ni aux outils de VIMAWEB ». Mettre en ligne le contredit. Dire : « je travaille sur une copie, et on décide ensemble de la mise en ligne »

### Rester compatible avec l'existant
- Ne rien modifier dans le logiciel du configurateur : je construis une pièce à côté qui s'y branche
- Écrire dans son format : si ma pièce disparaît, le configurateur continue de marcher
- Travailler dans les mêmes conditions que le vrai site (mêmes versions de PHP, WordPress, WooCommerce 11.1, Divi, plugins ; infos dans Outils > Santé du site)
- Tester avant chaque mise à jour : quelques fiches, le panier, les prix barrés, le paiement
- Ne pas changer les adresses des pages ni les identifiants des choix

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
- **Les accès à l'hébergement et au nom de domaine sont-ils au nom de Valérie ?** Où est hébergé le site, y a-t-il un environnement de test ?
- Quels plugins sont sous licence payante (configurateur, `wapf`, Divi) et au nom de qui ? Y a-t-il un contrat de maintenance avec VIMAWEB, et que prévoit-il en cas d'intervention d'un tiers ?
- Accepte-t-elle que je déploie en production en Phase 2, avec VIMAWEB informé, ou préfère-t-elle qu'il le fasse ?
- **Pour les maquettes :** avez-vous le logo en fichier vectoriel (SVG, AI ou PDF) et une version blanche ou en négatif pour fond sombre ? Avez-vous des photos de l'atelier (mains, cuir, coutures) ? Aujourd'hui le logo est un PNG et la photo d'accueil est une moto générique
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
- Maquettes corrigées le 06/10 : fond beige passé en blanc (sections alternées en gris neutre `#F5F5F5`), extrait de JavaScript qui s'affichait sur `index.html` supprimé. Maquettes refaites le 07/10 : double-clic sur `sellerieconfort-refonte/Maquette/lancer-maquettes.bat` (serveur local, fonctionne sans internet). Parcours à montrer : accueil → recherche « R6 » → fiche → configurateur (personnaliser les 8 zones) → ajouter au panier → panier

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
