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
- 2026-09-02 : Bug remonté — mail de suivi colis Sendcloud n'arrivait pas au client. Diagnostic : compte Sendcloud gratuit, email personnalisé de l'expéditeur bloqué derrière l'offre Premium → mails de suivi partent depuis l'adresse générique Sendcloud, réputation moyenne, tombent en spam côté client (ce qui arrivait sur `contact@esprit-docker.com` était en fait la notif de compte, pas le mail client). Palliatif implémenté : message "vérifiez vos spams" ajouté dans l'email de confirmation de commande et la page de confirmation post-paiement. Commit+push `944dca9`.

## Liens
- Projets : [[esprit-docker-site]]
- Patterns utilisés : [[pipeline-assets-produit-ecommerce]]
