---
tags: [client, discussion, p1, artisanat, commerce, france]
created: 2026-10-06
statut: discussion
priorite: p1
secteur: artisanat
localisation: france
body_synced: 2026-10-15
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
- 2026-10-07 : Sur [[sellerie-confort-configurateur]] — Refonte complète des 6 maquettes (`sellerieconfort-refonte/Maquette/`) : accueil, liste des selles (BMW), fiche produit, matières, configurateur, panier. Détails dans la fiche projet.
- 2026-10-08 : Sur [[sellerie-confort-configurateur]] — Analyse du catalogue complet (345 fiches configurables) : 337 sur la même logique (3 jeux réutilisables : 37 matières, 44 liserés, 26 surpiqures), 8 fiches atypiques (dont CFMOTO 800 NK) ; ≈ 2 254 couches, ≈ 83 000 images. (+1 autre(s) entrée(s) le même jour, voir la fiche projet)
- 2026-10-13 : Sur [[sellerie-confort-configurateur]] — Après la réunion du 07/10, Valérie OK pour la Phase 1. (+1 autre(s) entrée(s) le même jour, voir la fiche projet)
- 2026-10-13 : Sur [[sellerie-confort-configurateur]] — clause de plafonnement Phase 2 ajoutée au contrat (7 000 € HT max, 1 400 € de Phase 1 déduits, solde max 5 600 €)
- 2026-10-14 : Sur [[sellerie-confort-configurateur]] — Phase 1 lancée : contrat/devis signés, acompte 700 € versé, accès WordPress OK ; délai de 10 jours en cours.
- 2026-10-14 : Sur [[sellerie-confort-configurateur]] — reconnaissance Phase 1 bouclée, accord écrit d'export reçu, site local reconstruit (345 produits), alerte plugin compromis hors périmètre, nid d'abeille Z900 en cours
- 2026-10-14 : Sur [[sellerie-confort-configurateur]] — site local reconstruit comme la prod (front Divi, 345 produits), nid d'abeille Z900 validé sur sa propre photo mais transfert vers le configurateur non résolu
- 2026-10-14 : Sur [[sellerie-confort-configurateur]] — images de nid d'abeille rangées par modèle ; second jeu complet (BMW F900 XR) repéré pour tester la généralisation
- 2026-10-14 (fin de soirée) : Sur [[sellerie-confort-configurateur]] — clone local complété (catégories, URL de la prod, sélecteur « Ma Moto », options de commande reconstruites sur 345 fiches) ; constat de fiches dupliquées avec les visuels d'un autre modèle à signaler.
- 2026-10-15 : Sur [[sellerie-confort-configurateur]] — plan Phase 1 formalisé ([[phase-1]]), voie 1.7.6 + plugin envisagée, nid d'abeille testé sur 5 modèles, plus de mails à Valérie.
- 2026-10-15 (suite) : Sur [[sellerie-confort-configurateur]] — poste 3 : rendu matières reproductible à l'identique via texture maître reconstituée (version récente par défaut) ; poste 1 : 336 fiches sur 345 regroupables sur la 1.7.6.
- 2026-10-15 (nuit) : Sur [[sellerie-confort-configurateur]] — nid d'abeille testé sur 6 selles avec délimitations calées sur les calques, copie du site local avec regroupement famille/lot, 2.0.0 en test sur la copie ; règle : images d'origine conservées pour les modèles existants.
- 2026-10-15 : Sur [[sellerie-confort-configurateur]] — 2.0.0 testée sur une copie (commandes passées protégées, 55 configurateurs globaux, écran de gestion « Matières et couleurs » en admin de la copie, 19 tests sur 19).
- 2026-10-15 (nuit, suite) : Sur [[sellerie-confort-configurateur]] — nid d'abeille : K120 confirmé par défaut (test Ducati Diavel), orientation horizontale en cours d'affinage, 2e forme à recopier ; tests de logos brodés lancés.
- 2026-10-16 : Sur [[sellerie-confort-configurateur]] — nouvelle matière : grande photo haute résolution (texture maître) préférée au petit carré répété ; échelle auto à prévoir en Phase 2.

## Liens
- Projets : [[sellerie-confort-configurateur]]
- Réunions : [[2026-10-07-sellerie-confort]] (prépa)
- Réunions : [[2026-10-14-sellerie-confort-hebergement-acces]] (prépa : hébergement et accès)
- CR réunion : [[2026-10-07-sellerie-confort-cr-client]]
- CR réunion : [[2026-10-07-sellerie-confort-cr-interne]]

