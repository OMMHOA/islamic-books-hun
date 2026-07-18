# Review flags

Items to resolve during the two review passes:
(A) verifying `FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md` against the PDF, and
(B) proofreading the Hungarian in `FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md`.

**Fidelity policy (user decision, 2026-07-16): the Arabic original is the sole source
of truth.** Corroborated English-edition errors are corrected in **both** ENG-full and
HUN — plainly, no translator's notes (the `[helyesen: … — a ford.]` convention tried
earlier the same day was reverted). Where the Arabic itself errs, both files follow
the Arabic. Every correction is logged here, and the consolidated list of English-
edition errors lives in **`ENGLISH-EDITION-ERRATA.md`**.

Line numbers refer to the files as of 2026-07-14 (after Chapter 6 landed) and will
drift as the files grow — search for the quoted text if they no longer match.

---

## Master checklist (consolidated)

The single actionable to-do list, gathered from the per-chapter sections below.
Check items off here as they're resolved; the per-chapter sections hold the detail.

### A. Honorific artifacts — verify against PDF, then decide HUN handling

- [x] **Ch6** — (رضي الله عنه) on enemies of Islam (Ka'b ibn al-Ashraf, 'Amr ibn
  'Abdul Wudd, Ka'b ibn Asad). PDF has them; Arabic original doesn't → HUN omits.
  RESOLVED 2026-07-16 (Ch6 §1). Principle: no honorifics for enemies of Islam.
  **Update (fidelity policy, 2026-07-16): removed from ENG-full too** (17 spots).
- [x] **Ch7** ~4507 — Mūsā ibn 'Uqbah (رضي الله عنه): a later scholar, not a Ṣaḥābī.
  **AR-checked (p.259): «وروى موسى بن عقبة» — plain, no honorific.** ENG insertion;
  HUN omission correct. *(ENG-print check remains pass A, transcription fidelity only.)*
- [x] **Ch8** ~5978/~5980 — (عليه السلام) on the infant Ibrāhīm. **AR-checked (p.347):
  «أسماه إبراهيم، باسم جده أبى الأنبياء» and «وإنا بك يا إبراهيم لمحزونون» — no honorific
  anywhere, not even on the ancestor mention.** ENG insertions; HUN omits — correct.
- [x] **Ch9** ~6148 — "O son of Khaṭṭāb (رضي الله عنه)". **AR-checked**: Arabic has no
  honorific («يا ابن الخطاب»); ENG inserted it and HUN wrongly blesses the pagan father.
  → dropped in HUN → „Ó, Khaṭṭāb fia". ✅ APPLIED 2026-07-16.

### B. Qur'ān reference misprints — ✅ RESOLVED (2026-07-16)

**Final decision (user, 2026-07-16, superseding the note-convention tried earlier the
same day): faithful to the Arabic only → plain corrected refs in both ENG and HUN.**

- [x] **Ch6** line ~3339 — ENG cited (Qur'ān 7: 115). **AR-checked (p.190): [البقرة:
  ١١٥] = 2:115.** (Arabic quote order is 2:142 → 2:115 → 2:177; ENG reordered to
  142 → 177 → 115.) → ENG "(Qur'ān 2: 115)", HUN „(Korán 2: 115)". ✅ APPLIED.
- [x] **Ch7** fn7 ~5628 — ENG cited (Qur'ān 49: 24). **AR-checked (p.252 fn١):
  [الفتح: ٢٤] = 48:24.** → ENG "(Qur'ān 48: 24)", HUN „(Korán 48: 24)". ✅ APPLIED.

### C. Names/typos HUN silently normalized — verify PDF spelling, then unify

- [x] **Ch7** — Hubaybiyah/Ḥubaybiyah → HUN Ḥudaybiyah (~4907, fn15). **AR: «الحديبية»** — HUN correct.
- [x] **Ch7** — Thābit ibn **Aqrad** (~4861) vs ibn **Arqam** (~4837), same man → unify.
  **AR prints BOTH** (أرقم p.281 / أقرد p.282) — book-level inconsistency; HUN→Arqam OK.
  **2026-07-16: translator's note added at the Aqrad spot in ENG + HUN** (author-error
  convention); stray HUN "Aqram" typo fixed to Arqam.
