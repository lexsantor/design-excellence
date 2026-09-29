# External Design Excellence Revalidation

- **Date:** 2026-09-28
- **Status:** COMPLETED (closed through External Revalidation Evidence Reconciliation & Closure)
- **Previous milestone:** D-1 §4 Behavioral Root-Cause Investigation + Targeted Runtime Correction (`cd047ba`)
- **HEAD during the run and the closure:** `cd047ba`.
- **Workspace (disposable, repository-local, uncommitted):** `<revalidation-workspace>/`. Its `README.md` indexes the evidence.
- **Repository files changed:** this report and `STATE.md`. No skill source, installed copy, `loop.md` or other governed file changed.

Throughout, **Observed** marks what a file or transcript shows, and **Interpretation** marks a reading of it.

## 1. Authorization

The exact human authorization text:

> Autorizo el milestone External Design Excellence Revalidation.

- **Observed:** this text appears in the human's closure briefs (session `a2fe01ea…`, 16:54:15Z, and session `2ec58777…`). The build prompt (session `4d764813…`, 16:10:10Z) says "Run the authorized milestone: External Design Excellence Revalidation." It also told the builder not to modify the repository's governance. So `STATE.md` was not updated when the build started. This report and the `STATE.md` update record the milestone after the fact.
- **Interpretation:** this departs from the `loop.md` §1 step 2 order (record, then execute). The departure is procedural. The build brief itself asked for it, and no scope boundary was crossed.

## 2. Objective and hypothesis

- **Objective (build brief):** "validate the current Design Excellence system organically on a fresh, realistic client project after the recent D-1 §4 correction", treated "as a normal client delivery".
- **Hypothesis (derived from the brief):** on a fresh client-project greenfield page BUILD, the installed skill (post-`cd047ba`) routes, defines, directs, builds, validates and critiques according to its current specification, and any deviation is observable from the preserved evidence.

## 3. Project tested

