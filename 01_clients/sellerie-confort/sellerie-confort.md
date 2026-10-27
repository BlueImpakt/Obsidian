---
tags: [client, discussion, p1, artisanat, commerce, france]
created: 2026-10-06
statut: discussion
priorite: p1
secteur: artisanat
localisation: france
body_synced: 2026-10-27
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
- 2026-10-21/22 : vidéo promo Instagram (Remotion, rushes IA) : v1 29 s, variantes dézoom et « loupes matières » (33,4 s), version « infos » ; version client « Maquette » prête le 22/10, rien envoyé à la cliente — à envoyer en relance de l'audit le 28-29/10. Détail : [[sellerie-confort-configurateur]]
- 2026-10-27 : audit SEO de sellerieconfort.com livré — bases saines ; freins : fiches en double, codes internes dans les titres, LCP mobile ~19,6 s, page Divi de sauvegarde indexée

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
- **Chiffrage du 19/10, revu le 20/10** (Word + PDF `chiffrage-phases-1-2-3.docx` + variante fourchette, repris dans le rapport client) : Phase 2 = **17,5 j écran de gestion compris + 200 € HT d'outils = 6 325 € HT, 4 925 € HT à payer (Phase 1 déduite)**, sous le plafond de 7 000 € HT, paiement 50 % à la commande / 50 % à la mise en production ; Phase 3 (refonte complète du site + automatisations) = **20 à 28,5 j, 7 000 à 9 975 € HT**
- **Rapport client Phase 1 (20/10, artefact claude.ai + PDF v2, non envoyé)** : chiffrage aligné sur le Word (17,5 j d'un bloc, l'option 15 j + écran de gestion abandonnée), détail par lot conservé, relu et corrigé ; incohérences restantes à trancher, mail de synthèse prêt

## Next actions
- [ ] Réunion du 2026-10-07 : voir les next actions de [[sellerie-confort-configurateur]] (toutes les actions du projet y vivent)

## Journal
- 2026-10-20 : Sur [[sellerie-confort-configurateur]] — accès au dev et propriété du code documentés, état des lieux statistique livré (GA4 pages vues seulement, cookies posés malgré refus = non conforme CNIL), méthode Phase 2 copie locale sans données → dev → préprod → prod, rapport exporté en PDF v2.
- 2026-10-20 : Sur [[sellerie-confort-configurateur]] — rapport client aligné sur le Word : Phase 2 6 325 € HT (4 925 € à payer, 50/50 commande / mise en prod), Phase 3 7 000 à 9 975 € HT ; relecture complète, accord de neutralisation du dev demandé à Valérie.
- 2026-10-20 : Sur [[sellerie-confort-configurateur]] — champs année/taille/poids du configurateur passés en listes déroulantes (copie 8090, tests au vert)
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — groupes de configuration identifiés : Africa Twin 1100 = 1000 ; Transalp 600 dans un groupe de 41 fiches
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — vidéo promo Remotion pour Instagram en brainstorming (V1 100 % graphisme, scénario Africa Twin → configurateur → motarde), 3 pistes visuelles maquettées
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — vidéo promo Instagram : rushes IA validés (Google Flow), tâches 1 à 8 du montage Remotion validées, assemblage final en cours
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — vidéo promo : film complet de 30 s assemblé avec son, derniers défauts de rendu en correction
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — vidéo promo Reel 30 s v1 livrée et relue ; retours de Melvin en cours d'intégration.
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — vidéo promo v1 29 s livrée avec les retours de Melvin, variante « dézoom » de fin lancée sur copie.
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — vidéo promo : variante dézoom2 rendue (gros plan selle, motarde qui entre au recul).
- 2026-10-21 : Sur [[sellerie-confort-configurateur]] — vidéo promo v2 « loupes matières » rendue (33,4 s), à valider par Melvin.
- 2026-10-22 : Sur [[sellerie-confort-configurateur]] — vidéo promo : version « infos » (assise antidérapante, infographies dosseret) en rendu, modifs précédentes commitées.
- 2026-10-22 : Sur [[sellerie-confort-configurateur]] — bandeau central (aile Honda, ECG, yeux) branché sur l'Africa Twin ; vidéo promo mise à jour
- 2026-10-22 : Sur [[sellerie-confort-configurateur]] — vidéo promo version client « Maquette » prête ; à envoyer en relance de l'audit le 28-29/10
- 2026-10-27 : Sur [[sellerie-confort-configurateur]] — audit SEO de sellerieconfort.com livré : bases saines, freins = fiches en double, codes internes dans les titres, LCP mobile ~19,6 s, page Divi de sauvegarde indexée.

## Liens
- Projets : [[sellerie-confort-configurateur]]
- Réunions : [[2026-10-07-sellerie-confort]] (prépa)
- Réunions : [[2026-10-14-sellerie-confort-hebergement-acces]] (prépa : hébergement et accès)
- CR réunion : [[2026-10-07-sellerie-confort-cr-client]]
- CR réunion : [[2026-10-07-sellerie-confort-cr-interne]]

