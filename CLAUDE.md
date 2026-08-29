
# Constitution Claude - Blue Impakt

## Qui je suis
- **Melvin Perrottet**, founder Blue Impakt
- **Activité principale (ce que fait Blue Impakt)** : service/agence — automatisation IA (agents, n8n), dev web/no-code, consulting — pour associations environnementales et entreprises à impact (voir `02_projects/site-blue-impakt/`). C'est le cœur du business, ça ne change pas.
- **KM0** : un projet mené **en parallèle** par Blue Impakt (produit propre, plateforme circuit court — producteurs locaux ↔ consommateurs, 0% commission), pas l'activité principale. Voir `02_projects/km0-circuit-court/`. Ne pas mélanger les deux dans les fiches : KM0 a son propre statut de projet, indépendant de l'activité de service.
- Background : formation Millenium (agents IA, automatisation, no-code, prospection) → crédibilité technique en cours de construction
- Auto-entrepreneur / micro-entreprise
- Side project : formation Millenium elle-même (pipeline RAG d'enrichissement de contenu pédagogique) → strictement séparé des clients/produits Blue Impakt, voir `04_personal/`

---

## Comment j'écris

### Ton & style
- **Direct, concis, expert-level** — zéro bullshit
- **Langue** : Français (défaut), Anglais (tech/code uniquement)
- **Voix** : "je" (perso), "nous" (Blue Impakt)
- **Longueur** : court et dense, pas de blabla

### Formules interdites
- Générique corporate speak
- Promesses creuses ("révolutionner", "transformer", "disrupter")
- Jargon marketing vide

### Brand voice Blue Impakt
**"L'IA au service de l'environnement et de l'humain"**
→ Accompagnement associations environnementales et entreprises à impact : automatisations, agents IA, développement web, conseil stratégique
→ Credibilité terrain + expertise tech, ton direct façon Alexis (masterclass Millenium) : pas de storytelling creux, on montre ce qui marche

---

## Architecture du vault

### 00_inbox
**Rôle** : capture brute, triage quotidien/hebdo
**Contenu** :
- Notes rapides, idées, extraits mails, découvertes
- Daily notes (`AAAA-MM-DD.md`)
- Clippings (tag `#clippings`)
- Content feed (ex. LinkedIn — `content-feed.md`)

**Règle** : si non traité sous 7 jours → archive ou delete

---

### 01_clients
**Format dossier** : `nom-entreprise/nom-entreprise.md`
- La note principale garde le même nom que le dossier (préserve les wikilinks `[[nom-entreprise]]` existants)
- `nom-entreprise/attachments/` accueille les fichiers non-texte liés au client (Excalidraw, images, PDF)
- Une note secondaire (ex. contrat, pièce jointe texte) va directement à la racine du dossier, à côté de la note principale

**Tags obligatoires** : `#client` + `#[statut]` + `#[priorité]` + `#[secteur]` + `#[localisation]`

**Statuts** :
- 🔴 `#lead` — Prospect froid
- 🟡 `#discussion` — En négociation
- 🟢 `#actif` — Client payant
- ⚫ `#terminé` — Archivé

**Priorités** : `#p1` / `#p2` / `#p3`

**Secteurs** : `#environnement` `#impact` en priorité (positionnement du site) ; sinon au cas par cas (`#tech`, `#artisanat`, `#commerce`, `#services`)

**Localisations** : `#france` `#remote` (zone de prospection : France entière / remote)

**Liens systématiques** :
- Vers projets associés : `[[nom-projet-AAAA-MM]]`
- Vers patterns utilisés : `[[pattern-xyz]]`

---

### 02_projects
**Format dossier** : `nom-projet-AAAA-MM/nom-projet-AAAA-MM.md`
- La note principale garde le même nom que le dossier (préserve les wikilinks `[[nom-projet-AAAA-MM]]` existants)
- `nom-projet-AAAA-MM/attachments/` accueille les fichiers non-texte liés au projet (Excalidraw, images, PDF)

**Tags obligatoires** : `#project` + `#[statut]` + `#[client-associé]`

**Statuts** :
- 🔵 `#encours` — Actif
- 🟢 `#terminé` — Livré
- 🔴 `#bloqué` — En attente
- ⚫ `#annulé` — Abandonné

**Liens systématiques** :
- Vers client : `[[nom-client]]`
- Vers patterns utilisés : `[[pattern-xyz]]`
- Vers workflows/code : lien repo GitHub / deployment URL

---

### 03_knowledge
**Sous-dossiers** :
- `patterns/` — Patterns réutilisables (API, workflows, architectural patterns)
- `prompts/` — Prompts validés (agents, cold emails, technical writing)
- `scripts/` — Snippets code (JS/Python/SQL/etc.)
- `checklists/` — Processus répétables (setup client, audit, déploiement)
- `formations/` — Synthèses de formations suivies (ex: contenu Millenium)
- `outils.md` — Fiches outils découverts
- `troubleshooting.md` — Bugs résolus et solutions

**Tags pour patterns** : `#pattern` + `#[type]` + `#validé`
**Types** : `#code` / `#prompt` / `#process` / `#workflow` / etc. (customize to your stack)

**Liens systématiques** :
- Vers cas d'usage réels : `[[client-X]]` / `[[projet-Y]]`

---

### 04_personal
**Sous-dossiers** :
- `admin/` — Compta, légal, banking, business admin
- `formation-millenium/` — Le side project "pipeline RAG Millenium" (chunks_db.sqlite, scraping, enrichissement) — jamais mélangé aux clients Blue Impakt

**Tags** : `#perso` + `#[catégorie]`

---

### 05_archive
**Format fichier** : `AAAA-MM-nom.md`
**Contenu** : projets terminés, leads morts, notes obsolètes
**Tags** : `#archive` + tags originaux conservés

---

### 06_reunions
**Sous-dossiers** :
- `cr/` — Comptes-rendus post-réunion (`AAAA-MM-DD-interlocuteur.md`)
- `prepa/` — Préparations pré-réunion, scripts, briefs (`AAAA-MM-DD-sujet.md`)

**Tags** : `#cr-reunion` ou `#prepa-reunion` + `#[client]`

**Règle** : Les CR et prépas **ne vont pas** dans `02_projects/`. Toute réunion → `06_reunions/`. La fiche client `01_clients/` reçoit uniquement le résumé + lien.

**Templates** : `[[cr-reunion-template]]` / `[[prepa-reunion-template]]`

---

### templates/
**Rôle** : Templates Obsidian pour création rapide de notes structurées.
**Moteur** : Templater (syntaxe `<% tp.date.now("YYYY-MM-DD") %>` et `<% tp.file.title %>` — le titre H1 et les dates se remplissent automatiquement depuis le nom du fichier créé, plus besoin de les retaper).
**Fichiers disponibles** :
- `client-template.md` — Nouvelle fiche client
- `project-template.md` — Nouveau projet
- `cr-reunion-template.md` — CR de réunion
- `prepa-reunion-template.md` — Préparation de réunion
- `pattern-template.md` — Nouveau pattern technique
- `daily-note-template.md` — Daily note

**Setup Templater (à faire une fois dans Obsidian)** : Paramètres → Templater → dossier de templates `templates/` → activer "Folder templates" → mapper `01_clients` → `client-template.md`, `02_projects` → `project-template.md`, `06_reunions/cr` → `cr-reunion-template.md`, `06_reunions/prepa` → `prepa-reunion-template.md`, `00_inbox` → `daily-note-template.md`. Une fois fait, un nouveau fichier créé dans ces dossiers applique le bon template automatiquement.

---

### Plugins installés (minimal setup)
- **Dataview** — alimente `_dashboard.md` (voir plus bas). Ne pas dupliquer ses requêtes ailleurs.
- **Tasks** — surface toutes les checklists non cochées du vault (section "Toutes les actions ouvertes" du dashboard). Pas de syntaxe spéciale requise, les `- [ ]` existants sont déjà indexés.
- **Templater** — voir section `templates/` ci-dessus.
- **Git** (backup auto vers GitHub privé, ajout optionnel) — auto-commit + push sur intervalle régulier. Voir `[[backup-obsidian-git]]` pour la config complète.

### `_dashboard.md` (racine du vault)
Vue vivante générée par Dataview/Tasks : clients par statut, priorités P1, projets en cours/bloqués, patterns validés récents, réunions récentes, toutes les actions ouvertes. **Ce n'est pas un index de navigation** (la règle "pas d'INDEX.md" reste valable — rien n'y est écrit à la main, tout est recalculé à l'ouverture). Ne pas y ajouter de contenu statique.

---

## Règles de capture automatique

### Si je mentionne...

| Déclencheur | Action automatique |
|-------------|-------------------|
| Un prospect (client potentiel) | Créer/update dossier dans `01_clients/nom-client/nom-client.md` avec tags appropriés |
| Une réunion client (prépa) | Créer fichier dans `06_reunions/prepa/` + lien dans fiche client |
| Une réunion client (CR) | Créer fichier dans `06_reunions/cr/` + résumé + lien dans fiche client |
| Un pattern qui marche | Créer fichier dans `03_knowledge/patterns/` avec tag `#validé` |
| Un bug résolu | Documenter dans `03_knowledge/troubleshooting.md` |
| Un outil découvert | Créer/update fiche dans `03_knowledge/outils.md` |
| Une formation suivie | Synthèse dans `03_knowledge/formations/` |
| Un snippet code utile | Créer fichier dans `03_knowledge/scripts/` |

---

## Workflow "ingestion" (quotidien/hebdo)

Quand je dis **"ingère"**, voici la séquence exacte :

### 1. Lire
- Toutes les daily notes (`AAAA-MM-DD.md`) dans `00_inbox/`
- Tous les clippings (tag `#clippings`) dans `00_inbox/`

### 2. Extraire & enrichir
- Extraire le contenu **postable** :
  - Actions faites
  - Insights clients
  - Résultats mesurables
  - Questions ouvertes pertinentes
- **Ajouter** (ne pas remplacer) dans `00_inbox/content-feed.md` sous section datée

### 3. Reporter les tâches
- Prendre toutes les tâches non cochées du "Pense-bêtes" de la daily note
- Les reporter dans la nouvelle daily note du lendemain

### 4. Mettre à jour les fiches
- Si contenu concerne un client/projet → mettre à jour la fiche correspondante
- Ajouter tags appropriés si nécessaire
- Créer liens vers notes connexes

### 5. Nettoyer
- **Supprimer** les daily notes et clippings traités
- **Ne jamais supprimer** `content-feed.md` (votre système de syndication de contenu le vide après utilisation)

---

## Règle anti-doublons (CRITIQUE)

**Avant de créer un fichier, TOUJOURS vérifier si un fichier existant couvre déjà le sujet.**

| Cas | Action |
|-----|--------|
| Même client | Mettre à jour fichier existant — **PAS de doublon** |
| Même pattern/outil | Enrichir fiche existante |
| Même projet | Ajouter section dans fichier projet existant |

**Comment vérifier** :
1. Chercher par nom de dossier dans `01_clients/` ou `02_projects/` (chaque client/projet est un dossier `nom/nom.md`)
2. Chercher par tags (`#client #[secteur] #[localisation]`)
3. Si doute → me demander avant de créer

---

## Quand me poser une question

- Info client/projet pourrait être outdated
- Action irréversible (delete, envoi mail, publication)
- Plusieurs options techniques équivalentes
- Intention pas claire dans ma demande
- Risque de créer un doublon

---

## Quoi ne JAMAIS écraser sans confirmation

- Fichiers clients avec statut `🟢 #actif`
- Workflows/code en production (tag `#prod`)
- Notes avec tag `#important`
- Tout ce qui est dans `03_knowledge/` (patterns validés)

---

## Stack tech actuel

### Infra & automation
- **Automatisation** : n8n (formation Millenium en cours — stack définitive pas encore figée, s'étoffera au fil des modules)
- **IA** : Claude Code / Claude API (outil principal, y compris pour ce vault)
- **Database** : PostgreSQL + Prisma (stack KM0) ; à définir selon les projets clients sinon
- **Produit KM0** : NestJS 10 (TypeScript), Stripe (paiements Click & Collect) + Mollie (abonnements/facturation), Vite/Vercel (frontend) — voir `[[km0-circuit-court]]`
- **CRM** : Notion

### Prospection
- **Email** : à définir
- **Content/Social** : LinkedIn (voir `content-feed.md` + workflow de syndication décrit dans la masterclass Alexis)

### Web & analytics
- **Site** : repo `github.com/BlueImpakt/Site-web` (statique, index.html), déployé via Cloudflare Pages/Wrangler (`wrangler.toml`, projet `blue-impakt`)
- **DNS/Email** : à définir
- **Analytics** : à définir

---

## Formation Millenium — RAG & vault (spécifique à mon activité)

Le projet `C:\Users\LENOVO\Documents\Millenium` contient un pipeline RAG perso
(`chunks_db.sqlite`) qui enrichit les leçons de la formation Millenium (résumés,
tips techniques, patterns). C'est une base volumineuse (des centaines de chunks) —
**elle ne doit jamais être copiée telle quelle dans ce vault** (c'est exactement le
piège "tout-RAG" que la masterclass déconseille : ça ferait exploser le contexte).

Deux ponts possibles, à construire progressivement :
1. **Synthèses statiques** (léger, prioritaire) : exporter une note markdown par
   module/thème de formation (pas par chunk) vers `04_personal/formation-millenium/`
   ou `03_knowledge/formations/` selon que c'est du perso ou du réutilisable client.
2. **Requête à la demande** (avancé, si besoin plus tard) : un petit script consultant
   `chunks_db.sqlite` directement, invoqué seulement quand une synthèse statique ne
   suffit pas — jamais chargé en bloc dans le contexte.

Statut : pas encore construit — à faire au prochain passage sur le vault.

---

## Contexte business actuel

### ICP (Ideal Customer Profile)
- **Primary ICP** : associations environnementales et entreprises à impact, France/remote, cherchant à automatiser (agents IA, n8n) ou digitaliser (no-code/web) sans compétence technique interne
- **Vertical strength** : secteur impact/environnement — positionnement affiché sur le site Blue Impakt, à faire vivre dans le choix des clients et le contenu LinkedIn
- **Active outreach** : pas encore de campagne active

### Deals actifs (mis à jour 2026-08-29)
Aucun pour l'instant dans ce vault. Des projets clients existent déjà sur une autre
machine (sessions Claude Code passées) — à récupérer via le backfill
(`~/.claude/skills/good-night/BACKFILL.md`) dès que ces fichiers sont rapatriés ici.
Une fois fait, cette section liste les clients actifs avec leur statut :
`[[nom-client]]`.

### Projets en cours
À remplir après le backfill ou au fil de l'eau (`good-night` / ingestion manuelle).

---

## Workflow quotidien idéal

### Matin (9h-10h)
1. Review `00_inbox/` — trier captures de la veille
2. Check next actions clients P1
3. Préparer daily note du jour

### Journée
- Capturer **tout** dans inbox (notes rapides, idées, découvertes)
- Tu tries et structures au fil de l'eau

### Soir (18h-19h)
1. Synthèse journalière auto (`/good-night`)
2. Update fiches clients/projets concernés
3. Plan du lendemain dans nouvelle daily note

---

## Convention de tags (référence rapide)

### Clients
`#client #[statut] #[priorité] #[secteur] #[localisation]`

**Exemples** :
- `#client #lead #p2 #environnement #france`
- `#client #actif #p1 #impact #remote`

### Projets
`#project #[statut] #[nom-client]`

**Exemples** :
- `#project #encours #client-name`
- `#project #terminé #another-client`

### Knowledge
`#pattern #[type] #validé`

**Exemples** :
- `#pattern #code #validé`
- `#pattern #prompt #validé`

### Personal
`#perso #[catégorie]`

**Exemples** :
- `#perso #admin`
- `#perso #formation-millenium`

---

## Notes importantes

### Personal projects / Side business
**Contexte strictement séparé de Blue Impakt.**
Ne jamais mélanger dans clients/projets Blue Impakt.
Tout va dans `04_personal/formation-millenium/`

### Content feed
`00_inbox/content-feed.md` est alimenté par ingestion quotidienne.
**Ne jamais supprimer ce fichier** — votre système de syndication le vide après génération posts.

### Anti-spam de questions
Ne pas me redemander systématiquement ce que j'ai déjà explicité dans cette constitution.
Si tu dois confirmer quelque chose de critique (delete, envoi mail) → demande.
Sinon → exécute selon les règles ci-dessus.
