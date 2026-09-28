#!/usr/bin/env python3
"""Build review-wip/names.md — the short review list of Hungarian name forms.

    python3 names_build.py

The rule (user decisions 2026-09-25 / 2026-09-28) is translit() below and RULE_DOC in the output.
The list shows only what is worth a look: open questions, traditional forms, prophets, names
occurring 10+ times, frequent terms, and merged spelling variants. Every other name simply gets
translit() when the list is applied to the book.
"""
import collections
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
H = (ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md").read_text(encoding="utf-8")
E = (ROOT / "FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md").read_text(encoding="utf-8")
OUT = pathlib.Path(__file__).resolve().parent / "names.md"
FREQ = 10  # names at least this frequent are listed individually

W = re.compile(r"[A-Za-zÀ-ÖØ-öø-ɏḀ-ỿʿʾ']+(?:-[A-Za-zÀ-ÖØ-öø-ɏḀ-ỿʿʾ']+)*")
TR = set("āīūĀĪŪḥḤṭṬṣṢḍḌẓẒʿʾ")
SUFFIX = re.compile(r"^-?[a-záéíóöőúüű]{1,7}$")

# words that look foreign to the detector but are Hungarian/English/decided — not in the list
STOP = {"Most", "Amit", "Mind", "International", "Islamic", "Allah", "Allahu", "Akbar", "Arab", "Mohamed",
        "Mekka", "Medina", "Korán", "Jézus", "Mária", "Paradicsom", "Pokol", "Muszlim",
        "Publishing", "House", "Student", "Federation", "Organizations", "IIFSO", "Hollywood", "Marx", "Karl",
        "Kenya", "India"}
PARTICLES = {"Abil", "Ibn", "ibn", "bint", "Bint", "Umm", "Abū", "Abu", "Abī", "Abi", "Banū", "Banu", "Abul",
             "Dhū", "Dhul", "Al", "al"}
# single letters and symbols of the back-matter transliteration table — never converted
TABLE_LETTERS = {"ā", "ī", "ū", "ḍ", "ḥ", "ṣ", "ṭ", "ẓ", "a", "'a"}

# English-edition spellings that lost a long vowel (or split a letter) the Arabic has — fixed before the rule
FIX_SPELLING = {"Ḥirah": "Ḥīrah", "Bari": "Bārī", "Bāri": "Bārī", "Naṣiruddīn": "Nāṣiruddīn",
                "Nāṣiruddin": "Nāṣiruddīn", "Al-Ḥakim": "Al-Ḥākim", "Ḥakim": "Ḥākim", "Is-ḥāq": "Isḥāq",
                "Ibrahīm": "Ibrāhīm", "Ibrahim": "Ibrāhīm", "Ya'qub": "Ya'qūb", "Mūsa": "Mūsā", "Dawūd": "Dāwūd",
                "Rabi'ah": "Rabī'ah", "ḥadždzs": "ḥajj", "Muṭṭālib": "Muṭṭalib", "shādh": "shādhdh",
                "Mistah": "Misṭaḥ", "Fath": "Fatḥ",
                "Shādh": "Shādhdh", "Kulthum": "Kulthūm", "Buwat": "Buwāṭ", "Taqrib": "Taqrīb",
                "Mawahib": "Mawāhib", "'Awwam": "'Awwām"}
# same letters without accents, but different names — never merged as spelling variants
NOMERGE = {"Ḥaram", "Ḥarām", "Ḥirā'", "Ḥirā", "Sālim", "Salīm", "Qa'dah", "Q'ada", "Kadā'", "Qaḍā'", "Ḥakīm",
           "Ṭaba", "Ṭabah", "Ṭābah", "Sawah", "Sāwā", "'Aṣr", "'aṣr", "Salām", "Salam", "Al-Ḥaṭīm", "Ḥaṭīm"}
# extra remarks on a line of section 4, keyed by its Hungarian form
NOTES = {"Hákim": "the ḥadīth scholar al-Ḥākim; the one „Ḥakim ibn Ḥizām” is a different name → Hakím"}


def translit(w):
    """The rule: one transliterated word → Hungarian form (keeps the case of the first letter)."""
    s = FIX_SPELLING.get(w, w).replace("ʿ", "'").replace("ʾ", "'")
    art = ""
    m = re.match(r"^([Aa]l)[- ](.+)$", s)
    if m:
        art, s = "al-", FIX_SPELLING.get(m.group(2), m.group(2))
    cap = s.lstrip("'")[:1].isupper()
    t = s.lower()
    t = re.sub(r"ah$", "a", t)
    # 1) dotted/long letters → placeholders (so sḥ, dḥ… are not read as digraphs)
    for a, b in (("ā", "\x10"), ("ī", "\x11"), ("ū", "\x12"), ("ḥ", "\x13"), ("ṭ", "\x14"), ("ḍ", "\x15"),
                 ("ẓ", "\x16"), ("ṣ", "\x17")):
        t = t.replace(a, b)
    t = t.replace("s-\x13", "s\x13")  # Is-ḥāq → Isḥāq
    # 2) Hungarian digraphs already present (muhādzsir, szalām) are kept as they are
    t = t.replace("dzs", "\x06").replace("sz", "\x07")
    # 3) Arabic digraphs
    for a, b in (("sh", "\x01"), ("kh", "\x02"), ("gh", "\x03"), ("th", "\x04"), ("dh", "\x05")):
        t = t.replace(a, b)
    # 4) j and s before y→j creates new j's
    t = t.replace("j", "\x06").replace("s", "\x07")
    # 5) diphthongs, then y/w/q; aw → au only before a consonant other than w (Shawwāl → Savvál)
    t = re.sub("aw(?![aeiouáéíóúw\x10\x11\x12])", "au", t)
    for a, b in (("ay", "aj"), ("ai", "aj"), ("y", "j"), ("w", "v"), ("q", "k"), ("'", ""), ("ou", "u")):
        t = t.replace(a, b)
    for a, b in (("\x10", "á"), ("\x11", "í"), ("\x12", "ú"), ("\x13", "h"), ("\x14", "t"), ("\x15", "d"),
                 ("\x16", "z"), ("\x17", "sz"), ("\x01", "s"), ("\x02", "kh"), ("\x03", "gh"), ("\x04", "sz"),
                 ("\x05", "z"), ("\x06", "dzs"), ("\x07", "sz")):
        t = t.replace(a, b)
    t = t.replace("szsz", "ssz").replace("dzsdzs", "ddzs")
    if cap:
        t = t[:1].upper() + t[1:]
    return art + t


def bare(s):
    """Merge key: no article, no accents, no apostrophes, lowercase."""
    s = re.sub(r"^al-", "", s.lower())
    s = "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))
    return s.replace("'", "")


def accents(s):
    return sum(1 for c in s if ord(c) > 127)


def count(pattern):
    return len(re.findall(pattern, H))


# ---------- detection: every transliterated word in HUN, reduced to its stem ----------

# English-style transliteration without diacritics: w, q, or a y outside the Hungarian gy/ly/ny/ty
MARKERS = re.compile(r"w|q|(?<![glnt])y", re.I)
NOT_NAMES = {"Hollywood", "Publishing", "Pickthall", "IIFSO", "www", "Buddha", "Buddhát", "buddhizmus",
             "qadianizmus"}
# in broad mode a split must leave a real Hungarian ending (not „Al-Hari” + „th”, „al-Mughīra” + „h”)
SUF_START = re.compile(r"^-?(t|at|ot|et|öt|n|on|en|ön|nak|nek|hoz|hez|höz|tól|től|ból|ből|ba|be|ban|ben|ra|re|"
                       r"ról|ről|nál|nél|[b-df-hj-np-tv-z](al|el)|vá|vé|ig|ért|ként|kor|ul|ül|é|ék|i|ok|ek|ak|k|"
                       r"j?[aáeé]|s|os|es)")


def collect(H=H, broad=False):
    """→ (stem → occurrences, token → stem) for every transliterated word in H.

    broad=True (used when applying the list) also catches names the English edition spells differently:
    al-X glued to its article, lengthened forms (Quraydhához), and diacritic-less spellings (qibla, Khuwaylid)."""
    htok = collections.Counter(W.findall(H))
    etok = collections.Counter(W.findall(E))
    foreign = {t for t in htok if any(c in TR for c in t) or re.match(r"^'[A-Za-z]", t)
               or re.search(r"[a-z]'[a-z]", t, re.I)}
    engcaps = {t for t in etok if t[:1].isupper() and len(t) > 2}
    plain = {t for t in htok if t in engcaps and t not in foreign and t not in STOP}
    cand = (foreign | plain) - STOP
    # drop Hungarian words that only look foreign because of '…' (third-level quotes)
    hun_plain = {t.lower() for t in htok if t not in foreign}
    cand = {t for t in cand if not ("'" in (t[:1] + t[-1:]) and not any(c in TR for c in t)
                                    and t.strip("'").lower() in hun_plain)}
    cand -= {"'jós'", "'költő'", "'varázsló'", "'egy", "'Nem"}
    names = plain
    if broad:
        bare = lambda t: re.sub(r"^[Aa]l-", "", t)
        names = plain | {e for e in engcaps if e not in STOP and e not in NOT_NAMES
                         and (MARKERS.search(e) or re.search("sh|th|dh|'", e))}
        cand |= {t for t in htok if MARKERS.search(bare(t)) and t not in NOT_NAMES and t not in STOP}
        cand |= {t for t in htok if bare(t) != t and (bare(t) in names or bare(t) in cand)}
    for t in htok:  # suffixed forms of plain names (Quraisht, Quraishhoz, Zayddal…)
        if t in cand or not t[:1].isupper():
            continue
        for k in range(len(t) - 1, 2, -1):
            p = re.sub(r"^[Aa]l-", "", t[:k]) if broad else t[:k]
            lengthened = broad and p.endswith("á") and (p[:-1] + "ah" in names or p[:-1] + "a" in names)
            if (p in names or lengthened) and SUFFIX.match(t[k:]):
                cand.add(t)
                break
    known = set(etok) | set(cand)
    if broad:
        known |= {a + e for e in etok if e[:1].isupper() for a in ("Al-", "al-")}
        known = {k for k in known if len(k.strip("'")) > 2}  # no „kh” stems from the transliteration table
    known -= TABLE_LETTERS

    def ok_suffix(r):
        return SUFFIX.match(r) and (not broad or SUF_START.match(r))

    def stem_of(t):
        m = re.match(r"^(.+?)-([a-záéíóöőúüű]+)$", t)
        if m and not any(c in TR for c in m.group(2)) and not t.lower().startswith("al-"):
            t = m.group(1)  # Ḥudaybiyah-történet → Ḥudaybiyah
        if t in etok:
            return t
        for k in range(len(t) - 1, 1, -1):
            p, r = t[:k], t[k:]
            if p in known and ok_suffix(r):
                return stem_of(p) if p != t else p
            if p.endswith(("á", "é")) and SUFFIX.match(r):  # Ḥamzát ← Ḥamzah/Ḥamza
                base = p[:-1] + ("a" if p.endswith("á") else "e")
                for b in (base + "h", base):
                    if b in known:
                        return b
        return t

    groups, tok2stem = collections.Counter(), {}
    for t in cand:
        tok2stem[t] = stem_of(t)
        groups[tok2stem[t]] += htok[t]
    for s in list(groups):
        if s in PARTICLES or s in TABLE_LETTERS:
            del groups[s]
    return groups, {t: s for t, s in tok2stem.items() if s in groups}


# ---------- curated sections ----------

TRADITIONAL = [  # (spellings in the text, Hungarian form)
    (["'Umar", "Umar"], "Omár"), (["'Uthmān", "Uthmān"], "Oszmán"), (["'Alī", "Alī"], "Ali"),
    (["'Ā'ishah", "'Ā'isha"], "Áisa"), (["Khadījah", "Khadīja"], "Khadídzsa"), (["Fāṭimah", "Fāṭima"], "Fátima"),
    (["Ka'bah", "Ka'ba"], "Kába"),
]

PROPHETS = [  # (label, spellings, biblical form or None)
    ("Isḥāq", ["Isḥāq", "Is-ḥāq"], "Izsák"), ("Ibrāhīm", ["Ibrāhīm", "Ibrahīm", "Ibrahim"], "Ábrahám"),
    ("Dāwūd", ["Dāwūd", "Dawūd"], "Dávid"), ("Mūsā", ["Mūsā", "Mūsa"], "Mózes"), ("Jibrīl", ["Jibrīl"], "Gábriel"),
    ("Yūsuf", ["Yūsuf"], "József"), ("Ismā'īl", ["Ismā'īl"], "Izmael"), ("Nūḥ", ["Nūḥ"], "Noé"),
    ("Ya'qūb", ["Ya'qūb", "Ya'qub"], "Jákob"), ("Hārūn", ["Hārūn"], "Áron"), ("Yūnus", ["Yūnus"], "Jónás"),
    ("'Īsā", ["'Īsā", "Īsā"], "Jézus"), ("Maryam", ["Maryam"], "Mária"), ("Sulaymān", ["Sulaymān"], "Salamon"),
    ("Yaḥyā", ["Yaḥyā"], "János"), ("Ādām", ["Ādām", "Ādam"], "Ádám"), ("Ṣāliḥ", ["Ṣāliḥ"], None),
]
# occurrences the particle test can't classify, checked by hand (2026-09-28): other people, not the prophet
PERSON_CTX = ["Mubārak beszélte el nekünk Isḥāq", "Isḥāq elhagyott", "kivéve Ibrāhīm", "közölte Ibrāhīm útján",
              "szakadás van Ibrāhīm", "A fiút Ibrāhīm", "érted, Ibrāhīm", "ezt a Mūsāt", "Yūnus közölte", "De Yūnus",
              "ezt, Ya'qub", "Ó, Ya'qub"]  # the last two: Abū Yūsuf (Ya'qūb) addressed by name
SURA_CTX = ["Sūrah Maryam"]


def classify(spellings):
    c = collections.Counter()
    for sp in spellings:
        for m in re.finditer(r"(?<![\w'])" + re.escape(sp) + r"(?![\wāīū'])|(?<![\w'])" + re.escape(sp)
                             + r"(?=[a-záéíóöőúüű-])", H):
            pre, post = H[max(0, m.start() - 12):m.start()], H[m.end():m.end() + 25]
            around = H[max(0, m.start() - 40):m.end() + 30]
            if any(x in around for x in SURA_CTX):
                c["sura"] += 1
            elif (re.search(r"(Abū|Abu|Abī|Abi|Ibn|ibn|bint|Umm|Banū|Banu) $", pre)
                  or re.match(r"[a-záéíóöőúüű-]*\s*(ibn|bin|bint)\b", post) or any(x in around for x in PERSON_CTX)):
                c["person"] += 1
            else:
                c["prophet"] += 1
    return c


TERMS = [  # (spellings, proposal, note) — lowercase words; only frequent ones are listed
    (["ṣaḥīḥ"], "szahíh", "the grading word next to *hiteles*: „hiteles (szahíh)”"),
    (["ḥasan"], "haszan", "„jó (haszan)”"),
    (["gharīb"], "gharíb", "„ritka (gharíb)”"),
    (["mu'ḍal", "mursal", "marfū'", "mauqūf", "mawqūf", "matrūk", "mu'allaq", "mu'allal", "munqaṭi'", "mudallis",
      "tadlīs", "isnād", "mutawātir", "mawṣūl", "munkar", "shādh"], None, "ḥadīth-science terms, by the rule"),
    (["anṣār"], "anszárok", ""),
    (["anṣārī"], "anszárí", "one of the anṣār"),
    (["muhājir", "muhādzsir", "muhājirūn"], "muhádzsir(ok)", ""),
    (["āyah", "āyāh"], "vers", "where the text already says „āyah (vers)”, just „vers”"),
    (["āyāt", "āyāk", "Āyāt"], "versek", "likewise „āyāt (versek)” → „versek”"),
    (["da'wah", "da'wa", "da'wája"], "hívás", "the call to Islam; no settled Hungarian word — the rule gives *dava*"),
    (["ṣaḥābī", "ṣaḥāba", "ṣaḥābah"], "társ / társak", "as everywhere else in the book"),
    (["adhān"], "ezán", "the Hungarian dictionary word, like *müezzin*; the rule gives *azán*"),
    (["ṣalāh", "Ṣalāh", "Ṣalāt", "salāh"], "ima", ""),
    (["zakāh", "zakāt"], "zakát", ""),
    (["rak'a", "rak'ah", "rak'át"], "rakát", "the rule gives *raka*"),
    (["ḥajj", "Ḥajj", "ḥadždzs"], "haddzs", "or just *zarándoklat*"),
    (["'umrah", "'umra", "Umrah"], "umra", ""),
    (["tafsīr"], "tafszír", "Qur'ān commentary"),
    (["ḥanīf"], "haníf", ""),
    (["dhirā'"], "könyök", "the length unit (cubit)"),
    (["salām", "szalām"], "szalám", ""),
    (["sīrah", "sīra", "szīrah"], "szíra", ""),
    (["mu'adhdhin"], "müezzin", "the Hungarian word; the rule gives *muazzin*"),
    (["aḥābīsh"], "ahábís", "the text explains it"),
    (["riḍwān"], "ridván", "„ridván-fogadalom”"),
    (["sawīq"], "szavík", "the text explains it"),
]

# stems covered by the questions in section 1 — kept out of the automatic lists
QUESTION_STEMS = {"Khosrau", "Negus", "Sūrat", "Sūrah", "sūrah", "Ramaḍān", "Shawwāl", "Isrā'īl", "Ghazālī",
                  "Ṣaḥīḥ", "Sunan", "Ashhadu", "Hayya", "Assalatu", "Muhammadan", "Lā", "Allāhumma"}


def questions():
    months = ["Muḥarram", "Ṣafar", "Rabī'", "Jumādā", "Jumāda", "Rajab", "Sha'bān", "Ramaḍān", "Shawwāl",
              "Dhul-Qa'dah", "Dhul-Ḥijjah", "Dhū al-Ḥijjah"]
    n_months = sum(count(r"(?<![\w'])" + re.escape(m)) for m in months)
    return [
        ("Khosrau", f"{count('Khosrau')}×, the Persian king",
         "the rule gives *Khoszrau*; Hungarian history books write *Huszrau* (II. Huszrau). "
         "One place has the Arabic title instead: „Kisra városát”.", "Huszrau"),
        ("Negus", f"{count('Negus')}× capitalised, {count('négus')}× already *négus*",
         "Hungarian spells the Abyssinian king's title lowercase: *a négus*.", "négus"),
        ("Surah names", "Sūrat al-Tawbah, Sūrat ul-Lahab, Sūrah Maryam, Sūrah Hūd, Sūrah Fuṣṣilat, Sūrah Barā'ah…",
         "the rule alone would give *Szúrat al-Tauba*. Hungarian word order, without the Arabic article, "
         "reads better.", "a Tauba szúra, a Lahab szúra, a Marjam szúra, a Húd szúra"),
        ("Month names", f"{n_months}×: Ramaḍān, Shawwāl, Dhul-Ḥijjah…",
         "Hungarian writes month names lowercase (like *január*): *ramadán*, *savvál*, *zul-hiddzsa*.",
         "lowercase"),
        ("Banū Isrā'īl", f"{count('Banū Isrā')}×; the book already says *Izrael fiai* {count('Izrael [Ff]iai')}×",
         "the rule gives *Banú Iszráíl*.", "Izrael fiai"),
        ("Book titles", "Ṣaḥīḥ al-Bukhārī, Fatḥ al-Bārī, Al-Bidāyah, Sunan, Taqrīb…",
         "follow the rule too (*Szahíh al-Bukhárí*, *Fath al-Bárí*, *al-Bidája*), or keep the "
         "transliteration as a bibliographic reference?", "the rule"),
        ("The author's name", "title page and signature: *Muhammad Al-Ghazali*",
         "the rule gives *Muhammad al-Ghazálí*; the English edition's cover has *al-Ghazali*.",
         "Muhammad al-Ghazálí"),
        ("Arabic sentences", "adhān and shahāda, e.g. *Ashhadu an lā ilāha illa-llāh*",
         "follow the rule too (*Ashadu an lá iláha illa-lláh*), so a Hungarian reader pronounces them right?",
         "yes, the rule"),
        ("Transliteration table", "back matter, „# Átírási táblázat”",
         "explains the ā/ḥ/ṣ letters, which the Hungarian text no longer uses. Replace it with a short note "
         "on how names are written (the rule above)?", "replace with a note"),
    ]


RULE_DOC = """\
- long vowels ā ī ū → á í ú · dotted letters lose the dot: ḥ→h, ṭ→t, ḍ→d, ẓ→z, ṣ→sz
- sh→s, s→sz, th→sz, dh→z, j→dzs, y→j, w→v, q→k, aw→au, ay→aj
- **kh and gh stay** everywhere (Khálid, Ghatafán)
- the ʿayn/hamza apostrophe is dropped (Sa'd → Szad); final -ah → -a (Ḥamzah → Hamza)
- the article stays **al-**, not assimilated (al-Zubajr, al-Tirmizí); lowercase except at a sentence start
- Abū → Abu, Banū → Banú; ibn, bint, Umm unchanged
- prophets get their **Hungarian biblical names** (Ábrahám, Mózes); other people with the same name follow
  the rule (Ibn Iszhák, Abu Múszá, Abu Dávúd)
- already done: Mohamed (the Prophet), Muhammad (everyone else), Mekka, Medina, Jézus
- glossary headwords follow the same forms, and the glossary is re-sorted afterwards"""


def main():
    groups, _ = collect()
    lines = []
    out = lines.append

    out("# Names — Hungarian forms\n")
    out("**How to use this file:** each line reads `current spelling → Hungarian form (how many times)`.")
    out("Where you disagree, overwrite the **bold** form, or just tell me in chat. Whatever you leave")
    out("alone counts as accepted. Then I apply it to the whole book (with the Hungarian suffixes, e.g.")
    out("Quraisht → Kurajsot) and re-sort the glossary.\n")
    out(f"Generated by `review-wip/names_build.py`. {len(groups)} different names/terms occur in the")
    out(f"book; only the ones worth a look are listed. **The rest (mostly names that occur once or twice)")
    out("simply get the rule**, and you will see them in the ebook.\n")
    out("## The rule (decided 2026-09-28)\n")
    out(RULE_DOC + "\n")

    qs = questions()
    out(f"## 1. Questions for you ({len(qs)})\n")
    out("The rule can't settle these. My pick is after the arrow; change it if you disagree.\n")
    for i, (title, what, why, pick) in enumerate(qs, 1):
        out(f"**{i}. {title}** ({what}): {why}  ")
        out(f"→ **{pick}**\n")

    used = set(QUESTION_STEMS)
    out("## 2. Traditional Hungarian forms (deliberate exceptions to the rule)\n")
    for spellings, hu in TRADITIONAL:
        n = sum(groups.get(s, 0) for s in spellings)
        used.update(spellings)
        out(f"- {spellings[0]} → **{hu}** ({n})")
    out("")

    out("## 3. Prophets and angels\n")
    out("The biblical name is used only where the text means the prophet himself; other people with the")
    out("same name follow the rule. Glosses like „Nūḥ (Noé)” become just „Noé”.\n")
    for label, spellings, bib in PROPHETS:
        used.update(spellings)
        c = classify(spellings)
        rule = translit(spellings[0])
        if bib is None:
            out(f"- {label} → **{rule}** ({c['prophet'] + c['person']}; no biblical form — the rule, for the prophet"
                " and others alike)")
        elif c["prophet"] == 0:
            out(f"- {label} → only other people here → **{rule}** ({c['person']})")
        elif c["person"] == 0:
            out(f"- {label} → **{bib}** ({c['prophet']})" + (" · „Sūrah Maryam” → see question 3" if c["sura"] else ""))
        else:
            out(f"- {label} → **{bib}** (the prophet, {c['prophet']}) · other people → **{rule}** ({c['person']})")
    out("")

    # merge spelling variants: same letters once accents/article/apostrophes are ignored
    terms_all = {s for spellings, _, _ in TERMS for s in spellings}
    used |= terms_all
    merged = collections.defaultdict(list)
    for s, n in groups.items():
        if s in used or not s.lstrip("'")[:1].isupper():
            continue
        merged[s if s in NOMERGE else bare(translit(s))].append((n, s))

    def target(members):
        best = max(members, key=lambda m: (accents(translit(m[1])), m[0]))
        return re.sub(r"^al-", "", translit(best[1]))

    freq, variants = [], []
    for members in merged.values():
        total = sum(n for n, _ in members)
        members.sort(reverse=True)
        tgt = target(members)
        names = ", ".join(s for _, s in members)
        differ = len({re.sub(r"^al-", "", translit(s)) for _, s in members}) > 1
        if total >= FREQ and not (len(members) == 1 and translit(members[0][1]) == members[0][1]):
            freq.append((total, names, tgt))
        elif differ and total >= 3:
            variants.append((total, names, tgt))

    out(f"## 4. Frequent names ({FREQ}+ times), by the rule\n")
    out("Several spellings on one line are variants of the same name in the English edition; they all get the")
    out("one form. An article in the text stays: Al-Ḥākim → al-Hákim.\n")
    for total, names, tgt in sorted(freq, key=lambda r: (-r[0], r[1])):
        out(f"- {names} → **{tgt}** ({total})" + (f" — {NOTES[tgt]}" if tgt in NOTES else ""))
    out("")

    out("## 5. Terms (lowercase words)\n")
    out("My picks: a Hungarian word where there is a natural one (ima, vers, társ), a Hungarian spelling for")
    out("technical terms (szahíh, isznád). Terms not listed (rare ones) follow the rule.\n")
    for spellings, prop, note in TERMS:
        # stem counts include suffixed forms ('umrát); words the detector misses (mursal) are counted directly
        freq_of = {s: groups.get(s) or count(r"(?<![\w'])" + re.escape(s)) for s in spellings}
        present = [s for s in spellings if freq_of[s]]
        n = sum(freq_of[s] for s in present)
        if n < 3:
            continue
        shown = ", ".join(present)
        if prop is None:  # a group of terms that simply follow the rule
            prop = ", ".join(dict.fromkeys(translit(s) for s in present))
        out(f"- {shown} → **{prop}** ({n})" + (f" — {note}" if note else ""))
    out("")

    out("## 6. Other spelling variants merged (no action needed)\n")
    out("Less frequent names the English edition spells more than one way; the fullest spelling (closest to")
    out("the Arabic) wins.\n")
    for total, names, tgt in sorted(variants, key=lambda r: (-r[0], r[1])):
        out(f"- {names} → **{tgt}** ({total})")
    out("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(groups)} stems; questions {len(qs)}, frequent {len(freq)}, variants {len(variants)} → {OUT.name}"
          f" ({len(lines)} lines)")


if __name__ == "__main__":
    main()
