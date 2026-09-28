#!/usr/bin/env python3
"""Apply the reviewed names list (review-wip/names.md, user edits 2026-09-28) to the HUN file.

    python3 names_apply.py           # dry run: writes names-apply-report.txt only
    python3 names_apply.py --write   # also rewrites the HUN file

Decisions on top of names.md (user, 2026-09-28): every word-final long vowel in a name is shortened
(Bukhári, Iszra) except the particle Banú; all 16 „Izrael fiai” / Banū Isrā'īl → a Banú Iszráíl.
Lines of names.md the user edited are taken verbatim; unedited lines get the final-vowel rule.
"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import names_build as nb  # noqa: E402

HUN = nb.ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md"
LIST = HERE / "names.md"
REPORT = HERE / "names-apply-report.txt"
VOWELS = set("aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ")
SHORT = {"á": "a", "í": "i", "ú": "u"}


def shorten(w):
    """Word-final long vowel → short (user decision 2026-09-28)."""
    return re.sub(r"[áíú](?=$|-)", lambda m: SHORT[m.group()], w)


def rule(w):
    hu = re.search(r"(?<=[^aeiouāīū'ʿj])j[áé]\w*$", w)  # a Hungarian ending on an unrecognised stem: …jában
    if hu:
        return rule(w[:hu.start()]) + hu.group()
    t = nb.translit(w)
    if re.search(r"ll[aā]h$", w, re.I):  # Allah compounds are spelled like Allah
        t = re.sub(r"ll[aá]h?$", "llah", t)
    src, out = w.split("-"), t.split("-")
    if len(src) == len(out):  # capitals after a hyphen survive: 'Abdul-Rahmān → Abdul-Rahmán
        out = [o[:1].upper() + o[1:] if i and s.lstrip("'ʿ")[:1].isupper() else o
               for i, (s, o) in enumerate(zip(src, out))]
        t = "-".join(out)
    t = t.replace("lláh", "llah")
    # shorten a final long vowel only where the source had one (not a Hungarian ending: kaszídákká)
    src = nb.FIX_SPELLING.get(w, w).split("-")
    out = t.split("-")
    if len(src) == len(out):
        t = "-".join(shorten(o) if re.search(r"[āīūĀĪŪ]['ʿ]?$", s) else o for s, o in zip(src, out))
    return t


# ---------------------------------------------------------------- the reviewed list

def generated_lines():
    tmp = HERE / ".names-gen.tmp"
    out, nb.OUT = nb.OUT, tmp
    try:
        nb.main()
        return set(tmp.read_text(encoding="utf-8").splitlines())
    finally:
        nb.OUT = out
        tmp.unlink(missing_ok=True)


EXPECTED_ANSWERS = ["Huszrau", "négus", "a Tauba szúra, a Lahab szúra, a Marjam szúra, a Húd szúra", "lowercase",
                    "Banú Iszráíl", "the rule", "Muhammad al-Ghazáli", "yes, the rule", "replace with a note"]


def parse_list():
    """→ (FORMS: spelling → Hungarian, PROPHETS: spelling → (biblical, other))."""
    gen = generated_lines()
    forms, prophets, answers = {}, {}, []
    sec = 0
    for line in LIST.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            sec = int(line[3]) if line[3].isdigit() else 0
            continue
        edited = line not in gen
        bolds = re.findall(r"\*\*(.+?)\*\*", line)
        if sec == 1 and line.startswith("→ **"):
            answers.append(bolds[0])
            continue
        if sec < 2 or not line.startswith("- ") or not bolds:
            continue
        left = line[2:line.index(" → ")]
        if sec == 2:
            spellings = next(sp for sp, _ in nb.TRADITIONAL if sp[0] == left)
            for s in spellings:
                forms[s] = bolds[0]
        elif sec == 3:
            spellings = next(sp for lab, sp, _ in nb.PROPHETS if lab == left)
            fix = (lambda x: x) if edited else shorten
            if len(bolds) == 2:
                pair = (bolds[0], fix(bolds[1]))
            elif "only other people" in line:
                pair = (None, fix(bolds[0]))
            elif "no biblical form" in line:
                pair = (fix(bolds[0]), fix(bolds[0]))
            else:
                pair = (bolds[0], None)
            for s in spellings:
                prophets[s] = pair
        elif sec in (4, 5, 6):
            spellings = left.split(", ")
            target = bolds[0]
            targets = target.split(", ") if target.count(", ") == len(spellings) - 1 > 0 else \
                target.split(" / ") if target.count(" / ") == len(spellings) - 1 > 0 else [target] * len(spellings)
            for s, t in zip(spellings, targets):
                t = re.sub(r"\(ok\)$", "", t)
                if not edited:
                    t = shorten(t)
                forms[s] = ("al-" + t) if re.match(r"^[Aa]l-", s) else t
    assert answers == EXPECTED_ANSWERS, answers  # section 1 is hand-coded below; re-check if the user changes it
    return forms, prophets


# ---------------------------------------------------------------- hand-made replacements (run before the word pass)

GLOSSARY = {  # headword → Hungarian headword (text terms like ima/Paradicsom keep the Arabic term as headword)
    "Āyāt": "Áják", "Adhān": "Azán", "Aḥzāb": "Ahzáb", "Al Mīzān": "Al-Mízán", "Allāh": "Allah", "Arafah": "Arafa",
    "Dīn": "Dín", "Da'wah": "Dáwa", "Dhirā'": "Dirá", "Dhuhr": "Zuhr", "Dhul Qa'dah": "Zul-kada", "Dinars": "Dínár",
    "Ḥanīf": "Haníf", "Ḥarām": "Harám", "Ḥirā": "Hira", "Hijri": "Hidzsri", "Ḥūr": "Húr", "Huffādh": "Huffáz",
    "Imām": "Imám", "Isrā'": "Iszra", "'Issa": "Ísza", "Janābah": "Dzsanába", "Jannah": "Dzsanna",
    "Jizyah": "Dzsizja", "Jumada I & II": "Dzsumáda I. és II.", "Khilāfah": "Khiláfa", "Lāt és 'Uzza": "Lát és Uzza",
    "Maḥram": "Mahram", "Maghazī": "Magházi", "Mir'āj": "Mirádzs", "Miswāk": "Miszvák", "Mu'jiza": "Mudzsiza",
    "Mu'adhdhin": "Müezzin", "Mudhammam": "Muzammam", "Muhajirīn": "Muhádzsirok", "Muḥarram": "Muharram",
    "Mushrikūn": "Musrikún", "Nuṭfah": "Nutfa", "Qaṣīdahs": "Kaszídák", "Rak'ah": "Rakát", "Ramaḍān": "Ramadán",
    "Ṣalāh": "Szaláh", "Ṣaḥābī": "Szahába", "Riḍwān": "Ridván", "Sīrah": "Szíra", "Sūrah": "Szúra", "Safā": "Szafa",
    "Salām": "Szalám", "Salāsil": "Szalászil", "Sha'bān": "Sabán", "Shawwāl": "Savvál",
    "Subḥānallāh": "Szubhánallah", "Tahajjud": "Tahaddzsud", "Tayammum": "Tajammum", "Umrah": "Umra",
    "Uqiyah": "Ukija", "Zakāt al fitr": "Zakát al-fitr",
}

TRANSLIT_NOTE = """# A nevek átírásáról

