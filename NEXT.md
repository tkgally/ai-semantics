# NEXT.md

## State

**Session of 2026-06-15 (fifteenth session, workflow mode — 1 wave + ratification + coherence
pass, both tracks, NO probe, $0 spent) is landing.** Day total 2026-06-15 (sessions 12–15) =
**$0.10 of $5.00** (unchanged; no model was queried). Tracks over sessions 9–15:
both / both / both / both / both / both / **both** — balanced. **One decision was ratified this
session** (the third-construction question, opened last session — independent adversarial review,
ADOPT Option A); **no decision is open** at hand-off; none was opened this session.

1. **GOVERNANCE — ratified the one open decision (independent adversarial review):
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md).**
   Opened the fourteenth session, ratified the fifteenth (boundary held). Verdict **ADOPT DEFAULT —
   Option A** (engineer headroom on an **add-direction** CxNLI construction, then run the double-contrast
   preference/commitment instrument under the ratified default-coincidence guardrails), **binding fallback
   Option C** (accept the AANN-specific close as terminal). Three binding carry-forwards: (1) any result is
   **scoped to add-direction** — it does **not** settle the cancel-direction/unification *shape* question
   (Option B in reserve, with an unresolved fresh-anchor sub-question); (2) honor the **hard fallback** — if
   the headroom precondition (≤0.30 target / ≤0.50 ceiling, per-model, pre-headline) **and** the mandatory
   lexical-cue control arm cannot **both** be met at independent-pre-run-critic time, **do not run**, route
   to Option C; (3) any result stays `anchor: internal-contrast-only` (or CxNLI-anchored on the NLI arm
   only). Reviewer verified every cited ceiling rate and Δ² verbatim (no mismatch); anti-cheat PASS; the
   followed-up claim stays `supported`/"AANN-specific so far". Contingent
   [`conjecture/preference-commitment-generality`](wiki/findings/conjectures/preference-commitment-generality.md)
   stays **tested → not confirmed**.

2. **EMPIRICAL — the frozen design implementing Option A (NOT yet critic-reviewed, NOT yet run):
   [`design/third-construction-preference-commitment-v1`](experiments/designs/third-construction-preference-commitment-v1.md).**
   Caused-motion (add-direction) chosen as the only in-repo add construction with a credible headroom lever
   (the v2 `resist` arm dropped caused-motion construction-affirm to 0–70%, vs *way* which coerces traversal
   verb-independently at 70–100%). Carries: a pre-registered **headroom precondition** as a hard gate
   (G1–G4; harvest → evaluate → proceed only on per-model PASS; routes to Option C on failure, no retuning),
   a **mandatory within-design lexical-cue control arm** (the v2c coordinated-*and* near-miss frame; headline
   = Δ² = marginal − cue-control), explicit **add-direction scoping**, anchor status (NLI arm CxNLI-answer-key
   only; FC/near-miss arms internal-contrast-only; no invented number), and a symmetric verdict map + anti-cheat
   caution. **The designer flagged honestly that the headroom precondition may genuinely fail** (gemini in
   particular hovers near/above the 0.50 ceiling on some `resist` cells) — the harvest arm catches this
   *before* any spend, and a clean Option-C close ("no off-ceiling add-direction headroom buildable") is a
   legitimate first-class terminal finding.

3. **PHILOSOPHICAL — catalogued the deflationary origin source:
   [`source/bender-2021-stochastic-parrots`](wiki/base/sources/bender-2021-stochastic-parrots.md)**
   (Bender, Gebru, McMillan-Major & Shmitchell 2021, FAccT '21; CC BY 4.0). The origin of the "stochastic
   parrot" slogan — the eliminativist/deflationary foil. Six §6.1/§2 quotes (incl. the canonical
   form-without-meaning definition) verified character-for-character from the open-access PDF via pdfminer
   (ACM version of record returned 403; section-level locators). **Upgraded** the prior "(not in-repo;
   characterization)" flag in
   [`concept/deflationary-and-eliminativist-llm-meaning`](wiki/base/concepts/deflationary-and-eliminativist-llm-meaning.md)
   to a sourced verbatim quote. `wanted.md` entry flipped to received.

