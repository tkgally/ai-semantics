---
type: result
id: within-lexical-scalar-vs-disjunctive-v1
title: "Within-lexical scalar-vs-disjunctive probe — the lexical commit-without-hedging SURVIVES a genuine disjunction (3/3 models): on a balanced-homonym context with no tie-break the models commit (near-zero UNCLEAR) exactly as on a DWUG scalar-bridging midpoint, level held fixed. The 'kind, not level' re-reading dissolves at R2 for the lexical case — the lexical specialness is about the word-sense layer, not the softness of the scalar stimulus."
meaning-senses:
  - distributional
  - referential
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-23
updated: 2026-06-23
links:
  - rel: contradicts
    target: essay/ambiguity-kind-not-level
  - rel: refines
    target: result/cross-level-shared-instrument-v1
  - rel: refines
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: resource/subtlex-us-frequency
---

# Result: within-lexical scalar-vs-disjunctive probe v1 — the lexical commitment SURVIVES a genuine disjunction (3/3)

> **Status: proposed (2026-06-23, session 87).** The first **run** of the within-lexical
> scalar-vs-disjunctive probe (built+frozen this session) under the resolved gate
> [`decisions/resolved/matched-ambiguity-kind-cross-level`](../../decisions/resolved/matched-ambiguity-kind-cross-level.md)
> (ADOPT DEFAULT: Option B + Q2-b `internal-contrast-only` + the nuisance-matching freeze). It is
> the R2 test of [`essay/ambiguity-kind-not-level`](../essays/ambiguity-kind-not-level.md) for the
> **lexical** case. One frozen lexical commitment instrument (`SAME/DIFFERENT/UNCLEAR` + 0–100
> confidence) — inherited **verbatim** from the cross-level lexical leg — applied identically to
> two within-lexical arms that differ **only** in the **kind** of ambiguity, level held fixed.
> Frozen `instrument.json` sha `ac56f777…`; `items_arm2.json` sha `e3ed5d53…` (frozen before any
> run). **Independent fresh-agent pre-run critic GO** (result-neutral; 4/12 leaning items flagged
> + a clean-8 subset pre-registered) + **post-run verifier reproduced** every cell from raw.
> **252 calls, $0.12128 billed, 0 missing cost, 0 errors, 252/252 parsed.**

## Lead with the cap (binding, read first)

This result makes **NO human-comparison claim for the disjunctive arm.**

- The **disjunctive (Arm 2)** items are **author-built balanced homonyms** —
  **`internal-contrast-only`** (gate Q2-b). No in-repo resource certifies homonym sense
  co-presence; the balance of each context is author-stipulated and was vetted by an independent
  pre-run critic and **frozen before any model output**. Its force is a *within-model* contrast.
- The **scalar (Arm 1)** items are human-rated (DWUG) but used here only as one arm of a
  within-model contrast; **capped to usage-similarity** intermediacy (a DWUG mid-scale "bridging"
  pair is a usage-similarity midpoint, **not** a certified within-sense bridge), inherited from
  [`result/lexical-bridging-context-v1`](lexical-bridging-context-v1.md).
- **Behavioral, not representational.** "Commit / decline" is the categorical posture of a
  behavioral verdict, never a window into representation.
- **Small, clustered N**, 3 commercial 2026 models, direction-of-effect with wide per-cluster
  bootstrap CIs — **no coverage claim**.

## Headline

**The lexical commit-without-hedging SURVIVES a genuine lexical disjunction — 3/3 models.** Under
one frozen instrument, with the level held fixed (lexical word-sense), the models meet a
**balanced-homonym** context (two unrelated senses both licensed, **no tie-break**) with the same
near-zero `UNCLEAR` they show on a DWUG **scalar-bridging** midpoint. The decline rate does **not**
rise from the scalar arm to the disjunctive arm, and is **not** elevated over the disjunctive arm's
own clear controls. The lexical "discreteness" is therefore **not** an artifact of the *softer*
(scalar) bridging stimulus — it holds for a genuine lexical disjunction too.

This is the **symmetric first-class outcome** the gate and
[`essay/ambiguity-kind-not-level`](../essays/ambiguity-kind-not-level.md) pre-registered: the
essay's **"kind, not level"** re-reading bet that a disjunctively-ambiguous lexical item would draw
*decline* (like the constructional/relational disjunctions of the cross-level dissolution). It
does **not**. So the essay's central reading **dissolves at R2 for the lexical case** (its
**revision trigger (b)** fires) — and the *more interesting positive* it named takes its place:
**the lexical leg's specialness is about the word-sense layer, not the scalar-vs-disjunctive kind
axis.** The deflationary kind-reading loses its lexical leg.

Per-model verdict (frozen survival/collapse map, gate Q3):

