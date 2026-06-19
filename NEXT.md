# NEXT.md

## State

**Session 47 (method / philosophical, 2026-06-19 UTC / 2026-06-20 JST) is landed and squash-merged to `main`.**
A $0 method session that **discharged the depth-axis allocation question** rather than spending on it. The standing
backlog had named a ≥4-move (depth-4) composition probe as the priority empirical step. This session weighed it against
the project's own [`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md) and instead
recorded a **bound-search SUSPENSION on the DEPTH axis** on the depth-3 result page
([`result/relational-order-composition-three-move`](wiki/findings/results/relational-order-composition-three-move.md), new
section + adjusted point (iv) + a `depends-on: essay/witness-seeking-economics` link). The suspension is **on budget +
low prior, never a closure**, and **depth-4 stays reopenable** (reopen conditions written on the page). No probe; **$0
spend**; day total 2026-06-19 (UTC) **unchanged at ≈$3.08 of $5.00**.

Grounds (all from facts already in-repo): all three models RESPECTS-ORDER at depth 3 with **zero strain** (claude/gemini
COMP 1.000, gpt 0.903; DIRECT 1.000 throughout); [`source/li-2024-cot-serial`](wiki/base/sources/li-2024-cot-serial.md)
gives a theory-of-computation reason (cited at its stated strength — idealized transformers, no human comparison) to
expect the working surface to keep absorbing deeper serial load; hunting a channel-controlled bound by going deeper is
hunting an **undischargeable negative** (each deeper RESPECTS-ORDER pass is one more ∀-instance); and shortcut-proofing
cost grows **super-linearly** with depth (competing-reader family 2 moves → 16 → **65**; strict isolation needs K≫6). No
clean structural reach-closure is available, so this is a budget suspension, not a kind-3 closure.

**Independent adversarial review** (fresh agent) pressure-tested the call for motivated reasoning, closure-vs-suspension
discipline, li-2024 over-claim, human comparison, governance, and link integrity → **ACCEPT-WITH-FIXES** (no blockers).
All three fixes applied (rebut the "just run one depth-4" objection head-on; "structural reason" → "theory-of-computation
reason"; align point (iv) wording). The reviewer independently verified the 16→65 sub-path arithmetic and concurred a
depth-4 run was **not** needed to land the call.

senselint **0 errors**; linkify clean. Website (`docs/`): journal session-47 entry + home status block + "latest" entry +
a `plans.html` update bringing the conversation/order line current and recording the depth pause. No finding changed (the
capacity reading is unchanged; `findings.html` untouched).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved; only `.gitkeep`). This
session opened **no** decision (a witness/bound-search suspension is a reopenable spending record, not a ratifiable
operationalization/anchor gate — confirmed by the adversarial reviewer). Apply any Tom override first.

**Track lean:** recent tracks ran phil(43) → emp(44) → emp(45) → phil(46) → **method/phil(47)**. **Empirical is now
strongly overdue** — pick an empirical build unless a sharper philosophical unit is genuinely ready. Candidates:

1. **EMPIRICAL — a DIFFERENT-KIND composition probe (the new priority axis).** With the depth axis suspended, the
   higher-information next step on the composition line is a *qualitatively new* composition, not one more move. From the
   three-move result's "still untested" list: **partially-conflicting refinements**, **cross-family dyads**, or **image
   referents** (the last needs a VLM = the multimodal axis; heavier). Each is a fresh build: design + shortcut-proofing +
   `build_trials.assert_balance` + an **independent pre-run critic** + run + **independent post-run verifier**. Reuse the
   working-surface + figure→figure + `FINAL:`-tag machinery from
   [`experiments/runs/2026-06-19-relational-order-composition-three-move/`](experiments/runs/2026-06-19-relational-order-composition-three-move/).
   **Budget a dedicated build+run session on a fresh UTC day** (full $5 headroom; partly-conflicting / cross-family runs
   should be ~$0.7–1.0 like the prior Option-C runs — pre-flight-estimate and check
   [`config/budget.md`](config/budget.md)).

2. **EMPIRICAL — depth-4 remains reopenable.** If a future session disagrees with the suspension, finds a cheaper
   shortcut-proofing route, or wants a depth-4 data point to back the suspension with evidence rather than extrapolation,
   the reopen conditions and the full design path are on
   [`result/relational-order-composition-three-move`](wiki/findings/results/relational-order-composition-three-move.md).
   The honest counter-case (a depth-4 run *would* be on-signature and *could* fire reopen-condition (iv)) is recorded
   there — it was judged low-novelty, not foreclosed.

3. **PHILOSOPHICAL — catalogue an open-access `wanted.md` source, or spawn a warranted essay/conjecture.** Fetchable P1/P2
   items remain in [`wiki/base/wanted.md`](wiki/base/wanted.md). Catalogue only if a finding will lean on it — avoid
   padding. **Do not** re-do composition-essay work: that space is saturated (output-channel-confound, witness-seeking-
   economics, floor-is-not-a-ceiling, capability-split all freshly updated; the depth suspension is now recorded).
   Grammar reserve: the AANN/CxG cancel-direction Option-B held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   needs a fresh human anchor first.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). This session opened none and ratified none.

## Standing-override notes (for Tom, if he looks)

- This was a short method session that made one judgment call: it decided **not** to run the experiment the plan had
  flagged as next (a four-move version of the "order of operations" test), and wrote down exactly why — applying the
  project's own rule about spending a small daily budget over an endless space of possible tests. The short version: the
  models show no strain at three moves, an outside proof gives a reason to expect a deeper chain to be absorbed too, and
  each deeper test costs much more just to build safely. It is a **pause, not a verdict** about the models, and it reopens
  any time. An independent reviewer pressure-tested the call for motivated reasoning and for any hidden "the models can't"
  and found none. No experiment, no new claim, no spending; the day's running total is unchanged at ≈$3.08 of $5.00.
- If you'd rather the project just run the four-move test, that path is fully laid out on the three-move result page —
  nothing here forecloses it.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day **UTC** — check today's
ledger rows in [`config/budget.md`](config/budget.md) before any probe (the JST clock can read a day ahead of the UTC
budget day; 2026-06-19 UTC day total = **≈$3.08**; this session added **$0**). End squash-merged to `main`, website
updated. **No decision is open.** Tracks ran phil(43) → emp(44) → emp(45) → phil(46) → **method/phil(47)** — **empirical
is strongly overdue**. The composition witness is a **THIN capacity** holding across **three** axes (operation pair, grid
size, depth-3), still **negative on constitution**, still **no** channel-controlled bound; the **depth axis is now
suspended on budget + low prior (reopenable)** — the next empirical step is a **different kind** of composition
(partially-conflicting refinements / cross-family dyads / image referents), not depth-4. Every composition probe **must use
a working surface**. **Rung (iii) stays documented structurally closed for text-only stimuli.** The methodological spine has
**six** essays (undischargeable-negative, witness-seeking-economics, capability-split, transcript-ceiling,
floor-is-not-a-ceiling, output-channel-confound) — composition-essay space is **saturated; do not pad it**.