- [x] **Ch7** — "from **Aslaj**" (~5370) → HUN "Aslam törzsbeli". **AR (p.318):
  «وسعى ساعٍ من أسلم»** — Aslam; ENG typo, HUN correct.
- [x] **Ch7** — **mu'addal** (fn 98, 108, 116) → HUN standard **mu'ḍal**. **AR: the term
  is «معضل»** (seen at pp.187, 259, 349 footnotes) — HUN correct.
- [x] **Ch7** — Al-Halis / Al-Halīs varies. **AR: «الحليس»**, standard vocalization
  **al-Ḥulays** → renamed to **Al-Ḥulays/Ḥulays** in both ENG and HUN.
  ✅ APPLIED 2026-07-16 (fidelity policy).
- [x] **Ch8** — **Nooh** (~5860) → HUN Nūḥ. **AR (p.336): «من عهد نوح»** — HUN correct.
  (Arabic has no honorific there; ENG added (عليه السلام) — harmless, he is a prophet.)
- [x] **Ch8** — **Abū Sufāyn** (~5906) → Abū Sufyān — obvious corruption, fixed in
  ENG too (fidelity policy). ✅ APPLIED 2026-07-16.
- [x] **Ch8** — **Mudar** (~5996) → HUN Muḍar. **AR (p.349): «مضر»** — HUN correct.
- [x] **Ch8** — **Banu Ḥanifah** (~5994) → HUN Banū Ḥanīfah. **AR (p.349): «بني حنيفة»** —
  HUN correct. Bonus: Arabic reads «ظهر **فيها وفي بني حنيفة** دجالان» — the two impostors
  appeared "in it [Yemen] *and* in Banū Ḥanīfah" (al-Aswad al-ʿAnsī + Musaylimah); ENG
  flattened this to "in the Banu Ḥanifah" → HUN fixed: „Ott és a Banū Ḥanīfában".
  ✅ APPLIED 2026-07-16.
- [x] **Ch8** — **Abū Darda** (fn11) → HUN Abū Dardā'. **AR: «أبو الدرداء»** — HUN correct.
- [x] **Ch9** — **Mumūnah** (~6116) → HUN Maymūnah. **AR: «ميمونة»** — HUN correct.
- [x] **Ch9** — "grew more **sever**" (~6116) → "severe", fixed in ENG (print typo;
  HUN "súlyosbodott" was already fine). ✅ APPLIED 2026-07-16.

### D. Garbled / dubious passages kept as printed — verify PDF, decide

- [x] **Ch7** ~5098 — "until they reach the **seal**!" → **AR: «دون البحر» = "sea"**; ENG
  typo, HUN „a tengerig" correct.
- [x] **Ch7** ~4827 vs ~4737 — envoy's killer. **AR: «شرحبيل بن عمرو» = Shuraḥbīl** (p.280);
  ENG "Bubayl" is a corruption → HUN changed to Shuraḥbīl. ✅ APPLIED 2026-07-16.
- [x] **Ch7** ~5018 — "Sa'd ibn 'Ubādah, chief of the **Aws**" (was Khazraj). **AR-checked
  (p.292): the Arabic original itself prints «سعد بن عبادة زعيم الأوس»** — al-Ghazali's own
  error, ENG faithful → kept in both files **with translator's note** (ENG ~5018,
  HUN ~5001). ✅ APPLIED 2026-07-16.
- [ ] **Ch7** ~5246 / fn121 — book title "Prejudice and Tolerance…" vs "Tolerance and
  intolerance…" inconsistency → HUN mirrors both
- [x] **Ch7** ~4371 / fn4 — Al-Halīs "people who are **confused**". **AR: «قوم يتألهون»** =
  "devout / venerate the sacred rites"; ENG mistranslation → HUN „zavarban van" changed to
  „istenfélő". ✅ APPLIED 2026-07-16.
- [x] **Ch7** ~4946 — duplicated sentence. **AR-checked (p.289): single sentence**
  («علمنا الإسلام ألا ننسى الحسنات والفضائل لمن يخطئون حينًا بعد أن أصابوا طويلا») — the
  duplication is an ENG-edition dittography → HUN stays collapsed; ENG stays as printed
  *(pass-A: confirm the ENG print really duplicates)*.
