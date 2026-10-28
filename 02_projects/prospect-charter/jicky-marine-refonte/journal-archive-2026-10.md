# Archive Journal — jicky-marine-refonte

Entrées archivées automatiquement (seuil `## Journal` > 15, voir CLAUDE.md). Historique complet, ordre chronologique.

---

- 2026-10-25 : Note Tripadvisor réelle sur l'accueil, message d'avant-sortie dans la vue bureau (835d1dd). Photo principale = vignette de l'accueil du site d'origine, cartes pleines, une seule forme de fiche (mosaïque) (9ed5be5). VanDutch 55, Pardo 43, Nautitech 47 : photo principale en 450-530 px seulement, à demander en HD à Jicky.
- 2026-10-25 : Avis publics relevés (docs/avis-clients.md) : Tripadvisor 4,6/5 (75 avis, dernier nov. 2025), Google 4,1/5 (22). L'avis de nov. 2025 se plaint des instructions d'arrivée incomplètes et d'un bureau qui ne répond qu'après relance du concierge : argument direct pour le message d'avant-sortie automatique et le suivi.
- 2026-10-25 : 3e tour de revues sur le design C (accessibilité, personas, textes EN/FR, animations, code, Finish-Gate), corrigé (commit 39f95e3) ; bouton EN/FR dans l'en-tête. Questions à poser à Jicky : avis clients réels, montant des taxes/frais passagers, règle météo/annulation, conditions concierges, numéro WhatsApp.
- 2026-10-25 : Design C (direction frontend-design nourrie par 9 sites de brokers) retenu comme maquette principale ; toutes les photos du site, couverture = photo principale d'origine ; hero diaporama ; revue Finish-Gate + impeccable puis contre-revue, corrections faites (commit f206271, détail dans docs/revues/revue-c.md). Pages client passées en EN/FR (b30670f). Restent : PITCH_CONTACT, déploiement privé.
- 2026-10-25 : Maquette cliquable livrée (6 écrans, EN/FR, branche `maquette`) après quatre revues ; restent PITCH_CONTACT et le déploiement privé.
- 2026-10-25 : Étude paiement livrée : paiement carte déjà en place (Up2pay + Booking Form), Stripe impossible à Saint-Barth ; offre recentrée sur une réservation sur demande par paliers, phase 1 sans calendrier.
- 2026-10-25 : Photos de cartes choisies par Melvin figées dans le pipeline, fiches gardent leur photo d'origine (e9205ac, 5100067) ; grandes photos en webp qualité 95, surcoût hero ~1,2 Mo accepté (3f6ee70).
- 2026-10-27 : Galerie corrigée : photos entières sans défilement à toutes largeurs, grands formats harmonisés, agrandissement plafonné à 1,5× (279b442, 31 tests).
- 2026-10-27 : Benchmark des tunnels concurrents St-Barth : seul St Barth Yachting a un tunnel complet (dispo réelles, Stripe donc société hors île) ; MasterSki et les grosses flottes restent sur « écrivez-nous » ; St Barth Excursions encaisse via Systempay (contrat bancaire, comme Up2pay) ; les places de marché passent toutes par demande/devis. Confirme le parcours sur demande de la maquette.
- 2026-10-27 : Synthèse écrite (22 sites) : la maquette est dans la norme (demande puis lien), lui manquent l'annulation près du bouton, un délai de réponse chiffré et WhatsApp prérempli ; à noter, le barème d'annulation de St Barth Yachting est identique aux CGV Jicky (à vérifier).
- 2026-10-27 : Tunnel C complété (366f883, 31 tests) : barème d'annulation des CGV dans le récap avec lien, délai de réponse chiffré (Exemple), WhatsApp prérempli sur la fiche (Exemple). Synthèse benchmark commitée dans prospection-charter (1cbc122).
