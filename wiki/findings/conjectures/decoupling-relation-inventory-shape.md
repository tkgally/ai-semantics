---
type: conjecture
id: decoupling-relation-inventory-shape
title: "What carries the noun cue-strength–recovery decoupling is the SHAPE of the relation inventory, not the presence of a hierarchy: the clean decoupling needs both a low-cue-strength/high-recovery head disaligner AND a tail whose worst-recovered relations are NOT the lowest-cue-strength ones"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: proposed
contingent-on: []
created: 2026-07-10
updated: 2026-07-10
links:
  - rel: refines
    target: essay/cue-strength-recovery-decoupling
  - rel: depends-on
    target: result/lexical-relation-recovery-verb-decoupling-v1
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: result/adjective-antonymy-replication-v1
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: claim/lexical-relation-recovery-cue-strength-decoupling
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Conjecture: the decoupling is a relation-inventory-shape effect, not a hierarchy-presence effect

> **A registered bet (status `proposed`), spawned s200 from the reopened question the s199 verb
> falsification left standing.** It is the successor to the retired
> [`conjecture/decoupling-lexical-hierarchy-pos-generality`](decoupling-lexical-hierarchy-pos-generality.md)
> (falsified s199): where that conjecture said *decoupling ⇔ a lexical hierarchy exists*, this one says
> the hierarchy was only **one of two** conditions, and names the second. It is `internal-contrast-only`
> in spirit (like its parent essay): the head-to-head is *which corpus/lexicon statistic rank-predicts
> recovery*, a within-instrument comparison — **no human comparison, no claim that recovery escapes
> distribution**. It carries no `anchors` link (a conjecture never does); the eventual result should seek
> the terminal `internal-contrast-only` declaration, not a pending human anchor. **This bet is at genuine
> risk of unfalsifiable re-description** (with six relations and three descriptive features one can always
> partition a scatter after the fact); the confirm/falsify section is written to force a *fresh-inventory*
> test that the s186/s193/s196/s199 data cannot themselves settle, and to keep the within-data pattern as
> corroboration, never as the decisive evidence.

## Where this comes from — the three-point pattern the hierarchy story could not fit

The [`essay/cue-strength-recovery-decoupling`](../essays/cue-strength-recovery-decoupling.md) found, on
nouns, that raw contrastive-frame co-occurrence cue-strength does **not** rank-predict which WordNet
relations the frontier panel recovers (across-relation Spearman ρ_cue ≈ **−0.086** at s186,
[`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md);
≈ **+0.09** on a fresh corpus family at s193,
[`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md)).
The now-retired POS-hierarchy conjecture read this as the signature of a **lexical hierarchy** and bet the
decoupling would reappear on any POS with an IS-A-like backbone. Three POS have now been probed, and the
hierarchy story fails to sort them:

| POS | has IS-A hierarchy? | clean decoupling? | ρ_cue (across-relation) |
|---|---|---|---|
| nouns (s186 / s193) | **yes** (hypernymy) | **YES** | −0.086 / +0.09 |
| adjectives (s196) | **no** (`min_depth` degenerate 0) | **no** (H1-PARTIAL) | +0.4 / +0.8 / +0.4 |
| verbs (s199) | **yes** (troponymy, `min_depth` 0–12) | **no** (DECOUPLING-BREAKS 2/3) | +0.49 / +0.60 / +0.54 |

Verbs are the point that breaks "hierarchy ⇒ decoupling": they **have** a verified hierarchy yet pattern
with adjectives, not nouns
([`result/lexical-relation-recovery-verb-decoupling-v1`](../results/lexical-relation-recovery-verb-decoupling-v1.md)).
So hierarchy-presence is **not** the determinant. But the verb result's own leave-one-out diagnosis
(verifier-confirmed) points at what is: the noun-style **head disaligner is still present on verbs** —
hypernymy is low-cue-strength (frame-G² 0.0207) yet the **best**-recovered verb relation on all three
models — but it is **outvoted** by the joint **bottom-alignment of entailment and cause**, the two
sparsest verb relations, which are simultaneously the two **lowest-cue-strength** (0.0051, 0.0106) *and*
the two **lowest-recovery** relations. Dropping entailment or cause collapses ρ_cue to ≈ 0.10–0.30;
dropping hypernymy *raises* it to 0.7–0.9. The break is a **tail** effect, not a missing head.

