# islamic-books-hun

Goal: translate Islamic books to Hungarian, published as Markdown in this repo.
**Repo layout (since 2026-07-18): each book gets its own directory.** Root holds
only `README.md`, `LICENSE`, and this file.
Current book: **Fiqh-us-Seerah** by Muhammad al-Ghazali (IIPH Revised 2nd Edition,
1420 AH / 1999 CE, English translation, with Ḥadīth commentary by Sheikh
Muhammad Naṣiruddīn Al-Albānī) — everything in `fiqh-us-seerah/`; bare file names
below are relative to that directory.

## Pipeline

1. **English transcription** from the scanned PDF — ✅ done (2026-07-13, commit `edf317e`)
2. **Verification / proofreading** of the transcription — ⬜ not started (commit is marked "unverified")
3. **Hungarian translation** — ✅ **full draft complete** in
   `FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md` (2026-07-15): front matter +
   Chapters 1–9 + Epilogue ("# Utószó") + back matter ("# A könyvben használt jelek",
   "# Átírási táblázat", "# Szójegyzék"). The Glossary has all 71 entries (headwords
   kept in transliterated form as printed; only "Lāt and 'Uzza" → "Lāt és 'Uzza"
   changed). Remaining work is now **review/proofreading only** (pass B), tracked in
   `REVIEW-FLAGS.md`.
   Reused earlier drafts: sections 1.1–1.2, ch2 second half (Khadījah→Waraqah + footnotes),
   ch3 first third. (The ch3 draft's "no ¹⁵ by design" numbering turned out to be a
   dropped fn9 — restored and renumbered in G4, 2026-07-18; HUN ch3 now matches ENG 1:1.)
   Footnote counts after the G3 restorations + G4 ch3 repair (2026-07-18, all verified
   1:1 body↔list by script in both files): ch1 1–20, ch2 1–25, ch3 1–34,
   ch4 1–22, ch5 1–23, ch6 1–84, ch7 1–122, ch8 1–24, ch9 1–18. Note: ENG-full keeps ch9's
   footnotes at the very end of the book (after the Glossary); HUN places them right after
   ch9 per convention.
   **Review flags are tracked in `REVIEW-FLAGS.md`** — add new flags there, not here.
   **Pass-B terminology done (2026-07-16):** place name unified to **Mekka**; ḥadīth
   grade unified to **hiteles** (ṣaḥīḥ/sound/authentic — `ép` dropped as a grade); 6
   glossary headwords Hungarianized (Dzsihád/Tauhid/Umma/Hidzsra/Saría/Kalifa). See
   REVIEW-FLAGS §2–3. **Arabic-original corroboration complete (2026-07-16):** every
   flagged content question was checked against the Arabic original (`فقه السيرة`,
   image-only PDF, printed page = PDF page + 1); the honorific artifacts, both Qur'ān
   ref misprints (7:115→2:115, 49:24→48:24) and the garbled names/passages are all
   **English-edition errors** — 9 HUN fixes applied (see REVIEW-FLAGS "Arabic-original
   corroboration"). **Fidelity policy (2026-07-16): faithful to the Arabic original
   only** — corroborated English-edition errors are corrected in *both* ENG-full and
   HUN (done for all items verified so far: refs 2:115/48:24, enemy honorifics, Bubayl→
   Shuraḥbīl, seal→sea, Ḥulays, Aslam, Farwah, Sumayt, forger→tadlīs, dup sentence, etc.).
   Still open: pass-A checks against the *Arabic* (remaining transcription-quality
   doubts), coinage sanity-checks, and optional full glossary re-alphabetization.

## Files

All in `fiqh-us-seerah/`:

| File | What it is |
|---|---|
| `FiqhusSeerah-Muhammad-alGhazali.pdf` | Source scan, 512 PDF pages, no text layer. **PDF page = printed page − 2** |
| `FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md` | Complete English transcription: Preface → Chapters 1–9 → Epilogue → Glossary, ~176k words |
| `فقه السيرة - محمد الغزالي.pdf` | Arabic original scan (Maṭābiʿ al-Shurūq ed.), 368 PDF pages, no text layer. **Printed page = PDF page + 1**; PDF 368 = back cover |
| `FiqhusSeerah-Muhammad-al-Ghazali-AR-full.md` | Complete Arabic transcription (2026-07-17): printed pages 2–368, ~126.5k words, `[صفحة N]` page markers, per-page footnote blockquotes. Locating/reading aid for verification — not gospel; decision-critical readings re-checked on the rendered page. 9 `[غير مقروء]` spots (ch7, pp. 293–304) |
| `FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md` | **The Hungarian translation** — complete draft, front matter → Chapters 1–9 → Utószó → back matter |
| `REVIEW-FLAGS.md` | Running list of items for the verification/proofreading passes (transcription artifacts, misprints, terminology to unify) |
| `ENGLISH-EDITION-ERRATA.md` | Consolidated list of the English edition's errors verified against the Arabic original (wrong Qur'ān refs, inserted honorifics, mistranslations, corrupted names) — all corrected in both ENG-full and HUN per the fidelity policy |
| `g3-findings/` | Per-chapter findings of the G3 HUN ↔ AR verification pass (the reasoning behind each applied fix); outcomes are summarized in REVIEW-FLAGS §G and the errata file |

