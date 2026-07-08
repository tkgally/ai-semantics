---
id: lexical-relation-recovery-taxonomic-proxy-design
title: "Fresh relation-recovery / taxonomic-proxy probe (H1 + H2) — the four value-laden gates: level of analysis for H2 (anti-goalpost), the fresh control corpus, the second pre-registered proxy arm, and the internal-contrast-only anchor"
status: open
opened: 2026-07-08
opened-by: session-192
contingent-artifacts:
  - design/lexical-relation-recovery-taxonomic-proxy-v1
---

# Decision: the four value-laden gates of the fresh relation-recovery / taxonomic-proxy probe

## Why this is owed

The essay [`essay/cue-strength-recovery-decoupling`](../../findings/essays/cue-strength-recovery-decoupling.md)
(s187) registered a two-part falsifiable bet ([`predictions.md`](../../predictions.md) §B): **H1** — on
a fresh test, panel relation-recovery rank **again** decouples from raw contrastive-frame co-occurrence
cue-strength; **H2** — recovery rank tracks a **pre-registered taxonomic/definitional-structure proxy**
*better* than it tracks cue-strength. The theory second edition
[`theory/lexicon-grammar-continuum-v2`](../../findings/theory/lexicon-grammar-continuum-v2.md) (s191)
leaves the lexical pole's shadow-saturated corner **unplaced** and names exactly this fresh
relation-recovery probe (with the IS-A-depth proxy) as its re-placement trigger. The taxonomic-proxy
pilot [`note/taxonomic-proxy-recovery-pilot-v1`](../../findings/notes/taxonomic-proxy-recovery-pilot-v1.md)
(s188) did the $0, non-circular due-diligence and **provisionally** pre-registered IS-A path depth.

Turning this bet into a runnable probe forces four choices that *are* value-laden — chiefly **how H2 is
tested without moving the goalposts** (n = 6 relations is severely underpowered, and a powered item-level
test answers a *different* question). So this is a fresh design + decision-trail unit (design landed
s192: [`design/lexical-relation-recovery-taxonomic-proxy-v1`](../../../experiments/designs/lexical-relation-recovery-taxonomic-proxy-v1.md)).
The ratified scoring/anchor gates of the s186 sibling
([`decisions/resolved/antonymy-internal-contrast-scoring`](../resolved/antonymy-internal-contrast-scoring.md):
Q1-C control, Q2-A Soundness/HIT@3 residual, Q3 internal-contrast-only) are **reused, not re-litigated**;
what is genuinely new here is the H2 predictor arm and the freshness routes.

Nothing here changes any finding; it fixes the **yardstick** for a probe that has not run. Ratifying is
eligible from **session 193** (never the opening session), per [`PROJECT.md`](../../../PROJECT.md) §12.3:
independent adversarial review + one non-Anthropic panel vote; Tom's standing override outranks.

