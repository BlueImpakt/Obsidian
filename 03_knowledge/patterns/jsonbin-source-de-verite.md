---
tags: [pattern, workflow, validé]
created: 2026-08-29
type: workflow
---

# jsonbin-source-de-verite

## Contexte

Un client non-technique doit pouvoir modifier le contenu de son site (textes,
images, liens, couleurs, données) sans toucher au code ni passer par toi à chaque
virgule. Le site est statique (HTML/JSON, pas de CMS, pas de back-end à maintenir),
et le budget ne justifie pas un vrai CMS headless.

Validé en production sur [[naeco-site]] et [[naeco-carte]].

## Comment ça marche

Le contenu vit dans un bin **JSONbin** (privé), pas dans le repo. Le site le lit au
chargement. Un éditeur en ligne intégré (raccourci clavier, protégé par mot de
passe) permet à l'équipe client de modifier en direct — les changements sont
poussés vers JSONbin avec un debounce (~600 ms).

Conséquence structurante : **le repo n'est plus la source de vérité du contenu.**
D'où des garde-fous non négociables, sans lesquels on écrase le travail du client :

- **Toujours lire JSONbin avant toute modification de contenu** — jamais écraser
  depuis le HTML local, qui est potentiellement périmé de plusieurs jours
- **Patcher uniquement les champs modifiés** — ne jamais pousser l'objet complet
- **Ne jamais régénérer les données structurées depuis le code** (ex. les `coords`
  des tracés d'expédition) — les récupérer telles quelles depuis le bin
- **Un script de récupération d'état en début de session** (`check-remote.sh`) pour
  synchroniser avant de travailler
- **Ne jamais `git push` sans instruction explicite du client** — le déploiement
  est une décision, pas une conséquence automatique

## Code / config

```bash
# Début de session obligatoire : récupérer l'état réel du contenu
./check-remote.sh
```

Bins séparés par surface fonctionnelle (un pour le site, un pour la carte) plutôt
qu'un bin monolithique : limite le rayon d'impact d'un écrasement accidentel.

⚠️ Les clés JSONbin et mots de passe éditeur ne sont **jamais** recopiés dans ce
vault — ils vivent dans le gestionnaire de secrets du client.

## Quand le réutiliser

Bon choix : site vitrine / carte / page de contenu, client qui veut de l'autonomie
éditoriale, pas de budget CMS, contenu structuré mais peu volumineux.

Mauvais choix : contenu volumineux, multi-utilisateurs concurrents, besoin
d'historique de versions ou de workflow de validation → prendre un vrai CMS
headless.

## Cas d'usage réels
- [[naeco-site]] — contenu éditable par l'équipe (textes, images, couleurs)
- [[naeco-carte]] — expéditions, observations, données Pelagos, escales, sites d'étude
