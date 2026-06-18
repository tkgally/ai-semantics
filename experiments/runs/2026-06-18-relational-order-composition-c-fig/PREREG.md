# PREREG — FIGURE-TO-FIGURE WITNESS-SEEKING order-sensitive composition probe

## What this is (witness-seeking on the IMPLICATED axis)

The Option-C run ([`2026-06-18-relational-order-composition-c`](../2026-06-18-relational-order-composition-c/),
K=6) found a **split**: claude RESPECTS-ORDER at ceiling; **both** gemini (DIRECT 0.583) and gpt
(DIRECT 0.194) **failed the on-demand DIRECT gate** (< 0.80) → UNINTERPRETABLE. The first easing
([`2026-06-18-relational-order-composition-c-k4`](../2026-06-18-relational-order-composition-c-k4/))
shrank the **state space** K=6→K=4 and the split **survived** (gemini 0.594, gpt 0.438 — still
sub-gate). [`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md):
that easing was **off-signature**. The two failing models' error signature is **single-move readers**
— they apply only **one** of the two stamped moves (gpt's K=6 errors were single-move-dominated). The
implicated axis is therefore **chaining / per-move computation**, not track length. This probe eases
**that** axis, exactly as [`essay/capability-split`](../../../wiki/findings/essays/capability-split.md)
trigger (b) and NEXT.md name it: "a **figure-to-figure** move design (DAX changes directly to another
named figure via a printed map — **no position↔figure read-off**, the layer the single-move-reader
failure implicates)."

## The single manipulated variable = the RENDERING (a within-trial comparison)

The underlying trials are **byte-identical to the K=4 run**. `build_trials.py`, `SEED0=20260619`, the
96 records/model (64 COMP + 32 DIRECT), the geometry, the shortcut-proofing asserts, `analyze.py`, the
thresholds, and the verdict map are **all unchanged**, so `stimuli.json`'s sha256 is **identical** to
the K=4 run. The **only** change is the prompt rendering in `common.py`:

- **K=4 (positional):** showed a TRACK ("Position 1: a triangle …") and described each move as
  relative positional **arithmetic** ("moved one position toward the back … wraps around"; "moved to
  its mirror position"). The model had to read off figure↔position, do the arithmetic, and read back.
- **THIS (figure-to-figure):** shows **no positions**. Each move is an explicit **figure → figure
  lookup table** ("Move STEP: a triangle becomes a circle, a circle becomes a square, …"), derived
  directly from each record's `track`. Composing the two moves is two table look-ups; the
  position↔figure read-off is removed.

So this is the **same 96 trials presented two ways** — the cleanest possible attribution of any
DIRECT-gate change to the easing.

## Frozen stimuli

- `stimuli.json` sha256 = **`975e31bc4f13aff0e220a44cd709a62821f5a0a6a1cc03883a212debf3ef88ba`**
  (**identical to the K=4 run** — the manipulated variable is purely the rendering).
- Built by `build_trials.py` (no API), seed `SEED0 = 20260619`. 96 records/model (64 COMP + 32
  DIRECT), **3 models → 288 finding-bearing calls**.

## Witness logic (symmetric, frozen)

- **WITNESS** (gemini/gpt clear DIRECT ≥ 0.80 under figure-maps where they failed at K=4 positions):
  attributes the K=4 failure to the position↔figure read-off / per-move computation — the
  on-signature easing **worked**; re-opens the COMP order-sensitivity question for them. Fires
  [`essay/capability-split`](../../../wiki/findings/essays/capability-split.md) trigger (b).
- **NON-WITNESS** (DIRECT still fails under figure-maps): the composition inability is robust to
  removing the positional read-off too. Per
  [`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md)
  this is the **first genuinely on-signature** bound on the split (the easing eased the *implicated*
  axis), and warrants a **witness-search suspension note** (axes eased / implicated-but-un-eased /
  reopen condition) — **not** a closure (a behavioral negative is never closed;
  [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md)).
- **claude = POSITIVE CONTROL**: should still clear DIRECT (and ideally RESPECTS-ORDER); a claude
  failure would mean the figure-map rendering broke the instrument, not that the others are limited.

The **DIRECT gate is the empirical arbiter of "easier"** — the easiness is measured, not assumed.

## The binding adjudication (carried over unchanged, biased AGAINST the rich reading)

An operation-order gap here is **THIN** (the stamped move-list and the maps are in the record;
single-reader-recoverable). A RESPECTS-ORDER positive is a thin **"respects operation order"** finding
— **NOT** rung (iii) / constitution. The rich-side rung (iii) is documented **structurally closed**
for text-only stimuli (a transcript IS a final content+stamps record). Both verdicts thin.

