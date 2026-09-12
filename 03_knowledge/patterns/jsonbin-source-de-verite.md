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

## Sécurité — la clé JSONbin ne doit jamais vivre côté client

Sur un site "tout côté client, pas de backend", la clé JSONbin (et le mot de
passe éditeur) embarquée dans le HTML est visible en clair via "Afficher le code
source" — elle contourne même le mot de passe puisqu'on peut appeler l'API
JSONbin directement avec. Trouvé et corrigé sur [[naeco-carte]] (2026-09-11) :
architecture finale = **aucune** clé JSONbin côté client, lecture ET écriture
routées via un petit proxy Cloudflare Worker qui seul détient les secrets
(`wrangler secret put`). Piège rencontré en route : une clé JSONbin "restreinte
en lecture seule" créée via leur dashboard s'est révélée rejetée par un bug de
l'API JSONbin elle-même — ne pas supposer qu'une clé restreinte fonctionnera
comme documenté, tester l'appel réel avant de bâtir l'architecture autour.
Détails techniques : `03_knowledge/troubleshooting.md`.

**À appliquer dès le prochain projet JSONbin-côté-client** (dont [[naeco-site]]
si son éditeur venait à évoluer) : ne jamais laisser la clé JSONbin dans le HTML
servi, prévoir le proxy Worker dès la conception plutôt qu'en correctif après coup.

## Risque — la règle "patcher, jamais pousser l'état complet" doit être vérifiée dans le code, pas juste documentée

Sur [[naeco-carte]] (2026-09-11), une escale a été perdue parce que `jbSet()` poussait
tout le tableau local à chaque sauvegarde au lieu de patcher les champs modifiés —
alors que cette règle est actée plus haut dans ce document depuis la création du
pattern. Combinée à la race condition de chargement (fetch distant asynchrone), un
device au `localStorage` périmé a écrasé une donnée récente côté JSONbin, sans
retour arrière possible (bin sans versioning). Détails : `03_knowledge/troubleshooting.md`.
À vérifier systématiquement en revue de code sur tout projet utilisant ce pattern :
la fonction de sauvegarde patche-t-elle vraiment champ par champ, ou pousse-t-elle
l'état local complet ? Et le versioning du BaaS est-il activé ?

## Quand le réutiliser

Bon choix : site vitrine / carte / page de contenu, client qui veut de l'autonomie
éditoriale, pas de budget CMS, contenu structuré mais peu volumineux.

Mauvais choix : contenu volumineux, multi-utilisateurs concurrents, besoin
d'historique de versions ou de workflow de validation → prendre un vrai CMS
headless.

## Cas d'usage réels
- [[naeco-site]] — contenu éditable par l'équipe (textes, images, couleurs)
- [[naeco-carte]] — expéditions, observations, données Pelagos, escales, sites d'étude
