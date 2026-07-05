---
type: result
id: relational-order-composition-c
title: Order-sensitive composition (Option C, non-commuting operations) — across the full three-model panel only claude spontaneously orders two non-commuting moves by their stamps at ceiling; gemini AND gpt cannot compose them on demand (both uninterpretable), so order-sensitive composition is a claude-only capability here; the gap is adjudicated THIN and the rich-side rung (iii) is documented structurally closed for text-only stimuli
meaning-senses:
  - relational
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-18
updated: 2026-07-05
links:
  - rel: depends-on
    target: claim/relational-order-sensitive-reassignment
  - rel: depends-on
    target: result/relational-integration-rung-ii
  - rel: refines
    target: concept/relational-meaning
  - rel: supports
    target: essay/transcript-ceiling
  - rel: supports
    target: essay/update-is-not-constitution
---

# Result: order-sensitive composition (Option C) — a split positive, adjudicated thin, with the rich side documented closed

> **Status: proposed (2026-06-18).** Implements **Option C** (non-commuting operation semantics) of
> the ratified decision
> [`decisions/resolved/relational-rung-iii-path-dependence`](../../decisions/resolved/relational-rung-iii-path-dependence.md),
> under its **binding pre-run adjudication gate**. It tests the gap the rung-(ii) integration result
> explicitly left open — *is the composition itself **order-sensitive** (non-commutative), or only
> survival of a compatible turn (which a commutative conjunction passes equally)?*
> ([`result/relational-integration-rung-ii`](relational-integration-rung-ii.md), scope note 3;
> [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)
> scope limit 2). **Split result, now read across the full three-model panel:** `claude-sonnet-4.6`
> orders two non-commuting moves by their round stamps **spontaneously and at ceiling**
> (RESPECTS-ORDER); **both** `gemini-3.5-flash` **and** `gpt-5.4-mini` **cannot compose the two moves
> even when told the order** (DIRECT gate fails → UNINTERPRETABLE for each). So order-sensitive
> composition is occupied by **claude alone** — a one-of-three capability, not a panel property; two
> separately-trained models cannot even compose two non-commuting moves on demand in this instrument.
> The gap is **adjudicated THIN before the run** (a single reader applies the stamped move-list in
> order and reads off the answer) — reported as *"respects operation order,"* **not** rung (iii). The
> rich-side rung (iii) is documented **structurally closed for text-only stimuli** (the parallel,
> promotable headline). `anchor: internal-contrast-only`; **no human-comparison claim.** (gpt added in
> a later 2026-06-18 session — the generality re-run named by
> [`essay/capability-split`](../essays/capability-split.md) trigger (a); see *Third-model extension*
> below.)

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The "claude-only capability" reading
> below **dissolved the next day**: the elicitation-witness search found a working surface under
> which **all three** models compose the two non-commuting moves —
> [`result/relational-order-composition-c-reasoning-scaffold`](relational-order-composition-c-reasoning-scaffold.md)
> (2026-06-19; split dissolves 3/3). The capability gap was a **channel/format** gap, not a
> competence gap — the mechanism now consolidated in
> [`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md) (s177) and
> recorded on [`essay/capability-split`](../essays/capability-split.md) (trigger (b) FIRED — split
> dissolved). *(Back-annotation: this page's DIRECT-gate numbers under the original terse channel
> stand unchanged; what changed is what they license.)*

## The question (precise)

The relational ladder has two thin rungs: rung (i) order-sensitive **overwrite**
([`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md))
and rung (ii) non-overwrite **integration**
([`result/relational-integration-rung-ii`](relational-integration-rung-ii.md)). But integration was
shown only as **survival** of a compatible earlier turn — its design's constraints are *compatible*,
so a **commutative** conjunction ("DAX is striped AND a triangle") passes it exactly as a genuinely
order-sensitive composition would. The open question, named verbatim in that result's scope note 3:
*"it does NOT test whether the composition is itself order-sensitive (a commutative conjunction
would pass equally)."* This probe makes order genuinely load-bearing: the two turns are
**non-commuting operations**, so two orders of the same move-set reach **different** end states.