## Pre-registered thresholds (frozen, byte-identical to K=4 / K=6 — not tuned)

- `PRINT_CEILING = 0.50` — print-order / canonical-order reader's COMP score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.
- `POS_CHANCE = 1/K = 0.25` (figure-identity chance; the track-position picker is moot — no positions
  are shown).

## Verdict map (frozen, per model — identical to K=4 / K=6)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

## Shortcut-proofing (inherited unchanged from the byte-identical K=4 trials)

`build_trials.assert_balance` (PASS): target figure uniform (identity picker = 1/K = 0.25); print-order
& both canonical-order readers = exactly 0.50; start / single-move / reversed-order readers = 0;
frequency flat. `fixtures/make_fixtures.py` (**ALL FIXTURE ASSERTS PASS**): only genuine stamp-order
composition yields RESPECTS-ORDER; every print/canonical reader scores 0.50 on COMP; every
identity reader 1/K; any reader failing on-demand → UNINTERPRETABLE. The rendering is an
**information-preserving re-presentation** of the same trials (the maps are derived from `track`):
every idealized reader has an identical-scoring figure-table twin, and the track-position picker
simply **vanishes** (no positions shown), which only strengthens the proofing. `analyze.py` is
byte-identical to the K=4/K=6 runs.

## Spend (frozen)

Pre-flight ≈ **$0.30 billed** (288 calls; K=4 positional billed claude $0.199 / gemini $0.052 / gpt
$0.030 = $0.281; figure-map prompts are slightly longer, so budget a touch higher).
`HARD_STOP_USD = 0.60` on projected total. Record actual `usage.cost` after. Day total 2026-06-18
before this run ≈ **$0.620** of $5.00; projected after ≈ $0.91.

## Anti-cheat

The verdict map is symmetric and pre-registered: a non-witness (DIRECT still fails) is the first
on-signature bound and is fully reportable; a witness re-opens the COMP question; **neither reaches
rung (iii)** (adjudicated thin before the run). No threshold may be retuned after seeing data. The
instrument changes **only** by rendering from the byte-identical K=4 trials (same sha). `anchor:
internal-contrast-only`; **no human-comparison claim**.

## Independent pre-run critic

**GO** (fresh independent agent, 2026-06-18, before any finding-bearing call). The critic reproduced
the freeze (the fig-dir `stimuli.json` sha = `975e31bc…88ba`, **byte-identical** to the K=4
`stimuli.json`; `build_trials.py`/`analyze.py`/`fixtures/make_fixtures.py` byte-identical to K=4; all
fixture asserts PASS). It **recomputed the geometry from scratch** (did not trust the run's ops):
STEP/FLIP do not commute at any of the 4 starts; re-derived target/swapped/single-move/start ends for
all 96 records (**0 mismatches**); valid-config exclusion holds for every record; target figure and
track-position uniform; only stamp-order beats 0.50 (print-order / both canonical = 0.50; const-figure
/ track-position = 0.25; single-move / start / swapped = 0).

**The key new check — the figure-to-figure rendering — passed cleanly.** Parsing the move tables back
**out of the rendered prompt text** (trusting only text): the STEP/FLIP tables are the correct
figure→figure maps derived from each record's `track`, every table a valid bijection (FLIP an
involution, STEP a 4-cycle); listed in **fixed canonical SHAPES order** for all 96 (no positional
leakage); **0 "Position N" leaks across all 96 prompts**; composing the two parsed tables in stamp
order lands on `target_shape` and reversed on `swapped_shape` for **all 96 records** (text-traced).
A 12-strategy new-shortcut hunt at the figure-table level found **only stamp-order = 1.0**; the
track-position picker has **vanished** (no positions shown) — which only strengthens the proofing.
DIRECT solvability (apply the two named tables in the stated order) = **32/32**.

**The easing is on-signature** (removing the position↔figure read-off eases the per-move /
chaining layer the single-move-reader signature implicates, not an off-signature axis); the DIRECT
gate is a fair measured arbiter; the verdict map is symmetric and honest. **Governance: no new
`wiki/decisions/open/` entry owed** — a rendering-only, byte-identical-trial easing within the
already-ratified Option-C / `internal-contrast-only` frame, the exact "figure-to-figure" easing
pre-named in `capability-split` trigger (b). Thresholds byte-identical (not retuned). **No BLOCKER,
no SHOULD-FIX**; two harmless NITs (a contrast-example "Position 1" in a docstring; the `HARD_STOP_USD`
framing — both correct in context).