A magyar szövegben az arab neveket és szakkifejezéseket egyszerűsített magyar átírással írjuk, mellékjelek
nélkül, úgy, hogy magyarul olvasva közel járjanak az arab kiejtéshez:

- a hosszú magánhangzót ékezet jelöli (á, í, ú), a szó végén azonban rövid (al-Bukhári, Músza);
- ث sz, ج dzs, ح h, خ kh, ذ z, ش s, ص sz, ض d, ط t, ظ z, غ gh, ق k, و v, ي j; a szóvégi ة -a (Hamza);
- az ajn (ع) és a hamza (ء) jelét elhagyjuk (Szad, Kab);
- a névelő mindig al-, akkor is, ha a kiejtésben hasonul (al-Zubajr);
- a prófétáknál a magyarul meghonosodott bibliai nevet használjuk (Ábrahám, Mózes, József), az azonos nevű
  más személyeknél az átírást (Ibn Iszhák, Abu Músza);
- néhány név a megszokott magyar alakjában szerepel: Mohamed (a Próféta), Omár, Oszmán, Ali, Áisa,
  Ibn Kathir, al-Tirmidhi, Jathrib, Mekka, Medina.

"""

SYMBOLS = [  # „A könyvben használt jelek” — the Arabic formulas, by the rule
    ("Subḥānahu wa Ta'ālā", "Szubhánahu va Taála"), ("Ṣallā-Allāhu 'Alayhi wa Sallam", "Szalla-Allahu Alajhi va Szallam"),
    ("'Alayhis-Salām", "Alajhisz-Szalám"), ("Raḍiya Allāhu 'Anhū", "Radija Allahu Anhu"),
    ("Raḍiya Allāhu 'Anhā", "Radija Allahu Anha"), ("Raḍiya Allāhu 'Anhum", "Radija Allahu Anhum"),
]

MANUAL = [  # (old, new, expected count) — exact text, applied in order before the word pass
    # question 3: surah names
    ("a Sūrat ul-Lahabot", "a Lahab szúrát", 1), ("a Sūrah Hūdnál", "a Húd szúránál", 1),
    ("A Sūrat al-Tawbah sok", "A Tauba szúra sok", 1), ("a Sūrat al-Tawbah,", "a Tauba szúra,", 1),
    ("a Sūrat al-Tawbah elején", "a Tauba szúra elején", 1),
    ("a Sūrah Fuṣṣilat nyitó āyātjait (verseit)", "a Fusszilat szúra nyitó ájáit", 1),
    ("A Sūrah Al Najmban", "A Nadzsm szúrában", 1), ("a Sūrah Al Najmot", "a Nadzsm szúrát", 1),
    ("a Sūrah Maryam egy", "a Marjam szúra egy", 1), ("a Sūrat al Isrā' tafszírjában", "az Iszra szúra tafszírjában", 1),
    ("a Sūrah al Nisāból", "a Nisza szúrából", 1), ("a Sūrah al Tūrt", "a Túr szúrát", 1),
    ("a Sūrah Barā'ah első", "a Baráa szúra első", 1), ("a Sūrat al Aḥzāb āyātjait", "az Ahzáb szúra ájáit", 1),
    ("(többes sz. Sūrahs)", "(többes sz. szúrák)", 1),
    # question 4: month names, lowercase
    ("Rabī' al-Awwal", "rabi al-avval", 4), ("Ramaḍān", "ramadán", 7), ("Shawwāl", "savvál", 8),
    ("Muḥarram havában", "muharram havában", 1), ("Ṣafar hav", "szafar hav", 2), ("Rajab", "radzsab", 4),
    ("Jumādā és Sha'bān", "dzsumáda és sabán", 1), ("Sha'bān havában", "sabán havában", 1),
    ("6. Jumādában", "6. Dzsumádában", 1), ("Jumādā I havában", "dzsumáda I. havában", 1),
    ("Dhul Qi'dah", "zul-kada", 2), ("Dhul Q'adában", "zul-kadában", 1), ("*: Dhul-Ḥijjah", "*: Zul-hiddzsa", 1),  # the only one starts a glossary definition
    # question 5: Banú Iszráíl (collective, singular verb — like „a Banū Quraydhah megszegte”)
    ("„Izrael fiai azért tévelyedtek el, mert bizonyos könyveket örököltek atyáiktól.",
     "„A Banú Iszráíl azért tévelyedett el, mert bizonyos könyveket örökölt atyáitól.", 1),
    ("kifejezetten Izrael Fiaihoz jöttek", "kifejezetten a Banú Iszráílhoz jöttek", 1),
    ("Izrael Fiaitól Ismā'īl", "a Banú Iszráíltól Ismā'īl", 1),
    ("szövetséget kötött Izrael Fiainak prófétáival", "szövetséget kötött a Banú Iszráíl prófétáival", 1),
    ("amit a Banū Isrā'īl mondott", "amit a Banú Iszráíl mondott", 1),
    ("míg Izrael fiai érzelmeikkel, nyelvükkel és propagandájukkal Mohamed (ﷺ) és társai ellen fordultak",
     "míg a Banú Iszráíl érzelmeivel, nyelvével és propagandájával Mohamed (ﷺ) és társai ellen fordult", 1),
    ("kiváltképp Izrael fiai –", "kiváltképp a Banú Iszráíl –", 1),
    ("hogy Izrael fiai választásukat annak értelmének és következményeinek tökéletes megértésével hozták meg",
     "hogy a Banú Iszráíl választását annak értelmének és következményeinek tökéletes megértésével hozta meg", 1),
    ("Izrael fiainak magatartása a múltban és a jelenben aláírt szerződéseikkel szemben",
     "A Banú Iszráíl magatartása a múltban és a jelenben aláírt szerződéseivel szemben", 1),
    ("figyelmünket Izrael fiainak erre a megvetendő vonására", "figyelmünket a Banú Iszráíl e megvetendő vonására", 1),
    ("mészárlást rendelt Izrael fiainak.", "mészárlást rendelt a Banú Iszráílnak.", 1),
    ("amelyet Izrael fiai Khaybarnál elszenvedtek, teljesen megsemmisítette katonai erejüket",
     "amelyet a Banú Iszráíl Khaybarnál elszenvedett, teljesen megsemmisítette katonai erejét", 1),
    ("alkalmazták Izrael fiaira, amikor elhanyagolták a Tóra útmutatásait, és saját vágyaikat követték",
     "alkalmazták a Banú Iszráílra, amikor elhanyagolta a Tóra útmutatásait, és saját vágyait követte", 1),
    ("Izrael fiai hatalmas királyok voltak, azután megfosztattak királyságuktól és hatalmuktól, hogy az iszlám "
     "növekvő állama örökölje őket",
     "A Banú Iszráíl hatalmas királyok népe volt, azután megfosztatott királyságától és hatalmától, hogy az iszlám "
     "növekvő állama örökölje", 1),
    ("amelyet Izrael fiai kamatra épülő üzleteiken és erkölcstelen jellemükön keresztül exportálnak",
     "amelyet a Banú Iszráíl kamatra épülő üzletein és erkölcstelen jellemén keresztül exportál", 1),
    ("Izrael fiai vereséget szenvedtek,", "A Banú Iszráíl vereséget szenvedett,", 1),
    # āyāt: Hungarian plural áják, singular after quantifiers; the (vers…) glosses merge
    ("ezekkel az Āyāt-okkal (versekkel)", "ezekkel az ájákkal", 1),
    ("néhány koráni āyāt", "néhány koráni ája", 1), ("a többi āyāt", "a többi ája", 1),
    ("Számos koráni āyāt", "Számos koráni ája", 1), ("ezer āyāt", "ezer ája", 1),
    ("dezertálókról a következő āyāt nyilatkoztatott ki", "dezertálókról a következő ája nyilatkoztatott ki", 1),
    ("bíztak, a következő āyāt nyilatkoztatott ki", "bíztak, a következő áják nyilatkoztattak ki", 1),  # Q3:172–174
    ("később a következő āyāt nyilatkoztatott ki", "később a következő ája nyilatkoztatott ki", 1),
    ("a következő āyātot", "a következő áját", 1), ("a Korán āyātját", "a Korán ájáját", 1),
    ("āyāt (vers)", "ája", 1), ("āyātban (versben)", "ájában", 2),
    ("āyātjai (versei)", "ájái", 2), ("Āyāt-jai (versei)", "ájái", 1), ("āyātokat (verseket)", "ájákat", 3),
    ("āyāt (versek)", "áják", 4), ("Āyāt (versek)", "áják", 4), ("āyāk (versek)", "áják", 1),
    ("āyātjaival", "ájáival", 1), ("āyātjait", "ájáit", 2), ("āyātokat", "ájákat", 3), ("āyātokból", "ájákból", 1),
    ("āyātok", "áják", 4), ("āyākat", "ájákat", 1), ("āyāk", "áják", 3), ("āyāt", "áják", 3),
    # dhirā': „könyök (dirá)” at the first mention (its footnote explains the word), „könyök” after
    ("100 dhirā'³", "100 könyök (dirá)³", 1), ("3 dhirā' mélyre", "3 könyök mélyre", 1),
    ("A dhirā' egy könyöknyi", "A dirá egy könyöknyi", 1), ("Egy dhirā' egy könyöknyivel", "Egy dirá egy könyöknyivel", 1),
    # Arabic article glued with a hyphen
    ("zakāt-al fitr", "zakát al-fitr", 1),
    # Ṣalāh here is the blessing on the Prophet, not the prayer; glosses that would only repeat „ima”
    ("a *Ṣalāh* és *Salām* áldáskívánást", "a *szaláh* és *szalám* áldáskívánást", 1),
    ("az imám [Ṣalāt]", "az imám", 1), ("imádkozzatok (*ṣalāh*)", "imádkozzatok", 1),
    ("(többes sz. Rak'āt) ", "", 1), ("társak (ṣaḥāba)", "társak (szahábák)", 2),
    ("erre az Āyāra (versre)", "erre az ájára", 1), ("(többes sz. Ṣaḥābah)", "(többes sz. szahábák)", 1),
    ("Fatḥ-al Barit", "Fath al-Bárit", 1), ("Fatḥ-al Bariban", "Fath al-Báriban", 2),
    ("Ḥakim ibn Ḥizām", "Ḥakīm ibn Ḥizām", 1), ("(egyes sz. Muhajir)", "(egyes sz. muhádzsir)", 1),
    ("114 Sūrahra", "114 szúrára", 1), ("qadianizmus", "kadianizmus", 1),
    ("# Fiqh-us-Seerah –", "# Fikh al-Szíra –", 1),  # question 6: the title by the rule (فقه السيرة)
    # adjectives in -i: a name ending in -i takes no second -i (like helsinki); multi-word names keep -i with a hyphen
    ("a Rajī'-i ütközetben", "a radzsi ütközetben", 1), ("Bi'r Ma'ūnah-i", "Bir Maúna-i", 1),
]

SPECIAL_FORMS = {  # beyond names.md: questions 1, 2, 7 and a few spellings the rule would get wrong
    "Khosrau": "Huszrau", "Negus": "négus", "Al-Ghazali": "al-Ghazáli", "Al-Ghazālī": "al-Ghazáli",
    "Ghazālī": "Ghazáli", "Naṣir-ud-Dīn": "Násziruddín", "inshā'Allah": "insallah", "inshā'allah": "insallah",
    "inshāllah": "insallah", "da'wája": "dáwája", "ṣaḥāba": "szahába", "Ishāq": "Iszhák",
    "ʿUthmān": "Oszmán", "Hassan": "Haszan",  # Hassan: Ḥasan son of 'Alī (ch2)
    "aylaiak": "ajlaiak",  # the people of Aylah (the bare name doesn't occur)
    "Isrā'īl": "Iszráíl", "ḥadždzs": "haddzs", "anṣār": "anszár",
    "Abū": "Abu", "Abī": "Abi", "Banū": "Banú", "Banu": "Banú", "Dhū": "Zu", "Dhul": "Zul",
}
PARTICLE_TOKENS = {"Abū", "Abī", "Banū", "Banu", "Dhū", "Dhul"}
HYPHEN_SUFFIXES = {"t", "tól", "val", "i", "jal", "ban", "okkal", "jában", "jai", "jához", "sal", "nál", "hal"}
NO_LENGTHEN = re.compile(r"^(i($|a|e)|ként|kor|szerű)")  # adjective -i(ak), not -ig
ABBREV = {"sz", "pl", "vö", "ún", "ld", "ill", "kb"}


# ---------------------------------------------------------------- Hungarian morphology helpers

def harmony(w):
    """'back', 'front', or None for neutral vowels only (i, í, é): the last non-neutral vowel decides."""
    for c in reversed(w.lower()):
        if c in "aáoóuú":
            return "back"
        if c in "eöőüű":
            return "front"
    return None


FRONT = str.maketrans("aáoóuú", "eéeőüű")
TO_BACK = {"nek": "nak", "hez": "hoz", "höz": "hoz", "től": "tól", "ből": "ból", "ről": "ról", "be": "ba",
           "ben": "ban", "re": "ra", "nél": "nál", "INSTRel": "INSTRal", "en": "on", "ön": "on"}
TO_FRONT = {"nak": "nek", "hoz": "hez", "tól": "től", "ból": "ből", "ról": "ről", "ba": "be", "ban": "ben",
            "ra": "re", "nál": "nél", "INSTRal": "INSTRel", "on": "en"}


def instrumental(n, vowel):
    if n[-1] in VOWELS:
        return lengthen(n) + "v" + vowel
    for dg in ("dzs", "sz", "zs", "cs", "gy", "ly", "ny", "ty"):
        if n.endswith(dg):
            return n + vowel if n.endswith(dg[0] + dg) else n[:-len(dg)] + dg[0] + dg + vowel
    return n + vowel if len(n) > 1 and n[-1] == n[-2] else n + n[-1] + vowel


def lengthen(n):
    return n[:-1] + {"a": "á", "e": "é"}[n[-1]] if n[-1] in "ae" else n


def adjective_base(stem, known):
    """yathribi → ('Yathrib', 'i'), aylaiak → ('Aylah', 'iak'): a lowercase -i(ak) adjective of a known name."""
    m = re.match(r"^('?)(.+?)(i|iak|iek)$", stem)
    if not m:
        return None
    b = m.group(1) + m.group(2)[:1].upper() + m.group(2)[1:]  # 'aqaba → 'Aqaba
    for cand in (b, b + "h", b[:-1] + "ah" if b.endswith("a") else None):
        if cand and cand in known:
            return cand, m.group(3)
    return None


def split(tok, stem):
    """→ the suffix part of tok (Ḥamzát ← Ḥamzah + t), or None if tok doesn't parse."""
    if tok.startswith(stem):
        return tok[len(stem):]
    for tail in ("āh", "ah", "a", "ā", "e"):
        if stem.endswith(tail):
            base = stem[:-len(tail)]
            if tok.startswith(base) and tok[len(base):len(base) + 1] in ("á", "é"):
                return tok[len(base) + 1:]
    return None


