#!/usr/bin/env python3
"""User decisions 2026-09-25 — mechanical sweeps (run AFTER d1_content.py via apply.py).

    python3 specs/d2_mech.py [--dry]

6. Zayd ibn 'Amr ibn Nufayl: no (رضي الله عنه) — he died before the Prophethood (not a Ṣaḥābī);
   the Arabic has none. Removed inside his ch2 passage only (other Zayds keep theirs).
3. Jāhiliyyah → dzsáhilijja (Hungarian spelling, no italics; adjective → "dzsáhilijja kori").
1. Dashes: em dash — → en dash – (Hungarian norm; spacing unchanged).        [HUN only]
2. Closing quotes: straight " → ” (Hungarian „…”; every " in HUN closes a „). [HUN only]
Idempotent: each step only changes what is still in the old form.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
HUN = ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md"
ENG = ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md"
HON = " (رضي الله عنه)"
ZAYD = re.compile(r"((?:Zayd|Zaid|'Amr|Nufayl)[^\s(]*) \(رضي الله عنه\)")


def zayd_region(t, start_anchor, end_anchor):
    s = t.index(start_anchor)
    e = t.index(end_anchor, s)
    e = t.index("\n", e)  # end of that paragraph
    return s, e


def strip_zayd(t, start_anchor, end_anchor):
    s, e = zayd_region(t, start_anchor, end_anchor)
    seg, n = ZAYD.subn(r"\1", t[s:e])
    return t[:s] + seg + t[e:], n


JAHIL = [
    ("*Jahilīyyah*:", "*Dzsáhilijja*:"),  # glossary headword
    ("hogy ez a szó *dzsáhilī* eredetű", "hogy ez a szó a dzsáhilijja korából való"),
    ("néhány jāhilī szokás", "néhány dzsáhilijja kori szokás"),
    ("jāhilīyah-beli", "dzsáhilijja kori"),
    ("*jahilīyáját*", "dzsáhilijjáját"),
    ("*dzsáhilijját*", "dzsáhilijját"),
    ("*dzsáhilijjában*", "dzsáhilijjában"),
    ("*dzsáhilijja*", "dzsáhilijja"),
    ("*jahilīyah*", "dzsáhilijja"),
    ("jāhilīyájukban", "dzsáhilijjájukban"),
    ("jāhilīyájukhoz", "dzsáhilijjájukhoz"),
    ("jāhilīyájában", "dzsáhilijjájában"),
    ("jāhilīyáját", "dzsáhilijjáját"),
    ("jāhilīyában", "dzsáhilijjában"),
    ("jahilīyában", "dzsáhilijjában"),
    ("jāhilīyát", "dzsáhilijját"),
    ("jāhilīyah", "dzsáhilijja"),
    ("jahilīyah", "dzsáhilijja"),
    ("dzsāhilijjájában", "dzsáhilijjájában"),
    ("dzsāhilijja", "dzsáhilijja"),
]


def main():
    dry = "--dry" in sys.argv
    h = HUN.read_text(encoding="utf-8")
    e = ENG.read_text(encoding="utf-8")
    h, nh = strip_zayd(h, "A Próféta (ﷺ) küldetése előtt volt", "„Láttam Zayd ibn 'Amr ibn Nufaylt")
    e, ne = strip_zayd(e, "Before the Prophet's ministry there were", "\"I saw Zayd ibn 'Amr ibn Nufayl")
    print(f"Zayd ibn 'Amr honorifics removed: HUN {nh}, ENG {ne}")
    # the paragraph after the "I saw Zayd…" report still belongs to his passage
    for name, t_anchor, t_end in (("HUN", "„Láttam Zayd ibn 'Amr ibn Nufaylt", "\n\n"), ("ENG", "\"I saw Zayd ibn 'Amr ibn Nufayl", "\n\n")):
        t = h if name == "HUN" else e
        s = t.index(t_anchor)
        s2 = t.index(t_end, s) + 2          # next paragraph
        e2 = t.index("\n", s2)
        seg, n = ZAYD.subn(r"\1", t[s2:e2])
        t = t[:s2] + seg + t[e2:]
        print(f"  + following paragraph {name}: {n}")
        if name == "HUN":
            h = t
        else:
            e = t
    nj = 0
    for a, b in JAHIL:
        c = h.count(a)
        nj += c
        h = h.replace(a, b)
    print(f"dzsáhilijja replacements: {nj}; leftovers: {len(re.findall('[jJ][aā]hil|dzsāhil', h))}")
    print(f"em dashes → en: {h.count('—')}")
    h = h.replace("—", "–")
    print(f'closing quotes " → ”: {h.count(chr(34))}  (openers „: {h.count("„")})')
    h = h.replace('"', "”")
    if not dry:
        HUN.write_text(h, encoding="utf-8")
        ENG.write_text(e, encoding="utf-8")


if __name__ == "__main__":
    main()