## The two-condition statement

> The across-relation cue-strength–recovery decoupling (ρ_cue near zero or negative) is a property of the
> **shape of the relation inventory** — the joint scatter of (contrastive-frame cue-strength, panel
> recovery) across the POS's relations — and requires **both** of the following, not merely a hierarchy:
>
> - **(C1) A head disaligner.** At least one relation that is **low in contrastive-frame cue-strength yet
>   high in recovery** — pulling the top of the recovery ranking away from the top of the cue-strength
>   ranking. Taxonomic centrality supplies it: **hypernymy** is the head disaligner in *both* nouns and
>   verbs (low-cue, best-recovered). Adjectives have none — their most-cued relation (antonymy) is *also*
>   their best-recovered, so the head is aligned.
> - **(C2) No aligned tail.** The **worst-recovered** relations must **not** sit at the
>   **cue-strength floor** — must not also be the lowest-cue-strength relations. When the recovery-tail is
>   instead off the floor (up to a **cue-strength-rich**, *anti*-aligned tail), it reinforces the
>   decoupling; when the recovery-tail *is* the cue-strength floor (an *aligned* tail), it re-tracks
>   recovery with cue-strength and can outvote the head disaligner.
>
> The clean decoupling appears **iff both C1 and C2 hold**. The retired conjecture captured only C1
> (via "has a hierarchy"). Verbs satisfy C1 but **violate C2** (their worst-recovered relations,
> entailment and cause, are their lowest-cue-strength ones) → the decoupling breaks. Adjectives violate
> C1 → it never forms. Only nouns satisfy both → the clean decoupling is, among the three POS tested,
> noun-specific — **but the account predicts it is inventory-shape-specific, not POS-specific**: any
> inventory (a new POS, a different language, a re-composed relation set) that satisfies C1 ∧ C2 should
> decouple, and any that violates C2 should not, *regardless of whether it has a hierarchy.*

The single most discriminating feature between the decoupling (nouns) and its break (verbs), given that
both satisfy C1, is therefore **where the worst-recovered relations sit in the cue-strength ordering**.
Read this on the **same metric and corpus family for both POS** — contrastive-frame **G² on C4** (the
s193 noun run and the s199 verb run share it) — so the comparison is same-scale, not a mix of summaries:

- **Nouns (s193, frame-G² on C4).** The cue-strength floor is **synonymy (0.006)** and **hypernymy
  (0.008)** — and hypernymy, at the floor, is the **best**-recovered relation (the C1 head disaligner).
  The **worst**-recovered relations, **meronymy (0.019)** and **holonymy (0.031)**, sit **off** that floor
  (mid-pack; holonymy is in fact among the more-cued). So the recovery-tail is **not** the cue-strength
  floor → **C2 holds**.
- **Verbs (s199, frame-G² on C4).** The cue-strength floor is **entailment (0.0051)** and **cause
  (0.0106)** — and those two are the **worst**-recovered relations, while hypernymy (0.0207), just off the
  floor, is again best-recovered. So the recovery-tail **is** the cue-strength floor → **C2 fails**, and
  it outvotes the head disaligner (s199 leave-one-out: dropping entailment or cause restores ρ_cue ≈
  0.10–0.30).

