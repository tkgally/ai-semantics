# PREREG (DRAFT — awaiting independent pre-run critic GO) — relational spontaneous-recency arm (Option A)

**Status: DRAFT.** This is `PREREG-draft.md`; `probe.py full` refuses to run until it is frozen
to `PREREG.md` **after** an independent pre-run critic returns GO (binding carry-forward 3 of the
ratified decision: certify the task **unsolvable by a positional/lexical shortcut** on
idealized-reader fixtures *before* any run — **if it cannot be certified, route to Option C; do
not weaken the task to get a GO**).

## What this is and why it runs

The ratified design decision
[`decisions/.../relational-v5-text-position-neutralization`](../../../wiki/decisions/resolved/relational-v5-text-position-neutralization.md)
(adopt-default, 2026-06-16 adversarial review: **Option B then A, staged; C the binding fallback**)
authorizes an Option-A **position-rotated, stamp-gated chronology arm** for every model that
passed the Option-B stamp-comprehension gate. Both panel models passed B
([`result/relational-stamp-comprehension-b`](../../../wiki/findings/results/relational-stamp-comprehension-b.md):
claude + gemini each 1.000, position-following at chance) — they read the round stamp as a
recency value **on demand**. So A is warranted, and B's pass makes an A-null interpretable for
the first time.

Option A asks the question the staged design exists for, and the one
[`conjecture/commutative-convention`](../../../wiki/findings/conjectures/commutative-convention.md)
names as decisive: **when a coined term is reassigned to different referents across stamped
rounds, and the matcher is asked which referent the term picks out — without the query directing
attention to recency — does the model spontaneously weight the round stamp (treat the
most-recent agreement as operative: a *path-dependent, non-commutative* convention), or treat the
history as an order-insensitive content-set (*commutative*)?** Text-position is neutralized by
balanced rotation (Option A's geometry fix), so "follows stamped chronology" is finally separable
from "follows text position" (the v4 confound).

## Hypotheses / verdict (frozen)

Per model, over byte-identical stamped records with physical line-position **neutralized by
balanced rotation** and the term reassigned to K distinct figures (once each → frequency flat):

Two query conditions, each its own balanced-block roster:

- **SPONT (headline).** Query: *"Which of your figures does the term \"DAX\" refer to?"* — **no
  recency mention.** Report `latest_rate` = P(pick = max-round figure) [latest-governs: the
  operative-convention reading] and `first_rate` = P(pick = min-round figure) [anti-recency /
  first-governs diagnostic], each with a Wilson-95 interval.
- **DIRECT (manipulation check).** B-style explicit-recency query (*"…MOST RECENTLY (in the
  latest round)?"* / *"…EARLIEST (in the very first round)?"*). `direct_acc` = pooled accuracy.
  Confirms **on-demand** recency comprehension survives in *this* instrument (figures +
  reassignment + grid). It is **not** the headline; it gates interpretability of SPONT.

**Frozen verdict per model:**

| Verdict | Condition | Reading |
|---|---|---|
| `UNINTERPRETABLE` | `direct_acc < DIRECT_FLOOR (0.80)` | on-demand check failed *here*; SPONT cannot be read |
| `SPONTANEOUS-RECENCY` | direct gate passed **and** `latest_rate` Wilson-LB `> 0.25`, first not | order-sensitive (latest-governs) — **non-commutative** |
| `SPONTANEOUS-ANTI-RECENCY` | direct gate passed **and** `first_rate` Wilson-LB `> 0.25`, latest not | order-sensitive (first-governs) — **non-commutative** |
| `ORDER-SENSITIVE-MIXED` | direct gate passed **and** both LBs `> 0.25` | guard; report both |
| `COMMUTATIVE-HERE` | direct gate passed **and** neither LB `> 0.25` | the ratified **narrow A-null** |

**Conjecture reading.** `SPONTANEOUS-*` / `ORDER-SENSITIVE-MIXED` = order-sensitive ⇒ evidence
**against** commutativity (would move `conjecture/commutative-convention` toward falsification, in
the chronology direction, under its binding scope limits). `COMMUTATIVE-HERE` = consistent with
commutativity, in the **narrow spontaneous-weighting sense only** — the ratified wording:
*"comprehends recency on demand but does not spontaneously weight it here"* (binding carry-forward
4). **Never** inflated to "comprehends recency" in general, **never** to "the models chose to
ignore recency." A COMMUTATIVE-HERE does **not** by itself certify the commutative null (it is one
arm, narrow); it keeps the conjecture `proposed` with its inconclusiveness located, exactly as v4
left it.

## Instrument (frozen)

- Panel: **claude + gemini** (A-eligible relational panel carried from v4/B; both passed B; gpt
  was dropped from the finding-bearing relational panel for a stimulus-generation reason — not
  re-opened).
- Each record: a grid of **K=4** clearly-distinct figures (label + short description) + a stamped
  history in which the coined term **DAX** is reassigned across 4 **non-contiguous** rounds (e.g.
  `{2,4,7,9}`) to the 4 figures, **once each**. The history references a figure by its
  *description*; the answer space is the figure *label* (matcher maps description→label via the
  grid — the v4 instrument class). A sample SPONT prompt is reproduced in the design doc.
