---
tags: [jicky-marine, prospection]
created: 2026-10-25
projet: jicky-marine-refonte
---

# jicky-01-paiement-reservation

Projet : [[jicky-marine-refonte]] · Client : [[jicky-marine]] · Parent : [[prospect-charter]] · Source : repo `prospection-charter`, `docs/etudes/2026-10-25-jicky-marine-paiement.md`


Prospect n°1 du top 50 (jickymarine.com, Saint-Barthélemy). Objet : vérifier si « réservation et paiement en ligne » tient face à des prestations à plusieurs milliers d'euros, avant de le vendre.

## 1. Ce qui existe déjà (site + CGV)

- **Deux modes de réservation (CGV art. 3)**, tous deux hors site, rien n'est téléchargeable sur jickymarine.com :
  - **3.1 « Booking Form »** (bon de réservation officiel, envoyé par le bureau) : le client y écrit **son numéro de carte complet et signe**, puis le renvoie par email à reservation@jickymarine.com ; la prestation est « encaissée en totalité dès réception ». Donc une saisie manuelle de la carte, sans 3-D Secure : en cas de fraude ou de contestation, c'est Jicky qui paie, et des numéros de carte circulent par email (non conforme PCI-DSS). Point de douleur fort, à confirmer avec eux (comment ils saisissent ces cartes).
  - **3.2 Lien de paiement Up2pay** (Crédit Agricole), envoyé avec un « Récapitulatif de réservation » quand la demande arrive par email. Cartes : Visa, CB, Mastercard, American Express, Diners. **Le lien expire au bout de 90 minutes**, prix et disponibilité ne sont plus garantis ensuite.
- **Paiement intégral à la réservation** : la réservation n'est confirmée qu'à réception du paiement complet. Pas d'acompte.
- **Les CGV ne disent rien des plafonds.** C'est normal : le plafond par transaction est fixé par le contrat entre Jicky et sa banque, et chaque carte a son propre plafond chez la banque du client. Aucun des deux n'apparaît jamais dans des CGV.
- Virement accepté (réservation validée à réception des fonds) ; espèces à l'embarquement ; chèques refusés.
- Annulation : 95 € de frais + 5 % à plus de 7 jours, 50 % de 7 jours à 48 h, 100 % à moins de 48 h.
- Entité : SAS Jicky Marine, RCS Basse-Terre 453 983 850, BP 321 Gustavia.

Conséquence : **on ne peut pas leur vendre « le paiement en ligne »**, ils l'ont. Ce qui manque, c'est tout ce qui précède le paiement : voir les disponibilités, demander une date, recevoir le lien sans échange d'emails.

## 2. Gamme de prix (sortie à la journée, devise non affichée, € d'après les CGV)

| Palier | Exemples | Part de l'offre |
|---|---|---|
| < 3 000 € | Lagoon 420 (1 150–2 350), Nautitech 47 (1 100–2 350), sunsets (950–2 800), Leopard 45 demi-journée, Axopar 37, transferts Axopar | ~1/3 des tarifs |
| 3 000 – 8 000 € | Sunseeker 52/60/64, Fairline 65, Vandutch 55, Leopard 53, Fjord 53, Bali 54, Lagoon 55, Pardo 43 | la majorité |
| > 8 000 € | San Lorenzo 90 (9 000–18 920), Leopard 88 (9 900–11 900) | 2 bateaux |

## 3. Contraintes techniques

