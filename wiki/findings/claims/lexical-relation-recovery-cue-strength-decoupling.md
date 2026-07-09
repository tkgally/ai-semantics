---
type: claim
id: lexical-relation-recovery-cue-strength-decoupling
title: "On WordNet NOUN relations, raw contrastive-frame co-occurrence cue-strength does not rank-predict which relations the frontier panel recovers — a twice-replicated (two corpus families), powered-item-corroborated, within-distributional ABSENCE, scoped to nouns; the clean decoupling is carried by hypernymy and does NOT cross to adjectives (POS boundary, s196). Internal-contrast; no magnitude/interval claimed for the n=6 rank correlation; the H2 taxonomic-depth positive is NOT promoted (single-run, 2/3, between-relation)"
meaning-senses:
  - distributional
  - inferential
  - measurement-epistemic
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-09
updated: 2026-07-09
links:
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: depends-on
    target: result/lexical-relation-recovery-taxonomic-proxy-v1
  - rel: depends-on
    target: result/adjective-antonymy-replication-v1
  - rel: supports
    target: essay/cue-strength-recovery-decoupling
  - rel: refines
    target: theory/shadow-depth-table-v2
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Claim: on WordNet noun relations, raw contrastive-frame co-occurrence cue-strength does not rank-predict panel relation-recovery — twice-replicated, powered-item-corroborated, nouns only

> **Status: supported (2026-07-09, s197).** Cross-session, independent, adversarial claims-promotion
> review ([`PROTOCOL.md §3`](../../../PROTOCOL.md); program item B1) of the **noun** cue-strength–recovery
> decoupling (H1) — [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md)
> (s186, Simple English Wikipedia) and
> [`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md)
> (s193, C4 web text, fresh disjoint cues, verifier-REPRODUCED). The fresh-agent reviewer produced none of the
> underlying work. Promotion **fixes the yardstick, never the result** (see *Anti-cheat*).
>
> **This promotion is deliberately SCOPED to NOUNS, and to H1 (the absence) only.** The decoupling
> replicated **3/3 on two corpus families** and is corroborated near-zero at the **powered item grain**;
> what is promoted is exactly that within-distributional absence, at **n=6-Spearman strength — no
> magnitude or interval is claimed for the rank correlation**. Two things are held out of the promotion:
> (i) the **cross-POS** decoupling, which the s196 adjective replication showed does **not** cleanly hold
> (H1-PARTIAL) — a *characterized POS boundary*, cited here as a bound, not a support; and (ii) the **H2**
> taxonomic-depth positive (IS-A depth out-predicts cue-strength), which is **single-run, 2/3,
> between-relation, with its Hearst co-arm lost** and is therefore **NOT promoted** — it remains a
> result-level directional observation. `anchor: internal-contrast-only` (ratified s185/s193): **no human
> comparison** is made anywhere in this claim.
>
> **Split review, recorded (PROTOCOL §2/§3 decorrelation).** The fresh-agent reviewer returned
> **PROMOTE-NOUN-SCOPED**; the non-Anthropic decorrelation vote (`gpt-5.4-mini`) returned **REFUSE** —
> "the standing-unit bar is higher than a replicated *absence of association*; a twice-agreeing n=6
> rank-correlation null with no promoted-positive anchor is too close to a descriptive result." The
> divergence is weighed in *Anti-cheat* below; verdict authority rests with the fresh reviewer, and the
> dissent is honored by the claim's deliberate narrowness (nouns-only, H1-only, no interval, H2 held out).

## Statement

On the ratified 3-family panel (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`), across the six
WordNet **noun** relations (antonymy, synonymy, hypernymy, hyponymy, holonymy, meronymy), **the panel's
relation-wise recovery ranking does not track raw contrastive-frame co-occurrence cue-strength.** The
across-relation Spearman between recovery rank and cue-strength rank is **near-zero on every model, twice,
on two different corpus families**: **ρ_cue = −0.086 / −0.086 / −0.086** on Simple English Wikipedia
(s186) and **ρ_cue = +0.143 / +0.086 / +0.086** on C4 web text (s193, fresh cues disjoint from s186's 707
committed lemmas) — all ≤ +0.30, i.e. no positive rank association in either corpus. The **powered
item-level arm corroborates the absence at the cue grain**: a noun cue's own contrastive-frame
cue-strength does not predict its own recovery (item-level ρ ≈ 0, n ≈ 687 — *its in-repo provenance is
s196's comparative aside "against the noun run's item-level ρ ≈ 0", not a verifier-reproduced figure on a
noun result page; treated here as disclosed robustness color, not a second independently-reproduced
grain*). Concretely, in the s186 cue-strength ordering the most-cued relation is not the best-recovered:
antonymy is top of corpus cue-strength (control 𝒮 ≈ 0.077 vs 0.010–0.028 for the other five) yet
**hypernymy** — the *fourth*-most-cued **(s186 ordering)** — is best-recovered (raw 𝒮 ≈ 0.36–0.39), and
**meronymy** — the *second*-most-cued **(s186 ordering)** — is worst-recovered (raw 𝒮 ≈ 0.12–0.18). The
recovery ordering (hypernymy > antonymy > hyponymy ≈ synonymy > meronymy ≈ holonymy — s193 separates
hyponymy > synonymy, s186 ties them) holds 3/3 in both runs up to that tie.

