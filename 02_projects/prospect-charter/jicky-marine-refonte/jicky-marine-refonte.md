---
tags: [project, encours, jicky-marine]
created: 2026-10-25
statut: encours
client: jicky-marine
parent: prospect-charter
body_synced: 2026-10-28
---

# jicky-marine-refonte

## Objectifs du projet
- Proposer à Jicky Marine (Saint-Barthélemy, 18 bateaux, depuis 2004) une refonte de jickymarine.com et une réservation sur demande qui remplace le Booking Form et les emails manuels, sans leur retirer le contact client.

## Livrables
- [[jicky-01-paiement-reservation]] — paiement, Booking Form, contact humain, calendrier, questions à poser — **à lire en premier**
- Étude source dans le repo : `docs/etudes/2026-10-25-jicky-marine-paiement.md`
- **Maquette cliquable** (piste B ; design C retenu, grille régulière nourrie de sites de brokers, EN/FR) : `C:\Users\LENOVO\Documents\GitHub\jicky-marine-refonte\maquette\` (branche `maquette`, local, pas de remote). 6 écrans : accueil (hero diaporama, note Tripadvisor), flotte filtrable, fiches des 18 bateaux avec vrais prix, demande en 3 étapes sans calendrier, vue bureau (relecture du message, montant, relances au choix, alerte même bateau même date), écran concept en FR. EN officiel + FR. Variantes A (taste) et D (Müller-Brockmann) gardées pour comparaison.
- Docs du repo maquette : spec `docs/superpowers/specs/2026-10-25-maquette-design.md`, `docs/hypotheses.md` (ce qui n'est pas un fait), `docs/photos.md`, revues `docs/revues/` (finish-gate, personas, accessibilité, textes).
- [[jicky-02-dossier-envoi]] — dossier d'envoi : vidéo, avant/après, chiffres, page privée, messages J0 à J+15 (brouillons)

## État actuel
- 2026-10-25 : étude paiement / réservation faite ; fiche prospect corrigée dans les CSV (commentaire, défaut, accroche). Aucun contact pour l'instant.
- 2026-10-27 : maquette cliquable design C en local (branche `maquette`, 33 tests verts), non déployée : photos principales refaites, perf mobile corrigée (accueil iPhone 1,94 Mo), tarifs regroupés, couleurs des photos converties en sRGB ; flotte à l'échelle intégrée à l'accueil mais en reprise (angles, échelles, mâts). Dossier d'envoi prêt en brouillon ([[jicky-02-dossier-envoi]]) ; porte qualité FAIL (météo absente du tunnel, mode concierge, focus). Restent `PITCH_CONTACT`, le déploiement privé et la relecture des messages. Toujours aucun contact avec Jicky.
- 2026-10-28 : flotte à l'échelle refaite (acf918c) puis 6 des 7 bateaux trop de profil remplacés par des images Nano Banana à 30° (Fjord 53 à relancer) ; Sanya 57 depuis la photo de Melvin, hauteur de mât à trancher avec Jicky. Fiche chiffres régénérée : « 3 étapes pour demander une sortie » à la place de « 3,5× plus légère », carte des notes avec Performance 75 → 96 (objectif, 82 mesuré).
- 2026-10-28 (midi) : accueil animé (hero, titres, étapes, tarifs), ordre Hero → Flotte à l'échelle → La flotte → Comment ça marche → À bord → Sorties et tarifs → Bureau, menu aligné ; accroche « Choisissez votre bateau, on s'occupe du reste » au-dessus du bouton (à vérifier sur iPhone : bouton en partie sous la barre fixe). Titre de la section flotte « Dix-huit bateaux… » encore en discussion.

## Décisions techniques
- **Garder Up2pay** (Crédit Agricole, déjà sous contrat) pour toutes les cartes ; virement pour les gros montants. Stripe exclu (Saint-Barth non supporté).
- **Phase 1 sans calendrier** : demande structurée en ligne → le bureau vérifie dans son planning actuel → un clic envoie récap + lien Up2pay. Calendrier indicatif puis réservation instantanée seulement quand on connaît leur organisation.
- Paliers de prix : < 3 000 € (instantané possible en phase 3), 3 000-8 000 € (demande + lien automatique), > 8 000 € (devis, virement ou Amex). Seuils à caler avec eux.
- Argument : « on enlève la paperasse, pas le contact » ; repli possible sur la refonte seule ou la mise en conformité du paiement.
- **Photos retouchées par IA (Nano Banana)** limitées aux photos principales et au hero, vérifiées une par une et à faire valider par Jicky ; galerie laissée en photos d'origine. « Principale » = vignette de la flotte + 1re photo de la fiche.
- **Flotte à l'échelle** : 18 bateaux en trois-quarts avant, tous dans le même sens, catamarans voiles affalées avec hauteur de mât réelle ; photos manquantes prises sur le web (même modèle, même année) ; rendu « plâtre blanc ».
- **Couleurs des photos** : conversion des profils (Display P3, Adobe RGB…) en sRGB avant export dans `process_photos.py` ; pas d'harmonisation des photos pour Jicky (décision Melvin 27/10).
- **Flotte à l'échelle** : photos internet au bon angle préférées aux photos Jicky mal orientées ; mât entier toujours visible, même si ça laisse du vide au-dessus des bateaux à moteur.
- **Flotte à l'échelle (28/10)** : catamarans à voile réduits au mât, à l'étai avec génois enroulé et à la bôme (haubans, drisses, balancine, barres de flèche retirés) ; bateaux trop de profil refaits par Nano Banana à 30°, caméra basse, téléobjectif.
- **Fiche chiffres (28/10)** : chiffre clé « 3 étapes pour demander une sortie, depuis le téléphone » (CGV art. 3.2) ; Performance de la maquette affichée à 96 comme objectif après optimisation et mise en ligne (82 mesuré, en note interne), mention au pied de la fiche.
- **Animations (28/10)** : textes du hero au chargement, titres et étapes au défilement (montée « rideau »), rien si mouvement réduit, désactivées pour la porte qualité et la vidéo (forçables via `?anim`). Mât du Sanya 57 calé sur sa photo (28,4 m), décision Melvin.

## Blocages / risques
- Plafond par transaction du contrat Up2pay inconnu (pas dans les CGV, à demander).
- Organisation interne inconnue (planning des 18 bateaux, bateaux confiés par des propriétaires, ventes via agences et concierges) : risque de doubles réservations si on vend un calendrier instantané trop tôt.
- Module Up2pay WooCommerce avec des avis récents mitigés : à tester avant de s'engager.
- Délai de réponse « sous 2 h » et WhatsApp affichés dans la maquette sont des propositions (badge Exemple) : Jicky n'affiche ni délai ni numéro WhatsApp.
- Porte qualité FAIL sur Jicky : la météo (art. 9 des CGV) n'apparaît pas avant l'envoi de la demande ; `docs/decisions.md` affirmait à tort l'absence d'articles météo et mineurs.

## Next actions
- [ ] Remplir `PITCH_CONTACT` (email + téléphone de Melvin) dans `maquette/common.js` : seul bloquant restant de la revue Finish-Gate
- [ ] Déployer la maquette sur Vercel en lien privé (`vercel deploy --prod` dans `maquette/`, `vercel.json` noindex déjà prêt), puis la relire sur téléphone
- [ ] Rédiger le message d'accroche (site illisible sur mobile + Booking Form avec carte par email) avec le lien de la démo
- [ ] Demander à Jicky des photos haute définition (Leopard 45, Bali 54, Pardo 43 vignette 454 px ; Axopar 37 et Nautitech 47 remplacées le 2026-10-27 par des retouches Nano Banana)
- [x] Traduire en FR les pages client du design C (accueil, flotte, fiche, demande) — fait le 2026-10-25 (commit b30670f)
- [ ] Préparer le premier message (accroche mobile + Booking Form) et le canal (email info@ ou appel au +590 590 27 70 34)
- [ ] Trouver le nom du gérant (annuaire injoignable lors de l'audit)
- [ ] Poser les 12 questions de [[jicky-01-paiement-reservation]] au premier échange
- [ ] Vérifier avec le Crédit Agricole ou Jicky : plafond Up2pay, débit différé, enregistrement de carte, durée de validité du lien
- [x] Synthèse du benchmark des tunnels concurrents (lot C agences arrêté, jugé suffisant) : prospection-charter/docs/etudes/2026-10-27-jicky-marine-tunnels-concurrents.md
- [x] Ajouté à la maquette (366f883) : annulation des CGV dans le récap, délai « sous 2 h, 8 h-18 h » marqué Exemple, WhatsApp prérempli par bateau marqué Exemple ; délai réel et numéro WhatsApp à demander à Jicky
- [ ] Faire valider par Jicky les photos retravaillées par IA (Fairline 65, Axopar 37, Sanya 57, San Lorenzo 90, Lagoon 55, Nautitech 47), notamment l'inscription inventée sur le flybridge du Fairline
- [ ] Demander à Jicky : Fairline 63 ou 65 ? et pourquoi les demi-journées du San Lorenzo 90 sont « Saint-Barth » alors qu'il ne peut pas entrer dans la Réserve marine
- [x] Flotte à l'échelle : résultats des 3 agents récupérés (specs sourcées, photos 3/4 avant), planche montrée, rendu plâtre fait et intégré à l'accueil (2026-10-27)
- [ ] Flotte à l'échelle : faire confirmer par Jicky les identifications du 2026-10-28 — « Sunseeker 52 » = Camargue 50, « Sunseeker 60 » = Predator 56 2000-2004 ; reste « Lagoon 420 2026 » probablement Lagoon 42 et modèle exact du San Lorenzo 90
- [x] Flotte à l'échelle (reprise) : refaite le 2026-10-28 (acf918c) — photos internet caméra basse, parasites gommés, Sanya 57 plus long que le Lagoon 55, mâts entiers à la hauteur officielle ; angles : 7 bateaux encore trop de profil, voir ci-dessous
- [ ] Tunnel : mentionner la météo (art. 9 des CGV) avant l'envoi de la demande, et revoir `docs/decisions.md` qui dit les CGV sans articles météo ni mineurs (art. 9 et 13 existent)
- [ ] Porte qualité Jicky : corriger les autres échecs (mode concierge à 12 gestes avec nombre de personnes trop tard, focus invisible sur champs en erreur, fiche Fairline lente sur mobile 7,3 s, lien du bandeau prototype trop petit, Pardo 43 étiré 2,4×)
- [ ] Flotte à l'échelle : relancer le Fjord 53 dans Nano Banana (`research/nano-banana-30deg/PROMPTS.md`, section « Relance ») puis l'intégrer
- [ ] Flotte à l'échelle : faire confirmer par Jicky la hauteur réelle du mât du Sanya 57 (photo ≈ 28 m contre 22,25-23 m publiés, option « light air » ?) ; maquette calée sur la photo (28,4 m), décision Melvin du 2026-10-28

## Journal
- 2026-10-27 : Essai de relief 2.5D sur la photo proue du Pardo 43 (`maquette/relief.html`, 1313362) : carte de profondeur Depth Anything V2 calculée sur le processeur, shader WebGL, souris ou mouvement automatique, repli photo fixe. Gratuit, rien d'inventé. À valider par Melvin avant intégration au hero C. Pistes 3D gardées : flotte à l'échelle, demi-tour du Sanya 57 via Google Flow (2 photos réelles en début et fin).
- 2026-10-27 : Photos principales refaites via Nano Banana (Fairline 65, Axopar 37, Sanya 57, Lagoon 55, Nautitech 47, San Lorenzo 90 en route) et VanDutch 55 sur une photo existante 1240 px (c379ddb) ; 3e diapo hero Pardo 43 (3e6b647) ; Leopard 53 à 53 ft ; tarifs identiques regroupés sur une ligne (a6a97fc). IA limitée aux photos principales/hero, à faire valider par Jicky.
- 2026-10-27 : Barème d'annulation du récap reformulé au plus près des CGV (5cf5d2e) ; délai « sous 2 h » et WhatsApp prérempli gardés comme propositions « Exemple ».
- 2026-10-27 : 3 revues (Lighthouse, web-design-guidelines, états ouverts) puis 2 bloquants de chargement + 5 bugs corrigés (2c736ae) et cartes en 1200 px (0a5e5e1) : accueil iPhone 3,15 → 1,94 Mo, ~8,5 s en 4G lente ; a11y et bonnes pratiques à 100.
- 2026-10-27 : Flotte à l'échelle retenue sur l'accueil (avant les vignettes), défilement épinglé au scroll, rendu maquette blanche détaillé à partir des vraies photos de profil ; 13/18 bateaux ont un profil, 5 n'ont que des trois-quarts ; Blender écarté.
- 2026-10-27 : Flotte à l'échelle : rendu « plâtre blanc » essayé sur Pardo 43 et Sanya 57 (détourage BiRefNet gratuit + niveaux de gris modelés) ; détail conservé, rien d'inventé ; défauts : voiles du Sanya coupées, Pardo vu d'en haut, passagers visibles. Aperçu des 13 bateaux à profil sur l'accueil en cours.
- 2026-10-27 : Photos des cartes de l'accueil mises en attente derrière le hero (ff3a790, 33 tests) : affichage principal iPhone 4G lente ~6,9 → ~6,1 s en médiane ; Lighthouse simulé ne voit pas le gain.
- 2026-10-27 : Flotte à l'échelle révisée : 18 bateaux en trois-quarts avant, même sens, catamarans voiles affalées avec hauteur de mât réelle ; photos manquantes prises sur le web (même modèle, même année). Doute : « Lagoon 420 2026 » probablement un Lagoon 42.
- 2026-10-27 : Flotte à l'échelle intégrée à l'accueil avant les vignettes (dbe42dd puis corrections 20c3b54 et suivant) : 18 silhouettes plâtre 3/4 avant (photos Jicky + même modèle sur internet), mâts à la hauteur officielle (specs chantiers), section épinglée avec défilement horizontal au scroll. Revues animation et accessibilité faites et corrigées. Pipeline : research/depth/detourer-lot.mjs (BiRefNet), research/echelle.py, research/platre.py. À vérifier avec Jicky : Lagoon 420 = Lagoon 42, Sunseeker 60 = Predator 1re gén., modèle exact du Sunseeker 52.
- 2026-10-27 : Flotte à l'échelle jugée insuffisante par Melvin (angles incohérents, objets parasites, Sanya 57 plus petit que Lagoon 55, mâts coupés) : reprise lancée avec photos internet au bon angle, gréement redessiné et échelle des voiliers calée sur la tête de mât.
- 2026-10-28 : Flotte à l'échelle refaite (acf918c) : 18 photos internet en trois-quarts avant, caméra basse (sous-agents de recherche, cahier research/refs-internet/CAHIER-PHOTOS.md), gréement redessiné au-dessus de la bôme d'après des points relevés sur chaque photo, mâts entiers à la hauteur officielle, parasites et lettrage gommés. Sanya 57 désormais plus long que le Lagoon 55 (Lagoon calé sur sa coque de 16,56 m). Identifications : « Sunseeker 52 » = Camargue 50, « Sunseeker 60 » = Predator 56 2000-2004 — à confirmer avec Jicky. Leçon : les photos de drone gonflent la hauteur des bateaux (Leopard 53 : 8,7 m mesurés pour 5,7 m) : exiger une caméra basse.
- 2026-10-27 : Profils couleur des photos convertis en sRGB (9c8a98b, 36 fichiers, couleurs fidèles au site d'origine) ; message de la veille corrigé à 390 px (c994c7d) ; dossier d'envoi créé ([[jicky-02-dossier-envoi]] : vidéos 75 s, avant/après, page privée, brouillons J0-J+15, rien envoyé) ; porte qualité FAIL : météo absente du tunnel avant l'envoi alors que les CGV ont un article météo.
- 2026-10-28 : Angles relus : 7 bateaux encore trop de profil, refaits via Nano Banana à 30° (dossier research/nano-banana-30deg, intégration en cours) ; catamarans à voile réduits au mât, à l'étai avec génois enroulé et à la bôme. Fiche chiffres : performance, accessibilité, référencement dans une carte (75 → 82, 60 → 100, 82 → 100 ; maquette-outils a83025d).
- 2026-10-28 : 6/7 bateaux refaits via Nano Banana intégrés à 30° (d36f0d1), Sanya 57 depuis la photo de Melvin (c27279c), mâts revus (Lagoon 42 20,65 m, Nautitech 47 21,4 m), génois en tête de mât (4b2fc78), titre « Eighteen boats, one exclusive experience » (89862f7). Fiche chiffres : « 3 étapes pour demander une sortie » remplace « 3,5× plus légère », Performance 75 → 96 affichée comme objectif. Reste Fjord 53 ; mât du Sanya (photo ≈ 28 m / 23 m publiés) à trancher.
- 2026-10-28 : Textes de l'accueil animés (7fa3982, mouvement réduit respecté, coupé pour porte et vidéo), Axopar 37 restauré après un webp vide (dfb6442), « Sorties et tarifs » sous « À bord » et menu réordonné (4dad9bc, 99436f5), accroche « Choisissez votre bateau, on s'occupe du reste » + bouton à 30 % de transparence (9686871). Mât du Sanya 57 : suit la photo (28,4 m), décision Melvin.

## Liens
- Projet parent : [[prospect-charter]]
- Client : [[jicky-marine]]
- Patterns utilisés : [[stack-creation-site-web]]
- Repo / deployment : github.com/BlueImpakt/prospect-charter — site actuel : jickymarine.com
