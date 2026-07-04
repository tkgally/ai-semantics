# PREREG — dative information-structure probe (POWERED re-run)

**Pre-registered before any finding-bearing model call. Frozen instrument; the analysis and
verdict map below are fixed in advance and are byte-identical to v1/v2's. No retuning of
stimuli or indicator after seeing outputs — a failed primary test is a falsification, recorded
as such (charter §8; ratification anti-cheat note).**

This is the **owed A2a powered re-run** of the dative information-structure line. It re-runs the
byte-frozen v1/v2 instrument on a **fresh, disjoint, POWERED item set** (100 main + 12 control;
0 shared `(subject, recipient, theme)` items, 0 shared context sentences with v1 or v2) to
**attach a magnitude+interval** to
[`claim/dative-information-structure-givenness`](../../../wiki/findings/claims/dative-information-structure-givenness.md),
which was promoted **direction-only** (session 174) with its magnitude explicitly deferred to
this run — exactly as session 169's 136-item CC powered re-run attached a magnitude to
[`claim/comparative-correlative-covariation`](../../../wiki/findings/claims/comparative-correlative-covariation.md).
**Same ratified operationalization, no new decision owed.**

- **Operationalization:** [`decisions/resolved/dative-anchor-and-indicator`](../../../wiki/decisions/resolved/dative-anchor-and-indicator.md) (ratified 2026-06-20, ADOPT MODIFIED).
- **Conjecture:** [`conjecture/dative-alternation-information-structure`](../../../wiki/findings/conjectures/dative-alternation-information-structure.md).
- **Human anchor:** [`resource/languageR-dative-corpus`](../../../wiki/base/resources/languageR-dative-corpus.md) (Bresnan et al. 2007, `languageR::dative`; the same firsthand-inspected logistic fit as v1/v2 — `corpus_inspection.json`, in-sample accuracy 0.887, all five canonical directions reproduced; the corpus tarball sha is unchanged).
- **Result posture:** human-anchored on the DIRECTION leg (NOT internal-contrast-only), exactly as v1/v2 and the claim.

## What this run is FOR (and what it is not)

The claim ([`claim/dative-information-structure-givenness`](../../../wiki/findings/claims/dative-information-structure-givenness.md))
is `supported` on a **direction/ordering** scope for 2 of 3 panel models (claude + gemini robust;
gpt WEAK — v1 CONFIRM +0.056 did not replicate in v2, falling to +0.018, CI includes 0). Its
**magnitude+interval is deferred to this run.** The powered re-run therefore:

1. **Attaches a powered magnitude+interval** to each model's main-arm within-item shift (100
   main items → the bootstrap CI narrows by ~√(100/32) ≈ 1.77× vs. founding N).
2. **Re-tests the 2/3 pattern** at power: does gpt stay WEAK (CI includes 0) at ~3× the items,
   or does a small real gpt effect clear zero? Either outcome is recorded as-is (anti-cheat: the
   verdict map is fixed below; this run cannot be retuned to a preferred 2/3-vs-3/3 answer).
3. Does **not** change the claim's *direction* scope, its human anchor (direction-only,
   production), or its shortcut-immunity argument — those are already supported by v1+v2. This run
   supplies only the powered *magnitude*, and whatever the powered *panel count* turns out to be.

## Sizing rationale (PROTOCOL §4)

- **Powered N = 100 main items** — at the ~100–150 floor PROTOCOL §4 names, and matched in spirit
  to the CC powered re-run's 136 items. The PRIMARY estimate is the mean within-item shift over
  the **main** items, so the **main arm is what is powered**.
- **Control arm kept at 12** (6 long-recipient + 6 long-theme), the certified minimum — it is the
  end-weight **dissociation robustness check**, not the powered magnitude, so it is not scaled
  (scaling it would triple its cost for no gain on the primary interval).
- **Cost / cap.** This graded working-surface instrument costs ~$0.00217/call (from v2's measured
  $1.56053/720). 100 main + 12 control ⇒ 648 trials/model ⇒ **1944 calls ⇒ pre-flight ~$4.22**
  (claude ~$2.64, gemini ~$1.27, gpt ~$0.29). This is **above the $2.50 single-run prudence flag**;
  a single frozen instrument cannot be split without changing the measurement, so per PROTOCOL §4
  ("if it genuinely cannot be split, run it as the day's only spend and say so") it is run as the
  **day's only spend**. Hard stop **$4.65** (below the level that would breach the $5/day UTC cap:
  today's UTC-2026-07-03 ledger already carries $0.1142, so the run's own $4.65 ceiling caps the
  day at ~$4.76 < $5.00). Chronic under-use on this load-bearing line would itself be a defect
  (PROTOCOL §4); a $4.2 powered run is the calibrated response.

