#!/usr/bin/env python3
"""Front-vowel rule: dry run / apply over the HUN books.

annot.tsv: current base -> Arabic (DMG) or =MANUAL.
Old rule (fatha -> a) must reproduce the current base; the new rule gives the new base.
Usage: fv.py [--apply]   (already applied 2026-10-11; a re-run finds nothing to change)
"""
import re, sys, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '../../..'))
FILES = ['fiqh-us-seerah/FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md',
         'muslim-home/MuslimHome-Muhammad-Salih-al-Munajjid-HUN.md']

CONS = {'ʾ': '', 'ʿ': '', 'b': 'b', 't': 't', 'ṭ': 't', 'ṯ': 'sz', 's': 'sz', 'ṣ': 'sz',
        'j': 'dzs', 'ḥ': 'h', 'h': 'h', 'ḫ': 'kh', 'd': 'd', 'ḍ': 'd', 'ḏ': 'z', 'z': 'z',
        'ẓ': 'z', 'r': 'r', 'š': 's', 'ġ': 'gh', 'f': 'f', 'q': 'k', 'k': 'k', 'l': 'l',
        'm': 'm', 'n': 'n', 'w': 'v', 'y': 'j'}
GEM = {'sz': 'ssz', 'dzs': 'ddzs', 'kh': 'kkh', 'gh': 'ggh'}
LONG = {'ā': 'á', 'ī': 'í', 'ū': 'ú'}
HEAVY = set('ʾʿḥḫġqṣḍṭẓr')
VOW = set('aiuāīū')


def segs(word):
    """DMG word -> list of [kind, letter, geminate]"""
    out = []
    for ch in word:
        if ch in VOW:
            out.append(['V', ch, False])
        elif ch in CONS:
            if out and out[-1][0] == 'C' and out[-1][1] == ch:
                out[-1][2] = True
            else:
                out.append(['C', ch, False])
        else:
            raise ValueError(f'bad char {ch!r} in {word!r}')
    return out


def conv_word(word, front):
    s = segs(word)
    allah = word.endswith('llāh')
    res = []
    n = len(s)
    last = n - 1
    while last > 0 and s[last][0] == 'C' and s[last][1] in 'ʾʿ':
        last -= 1
    for i, (k, ch, gem) in enumerate(s):
        if k == 'C':
            h = CONS[ch]
            if ch == 'w':  # diphthong aw/ew: w after a, before consonant or end, not geminate
                if (not gem and i > 0 and s[i-1][0] == 'V' and s[i-1][1] == 'a'
                        and (i == n-1 or s[i+1][0] == 'C')):
                    h = 'u'
            if gem:
                h = GEM.get(h, h + h if h else '')
            res.append(h)
        else:
            if ch in LONG:
                res.append(LONG[ch] if i < last else ch.translate(str.maketrans('āīū', 'aiu')))
            elif ch == 'a' and front and i < last:
                prev = s[i-1] if i > 0 else None
                nxt = s[i+1]
                blocked = (prev is None or prev[0] == 'V' or prev[1] in HEAVY
                           or nxt[0] == 'V' or nxt[1] in HEAVY
                           or (allah and nxt[1] == 'l' and nxt[2] and i == n-4))
                res.append('a' if blocked else 'e')
            else:
                res.append(ch)
    out = ''.join(res)
    if allah:
        out = out[:-3] + 'lah' if out.endswith('láh') else out
    return out


def conv(dmg, front):
    return re.sub(r'[^\s-]+', lambda m: conv_word(m.group(0), front), dmg)


def cap_like(src, s):
    sp, ss = re.split(r'([- ])', src), re.split(r'([- ])', s)
    if len(sp) != len(ss):
        return s[0].upper() + s[1:] if src[0].isupper() else s
    return ''.join(b[0].upper() + b[1:] if a and b and a[0].isupper() else b for a, b in zip(sp, ss))


# ---------------- suffix harmony ----------------
BACK, FRONT = set('aáoóuú'), set('eéöőüű')


def harmony(stem):
    for ch in reversed(stem.lower()):
        if ch in BACK:
            return 'B'
        if ch in FRONT:
            return 'F'
    return 'F'


SUFMAP = [  # back -> front (unrounded e-stems), longest first
    ('jaiknak', 'jeiknek'), ('jainak', 'jeinek'), ('jának', 'jének'), ('jából', 'jéből'),
    ('jában', 'jében'), ('jához', 'jéhez'), ('jával', 'jével'), ('jától', 'jétől'),
    ('jára', 'jére'), ('járól', 'jéről'), ('jait', 'jeit'), ('jai', 'jei'), ('ját', 'jét'),
    ('ja', 'je'), ('juk', 'jük'), ('jukat', 'jüket'),
    ('oknak', 'eknek'), ('okkal', 'ekkel'), ('okat', 'eket'), ('okhoz', 'ekhez'), ('októl', 'ektől'),
    ('ok', 'ek'), ('akat', 'eket'), ('ak', 'ek'),
    ('nak', 'nek'), ('ban', 'ben'), ('ból', 'ből'), ('ba', 'be'), ('ról', 'ről'), ('ra', 're'),
    ('tól', 'től'), ('hoz', 'hez'), ('nál', 'nél'), ('val', 'vel'), ('on', 'en'), ('ot', 'et'),
    ('at', 'et'), ('iak', 'iek'), ('ival', 'ivel'), ('inak', 'inek'), ('ihoz', 'ihez'),
    ('itól', 'itől'), ('ira', 'ire'), ('iról', 'iről'), ('ival', 'ivel'), ('iban', 'iben'),
    ('ijával', 'ijével'),
]
NEUTRAL_SUF = {'', 't', 'i', 'é', 'ék', 'ig', 'ért', 'ként', 'ét', 'n', 'ien', 'it', 'nek', 'nél',
               'ben', 'ből', 'be', 're', 'ről', 'től', 'hez', 'vel', 'et', 'ek', 'eket', 'en', 'je',
               'ji', 'iért', 'iek', 'ival'}