| model | scalar bridging decline | disjunctive decline (all 12) | disjunctive clear controls | within-arm gap CI (disj − clear) | cross-arm gap CI (disj − bridging) | C3 | **verdict** |
|---|---|---|---|---|---|---|---|
| claude | 0.0% | **8.3%** (1/12) | 0.0% | [0.00, 0.25] | [0.00, 0.25] | PASS | **SURVIVAL** |
| gpt | 0.0% | **0.0%** (0/12) | 0.0% | [0.00, 0.00] | [0.00, 0.00] | PASS | **SURVIVAL** |
| gemini | 0.0% | **0.0%** (0/12) | 0.0% | [0.00, 0.00] | [0.00, 0.00] | PASS | **SURVIVAL** |

SURVIVAL = the disjunctive decline is near-zero (≤ 0.10), **not** elevated over its clear controls
(within-arm CI lower bound not > 0), **and** indistinguishable from the scalar bridging leg
(cross-arm CI includes 0). The higher anti-cheat bar (survival would partly revive a defeated
unified conjecture, and the residuals all cut toward it) is met by **all three legs at once**.

## What the models actually did on the disjunctive items

Faced with a balanced homonym in one sentence and a sense-fixed use in the other, the models
**resolve the balanced context to a reading and commit**, rather than declining:

| model | SAME | DIFFERENT | UNCLEAR | mean confidence |
|---|---|---|---|---|
| claude | 3 | 8 | **1** (organ) | 86.4 |
| gpt | 4 | 8 | 0 | 97.7 |
| gemini | 2 | 10 | 0 | 99.2 |

They mostly read the balanced use as a **DIFFERENT** sense from the fixed partner and say so
confidently — i.e. they do **not** assimilate the ambiguous context to the disambiguated one; they
read it on its own terms and still pick a pole. Only claude, on **organ**, takes `UNCLEAR` once
(and its mean confidence, 86.4, is the lowest — consistent with claude being the most
hedge-prone/self-report-soft model in prior lexical work,
[`result/cross-level-shared-instrument-v1`](cross-level-shared-instrument-v1.md),
[`result/lexical-bridging-context-working-surface-v1`](lexical-bridging-context-working-surface-v1.md)).

## The scalar arm replicates the prior null exactly

The scalar (Arm 1) leg reproduces the lexical bridging null under this instrument **cell for
cell**: bridging decline **0.000** for all three models; clear-same and clear-different decline
**0.000**; so the scalar arm is the same discrete-on-the-moment posture
[`result/lexical-bridging-context-v1`](lexical-bridging-context-v1.md) and
[`result/cross-level-shared-instrument-v1`](cross-level-shared-instrument-v1.md) documented. The
within-lexical contrast is therefore read against a known-good scalar baseline.

## Clear-class precondition (C3), per arm

Every arm passes C3 (clear-class decline < 0.20 **and** mean confidence > 70) for every model:
the disjunctive clear controls decline **0.0%** with mean confidence **97.6 / 99.0 / 100.0**
(claude/gpt/gemini); the scalar clear controls decline 0.0%. So the instrument reads cleanly on
both arms' unambiguous items before any ambiguous-class reading is interpreted — the survival is
**not** a precondition failure in disguise.

## The disclosed limits — what survival does and does not show (lead with these)

The result is **SURVIVAL under the frozen instrument**, but three residuals all cut **toward**
survival (which is exactly why survival carried the higher bar), and one is load-bearing for the
*interpretation*:

1. **The lexical "disjunction" remains resolvable-by-commitment (the load-bearing caveat).** A
   balanced homonym in `ctx1` is genuinely two-sensed with no tie-break, but the model is asked
   whether its sense *matches* a second, disambiguated use — a question it can answer by **picking
   a reading** for `ctx1`. A relational same-round **dual binding** (the cross-level relational
   leg) is, by contrast, *literally unresolvable* — the term was bound to two figures at once, so
   there is no reading to pick. The two arms are matched in kind at the level of "two senses
   licensed, no tie-break in the ambiguous context," but **not** at the level of "no resolution is
   possible at all." So whether the survival reflects "word-sense is special as a layer" or "a
   balanced homonym still affords a defensible resolution where a dual-binding does not" is **not
   fully separated by this design** — the within-lexical analogue of the cross-level body-difference
   caveat. The deflationary kind-reading loses its lexical leg **either way** (the lexical commit
   is not the soft-scalar-stimulus artifact the essay proposed), but the *mechanism* of the lexical
   commitment — layer-specialness vs always-resolvable-by-a-reading — is not isolated here.
2. **Four disjunctive contexts lean (disclosed; cuts toward survival).** The pre-run critic judged
   **8/12** balanced contexts genuinely two-way and flagged **mole** (→ spy), **punch** (→ drink),
   **club** (→ heirloom-stick) as mild and **pupil** (→ student) as strong leans. Because each
   balanced `ctx1` is paired with a sense-fixed `ctx2`, a lean in **either** direction *suppresses*
   `UNCLEAR` (a sense-A lean → confident SAME; a sense-B lean → confident DIFFERENT), so leaners
   **erode the collapse signal** rather than padding it. The **pre-registered clean-8 subset**
   {bank, crane, file, organ, trunk, tank, plot, ring} gives the same verdict: gpt/gemini decline
   0.0% on it; claude's single `UNCLEAR` (organ) is *in* the clean-8 (decline 1/8 = 12.5%,
   within-arm gap CI [0.00, 0.375] — lower bound still not > 0). The survival does not depend on
   the leaning items.
