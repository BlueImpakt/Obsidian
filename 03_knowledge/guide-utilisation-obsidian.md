---
tags: [knowledge, guide]
---

# Guide pratique — utiliser ce vault au quotidien

Pas un rappel de l'architecture (déjà dans [[CLAUDE.md]]) : ce guide répond à
"qu'est-ce que je fais concrètement, quand, avec quelle commande" pour
l'activité Blue Impakt (automatisation IA/no-code/consulting pour associations
environnementales et entreprises à impact, + KM0 en parallèle) et la formation
Millenium en cours.

## Le principe de base à ne jamais perdre de vue

Ce vault ne vaut que par ce qu'il contient à jour. Une session Claude Code sur
ce dossier lit `CLAUDE.md` + les fichiers pertinents avant de répondre — donc
plus tu (ou l'ingestion auto) alimentes les fiches clients/projets, plus les
réponses de Claude sont précises et sourcées. À l'inverse, un vault qui se vide
de contenu frais redevient une simple app de prise de notes.

## Workflow type d'une journée

**Le matin** — tu ouvres `_dashboard.md` (une fois Dataview/Tasks installés,
voir [[backlog-ameliorations-vault]]) pour voir les clients actifs, les tâches
en cours et ce qui a été capté la veille par `good-night`. Rien à faire de
particulier si le dashboard n'est pas encore actif : ouvre directement la
daily note du jour (créée automatiquement par le rollover de `good-night`).

**Pendant la journée** — deux façons de faire rentrer de l'info dans le vault :

1. **Tu lances une session Claude Code dans le dossier du vault** et tu lui
   parles directement : *"Nouveau client, Théo Maréchal, RDV mardi 9h,
   ingère tout ça dans le volt"* — Claude crée/complète la fiche client,
   les next actions, etc. C'est la manière volontaire, comme dans la démo
   d'Alexis.
2. **Tu travailles sur un projet client ailleurs** (repo esprit-docker, naeco,
   KM0, Site-web...) et tu fais juste `/clear` en fin de session — le hook
   `agent-clear` tourne en fond, relit la conversation, et ingère
   automatiquement ce qui est pertinent dans le vault. Rien à taper de plus,
   c'est le comportement par défaut sur *tous* tes projets, pas seulement
   quand tu es dans le dossier vault.

**Un appel/visio client** — tu enregistres (dictaphone téléphone ou PC), puis
dans une session Claude Code : `/transcribe` + le fichier audio. Ça transcrit
en local (Whisper), remplit le compte-rendu dans `06_reunions/`, et génère les
next actions pour la fiche client concernée. Pas besoin de retaper le CR à la
main.

**Le soir** — `/good-night` en fin de journée, même si `agent-clear` a déjà
tourné plusieurs fois : il repasse sur *toutes* les sessions Cloud Code de la
journée (y compris celles où tu as fermé le terminal sans faire `/clear`),
garantit qu'aucune info n'est perdue, et prépare la note du lendemain. C'est
la sécurité qui rattrape ce que `agent-clear` aurait pu manquer.

## Nouveau client / nouveau projet

Ne pas créer la fiche à la main depuis zéro : soit tu ingères directement (voir
ci-dessus), soit tu dis à Claude *"nouveau client, template client, [infos]"* —
il applique `templates/client-template.md`, remplit les variables (statut,
secteur, contexte), et crée le lien vers `02_projects/` si un projet est déjà
identifié. Le but du template : que toutes les fiches clients aient exactement
la même structure, ce qui permet à Claude de savoir où chercher sans avoir à
lire tout le fichier.

## Utiliser la formation Millenium pendant un travail client

Deux niveaux, à choisir selon le besoin (détail complet dans
[[03_knowledge/formations/_index|index formations]]) :

- **Une notion stable et pédagogique** ("c'est quoi un RAG", "comment
  fonctionne le re-ranking") → les notes de synthèse dans
  `03_knowledge/formations/` suffisent, pas besoin d'invoquer un skill.
- **Retrouver la formulation exacte de Théo ou un tip technique précis, avec
  lien vidéo à citer** → skill `/millenium-rag` (recherche sémantique dans les
  6605 chunks). Si en plus tu veux vérifier qu'un prix/une version d'outil n'a
  pas changé depuis l'enregistrement → `/millenium-rag-open` (ajoute une
  recherche web en complément, toujours en distinguant formation vs web dans
  la réponse).

Utile aussi bien pour te rafraîchir la mémoire que pour appuyer un discours
client avec une source précise.

## Basculer entre les comptes GitHub sans se ré-authentifier

Chaque org (BlueImpakt, espritdocker, NAECOEXPEDITION) a son propre
`credential.https://github.com/<org>.username` dans la config git globale —
tu n'as jamais besoin de te reconnecter en changeant de client. Si un jour tu
prends un nouveau client avec un repo GitHub sous une org que tu n'as pas
encore, il faudra ajouter la même ligne de config pour cette nouvelle org (le
principe reste identique, demande à Claude de le refaire si besoin).

## Garder le vault propre

Pas d'audit automatique en place pour l'instant (voir Paperclip dans
[[backlog-ameliorations-vault]] si ça devient nécessaire à grande échelle).
En attendant, réflexe simple : si tu remarques une fiche client au statut
visiblement obsolète ou un doublon, dis-le directement à Claude dans une
session sur le vault — il peut corriger/archiver à la volée, pas besoin
d'attendre un outil dédié.

## Ce qui reste manuel

- Cocher/décocher les tâches dans les fiches (Tasks, une fois installé,
  simplifie juste la vue globale — la case elle-même reste un geste manuel)
- Trier ce qui atterrit dans `00_inbox` (clippings web, notes rapides) vers
  les bons dossiers clients/projets/knowledge
- Toute décision de contenu (quoi publier, quoi répondre à un client) —
  Claude prépare, tu valides
