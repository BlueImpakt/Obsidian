---
tags: [project, encours, sabinas-watersport]
created: 2026-10-21
statut: encours
client: sabinas-watersport
parent: prospect-charter
body_synced: 2026-11-01
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
- **v2 au niveau du skill [[maquette-prospect]] (31/10/2026)** : [[sabinas-11-note-relecture]] — **à lire en premier pour la v2** ; écart au skill, faits, hypothèses, décisions, étude de réservation dans `attachments/` et dans `docs/` du repo (`11-ecart-au-skill.md`, `faits.md`, `hypotheses.md`, `decisions.md`, `etudes/2026-10-31-sabinas-reservation.md`), `DESIGN.md` à la racine, porte qualité `gate.json` + `gate-faits.json`, tests `tests/`.
- [[sabinas-12-dossier-envoi]] — dossier d'envoi : vidéo, avant/après, chiffres, page privée, messages J0 à J+15 (brouillons)

## État actuel
- 2026-10-22 : analyse terminée ; maquette v1 (`maquette/`) déployée sur Vercel (noindex, lien privé), plan de redirection 301 des 3 domaines rédigé (§1.6 du doc stack), accroche WhatsApp DE/EN rédigée avec le lien de la démo, page concept enrichie (« Ce qu'il y a derrière le site »). Maquette concurrente au Prompt 3D (`maquette-3d/`, piste C « Horizon ») : corrections finish-gate en cours, puis comparaison A/B. Reste : contact de Melvin dans la maquette (`PITCH_CONTACT`), reconfirmation des chiffres d'avis, envoi.
- 2026-10-23 : e-mail de relance EN finalisé (stack détaillée, demande de créneau de 10 min), pas encore envoyé.
- 2026-10-31 : maquette `maquette/` mise au niveau du skill [[maquette-prospect]] : hero plein écran (vue drone HD), en-tête avec l'accroche de Sabina, grille de 6 cartes pleines, section « Prix et conditions » (seul endroit des tarifs), acompte réel de 150 €, WhatsApp pré-rédigé à chaque étape, calendrier borné aux saisons réelles, photos q95 régénérées depuis les originaux, 4 langues (EN, DE, IT, FR ; DE et IT relus par agents). Erreurs de la v1 corrigées : « dès 640 € » sur le speedboat (400 €), acompte de 30 % inventé, 479 avis (510). Porte qualité n° 6 **PASS** (LCP téléphone en vrai bridage 3,8 s pour 4,0 s, poids 903 Ko, accessibilité et bonnes pratiques 100, 45 faits vérifiés en 4 langues, tunnel 7 gestes). Commits a3a3d82 → 59aea5d. **Pas redéployée** : la version en ligne est encore la v1.

## Décisions techniques
- **Un seul site** sur `sabinas-watersport.com` (le nom qui porte les avis Google), avec deux univers *Boat trips* et *Watersports*. `catamaran-yachtsailing-rhodos.com` et `dolphin-tours-rhodos.com` redirigés page par page (plan 301 rédigé, §1.6 du doc stack).
- **Langues** : EN = version officielle, DE et FR en sélecteur. IT (ajouté le 2026-10-31 d'après le skill, sans locuteur dans l'équipe) à garder seulement si un membre de l'équipe parle italien (décision du 2026-11-01). PL plus tard.
- **Stack retenue** (après comparaison avec [[stack-creation-site-web]], voir [[sabinas-06-comparatif-stack-pattern]]) : Astro + Tailwind + TS (îlots React) + Sanity + Cloudflare + n8n + Stripe. Moteur maison P3 : **Convex** + BetterAuth + Stripe Connect (remplace Supabase). Polar écarté (service physique, TVA grecque).
- **Réservation P1** : demande structurée → validation de Sabina → lien d'acompte Stripe → automatismes n8n (rappel J-1, alerte vent, demande d'avis J+1). P2 Bókun si elle veut un calendrier en libre-service ou la synchro Viator.
- **Maquette** : déployée sur Vercel en lien privé (noindex), pas de publication publique claude.ai (page à la marque d'un tiers).

## Blocages / risques
- Les 3 domaines sont chez InterNetX (revendeur Jimdo), sur les DNS Jimdo : il faut les transférer avant toute résiliation. Codes de transfert : 2 à 4 semaines.
- `dolphin-tours-rhodos.com` **expire le 2026-12-01**.
- Avis reconfirmés le 2026-10-31 sur Wanderlog (Google 5,0/510, TripAdvisor 4,9/443 — la v1 affichait 479 avis Google) ; prix Viator (~1 250 €) lu sur un miroir, encore à reconfirmer.
- Mentions légales sans AFM ni GEMI, statut juridique des 2 entités inconnu.

## Next actions
- [ ] Reconfirmer le prix Viator (~1 250 €) — avis reconfirmés le 31/10 (Google 5,0 / 510, Tripadvisor 4,9 / 443)
- [ ] Remplir `PITCH_CONTACT` (e-mail + WhatsApp de Melvin) dans `maquette/app.js`
- [ ] Une fois validé, extraire le boilerplate en pattern dans `03_knowledge/patterns/`
- [ ] Maquette 3D : abandonnée de fait (la v2 est faite sur `maquette/`) — à confirmer par Melvin
- [ ] Après avoir rempli `PITCH_CONTACT` (ligne 14 de `maquette/app.js`), incrémenter le `?v=` des scripts dans `index.html`, puis redéployer (`vercel deploy --prod` dans `maquette/`) ; l'accroche contient déjà le lien de la démo
- [x] Maquette : lien LinkedIn de recherche retiré, Instagram `sabinas.watersport` ajouté (2026-10-31)
- [ ] Vérifier avec Sabina : point de rendez-vous catamaran (Stafilia Beach, pas Kiotari) et voisin de Dolphin Tours (Aulus Lindos vs Lindian Village)
- [ ] Trancher l'hébergement des automatisations (n8n auto-hébergé ~6,5 €/mois vs Convex, tarifs officiels à vérifier)
- [ ] Envoyer l'e-mail de relance à Sabina (version finale dans [[sabinas-08-message-accroche]]) ; harmoniser la durée proposée (10 min e-mail vs 15 min WhatsApp DE)
- [ ] Relire la v2 ([[sabinas-11-note-relecture]]) et la tester 10 min sur iPhone sur https://sabinas-xuygcn.vercel.app/ (bureau et mode intermédiaire compris) ; trancher : recadrage portrait du hero, bouton principal, mise en page du hero sur ordinateur, adresse mail affichée
- [x] Revues de la v2 : comparaison à l'aveugle (1re, 7,8 contre 7,5 pour Edmiston), Finish-Gate, personas, accessibilité, code, couverture du site ; dossier d'envoi ([[sabinas-12-dossier-envoi]]) (2026-10-31)
- [ ] Messages d'envoi : adapter le J0 (modèle de premier contact alors que Sabina a déjà reçu la v1) et écrire ou sauter le J+8 (aucun détail d'avis vérifié) ; J0 par défaut mardi 3/11, lien de la maquette v2 valable jusqu'au 10/11
- [ ] Demander à Sabina le modèle du voilier (coque « Gib'Sea 302 », annonce Click&Boat « Dufour 30 Classic ») et le rôle de Roland / nom « Dolphin Tours »
- [ ] Poser à Sabina les 5 questions de l'étude de réservation (solde, météo, annulation, délai de réponse, hôtels)
- [ ] Italien : demander à Sabina si quelqu'un de l'équipe parle italien ; sinon retirer l'IT de la v2 (cliente « Giulia Rossi » du bureau en FR/DE) et republier

## Journal
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
- 2026-10-31 : Mise au niveau du skill maquette-prospect : repo sous git, écart au skill (`docs/11`), extraction outillée des 3 domaines, faits sourcés + porte qualité (`gate.json`), `DESIGN.md`, étude de réservation ; hero plein écran, en-tête, cartes pleines, « Prix et conditions », tunnel 7 gestes avec WhatsApp pré-rédigé, italien ajouté, allemand relu (62 corrections). Note : [[sabinas-11-note-relecture]].
- 2026-10-31 : Porte qualité n° 6 PASS sur la v2 (poids 2,1 Mo → 903 Ko, LCP téléphone 3,8 s, a11y et bonnes pratiques 100) ; bug v1 corrigé (barre du bas de la fiche catamaran sans présélection) ; commits jusqu'à 59aea5d, non redéployée.
- 2026-10-31 : Passe v2 terminée : vue bureau de Sabina (confirmer en 2 gestes, alerte vent, planning), mode intermédiaire (réception d'hôtel, agence), audit de couverture (modèle du voilier et « retour sous voiles » retirés), étude des tunnels de Rhodes (réservation instantanée seulement sur les plateformes, où Sabina vend), comparaison à l'aveugle 1re ; porte n° 10 PASS. Dossier d'envoi fait (vidéo EN 68 s, avant/après, messages). **v2 publiée sur https://sabinas-xuygcn.vercel.app/** (page privée `/p/`), v1 intacte sur sabinas-concept-x7k2m9. Commit 957daa4.
- 2026-10-31 : Dossier d'envoi v2 corrigé côté outil (J+8 réglable, attente d'images limitée) ; J0 à adapter (second contact après la v1), J+8 sans détail d'avis vérifié.
- 2026-11-01 : Dossier d'envoi : bandeau cookies du site d'origine masqué sur vidéo et avant/après (outil e75b595). Italien de la v2 remis en cause : gardé seulement si un membre de l'équipe parle italien, sinon retrait et republication (~20 min).

## Liens
- Projet parent : [[prospect-charter]]
- Client : [[sabinas-watersport]]
- Patterns utilisés : [[stack-creation-site-web]]
- Repo / deployment : `C:\Users\LENOVO\Documents\GitHub\sabina-watersport-refonte` (local, sous git depuis le 2026-10-31) — sites actuels : sabinas-watersport.com · catamaran-yachtsailing-rhodos.com · dolphin-tours-rhodos.com

