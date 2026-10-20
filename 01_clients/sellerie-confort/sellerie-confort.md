---
tags: [client, discussion, p1, artisanat, commerce, france]
created: 2026-10-06
statut: discussion
priorite: p1
secteur: artisanat
localisation: france
body_synced: 2026-10-20
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
- Dev de la Phase 2 (17/10, repris dans le rapport le 20/10) : copie exacte de la prod sur l'hébergement, données clients comprises, neutralisée, encadrée par une clause RGPD de sous-traitance (art. 28) au contrat de Phase 2

## Besoins identifiés
- Ajouter une couleur ou une matière beaucoup plus simplement (regroupement par famille au lieu d'une photo par selle, par zone, par matière)
- Afficher les logos/broderies choisis directement sur la selle
- Listes de choix plus lisibles côté client final ; refonte visuelle éventuelle du site entier, par étapes

## Devis / propositions
- Devis I-26-10-1 (08/10) — Phase 1 audit technique : **1 400 € HT** (4 j × 350 €), TVA non applicable (art. 293 B CGI), acompte 50 % à la signature ; I-26-10-2 (acompte 50/50) présent à côté, référence à aligner dans le contrat ; I-26-08-1 (1 600 €) obsolète. **Signé le 14/10** (acompte 700 € versé)
- Contrat Phase 1 : réécrit le 13/10 (Word + PDF, 1 400 € HT), clause de plafonnement Phase 2 ajoutée le 13/10, **signé le 14/10**
- Phase 2 : à chiffrer à l'issue de la Phase 1 (fourchette annoncée 4 000 à 7 000 €, taux 350 €/j) ; **plafond contractuel 7 000 € HT**, 1 400 € de Phase 1 déduits, solde max 5 600 €
- **Chiffrage du 19/10** (Word + PDF `chiffrage-phases-1-2-3.docx` + variante fourchette) : Phase 2 = **17,5 j, 6 125 € HT à payer (Phase 1 déduite)** ; Phase 3 (refonte complète du site + automatisations) = **20 à 23 j, 7 000 à 8 050 € HT**
- **Rapport client Phase 1 (20/10, artefact claude.ai, non envoyé)** : Phase 2 présentée à **15 j (5 250 € HT)** + écran de gestion en option (2,5 j, 875 € HT) pour tenir le plafond, au lieu des 17,5 j d'un bloc du Word, à valider avant envoi

## Next actions
- [ ] Réunion du 2026-10-07 : voir les next actions de [[sellerie-confort-configurateur]] (toutes les actions du projet y vivent)

## Journal
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — Écran de gestion « Matières et couleurs » en 4 onglets d'après les trois jeux de choix standard (listes de 37, 44 et 26 choix) : Matières 37, Liserés 44, Surpiqûres 26, plus À vérifier 183 (nid d'abeille nommé autrement 52, petites pointes R6 44, variantes ou… Détails dans la fiche projet.
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — panier perdu diagnostiqué : Payline vide le panier avant la banque, Cofidis détache la session, panier invité 2 jours ; correctif préconisé (pas de vidage avant paiement, 30 jours).
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — fiches produit (configurable / non configurable) prototypées au design de la maquette, revue design multi-agents et 4 défauts bloquants corrigés.
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — fiche d'habillage A4 maquettée, courriel « En fabrication » retenu ; module de sauvegarde/envoi de configuration et relances testé sur la copie ; retour/caution à simplifier.
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — relances configuration/panier cadrées RGPD, caution non relancée pour Alma/Cofidis/carte virtuelle, configurateur tenant à l'écran avec logos 26 couleurs, reprise progressive de l'hébergement o2switch au nom de Valérie.
- 2026-10-17 : relance du configurateur finalisée sur la copie (bouton seulement dans le récapitulatif, proposition au départ, 2 rappels 24 h / 72 h, case « pas de rappel », bilan d'effet dans WooCommerce › Relances, 16/16 tests)
- 2026-10-17 : dev de la Phase 2 décidé : copie exacte de la prod en préprod WP Tiger (o2switch), RGPD cadrée au contrat (art. 28), neutralisation obligatoire à chaque copie ([[phase-1]] §23)
- 2026-10-17 : Sur [[sellerie-confort-configurateur]] — logos brodés branchés sur Duke et CBF, couleurs de broderie par familles, configurateur sans défilement ; import Z900 bloqué par l'arrêt de MySQL de Local.
- 2026-10-19 : Sur [[sellerie-confort-configurateur]] — taille des logos calculée sur la surface du calque (plafond dosseret 45 %), Z900 importée aux 26 fils.
- 2026-10-19 : Sur [[sellerie-confort-configurateur]] — chiffrage Phase 2 17,5 j (6 125 € HT, Phase 1 déduite) et Phase 3 20-23 j (7 000-8 050 € HT), Word + PDF prêts.
- 2026-10-19 : Sur [[sellerie-confort-configurateur]] — logos brodés : règle de taille complète (45 % de √surface, min 5 cm dosseret, 4-7 cm bandes) et orientations validées sauf l'aile Honda sur bandes ; bug du script d'import corrigé, Duke / CBF / Z900 réparées.
- 2026-10-20 : Sur [[sellerie-confort-configurateur]] — Chiffrage revu (Word `Phase 1/chiffrage-phases-1-2-3*.docx`) : Phase 2 17,5 j (6 125 € HT à payer, plafond de 16 j dépassé de 1,5 j avec l'écran de gestion), Phase 3 20 à 23 j (7 000 à 8 050 € HT). (+1 autre(s) entrée(s) le même jour, voir la fiche projet)
- 2026-10-20 : Sur [[sellerie-confort-configurateur]] — rapport Phase 1 version client rédigé (artefact, 9 annexes visuelles), Phase 2 présentée à 15 j + option écran de gestion ; dev Phase 2 sur copie avec données clients neutralisée (RGPD art. 28).
- 2026-10-20 : Sur [[sellerie-confort-configurateur]] — options de broderie incohérentes sur 296 fiches (18 groupes sur 46) à homogénéiser en Phase 2 ; copie fusionnée en 46 configurateurs ; aile Honda en miroir.
- 2026-10-20 : Sur [[sellerie-confort-configurateur]] — captures définitives des annexes du rapport client posées (matières, écran de gestion, logo 3D, étapes 1-3 sur Z900)

## Liens
- Projets : [[sellerie-confort-configurateur]]
- Réunions : [[2026-10-07-sellerie-confort]] (prépa)
- Réunions : [[2026-10-14-sellerie-confort-hebergement-acces]] (prépa : hébergement et accès)
- CR réunion : [[2026-10-07-sellerie-confort-cr-client]]
- CR réunion : [[2026-10-07-sellerie-confort-cr-interne]]

