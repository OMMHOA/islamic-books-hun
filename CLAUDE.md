# islamic-books-hun

Goal: translate Islamic books to Hungarian, published as Markdown in this repo. Each book has
its own directory; the root holds only `README.md`, `LICENSE` and this file.

Current book: **Fiqh-us-Seerah** by Muhammad al-Ghazali (IIFSO Revised 2nd Edition,
distributed by IIPH, 1420 AH / 1999 CE, English translation, with ḥadīth commentary by Sheikh
Muhammad Naṣiruddīn al-Albānī) — Hungarian title **Fikh al-Szíra**. Everything is in
`fiqh-us-seerah/`; bare file names below are relative to it.

## Status

The Hungarian translation is **complete and verified against the Arabic original**. What's
left is proofreading and style work, listed in **`TODO.md`** — add new open items there.
English-edition errors go in **`ENGLISH-EDITION-ERRATA.md`**. Everything else is in the git
history.

How we got here (details in the commits):
- 2026-07-13 English transcription from the scan by parallel Sonnet subagents (`edf317e`).
- 2026-07-15 Hungarian draft complete; 2026-07-16 fidelity policy (below) and terminology pass.
- 2026-07-17/18 verification against the Arabic: G1 Arabic transcription (`47638d4`), G2
  Qur'ān-reference sweep, G3 chunk-aligned HUN↔AR pass (`e73e417`…`4610a04`), G4 name and
  ḥadīth-grade sweep (`9306cd9`).
- 2026-07-20 → the user's read-through (Mohamed, Medina, no *menny*).
- 2026-09-25 Opus 5.5 full HUN↔AR re-read (`0f65ee4`) and the user's decisions on it
  (`6abd248`); the per-item findings log is `review-wip/opus55-findings.md` in that commit.
- 2026-09-28 Hungarian name forms book-wide (`ad561d3`); the user-reviewed per-name list is
  `review-wip/names.md` in that commit, the old `REVIEW-FLAGS.md` log likewise.
