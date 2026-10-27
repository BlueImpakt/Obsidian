---
tags: [project, encours, sabinas-watersport]
created: 2026-10-21
statut: encours
client: sabinas-watersport
parent: prospect-charter
body_synced: 2026-10-23
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
- Maquette mobile cliquable (home + fiche catamaran + réservation 3 étapes + écran concept), EN officiel + FR/DE, dossier `maquette/` du repo — **v1 livrée** (revues Finish-Gate, accessibilité, textes appliquées). `?lang=de` ouvre en allemand.
- [[sabinas-08-message-accroche]] — WhatsApp + e-mail en allemand, avec traduction FR
- [[sabinas-09-inventions-et-hypotheses]] — ce qui n'est pas un fait dans la maquette (à valider avec Sabina)
- [[sabinas-07-prompt-3d-direction-artistique]] — Prompt 3D (2 transcripts + accès vault) pour la maquette concurrente `maquette-3d/` (test A/B), piste C « Horizon » retenue, en cours
- Walkthrough personas après maquette : `docs/07-walkthrough-apres.md` du repo (6/10 frictions résolues, 4 partielles)

## État actuel
- 2026-10-22 : analyse terminée ; maquette v1 (`maquette/`) déployée sur Vercel (noindex, lien privé), plan de redirection 301 des 3 domaines rédigé (§1.6 du doc stack), accroche WhatsApp DE/EN rédigée avec le lien de la démo, page concept enrichie (« Ce qu'il y a derrière le site »). Maquette concurrente au Prompt 3D (`maquette-3d/`, piste C « Horizon ») : corrections finish-gate en cours, puis comparaison A/B. Reste : contact de Melvin dans la maquette (`PITCH_CONTACT`), reconfirmation des chiffres d'avis, envoi.
- 2026-10-23 : e-mail de relance EN finalisé (stack détaillée, demande de créneau de 10 min), pas encore envoyé.

## Décisions techniques
- **Un seul site** sur `sabinas-watersport.com` (le nom qui porte les avis Google), avec deux univers *Boat trips* et *Watersports*. `catamaran-yachtsailing-rhodos.com` et `dolphin-tours-rhodos.com` redirigés page par page (plan 301 rédigé, §1.6 du doc stack).
- **Langues** : EN = version officielle, FR et DE en sélecteur (décision Melvin 2026-10-21). IT + PL plus tard.
- **Stack retenue** (après comparaison avec [[stack-creation-site-web]], voir [[sabinas-06-comparatif-stack-pattern]]) : Astro + Tailwind + TS (îlots React) + Sanity + Cloudflare + n8n + Stripe. Moteur maison P3 : **Convex** + BetterAuth + Stripe Connect (remplace Supabase). Polar écarté (service physique, TVA grecque).
- **Réservation P1** : demande structurée → validation de Sabina → lien d'acompte Stripe → automatismes n8n (rappel J-1, alerte vent, demande d'avis J+1). P2 Bókun si elle veut un calendrier en libre-service ou la synchro Viator.
- **Maquette** : déployée sur Vercel en lien privé (noindex), pas de publication publique claude.ai (page à la marque d'un tiers).

## Blocages / risques
- Les 3 domaines sont chez InterNetX (revendeur Jimdo), sur les DNS Jimdo : il faut les transférer avant toute résiliation. Codes de transfert : 2 à 4 semaines.
- `dolphin-tours-rhodos.com` **expire le 2026-12-01**.
- Chiffres d'avis (Google 5,0/479, TripAdvisor 4,9/443) et prix Viator (~1 250 €) lus sur des miroirs : à reconfirmer avant de les afficher.
- Mentions légales sans AFM ni GEMI, statut juridique des 2 entités inconnu.

## Next actions
- [ ] Reconfirmer notes et nombre d'avis Google/TripAdvisor + prix Viator
- [ ] Remplir `PITCH_CONTACT` (e-mail + WhatsApp de Melvin) dans `maquette/app.js`
- [ ] Une fois validé, extraire le boilerplate en pattern dans `03_knowledge/patterns/`
- [ ] Maquette 3D : finir les corrections du finish-gate (B1 « Everywhere. » qui déborde sur Für Sie en EN, 8 majeurs) puis comparer `maquette/` et `maquette-3d/` et choisir celle à envoyer
- [ ] Après avoir rempli `PITCH_CONTACT` (ligne 14 de `maquette/app.js`), incrémenter le `?v=` des scripts dans `index.html`, puis redéployer (`vercel deploy --prod` dans `maquette/`) ; l'accroche contient déjà le lien de la démo
- [ ] Maquette : trouver l'URL LinkedIn de Sabina (profil ou page) pour le bouton du footer, sinon le retirer ; décider d'ajouter Instagram (`sabinas.watersport`)
- [ ] Vérifier avec Sabina : point de rendez-vous catamaran (Stafilia Beach, pas Kiotari) et voisin de Dolphin Tours (Aulus Lindos vs Lindian Village)
- [ ] Trancher l'hébergement des automatisations (n8n auto-hébergé ~6,5 €/mois vs Convex, tarifs officiels à vérifier)
- [ ] Envoyer l'e-mail de relance à Sabina (version finale dans [[sabinas-08-message-accroche]]) ; harmoniser la durée proposée (10 min e-mail vs 15 min WhatsApp DE)

## Journal
- 2026-10-21 : Analyse des 3 sites livrée (6 docs + inventaire photos). Décision : un seul site sur sabinas-watersport.com, EN/DE d'abord, stack Astro + Sanity + n8n + Stripe, pack Pro 3 500 à 4 800 € + 89 à 129 €/mois.
- 2026-10-21 : Pattern [[stack-creation-site-web]] enrichi d'une variante « site d'activités / tourisme » (Astro + Sanity + Cloudflare + n8n + Stripe, réservation par paliers, Convex au palier 3).
- 2026-10-21 : Maquette v1 livrée (home avec carte vedette + lignes tarifaires, fiche catamaran avec carte d'itinéraire, réservation 3 étapes, écran concept pour Sabina ; EN officiel + FR/DE ; photos client en WebP ; Motion). Revues Finish-Gate, WCAG AA et textes appliquées. Message d'accroche DE rédigé. Polar écarté (interdit les services de voyage), Stripe conservé.
- 2026-10-21 : Prompt 3D écrit ([[sabinas-07-prompt-3d-direction-artistique]], 2 transcripts YouTube + accès vault en lecture seule) pour un test A/B : maquette parallèle `maquette-3d/` construite sans voir `maquette/`.
- 2026-10-21 : Maquette v1 itérée : walkthrough après = 6/10 frictions résolues ; tarifs sports nautiques en page détail ; vedette par filtre ; renommage Private / Half-Private tour, ton luxury & exclusive ; galeries fléchées ; hero drone HD ; 7 vidéos YouTube en nocookie ; bug Motion (scale(0)) corrigé.
- 2026-10-21 : Maquette 3D : 3 pistes en aveugle (A Bordalbum, B Carte de bord, C Horizon), Melvin choisit C (+ mode soleil clair) ; home, fiche, réservation et écran Für Sie construits ; a11y et LCP OK, finish-gate KO (1 bloquant, 8 majeurs) en correction.
- 2026-10-21 : Maquette v1 : liens d'avis Google / Tripadvisor intégrés et centrés dans leurs cartes de note (EN/FR/DE), scripts en `?v=36`.
- 2026-10-21 : Maquette v1 peaufinée : header « Exclusive boat trips » / Watersports, footer Facebook + LinkedIn, hero « Your own sailing day », photos watersports de Sabina (7 cartes), galeries PC 5 éléments sans défilement avec vidéo au centre tenant dans la première vue ; scripts en `?v=53`.
- 2026-10-21 : Maquette v1 : vidéo YouTube dans le hero, vidéos réparties par Melvin entre galeries et accueil, carte remplacée par une vraie carte OpenStreetMap à 4 repères (spots de Sabina non placés faute de coordonnées fiables) ; revue ux-copy + design-critique et boucle prospection à 4/5, reste le contact de réponse et l'hébergement privé (scripts `?v=68`).
- 2026-10-22 : Plan de redirection 301 des 3 domaines rédigé (§1.6 du doc stack) ; maquette déployée sur Vercel (noindex, lien privé), à utiliser pour l'accroche une fois PITCH_CONTACT rempli.
- 2026-10-22 : Accroche WhatsApp DE/EN rédigée avec le lien de la démo ; section « Ce qu'il y a derrière le site » (Astro, Sanity, Cloudflare, Stripe, automatismes) ajoutée à la page concept ; message insiste sur paiement sécurisé, 3 domaines redirigés, maquette évolutive.
- 2026-10-23 : E-mail de relance EN rédigé (lien maquette Vercel, stack en 6 lignes, conclusion « When would you have 10 minutes to discuss it? ») et reporté dans [[sabinas-08-message-accroche]] ; le WhatsApp DE propose encore « 15 minutes ».

## Liens
- Projet parent : [[prospect-charter]]
- Client : [[sabinas-watersport]]
- Patterns utilisés : [[stack-creation-site-web]]
- Repo / deployment : `C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte` (local, pas de git) — sites actuels : sabinas-watersport.com · catamaran-yachtsailing-rhodos.com · dolphin-tours-rhodos.com
