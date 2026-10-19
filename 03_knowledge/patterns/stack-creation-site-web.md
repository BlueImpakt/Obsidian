---
tags: [pattern, process, validé]
created: 2026-10-15
type: process
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