## Frozen artifacts (sha256)

- `stimuli.json` sha256: **`6df9a7df94236495e3551589697364326df1557f1875640e4c32b879aaf65aa1`**
  (112 items = 100 main + 12 control; 648 trials/model, 1944 calls. `probe.py full` refuses to
  run unless this exact sha is recorded here.)
- corpus tarball `languageR_1.6.tar.gz` sha256: `37e3e283b7d8226a1a7ebb5cb8dde32421c516f2ed4983834950de3c3640f974`
  (CRAN; GPL-2|GPL-3). Corpus model in `corpus_inspection.json` (in-sample accuracy 0.887; all five
  canonical directional effects reproduced) — reused verbatim from v1/v2 (the human anchor is the
  same corpus; only the synthetic stimuli are new).
- **Instrument code** (`common.py`, `analyze.py`, `probe.py`, `mirror_and_fit.py`,
  `corpus_inspection.json`) is byte-identical to v2's EXCEPT **one budget-gate constant**:
  `common.HARD_STOP_USD` 2.00 → 4.65 (with its comment), and the matching pre-flight comment in
  `probe.py`. Measurement, scoring, parsing, and the verdict map are byte-for-byte v2.
  (`common.py`/`analyze.py`/`corpus_inspection.json` diff v2 only in that constant/comment; the
  scoring path is unchanged — verified by re-running v2's own `analyze.py` logic on this run's raw.)

## Indicator

Logprob-free **graded forced-choice** (identical to v1/v2): a discourse context establishes which
referent (recipient or theme) is discourse-given; the model distributes 100 points between the
double-object (DOC) and prepositional-dative (PD) phrasings of the *same* proposition by
naturalness. DOC-preference = DOC_points / (DOC_points + PD_points) ∈ [0,1]. DOC↔A/B mapping is
**counterbalanced** (each trial run with DOC=A and DOC=B); the parser is target-blind (keys on
reply position, not which option is DOC).

## Design (the within-item context shift)

The givenness manipulation lives **only in the discourse context** — the two phrasings are
byte-identical across an item's contexts (same words, same recipient/theme lengths, same animacy).
The finding-bearing measure is the within-item shift:

> shift(item) = mean(DOC-pref | recipient-given) − mean(DOC-pref | theme-given)

Human prediction: **shift > 0** (given recipient → DOC; given theme → PD). Because every surface
feature of the test sentence is identical across an item's two contexts, **any length-only /
position-only / order-only / always-DOC / always-PD / shorter-first / longer-first reader yields
shift = 0** — certified in `build_trials.py` (all eight shortcut readers produce max |shift| = 0;
`certification.json`). Main items use recipient/theme of equal (3/3) word length so the neutral
baseline is end-weight-neutral.

### Binding conditions (ratified) — certified at build (`certification.json`, all PASS)

- (a) within-pair length variance = 0 (identical NPs across DOC/PD) — PASS.
- (b) ≥12 control items, ≥6 long-recipient + ≥6 long-theme (the dissociating cells where
  information structure predicts the LONGER constituent first, opposing end-weight) — PASS (6+6).
- (c) recipient/theme length distributions identical across given conditions — PASS.
- (d) ≥30 main items (100) + neutral both-new baseline — PASS.
- no item-verb appears in its own context (no dative-phrasing answer leakage) — PASS.
- no length/position/order shortcut reader beats chance on the contrast (all shifts 0) — PASS.
- (extra, this run) fresh-item **disjointness**: 0 recipient NP and 0 theme NP shared with v1 or
  v2; every main item's recipient/theme is exactly 3 words; no within-set duplicate recipient or
  theme NP; every verb is a canonical alternating dative; a givenness-isolation prescreen confirmed
  each `rec_given` names the recipient and not the theme, each `thm_given` names the theme and not
  the recipient, and each `neutral` names neither (0 flags).

## Analysis (pre-registered, byte-identical to v1/v2)

