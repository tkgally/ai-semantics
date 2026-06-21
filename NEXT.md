# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 75 (UTC 2026-06-21) spent **$0** (governance + dual-track groundwork — no
model queried). UTC-day 2026-06-21 total is unchanged at **$2.870** ($1.964 s64 + $0.503 s69 + $0 s70 + $0.280 s71 +
$0.123 s72 + $0 s73 + $0 s74 + $0 s75) of $5.00 (headroom **$2.130** *if the next session is still 2026-06-21 UTC*; a
new UTC day resets to the full $5 — **check the clock**). Single-run prefer-split flag unchanged (~$2.50/run). Full
ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 75 (UTC 2026-06-21) — governance + dual-track groundwork, $0 — ratified BOTH lexical bridging-context gates
(cross-session), froze the bridging-stratum + design spec, and wrote a new essay.** Workflow mode: reconciliation
(two independent fresh-agent adversarial-review ratifications) + one wave of 2 parallel bounded units + a read-only
adversarial coherence pass (1 BLOCKER fixed at integration — a misattributed quote). No experiment ran.

- **GOVERNANCE — both lexical bridging-context gates RATIFIED (cross-session; opened s74, ratified s75).** Each by a
  separate independent fresh-agent adversarial review:
  - [`decisions/resolved/lexical-bridging-context-operationalization`](wiki/decisions/resolved/lexical-bridging-context-operationalization.md)
    — **ADOPT DEFAULT + 3 binding mods:** the **B-primary (graded confidence) + C-categorical-cross-check ("both/unclear")
    fixed panel**, A (forced-judgment dispersion) characterizing-only; (1) **numeric freeze + sha256** of bands/wording
    before data, (2) **per-axis** reading (position by B alone; confidence/dispersion by both B and C — *not* a blanket
    AND), (3) **B–C disagreement is a mixed/weak result, not the null**. v1 clause-(c) context control bound non-optional.
  - [`decisions/resolved/lexical-bridging-context-anchor`](wiki/decisions/resolved/lexical-bridging-context-anchor.md)
    — **ADOPT the DWUG-stratum + WiC-poles DESIGN with a binding CLAIM-SCOPE CAP:** the human-comparison force is capped
    to **usage-similarity intermediacy**, never "two senses co-present"; **≥3-rater floor**; **collapses to
    `internal-contrast-only`** if the floored pool is too thin. One quote-integrity fix applied.
- **EMPIRICAL groundwork — bridging stratum FROZEN + design spec written + buildability reported ($0).** Built
  deterministically from the committed v1 DWUG manifest (no corpus text, CC BY-ND posture). Surviving pool under the
  **≥3-rater floor: 9 clear-same / 24 bridging / 15 clear-different = 48 pairs** (152 dropped); the **clear-same pole is
  thin (9/7)** — WiC-T supplement permitted (clear poles only). Verdict: **RUNNABLE-as-human-comparison (capped),
  conditional** (collapse-to-`internal-contrast-only` stays live). Artifacts: [`experiments/designs/lexical-bridging-context-v1.md`](experiments/designs/lexical-bridging-context-v1.md)
  (frozen design: B+C panel with numeric PLACEHOLDERS, per-axis reading, Q3 control, claim cap, run blocker) + the
  frozen [`experiments/designs/lexical-bridging-context-v1/stratum.csv`](experiments/designs/lexical-bridging-context-v1/stratum.csv)
  (sha256 `e7d36773…`), `freeze_stratum.py` (deterministic), and `BUILDABILITY.md`.
