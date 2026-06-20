# PREREG — CROSS-FAMILY (heterogeneous-operation) order-sensitive composition, POSITION-ANCHORED + MATCHED-PAIR (Option-C generality axis)

**Run:** `2026-06-20-relational-order-composition-cross-family`
**Frozen stimuli:** `stimuli.json`
**rstrip-sha256 = `f8d70547f55393de6f9a6652b4dde9122df3d667fefebf5091bc86e7661c8b85`**
(the `probe.py full` gate refuses to run unless this exact sha is recorded here)

> **Status at freeze: design complete, balance + fixtures certified, awaiting the FINAL independent
> pre-run critic GO.** No finding-bearing call may run before the critic returns GO.
>
> **Design history (disclosed — three pre-run NO-GOs, each fixed).** (1) An **object-anchored** design
> (readout = "what color is the moved token DAX?") was NO-GO'd: a stamp-using one-op reader
> `apply-only-earlier` scored 0.75, because following the *moved* token makes the spatial op a
> relabeling under which the attribute op is inert in most cells. (2) A structural-verification pass
> refuted the tempting "cross-family is unbuildable" closure and supplied the fix: **anchor the readout
> to a FIXED spot** ("what color is on the DAX spot?"). (3) The position-anchored design was then
> NO-GO'd for a *different* reason: the visible **swap-pair geometry was confounded with the cell**
> (`swap_pair × stamp_first` 12:6), and since the SWAP move names its spots, a geometry-keyed reader
> scored up to 0.83 without reading stamps. **This design fixes that with a MATCHED-PAIR construction**
> (below), which makes stamp order independent of *all* visible geometry by construction.

## The question (precise)

Every prior Option-C run composed operations of the **same family** (position permutations as opaque
figure→figure tables). [`claim/relational-order-sensitive-reassignment`] scope limit 2 names the
untested axis verbatim — *"generality (image referents, cross-family dyads) is untested."* **This probe
composes two TRANSPARENTLY HETEROGENEOUS, non-commuting operations — one SPATIAL (a swap), one
ATTRIBUTE (a recolor) — and asks whether the working-surface composition capacity extends to binding
two updates of *different kinds* in stamp order.**

## Operations + position-anchored readout

A row of `K=4` spots, each holding a colored token. One spot `s` is nicknamed the **"DAX spot"** (the
readout). **SWAP** names two spots whose tokens exchange places (color travels); **RECOLOR** names one
spot whose token is repainted. The DAX spot `s` is one of the two swap spots and the RECOLOR targets
one of them, so **both ops are live at the readout** and **do not commute** on the color at `s`. Each
record stamps the two ops with two rounds; the true composition applies them in **stamp order**.

- **COMP (headline, spontaneous):** op-lines shown, query asks only the color on the DAX spot — does
  **not** state the order.
- **DIRECT (on-demand gate):** query states the order. Gate `direct_acc ≥ 0.80`; else UNINTERPRETABLE.

## Why it is shortcut-clean: the MATCHED-PAIR construction

The four logical **cells** = readout_type {`SAME` = DAX spot is the recolor target; `DIFF` = DAX spot
is the other swap spot} × stamp_first {SWAP, RECOLOR}. The DAX spot's own initial color is always
overwritten, so the answer is always one of {`Cr` (recolor color), `C_oth` (the other swap spot's
initial color)} — `Cr` in {(SAME,SWAP),(DIFF,RECOLOR)}, `C_oth` in {(SAME,RECOLOR),(DIFF,SWAP)}.

A **unit** fixes the *entire visible scene* — the swap pair (a,b), the readout spot s, the recolor
target m, the full initial coloring, the recolor color, the round pair {r1,r2}, and the physical print
order of the two op-lines — and emits a **matched pair** of records that differ **only in which op
carries the earlier round stamp** (SWAP-first vs RECOLOR-first), with **opposite answers**. The two
prompts of a pair are therefore byte-identical except that the two round numbers are swapped between
the SWAP and RECOLOR lines. Consequently **stamp order is independent of everything visible except the
round stamps themselves**: any reader that does not read the per-op round stamps — including one keyed
on the swap-pair or any visible-geometry signature — gets exactly one record of each pair right and is
pinned at **0.50**. Only reading the round stamps and applying the two ops **in stamp order** clears
0.50 (= 1.0). This is certified two ways in `assert_balance`: (i) a **geometry-oracle** upper bound
(group by the full visible-minus-stamps signature, take the best constant guess per group) = **0.5000**;
(ii) the brute-forced non-composing reader family (single-op, stamp-using partials, fixed/reverse/print
orders, fixed-spot, const) all ≤ 0.50 (worst = 0.5000; `apply-only-earlier` = 0.25).