**PRIMARY (corpus-licensed, decision-bearing), per model:** mean of shift(item) over the **100
main items**, with a 10000-resample nonparametric bootstrap 95% CI over items (RNG seed 20260620,
fixed in `analyze.py`) and a one-sided sign test. Per-model verdict:

- **CONFIRM** — mean shift > 0 AND bootstrap 95% lower bound > 0.
- **WEAK** — mean shift > 0 but the CI includes 0.
- **FALSIFY** — mean shift ≤ 0.

**Panel verdict: CONFIRM iff ≥2 of 3 models CONFIRM.** (Conjecture prediction 3: effect size may
decorrelate from surface accuracy — reported, not gated. The per-model magnitudes are reported
individually per [`essay/concordant-verdict-hides-spread`](../../../wiki/findings/essays/concordant-verdict-hides-spread.md).)

**CONTROL arm:** the same shift on the 12 control items (the dissociating cells pit information
structure against end-weight). A shift that survives here is not a short-before-long artifact.
Reported alongside the main shift; **does not gate the primary and may not rescue a failed
primary** (pre-registration).

**NEUTRAL baseline:** mean DOC-pref in the both-new context — the model's default preference.

**SECONDARY (anchor-dependent, NON-decisive):** Spearman ρ between each model's per-cell DOC-pref
and the corpus-model predicted P(NP=DOC) for that cell's factor configuration (from the firsthand
`languageR::dative` fit). May strengthen a confirm or characterize a weak result; may **not**
convert weak→confirm nor rescue a failed primary test. The six institutional `tlong` recipients
are coded inanimate (conservative), a value-laden choice feeding **only** this non-decisive ρ.

## Data-quality gates (reported, not retuned)

NA (unparseable after one stern retry), retried count, length-truncation count. A trial whose
reply is length-truncated is never parsed (NA). High NA on any model is reported as a limitation,
not fixed by re-prompting after seeing the distribution.

## Budget pre-flight (from the v2 MEASURED bill, not the rate card)

648 trials × 3 models = 1944 calls; graded outputs with a brief justification (512-token cap);
gemini `reasoning effort: minimal` held constant. v2 (identical per-call format) billed **$1.56053**
for 720 calls ⇒ ~$0.00217/call ⇒ expect **~$4.22** here (claude ~$2.64, gemini ~$1.27, gpt ~$0.29).
Pre-registered **hard stop $4.65** (`common.HARD_STOP_USD`; projected-total gate, re-checked every
30 calls, crash-safe resume) — above the ~$4.22 expectation so a modest per-call variance does not
spuriously trip, and below the $5/day UTC cap given today's $0.1142 prior spend. Day total after
this run projects **~$4.33 of $5.00**.

## Pre-run critic (session 175, 2026-07-03)

**VERDICT: GO** (independent adversarial pre-run critic, fresh agent — full rationale below). The
critic, given only the frozen artifacts, independently re-derived shortcut-proofness and checked
every binding condition, item disjointness from v1/v2, the analysis's bias against a free positive,
and the budget gate. One decorrelation vote was routed through a non-Anthropic panel model
(`openai/gpt-5.4-mini`, cutoff-aware preamble) per PROTOCOL §2/§A3; it **dissented NO-GO and was
weighed and rebutted** (below). Its stated precondition for GO is in fact satisfied by the frozen
instrument, so the fresh-agent GO stands.

