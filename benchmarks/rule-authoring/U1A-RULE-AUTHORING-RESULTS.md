# U1a Rule Authoring — WCAG 2.2 Reflow Floor — Results

**Status:** COMPLETED.
**Rule:** `A11Y-010 — Reflow at 320 CSS px (WCAG 2.2 SC 1.4.10)`, canonical in `design-excellence/references/rule-catalog/accessibility.md` (Always-on section).
**Provenance (Taint Ruling `04e03df`, C1–C4):** PASS. Every clause is independently supported at matching specificity; no catalog content.
**Critique/review:** PASS. One blind reviewer returned PASS WITH CORRECTIONS; all corrections were applied or recorded (§11), and a confirmation round followed.
**Parent commit:** `04e03df`.

Identity boundary: follows Integration Contract §15. Residue items keep the labels R1–R16 of the earlier audits. No catalog id other than PRN ids appears.

---

## 1. Milestone authorization

The human authorized this milestone in their direct message of 2026-09-27: "U1a Rule Authoring, conditioned on the four provenance gates of Taint Ruling 04e03df."

The accompanying brief delegated seven authoring decisions to this milestone. The two that authorize changes outside the Rule Catalog are the primary record for the critique-protocol edit, quoted verbatim:

> "6. CRITIQUE FLOOR — Determine whether U1a belongs in the Level 1 CRITIQUE floor based on the existing critique protocol. Do not broaden the floor beyond what the protocol supports."
>
> "7. CROSS-REFERENCES — Add only references/pointers that are necessary for the rule to function correctly within the existing architecture. Do not duplicate the rule across files. Prefer one canonical rule with pointers over multiple copies."

Two more lines of the brief confirm that a critique-protocol edit was anticipated: "Check consistency with the critique protocol if modified." (VALIDATION) and "any other existing file modified by this milestone" (FILES TO PROVIDE).

Governance disclosures:
- **STATE.md did not record the authorization when the run began.** It showed the Taint Ruling milestone COMPLETED and "No milestone is authorized". The authorization came from the human's own message, not from pasted content. It was recorded in the `STATE.md` governance fields before any other work, as in the four previous milestones (`loop.md` §7 permits governance-field changes with explicit human authorization).
- **The Authorization field was corrected once during the run.** The first entry summarized the scope as "into the Rule Catalog only", which omitted brief items 6 and 7. The reviewer flagged this as blocking finding B1 (§11). The field now records items 6 and 7. No scope beyond the brief was added.
- **Taint Ruling C4 (disclosed authorization)** is met in §8 and §9 of this report, as the brief requires.

## 2. Scope and explicit exclusions

**In scope:**
- author U1a into the Rule Catalog;
- decide the critique-floor listing (brief item 6);
- add only the pointers needed for the rule to function (brief item 7);
- validate and review the rule;
- write this report, update `STATE.md` operational fields, and make one local commit.

**Excluded, and not done:**
- U1b, U1c, U2 and U3;
- `loop.md`;
- the Integration Contract;
- governance clarification, including the Taint Ruling §12 recommended `loop.md` §4 wording;
- new benchmark scenarios;
- a second provenance route;
- the Principle Pool;
- INTX-003, TYPE-006 and LAYOUT-004;
- `SKILL.md`;
- pushing.

## 3. Final authored rule

As committed in `accessibility.md`:

