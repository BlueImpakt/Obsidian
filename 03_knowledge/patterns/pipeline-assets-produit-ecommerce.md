---
tags: [pattern, code, validé]
created: 2026-08-29
type: code
---

# pipeline-assets-produit-ecommerce

## Contexte

E-commerce avec un catalogue à fortes variantes visuelles : un même produit
photographié sous plusieurs faces (face/profil), décliné en motifs et coloris.
Les photos brutes du client sont hétérogènes (résolutions, ombres, reflets,
fonds), et les retoucher une par une à la main ne passe pas à l'échelle.

Validé en production sur [[esprit-docker-site]] (chapellerie, ~dizaines de
variantes). Identifié dans la fiche projet comme *le vrai savoir-faire technique
du projet* — plus différenciant que le site lui-même.

## Comment ça marche

Un pipeline de scripts Node (`.mjs`) exécutés en local, pas un service tiers —
donc reproductible, versionné, et sans coût par image :

1. **Export / préparation** vers l'outil de détourage (Photoroom)
2. **Correction d'ombres et de reflets** — homogénéise des prises de vue faites
   dans des conditions différentes
3. **Feathering** des bords après détourage, pour éviter l'effet découpé
4. **Dédoublonnage de variantes** — détecte les visuels quasi-identiques qui
   gonflent le catalogue sans valeur ajoutée
5. **Audit de résolutions** — repère les images sous-dimensionnées avant qu'elles
   n'arrivent en production

Stockage final : Cloudflare R2 via client S3-compatible (`@aws-sdk/client-s3`).

## Code / config

```
Stack : Node (scripts .mjs autonomes, un par étape)
Détourage : Photoroom
Stockage : Cloudflare R2 (API S3-compatible)
```

Chaque étape est un script indépendant plutôt qu'un pipeline monolithique : on
peut rejouer une seule correction sur un lot sans tout retraiter.

## Quand le réutiliser

Bon choix : tout e-commerce où le client fournit ses propres photos produit et où
la cohérence visuelle du catalogue conditionne la conversion. Transposable
au-delà de la chapellerie (artisanat, mode, mobilier).

Argument commercial : c'est un livrable **réutilisable d'un client à l'autre**, à
valoriser comme tel plutôt que de le refacturer à zéro à chaque projet.

## Cas d'usage réels
- [[esprit-docker-site]] — catalogue chapeaux, variantes face/profil + motifs
