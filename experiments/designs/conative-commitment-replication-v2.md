---
type: design
id: conative-commitment-replication-v2
title: conative COMMITMENT-ONLY replication v2 — is claude's single-model commitment-without-preference anomaly stable, or noise?
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: provisional
anchor: pending
contingent-on: []
created: 2026-06-15
updated: 2026-06-15
links:
  - rel: depends-on
    target: result/conative-preference-commitment-v1
  - rel: depends-on
    target: design/conative-preference-commitment-v1
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Experiment design v2 — conative COMMITMENT-ONLY direct replication

> **A clean direct replication, not a new test.** It re-runs the *identical instrument,
> thresholds, scoring, bootstrap, and panel* of [`design/conative-preference-commitment-v1`](conative-preference-commitment-v1.md)
> on a **fresh, disjoint verb set**, to ask the one question a replication answers about
> [`result/conative-preference-commitment-v1`](../../wiki/findings/results/conative-preference-commitment-v1.md):
> is claude-sonnet-4.6's lone positive effect — **Δ²_commit = +0.46, 95% CI [0.08, 0.79]**, a
> COMMITMENT-ONLY double contrast (commitment shift without preference shift, the mirror of the
> AANN dissociation) — a **stable single-model property** or **one-item-set noise**? Runs under the
> already-ratified [`decisions/resolved/fresh-construction-inferential-generalization`](../../wiki/decisions/resolved/fresh-construction-inferential-generalization.md)
> (Option A — the conative). **No new decision is opened; the yardstick is fixed.**

## 1. Why this, why now

The v1 conative run returned VERDICT INCONCLUSIVE: the AANN preference-without-commitment shape did
**not** generalize (Δ²_pref non-positive in all three models — the paraphrase "preference" component
was absorbed by the bare-*at* lexical cue), and the only construction-specific effect was claude's
**COMMITMENT-ONLY** Δ²_commit = +0.46. That effect is interesting precisely because it is the
*mirror* of the AANN finding — but it rests on **one model, one item set, a wide CI** (n = 12
conative vs 8 resist stems), and v1's own *Honest limits* flagged it as "an anomaly worth a future
look, not a finding." A single anomaly on one verb sample is exactly what a direct replication on an
independent sample is for. This is the **cheap unit** the v1 handoff (`NEXT.md`) named.

## 2. What is held identical to v1 (the replication discipline)

Everything that defines the yardstick is reused **verbatim**, to make this a clean replication and
not a re-tuning:

- **Instrument.** Both arms unchanged: Arm 1 paraphrase forced-choice (the PREFERENCE signal, the
  weaker instrument); Arm 2 NLI entailment (the COMMITMENT signal, the load-bearing discriminator,
  hypothesis = *"&lt;subj&gt; made contact with &lt;obj&gt;."*, relation 0/1/2). `probe.py`'s
  `NLI_SYS`, `PARA_SYS`, `P_PARA`, and the parsers are copied byte-for-byte from the v1 run.
- **Scoring & verdict map.** `analyze.py` is copied **byte-for-byte** from the v1 run (its
  `--selftest`, 30 checks, re-passes here). Δ²_pref / Δ²_commit, τ = 0.20 (inclusive), the strict
  bootstrap 95% CI-lower **> 0** rule (10,000 resamples, seed 20260615), the per-model verdict map,
  and the panel verdict are all the v1 definitions.
- **The double contrast and the headroom precondition** are the v1 ones (Δ² net of the bare-*at*
  cue; per-model headroom gate P(NLI=entail|transitive) ≥ 0.85 **and** P(paraphrase=D|transitive) ≥
  0.85; whole-design gate ≥ 2/3 models clear headroom or route to the Option-B fallback).
- **Panel** unchanged (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash; gemini `effort:minimal`,
  temperature 0).
- **The pre-registered gpt-5.4-mini scoring rule** (its known conative NLI fragility is **not**
  retrofitted as confirmation) carries over verbatim.

## 3. What changes — only the verbs (a fresh, disjoint lexical sample)

The single deliberate difference from v1: a **fresh, disjoint** verb set, structurally parallel to
v1 (`prep.py` asserts disjointness mechanically).

- **Conative (12, fresh):** slap, smack, pound, beat, strike, rap, tap, bash, batter, poke, bite,
  thump — all Levin (1993) conative-alternation verbs (hit verbs + poke/bite): the transitive
  robustly entails completed contact; "V at NP" cancels the contact guarantee. Disjoint from v1's
  kick/hit/punch/slash/stab/claw/swat/jab/chop/scratch/hack/whack.