That flip — *does the recovery-tail coincide with the cue-strength floor?* — not the presence or absence of
a hierarchy, is where the two POS part. (On the earlier s186 noun corpus the same rank fact reads even more
sharply under that run's **control-𝒮** summary, where meronymy/holonymy are the *second*/third-most-cued of
the six — an outright anti-aligned tail; but that is a *different* contrastive-frame summary on a different
corpus, so the load-bearing statement is the **within-POS rank** one above on the shared frame-G²/C4 scale,
not a same-scale magnitude claim across summaries.)

## Why this is a real advance over the retired conjecture, not a rename

The retired conjecture's mechanism was *the head*: "a taxonomically central, cheaply-cued relation is
best-recovered, and that scramble carries the decoupling." The verb data show that **head mechanism is
still operating where the decoupling is absent** (hypernymy tops verb recovery too), so the head cannot be
the whole story. This conjecture keeps C1 as *necessary* but demotes it from *sufficient*, and adds C2 as
the condition the retired bet silently assumed. That is a genuine content change with a different, sharper
falsifier (below): it forbids a specific configuration — C1-satisfying-but-C2-violating inventories that
decouple, or C2-satisfying inventories with a head disaligner that do not.

## What would confirm

Read orderings, not coefficients (n = 3 models). The decisive evidence must come from a **fresh inventory
the current three POS did not fit to** — the within-data pattern below is corroboration only.

1. **Forward test (the load-bearing one).** On a **fresh, pre-registered** relatum-recovery probe over a
   relation inventory chosen *before recovery is observed* to satisfy **C1 ∧ C2** — a head disaligner
   present, and the low-recovery relations not the lowest-cue-strength — the across-relation decoupling
   **appears** (ρ_cue ≤ +0.30 on ≥2/3 models), and on a matched inventory chosen to **violate C2** (a head
   disaligner present, but low-cue-strength relations deliberately placed at the recovery tail) it does
   **not** (ρ_cue clearly positive, ≥2/3). Candidate fresh inventories that dissociate the two conditions
   *without confounding POS*: a within-noun **sub-inventory contrast** (the same POS, two relation sets
   differing only in whether the recovery-tail is cue-strength-rich); a **cross-linguistic** replication
   (program A6) where a language's relation inventory has a different cue-strength profile; or a POS/language
   whose hierarchy co-occurs with a cue-strength-poor tail (predicting a *break*, against the retired bet's
   intuition).
2. **Within-data corroboration ($0, not decisive).** The already-measured noun and verb scatters
   **instantiate** C1 ∧ C2: nouns satisfy both (documented cue-strength/recovery numbers above; the
   decoupling holds 3/3 over two corpora), verbs satisfy C1 and violate C2 (the s199 leave-one-out:
   removing the aligned tail entailment+cause restores ρ_cue ≈ 0.10–0.30). This shows the account **fits**
   the three points it was built on — a consistency check, explicitly **not** a confirmation, because the
   partition was chosen after seeing these scatters.

## What would falsify

1. **A C1 ∧ C2 inventory that does not decouple.** A fresh inventory pre-registered to satisfy both
   conditions in which cue-strength nonetheless rank-predicts recovery (ρ_cue clearly positive, ≥2/3) —
   the two conditions are not jointly sufficient, and the account is wrong or incomplete.
2. **A C2-violating inventory (aligned tail) that decouples anyway.** A fresh inventory with a head
   disaligner but a cue-strength-poor recovery-tail that *still* shows ρ_cue ≤ +0.30 (≥2/3) — the tail
   condition is not necessary, so the added content over the retired conjecture is spurious and "has a head
   disaligner" (≈ the retired C1) was enough after all.
3. **Cue-strength predicts recovery even where C1 holds and C2 holds, on nouns' own corpus refreshed.** If
   a further fresh **noun** run (a third corpus family) shows cue-strength recovering rank-predictive power,
   the noun decoupling itself was corpus-specific and the whole inventory-shape framing loses its one solid
   point (this would also contest the promoted noun claim, so it is the sharpest and least likely
   falsifier).