- [x] **Ch7** fn94 vs fn103 — (Abul) Zubayr "a forger" vs "known for tadlīs". **AR-checked:
  the Arabic says مدلس in BOTH** (p.307 fn٣ «أبو الزبير مدلس وقد عنعنه»; p.315 fn١ «أبا
  الزبير مدلس»; same again in ch4's pledge footnote, p.114 fn١ «عنعنة أبي الزبير وكان
  مدلسًا») — "a forger" is an **ENG mistranslation pattern**, not the book's inconsistency.
  → HUN fixed „hamisító" → „ismert a tadlīsról" at fn94 (~5797) **and** ch4 fn4 (~2236);
  fn103 already said „tadlīsról ismert". ✅ APPLIED 2026-07-16. ENG stays as printed.
- [x] **Ch8** ~5922 — dish "**Sumayt**". **AR-checked (p.343): «ولا رأى شاة سميطًا بعينه
  قط»** — a whole roasted/scalded sheep (*shāh samīṭ*); ENG even dropped the word "sheep".
  → HUN fixed: „sumaytot" → „egészben sült birkát (*samīṭ*)". ✅ APPLIED 2026-07-16.
- [x] **Ch8** ~6048 — Farwah. **AR-checked (p.353): «فروة بن عمرو الجذامي»** = Farwah ibn
  **'Amr** al-**Judhāmī** (ENG "'Umar…Judhāmā" doubly corrupt), and the garbled ENG sentence
  lost «فاعتنق الإسلام وبعث إلى النبي ﷺ يخبره بذلك» (he embraced Islam and sent word to the
  Prophet — this is what enraged the Romans; beheaded at the water of «عفراء» in Palestine,
  left crucified). → HUN fixed: name corrected + bracketed bridge replaced with the full
  clause „amikor felvette az iszlámot, és követe útján hírül adta ezt a Prófétának (ﷺ)".
  ✅ APPLIED 2026-07-16.
