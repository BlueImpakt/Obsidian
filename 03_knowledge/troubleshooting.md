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

### Suite : boucle d'emballement une fois le hook actif

**Symptôme** : hook enfin fonctionnel → ~33 agents `claude -p` déclenchés en 3 min, en accélération.

**Root cause** : deux effets cumulés. (1) `SessionEnd` fire **~2× par `/clear`** sur ce build. (2) surtout : l'agent d'ingestion lance lui-même `claude -p`, dont la fin re-déclenche `SessionEnd` → nouvel agent → récursion. Les agents se reconnaissent comme « méta » et n'écrivent rien dans le vault (donc pas de corruption), mais le *spawn* continue.

**Fix** — deux gardes en tête de `ingest_on_clear.sh` :
1. **Anti-récursion** : le lancement fait `nohup env GOODNIGHT_INGEST=1 bash -c "... claude -p ..."`. Le hook sort immédiatement si `$GOODNIGHT_INGEST = 1` (le marqueur est bien hérité par le hook `SessionEnd` de la session headless — vérifié).
2. **Rate-limit** : sentinelle `state/.last-ingest` (`touch` avant lancement) ; le hook sort si elle a moins de 180 s. Absorbe le double-fire et plafonne à une ingestion / 3 min.

**Contrepartie assumée** : un vrai `/clear` avec du travail neuf dans les 180 s suivant une ingestion est différé — mais le `/clear` qualifiant suivant ré-scanne **toutes** les sessions non ingérées (rien n'est perdu), et `/good-night` balaie le soir.

**Vérif OK** = trace avec **1 seul** `LAUNCHED` puis des `SKIP (... < 180s)` / `SKIP (session issue de l ingestion)`, sans cascade.

## [[naeco-carte]] — tracés d'expédition qui reviennent à leur position initiale en cours d'édition

**Symptôme** : en mode éditeur, un tracé déplacé revient parfois tout seul à sa position d'avant, sans intervention.

**Root cause** : race condition au chargement de la page. Le `fetch` JSONbin `/latest` (asynchrone, 2-10 s de latence typique sur l'offre gratuite) répond parfois **après** que l'utilisateur soit entré en mode édition et ait déjà modifié un tracé. Le `.then()` du fetch remplaçait alors `expeditions` **sans aucune condition**, écrasant la modif en cours à l'écran et dans le localStorage — indépendamment de toute action de l'utilisateur.

**Fix** : flag `localDirty` passé à `true` dans l'intercepteur d'écriture locale (`ls_set`, `index.html:545-547`) ; garde ajoutée dans le `.then()` du chargement distant (`index.html:2620-2627`) qui ignore la réponse JSONbin si `localDirty` ou mode édition actif. Une fois qu'une modif locale a eu lieu, le chargement distant est volontairement sauté pour le reste de la session — recharger la page pour repartir de l'état JSONbin le plus récent.

**À retenir** : tout site avec le pattern [[jsonbin-source-de-verite]] (fetch distant au chargement + édition en direct possible immédiatement) doit gérer explicitement le cas où le fetch répond en retard sur une action utilisateur déjà en cours — sinon la version distante écrase silencieusement la version locale.