```
### A11Y-010 — Reflow at 320 CSS px (WCAG 2.2 SC 1.4.10)
- **category:** accessibility · **layer:** P5 (UX/usability — a WCAG 2.2 AA criterion, but not one of the four accessibility floors on the `SKILL.md` §3 enumerated P1 list; kept P5, as `A11Y-005` and `A11Y-008` are)
- **principle:** at a viewport width equivalent to 320 CSS px (1280 CSS px at 400% zoom), content can be presented without loss of information or functionality and without requiring scrolling in two dimensions — for example, no line of text runs past the edge of the viewport so that it has to be scrolled back and forth to be read. Content designed to scroll horizontally (e.g. vertical text) meets the same requirement at a height of 256 CSS px. Adjusting or relocating content is not a loss as long as users can still reach it; information that is hidden, clipped or truncated at that width counts as lost unless the same or equivalent content remains available — elsewhere on the page, through a mechanism that reveals it, or through a link to another view. This does not require a single column, and sections may scroll horizontally as long as each unit in them can be read or used without scrolling in two dimensions — for example a carousel whose panels each fit within 320 CSS px.
- **severity:** major
- **applicability:** always-on for every browser-rendered interface — reflow also serves people who zoom on large screens — checked on whatever the task creates, changes or evaluates (BUILD, REDESIGN, POLISH of the touched area, CRITIQUE, AUDIT; VALIDATE runs only the gates relevant to what was touched, `SKILL.md` §1). Distinct from `INTX-003` (clickable text wrapping), `LAYOUT-005`/`HARDEN-003` (specific overflow causes, used below as fixes) and `A11Y-008` (zoom must not be disabled).
- **exceptions:** parts of the content that require two-dimensional layout for usage or meaning — for example (WCAG Note 2 and its Understanding document) images required for understanding (such as maps and diagrams), video, games, presentations, data tables and grids (not their individual cells), interfaces where a toolbar must stay in view while content is manipulated, and preformatted text or code whose layout carries meaning. Those parts may need scrolling in two dimensions, within their own section or at page level, so long as they can still be scrolled into view and all other content needs scrolling in one direction only. A cell of a data table or grid is not excepted unless its own content requires two-dimensional layout. Excepted content is excepted from this rule only; every other rule still applies to it (keyboard operability: `A11Y-002`).
- **evidence:** public standard: WCAG 2.2 SC 1.4.10 Reflow (Level AA), its W3C Understanding document, techniques C31, C32, C33, C38, G206, G225 and failure F102. DE-native: in `RESPONSIVE-REFLOW-REPLICATION-RESULTS.md` (2026-09-27) every build set a root `overflow-x: clip` (`LAYOUT-004`), which lets a document-width check pass by construction, and the harness of the benchmark it replicated had initially exempted every scroll container — so this rule's validation neither trusts document width alone nor exempts scroll containers wholesale. No DE build has yet been observed failing this criterion: the entry is a checkable floor, not a correction of observed behaviour.
- **freshness:** source: WCAG 2.2 (W3C Recommendation, 12 December 2024), SC 1.4.10 with its Understanding document and techniques — external authority; cite the spec directly, not this file. Text verified against W3C 2026-09-27. status: review_interval_days: 365.
- **validation:** mechanical-countable, subject to the capability gating in `SKILL.md` §1 — rendered, Enhanced mode only. Use a 320 CSS px wide viewport (the usable edge is `documentElement.clientWidth`, 1 px tolerance); measure after entrance animations have settled (or with reduced motion); if the page offers a layout switch (G206), measure with it active. Ignore content hidden by design (visually-hidden text, skip links shown only on focus, closed menus, drawers and dialogs — checked open in (5)) and decoration; judge only elements that carry text, controls or information. With any root `overflow-x: clip`/`hidden` neutralised for measurement: (1) every element that extends past the viewport's left or right edge — outside a horizontal scroll container and not clipped by a non-root ancestor — is part of excepted content that the real page (root clip restored) still lets the user scroll into view; otherwise FAIL; (2) every horizontal scroll container holds excepted content (say why it needs two-dimensional layout) or units a user reads or operates that are each fully visible within the container's visible width (G225), and page-level horizontal scrolling occurs only because of excepted content; otherwise FAIL — never exempt scroll containers wholesale; (3) no text or control is clipped (`scrollWidth > clientWidth` or `scrollHeight > clientHeight` by more than 1 px under `overflow: hidden`/`clip`, with text or a control in the clipped area, or cut by `line-clamp`) or truncated, unless a mechanism reveals the rest (for example carousel controls or a "more" control); (4) all content, navigation and controls present at 1280 CSS px width are still available at 320 CSS px as the same or equivalent content — directly, through a control that reveals it, or through a link to another view (F102); (5) repeat (1)–(3) with each menu, drawer, disclosure and dialog open; (6) for content designed to scroll horizontally, repeat (1)–(3) at a 256 CSS px viewport height with the axes swapped. Cells of data tables and grids are checked like other content: each cell's content must be readable within the container's visible width without scrolling in two dimensions, unless its own content requires two-dimensional layout. Without rendering capability: report `skipped — capability unavailable`, and statically flag fixed `width`/`min-width` values wider than 320 CSS px on non-excepted content for later verification.
- **remediation:** fix the element that overflows rather than hiding the overflow. Reflow with grid or flexbox and media or container queries (WCAG techniques C32, C31; `LAYOUT-003`), fluid tracks and `min-width: 0` (`LAYOUT-005`, `HARDEN-003`), wrapping for long strings (C33), and labels and inputs that fit (C38). Where content no longer fits side by side, any presentation that keeps it available is acceptable — for example stacking, navigation moved behind a "More" or menu button, a control that reveals truncated text, horizontally scrolling panels that each fit 320 CSS px (G225), or an option to switch layout (G206). `INTX-003` governs navigation labels that would wrap; if its fix order drops items, keep them available elsewhere (check 4). A root `overflow-x: clip` (`LAYOUT-004`) removes the page scrollbar but does not make overflowing content available: content it cuts off is lost, so wide excepted content under such a clip needs its own scroll container, the clip removed, or a presentation that fits.
```

**Critique-protocol pointer:** `critique-protocol.md` Level 1, axis 5 now lists "(A11Y-001, A11Y-002, A11Y-003, A11Y-004, A11Y-009, A11Y-010)". This is the only other file changed in `design-excellence/`.

### Changes from the candidate entry (Rule Candidate Evaluation §12), and why

