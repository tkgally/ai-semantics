---
type: result
id: lexical-relation-recovery-verb-decoupling-v1
title: "The cue-strength–recovery decoupling does NOT reappear on verbs — it BREAKS (2/3): despite a verified troponymy hierarchy, verb recovery rank RE-tracks contrastive-frame cue-strength (ρ_cue +0.49/+0.60/+0.54), falsifying the POS-hierarchy conjecture; H2 depth arm pre-registered UNDER-POWERED (internal-contrast)"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-09
updated: 2026-07-09
links:
  - rel: operationalizes
    target: design/lexical-relation-recovery-verb-decoupling-v1
  - rel: contradicts
    target: conjecture/decoupling-lexical-hierarchy-pos-generality
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: result/adjective-antonymy-replication-v1
  - rel: depends-on
    target: claim/lexical-relation-recovery-cue-strength-decoupling
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: resource/cooccurrence-corpus-scouting
---

# Result — verb-relation decoupling probe (H-verb-1 + H-verb-2)

> **Status: proposed (reading-bearing result; s199, 2026-07-09). VERDICT: DECOUPLING-BREAKS (2/3) —
> the third-point verb test FALSIFIES [`conjecture/decoupling-lexical-hierarchy-pos-generality`](../conjectures/decoupling-lexical-hierarchy-pos-generality.md).**
> **H-verb-1 — DECOUPLING-BREAKS (2/3).** On a fresh verb-relation recovery probe (fresh cues disjoint
> from all prior sets; the byte-frozen s193 C4 contrastive-frame G² control, only the cue POS → verbs),
> across-relation recovery rank **re-tracks** contrastive-frame cue-strength: ρ_cue = **+0.49 / +0.60 /
> +0.54** (A inconclusive in the +0.30–0.50 gap; B and C clearly positive, > +0.50). The gold-size-
> insensitive **HIT@3** co-primary is even more strongly positive (ρ_cue = **+0.71 / +0.77 / +0.54**).
> So a part of speech that **has** a lexical hierarchy (WordNet troponymy — verified non-degenerate,
> `min_depth` 0–12) still shows cue-strength predicting recovery — verbs pattern like **adjectives**, not
> like nouns. This fires the conjecture's falsifier 1/3: **the central identification (decoupling ⇔
> lexical hierarchy) collapses.**
> **H-verb-2 — DEPTH-FAILS, and pre-registered UNDER-POWERED (B1/B2).** The troponymy-depth proxy did
> not out-predict cue-strength (ρ_depth = +0.26 / +0.03 / +0.09 — the *wrong* sign for the predicted
> negative, 0/3 clear the 0.20 margin). But the depth arm was frozen **UNDER-POWERED before any model
> call**: the non-antonymy CORE-4 mean-depth range is **0.277 < 0.50** (degenerate; B1), so H2 is
> **non-falsifying** — it cannot cleanly fire the mechanism-falsifier, and it is moot here anyway because
> the decoupling itself did not reappear.
> `anchor: internal-contrast-only` (ratified s199): the force is a within-instrument comparison of *which
> corpus/lexicon statistic rank-predicts recovery* — **no human comparison**. An independent post-run
> verifier **REPRODUCED** every figure from raw (max ρ discrepancy 0.0004, storage rounding only).

**This is a first-class NEGATIVE result — the sharpest outcome the design pre-named.** It is *one point in
a three-point pattern* (nouns / adjectives / verbs), not an isolation of any single cause: verbs confound
POS with hierarchy exactly as nouns do (they carry their own aspect/argument-structure differences), so
DECOUPLING-BREAKS is the clean falsifier, not a demonstration that hierarchy is irrelevant. It does **not**
touch the nouns-only [`claim/lexical-relation-recovery-cue-strength-decoupling`](../claims/lexical-relation-recovery-cue-strength-decoupling.md)
(which was always noun-scoped, H1-only, internal-contrast) — if anything it **vindicates that claim's
deliberate narrowness**.