- [x] **Ch8** fn21 — "**Ṣiba Ibn 'Arfataḥ a-Ghifārī**". **AR-checked (p.349 fn١):
  «سباع بن عرفطة الغفاري»** = Sibā' ibn 'Urfuṭah al-Ghifārī; ENG corrupt → HUN fixed.
  ✅ APPLIED 2026-07-16. (Same footnote also prints «معضلاً» — mu'ḍal again.)
- [ ] **Ch8** ~5850 — inline Qur'ān 4:3 with no reference in print → HUN also no reference
- [ ] **Ch8** ~5936 — Qur'ān 33:28–29 garbled in transcription → verify printed wording.
  **AR (p.346): full verses printed cleanly** [الأحزاب: ٢٨، ٢٩] — the garble is ENG-side;
  check the ENG print in pass A, and check the HUN rendering against the Arabic wording.
- [ ] **Ch9** ~6196 — "what one's right hand possessed" (*mā malakat aymānukum*) → HUN
  literal "akit jobb kezünk birtokol"; consider a gloss
- [ ] **Ch9** ~6206 — "the Companion on high from paradise" (*al-rafīq al-aʿlā*) → HUN
  "a Legfőbb Társ"; confirm preferred rendering

### E. Pass-B leftovers (Hungarian side)

- [ ] **Ch6** coinages — portyázó különítmények / Árok-ütközet / szövetségesek / recitálók
- [ ] **Ch7** coinages — Nehézség Serege / riḍwān-fogadalom / szabadon bocsátottak /
  A viszály (ḍirār) mecsete / akiknek szívét meg kellett nyerni / A beduinok megzabolázása
- [ ] **Ch8** coinages — saría / mudzsáhidok / Megszilárdulás / A búcsúzarándoklat /
  Madīnába / 'ulamā' (vallástudósok) / a Nagy Zarándoklat napja
- [ ] **Ch9** — Qur'ān 3:144 rendered fresh; verify vs a standard Hungarian Qur'ān translation
- [ ] **Glossary** — optional full Hungarian re-alphabetization of all 71 entries (currently
  book-order; "Dzsihád" sits in the old *J*-cluster). Separate pass if wanted.
- [ ] **Glossary** book imprecisions kept as printed — decide: Isrā'/Mi'rāj definition swap,
  *Mir'āj* headword spelling, *Jahilīyyah* double-y (back matter §1)

### F. Housekeeping

- [ ] Update `README.md` links (stale now that all chapters landed)
- [ ] Decide fate of legacy/working files: partial `-ENG.md`, `chapter*-normalized.md`,
  `-HUN-Chapter3…md`, `-HUN-Khadijah.md` (superseded by the `-full` files)

### G. Arabic-source verification plan (2026-07-16) — SUPERSEDES the old pass A

**Rationale (user decision 2026-07-16):** the Arabic is the sole source of truth, and
every corroboration so far has shown the English edition carries its own errors that
read fluently (seal/sea, forger/tadlīs, corrupted names…). Proofreading ENG-full
against the *English* scan can only catch our OCR mistakes while re-validating the
English edition's translation mistakes. So the verification pass targets the Arabic
directly; the old "pass A vs ENG scan" is demoted (residual ENG OCR errors matter only
where they propagated to HUN — G3 catches those; ENG-print spot-checks still open,
e.g. the ch7 ~4946 dittography, fold into G3).

- [x] **G1. Transcribe the Arabic original** → `FiqhusSeerah-Muhammad-al-Ghazali-AR-full.md`
  — **DONE 2026-07-17.** Printed pages 2–368 (367 page blocks), ~126.5k words, whole-book
  `[صفحة N]` continuity verified by script (no gaps, no duplicates). PDF 368 = back cover,
  not transcribed. Source: `فقه السيرة - محمد الغزالي.pdf`, 368 pages, image-only,
  **printed page = PDF page + 1** (TOC on printed 365–367). Same parallel-subagent
  pipeline as the ENG run (2026-07-13); fragments in `.transcription-fragments/ar/`.
  Page markers `[صفحة N]` per printed page; per-page footnotes as blockquotes after
  each page. **Caveat: the AR transcription is a locating/reading aid, not gospel** —
  Arabic OCR is more error-prone; decision-critical readings are re-checked on the
  rendered PDF page (now with an exact location to look at).
  Chapter → PDF-page map: front 1–13, ch1 14–44, ch2 45–69, ch3 70–107, ch4 108–133,
  ch5 134–157, ch6 158–245, ch7 246–331, ch8 332–352, ch9+خاتمة+TOC 353–367.
  Known transcription-quality notes:
  - 9 `[غير مقروء]` spots, all in ch7b's slice (printed 293, 295, 297, 300, and several
    on 304 — worst print degradation of the book; the rest recovered at high DPI).
  - Repaired during stitching: ch8's agent had skipped printed 346 and mislabeled
    347–349 as 346–348 — caught via marker-gap check, markers renumbered, page 346
    transcribed directly from the rendered scan (main-session verification).
  - Name-spelling inconsistencies preserved as printed (e.g. ثابت بن أرقم / ثابت بن أقرد
    on one page; نوف بن معاوية vs نوفل, printed 286); ch3: printed 96 has two (١) body
    markers, the second footnote's text typeset at the bottom of printed 97.
- [x] **G2. Scripted Qur'ān-reference sweep** — **DONE 2026-07-17.** Script
  (`scripts/g2_quran_sweep.py`, re-runnable) extracted every `(Korán X: Y)` / `(Qur'ān X: Y)`
  ref (HUN 222, ENG 221), validated all against the Kufan āyah counts (surah 1–114,
  āyah ≤ max, ranges ascending) — **zero out-of-range refs** — and sequence-aligned
  the ENG↔HUN ref lists. Findings (all corroborated against the Arabic original):
  - **ENG 43:19-20 + 43:21-23 → 53:19-23** (ch3, cranes/Sūrat an-Najm passage;
    AR p.87 prints سورة النجم) — fixed in ENG-full; HUN was already correct.
    Errata #2a.
  - **ENG 3:91 → 3:191** (ch5, ﴿ربنا ما خلقت هذا باطلاً﴾; AR p.148 prints
    [آل عمران: ١٩١]) — fixed in ENG-full; HUN was already correct. Errata #2b.
  - HUN fn12 (ch3) carries a clarifying **(Korán 16: 106)** the ENG footnote lacks —
    intentional HUN addition, ref verified correct (the ʿAmmār verse); kept.
    *(After the G4 ch3 renumbering this body marker is fn13.)*
  Quoted-wording verification (vs canonical text) folds into G3, which reads every
  quote against the Arabic anyway.