- **Why distinct figures, not v4 near-twins (a deliberate, surfaced deviation from the Option-A
  sketch).** The decision's Option-A *sketch* suggested keeping the v4 near-twin harvest class.
  This arm deliberately uses **clearly-distinct** figures and **no** harvest/certification of
  near-twins, because near-twins would **confound** a recency failure with a *discrimination*
  failure: a model could score low on SPONT either because it ignores recency (what we want to
  measure) or because it cannot tell the figures apart. Option A isolates **spontaneous
  recency-weighting**, so the only hard step must be reading the stamp; the figures must be
  trivially discriminable. Shortcut-proofing comes from the **balanced-block construction**, not
  from near-twin difficulty. (Option B was likewise ratified without near-twins, for the same
  reason — no stimulus-certification burden.) **This deviation is flagged for the independent
  critic to rule on** — if the critic judges that dropping near-twins changes what Option A tests
  in a way that needs re-surfacing, route accordingly rather than weakening the task.
- **Position AND lexical AND frequency neutralization (balanced-block design).** Each subset is an
  independent balanced-block roster: N distinct present-sets (each figure in exactly N·K/|pool|
  sets) × K records under a Latin square, so within a present-set the governing figure cycles
  through all K members once **and** the governing line's physical history-slot cycles through all
  K slots once. **Three shortcut bounds are proven at build, separately per subset** (over all K!
  slot strategies and all |pool|! figure orderings): (a) every constant-physical-history-slot
  strategy scores **exactly 1/K**; (b) **every** fixed figure-preference ordering (incl. the
  grid-order ordering, so a "grid-position" strategy is covered) scores **exactly 1/K**; (c) each
  figure appears exactly once per record, so the **frequency** heuristic carries no signal. So no
  position, lexical, or frequency shortcut can clear the SPONT order-sensitivity bar or the DIRECT
  floor — **only spontaneously reading the round stamp as recency can.**
- Forced single-label elicitation; strict parse; **a `finish_reason == "length"` reply is never
  parsed**; one stern retry on parse-fail then NA. `reasoning: minimal` on gemini (cost caveat).
- INTRO is the **same neutral framing B used and B proved both models read**: it states the stamp
  semantics ("a higher round number means it was said more recently") and that lines are not in
  round order, and that the term was reassigned — but does **not** instruct the model to weight
  recency or to treat the latest agreement as operative. The SPONT vs DIRECT contrast lives
  **entirely in the question**, holding the record framing constant.

## Pre-registered constants (frozen)

- `K = 4`; `N_BLOCKS_SPONT = 12` ⇒ **48 SPONT records/model**; `N_BLOCKS_DIRECT = 8` ⇒ **32
  DIRECT records/model** (16 DIR_MR + 16 DIR_LR). Total **80 records/model × 2 models = 160
  finding-bearing calls.**
- `DIRECT_FLOOR = 0.80`; `POS_CHANCE = 1/K = 0.25`. SPONT order-sensitivity bar = Wilson-95
  lower bound strictly above `POS_CHANCE`.
- `ROUND_SETS`, `FIGURES`, `TERM = "DAX"`, `SEED0 = 20260616` frozen in `common.py`.
- `stimuli.json` sha256: `432cb57d4aeefea62f382923fbc98019a184bd1e62879956edcd0e3dd944ff71`
  *(orchestrator: confirm this matches `python3 build_trials.py` output before freezing.)*

## Idealized-reader fixtures (run, no API — the GO-discipline)

`python3 fixtures/make_fixtures.py` builds the frozen stimuli through the real
`build_trials.build()` and six synthetic raw sets; **all asserts PASS**:

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
manipulation gate refuses to read a SPONT null as the A-null unless on-demand comprehension is
demonstrated in this very instrument. These are synthetic and are never findings.

## Anchor

`anchor: internal-contrast-only` (ratified 2026-06-16). Within-model behavioural contrast over
byte-identical content; **no human-comparison claim**. (No in-repo human resource grounds human
order-/path-sensitivity at this grain — Brennan & Clark report an order-*insensitive* statistic —
and none is owed because no human contrast is asserted; binding carry-forward 5.)

## Spend (frozen gate)

Billed `usage.cost` only (never rate-card). Per-phase ledger; every API phase pre-checks
ledger-total + projected ≤ **$0.50** hard stop. Pre-flight estimate (per B's measured
~$0.00033/call over 96 calls = $0.0529): liveness ≈ $0.002; full 160 calls ≈ **$0.05–0.10** →
inside the $0.50 stop and the $5.00/day cap (day total going in: $0.053). Record actuals in
`config/budget.md`.

## Execution order (after critic GO)

```
python3 fixtures/make_fixtures.py   # no API — asserts PASS (already run at build)
python3 build_trials.py             # no API — stimuli.json + sha256
# ORCHESTRATOR: apply critic fixes; confirm sha256; freeze PREREG-draft.md -> PREREG.md; commit
python3 probe.py liveness           # 2 calls; both models must parse (on-demand correct = F8)
python3 probe.py full               # 160 calls -> raw/probe-<model>.jsonl
python3 analyze.py                  # no API -> printed verdict + raw/analysis.json
# then: independent post-run verifier reproduces every number from raw, own route.
```
