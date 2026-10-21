---
tags: [pattern, process, stack, boilerplate]
source: formation Millenium (17.01, 17.06, 17.09, 17.14) + discussions
---

# Stack création site web (boilerplate réutilisable avec Claude Code)

Pattern pour créer vite des sites avec fonctionnalités (comptes, réservation, paiement) en réutilisant le même socle d'un client à l'autre. Cas d'école discuté : site de réservation de sorties catamaran pour une entreprise grecque, clientèle internationale.

## Principe
Configurer une fois tous les modules (front, base, auth, paiement) sur un projet modèle, le sauvegarder comme template, puis le dupliquer pour chaque nouveau client au lieu de tout reconfigurer. Deux voies (leçon 17.06) : partir d'une boilerplate existante et l'adapter, ou construire la sienne. Une boilerplate ne fournit pas la logique métier : créneaux, dates, disponibilité par bateau restent à développer par-dessus.

Dans le prompt de départ de Claude Code, préciser la stack explicitement plutôt que de le laisser choisir.

## Stack

| Brique | Choix recommandé | Alternatives |
|---|---|---|
| Front | Next.js (React) + Tailwind CSS + TypeScript | Astro (sites peu interactifs), Remix |
| Base + back-end | Convex : temps réel natif, tout en TypeScript, utile contre le surbooking | Supabase, Neon (Postgres, pas de temps réel natif), Appwrite, PocketBase (gratuit, auto-hébergé), Firebase |
| Authentification | BetterAuth (préférence de la formation) | Clerk (20 $/mois pour 50 000 MAU, d'après la leçon) |
| Paiement | Polar.sh ou Stripe, voir ci-dessous | |
| Hébergement | Vercel ou Cloudflare Pages, voir ci-dessous | |
| Code | Git + GitHub, déploiement continu | |
| Nom de domaine | environ 10 à 15 €/an | Cloudflare Registrar (prix coûtant) |

## Paiement : Polar vs Stripe
- **Polar** = merchant of record : il vend à la place de l'entreprise, collecte et reverse la TVA locale, puis reverse le net par virements réguliers (léger délai). Utile pour une clientèle internationale sans comptable à l'aise avec le multi-pays. Plus cher : 4 % + 0,40 € selon la leçon 17.01. Une recherche web pendant la discussion suggère un passage à 5 % + 0,50 € début 2026 pour les nouveaux comptes : **à vérifier sur le site de Polar**.
- **Stripe** : 1,5 % + 0,25 € en Europe (leçon 17.01). L'entreprise reste vendeur officiel et gère sa TVA multi-pays elle-même. Pertinent si elle a déjà un comptable qui s'en charge ou si l'essentiel des ventes est en zone euro.
- Intégration (leçon 17.09) : fournir à Claude Code la documentation technique de l'outil (ex. `llmfull.txt` de Polar), préciser qu'il s'agit d'un compte de test, annulation d'abonnement effective en fin de cycle, changer tout token partagé en clair.

## Hébergement : Vercel vs Cloudflare Pages
- **Vercel** : intégration native avec Next.js, le plus simple à démarrer. Payant dès l'usage commercial : plan Pro à environ 20 $/mois/utilisateur (le plan gratuit exclut l'usage commercial). Bande passante facturée au-delà du quota.
- **Cloudflare Pages** : gratuit même en commercial, bande passante illimitée. Intégration Next.js un peu moins fluide (adaptateur parfois nécessaire, fonctionnalités serveur avancées à configurer).
- Tarifs issus de recherches web pendant la discussion : à revérifier avant de chiffrer un devis.