- [ ] **G3. Chunk-aligned HUN ↔ AR verification pass** — subagents compare the HUN
  translation against the Arabic text chunk by chunk. Catches all three error classes
  at once: ENG OCR errors, undiscovered ENG-edition mistranslations, HUN drift.
  Absorbs the remaining D-items and the E coinage checks in context.
- [x] **G4. Name + ḥadīth-grade sweep** — **DONE 2026-07-18.** Scripts:
  `scripts/g4_grade_sweep.py` (per-chapter ENG↔HUN footnote grade-label alignment +
  HUN untranslated-label scan), `scripts/g4_ar_align.py` (AR per-page footnote grades
  bucketed by the chapter→page map, sequence-aligned vs ENG),
  `scripts/g4_name_sweep.py` (capitalized-token clustering on diacritic-stripped keys,
  both files). Findings & fixes:
  - **Grades:** every ENG↔HUN leading grade label agrees (S/H/W/NS); the AR alignment
    flags were all drift artifacts of the English edition's footnote merging (spot-checks
    incl. ch6 fn52–54 vs AR p.202 confirmed correct, e.g. ENG fn53 "Not authentic" =
    AR «حديث لا يصح»). 6 HUN footnotes still carried untranslated `Ṣaḥīḥ` labels
    (ch4 fn18/19/22, ch6 fn7/45/55) → `Hiteles (ṣaḥīḥ)` per convention.
  - **ch3 footnote repair:** the "HUN ch3 skips ¹⁵ by design" belief was a
    misdiagnosis — HUN had *dropped ENG fn9* (Al-Albānī's grading of the Sūrat
    ul-Lahab story; AR p.76 fn١ «حديث صحيح أخرجه البخارى ومسلم»), shifting fn9–15.
    Restored fn9 („Hiteles hadísz, Bukhārī és Muszlim beszélte el."), renumbered
    9–14→10–15; HUN ch3 is now a clean 1–34, body↔list 1:1 verified by script.
  - **Names (fixed in both files per fidelity policy):** ENG "Ibn Ḥibbān" (kunyah of
    'Abdullāh ibn Ubayy, ch1) → **Abū Ḥibbān** per AR p.23 «أبو حبان» + translator's
    note (the Arabic itself misprints the well-known **Abū Ḥubāb**); "Abbān ibn Sa'īd"
    → **Abān** per AR p.253 «أبان» + note (AR misprints his father as «سعد», correct
    Sa'īd — rendered-page verified for both); Badīl/Budayl → **Budayl** (AR بديل
    identical); Abū Bukhtari/Abul Bukhturi → **Abul Bukhturi** (AR البخترى identical,
    Badr list + ṣaḥīfah scene); Al-Qarrah/Al-Qārrah → **Al-Qārah** (AR القارة in both
    the Rajī' and Bi'r Ma'ūnah lists — note the AR prints al-Qārah where the canonical
    Bi'r Ma'ūnah list has 'Uṣayyah; kept faithful); Ubāyy→Ubayy (6×/file);
    Zainab→Zaynab, Ruqaiyyah/Ruqayya→Ruqayyah, Jamuḥ→Jamūh, Aḥmed→Aḥmad (ENG+HUN).
  - **ENG print typos fixed silently:** Shybah→Shaybah, Kharzraj→Khazraj,
    Zoroastranism→Zoroastrianism, Muhammed→Muhammad (2×).
  - **HUN-internal unifications:** Anasz(tól)→Anas(tól), Hurayrah→Hurairah,
    Khoszrau→Khosrau; the restored Bilāl-couplet's phonetic spellings aligned to the
    book's transliteration (dzsalíl→jalīl, Madzsanna→Majannah, Sámah és Tafíl→Shāmah
    és Ṭafīl).
  - **Checked and left alone (verified legit/faithful):** Samwān fort + 'Azūl duelist
    (AR p.264 prints سموان/عزولا), Al-Wāḥidī (real muffasir, ≠ Wāqidī), Wāqifī,
    Kharijah, 'Utban ('Itbān ibn Mālik), Ḥudhāfah, Zubayd (tribe), Sirar (place),
    al-Sulamī "Al Salami", 'Umayr ibn al-Ḥumām "Hamām", Majnah/Dhul-Majāz markets,
    Naufal/Nawfal (per-person variance, mirrored consistently), plus the book-wide
    diacritic variance the English edition itself carries (Ḥākim/Ḥakim etc.).

---

## Arabic-original corroboration (2026-07-16)

Checked the flagged items against the **Arabic original** `فقه السيرة - محمد الغزالي.pdf`
(Maṭābiʿ al-Shurūq ed., 368 pp, image-only — no text layer). **Offset: printed page =
PDF page + 1** (i.e. PDF page = printed − 1). Note the Arabic edition *does* carry the
ḥadīth-grading footnotes (صحيح/ضعيف), so footnote items are checkable here too. Arabic
Qurʾān citations sampled were all correct ([الفتح: ٢٧]=48:27, [النور: ٣٣]=24:33,
[طه: ١٣١،١٣٢]), supporting that the two flagged verse misprints are English-edition errors.

### Corroborated — HUN fixes ✅ APPLIED (2026-07-16)

- **A-ch9 Khaṭṭāb honorific** (printed p.356): Arabic reads plain **«يا ابن الخطاب»** —
  **no honorific**. The ENG (رضي الله عنه) is an English-edition insertion, and the current
  HUN „Khaṭṭāb (رضي الله عنه) fia" wrongly attaches the blessing to the *pagan father*
  al-Khaṭṭāb. → **Drop it in HUN**: „Ó, Khaṭṭāb fia". (Consistent with the enemy-of-Islam
  principle re the pagan father.)
