---
tags: [project, encours, sabinas-watersport]
created: 2026-10-21
statut: encours
client: sabinas-watersport
body_synced: 2026-10-21
---

# sabinas-watersport-refonte

## Objectifs du projet
- Proposer à froid une refonte web à Sabina (Sabine Kuehl) et Roland, Sabinas Watersport Rhodos (Lardos, Rhodes, Grèce) : regrouper leurs 3 sites Jimdo en un seul site qui convertit.
- En faire un **boilerplate réplicable** pour les opérateurs d'activités nautiques et d'excursions bateau (prospection sectorielle).

## Livrables
- Dossier d'analyse (ce dossier) :
  - [[sabinas-05-synthese]] — **à lire en premier**
  - [[sabinas-00-trois-domaines-chronologie]] — pourquoi 3 domaines, dates de MAJ
  - [[sabinas-01-audit-contenu]] — catalogue et tarifs 2026, incohérences, audit technique
  - [[sabinas-02-marche-concurrence]] — réputation, concurrents Rhodes, logiciels de réservation, cadre légal grec, langues
  - [[sabinas-03-walkthrough-cro]] — parcours mobile de 3 personas, top 10 frictions, 10 exigences maquette
  - [[sabinas-04-stack-boilerplate]] — stack, paliers de réservation, packs et prix
  - [[sabinas-assets-inventaire]] — 31 photos et 7 vidéos réutilisables
  - [[sabinas-06-comparatif-stack-pattern]] — stack des agents vs [[stack-creation-site-web]], stack retenue
- Maquette mobile cliquable (home + fiche catamaran + réservation 3 étapes), DE/EN, envoyée par lien à froid — **à faire**
- Message d'accroche e-mail/WhatsApp en allemand — **à faire**

## État actuel
- 2026-10-21 : analyse terminée (4 agents : audit, marché, CRO, stack). Brief validé ; maquette mobile écrite (home, fiche catamaran, réservation en 3 étapes, écran concept ; EN avec FR/DE), vérification en taille mobile en cours.

## Décisions techniques
- **Un seul site** sur `sabinas-watersport.com` (le nom qui porte les avis Google), avec deux univers *Boat trips* et *Watersports*. `catamaran-yachtsailing-rhodos.com` et `dolphin-tours-rhodos.com` redirigés page par page.
- **Langues** : EN + DE d'abord (45 % des touristes de Rhodes), puis IT + PL, FR en option.
- **Stack retenue** (après comparaison avec [[stack-creation-site-web]], voir [[sabinas-06-comparatif-stack-pattern]]) : Astro + Tailwind + TS (îlots React) + Sanity + Cloudflare + n8n + Stripe. Moteur maison P3 : **Convex** + BetterAuth + Stripe Connect (remplace Supabase). Polar écarté (service physique, TVA grecque).
- **Réservation P1** : demande structurée → validation de Sabina → lien d'acompte Stripe → automatismes n8n (rappel J-1, alerte vent, demande d'avis J+1). P2 Bókun si elle veut un calendrier en libre-service ou la synchro Viator.
- **Maquette** : fichier HTML local hébergé en privé par Melvin, pas de publication publique claude.ai (page à la marque d'un tiers).

## Blocages / risques
- Les 3 domaines sont chez InterNetX (revendeur Jimdo), sur les DNS Jimdo : il faut les transférer avant toute résiliation. Codes de transfert : 2 à 4 semaines.
- `dolphin-tours-rhodos.com` **expire le 2026-12-01**.
- Chiffres d'avis (Google 5,0/479, TripAdvisor 4,9/443) et prix Viator (~1 250 €) lus sur des miroirs : à reconfirmer avant de les afficher.
- Mentions légales sans AFM ni GEMI, statut juridique des 2 entités inconnu.

## Next actions
- [ ] Construire la maquette mobile DE/EN avec les vraies photos
- [ ] Reconfirmer notes et nombre d'avis Google/TripAdvisor + prix Viator
- [ ] Rédiger le message d'accroche en allemand (e-mail + WhatsApp)
- [ ] Héberger la maquette sur une URL privée (Cloudflare Pages ou Netlify)
- [ ] Une fois validé, extraire le boilerplate en pattern dans `03_knowledge/patterns/`

## Journal
- 2026-10-21 : Analyse des 3 sites livrée (6 docs + inventaire photos). Décision : un seul site sur sabinas-watersport.com, EN/DE d'abord, stack Astro + Sanity + n8n + Stripe, pack Pro 3 500 à 4 800 € + 89 à 129 €/mois.
- 2026-10-21 : Pattern [[stack-creation-site-web]] enrichi d'une variante « site d'activités / tourisme » (Astro + Sanity + Cloudflare + n8n + Stripe, réservation par paliers, Convex au palier 3).
- 2026-10-21 : Brief validé, maquette mobile écrite (home, fiche catamaran, réservation 3 étapes, écran concept ; EN + FR/DE, photos client en WebP, animations Motion), vérification mobile en cours. Polar écarté (interdit les services de voyage), Stripe conservé.

## Liens
- Client : [[sabinas-watersport]]
- Patterns utilisés : [[stack-creation-site-web]]
- Repo / deployment : `C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte` (local, pas de git) — sites actuels : sabinas-watersport.com · catamaran-yachtsailing-rhodos.com · dolphin-tours-rhodos.com
