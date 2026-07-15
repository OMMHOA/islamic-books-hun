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

### 3. Terminology consistency — pass B

- Older drafts (ch1–ch3 reused material) say **Mekka / hiteles hadísz**; newer chapters
  (ch4–ch6) say **Makka / ép hadísz**. Unify (direction: Makka/ép, per CLAUDE.md).
- Ḥadīth grading map used in ch5–6: authentic → **hiteles**, sound/ṣaḥīḥ → **ép**,
  ḥasan/good → **jó**, weak → **gyenge**. Verify ch1–4 footnotes follow the same map.
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

## Carried over from earlier chapters

- HUN ch3 footnote numbering intentionally differs from ENG: HUN ch3 has no ¹⁵ entry —
  the draft's ¹⁴ covers ENG's ¹⁵; body markers match their own footnote list.
  Don't "fix" this to match ENG mechanically.
- ENG-full preserves the book's own misprints verbatim (e.g. "United Sates" p. 177,
  "Egyt" p. 194, duplicated sentence on p. 83) — intentional, per transcription
  conventions in CLAUDE.md.