- **D-ch7 Al-Ḥulays "confused"** (printed p.250): Arabic **«إن هذا من قوم يتألهون»** = "a
  people who are devout / venerate [the sacred rites]"; the passage then has him awed
  (إعظاماً) by the sight of the hady. ENG "confused" is a **mistranslation**; HUN
  „zavarban van" is **wrong → fix** (e.g. „istenfélő nép" / „akik tisztelik a szent
  [áldozati állatokat]").
- **D-ch7 Bubayl → Shuraḥbīl** (printed p.280): the envoy's killer is
  **«شرحبيل بن عمرو»** (Shuraḥbīl ibn ʿAmr) — «أوثق شرحبيل بن عمرو رباطه ثم قدمه فضرب عنقه».
  ENG "Bubayl ibn ʿAmr" is a corruption; HUN keeps "Bubayl" → **change to Shuraḥbīl**
  (matches the other ENG mention at ~4737 and the Arabic).

### Corroborated — HUN already correct (no change)

- **D-ch7 "seal" → "sea"** (printed p.299): **«لا تنتهي هزيمتهم دون البحر»** = "the sea".
  ENG "seal" is the typo; HUN „a tengerig" is right.
- **C-ch7 Ḥudaybiyah**: Arabic **«الحديبية»** throughout ch7. HUN Ḥudaybiyah correct;
  ENG "Hubaybiyah/Ḥubaybiyah" is a corruption.
- **C-ch9 Maymūnah** (printed p.354): **«ميمونة»**. HUN correct; ENG "Mumūnah" is a typo.
- **C-ch8 Abū Dardā'** (printed p.344, footnote): **«أبو الدرداء»**. HUN correct.

### Corroborated — book-level inconsistency (ENG faithful, HUN unified)

- **C-ch7 Thābit ibn Aqrad / Arqam**: the **Arabic original itself prints both** —
  **«ثابت بن أرقم»** (printed p.281, Abū Hurayrah narration) and **«ثابت بن أقرد»**
  (printed p.282, banner scene). So the ENG double-spelling faithfully mirrors the Arabic.
  HUN's unification to the historically-correct **Arqam** is sound.

