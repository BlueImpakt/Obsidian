---
tags: [knowledge]
---

# Troubleshooting

Bugs résolus et leur solution. Une section par bug, avec contexte + fix.

## Hook d'ingestion `/clear` ne se déclenchait jamais (Claude Code 2.1.199 / Windows)

**Contexte** : la chaîne `/clear` → agent headless `good-night` (ingestion continue du vault, voir `[[ajouter-lecon-au-rag-millenium]]` pour le pipeline voisin) semblait fonctionner (logs présents le 2026-08-29) mais plus rien après 22h40. Les 3 logs initiaux se sont révélés être des lancements **manuels** du script pour le tester, pas de vrais déclenchements automatiques — donc en réalité le hook n'avait jamais tourné tout seul.

**Root cause** (trouvée par test matriciel, 4 combinaisons event/matcher instrumentées en parallèle) : sur ce build (Claude Code 2.1.199, Windows), `/clear` déclenche bien `SessionStart` **et** `SessionEnd`, mais le `source`/`reason` transmis n'est **pas** la chaîne littérale `"clear"` — la doc officielle est fausse pour cette version. Résultat : tout hook avec `"matcher": "clear"` exact est mort-né, seuls les matchers en **alternation** (`startup|resume|clear|compact|fork`) firent. En plus, les hooks `SessionStart` reçoivent un **stdin vide** sur ce build — un script qui fait `INPUT="$(cat)"` puis filtre sur `source` en JSON échoue systématiquement, même si l'event se déclenche.

**Fix** :
1. `~/.claude/settings.json` : hook basculé de `SessionStart` vers **`SessionEnd`**, avec un matcher en alternation `"clear|logout|prompt_input_exit|other"` (jamais `"clear"` seul).
2. `~/.claude/skills/good-night/ingest_on_clear.sh` : suppression du bloc lecture stdin + garde applicatif sur `source` (redondant avec le matcher `settings.json`, et mortel quand stdin est vide) — le script se fie désormais uniquement au matcher.

**Comment vérifier que ça tourne** : `~/.claude/skills/good-night/state/logs/hook-trace.log` doit contenir une ligne `FIRED` puis `LAUNCHED` à chaque `/clear`.

**À retenir** : ne jamais faire confiance à la doc Claude Code sur la valeur exacte de `source`/`reason` pour un event donné sans l'avoir vérifiée par une sonde catch-all sur ce build précis — instrumenter (log inconditionnel en tête de script + matcher large) avant de committer un matcher strict.