def attach(n, suf, stem):
    """Hungarian form n + the suffix the old word carried, re-fitted to n."""
    if not suf:
        return n
    if suf.startswith("-"):
        if suf[1:] not in HYPHEN_SUFFIXES:
            return n + suf  # compound: Hudajbija-történet
        suf = suf[1:]
    old = rule(stem)
    old_vowel_end = stem[-1] in "aeiouāīūáéíóú"
    m = re.match(r"^([b-df-hj-np-tv-z])(al|el)$", suf)
    if m and (not old_vowel_end or m.group(1) == "v"):
        suf = "INSTR" + m.group(2)
    elif suf in ("val", "vel"):
        suf = "INSTR" + suf[1:]
    word = re.sub(r"^[Aa]l-", "", n)  # the article doesn't count for vowel harmony (al-Hidzsrben)
    if harmony(word) == "front" and harmony(old) == "back":  # Mūsānak → Mózesnek
        suf = suf.translate(FRONT)
    # a case ending always follows the word (the text has „Quraishhez” beside „Quraishhoz”)
    suf = {"back": TO_BACK, "front": TO_FRONT}.get(harmony(word), {}).get(suf, suf)
    if suf.startswith("INSTR"):
        return instrumental(n, suf[5:])
    if n[-1] in VOWELS:
        if not old_vowel_end:
            suf = re.sub(r"^[oeöa](?=[tnk])", "", suf)  # Usāmahot → Uszamát
        if not NO_LENGTHEN.match(suf):
            n = lengthen(n)
    return n + suf


