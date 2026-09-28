#!/usr/bin/env python3
"""Footnote checker / shifter for one chapter of the HUN or ENG file.

  python3 fntool.py check HUN|ENG <chapter-no>
  python3 fntool.py shift HUN|ENG <chapter-no> <from_n> <delta> <expect_max>

A chapter spans from its heading to the next chapter heading (ch9 HUN: to "# Utószó";
ch9 ENG: its footnotes sit after the Glossary, so ch9 ENG is not supported here).
Body markers = superscript-digit runs outside the footnote list; list entries = lines of
the footnote list that start with a superscript run. `shift` renumbers every marker
>= from_n by +delta, but only if the current highest list number equals expect_max
(guards against running the same shift twice).
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = {"HUN": ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md",
         "ENG": ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md"}
HUN_H = ["Első", "Második", "Harmadik", "Negyedik", "Ötödik", "Hatodik", "Hetedik", "Nyolcadik", "Kilencedik"]
ENG_H = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
SUP = "⁰¹²³⁴⁵⁶⁷⁸⁹"
TO_SUP = str.maketrans("0123456789", SUP)
FROM_SUP = str.maketrans(SUP, "0123456789")
RUN = re.compile(f"[{SUP}]+")


def span(which, text, ch):
    if which == "HUN":
        start = text.index(f"\n# {HUN_H[ch-1]} fejezet\n")
        end = text.index("\n# Utószó\n") if ch == 9 else text.index(f"\n# {HUN_H[ch]} fejezet\n")
    else:
        assert ch != 9, "ENG ch9 footnotes live after the Glossary"
        start = text.index(f"\n# Chapter {ENG_H[ch-1]}\n")
        end = text.index(f"\n# Chapter {ENG_H[ch]}\n")
    return start, end


def parse(seg, which):
    head = "\n## Lábjegyzetek\n" if which == "HUN" else "\n## Footnotes\n"
    k = seg.index(head)
    body, lst = seg[:k], seg[k:]
    bnums = [int(m.group().translate(FROM_SUP)) for m in RUN.finditer(body)]
    lnums = [int(m.group(1).translate(FROM_SUP)) for m in re.finditer(f"\n([{SUP}]+) ?", lst)]
    return k, body, lst, bnums, lnums


def main():
    cmd, which, ch = sys.argv[1], sys.argv[2], int(sys.argv[3])
    p = FILES[which]
    text = p.read_text(encoding="utf-8")
    s, e = span(which, text, ch)
    seg = text[s:e]
    k, body, lst, bnums, lnums = parse(seg, which)
    if cmd == "check":
        print("body:", bnums)
        print("list:", lnums)
        ok = bnums == lnums == list(range(1, len(lnums) + 1))
        print("OK 1..N aligned" if ok else "MISMATCH")
        return
    if cmd == "shift":
        frm, delta, expect = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
        if max(lnums) != expect:
            sys.exit(f"REFUSED: list max is {max(lnums)}, expected {expect} (already shifted?)")
        def sub(m):
            n = int(m.group().translate(FROM_SUP))
            return str(n + delta).translate(TO_SUP) if n >= frm else m.group()
        body2 = RUN.sub(sub, body)
        lst2 = re.sub(f"(?<=\n)[{SUP}]+(?= ?)", sub, lst)
        p.write_text(text[:s] + body2 + lst2 + text[e:], encoding="utf-8")
        _, _, _, b2, l2 = parse(body2 + lst2, which)
        print("body:", b2)
        print("list:", l2)
        return
    sys.exit("unknown command")


if __name__ == "__main__":
    main()
