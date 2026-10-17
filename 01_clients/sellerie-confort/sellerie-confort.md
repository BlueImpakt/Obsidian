---
tags: [client, discussion, p1, artisanat, commerce, france]
created: 2026-10-06
statut: discussion
priorite: p1
secteur: artisanat
localisation: france
body_synced: 2026-10-17
---

# sellerie-confort

## Relationnel
- **Société** : Sellerie Confort S.A.R.L. (RCS Le Mans), Cérans-Foulletourte (72). Fabrication artisanale française de selles de moto sur-mesure, vendues sur sellerieconfort.com (~1 520 fiches produits, 27 marques)
- **Contact** : Valérie Cenizo, co-gérante. Gère elle-même le contenu et dispose des accès WordPress : c'est elle l'utilisatrice réelle du back-office, pas un développeur
- **Prestataires en place** : VIMAWEB (webmaster, maintenance, aide technique ponctuelle) et ARTEO Conseil (créateur du site d'après les mentions légales). Ils restent. Consigne : limiter les contacts avec eux, rester sur le design sans toucher à leurs outils
- **Secteur hors cible principale** (artisanat/e-commerce, pas environnement/impact) : à garder en tête pour le positionnement

## Historique des échanges
- Début août 2026 : maquettes envoyées par Blue Impakt
- 2026-08-07 : retour client positif (« on aime beaucoup sauf la couleur beige »), demande de simplifier l'ajout de couleurs/matières et d'afficher les logos choisis sur la selle, et demande de prix. Réponse de Blue Impakt le jour même (3 points à préciser, proposition de point rapide)
- Ensuite : la cliente précise le fonctionnement manuel actuel (patch physique, photo, ajout à la main sur chaque fiche) puis Blue Impakt envoie la proposition en 3 étapes + broderies, avec Phase 1 d'audit (devis + projet de contrat)
- 2026-10-07 : réunion d'environ 2 h avec Valérie — besoin confirmé, maquettes très appréciées, rien signé (accord de son mari attendu), nouvelle offre orale Phase 1 à 1 400 € HT ; une agence web les rencontre début novembre. CR : [[2026-10-07-sellerie-confort-cr-interne]] · [[2026-10-07-sellerie-confort-cr-client]]
- 2026-10-08 : maquettes mises en ligne sur Netlify pour l'envoi (Outlook perd les `assets/` des pièces jointes)
- 2026-10-13 : contrat Phase 1 réécrit (1 400 € HT, acompte 50 %), CR client envoyé avec un placeholder de créneaux à compléter ; Valérie en congés à partir du 17/10 ; Valérie OK pour la Phase 1 ; clause de plafonnement Phase 2 ajoutée (7 000 € HT max)
- 2026-10-14 : Phase 1 lancée — contrat et devis signés, acompte 700 € versé, accès WordPress OK ; délai de 10 jours en cours
- 2026-10-14 : accord écrit d'export reçu de la cliente (reconstruction du site en local)

## Décisions prises
- Phase 1 = audit technique avant chiffrage ferme de la Phase 2, **1 400 € HT** (4 j × 350 €) déduits de la Phase 2 si suite ; elle inclut, sans supplément, l'audit des automatisations, le suivi du parcours et le panier perdu
- Le seul engagement pris : **tester l'IA** (patchs matières et broderies) avant de s'engager. Étape 1 optionnelle, les photos existantes sont conservées
- Aucun accès à la prod : clone local, aucun accès direct à la base, aucune donnée clients/commandes/paiements consultée
- WordPress conservé pour la refonte (moins cher et moins risqué que du from scratch) — à confirmer par l'audit
- Images d'origine conservées pour les modèles existants ; pour une nouvelle matière, grande photo haute résolution (texture maître) préférée au petit carré répété, échelle auto à prévoir en Phase 2

## Besoins identifiés
- Ajouter une couleur ou une matière beaucoup plus simplement (regroupement par famille au lieu d'une photo par selle, par zone, par matière)
- Afficher les logos/broderies choisis directement sur la selle
- Listes de choix plus lisibles côté client final ; refonte visuelle éventuelle du site entier, par étapes

## Devis / propositions
- Devis I-26-10-1 (08/10) — Phase 1 audit technique : **1 400 € HT** (4 j × 350 €), TVA non applicable (art. 293 B CGI), acompte 50 % à la signature ; I-26-10-2 (acompte 50/50) présent à côté, référence à aligner dans le contrat ; I-26-08-1 (1 600 €) obsolète. **Signé le 14/10** (acompte 700 € versé)
- Contrat Phase 1 : réécrit le 13/10 (Word + PDF, 1 400 € HT), clause de plafonnement Phase 2 ajoutée le 13/10, **signé le 14/10**
- Phase 2 : à chiffrer à l'issue de la Phase 1 (fourchette annoncée 4 000 à 7 000 €, taux 350 €/j) ; **plafond contractuel 7 000 € HT**, 1 400 € de Phase 1 déduits, solde max 5 600 €

## Next actions
- [ ] Réunion du 2026-10-07 : voir les next actions de [[sellerie-confort-configurateur]] (toutes les actions du projet y vivent)

## Journal
- 2026-10-15 (nuit, suite) : Sur [[sellerie-confort-configurateur]] — nid d'abeille : K120 confirmé par défaut (test Ducati Diavel), orientation horizontale en cours d'affinage, 2e forme à recopier ; tests de logos brodés lancés.
- 2026-10-16 : Sur [[sellerie-confort-configurateur]] — nouvelle matière : grande photo haute résolution (texture maître) préférée au petit carré répété ; échelle auto à prévoir en Phase 2.
- 2026-10-16 : Sur [[sellerie-confort-configurateur]] — logos brodés en pose 3D (MoGe-2) validée sur MT-09, nid d'abeille forme A alignée sur l'axe de la selle et forme B validée.
- 2026-10-16 : Sur [[sellerie-confort-configurateur]] — logos brodés : orientation B validée et série finale propre ; configurateur gratuit sans licence, Divi utilisable sans licence ; habillage du plugin commencé en local.
- 2026-10-16 (appel Valérie) : Sur [[sellerie-confort-configurateur]] — appel : images d'origine = vignettes répétées, VIMAWEB colore par code (60 €/selle), nid d'abeille facultatif par réglage de couche ; détourage auto des calques : SAM 0,39, modèle entraîné 0,51 IoU, Kaggle/Mask2Former à tester.
- 2026-10-16 : Sur [[sellerie-confort-configurateur]] — détourage automatique des calques : Mask2Former IoU 0,72, SegFormer 0,64, insuffisant en production, piste semi-automatique ; logos brodés testés dans le configurateur local (2 options, import de logo client OK).
- 2026-10-16 : Sur [[sellerie-confort-configurateur]] — segmentation Mask2Former v2 IoU 0,64 (pas mieux que 0,72), SAM 3 à tester ; logos brodés ajustés (56 %, horizontal sur bande, « Sans logo ») ; estimation postes 5-6 ≈ 1,5 j.
- 2026-10-16 : Sur [[sellerie-confort-configurateur]] — SAM 3 testé (0,44, zones compactes 0,8-0,94) : conclusion qu'aucun modèle testé ne remplace le détourage de Valérie ; parcours sans fiche récap (panier direct) ; mise en prod dev → préprod → prod cadrée (§23) ; écran Matières 37 / Liserés 44 / Surpiqûres 26 propre.
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — Écran de gestion « Matières et couleurs » en 4 onglets d'après les trois jeux de choix standard (listes de 37, 44 et 26 choix) : Matières 37, Liserés 44, Surpiqûres 26, plus À vérifier 183 (nid d'abeille nommé autrement 52, petites pointes R6 44, variantes ou… Détails dans la fiche projet.
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — panier perdu diagnostiqué : Payline vide le panier avant la banque, Cofidis détache la session, panier invité 2 jours ; correctif préconisé (pas de vidage avant paiement, 30 jours).
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — fiches produit (configurable / non configurable) prototypées au design de la maquette, revue design multi-agents et 4 défauts bloquants corrigés.
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — fiche d'habillage A4 maquettée, courriel « En fabrication » retenu ; module de sauvegarde/envoi de configuration et relances testé sur la copie ; retour/caution à simplifier.
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — relances configuration/panier cadrées RGPD, caution non relancée pour Alma/Cofidis/carte virtuelle, configurateur tenant à l'écran avec logos 26 couleurs, reprise progressive de l'hébergement o2switch au nom de Valérie.
- 2026-10-17 : relance du configurateur finalisée sur la copie (bouton seulement dans le récapitulatif, proposition au départ, 2 rappels 24 h / 72 h, case « pas de rappel », bilan d'effet dans WooCommerce › Relances, 16/16 tests)
- 2026-10-17 : dev de la Phase 2 décidé : copie exacte de la prod en préprod WP Tiger (o2switch), RGPD cadrée au contrat (art. 28), neutralisation obligatoire à chaque copie ([[phase-1]] §23)

## Liens
- Projets : [[sellerie-confort-configurateur]]
- Réunions : [[2026-10-07-sellerie-confort]] (prépa)
- Réunions : [[2026-10-14-sellerie-confort-hebergement-acces]] (prépa : hébergement et accès)
- CR réunion : [[2026-10-07-sellerie-confort-cr-client]]
- CR réunion : [[2026-10-07-sellerie-confort-cr-interne]]

