# G3 — chunk-aligned HUN ↔ AR verification pass

Method: per-chapter Sonnet subagents compare the HUN translation against the Arabic
original (source of truth), consulting ENG-full to classify divergences (ENG-edition
error vs HUN drift). Agents write findings **incrementally** to `g3-findings/NN-*.md`
(one file per chunk) — nothing is lost to session-limit kills; re-scan this table and
relaunch missing chunks. Agents do NOT edit the translation files; fixes are applied
in the main session after review.

Chunk map (AR pages are printed pages = PDF page + 1):

| Chunk | AR pages | HUN lines | Findings file | Status |
|---|---|---|---|---|
| ch1 | 15–45 | 133–663 | 02-ch1.md | ✅ done w1 (6 findings) |
| ch2 | 46–70 | 664–1120 | 03-ch2.md | ✅ done w2 (7 findings; Ḥilf al-Fuḍūl «بني عبدالمطلب» lead resolved — genuinely printed in AR, ENG/HUN reading likely already correct, flagged NOTE) |
| ch3 | 71–108 | 1121–1840 | 04-ch3.md | ✅ done w2 (fn2–7 marker scrambling + 3 FIX-BOTH + 1 FIX-HUN) |
| ch4 | 109–134 | 1841–2277 | 05-ch4.md | ✅ done w1 (15 entries) |
| ch5 | 135–158 | 2278–2746 | 06-ch5.md | ✅ done w2 (3 FIX-BOTH, 1 FIX-HUN, 2 NOTE) |
| ch6a | 159–188 | 2747–3265 | 07-ch6a.md | ✅ done w2 (3 FIX-BOTH: Majdī ibn ʿAmr, ʿAqīl, Badr 315-vs-313; 2 NOTE) |
| ch6b | 189–217 | 3267–3665 | 08-ch6b.md | ✅ done w3 (4 FIX-BOTH name corruptions: Barāʾ ibn ʿĀzib, ʿUqbah ibn ʿĀmir, ʿAḍal, Banū Muḥārib) |
| ch6c | 218–246 | 3663–4292 | 09-ch6c.md | ✅ done w3 (2 FIX-BOTH: dhirāʿ cubits→feet, Khālid intended-vs-completed hijrah) |
| ch7a | 247–275 | 4293–4736 | 10-ch7a.md | ✅ done w3 (2 FIX-BOTH: al-Qaṣwāʾ→"Qasira", dropped Durayd couplet; 1 NOTE) |
| ch7b | 276–304 | 4739–5169 | 11-ch7b.md | ✅ done w3 (2 FIX-BOTH: Abū Khaythamah, Sulaym; 1 NOTE) |
| ch7c | 305–332 | –5854 (agent locates) | 12-ch7c.md | ✅ done (w4 pp.305–309 + w5 tail pp.310–332): 5 FIX-BOTH (fn121 title unified, ʿUqaylī not Ibn Ḥajar, dropped p.319 fn, fn108 dropped clause, ʿUlayyah not ʿAṭiyah); 3 NOTE |
| ch8 | 333–353 | 5855–6150 | 13-ch8.md | ✅ done w4 (6 FIX-BOTH incl. Qur'ān 4:3 ref + ḥilm couplet + fn9 inversion; 1 AR-AUTHOR-ERROR مريم/Māriyah; both D-items resolved) |
| ch9+Utószó | 354–364 | 6151–6314 | 14-ch9.md | ✅ done w5: 3 FIX-BOTH (fn3 "very weak", al-iḥtirāf mistranslation, "and what a life!" interpolation); 1 AR-AUTHOR-ERROR (Albānī date misprint, HUN already correct); 7 NOTE; both D-items clean |
| front matter | 2–14 | 1–132 | 01-front.md | ✅ done w4 (0 FIX, 4 NOTE, 5 OK; HUN Hadísz-terminológia = pure IIPH addition, no AR counterpart) |

Open D-items to fold into their chunk's prompt:
- ch7: fn121 book-title inconsistency ("Prejudice and Tolerance…" vs fn's
  "Tolerance and intolerance…") — check AR fn for al-Ghazali's actual title (ch7c).
- ch8: HUN ~5850-area Qur'ān 4:3 quote with no ref printed — check AR.
- ch8: ~5936 Qur'ān 33:28–29 wording — ENG print suspected garbled; AR p.346 clean.
- ch9: ~6196 gloss decision; ~6206 "al-rafīq al-aʿlā" rendering vs AR p.354ff.
- Coinage sanity-checks (REVIEW-FLAGS §E) — each agent flags awkward/invented
  HUN coinages in its chunk.

Findings entry format (append-only, one block per finding):

    ## [SEVERITY] AR p.N / HUN ~line
    AR: <Arabic reading (re-render page if decision-critical)>
    ENG: <English edition reading>
    HUN: <Hungarian reading>
    → <what's wrong + recommended fix>

SEVERITY: FIX-HUN (HUN drifted from AR) | FIX-BOTH (ENG-edition error propagated,
fix ENG+HUN) | AR-AUTHOR-ERROR (Arabic itself errs → keep + translator's note) |
NOTE (name/grade/coinage observation, feeds G4) | OK (chunk verified clean — write
one OK line per major section so coverage is provable).
