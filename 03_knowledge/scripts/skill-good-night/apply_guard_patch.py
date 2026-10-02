#!/usr/bin/env python3
"""Ajoute le garde-fou anti-secret à daily_note.py (idempotent, avec backup .bak).

Usage : python apply_guard_patch.py "C:/Users/LENOVO/.claude/skills/good-night/daily_note.py"
Prérequis : vault_guard.py dans le même dossier que daily_note.py.
"""
import pathlib
import py_compile
import shutil
import sys

IMPORT_ANCHOR = "import unicodedata\n"
IMPORT_ADD = "from vault_guard import assert_no_secret  # garde-fou anti-secret\n"
CALL_ANCHOR = "    new_lines = [l.rstrip() for l in new_content.splitlines() if l.strip()]\n"
CALL_ADD = "    assert_no_secret(new_content)\n"

p = pathlib.Path(sys.argv[1])
src = p.read_text(encoding="utf-8")
if IMPORT_ADD in src:
    print("Déjà patché, rien à faire.")
    sys.exit(0)
if src.count(IMPORT_ANCHOR) != 1 or src.count(CALL_ANCHOR) != 2:
    print(f"ABORT : ancres inattendues (import={src.count(IMPORT_ANCHOR)}, new_lines={src.count(CALL_ANCHOR)}) — fichier non modifié.")
    sys.exit(1)
out = src.replace(IMPORT_ANCHOR, IMPORT_ANCHOR + IMPORT_ADD).replace(CALL_ANCHOR, CALL_ADD + CALL_ANCHOR)
shutil.copy2(p, str(p) + ".bak")
p.write_text(out, encoding="utf-8")
try:
    py_compile.compile(str(p), doraise=True)
except py_compile.PyCompileError as e:
    shutil.copy2(str(p) + ".bak", p)
    print(f"ABORT : le fichier patché ne compile pas, restauré ({e}).")
    sys.exit(1)
print("OK : daily_note.py patché (1 import + 2 appels assert_no_secret). Backup : daily_note.py.bak")
