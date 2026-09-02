---
tags: [client, actif, p2, artisanat, france]
created: 2026-08-29
statut: actif
priorite: p2
secteur: artisanat
localisation: france
---

# esprit-docker

## Relationnel
- **Contact** : Morgane Le Mouee — Entreprise Individuelle (micro-entrepreneur)
- **Activité** : Esprit Docker — chapellerie / site e-commerce de chapeaux (nom commercial "Esprit Docker", nom de code projet `esprit-chapellerie`)
- **Site** : [www.esprit-docker.com](https://www.esprit-docker.com)
- **Contact pro** : contact@esprit-docker.com

## Historique des échanges
-

## Décisions prises
-

## Besoins identifiés
- Site e-commerce Next.js pour vente de chapeaux, avec gestion avancée de variantes produit (photos par face/profil, motifs, détourage)

## Devis / propositions
-

## Next actions
- [ ]

## Journal
- 2026-08-29 : Repo identifié (`github.com/espritdocker/esprit-docker`), fiche client créée à partir des mentions légales/CGV du site
- 2026-08-30 : Repo local resynchronisé (5 commits récupérés depuis un autre PC — série hash PBKDF2 sur l'auth admin tentée puis revertée, retour à `ADMIN_PASSWORD` en Secret Cloudflare). Recommandation en attente : ajouter `.claude/settings.local.json` au `.gitignore`
- 2026-09-02 : Bug remonté — mail de suivi colis Sendcloud n'arrivait pas au client. Diagnostic initial (infirmé plus tard dans la journée, voir entrée suivante) : compte Sendcloud gratuit, email personnalisé de l'expéditeur bloqué derrière l'offre Premium → mails de suivi partent depuis l'adresse générique Sendcloud, réputation moyenne, tombent en spam côté client (ce qui arrivait sur `contact@esprit-docker.com` était en fait la notif de compte, pas le mail client). Palliatif implémenté malgré tout : message "vérifiez vos spams" ajouté dans l'email de confirmation de commande et la page de confirmation post-paiement. Commit+push `944dca9`.
- 2026-09-02 : Investigation approfondie du même bug (mail de suivi Sendcloud) reprise plus tard dans la journée — le diagnostic "spam" ci-dessus est **infirmé** : le client a bien reçu en inbox l'email "disponible en point relais", et ce mail vient en fait directement de **Mondial Relay**, pas de Sendcloud. Analytics Sendcloud confirme **0 email de suivi envoyé en 30 jours** (pas quelques échecs, un vrai zéro). Causes écartées une à une : toggle global ON, templates activés France + Autres pays, webhook actif (le 400 du 29/08 était un faux problème, déjà corrigé par le commit `cd5a79e` 10 min après coup). Reste une piste Sendcloud non vérifiée — permission "envoyer automatiquement les messages de suivi" au niveau de l'intégration API, jamais localisée dans le panel — à checker avant de basculer sur la solution de repli retenue : email "expédié" custom envoyé depuis le webhook Sendcloud via Brevo, verrouillé par une nouvelle colonne `commandes.suivi_email_envoye_at` (même pattern anti-doublon que `numero_facture` pour l'email de confirmation). Implémentation pas encore lancée, en attente de la vérif de la permission d'intégration.

## Liens
- Projets : [[esprit-docker-site]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