### Second pass (2026-07-16, later session) — ✅ ALL remaining items checked

Chapter page map from the Arabic TOC (printed pages): ch4 الهجرة العامة 109, ch5 أسس
البناء 135, ch6 الكفاح الدامي 159, ch7 طور جديد 247 (الفتح الأعظم 285, حنين 297,
الطائف 306, تبوك 310, المخلفون 316), ch8 أمهات المؤمنين 333 (استقرار 348, حجة
الوداع 349, إلى المدينة 352), ch9 الرفيق الأعلى 354, خاتمة 362.

Results (details + applied HUN fixes are in the Master checklist above):

- **B misprints**: Arabic prints **[البقرة: ١١٥]** (p.190) and **[الفتح: ٢٤]** (p.252 fn١)
  — both flagged refs are ENG-edition misprints. Arabic quote order on p.190 is
  2:142 → 2:115 → 2:177 (ENG reordered). Decision: keep as printed + translator's note
  (`[helyesen: X: Y — a ford.]`) — applied to both spots in HUN.
- **A-ch7 Mūsā ibn ʿUqbah** (p.259): plain, no honorific — ENG insertion; HUN correct.
- **A-ch8 infant Ibrāhīm** (p.347): plain «إبراهيم» / «يا إبراهيم» — ENG insertions;
  HUN correct.
- **C names**: Aslam (p.318), Nūḥ (p.336), Muḍar (p.349), Banū Ḥanīfah (p.349),
  mu'ḍal «معضل» (pp.187/259/349 fns) — all confirm HUN normalizations. New sub-flag:
  Arabic «الحليس» suggests **al-Ḥulays**, HUN currently "Al-Halīs".
- **D**: Sa'd ibn ʿUbādah "chief of the Aws" is **in the Arabic original** (p.292);
  duplicated Ḥātib sentence is ENG dittography (Arabic single, p.289); "Sumayt" =
  «شاة سميطًا» roasted sheep (p.343); Farwah = «فروة بن عمرو الجذامي» + lost clause
  «فاعتنق الإسلام وبعث إلى النبي ﷺ يخبره بذلك» (p.353); Zubayr "forger" = ENG
  mistranslation of «مدلس» (pp.307/315 fns; also ch4 pledge fn, p.114); ch8 fn21 =
  «سباع بن عرفطة الغفاري» (p.349 fn١); Aḥzāb 28–29 printed cleanly (p.346).

**HUN fixes applied this pass (6):** fn94 + ch4 fn4 „hamisító" → „ismert a tadlīsról";
„sumaytot" → „egészben sült birkát (*samīṭ*)"; Farwah name + un-bracketed Islam-clause;
„Ott és a Banū Ḥanīfában" (two impostors: Yemen + B. Ḥanīfah); ch8 fn21 → Sibā' ibn
'Urfuṭah al-Ghifārī.

### Fidelity-policy application to ENG-full (2026-07-16, after the policy decision)

Per the Arabic-only fidelity policy, all corroborated English-edition errors were
corrected **in `-ENG-full.md` as well** (they had previously been kept "as printed"):

- Qur'ān refs 7:115 → **2:115** (3339), 49:24 → **48:24** (fn7)
- Honorifics removed where the Arabic has none: Ka'b ibn al-Ashraf ×6, 'Amr ibn 'Abdul
  Wudd ×2, Ka'b ibn Asad ×9 (enemy honorifics, ch6); Mūsā ibn 'Uqbah (4507); infant
  Ibrāhīm ×2 (5978/5980); "O son of Khaṭṭāb" (6148)
