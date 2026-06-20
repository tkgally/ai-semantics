# PREREG — dative information-structure probe (v2 REPLICATION)

**Pre-registered before any model call. Frozen instrument; the analysis and verdict map
below are fixed in advance and are byte-identical to v1's. No retuning of stimuli or
indicator after seeing outputs — a failed primary test is a falsification, recorded as
such (charter §8; ratification anti-cheat note).**

This is a **direct replication** of the session-51 result
[`result/dative-information-structure-v1`](../../../wiki/findings/results/dative-information-structure-v1.md)
on a **fresh, disjoint item set** (0 shared `(subject, recipient, theme)` items, 0 shared
context sentences; only generic control-arm fillers such as *the museum* / *a medal* /
*a poem* recur). **Same ratified operationalization, no new decision owed.**

- **Operationalization:** [`decisions/resolved/dative-anchor-and-indicator`](../../../wiki/decisions/resolved/dative-anchor-and-indicator.md) (ratified 2026-06-20, ADOPT MODIFIED).
- **Conjecture:** [`conjecture/dative-alternation-information-structure`](../../../wiki/findings/conjectures/dative-alternation-information-structure.md).
- **Human anchor:** [`resource/languageR-dative-corpus`](../../../wiki/base/resources/languageR-dative-corpus.md) (Bresnan et al. 2007, `languageR::dative`; the same firsthand-inspected logistic fit as v1 — `corpus_inspection.json`, in-sample accuracy 0.887, all five canonical directions reproduced; the corpus tarball sha is unchanged).
- **Result posture:** human-anchored (NOT internal-contrast-only).
- **Replication motive:** firms up the v1 direction-of-effect and, in particular, exercises revision trigger (c) of [`essay/concordant-verdict-hides-spread`](../../../wiki/findings/essays/concordant-verdict-hides-spread.md) — does the order-of-magnitude effect-size spread (gemini +0.524 ≫ claude +0.327 ≫ gpt +0.056) reproduce, compress, or move on fresh items? gpt's small-but-clearing **+0.056** especially wants a fresh-item check before any weight rests on its size.

## Frozen artifacts (sha256)

- `stimuli.json` sha256: **`32d3e6225b328920d3612cd418a62cb61f34445dc55ee7e1a2841d9b9cddbf9b`**
  (44 items = 32 main + 12 control; 240 trials. `probe.py full` refuses to run unless
  this exact sha is recorded here.)
- corpus tarball `languageR_1.6.tar.gz` sha256: `37e3e283b7d8226a1a7ebb5cb8dde32421c516f2ed4983834950de3c3640f974`
  (CRAN; GPL-2|GPL-3). Corpus model in `corpus_inspection.json` (in-sample accuracy 0.887;
  all five canonical directional effects reproduced) — reused verbatim from v1 (the human
  anchor is the same corpus; only the synthetic stimuli are new).

## Indicator

Logprob-free **graded forced-choice** (identical to v1): a discourse context establishes
which referent (recipient or theme) is discourse-given; the model distributes 100 points
between the double-object (DOC) and prepositional-dative (PD) phrasings of the *same*
proposition by naturalness. DOC-preference = DOC_points / (DOC_points + PD_points) ∈ [0,1].
DOC↔A/B mapping is **counterbalanced** (each trial run with DOC=A and DOC=B); the parser
is target-blind (keys on reply position, not which option is DOC).

## Design (the within-item context shift)

The givenness manipulation lives **only in the discourse context** — the two phrasings
are byte-identical across an item's contexts (same words, same recipient/theme lengths,
same animacy). The finding-bearing measure is the within-item shift:

> shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)

Human prediction: **shift > 0** (given recipient → DOC; given theme → PD). Because every
surface feature of the test sentence is identical across an item's two contexts, **any
length-only / position-only / order-only / always-DOC / always-PD / shorter-first /
longer-first reader yields shift = 0** — certified in `build_trials.py` (all eight
shortcut readers produce max |shift| = 0; `certification.json`).

### Binding conditions (ratified) — certified at build (`certification.json`, all PASS)

- (a) within-pair length variance = 0 (identical NPs across DOC/PD) — PASS.
- (b) ≥12 control items, ≥6 long-recipient + ≥6 long-theme (the dissociating cells where
  information structure predicts the LONGER constituent first, opposing end-weight) — PASS (6+6).
- (c) recipient/theme length distributions identical across given conditions — PASS (same items).
- (d) ≥30 main items (32) + neutral both-new baseline — PASS.
- no item-verb appears in its own context (no dative-phrasing answer leakage) — PASS.
- no length/position/order shortcut reader beats chance on the contrast (all shifts 0) — PASS.

## Analysis (pre-registered, byte-identical to v1)

**PRIMARY (corpus-licensed, decision-bearing), per model:** mean of shift(item) over the
32 main items, with a 10000-resample nonparametric bootstrap 95% CI over items (RNG seed
20260620, fixed in `analyze.py`) and a one-sided sign test. Per-model verdict:

- **CONFIRM** — mean shift > 0 AND bootstrap 95% lower bound > 0.
- **WEAK** — mean shift > 0 but the CI includes 0.
- **FALSIFY** — mean shift ≤ 0.

**Panel verdict: CONFIRM iff ≥2 of 3 models CONFIRM.** (Conjecture prediction 3: effect
size may decorrelate from surface accuracy — reported, not gated. The per-model magnitudes
are reported individually per [`essay/concordant-verdict-hides-spread`](../../../wiki/findings/essays/concordant-verdict-hides-spread.md).)

**CONTROL arm:** the same shift on the 12 control items (the dissociating cells pit
information structure against end-weight). A shift that survives here is not a
short-before-long artifact. Reported alongside the main shift.

**NEUTRAL baseline:** mean DOC-pref in the both-new context — the model's default
preference, so a context-insensitive shallow preference is visible.

**SECONDARY (anchor-dependent, NON-decisive):** Spearman ρ between each model's per-cell
DOC-pref and the corpus-model predicted P(NP=DOC) for that cell's factor configuration
(from the firsthand `languageR::dative` fit). May strengthen a confirm or characterize a
weak result; may **not** convert weak→confirm nor rescue a failed primary test. The six
institutional `tlong` recipients are coded inanimate (conservative), a value-laden choice
feeding **only** this non-decisive ρ — flagged in v1's pre-run critic as owing no new
decision.

## Data-quality gates (reported, not retuned)

NA (unparseable after one stern retry), retried count, length-truncation count. A trial
whose reply is length-truncated is never parsed (NA). High NA on any model is reported as
a limitation, not fixed by re-prompting after seeing the distribution.

## Budget pre-flight (from the v1 MEASURED bill, not the rate card)

240 trials × 3 models = 720 calls; graded outputs with a brief justification (512-token
cap); gemini `reasoning effort: minimal` held constant. v1 (identical structure) billed
**$1.578** total (claude $0.990, gemini $0.485, gpt $0.103; liveness $0.005). Expect ~$1.58
again. Pre-registered **hard stop $2.00** (projected-total gate, re-checked every 30 calls,
crash-safe resume) — headroom above the v1 measure so a small per-call variance does not
spuriously trip; under the $2.50 single-run flag. Day total after this run projects ~$3.16
of the $5/day UTC cap (session-51 $1.583 + ~$1.58).

## Pre-run critic (session 53, 2026-06-20)

**VERDICT: GO** (independent adversarial pre-run critic, fresh agent — full rationale below).
The critic, given only the frozen `stimuli.json` (sha
`32d3e6225b328920d3612cd418a62cb61f34445dc55ee7e1a2841d9b9cddbf9b`), `build_trials.py`,
`certification.json`, and this PREREG, independently re-derived the shortcut-proofness and
checked every binding condition, item disjointness from v1, the analysis's bias against a
free positive, and the budget gate.

> **Pre-run critic GO rationale (session 53, independent fresh agent).** Given only the frozen `stimuli.json` (sha `32d3e6225b328920d3612cd418a62cb61f34445dc55ee7e1a2841d9b9cddbf9b`), `build_trials.py`, `certification.json`, and this PREREG, the critic independently re-derived shortcut-proofness — writing fourteen fresh surface-only readers (DOC/PD lengths, "the"-counts, verb identity, recipient−theme length delta, definiteness, A/B-order interactions, a sentence-seeded pseudo-random reader) and confirming every one yields a within-item shift of exactly 0, while a control reader that peeks at the discourse context yields 1.0; only reading the prior context can move the measure off zero. Against the frozen items the critic verified all binding conditions (within-pair NP identity, 6 long-recipient + 6 long-theme dissociating controls with genuine 3–7-word gaps, 32 length-matched main items, neutral baseline, no item-verb in its own context), spot-checked nine items for genuine prior-mention givenness with no ditransitive answer-leak and correct animacy, confirmed full item- and context-disjointness from v1 (only generic fillers "the museum"/"a medal"/"a poem" recur), confirmed all verbs are canonical alternating datives, confirmed the analysis is biased against a free positive (CONFIRM needs mean shift > 0 AND bootstrap lower bound > 0; FALSIFY is the default; the secondary corpus Spearman and the inanimate-recipient coding feed only the non-decisive measure and never the verdict; the parser is target-blind), confirmed the run owes no new operationalization decision, and confirmed the $2.00 hard stop is a pure pre-call budget gate under the $2.50 flag with the day projecting ~$3.16 of the $5 cap. The build reproduces the frozen sha exactly from source. No blocker found. **VERDICT: GO.** (Two NITs, both addressed: a stale v1-draft "$1.50" prose comment in `probe.py` was corrected to the $2.00 gate; this blockquote placeholder is now filled.)

## Run procedure

1. `python3 probe.py liveness` — 3 calls, all must parse the graded FINAL line.
2. Independent pre-run critic GO recorded above (session 53, on this exact sha).
3. `python3 probe.py full` — refuses unless this sha is recorded above.
4. `python3 analyze.py` → `analysis.json`.
5. Independent post-run verifier reproduces the numbers from raw before the result page is written.