| Candidate wording | Outcome | Reason |
|---|---|---|
| "The page as a whole never requires horizontal scrolling"; excepted content "may scroll … within their own container; nothing else may" | **Removed** | Stricter than WCAG (fails C2). The Understanding allows page-level bidirectional scrollbars "to support the viewing of excepted content", and allows sections that scroll horizontally when each part reads without 2D scrolling |
| "identifiable as scrollable" | **Removed** (brief decision 2) | No independent source at that specificity: WCAG requires no visual scroll affordance, and A11Y-002 covers keyboard operability only |
| "An exempt container must still be reachable and operable by keyboard (`A11Y-002`)" | **Replaced by a pointer** | "Every other rule still applies to it (keyboard operability: `A11Y-002`)" creates no new requirement |
| "is presented" | "**can** be presented", plus layout-switch handling | WCAG wording; G206 |
| element-level loss | "same or equivalent content", relocation not a loss | F102; Understanding |
| closed exception list | "for example (WCAG Note 2)", grids, preformatted text | WCAG Note 2 is a list of examples; Understanding |
| "side regions leave the flow or collapse behind a control" | **Not present** (brief decision 1) | Only "stacking" and "navigation moved behind a 'More' or menu button" appear, as examples of acceptable presentations sourced from W3C (C32; Understanding) |
| validation (1)–(5) | reworked into (1)–(6) | Reviewer findings S3, S4, M1–M6, M11 (§11) |

## 4. Rule ID and canonical location

- **ID: `A11Y-010`.** It is the next unused number in the accessibility namespace (A11Y-001…A11Y-009 exist; `grep` finds no other A11Y-010).
- **Location:** `accessibility.md`, `## Always-on` section, directly after A11Y-009 and before `## Conditional`. The file already orders entries by section rather than by number (A11Y-009 sits before A11Y-005), so no taxonomy change was made.
- **One canonical copy.** The only other mention is the id in `critique-protocol.md` axis 5, which is a pointer. `SKILL.md` §9.5 "one rule, one place" holds.
- **No pointer in `layout-interaction.md`.** It is unnecessary: the axis 5 listing makes the rule reachable in every task with a critique floor, which is the reach Phase 7.1 established for always-on accessibility entries.

## 5. Authority/severity/applicability

The candidate evaluation's classification (P5, major, `accessibility.md`, always-on) was re-checked against the current catalog. **No deviation was made.**

- **Layer P5.**
  - Reflow is not one of `SKILL.md` §3's four enumerated accessibility floors (contrast, focus-visible, keyboard operability, reduced-motion respect).
  - Its WCAG AA status does not raise it to P1: A11Y-005 (WCAG 2.2 AA) and A11Y-008 are P5 under the Phase 4 correction.
  - No ordinary best practice was raised to P1.
- **Severity major.**
  - Critical was considered and not taken. A11Y-008 and A11Y-009 are critical because their failures are total for the affected users. Reflow failures range from a two-dimensional scrolling burden to loss of content, and no DE build has shown one.
  - The reviewer agreed (test 8 PASS).
- **Always-on, not Conditional.**
  - WCAG 1.4.10 applies to all web content. It is not tied to a platform or an interaction, which is what the file's Conditional section is for.
  - The Understanding document also says reflow "helps people who need to resize or zoom in a web interface on larger devices", so it is not a mobile-only rule.
  - The applicability clause states this. VALIDATE still runs only the gates relevant to what was touched (`SKILL.md` §1).
- **Critique floor (brief decision 6): included.**
  - `critique-protocol.md` axis 5 lists every always-on accessibility entry (001, 002, 003, 004, 009).
  - `benchmarks/phase-7/PHASE-7.1-INTEGRITY-AUDIT.md` §2 showed that an always-on entry left off that list is reachable only when `accessibility.md` happens to be loaded. Commit `2da3b06` closed that gap for A11Y-009.
  - Adding A11Y-010 follows the protocol's existing membership rule, so it does not broaden the floor.
  - The axis label "the P1 always-on gates" was already inaccurate before this milestone (A11Y-004 and A11Y-009 are P5). It was not changed (§15, reviewer M10).

## 6. Clause-by-clause provenance table

Sources:
- **W:** WCAG 2.2 normative text (W3C Recommendation, 12 December 2024).
- **U:** W3C Understanding document for SC 1.4.10.
- **T:** W3C technique or failure.
- **DE:** an existing Design Excellence entry or file.
- **M:** DE-native measurement.

All quotes were verified against W3C on 2026-09-27 (§7).