- Names: Bubayl → **Shuraḥbīl** (4827); Hubaybiyah/Ḥubaybiyah → **Ḥudaybiyah** (4907,
  fn15); Aslaj → **Aslam** (5370); Mumūnah → **Maymūnah** (6116); Abū Darda → **Abū
  Dardā'** (fn11); Al-Halis/Al-Halīs/Halīs → **Al-Ḥulays/Ḥulays** (4369–4377; Arabic
  «الحليس» — HUN renamed too); "Mursi ibn 'Aqabah" → **Mūsā ibn 'Uqbah** (ch6 fn36 —
  also fixed in HUN fn36, which had carried the corruption); mu'addal → **mu'ḍal**
  (fns 36/98/108/116); Ṣiba Ibn 'Arfataḥ a-Ghifārī → **Sibā' ibn 'Urfuṭah al-Ghifārī**
  (fn21); Farwah ibn 'Umar al-Judhāmā → **Farwah ibn 'Amr al-Judhāmī** + restored lost
  clause (6048)
- Text: "reach the seal" → **"reach the sea"** (5098); "people who are confused" →
  **"devout"** (4371, «يتألهون»); Ḥātib duplicated sentence collapsed (4946); "Sumayt"
  → **"a whole roasted sheep (samīṭ)"** (5922); "a forger" → **"known for tadlīs"**
  (fn4 ch4, fn94 ch7, «مدلس»); "grew more sever" → **severe** (6116, print typo)
- The `[helyesen: … — a ford.]` notes in HUN were replaced by plain corrected refs.

NOT changed (Arabic itself has it): Sa'd ibn 'Ubādah "chief of the Aws" (p.292);
Thābit Aqrad/Arqam double spelling (Arabic prints both; HUN unified to Arqam).

---

## Chapter 6 (translated 2026-07-14)

### 1. Honorific (رضي الله عنه) after enemies of Islam — ✅ RESOLVED (2026-07-16)

The ENG transcription places (رضي الله عنه) after men who died as enemies of Islam.
**PDF confirmed (2026-07-16): the official English translation really does print them**
(e.g. Ka'b ibn al-Ashraf). But the **Arabic original has none** — they are artifacts of
the English translation. **Decision — editorial principle: no Islamic honorifics for
enemies of Islam.** Originally they stayed in ENG-full (faithful-transcription rule);
**under the 2026-07-16 Arabic-only fidelity policy they were removed from ENG-full
as well**. Omitted from HUN throughout. Flag closed.

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

- **Place name → `Mekka`** (the standard Hungarian spelling). History: on 2026-07-15 the
  17 ch1 `Mekka` forms were first unified *to* `Makka` (matching the newer chapters); on
  2026-07-16, per user decision, the whole book was reversed to **`Mekka`** (all `Makka*`
  place forms incl. the `makkai` adjectives). The ordinary Hungarian word *mekkora*
  ("how big") and unrelated words containing the substring *makk* (*bántalmakkal*,
  *szidalmakkal*, *alkalmakkor*) were left alone.
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

### 2. Glossary term consistency vs running translation — ✅ DONE (2026-07-16)

Decision: **Hungarianize the flagged headwords** to match the running text. Changed 6:
*Jihād*→**Dzsihád**, *Tawhīd*→**Tauhid**, *Ummah*→**Umma**, *Hijrah*→**Hidzsra**,
*Shari'ah*→**Saría**, *Khalīfah*→**Kalifa** (its redundant "Kalifa." gloss removed).
*Zakāt* was in the flag list but **has no glossary headword** (glossary runs A→Uqiyah,
no Z entry) — nothing to change.

**Open sub-question (ordering):** the glossary preserves the printed book's
(transliterated) entry order, not Hungarian collation, so the headwords were changed
**in place**. Six stay in their letter-neighborhood, but **Dzsihád** now sits in the
old *J*-cluster (between *Janābah/Jannah* and *Jizyah*). Left there to avoid a partial
re-sort of an otherwise book-ordered list. If a full Hungarian re-alphabetization of all
71 entries is wanted, that's a separate pass.

## Carried over from earlier chapters

- HUN ch3 footnote numbering intentionally differs from ENG: HUN ch3 has no ¹⁵ entry —
  the draft's ¹⁴ covers ENG's ¹⁵; body markers match their own footnote list.
  Don't "fix" this to match ENG mechanically.
- ENG-full preserves the book's own misprints verbatim (e.g. "United Sates" p. 177,
  "Egyt" p. 194, duplicated sentence on p. 83) — intentional, per transcription
  conventions in CLAUDE.md.
