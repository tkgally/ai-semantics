# PREREG (DRAFT — awaiting independent pre-run critic GO) — relational IMPLICIT-reassignment control

**Status: DRAFT.** This is `PREREG-draft.md`; `probe.py full` refuses to run until it is frozen
to `PREREG.md` **after** an independent pre-run critic returns GO. The binding pre-run gate is the
same one Option A carried (certify the task **unsolvable by a positional/lexical/frequency
shortcut** on idealized-reader fixtures *before* any run — if it cannot be certified, do not run;
**do not weaken the task to get a GO**).

## What this is and why it runs

This is the **implicit-reassignment control** of
[`result/relational-spontaneous-recency-a`](../../../wiki/findings/results/relational-spontaneous-recency-a.md)
(Option A of the ratified relational-v5 staged design). Option A found both panel models recover a
**reassigned** coined term by its **most-recent binding**, *spontaneously* (SPONT latest-binding
rate 1.000, physical-position at chance, DIRECT on-demand 1.000, 0 NA) → promoted to
[`claim/relational-order-sensitive-reassignment`](../../../wiki/findings/claims/relational-order-sensitive-reassignment.md)
(LLM referential conventions are order-sensitive / non-commutative in the regime where recency
disambiguates).

That claim carries one **sharpest open caveat**, flagged in advance by the Option-A post-run
verifier and written into the claim as **scope limit 4 / revision trigger 2**:

> *"Spontaneous = query-not-directed, not cue-free.* The framing flags that the term was reassigned
> (a choice among bindings is required); the models resolve that choice by recency without the query
> asking them to."
>
> *Revision trigger 2:* Evidence that the latest-binding-wins behaviour is a **surface artifact** of
> the explicit "was reassigned" wording (e.g. it vanishes when reassignment is implicit) would
> **narrow** it.

This control runs exactly that test. It removes Option A's one explicit reassignment sentence —

> *"The term was reassigned: in different rounds you agreed it referred to different figures."*

