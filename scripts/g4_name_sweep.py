#!/usr/bin/env python3
"""G4 step 3: proper-name sweep.

1. Extract capitalized name tokens (and multi-word name phrases) from HUN-full
   and ENG-full.
2. Cluster near-duplicates (edit distance <= 2 on a diacritic-stripped key) to
   surface inconsistent spellings of the same name.
3. Report HUN-vs-ENG asymmetries for name phrases.
"""
import re
import unicodedata
from collections import Counter
from itertools import combinations

NAME_RE = re.compile(
    r"\b[A-ZĀĪŪḤṢḌṬẒʿ'‘][a-zāīūḥṣḍṭẓèéáíóúöüőű'ʿ‘\-]+"
    r"(?:\s+(?:ibn|bint|abū|Abū|abī|Abī|al|Al|ul|adh|ath|az|ar|an)[\-\s][A-ZĀĪŪḤṢḌṬẒ'ʿ‘]?[a-zāīūḥṣḍṭẓ'ʿ‘\-]+)*")

STOP_HU = set('''A Az Egy És Ha Hogy Nem Igen Ekkor Aztán Azután Majd Amikor Miután
Ez Ezek Ezt Ebben Ekként Így Úgy Ők Ő Mi Ti Én Te De Vagy Mert Mivel Bár Noha
Végül Most Már Még Csak Sőt Tehát Ennek Annak Amint Ahogy Előszó Fejezet
Lábjegyzetek Korán Allah Próféta Prófétai Küldött Könyv Isten Uram Urunk Ura
Mindenható Magasztos Napján Nap Paradicsom Pokol Tűz Utolsó Végítélet
Hidzsra Dzsihád Umma Saría Kalifa Tauhid Óh Ó Belé Miért Hol Ki Kik Mit Ne
Vajon Talán Minden Ilyen Olyan Akkor Ott Itt Ime Íme Mekka Mekkába Mekkában
Mekkából Medina Az-e Volt Van Lesz'''.split())
STOP_EN = set('''The A An And If That Not Yes Then After When This These It In
On At By For To From With Chapter Footnotes Preface Glossary Epilogue Allah
Prophet Messenger Book God Lord Almighty Day Paradise Hell Fire Last Judgement
He She They We You I But Or Because Since Although Finally Now Already Still
Only Even So Thus His Her Their Our Your My Who Whom What Why Where How No
Every Such There Here Islam Islamic Muslims Muslim Makkah Madinah Whoever
Indeed Verily O Surely However Moreover Furthermore Nevertheless Meanwhile
Perhaps Some Any All Both Each Most Many Few Other Another Once Twice
Qur'ān Sūrah Sūrat Ḥadīth Ḥadīths Āyāh Āyāt'''.split())


def strip_key(s):
    s = s.replace('ʿ', '').replace('‘', '').replace("'", '')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.lower()


def tokens(path, stop):
    text = open(path, encoding='utf-8').read()
    single = Counter()
    for m in re.finditer(r"[A-ZĀĪŪḤṢḌṬẒ][\w'ʿ‘\-āīūḥṣḍṭẓèéáíóúöüőű]+", text):
        w = m.group(0)
        if w not in stop and len(w) > 2:
            single[w] += 1
    return single


def cluster(counter, label):
    """Group tokens whose diacritic-stripped keys are within edit distance 1."""
    keys = {}
    for w, c in counter.items():
        keys.setdefault(strip_key(w), []).append((w, c))
    # same stripped key, different surface forms -> diacritic inconsistency
    print(f'\n### {label}: same base, different diacritics/spelling')
    for k, forms in sorted(keys.items()):
        if len(forms) > 1:
            total = sum(c for _, c in forms)
            if total >= 2:
                print(f'  {k}: ' + ', '.join(f'{w}×{c}' for w, c in
                                             sorted(forms, key=lambda x: -x[1])))
    # near keys (edit distance 1, length >= 5) - candidate corruptions
    print(f'\n### {label}: edit-distance-1 base pairs (possible corruptions)')
    ks = [k for k in keys if len(k) >= 5]
    def ed1(a, b):
        if abs(len(a) - len(b)) > 1:
            return False
        if len(a) == len(b):
            return sum(x != y for x, y in zip(a, b)) == 1
        if len(a) > len(b):
            a, b = b, a
        for i in range(len(b)):
            if a == b[:i] + b[i+1:]:
                return True
        return False
    seen = set()
    for a, b in combinations(sorted(ks), 2):
        if a[:2] != b[:2]:   # cheap prefix filter
            continue
        if ed1(a, b) and (a, b) not in seen:
            seen.add((a, b))
            fa = sum(c for _, c in keys[a])
            fb = sum(c for _, c in keys[b])
            if min(fa, fb) >= 1 and max(fa, fb) >= 3:
                print(f'  {a} ({fa}) ~ {b} ({fb}): '
                      + ' | '.join(f'{w}×{c}' for w, c in keys[a] + keys[b]))


def main():
    hun = tokens('FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md', STOP_HU)
    eng = tokens('FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md', STOP_EN)
    cluster(hun, 'HUN')
    cluster(eng, 'ENG')


if __name__ == '__main__':
    main()