## Design parameters (frozen)

- `K = 4` spots; answer space = **6 colors**; const-color = 1/6. Recolor color disjoint from every
  initial color; the DAX spot's own initial color is never the answer.
- **16 visible geometries** (4 swap pairs × 4 (s,m) on the swap spots) → perfectly balances swap pair,
  readout spot `s` (4× each), and readout_type (8 SAME / 8 DIFF).
- COMP: 16 geometries × 3 color-reps × **matched pair (2 orders)** = **96 records/model**.
- DIRECT: 16 geometries × **matched pair (2 orders)** = **32 records/model**.
- Total **128 records/model × 3 models = 384 finding-bearing calls.**
- Balance (proven at build): answer color uniform over 6 (16 each); cells / stamp_first / readout_type
  / readout-spot / print-order all balanced; every record order-discriminating (`target ≠ reverse`).
- Working-surface elicitation **held identical** to prior Option-C working-surface runs (`FINAL:` tag,
  `MAX_TOKENS = 1024`, gemini `effort: minimal` held constant, length-truncation never parsed,
  target-blind parser).
- Panel: claude = positive control; gemini + gpt = the cross-family targets.
- Pre-flight cost: depth-2, short CoT; estimate **≈ $0.7–1.0**; pre-registered **hard stop $1.50**.

## Frozen verdict map (identical to every prior Option-C run)

- `UNINTERPRETABLE` : `direct_acc < 0.80`.
- `RESPECTS-ORDER` : DIRECT gate passed AND COMP target-rate Wilson-95 LB > 0.50.
- `ORDER-BLIND-OR-WEAKER` : DIRECT gate passed AND COMP target-rate Wilson-95 LB ≤ 0.50.

## ADJUDICATION (binding, before the run, biased AGAINST the rich reading)

Per [`decisions/resolved/relational-rung-iii-path-dependence`]: an operation-order gap here is
**THIN** (the stamped op-list, spots, and colors are in the record; single-reader-recoverable).
RESPECTS-ORDER is reported as a thin **"respects operation order" / cross-family-composition** finding,
**never** rung (iii). The rich-side rung (iii) program stays documented **structurally closed for
text-only stimuli**. `anchor: internal-contrast-only`; **no human-comparison claim.**

## No new decision is owed (surfaced for the critic to gate)

The ratified Option-C decision adopted **"non-commuting operation semantics"** *agnostic to which
operations realize them* and **did not freeze the operation kind**. Like the alt-pair (D4→A4), grid
size, and move count — none of which owed a new decision — the operation-KIND change is the same class
of within-frame variation. **No new `wiki/decisions/open/` entry is owed**; the critic gates this.

## Certifications run at freeze (no API)

- `python3 build_trials.py` → `assert_balance` PASS: 96 COMP + 32 DIRECT; **composer = 1.000**;
  **geometry-oracle = 0.5000**; every brute-forced non-composing reader ≤ 0.50 (`apply-only-earlier`
  = 0.25); all balance checks pass; every record order-discriminating. Frozen sha above.
- `python3 fixtures/make_fixtures.py` → ALL FIXTURE ASSERTS PASS: only a genuine stamp-order composer
  → RESPECTS-ORDER (1.0); report-Cr / fixed-order / print-order → 0.50; earlier-only → 0.25; all
  ORDER-BLIND-OR-WEAKER; const-color / direct-fail → UNINTERPRETABLE.

## Anchor

`internal-contrast-only`, carried forward and ratified for the Option-C program. Within-model contrast
over balanced/order-permuted content; no human comparison asserted or owed.
