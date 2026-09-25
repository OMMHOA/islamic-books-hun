#!/usr/bin/env python3
"""Print the footnotes of one AR printed page (full text) with their body anchor context.

    python3 arpage.py PAGE [PAGE2 ...]
"""
import re
import sys

A = "/home/condoriano/hobby/islamic-books-hun/fiqh-us-seerah/FiqhusSeerah-Muhammad-al-Ghazali-AR-full.md"
L = open(A, encoding="utf-8").read().split("\n")


def page_lines(pg):
    out, on = [], False
    for l in L:
        m = re.match(r"^\[صفحة (\d+)\]", l)
        if m:
            on = int(m.group(1)) == pg
            continue
        if on:
            out.append(l)
    return out


for pg in map(int, sys.argv[1:]):
    lines = page_lines(pg)
    body = [l for l in lines if not l.startswith(">")]
    print(f"=== p.{pg}")
    for l in lines:
        m = re.match(r"^> (\(([٠-٩0-9]+|\*)\))", l)
        if not m:
            continue
        mk = m.group(1)
        ctx = next((b[max(0, b.find(mk) - 120):b.find(mk) + len(mk)] for b in body if mk in b), "")
        print(f"[{mk}] ANCHOR: …{ctx}")
        print(f"      NOTE: {l[2:]}")