| # | Clause | Support | Specificity |
|---|---|---|---|
| P1 | 320 CSS px (1280 at 400% zoom); "can be presented without loss of information or functionality and without requiring scrolling in two dimensions" | W SC text; W Note 1 | verbatim |
| P2 | "for example, no line of text runs past the edge…" | U Intent: "When lines of text extend beyond the edge of a viewport, users will be forced to scroll back-and-forth to read line by line." | example of the SC, not a narrowing |
| P3 | 256 CSS px height for content designed to scroll horizontally | W SC text; W Note 1, second sentence | verbatim |
| P4 | adjusting or relocating is not a loss; hidden, clipped or truncated counts as lost unless the same or equivalent content remains available elsewhere, via a reveal mechanism, or via a link | U "Neither adjusting or relocating content is considered a loss of information or functionality, so long as users are still able to access the content."; T F102 description ("repositioned in a single column view, or through some interaction … in a disclosure area, a dialog, or via a link to another view") and test step 3 ("the same or equivalent content via disclosure widgets, pop-ups, or links to other views") | matches F102 |
| P5 | no single-column requirement | U "Conforming to this success criterion doesn't mean all sections of content need to stack in a single column within smaller viewports." | verbatim |
| P6 | sections may scroll horizontally if each unit reads or is used without 2D scrolling, e.g. a carousel whose panels fit 320 | U "Nor does it require all sections of content scroll in a single direction, so long as each can be read without two-dimensional scrolling to read the lines of text they present."; U carousel passage; T G225 | matches U and G225 |
| L | layer P5 | DE `SKILL.md` §3 enumerated P1 list; DE A11Y-005, A11Y-008 | DE authority |
| S | severity major | DE authority; DE precedent A11Y-004/005/006/007 major vs A11Y-008/009 critical | DE authority |
| A1 | always-on, every browser-rendered interface, on whatever a task creates, changes or evaluates | W scope (web content); U "It also helps people who need to resize or zoom in a web interface on larger devices"; DE `accessibility.md` always-on definition; DE `SKILL.md` §1 VALIDATE | DE authority over its own modes |
| A2 | distinct from INTX-003, LAYOUT-005/HARDEN-003, A11Y-008 | DE entries' own stated scopes | descriptive |
| E1 | excepted content "for example (WCAG Note 2 and its Understanding document)…", grids, preformatted text or code | W exception; W Note 2 ("Examples of content which requires two-dimensional layout are …"); U "exceptions for data tables and grids"; U preformatted text: "This success criterion does not apply where that meaning would be lost." | matches W and U |
| E2 | excepted parts may scroll in 2D in their own section or at page level, so long as they can be scrolled into view and all other content needs one-direction scrolling | U section "Content that meets exceptions for Reflow": "Reflow does not prohibit web pages from presenting both horizontal and vertical scrollbars for individual sections of content. Nor does it disallow the use of bidirectional scrollbars at the page (viewport) level in order to support the viewing of excepted content, so long as the non-excepted content only needs scrolling in one direction." | "can be scrolled into view" is an **interpretation** of U's framing (scrollbars are permitted "to support the viewing of excepted content"), proposed independently by the reviewer (S3) and adopted. It is flagged here as the one judgement-bearing clause |
| E3 | cells not excepted unless their own content needs 2D | U "individual cells would still need to meet Reflow - unless the cell contains content that also requires two-dimensional layout for usage or meaning." | verbatim in substance |
| E4 | excepted from this rule only; A11Y-002 pointer | WCAG conformance model (every success criterion applies); DE A11Y-002 | pointer; no new requirement |
| EV | evidence field | W, U, T; M `RESPONSIVE-REFLOW-REPLICATION-RESULTS.md` §7 (root `overflow-x: clip` in all three builds; "R2 alone could pass by construction") and §2 ("the main harness initially exempted all scroll regions") | factual |
| F | freshness | DE A11Y-001 freshness precedent; W Recommendation date | convention |
| V0 | mechanical-countable, rendered, Enhanced mode only, capability-gated; clientWidth edge; after animations settle; layout switch active | DE `SKILL.md` §1 "Mechanical gating and capability honesty"; DE INTX-003/TYPE-006 phrasing; M dry-run (usable width 305 of 320 with a classic scrollbar); DE MOTION-007/A11Y-003 (reduced motion); W "can be presented" and T G206 | method, not a norm |
| V1 | ignore content hidden by design (visually-hidden text, skip links, closed menus, drawers and dialogs — checked open in (5)) and decoration; judge elements carrying text, controls or information | W (information and functionality); DE A11Y-009 ("legitimate hidden-by-design UI: closed accordions/disclosures/modals/drawers"); M dry-run (skip links surfaced as false positives in two builds) | method |
| V2 | neutralise root clip for measurement | M (root clip in every build); DE LAYOUT-004 mechanics | method |
| V3 | check (1) | W exception; U page-level clause; E2 | as E2 |
| V4 | check (2) | T G225 ("each card will remain fully visible without the need for additional horizontal scrolling"; test step 5 "fully readable without the need for additional horizontal scrolling"); U page-level clause; M harness defect | matches G225 |
| V5 | check (3), including vertical clipping and line-clamp (1 px tolerance, text or a control in the clipped area), unless a mechanism reveals the rest (carousel controls, a "more" control) | W no loss; U truncation example ("a mechanism is provided on the web page to reveal the truncated content"); U carousel passage | application of W |
| V5a | cells: each cell's content readable within the container's visible width without 2D scrolling, unless its own content needs 2D layout | U "individual cells would still need to meet Reflow - unless the cell contains content that also requires two-dimensional layout for usage or meaning." | application of U |
| V6 | check (4) | T F102 test procedure (1280 baseline, 320 target, "same or equivalent content via disclosure widgets, pop-ups, or links to other views") | matches F102 |
| V7 | check (5), open states | W (content revealed by interaction is content); T F102 (disclosure areas and dialogs hold content) | application of W |
| V8 | check (6), 256 px height | W SC text; W Note 1 | verbatim |
| V9 | static fallback | DE `SKILL.md` §1 `skipped — capability unavailable`; DE A11Y-009 static-fallback precedent; an element wider than 320 CSS px cannot fit a 320 CSS px viewport | method |
| R1 | fix the element that overflows rather than hiding the overflow | W no loss; DE LAYOUT-004 (clip prevents the scrollbar) | application |
| R2 | C32, C31, LAYOUT-003; LAYOUT-005, HARDEN-003; C33; C38 | T sufficient techniques for SC 1.4.10; DE entries | options |
| R3 | acceptable presentations: stacking; navigation moved behind a "More" or menu button; reveal control; panels fitting 320 (G225); layout switch (G206) | T C32 ("reflow columns"); U "the navigation changes first to hide options behind a 'More' dropdown menu. As zooming continues, most navigation options are eventually behind a 'hamburger' menu button."; U truncation example; T G225, G206 | examples, "for example" |
| R4 | INTX-003 governs wrapping nav labels; dropped items stay available | DE INTX-003 fix order; T F102 | consistency note |
| R5 | root clip consequence; own scroll container, clip removed, or a presentation that fits | DE LAYOUT-004 mechanics; U E2 framing | options, not a mandate |
| CP | critique-protocol axis 5 listing | DE `critique-protocol.md` axis 5 membership; DE Phase 7.1 integrity audit §2; commit `2da3b06` | pointer |