- **Stripe est exclu** : Saint-Barthélemy fait partie des territoires non supportés (Saint-Martin, Guadeloupe, Martinique le sont). Idem pour la plupart des moteurs de réservation « clé en main » qui reposent sur Stripe. → On garde **Up2pay**, déjà sous contrat : il existe un module WooCommerce officiel (hosted payment page + notification serveur), avec option de débit différé. Avis récents mitigés sur le module : à tester avant de s'engager.
- **Frais carte sur gros montants** (repère : grille publique Stripe, carte hors UE 3,15 % + 0,25 €) : 950 € → ~30 € ; 5 200 € → ~164 € ; 16 500 € → ~520 €. Les taux Up2pay et Amex de Jicky sont négociés, inconnus. Le surcoût existe déjà aujourd'hui (ils encaissent déjà par carte) : le site ne le crée pas.
- **Refus côté banque** sur gros montants : cartes françaises plafonnées (souvent quelques milliers d'euros sur 30 jours), cartes US premium sans plafond fixe mais filtrage anti-fraude sur une grosse transaction à l'étranger. C'est le vrai risque d'échec sur le palier > 8 000 €, pas le site.
- **Plafond du contrat VAD** : le contrat Up2pay a probablement un plafond par transaction / par mois fixé par la banque. Non trouvé publiquement → à demander.

### Quel outil si pas Stripe

- **Up2pay (Crédit Agricole), déjà sous contrat : à garder.** L'encaissement passe par le contrat VAD que Jicky a avec sa banque : rien à ouvrir, rien à faire valider, l'Amex et le virement fonctionnent déjà.
- **Si on change un jour** : rester sur une passerelle branchée sur un contrat VAD bancaire français (PayZen/Systempay de Lyra, Monetico, Mercanet…). C'est la banque de Jicky qui encaisse, donc pas d'exclusion territoriale propre à la passerelle.
- **À éviter** : les plateformes qui encaissent pour le compte du marchand. Stripe et WooPayments excluent Saint-Barthélemy noir sur blanc ; pour Mollie, PayPlug, SumUp et PayPal, pas de confirmation trouvée pour Saint-Barth → non fiable sans réponse écrite de leur part.
- Côté site : c'est le moteur de réservation qui doit savoir appeler Up2pay. Il existe un module WooCommerce officiel ; avec un outil sur mesure ou n8n, on passe par la page de paiement hébergée Up2pay.

## 4. Preuve marché : les mêmes bateaux se vendent déjà en ligne, payés d'avance

L'agence **Isle Blue** (isleblue.co) vend en ligne un « Sunseeker 60ft Predator » à Saint-Barth (mêmes itinéraires St Barth / St Martin / Anguilla, mêmes 95 € de frais d'annulation, mêmes dates de haute saison que Jicky — l'opérateur n'est pas nommé, mais c'est très probablement leur bateau) :
- 5 840,64 $ la journée St Barth (Jicky : 5 200 €), + 15 % taxe/service + 21 €/passager ;
- **paiement intégral à la réservation**, par carte, en ligne ; réservation 48 h à l'avance minimum ; disponibilité confirmée après coup.

→ La clientèle paie déjà 5 000–8 000 € d'avance en ligne, **mais chez l'intermédiaire**, qui prend sa marge. Le prix n'est pas le blocage ; la friction du site direct l'est.

## 5. Recommandation : paiement par paliers, pas de panier « payer maintenant » unique

1. **< 3 000 €** : réservation instantanée + paiement carte complet en ligne (Up2pay), à condition que le calendrier par bateau soit tenu à jour.
2. **3 000 – 8 000 €** : **demande de réservation en ligne** (bateau, date, formule, passagers, traiteur) → le bureau confirme la dispo en un clic → **lien Up2pay généré et envoyé automatiquement** (n8n), relances automatiques, confirmation et fiche de sortie à réception du paiement. C'est leur process actuel, sans les emails manuels ni le lien de 90 minutes qui expire.
3. **> 8 000 € (San Lorenzo 90, Leopard 88)** : sur devis. Le site qualifie la demande ; paiement par virement ou lien Amex géré par le bureau.

Option à proposer, pas à imposer : acompte (ex. 30–50 %) sur les paliers 2–3 pour réduire les refus carte — demande une modification des CGV (aujourd'hui paiement intégral).

Seuils (3 000 / 8 000 €) = hypothèses de départ, à caler sur les chiffres de Jicky.

## 5 bis. Virement et Booking Form

**Virement** : aucun plafond côté Jicky (le compte reçoit n'importe quel montant) et quasiment pas de contestation possible : c'est le paiement le plus sûr pour eux. Limites côté client : plafonds de virement de sa banque (souvent bas vers un nouveau bénéficiaire, relevables), virement international pour les clients US (frais d'environ 25-50 $, change, 1 à 5 jours). Trop lent pour une réservation à quelques jours de la sortie → réservé aux gros montants réservés tôt.

**Pourquoi un Booking Form avec la carte du client** (hypothèses, les CGV ne le disent pas) :
1. **Conciergeries / agences de villas** : à Saint-Barth, beaucoup de réservations passent par le concierge de l'hôtel ou de la villa, qui remplit le bon avec la carte et la signature du client. Le titulaire n'est pas là pour valider le 3-D Secure, donc le lien Up2pay ne marche pas.
2. **Moins de refus sur gros montants** : une carte saisie à la main ne passe pas par le 3-D Secure (pas de SMS bloqué à l'étranger, pas de lien expiré à 90 minutes).
3. **Extras après coup** (traiteur, heures en plus, jouets nautiques) : la carte permet de débiter plus tard.
4. **Habitude** : activité depuis 2004, le bon précède très probablement Up2pay ; c'est l'usage hôtelier (« credit card authorization form »).

**Ce que ça leur coûte** : sans 3-D Secure, la fraude et les contestations sont à leur charge ; un client US qui conteste (« paiement non autorisé ») gagne souvent, même avec une signature. Des numéros de carte en clair dans une boîte mail : non conforme PCI-DSS et RGPD, une fuite peut coûter le contrat VAD.

**Remplacement proposé** (on garde leurs trois cas, on supprime la carte par email) :
- client direct → lien Up2pay automatique, validité plus longue que 90 minutes si le contrat le permet ;
- concierge → lien envoyé directement au titulaire de la carte, ou agence facturée au mois et payée par virement ;
- extras → lien complémentaire après la sortie, ou carte enregistrée chez Up2pay plutôt que dans un email (option d'enregistrement de carte Up2pay non vérifiée).

C'est un meilleur angle commercial que « le paiement en ligne » : sécuriser l'encaissement qu'ils font déjà, sans changer de banque.

## 5 ter. S'ils veulent garder un vrai contact avant paiement

On automatise ce qui entoure la conversation, pas la conversation :
- **reste humain** : réponse au client (téléphone, WhatsApp, email), conseil bateau / itinéraire / traiteur, et la décision d'envoyer le lien de paiement — rien ne part sans un clic du bureau ;
- **retiré** : les questions répétées (formulaire de demande structuré en amont), la rédaction du récap et du lien Up2pay (un bouton), le renvoi du lien expiré, la confirmation de charter, la fiche de sortie équipage, le rappel J-1 et la demande d'avis J+1, le Booking Form avec carte par email.

Formulation : « On ne remplace pas votre bureau, on lui enlève la paperasse : vous gardez chaque échange, mais quand le client dit oui, récap, paiement et confirmation partent en un clic. »

Repli sans aucune automatisation : refonte seule (mobile, prix lisibles, FR, WhatsApp/appel visibles) ou mise en conformité du paiement (fin des cartes par email).

## 5 quater. Calendrier : pas nécessaire pour démarrer

Un calendrier en ligne n'est obligatoire que pour la réservation **instantanée**. Sur demande, le bureau vérifie la dispo dans l'outil qu'il utilise déjà. Même Isle Blue affiche « Availability to be confirmed ». On ne sait pas comment Jicky s'organise → on avance par phases :

| Phase | Client | Bureau | Calendrier |
|---|---|---|---|
| 1. Sur demande (tous montants) | formulaire bateau / date / formule / passagers / traiteur | vérifie dans son planning actuel, clique pour envoyer récap + lien Up2pay | aucun |
| 2. Indicatif | dates « probablement disponibles » / « complètes » | rien de plus | lecture seule de leur outil (Google Agenda, Excel, logiciel) |
| 3. Instantané (petits montants) | réserve et paie seul | gère les exceptions | planning fiable, à jour en temps réel |

Ne pas vendre l'instantané d'entrée : 18 bateaux vendus en direct, par les agences et par les conciergeries, un calendrier mal synchronisé produit des doubles réservations. Les paliers de prix (§5) s'appliquent dans chaque phase ; le palier 1 « réservation instantanée » n'est possible qu'en phase 3.

## 6. Ce que ça change pour la prospection

- L'offre n'est plus « paiement en ligne » mais **« réserver en direct aussi facilement que chez Isle Blue, sans la marge de l'agence »** : disponibilités, demande en 1 minute, lien de paiement automatique, WhatsApp/appel, version FR, site mobile.
- L'accroche actuelle reste juste sur le mobile et l'absence de téléphone ; « ne permet pas de réserver » est à nuancer (réservation par email + lien carte).

## 7. Questions à poser à Jicky

1. Part des réservations directes vs agences / conciergeries / villas (et commissions versées).
2. Taux de liens de paiement non payés ou refusés, surtout au-dessus de 5 000 €.
3. Plafond par transaction du contrat Up2pay ; contrat Amex séparé ou non ; taux.
4. Où vivent les disponibilités aujourd'hui (agenda, Excel, logiciel) et qui les met à jour.
5. Ouverts à un acompte, ou paiement intégral non négociable ?
6. Qui remplit les Booking Forms : les clients eux-mêmes ou les concierges ?
7. Comment saisissent-ils les cartes reçues (back-office Up2pay, terminal) ?
8. Ont-ils déjà eu des contestations ou des fraudes sur ces paiements ?
9. Où vit le planning des 18 bateaux (tableau, Excel, Google Agenda, logiciel de flotte) et qui le met à jour ?
10. Quand une agence (Isle Blue) ou un concierge réserve, comment l'apprennent-ils ?
11. Quels bateaux sont à eux, lesquels sont confiés par des propriétaires qui gardent leurs propres dates ?
12. Combien de demandes par jour en haute saison, et combien d'allers-retours avant paiement ?

## Sources

- jickymarine.com (accueil, tarifs) et jickymarine.com/conditions.htm (CGV), consultés le 25/10/2026
- [Stripe — territoires d'outre-mer supportés](https://support.stripe.com/questions/stripe-availability-for-outlying-territories-of-supported-countries)
- [Stripe — tarifs France](https://stripe.com/fr/pricing)
- [Up2pay e-Transactions — module WooCommerce](https://wordpress.org/plugins/e-transactions-wc) ; [Crédit Agricole — Up2pay e-Transactions](https://www.credit-agricole.fr/professionnel/compte/e-commerce/Up2pay_e-Transactions.only-content.html)
- [WooPayments — pays supportés](https://woocommerce.com/document/woopayments/compatibility/countries/)
- [Isle Blue — Sunseeker 60ft Predator, St Barts](https://isleblue.co/st-barts/experiences/st-barts-boat-charter-sunseeker-60ft-predator)
