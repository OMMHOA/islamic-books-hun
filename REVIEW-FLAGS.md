# Review flags

Items to resolve during the two review passes:
(A) verifying `FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md` against the PDF, and
(B) proofreading the Hungarian in `FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md`.

Line numbers refer to the files as of 2026-07-14 (after Chapter 6 landed) and will
drift as the files grow — search for the quoted text if they no longer match.

## Chapter 6 (translated 2026-07-14)

### 1. Honorific (رضي الله عنه) after enemies of Islam — pass A (check PDF), then pass B

The ENG transcription places (رضي الله عنه) after men who died as enemies of Islam.
Almost certainly artifacts of the book (or OCR pass), since the same honorific is used
correctly elsewhere in the same passages. **The HUN translation deliberately omits them.**
Confirm against the PDF whether the printed book really has them; if yes, they stay in
ENG-full (faithful transcription) and stay out of HUN.

| Person | ENG-full lines | HUN handling |
|---|---|---|
| Ka'b ibn al-Ashraf (Jewish chief, assassinated) | ~3263–3297 (multiple) | omitted (HUN ~3215 ff.) |
| 'Amr ibn 'Abdul Wudd (killed by 'Alī at the Ditch) | ~3871–3875 | omitted (HUN ~3829 ff.) |
| Ka'b ibn Asad (Banū Quraydhah chief) | ~3887–3899, 4056, 4092 | omitted (HUN ~3847 ff.) |

Note: 'Amr ibn al Jamūh (ENG ~3489) is a Ṣaḥābī — his (رضي الله عنه) is correct and kept.

### 2. Qur'ān reference misprint — pass A

ENG-full line 3339: "(To Allāh belong the East and the West…) **(Qur'ān 7: 115)**" —
this verse is 2:115. Kept as printed in both ENG (line 3339) and HUN (line ~3299).
Decide in review whether the HUN edition should silently correct it or keep it with a
translator's note.

### 3. Terminology consistency — pass B ✅ DONE (2026-07-15 / -16)

- **Mekka → Makka** — done (17 occurrences, all in the reused ch1 material; the Hungarian
  word *Mekkora* "how big" was correctly left alone).
- **Ḥadīth grading map — FINAL decision (2026-07-16): ṣaḥīḥ → `hiteles` everywhere.**
  Both ENG "sound" and ENG "authentic" render the single grade ṣaḥīḥ, so they map to the
  **same** Hungarian word, **`hiteles`** — the standard term and the one the book's own
  glossary uses (`*Ṣaḥīḥ*: hiteles hadísz`, front matter). `ép` is **not** a ḥadīth grade
  and no longer used as one. Map: ṣaḥīḥ/sound/authentic → **hiteles**, ḥasan/good → **jó**,
  ḍaʿīf/weak → **gyenge**.
  - **History:** the earlier drafts split "sound" → *ép* vs "authentic" → *hiteles*, an
    invented two-tier distinction (ṣaḥīḥ is one grade). On 2026-07-15 ch2–3 were first
    unified *to* that ép-convention; on 2026-07-16, per user decision, the whole book was
    converted the other way — **all grade-sense `ép` → `hiteles`** (209 replacements incl.
    the `Ép (ṣaḥīḥ):` / `Ép:` footnote labels in ch7–9, `ép hadísz`, `ép lánc*`, and
    predicate/comparative forms `lánca ép`, `… szerint ép`, `épnek nyilvánítja`, `épebb`).
  - **`ép` deliberately kept (ordinary Hungarian word, not a grade):** `ép ítélőképesség`,
    `ép gondolkodó`, `ép elmével`, `ép, erős ifjút`, `ép testű`, and L≈2715
    "a hadísz értelme … ép" (the *meaning* is sound — that hadith's chain is weak, so it is
    **not** ṣaḥīḥ; `hiteles` would be wrong there).
  - **`hasan`/`jó` untouched**, incl. ch3 fn8 (ENG "good Ḥadīth" → `jó`).
  - **Glossary** `Mu'allal` def updated: "apparently sound" → `látszólag hiteles`.
- Ch6 coinages to sanity-check: "flying columns" → **portyázó különítmények**;
  "Battle of the Ditch" → **Árok-ütközet**; "Confederates" → **szövetségesek**;
  "reciters" (Bi'r Ma'ūnah) → **recitálók**.

### 4. Verified clean (no action needed)

- Ch6 footnotes: all 84 body markers appear exactly once and the `## Lábjegyzetek`
  list runs 1–84 in order, matching ENG (checked by script, 2026-07-14).

## Chapter 7 (translated 2026-07-15)

HUN ch7 starts at line 4293 ("# Hetedik fejezet"); ENG ch7 at line 4326.
Footnotes 1–121 verified by script: list runs 1–121 in order, each body marker
appears exactly once (both ENG and HUN).

### 1. Honorific artifact — pass A, then B

- ENG ~4507: **Mūsā ibn 'Uqbah (رضي الله عنه)** — he is a later scholar
  (maghāzī author, d. 141 AH), not a Ṣaḥābī. **HUN omits the honorific.**
  Check the PDF whether the print really has it.

### 2. Qur'ān reference misprint — pass A

- ENG footnote 7 (line ~5628): "And he it is Who has withheld men's hands from
  you…" cited as **(Qur'ān 49: 24)** — the verse is 48:24. Kept as printed in
  both ENG and HUN (HUN footnote ⁷ says "Korán 49: 24").

### 3. Names/typos where HUN silently normalized — pass A (verify against PDF)

- "treaty of **Hubaybiyah**" (ENG ~4907) and "story of **Ḥubaybiyah**"
  (ENG footnote 15) → HUN writes ḥudaybiyai/Ḥudaybiyah throughout.
- "**Thābit ibn Aqrad**" (ENG ~4861) vs "Thābit ibn Arqam" (ENG ~4837, same man)
  → HUN uses Arqam/Aqram; unify in pass B once PDF checked.
- "another from **Aslaj**" (ENG ~5370, Ka'b ibn Mālik story) → HUN says
  "Aslam törzsbeli".
- "**mu'addal**" (ENG footnotes 98, 108, 116) → HUN uses the standard term
  **mu'ḍal**.
- Al-Halis / Al-Halīs ibn 'Alqamah spelling varies in ENG → HUN unified to
  Al-Halīs.

### 4. Kept as printed (decide in review)

- ENG ~5098 (Ḥunayn): Abū Sufyān: "Their defeat will not end until they reach
  the **seal**!" — almost certainly "sea"; **HUN translated "a tengerig"**.
  Confirm against PDF.
- ENG ~4827 (Mu'tah): the envoy's killer is "**Bubayl ibn 'Amr**", but at
  ENG ~4737 the same episode names **Shuraḥbīl ibn 'Amr**. HUN keeps "Bubayl
  ibn 'Amr" at the Mu'tah spot, faithful to ENG.
- ENG ~5018: "Sa'd ibn 'Ubādah, chief of the **Aws**" — he was chief of the
  Khazraj. HUN keeps "az Aws főnöke" (faithful).
- ENG ~5246 book title "Prejudice and Tolerance between Islām and Christianity"
  vs footnote 121 "Tolerance and intolerance Between Islām and Christianity" —
  same book, inconsistent in print; HUN mirrors the inconsistency
  („Az előítélet és türelem…" / „Türelem és türelmetlenség…").
- ENG ~4371 (footnote 4 context): Al-Halīs "is coming from people who are
  **confused**" — standard sīrah texts say "who venerate the sacrificial
  animals"; HUN follows ENG ("zavarban van"). Check PDF.
- ENG ~4946 duplicated sentence: "Islām has taught us not to forget the good
  deeds and virtues in him. Islām has taught us not to forget the good deeds
  and virtues of those…" — **HUN collapsed the duplication into one sentence.**
  If the print really duplicates it, ENG stays, HUN stays collapsed.
- ENG footnote 94 calls (Abul) Zubayr "a forger" while footnote 103 says he is
  "known for tadlīs" — the book's own inconsistency, kept in both files.

### 5. Ch7 coinages to sanity-check — pass B

- "Army of Hardship" → **Nehézség Serege**; "Pledge of riḍwān" →
  **riḍwān-fogadalom**; "the freed ones (ṭulaqā')" → **szabadon bocsátottak**;
  "Mosque of Dissent (ḍirār)" → **A viszály (ḍirār) mecsete**;
  "those whose hearts were to be reconciled" → **akiknek szívét meg kellett
  nyerni**; "Harnessing of the Bedouin" → **A beduinok megzabolázása**.

## Chapter 8 (translated 2026-07-15)

HUN ch8 starts at line 5855 ("# Nyolcadik fejezet"); ENG ch8 at line 5816.
Footnotes 1–24 verified by script: list runs 1–24 in order, each body marker
appears exactly once (both ENG and HUN).

### 1. Honorific artifact — pass A, then B

- ENG ~5978 and ~5980: **(عليه السلام)** after the Prophet's infant son
  **Ibrāhīm** — the honorific belongs to the ancestor-prophet Ibrāhīm, not the
  baby. **HUN omits it at these two spots.** The honorifics after the
  prophet Ibrāhīm elsewhere in the chapter (ENG ~5866, ~6030) are correct
  and kept. Check the PDF whether the print really has them on the infant.

### 2. Names/typos where HUN silently normalized — pass A (verify against PDF)

- "**Nooh**" (ENG ~5860) → HUN **Nūḥ**.
- "**Abū Sufāyn**" (ENG ~5906) → HUN **Abū Sufyān**.
- "**Mudar**" (ENG ~5996) → HUN **Muḍar**.
- "**Banu Ḥanifah**" (ENG ~5994) → HUN **Banū Ḥanīfah**.
- "**Abū Darda**" (ENG footnote 11) → HUN **Abū Dardā'**.

### 3. Kept as printed (decide in review)

- ENG ~5922: guests served "**Sumayt**" — likely *samīṭ* (roasted sheep);
  HUN keeps "*sumaytot*". Check PDF / identify the dish.
- ENG ~6048: "**Farwah ibn 'Umar al-Judhāmā**" — historically Farwah ibn
  'Amr al-Judhāmī; kept as printed in both files. The same sentence is
  garbled in ENG ("was governor or Ma'ān … on behalf of the Romans were
  enraged") — **HUN bridges it with a bracketed insertion**
  "[amikor felvette az iszlámot,]". Check the PDF for the actual sentence.
- ENG footnote 21: "**Ṣiba Ibn 'Arfataḥ a-Ghifārī**" — usually Sibā' ibn
  'Urfuṭah al-Ghifārī; kept as printed in both files.
- ENG ~5850: inline Qur'ān 4:3 quote with no reference in print ("If you
  fear that you cannot be just, then only one") — HUN likewise quotes it
  without a (Korán 4: 3) reference: "Ha pedig féltek, hogy nem tudtok
  igazságosak lenni, akkor csak egyet."
- ENG ~5936 (Qur'ān 33: 28–29) is garbled in transcription ("Say to wives…
  come! Shall content you") — HUN renders a readable version; verify the
  printed wording in pass A.

### 4. Ch8 coinages to sanity-check — pass B

- *Shari'ah* → **saría** (older HUN material once used "iszlám törvény");
- *Mujāhidin* → **mudzsáhidok**;
- "Settling Down" → **Megszilárdulás**;
- "The Farewell Pilgrimage" → **A búcsúzarándoklat**; "To Madīnah" →
  **Madīnába**;
- *'ulamā'* → ***'ulamā'* (vallástudósok)**;
- "day of the Greater Pilgrimage" → **a Nagy Zarándoklat napja**.

## Chapter 9 (translated 2026-07-15)

HUN ch9 starts after the ch8 footnotes ("# Kilencedik fejezet"); ENG ch9 body at
line 6112. **Note:** in ENG-full the ch9 footnotes 1–18 are physically at the very
end of the book (lines ~6437–6471, after the Glossary), not right after the chapter.
HUN places them in a `## Lábjegyzetek` block right after ch9 per convention.
Footnotes 1–18 verified by script: list runs 1–18 in order, each body marker appears
exactly once (both the HUN body and its footnote list).

### 1. Honorific artifact — pass A, then B

- ENG ~6148: **"O son of Khaṭṭāb (رضي الله عنه)"** — the Prophet addressing 'Umar.
  Placement of the honorific right after "Khaṭṭāb" (ʿUmar's pagan father) is odd,
  though it plausibly refers to ʿUmar (the son). **HUN keeps it** as printed
  („Ó, Khaṭṭāb (رضي الله عنه) fia"). Check the PDF.

### 2. Names/typos where HUN silently normalized — pass A (verify against PDF)

- "**Mumūnah's house**" (ENG ~6116, second mention of Maymūnah) → HUN uses
  **Maymūnah** both times.
- "the illness grew more **sever**" (ENG ~6116) → HUN normal ("súlyosbodott").

### 3. Kept / rendered as printed (decide in review)

- "what one's right hand possessed" (ENG ~6196, the slaves/dependants formula
  *mā malakat aymānukum*) → HUN literal **"akit jobb kezünk birtokol"**. Faithful
  but obscure; consider a gloss in review.
- "**the Companion on high from paradise**" (ENG ~6206, the Prophet's dying words
  *al-rafīq al-aʿlā*) → HUN title and death-scene both render **"a Legfőbb Társ"**.
  Consistent; confirm the phrasing is the preferred Hungarian rendering.
- Qur'ān 3:144 (ENG ~6218) rendered fresh into HUN; verify against a standard
  Hungarian Qur'ān translation in pass B.

## Back matter (translated 2026-07-15)

Symbols ("# A könyvben használt jelek"), Transliteration Chart ("# Átírási
táblázat"), and Glossary ("# Szójegyzék") translated. Glossary: 71 entries, verified
1:1 against ENG by script; headwords kept in the printed transliterated form (only
"Lāt and 'Uzza" → "Lāt és 'Uzza").

### 1. Kept as printed — book imprecisions (decide in review)

- **Isrā' / Mi'rāj swap:** the Glossary defines *Isrā'* as "The Prophet's ascension"
  and *Mir'āj* as "the ascension … to the heavens". Conventionally Isrā' is the night
  *journey* (Makka→Jerusalem) and Mi'rāj the ascension. HUN mirrors the book's
  definitions faithfully („*Isrā'*: A Próféta felemelkedése.").
- Book spells the ascension headword *Mir'āj* (usually Mi'rāj); kept.
- *Jahilīyyah* headword double-y as printed (running text uses jahilīyah); kept.
- Symbols: ENG prints "Subḥānahu wa **T'ālā**" (typo) → HUN corrected to
  "Subḥānahu wa Ta'ālā". The gloss 'The Exalted' → „A Magasztos" (matches the
  *Allāh* glossary entry).
- Transliteration Chart kept intact (Arabic→Latin romanization the HUN text also
  uses); only headers/notes translated. The ẓ row keeps the book's underlined
  `<u>dh</u>`.

### 2. Glossary term consistency vs running translation — pass B

Glossary headwords stay transliterated, but several appear Hungarianized in the
chapters. If a unified reader-facing form is wanted, cross-check:
*Jihād*↔dzsihád, *Tawhīd*↔tauhid, *Ummah*↔umma, *Hijrah*↔hidzsra,
*Shari'ah*↔saría, *Zakāt*↔zakát, *Khalīfah*↔kalifa.

## Carried over from earlier chapters

- HUN ch3 footnote numbering intentionally differs from ENG: HUN ch3 has no ¹⁵ entry —
  the draft's ¹⁴ covers ENG's ¹⁵; body markers match their own footnote list.
  Don't "fix" this to match ENG mechanically.
- ENG-full preserves the book's own misprints verbatim (e.g. "United Sates" p. 177,
  "Egyt" p. 194, duplicated sentence on p. 83) — intentional, per transcription
  conventions in CLAUDE.md.