def sentence_start(text, pos):
    j = pos - 1
    quote = False
    while j >= 0 and text[j] in " *„»([\"'_":
        quote |= text[j] == "„"
        j -= 1
    if j < 0 or text[j] in "\n#":
        return True
    if text[j] in "!?…" or (text[j] == ":" and quote):
        return True
    if text[j] == ".":
        word = re.search(r"(\w+)\.$", text[max(0, j - 6):j + 1])
        if word and word.group(1).isdigit():  # „13. ája” — an ordinal, unless it numbers a list item
            return text[max(0, j - len(word.group(1)) - 1):j - len(word.group(1))] in ("", "\n")
        return not (word and word.group(1) in ABBREV)
    if text[j] in "⁰¹²³⁴⁵⁶⁷⁸⁹":  # footnote text: ¹² at the line start
        k = j
        while k >= 0 and text[k] in "⁰¹²³⁴⁵⁶⁷⁸⁹":
            k -= 1
        return k < 0 or text[k] == "\n"
    return False


def prophet_kind(text, pos, end):
    pre, post = text[max(0, pos - 12):pos], text[end:end + 25]
    around = text[max(0, pos - 40):end + 30]
    if (re.search(r"(Abū|Abu|Abī|Abi|Ibn|ibn|bint|Umm|Banū|Banu) $", pre)
            or re.match(r"\s*(ibn|bin|bint)\b", post) or any(x in around for x in nb.PERSON_CTX)):
        return "person"
    return "prophet"


