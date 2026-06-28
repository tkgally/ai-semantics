# PREREG — causative-inchoative progressive cancel-suppression calibration (2026-06-28, session 140)

**Frozen before any API call.** Measures whether the **progressive** suppresses the held
causative-inchoative result entailment that the s139 survey B2-confirmed at ceiling, in the
matched conflicting-cue paradigm of [`result/conative-cancel-direction-v2`](../../../wiki/findings/results/conative-cancel-direction-v2.md).
A **calibration of the cancel arm** — no ADD arm is paired, so it does **not** test
[`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md).
`internal-contrast-only` (no human anchor, no human-comparison claim).

## Why this ran

[`result/monotonicity-verbal-cancel-survey-v1`](../../../wiki/findings/results/monotonicity-verbal-cancel-survey-v1.md)
(s139) B2-confirmed three held-at-ceiling verbal defaults and identified the
**causative-inchoative** family as the one that admits a genuine **same-verb constructional
cancel** — the progressive/imperfective paradox ("Sam was breaking the vase" ⊭ "The vase
broke"). The standing s135/C1 lesson is binding: **measure the cancel, don't assume it.** This
probe is that measurement — the prerequisite for (and only on a clean signal) the matched
within-verbal add-vs-cancel battery.

## Frozen design

- **Frozen item set:** `experiments/data/monotonicity-causative-progressive-cancel/items.csv`,
  sha256[:16] **`5ba8a996fa70cf55`**. 18 items, the 6 s139 B2-confirmed verbs × 3 conditions
  (same subject/object triples, so `default` re-uses the s139 default). Hypothesis throughout =
  "The &lt;obj&gt; &lt;inch&gt;." —
  - **default** (diff 1): "Sam broke the vase." → gold **YES** (held entailment, B2-confirmed ceiling anchor).
  - **progressive** (diff 2): "Sam was breaking the vase." → gold **NO** (imperfective paradox; LOW affirm = good suppression).
  - **cue** (diff 3): "Sam was breaking the vase, and the pieces scattered across the floor." → gold **YES** (an explicit result-consequence that entails the result **without echoing** "broke" re-licenses).
- **Instruments:** NLI (primary) + forced-choice, temperature 0, panel claude-sonnet-4.6 /
  gpt-5.4-mini / gemini-3.5-flash. 18 × 2 × 3 = **108 calls**.
- **Indicator:** affirm-the-result rate per condition; **report-the-rate** (no pass bar tuned
  after data), matched to conative-cancel-v2.

## Reading (stated before the run; nothing tuned after)

- **Conative-shaped suppression** — default ~ceiling (re-confirms s139), `progressive` affirm
  meaningfully **below** it (`suppression_no_cue = 100 − progressive_affirm > 0`), cue
  re-licensing (`cue_affirm > progressive_affirm`) → the matched within-verbal **battery** can
  be built next (frozen resultative ADD arm sha `80bd4b60b55a3e60` + this progressive CANCEL
  arm, read by the frozen s134 thresholds) → the clean within-verbal confirm that discharges M2.
- **No suppression** — `progressive` affirm stays ~default (the C1-style aspectual-weakness
  outcome under strict NLI) → the **sharpened principled-limit** finding (held verbal defaults
  exist, but the panel resists their aspectual cancel).

Either outcome is a clean result. The probe **calibrates the cancel arm**; it does not pair the
ADD arm, so no asymmetry is computed and the conjecture is not tested here.

## Anti-cheat

- CSV frozen + sha256-hashed before any call; golds frozen.
- No ADD arm run → no asymmetry magnitude is computable at this calibration.
- No threshold tuned after data (report-the-rate). Do-not-re-grind: this is **not** a re-run of
  the ruled-out s135 for-durative / C1 completion arms — it tests the progressive cancel of the
  **lexical result-state** default (B2-confirmed at ceiling 1.00 in s139), a different inference
  than C1's incremental-completion default (which floored). The progressive cancel IS aspectual,
  so its suppression is exactly what must be measured here, not assumed.

## Procedure

1. `python3 build_items.py` — freeze + hash the CSV. ✅ (sha `5ba8a996fa70cf55`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO on the frozen set + this PREREG.
3. On GO: `OPENROUTER_API_KEY=… python3 probe.py` (108 calls), then `python3 analyze.py` →
   `raw/gate.json`.
4. Independent fresh-agent **post-run verifier** recomputes every per-condition cell.
5. Write [`result/monotonicity-causative-progressive-cancel-v1`](../../../wiki/findings/results/monotonicity-causative-progressive-cancel-v1.md).

## Human anchor

None. Within-model cancel-arm calibration, `internal-contrast-only`.
