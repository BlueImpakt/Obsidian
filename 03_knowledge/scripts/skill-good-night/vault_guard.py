#!/usr/bin/env python3
"""Garde-fous déterministes du vault, utilisés par good-night / agent-clear.

  python vault_guard.py --vault V feed-append --date AAAA-MM-JJ --content-file F
  python vault_guard.py --vault V lint

Importable : `from vault_guard import assert_no_secret` (daily_note.py).
"""
import argparse
import pathlib
import re
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

SECRET_RE = re.compile(
    r"\$2[aby]\$\d{2}\$[./A-Za-z0-9]{6,}|sk_(?:live|test)_[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{20,}"
    r"|AKIA[0-9A-Z]{12,}|xox[bp]-[A-Za-z0-9-]{10,}"
    r"|(?:api[_-]?key|master[_-]?key|password|mot de passe|token)\s*[:=]\s*[`\"']?[A-Za-z0-9/+_.$-]{20,}",
    re.I,
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def assert_no_secret(text):
    """Refuse (exit 1) toute écriture contenant un motif de secret."""
    hits = [m.group(0)[:8] + "…" for m in SECRET_RE.finditer(text)]
    if hits:
        print(f"REFUS : secret probable dans le contenu ({', '.join(hits[:3])}). "
              "Remplace la valeur par <VALEUR-DU-SECRET> et relance.", file=sys.stderr)
        sys.exit(1)


def norm(line):
    return re.sub(r"\s+", " ", line.strip())


def cmd_feed_append(args):
    if not DATE_RE.match(args.date):
        print(f"REFUS : --date invalide {args.date!r}.", file=sys.stderr)
        sys.exit(2)
    feed = pathlib.Path(args.vault) / "00_inbox" / "content-feed.md"
    if not feed.exists():
        print(f"REFUS : {feed} introuvable (on ne le recrée jamais).", file=sys.stderr)
        sys.exit(1)
    content = pathlib.Path(args.content_file).read_text(encoding="utf-8") if args.content_file else (args.content or "")
    assert_no_secret(content)
    new = [l.rstrip() for l in content.splitlines() if l.strip()]
    if not new:
        print("OK : rien à ajouter.")
        return

    text = feed.read_text(encoding="utf-8")
    heading = f"## {args.date}"
    parts = re.split(r"(?m)^(?=## )", text)
    idx = [i for i, p in enumerate(parts) if p.split("\n", 1)[0].strip() == heading]

    if not idx:
        sep = "" if text.endswith("\n\n") else ("\n" if text.endswith("\n") else "\n\n")
        out = text + sep + f"{heading}\n\n" + "\n".join(new) + "\n"
        feed.write_text(out, encoding="utf-8")
        print(f"OK : section {args.date} créée ({len(new)} ligne(s)).")
        return

    # fusionne d'éventuels doublons de section vers la première, puis ajoute sans doublon
    first = idx[0]
    body_lines = []
    for i in idx:
        body_lines += [l.rstrip() for l in parts[i].split("\n", 1)[1].splitlines() if l.strip()]
    seen, merged = set(), []
    for l in body_lines:
        if norm(l) not in seen:
            seen.add(norm(l))
            merged.append(l)
    added = 0
    for l in new:
        if norm(l) not in seen:
            seen.add(norm(l))
            merged.append(l)
            added += 1
    parts[first] = f"{heading}\n\n" + "\n".join(merged) + "\n\n"
    for i in reversed(idx[1:]):
        del parts[i]
    feed.write_text("".join(parts).rstrip("\n") + "\n", encoding="utf-8")
    print(f"OK : section {args.date} mise à jour (+{added}, {len(idx)-1} doublon(s) de section fusionné(s)).")


def cmd_lint(args):
    script = pathlib.Path(args.vault) / "03_knowledge" / "scripts" / "vault_lint.py"
    if not script.exists():
        print(f"lint indisponible : {script} absent.", file=sys.stderr)
        sys.exit(0)
    r = subprocess.run([sys.executable, str(script), str(args.vault)])
    sys.exit(r.returncode)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("feed-append")
    f.add_argument("--date", required=True)
    g = f.add_mutually_exclusive_group(required=True)
    g.add_argument("--content-file")
    g.add_argument("--content")
    f.set_defaults(func=cmd_feed_append)
    l = sub.add_parser("lint")
    l.set_defaults(func=cmd_lint)
    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