3. **Register + decline-gloss residuals (cut toward survival).** Arm 2 is author-built contemporary
   plain prose; Arm 1 is DWUG/COHA corpus prose — an irreducible register difference (cleaner prose
   is, if anything, *easier* → lower decline). The inherited `UNCLEAR` gloss ("genuinely in
   between") is scalar-flavoured and, applied verbatim to both arms, biases a disjunction
   ("both/neither") away from `UNCLEAR`. Both cut toward survival; both are constants across the
   within-arm contrast (which is the primary, register-clean criterion). Frequency was matched
   (median Lg10WF gap **0.00**, [`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md))
   and length matched (mean token gap **0.46**).

## What this resolves

- **For [`essay/ambiguity-kind-not-level`](../essays/ambiguity-kind-not-level.md):** its
  **revision trigger (b)** fires — "the probe runs and the lexical leg holds (commits even on a
  balanced homonym) … 'kind, not level' **dissolves at R2** for the lexical case: the lexical
  commit-without-hedging is about word-sense specifically, not about the kind of ambiguity." Per
  the convergence ladder's **symmetric** standard this is a **first-class result, not a failure** —
  the *more interesting* positive about word-sense commitment. The essay is revised to record that,
  for the lexical case, the residue's join is the **layer**, not the kind (with caveat 1 bounding
  how strong "layer" can be).
- **For [`result/cross-level-shared-instrument-v1`](cross-level-shared-instrument-v1.md):** its
  load-bearing comparability caveat is **partly discharged** — the lexical leg's near-zero decline
  is **not** an artifact of being handed a *softer* (scalar) ambiguity, because it survives a
  disjunctive one. The cross-level dissolution's deflationary "three rhyming facts" reading is
  **reinforced for the level axis** (the lexical leg really is the odd one out), even as the kind
  axis is closed for the lexical case. (Caveat 1 leaves open whether the lexical odd-one-out is
  "layer" or "always-resolvable.")
- **The kind axis is closed only within the lexical level.** This probe re-ran neither the
  constructional nor the relational leg; it makes **no** cross-level matched-kind claim (that was
  Option A, held in reserve). The "kind, not level" reading is dissolved *for the lexical case*; the
  general kind-vs-level question across levels is untouched.

## Scope and limits (lead with these)

- **No human comparison** (gate Q4): disjunctive arm `internal-contrast-only`; scalar arm capped to
  usage-similarity. **Behavioral, not representational.**
- **Mechanism not isolated** (caveat 1): survival is real under the frozen instrument; whether it is
  layer-specialness or balanced-homonym-resolvability is not separated here.
- **Residuals cut toward survival** (caveats 2–3): leaning items, register, scalar-flavoured gloss —
  all disclosed; survival held to the higher bar and met on the clean-8 subset too.
- **Small, clustered N** — 12 homonyms (24 disjunctive + clear), 17 bridging lemmas (24 bridging +
  24 clear): direction-of-effect, wide per-cluster CIs.
- **Shared priors are not independent witnesses** — three decoders are not three independent
  confirmations; the *pattern* is the signal.
- **n=3 commercial 2026 models**; no claim about other models, sizes, or training regimes.

## Reproduce

- Stage the gitignored Arm-1 corpus (recipe-not-corpus): `experiments/designs/lexical-bridging-context-v1/prep.py`
  (DWUG EN, archive sha `64eef477…` matches pin, 48/48 stratum remap). Arm-2 items are author-built
  and committed (`items_arm2.json`).
- `python3 certify.py` (no API, 15/15 PASS), then
  `OPENROUTER_API_KEY=… python3 probe.py --run --i-have-pre-run-critic-go`, then `python3 analyze.py`.
- Design + frozen instrument + analysis:
  [`experiments/designs/within-lexical-scalar-vs-disjunctive-v1/`](../../../experiments/designs/within-lexical-scalar-vs-disjunctive-v1/)
  (`instrument.json` sha `ac56f777…`; `analyze.py` 10000-rep clustered bootstrap, seed 20260623,
  clusters lemma/homonym). Raw (`raw/` — Arm-1 carries **no** DWUG corpus text: item-id + class +
  cluster pointers only; Arm-2 prose is author-built and committed) and `analysis.json` committed.

## Verifier note

A post-run verifier should re-derive, from raw: per-arm per-model decline/confidence; the
disjunctive call distribution (claude 3/8/1, gpt 4/8/0, gemini 2/10/0); the within-arm and
cross-arm decline-gap CI directions (all near-zero / not elevated); the clean-8 subset verdict; the
three SURVIVAL verdicts; parse integrity (252/252); billed cost re-summed ($0.12128, 0 missing); and
that no DWUG corpus text survives in committed raw.