A non-falsifying ambiguous outcome to pre-name: a fresh inventory can land ρ_cue in the **+0.3 to +0.5
gap** (as adjectives and one verb model did), in which case the powered item-level arm breaks the tie — the
s196/s199 precedent for reading a boundary from converging under-powered and powered arms.

## Scope and honesty caps (read before citing)

- **Post-hoc partition risk is the headline caveat.** C1/C2 were read *off* three already-measured
  scatters. Any account with enough descriptive features fits three points; the bet is only worth its
  **forward** test (confirm-1 / falsify-1,2). Cite this as a registered bet, never as an explanation the
  data have confirmed.
- **The design that separates C2 from POS is nontrivial and not yet built** — exactly the reason s199
  declined to register this as a bet that session ("pending a design that could separate the tail-alignment
  reading from hierarchy without confounding POS"). Registering the bet does not discharge that difficulty;
  the natural first move is a **within-noun sub-inventory** contrast (no POS confound) or the **A6
  cross-linguistic** scout, each needing its own frozen design, pre-run critic, and cross-session
  ratification before any spend.
  **→ Feasibility scouted s201** ([`note/decoupling-fresh-inventory-scout-v1`](../notes/decoupling-fresh-inventory-scout-v1.md)):
  both routes are legitimate **natural-experiment** forward tests (recovery is *observed* for either, so
  "recovery isn't designable a priori" disqualifies neither); raw material is abundant, including a
  fresh, **un-probed** candidate head disaligner (`instance-hypernymy`). The binding step for the
  within-noun route is a **$0-to-modest C4 cue-strength scout** of the fresh sub-types, to learn whether
  a **C2-*dissociating*** sub-inventory pair is assemblable; within-noun is favored as the lower-cost
  first move (no license, no POS confound), A6 as the higher-freshness license-gated alternative. Route
  not ratified; the design session chooses.
- **Necessity of C1 rests on two POS; C2 rests on the nouns-vs-verbs flip.** "Adjectives lack a head
  disaligner" and "verbs' tail is cue-strength-poor" are each single-inventory facts; a second adjective- or
  verb-family inventory could complicate them. The retired conjecture's warning against reading a 2–3-point
  pattern as a law applies here in full.
- **The noun H2 (taxonomic depth out-predicts cue-strength) is the C1 vehicle and is itself only 2/3,
  single-run, between-relation, Hearst-arm-lost** (s193). C1 inherits those caveats; "taxonomic centrality
  supplies the head disaligner" is a characterized-but-not-robust mechanism, not a settled one. On verbs the
  troponymy-depth arm was pre-registered UNDER-POWERED (degenerate depth spread) and says nothing either way.
- **Within-distributional only; no human comparison.** Like the parent essay and the retired conjecture,
  every predictor here is form-internal (contrastive-frame cue-strength, taxonomic-depth structure), and
  "recovery" is same-task relatum production scored against a shared WordNet target that cancels in the
  head-to-head. If inventory shape wins, that is *one form-internal statistic configuration out-ranking
  another*, never recovery reaching past distribution to reference or truth
  ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)'s caveat that
  distribution is "by itself, silent on reference and on truth" is untouched). The relations at stake are
  inferential-role structure in the [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)
  sense.
- **The nouns-only [`claim/lexical-relation-recovery-cue-strength-decoupling`](../claims/lexical-relation-recovery-cue-strength-decoupling.md)
  is untouched.** This conjecture proposes *why* that claim is noun-specific; it neither strengthens nor
  weakens the claim, which stays scoped to nouns, H1-only, internal-contrast, no-magnitude.
- **Opens no `decisions/open/` entry.** Registration makes no value-laden methodological choice; the design
  gates (which fresh inventory, how to operationalize "head disaligner present" and "tail cue-strength"
  before recovery is observed) are chosen at design freeze, exactly as the noun/adjective/verb runs chose
  theirs.
