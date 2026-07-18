#!/usr/bin/env python3
"""G4 ḥadīth-grade sweep: extract per-chapter footnote grade labels from
ENG-full and HUN-full, align them, and report mismatches.

Grade canon: S = ṣaḥīḥ/sound/authentic/hiteles, H = ḥasan/good/jó,
W = ḍaʿīf/weak/gyenge. Footnotes with no grade label are '-'.
"""
import re
import sys
import unicodedata

SUP = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
       '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}


def sup_to_int(s):
    return int(''.join(SUP[c] for c in s))


def parse_footnote_blocks(path, chapter_heads, block_head):
    """Return {chapter: {fn_num: text}} for the footnote block following each chapter."""
    lines = open(path, encoding='utf-8').readlines()
    # locate chapter start lines and footnote block starts
    chapters = {}  # ch -> (start_line_idx)
    for i, ln in enumerate(lines):
        m = re.match(r'^# ' + chapter_heads, ln)
        if m:
            chapters[len(chapters) + 1] = i
    result = {}
    ch_items = sorted(chapters.items())
    for idx, (ch, start) in enumerate(ch_items):
        end = ch_items[idx + 1][1] if idx + 1 < len(ch_items) else len(lines)
        # find footnote blocks in [start, end); ch9's block may be at file end (ENG)
        fns = {}
        in_block = False
        for i in range(start, end):
            if lines[i].startswith(block_head):
                in_block = True
                continue
            if in_block:
                if lines[i].startswith('# '):
                    in_block = False
                    continue
                m = re.match(r'^([⁰¹²³⁴⁵⁶⁷⁸⁹]+)\s*(.*)', lines[i])
                if m:
                    fns[sup_to_int(m.group(1))] = m.group(2).strip()
        result[ch] = fns
    return result


# First grade keyword found in the opening of the footnote (Al-Albānī's verdict
# always leads). NS = explicitly negated ("Not authentic" / "Nem hiteles").
ENG_LEAD = re.compile(
    r"(not\s+(?:authentic|sound|ṣaḥīḥ)"
    r"|ṣaḥīḥ|saḥīḥ|sahih|saheeh|sound|authentic"
    r"|ḥasan|hasan|good"
    r"|weak|ḍa'īf|da'īf|da'eef|ḍa'eef)", re.I)
HUN_LEAD = re.compile(
    r"(nem\s+hiteles|hiteles|ṣaḥīḥ|jó\b|ḥasan|gyenge|ḍa'īf|da'īf)", re.I)
CANON = {'ṣaḥīḥ': 'S', 'saḥīḥ': 'S', 'sahih': 'S', 'saheeh': 'S', 'sound': 'S',
         'authentic': 'S', 'hiteles': 'S',
         'ḥasan': 'H', 'hasan': 'H', 'good': 'H', 'jó': 'H',
         'weak': 'W', "ḍa'īf": 'W', "da'īf": 'W', "da'eef": 'W', "ḍa'eef": 'W',
         'gyenge': 'W'}


def grade_of(text, lead_re, prefix=45):
    m = lead_re.search(text[:prefix])
    if not m:
        return '-'
    w = m.group(1).lower()
    if w.startswith('not') or w.startswith('nem'):
        return 'NS'
    return CANON[re.sub(r'\s+', ' ', w)]


def inline_grades(text, lang):
    """Grade words appearing anywhere in the footnote (for context on '-' rows)."""
    if lang == 'eng':
        words = re.findall(r'(ṣaḥīḥ|sound|authentic|ḥasan|hasan\b|weak|ḍa\'īf|da\'eef)',
                           text, re.I)
    else:
        words = re.findall(r'(hiteles|jó\b|gyenge)', text, re.I)
    return sorted(set(w.lower() for w in words))


def main():
    eng = parse_footnote_blocks(
        'FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md',
        r'Chapter (One|Two|Three|Four|Five|Six|Seven|Eight|Nine)\b',
        '## Footnotes')
    hun = parse_footnote_blocks(
        'FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md',
        r'(Első|Második|Harmadik|Negyedik|Ötödik|Hatodik|Hetedik|Nyolcadik|Kilencedik) fejezet',
        '## Lábjegyzetek')

    mismatches = []
    stats = {}
    for ch in range(1, 10):
        e, h = eng.get(ch, {}), hun.get(ch, {})
        nums = sorted(set(e) | set(h))
        print(f'\n=== Chapter {ch}: ENG {len(e)} fns, HUN {len(h)} fns ===')
        for n in nums:
            et, ht = e.get(n), h.get(n)
            if et is None or ht is None:
                # ch3 HUN skips fn15 by design
                if not (ch == 3 and n == 15 and ht is None):
                    print(f'  fn{n}: MISSING in {"ENG" if et is None else "HUN"}')
                continue
            eg = grade_of(et, ENG_LEAD)
            hg = grade_of(ht, HUN_LEAD)
            stats.setdefault(ch, []).append((n, eg, hg))
            if eg != hg:
                mismatches.append((ch, n, eg, hg))
                print(f'  fn{n}: ENG={eg} HUN={hg}')
                print(f'      ENG: {et[:130]}')
                print(f'      HUN: {ht[:130]}')
        graded = [x for x in stats.get(ch, []) if x[1] != '-' or x[2] != '-']
        print(f'  ({len(graded)} graded fns this chapter)')

    print(f'\n{len(mismatches)} leading-label mismatches: {mismatches}')

    # Convention check: untranslated grade terms leading a HUN footnote
    print('\n=== HUN convention scan (untranslated Ṣaḥīḥ/Ḍa\'īf labels) ===')
    for ch in range(1, 10):
        for n, t in sorted(hun.get(ch, {}).items()):
            if re.match(r"^\W{0,3}(Ṣaḥīḥ|Ḍa'īf|Ḥasan)\b(?! *\()", t) \
               and not re.match(r'^\W{0,3}Ṣaḥīḥ(ja|já|s|<)', t):
                print(f'  ch{ch} fn{n}: {t[:110]}')

    # Dump per-chapter grade sequences (for the AR alignment step)
    import json
    seq = {ch: [(n, eg if eg != '-' else hg) for n, eg, hg in stats.get(ch, [])
                if eg != '-' or hg != '-'] for ch in range(1, 10)}
    with open('scripts/g4_graded_fns.json', 'w') as f:
        json.dump(seq, f, ensure_ascii=False, indent=1)
    print('\nWrote scripts/g4_graded_fns.json')


if __name__ == '__main__':
    main()
