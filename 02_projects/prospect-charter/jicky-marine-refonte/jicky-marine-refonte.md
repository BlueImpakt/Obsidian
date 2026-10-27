---
tags: [project, encours, jicky-marine]
created: 2026-10-25
statut: encours
client: jicky-marine
parent: prospect-charter
body_synced: 2026-10-27
---

# jicky-marine-refonte

## Objectifs du projet
- Proposer à Jicky Marine (Saint-Barthélemy, 18 bateaux, depuis 2004) une refonte de jickymarine.com et une réservation sur demande qui remplace le Booking Form et les emails manuels, sans leur retirer le contact client.

## Livrables
- [[jicky-01-paiement-reservation]] — paiement, Booking Form, contact humain, calendrier, questions à poser — **à lire en premier**
- Étude source dans le repo : `docs/etudes/2026-10-25-jicky-marine-paiement.md`
- **Maquette cliquable** (piste B ; design C retenu, grille régulière nourrie de sites de brokers, EN/FR) : `C:\Users\LENOVO\Documents\GitHub\jicky-marine-refonte\maquette\` (branche `maquette`, local, pas de remote). 6 écrans : accueil (hero diaporama, note Tripadvisor), flotte filtrable, fiches des 18 bateaux avec vrais prix, demande en 3 étapes sans calendrier, vue bureau (relecture du message, montant, relances au choix, alerte même bateau même date), écran concept en FR. EN officiel + FR. Variantes A (taste) et D (Müller-Brockmann) gardées pour comparaison.
- Docs du repo maquette : spec `docs/superpowers/specs/2026-10-25-maquette-design.md`, `docs/hypotheses.md` (ce qui n'est pas un fait), `docs/photos.md`, revues `docs/revues/` (finish-gate, personas, accessibilité, textes).

## État actuel
- 2026-10-25 : étude paiement / réservation faite ; fiche prospect corrigée dans les CSV (commentaire, défaut, accroche). Aucun contact pour l'instant.
- 2026-10-27 : maquette cliquable design C en local (branche `maquette`, 33 tests verts), non déployée : photos principales refaites, perf mobile corrigée (accueil iPhone 1,94 Mo), tarifs regroupés ; flotte à l'échelle en cours d'essai. Restent `PITCH_CONTACT`, le déploiement privé et le message d'accroche. Toujours aucun contact avec Jicky.

## Décisions techniques
- **Garder Up2pay** (Crédit Agricole, déjà sous contrat) pour toutes les cartes ; virement pour les gros montants. Stripe exclu (Saint-Barth non supporté).
- **Phase 1 sans calendrier** : demande structurée en ligne → le bureau vérifie dans son planning actuel → un clic envoie récap + lien Up2pay. Calendrier indicatif puis réservation instantanée seulement quand on connaît leur organisation.
- Paliers de prix : < 3 000 € (instantané possible en phase 3), 3 000-8 000 € (demande + lien automatique), > 8 000 € (devis, virement ou Amex). Seuils à caler avec eux.
- Argument : « on enlève la paperasse, pas le contact » ; repli possible sur la refonte seule ou la mise en conformité du paiement.
- **Photos retouchées par IA (Nano Banana)** limitées aux photos principales et au hero, vérifiées une par une et à faire valider par Jicky ; galerie laissée en photos d'origine. « Principale » = vignette de la flotte + 1re photo de la fiche.
- **Flotte à l'échelle** : 18 bateaux en trois-quarts avant, tous dans le même sens, catamarans voiles affalées avec hauteur de mât réelle ; photos manquantes prises sur le web (même modèle, même année) ; rendu « plâtre blanc ».

## Blocages / risques
- Plafond par transaction du contrat Up2pay inconnu (pas dans les CGV, à demander).
- Organisation interne inconnue (planning des 18 bateaux, bateaux confiés par des propriétaires, ventes via agences et concierges) : risque de doubles réservations si on vend un calendrier instantané trop tôt.
- Module Up2pay WooCommerce avec des avis récents mitigés : à tester avant de s'engager.
- Délai de réponse « sous 2 h » et WhatsApp affichés dans la maquette sont des propositions (badge Exemple) : Jicky n'affiche ni délai ni numéro WhatsApp.

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
- [ ] Flotte à l'échelle : récupérer les résultats des 3 agents (caractéristiques sourcées des 18 bateaux, photos trois-quarts avant catamarans voiles affalées et yachts), montrer la planche d'une photo par bateau orientée dans le même sens, puis passer au rendu « plâtre blanc »
- [ ] Flotte à l'échelle : lever les doutes de modèle — « Lagoon 420 2026 » probablement Lagoon 42, photos « Sunseeker 60 » nommées `predator-56`, modèle exact du San Lorenzo 90 et du Sunseeker 52

## Journal
- 2026-10-25 : Maquette cliquable livrée (6 écrans, EN/FR, branche `maquette`) après quatre revues ; restent PITCH_CONTACT et le déploiement privé.
- 2026-10-25 : Étude paiement livrée : paiement carte déjà en place (Up2pay + Booking Form), Stripe impossible à Saint-Barth ; offre recentrée sur une réservation sur demande par paliers, phase 1 sans calendrier.
- 2026-10-25 : Photos de cartes choisies par Melvin figées dans le pipeline, fiches gardent leur photo d'origine (e9205ac, 5100067) ; grandes photos en webp qualité 95, surcoût hero ~1,2 Mo accepté (3f6ee70).
- 2026-10-27 : Galerie corrigée : photos entières sans défilement à toutes largeurs, grands formats harmonisés, agrandissement plafonné à 1,5× (279b442, 31 tests).
- 2026-10-27 : Benchmark des tunnels concurrents St-Barth : seul St Barth Yachting a un tunnel complet (dispo réelles, Stripe donc société hors île) ; MasterSki et les grosses flottes restent sur « écrivez-nous » ; St Barth Excursions encaisse via Systempay (contrat bancaire, comme Up2pay) ; les places de marché passent toutes par demande/devis. Confirme le parcours sur demande de la maquette.
- 2026-10-27 : Synthèse écrite (22 sites) : la maquette est dans la norme (demande puis lien), lui manquent l'annulation près du bouton, un délai de réponse chiffré et WhatsApp prérempli ; à noter, le barème d'annulation de St Barth Yachting est identique aux CGV Jicky (à vérifier).
- 2026-10-27 : Tunnel C complété (366f883, 31 tests) : barème d'annulation des CGV dans le récap avec lien, délai de réponse chiffré (Exemple), WhatsApp prérempli sur la fiche (Exemple). Synthèse benchmark commitée dans prospection-charter (1cbc122).
- 2026-10-27 : Essai de relief 2.5D sur la photo proue du Pardo 43 (`maquette/relief.html`, 1313362) : carte de profondeur Depth Anything V2 calculée sur le processeur, shader WebGL, souris ou mouvement automatique, repli photo fixe. Gratuit, rien d'inventé. À valider par Melvin avant intégration au hero C. Pistes 3D gardées : flotte à l'échelle, demi-tour du Sanya 57 via Google Flow (2 photos réelles en début et fin).
- 2026-10-27 : Photos principales refaites via Nano Banana (Fairline 65, Axopar 37, Sanya 57, Lagoon 55, Nautitech 47, San Lorenzo 90 en route) et VanDutch 55 sur une photo existante 1240 px (c379ddb) ; 3e diapo hero Pardo 43 (3e6b647) ; Leopard 53 à 53 ft ; tarifs identiques regroupés sur une ligne (a6a97fc). IA limitée aux photos principales/hero, à faire valider par Jicky.
- 2026-10-27 : Barème d'annulation du récap reformulé au plus près des CGV (5cf5d2e) ; délai « sous 2 h » et WhatsApp prérempli gardés comme propositions « Exemple ».
- 2026-10-27 : 3 revues (Lighthouse, web-design-guidelines, états ouverts) puis 2 bloquants de chargement + 5 bugs corrigés (2c736ae) et cartes en 1200 px (0a5e5e1) : accueil iPhone 3,15 → 1,94 Mo, ~8,5 s en 4G lente ; a11y et bonnes pratiques à 100.
- 2026-10-27 : Flotte à l'échelle retenue sur l'accueil (avant les vignettes), défilement épinglé au scroll, rendu maquette blanche détaillé à partir des vraies photos de profil ; 13/18 bateaux ont un profil, 5 n'ont que des trois-quarts ; Blender écarté.
- 2026-10-27 : Flotte à l'échelle : rendu « plâtre blanc » essayé sur Pardo 43 et Sanya 57 (détourage BiRefNet gratuit + niveaux de gris modelés) ; détail conservé, rien d'inventé ; défauts : voiles du Sanya coupées, Pardo vu d'en haut, passagers visibles. Aperçu des 13 bateaux à profil sur l'accueil en cours.
- 2026-10-27 : Photos des cartes de l'accueil mises en attente derrière le hero (ff3a790, 33 tests) : affichage principal iPhone 4G lente ~6,9 → ~6,1 s en médiane ; Lighthouse simulé ne voit pas le gain.
- 2026-10-27 : Flotte à l'échelle révisée : 18 bateaux en trois-quarts avant, même sens, catamarans voiles affalées avec hauteur de mât réelle ; photos manquantes prises sur le web (même modèle, même année). Doute : « Lagoon 420 2026 » probablement un Lagoon 42.

## Liens
- Projet parent : [[prospect-charter]]
- Client : [[jicky-marine]]
- Patterns utilisés : [[stack-creation-site-web]]
- Repo / deployment : github.com/BlueImpakt/prospect-charter — site actuel : jickymarine.com
