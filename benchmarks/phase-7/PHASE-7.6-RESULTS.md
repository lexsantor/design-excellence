# Phase 7.6 — Targeted Integration Benchmark

## 1. Test Setup

**Task:** design and build a fictional B2B landing page for "ORBIT" — a premium platform for professional-services teams coordinating client work, approvals, documents, and project milestones. Positioning: calm, precise, operational, trustworthy.

**Environment:** genuinely-empty project (no existing repo, no `.design/context.md`, no prior design decisions). `/design-excellence` was **not invoked** per the task instruction; this benchmark instead walks the skill's own documented pipeline (`SKILL.md` §1–§9) directly and manually, exactly as the skill would, so the reasoning is inspectable rather than hidden inside a skill invocation.

**Implementation conditions:** no component library, icon library, motion library, visual style, or layout system was named by the brief. Reicon, Kinetics, and SmoothUI are present in the repository as T4 references (`design-excellence/references/{reicon,kinetics,smoothui}.md`) but were not opened until their own stated activation conditions were independently satisfied by upstream design decisions — see §3–§5.

**What this document is:** a full trace of the classification → design → implementation-source-consultation sequence, written as the design record would appear in `.design/context.md` if this were a real run, plus the evaluation the task requires. No files were created for an actual ORBIT project; per the task's Output Restriction, only this document exists.

## 2. Design Decisions Before Implementation Sources

Classification (`SKILL.md` §2), stated before any styling:

> Reading this as: page-scope BUILD on a genuinely-empty project.

Register / Genre / Dials (`SKILL.md` §4), stated before DIRECT:

> Reading this as: hybrid-led modern-minimal work, variance=Medium(4), motion=Low(2), density=Medium(5).

Reasoning:
- **Register — hybrid.** The audience is evaluating a workflow tool (product-led pull), but the brief explicitly asks for "premium," "trustworthy" positioning on a page whose entire job is persuasion before signup (brand-led pull). Neither pull dominates cleanly; hybrid sets variance's ceiling at Medium rather than Low (pure product-led) or High (pure brand-led).
- **Genre — modern-minimal.** "Calm, precise, operational" is a direct, brief-stated register/emotional signal, not a category stereotype applied by default (the Phase 6 correction in `SKILL.md` §4 specifically requires this distinction) — editorial reads too publication-like for a workflow tool, atmospheric-expressive contradicts "precise/operational," playful directly contradicts "trustworthy."
- **MOTION_INTENSITY — Low.** "Calm" is a direct textual signal against decorative motion; Low band suppresses the delight tier per `MOTION-002`.
- **VISUAL_DENSITY — Medium.** The brief requires explaining a real workflow (four coordination surfaces: client work, approvals, documents, milestones) — too sparse a page under-communicates the product; a dashboard-dense treatment would misrepresent a marketing page.