Deleted in the 2026-07-18 housekeeping (recoverable from git history): the legacy
partial `-ENG.md`, the partial HUN drafts (`FiqhusSeerah-Muhammad-al-Ghazali.md`,
`-HUN-Chapter3…`, `-HUN-Khadijah`), the `chapter*-normalized.md` working files,
`.transcription-fragments/`, and the one-shot `scripts/g2_*`/`g4_*` sweep scripts.

## How the transcription was made (2026-07-13)

Parallel Claude Sonnet subagents each transcribed a chapter (long chapters split in
thirds) from rendered PDF pages; fragments were then stitched and the split-chapter
seams and footnote numbering verified (ch. 6 footnotes 1–84, ch. 7 footnotes 1–121,
continuous). Each agent self-checked footnote marker ↔ text matching and page
continuity, but **no human or second-model proofread has happened yet**. Agents
flagged and preserved the book's own misprints verbatim (e.g. "United Sates" p. 177,
"Egyt" p. 194, duplicated sentence on p. 83). *(Preservation policy since superseded —
see the fidelity policy under Transcription conventions.)*

## Transcription conventions (keep these when editing/verifying)

- **Fidelity policy (user decision 2026-07-16): the Arabic original is the sole source
  of truth.** English-edition errors (mistranslations, corrupted names, wrong Qur'ān
  refs, honorifics the Arabic doesn't have) are **corrected in both `-ENG-full.md` and
  the HUN file** once corroborated against the Arabic PDF — no translator's notes, just
  the correct text; log every correction in `REVIEW-FLAGS.md`. Obvious English print
  typos ("United Sates", "Egyt") may be fixed silently in pass A. Where the **Arabic
  itself** errs (e.g. Sa'd ibn 'Ubādah "chief of the Aws", AR p.292), both files stay
  faithful to the Arabic **and get an inline bracketed translator's note** — ENG
  `[… — translator's note]`, HUN `[… — a ford.]`. (This supersedes the original
  "faithful to the printed English text, typos included" rule.)
- Diacritics preserved: Qur'ān, Ḥadīth, Madīnah, Āyāh, Ṣaḥābī…
- Honorifics: (ﷺ) after the Prophet/Muhammad, (ﷻ) after Allah, (رضي الله عنه), (عليه السلام)
- Qur'ān quotes: plain paragraph in parentheses + `(Qur'ān X: Y)` reference
- Headings: `# Chapter N` + `# Title` (two lines), `##` for sections
- Footnotes: Unicode superscript markers (¹ ² ³…) in text; texts collected in a
  `## Footnotes` block at the end of each chapter, numbered per chapter as in the book
