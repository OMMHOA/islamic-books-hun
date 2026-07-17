#!/usr/bin/env python3
"""G2: Qur'an-reference sweep for FiqhusSeerah HUN + ENG files.

1. Extract every (Korán X: Y[-Z]) / (Qur'ān X: Y[-Z]) ref with line numbers.
2. Validate: surah 1-114, ayah(s) within the surah's Kufan ayah count,
   range start < end.
3. Sequence-align the ENG and HUN ref lists to spot drift/missing refs.
4. Scan for malformed near-miss patterns the strict regex would skip.
"""
import re, sys, difflib

# Kufan/Hafs ayah counts, surahs 1..114
AYAHS = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,
135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,
59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,
44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,
19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]
assert len(AYAHS) == 114

HUN = "/home/condoriano/hobby/islamic-books-hun/FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md"
ENG = "/home/condoriano/hobby/islamic-books-hun/FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md"

REF = re.compile(r"\((?:Korán|Qur'ān)\s*(\d+)\s*:\s*(\d+)(?:\s*[–\-]\s*(\d+))?\)")

def extract(path):
    refs = []
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            for m in REF.finditer(line):
                s, a1 = int(m.group(1)), int(m.group(2))
                a2 = int(m.group(3)) if m.group(3) else None
                refs.append((ln, s, a1, a2, m.group(0)))
    return refs

def validate(refs, label):
    bad = []
    for ln, s, a1, a2, raw in refs:
        if not (1 <= s <= 114):
            bad.append((ln, raw, f"surah {s} out of range")); continue
        maxa = AYAHS[s-1]
        if not (1 <= a1 <= maxa):
            bad.append((ln, raw, f"ayah {a1} > {maxa} (surah {s} max)"))
        if a2 is not None:
            if not (1 <= a2 <= maxa):
                bad.append((ln, raw, f"range end {a2} > {maxa} (surah {s} max)"))
            elif a2 <= a1:
                bad.append((ln, raw, f"range {a1}-{a2} not ascending"))
    print(f"== {label}: {len(refs)} refs, {len(bad)} invalid ==")
    for ln, raw, why in bad:
        print(f"  line {ln}: {raw}  -- {why}")
    return bad

def key(r):  # canonical form for alignment
    _, s, a1, a2, _ = r
    return f"{s}:{a1}" + (f"-{a2}" if a2 else "")

hun, eng = extract(HUN), extract(ENG)
validate(hun, "HUN"); validate(eng, "ENG")

print("\n== ENG <-> HUN sequence alignment (drift check) ==")
he, hh = [key(r) for r in eng], [key(r) for r in hun]
sm = difflib.SequenceMatcher(a=he, b=hh, autojunk=False)
same = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        same += i2 - i1; continue
    eside = [(eng[i][0], he[i]) for i in range(i1, i2)]
    hside = [(hun[j][0], hh[j]) for j in range(j1, j2)]
    print(f"  {tag.upper()}: ENG {eside if eside else '—'}  |  HUN {hside if hside else '—'}")
print(f"  ({same} refs align 1:1)")

print("\n== near-miss pattern scan (possible malformed refs) ==")
loose = re.compile(r"(Korán|Qur'ān|Quran|Koran)[^)\n]{0,20}\d")
for path, label in ((HUN, "HUN"), (ENG, "ENG")):
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            for m in loose.finditer(line):
                seg = line[m.start():m.start()+40]
                if not REF.search(line[max(0,m.start()-1):m.start()+40]):
                    print(f"  {label} line {ln}: ...{seg.strip()}...")
