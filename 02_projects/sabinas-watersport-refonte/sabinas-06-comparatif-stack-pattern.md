---
tags: [project-doc, sabinas-watersport]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: GitHub/sabina-watersport-refonte/docs/06-comparatif-stack-pattern.md
---

↩ [[sabinas-watersport-refonte]]

# Comparatif : stack des agents (doc 04) vs pattern [[stack-creation-site-web]]

21/10/2026. Le pattern du vault a été écrit pour le même cas d'école (« réservation de sorties catamaran pour une entreprise grecque »). Il est **orienté application** : comptes, réservation temps réel, paiement. Le doc 04 est **orienté site de contenu qui convertit**, avec une réservation qui monte en puissance par paliers.

## Brique par brique

| Brique | Pattern vault | Doc 04 (agents) | Verdict pour Sabina et le secteur |
|---|---|---|---|
| Front | Next.js + Tailwind + TS | Astro | **Astro + Tailwind + TS**, avec des îlots React pour les parties interactives (calendrier, formulaire). 95 % du site est du contenu multilingue lu en 4G : Astro envoie zéro JS par défaut. Le pattern le dit lui-même (« Astro pour sites peu interactifs »). On garde Tailwind, TypeScript et React. |
| Édition par le client | **absent** | Sanity (Studio sur mobile) | **Le trou du pattern.** Sabina doit changer un prix depuis son téléphone sans appeler Melvin. Sans CMS, il faut coder une interface d'admin. Sanity (ou Keystatic si on veut tout dans git). |
| Base / back-end | Convex (temps réel, anti-surbooking) | Rien en P1 ; Supabase en P3 | **Convex en P3, à la place de Supabase.** En P1, Sabina valide chaque demande à la main : pas de risque de surbooking, donc pas besoin de base. Le temps réel compte seulement quand on vend des places en libre-service (semi-privé 8 places, voilier partagé 6). Convex le fait nativement, Supabase non : le pattern a raison sur ce point. |
| Authentification | BetterAuth | Aucune (Sanity gère l'accès admin) | **Pas d'auth côté touristes** : personne ne crée de compte pour une sortie en bateau. BetterAuth sert seulement au back-office opérateur en P3. |
| Paiement | Polar (merchant of record) ou Stripe | Stripe (compte au nom du client), Stripe Connect en P3 | **Stripe.** Polar est fait pour les produits numériques (SaaS, téléchargements). Une excursion en bateau est un service physique vendu en Grèce avec la TVA grecque : le modèle merchant of record n'apporte rien et coûte plus cher (4 à 5 % + 0,40 à 0,50 € contre 1,5 % + 0,25 €). Éligibilité de Polar à vérifier, mais à écarter par défaut. |
| Hébergement | Vercel ou Cloudflare Pages | Cloudflare (Pages + Workers + Turnstile + redirections) | **Cloudflare.** Accord. Vercel Hobby interdit l'usage commercial, et Pro coûte 20 $/mois. |
| Domaine | Cloudflare Registrar | Regroupement + 301 | **Cloudflare Registrar.** Transférer les 3 domaines de Sabina (aujourd'hui chez InterNetX/Jimdo) et y gérer les redirections 301. |
| Automatisation | absent | n8n auto-hébergé (confirmation, J-1, alerte vent, avis J+1) | **n8n.** C'est le différenciateur Blue Impakt et la justification du mensuel. Le pattern ne le prévoit pas. |
| Booking SaaS | absent | Bókun (P2) | Option utile si l'opérateur veut synchroniser Viator ou GetYourGuide sans tout recoder. |
| Spécifique secteur | absent | i18n + hreflang, schema.org (TouristTrip, Offer), WhatsApp, avis, multi-domaines | À ajouter au pattern pour la variante « opérateur d'activités ». |

## Stack retenue (synthèse des deux)

- **Socle (tous les clients du secteur)** : Astro + Tailwind + TypeScript (îlots React) · Sanity · Cloudflare (Pages, Workers, Registrar, Turnstile) · n8n · Stripe au nom du client.
- **Réservation P1 (Sabina au lancement)** : formulaire structuré → Worker → n8n → Sabina valide → lien d'acompte Stripe.
- **Réservation P2** : Bókun intégré si un calendrier en libre-service ou la synchro OTA est nécessaire.
- **Réservation P3 (moteur maison, multi-clients)** : **Convex** (inventaire de places en temps réel) + BetterAuth (back-office opérateur) + Stripe Connect. Cela remplace Supabase dans le doc 04.

## Ce que ça change dans le pattern
Le pattern reste valable pour une **application** (comptes, temps réel). Il lui manque une **variante « site d'activités / tourisme »** : CMS client, multilingue, automatisations n8n, réservation par paliers, Stripe plutôt que Polar pour des services physiques.
