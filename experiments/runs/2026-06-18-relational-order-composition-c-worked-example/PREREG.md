# PREREG — WORKED-EXAMPLE-SCAFFOLD WITNESS-SEEKING order-sensitive composition probe

## What this is (witness-seeking on the CHAINING axis — the axis the figure-to-figure run LOCALIZED)

The Option-C run ([`2026-06-18-relational-order-composition-c`](../2026-06-18-relational-order-composition-c/),
K=6) found a **split**: claude RESPECTS-ORDER at ceiling; **both** gemini (DIRECT 0.583) and gpt
(DIRECT 0.194) **failed the on-demand DIRECT gate** (< 0.80) → UNINTERPRETABLE. Two easings have since
failed to find a witness:

- **K=6→K=4 state-space** ([`…-k4`](../2026-06-18-relational-order-composition-c-k4/)) — **OFF-signature**
  (per [`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md));
  split survived (gemini DIRECT 0.594, gpt 0.438).
- **figure-to-figure rendering** ([`…-fig`](../2026-06-18-relational-order-composition-c-fig/)) — the
  **on-signature read-off** easing; split survived (gemini DIRECT 0.656, gpt 0.250). The decisive
  detail: even when **told the order** on the DIRECT arm, **gpt applied only one of the two moves
  65.6% of the time** (gemini 21.9%; claude 0%). So the residual difficulty is **not** the per-move
  read-off (the figure-maps removed it) but **chaining itself** — holding two operations and applying
  **both** in sequence.

The fig-run result and `essay/witness-seeking-economics` name the two un-eased on-signature axes: a
**worked-example scaffold** (demonstrate that both stamped moves must be applied) and **fewer chaining
steps**. This probe eases the **first** of those. It is the **first easing of the chaining axis** the
fig run implicated — a **new axis** (the three prior runs eased state-space and read-off, never
chaining), so its expected information is not the diminished value of re-easing an exhausted axis.

## The single manipulated variable = a WORKED EXAMPLE (within-trial comparison)

The underlying trials are **byte-identical to the K=4 / figure-to-figure runs**. `build_trials.py`,
`SEED0 = 20260619`, the 96 records/model (64 COMP + 32 DIRECT), the geometry, the shortcut-proofing
asserts, `analyze.py`, the thresholds, and the verdict map are **all unchanged**, so `stimuli.json`'s
sha256 is **identical** (`975e31bc…88ba`). The **figure-to-figure rendering is also unchanged** (each
move an explicit figure→figure table; no positions shown). The **only** change from the fig run is the
insertion of one **worked-example block** (`WORKED_EXAMPLE` in `common.py`) demonstrating how two
moves are combined in sequence: apply the FIRST move to the start, then the SECOND move to the RESULT
of the first. So the cleanest single-variable comparison is **fig-run (no scaffold) → this run
(scaffold)**, on the very same trials, same rendering — isolating the chaining scaffold.

## The critical design constraint (no stamp-resolution leak)

Per NEXT.md and the fig-run reopen condition, the worked example must ease **chaining** **without**
teaching **stamp-resolution** (how to read round stamps to decide which move is first), else it
contaminates the COMP spontaneity measurement. The example therefore:

1. Uses a **disjoint illustrative item set** (colored lights, not the figures) and **disjoint move
   names** (PUSH/TURN, not STEP/FLIP) — so **no trial answer or trial map leaks**.
2. Gives the order **explicitly** ("first PUSH, then TURN") — it **never** infers order from round
   numbers (no digits, no "round"/"stamp"/"earlier"/"recent" appear in the block). It teaches only the
   **chaining mechanic** (feed the first move's output into the second), which is exactly the
   single-move-reader failure the fig run implicated; it leaves the **COMP question** (spontaneously
   ordering the two moves by their stamps) **untaught**.

So the **DIRECT** arm (order stated) gets the easing; the **COMP** spontaneity arm does not. The
example arithmetic is self-consistent and correct (PUSH = forward 3-cycle red→green→blue→red; TURN
swaps red↔blue, fixes green; start green → PUSH → blue → TURN → red).

## Frozen stimuli

- `stimuli.json` sha256 = **`975e31bc4f13aff0e220a44cd709a62821f5a0a6a1cc03883a212debf3ef88ba`**
  (**identical** to the K=4 and figure-to-figure runs — the manipulated variable is purely the added
  worked example). Built by `build_trials.py` (no API), seed `SEED0 = 20260619`. 96 records/model
  (64 COMP + 32 DIRECT), **3 models → 288 finding-bearing calls**.

## Witness logic (symmetric, frozen)

- **WITNESS** (gemini/gpt clear DIRECT ≥ 0.80 under the scaffold where they failed without it):
  attributes the fig-run failure to the **chaining-demonstration gap** — showing that both moves must
  be applied in sequence let them compose on demand; re-opens the COMP order question for them. Fires
  [`essay/capability-split`](../../../wiki/findings/essays/capability-split.md) trigger (b) and
  [`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md) trigger (a).
- **NON-WITNESS** (DIRECT still fails with the scaffold): the composition inability is robust even to
  a worked demonstration of chaining — a strong on-signature bound that further localizes the
  difficulty and warrants **updating the witness-search suspension note** — **not** a closure (a
  behavioral negative is never closed; [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md)).
- **claude = POSITIVE CONTROL**: should still clear DIRECT (and ideally RESPECTS-ORDER); a claude
  failure would mean the scaffold broke the instrument, not that the others are limited.

The **DIRECT gate is the empirical arbiter of "easier"** — the easiness is measured, not assumed.

## The binding adjudication (carried over unchanged, biased AGAINST the rich reading)

An operation-order gap here is **THIN** (the stamped move-list and the maps are in the record;
single-reader-recoverable). A RESPECTS-ORDER positive is a thin **"respects operation order"** finding
— **NOT** rung (iii) / constitution. The rich-side rung (iii) is documented **structurally closed**
for text-only stimuli. Both verdicts thin.

## Pre-registered thresholds (frozen, byte-identical to K=4 / K=6 / fig — not tuned)

- `PRINT_CEILING = 0.50` — print-order / canonical-order reader's COMP score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.
- `POS_CHANCE = 1/K = 0.25` (figure-identity chance; track-position picker moot — no positions shown).

## Verdict map (frozen, per model — identical to K=4 / K=6 / fig)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

## Shortcut-proofing (inherited unchanged from the byte-identical trials)

`build_trials.assert_balance` (PASS) + `fixtures/make_fixtures.py` (ALL ASSERTS PASS): target figure
uniform (identity picker = 1/K); print-order & both canonical-order readers = exactly 0.50;
start/single-move/reversed-order readers = 0; frequency flat; only genuine stamp-order composition
yields RESPECTS-ORDER. The worked example adds **no** trial information (disjoint items/moves), so
every idealized reader's score is unchanged; `analyze.py` is byte-identical and rendering-invariant.

## Spend (frozen)

Pre-flight ≈ **$0.40 billed** (288 calls; the fig run billed $0.366 with figure-map prompts; the added
worked example lengthens every prompt by ~150 tokens, so budget a touch higher). `HARD_STOP_USD = 0.60`
on projected total. Record actual `usage.cost` after. Day total 2026-06-18 before this run ≈ **$0.986**
of $5.00; projected after ≈ **$1.39**.

## Anti-cheat

The verdict map is symmetric and pre-registered; a non-witness is fully reportable and a witness
re-opens the COMP question; **neither reaches rung (iii)** (adjudicated thin before the run). No
threshold may be retuned after seeing data. The instrument changes **only** by the added worked example
(same sha trials, same fig rendering). `anchor: internal-contrast-only`; **no human-comparison claim.**

## Independent pre-run critic

**GO** (fresh independent agent, 2026-06-18, before any finding-bearing call). The critic recomputed
everything from the code and text without trusting the run's claims:

- **Freeze integrity — CONFIRMED.** `stimuli.json` sha256 (rstrip-newline, as `_require_frozen`
  computes) = `975e31bc…88ba`; **byte-identical** to the `-fig` sibling (`cmp` clean);
  `build_trials.py`/`analyze.py`/`fixtures/make_fixtures.py`/`probe.py` all byte-identical to `-fig`;
  rebuilding from `build()` regenerates the exact sha from scratch.
- **Geometry, recomputed from scratch — 0 mismatches.** STEP/FLIP do not commute at any of the 4
  starts; re-derived target/swapped/step1/flip1/start/op_lo/op_hi for all 96 records (0 mismatches);
  all **32/32 DIRECT** solvable; subset counts 64 COMP + 32 DIRECT.
- **Rendering, traced from prompt text only — 0 position leaks.** Parsed the STEP/FLIP figure→figure
  tables back out of all 96 prompts; stamp-order composition lands on `target_shape` for all 96;
  **0 "Position" occurrences**; DIRECT query states the order and matches stamp order.
- **The key check — worked example — CLEAN on all four sub-checks.** (a) No trial leak (zero whole-word
  trial figures or move names; disjoint red/green/blue lights + PUSH/TURN); (b) **no stamp-resolution
  teaching** — order given explicitly, no digits / "round" / "stamp" / "earlier" / "recent" in the
  block, so the COMP spontaneity arm stays uncontaminated (the critical property); (c) arithmetic
  correct and self-consistent (PUSH(green)=blue, TURN(blue)=red; start/intermediate/final all
  distinct); (d) single variable — `common.py` diff vs `-fig` shows the only functional prompt change
  is the inserted `WORKED_EXAMPLE` block (one line in `build_user`), the fig rendering unchanged.
- **Shortcut-proofing — ALL FIXTURE ASSERTS PASS** (genuine stamp-order → RESPECTS-ORDER; print/both
  canonical = 0.50; identity/position = 1/K; any DIRECT-failing reader → UNINTERPRETABLE); the disjoint
  worked example adds no new shortcut.
- **Thresholds untuned** (DIRECT_FLOOR=0.80, PRINT_CEILING=0.50, POS_CHANCE=0.25, K=4 — byte-identical
  to `-fig`/`-k4`).
- **Governance — no new decision owed.** A presentation/scaffold easing within the already-ratified
  Option-C / `internal-contrast-only` frame (byte-identical trials, unchanged geometry/thresholds/
  verdict-map/adjudication, single added variable), consistent with the K=4, figure-to-figure, and
  gpt-extension easings; pre-named in the fig-run reopen condition and `capability-split` trigger (b).
- **Verdict-map symmetry / honesty — CONFIRMED** (symmetric pre-registered map; non-witness reportable;
  internal-contrast-only; no human comparison; thin, never rung-(iii)).

**No BLOCKER, no SHOULD-FIX**; one NIT (the run dir is untracked in git — expected for a fresh run).
The probe is clear to proceed to finding-bearing calls.