**No clause rests on catalog material.**

## 7. WCAG verification

W3C sources fetched on 2026-09-27 by the main agent, and independently by the reviewer:

| Source | Verified content |
|---|---|
| `https://www.w3.org/TR/WCAG22/` | Title and status "W3C Recommendation 12 December 2024". SC 1.4.10 Reflow (Level AA): "Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for: Vertical scrolling content at a width equivalent to 320 CSS pixels; Horizontal scrolling content at a height equivalent to 256 CSS pixels. Except for parts of the content which require two-dimensional layout for usage or meaning." Note 1: "320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom. For web content which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom." Note 2: "Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content." Two notes in total |
| `https://www.w3.org/WAI/WCAG22/Understanding/reflow.html` | Intent paragraphs; "Conforming … doesn't mean all sections of content need to stack in a single column …"; "Nor does it require all sections of content scroll in a single direction, so long as each can be read without two-dimensional scrolling …"; section "Content that meets exceptions for Reflow" with the two scrollbar sentences quoted in §6 E2; the cells sentence; "exceptions for data tables and grids"; preformatted text; "Neither adjusting or relocating content is considered a loss …"; the carousel passage; the "More" and hamburger navigation example; the truncation example; "It also helps people who need to resize or zoom … on larger devices"; sufficient techniques C32, C31, C33, C38, SCR34, G206, G224, G225; failure F102 |
| `https://www.w3.org/WAI/WCAG22/Techniques/failures/F102` | Title, description and test procedure as quoted in §6 P4 and V6 |
| `https://www.w3.org/WAI/WCAG22/Techniques/general/G225` | Title "Section panels that scroll horizontally are designed to fit within a width of 320 CSS pixels on a vertically scrolling page"; description and test step 5 as quoted in §6 V4 |
| G206, C31, C32, C33, C38 | Titles as listed on the Understanding page. The reviewer fetched each page |

Limitation: the fetch tool summarizes pages and quotes passages on request. Every passage relied on was quoted individually, and the main agent and the reviewer checked it independently.

## 8. Four provenance-gate checks (Taint Ruling `04e03df` §11)

| Gate | Result | How it is satisfied |
|---|---|---|
| **C1 Independent support** | PASS | Every clause in §6 traces to W, U or T (WCAG, a source family already admitted by A11Y-001, A11Y-005 and A11Y-006), to an existing DE entry, or to DE-native measurement. Catalog material supports no clause |
| **C2 Specificity match** | PASS | Clauses stricter than WCAG in the candidate were removed (§3 table). Remediation items are examples, not mandates (§10). The one judgement-bearing clause, E2's "can be scrolled into view", is disclosed in §6 and was proposed independently by the reviewer. DE-native evidence supports only validation method (clip neutralisation, container classification, usable edge), never the norm |
| **C3 No catalog content** | PASS | No catalog observation, id, formulation or rejected-principle content (§9) |
| **C4 Disclosed authorization** | PASS | The topic's catalog origin and the rejected-principle overlap are disclosed in §9. The clause trace is in §6. How each gate was met is in this table. The human's authorization named these gates as its condition (§1) |