- **PHILOSOPHICAL — new essay** [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md)
  (the project's nineteenth): a graded sense **scale** (cross-item, established by v1) and graded sense **commitment**
  (within-item, the unrun Prediction 4) are logically independent; the null "graded scale, ungraded commitment" is a
  substantive behavioral finding, not a failure. Behavior-not-representation; usage-similarity cap; four revision
  triggers + honesty box.
- **Hygiene:** fixed a pre-existing quote-integrity defect on [`concept/polysemy`](wiki/base/concepts/polysemy.md)
  (it misquoted `referential-meaning` as "co-occurrence statistics encode"; the page actually says "next-token
  prediction optimizes for" — re-quoted verbatim, idea preserved as framing).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no open decisions. (Both lexical bridging
gates were resolved this session; do not re-ratify them.) Apply any Tom override first.

**Track lean.** 70 dual · 71 dual · 72 dual · 73 phil+diversify · 74 method/groundwork · 75 **governance + lexical
groundwork + philosophical**. The lexical axis is now the **active front** (right up to the run blocker); keep
weighting there until the bridging probe runs, then rebalance.

1. **EMPIRICAL — unblock + run the lexical bridging-context probe** (the design is frozen up to two blockers; the
   lowest-friction way to land the reopened lexical axis):
   - **(a) Re-fetch corpus text** — DWUG `dwug_en.zip` (Zenodo 14028531, CC BY-ND) into the **gitignored** data area
     (`experiments/data/dwug/`), re-map `id1`/`id2` → usage sentences + target offsets, re-record archive sha256.
     **No re-fetch script exists** — write a `prep.py` (cf. `experiments/data/subtlex-us/prep.py`). WiC `WiC_dataset.zip`
     likewise **if** the clear poles are supplemented (advisable — clear-same is thin at 9). *Network-bearing; verify the
     environment's network policy allows the fetch — if blocked, that is an honest blocker to record.*
   - **(b) Freeze the instrument numbers** (B's midpoint band, C's verbatim third-option wording, A's sample/temp) +
     sha256, under an **independent pre-run critic** (operationalization condition b/h). Re-check the **clear-same
     precondition** empirically; if unmet even with WiC support, **collapse to `internal-contrast-only`** and relabel.
   - **(c) Run** (spend-bearing; pre-flight per [`config/budget.md`](config/budget.md)). **Cost note:** v1's lexical run
     was gemini-heavy (~$3.13); keep gemini `effort: minimal` and scale, or split — a confidence + third-option panel
     over 48 pairs × variants could be pricey. Lead any result with the usage-similarity-vs-sense label discipline.
   - Files: [`experiments/designs/lexical-bridging-context-v1.md`](experiments/designs/lexical-bridging-context-v1.md);
     stratum + BUILDABILITY in `experiments/designs/lexical-bridging-context-v1/`.
2. **PHILOSOPHICAL/THEORY — sync the theory pages** to the within-item axis + the new essay:
   [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md) and
   [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) should register the cross-item-vs-
   within-item gradience distinction and [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md).
   The essay's revision triggers fire on the probe outcome.
3. **DIVERSIFY (if the lexical unit isn't picked up)** — essay trigger (b) the few→many scalar mechanism
   (`internal-contrast-only`, human anchor scouted null — see [`result/function-word-few-many-split`](wiki/findings/results/function-word-few-many-split.md)),
   or the dormant **relational** axis (order-composition ladder).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**NONE.** `wiki/decisions/open/` is empty (both lexical bridging gates resolved session 75; do not re-ratify).

## Standing-override notes (for Tom, if he looks)

- Session 75 spent **$0** (no model queried; UTC-day 2026-06-21 total unchanged at $2.870 of $5).
- Plain-language version: a session that **approved** (via independent review, the rules' cross-session safeguard) the
  two judgment calls the previous session wrote down for the word-ambiguity test — how to measure whether a model is
  "less sure," and how to certify a word is genuinely ambiguous from human data — adding two honest safeguards (the
  measure is fixed in numbers before any data; the people-comparison is capped to "people rated the uses as middling
  in similarity," never "two meanings are present"). It then **built the test to the edge of running**: it locked down
  the exact 48 word-use pairs (only those at least three people rated), found the set usable but thin, and reported the
  one thing that blocks the run — the underlying sentences are under a no-derivatives licence and must be re-fetched. It
  also wrote a short essay on why a model that ranks senses smoothly across examples but answers each single ambiguous
  case with full confidence would be a real finding, not a failure. No experiment ran.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratifications owed.
**The lexical axis is the active front:** the bridging-context probe is **built up to two blockers** — (a) re-fetch the
DWUG corpus text (gitignored, CC BY-ND, no prep script yet) + WiC if poles supplemented; (b) freeze the instrument
numbers under an independent pre-run critic + re-check the thin clear-same precondition (collapse to
`internal-contrast-only` if unmet) — then run (spend-bearing, gemini-cost-aware). Or sync the theory pages, or
diversify (few→many mechanism / relational). End squash-merged to `main`, website updated **with the JST clock-time
stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote
> `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main`
> first** (sessions 64–75 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text is also gitignored** (CC BY-ND) and **has no prep
> script yet** — writing one is part of next session's bridging-probe unblock (Zenodo 14028531). The frozen bridging
> **stratum** (`experiments/designs/lexical-bridging-context-v1/stratum.csv`, manifest-derived columns only) **is**
> committed; the corpus sentences it indexes are not. The full BLiMP dataset is **not** in-repo (only a 10-line sample).
