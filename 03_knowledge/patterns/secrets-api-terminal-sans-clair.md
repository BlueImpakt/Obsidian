---
tags: [pattern, securite, validé]
created: 2026-09-23
type: securite
---

# secrets-api-terminal-sans-clair

## Contexte

Donner à Claude Code un accès API (clé + secret) pour qu'il puisse gérer un
service (ex. supprimer / déplacer des médias Cloudinary) **sans jamais coller
le secret dans le chat** : tout ce qui est tapé dans la conversation est
stocké dans le transcript de session et envoyé au modèle.

Principe : l'utilisateur saisit le secret dans **son propre terminal**, il est
écrit dans un fichier local **hors de tout repo**, et les scripts le lisent
depuis ce fichier. Claude n'affiche, ne copie ni ne commite jamais les valeurs.

## Comment ça marche

1. **Créer une clé dédiée** dans le dashboard du service (ex. Cloudinary →
   Settings → API Keys → Generate New). Une clé dédiée se révoque d'un clic sans
   rien casser d'autre. Donner le rôle le plus étroit possible (ou "master" si
   c'est un usage ponctuel et que la clé sera révoquée ensuite).
2. **Écrire le fichier depuis PowerShell** (pas dans le chat) : `Read-Host`
   pose les questions une par une, la saisie ne passe pas par l'historique du
   chat. Coller UNIQUEMENT la valeur demandée à chaque invite.
3. **Fichier hors repo** : `~/.claude/cloudinary.env` (jamais dans un dossier
   versionné, donc jamais commité).
4. **Vérifier sans lire** : Claude contrôle seulement les noms de variables et
   les longueurs de valeurs (ex. clé Cloudinary = 15 chiffres, secret = 27
   caractères), jamais le contenu.
5. **Les scripts lisent le fichier** (`os.environ.setdefault` depuis
   `~/.claude/cloudinary.env`) et tournent en **simulation par défaut** ; les
   actions destructrices exigent un flag explicite (`--yes`) ET une
   confirmation de l'utilisateur dans le chat.

## Code / config

Création du fichier (PowerShell, UTF-8 sans BOM) :
```powershell
$k = Read-Host "api key"; $s = Read-Host "api secret"
[IO.File]::WriteAllText("$env:USERPROFILE\.claude\cloudinary.env", "CLOUDINARY_API_KEY=$k`nCLOUDINARY_API_SECRET=$s`n")
```

Vérification sans afficher les valeurs (bash) :
```bash
awk '{ sub(/\r$/,""); i=index($0,"="); printf "ligne %d: nom=%s, longueur_valeur=%d, numerique=%s\n", NR, substr($0,1,i-1), length($0)-i, (substr($0,i+1) ~ /^[0-9]+$/?"oui":"non") }' ~/.claude/cloudinary.env
```

Chargement côté script (Python) :
```python
ENV_FILE = os.path.expanduser("~/.claude/cloudinary.env")
if os.path.exists(ENV_FILE):
    for line in open(ENV_FILE, encoding="utf-8"):
        if "=" in line:
            k, v = line.strip().split("=", 1)
            os.environ.setdefault(k, v)
```

### Pièges rencontrés
- **Coller la mauvaise chose à l'invite** : la 1re tentative avait une "clé" de
  119 caractères non numériques (texte collé en trop). La vérification par
  longueur/format l'a détecté avant tout appel API.
- **Format inattendu du fichier** : un premier fichier n'avait pas les noms
  `CLOUDINARY_API_*` (2 lignes, première commençant par des chiffres) — signe
  d'une commande mal collée. Recréer le fichier plutôt que deviner.
- **Confondre Cloudinary et Cloudflare** : deux services différents (médias vs
  Workers/D1/R2), deux dashboards, deux jeux de clés.
- **Upload non signé ≠ gestion** : avec juste le `cloud name` + un preset non
  signé on peut uploader et ranger en dossiers (le dossier = chemin du
  `public_id`), mais pas supprimer/renommer — il faut une requête signée
  (clé + secret) ou l'Admin API en auth basique.
- Ne pas afficher la sortie brute des scripts si elle peut contenir des
  identifiants ; masquer avec `sed` en cas de doute.

## Cas d'usage réels
- [[naeco-carte]] — nettoyage des doublons orphelins Cloudinary
  (`rorqual/drone/`, `rorqual/souffle/`) après réorganisation en
  `rorqual/short/` et `rorqual/long/`.