— from the INTRO and re-measures the SPONT latest-binding rate. **Everything else is held
identical.** The frozen stimuli roster is **byte-identical to Option A** (same `stimuli.json`
sha256 `432cb57d4aeefea62f382923fbc98019a184bd1e62879956edcd0e3dd944ff71`; the INTRO text lives in
`common.py`'s prompt renderer, not in the roster), so the **only** difference between this run and
Option A is the one dropped sentence — a clean single-factor control.

**The question this isolates:** when a coined term simply **is** used for different figures across
stamped rounds — with **no sentence flagging that a reassignment occurred** — and the matcher is
asked which figure the term refers to (no recency mention), does the model **still** spontaneously
recover the **most-recent** binding, or does removing the explicit reassignment flag collapse the
latest-binding-wins behaviour?

## Hypotheses / verdict (frozen)

Per model, over byte-identical stamped records with physical line-position **neutralized by
balanced rotation** and the term used for K distinct figures (once each → frequency flat):

Two query conditions, each its own balanced-block roster (the Option-A geometry, unchanged):

- **SPONT (headline).** Query: *"Which of your figures does the term \"DAX\" refer to?"* — **no
  recency mention.** Report `latest_rate` = P(pick = max-round figure) [latest-governs: the
  operative-convention reading] and `first_rate` = P(pick = min-round figure) [anti-recency /
  first-governs diagnostic], each with a Wilson-95 interval.
- **DIRECT (manipulation check).** B-style explicit-recency query (*"…MOST RECENTLY (in the
  latest round)?"* / *"…EARLIEST (in the very first round)?"*). `direct_acc` = pooled accuracy.
  Confirms **on-demand** recency comprehension survives in *this* instrument **without** the
  reassignment flag (figures + stamped history + grid). It is **not** the headline; it gates
  interpretability of SPONT (a SPONT null is uninterpretable unless on-demand reading is intact
  here).

**Frozen verdict per model (identical map to Option A):**

| Verdict | Condition | Reading |
|---|---|---|
| `UNINTERPRETABLE` | `direct_acc < DIRECT_FLOOR (0.80)` | on-demand check failed *here*; SPONT cannot be read |
| `SPONTANEOUS-RECENCY` | direct gate passed **and** `latest_rate` Wilson-LB `> 0.25`, first not | order-sensitive (latest-governs) — **non-commutative** |
| `SPONTANEOUS-ANTI-RECENCY` | direct gate passed **and** `first_rate` Wilson-LB `> 0.25`, latest not | order-sensitive (first-governs) — **non-commutative** |
| `ORDER-SENSITIVE-MIXED` | direct gate passed **and** both LBs `> 0.25` | guard; report both |
| `COMMUTATIVE-HERE` | direct gate passed **and** neither LB `> 0.25` | order-insensitive **without** the explicit flag |

## What each outcome means for the claim (frozen, pre-registered)

This is a **control on an existing supported claim**, so the result reading is fixed in advance and
points at `claim/relational-order-sensitive-reassignment`:

- **Both models `SPONTANEOUS-RECENCY` (latest-binding rate persists ≈ ceiling).** The
  latest-binding-wins behaviour is **not** a surface artifact of the explicit "was reassigned"
  wording: it survives when the reassignment is implicit. This **strongly bounds** revision-trigger 2
  in the claim's favour and **strengthens** the claim — order-sensitivity holds even without the
  scaffolding sentence. Scope limit 4 is **tightened**: "spontaneous" was already query-not-directed;
  now it is also flag-not-directed. (The claim stays `supported`; no inflation beyond
  internal-contrast-only.)
- **Both models `COMMUTATIVE-HERE` (latest-binding rate collapses to ~chance).** The Option-A effect
  **was** carried by the explicit reassignment flag. Revision trigger 2 **fires**: the claim is
  **narrowed** to the explicit-reassignment frame (the models track recency only when told a
  reassignment occurred). The Option-A positive is preserved but scoped.
- **Split / `ORDER-SENSITIVE-MIXED` / `UNINTERPRETABLE`.** Report per model exactly; narrow the claim
  to the models/regime where order-sensitivity survives; locate the inconclusiveness. A model that
  fails the DIRECT gate **here** (despite passing B and the Option-A DIRECT) is `UNINTERPRETABLE` for
  SPONT — flag it; do not read its SPONT as either outcome.

**Anti-retuning (binding).** The verdict map, the DIRECT floor (0.80), the SPONT bar (Wilson-95
LB > 0.25), and the frozen roster are all carried **verbatim** from Option A and frozen here
**before** any call. The outcome is read off these fixed instruments; the indicator is not adjusted
after seeing results (PROTOCOL §8). A collapse is as publishable as a persistence — the null narrows
a claim, which is a first-class result.

## Instrument (frozen)

- Panel: **claude + gemini** (the A-eligible relational panel carried from v4/B/Option A; both
  passed B; gpt was dropped from the finding-bearing relational panel for a stimulus-generation
  reason — not re-opened, to keep this a clean control of Option A).
- Each record: a grid of **K=4** clearly-distinct figures (label + short description) + a stamped
  history in which the coined term **DAX** is used for the 4 figures across 4 **non-contiguous**
  rounds (e.g. `{2,4,7,9}`), **once each** — so the content-set is *symmetric* (all four figures are
  "called DAX") and **only recency disambiguates**, and the frequency heuristic is flat. The history
  references a figure by its *description*; the answer space is the figure *label* (matcher maps
  description→label via the grid — the v4/Option-A instrument class). A sample SPONT prompt is in the
  README and design doc.
- **The sole manipulation vs Option A: the INTRO drops the explicit reassignment flag.** Option A's
  INTRO said *"The term was reassigned: in different rounds you agreed it referred to different
  figures."* This control's INTRO omits that sentence entirely. It **keeps** the stamp semantics
  ("a higher round number means it was said more recently") and the not-in-round-order note —
  exactly the framing **Option B proved both models read on demand** — because those are required
  for the stamp to be interpretable and for the DIRECT gate to be meaningful. The model must itself
  notice the term picks out different figures across rounds.
- **Distinct figures, not v4 near-twins** (carried from Option A, ratified there): near-twins would
  confound a recency failure with a discrimination failure; this control isolates recency-weighting,
  so figures are trivially discriminable and shortcut-proofing comes from the balanced-block
  construction, not near-twin difficulty.
- **Position AND lexical AND frequency neutralization (balanced-block design).** Each subset is an
  independent balanced-block roster: N distinct present-sets (each figure in exactly N·K/|pool|
  sets) × K records under a Latin square, so within a present-set the governing figure cycles through
  all K members once **and** the governing line's physical history-slot cycles through all K slots
  once. **Three shortcut bounds are proven at build, separately per subset** (over all K! slot
  strategies and all |pool|! figure orderings): (a) every constant-physical-history-slot strategy
  scores **exactly 1/K**; (b) **every** fixed figure-preference ordering (incl. the grid-order
  ordering, so a "grid-position" strategy is covered) scores **exactly 1/K**; (c) each figure appears
  exactly once per record, so the **frequency** heuristic carries no signal. So no position, lexical,
  or frequency shortcut can clear the SPONT order-sensitivity bar or the DIRECT floor — **only
  reading the round stamp as recency can.**
- Forced single-label elicitation; strict parse; **a `finish_reason == "length"` reply is never
  parsed**; one stern retry on parse-fail then NA. `reasoning: minimal` on gemini (cost caveat).

## Pre-registered constants (frozen)

- `K = 4`; `N_BLOCKS_SPONT = 12` ⇒ **48 SPONT records/model**; `N_BLOCKS_DIRECT = 8` ⇒ **32
  DIRECT records/model** (16 DIR_MR + 16 DIR_LR). Total **80 records/model × 2 models = 160
  finding-bearing calls.**
- `DIRECT_FLOOR = 0.80`; `POS_CHANCE = 1/K = 0.25`. SPONT order-sensitivity bar = Wilson-95
  lower bound strictly above `POS_CHANCE`.
- `ROUND_SETS`, `FIGURES`, `TERM = "DAX"`, `SEED0 = 20260616` frozen in `common.py` — **identical
  to Option A**.
- `stimuli.json` sha256: `432cb57d4aeefea62f382923fbc98019a184bd1e62879956edcd0e3dd944ff71`
  — **byte-identical to Option A's frozen roster** (confirm against `python3 build_trials.py`
  output before freezing). The INTRO manipulation is in `common.py`'s renderer, not the roster.

