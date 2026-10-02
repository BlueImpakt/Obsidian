#!/usr/bin/env python3
"""Contrôle qualité du vault — à lancer en dernière étape de good-night / agent-clear.

Usage : python vault_lint.py [chemin_vault] [--strict]
Sortie : une ligne par anomalie (CODE chemin détail). Code retour 1 si anomalie
bloquante (SECRET, ROOT, DUPSEC) ou si --strict et au moins une anomalie.
Stdlib uniquement, lecture seule.
"""
import re, sys, datetime
from pathlib import Path

ROOT = Path(next((a for a in sys.argv[1:] if not a.startswith("--")), "."))
STRICT = "--strict" in sys.argv
SKIP_DIRS = {".git", ".obsidian", "formations"}
ROOT_ALLOWED = {"CLAUDE.md", "_dashboard.md", ".gitignore"}
PLACEHOLDERS = {"client-X", "nom-client", "nom-entreprise", "nom-projet-AAAA-MM", "pattern-xyz", "projet-Y"}
SECRET_RE = re.compile(
    r"\$2[aby]\$\d{2}\$[./A-Za-z0-9]{6,}|sk_(?:live|test)_[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{20,}"
    r"|AKIA[0-9A-Z]{12,}|xox[bp]-[A-Za-z0-9-]{10,}|(?:api[_-]?key|master[_-]?key|password|mot de passe|token)\s*[:=]\s*[`\"']?[A-Za-z0-9/+_.$-]{20,}",
    re.I,
)
INBOX_MAX_DAYS = 7
ARCHIVE_DAILY_MAX = 10
JOURNAL_MAX = 15

issues, blocking = [], set()


def flag(code, path, detail="", block=False):
    issues.append(f"{code} {path} {detail}".rstrip())
    if block:
        blocking.add(code)


def notes():
    for p in ROOT.rglob("*.md"):
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts):
            yield p


def rel(p):
    return p.relative_to(ROOT).as_posix()


all_notes = list(notes())
names = {p.stem for p in ROOT.rglob("*.md") if ".git" not in p.parts}

for p in all_notes:
    text = p.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        flag("EMPTY", rel(p), "fichier vide")
    for m in SECRET_RE.finditer(text):
        flag("SECRET", rel(p), f"motif sensible « {m.group(0)[:8]}… »", block=True)
    in_code = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        for m in re.finditer(r"\[\[([^\]|#]+)", line):
            t = m.group(1).strip()
            base = Path(t).stem if t.endswith(".md") else Path(t).name
            if base not in names and t not in PLACEHOLDERS and not (ROOT / t).exists():
                flag("LINK", rel(p), f"[[{t}]] sans cible")

for p in ROOT.iterdir():
    if p.is_file() and p.name not in ROOT_ALLOWED and p.suffix in {".md", ".canvas"}:
        flag("ROOT", p.name, "fichier parasite à la racine", block=True)
    if p.suffix == ".canvas" and p.is_file() and p.read_text().strip() in {"", "{}"}:
        flag("EMPTY", p.name, "canvas vide")

feed = ROOT / "00_inbox" / "content-feed.md"
if feed.exists():
    seen = {}
    for h in re.findall(r"(?m)^## (.+)$", feed.read_text(encoding="utf-8")):
        seen[h.strip()] = seen.get(h.strip(), 0) + 1
    for h, n in seen.items():
        if n > 1:
            flag("DUPSEC", "00_inbox/content-feed.md", f"section « {h} » x{n} — fusionner", block=True)

today = datetime.date.today()
for p in (ROOT / "00_inbox").glob("20??-??-??.md"):
    age = (today - datetime.date.fromisoformat(p.stem)).days
    if age > INBOX_MAX_DAYS:
        flag("STALE", rel(p), f"{age} j dans l'inbox (> {INBOX_MAX_DAYS}) — archiver")
    elif age >= 0:
        for l in p.read_text(encoding="utf-8").splitlines():
            if re.match(r"- \[ \] \S", l) and re.search(r"\b(naeco|esprit|km0|blue-impakt)", l, re.I):
                flag("TASKDUP", rel(p), "tâche rattachable à une fiche — doit vivre dans la fiche")
                break

arch = list((ROOT / "05_archive" / "daily").glob("*.md"))
if len(arch) > ARCHIVE_DAILY_MAX:
    flag("CAP", "05_archive/daily", f"{len(arch)} fichiers (> {ARCHIVE_DAILY_MAX})")

for p in all_notes:
    r = rel(p)
    if r.startswith(("01_clients/", "02_projects/")) and "journal-archive" not in r:
        t = p.read_text(encoding="utf-8")
        fm = re.match(r"---\n(.*?)\n---", t, re.S)
        tags = re.search(r"tags:\s*\[(.*?)\]", fm.group(1)) if fm else None
        tagset = {x.strip() for x in tags.group(1).split(",")} if tags else set()
        if r.startswith("01_clients/") and not {"client"} <= tagset:
            flag("TAGS", r, "tags client manquants")
        if r.startswith("01_clients/") and len(tagset) < 5:
            flag("TAGS", r, "attendu: client+statut+priorité+secteur+localisation")
        if r.startswith("02_projects/") and len(tagset) < 3:
            flag("TAGS", r, "attendu: project+statut+client-associé")
        j = re.search(r"(?ms)^## Journal\n(.*?)(?=^## |\Z)", t)
        if j and len(re.findall(r"(?m)^- ", j.group(1))) > JOURNAL_MAX + 3:
            flag("JOURNAL", r, f"> {JOURNAL_MAX} entrées — archiver")

for i in issues:
    print(i)
print(f"-- {len(issues)} anomalie(s)")
sys.exit(1 if blocking or (STRICT and issues) else 0)