BACK_SUF = {b for b, f in SUFMAP} | {'al', 'éban', 'ékhoz', 'nál', 'át', 'ának', 'ával', 'ához', 'ától',
            'ára', 'áról', 'ában', 'ából', 'ába', 'án', 'áig', 'áért', 'áé', 'ái', 'áit', 'ája', 'áját',
            'ájának', 'ájában', 'ájával', 'áról', 'ánál', 'ával', 'ául', 'ul', 'ság', 'ságát',
            'jába', 'k', 'kat', 'knak', 'kkal', 'król', 'któl', 'khoz', 'kra', 'iakat', 'iaknak', 'iaktól', 'iakkal', 'iakra', 'iakhoz', 'ijja', 'ijjával'}
ALLOWED = BACK_SUF | NEUTRAL_SUF | {f for b, f in SUFMAP}


def refit(old_stem, new_stem, suf):
    """return (suffix, ok)"""
    core0 = suf.lstrip('-')
    if not (core0 in ALLOWED or re.fullmatch(r'(.)\1?al', core0) or re.fullmatch(r'(.)\1?el', core0)):
        return suf, None
    if harmony(old_stem) == harmony(new_stem) or not suf:
        return suf, True
    if harmony(new_stem) == 'F':
        core = suf.lstrip('-')
        dash = suf[:len(suf)-len(core)]
        # assimilated instrumental: Xal after consonant X  (Anasszal -> Anesszel)
        m = re.fullmatch(r'(.)\1?al', core)
        if (m and core not in ('val',)) or core == 'al':
            return dash + core[:-2] + 'el', True
        if core in ('éban', 'ékhoz'):
            return dash + {'éban': 'ében', 'ékhoz': 'ékhez'}[core], True
        for b, f in SUFMAP:
            if core == b:
                return dash + f, True
        if core in NEUTRAL_SUF:
            return suf, True
        return suf, False
    return suf, False


LET = 'A-Za-zÁÉÍÓÖŐÚÜŰáéíóöőúüű'


def load():
    rows = []
    for line in open(os.path.join(HERE, 'annot.tsv')):
        if line.startswith('#') or not line.strip():
            continue
        base, dmg = line.rstrip('\n').split('\t')
        rows.append((base, dmg))
    return rows


def main():
    apply = '--apply' in sys.argv
    rows = load()
    mapping = {}
    problems = []
    for base, dmg in rows:
        if dmg.startswith('='):
            new = dmg[1:]
        else:
            old = cap_like(base, conv(dmg, False))
            new = cap_like(base, conv(dmg, True))
            if old != base:
                problems.append(f'ROUNDTRIP {base}: old rule gives {old}')
                continue
        if new != base:
            mapping[base] = new
    for p in problems:
        print(p)
    bases = sorted(mapping, key=len, reverse=True)
    pat = re.compile(r'(?<![' + LET + r'])(' + '|'.join(
        re.escape(b) + ('|' + re.escape(b[:-1] + 'á') if b.endswith('a') else '') for b in bases)
        + r')([' + LET + r'-]*)')
    report = collections.Counter()
    bad = collections.Counter()
    skipped = collections.Counter()
    for f in FILES:
        path = os.path.join(REPO, f)
        text = open(path).read()

        def rep(m):
            tok, rest = m.group(1), m.group(2)
            if tok in mapping:
                b, new = tok, mapping[tok]
            else:  # lengthened final a
                b = tok[:-1] + 'a'
                new = mapping[b][:-1] + 'á'
            # a hyphenated rest: only the part up to the first hyphen is a suffix
            suf, tail = (rest.split('-', 1) + [''])[:2] if '-' in rest else (rest, None)
            nsuf, ok = refit(b, mapping[b], suf)
            if ok is None:
                skipped[f'{tok}{rest}'] += 1
                return m.group(0)
            if tail is not None and tail and not re.match(r'[a-záéíóöőúüű]', tail[0]):
                pass
            out = new + nsuf + ('-' + pat.sub(rep, tail) if tail is not None else '')
            key = f'{tok}{rest} → {out}'
            if not ok:
                bad[f'{f.split("/")[0]}: {key}'] += 1
            report[key] += 1
            return out

        new_text = pat.sub(rep, text)
        if apply:
            open(path, 'w').write(new_text)
    with open(os.path.join(HERE, 'report.txt'), 'w') as fh:
        for k, c in sorted(report.items(), key=lambda x: x[0].lower()):
            fh.write(f'{c:4}  {k}\n')
    print(f'{len(mapping)} bases change; {sum(report.values())} tokens ({len(report)} distinct)')
    for k, c in bad.items():
        print('SUFFIX?', c, k)
    print('SKIPPED (not base+suffix):', ' '.join(f'{k}:{c}' for k, c in sorted(skipped.items())))


if __name__ == '__main__':
    main()
