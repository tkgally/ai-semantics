# PREREG-draft — conative COMMITMENT-ONLY replication v2

> **DRAFT.** Becomes `PREREG.md` (the freeze) **only after** a fresh independent pre-run critic
> returns GO (or GO-WITH-FIXES with the fixes applied and stimuli refrozen). `probe.py`'s freeze
> guard refuses to call the API until `PREREG.md` exists.

## 0. One-line statement

A **clean direct replication** of the single positive effect in
`result/conative-preference-commitment-v1` — claude-sonnet-4.6's **COMMITMENT-ONLY** double contrast
(Δ²_commit = +0.46, 95% CI [0.08, 0.79]) — on a **fresh, disjoint** verb set, same instrument /
thresholds / scoring / panel. Runs under the ratified
`decisions/resolved/fresh-construction-inferential-generalization` (Option A — the conative). **No
new decision; the yardstick is fixed.**

## 1. Frozen materials

- `stimuli.json` — 40 items, seed 20260615, **sha256[:16] = `84e2e0d6afb4b5b6`** (record at freeze;
  re-run `prep.py` must reproduce it bit-for-bit).
- `prep.py` — authoring + mechanical asserts (all PASS, including disjointness-from-v1); no API.
- `probe.py` — instrument code byte-for-byte from the v1 run; the only file that calls the API.
- `analyze.py` — byte-for-byte from the v1 run; `--selftest` re-passes (30 checks).

## 2. Design (inherited verbatim from design/conative-preference-commitment-v1; see design/conative-commitment-replication-v2 §2)

- **Four families** (40 items): transitive_conative (12, headroom anchor) / conative (12, target) /
  resist-LCC (8, anomalous bare-*at* cue control) / transitive_resist (8, resist baseline).
- **Arm 1 — paraphrase forced-choice** (PREFERENCE, the weaker instrument): two lexically
  parity-matched options differing only by "did not necessarily"; seed-counterbalanced A/B;
  preference measure = P(cancel reading C chosen).
- **Arm 2 — NLI entailment** (COMMITMENT, the discriminator): premise = sentence, hypothesis = "made
  contact"; 0/1/2; withhold = P(NLI ≠ 0).
- **Headline = double contrast Δ²** net of the bare-*at* cue: Δ²_pref / Δ²_commit = P(·|conative) −
  P(·|resist). "Positive" iff Δ² ≥ τ (**0.20**, inclusive) **and** bootstrap 95% CI-lower **> 0**
  (10,000 resamples, seed 20260615, two-sample item-level).
- **Headroom precondition** (per model): P(NLI=entail|transitive) ≥ 0.85 **and**
  P(paraphrase=D|transitive) ≥ 0.85. Whole-design gate: ≥ 2/3 models clear headroom, else route to
  the Option-B fallback. No retuning.
- **Panel:** claude-sonnet-4.6 (A) / gpt-5.4-mini (B) / gemini-3.5-flash (C, `effort:minimal`),
  temperature 0.

## 3. The fresh, disjoint verb set (the only change from v1)

- **Conative (12):** slap, smack, pound, beat, strike, rap, tap, bash, batter, poke, bite, thump.
- **Resist / LCC (8):** hug, caress, cradle, crumple, squash, flatten, dent, mangle.
- Disjointness from the v1 sets is asserted mechanically by `prep.py` (PASS).
- **Critic-vet list:** squash/flatten/dent flagged as *possibly* marginal (a "made X-ing attempts
  toward" reading conceivable but not lexicalized) — conservative direction (would shrink Δ², not
  inflate it). The result page will report a with/without robustness check on any verb the critic
  flags, exactly as v1 did for smash/crush.

## 4. Pre-registered prediction (frozen before any call)

- **PRIMARY — REPLICATES** iff **claude's category is again COMMITMENT-ONLY**: Δ²_commit ≥ 0.20 with
  bootstrap 95% CI-lower > 0, **and** Δ²_pref NOT positive.