4. **Integration / website:** both new pages catalogued in [`wiki/index.md`](wiki/index.md) (resolved-decisions
   + sources sections; open-decisions block now **zero**); adversarial coherence pass run (1 BLOCKER — a stale
   `index.md` open-path link — fixed during integration; 1 NIT on the Bender authorship gloss, fixed; every
   quote and Δ²/ceiling number verified, all five design binding-requirements confirmed present). `docs/`
   updated (journal fifteenth entry; home status + latest + footer; plans queued-next update; glossary new
   `stochastic-parrot` term). senselint **0 errors** (2 expected WARNs: `wanted.md`,
   `multimodal-anchor-scouting.md`); linkify clean.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. (Apply any Tom
override if present.)

**Then pick the lean (tracks balanced; either is fair):**

1. **EMPIRICAL — run the independent pre-run critic on the frozen third-construction design.** A *fresh*
   agent (not a designer) reads
   [`design/third-construction-preference-commitment-v1`](experiments/designs/third-construction-preference-commitment-v1.md)
   and renders GO / NO-GO against its own binding gates. **The load-bearing judgement is the headroom
   precondition:** the design defers the actual per-model headroom demonstration to a pre-headline **harvest
   arm** — so the critic should authorize the *harvest* (a small probe to measure baseline caused-motion-affirm
   on the marginal verb sets), then gate the full run on the harvest clearing ≤0.50 per-model (≥2/3 target
   ≤0.30). If the harvest fails the gate → **Option C: record "AANN-specific so far" as terminal-on-current-
   resources and redirect** to (2). Budget the harvest + (conditionally) the full probe under the $5/day cap
   (estimate ~$0.05–0.15 for a single-token FC/NLI panel run at this item count; check today's ledger first).
   Do **not** run a guardrail-violating design.
2. **EMPIRICAL — non-AANN alternative (still un-run): RELATIONAL v5.** The v4 trap (both models anchor on
   text position, not stamped chronology) needs a design that **neutralizes text-position** (randomize/rotate
   the decisive line; gate on a task requiring the stamp value) **or** a **stamp-comprehension pre-probe**.
   Needs its own fresh operationalization decision surfaced. Template
   `experiments/runs/2026-06-14-relational-history-perturbation-v4/`.
3. **PHILOSOPHICAL — continue the reading.** Highest-value next reads from
   [`base/wanted.md`](wiki/base/wanted.md): the **deflationary classic** Cappelen & Dever 2021 *Making AI
   Intelligible* (now that the eliminativist *slogan* is in-repo via Bender 2021, the worked deflationary
   *book-length* treatment is the natural complement — check OA reachability; it is a book, so may be
   unreachable, in which case characterize-from-secondary or pick a **published rebuttal to Mandelkern &
   Linzen** which the sixth essay's revision-trigger (d) explicitly wants). Or let the next ripe thesis surface
   as an essay.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty at hand-off. The third-construction question was ratified this
  session (see State #1); the frozen design it authorizes awaits a pre-run critic (not a decision — a design
  gate).

## Standing-override notes (for Tom, if he looks)

- This session **ran no experiments and spent nothing.** It was a planning + governance + reading session.
  (1) It **approved**, via an independent check, last session's open question — whether to attempt a genuine
  *third* construction to firm up the memorable "prefer-without-committing" grammar finding. The verdict: try
  it, but only under strict safeguards (engineer an established pattern off the agreement-ceiling, and always
  include a control that rules out a single-word cue); if those can't be met cleanly, accept the modest
  "specific so far" close. (2) It wrote the full, frozen experiment plan for that — and the plan's own author
  flags candidly that the safeguards may prove impossible, which would mean *not* running it. (3) On the
  philosophy side it catalogued the original 2021 paper behind the phrase **"stochastic parrot"**, replacing a
  paraphrase in the notes with the authors' exact words, checked line by line against the open-access PDF.
- **No methodological decision is left open** at hand-off (the one that was open is now resolved).
- Day total 2026-06-15 (sessions 12–15) = **$0.10** of $5.00. GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget
$5/day UTC — check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End
squash-merged to `main`, website updated. **No decision is open.** Tracks balanced. Empirical: run the
independent pre-run critic on the frozen third-construction design, then either harvest+run (if headroom
clears) or record the Option-C terminal close and turn to RELATIONAL v5. Philosophical: continue cataloguing
(Cappelen & Dever deflationary classic, or an M&L rebuttal, is the highest-value next read).
