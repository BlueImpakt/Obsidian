---
tags: [project-doc, sabinas-watersport]
created: 2026-10-21
projet: sabinas-watersport-refonte
source: GitHub/sabina-watersport-refonte/docs/05-synthese.md
---

↩ [[sabinas-watersport-refonte]]

# Synthèse — refonte Sabinas Watersport Rhodos

21/10/2026. Sources : docs 00 à 04 + assets-inventaire.

## Le client en une phrase
Sabina (Sabine Kuehl) et Roland, Allemands installés à Stafilia Beach (Lardos, Rhodes) depuis 2007. Ils tiennent un centre nautique, et depuis 2023 une société de croisières (catamaran Lavezzi 40 « THOI », voilier, speedboat). Leur réputation est excellente (Google 5,0/479, TripAdvisor 4,9/443, n° 1 à Lardos, chiffres à reconfirmer), mais leur web est éclaté et ne convertit pas.

## Le problème
- **3 domaines Jimdo**, nés en 2007, 2017 et 2022, au fil des nouvelles activités. Aucun n'a le catalogue complet. Tout est mis à jour à la main une fois par an (janvier-février), en 3 langues sur 3 sites.
- **Réservation** : formulaire libre à 4 champs (pas de date, d'activité ni de nombre de personnes), acompte PayPal fixe de 150 €, aucune condition écrite (annulation, météo, enfants).
- **La note et les avis** ne sont affichés nulle part.
- **Aucun contact cliquable** (appel, WhatsApp) sur mobile.
- **Prix en direct** : catamaran privé 950 € contre environ 1 250 € sur Viator. Les sites ne présentent pas cet écart comme un avantage.
- **Légal** : mentions incomplètes (pas d'AFM/GEMI), « droit de rétractation » inadapté, e-mail web.de personnel.

## La réponse
1. **Un seul site**, sabinas-watersport.com (le nom qui porte les avis), avec deux univers : *Boat trips* et *Watersports*. Les 2 autres domaines sont redirigés page par page. dolphin-tours-rhodos.com expire le **01/12/2026** : le renouveler pour garder la redirection.
2. **Langues** : EN + DE d'abord (45 % des touristes de Rhodes), puis IT + PL. FR en option.
3. **Stack** (doc 04) : Astro + Sanity (prix modifiables depuis le téléphone) + Cloudflare + n8n + Stripe. Infra 3 à 10 €/mois.
4. **Réservation P1** : demande structurée (activité, date, personnes) → n8n → Sabina valide d'un tap → lien d'acompte Stripe → confirmation, rappel J-1, alerte vent, demande d'avis J+1. Passage à Bókun (P2) si elle veut un calendrier en libre-service ou la synchronisation Viator.
5. **Offre** : pack Pro 3 500 à 4 800 € + 89 à 129 €/mois, en prix pilote contre une étude de cas. Mise en ligne cible mi-janvier 2027, avant la saison.

## Ce que la maquette doit prouver (doc 03)
Premier écran clair en 5 secondes (bateau, « privé · Lindos · depuis 2007 », note et nombre d'avis, 2 CTA) · barre collante WhatsApp / Appeler / Réserver · cartes produit avec prix en texte · fiche activité au gabarit fixe · réservation en 3 étapes avec prix calculé · conditions visibles · bloc « Sabina & Roland » · encart « pourquoi réserver en direct ».

## À valider avec Sabina
Statut juridique et licences · gestion actuelle de Viator · originaux des photos drone · nationalités réelles des clients · envie ou non d'une offre partagée (sunset, snorkeling) pour capter les familles et les 25–35 ans.