- **Project:** a small health clinic (identity withheld in this public copy). The client objective was a Spanish landing page whose primary conversion is booking or requesting a first consultation.
- **Project state:** genuinely empty. **Observed:** `context.md` records `project_state: greenfield` and "genuinely-empty project; nothing to preserve"; the workspace was new.
- **Builder:** an interactive session, invoked with `/design-excellence` (installed copy at `C:\Users\<user>\.claude\skills\design-excellence\`), model `claude-opus-5-5`. Build window: 16:10:10Z to 16:28:22Z.

## 4. Scope and routing

- **Observed (`context.md`, builder's final message):** page-scope BUILD on a genuinely-empty project. The stages evidenced are DEFINE (the `context.md` write, 16:14:36Z), DIRECT (Rejected Directions record), DESIGN (Visual System), BUILD (the page written from 16:14:42Z), VALIDATE (Playwright checks from 16:16Z), CRITIQUE Level 1 and Level 2, REFINE and SHIP.
- **Observed:** INSPECT and AUDIT did not run, which matches the specification for genuinely-empty BUILD. The rule, anti-slop, style, reference and critique files were loaded before DEFINE (narration at 16:11:30Z to 16:11:51Z).

## 5. Register / Genre / Dials

- **Observed (`context.md` front matter):** register `brand-led`, genre `atmospheric-expressive`, dials variance 5, motion_intensity 4, visual_density 3. They were recorded at 16:14:36Z, before any page file.
- **Observed (transcript):** no visible assistant text in the build session contains the `SKILL.md` §2 classification line ("Reading this as: …") or a §4 Register/Genre/Dials declaration line. The only occurrences of "Reading this as" are in the loaded skill text itself (transcript lines 6, 9, 17). The visible text before the first `context.md` write is four progress notes (16:11:30Z, 16:11:42Z, 16:11:51Z, 16:14:42Z). Thinking content is mostly not stored (15 of 61 thinking blocks non-empty), so it could not be checked in full.
- **Observed:** the builder's final message says "Both lines were stated visibly before any file was written." The transcript does not support that sentence.
- **Interpretation:** in this run, the §2 and §4 one-line disclosures (D-1) were not observed as visible text, even though the installed `SKILL.md` §1 DEFINE row carries the `cd047ba` anchor. This is one run (n=1) in an interactive, non-headless session. This closure did not investigate the cause; see §15 and §16.

## 6. Concept / name hypothesis

- **Observed (`context.md`):** "Concept detection: HYPOTHESIS." The business name has an ordinary second meaning; the brief never states it as the naming rationale, so it may inform mood and rhythm only, with no literal icon or motif (paraphrased; identifying detail withheld).
- **Observed:** the committed direction records the hypothesis-derived pace as "Hypothesis-derived exploration (not concept evidence)". The Level 2 brief passed HYPOTHESIS as a recorded input. The reviewer did not run the structural test, stating "DEFINE recorded HYPOTHESIS".
- **Interpretation:** handling is consistent with the §1 three-state model. HYPOTHESIS did not activate the structural test or LAYOUT-009.

## 7. Direction exploration and selected direction

- **Observed (`context.md` Rejected Directions):** two candidates were recorded.
  - **Rejected, candidate B "Long document index":** long editorial single column with numbered index navigation (REF-003). Rejected with reference to `style-catalog.md` STYLE-EDITORIAL-01 `best_for` (long-form), its accessibility-risk note, and proximity to SLOP-011 cluster 3.
  - **Committed, direction A (named after the location; name withheld):** the distinguishing dimensions are composition (one-frame hero unit, PRN-0001 adapted), color (shutter green plus ochre, derived from the location), typography (low-contrast warm serif, Young Serif with Hanken Grotesk) and materiality (chamfered corners). The contact block uses REF-009. REF-002 was considered and judged unnecessary, with a reason.
- **Observed (Level 2 verbatim):** all four committed dimensions were judged carried. The one-frame claim holds only on tall wide frames (900×700 exception). The chamfer grammar was inconsistent at v4.

## 8. Implementation summary

- **Observed:** plain HTML plus CSS, no JavaScript, no build step and no dependencies other than Google Fonts (`index.html`, `styles.css`). Sections: hero (headline, book and call actions, a four-fact band, a typographic address "plaque" in place of photography), tiered audiences, first-visit steps, team with monogram portrait slots, and a rule-segmented contact block.
- **Observed:** the primary action links to the clinic's online booking page, with phone, WhatsApp, email and Google Maps as fallbacks. The builder did not build a request form, because there was no backend (`context.md` Constraints).

## 9. Content truth / anti-fabrication

- **Observed (`context.md` Fact sources):** every published fact is mapped to a source: the client brief, the clinic's own site (fetched 2026-09-28), public third-party listings. The spine mention is marked single-source.
- **Observed ("Deliberately NOT published"):** degrees and institutions, years in practice, languages per practitioner, techniques, first-visit price and duration, and opening hours were withheld. The stated reason is that they appear only in third-party listings, some with demonstrable errors.
- **Observed (Level 2 verbatim):** "Correctly withheld: price, duration, hours, credentials. No medical claims or outcomes." The reviewer raised "pendiente de confirmar por la clínica" as an internal note in public copy (major). It flagged "tu columna", the floor-and-door line and "Cuéntanos tu situación al reservar" as untraceable or assumed (minor).
- **Observed (resolution):** the placeholders were rewritten in first person or moved to HTML comments. `grep "pendiente" index.html` returns nothing in the final file. The copy was softened (a shorter floor-and-door line, "llámanos antes de reservar"). The builder disputed "tu columna" and kept it as traceable to a third-party listing, single-source.
- **Observed:** the three external conversion URLs returned HTTP 200 (16:21:35Z).

## 10. Critique chronology

| Step | Time (UTC) | Build assessed | Record |
|---|---|---|---|
| Level 1 self-critique, recorded before any Level 2 dispatch | 16:22:12Z | v4 | `context.md` "Level 1 critique (recorded before any Level 2 dispatch)" |
| Level 2 brief assembled; rubric check printed `RUBRIC BYTE-IDENTICAL` | 16:23:06Z | v4 | `_evidence/L2-BRIEF.md`, `rubric-extracted.txt` |
| Level 2 dispatched (fresh `lexia-design:visual-critic`) | 16:23:16Z | v4 | transcript |
| Level 2 hand-back | 16:25:13Z | v4 | `_evidence/L2-REVIEWER-REPORT-VERBATIM.md` |
| Synthesis and corrections (REFINE) | 16:25:41Z onward | v4 → v5 | `context.md` "Synthesis" |
| Post-Level 2 verification (rendered re-checks plus a self-assessment formed after Level 2, not independent of it) | 16:26:43Z | v5 | `context.md` "Level 1, formed after Level 2 (not independent of it)" |

- **Pre-dispatch Level 1 (observed):** Genericness 3, Hierarchy 4, Distinctiveness `not assessable: first Fingerprint History entry`, Craft 4, Accessibility 4, Technical 4. No axis was below 3, so the Level 1 escalation was not triggered.
- The pre-dispatch Level 1 was not revised. The reconciliation step appended a clarifying note under generation 1 and rewrote no existing line.

## 11. Level 2 independent review

- **Trigger (observed, `L2-BRIEF.md`):** "production-facing work (the public website of [the client], delivered as a client project)".
- **Transport (observed):** the rubric block in the brief is byte-identical to the extraction from the installed `critique-protocol.md`. Both hash to SHA-256 `49a5d02804c339bb5d8d473cc7857c02250712fbf62592a87fcb52e0174083c4`. The brief carries no Level 1 content.
- **Independence (observed, reviewer's own statement):** "I did not open the live render or anything under `.design/`."
- **Scores (observed):** Genericness 4, Hierarchy 3, Distinctiveness not assessable (first entry), Craft 4, Accessibility 4, Technical 5.
- **Record forms:** `L2-REVIEWER-REPORT-VERBATIM.md` is authoritative. The builder's condensed transcription, `L2-REVIEWER-REPORT.md`, matches it in scores, findings and fixes but not in wording. The verbatim file records its own extraction source and SHA-256 (`7e83a865…`); this closure did not recompute that hash.

## 12. Concrete Level 2 finding: mobile hierarchy / address slab

- **Observed (verbatim):** "Major, v4-768 and v4-390: below 900px the plaque's street name uses `clamp(2.5rem, 20cqi, 6.5rem)` (css:129) and renders at about 90px, against an H1 of about 40px. Primary and secondary are inverted: the address outranks the value proposition, and the plaque pushes the fact band off screen."
- **Observed:** the pre-dispatch Level 1 scored Hierarchy 4 and did not record this. The synthesis states "L1 missed the narrow-frame plaque/H1 inversion; L2 is right".
- **Observed (correction):** the plaque type was capped at the H1 size, `min(20cqi, var(--step-hero))` (`context.md` Responsive Notes).
- **Observed (v5 measurement, 16:26:43Z):** `plaquePx` equals `h1px` at every tested width (37.6 at 320/390/560, 41.472 at 768, 48.546 at 899, 48.6 at 900, 55.296 at 1024, 59.2 at 1280, 66.6 at 1440). The plaque text fits at every width.
- **Interpretation:** this is the run's clearest instance of Level 2 catching a defect that Level 1 and the builder's own VALIDATE missed.

## 13. Resulting corrections

Adopted from Level 2 (observed, `context.md` synthesis and final code):

1. Plaque type capped at the H1 size.
2. Placeholders rewritten in first person or moved to HTML comments.
3. The fact band's "Dónde" replaced by team names (address repetition).
4. Closing band removed (it duplicated the contact actions).
5. Chamfers unified to two variants.
6. Mobile nav row added below 900px, replacing `display:none`.
7. Copy softened (a shorter floor-and-door line, "llámanos antes de reservar").

Not adopted: self-hosting fonts (deferred), and the emptiness at the top of the plaque (kept as a deliberate color mass). Disputed: "tu columna" (kept, single-source).

## 14. Final v5 validation, accessibility and browser evidence

All observed in the build transcript and `_evidence/`:

- **Responsive (v5, 16:26:43Z):** at 320, 390, 560, 768, 899, 900, 1024, 1280 and 1440, the `over`, `clipped` and `wrapped` lists are empty. The mobile nav scrolls only at 320 and 390, and each link fits its container.
- **Focus not obscured (v5):** 21 focus stops at 390 and at 320, with none bad.
- **Earlier keyboard walk (v4, 16:19:39Z to 16:21:09Z):** 3px focus outline on every stop. At 390 one reverse-tab stop (footer email) came back not fully visible. The builder investigated it before Level 2 (16:20:45Z) and verified it on v5 by the 21-stop check above.
- **Contrast (16:19:27Z):** every token pair used passes. The lowest is ochre on shutter at 5.33:1 against a 4.5 requirement. The reviewer computed the same pairs independently (5.3 lowest).
- **Reduced motion (16:21:22Z):** `anims: 0`, H1 opacity 1, `scroll-behavior: auto`.
- **Console:** one error, `favicon.ico` 404 from the local server (`_evidence/playwright-mcp/console-*.log`). There are no page script errors (the page has no JavaScript).
- **Screenshots:** `v5-{320,390,768,1024,1440}-{full,viewport}.png` are the final visual evidence. The reconciliation step confirmed they show the final code (no closing band, H1 leading at 390, no placeholder copy). v1 to v4 remain as history.
- **Engine:** Chromium via Playwright only.

## 15. Limitations

Established limitations, unchanged:

- Self-hosting fonts deferred (the Google Fonts stylesheet stays render-blocking).
- Unused `.btn-on-dark` CSS remains (`styles.css:78`, `:82`; no use in `index.html`).
- Unconfirmed clinic facts were deliberately withheld (credentials, hours, price, duration, languages per practitioner, photos).
- Browser testing was Chromium only.

Additional observations recorded by this closure. These are not new limitations of the delivered page; they qualify the evidence:

- **n=1**, one model.
- **Not unprimed:** the build ran in the interactive control session, and its prompt named the milestone and discussed Level 1/Level 2. Unlike the earlier headless organic runs, the builder knew it was a validation.
- **D-1 disclosure not observed** (§5), and the builder's final message misstated it.
- **Stored thinking** is only partly available, so internal-only classification could not be fully examined.
- **Reviewer isolation** from `.design/` rests on instruction and the reviewer's own statement.
- **Late recording:** the milestone was recorded in `STATE.md` after execution (§1).

## 16. Open question

- **OQ-D1-R: D-1 recurrence after `cd047ba`.** One organic run after the fix showed §2 and §4 visible (`20260928-d1-section4-behavioural-correction.md`). This run shows neither. Possible explanations include session type (interactive and primed rather than headless), long pre-DEFINE loading, or incomplete adherence. None of these was tested. Whether to investigate is a human decision. This closure changes no skill behavior and authorizes nothing.

## 17. Evidence locations

- **Workspace:** `<revalidation-workspace>/`
  - `<site>/index.html`, `styles.css`, `.design/context.md`
  - `README.md` (evidence index and critique chronology)
  - `_evidence/L2-BRIEF.md`, `rubric-extracted.txt`, `L2-REVIEWER-REPORT-VERBATIM.md`, `L2-REVIEWER-REPORT.md`
  - `_evidence/v1…v5-*.png` (v5 final), `_evidence/playwright-mcp/`
- **Transcripts** (outside the repository, not copied): `C:\Users\<user>\.claude\projects\C--Users-<user>-Desktop-design-excellence\`
  - `<session>.jsonl`: build and Level 2 dispatch.
  - `<session>.jsonl`: reconciliation, stopped by a usage limit.
  - `<session>.jsonl`: closure.
- **Also present, not part of this milestone's evidence:** `<revalidation-workspace>.zip` (untracked, pre-existing, not modified).

## 18. Reconciliation and closure actions (workspace only, uncommitted)

- `_evidence/L2-REVIEWER-REPORT-VERBATIM.md` added: the reviewer's final message, extracted unedited.
- `_evidence/L2-REVIEWER-REPORT.md` retitled as a condensed transcription, with a pointer to the verbatim file. Body unchanged.
- `.design/context.md` gained an appended note recording the shipped post-Level 2 structure and the chronology. No existing line was rewritten.
- `README.md` was corrected.
  - The condensed report is no longer called verbatim, and both report files are distinguished.
  - The critique chronology is spelled out: pre-dispatch Level 1, then Level 2, then corrections, then post-Level 2 verification on v5.
  - The claim that the classification, §4, DIRECT and Level 1 lines exist as visible transcript output was corrected to match the transcript.
- `index.html` and `styles.css` were not modified during reconciliation or closure (SHA-256 before and after this closure step are identical).

## 19. Design Excellence source behavior

**No Design Excellence source behavior changed.** This milestone changed neither `design-excellence/` nor the installed copy (`C:\Users\<user>\.claude\skills\design-excellence\`). Both hash identically before and after the closure step. `loop.md`, the Integration Contract, architecture, T4, references and the Principle Pool are also untouched. A scan of the build session's tool calls found no T4 source access.

## 20. Final disposition

**COMPLETED.** The hypothesis is accepted with one recorded deviation.

These behaved as specified on a client-project greenfield page BUILD:
- routing;
- classification recorded before styling;
- three-state concept handling (HYPOTHESIS);
- DIRECT with a catalog-traceable rejection and carried dimensions;
- first-entry fingerprint handling;
- Level 1 before Level 2;
- byte-identical rubric transport with no Level 1 leakage;
- reviewer independence;
- a labelled synthesis that recorded disagreement;
- anti-fabrication and honest no-backend conversion;
- the always-on accessibility floor on the rendered v5.

Level 2 found a major mobile hierarchy inversion that Level 1 missed, and it was corrected and verified on v5.

**Deviation:** the §2 and §4 one-line disclosures (D-1) were not observed as visible text (§5, OQ-D1-R).

**Next action:** await human direction. No milestone is authorized.
