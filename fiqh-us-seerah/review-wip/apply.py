#!/usr/bin/env python3
"""Idempotent exact-match edit engine for the Opus 5.5 review fixes.

Usage: python3 apply.py specs/ch9.py [--dry]

A spec module defines EDITS = [E(target, id, old, new), ...] where target is
"HUN" or "ENG". For each edit: if `old` occurs exactly once it is replaced; if it
occurs 0 times but `new` is present, the edit counts as already applied; anything
else aborts the whole spec (no file is written). Applied ids are appended to
applied.log so progress survives a lost session.
"""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = {
    "HUN": ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md",
    "ENG": ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md",
}


class E:
    def __init__(self, target, id, old, new, count=1):
        assert target in FILES, target
        self.target, self.id, self.old, self.new, self.count = target, id, old, new, count


def main():
    spec_path = pathlib.Path(sys.argv[1])
    dry = "--dry" in sys.argv
    spec = importlib.util.spec_from_file_location("spec", spec_path)
    mod = importlib.util.module_from_spec(spec)
    mod.E = E
    sys.modules["apply"] = sys.modules[__name__]
    spec.loader.exec_module(mod)
    texts = {k: p.read_text(encoding="utf-8") for k, p in FILES.items()}
    applied, skipped, errors = [], [], []
    for e in mod.EDITS:
        t = texts[e.target]
        n = t.count(e.old)
        if e.new and e.old in e.new and e.new in t:
            skipped.append(e)  # old is a substring of new: presence of new means done
        elif n == e.count:
            texts[e.target] = t.replace(e.old, e.new)
            applied.append(e)
        elif n == 0 and e.new and e.new in t:
            skipped.append(e)
        else:
            errors.append(f"{e.id} [{e.target}]: old found {n}x (expected {e.count}): {e.old[:90]!r}")
    for msg in errors:
        print("ERROR", msg)
    if errors:
        print(f"ABORTED: {len(errors)} error(s); nothing written.")
        sys.exit(1)
    print(f"{spec_path.name}: {len(applied)} applied, {len(skipped)} already applied.")
    if dry:
        return
    for k, p in FILES.items():
        if texts[k] != p.read_text(encoding="utf-8"):
            p.write_text(texts[k], encoding="utf-8")
    with open(pathlib.Path(__file__).parent / "applied.log", "a", encoding="utf-8") as f:
        for e in applied:
            f.write(f"{spec_path.stem}\t{e.id}\t{e.target}\n")


if __name__ == "__main__":
    main()
