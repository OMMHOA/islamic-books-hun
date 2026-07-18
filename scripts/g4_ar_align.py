#!/usr/bin/env python3
"""G4 step 2: align AR footnotes (per-page blockquotes) with ENG per-chapter
footnotes in sequence, and compare ḥadīth-grade verdicts.

AR chapter page map (printed pages, from REVIEW-FLAGS §G / G3 PLAN):
ch1 15-45, ch2 46-70, ch3 71-108, ch4 109-134, ch5 135-158,
ch6 159-246, ch7 247-332, ch8 333-353, ch9 354-364.
"""
import re
import json

AR_DIGITS = '٠١٢٣٤٥٦٧٨٩'
CH_PAGES = {1: (15, 45), 2: (46, 70), 3: (71, 108), 4: (109, 134),
            5: (135, 158), 6: (159, 246), 7: (247, 332), 8: (333, 353),
            9: (354, 364)}


def ar2int(s):
    return int(''.join(str(AR_DIGITS.index(c)) for c in s))


def ar_grade(text):
    """Grade verdict from the opening of an AR footnote."""
    head = text[:60]
    if re.search(r'^(حديث\s+)?(إسناده\s+)?صحيح', head):
        return 'S'
    if re.search(r'^(حديث\s+)?(إسناده\s+)?حسن', head):
        return 'H'
    if re.search(r'^(حديث\s+)?(إسناده\s+)?ضعيف|^هذا حديث ضعيف', head):
        return 'W'
    if re.search(r'^لم يصح|^لا يصح|^ليس بصحيح|^غير صحيح', head):
        return 'NS'
    return '-'


def load_ar(path):
    """[(page, fn_num_on_page, text)] in document order."""
    page = None
    out = []
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'\[صفحة (\d+)\]', ln)
        if m:
            page = int(m.group(1))
            continue
        m = re.match(r'>\s*\(([٠-٩]+)\)\s*(.*)', ln)
        if m and page is not None:
            out.append((page, ar2int(m.group(1)), m.group(2).strip()))
        else:
            m = re.match(r'>\s*\*\s*(.*)', ln)  # unnumbered author-comment fns
            if m and page is not None:
                out.append((page, 0, m.group(1).strip()))
    return out


def main():
    ar = load_ar('FiqhusSeerah-Muhammad-al-Ghazali-AR-full.md')
    graded = json.load(open('scripts/g4_graded_fns.json'))  # ch -> [[n, grade]]

    # also need full ENG fn list per chapter for counting
    import importlib.util
    spec = importlib.util.spec_from_file_location('gs', 'scripts/g4_grade_sweep.py')
    gs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module.__self__ if False else None
    # reuse parser without running main
    import types
    src = open('scripts/g4_grade_sweep.py').read().replace("if __name__ == '__main__':\n    main()", '')
    mod = types.ModuleType('gs')
    exec(src, mod.__dict__)
    eng = mod.parse_footnote_blocks(
        'FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md',
        r'Chapter (One|Two|Three|Four|Five|Six|Seven|Eight|Nine)\b',
        '## Footnotes')

    for ch, (p0, p1) in CH_PAGES.items():
        ar_ch = [(p, n, t) for (p, n, t) in ar if p0 <= p <= p1]
        e = eng[ch]
        print(f'\n=== ch{ch}: AR {len(ar_ch)} fns (pages {p0}-{p1}), ENG {len(e)} fns ===')
        if len(ar_ch) != len(e):
            print('  COUNT MISMATCH — sequence alignment unreliable, listing AR pages:')
            from collections import Counter
            print('  ', dict(sorted(Counter(p for p, _, _ in ar_ch).items())))
            continue
        for i, (p, n, t) in enumerate(ar_ch, start=1):
            ag = ar_grade(t)
            eg = mod.grade_of(e[i], mod.ENG_LEAD)
            if ag != eg and ag != '-' and eg != '-':
                print(f'  ENG fn{i} (AR p.{p} ({n})): AR={ag} ENG={eg}')
                print(f'    AR : {t[:120]}')
                print(f'    ENG: {e[i][:120]}')


if __name__ == '__main__':
    main()