> **Pre-run review already on record (s192, design-stage — NOT the ratification).** The design carrying
> these gates cleared a fresh-agent pre-run critic + one non-Anthropic vote, both **GO-WITH-CONDITIONS**,
> fabrication-check PASS ([`REVIEW-design-s192.md`](../../../experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy-design/REVIEW-design-s192.md)).
> **For the s193 ratifier:** both reviewers converged on Q1-C, Q3-A, Q4 internal-contrast-only, but
> **diverged on Q2** — the non-Anthropic vote picked **Q2-B (C4 primary)**, arguing full Wikipedia is
> "too close to the original register" (same source family as s186's Simple Wikipedia) to be a strong
> H1 falsifier; the critic kept Q2-C with a Wikipedia-only scope-cap and "C4 strongly preferred." **Weigh
> whether C4 should be primary/co-primary rather than a sensitivity arm.** Six freeze-time conditions are
> recorded on the design; ratification fixes the gates, the freeze honors the conditions.

## Gate Q1 — level of analysis for H2 (the anti-goalpost-moving gate; load-bearing)

The essay registered H2 as an **across-relation rank** hypothesis (recovery rank vs proxy rank over the
six relations, head-to-head against cue-strength rank). But **n = 6 relations cannot be a significant
Spearman**, and IS-A depth is a **per-cue** property, so a far more powerful **item-level** test exists
(regress a cue's recovery on its own IS-A depth, N ≈ 700–900). Choosing item-level *alone* silently
redefines H2 after the fact. Options:

- **A — across-relation rank only** (6 points). Faithful to the exact registered bet; underpowered.
- **B — item-level cue-depth regression only** (~700–900 items; powered). Powered, but a **different**
  hypothesis (within-relation cue-depth → recovery), and adopting it alone moves the goalposts.
- **C (provisional default) — across-relation rank PRIMARY and verdict-bearing (n = 6, reported with
  its wide CI), PLUS the item-level analysis as a POWERED SECONDARY** reported side-by-side. The
  head-to-head of record stays |ρ(depth, recovery)| vs |ρ(cue-strength, recovery)| across relations,
  ≥2/3 models; the item-level arm buys power and guards an n=6 fluke **without** changing what H2 was
  registered to predict. A **divergence** between the two levels is itself a first-class reported
  outcome.

**Why value-laden:** the choice is *what counts as testing H2*. C keeps the registered bet primary and
must pre-commit that the across-relation result is the verdict of record even if the item-level arm
looks stronger.

## Gate Q2 — the fresh control corpus

H1's falsifier requires a **fresh** test; "a different control corpus" is a named route, and the
cleanest for a noun-relation replication. s186 used **Simple English Wikipedia**. Both candidates below
cleared the s185 license scout firsthand ([`resource/cooccurrence-corpus-scouting`](../../base/resources/cooccurrence-corpus-scouting.md)).
Options:

- **A — full English Wikipedia** (CC BY-SA 4.0 + GFDL). Cleanest license, best pretraining proxy,
  billions of words; but the **same source family** as Simple Wikipedia (encyclopedic register) — a real
  change (≈100× larger, un-simplified) but the weakest register-decorrelation.
- **B — C4** (`allenai/c4`, ODC-BY). Web register, genuinely different; the strongest fresh test, at the
  cost of a heavier fetch (streamable; only the fixed cue set counted).
- **C (provisional default) — full English Wikipedia PRIMARY + C4 as a labelled register-decorrelation
  SENSITIVITY arm** iff tractable within the day's budget/effort; if only one is tractable, Wikipedia is
  primary and the C4 arm is **deferred and named** (an honest scope note, not a silent drop). The
  cue-strength ranking for the head-to-head is Wikipedia's.

**Why value-laden:** how "different" the corpus must be *is* how strong a fresh test H1 gets. The
decision fixes whether register-decorrelation is required for the primary verdict or is a sensitivity
check.

## Gate Q3 — the second pre-registered proxy arm (definitional-frame)

The pilot pre-registered **IS-A path depth** alone, but flagged that the essay's actual
"definitional-frame statistic" means **corpus Hearst-style hypernym frames** (WordNet gloss-length is
only a cheap echo, deliberately *not* frozen by the pilot). Since the Q2 corpus is fetched anyway, a
corpus definitional-frame proxy is nearly free and tests the essay's "it would still be a distributional
story" head-on. Options:

- **A (provisional default) — IS-A path depth PRIMARY (the pilot's frozen spec) + a corpus Hearst-frame
  definitional-density proxy as a SECOND pre-registered arm.** Per the essay, H2 is satisfied if *any*
  pre-registered taxonomic/definitional proxy out-predicts cue-strength (≥2/3); both proxies' specs +
  predicted signs frozen **before** recovery. A pre-registered multiple-comparison rule (H2 fires-for
  only if a **named** proxy wins in its **pre-registered** direction) is set at freeze.
- **B — IS-A path depth only** (simplest; faithful to the single pre-registered proxy; forgoes a
  nearly-free arm and leaves the essay's named definitional-frame candidate untested).
- **C — add the ill-behaved candidates** (subtree connectivity, polysemy). **Rejected up front** by the
  pilot (subtree ≈ fan-out baseline; gloss length a fishing hazard).

**Why value-laden:** whether H2's proxy is operationalized narrowly (one structural primitive) or as the
essay wrote it (structural **or** definitional-frame) changes what can fire H2, and a second arm raises
the multiple-comparison bar the freeze must handle.

## Gate Q4 — the anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — following the s186 Q3 ratification
  exactly. Recovery is scored against WordNet as a **shared definitional target that cancels in the
  head-to-head**; the predictors (contrastive-frame G², IS-A depth, any Hearst proxy) are corpus/lexicon
  **statistics**; no human recovery baseline enters. So the result makes **no human-comparison claim**
  and no `resource` anchor is required (CLAUDE.md terminal state; the s186 gloss-extension —
  internal-contrast covers model-vs-computational-baseline — applies). Per CLAUDE.md this declaration
  needs cross-session ratification, which this decision supplies. Until ratified the design carries
  `anchor: pending` naming this decision in `contingent-on:`.

## Provisional defaults, together

**Q1-C** (across-relation primary + item-level powered secondary) · **Q2-C** (Wikipedia primary + C4
sensitivity arm if tractable) · **Q3-A** (IS-A depth primary + a corpus Hearst-frame second arm) ·
**Q4 internal-contrast-only**. These cohere: Q1-C keeps the registered across-relation bet primary while
buying power; Q2/Q3 make the test genuinely *fresh* (different corpus) and give H2 its best-specified
predictor(s); Q4 certifies the whole thing as a within-instrument predictor comparison with no human
claim. The load-bearing gate is **Q1** — it is the one place goalpost-moving could smuggle in a win.

## Anti-cheat note (for the ratifying reviewer)

The defaults lean *away* from easy confirmation: Q1-C **refuses** to swap the underpowered registered
bet for the powered-but-different item-level test as the verdict of record; Q2 demands a corpus
*different* from s186's so H1 cannot win by same-corpus artifact; Q3's second arm comes with a
pre-registered multiple-comparison rule; every proxy spec, predicted sign, and threshold is frozen in
PREREG **before** recovery; and the H1-break, H2-lose, and both-null outcomes are pre-named first-class
results. The pilot already **refused the exploratory maximum** (gloss length) on principle. Ratification
fixes the yardstick, never the result — if the review is motivated by wanting H2 to win, that is the
anti-cheat violation; stop.

## What ratification unblocks

Fix Q1–Q4 → fetch the Q2 corpus (own resource page + verified license, already scouted) → freeze
`prep.py` (fresh disjoint cues, freq-matched, outlier-capped; byte-frozen s186 G² construction with only
the corpus changed; IS-A depth + any Q3 proxy computed and frozen over the fresh cues) + thresholds +
PREREG → pre-run critic + non-Anthropic vote → run on the panel (powered N ~120–150 cues/relation,
≈ $0.35–0.65) → post-run verifier. Design:
[`design/lexical-relation-recovery-taxonomic-proxy-v1`](../../../experiments/designs/lexical-relation-recovery-taxonomic-proxy-v1.md).
