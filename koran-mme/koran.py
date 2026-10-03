#!/usr/bin/env python3
"""The MME Hungarian Qur'ān translation: build the Markdown from the .doc, look up verses.

  koran.py 2:255            one verse
  koran.py 10:68-70         a range (en dash also accepted)
  koran.py 9                a whole surah
  koran.py build            Koran_MME_1-114_Final.doc → Koran-MME.md (needs LibreOffice + pandoc)
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'Koran_MME_1-114_Final.doc'
OUT = HERE / 'Koran-MME.md'
PANDOC_FALLBACK = HERE.parent / 'fiqh-us-seerah/.build-tools/pandoc-3.6.4/bin/pandoc'

# Verses per surah (Ḥafṣ numbering, 6236 in all).
COUNTS = [7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110,
          98, 135, 112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88,
          75, 85, 54, 53, 89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13,
          14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19,
          36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4,
          7, 3, 6, 3, 5, 4, 5, 6]
SUPERSCRIPT = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')

HEADER = """\
# A Korán magyar fordítása (MME)

Forrás: `Koran_MME_1-114_Final.doc` (ugyanebben a könyvtárban), a `koran.py build` alakította át.
Minden ája egy sor: `szúra:ája szöveg` – pl. `2:255 …`; a nem számozott bászmala `S:0`. A
szögletes zárójeles [kiegészítések] és a kerek zárójeles (magyarázatok) a fordítóéi. Keresés:
`koran.py 2:255`, `koran.py 10:68-70`, `koran.py 9`.
"""


def convert_doc():
    """The .doc is RTF; LibreOffice → docx → pandoc GFM keeps the footnote and the italics."""
    pandoc = 'pandoc' if subprocess.run(['which', 'pandoc'], capture_output=True).returncode == 0 \
        else str(PANDOC_FALLBACK)
    with tempfile.TemporaryDirectory() as tmp:
        rtf = Path(tmp) / 'koran.rtf'
        rtf.write_bytes(SRC.read_bytes())
        subprocess.run(['soffice', '--headless', '--convert-to', 'docx', '--outdir', tmp, str(rtf)],
                       check=True, capture_output=True)
        return subprocess.run([pandoc, str(Path(tmp) / 'koran.docx'), '-t', 'gfm', '--wrap=none'],
                              check=True, capture_output=True, text=True).stdout


def clean(s):
    s = re.sub(r'</?span[^>]*>', '', s)          # editor's highlighting
    s = re.sub(r'\\([.\[\]*_()#!-])', r'\1', s)   # pandoc escapes
    s = s.replace('\u00a0', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def build():
    lines = convert_doc().split('\n')
    notes = {}
    body = []
    for ln in lines:
        m = re.match(r'\[\^(\d+)\]:\s*(.*)', ln)
        if m:
            notes[m.group(1)] = clean(m.group(2))
        else:
            body.append(ln)

    surahs = []          # [num, title, basmala, [(verse, text, [notes])]]
    problems = []
    splits = []
    for raw in body:
        ln = clean(re.sub(r'^(?:#+\s+|>\s*)+', '', raw).replace('**', ''))
        if not ln:
            continue
        nxt = len(surahs) + 1
        m = re.match(r'(\d+)\.\s*(?:szúra\s*[–-]\s*)?(.*?)\s*(?:c\.\s*szúra)?$', ln)
        if m and int(m.group(1)) == nxt and re.search(r'c\.\s*szúra$|^\d+\.\s*szúra\b', ln):
            title = re.sub(r'\s+–\s+\(', ' (', m.group(2))
            surahs.append([nxt, title, None, []])
            continue
        if not surahs:
            problems.append(f'before surah 1: {ln[:80]}')
            continue
        s = surahs[-1]
        if re.fullmatch(r'A Könyörületes(?: és|,) (?:az )?Irgalmas Allah nevében\.', ln):
            if s[2] or s[3]:
                problems.append(f'{s[0]}: stray basmala')
            s[2] = ln
            continue
        m = re.match(r'(\d+)\s*[.,:]?\s*(.*)', ln)
        want = len(s[3]) + 1
        if not m or int(m.group(1)) < want:
            problems.append(f'{s[0]}:{want} expected, got: {ln[:80]}')
            continue
        if int(m.group(1)) > want:
            problems.append(f'{s[0]}:{want}–{int(m.group(1)) - 1} missing')
            s[3].extend((v, None, []) for v in range(want, int(m.group(1))))
            want = int(m.group(1))
        # a few verses are glued onto the previous one: "…vesztesek.38. Mondd…"
        parts = [m.group(2)]
        while g := re.search(rf'(?<=[.!?”])\s*{want + len(parts)}\.\s*(?=\S)', parts[-1]):
            splits.append(f'{s[0]}:{want + len(parts)}')
            parts[-1:] = [parts[-1][:g.start()], parts[-1][g.end():]]
        for i, text in enumerate(parts):
            refs = []

            def ref(r):
                refs.append(notes[r.group(1)])
                return str(len(refs)).translate(SUPERSCRIPT)
            s[3].append((want + i, re.sub(r'\[\^(\d+)\]', ref, text), refs))

    if len(surahs) != 114:
        problems.append(f'{len(surahs)} surahs found')
    for s in surahs:
        if len(s[3]) != COUNTS[s[0] - 1]:
            problems.append(f'surah {s[0]}: {len(s[3])} verses, expected {COUNTS[s[0] - 1]}')
        if not s[2] and s[0] not in (1, 9):
            problems.append(f'surah {s[0]}: no basmala')
    if problems:
        sys.exit(f'build failed ({len(problems)} problems):\n  ' + '\n  '.join(problems[:40]))

    out = [HEADER]
    for num, title, basmala, verses in surahs:
        out.append(f'## {num}. {title}\n')
        if basmala:
            out.append(f'{num}:0 {basmala}\n')
        for v, text, refs in verses:
            out.append(f'{num}:{v} {text}\n')
            for i, note in enumerate(refs, 1):
                out.append(f'> {str(i).translate(SUPERSCRIPT)} {note}\n')
    OUT.write_text('\n'.join(out))
    print(f'split glued verses: {", ".join(splits)}')
    print(f'{OUT.name}: 114 surahs, {sum(len(s[3]) for s in surahs)} verses, {len(notes)} footnote(s)')


def lookup(arg):
    m = re.fullmatch(r'(\d+)(?::(\d+)(?:[-–](\d+))?)?', arg.replace(' ', ''))
    if not m:
        sys.exit(f'bad reference: {arg}')
    s = m.group(1)
    lo = int(m.group(2)) if m.group(2) else 1
    hi = int(m.group(3) or m.group(2) or 999)
    hit = False
    for ln in OUT.read_text().split('\n'):
        k = re.match(r'(\d+):(\d+) ', ln)
        if k:
            hit = k.group(1) == s and lo <= int(k.group(2)) <= hi
        if hit and (k or ln.startswith('> ')):
            print(ln)
        elif ln.startswith('## ') and m.group(2) is None and ln[3:].startswith(s + '.'):
            print(ln)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == 'build':
        build()
    else:
        for a in sys.argv[1:]:
            lookup(a)
