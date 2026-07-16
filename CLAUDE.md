# islamic-books-hun

Goal: translate Islamic books to Hungarian, published as Markdown in this repo.
Current book: **Fiqh-us-Seerah** by Muhammad al-Ghazali (IIPH Revised 2nd Edition,
1420 AH / 1999 CE, English translation, with Ḥadīth commentary by Sheikh
Muhammad Naṣiruddīn Al-Albānī).

## Pipeline

1. **English transcription** from the scanned PDF — ✅ done (2026-07-13, commit `edf317e`)
2. **Verification / proofreading** of the transcription — ⬜ not started (commit is marked "unverified")
3. **Hungarian translation** — ✅ **full draft complete** in
   `FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md` (2026-07-15): front matter +
   Chapters 1–9 + Epilogue ("# Utószó") + back matter ("# A könyvben használt jelek",
   "# Átírási táblázat", "# Szójegyzék"). The Glossary has all 71 entries (headwords
   kept in transliterated form as printed; only "Lāt and 'Uzza" → "Lāt és 'Uzza"
   changed). Remaining work is now **review/proofreading only** (pass B), tracked in
   `REVIEW-FLAGS.md`, plus updating `README.md` links.
   Reused earlier drafts: sections 1.1–1.2, ch2 second half (Khadījah→Waraqah + footnotes),
   ch3 first third (its footnote numbering differs from ENG: HUN ch3 has no ¹⁵ entry by
   design — draft's ¹⁴ covers ENG ¹⁵; body markers match their footnote lists).
   Ch6 footnotes 1–84, ch7 footnotes 1–121, ch8 footnotes 1–24 and ch9 footnotes 1–18
   verified 1:1 body↔list by script. Note: ENG-full keeps ch9's footnotes at the very
   end of the book (after the Glossary); HUN places them right after ch9 per convention.
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
   doubts), coinage sanity-checks, optional full glossary re-alphabetization, and
   `README.md` links.

## Files

| File | What it is |
|---|---|
| `FiqhusSeerah-Muhammad-alGhazali.pdf` | Source scan, 512 PDF pages, no text layer. **PDF page = printed page − 2** |
| `FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md` | Complete English transcription: Preface → Chapters 1–9 → Epilogue → Glossary, ~176k words |
| `REVIEW-FLAGS.md` | Running list of items for the verification/proofreading passes (transcription artifacts, misprints, terminology to unify) |
| `ENGLISH-EDITION-ERRATA.md` | Consolidated list of the English edition's errors verified against the Arabic original (wrong Qur'ān refs, inserted honorifics, mistranslations, corrupted names) — all corrected in both ENG-full and HUN per the fidelity policy |
| `FiqhusSeerah-Muhammad-al-Ghazali.md` | Hungarian translation, main file (Chapter 1 sections 1.1–1.2 so far) |
| `FiqhusSeerah-Muhammad-al-Ghazali-HUN-Chapter3-AkuldetesKuzdelme.md` | Hungarian Chapter 3 draft |
| `FiqhusSeerah-Muhammad-al-Ghazali-HUN-Khadijah.md` | Hungarian Khadījah section draft (from Chapter 2) |
| `chapter2-normalized.md`, `chapter3-normalized.md`, `chapter3-summary-hu.md` | Working files for the HUN drafts |
| `FiqhusSeerah-Muhammad-al-Ghazali-ENG.md` | **Legacy** partial English transcription (sections 1.1–1.2 + parts of ch. 2, non-sequential). Superseded by `-ENG-full.md`; kept for reference |
| `.transcription-fragments/` | Untracked backup of the per-chapter transcription fragments; deletable anytime |

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
  faithful to the Arabic. (This supersedes the original "faithful to the printed English
  text, typos included" rule.)
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
(see the pipeline note above). Remaining:

1. **Pass A** — verify/proofread `-ENG-full.md` against the PDF (committed but unverified):
   honorific artifacts, Qur'ān 7:115 & other misprints, garbled sentences (REVIEW-FLAGS
   §1/§3/§4 per chapter).
2. **Pass B leftovers** — coinage sanity-checks and the optional full Hungarian
   re-alphabetization of the glossary (REVIEW-FLAGS §2 open sub-question).
3. Update `README.md` links (currently stale) now that all chapters have landed.
4. Decide fate of the legacy partial `-ENG.md` and the `chapter*-normalized.md` /
   `-HUN-Chapter3…` / `-HUN-Khadijah.md` working files (superseded by the `-full` files).
