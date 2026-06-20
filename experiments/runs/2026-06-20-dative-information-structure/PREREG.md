# PREREG — dative information-structure probe (v1)

**Pre-registered before any model call. Frozen instrument; the analysis and verdict map
below are fixed in advance. No retuning of stimuli or indicator after seeing outputs —
a failed primary test is a falsification, recorded as such (charter §8; ratification
anti-cheat note).**

- **Operationalization:** [`decisions/resolved/dative-anchor-and-indicator`](../../../wiki/decisions/resolved/dative-anchor-and-indicator.md) (ratified 2026-06-20, ADOPT MODIFIED).
- **Conjecture:** [`conjecture/dative-alternation-information-structure`](../../../wiki/findings/conjectures/dative-alternation-information-structure.md).
- **Human anchor:** [`resource/languageR-dative-corpus`](../../../wiki/base/resources/languageR-dative-corpus.md) (Bresnan et al. 2007, `languageR::dative`; mirrored + firsthand-inspected this build — 3263×15, factor levels confirmed; promoted `external-only`→`catalogued`).
- **Result posture:** human-anchored (NOT internal-contrast-only) — the corpus is a real human resource.

## Frozen artifacts (sha256)

- `stimuli.json` sha256: **`0ffe3700524a8e5e0780820bab2fa4301923d37d93f7683d69515c968c4ababf`**
  (44 items = 32 main + 12 control; 240 trials. `probe.py full` refuses to run unless
  this exact sha is recorded here.)
- corpus tarball `languageR_1.6.tar.gz` sha256: `37e3e283b7d8226a1a7ebb5cb8dde32421c516f2ed4983834950de3c3640f974`
  (CRAN; GPL-2|GPL-3). Corpus model in `corpus_inspection.json` (in-sample accuracy 0.887;
  all five canonical directional effects reproduced).

## Indicator

Logprob-free **graded forced-choice**: a discourse context establishes which referent
(recipient or theme) is discourse-given; the model distributes 100 points between the
double-object (DOC) and prepositional-dative (PD) phrasings of the *same* proposition by
naturalness. DOC-preference = DOC_points / (DOC_points + PD_points) ∈ [0,1].
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
shortcut readers produce max |shift| = 0). Only tracking the discourse context can move
the shift off zero.

### Binding conditions (ratified) — certified at build (`certification.json`, all PASS)

- (a) within-pair length variance = 0 (identical NPs across DOC/PD) — PASS.
- (b) ≥12 control items, ≥6 long-recipient + ≥6 long-theme (the dissociating cells where
  information structure predicts the LONGER constituent first, opposing end-weight) — PASS (6+6).
- (c) recipient/theme length distributions identical across given conditions — PASS (same items).
- (d) ≥30 main items (32) + neutral both-new baseline — PASS.
- no item-verb appears in its own context (no dative-phrasing answer leakage) — PASS.
- no length/position/order shortcut reader beats chance on the contrast (all shifts 0) — PASS.

## Analysis (pre-registered)

**PRIMARY (corpus-licensed, decision-bearing), per model:** mean of shift(item) over the
32 main items, with a 10000-resample nonparametric bootstrap 95% CI over items and a
one-sided sign test. Per-model verdict:

- **CONFIRM** — mean shift > 0 AND bootstrap 95% lower bound > 0 (human direction,
  length+animacy held constant by construction).
- **WEAK** — mean shift > 0 but the CI includes 0 (a directional hint that does not clear).
- **FALSIFY** — mean shift ≤ 0 (no shift, or the wrong direction).

**Panel verdict: CONFIRM iff ≥2 of 3 models CONFIRM.** (Conjecture prediction 3: effect
size may decorrelate from surface accuracy — reported, not gated.)

**CONTROL arm:** the same shift on the 12 control items (the dissociating cells pit
information structure against end-weight). A shift that survives here is not a
short-before-long artifact. Reported alongside the main shift.

**NEUTRAL baseline:** mean DOC-pref in the both-new context — the model's default
preference, so a context-insensitive shallow preference is visible.

**SECONDARY (anchor-dependent, NON-decisive — ratification modification 2):** Spearman ρ
between each model's per-cell DOC-pref and the corpus-model predicted P(NP=DOC) for that
cell's factor configuration (from the firsthand `languageR::dative` fit). **May strengthen
a confirm or characterize a weak result; may NOT convert weak→confirm nor rescue a failed
primary test.**

## Data-quality gates (reported, not retuned)

NA (unparseable after one stern retry), retried count, length-truncation count. A trial
whose reply is length-truncated is never parsed (NA). High NA on any model is reported as
a limitation, not fixed by re-prompting after seeing the distribution.

## Budget pre-flight

240 trials × 3 models = 720 calls; short graded outputs (≤512-token cap, brief
justification). Comparable single-output panel probes bill ~$0.0001–0.0003/call →
**~$0.10–0.25 expected**; pre-registered **hard stop $0.60** (projected-total gate in
`common.py`). gemini held at `effort: minimal`. Well inside the $5/day UTC cap.

## Run procedure

1. `python3 probe.py liveness` — 3 calls, all must parse the graded FINAL line.
2. Independent pre-run critic GO (this session) on the frozen sha; a fresh pre-run critic
   GO is re-confirmed right before spend if the run lands in a later session.
3. `python3 probe.py full` — refuses unless this sha is recorded above.
4. `python3 analyze.py` → `analysis.json`.
5. Independent post-run verifier reproduces the numbers from raw before the result page is written.