- **FAILS TO REPLICATE** iff claude's Δ²_commit is not positive on the fresh set (CI-lower ≤ 0 and/or
  Δ² < τ) **or** claude lands in a different category (CONVERGENT-POSITIVE / PARAPHRASE-ONLY /
  LEXICAL-CUE ARTIFACT / NULL). Either marks the v1 +0.46 as plausibly one-item-set noise.
- **HEADROOM-FAIL for claude** → claude result uninterpretable → replication INCONCLUSIVE for the
  target model (reported; no retuning).
- **Secondary (reported, not decisive):** gpt-5.4-mini predicted to remain LEXICAL-CUE ARTIFACT (its
  known conative NLI fragility — **not** retrofitted as confirmation, per the carried-over scoring
  rule); gemini predicted non-positive or near-miss.

## 5. Anchor discipline (identical split to v1)

- NLI commitment arm, conative items: **human-anchored** via `resource/scivetti-2025-cxnli-dataset`
  (conative gold = non-entailment; answer-key + ≈0.90 aggregate baseline, NOT a per-item gradient).
- Paraphrase arm + resist/LCC arm: **internal-contrast-only**. Expert-stipulated cancel reading
  labelled as such. No anchor invented.

## 6. Spend

240 calls; pre-flight ≈ $0.05 (expected $0.04–0.08 billed; v1 billed $0.05 for the same shape).
`ABORT_USD = 0.50`. Day total 2026-06-15 before this run: $0.05 (the v1 run); ample headroom under
the $5.00/day UTC cap. Actual billed `usage.cost` summed and recorded; missing-cost calls counted.

## 7. Anti-cheat affirmations

- The fresh verbs, thresholds, scoring, and the §4 prediction are frozen **before** any model call.
- The instrument and analysis code are byte-for-byte from the v1 run (verifiable by `diff`).
- The replication can only **confirm or fail to confirm** claude's v1 effect; nothing here is tuned
  to make a null positive. A non-replication is a first-class, reportable outcome.

## 8. Pre-run critic verdict (fresh independent agent, 2026-06-15) — GO

A fresh independent pre-run critic (did not design this experiment) returned **GO** — no
BLOCKER, no SHOULD-FIX. Confirmed: `analyze.py` byte-identical to v1 (`diff` empty, `--selftest`
30/30); `probe.py` differs only in the docstring (executable code identical); `prep.py` reproduces
sha256[:16] = `84e2e0d6afb4b5b6` with all 16 asserts PASS (incl. the 3 disjointness checks); all 12
conative verbs genuinely alternate with transitive contact-entailment; all 8 resist verbs are
non-alternating, contact-entailing, and carry **no lexicalized idiomatic "at" reading** (the v1
"snap at" defect class — LCC purity holds); the marginal-verb contaminant direction is verified
**conservative** (squash/flatten/dent could only *shrink* Δ²_commit, never inflate it); the §4
prediction is falsifiable/symmetric and the gpt-5.4-mini anti-cheat scoring rule carries over.

**Accepted NITs (no stimulus change; freeze hash unchanged):**
- (i) Because `analyze.py` is byte-for-byte from v1 by design, `results.json` will carry the
  **inherited v1 label strings** (`"run": "...-v1"`, the v1 design path) and `report()` prints
  "v1". This is a cosmetic mislabel, **not** a yardstick change; editing the code would break the
  byte-for-byte claim. The result page + README note this; the code stays untouched.
- (ii) "strike at" / "beat at" have figurative uses; with the concrete objects (gong, rug) the
  literal conative dominates, but any figurative lean would *inflate* Δ²_commit (pro-effect
  direction). The result page will report a with/without robustness check on **strike** (and
  **beat**) if claude's per-verb withhold looks anomalously high — the same treatment v1 gave its
  flagged smash/crush verbs.
- (iii) "bash at" / "thump at" are the least-frequent conative frames but attested/grammatical — no
  action.

Verdict applied: PREREG-draft.md frozen as this PREREG.md; stimuli unchanged (sha256[:16]
`84e2e0d6afb4b5b6`). The probe may run.