## Instrument (frozen; pre-run-critic-gated; adjudicated thin)

Run dir: [`experiments/runs/2026-06-18-relational-order-composition-c/`](../../../experiments/runs/2026-06-18-relational-order-composition-c/).
Design: [`relational-order-composition-c`](../../../experiments/designs/relational-order-composition-c.md).

- **Non-commuting operation semantics.** K=6 distinct figures lie along a stated **track**
  (position 1..6). A coined token **DAX** starts on a stated figure and undergoes **two stamped
  moves** from the dihedral generators of a 6-ring: **STEP** (`p → (p+1)%6`, "one position toward
  the back, wrapping back→front") and **FLIP** (`p → 5−p`, "mirror position": 1↔6, 2↔5, 3↔4). STEP
  and FLIP do **not** commute, so applying them in **stamp order** (lower round first) lands DAX on a
  **different** figure than applying them reversed. The two move-lines are printed in round order in
  **half** the records and reversed in the other half (print order decoupled from stamp order).
- **Two arms.** **COMP** (headline, 72/model): *"Which figure does DAX sit on now?"* — the order is
  **not** stated. **DIRECT** (on-demand gate, 36/model): the order is stated explicitly (*"first …
  then …"*). DIRECT confirms the model **can** compose the two moves in this instrument; if
  `direct_acc < 0.80`, COMP is UNINTERPRETABLE.
- **Shortcut-proof by construction.** Balanced-block roster; all 6 shapes present every record.
  Proven at build, separately per arm: every figure-identity picker and every track-position picker
  scores **1/K = 0.1667**; the **print-order reader and both canonical fixed-order readers** (always
  STEP-then-FLIP; always FLIP-then-STEP) score **exactly 0.50** (print matched to stamp order in half
  the records; true order balanced 6 SF / 6 FS); the **start / single-move (STEP-only, FLIP-only) /
  reversed-order ("swapped") readers score 0** on the target. So **only ordering the two moves by
  their stamps can clear the 0.50 bar.** Six idealized-reader fixtures certify the verdict map.
- **The binding adjudication (decided BEFORE the run, biased AGAINST the rich reading).** An
  operation-order gap here is **THIN**: the stamped move-list is *in the record*, so a single reader
  applies it in stamp order and reads off the answer (single-reader-recoverable). A RESPECTS-ORDER
  positive is therefore a thin *"respects operation order"* finding — **not** promoted to rung (iii) /
  constitution. The rich-side rung (iii) is documented **structurally closed** for text-only stimuli
  (a transcript *is* a final content+stamps record — [`essay/transcript-ceiling`](../essays/transcript-ceiling.md)).
- **Independent pre-run critic + adjudicator GO** (fresh agent): independently enumerated reader
  families (constant-figure 0.167; track-position 0.167; print-order 0.50; both canonical 0.50;
  start / single-move / reversed-order 0.00; *exotic* readers — last-printed-move, higher-stamp-move
  [the rung-(i) recency heuristic], lower-stamp-move — **all 0.00**), confirmed it **could not
  construct any reader beating 0.50 without stamp-order**, ruled the adjudication **THIN**, anti-cheat
  **PASS**, and confirmed no new decision owed (a frozen design under the already-ratified Option-C
  decision and `internal-contrast-only` posture).
- Forced single-figure elicitation; one stern retry then NA; `HARD_STOP_USD = 0.55`.

## The headline (verified — numbers not altered)

| model | DIRECT on-demand acc | COMP target (stamp-order composition) | Wilson 95% | swapped (reversed-order) | start | step-only | flip-only | NA | verdict |
|---|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | **0.861** (31/36) | **1.000** (72/72) | [0.949, 1.000] | 0.000 | 0.000 | 0.000 | 0.000 | 0 | **RESPECTS-ORDER** |
| gemini-3.5-flash | **0.583** (21/36) | 0.319 | [0.223, 0.434] | 0.222 | 0.000 | 0.153 | 0.264 | 0 | **UNINTERPRETABLE** |
| gpt-5.4-mini | **0.194** (7/36) | 0.111 | [0.057, 0.204] | 0.125 | 0.069 | 0.181 | 0.250 | 0 | **UNINTERPRETABLE** |

- **claude — RESPECTS-ORDER.** Its DIRECT on-demand composition passes (0.861 > 0.80), and on COMP it
  recovers the **stamp-order** end figure **every time** (72/72, Wilson LB 0.949 — far above the 0.50
  print/canonical ceiling). The reversed-order ("swapped"), start, and single-move readings are taken
  **zero** times. So claude **spontaneously orders the two non-commuting moves by their round stamps**
  — order-sensitive composition. Its (unrequested) reasoning makes this transparent: it routinely
  writes *"Let me trace the moves in round order"* / *"the moves need to be applied in round order
  (Round 1 first, then Round 6)"* before answering. This fills the integration result's scope-note-3
  gap: the composition is genuinely **non-commutative**, not mere survival.
- **gemini — UNINTERPRETABLE.** Its DIRECT on-demand gate **fails** (0.583 < 0.80): gemini cannot
  reliably compose two non-commuting spatial moves *even when told the order explicitly*. Its COMP
  rate (0.319) is therefore **uninterpretable** — the gate correctly refuses to read it (we cannot
  tell spontaneous order-blindness from inability-to-compose). gemini follows no single shortcut
  cleanly (swapped 0.222, flip-only 0.264, step-only 0.153) — it is simply failing the task.
- **gpt — UNINTERPRETABLE (third-model extension).** Its DIRECT on-demand gate fails even harder than
  gemini's (0.194 < 0.80, Wilson [0.097, 0.350] — the whole CI sits far below the floor): gpt-5.4-mini
  cannot compose two non-commuting spatial moves *even when told the order explicitly*. Its COMP rate
  (0.111) is therefore uninterpretable. The error pattern is diagnostic of the failure mode: the bulk
  of gpt's wrong answers are **single-move readers** (flip-only 0.250, step-only 0.181) — it frequently
  applies only **one** of the two stamped moves, rather than composing both. It answered in strict
  forced format on all 108 records (0 NA, 0 retried, 0 truncation), so the low score is a genuine
  composition-ability limit, not a parse artifact.
- **Clean record:** 324/324 answered across the three models, **0 NA, 0 retried, 0 length-truncation**.

**Discipline.** Independent pre-run critic + adjudicator GO (THIN adjudication; reader-family
enumeration; anti-cheat PASS). Independent **post-run verifier** re-derived every stamp-order target
from the geometry by its own route, recomputed every rate from raw with its own parser (0
parse-disagreements on all 216 records), and audited claude's last-line extraction — **REPRODUCED**
(claude COMP 72/72 [0.9493, 1.0]; claude DIRECT 0.8611; gemini DIRECT 0.5833; 0 NA; cost
$0.298353). The verifier's decisive check: on the **reverse-printed** records, claude's reasoning
explicitly re-sorts by round stamp before answering, so the 1.000 is genuine order-sensitive
composition and **not** a print-order shortcut.

## What this shows — and what it does NOT (binding scope)

**Shows (within-model, internal-contrast-only):**

1. **Order-sensitive composition is occupied — by one model.** claude's recovered referent depends on
   the **order** in which two non-commuting operations were applied, spontaneously and at ceiling.
   This is a **stricter** dependence than rung (ii) integration (which a commutative conjunction
   passed equally): claude distinguishes o-lo→o-hi from o-hi→o-lo. It is the first relational evidence
   of genuinely **non-commutative composition** (as opposed to non-commutative *overwrite*, rung i, or
   commutative *survival*, rung ii).
2. **It is still THIN — adjudicated before the run.** The gap is single-reader-recoverable: the
   stamped move-list is in the record, and claude's own reasoning shows it computing a function of
   (start, moves, stamps). It is *"respects operation order,"* **not** rung (iii) path-dependence and
   **not** between-agent constitution.
3. **The rich-side rung (iii) is documented structurally closed for text-only stimuli.** This is the
   **strongest order-load-bearing text design** the project can build (two genuinely non-commuting
   operations), and even a perfect gap here is thin — because a transcript *is* a final content+stamps
   record, so no text stimulus can carry arrival-order surplus *outside* what the record states. Per
   [`decisions/resolved/relational-rung-iii-path-dependence`](../../decisions/resolved/relational-rung-iii-path-dependence.md)
   (§A5) this **documented closure is a fully promotable outcome**, not a failure, and it
   **corroborates** [`essay/transcript-ceiling`](../essays/transcript-ceiling.md) — its **revision
   trigger (a)** (a certified Option-C gap the gate judged *non*-single-reader-recoverable) is **NOT
   activated**: the gate ruled the gap thin, so the ceiling stands.

It does **NOT** show:

- **Not rich constitution, not path-dependence (rung iii).** See point 2; the adjudication settled
  this before any data.
- **Not a both-model finding — and now confirmed not a panel finding** *(under this page's terse
  channel; the s183 update box above records that a working surface later dissolved the split 3/3)*.
  Only claude clears the
  on-demand gate. **Both** gemini and gpt are uninterpretable here (an instrument-capability limit for
  each, not a clean order-blind null). So order-sensitive composition is occupied **by claude alone**
  across the full three-model panel — a **one-of-three** capability, not a property of "the panel" or
  of "LLMs"; generality is bounded, and the single-model positive is weaker than the both-model
  ceilings of rungs (i)–(ii). Running the third model did **not** widen the split toward a panel
  property (the outcome [`essay/capability-split`](../essays/capability-split.md) trigger (a)
  anticipated for a *composing* third model); it **sharpened the claude-only reading** — two
  separately-trained models cannot compose two non-commuting moves on demand in this instrument.
- **Not a single-forward-pass behaviour for claude.** claude **ignored the forced-format
  instruction** and emitted chain-of-thought on ~98/108 records, ending with the answer on the last
  line (which the parser extracted). So "spontaneous" means *claude chose, unprompted, to reason in
  round order* — arguably **stronger** transparency than a single token, but it is reasoned
  composition, not a reflex. (gemini answered in single tokens and got the composition wrong.)
- **Not a human comparison** (`anchor: internal-contrast-only`). No in-repo resource grounds human
  operation-order composition at this grain; none is owed because no human contrast is asserted.

## Honesty box

- **Split verdict, single-model positive (full panel).** claude RESPECTS-ORDER at ceiling (COMP
  72/72, Wilson LB 0.949; DIRECT 0.861); gemini UNINTERPRETABLE (DIRECT 0.583 < 0.80); gpt
  UNINTERPRETABLE (DIRECT 0.194 < 0.80). The positive is **one of three models**, not the panel —
  narrower than rungs (i)–(ii), which both models cleared. Two separately-trained models fail the
  on-demand composition gate.
- **claude emitted CoT despite the forced format.** 98/108 claude replies were chain-of-thought with
  the answer on the final line (non-strict parse). The independent post-run verifier re-derived each
  stamp-order target from the geometry and confirmed the last-line extraction is the genuine final
  answer (not a mid-reasoning shape) and matches the derived target. The result rests on a transparent
  reasoned ordering, not a black-box single token.
- **gemini's failure is a composition-ability limit, not a parse artifact.** gemini gave 108 strict
  single-token answers; its DIRECT errors are genuine wrong figures (verified against the derived
  target). The instrument is simply too hard for it — so it yields no usable order-sensitivity signal.
- **gpt's failure is likewise a composition-ability limit, not a parse artifact.** gpt gave 108 strict
  single-figure answers (0 NA, 0 retried, 0 truncation); its DIRECT errors are genuine wrong figures,
  predominantly **single-move** readers (flip-only 0.250, step-only 0.181) — it applied only one of the
  two stamped moves. The independent post-run verifier re-derived every stamp-order target from the
  STEP/FLIP geometry, re-parsed all 108 records with its own parser (0 disagreements), and confirmed
  the failure is genuine, not formatting noise.
- **Adjudicated THIN; rich side closed by construction.** The decision's gate, applied before the run
  and biased against the rich reading, ruled the gap thin; the rich-side rung (iii) closure for
  text-only stimuli holds regardless of the verdict. A null (had both models been order-blind) would
  have been equally promotable.
- **One operationalization.** STEP/FLIP on a 6-track, two moves, two rounds, text figures. Generality
  (other operation pairs, >2 moves, image referents, cross-family dyads, a panel that can all compose)
  untested. The third-model extension tested *panel* generality (claude-only confirmed across three
  models); the *instrument* generality directions above remain untested.
- **Witness-seeking follow-up (no witness).** A later 2026-06-18 session ran the
  [`essay/capability-split`](../essays/capability-split.md) trigger-(b) probe — the **same** STEP/FLIP
  pair with the track shrunk **K=6 → K=4** (an easier instrument) — to test whether gemini's/gpt's
  UNINTERPRETABLE here was driven by K=6 difficulty. It was **not**: both still failed the on-demand
  gate at K=4 (gemini 0.594, gpt 0.438; claude still RESPECTS-ORDER), so the two UNINTERPRETABLE
  verdicts **survive halving the instrument** — the claude-only composition reading is bounded from
  below ([`result/relational-order-composition-c-easier-k4`](relational-order-composition-c-easier-k4.md)).
- **Spend.** Original run (claude+gemini): 216 finding-bearing calls + 2 liveness = **$0.29835 billed**
  (`usage.cost`-summed, 0 missing; claude $0.23175, gemini $0.06383, liveness $0.00278). Third-model
  extension (gpt): 108 finding-bearing calls + 1 liveness = **$0.03702 billed** (gpt $0.03663, liveness
  $0.00038; 0 missing). Both inside the $0.55 per-run hard stop; day total 2026-06-18 ≈ **$0.335** of
  the $5.00/day cap.

## Third-model extension (gpt-5.4-mini) — provenance

Run in a later 2026-06-18 session to test the panel generality the honesty box and
[`essay/capability-split`](../essays/capability-split.md) trigger (a) named. Run dir:
[`experiments/runs/2026-06-18-relational-order-composition-c-gpt/`](../../../experiments/runs/2026-06-18-relational-order-composition-c-gpt/).

- **Same frozen instrument, byte-identical stimuli.** `stimuli.json` is byte-identical to the original
  run (sha256 of the newline-stripped blob = `89f078e3…374cfc`, matching the original PREREG); probe /
  analyze / verdict-map code unchanged. Only the panel dict differs (`{"gpt": panel.B}`).
- **No panel-change decision owed.** `openai/gpt-5.4-mini` **is** `panel.B`
  ([`config/models.md`](../../../config/models.md)); the budget panel-change rule fires only for a
  model *not* in the panel. gpt was dropped from the earlier relational *history-perturbation* line for
  a **stimulus-generation** reason (it could not supply solo-decodable near-twin descriptions in the
  harvest design — [`result/relational-history-perturbation-v4`](relational-history-perturbation-v4.md);
  [`result/relational-stamp-comprehension-b`](relational-stamp-comprehension-b.md)), which is
  **inapplicable** to a fully synthetic instrument with no model-generated descriptions.
- **Independent gates.** A fresh **pre-run critic** GO'd the extension (panel-change adjudication: none
  owed; drop-reason adjudication: inapplicable; freeze intact). A fresh **post-run verifier**
  REPRODUCED every number from raw (DIRECT 7/36 = 0.194 [0.097, 0.350]; COMP 8/72 = 0.111; 0 NA;
  $0.037017 billed, 0 missing) and confirmed gpt's failure is a genuine composition-ability limit
  (single-move readers dominate), not a parse artifact.