- 2026-09-29 the review's remaining suggestions applied to both files after the user's go-through
  (the decision list and what was dropped are in that commit's message).

## Files

| File | What it is |
|---|---|
| `FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md` | **The Hungarian translation**: front matter → Chapters 1–9 → Utószó → back matter („A könyvben használt jelek”, „A nevek átírásáról”, „Szójegyzék” — 71 entries, Hungarian alphabetical order) |
| `FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md` | English transcription, ~176k words, corrected per the Arabic (see the errata). ch9's footnotes sit at the very end (after the Glossary); HUN puts them after ch9 |
| `FiqhusSeerah-Muhammad-al-Ghazali-AR-full.md` | Arabic transcription, printed pages 2–368, `[صفحة N]` page markers, per-page footnote blockquotes. A locating/reading aid, not gospel — re-check decision-critical readings on the scan. 9 `[غير مقروء]` spots (ch7, pp. 293–304) |
| `FiqhusSeerah-Muhammad-alGhazali.pdf` | English source scan, 512 pages, no text layer. **PDF page = printed page − 2** |
| `فقه السيرة - محمد الغزالي.pdf` | Arabic original scan (Maṭābiʿ al-Shurūq ed.), 368 pages, no text layer. **Printed page = PDF page + 1**; PDF 368 = back cover. Chapter → PDF pages: front 1–13, ch1 14–44, ch2 45–69, ch3 70–107, ch4 108–133, ch5 134–157, ch6 158–245, ch7 246–331, ch8 332–352, ch9 + خاتمة + TOC 353–367 |
| `ENGLISH-EDITION-ERRATA.md` | The English edition's errors verified against the Arabic, by type — all corrected in ENG-full and HUN |
| `TODO.md` | Open work, incl. the unapplied style suggestions of the 2026-09-25 review |
| `build-ebooks.sh` | Builds `FiqhusSeerah-HUN.pdf` + `.epub` from the HUN file (pandoc + typst, fetched into the git-ignored `.build-tools/`); the user reads the book this way |
| `tools/` | `fntool.py check HUN\|ENG N` (footnotes 1..N aligned body↔list) and `shift`; `fnins.py` (insert a footnote with renumbering); `apply.py` (idempotent exact-match edit engine for spec files); `arpage.py N` (Arabic footnotes of a printed page with their anchors) |

Footnote counts (both files, 1:1 body↔list): ch1 21, ch2 27, ch3 35, ch4 25, ch5 23, ch6 100,
ch7 128, ch8 24, ch9 18. Run `tools/fntool.py check` after any footnote edit.

## Fidelity policy (both files)

- **The Arabic original is the sole source of truth** (user decision 2026-07-16). English-
  edition errors (mistranslations, corrupted names, wrong Qur'ān refs, honorifics the Arabic
  doesn't have, dropped text/footnotes) are **corrected in both `-ENG-full.md` and the HUN
  file** once checked against the Arabic scan — the correct text, no translator's note — and
  logged in `ENGLISH-EDITION-ERRATA.md`. Pure English print typos may be fixed silently.
- Where the **Arabic itself** errs (e.g. Sa'd ibn 'Ubādah "chief of the Aws", AR p.292), both
  files stay faithful to the Arabic **with an inline note** — ENG `[… — translator's note]`,
  HUN `[… – a ford.]`.
- **No softening** (user decision 2026-09-25): render the author as bluntly as he wrote —
  generalisations (e.g. about the Jews) and insults included, even where he is wrong.
  Qualifiers the English added ("some of", "among") are removed.

## Conventions (both files)

- Honorifics: (ﷺ) after the Prophet, (ﷻ) after Allah, (رضي الله عنه) only for Companions — never
  for enemies of Islam or pre-Islamic figures such as Zayd ibn 'Amr ibn Nufayl — and
  (عليه السلام) for prophets.
- Headings: `# Chapter N` + `# Title` (two lines), `##` for sections.
- Footnotes: Unicode superscript markers (¹ ² ³…) in the text, texts in a `## Footnotes` block
  at the end of each chapter, numbered per chapter.
- Poetry: each line its own *italic* paragraph. The book's ❑ ornament is dropped.
- ENG keeps the transliteration diacritics (Qur'ān, Ḥadīth, Madīnah…); Qur'ān quotes as a plain
  paragraph in parentheses + `(Qur'ān X: Y)`.

## Hungarian conventions

- Qur'ān quotes: `(… szöveg …) (Korán X: Y)`; en dash in verse ranges (10: 68–70).
- Quotation marks „…”, second level »…«, third level '…'. Dashes: spaced en dash ( – ) as
  gondolatjel, unspaced in ranges; no em dashes.
- **Allah** wherever the Arabic has الله — also from pagans, Jews and Christians (oaths «والله» →
  „Allahra (ﷻ)”); *isten/Isten* only for إله.
- The Prophet is **Mohamed** (Mohamedet, Mohameddel…); everyone else named Muhammad keeps
  *Muhammad* (Muhammad al-Ghazáli, Muhammad Násziruddín al-Albáni, ḥadīth narrators), as does
  the shahāda (*Muhammadan raszúlu-llah*). **Mekka**, **Medina** (leave the word *mekkora*
  alone).
- Render the author's word even when the Hungarian has a Christian ring: صلب → **keresztre feszít**
  (user decision 2026-09-28; crucifixion predates Jesus). This is not the *menny* case below, where
  the Arabic has neutral words (السماء, الجنة) that *menny* doesn't render.
- Afterlife: never *menny/mennyország*. السماء → **ég / égi / egek**; الجنة → **Paradicsom**;
  الآخرة → **túlvilág**; **Pokol** capitalised like Paradicsom (derived adjectives lowercase).
  (The unrelated *mennyi, mennyire, mennydörgés, mennykő, mennyezet* are fine.)
- Ḥadīth grades: ṣaḥīḥ/"sound"/"authentic" → **hiteles** (al-Albānī's labels: `Hiteles
  (szahíh):`); ḥasan → **jó**; ḍaʿīf → **gyenge**. *ép* is NOT a grade (it means "intact").
- Terms: Korán, hadísz, umma, tauhid, **dzsáhilijja** (not italic; "dzsáhilijja kori"), **ája /
  áják** (singular after quantifiers: „néhány ája”), **dáwa**, **szahába** (pl. szahábák),
  **azán**, **ima** (ṣalāh), **zakát**, **rakát**, **haddzs**, **umra**, **müezzin**, **könyök**
  (dhirāʿ), **anszár(ok)**, **muhádzsir(ok)**; ḥadīth-science terms by the name rule (szahíh,
  haszan, gharíb, murszal, mudal, isznád, tadlísz…).
- **Names** (user decisions 2026-09-25/28) — Hungarian transcription, no diacritics:
  - ā ī ū → á í ú, but a **word-final long vowel is short** (al-Bukhári, Músza, Iszra; the
    particle Banú excepted); ḥ ṭ ḍ ẓ ṣ → h t d z sz; sh→s, s→sz, th→sz, dh→z, j→dzs, y→j, w→v,
    q→k, aw→au, ay→aj; **kh and gh stay** (Khálid, Ghatafán); ʿayn/hamza dropped (Szad, Kab);
    final -ah → -a (Hamza); **al-** never assimilated (al-Zubajr); Abū → Abu, Banū → Banú.
    Allah compounds keep *-llah* (Abdullah).
  - Prophets get their **biblical names** (Ábrahám, Mózes, Izsák, József, Gábriel, Noé…; but
    **Iszmaíl**); other people with the same name follow the rule (**Ibn Iszhák**, Abu Músza,
    Abu Dávúd, Ibrahim).
  - Known forms: Omár, Oszmán, Ali, Áisa, Khadídzsa, Fátima, Kába, Ibn Kathir, al-Tirmidhi,
    Jathrib, Muád, Szulejmán, Huszrau; *a négus* (lowercase).
  - Surahs „a Tauba szúra”; month names lowercase (ramadán, savvál, zul-kada); **a Banú
    Iszráíl** for بنو إسرائيل (collective, singular verb — like „a Banú Kurajza”); book titles by
    the rule (Szahíh al-Bukhári, Fath al-Bári).
  - Endings follow the Hungarian form and its vowel harmony (Áisától, Kurajssal, Mózesnek).
  - Glossary headwords use the same forms; where the text uses a Hungarian word (ima,
    Paradicsom), the headword is the Arabic term (*Szaláh*, *Dzsanna*).
