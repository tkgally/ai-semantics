# NEXT.md

## State

**Session 46 (philosophical, 2026-06-19 UTC / 2026-06-20 JST) is landed and squash-merged to `main`.**
A $0 writing session that **discharged the carried-over grounding unit**: it folded
[`source/li-2024-cot-serial`](wiki/base/sources/li-2024-cot-serial.md) (catalogued session 43) into the **central argument**
of [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) — its "A machine performance/competence
gap" section, which previously cited the source only in the *forward notes* while the section itself flagged the
competence/performance frame as lacking outside theoretical support — and into the concept page
[`concept/formal-vs-functional-competence`](wiki/base/concepts/formal-vs-functional-competence.md) (a new "complexity-theoretic
sharpening of the *performance* side" paragraph; the source's `refines` edge now declared from both ends). No probe; **$0 spend**;
day total 2026-06-19 (UTC) **unchanged at ≈$3.08 of $5.00**.

The fold is tightly scoped and independently reviewed: every Li et al. quote (the verbatim-verified abstract strings — "CoT
empowers the model with the ability to perform inherently serial computation…", "can only solve problems in TC^0 without CoT",
"with T steps of CoT" / "can solve any problem solvable by boolean circuits of size T", "the composition of permutation groups")
is used at the source's stated strength: a **theory-of-computation result about idealized transformers**, grounding the
serial-computation mechanism's *plausibility*, **not** the panel's internals, licensing **no** human comparison. The cited result
stays THIN / `internal-contrast-only`. The adversarial reviewer's one SHOULD-FIX was applied (an "exact object" over-identification
softened to "same *class* of object … the paper's example is the asymptotic `S_5`, not the project's finite stimuli").

senselint **0 errors**; linkify clean. Website (`docs/`): journal session-46 entry + home status block + "latest" entry; no
finding changed (this is method-essay grounding), so `findings.html`/`plans.html` untouched.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). This session opened **no**
decision (the source fold is within-frame: it cites an already-catalogued theory source at its stated strength, no human anchor or
operationalization owed). Apply any Tom override first.

**Track lean:** recent tracks ran phil(43) → emp(44) → emp(45) → **phil(46)**. Either lean is defensible next; the empirical
composition line has a clear *un-built* next step (below), so an **empirical build session is the natural pick** unless a sharper
philosophical unit is ready. Candidates, either track:

1. **EMPIRICAL — deeper-still (≥4-move) composition (the priority axis).** The only remaining way to hunt a **channel-controlled**
   composition bound: [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) trigger-(b) ("a
   serial-computation negative that *survives* a widened channel") is **still open** — tested at depth 3 and did **not** fire (all
   three RESPECTS-ORDER on the working surface). Build cost grows: the competing-reader set expands with depth; use the
   generic-permutation + brute-forced `assert_balance` template from session 45 (the dihedral STEP/FLIP family collapses past two
   moves). K=6 is likely too small to strict-isolate at 4 moves — probably needs K≥7/8. **Budget a dedicated build session with its
   own independent pre-run critic.** Pre-flight: a 4-move run will cost more than the ~$0.80 three-move run (deeper CoT); estimate
   before launching and check the UTC-day ledger in [`config/budget.md`](config/budget.md). Other composition axes if a 4-move build
   is too heavy: **partially-conflicting refinements**, **image referents**, **cross-family dyads**.

2. **PHILOSOPHICAL — catalogue an open-access `wanted.md` source, or spawn a warranted essay/conjecture.** Fetchable P1/P2 items
   remain in [`wiki/base/wanted.md`](wiki/base/wanted.md) (e.g. the relational anchors Clark & Wilkes-Gibbs 1986 / Pickering &
   Garrod 2004; the still-uncatalogued Grindrod 2026 / Sterken–Cappelen chapter). Catalogue only if a finding will lean on it —
   avoid padding. The li-2024 grounding unit is now **fully discharged**; do not re-do it.

   Grammar reserve: the AANN/CxG cancel-direction Option-B held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md) needs a
   fresh human anchor first.

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). This session opened none.

## Standing-override notes (for Tom, if he looks)

- This was a short philosophy/writing session: it took an outside computer-science proof the project had filed a few sessions ago
  (which shows mathematically *why* letting a model write out its working unlocks step-by-step reasoning it can't do "in one shot")
  and wired it into the **core** of the project's own method essay on that lesson — the part of the argument that had still been
  noting the support was missing — plus the relevant reference page. The edits were kept narrow and an independent check verified
  every quotation word-for-word, confirmed the proof is correctly described as being about idealised model designs (not the actual
  systems the project tests) and makes no comparison to people, and caught one over-strong phrase (now fixed). No experiment, no new
  claim, no spending; the day's running total is unchanged at ≈$3.08 of the $5.00/day cap.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions changelog at
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day **UTC** — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe (the JST clock can read a day ahead of the UTC budget day; 2026-06-19 UTC
day total = **≈$3.08**; this session added **$0**). End squash-merged to `main`, website updated. **No decision is open.** Tracks
ran phil(43) → emp(44) → emp(45) → **phil(46)**; the **≥4-move composition build** is the priority un-built empirical step (the
trigger-(b) channel-*controlled* bound is still the one open contrast on the composition line — negative at depth 3). The
composition witness is a **THIN capacity** over **three** axes (operation pair, grid size, depth), still **negative on
constitution**, still **no** channel-controlled bound found. Every composition probe **must use a working surface**. **Rung (iii)
stays documented structurally closed for text-only stimuli.** The methodological spine has **six** essays (undischargeable-negative,
witness-seeking-economics, capability-split, transcript-ceiling, floor-is-not-a-ceiling, output-channel-confound — the last now
carrying the li-2024-cot-serial theory grounding in its central section).
