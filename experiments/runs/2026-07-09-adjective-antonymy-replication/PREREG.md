# PREREG — ADJECTIVE-antonymy replication probe (H1 decoupling + the antonymy-shadow clause)

**Frozen s196, 2026-07-09, BEFORE any model call.** Design:
[`design/adjective-antonymy-replication-v1`](../../designs/adjective-antonymy-replication-v1.md).
Gates RATIFIED s196:
[`decisions/resolved/adjective-antonymy-replication-design`](../../../wiki/decisions/resolved/adjective-antonymy-replication-design.md)
— **Q1-C / Q2-A / Q3 internal-contrast-only.** This file freezes the item set, the control, the corpus,
the verdict map with numeric thresholds, and the anti-cheat fence. Nothing below may be touched after
recovery is observed.

## The question (nothing wider) — J&K's HOME part of speech

On a **fresh** relatum-production probe over four WordNet **adjective** relations (antonymy, synonymy,
similar-to, also-see), run on the panel against a contrastive-frame G² control on **C4 web text** (the
s193-frozen corpus; the byte-frozen s186/s193 G² construction, only the cue POS + candidate pool
changing), re-tested where Justeson & Katz actually **measured** contrastive-frame saturation —
predicative adjectives:

- **PRIMARY — the antonymy-shadow clause (s186 clause 1, in J&K's home POS):** is adjective antonymy's
  HIT@3 recovery residual over the contrastive-frame control **among the largest** (the s186
  falsification replicates: the shadow does NOT saturate antonymy) or the **smallest / near-zero** (the
  measured-denser adjective framing reconstructs antonym recovery — a POS boundary on the s186
  falsification)?
- **CO-PRIMARY at true low power — H1, the decoupling (essay trigger (a)'s adjective route):** does
  across-relation recovery rank **again decouple** from contrastive-frame cue-strength (ρ_cue ≤ +0.30,
  ≥2/3 models) — or does cue-strength recover its predictive power on adjectives (ρ_cue > +0.50, ≥2/3),
  showing the decoupling was noun-specific?

**Internal-contrast only** (Q3): recovery is scored against WordNet, a shared target that cancels in the
head-to-head; the predictor (contrastive-frame G²) is a corpus statistic; no human baseline enters.
**H2 is NOT tested** (Q2-A): adjective `min_depth()` is a degenerate constant 0 (empty `hypernyms()`) —
WordNet has no adjective IS-A taxonomy, so H2's frozen proxy cannot transfer. **Adjectives only; never
pooled with the noun probes.**

## Frozen artifacts (built + committed BEFORE any model call)

- **`items.json`** (`prep.py`, SEED 20260709): FRESH cue adjectives per relation, DISJOINT from the 707
  committed s186 noun cue lemmas (asserted 0 overlap, 4/4 relations; the exclusion covers noun/adjective
  homographs like light/right/fine). WordNet POS `a`+`s` (heads + satellites). Gold relatum set
  word-form level; `relata()` adjective branches are the POS-specific parallel of the s186 `relata()`.
  Frequency band Lg10WF ∈ [2.0, 4.5] (byte-identical to s186/s193 — the iconic-outlier cap: the
  very-high-frequency iconic pairs *big/good/hot* J&K/Cao flag as G² outliers sit above 4.5 and are
  excluded). Matched to **antonymy's** fresh per-bin Lg10WF profile (the primary + one of the two
  sparsest relations). **ACHIEVED per-relation N (freeze finding):**

  | relation | N | Lg10WF median | gold size median (mean) |
  |---|---|---|---|
  | antonymy | 130 | 2.839 | 1 (1.13) |
  | synonymy | 130 | 2.839 | 3 (3.60) |
  | similar | 130 | 2.839 | 2 (3.92) |
  | also-see | 130 | 2.824 | 2 (2.42) |

  **520 verdict-bearing cues** (130 × 4; the item-level SECONDARY arm pools all 520). Antonymy gold size
  ≈ 1 (mean 1.13) — the small-gold confound that caps Soundness at 1/k; **HIT@3 is the scorer of record
  for the antonymy-shadow PRIMARY** (C6). Measured fresh eligible pools (s196): antonymy 512, synonymy
  1475, similar 1993, also-see 482 — all clear the powered N=130.

- **`control.json` / `counts.json`** (`build_cooc_c4.py`): the contrastive-frame G² control on **C4**.
  `signed_g2` + `compute_control` produce **byte-identical output** to the s186 `build_cooc.py`
  (verified by assertion — a battery of inputs + a synthetic `compute_control` case; K, FRAME_WIN,
  CONNECTIVES identical); only the C4 IO adapter (byte-identical to the s193 adapter) and the adjective
  cue/candidate-pool sets differ. **Corpus:** C4 (`allenai/c4` en) shards **00000–00002** streamed and
  discarded (the s193-frozen shard set). Achieved volume asserted ≥ s186's 21.3M sentences / ~320M
  tokens before writing. ODC-BY (+ Common-Crawl terms — travels to the result provenance). **NO Hearst
  arm** (H2 does not transfer; Q2-A). **NB (J&K-relevant):** the conjunction/adjacency frame is exactly
  J&K's measured adjective conjunction frame ("*cold and hot*"), so the control is on its home ground
  here in a way it was not for nouns — a stronger reconstruction test than the noun runs faced.

## Frozen predictor vectors (pre-recovery — legitimate to state; NO model data existed when computed)

*(Computed from `control.json` after the C4 build, still BEFORE any model call — legitimate to state.)*

| relation | cue-strength (frame-G² 𝒮) | cue-strength (sent-G² 𝒮) | control-frame HIT@3 | cues w/ ≥1 control cand |
|---|---|---|---|---|
| antonymy | **0.1214** | 0.1487 | 0.3643 | 129/130 |
| synonymy | 0.0465 | 0.0388 | 0.1240 | 129/130 |
| similar | 0.0462 | 0.0487 | 0.1154 | 130/130 |
| also-see | 0.0615 | 0.0487 | 0.1846 | 130/130 |

**Antonymy has by far the highest cue-strength** (frame-G² 𝒮 0.1214 vs ~0.046–0.062 for the other
three; HIT@3 0.364 vs 0.115–0.185) — the contrastive-frame control recovers antonym relata much better
than any other relation's relata, exactly J&K's measured adjective contrastive-frame saturation. This is
the sharp version of the antonymy-shadow test: the control is genuinely strong on antonymy here, so a
large *model* residual over it is a real clearance, and a small one is a real reconstruction.

**Mean control-frame soundness = 0.0689 (≥ 0.05 floor) → the calibration gate CLEARS** (computed before
any model call). Unlike s186's noun run (mean 0.029, gate fired → residual arm descriptive-only), the
adjective contrastive-frame control is strong enough to be a **powered** comparator, so the
antonymy-shadow **RESIDUAL arm is verdict-bearing here, not descriptive-only** — a material difference
the POS change produced, because the contrastive frame is J&K's home ground for adjectives. (The
frame-ablation arm C1 remains mandatory as an independent corpus-free line.)