# ---------------------------------------------------------------- the passes

def main(write):
    forms, prophets = parse_list()
    forms.update(SPECIAL_FORMS)
    text = HUN.read_text(encoding="utf-8")
    log = collections.defaultdict(collections.Counter)

    # 1) back matter: symbols, transliteration table, glossary headwords — inserted as placeholders, so the
    #    word pass can't convert them a second time (Dáwa, Kathir), and put back at the end
    held = []

    def hold(s):
        held.append(s)
        return f"\x00{chr(0xE000 + len(held) - 1)}\x00"

    for a, b in SYMBOLS:
        assert text.count(a) == 1, a
        text = text.replace(a, hold(b))
    t0, t1 = text.index("# Átírási táblázat"), text.index("# Szójegyzék")
    text = text[:t0] + hold(TRANSLIT_NOTE) + "---\n\n" + text[t1:]
    g0 = text.index("# Szójegyzék")
    gloss = text[g0:]
    for a, b in GLOSSARY.items():
        n = gloss.count(f"\n*{a}*:")
        assert n == 1, (a, n)
        gloss = gloss.replace(f"\n*{a}*:", f"\n*{hold(b)}*:")
    text = text[:g0] + gloss

    # 2) hand-made replacements
    for a, b, n in MANUAL:
        got = text.count(a)
        assert got == n, (a, got, n)
        text = text.replace(a, b)
        log["manual"][f"{a}  →  {b}"] += n

    # 3) „Al X” / „al X” → al-X (then the word pass decides the case)
    text, n = re.subn(r"(?<![\w'])([Aa]l) (?=['ʿ]?[A-ZĀĪŪḤṬṢḌẒ])", r"\1-", text)
    log["article"][f"Al X → al-X"] += n

    # 4) the word pass
    groups, tok2stem = nb.collect(text, broad=True)

    def root(s):
        seen = set()
        while s in tok2stem and tok2stem[s] != s and s not in seen:
            seen.add(s)
            s = tok2stem[s]
        return s

    edits = []
    for m in nb.W.finditer(text):
        tok = m.group()
        if tok in PARTICLE_TOKENS:
            stem, suf = tok, ""
        elif tok in tok2stem:
            stem = root(tok)
            suf = split(tok, stem)
            if suf is None:
                log["UNPARSED (left as is)"][tok] += 1
                continue
        else:
            continue
        if stem in prophets:
            bib, other = prophets[stem]
            kind = prophet_kind(text, m.start(), m.end())
            n = (bib if kind == "prophet" else other) or (other if bib is None else bib)
            if n is None:
                n = rule(stem)
            log["prophets"][f"{tok} ({kind}) → {attach(n, suf, stem)}"] += 1
        elif stem in forms:
            n = forms[stem]
        elif stem in ("Āyah", "Āyāh", "Ṣaḥābī", "Da'wah", "Zakāh", "Zakāt"):  # the term capitalised mid-sentence
            n = forms[stem[:1].lower() + stem[1:]]
        elif stem.lstrip("'")[:1].islower() and adjective_base(stem, set(forms) | set(groups)):  # yathribi
            base, ending = adjective_base(stem, set(forms) | set(groups))
            n = forms[base] if base in forms else rule(base)
            n = n[:1].lower() + n[1:] + ending
        elif stem[:1].islower() and stem.endswith("ai"):  # ḥudaybiyai → hudajbijai
            n = rule(stem[:-1]) + "i"
        elif re.match(r"^[Aa]l-", stem) and stem[3:4].isupper() and stem[3:] in forms:  # names only
            n = "al-" + re.sub(r"^al-", "", forms[stem[3:]])
        else:
            n = rule(stem)
        new = attach(n, suf, stem)
        start = sentence_start(text, m.start())
        if new.startswith("al-") and (start or text[m.start() - 1:m.start()] == "*"):
            new = "A" + new[1:]
        elif start and new[:1].islower():
            new = new[:1].upper() + new[1:]
        elif not start and tok[:1].isupper() and new[:1].isupper() and n[:1].islower():
            pass  # a lowercase term (négus, ima) stays lowercase mid-sentence
        if new == tok:
            continue
        # the article in front: a ↔ az
        am = re.search(r"(?:(?<=[\s(„*])|^)([Aa]z?) (\*?)$", text[max(0, m.start() - 8):m.start()])
        if am and am.start() == 0 and m.start() > 8:
            am = None  # the window cut a word: not an article
        if am:
            want = "az" if new.lstrip("'")[:1].lower() in "aáeéiíoóöőuúüű" else "a"
            if am.group(1).lower() != want:
                art = want if am.group(1)[0] == "a" else want.capitalize()
                a0 = m.start() - len(am.group(0))
                edits.append((a0, a0 + len(am.group(1)), art))
                log["article a/az"][f"{am.group(1)} {tok} → {art} {new}"] += 1
        edits.append((m.start(), m.end(), new))
        key = "suffix re-fitted" if suf and not new.endswith(suf) else "plain"
        log[key][f"{tok} → {new}"] += 1
    for a, b, new in sorted(edits, reverse=True):
        text = text[:a] + new + text[b:]
    text = re.sub("\x00(.)\x00", lambda m: held[ord(m.group(1)) - 0xE000], text)

    # 5) glosses that now repeat the word: „Ábrahámot (Ábrahámot)”, „ája (vers)”
    def collapse(m):
        log["gloss merged"][m.group(0)] += 1
        return m.group(1)
    text = re.sub(r"(?<![\w'])((?:[\w'-]+ )?[\w'-]+) [(\[]\*?\1\*?[)\]]", collapse, text)
    text = re.sub(r"(?<![\w'])([Áá]j[áa]\w*) \(vers\w*\)", collapse, text)

    # 6) glossary re-sorted (Hungarian alphabet)
    text = sort_glossary(text, log)

    # 7) leftovers: any transliteration letter still in the text
    for m in re.finditer(r"[\w'-]*[āīūĀĪŪḥḤṭṬṣṢḍḌẓẒ][\w'-]*", text):
        log["LEFTOVER"][m.group()] += 1

    with REPORT.open("w", encoding="utf-8") as f:
        for sec in sorted(log, key=lambda s: (s not in ("UNPARSED (left as is)", "LEFTOVER"), s)):
            f.write(f"\n=== {sec} ({sum(log[sec].values())} occurrences, {len(log[sec])} distinct)\n")
            for k, n in sorted(log[sec].items(), key=lambda kv: (-kv[1], kv[0])):
                f.write(f"{n:4}  {k}\n")
    print(f"report → {REPORT.name}: " + ", ".join(f"{s} {sum(c.values())}" for s, c in sorted(log.items())))
    if write:
        HUN.write_text(text, encoding="utf-8")
        print("HUN file written")


