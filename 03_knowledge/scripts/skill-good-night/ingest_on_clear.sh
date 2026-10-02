#!/usr/bin/env bash
# Hook SessionEnd : a chaque fin de session (dont /clear), lance en arriere-plan
# un agent Claude headless qui ingere la conversation terminee dans le vault.
# NB build Windows 2.1.x : /clear n'emet pas source/reason="clear", stdin vide
# -> pas de filtre sur la charge JSON, on se fie au matcher settings.json.

TRACE="/c/Users/LENOVO/.claude/skills/good-night/state/logs/hook-trace.log"
SKILL_DIR="/c/Users/LENOVO/.claude/skills/good-night"
LOG_DIR="$SKILL_DIR/state/logs"
mkdir -p "$LOG_DIR" 2>/dev/null || true
printf '%s  FIRED pid=%s ppid=%s\n' "$(date +%FT%T)" "$$" "$PPID" >> "$TRACE" 2>/dev/null || true

# Garde 0 — opt-out manuel : le skill `fullclear` pose cette sentinelle pour qu'un
# `/clear` jetable (test, bruit, faux depart) ne remonte pas dans le vault.
# Usage unique + peremption 6 h (evite qu'une sentinelle oubliee tue une vraie
# ingestion des jours plus tard).
SKIP="$SKILL_DIR/state/.skip-ingest"
if [ -f "$SKIP" ]; then
  skip_age=$(( $(date +%s) - $(stat -c %Y "$SKIP" 2>/dev/null || echo 0) ))
  rm -f "$SKIP"
  if [ "$skip_age" -lt 21600 ]; then
    # neutralise le 2e fire de SessionEnd via la garde rate-limit ci-dessous
    touch "$SKILL_DIR/state/.last-ingest"
    printf '%s  SKIP (/fullclear opt-out, sentinelle %ss)\n' "$(date +%FT%T)" "$skip_age" >> "$TRACE" 2>/dev/null || true
    exit 0
  fi
  printf '%s  IGNORE sentinelle /fullclear perimee (%ss) -> ingestion normale\n' "$(date +%FT%T)" "$skip_age" >> "$TRACE" 2>/dev/null || true
fi

# Garde 1 — anti-boucle : l'agent d'ingestion lance lui-meme `claude -p`, dont la
# fin refait un SessionEnd. Ce marqueur d'env casse la recursion.
if [ "${GOODNIGHT_INGEST:-}" = "1" ]; then
  printf '%s  SKIP (session issue de l ingestion)\n' "$(date +%FT%T)" >> "$TRACE" 2>/dev/null || true
  exit 0
fi

# Garde 2 — rate-limit : SessionEnd fire ~2x par /clear, et filet de securite si
# la garde 1 ne suffit pas. Au plus une ingestion toutes les 180 s.
SENTINEL="$SKILL_DIR/state/.last-ingest"
if [ -f "$SENTINEL" ]; then
  age=$(( $(date +%s) - $(stat -c %Y "$SENTINEL" 2>/dev/null || echo 0) ))
  if [ "$age" -lt 180 ]; then
    printf '%s  SKIP (ingestion il y a %ss < 180s)\n' "$(date +%FT%T)" "$age" >> "$TRACE" 2>/dev/null || true
    exit 0
  fi
fi
touch "$SENTINEL"

set -uo pipefail
VAULT="C:/Users/LENOVO/Documents/Obsidian/BLUE IMPAKT"
STAMP="$(date +%Y%m%d-%H%M%S)"

if [ -f "$SKILL_DIR/state/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  . "$SKILL_DIR/state/.env"
  set +a
fi

# Controle qualite deterministe apres l'agent : secrets, liens casses, doublons de
# section du feed, fichiers parasites a la racine, dailies > 7 j. Resultat dans le
# log d'ingestion + trace ; code != 0 = anomalie bloquante a corriger.
PY="$(command -v python3 || command -v python || echo python)"
LINT="\"$PY\" \"$SKILL_DIR/vault_guard.py\" --vault \"$VAULT\" lint"

nohup env GOODNIGHT_INGEST=1 bash -c "cd '$VAULT' && claude -p --dangerously-skip-permissions \"\$(cat '$SKILL_DIR/ingest_prompt.md')\"; echo; echo '=== LINT ==='; $LINT; rc=\$?; printf '%s  LINT rc=%s\n' \"\$(date +%FT%T)\" \"\$rc\" >> '$TRACE'" \
  > "$LOG_DIR/ingest-$STAMP.log" 2>&1 &
disown

printf '%s  LAUNCHED agent -> ingest-%s.log\n' "$(date +%FT%T)" "$STAMP" >> "$TRACE" 2>/dev/null || true
exit 0