- Poetry couplets: each line its own *italic* paragraph
- The book's ❑ paragraph ornament is dropped

## Hungarian translation conventions (from existing HUN files)

- Same heading/honorific/footnote conventions as above
- Qur'ān quotes: `(… szöveg …) (Korán X: Y)` — en-dash in verse ranges (pl. 10: 68–70)
- Hungarian quotation marks: „…"
- Terms: Allah (no diacritic in HUN running text), Korán, hadísz, umma, tauhid,
  Mohamed → **Muhammad** (kept as in existing HUN files)
- Place name: **Mekka** (the standard Hungarian spelling); leave the ordinary Hungarian
  word *mekkora* ("how big") alone
- **Ḥadīth grading terms:** ṣaḥīḥ / "sound" / "authentic" → **hiteles** (one grade, one
  word — matches the glossary `*Ṣaḥīḥ*: hiteles hadísz`); ḥasan / "good" → **jó**;
  ḍaʿīf / "weak" → **gyenge**. Al-Albānī's `Ṣaḥīḥ:` footnote labels → `Hiteles (ṣaḥīḥ):`.
  **`ép` is NOT a grade** — it is the ordinary word "intact/sound" (ép ítélőképesség, ép
  testű, "az értelme ép"); do not use it for ṣaḥīḥ. (An earlier draft's *ép*-for-sound
  convention was reverted book-wide on 2026-07-16 — see `REVIEW-FLAGS.md` §3.)

## Next steps

The Hungarian **translation draft is complete** and pass-B **terminology** is done
(see the pipeline note above). **New verification plan (2026-07-16): verify against
the Arabic original directly** — see REVIEW-FLAGS `§G` for the full rationale and the
chapter→PDF-page map. This supersedes the old "pass A vs the English scan" (which
could only catch our OCR errors while re-validating the English edition's own
translation errors).

1. ~~**G1 — transcribe the Arabic original**~~ ✅ **done 2026-07-17**:
   `FiqhusSeerah-Muhammad-al-Ghazali-AR-full.md`, printed pages 2–368, continuity
   verified. A locating/reading aid, not gospel — decision-critical readings get
   re-checked on the rendered page. Details in REVIEW-FLAGS §G.
2. ~~**G2 — scripted Qur'ān-reference sweep**~~ ✅ **done 2026-07-17**
   (`scripts/g2_quran_sweep.py`; zero out-of-range refs, 2 ENG ref errors fixed —
   details in REVIEW-FLAGS §G).
3. ~~**G3 — chunk-aligned HUN ↔ AR verification pass**~~ ✅ **done 2026-07-17/18**
   (per-chapter subagents, findings in `g3-findings/`; all FIX items applied incl.
   5 dropped-footnote restorations — details in REVIEW-FLAGS §G and the errata file).
4. ~~**G4 — name + ḥadīth-grade sweep**~~ ✅ **done 2026-07-18**
   (`scripts/g4_grade_sweep.py`, `g4_ar_align.py`, `g4_name_sweep.py`; all grade
   labels verified aligned; ch3 dropped fn9 restored + renumbered to a clean 1–34;
   ~20 name fixes/unifications incl. Abū Ḥibbān and Abān with translator's notes —
   details in REVIEW-FLAGS §G4 and the errata file).
5. ~~Housekeeping~~ ✅ **done 2026-07-18**: superseded working files and one-shot
   scripts deleted (see the Files section), `g3-findings/` committed as audit trail,
   repo restructured into per-book directories (`fiqh-us-seerah/`), `README.md`
   links updated.
6. Optional/remaining: glossary re-alphabetization; the "still open" pass-A items
   listed in the pipeline note (remaining transcription-quality doubts vs the
   Arabic, coinage sanity-checks).