## Idealized-reader fixtures (run, no API — the GO-discipline)

`python3 fixtures/make_fixtures.py` builds the frozen stimuli through the real
`build_trials.build()` and six synthetic raw sets; **all asserts PASS** (the fixtures are
prompt-text-agnostic — they certify the verdict map + shortcut bounds over the roster, which is
unchanged):

- `spont_latest` (on-demand + spontaneous recency) → **SPONTANEOUS-RECENCY**, `latest_rate = 1.0`.
- `first_governs` (on-demand + anti-recency) → **SPONTANEOUS-ANTI-RECENCY**.
- `commutative` (on-demand OK, SPONT order-insensitive) → **COMMUTATIVE-HERE**, `latest_rate =
  first_rate = 1/K` exactly.
- `lastpos` (pure position-follower) → **UNINTERPRETABLE**, **not** order-sensitive, SPONT
  `latest_rate = 1/K` exactly.
- `figpref` (fixed figure-preference) → **UNINTERPRETABLE**, **not** order-sensitive.
- `direct_fail` (SPONT looks spontaneous, on-demand FAILS) → **UNINTERPRETABLE** (the gate guards
  a false positive even at SPONT `latest_rate = 1.0`).

**The load-bearing certification:** no positional / lexical / frequency shortcut ever yields a
`SPONTANEOUS-*` (non-commutative) verdict — only genuine stamp-recency reading does; and the
manipulation gate refuses to read a SPONT null as order-insensitivity unless on-demand comprehension
is demonstrated in this very instrument. These are synthetic and are never findings.

## Anchor

`anchor: internal-contrast-only` (carried from Option A, ratified 2026-06-16). Within-model
behavioural contrast over byte-identical content; **no human-comparison claim**. (No in-repo human
resource grounds human order-/path-sensitivity at this grain — Brennan & Clark report an
order-*insensitive* statistic — and none is owed because no human contrast is asserted.)

## Spend (frozen gate)

Billed `usage.cost` only (never rate-card). Per-phase ledger; every API phase pre-checks
ledger-total + projected ≤ **$0.50** hard stop. Pre-flight estimate (per Option A's measured
$0.124444 over 160 finding-bearing calls = ~$0.00078/call): liveness ≈ $0.002; full 160 calls ≈
**$0.10–0.13** → inside the $0.50 stop and the $5.00/day cap (day total going in: $0.00). Record
actuals in `config/budget.md`.

## Execution order (after critic GO)

```
python3 fixtures/make_fixtures.py   # no API — asserts PASS (already run at build)
python3 build_trials.py             # no API — stimuli.json + sha256 (must = Option A's)
# ORCHESTRATOR: apply critic fixes; confirm sha256; freeze PREREG-draft.md -> PREREG.md; commit
python3 probe.py liveness           # 2 calls; both models must parse (on-demand correct = F8)
python3 probe.py full               # 160 calls -> raw/probe-<model>.jsonl
python3 analyze.py                  # no API -> printed verdict + raw/analysis.json
# then: independent post-run verifier reproduces every number from raw, own route.
```
