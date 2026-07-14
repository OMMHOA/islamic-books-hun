# islamic-books-hun

Goal: translate Islamic books to Hungarian, published as Markdown in this repo.
Current book: **Fiqh-us-Seerah** by Muhammad al-Ghazali (IIPH Revised 2nd Edition,
1420 AH / 1999 CE, English translation, with Ḥadīth commentary by Sheikh
Muhammad Naṣiruddīn Al-Albānī).

## Pipeline

1. **English transcription** from the scanned PDF — ✅ done (2026-07-13, commit `edf317e`)
2. **Verification / proofreading** of the transcription — ⬜ not started (commit is marked "unverified")
3. **Hungarian translation** — 🟡 in progress in `FiqhusSeerah-Muhammad-al-Ghazali-HUN-full.md`:
   front matter + Chapters 1–7 done (ch7 landed 2026-07-15, ~124.5k words total).
   **Next: Chapter 8** (ENG-full line 5816, "The Mothers of the Believers").
   Reused earlier drafts: sections 1.1–1.2, ch2 second half (Khadījah→Waraqah + footnotes),
   ch3 first third (its footnote numbering differs from ENG: HUN ch3 has no ¹⁵ entry by
   design — draft's ¹⁴ covers ENG ¹⁵; body markers match their footnote lists).
   Ch6 footnotes 1–84 and ch7 footnotes 1–121 verified 1:1 body↔list by script.
   **Review flags (honorific artifacts in ENG, Qur'ān 7:115 misprint, Mekka/Makka +
   hadísz-grading terminology) are tracked in `REVIEW-FLAGS.md`** — add new flags there,
   not here.

## Files

| File | What it is |
|---|---|
| `FiqhusSeerah-Muhammad-alGhazali.pdf` | Source scan, 512 PDF pages, no text layer. **PDF page = printed page − 2** |
| `FiqhusSeerah-Muhammad-al-Ghazali-ENG-full.md` | Complete English transcription: Preface → Chapters 1–9 → Epilogue → Glossary, ~176k words |
| `REVIEW-FLAGS.md` | Running list of items for the verification/proofreading passes (transcription artifacts, misprints, terminology to unify) |
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
"Egyt" p. 194, duplicated sentence on p. 83).

## Transcription conventions (keep these when editing/verifying)

- Faithful to the printed text, including its typos and awkward grammar
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

## Next steps

1. Verify/proofread `-ENG-full.md` against the PDF (it is committed but unverified)
2. Continue the Hungarian translation from `-ENG-full.md` — use a stronger model than
   Sonnet for translation quality (Opus/Fable); Sonnet was only used for OCR-style
   transcription
3. Decide fate of the legacy partial `-ENG.md` and the `chapter*-normalized.md`
   working files once superseded
4. Update `README.md` links when new translated chapters land