## Panel & elicitation (byte-identical to the s186 neutral + frame arms)

Panel = [`config/models.md`](../../../config/models.md) `panel.A/.B/.C` (never hardcode slugs).
Temperature 0, zero-shot, single-turn, neutral system prompt; `google/*` gets
`reasoning={"effort":"minimal"}`. NEUTRAL + FRAME prompts + `parse_words` byte-identical to s186
`probe.py`. **Two arms:** neutral (all 4 relations) + **frame (antonymy only — MANDATORY, C1)**.
`ABORT_USD = 1.20`. Every call records `usage.cost`. Expected ~1,950 calls (1,560 neutral + 390 frame).

## Metrics

- **Recovery 𝒮** (per relation) = mean **Soundness** (Cao precision-over-produced). **HIT@3** =
  gold-size-insensitive co-primary (a hit is a hit regardless of over-production).
- **Cue-strength** (per relation) = mean 𝒮(control top-3, frame variant) — the s186 clause-2 quantity.
- **ρ_cue** = across-relation Spearman (n=4, **tie-naive** — the s186/s193 pipeline) of recovery against
  cue-strength, **per model**.
- **Antonymy-shadow residual** = per-cue HIT@3(model, neutral) − HIT@3(control, frame), bootstrap 95% CI
  (B=2000, seed 20260709).

## Verdict map (FROZEN; direction fixed; C2/C3/C6/C8)

**PRIMARY = the antonymy-shadow clause** (Q1-C). Relation-agnostic, pre-registered RANK+MARGIN rule
(C6), per model, on the HIT@3 residual over the 4 relations (`ANT_NEARZERO = 0.10`):
- **CLEARS** iff antonymy residual ≥ 0.10 **and** ≥ the median of the 4 relation residuals (among the
  largest, clears the control).
- **SATURATES** iff antonymy residual < 0.10 **and** is the smallest of the 4 (near-zero and the
  smallest — the control reconstructs antonym recovery).
- **MIDDLING** otherwise (pre-named null: neither a clean clear nor a clean saturate).
- Aggregate: **ANT-CLEARS-CONTROL** iff CLEARS on ≥2/3; **ANT-SATURATES** iff SATURATES on ≥2/3; else
  **ANT-MIDDLING/MIXED**.

**Calibration gate (C3):** if mean control-frame soundness over all cues **< 0.05**, the antonymy-shadow
**residual** arm is **DESCRIPTIVE-ONLY** and interpretive weight shifts to the frame-ablation arm (C1,
corpus-free) + H1. (s186's analog was 0.029 < 0.05 → fired; a refire is the expected case and is why C1
is mandatory.)