## 9. Catalog-taint leakage check

**Disclosure (C4).** The reflow topic was surfaced during catalog work:
1. The Reference Architecture Audit found 16 unrouted catalog observations.
2. Three of them are responsive items, R1, R3 and R4:
   - R1: no narrow-viewport adaptation, side navigation staying in flow, clipping;
   - R3: a sidebar leaving the canvas, the header reduced to a menu control, cards stacked below;
   - R4: every module kept and stacked below the main feed.
3. They became unit U1 in the Residue Disposition Audit.
4. Seeking independent authority for U1, the Rule Candidate Evaluation found that DE lacked WCAG 2.2 SC 1.4.10 and split out U1a as the WCAG-grounded part.
5. The Taint Ruling (`04e03df`) found U1a's provenance to be chain A: discovery only.

**Overlap with rejected principles: none.**
- R1, R3 and R4 back no principle, accepted or rejected.
- The five rejected principles concern:
  - PRN-0002: calculation consistency and explanation;
  - PRN-0004: selection scope under filtering;
  - PRN-0005: conditional forms;
  - PRN-0006: comparison marks;
  - PRN-0007: spatial arrangement and linked views.
- None concerns reflow. The reviewer read all five records' abstractions and found no overlap.

**Wording comparison:**

| Catalog-side content | Present in A11Y-010? |
|---|---|
| side navigation stays in flow / side regions leave the flow or collapse (R1, R3; candidate "side regions") | No. No side-region wording at all |
| header reduced to a menu control (R3) | Only as the W3C example "navigation moved behind a 'More' or menu button", one option in an open "for example" list, with W3C wording and support |
| every module kept, stacked in order below the feed (R4) | No. The rule states WCAG's "same or equivalent content" and explicitly "does not require a single column". No ordering or keep-every-module mandate. The corrected P4 also removes an element-level reading the reviewer flagged as close to U1c (S1) |
| accepted PRN-0001 / PRN-0003 narrow-frame clauses (`principle-pool.md`) | No overlap. A11Y-010 contradicts PRN-0001's one-frame bound on no point, adds no frame logic, and borrows no wording (the candidate "way to reach" phrasing was replaced by W3C's "mechanism … reveal" and "link to another view") |

- **No catalog id, product, vendor, path, measurement or source name** appears in the rule or in `critique-protocol.md`.
- **The evidence field cites only a DE benchmark report** (the replication) for DE-native measurements.
- **The rule stands alone.** It is understandable without any catalog or audit history.

## 10. Remediation vs prescription check

- The remediation lists techniques and presentations as options: "any presentation that keeps it available is acceptable — for example …".
- No sidebar collapse, stacking order, single column, containment or implementation pattern is required.
- The one conditional statement ("wide excepted content under such a clip needs its own scroll container, the clip removed, or a presentation that fits") offers three alternatives and describes a CSS consequence. It is not a mandate (reviewer M8, adopted).
- The only normative content lives in the principle and exceptions, which are WCAG's.
- The reviewer rated this test PASS.

## 11. Critique/reviewer result

**Self-critique.** Frozen and hashed before the reviewer ran (SHA-256 `c6d3fdc1…b1af9b`). Verdict PASS, with notes: the corrected WCAG fidelity, the removed "identifiable as scrollable", the testability shown by the dry-run, and the pre-existing axis 5 label inaccuracy. The DE critique protocol's six axes judge design output, not rule text, so the milestone's critique floor was this self-validation (§12) plus the independent review required by `loop.md` §8 and Taint Ruling C4.

**Independent review (`loop.md` §8).** One fresh, blind, read-only general-purpose reviewer.
- **Received:** the authored diff; the Taint Ruling; the claimed clause trace; the raw dry-run outputs; the candidate evaluation; the replication; the residue statements; the Phase 7.1 audit; the DE governance and Rule Catalog; `principle-pool.md`; read access to the five rejected principle records; and W3C web access.
- **Withheld:** the main agent's self-critique verdict.
- **Changes made:** none.
- **Result:** PASS WITH CORRECTIONS.

Per-test results:

| # | Test | Result |
|---|---|---|
| 1 | WCAG fidelity | FAIL, correctable |
| 2 | Provenance and specificity | FAIL, correctable |
| 3 | Catalog-taint leakage | **PASS** |
| 4 | Applicability and exceptions | FAIL, correctable |
| 5 | Remediation vs prescription | **PASS** |
| 6 | Actionability and testability | FAIL, correctable |
| 7 | Consistency | FAIL, procedural (B1) |
| 8 | Severity and layer | **PASS** |

Reconciliation:

| Finding | Reviewer | Reconciliation |
|---|---|---|
| **B1** critique-protocol listing lacks recorded authorization | BLOCKING | **Resolved with evidence the reviewer lacked.** The human's brief items 6 and 7 and "Check consistency with the critique protocol if modified" authorize the decision. The `STATE.md` summary understated this and was corrected (§1). The substance was confirmed sound by the reviewer (Phase 7.1 precedent). Confirmation round: see below |
| **S1** element-level loss; F102 "same or equivalent" | SHOULD-FIX | **Adopted** (P4, check 4); verified against F102 and the Understanding |
| **S2** closed exception list | SHOULD-FIX | **Adopted**: "for example (WCAG Note 2)", "data tables and grids", preformatted text or code; verified |
| **S3** decoration false positive; root-clipped excepted content false negative | SHOULD-FIX | **Adopted**: judge only elements carrying text, controls or information; excepted content must remain scrollable into view on the real page (E2 and check 1; disclosed interpretation, §6) |
| **S4** vertical clipping; open states | SHOULD-FIX | **Adopted** (checks 3 and 5) |
| **M1–M9, M11** | MINOR | **Adopted**: non-root-ancestor clipping to (3); measure after animations settle; G225 "fully visible within the container's visible width"; page-level scrolling only for excepted content; clientWidth edge with 1 px tolerance; "can be presented" and layout switch; 256 px check (6) and cells; "excepted from this rule only" with A11Y-002 pointer; containment alternatives; INTX-003 dropped items; "wider than 320 CSS px" |
| **M10** axis 5 label "P1 always-on gates" lists P5 ids | MINOR | **Not adopted; deferred.** The label predates this milestone. Relabelling changes existing text, which brief item 7 does not cover. A11Y-010's own layer field states P5 and `SKILL.md` §3 governs P1 membership. Recorded in §15 as NOT authorized |
| **M12** trace quote for the navigation example | MINOR | **Adopted in this report**: verbatim W3C text now quoted in §6 R3 |
| **N1** "initially" | NOTE | Adopted |
| **N2** dry-run limits | NOTE | Recorded (§12) |
| **N3** P6 trace citation | NOTE | Adopted: the "does not prohibit … scrollbars" sentence now supports E2 only |
| **N4** text-only gloss; generalize the section condition | NOTE | Adopted: the gloss is an example; sections may scroll "as long as each unit … can be read or used" |
| **N5, N6** Understanding revision cadence; mechanical-countable judgement | NOTE | Accepted as limitations (§12) |
| **N7** C4 disclosure must be in the report | NOTE | Done (§8, §9) |

**Confirmation round (same reviewer, after corrections): PASS.**
- **B1: RESOLVED.** "Brief item 6 … is the separate §2 authorization that Taint Ruling §12.1 requires". The adopted condition: this report quotes items 6 and 7 verbatim as the primary record (§1), and the `STATE.md` correction counts only as a transcription of the human's text.
- **M10 deferral: accepted.** Relabelling is "neither an inclusion decision (item 6) nor a pointer the rule needs to function (item 7)".
- **Corrections:** "applied faithfully, with no new WCAG-fidelity, specificity or taint problem".
- **Four further phrase-level fixes,** all adopted in the final text:

| # | Issue | Fix applied |
|---|---|---|
| 1 | Regression: the ignore list had lost closed menus and drawers, so an off-canvas drawer could fail check (1) | Ignore list now includes "closed menus, drawers and dialogs — checked open in (5)" (A11Y-009 hidden-by-design precedent) |
| 2 | Check (3)'s reveal clause read as modifying "truncated" only, so carousel slides routed to (3) by M1 could fail | Now "clipped … or truncated, unless a mechanism reveals the rest (for example carousel controls or a "more" control)" (Understanding truncation example and carousel passage) |
| 3 | "for example (WCAG Note 2)" misattributed grids and preformatted text | Now "(WCAG Note 2 and its Understanding document)" |
| 4 | Sub-pixel false fires in (3); cells had no operational step | (3) uses "by more than 1 px … with text or a control in the clipped area". Cells: "each cell's content must be readable within the container's visible width without scrolling in two dimensions, unless its own content requires two-dimensional layout" (Understanding cells sentence) |

The confirmation reviewer could not verify M12 and N3, since they are trace corrections in this report. They appear in §6 rows R3 and E2/P6.

## 12. Validation result

**Structural checks (all pass):**
- `A11Y-010` appears exactly once as a heading, and once as a pointer in `critique-protocol.md`.
- Every cross-referenced id exists: INTX-003, LAYOUT-003, LAYOUT-004, LAYOUT-005 (`layout-interaction.md`); HARDEN-003 (`performance-hardening.md`); A11Y-002, A11Y-005, A11Y-008 (`accessibility.md`).
- The field order matches neighbouring always-on entries: category and layer, principle, severity, applicability, exceptions, evidence, freshness, validation, remediation.
- `git diff --check` is clean, and line endings are unchanged: the diff touches only the added block and the one axis 5 line.

**Consistency checks:**
- P5 matches the Phase 4 accessibility discipline.
- No contradiction with LAYOUT-004. Root clip remains correct for `position: sticky`; A11Y-010 only states that clip does not satisfy reflow.
- INTX-003 and TYPE-006 are unchanged; their undefined "required floor widths" are a follow-up (§15).
- One rule, one place holds.
- The critique protocol is consistent with its own membership rule for axis 5.