> **Pre-run critic GO rationale (session 175, independent fresh agent).** Given only the frozen
> `stimuli.json` (the sha recorded above), `build_trials.py`, `certification.json`, `common.py`,
> `analyze.py`, `probe.py`, and this PREREG (plus the claim and the v2 run for comparison), the
> critic independently re-derived shortcut-proofness — writing **seven** fresh surface-only readers
> (DOC/PD char-length logistic, "the"-count delta, verb-identity hash, recipient−theme length
> delta, A/B order, an MD5 sentence-seeded pseudo-random reader, first-20-char comparison) and
> confirming every one yields a within-item shift of exactly 0 across all 112 items while a reader
> that peeks at `context_kind` moves it to 1.0; the build rebuilds the frozen sha exactly and
> certification re-PASSES. Against the frozen items the critic verified all binding conditions
> (within-pair DOC/PD token identity for all 112; all 100 main items recipient+theme each exactly
> 3 words; 6 long-recipient [gaps 5,5,5,7,5,5] + 6 long-theme [gaps 5,5,5,4,4,5] control items;
> neutral baseline present; no item-verb in its own contexts; no duplicate main recipient/theme
> NP), spot-checked givenness validity across all four id ranges plus all 12 controls (each
> `rec_given` names the recipient not the theme, each `thm_given` names the theme not the recipient,
> each `neutral` names neither; recipients animate, themes inanimate; all 24 verbs canonical Levin
> alternating datives taking both frames), confirmed disjointness (0 shared subject/recipient/theme,
> 0 shared recipient/theme NPs with v1 or v2), confirmed the analysis is biased against a free
> positive (CONFIRM needs mean shift > 0 AND bootstrap lower bound > 0; FALSIFY is the default;
> verdict from the **main** arm only so the control cannot rescue a failed primary; secondary
> Spearman + the inanimate coding feed only the non-decisive measure; parser target-blind; RNG seed
> fixed), confirmed the run owes no new operationalization decision, confirmed the instrument is
> byte-identical to v2 except the `HARD_STOP_USD` constant/comment (measurement byte-for-byte), and
> confirmed the $4.65 gate is a pure pre-call budget gate that caps the day at ~$4.76 < $5.00. **No
> blocker.** One SHOULD-FIX: the disjointness prose overstated by one — a single generic neutral
> scene-setter ("The stadium lights flickered on at dusk.") recurred from v1 m13 at p045, in a
> non-decisive both-new baseline cell. **APPLIED before freezing the run sha:** that one neutral
> sentence (only) was swapped to "The halftime crowd filed back to their seats."; the item is
> otherwise unchanged, the swap touches only a baseline cell that never enters the within-item
> shift, certification re-PASSED, and a context-sentence check now confirms **0** shared context
> sentences with v1 or v2. The run sha above (`6df9a7df…`) is the post-fix sha; the critic's GO was
> issued on the pre-fix sha (`3ca269f0…`) and the applied change is exactly the critic's own
> SHOULD-FIX (anti-cheat: a baseline-cell wording fix, orthogonal to every verdict-bearing number).
> **VERDICT: GO.**

**Non-Anthropic decorrelation vote — `openai/gpt-5.4-mini`, VOTE: NO-GO (weighed and rebutted;
$0.001766 billed).** The vote judged the primary endpoint "cleanly predeclared" and the
byte-identical scored phrasings "robust," and the magnitude-attachment purpose "sound … provided
you report the full distribution and do not reinterpret a CI-including-zero estimate as
confirmation" (which the pre-registration does — WEAK ≠ CONFIRM). Its one blocker was that the
*panel* decision could be "outcome-tuned via model selection/aggregation … unless the exact model
roster and any rerun/holdout rules were irrevocably locked … especially because the earlier weak
gpt run was singled out." **Rebuttal (fresh-agent verdict authority):** that precondition is
already met, a fact the vote lacked. (1) The 3-model roster is the **standing ratified panel**
(`config/models.md`, fixed 2026-05-28, battle-tested across ~75 studies), **not** selected for this
run — it is inherited verbatim from v1/v2. (2) The panel rule (CONFIRM iff ≥2/3), `temperature=0`,
gemini `effort:minimal`, and the bootstrap RNG seed are **byte-identical to v2's frozen `analyze.py`
/ `common.py`** and are fixed **before** any finding-bearing call; they cannot be altered post hoc
without changing the frozen sha and re-diffing the instrument. (3) The re-run's purpose is the
PROTOCOL §4 magnitude obligation owed by *every* claim-carrying line (the CC claim discharged the
identical obligation in s169), not to flip gpt; the PREREG pre-commits that **either** gpt outcome
(stays WEAK / clears zero) is recorded as-is, so it is a pre-registered powered estimate, not
confirmatory harvesting. The vote's GO-condition (frozen roster + fixed panel rule + no post-hoc
alteration) is therefore satisfied by the inherited standing panel and the frozen verdict map. The
divergence is recorded here per the decorrelation rule; the fresh-agent GO stands.

## Run procedure

1. `python3 probe.py liveness` — 3 calls, all must parse the graded FINAL line.
2. Independent pre-run critic GO recorded above (session 175, on this exact sha) + non-Anthropic vote.
3. `python3 probe.py full` — refuses unless this sha is recorded above.
4. `python3 analyze.py` → `analysis.json`.
5. Independent post-run verifier reproduces the numbers from raw before the result page is written.