The claim is **within-distributional and internal-contrast throughout**: recovery is scored against
WordNet, a shared target that cancels in the head-to-head, and cue-strength is a corpus statistic, so the
force is "*which corpus statistic tracks recovery*," never a model-vs-human comparison. What is claimed is
narrow and exact: **raw contrastive-frame co-occurrence cue-strength is a poor rank-predictor of
relation-wise recovery on this panel, for nouns** — *not* that recovery escapes distribution, and *not*
that cue-strength is causally irrelevant.

The claim is **scoped and qualified**, never a universal or cross-POS statement:

- **Nouns only — the clean decoupling does not cross to adjectives (a characterized POS boundary).** In
  J&K's home POS (adjectives), s196 found the decoupling did **not** cleanly replicate (ρ_cue +0.4/+0.8/+0.4;
  powered item-level ρ ≈ +0.25, all three) — cue-strength *partially* recovers its predictive power. The
  boundary is mechanistic, not noise: on nouns the rank-scramble is carried by **hypernymy** (a
  low-cue-strength but taxonomically central relation being best-recovered), and **adjectives have no IS-A
  taxonomy**, so nothing scrambles the ordering. The decoupling is therefore a **noun** phenomenon,
  carried by a taxonomic relation adjectives lack. This is a bound on the claim, and part of why the claim
  is well-scoped — not a support for it.
- **The verdict of record is an across-relation (n = 6) Spearman; no magnitude/interval is claimed.** n =
  6 is a wide-CI rank correlation; the promoted statement is qualitative and directional — *near-zero
  across-relation rank correlation, ≤ +0.30, 3/3, on two corpus families* — with the **powered item-level
  arm (n ≈ 687, ρ ≈ 0) reported as robustness corroboration, not as the verdict**. No coefficient with an
  interval is asserted for the rank correlation.
- **H2 (taxonomic depth as the replacement predictor) is NOT promoted.** s193's pre-registered IS-A-depth
  proxy out-predicted cue-strength (ρ_depth −0.20/−0.37/−0.37, predicted negative) — but only on **2/3**
  models, on a **single run**, **between-relation only** (item-level depth→recovery ρ ≈ 0), and its
  co-registered **Hearst-frame arm lost** (wrong-signed, −0.54/−0.49/−0.49). That does not clear the §3
  replication bar; it is recorded below as an unpromoted directional observation, not as claim content.

## Grounds

Two own-design results, byte-identical G² instrument across two corpus families, replicating the
**absence** on fresh disjoint cues; both independently recomputed from raw.

Across-relation Spearman ρ_cue (recovery rank vs contrastive-frame cue-strength rank, n = 6 relations,
tie-naive — the frozen s186 pipeline; the SOLE pre-registered verdict of record), per model:

| corpus family | claude-sonnet-4.6 | gpt-5.4-mini | gemini-3.5-flash | verdict |
|---|---:|---:|---:|---|
| s186 — Simple English Wikipedia (~21.3M sentences) | −0.086 | −0.086 | −0.086 | near-zero, 3/3 |
| s193 — C4 web text (22.3M sentences, fresh disjoint cues) | +0.143 | +0.086 | +0.086 | ≤ +0.30, 3/3 |

- **What replicated (the claim's spine).** s193 ran the fresh test on **a different corpus family** with
  **fresh cues verifier-confirmed disjoint from the 707 committed s186 lemmas**, on a **byte-identical**
  contrastive-frame G² control (only the sentence-streaming IO adapter changed). ρ_cue stayed near-zero
  and ≤ +0.30 on all three models: *"s186's decoupling was **not** a corpus- or set-specific artifact"*
  ([`result/lexical-relation-recovery-taxonomic-proxy-v1`](../results/lexical-relation-recovery-taxonomic-proxy-v1.md)).
  The recovery ordering (hypernymy best, part-whole worst, antonymy second) reproduced 3/3 across both
  runs, and HIT@3 gives the same ordering.
- **The powered item-level arm corroborates the absence.** On nouns, a cue's own cue-strength does not
  predict its own recovery — item-level ρ ≈ 0 (n ≈ 687), the contrast s196 draws explicitly *"against the
  noun run's item-level ρ ≈ 0"* ([`result/adjective-antonymy-replication-v1`](../results/adjective-antonymy-replication-v1.md)).
  So the near-zero is not an n=6 power artifact: it holds at the powered grain too. (Per the s193 design's
  Q1-C, the item-level arm is pre-registered descriptive/non-decisive — it cannot on its own move a
  verdict; it is used here only as disclosed robustness color around the pre-registered across-relation
  verdict, never as the verdict itself.)
- **Both runs are recompute-verified.** s186's post-run verifier *"reproduced every load-bearing figure
  from raw"*; s193's verifier **REPRODUCED** every figure (*"0.000 max ρ discrepancy"*). Data quality:
  s186 6/2730 empty, 0 errors; s193 4/2061 empty, 0 errors.

## The POS boundary (a bound, cited from s196 — not a support)

[`result/adjective-antonymy-replication-v1`](../results/adjective-antonymy-replication-v1.md) (s196) tested
the same decoupling on **four WordNet adjective relations** (130 fresh cues each, the same byte-frozen
C4 G² control). The clean across-relation decoupling **did not replicate**: ρ_cue = +0.4/+0.8/+0.4
(H1-PARTIAL/AMBIGUOUS — no clean replicate at ≤ +0.30, no clean 2/3 break), and the **powered item-level
arm agreed** (ρ ≈ +0.25, all three) — *"on adjectives, contrastive-frame cue-strength partially predicts
recovery."* The page's own reading: the noun decoupling was *"carried by **hypernymy** … a *low*-cue-strength
but taxonomically central relation being *best*-recovered,"* and *"**adjectives have no hypernymy** … so
nothing scrambles the ordering."* This claim is **noun-scoped precisely because** the mechanism that
carries the decoupling is a taxonomic relation adjectives lack. s196 is therefore cited as the claim's
boundary, and the claim asserts nothing about adjective recovery. The general POS-structural bet this
boundary suggests — the decoupling should reappear in any POS with a lexical hierarchy and vanish in any
without — is registered separately as
[`conjecture/decoupling-lexical-hierarchy-pos-generality`](../conjectures/decoupling-lexical-hierarchy-pos-generality.md)
(verbs, with troponymy, the decisive test), **not** asserted here.

## H2 (taxonomic depth) — recorded, NOT promoted

s193 found that its pre-registered **primary** proxy, IS-A path depth (`min_depth`, predicted sign
negative), out-predicted cue-strength: ρ_depth = −0.20/−0.371/−0.371, clearing the pre-registered 0.20
margin on **2/3** models. This is a genuine, interesting directional result — but it is **not promoted**,
for four stated reasons: it is a **single run** (no replication, the §3 gate); it is **2/3**, not 3/3; it
is **between-relation only** (item-level depth→recovery ρ ≈ +0.055/+0.008/+0.042, near-zero — the depth
story is about relation categories, not individual cues); and its co-registered **Hearst-frame arm lost**
(ρ_hearst −0.543/−0.486/−0.486, opposite its positive prediction), so only one of two operationalizations
of the "definitional-structure" construct succeeded. A future within-family or same-POS replication of the
depth effect (or the verb-troponymy test in the conjecture above) could earn a separate promotion; this
claim makes no H2 assertion.

## What this claim does NOT say

- **No cross-POS claim.** Scoped to WordNet noun relations. The decoupling does **not** cleanly hold on
  adjectives (s196); the claim asserts nothing about adjective, verb, or any non-noun recovery.
- **Not a magnitude or interval.** The verdict of record is an n=6 across-relation Spearman; the claim
  states only a near-zero / ≤ +0.30 rank correlation, 3/3, twice, plus a corroborating powered item-level
  ρ ≈ 0. No coefficient-with-interval is asserted for the rank correlation.
- **Not "recovery is non-distributional."** The load-bearing statement is that **raw contrastive-frame
  co-occurrence cue-strength** — one form-internal statistic — does not rank-predict recovery. A different
  distributional statistic (e.g. hierarchical position) may predict it (s193's H2 suggests exactly that).
  The [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) caveat is untouched;
  nothing here touches reference or grounding.
- **Not "cue-strength is irrelevant."** The claim is about *rank-prediction of the cross-relation
  ordering*; it does not assert cue-strength has zero causal role, only that it does not track which noun
  relations the panel recovers.
- **No H2 promotion.** Taxonomic-depth-as-replacement-predictor is single-run/2/3/between-relation with a
  lost co-arm and is not claim content.
- **No human comparison.** `internal-contrast-only`: recovery is scored against a shared WordNet target
  that cancels in the head-to-head; no human recovery baseline is imported and none is owed.
- **Not a claim about residual magnitude.** The separate residual/separability arm was descriptive-only
  (the s186 calibration gate fired, mean control 𝒮 ≈ 0.029 < 0.05); the claim leans only on the two
  directly-measured rankings, which that caveat does not touch.
- **Not a model ranking, not a representation claim.** Behavioral relatum-production only; silent on
  internal structure.

## Bounds

- **Nouns only; two corpus families; n = 3 models, orderings not coefficients; never pooled across models
  or with the adjective probe.**
- **Verdict of record is an n = 6 across-relation Spearman** (wide CI); the powered item-level arm (n ≈
  687) is corroboration/robustness, not the pre-registered verdict.
- **Proxy-corpus fence.** Cue-strength is G² over Simple English Wikipedia (s186) and C4 (s193), both
  proxies for the panel's unknown pretraining distribution; the decoupling is only as good as those
  proxies — but it now holds across two of them.
- **Construct-validity note (H2 side, not promoted here).** IS-A depth and the recovery-scoring key share
  a source (WordNet); irrelevant to H1, which compares recovery against cue-strength.
- **Single lab, three specific model versions, cross-model shared priors** — three decoders agreeing is
  weak on its own; here the independent bearing comes from the two-corpus replication and the powered
  item-level corroboration, not from a human anchor (there is none, by design).

## Anchor

This claim carries `anchor: internal-contrast-only` and **no `anchors:` resource link**, which
CLAUDE.md check-4 state (b) permits: the claim makes **no human-comparison statement**. Its entire force
is a within-instrument contrast — the panel's recovery ranking against a corpus cue-strength statistic, on
a shared WordNet target that cancels in the head-to-head. Both underlying results are ratified
`internal-contrast-only` (s185 for s186; s193 for the taxonomic-proxy run), and the claim inherits that
terminal declaration; it never asserts the panel reproduces or differs from any human relatum-recovery
baseline. This is a within-distributional, model-vs-corpus-statistic finding — not a competence-vs-human
claim.

## Anti-cheat

Promotion fixes the **yardstick** — the pre-registered near-zero-Spearman verdict map (ρ_cue ≤ +0.30 on
the frozen n=6 tie-naive pipeline) and the ratified internal-contrast fence — **never the result**. The
s193 bands were frozen in `PREREG.md` before any model call, the panel roster was the standing ratified
one, the C4 corpus and IS-A-depth proxy were frozen before recovery was observed, and both runs were
recomputed from raw by independent verifiers (0.000 max ρ discrepancy). The claim states **no more than
two corpus families × 3/3 near-zero across-relation Spearman + a powered item-level ρ ≈ 0** license: raw
contrastive-frame cue-strength does not rank-predict noun-relation recovery on this panel. It states the
absence at exactly n=6 strength (no invented interval), holds out the un-replicated H2, and scopes to
nouns because the mechanism (hypernymy) is noun-specific. The exciting over-reads — "recovery is
non-distributional," "cue-strength is irrelevant to lexical recovery," "the decoupling is a universal fact
about frontier lexical recovery," or any human-comparison — are exactly what the within-distributional
framing, the H2 exclusion, the POS boundary, and the internal-contrast anchor refuse. Nothing here
outruns the two result pages it consolidates.

**The divergent vote, weighed.** The non-Anthropic decorrelation vote returned **REFUSE**, arguing the
standing-claim bar is higher than a "replicated absence of association," that the verdict of record is a
twice-agreeing wide-CI n=6 Spearman, and that with **no promoted-positive anchor** (H2 held out) the
statement sits "too close to a descriptive result." This is a *higher-threshold* argument, not a claim of
factual error, and it is honored three ways rather than overridden silently: (i) the promotion is confined
to exactly what two 3/3 corpus-family replications plus a powered item-level ρ ≈ 0 license, with **no**
positive replacement (H2) smuggled in; (ii) the §3 bar this project sets — *replicated + survived its
controls* — is met on nouns (two corpus families, disjoint cues, verifier-reproduced, controls untouched
by the residual-arm caveat); and (iii) the claim's compounding value is not a bare null but a **framework
correction** — it breaks the `contrastive-frame cue-density ≈ shadow-depth` identification the lexical pole
of [`theory/shadow-depth-table-v2`](../theory/shadow-depth-table-v2.md) leaned on — a use the project's
claims layer already makes for gap/bound findings
([`claim/constructional-divergent-form-generalization-gap`](constructional-divergent-form-generalization-gap.md),
[`claim/dative-pronominality-partial-reach`](dative-pronominality-partial-reach.md)). The vote's future-work
condition (a third independent noun run for a tighter aggregate, and a replicated positive replacement if
the claim is to be *about mechanism*) is recorded as the strengthening path, and is exactly what the H2
exclusion and the verb conjecture leave open.

## Status

`status: supported`, **scoped to nouns, H1 only**. What is supported: across the six WordNet noun
relations, the panel's relation-wise recovery ranking does not track raw contrastive-frame co-occurrence
cue-strength — a near-zero across-relation Spearman (ρ_cue −0.086 / +0.14 / +0.09 range, ≤ +0.30, 3/3) on
**two corpus families** (Simple English Wikipedia s186; C4 web text s193, fresh disjoint cues), corroborated
by a **powered item-level ρ ≈ 0** (n ≈ 687), within-distributional and internal-contrast throughout.
`supported` attaches to that noun-scoped absence and its two-corpus replication. It does **NOT** attach to:
a cross-POS claim (s196 POS boundary), the H2 taxonomic-depth positive (single-run/2/3/between-relation,
not promoted), any magnitude/interval for the rank correlation, any non-distributional or human-comparison
reading — all explicitly disclaimed above. The three underlying results remain `status: proposed` (this
promotion consolidates them; per the result-status discipline, support migrates to this claim layer).
`contingent-on: []` — the governing gates
([`decisions/resolved/antonymy-internal-contrast-scoring`](../../decisions/resolved/antonymy-internal-contrast-scoring.md),
[`decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design`](../../decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design.md))
are ratified.