- **Resist / LCC (8, fresh):** hug, caress, cradle (Levin touch verbs — lexicalize contact, do not
  undergo the conative) + crumple, squash, flatten, dent, mangle (change-of-state verbs, like v1's
  break/shatter/crush/smash; non-alternating, entail contact transitively, anomalous in "V at NP").
  Disjoint from v1's touch/embrace/break/shatter/crush/smash/bump/split. None carries a lexicalized
  idiomatic "at"-reading (the v1 snap→bump lesson is honored). Verbs that *might* be marginal
  (squash/flatten/dent — a "made X-ing attempts toward" reading is conceivable but not lexicalized)
  are named for the independent pre-run critic to vet; same conservative direction as v1's
  smash/crush (would only **shrink** Δ², never manufacture a false positive). The result page must
  report a with/without robustness check on any verb the critic flags.

## 4. Pre-registered prediction (the replication's point)

Frozen **before** any model call (full statement in `PREREG.md`):

- **PRIMARY (replication target).** If claude's COMMITMENT-ONLY effect is a stable property, claude's
  **Δ²_commit ≥ τ (0.20) with bootstrap 95% CI-lower > 0** reproduces on the fresh verbs, with
  **Δ²_pref NOT positive** (still COMMITMENT-ONLY, not CONVERGENT-POSITIVE). **REPLICATES** = that
  exact category recurs for claude.
- **FAILS TO REPLICATE** = claude's Δ²_commit is not positive on the fresh set (CI-lower ≤ 0 and/or
  Δ² < τ), or claude flips to a *different* category. This would mark the v1 +0.46 as plausibly
  one-item-set noise.
- **Secondary (not the headline):** gpt-5.4-mini is predicted to remain LEXICAL-CUE ARTIFACT (its
  known NLI fragility — commits to contact under NLI); gemini-3.5-flash predicted non-positive or a
  near-miss. These are reported but do not decide the replication; the replication is **about
  claude**.
- **No post-hoc tuning.** Verbs, thresholds, scoring, and this prediction are frozen pre-run. The
  effect either reappears on independent items or it does not.

The headroom gate still applies per model; if claude fails headroom on the fresh set the claude
result is uninterpretable and the replication is INCONCLUSIVE for the target model (reported as
such, no retuning).

## 5. Anchor discipline (identical split to v1, design §8)

- **NLI commitment arm, conative items — human-anchored** via
  [`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)
  (conative subset, ratified 2026-05-29). The CxNLI conative gold for a "V-at-NP → made contact"
  hypothesis is **non-entailment** (the catalogued triple *"I sipped at the Heineken."* / *"The
  Heineken was not the target of my sipping."* is **Contradiction**, Table 9; Exp-1 native baseline
  ≈ 0.90) — an **answer-key comparison + aggregate baseline, NOT a per-item human gradient**.
- **Paraphrase forced-choice arm and resist/LCC arm — `internal-contrast-only`.** No in-repo human
  paraphrase-preference norm exists; the anomalous at-string has no human reading key. The
  expert-stipulated conative-correct paraphrase reading (cancel) is labelled expert-stipulated. **No
  anchor invented.**

## 6. Files & freeze discipline (inherited binding condition I8)

- `experiments/runs/2026-06-15-conative-commitment-replication-v2/prep.py` — stimulus authoring;
  emits `stimuli.json` (frozen, seed 20260615); asserts parity / minimal-pair / counterbalancing /
  **disjointness-from-v1**; **no model calls**. Freeze hash recorded in `README.md` + `PREREG.md`.
- `.../stimuli.json` — frozen materials (committed before any probe call).
- `.../probe.py` — panel calls (paraphrase-FC + NLI, temperature 0, gemini `effort:minimal`);
  instrument code byte-for-byte from the v1 run; **refuses to run without a frozen `PREREG.md` and a
  present `analyze.py`**; `ABORT_USD = 0.50`.
- `.../analyze.py` — byte-for-byte from the v1 run; `--selftest` re-passes (30 checks).
- `.../PREREG-draft.md` → `PREREG.md` (frozen only after a **fresh independent pre-run-critic GO**).

## 7. Spend — pre-flight estimate

Identical shape to v1: 40 items × 2 instruments × 3 models = **240 calls** (+ a small verbatim retry
per unparseable response). At the v1 measured shape (240 calls billed **$0.05**), the point estimate
is **≈ $0.05; expected $0.04–0.08 billed**. Well under the single-run flag ($0.50) and the
**$5.00/day UTC** cap ([`config/budget.md`](../../config/budget.md); day total 2026-06-15 before
this run: $0.05 from the v1 run, leaving ample headroom). Actual billed `usage.cost` recorded in the
run record; missing-cost calls counted, never silently dropped.