**Concept detection (`SKILL.md` §1):** the name "ORBIT" carries an obvious orbital/coordination metaphor, but the brief's own text never asks for that idea to be embodied and contains no recurring reference object beyond the product name itself. Per the DEFINE bright-line test ("point at the sentence — if you can't, it isn't evidenced"), this is **HYPOTHESIS**, not DETECTED/EVIDENCED. Logged as: *hypothesis — "orbit" name plausibly maps to a coordination/hub metaphor; not brief-stated.* Consequence: `layout-interaction.md` LAYOUT-009's mandatory structural-translation requirement does **not** activate — nothing downstream is obligated to express "orbit" visually. This distinction is load-bearing for §6 below (it closes off a name-driven route into unjustified iconography/motion that the task's own accidental-chain list doesn't enumerate but is structurally identical to SLOP-011's "unconsidered default" pattern).

**DIRECT — two candidates stated before committing (`SKILL.md` §1):**
- *Candidate A — "Structured editorial-calm":* generous whitespace, single accent color, workflow presented as a plain horizontal numbered sequence, no literal orbit imagery.
- *Candidate B — "Orbit-informed hub-and-spoke":* a central "project" node with client work / approvals / documents / milestones arranged radially around it, visually literalizing the HYPOTHESIS.

**Committed: Candidate A.** Reasoning logged as a rejected-direction entry: Candidate B is distinct from A on composition, imagery, and interaction (clears the 2-of-6 distinctness bar), but a literal orbit diagram risks becoming a decorative centerpiece competing with the actual workflow explanation, and — because the concept is HYPOTHESIS, not brief-evidenced — building structure around it would be design-by-coincidence-of-name rather than design-by-brief. Rejected for register fit, not for cost or difficulty.

**SHAPE (structure, before any implementation source is opened):**
1. Nav — logo, minimal links, one CTA button.
2. Hero — headline, subhead, primary CTA, secondary CTA, product mockup.
3. Problem framing — coordination overhead across concurrent client engagements (brief's own stated pain point).
4. How it works — four-step workflow sequence: client work → approvals → documents → milestones.
5. Why it reduces overhead — three benefit points (visibility, accountability, fewer status-chase messages).
6. Trust strip — qualitative positioning line, deliberately **no fabricated client count, logos, or percentage metric** (`SKILL.md` §9 Principle 8 / `content-copy.md` CONTENT-003 — this is a fictional product; inventing "500+ teams" or a fabricated logo wall would be exactly the anti-fabrication failure P1 exists to block).
7. Final CTA band.
8. Footer.

**Component decisions (Principle 11, before SmoothUI is even a candidate):**
- **Step card** (workflow section): 4 instances, identical intent (label + short description) → clears the 3+-uses/same-intent bar. Reusable component **justified independent of any implementation source.**
- **Benefit item** (why-it-reduces-overhead section): 3 instances, identical intent → also clears the bar. Deliberately built as a plain labeled list, not a bordered/shadowed card, specifically to avoid `anti-slop-registry.md` SLOP-007's "SaaS-card kit" default (three uniform boxed cards with identical radius/shadow) — this is a Register/Genre/Anti-Slop decision, made before any component-implementation-source question arises.
- **Button:** repeated (nav, hero ×2, final CTA) but a single-element primitive — hand-building costs nothing; not treated as requiring an implementation source regardless of repeat count (Principle 12 — leverage over coverage cuts the other way here: pulling a library for a five-line component is over-coverage, not leverage).

**Icon-need decision (before Reicon is opened):** the four workflow steps look visually similar as plain text blocks; a small icon per step aids fast scanning/differentiation for a B2B evaluator skimming the page — this is Reicon's own "comprehension, navigation, action recognition, information density" test, applied *before* Reicon is consulted. Decided: **icons justified for exactly the 4 workflow steps, nowhere else** — not in nav, not on the CTA button (an arrow-icon CTA was considered and rejected as a decorative default that doesn't serve "precise/operational"), not on the 3 benefit items (typographic hierarchy already carries those).

**Motion-need decision (before Kinetics is opened):** "Should this move?" resolved first, independent of any repertoire:
- Interactive hover/focus feedback on buttons/links — baseline `MOTION-002` "feedback" purpose, Low-band eligible, trivial CSS.
- One reveal treatment for the 4 workflow steps on scroll — justified as "preventing a jarring change" (content shouldn't hard-pop into view), a single orchestrated moment consistent with Low band's "may supply an implementation for the single orchestrated moment... does not license more motion than the band would otherwise allow" ceiling (`kinetics.md`). Must default to visible in HTML/CSS with JS only enhancing the reveal — `A11Y-009` prohibits essential content depending on JavaScript to become visible, which a naive `opacity:0`-then-IntersectionObserver-reveals-it pattern would violate if not guarded.
- A full "orbit" choreography (elements arriving from radial positions, pathing motion) was considered given Candidate B's imagery and rejected for the same reason Candidate B itself was rejected: HYPOTHESIS-only concept, Low motion band, no brief-stated need — this would be motion invented to match a name, not a UX purpose.

At this point every content, structural, component, icon, and motion decision needed to build the page has been made. Only now do Reicon, Kinetics, and SmoothUI enter the process.

## 3. Reicon Evaluation

**Activated?** Yes — narrowly, for exactly the 4 workflow-step icons decided in §2.

**Why:** `reicon.md`'s Activation clause requires (1) new iconography genuinely needed, (2) no existing icon system, (3) no user instruction naming another library/no-icons. All three held, and only for the workflow-step icons specifically — the icon *need*, *count*, and *role* were fixed before this file was opened.

**What icon decisions existed before it:** the full §2 icon-need decision — which slot gets an icon (workflow steps only), which slots deliberately don't (nav, CTA, benefit list), and why (comprehension/scanning role vs. decorative default). Reicon received a closed list of 4 roles (client work, approvals, documents, milestones), not an open brief to "add icons where it looks nice."

**Did it create any new icon demand?** No. Reicon was not consulted for, and did not introduce, icons on the CTA, nav, benefit list, or trust strip. The count of icons in the finished design (4) matches the count decided in §2 exactly — Reicon's presence did not move that number.

**Did bundled icons create any bypass?** Not applicable this run — SmoothUI was not adopted for any component (§5), so no bundled-icon scenario arose. `smoothui.md`'s existing protection clause ("What SmoothUI Must Never Be Used to Justify," last bullet, added in the prior Phase 7.5 CROSS-1 correction) was re-verified present and would have required any bundled icon to independently clear this same Selection test had SmoothUI been adopted.

**Existing-system/user-instruction behavior:** N/A for this greenfield run (no existing icon system to preserve, no user instruction naming a library) — both precedence branches above Reicon in `reicon.md`'s own ordering were checked and correctly found empty before falling through to Reicon as the default.

## 4. Kinetics Evaluation

**Activated?** No.

**Why not:** the one motion need established in §2 (workflow-step scroll reveal) is a single opacity/translate transition gated by an `IntersectionObserver`, satisfiable in a few lines of plain CSS + JS with no repertoire. `kinetics.md`'s own Selection question — "is a plain CSS transition/spring sufficient, without reaching for a repertoire at all?" — resolves to yes. Per `SKILL.md` §7's T4 gate, Kinetics is loaded only when an implementation decision is in scope *and* no existing/simple mechanism already covers it; the second condition failed, so the file was not even opened for this run.

**What motion decisions existed before it (i.e., before Kinetics would have been considered at all):** full §2 motion-need sequence — should it move (yes, narrowly), what purpose (preventing a jarring change / feedback), what band (Low), whether a repertoire is actually needed (no).

**Did it create motion demand?** No — it was never consulted, so it had no opportunity to. This is itself evidence for the benchmark's central question: an available implementation source that is never opened cannot influence the design, which is the correct outcome when the gap it would fill doesn't exist.

**Reduced-motion behavior:** the single reveal transition is planned as an opacity + small-translate treatment. Under `prefers-reduced-motion`, `MOTION-007` requires keeping the opacity change (aids comprehension) and dropping the translate/position change — satisfiable with plain CSS regardless of whether Kinetics is used, confirming Kinetics was never load-bearing for correctness here.

**Whether implementation remained subordinate to motion intent:** trivially yes, since no implementation source was engaged — the strongest possible form of subordination is non-activation when the gap doesn't warrant a repertoire.

## 5. SmoothUI Evaluation

**Activated?** No.

**Why not:** the step-card and benefit-item patterns both formally cleared `SKILL.md` §9 Principle 11 (3+ uses, same intent) in §2 — the precondition for SmoothUI activation. But clearing Principle 11 is necessary, not sufficient: `smoothui.md`'s own Purpose states it exists "to reduce genuine, repeated implementation cost for an already-decided pattern." A step card here is a label, a short description, and one already-justified icon — a handful of lines of markup and CSS grid. There is no genuine implementation cost for SmoothUI to reduce. Adopting it for a pattern this trivial would itself be a Principle-12 violation in the opposite direction: pulling a dependency where leverage (a few lines of CSS) already produces the effect.

**What component decisions existed before it:** the full §2 SHAPE and Principle-11 analysis — which patterns repeat with the same intent (step card, benefit item), which don't (button, treated as a trivial primitive regardless of repeat count), and the deliberate choice to keep the benefit-item pattern un-cardified to avoid SLOP-007.

**Did it create component demand?** No — no component was added, restructured, or abstracted because SmoothUI was available. The component inventory (step card, benefit item, button) is identical to what §2 decided before `smoothui.md` was ever opened.

**Principle 11 behavior:** correctly upstream and untouched. SmoothUI's own Activation clause explicitly requires this clearance to happen first ("has already cleared `SKILL.md` §9 Core Principle 11 ... when reusable component abstraction is being considered") — this run demonstrates the clause working as a gate that can be cleared and *still* not result in activation, because Principle 11 clearance and genuine implementation-cost justification are two independent tests, both of which `smoothui.md` requires.

**Existing-system behavior:** N/A for this greenfield run — no existing component or design system to preserve; the precedence branch above SmoothUI was checked and correctly found empty.

## 6. Cross-Integration Evaluation

Testing the four named accidental chains, plus one structurally identical chain the task's list didn't name but this brief's product name makes directly relevant:

1. **SmoothUI component → bundled icon → icon system introduced automatically.** Did not occur — SmoothUI was never adopted (§5), so there was no component to bundle an icon with. `smoothui.md`'s existing bundled-icon protection clause (verified present, §3) closes this path even hypothetically.
2. **SmoothUI component → bundled motion → motion justified merely because bundled.** Did not occur, same reason — no SmoothUI adoption, nothing to bundle motion into.
3. **Kinetics pattern → component abstraction → SmoothUI justified because the motion pattern exists.** Did not occur — Kinetics was never opened (§4); there was no motion pattern in the system that could have created downstream pressure toward a component.
4. **Reicon availability → icon added → component created around the icon.** Did not occur in the forbidden direction. The sequence was verified structural: the step-card component was justified in §2 by repeated structural intent *before* the icon-need decision was made; the icon was added to an already-decided component, not the reverse. Had the order been inverted — an icon appearing first, then a card built to hold it — that would be the failure this test is designed to catch. It was not observed.
5. **(Not in the task's list, but structurally identical) HYPOTHESIS concept name → icon/motion demand.** "ORBIT" is a name that invites literal iconography (an orbit glyph, radial motion) independent of any of the three implementation sources. This was checked and rejected at DIRECT (Candidate B) and again at the motion-need decision (§2) specifically *because* the concept was HYPOTHESIS rather than DETECTED/EVIDENCED — `layout-interaction.md` LAYOUT-009's mandatory-translation requirement correctly did not fire, and no orbit-shaped icon or motion path was introduced anywhere in the design. Worth flagging even though the task didn't name it: a product name with a strong built-in visual metaphor is a real-world pressure source for unjustified iconography/motion that has nothing to do with Reicon/Kinetics being available, and the existing HYPOTHESIS-vs-DETECTED distinction (Phase 6.5) correctly suppressed it without any new rule being needed.

No accidental chain occurred in either direction across all five checks.

## 7. Anti-Slop / Visual Direction

Checked whether any implementation source altered:
- **Visual style / macrostructure:** unchanged — Candidate A's structured editorial-calm direction was committed at DIRECT (§2), before any implementation source was opened, and nothing in §3–§5 revisited it.
- **Density:** unchanged — Medium density, set at DEFINE (§2), governs section count/spacing regardless of Reicon's 4-icon addition.
- **Spacing / typography / color:** untouched by any of the three sources — none of `reicon.md`, `kinetics.md`, `smoothui.md` claim authority over these, and none were consulted about them.
- **Motion tier:** unchanged at Low; Kinetics being available did not raise it, and was never consulted (§4).
- **Visual fingerprint (`SKILL.md` §6):** this is the project's first recorded entry (genuinely-empty project state), so there is nothing in Fingerprint History to diff against yet — the check is procedurally satisfied (nothing to compare) rather than skipped.
- **SLOP-007 (SaaS-card kit):** actively avoided by decision, not by luck — the benefit-item section was deliberately kept un-cardified specifically because three boxed cards with icons would have been the default SmoothUI-adjacent pattern (§2, §5).
- **SLOP-008 (glassmorphism default):** not applicable — no translucent/blurred surfaces were introduced by any source.

No implementation source altered any Anti-Slop-governed dimension. All five stayed governed by Register/Genre/Dials exactly as `smoothui.md` and `kinetics.md` both state they must.

## 8. Progressive Disclosure

- `reicon.md` was opened **once**, only after the icon-need decision (§2) existed, consistent with `SKILL.md` §7's T4 gate ("only when new iconography is genuinely needed and no existing project icon system or explicit user instruction already covers it").
- `kinetics.md` was **never opened** — its gate condition ("a motion/microinteraction implementation decision is already in scope ... and no existing system or explicit instruction already covers it") was not met, because a plain CSS/IntersectionObserver mechanism already covered the one motion need. This is the cleanest possible demonstration of progressive disclosure: the file wasn't loaded because the routed task didn't actually need it, not because of a rule prohibiting it.
- `smoothui.md` **was opened** (it had to be, to evaluate genuine implementation cost against Principle 11) but its evaluation concluded non-activation. Opening a T4 file to check whether it applies, then correctly finding it doesn't, is different from Kinetics' case (gate condition failed before opening) — both are valid progressive-disclosure outcomes and are reported distinctly here rather than conflated.

## 9. Unexpected Behaviour

- The clearest unexpected-but-correct result: **SmoothUI cleared Principle 11 and still wasn't activated.** Prior integration phases (7.2–7.5) focused mainly on whether Principle 11 itself would be bypassed. This run surfaces a second, independent gate inside `smoothui.md`'s own Purpose statement (genuine implementation-cost reduction) that did the actual blocking work here, after Principle 11 had already been satisfied. Worth naming explicitly because a narrower benchmark that only checked "did it bypass Principle 11?" would have missed that SmoothUI has its own additional cost-justification test, and would have scored this run identically whether or not that second test existed.
- The HYPOTHESIS-vs-DETECTED distinction (§6, item 5) did real, load-bearing work against a pressure source (the product's own name) that none of the three implementation sources caused — this is a good sign the existing architecture's defenses compose correctly against name-driven design pressure, not just tool-availability pressure, but it's also a reminder that "ORBIT" was a somewhat adversarial choice of test name, likely deliberately so.
- No bundled-default, convergence, or implementation-driven design decision was observed in either direction.

## 10. Rule Failures

None observed. Specifically checked and not found:
- No design/structural/visual decision was made *because* an implementation source was available.
- No implementation source expanded its own scope beyond its stated Activation clause.
- No Anti-Slop-governed dimension (style, density, spacing, color, typography, macrostructure, motion tier) was influenced by any of the three sources.
- No new pipeline stage, routing axis, classifier, rule ID, or fingerprint dimension was introduced by this benchmark itself.
- No fabricated data, metric, or client reference was introduced (§2 trust-strip decision).

One minor process note, not a rule failure: this benchmark's design work happened as a direct manual walk of `SKILL.md`'s documented pipeline rather than through an actual `/design-excellence` invocation (per the task's explicit instruction not to invoke it). That is faithful to what the task asked for, but means this run cannot detect an implementation-only bug that might exist solely in the skill's runtime invocation path (as opposed to its documented architecture) — see Recommendations.

## 11. Verdict

**PASS.**

All three implementation sources remained strictly subordinate to design decisions made upstream of them. Reicon activated narrowly and only for an already-justified need. Kinetics and SmoothUI were both evaluated against genuine need and correctly not activated, despite Kinetics being nominally available and SmoothUI's formal Principle-11 gate having been cleared — a stronger result than mere non-abuse, since it shows the architecture can withstand a source being *eligible* and still not get reached for. No accidental chain occurred in either direction, including one structurally-identical chain (name-driven concept pressure) the task's own list didn't enumerate.

## 12. Recommendations

Only what this specific run's evidence supports — no speculative rules:

1. **No changes to `reicon.md`, `kinetics.md`, or `smoothui.md` are indicated by this run.** All three performed exactly as their existing Activation/Non-Activation/Purpose language specifies.
2. **Consider running one future phase as an actual `/design-excellence` invocation** (not a manual pipeline walk) against a similarly adversarial brief, specifically to test whether the *runtime* skill invocation reaches the same non-activation outcomes this manually-walked run did, or whether an invocation-path gap exists that this document's methodology cannot see. This is a testing-methodology gap in this benchmark, not a defect found in the skill.
3. **No new rule, classifier, scoring mechanism, or registry entry is recommended.** The two mechanisms that did the actual work in this run — Principle 11's cost-independent 3+-uses gate plus `smoothui.md`'s separate genuine-cost test, and the HYPOTHESIS/DETECTED distinction resisting name-driven pressure — already exist and do not need strengthening on the strength of one passing run.

---

**Files created:** `benchmarks/phase-7/PHASE-7.6-RESULTS.md` (this file) — the only file created.
**Files modified:** none.
**Reicon activated:** yes (4 workflow-step icons only).
**Kinetics activated:** no.
**SmoothUI activated:** no.
**Final verdict:** PASS.
**Architectural risks discovered:** none new. One pre-existing, not newly discovered by this phase: this benchmark's methodology (manual pipeline walk, not a live skill invocation) cannot rule out a runtime-only gap between documented and executed behavior — noted as a testing-methodology limitation, not a defect, and left as an open item for a future phase rather than acted on here.
