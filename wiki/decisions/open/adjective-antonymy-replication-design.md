---
id: adjective-antonymy-replication-design
title: "Adjective-antonymy replication probe — the value-laden gates: the adjective relation inventory + registered primary clause, whether to open a NEW adjective-structural bet (H2 does not transfer), and the internal-contrast-only anchor"
status: open
opened: 2026-07-09
opened-by: session-195
contingent-artifacts:
  - design/adjective-antonymy-replication-v1
---

# Decision: the value-laden gates of the adjective-antonymy replication probe

> **OPEN — opened session 195 (2026-07-09), ratifiable session 196+.** Per
> [`PROJECT.md`](../../../PROJECT.md) §12.3 the surfacing session never ratifies its own decision;
> a later session runs the independent adversarial review (fresh reviewer with verdict authority +
> one non-Anthropic decorrelation vote, PROTOCOL §2). Tom's standing override outranks. Provisional
> defaults below: **Q1-C / Q2-A / Q3 internal-contrast-only.** The design
> [`design/adjective-antonymy-replication-v1`](../../../experiments/designs/adjective-antonymy-replication-v1.md)
> carries `anchor: pending` and names this decision in `contingent-on:` until ratified.

## Why this is owed

The design [`design/adjective-antonymy-replication-v1`](../../../experiments/designs/adjective-antonymy-replication-v1.md)
operationalizes [`essay/cue-strength-recovery-decoupling`](../../findings/essays/cue-strength-recovery-decoupling.md)'s
registered **H1** (revision trigger (a)'s named **adjective-antonymy replication** route) and
[`essay/antonymy-outlier-distributional-shadow`](../../findings/essays/antonymy-outlier-distributional-shadow.md)'s
contrastive-frame premise, re-tested in the POS where Justeson & Katz actually **measured**
contrastive-frame saturation ([`source/justeson-katz-1991-antonym-cooccurrence`](../../base/sources/justeson-katz-1991-antonym-cooccurrence.md)):
**predicative adjectives**. s186 ([`result/lexical-relation-shadow-saturation-v1`](../../findings/results/lexical-relation-shadow-saturation-v1.md))
and s193 ([`result/lexical-relation-recovery-taxonomic-proxy-v1`](../../findings/results/lexical-relation-recovery-taxonomic-proxy-v1.md))
both stand on **nouns only**, where the J&K source page says the contrastive-frame premise is an
*"extrapolation beyond J&K's data."* Turning that gap into a runnable probe forces three value-laden
choices. Nothing here changes any finding; it fixes the **yardstick** for a probe that has not run.

## Gate Q1 — the adjective relation inventory + the registered primary clause

WordNet's adjective relations are fewer and less standard than the noun taxonomy (in-band feasibility
measured s195: antonymy 701, synonymy 2238, similar-to 4538, also-see 698 cues with a single-word
in-band relatum). Two coupled questions: **which relations** enter the across-relation decoupling arm,
and **which clause** is the registered verdict of record.

- **Q1-A — antonymy + synonymy only** (2 relations). Cleanest, but a 2-point across-relation Spearman is
  degenerate — the decoupling arm cannot carry H1; antonymy-shadow clause would be the only real test.
- **Q1-B — antonymy + synonymy + similar-to + also-see** (4 relations). Enough points for a (weak) rank
  test of the decoupling, closest to s186's structure. Risk: `similar_to`/`synonymy` near-duplicative;
  `also_see` least-standard. Decoupling (H1) primary; antonymy-shadow co-primary.
- **Q1-C (provisional default) — the 4-relation set for the across-relation decoupling arm, with the
  ANTONYMY-SHADOW clause as the registered PRIMARY and the decoupling (H1) as a REGISTERED CO-PRIMARY
  reported at its true low power**, plus the item-level cue-strength→recovery arm (~400–800 cues) as a
  POWERED SECONDARY (the s193 Q1-C discipline: descriptive/robustness-only, can never on its own fire
  H1). Rationale: the antonymy-shadow clause is the sharpest adjective-specific test (J&K's home POS,
  one well-defined relation, independent of the thin relation count), so it carries primary weight; the
  4-relation decoupling arm is reported honestly as underpowered (≤4 points) and backed by the item-level
  arm. An across-relation vs item-level **divergence** is a first-class reported outcome.