**Frame-ablation arm (C1 + C8, corpus-free — the hedge against the calibration gate):** antonym HIT@3,
neutral (frame-suppressed) vs frame-present. Pre-registered numeric rule (C8, `DELTA_ABLATE = 0.15`):
antonym recovery **SURVIVES-SUPPRESSION** iff HIT@3(neutral) ≥ HIT@3(frame) − 0.15 on ≥2/3 models
(removing the contrastive frame does not collapse recovery — the model is not relying on the frame to
produce antonyms; this re-tests s186's "antonym recovery survives frame suppression" in J&K's home POS).
**FRAME-DEPENDENT** otherwise.

**H1 co-primary (decoupling; C2 exhaustive bands, on primary soundness ρ_cue), reported at true low
power (≤4 relations):**
- **DECOUPLING-REPLICATES** iff ρ_cue **≤ +0.30** on **≥2/3** models.
- **DECOUPLING-BREAKS** iff ρ_cue **> +0.50** on **≥2/3** models (cue-strength recovers its predictive
  power on adjectives — s186/s193's decoupling was noun-specific; fires essay trigger (a) against).
- **H1-PARTIAL/AMBIGUOUS** otherwise (pre-named first-class).
- **C4 asymmetry acknowledged:** on ≤4 points a high-variance ρ near 0 puts more mass under the wide
  REPLICATES band than the narrow BREAKS band, so the across-relation H1 arm **cannot on its own carry
  claim promotion** — promotion rests on the noun replications (s186 + s193) **plus** this POS-crossing
  arm read together, backed by the item-level arm. A REPLICATES here is a *third* replication across
  corpus AND POS, weighed with that caveat.

**Item-level SECONDARY (C7):** pooled (all 520 cues) Spearman of each cue's own contrastive-frame
cue-strength (control-frame soundness) against its own recovery soundness, per model. **DESCRIPTIVE /
ROBUSTNESS-ONLY — NON-DECISIVE; can never on its own fire or break H1.** A divergence between the
across-relation and item-level arms is a pre-named first-class reported outcome.

**Pre-named nulls (first-class):** ρ_cue near-zero **and** the antonymy residual middling; or an
across-vs-item-level divergence (reported, not resolved by fiat). **n = 3 models; orderings, not
coefficients; adjectives only. No pooling across models or across POS.**

## What each outcome feeds

- **ANT-CLEARS + H1 REPLICATES:** the s186 falsification is at its most robust (antonymy is not the
  shadow-saturated relation even where the contrastive-frame saturation is measured-strongest) **and**
  the decoupling holds across a POS boundary — a *third* replication (s186 nouns, s193 fresh nouns+C4,
  s196 adjectives) across corpus AND POS. This is the evidentiary basis for a **promotion review** of the
  decoupling to a `claim` (cross-session, adversarial), read with the ≤4-relation caveat above.
- **ANT-SATURATES:** a clean, first-class POS-boundary result — shadow-saturation holds specifically for
  adjectives, where J&K's premise is measured; the antonymy-outlier essay's reading is re-scoped to the
  POS where it is real, and the noun falsification is bounded, not overturned.
- **H1 BREAKS:** cue-strength predicts recovery on adjectives — trigger (a) fires against; scope the
  decoupling to nouns or retract; blocks the claim promotion.
- **A [`predictions.md`](../../../wiki/predictions.md) row** is registered at freeze (co-registered with
  the existing §B decoupling bet, not double-scored); outcome updated the run session.

## Anti-cheat fence (PROTOCOL §B; the eight conditions)

The fresh disjoint adjective cue sets, the band [2.0,4.5] outlier cap, k=3, the 4-relation inventory,
the ρ_cue bands, the antonymy-residual RANK+MARGIN rule (`ANT_NEARZERO`), the calibration floor
(`CALIB_FLOOR = 0.05`), and the frame-ablation Δ-rule (`DELTA_ABLATE = 0.15`) are **all frozen here
BEFORE any model call**. No band, rule, or threshold is touched after recovery is seen. The
DECOUPLING-BREAKS, ANT-SATURATES, ANT-MIDDLING, and null outcomes are pre-named first-class.

**The eight freeze-time conditions (design + s196 ratification):** C1 frame-ablation MANDATORY · C2
exhaustive H1 bands (no dead-zone) · C3 numeric calibration floor + descriptive-only fallback protocol ·
C4 ≤4-point asymmetry stated (across-relation H1 arm cannot alone carry claim promotion) · C5
similar/synonymy near-duplication contingency (route weight to the item-level arm; tie-naive Spearman
handles ties) · C6 HIT@3 + relation-agnostic RANK+MARGIN rule on the antonymy-shadow primary · C7
item-level arm locked descriptive/robustness-only · **C8 (added s196) the frame-ablation arm has its own
pre-registered numeric decision rule (`DELTA_ABLATE`)**.

**Construct-validity scope caveat (carried, not a gate):** the contrastive-frame G² construction is
byte-frozen from a noun-cue instrument; only the cue POS + candidate pool V (adjectives) differ, verified
by the `_assert_frozen_g2()` battery. Recovery scoring and the G² control share no human key; Q3 stays
internal-contrast-only.
