---
tags: [knowledge, backlog]
---

# Backlog — améliorations vault à considérer plus tard

Issu du tour complet de la masterclass [[masterclass-claude-code-obsidian-alexis]]
(2026-08-29) : ce qu'Alexis montre mais qu'on n'a pas encore implémenté ici, par
choix (pas encore utile) plutôt que par oubli. À relire si l'activité évolue.

## 1. Compatibilité multi-IA (AGENTS.md générique)

Suggestion d'un participant (Mark) pendant le live : au lieu d'un seul `CLAUDE.md`,
créer un `AGENTS.md` générique (standard utilisé par OpenAI/Codex) qui porte le
contenu réel, avec `CLAUDE.md` et `GEMINI.md` réduits à un simple pointeur vers
`AGENTS.md`. Avantage : le vault reste utilisable si un jour on bascule sur une
autre IA (Codex, Gemini) sans tout réécrire.

**À faire si** : usage réel d'une autre IA en plus de Claude Code se présente.
Pas urgent tant que 100% Claude.

## 2. Section "Content Feed" dans la daily note

Alexis a une section dédiée dans sa note du jour qui capture spécifiquement les
insights/réussites/blocages utilisables pour du storytelling LinkedIn — alimentée
automatiquement au fil de la journée, puis envoyée 1-2x/semaine à un workflow qui
génère 3 propositions de post. Distinct de "Ce qu'on a fait" (plus factuel) :
le Content Feed cible explicitement l'angle narratif réutilisable.

Nécessite en plus le plugin **Post Webhook** (envoie le contenu d'une note vers un
webhook n8n) — pas installé.

**À faire si** : volonté d'industrialiser la présence LinkedIn de Blue Impakt avec
du contenu storytelling régulier plutôt que ponctuel.

## 3. Dashboard custom connecté CRM/agenda avec délégation en 1 clic

Le dashboard qu'Alexis montre n'est pas Dataview/Tasks : c'est du développement
custom qui liste les tâches, permet de valider/supprimer, et déclenche
automatiquement une session Claude Code en arrière-plan pour déléguer une tâche
("cherche les contacts potentiels de Christelle" → lancement auto d'un agent).
Connecté à son Google Agenda et son CRM (Twenty, via MCP).

**À faire si** : le volume de tâches déléguées à Claude devient assez important
pour justifier ce niveau d'automatisation. Pour l'instant CRM = Notion
([[CLAUDE.md|contexte business]]), pas de CRM ouvert en MCP.

## 4. Paperclip (orchestrateur multi-agents)

Outil open source présenté par Alexis comme "le niveau au-dessus" : plusieurs
agents avec rôles fixes (veille concurrentielle, veille communauté/tendances,
rédaction...) qui se réveillent sur des routines programmées (ex: lundi matin)
et rapportent à un agent "CEO". Alexis le présente lui-même comme à essayer
seulement après plusieurs semaines de bases bien rodées — explicitement pas pour
débuter.

**À faire si** : le socle actuel (good-night / agent-clear / dashboard) tourne
bien depuis un moment et qu'un vrai besoin de veille concurrentielle/tendances
automatisée en continu se fait sentir.

## Point de vigilance (pas un todo — un réflexe)

Si Claude Code semble "oublier" de consulter le vault avant de répondre, la cause
possible : un skill (ex. `superpowers:brainstorming`, déclenché par des mots comme
"réfléchir") prend la priorité sur la lecture du contexte vault. Réflexe à avoir :
le dire explicitement à Claude dans la session ("va d'abord consulter le vault"),
pas une config à préparer en amont.