**Why value-laden:** the adjective inventory forces a trade between a faithful-but-degenerate 2-relation
test and a fuller-but-noisier 4-relation one, and a choice of which clause is primary. Q1-C must
pre-commit that a small-inventory decoupling result is reported at its true (low) power, never dressed up.

## Gate Q2 — a structural-proxy arm for adjectives? (H2 does NOT transfer)

H2's frozen proxy — **IS-A path depth** ([`note/taxonomic-proxy-recovery-pilot-v1`](../../findings/notes/taxonomic-proxy-recovery-pilot-v1.md))
— is **undefined for adjectives**: WordNet has no adjective IS-A taxonomy (adjectives are organized by
antonymy + satellite `similar_to` clustering). So this route **cannot replicate H2**; the question is
whether to open a *new* adjective-structural bet or run H1-only.

- **Q2-A (provisional default) — NO structural-proxy arm; run H1-only, and state explicitly on the
  result that the adjective route discharges H1 but by construction cannot replicate H2.** Keeps the
  unit lean and the pre-registration undiluted; the s193 noun run stays the sole H2 evidence.
- **Q2-B — open a NEW pre-registered adjective-structural bet** (e.g. satellite-vs-head position or
  cluster centrality in the `similar_to` graph) as a fresh proxy with its own predicted sign, frozen
  before recovery. **Not** an H2 replication — a new conjecture in a new POS, needing its own
  predictions.md row; far weaker a-priori motivation than IS-A depth (no "genus a definition names
  first" story) and a multiple-comparison burden.
- **Q2-C — reject up front:** import a noun IS-A depth for adjectives via derivational/pertainym links
  (score "cold" through its noun "coldness"). **Rejected** — smuggles a noun taxonomy onto adjective
  cues through a lossy arbitrary hop, exactly the post-hoc proxy construction the pilot's anti-fishing
  discipline forbids.

**Why value-laden:** whether the unit stays a clean single-hypothesis (H1) replication or takes on a
new, weakly-motivated structural bet. The default (Q2-A) protects the H1 claim-promotion route from
multiple-comparison dilution and refuses to overstate the unit as an "H2 beyond nouns" test.

## Gate Q3 — the anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — following s186 Q3 / s193 Q4 exactly.
  Recovery is scored against WordNet as a **shared definitional target that cancels in the contrast**;
  the predictor (contrastive-frame G²) is a corpus statistic; no human recovery baseline enters, so the
  result makes **no human-comparison claim** and no `resource` anchor is required (CLAUDE.md terminal
  state; the s186 model-vs-computational-baseline gloss-extension applies). Per CLAUDE.md this terminal
  declaration needs cross-session adversarial ratification — which this decision supplies. Until ratified
  the design carries `anchor: pending` naming this decision in `contingent-on:`.

## Provisional defaults, together

**Q1-C** (4-relation decoupling arm; antonymy-shadow clause primary + decoupling co-primary at true
power; powered item-level secondary) · **Q2-A** (no structural-proxy arm; H1-only; state H2 does not
transfer) · **Q3 internal-contrast-only**. These cohere: Q2-A keeps the probe a clean H1 replication +
antonymy-shadow re-test, which is exactly what Q3's internal-contrast-only certifies, and Q1-C fixes the
antonymy-shadow clause — the one adjective test independent of the thin relation count — as the primary.

## What ratification unblocks

Fix Q1–Q3 → freeze `prep.py` (fresh disjoint adjective cues, freq-matched, outlier-capped; byte-freeze
the s193 contrastive-frame G² construction, only the cue POS changing; recompute G² over the adjective
cues on the frozen C4 shards) + *k* + relation inventory + per-relation N + ρ-band + antonymy-residual
thresholds + calibration floor + PREREG before any model call → independent pre-run critic + one
non-Anthropic vote → run on the panel (powered N ~120–150 cues/relation, ≈ $0.25–0.55) → post-run
verifier. Design: [`design/adjective-antonymy-replication-v1`](../../../experiments/designs/adjective-antonymy-replication-v1.md).