## Coûts Convex (à revérifier)
Gratuit jusqu'à 1 M d'appels de fonction et 500 Mo de stockage (jusqu'à 6 développeurs), puis environ 25 $/mois/développeur.

## Multi-clients
Le plus propre : un compte Convex par client, à son nom et avec sa propre facturation (comme le domaine et l'hébergement). Alternative : tout sous le compte agence et refacturation, avec plus de contrôle mais plus de responsabilité.

## Quand ce pattern est pertinent
Projets avec réservation en temps réel, comptes utilisateurs et paiement sécurisé. Pour un site vitrine simple sans compte ni paiement, Next.js + Tailwind suffisent.

## Liens
- Leçons : `formation-ia/1701-créer-sa-stack-technique`, `1706-comprendre-les-boilerplate`, `1709-intégration-des-paiements`, `1714-créer-la-landing-page`
- Boilerplates payantes citées : ShipFast (200 $), Super Starter, OpenSaaS

---

## Variante : site d'activités / tourisme (ajout du 2026-10-21)

Pour les opérateurs d'activités (excursions bateau, sports nautiques, tours guidés) : petites structures saisonnières, clientèle internationale sur mobile, gérant peu technophile. Le besoin principal est un **site de contenu qui convertit**, pas une application. La réservation monte en puissance par paliers. Variante issue du cas [[sabinas-watersport-refonte]] (comparatif complet : [[sabinas-06-comparatif-stack-pattern]]).

### Ce qui change par rapport à la stack principale

| Brique | Stack principale | Variante tourisme | Raison |
|---|---|---|---|
| Front | Next.js + Tailwind + TS | **Astro** + Tailwind + TS, îlots React pour le calendrier et le formulaire | Surtout du contenu multilingue lu en 4G : zéro JS par défaut |
| Édition par le client | — | **Sanity** (Studio utilisable sur mobile), ou Keystatic pour tout garder dans git | Le gérant change un prix ou une date depuis son téléphone, sans appeler l'agence |
| Base / back-end | Convex | Aucune au lancement ; **Convex** seulement pour le moteur maison (palier 3) | Tant que le gérant valide chaque demande, il n'y a pas de surbooking possible |
| Authentification | BetterAuth | Aucune côté visiteurs ; BetterAuth pour le back-office opérateur au palier 3 | Personne ne crée de compte pour une sortie en bateau |
| Paiement | Polar ou Stripe | **Stripe** au nom du client (Stripe Connect au palier 3, l'agence ne détient jamais les fonds) | Service physique vendu localement avec la TVA locale : le merchant of record de Polar, pensé pour le numérique, n'apporte rien, coûte plus cher, et surtout **la politique d'usage de Polar interdit les « Human services » et les « Travel Services »** (vérifié le 2026-10-21) : une excursion n'est pas éligible |
| Hébergement | Vercel ou Cloudflare Pages | **Cloudflare** (Pages, Workers, Turnstile, redirections, Registrar) | Gratuit en commercial ; redirections 301 des anciens domaines au même endroit |
| Automatisation | — | **n8n** auto-hébergé | Différenciateur Blue Impakt, justifie le mensuel |

### Réservation par paliers
1. **P1, demande structurée** (par défaut au lancement) : formulaire activité + date + personnes → Worker Cloudflare → n8n → le gérant valide d'un tap → lien d'acompte Stripe → confirmation. Zéro commission.
2. **P2, SaaS de booking intégré** (Bókun, Regiondo) : quand il faut un calendrier en libre-service, des places vendues à l'unité ou la synchronisation Viator/GetYourGuide.
3. **P3, moteur maison multi-clients** : Convex (inventaire de places en temps réel) + BetterAuth + Stripe Connect. À envisager seulement à partir de 8 à 10 clients dans le secteur.

### Briques spécifiques au secteur
- Multilingue avec `hreflang` (langues à choisir selon les nationalités de touristes de la destination), contenus saisis une fois et traduits.
- schema.org : `TouristTrip`, `Offer`, `LocalBusiness`, `FAQPage`, `AggregateRating`.
- Barre d'action collante sur mobile : WhatsApp (message pré-rempli), Appeler, Réserver.
- Note et avis Google/TripAdvisor affichés et visibles même si les cookies sont refusés.
- Conditions visibles avant la demande : acompte, annulation, météo, enfants.
- Workflows n8n : confirmation, rappel J-1 avec point de rendez-vous, alerte vent (le gérant valide avant envoi), demande d'avis J+1.
- Regroupement de domaines multiples : un seul site, redirections 301 page par page, transfert des domaines vers Cloudflare Registrar avant toute résiliation de l'ancien builder.

### Quand utiliser cette variante plutôt que la stack principale
Site vitrine + réservation d'activités, catalogue de moins de ~30 produits, pas de comptes clients. Dès qu'il faut des comptes, un espace membre ou de la réservation temps réel sur plusieurs opérateurs, on revient à la stack principale (Next.js + Convex + BetterAuth).