HU_ORDER = ["a", "b", "c", "cs", "d", "dz", "dzs", "e", "f", "g", "gy", "h", "i", "j", "k", "l", "ly", "m", "n", "ny",
            "o", "ö", "p", "q", "r", "s", "sz", "t", "ty", "u", "ü", "v", "w", "x", "y", "z", "zs"]
FOLD = str.maketrans("áéíóőúű", "aeioöuü")


def hu_key(word):
    w = word.lower().lstrip("'").translate(FOLD)
    key, i = [], 0
    while i < len(w):
        for L in (3, 2, 1):
            if w[i:i + L] in HU_ORDER:
                key.append(HU_ORDER.index(w[i:i + L]))
                i += L
                break
        else:
            i += 1
    return key, word.lower()


def sort_glossary(text, log):
    g0 = text.index("# Szójegyzék")
    head, body = text[:g0], text[g0:]
    lines = body.split("\n")
    title, entries, tail = lines[0], [], []
    for line in lines[1:]:
        if line.startswith("*"):
            entries.append(line)
        elif line.strip() and not entries:
            raise SystemExit(f"unexpected glossary line: {line[:60]}")
        elif line.strip():
            tail.append(line)
    assert not tail, tail[:3]
    before = [e.split("*")[1] for e in entries]
    entries.sort(key=lambda e: hu_key(e.split("*")[1]))
    log["glossary order"]["; ".join(e.split("*")[1] for e in entries)] += 1
    assert sorted(before) == sorted(e.split("*")[1] for e in entries)
    return head + title + "\n\n" + "\n\n".join(entries) + "\n"


if __name__ == "__main__":
    main("--write" in sys.argv)