Design [`design/lexical-relation-recovery-verb-decoupling-v1`](../../../experiments/designs/lexical-relation-recovery-verb-decoupling-v1.md);
gates ratified s199 ([`decisions/resolved/verb-relation-decoupling-design`](../../decisions/resolved/verb-relation-decoupling-design.md):
**Q1-C / Q2-A / Q3 internal-contrast-only**, + binding conditions **B1–B3**). Frozen `PREREG.md` + a
freeze-stage pre-run critic (**GO**; the non-Anthropic freeze vote's NO-GO overruled on the merits) + an
independent post-run verifier (**REPRODUCED**) under
[`experiments/runs/2026-07-09-verb-relation-decoupling/`](../../../experiments/runs/2026-07-09-verb-relation-decoupling/).

## What ran

A fresh relatum-production probe over **six** WordNet **verb** relations, on the
[`config/models.md`](../../../config/models.md) panel (`panel.A` claude-sonnet-4.6, `.B` gpt-5.4-mini,
`.C` gemini-3.5-flash), temperature 0, one neutral (frame-suppressed) arm + an antonymy frame-ablation
hedge. 776 verdict-bearing fresh cues, POS-agnostic-surface disjoint from the 1,740 prior cue lemmas
(s186 nouns + s193 fresh nouns + s196 adjectives); frequency-matched (Lg10WF band [2.0,4.5]) to antonymy's
fresh profile. **`cause` was included as a sixth relation by the frozen mechanical rule** (achieved
matched-N 126 ≥ 100). 2,718 calls, **$0.5115** billed, 0 empties.

**Relation inventory + frozen predictors (pre-recovery):**

| relation | N | recovery 𝒮 (A/B/C) | HIT@3 (A/B/C) | cue-strength (frame-G²) | troponymy-depth |
|---|---|---|---|---|---|
| hypernymy | 130 | 0.408 / 0.350 / 0.413 | 0.76 / 0.68 / 0.77 | 0.0207 | 2.192 |
| synonymy | 130 | 0.292 / 0.265 / 0.281 | 0.58 / 0.54 / 0.55 | 0.0308 | 2.208 |
| antonymy | 130 | 0.280 / 0.278 / 0.292 | 0.78 / 0.78 / 0.76 | **0.0923** | 1.577 |
| troponymy | 130 | 0.195 / 0.180 / 0.187 | 0.42 / 0.38 / 0.42 | 0.0487 | 2.431 |
| cause | 126 | 0.103 / 0.112 / 0.098 | 0.25 / 0.26 / 0.22 | 0.0106 | 1.690 |
| entailment | 130 | 0.097 / 0.092 / 0.115 | 0.26 / 0.23 / 0.31 | 0.0051 | 2.154 |

**Recovery ordering (all three models): hypernymy > {synonymy ≈ antonymy} > troponymy > {cause, entailment}.**

## Why the decoupling breaks on verbs (leave-one-out diagnosis, verifier-confirmed)

The positive ρ_cue is **not** a single-relation artifact. It is carried by the joint **bottom-alignment
of entailment and cause** — the two sparsest verb relations, which are simultaneously the two
lowest-cue-strength (0.0051, 0.0106) *and* the two lowest-recovery relations. The noun-style **disaligner
is still present**: **hypernymy** is low-cue-strength (0.0207) yet the **best-recovered** relation on all
three models — exactly the "a taxonomically central, cheaply-cued relation is best recovered" scramble
that carried the *noun* decoupling. But on verbs it is one relation against a field that otherwise aligns
cue-strength with recovery, and it is **outvoted**. Leave-one-out (verifier): dropping entailment or cause
collapses ρ_cue to ≈ 0.10–0.30; dropping hypernymy *raises* it to 0.7–0.9; dropping any other relation
leaves ρ_cue ≥ +0.50. So cue-strength regains rank-predictive power on verbs despite the verified verb
hierarchy — the pre-named DECOUPLING-BREAKS.

The reading of the falsification is therefore **specific, not sweeping**: it is not that verb recovery is
insensitive to taxonomic structure (hypernymy's chart-topping recovery says otherwise), but that on the
verb relation inventory the taxonomic scramble is **not strong enough to decouple the overall rank** from
cue-strength — the sparse, weakly-cued, weakly-recovered relations (entailment, cause) re-align the two.

## What this falsifies, and what it does not

- **Falsifies [`conjecture/decoupling-lexical-hierarchy-pos-generality`](../conjectures/decoupling-lexical-hierarchy-pos-generality.md)
  (registered s197).** The conjecture's central identification — *the decoupling co-varies with the
  presence of a lexical hierarchy, POS by POS; it reappears in any POS with an IS-A-like backbone and
  vanishes in any without* — predicted the decoupling would **reappear on verbs** (ρ_cue ≤ +0.30, ≥2/3).
  It did not (ρ_cue > +0.50 on 2/3; the adjective band). A POS that *has* a hierarchy still shows
  cue-strength predicting recovery. The conjecture is **retired (falsified)**; the noun/adjective contrast
  is **not** explained by hierarchy-presence alone.
- **Does NOT touch the nouns-only [`claim/lexical-relation-recovery-cue-strength-decoupling`](../claims/lexical-relation-recovery-cue-strength-decoupling.md).**
  That claim was already nouns-only, H1-only, internal-contrast, no-magnitude, with the cross-POS claim
  **blocked** (s196). This result adds a **second** POS (verbs, after adjectives) where the clean
  decoupling is absent — reinforcing that the clean decoupling is a **noun-specific** phenomenon and
  vindicating the claim's deliberate narrowness. The claim's `supported` status is unchanged.
- **Leaves H2 (the depth mechanism) untested on verbs.** The troponymy-depth arm was pre-registered
  UNDER-POWERED (B1: the non-antonymy CORE-4 depth spread is degenerate, range 0.277 < 0.50, because four
  of the five core relations cluster near depth ≈ 2.2 and only antonymy — confounded with its cue-strength
  — is shallow). So DEPTH-FAILS here is **non-falsifying**, and a DEPTH-OUT-PREDICTS would likewise have
  been flagged not-noun-equivalent (B2). The verb probe cannot say whether the taxonomic-depth mechanism
  transfers; it says the *decoupling* does not.

## Scope caps (LOAD-BEARING — read before citing)

1. **Internal-contrast only** (Q3, ratified). No human comparison. The head-to-head is *which
   form-internal statistic (contrastive-frame cue-strength vs troponymy-depth) tracks recovery* — a
   within-instrument comparison.
2. **One point in a three-point pattern, not an isolation** (B3). Verbs confound POS with hierarchy as
   nouns do; DECOUPLING-BREAKS is the clean falsifier of "hierarchy ⇒ decoupling," **not** a demonstration
   that hierarchy is causally irrelevant (hypernymy's top recovery shows taxonomic structure still
   matters within-POS). Read alongside the noun and adjective points; never merged with them.
3. **The break leans on two thin-signal relations** (verifier flag). Dropping entailment or cause collapses
   ρ_cue; the effect is a genuine data feature of the verb relation inventory (its two sparsest relations
   sit jointly at the bottom of both rankings), disclosed, not eliminated. A is INCONCLUSIVE (ρ_cue 0.486),
   so the break is 2/3, not 3/3, on soundness — though 3/3 on the HIT@3 co-primary.
4. **n = 3 models; orderings, not coefficients; VERBS only.** Never pooled across models or POS.
5. **Within-distributional only.** Cue-strength re-predicting recovery is *one form-internal statistic
   tracking another*, never recovery escaping distribution
   ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)'s "silent on
   reference and truth" caveat untouched).
6. **Hypernymy gold-size confound** (carried from s186/s193): hypernymy median gold ≈ 10 vs antonymy's ≈ 1,
   so its recovery advantage is partly a gold-size artifact — mitigated by the HIT@3 co-primary (on which
   hypernymy is still high but antonymy ties it), disclosed, not eliminated. Gold is all-sense while the
   depth proxy is first-synset (byte-identical to the noun run).

## What each outcome feeds

- **The POS-structural conjecture is retired.** "What makes the noun decoupling clean" is **reopened** with
  hierarchy-presence ruled out as the *sole* determinant. A candidate the data suggest: the decoupling is
  clean when the relation inventory has a strongly-recovered, low-cue-strength taxonomic relation **and
  lacks** sparse low-recovery/low-cue-strength relations that re-align the tail — a *finer* structural
  story than "has a hierarchy," and one this result does not itself establish (a bet, not a finding).
- **The essay's POS-generality speculation is revised** (a dated box on
  [`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md)): the noun
  reading stands (claim layer), the cross-POS generalization is now **falsified on both non-noun POS**.
- **A [`predictions.md`](../../predictions.md) outcome** is recorded (the s197 conjecture bet →
  fired-against/falsified; co-registered, not double-scored).
- **No new conjecture is spawned this session** — the reopened "what carries the clean decoupling" question
  is logged as a candidate refinement, not registered as a bet, pending a design that could separate the
  tail-alignment reading from hierarchy without confounding POS.