**Validation dry-run** (a test of the check procedure, not a benchmark):
- **Setup.** The rule's checks were run with a browser tool on the three existing DE builds from the Responsive Reflow Replication (disposable copies in an earlier session's scratchpad, served locally). The viewport was 320×800 CSS px, giving a usable width of 305 because of a classic vertical scrollbar. Controls were compared at a 1440 px viewport.
- **Findings:**
  - All three builds set a root `overflow-x: clip`. With it neutralised, no page overflow appeared (scrollWidth 305 = clientWidth 305).
  - B1's scrolling navigation strip (305 of 442 px) holds nav links that each fit, so it passes. The candidate wording ("classify every scroll container as exempt or FAIL") would have failed it wrongly.
  - B3's scroll container (271 of 511 px) holds a `<table>`, which is excepted, so it passes.
  - Skip links positioned off-screen until focused surfaced as off-edge elements in B1 and B2. This led to the hidden-by-design exclusion.
  - No clipped text was found, and every control present at 1440 px was available at 320 px (menus opened).
  - The only console errors were favicon 404s.
- **Limitations (reviewer N2):**
  - The dry-run exercised the pre-correction checks (1)–(4). Corrected checks (5) and (6) and the corrected check (1) (root clip restored) were not re-run.
  - It compared against 1440 px, not the rule's 1280 px, and compared controls only, not all content.
  - None of the three builds contains decoration bleed, carousels, code blocks, non-table grids, dialogs, vertical clipping, root-clipped excepted content or horizontally scrolling (vertical-text) content, so those paths are untested.
  - "mechanical-countable" makes a FAIL gate SHIP (`SKILL.md` §1), although checks (1), (2) and (4) include judgement (classifying excepted content). This follows the A11Y-004 and INTX-003 precedent.
  - The Understanding document is non-normative and revised more often than the Recommendation. The 365-day review interval covers this.
- **Housekeeping:**
  - The browser tool wrote a `.playwright-mcp/` folder (page snapshots and console logs from this run) into the repository root. It was deleted and is not committed.
  - The local HTTP server was stopped.
  - No build, benchmark scenario or artifact was created.

## 13. Files changed

**Changed:**
- `design-excellence/references/rule-catalog/accessibility.md`: A11Y-010 added (11 lines).
- `design-excellence/references/critique-protocol.md`: Level 1 axis 5 list gains `A11Y-010` (one line).
- `STATE.md`:
  - governance fields set from the human's authorization (Authorization corrected once, §1);
  - operational fields (Iteration, Status, Blockers, Pending human gate, Next action).
- `benchmarks/rule-authoring/U1A-RULE-AUTHORING-RESULTS.md` (added; this report).

**Not changed:**
- `loop.md`;
- the Integration Contract and every catalog file;
- `SKILL.md`;
- `layout-interaction.md`, including INTX-003, LAYOUT-003, LAYOUT-004 and LAYOUT-005;
- `typography.md` (TYPE-006);
- `performance-hardening.md`;
- `content-copy.md`, `color.md`, `motion.md`;
- `principle-pool.md`, `visual-references.md` and every other reference file;
- all other benchmarks and reports;
- `rules.md`; `scratchpad/`.

Disposable material (draft rule, claimed trace, dry-run script, self-critique) stays outside the repository and is not committed.

## 14. Commit SHA

This report is part of the milestone's single local commit, and a file cannot contain its own commit hash. The SHA is reported in the milestone's final response and is visible with `git log -1`. Parent: `04e03df`. Nothing was pushed.

## 15. Remaining follow-up work — NOT authorized

Each item needs separate human authorization. None is started or implied by this milestone.
1. **Axis 5 label.** Correct `critique-protocol.md` axis 5 "the P1 always-on gates", which now lists three P5 entries (A11Y-004, A11Y-009, A11Y-010). This is a pre-existing inaccuracy (reviewer M10).
2. **Floor widths.** Define INTX-003's and TYPE-006's undefined "required floor widths", for example as 320 CSS px per A11Y-010. This changes their meaning.
3. **LAYOUT-004 cross-reference.** Optionally add a pointer from LAYOUT-004 to A11Y-010 ("clip prevents the scrollbar; it does not fix overflow"). It is not needed for A11Y-010 to function.
4. **Untested validation paths.** Exercise the checks the dry-run could not (§12 limitations) on existing or future DE artifacts. This would need an authorized milestone and must not become a benchmark hunt (`loop.md` §15).
5. **WCAG 2.2 SC 1.4.1 Use of Color** (Level A). It is absent from DE, and a candidate evaluation was recorded as possible by the Rule Candidate Evaluation and the Taint Ruling.
6. **`loop.md` §4 clarification** recommended by the Taint Ruling §12. This is a `loop.md` §7 change.
