---
tags: [project-doc, sabinas-watersport]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: GitHub/sabina-watersport-refonte/docs/04-stack-boilerplate.md
---

↩ [[sabinas-watersport-refonte]]

# 04 — Stack boilerplate & méthode de déploiement « opérateurs nautiques / excursions »

> Document d'architecture décisionnel. Client zéro : Sabinas Watersport Rhodos (Lardos, Rhodes).
> Cible : refaire vite et bien les sites des petits opérateurs d'activités nautiques, d'excursions en bateau et de tours.
> Rédigé le 21/10/2026. Tous les prix d'outils sont datés et sourcés en fin de document. Un prix marqué *(tiers)* vient d'un site comparatif, pas de l'éditeur : à reconfirmer avant devis.

---

## 0. TL;DR

| Sujet | Décision |
|---|---|
| Front | **Astro** (sortie statique, îlots JS minimaux) |
| Contenu éditable | **Sanity** (plan Free, Studio hébergé, utilisable sur mobile). Fallback : Keystatic Cloud |
| Hébergement / DNS / anti-spam / analytics | **Cloudflare** (Pages ou Workers static assets, Registrar, Turnstile, Web Analytics sans cookie, Bulk Redirects) |
| Automatisation | **n8n self-hosted** sur un VPS Hetzner partagé entre clients (autorisé par la licence tant que les clients n'accèdent pas à n8n) |
| Paiement | **Stripe** (compte au nom du client, Checkout/Payment Links pour l'acompte) |
| Booking | Paliers : **P1** demande de réservation intelligente + acompte Stripe → **P2** SaaS embarqué (Bókun par défaut) → **P3** moteur maison seulement si 8-10 clients le justifient |
| Domaines Sabina | **Un seul site** sur `sabinas-watersport.com`, `/en/ /de/ /fr/` (+ `/it/ /pl/` plus tard), 301 page à page depuis `catamaran-yachtsailing-rhodos.com` et `dolphin-tours-rhodos.com` |
| Méthode | Monorepo `core` + `sites/<client>`, `client.config.ts`, migration de contenu assistée par IA, **5 jours ouvrés** de production par client une fois le kit contenu complet |
| Modèle éco | Setup 1 800 → 8 000 € selon le pack + récurrent 39 → 249 €/mois. Le récurrent finance l'hébergement, la maintenance et surtout les automatisations |

Règle d'or : le gérant ou la gérante **saisit un prix une seule fois** (pas une fois par langue), depuis son téléphone, et le site est à jour 1 à 2 minutes plus tard, sans appeler Melvin.

---

## 1. Exigences du secteur

### 1.1 Constat sur l'existant de Sabina (crawl du 21/10/2026, `research/raw/`)

- **3 sites Jimdo** : `sabinas-watersport.com` (23 URLs, EN/DE/FR), `catamaran-yachtsailing-rhodos.com` (18 URLs, EN/DE/FR partiel), `dolphin-tours-rhodos.com` (4 URLs, EN, sur Jimdo Creator/Dolphin). Le contenu se recoupe : trois sites se partagent les mêmes requêtes Google et la même marque.
- `dolphin-tours-rhodos.com` précise « NO specific dolphin watching tours ». Le nom de domaine promet un produit qui n'existe pas : mauvais signal pour Google comme pour le client.
- Prix : une partie en texte (watersports : windsurf 55 €/h, jetski 45/50 €, catamaran privé 6 h 950/1 050/1 150 € selon 4/6/8 pers.), une partie en images. Chaque prix est **dupliqué dans 3 langues × 2 sites**, d'où des incohérences garanties dans le temps.
- Réservation : formulaire de contact (Powr.io, bloqué par le bandeau cookies), WhatsApp (+49), mobile grec (+30), page « Deposit payment ». Aucune disponibilité, aucun paiement intégré.
- Preuve sociale : un lien et un badge TripAdvisor. Pas d'avis sur le site, pas d'AggregateRating.
- YouTube et Google Maps sont bloqués par défaut par le bandeau cookies : la page affiche « content is not displayed », ce qui donne une mauvaise première impression.
- Titres de pages bourrés de mots-clés (« /Hilton/ Domes Aulus Rhodes/ Amoh Pefkos/ Lindos Imperial… »). C'est du SEO de 2010.

### 1.2 Exigences fonctionnelles (communes au secteur)

| # | Exigence | Détail / critère d'acceptation |
|---|---|---|
| F1 | Catalogue d'activités | Activité = page dédiée, catégorie (croisière, privé, voile, sports nautiques, snorkeling), durée, horaires, capacité, point de RDV, inclus/non inclus, itinéraire, galerie |
| F2 | Variantes de prix | Privé (prix par bateau selon tranche de pax), partagé (par personne), enfant, durée (10 min / 1 h / 3 h / 8 h), saison (basse/haute), suppléments (transfert, champagne). **Prix saisi 1 fois, affiché dans toutes les langues** |
| F3 | Multilingue | EN (x-default), DE, FR au lancement. IT, PL, NL, SV en option. URLs localisées, `hreflang` réciproques, sélecteur de langue qui conserve la page courante |
| F4 | Disponibilités | P1 : jours complets grisés + fermetures saisonnières. P2/P3 : créneaux et places en temps réel |
| F5 | Réservation + acompte | Demande → confirmation par l'opérateur → lien d'acompte Stripe (20-30 %) → confirmation + .ics + point de RDV. Solde sur place |
| F6 | WhatsApp | Bouton flottant `wa.me` avec message pré-rempli contextuel (activité + langue). Aucune dépendance à l'API WhatsApp au palier 1 |
| F7 | Avis | Badges Google/TripAdvisor (liens), avis récents mis en avant, collecte d'avis post-activité automatisée |
| F8 | Galerie / vidéo | Images responsive AVIF/WebP, vidéo en *facade* (poster + clic pour charger YouTube/Vimeo, ou MP4 court auto-hébergé sans son pour le hero) |
| F9 | Météo / annulation | Politique claire et multilingue (« annulé par nous pour vent = remboursé ou reporté »), bandeau « Opérations suspendues aujourd'hui » activable depuis le téléphone |
| F10 | Point de RDV | Carte statique (image) + lien Google Maps / Apple Maps, photo du ponton, instructions par langue |
| F11 | FAQ | Par activité + FAQ générale, réutilisée par le chatbot |
| F12 | Pages légales | Mentions (identité, n° fiscal grec / registre), confidentialité, CGV et conditions d'annulation, cookies. Modèles dans le boilerplate |

### 1.3 Exigences non-fonctionnelles

| # | Exigence | Cible mesurable |
|---|---|---|
| N1 | Performance mobile 4G | LCP < 2,0 s sur un téléphone Android milieu de gamme en 4G simulée, CLS < 0,05, INP < 200 ms. Lighthouse mobile ≥ 95. JS ≤ 30 Ko gzip par page hors widget de booking. Hero ≤ 120 Ko |
| N2 | SEO technique | HTML statique, sitemap par langue, `hreflang`, canonical, données structurées valides (Rich Results Test sans erreur), aucun prix en image |
| N3 | Données structurées | `LocalBusiness` (+ `geo`, `openingHoursSpecification` saisonnière, `sameAs`), `TouristTrip` + `Offer` par activité, `BreadcrumbList`, `FAQPage`, `AggregateRating` **uniquement sur des avis collectés en propre** (voir 1.4) |
| N4 | RGPD / ePrivacy | Pas de cookie non essentiel par défaut, donc **pas de bandeau cookies** au lancement. Embeds tiers en click-to-load. Données de réservation hébergées en UE. Registre des traitements fourni |
| N5 | Accessibilité | WCAG 2.2 AA comme standard du boilerplate. Le European Accessibility Act exempte les microentreprises de services, mais tous les clients ne seront pas des microentreprises |
| N6 | Autonomie client | Changer un prix, une date de fermeture, une photo ou activer le bandeau météo en moins de 2 minutes sur mobile, sans formation technique |
| N7 | Robustesse | Une demande de réservation n'est **jamais** perdue, même si n8n est en panne (voir 4.1) |
| N8 | Coût récurrent infra | ≤ 10 €/mois par client hors domaine et hors frais Stripe |
| N9 | Réversibilité | Le client possède son domaine, son Stripe, son Google Business Profile et son projet Sanity. Il peut partir avec un export complet |

### 1.4 Points SEO souvent mal faits dans ce secteur

- **AggregateRating auto-déclaré** : Google n'affiche pas d'étoiles pour un `LocalBusiness` ou une `Organization` qui note sa propre entreprise. Ses règles interdisent aussi de baliser des avis copiés depuis TripAdvisor ou Google. On peut afficher ces avis (en citant la source), mais **pas les mettre en schema**. On ne balise que les avis collectés sur le site après l'activité.
- **FAQPage** : depuis 2023, Google réserve ce rich snippet aux sites gouvernementaux et de santé. On garde le balisage, utile pour la compréhension du contenu et les moteurs IA, mais sans en attendre d'étoiles ni d'accordéon dans les SERP.
- **TouristTrip** ne produit pas de rich result Google. Il structure l'offre (itinéraire, `touristType`, `provider`). Le vrai levier de visibilité « réserver » sur Google est **Google Things to do / Reserve with Google**, accessible uniquement via un partenaire de connectivité, donc au palier 2 (voir 3.3).
- **Google Business Profile** pèse plus lourd que tout le reste en SEO local. Catégories, photos, horaires saisonniers, lien site par langue, réponses aux avis : c'est dans la checklist de déploiement, pas en option.
- **Moteurs IA** (ChatGPT, Perplexity, AI Overviews) : ils citent du texte factuel. Prix, durée, point de départ et inclus doivent être en texte, ce qui est impossible avec des prix en image.

### 1.5 Multi-domaines : décision pour Sabina

**ADR-001 : Site unifié sur un seul domaine**

- **Statut** : Proposé
- **Contexte** : 3 domaines Jimdo, contenus redondants, autorité éclatée, un domaine trompeur (dolphin). La marque connue sur TripAdvisor et Google est « Sabinas Watersport Rhodos ».
- **Options**
  1. *Garder 3 sites* : on triple la maintenance, les sites se cannibalisent, et chaque prix est à mettre à jour 3 fois.
  2. *Site unifié + 301* : autorité consolidée, un seul CMS, une seule fiche par activité.
  3. *Site unifié + domaines secondaires en landing pages* : complexité pour un gain nul, Google n'accorde presque plus de bonus aux domaines à mots-clés exacts (« exact match domain »).
- **Décision** : option 2. Domaine principal `sabinas-watersport.com`, cohérent avec la marque, la fiche TripAdvisor et l'URL la plus ancienne et la plus fournie. Structure `/{lang}/{slug-localisé}/`. `x-default` → `/en/`.
- **Conséquences** : redirections 301 **page à page** (pas toutes vers la home) pour les ~45 URLs connues. Les anciens domaines restent renouvelés **au moins 2 ans** (idéalement à vie, c'est ~10-15 €/an). Les DNS sont transférés hors Jimdo **avant** la résiliation des packs Jimdo (voir risques 7.4).

Règle générale pour le boilerplate : **1 opérateur = 1 domaine**. On ne fait de multi-sites que pour deux marques réellement distinctes (clientèle et produits différents), jamais pour « ranker » sur un mot-clé.

---

## 2. Comparatif des stacks

### 2.1 Options

- **(A) Astro + CMS headless/git + Cloudflare** : site statique ultra-rapide. Le contenu vit dans un CMS (Sanity, Keystatic, Decap/Sveltia, Payload). Chaque publication déclenche un rebuild de 1 à 2 min.
- **(B) Next.js + Supabase + Stripe** : application full-stack avec booking maison.
- **(C) WordPress + thème + plugin booking** : l'écosystème connu, à maintenir.
- **(D) Webflow ou Framer + widget de booking SaaS** : no-code hébergé.

### 2.2 Tableau (notes de 1 à 5, 5 = meilleur pour ce cas)

| Critère | A. Astro + Sanity + Cloudflare | B. Next.js + Supabase + Stripe | C. WordPress + plugins | D. Webflow / Framer + widget |
|---|---|---|---|---|
| Coût de build du **1er** site | 3 (≈ 10-15 j, boilerplate inclus) | 1 (≈ 25-40 j avec booking) | 4 (≈ 6-8 j) | 4 (≈ 5-7 j) |
| Coût de build des sites **suivants** | **5** (≈ 5 j) | 3 | 3 (chaque site dérive) | 3 (clonage de template, mais pas de code partagé) |
| Coût récurrent client (infra) | **5** : ~0-5 €/mois (Cloudflare Free, Sanity Free) | 2 : Supabase Pro 25 $/mois dès qu'on est en prod (le Free se met en pause après 1 semaine d'inactivité), Vercel Pro 20 $/mois (Hobby interdit en commercial) | 3 : hébergement 5-25 €/mois + licences (WPML ~99 €/an *(tiers)*, plugin booking premium) | 2 : Webflow CMS ~23 $/mois + localisation ~9 $/locale/mois *(tiers)* ; Framer Basic 10 $/mois + **20 $/locale/mois** |
| Autonomie client (mobile) | 4 : Sanity Studio fonctionne sur mobile, prix saisi une fois | 2 : admin à développer soi-même | 4 : WP admin connu, mais lourd sur mobile et risque de casser la mise en page | 3 : l'Editor fonctionne, mais le mobile est médiocre et les champs prix sont à dupliquer par locale selon le modèle |
| Performance 4G | **5** : HTML statique, ~0 JS | 4 : bonne si bien faite, plus de JS | 2 : correcte avec du travail, se dégrade avec chaque plugin | 3 : bonne, mais runtime JS imposé, surtout sur Framer |
| SEO (technique + i18n + schema) | **5** : contrôle total | 5 | 4 : plugins SEO matures, hreflang via WPML/Polylang | 3 : schema custom limité, i18n payante par langue |
| Scalabilité pour Melvin (seul) | **5** : un `core` partagé, mises à jour propagées, CI | 2 : chaque client devient une app à maintenir | 2 : N sites × M plugins à patcher (sécurité) | 2 : pas de code partagé, chaque site est un îlot |
| Lock-in | 4 : Astro open source (racheté par Cloudflare en 01/2026, reste MIT), contenu exportable en NDJSON | 4 : open source, mais du code maison à maintenir | 5 : open source | 1 : propriétaire, export partiel |
| Maintenance / sécurité | **5** : rien à patcher côté serveur | 3 | 1 : mises à jour hebdomadaires, surface d'attaque | 5 : géré par l'éditeur |
| **Total /45** | **41** | 26 | 28 | 26 |

### 2.3 Choix du CMS dans l'option A

**ADR-002 : Sanity comme CMS par défaut**

| | **Sanity** | Keystatic (Cloud) | Decap / Sveltia | Payload |
|---|---|---|---|---|
| Édition sans compte GitHub | Oui | Oui avec Keystatic Cloud (Free jusqu'à 3 utilisateurs par équipe, puis 5 $/user/mois) | **Non** : Netlify Identity/Git Gateway est déprécié, il faut GitHub OAuth | Oui |
| UX mobile | Correcte : Studio responsive, publication en 1 tap | Correcte | Moyenne | Bonne |
| i18n champ par champ (prix non dupliqué) | Oui (champs `{en,de,fr}` ou plugin) | Faisable, moins ergonomique | Faisable | Oui (natif) |
| Images (CDN, recadrage, hotspot) | Oui, inclus | Payant (Cloud Images, plan Pro dès 10 $/mois) ou dans le repo | Dans le repo | À héberger |
| Où vit le contenu | Cloud Sanity (export CLI) | **Git** (aucun lock-in) | Git | Base de données à héberger |
| Coût | Free : 20 sièges, 10k documents, 2 datasets publics, 250k requêtes API/mois | Free ≤ 3 users | Gratuit | Serveur + base de données à payer et maintenir |
| Webhook → rebuild | Natif | Commit git → build | Commit git → build | Natif |

- **Décision** : Sanity, un projet Free par client, créé par Melvin puis transféré au client (ou invitation du client en *Administrator*).
- **Pourquoi** : édition mobile correcte sans GitHub, prix saisi une seule fois, CDN d'images gratuit avec recadrage, et schémas en TypeScript partagés entre clients via le `core`.
- **Ce qu'on accepte** : une dépendance SaaS. Sanity a déjà modifié son plan gratuit par le passé. Et un dataset Free est **public** : n'importe qui ayant l'ID du projet peut lire le contenu. C'est acceptable pour du contenu marketing (les prix sont publics de toute façon), **jamais** pour des réservations ou des données personnelles.
- **Atténuation** : export NDJSON nocturne (`sanity dataset export`) vers Cloudflare R2 par n8n. Le schéma de contenu est neutre (section 5.3) : migrer vers Keystatic ou Payload reste une affaire de script, pas de réécriture.
- **Fallback** : Keystatic Cloud, si le client refuse un SaaS de plus ou si Sanity durcit son plan Free.

### 2.4 Recommandation

**Stack A : Astro + Sanity + Cloudflare + n8n (Hetzner) + Stripe.**

1. C'est la seule option où **le 10e site coûte nettement moins cher que le 2e** : le `core` partagé porte composants, schémas, JSON-LD et workflows.
2. Les cibles 4G et SEO sont atteintes par construction, pas par optimisation.
3. Coût récurrent quasi nul côté infra : le mensuel facturé est presque entièrement de la marge sur du service (automatisations, suivi).
4. Pas de serveur web à patcher. Le seul serveur est le VPS n8n, mutualisé.
5. Le booking reste découplé : un SaaS au palier 2 ou un moteur maison au palier 3 se branchent sans toucher au site.

Ce qu'on paie : un investissement initial (boilerplate) plus élevé que WordPress, et Melvin doit être à l'aise avec Astro et TypeScript. C'est un vrai coût d'apprentissage si son profil est surtout no-code. Atténuation : Sabina sert de client zéro, et on ne généralise qu'au 2e client (voir 5.6).

---

## 3. Booking : architecture en paliers

### 3.1 Vue d'ensemble

```
                        ┌───────────────────────────── Site Astro (statique, Cloudflare) ─────────────────────────────┐
 Touriste (mobile 4G) → │ Page activité → BookingCTA sticky → formulaire (P1) │ widget SaaS (P2) │ checkout maison (P3) │
                        └───────────────┬──────────────────────────────┬──────────────────────┬───────────────────────┘
                                        │ POST /api/request            │ iframe/JS            │ API
                                        ▼                              ▼                      ▼
                        Worker Cloudflare (Turnstile, validation,   SaaS booking          Supabase + Stripe
                        file D1 = filet de sécurité)                (Bókun/Regiondo…)     (multi-tenant)
                                        │ webhook                      │ webhooks              │ webhooks
                                        ▼                              ▼                      ▼
                        ┌──────────────────────── n8n (Hetzner, mutualisé) ─────────────────────────┐
                        │ notif opérateur · lien acompte Stripe · confirmations · J-1 · météo · avis │
                        └───────────────────────────────────────────────────────────────────────────┘
                                        │
                     Google Calendar opérateur · email (Brevo/Resend) · WhatsApp (wa.me ou Cloud API) · Stripe
```

Le site ne sait **jamais** comment le booking est implémenté. Il appelle un composant `BookingCTA` dont l'implémentation dépend de `client.config.ts → booking.mode = "request" | "saas" | "native"`. C'est la frontière qui rend les paliers réversibles.

### 3.2 Palier 1 : demande de réservation intelligente (défaut, Sabina au lancement)

**Parcours client**

1. Sur la page activité, le formulaire est pré-rempli : activité, variante (privé 4/6/8 pers.), date (les jours complets sont grisés), nombre d'adultes et d'enfants, hôtel ou zone, langue, email, WhatsApp, message. Anti-spam : Turnstile (invisible).
2. Prix indicatif calculé côté client : total, acompte de 30 %, solde sur place.
3. Écran de confirmation : « Demande reçue. Réponse sous 2 h entre 8 h et 21 h (heure de Rhodes) », avec un bouton WhatsApp pour accélérer.

**Côté opérateur (Sabina)**

4. Elle reçoit un email + une notification avec un récap et 3 boutons, qui sont des liens signés vers un webhook n8n : **✅ Confirmer** · **📅 Proposer une autre date** · **❌ Refuser (complet / météo)**.
5. **Confirmer** : n8n crée une session Stripe Checkout pour l'acompte (montant et métadonnées de réservation), puis envoie au client un email dans sa langue avec le lien de paiement (expiration 24-48 h). Le lien part aussi en WhatsApp si le client a donné son numéro et qu'on est au palier WhatsApp API ; sinon c'est Sabina qui l'envoie d'un tap via `wa.me` pré-rempli.
6. Webhook Stripe `checkout.session.completed` → n8n : réservation passée à « acompte payé », événement créé dans le Google Calendar de Sabina, email de confirmation (point de RDV, carte, .ics, conditions météo et annulation), ligne ajoutée au journal des réservations.
7. Jours complets : n8n lit Google Calendar toutes les 15 min et publie un JSON `/availability.json` (KV Cloudflare) que le date-picker consomme. Règle simple par activité : 1 daytrip et 1 sunset par bateau et par jour.

**Stockage** : Google Calendar = vue de l'opérateur, qu'il utilise déjà. Le journal des réservations est une table n8n (Data Tables) ou une table Postgres sur le VPS. On évite le Google Sheet partagé, trop facile à casser. **Aucune donnée personnelle dans Sanity.**

**Coût** : 0 € de licence. Stripe 1,5 % + 0,25 € pour une carte standard de l'EEE ; 3,15 % + 0,25 € (+2 % de conversion) pour une carte hors EEE ; 2,5 % + 0,25 € pour une carte UK. Sur un acompte de 300 € payé avec une carte allemande, ~4,75 €.

**Limites assumées** : pas de disponibilité au créneau près, une confirmation humaine (délai), pas de distribution OTA, pas de Google Things to do.

### 3.3 Palier 2 : SaaS de booking embarqué

Comparatif (prix vérifiés le 21/10/2026, voir sources) :

| SaaS | Abonnement | Commission / frais | Qui paie | Points clés pour ce secteur |
|---|---|---|---|---|
| **Bókun** (groupe Tripadvisor/Viator) | Free 0 $ · **Start 49 $/mois** · Plus 149 $/mois · Premium 499 $/mois | Start +1,5 %, Plus +1,25 % (la page indique aussi 1 %), Premium +1 % sur les réservations concernées ; 0 % hors ligne ; 0 frais Bókun sur Viator | Opérateur | Channel manager OTA (Viator, GetYourGuide…), payment links, ressources (bateaux), partenaire Google Things to do. **Défaut recommandé** |
| **Regiondo** | ~49-58 €/$ à ~199-234 €/$ par mois *(tiers, sources contradictoires)* | Frais par ticket (~0,49-0,56 €) et frais d'usage % selon les sources *(tiers)* | Opérateur | Fort sur le marché DACH, pertinent si la clientèle est majoritairement germanophone. Prix à obtenir en direct |
| **Rezdy** | Foundation 49 $ · Accelerate 99 $ · Expansion 249 $/mois | **3 % en ligne** (absorbable ou refacturable au client) + 0,70-1 $ par réservation offline/agent | Au choix | Gros réseau de revendeurs (Australie / UK) |
| **Checkfront** | **99 €/mois** | **3 % en ligne**, 0 % offline | Au choix | Gestion des ressources solide, widgets React, API sans surcoût |
| **TuriTop** | ~99 €/mois + 1 à 1,5 %, ou modèle par personne (0,03-0,10 €/pers.) *(tiers + page officielle partielle)* | Variable | Variable | Espagnol, bon rapport qualité/prix, tarification confuse : demander un devis |
| **FareHarbor** | 0 € | **Jusqu'à 6 %** de frais de réservation **payés par le client final** à l'achat (2 % via API/tiers) *(tiers, cohérents entre eux)* | Client final | « Gratuit » pour l'opérateur, mais les frais apparaissent au checkout (friction), contrat et écosystème fermés. Déconseillé par défaut |

**Recommandation P2** : **Bókun Start** pour un opérateur comme Sabina (produits majoritairement privés, besoin d'OTA à terme), ou **Free** si l'objectif n'est que de gérer le calendrier sans vente en ligne. À volume égal, 1,5 % + 49 $/mois revient moins cher que 3 % dès ~3 300 $ de CA en ligne par mois. Le widget est chargé **uniquement** au clic sur « Réserver » (facade) pour préserver la performance des pages.

**Ce qui ne bouge pas en P2** : les workflows n8n à valeur ajoutée (J-1, météo, avis, relances) se branchent sur les webhooks du SaaS. Le SaaS gère l'inventaire, Blue Impakt garde la couche relation client. C'est la différenciation.

### 3.4 Palier 3 : moteur maison (Supabase + Stripe)

- **Périmètre** : produits, créneaux, inventaire (bateaux, places), réservations, acomptes et soldes, annulations et remboursements, back-office mobile pour l'opérateur, iCal export.
- **Architecture** : un seul backend **multi-tenant** (Supabase Pro, RLS par `operator_id`), **Stripe Connect** (comptes connectés au nom de chaque opérateur : Melvin ne détient jamais les fonds, ce qui évite d'être prestataire de paiement), un site Astro par client qui appelle l'API.
- **Coût de build** : 30 à 50 jours la première fois. C'est un produit, plus une prestation, et ça se rapproche de la logique KM0 (0 % de commission).
- **Ce que ça coûte vraiment** : surbooking, fuseaux horaires, SCA/3-D Secure, litiges et chargebacks, remboursements partiels, support en pleine saison. Sur un SaaS, c'est l'éditeur qui encaisse ce risque ; avec un moteur maison, c'est Melvin, en août, seul.

### 3.5 Quand passer d'un palier à l'autre

| Passage | Déclencheurs (il en faut au moins 2) |
|---|---|
| **P1 → P2** | > 150-200 réservations par saison · > 20 % des demandes perdues faute de réponse rapide (mesuré par n8n : demandes non confirmées ou non payées) · produits **partagés au siège** (par ex. sunset cruise à 12 places vendues à la place) · plusieurs bateaux ou équipes · volonté d'être sur Viator, GetYourGuide ou Google Things to do · l'opérateur passe plus de 30 min/jour sur la gestion des réservations |
| **P2 → P3** | ≥ 8-10 clients Blue Impakt dans le vertical avec des besoins homogènes · frais SaaS cumulés du portefeuille > ~1 500 €/mois · fonctionnalité bloquante absente des SaaS · **et** Melvin a la capacité de faire du support en saison (associé ou sous-traitant). Sans cette dernière condition, on ne passe pas en P3 |
| **Retour P2 → P1** | Le SaaS coûte plus qu'il ne rapporte (peu de ventes en ligne, clientèle qui réserve sur place). On le garde éventuellement pour le calendrier seul (Bókun Free) |

---

## 4. Couche automatisation & IA (le différenciateur Blue Impakt)

### 4.1 Principes

1. **Humain dans la boucle** sur tout ce qui engage l'opérateur : confirmation, report météo, remboursement. L'automatisation prépare et l'opérateur valide d'un tap.
2. **Aucune demande perdue** : le Worker Cloudflare écrit d'abord la demande dans D1 (base SQLite), **puis** appelle n8n. Si n8n ne répond pas, le Worker envoie un email de secours direct à l'opérateur et un job de rattrapage relit D1. Le VPS n8n mutualisé est un point de défaillance unique pour tous les clients : on le traite comme tel.
3. **Workflows = templates versionnés** dans `packages/n8n-templates/`, paramétrés par client (variables et credentials). Un correctif est appliqué partout via un script d'import (API n8n).
4. **Licence n8n** : la FAQ officielle de la Sustainable Use License autorise un consultant à faire tourner, sur **sa propre instance**, des workflows pour plusieurs clients, sans limite de nombre, **à condition que les clients n'aient pas accès à l'interface n8n**. Ne jamais donner d'accès n8n à un client.

### 4.2 Catalogue de workflows

| # | Workflow | Déclencheur | Action | Palier |
|---|---|---|---|---|
| W1 | Réception demande | Webhook Worker | Normalise la demande, notifie l'opérateur avec 3 boutons signés, accuse réception au client dans sa langue | P1 |
| W2 | Acompte | Clic « Confirmer » | Crée la session Stripe Checkout, envoie le lien au client, programme une relance à H+24 si non payé, expiration à H+48 | P1 |
| W3 | Confirmation | Webhook Stripe | Calendar, email de confirmation + .ics + point de RDV, journal | P1 |
| W4 | Rappel J-1 | Cron 18 h (heure de Rhodes) | Email (et WhatsApp en option) : heure, point de RDV avec photo du ponton et lien Maps, quoi apporter, contact du jour | P1 |
| W5 | Alerte météo/vent | Cron 6 h et 18 h, J-1 et J-0 | Récupère vent et rafales sur le point de RDV. Au-dessus du seuil défini par activité (ex. vent > 5 Bft pour le voilier, rafales > 25 nœuds), envoie à l'opérateur « 3 sorties à risque demain » avec un bouton **Prévenir les clients et proposer un report**. Rien ne part sans validation | P1 |
| W6 | Demande d'avis | J+1, 10 h | Email ou WhatsApp personnalisé : lien direct vers l'avis Google (`writereview`) ou TripAdvisor selon la langue et l'historique. Formulaire « note interne » d'abord si l'opérateur le veut. Attention : le *review gating* (ne solliciter que les clients satisfaits) est interdit par Google ; on demande à tout le monde | P1 |
| W7 | Relance devis | Demande sans réponse client à H+24 / H+72 | Relance douce + proposition d'une alternative (autre date, autre activité) | P1 |
| W8 | Sync calendrier → dispos | Cron 15 min | Google Calendar → `availability.json` (KV) | P1 |
| W9 | Bandeau opérations | Message de l'opérateur (« STOP today wind ») sur un canal dédié, ou toggle dans Sanity | Active le bandeau météo multilingue sur le site + rebuild | P1 |
| W10 | Backup contenu | Cron nocturne | `sanity dataset export` → R2, rétention 30 jours | P1 |
| W11 | Debounce rebuild | Webhook Sanity | Regroupe les publications (fenêtre de 3 min) puis déclenche un seul build (GitHub Actions) | P1 |
| W12 | Rapport hebdo | Lundi 8 h | Demandes, taux de conversion demande → acompte, CA acomptes, avis obtenus, pannes. Envoyé à l'opérateur **et** à Melvin (c'est la justification du mensuel) | P1 |
| W13 | Chatbot FAQ (site) | Widget site | Voir 4.3 | P2 / Premium |
| W14 | Ponts SaaS | Webhooks Bókun etc. | Branche W3-W7 et W12 sur les réservations du SaaS | P2 |

**Source météo** : MET Norway Locationforecast (gratuit, usage commercial autorisé avec attribution, à reconfirmer à la mise en place). **Ne pas** utiliser l'API gratuite d'Open-Meteo : elle est réservée à l'usage non commercial (vérifié le 21/10/2026). Ses plans commerciaux existent, mais leur prix n'est pas affiché publiquement.

### 4.3 IA

| Usage | Modèle | Garde-fous | Coût estimé |
|---|---|---|---|
| **Traduction assistée** des contenus (EN → DE/FR/IT/PL) | Claude Sonnet 5.5 (2 $/10 $ par million de tokens in/out) | Glossaire par client (noms de lieux, de bateaux, termes nautiques), ton défini, **relecture native obligatoire** sur les pages clés (accueil, activités, CGV). Les traductions arrivent dans Sanity en brouillon, jamais publiées directement | Site de ~25k mots × 4 langues ≈ 3-5 $ en tokens. Le vrai coût est la relecture humaine |
| **Migration de l'ancien site** | Claude Sonnet 5.5 (texte + vision pour les prix en image) | Extraction vers un JSON typé selon le schéma de la section 5.3, validée par Zod, puis revue humaine avant import | < 5 $ par site |
| **Chatbot FAQ** sur le site | Claude Haiku 5.5 (0,10 $/0,50 $ par million de tokens) | Réponses **uniquement** à partir des FAQ, activités et prix de Sanity (contexte injecté et mis en cache). Ne confirme jamais une réservation ni une disponibilité. Escalade vers WhatsApp/formulaire avec transcription. Disclaimer IA. Logs sans données personnelles | ~500 conversations/mois en haute saison ≈ 2-5 $/mois. Même avec Sonnet 5.5 : ~15-45 $/mois |
| **Brouillons de réponse aux avis** | Haiku 5.5 | L'opérateur valide chaque réponse | Négligeable |

**WhatsApp via l'API (Cloud API)** : pas au palier 1. Raisons :
- (a) Sabina utilise WhatsApp sur son téléphone, et basculer son numéro vers l'API impose la *coexistence* (app Business + API) ou un second numéro ;
- (b) depuis le 01/07/2025, Meta facture au message délivré selon le **pays du destinataire**. Un message *utility* vers un numéro allemand coûte ~0,046 € *(tiers, juillet 2026)* ;
- (c) au **01/10/2026**, les messages utility envoyés dans la fenêtre de service de 24 h deviennent payants, et les messages de service passent à un palier gratuit de 1 000/mois par numéro (doc Meta, vérifiée le 21/10/2026).

Au palier 1, on s'appuie donc sur l'email et sur des liens `wa.me` pré-remplis que l'opérateur envoie d'un tap. Exemple de coût si on active l'API : 300 réservations × 3 messages × ~0,05 € ≈ 45 €/saison, plus la marge éventuelle d'un BSP.

### 4.4 Coûts d'infrastructure de la couche automatisation (vérifiés le 21/10/2026)

| Poste | Option | Coût | Commentaire |
|---|---|---|---|
| n8n | **Self-hosted Community** sur Hetzner Cloud | VPS à partir de ~6,49 €/mois HT (« Regular Performance ») + backups (~20 %) | **Mutualisé** entre tous les clients. Postgres, Caddy, backups quotidiens, monitoring uptime. ~2 h/mois de maintenance |
| n8n | n8n Cloud | Starter 20 €/mois (2,5k exécutions), Pro 50 €/mois (10k), prix en facturation annuelle | Plus simple, mais 2,5k exécutions sont vite atteintes à plusieurs clients. Plutôt pour démarrer avec 1 ou 2 clients si Melvin ne veut pas d'ops |
| Email transactionnel | Brevo ou Resend | Paliers gratuits a priori suffisants à ce volume (non vérifiés ici, à confirmer) | Domaine d'envoi authentifié (SPF, DKIM, DMARC) par client |
| LLM | API Anthropic | 2-10 $/mois par client avec chatbot | Clé API au nom de Blue Impakt, refacturée dans le pack |
| Météo | MET Norway | 0 € | Attribution obligatoire |
| Avis Google (affichage) | Places API (New), Place Details | 1 appel/jour ≈ 30/mois, sous le quota gratuit mensuel du SKU (5 000 en Pro, 1 000 en Enterprise si on récupère les avis) *(chiffres tiers, à reconfirmer)* | Mis en cache au build. Aucun appel côté navigateur |
| Anti-spam | Cloudflare Turnstile | 0 € | Pas de cookie de tracking |

**Coût infra total par client ≈ 3 à 10 €/mois** (part de VPS + LLM + domaine lissé), hors frais Stripe et hors SaaS de booking.

---

## 5. Structure du boilerplate

### 5.1 Arborescence (monorepo)

**ADR-003 : Monorepo `core` + `sites/*` plutôt qu'un template copié par client**

- **Contexte** : Melvin est seul. Avec un template copié, chaque site diverge et un correctif doit être appliqué N fois.
- **Décision** : monorepo pnpm workspaces. Le `core` contient le code partagé, chaque `sites/<client>` ne contient que de la configuration, du thème et des surcharges explicites.
- **Conséquences** : un changement dans le `core` peut casser tous les sites, d'où une CI qui builde tous les sites et lance les tests visuels et de schéma avant merge. Pour la sortie d'un client, un script `tooling/eject` produit un repo autonome (core vendorisé). On écarte l'alternative « core publié en package npm versionné » : plus propre, mais trop de cérémonie pour un développeur seul. On la reconsidérera au-delà de ~15 sites.

```
blueimpakt-sites/
├── packages/
│   ├── core/                         # tout ce qui est partagé
│   │   ├── components/
│   │   │   ├── sections/             # Hero, ActivityGrid, PriceTable, Itinerary, Included, Reviews, Gallery, FAQ, MeetingPoint, CTABoth…
│   │   │   ├── booking/              # BookingCTA (switch request|saas|native), RequestForm, DatePicker, SaasFacade
│   │   │   └── ui/                   # Button, Badge, LangSwitcher, WhatsAppFloat, WeatherBanner, Price
│   │   ├── layouts/                  # BaseLayout (head SEO, hreflang, JSON-LD), ActivityLayout, LegalLayout
│   │   ├── lib/
│   │   │   ├── seo/                  # jsonld.ts (LocalBusiness, TouristTrip, Offer, FAQPage, Breadcrumb), hreflang.ts, sitemap.ts
│   │   │   ├── i18n/                 # routing, dictionnaires UI (EN/DE/FR/IT/PL/NL), formatage prix/dates par locale
│   │   │   ├── pricing.ts            # résolution variante/saison, calcul acompte
│   │   │   └── sanity.ts             # client + requêtes GROQ typées
│   │   ├── styles/                   # tokens.css (variables), base.css, themes/{lagoon,sunset,aegean,sand}.css
│   │   └── astro-preset.ts           # intégrations Astro communes (i18n, sitemap, images, adapter)
│   ├── sanity-schemas/               # schémas Activity, Boat, FAQ, Review, Page, Location, Settings + structure du Studio + i18n
│   ├── workers/                      # /api/request (Turnstile, Zod, D1, appel n8n, fallback email), /api/availability
│   ├── n8n-templates/                # W1…W14 exportés en JSON + variables.md + script d'import via l'API n8n
│   └── legal-templates/              # mentions, confidentialité, CGV/annulation, registre RGPD (EN/DE/FR), à faire valider
├── sites/
│   └── sabina/
│       ├── client.config.ts          # LE fichier de config client (ci-dessous)
│       ├── theme.css                 # surcharges de tokens (palette, typo)
│       ├── astro.config.mjs          # 5 lignes : import du preset + config
│       ├── src/pages/[lang]/…        # routes générées par le core, surcharges ponctuelles autorisées
│       ├── public/                   # favicon, og-image, logo.svg
│       ├── redirects.csv             # ancienne URL → nouvelle URL (source de vérité des 301)
│       └── studio/sanity.config.ts   # importe sanity-schemas, titre/logo client
├── tooling/
│   ├── create-site/                  # `pnpm create-site sabina` : scaffold, projet Sanity, projet Cloudflare, secrets
│   ├── migrate/                      # crawl de l'ancien site → extraction LLM → JSON validé → NDJSON Sanity
│   ├── redirects/                    # redirects.csv → Cloudflare Bulk Redirects (anciens domaines) + _redirects (même domaine) + test HTTP
│   ├── checks/                       # Lighthouse CI, linkinator, pa11y, validation JSON-LD, test hreflang réciproques
│   └── eject/                        # export d'un site autonome pour un client qui part
└── .github/workflows/
    ├── ci.yml                        # build + checks de tous les sites touchés par le diff
    └── deploy.yml                    # déclenché par W11 (repository_dispatch) ou un push : build → wrangler deploy
```

### 5.2 `client.config.ts` (exemple Sabina)

```ts
export default defineClient({
  id: "sabina",
  brand: {
    name: "Sabinas Watersport Rhodos",
    legalName: "…",                       // raison sociale exacte, à collecter
    logo: "/logo.svg",
    theme: "aegean",                      // preset de thème, surchargé par theme.css
  },
  domains: {
    primary: "www.sabinas-watersport.com",
    legacy: ["catamaran-yachtsailing-rhodos.com", "dolphin-tours-rhodos.com"], // → Bulk Redirects
  },
  locales: { default: "en", enabled: ["en", "de", "fr"], planned: ["it", "pl"] },
  contact: {
    whatsapp: "+49…",                     // numéro réellement suivi
    phone: "+30…",
    email: "info@…",
    whatsappPrefill: { en: "Hi Sabina, I'm interested in {activity} on {date}", de: "…", fr: "…" },
    responseTime: { en: "within 2 hours, 8am–9pm", de: "…", fr: "…" },
  },
  location: {
    address: "Lardos 851 09, Rhodes, Greece",
    geo: { lat: 0, lng: 0 },              // point de RDV exact (ponton), à relever sur place
    timezone: "Europe/Athens",
    season: { from: "04-15", to: "10-31" },
  },
  booking: {
    mode: "request",                      // "request" (P1) | "saas" (P2) | "native" (P3)
    depositPercent: 30,
    currency: "EUR",
    stripeAccount: "acct_…",              // compte du client
    saas: null,                           // { provider: "bokun", widgetId: "…" } en P2
  },
  automation: {
    n8nBaseUrl: "https://flows.blueimpakt.xx",
    workflows: ["W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12"],
    weather: { provider: "met-norway", thresholds: { sailing: { windBft: 5 }, catamaran: { gustKt: 25 } } },
    reviewLinks: { google: "https://g.page/r/…/review", tripadvisor: "https://www.tripadvisor.com/…" },
  },
  social: { tripadvisor: "…", googleMaps: "…", instagram: "…", facebook: "…", youtube: "…" },
  analytics: { cloudflareWebAnalytics: true, consentRequired: false },  // passe à true si on ajoute des pixels Ads
  features: { chatbot: false, weatherBanner: true, reviewsWidget: true },
});
```

Tout ce qui est éditorial (textes, prix, photos, FAQ) va dans **Sanity**. Tout ce qui est structurel (domaines, langues, mode de booking, intégrations) va dans **`client.config.ts`**. L'opérateur ne touche jamais au second.

### 5.3 Schéma de contenu (Sanity)

Convention : `i18nString` / `i18nText` / `i18nBlock` = objet `{ en, de, fr, it?, pl? }`. **Les prix, durées, capacités et dates ne sont jamais localisés.**

**Activity**

| Champ | Type | Note |
|---|---|---|
| `title` | i18nString | requis |
| `slug` | `{ en, de, fr… }` slug | localisé, utilisé pour hreflang |
| `category` | enum `cruise \| private-boat \| sailing \| watersport \| snorkeling \| tour` | |
| `format` | enum `private \| shared \| both` | |
| `summary` | i18nText (≤ 160 car.) | carte + meta description par défaut |
| `body` | i18nBlock | |
| `heroImage` | image (hotspot) + `alt` i18n | requis |
| `gallery` | image[] + `alt` i18n | |
| `video` | `{ provider: youtube\|vimeo\|file, id, poster }` | facade |
| `duration` | `{ minutes, label i18n? }` | ex. 360 |
| `schedule` | `{ departures: ["10:30"], returnTime: "16:30", days: [1..7] }` | |
| `capacity` | `{ min, max }` | |
| `boat` | ref → Boat | optionnel |
| `meetingPoint` | ref → Location | requis |
| `priceOptions` | PriceOption[] | voir ci-dessous |
| `included` / `notIncluded` | i18nString[] | |
| `itinerary` | `{ time?, title i18n, description i18n, location? }[]` | |
| `requirements` | i18nText | âge, natation, permis |
| `cancellationPolicy` | ref → Page ou i18nText | météo, no-show |
| `faqs` | ref → FAQ[] | |
| `seasonOverride` | `{ from, to }` | si différent de la saison globale |
| `status` | enum `active \| hidden \| soldOut \| suspended` | `suspended` = bandeau sur la fiche |
| `bookingRef` | `{ saasProductId? }` | P2 |
| `seo` | `{ title i18n?, description i18n?, ogImage? }` | |
| `order` | number | tri |

**PriceOption** (objet imbriqué)

| Champ | Type | Exemple |
|---|---|---|
| `label` | i18nString | « Jusqu'à 6 personnes » |
| `kind` | enum `private \| perPerson \| child \| extra` | |
| `unit` | enum `perBoat \| perPerson \| perHour \| perSession \| per10min` | |
| `amount` | number (EUR) | 1050 |
| `paxMin` / `paxMax` | number | 5 / 6 |
| `childAge` | `{ from, to }` | |
| `season` | enum `all \| low \| high` + `{ from, to }` | |
| `depositPercent` | number? | surcharge du défaut |
| `highlight` | boolean | « le plus choisi » |

**Boat** : `name`, `type` (catamaran, voilier, speedboat, RIB), `length`, `capacity`, `features` i18nString[], `images`, `licence?`, `crew` i18nText.

**Location** : `name` i18n, `kind` (meetingPoint, base, destination), `geo` {lat, lng}, `address`, `mapsUrl`, `photo`, `instructions` i18nText, `parking` i18nText.

**FAQ** : `question` i18nString, `answer` i18nBlock, `scope` (global | activity | booking | weather), `order`. C'est aussi la source du chatbot.

**Review** (avis collectés en propre via W6 + avis tiers mis en avant)

| Champ | Type | Note |
|---|---|---|
| `author` | string (prénom + initiale) | consentement à la publication |
| `country` | string | |
| `rating` | 1-5 | |
| `text` | string + `lang` | **non traduit** (authenticité), traduction à la volée optionnelle |
| `date` | date | |
| `activity` | ref → Activity | |
| `source` | enum `site \| google \| tripadvisor` | **seuls les avis `site` alimentent l'AggregateRating en JSON-LD** |
| `sourceUrl` | url | obligatoire si la source est tierce |
| `featured` | boolean | |

**Page** (accueil, à propos, contact, légal, landing SEO) : `title`, `slug` i18n, `sections[]` = blocs typés correspondant aux composants (Hero, ActivityGrid, Reviews…) avec leurs champs, `seo`.

**Settings** (singleton) : `weatherBanner` `{ active, message i18n, until }`, `closedDates` [{ from, to, activities? }], `announcement` i18n, `defaultOgImage`.

Garde-fous de saisie : validations Sanity (montant > 0, `paxMax ≥ paxMin`, `alt` requis dans la langue par défaut). Une vue Studio « **Prix** » liste toutes les PriceOptions de toutes les activités sur un seul écran mobile, éditables en ligne : c'est l'écran que l'opérateur utilisera 90 % du temps.

### 5.4 Composants de sections

| Composant | Rôle | Notes perf / UX |
|---|---|---|
| `Hero` | Titre, accroche, image ou MP4 court muet, CTA primaire (réserver) + secondaire (WhatsApp), badges avis | Image `fetchpriority=high`, pas de carrousel |
| `ActivityGrid` | Grille filtrable par catégorie | Filtres en CSS ou JS minimal |
| `ActivityCard` | Image, titre, durée, « à partir de X € », format privé/partagé, note | Prix « à partir de » calculé depuis les PriceOptions |
| `PriceTable` | Variantes par saison et tranche de pax, acompte affiché | Texte HTML, jamais d'image ; mobile = cartes empilées |
| `Itinerary` | Timeline horaire | |
| `Included` | Inclus / non inclus (icônes) | |
| `BookingCTA` | Barre **sticky en bas sur mobile** : prix « à partir de » + « Réserver » + icône WhatsApp | Switch `request \| saas \| native`, safe-area iOS |
| `RequestForm` | Formulaire P1 avec estimation de prix | Validation côté client et serveur, Turnstile, < 10 Ko JS |
| `Reviews` | Avis mis en avant + badges Google/TripAdvisor + note moyenne | Schema uniquement sur les avis `site` |
| `Gallery` | Grille + lightbox | Lazy-load, lightbox chargée au clic |
| `FAQ` | Accordéon `<details>` | 0 JS |
| `MeetingPoint` | Carte statique (image) + boutons Google/Apple Maps + photo + instructions | Pas d'iframe Maps, donc pas de consentement à demander |
| `WhatsAppFloat` | Bouton flottant, message pré-rempli contextuel | Masqué quand `BookingCTA` sticky est visible (un seul CTA flottant) |
| `WeatherBanner` | Bandeau global « opérations suspendues » | Piloté par Settings ou W9 |
| `TrustBar` | Années d'expérience, licence, nombre d'avis | |
| `LangSwitcher` | Conserve la page courante via les slugs localisés | |
| `CTABoth` | Bloc final de page : réserver / poser une question | |

### 5.5 Thèmes

- Tokens CSS (`--color-primary`, `--color-accent`, `--color-surface`, `--radius`, `--font-display`, `--font-body`, `--space-*`) dans `tokens.css`.
- 4 presets : `aegean` (bleu profond + blanc), `lagoon` (turquoise + sable), `sunset` (corail + nuit), `sand` (neutre chaud). Le site client choisit un preset et surcharge 3 à 6 variables dans `theme.css`.
- Typo : 2 familles maximum, auto-hébergées, `font-display: swap`, sous-ensemble `latin` + `latin-ext` (nécessaire pour PL, CZ, TR).
- Contrastes vérifiés automatiquement en CI (AA).

### 5.6 Pipeline de déploiement d'un nouveau client

**Pré-requis bloquant** : le chrono démarre quand le **kit contenu** est complet : questionnaire rempli, photos HD (≥ 15), liste des activités et prix, accès registrar/DNS, Google Business Profile, compte Stripe vérifié au nom du client. Sans ce kit, pas de date de livraison : c'est la première cause de dérapage.

| Jour | Étapes | Livrable |
|---|---|---|
| **J0** (avant, 1-2 h) | Kick-off 45 min · questionnaire (Tally) · crawl de l'ancien site (`tooling/migrate crawl`) · inventaire des URLs → `redirects.csv` brut | Kit contenu validé |
| **J1** | `pnpm create-site <client>` : scaffold, projet Sanity, projet Cloudflare, secrets · choix du thème et des tokens · `tooling/migrate extract` : LLM → JSON validé → import Sanity (activités, prix, FAQ) · revue humaine des prix (contrôle 1:1 avec la grille fournie par le client) | Site de staging alimenté avec le vrai contenu |
| **J2** | Assemblage des pages (accueil, activités, à propos, contact, légal) · rédaction et réécriture de la langue source · traduction IA vers les autres langues → brouillons Sanity · envoi aux relecteurs natifs (client ou freelance) | Staging complet en langue source, traductions en relecture |
| **J3** | Booking P1 : import des workflows W1-W12 (`n8n-templates import --client`), credentials (Stripe, Google Calendar, email), test de bout en bout (demande → confirmation → paiement test → .ics → J-1 simulé → avis) · bandeau météo · formulaire | Parcours de réservation testé en mode test Stripe |
| **J4** | SEO : JSON-LD validé, hreflang réciproques, sitemaps, `redirects.csv` finalisé et testé (`tooling/redirects test` = 100 % des anciennes URLs en 301 vers une page 200) · checks Lighthouse, a11y, liens · RGPD (pages légales, registre) · intégration des retours de relecture | Staging « release candidate », rapport des checks |
| **J5** | Formation client 30-45 min (visio + vidéo Loom de 5 min « changer un prix / activer le bandeau météo » + fiche A4 dans sa langue) · bascule DNS · Bulk Redirects des anciens domaines · Search Console (propriété domaine + sitemaps + changement d'adresse pour les anciens domaines) · Google Business Profile (URL, catégories, horaires saisonniers) · Stripe en mode live | **Mise en ligne** |
| J+7 / J+30 / J+90 | Search Console (couverture, 404, hreflang) · logs 404 → compléter les redirections · premier rapport W12 · point client | Rapport post-lancement |

Durée cible : **5 jours ouvrés de production Melvin**, livrés en **2 à 3 semaines calendaires** (attente de relecture, DNS, validations client).

**Règle d'industrialisation** : ne pas construire le boilerplate « en chambre ». Sabina est construite **dans la forme** du monorepo (core, config, schémas), mais on n'extrait et ne généralise un composant qu'au moment où le **2e client** en a besoin (règle de trois). Budget réaliste : Sabina 10-15 jours (boilerplate v1 inclus), client 2 ~7 jours, client 3 et suivants ~5 jours.

**Calendrier commercial du secteur** : on construit entre octobre et février et on met en ligne **au plus tard fin février**, pour laisser à Google 6 à 8 semaines de recrawl avant les réservations d'été. Pour Sabina, à date (21/10/2026), une mise en ligne mi-janvier 2027 est la cible. On ne migre **jamais** un site en pleine saison (juin-septembre).

---

## 6. Modèle économique pour Melvin

### 6.1 Packs

| | **Essentiel** | **Pro** (cible Sabina) | **Premium** |
|---|---|---|---|
| Site | Astro + Sanity, ≤ 8 activités, 3 langues, thème preset | ≤ 15 activités, 3 langues + 2 en option | Illimité, 5 langues |
| Migration SEO | 301 + Search Console | idem + consolidation multi-domaines | idem |
| Booking | Demande simple (W1) + WhatsApp | **Palier 1 complet** (W1-W12) : acompte Stripe, J-1, météo, avis, rapport hebdo | Palier 1 **ou** intégration du SaaS (P2) + OTA/Google Things to do |
| IA | Traduction initiale | Traduction initiale + traduction des mises à jour | + chatbot FAQ + brouillons de réponses aux avis |
| Google Business Profile | Mise à jour | Optimisation complète | + suivi mensuel |
| **Setup** | **1 800 – 2 500 €** | **3 500 – 4 800 €** | **5 500 – 8 000 €** |
| **Mensuel** | **39 – 49 €** (hébergement, maintenance, sauvegardes, petites modifs ≤ 30 min/mois) | **89 – 129 €** (+ exploitation des automatisations, rapport hebdo, 1 h de modifs/mois) | **179 – 249 €** (+ chatbot, suivi SEO, 2 contenus saisonniers, revue de saison) |

**Options** : langue supplémentaire 250-400 € (IA + relecture native) · nouvelle activité au-delà du forfait 80-150 € · shooting photo/drone via un partenaire local (refacturé) · campagne Google Ads saisonnière (forfait + budget pub du client).

**Fourchettes, pas des prix fixes** : le marché grec local est moins cher (sites à 800-2 000 € chez les agences locales). On vise les opérateurs à **ticket moyen élevé** (privés, catamaran, > 80 € par personne) et à clientèle internationale, pour qui l'argument est le ROI : un seul daytrip privé de plus par saison (950-1 150 € chez Sabina) paie le mensuel Pro de l'année. Un no-show évité grâce à l'acompte (~300 €) paie 3 mois.

### 6.2 Ce qui est récurrent (et pourquoi le client paie)

1. **Infra et maintenance** : quasi nul en coût réel (3-10 €/mois), forte valeur perçue (« le site ne tombe jamais, je ne m'en occupe pas »).
2. **Automatisations exploitées** : c'est le cœur du récurrent. Elles tournent sur l'infra de Melvin, et si le client arrête de payer, elles s'arrêtent. C'est le *lock-in* légitime, celui de la valeur rendue (le site, lui, reste au client).
3. **Rapport hebdo W12** : rend la valeur visible chaque lundi, c'est un anti-résiliation.
4. **Revue de saison** (Premium, octobre) : bilan, nouveaux prix, nouvelles activités. C'est aussi le moment de l'upsell P1 → P2 ou d'une langue en plus.

### 6.3 Saisonnalité côté Melvin

- Les ventes de setup se concentrent d'**octobre à février**. L'été rapporte du récurrent et du support.
- Le client facturé au mois paie aussi l'hiver, quand il n'encaisse rien. Deux options : prélèvement SEPA mensuel 12/12, ou **annuel payé en octobre** (fin de saison, trésorerie pleine) avec -10 à -15 %. Éviter la facturation « saison seulement » : elle fait fondre le revenu récurrent de Melvin.
- Pas de commission sur les réservations : c'est un argument commercial face à FareHarbor (jusqu'à 6 % payés par le client final) et cohérent avec la ligne Blue Impakt / KM0. Melvin ne doit jamais encaisser les fonds des clients.

### 6.4 Projection indicative

Avec 8 clients Pro en 2 ans : setup ≈ 30-38 k€ (non récurrent), récurrent ≈ 8 × ~110 € × 12 ≈ **10,5 k€/an** pour ~5 h/mois de maintenance mutualisée. Coûts infra ≈ 600 €/an. Le récurrent ne devient significatif qu'à partir de 10-15 clients : le setup reste le revenu principal les 2 premières années.

**Sabina, client zéro** : proposer le pack Pro à prix pilote (-25 à -30 %) en échange d'un témoignage vidéo, d'une étude de cas chiffrée publiable (avant/après : performance, demandes, taux d'acompte) et d'introductions auprès d'autres opérateurs de la côte Est (Lindos, Pefkos, Kiotari).

---

## 7. Risques et anti-patterns

### 7.1 Dépendance à un SaaS commissionné

- **Risque** : le SaaS augmente ses frais, change ses conditions, ou détient la relation client (emails, avis, données). Sur FareHarbor, les frais payés par le client final rendent le prix affiché trompeur au checkout.
- **Parade** : les données clients et les workflows de relation (J-1, avis, relances) restent dans la couche n8n de Blue Impakt (exports réguliers). Le site appelle le SaaS via `BookingCTA` uniquement, ce qui permet de changer de SaaS sans refaire le site. Toujours lire la clause de résiliation et de portabilité des données avant de signer.

### 7.2 Le client ne met pas à jour

- **Risque** : prix 2026 affichés en 2027, activités arrêtées toujours en ligne, d'où des litiges et une perte de confiance.
- **Parades** :
  - un champ `validUntil` sur les grilles de prix. Si la date est dépassée, n8n relance le client 30 jours avant le début de saison et le site affiche « prix sur demande » plutôt qu'un prix périmé ;
  - la vue Studio « Prix » sur un seul écran ;
  - un rappel annuel automatique « vérifiez vos prix 2027 » en février ;
  - la revue de saison dans le pack Premium.

### 7.3 Saisonnalité

- **Côté client** : pas de budget en hiver, pas de temps en été. On vend et on livre d'octobre à février, on ne touche à rien en production de juin à septembre (gel des déploiements non urgents), et les mises à jour du `core` se déploient en basse saison.
- **Côté Melvin** : un support d'été réactif sur le chemin critique (formulaire, paiement), avec monitoring uptime et alertes Telegram. Pour tout le reste, une réponse sous 48 h.

### 7.4 Migration SEO des 3 domaines Jimdo

| Risque | Parade |
|---|---|
| Domaines enregistrés **chez Jimdo** (inclus dans les packs) : la résiliation du pack peut faire perdre le domaine | **Avant toute chose**, vérifier qui est le registrar, demander les codes de transfert (auth codes) et transférer vers Cloudflare Registrar ou le registrar du client. Ne résilier les packs Jimdo **qu'après** le transfert effectif. Les retours d'utilisateurs signalent des délais pour obtenir les codes : anticiper de 2 à 4 semaines |
| **Emails hébergés chez Jimdo** sur ces domaines : coupure au transfert | Inventorier les boîtes mail (`info@…`) et migrer les MX (Google Workspace, Zoho, ou l'hébergeur du client) avant de toucher au DNS |
| 301 vers la home = perte du positionnement des pages profondes | Mapping **page à page** dans `redirects.csv` (~45 URLs) + test automatisé. Cloudflare Bulk Redirects (Free : 10 000 redirections, 5 listes, 15 règles par compte) |
| URLs encodées (`%C3%BCber-uns`, `demande-de-r%C3%A9servation`) | Tester les deux formes (encodée et décodée) |
| Anciens domaines non renouvelés dans 1 an = 301 perdues | Renouvellement automatique sur 2 ans minimum, au nom du client |
| Perte temporaire de trafic | Normal sur 4 à 8 semaines. Mise en ligne en basse saison, « changement d'adresse » dans Search Console pour chaque ancien domaine, sitemaps des anciennes URLs soumis quelques semaines pour accélérer le recrawl des 301 |
| Avis TripAdvisor et fiches OTA pointant vers les anciens domaines | Mettre à jour les liens TripAdvisor, GBP, Facebook, Instagram et OTA le jour J (checklist) |

### 7.5 Anti-patterns à refuser

1. **Prix en images** : illisibles par Google et l'IA, à refaire à chaque saison, non traduisibles.
2. **Une copie de page par langue avec ses propres prix** : c'est la source n°1 d'incohérences. Le prix est une donnée, pas du texte.
3. **Bandeau cookies par réflexe**, alors qu'aucun cookie non essentiel n'est posé. Si on ajoute un pixel Ads/Meta plus tard, on active le module CMP (vanilla-cookieconsent, MIT) + Consent Mode v2, avec `consentRequired: true` dans la config.
4. **Iframes Google Maps et YouTube chargées par défaut** : poids, RGPD, LCP. On utilise une facade.
5. **Automatiser l'annulation météo** sans validation humaine : risque juridique et relationnel.
6. **Chatbot qui « confirme » une dispo ou invente un prix** : il est restreint à la FAQ et aux données Sanity, et il escalade.
7. **Moteur de booking maison au client n°1** : c'est 3 mois de développement pour un besoin qu'un formulaire intelligent couvre.
8. **Melvin propriétaire des comptes du client** (domaine, Stripe, GBP) : c'est un conflit le jour où le client part, et un risque si Melvin est indisponible. Le client est propriétaire, Melvin est invité en admin.
9. **Donner un accès n8n au client** : non conforme à la licence en mode mutualisé, et risque de casse.
10. **Généraliser avant le 2e client** : c'est de l'architecture astronaute.
11. **Review gating** (ne demander un avis qu'aux clients satisfaits) : interdit par Google.
12. **Baliser en JSON-LD des avis TripAdvisor/Google copiés** : contraire aux règles Google, risque d'action manuelle.

### 7.6 Points juridiques à faire valider (hors expertise de ce document)

- **Droit de rétractation** : les services de loisirs à date déterminée en sont exclus par la directive 2011/83/UE (art. 16, l). Les CGV doivent le dire clairement, et le bouton de rétractation (obligation UE récente, déjà visible sur le site Jimdo Dolphin) est à cadrer par un juriste selon le palier.
- **Mentions légales** d'une entreprise grecque dirigée par une Allemande : quelles obligations, grecques et éventuellement allemandes (Impressum) si elle cible le marché allemand ?
- **Acompte** : qualification (arrhes ou acompte) et règles de remboursement en cas d'annulation météo, à aligner avec la pratique actuelle de Sabina.
- **Facturation de Melvin** : prestation B2B intra-UE depuis une micro-entreprise française vers un client grec, avec les mentions TVA adaptées (à confirmer avec le comptable).

---

## 8. Décisions à prendre par Melvin (prochaines étapes)

1. Valider ADR-001 (domaine unique `sabinas-watersport.com`) avec Sabina, et **lancer immédiatement la vérification registrar et emails des 3 domaines Jimdo**.
2. Valider ADR-002 (Sanity) ou choisir Keystatic Cloud si Melvin préfère un contenu dans git.
3. Valider ADR-003 (monorepo) et le palier de départ de Sabina (P1 recommandé).
4. Envoyer le questionnaire et le kit contenu à Sabina. Date cible de mise en ligne : **mi-janvier 2027**.
5. Préparer la proposition commerciale Pro au prix pilote.

---

## Sources (consultées le 21/10/2026)

**Booking SaaS**
- Bókun, pricing officiel : https://www.bokun.io/pricing
- Rezdy, pricing officiel : https://www.rezdy.com/pricing/
- Checkfront, pricing officiel : https://www.checkfront.com/pricing/
- FareHarbor, frais *(tiers, page officielle en erreur)* : https://captainbook.io/blog/fareharbor-pricing-fees-explained · https://www.capterra.co.uk/software/135106/fareharbor · https://www.softwareadvice.com/appointment-scheduling/fareharbor-profile/
- Regiondo *(tiers, contradictoires)* : https://www.trekksoft.com/en/blog/regiondo-pricing-guide-what-to-know-before-you-buy · https://captainbook.io/vs/regiondo · https://www.g2.com/products/regiondo/pricing
- TuriTop *(tiers + page officielle partielle)* : https://www.trekksoft.com/en/blog/turitop-pricing-guide-what-to-know-before-you-buy · https://turitop.com/?p=15537 · https://us.fitgap.com/products/058557/turitop
- Google Things to do / Reserve with Google, partenaires : https://support.google.com/google-ads/answer/13189190 · https://arival.travel/as-reserve-with-google-grows-so-do-questions/

**Paiement et messagerie**
- Stripe, tarifs FR : https://stripe.com/fr/pricing
- WhatsApp Business Platform, pricing Meta : https://developers.facebook.com/docs/whatsapp/pricing
- Tarif Allemagne *(tiers, juillet 2026)* : https://chatmaxima.com/whatsapp-api-pricing/germany/ · https://whautomate.com/whatsapp-business-api-pricing-germany

**Automatisation et IA**
- n8n, pricing : https://n8n.io/pricing/
- n8n, FAQ de la Sustainable Use License : https://docs.n8n.io/n8n-community-license/community-license/license-faq
- Anthropic, tarifs API (référence interne Claude API, cache du 06/10/2026) : Haiku 5.5 à 0,10/0,50 $, Sonnet 5.5 à 2/10 $, Opus 5.5 à 4/20 $ par million de tokens (in/out)
- Open-Meteo, conditions : https://open-meteo.com/en/pricing
- Google Places API *(tiers + doc Google partielle)* : https://www.woosmap.com/blog/google-places-api-pricing · https://developers.google.com/maps/billing-and-pricing/pricing

**CMS**
- Sanity, pricing : https://www.sanity.io/pricing
- Keystatic Cloud : https://keystatic.com/docs/cloud · Keystatic GitHub mode : https://keystatic.com/docs/github-mode
- TinaCMS, pricing : https://tina.io/pricing
- Dépréciation de Netlify Identity / Git Gateway : https://github.com/decaporg/decap-cms/discussions/7419 · https://answers.netlify.com/t/alternative-to-netlify-identity-for-cms-access/151548

**Hébergement et infra**
- Cloudflare Pages, limites : https://developers.cloudflare.com/pages/platform/limits/
- Cloudflare Redirects, quotas : https://developers.cloudflare.com/rules/url-forwarding/
- Rachat d'Astro par Cloudflare (16/01/2026) : https://secure.businesswire.com/news/home/20260116386991/en/Cloudflare-Acquires-Astro-to-Accelerate-the-Future-of-High-Performance-Web-Development
- Hetzner Cloud : https://www.hetzner.com/cloud/
- Supabase, pricing : https://supabase.com/pricing
- Vercel, pricing : https://vercel.com/pricing

**Alternatives no-code et WordPress**
- Framer, pricing : https://www.framer.com/pricing
- Webflow *(tiers, page officielle non lisible)* : https://www.activepieces.com/blog/webflow-pricing-2026-plans-seats-and-real-costs · https://www.digidop.com/fr/blog/prix-webflow-site
- WPML *(tiers)* : https://nexterwp.com/blog/wpml-vs-polylang-vs-translatepress/

**Domaines**
- Transfert de domaine depuis Jimdo *(retours d'utilisateurs)* : https://community.ovhcloud.com/t/transfert-nom-de-domaine-depuis-jimdo/24151 · https://discourse.webflow.com/t/how-can-i-transfer-a-domain-from-jimdo-to-webflow/173413
