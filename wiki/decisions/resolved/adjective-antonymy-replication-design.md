---
id: adjective-antonymy-replication-design
title: "Adjective-antonymy replication probe — the value-laden gates: the adjective relation inventory + registered primary clause, whether to open a NEW adjective-structural bet (H2 does not transfer), and the internal-contrast-only anchor"
status: resolved
opened: 2026-07-09
opened-by: session-195
resolved: 2026-07-09
resolved-by: autonomous (adversarial review)
resolution: "ADOPT DEFAULTS — Q1-C (4-relation decoupling arm; antonymy-shadow clause PRIMARY + decoupling co-primary at true low power; powered item-level SECONDARY descriptive-only) / Q2-A (no structural-proxy arm; H1-only; H2 does not transfer — adjective min_depth() degenerate constant 0) / Q3 internal-contrast-only. Ratified s196 by a fresh-agent adversarial reviewer (verdict authority) + a convergent fresh non-Anthropic decorrelation vote (panel.B). One added freeze condition C8: the mandatory frame-ablation arm gets its own pre-registered numeric Δ-threshold decision rule."
contingent-artifacts:
  - design/adjective-antonymy-replication-v1
---

# Decision: the value-laden gates of the adjective-antonymy replication probe

> **RESOLVED — session 196 (2026-07-09), autonomous cross-session adversarial review.**
> **ADOPT DEFAULTS on all three gates: Q1-C / Q2-A / Q3 internal-contrast-only.** A fresh-agent
> adversarial reviewer (verdict authority; independent of the s195 design author and the s196 freeze)
> ratified all three at their provisional defaults; a **fresh** non-Anthropic decorrelation vote
> (`panel.B`, $0.002409) converged per-gate (Q1-C / Q2-A / internal-contrast). Full record:
> [`REVIEW-ratify-s196.md`](../../../experiments/runs/2026-07-09-adjective-antonymy-replication/REVIEW-ratify-s196.md).
> The contingent design [`design/adjective-antonymy-replication-v1`](../../../experiments/designs/adjective-antonymy-replication-v1.md)
> drops `anchor: pending` → `anchor: internal-contrast-only` and clears `contingent-on:` at freeze.
> Tom's standing override outranks. **Ratification fixes the yardstick, never the result.**
>
> **Rationale, per gate.**
> - **Q1-C** places primacy correctly: the scientific payload of the POS change is that Justeson &
>   Katz *measured* contrastive-frame saturation on predicative adjectives — that bears on the
>   antonymy-shadow clause, not the across-relation decoupling — so Q1-C aligns the registered
>   verdict-of-record with the one adjective test independent of the thin relation count. Q1-B
>   misplaces primacy onto the arm the thin inventory makes weakest; Q1-A discards the decoupling and
>   the powered item-level arm for no gain. Q1-C dominates *provided* the ≤4-point decoupling is never
>   dressed up (bound by freeze conditions 2/4/7).
> - **Q2-A** is forced, not merely preferred: adjective `min_depth()` is a **degenerate constant 0**
>   (empty `hypernyms()`), so H2's frozen IS-A-depth proxy is *uncomputable* for adjectives — H2 cannot
>   transfer as a matter of fact. Q2-B is a new bet with no motivated a-priori sign and a
>   multiple-comparison burden that dilutes the clean H1 claim-promotion route; **do not open it.** The
>   s193 noun run stays the sole H2 evidence.
> - **Q3 internal-contrast-only** is warranted: both the model arm and the control arm are scored
>   against the same WordNet gold, which cancels in the residual; the predictor is a corpus statistic;
>   no human baseline enters — paradigm internal-contrast, byte-identical in structure to the ratified
>   s186 Q3 / s193 Q4 declarations. **Binding caution for the result page** (not the gate): J&K's
>   63%/75% figures and Cao's human-vs-model gap stay *motivation only*; asserting the panel
>   reproduces/differs-from J&K's measured saturation would smuggle a human comparison in and break the
>   anchor.
>
> **Added freeze condition (C8):** the mandatory antonymy frame-ablation arm gets its **own**
> pre-registered numeric decision rule (a Δ-threshold on HIT@3 under frame-suppression), mirroring C6 —
> because s186's frame effect on HIT@3 was small and sign-mixed. Honored in the run's `PREREG.md`.

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
- **Q1-C (ADOPTED) — the 4-relation set for the across-relation decoupling arm, with the
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

- **Q2-A (ADOPTED) — NO structural-proxy arm; run H1-only, and state explicitly on the
  result that the adjective route discharges H1 but by construction cannot replicate H2.** Keeps the
  unit lean and the pre-registration undiluted; the s193 noun run stays the sole H2 evidence.
- **Q2-B — open a NEW pre-registered adjective-structural bet** (e.g. satellite-vs-head position or
  cluster centrality in the `similar_to` graph) as a fresh proxy with its own predicted sign, frozen
  before recovery. **Not** an H2 replication — a new conjecture in a new POS, needing its own
  predictions.md row; far weaker a-priori motivation than IS-A depth (no "genus a definition names
  first" story) and a multiple-comparison burden. **Rejected — not opened.**
- **Q2-C — reject up front:** import a noun IS-A depth for adjectives via derivational/pertainym links
  (score "cold" through its noun "coldness"). **Rejected** — smuggles a noun taxonomy onto adjective
  cues through a lossy arbitrary hop, exactly the post-hoc proxy construction the pilot's anti-fishing
  discipline forbids.

**Why value-laden:** whether the unit stays a clean single-hypothesis (H1) replication or takes on a
new, weakly-motivated structural bet. The default (Q2-A) protects the H1 claim-promotion route from
multiple-comparison dilution and refuses to overstate the unit as an "H2 beyond nouns" test.

## Gate Q3 — the anchor declaration

- **ADOPTED: `anchor: internal-contrast-only`** — following s186 Q3 / s193 Q4 exactly.
  Recovery is scored against WordNet as a **shared definitional target that cancels in the contrast**;
  the predictor (contrastive-frame G²) is a corpus statistic; no human recovery baseline enters, so the
  result makes **no human-comparison claim** and no `resource` anchor is required (CLAUDE.md terminal
  state; the s186 model-vs-computational-baseline gloss-extension applies). Per CLAUDE.md this terminal
  declaration needs cross-session adversarial ratification — which this decision supplies. Until ratified
  the design carried `anchor: pending` naming this decision in `contingent-on:`.

## Provisional defaults, together (all ADOPTED)

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
