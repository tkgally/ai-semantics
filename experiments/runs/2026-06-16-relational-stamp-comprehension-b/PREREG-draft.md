# PREREG (DRAFT) — relational stamp-comprehension pre-probe (Option B)

**Status: DRAFT. Frozen → `PREREG.md` by the orchestrator ONLY after an independent pre-run
critic returns GO.** `probe.py full` refuses to run until `PREREG.md` exists and records the
frozen `stimuli.json` sha256.

## What this is and why it runs

The ratified design decision
[`decisions/.../relational-v5-text-position-neutralization`](../../../wiki/decisions/resolved/relational-v5-text-position-neutralization.md)
(adopt-default, 2026-06-16 adversarial review: **Option B then A, staged; C the binding
fallback**) requires a cheap **stamp-comprehension pre-probe** to run **before** any
geometry-decoupled chronology arm (Option A). The motivating fact is v4's binding scope limit:
both panel models follow physical text-position, and *"position-following here is
indistinguishable from stamp-blindness"* — so a chronology arm cannot be interpreted until we
know whether the models read the round **stamp** as a recency value **at all**.

This probe answers exactly that, and nothing more. It is a **gate**, not a relational result.

## Hypotheses / verdict (frozen)

Per model, over byte-identical stamped records with physical line-position **neutralized by
balanced rotation** (so only the stamp value disambiguates):

- **PASS (comprehends the stamp value)** iff `accuracy ≥ PASS_FLOOR (0.80)` **AND** the Wilson
  95% lower bound `> POS_CHANCE (1/K = 0.25)`. *(The CI condition is conservative belt-and-suspenders
  — at acc = 0.80 the Wilson lower bound is already ≈ 0.66 > 0.25, so the floor implies it; it is
  retained for symmetry with the FAIL-side diagnostic, not because it does independent work.)*
- **FAIL (stamp-blind on this instrument)** otherwise.

Routing (binding, carried from the ratification):
- A model that **PASSES** earns an Option-A position-rotated, stamp-gated chronology arm
  (a later phase; built and certified separately).
- A model that **FAILS** → v4's position-following is explained as stamp-blindness for it.
- **BOTH** panel models FAIL → the relational-history line **closes at Option C**. The stamp
  format is **NOT** retuned and B is **NOT** re-run to chase a pass (anti-cheat carry-forward:
  *"do not retune the stamp format until something positive appears"*).

## Instrument (frozen)

- Panel: **claude + gemini** (A-eligible relational panel carried from v4; gpt was dropped from
  the finding-bearing relational panel for a stimulus-generation reason, not comprehension —
  not re-opened here).
- Each record: **K=4** lines. Each line couples a round **stamp** to a frozen **nonce**
  convention: `- Round {r}: we agreed to call it "{NONCE}".` Round values are drawn from frozen
  **non-contiguous** quadruples (e.g. `{2,4,7,9}`), so the answer requires reading the stamp
  *value*, not a default "round 1 = first" assumption.
- Two query types, within-subject: **MR** ("agreed MOST RECENTLY / latest round" → max-round
  nonce) and **LR** ("agreed EARLIEST / first round" → min-round nonce). Both directions force
  use of the stamp as an ordered scale (a model that merely fixates a salient number won't get
  *earliest* reliably).
- **Position AND lexical neutralization (balanced-block design).** 12 distinct present-sets
  (4-nonce subsets, each nonce in exactly 6 sets); each set yields K=4 records under a Latin
  square so that, within a set, the **correct nonce cycles through all 4 members once** AND the
  **correct line's physical slot cycles through all 4 positions once** ⇒ **48 records/model**,
  24/query. Round values and nonce identities are independent of physical position (asserted).
  Two shortcut bounds are **proven at build** (not just claimed): (a) every constant-physical-slot
  strategy scores **exactly 1/K = 0.25**; (b) **every one of the 8! fixed nonce-preference
  orderings** also scores **exactly 1/K** (because, conditional on the present-set, the correct
  nonce is uniform over its members). So no position or lexical shortcut can exceed 0.25 — only
  reading the stamp **value** as recency can clear the 0.80 floor. *(This balanced-block design
  replaced an earlier unconstrained-nonce build after the 2026-06-16 pre-run critic found a
  residual nonce-identity cue worth ~0.46; the fix drives every lexical shortcut to exactly 1/K.)*
- Forced single-label elicitation; strict parse; **a `finish_reason == "length"` reply is never
  parsed**; one stern retry on parse-fail then NA. `reasoning: minimal` on gemini (cost caveat).
- INTRO is **neutral**: it states that a higher round number means more recently and that lines
  are not necessarily in round order, but does **not** instruct the model to weight recency or
  position — whether it reads the stamp as recency is what is measured.

## Pre-registered constants (frozen)

- `K = 4`; `QUERIES = ["MR","LR"]`; `N_BLOCKS = 12` ⇒ 48 records/model, 96 finding-bearing
  calls total.
- `PASS_FLOOR = 0.80`; `POS_CHANCE = 0.25`. Rationale: a stamp-reader is near 1.0 and **every**
  position or lexical shortcut scores **exactly 0.25** (proven at build over all K! slot
  strategies and all 8! nonce orderings), so 0.80 cleanly separates comprehension from any
  shortcut, with margin for occasional slips.
- `ROUND_SETS`, `NONCES`, `SEED0 = 20260616` frozen in `common.py`.
- `stimuli.json` sha256: `bccd3be6d5c57707f535aa998c380310fedb7445341bae7532cbb71c221da6b3`
  *(orchestrator: confirm this line matches `python3 build_trials.py` output before freezing.)*

## Idealized-reader fixtures (run, no API — the GO-discipline)

`python3 fixtures/make_fixtures.py` builds the frozen stimuli through the real
`build_trials.build()` and three synthetic raw sets; all asserts PASS:
- `raw_stamp` (perfect stamp-reader) → **PASS/PASS**, acc 1.000.
- `raw_lastpos` (always physically-last) → **FAIL/FAIL**, acc **exactly 0.250** (= 1/K).
- `raw_firstpos` (always physically-first) → **FAIL/FAIL**, acc **exactly 0.250**.
So the verdict cannot be passed by a position heuristic; only stamp-value reading clears 0.80.

## Anchor

`anchor: internal-contrast-only` (ratified 2026-06-16). Within-model behavioural check over
byte-identical content; **no human-comparison claim**. (No in-repo human resource grounds
stamp-/order-comprehension; none is owed because no human contrast is asserted.)

## Spend (frozen gate)

Billed `usage.cost` only (never rate-card). Per-phase ledger; every API phase pre-checks
ledger-total + projected ≤ **$0.50** hard stop. Pre-flight estimate (conservative, per v4/conative
ledger per-call rates ~$0.0002–0.0008): liveness ≈ $0.002; full 96 calls ≈ **$0.02–0.08** →
trivially inside the $0.50 stop and the $5.00/day cap. Record actuals in `config/budget.md`.

## Execution order (after critic GO)

```
python3 fixtures/make_fixtures.py   # no API — asserts PASS (already run at build)
python3 build_trials.py             # no API — stimuli.json + sha256
# ORCHESTRATOR: apply critic fixes; confirm sha256; freeze PREREG-draft.md -> PREREG.md; commit
python3 probe.py liveness           # 2 calls; both models must parse (correct = DRISBO)
python3 probe.py full               # 96 calls -> raw/probe-<model>.jsonl
python3 analyze.py                  # no API -> printed verdict + raw/analysis.json
```
