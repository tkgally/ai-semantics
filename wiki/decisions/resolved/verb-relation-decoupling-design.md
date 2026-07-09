---
id: verb-relation-decoupling-design
title: "Verb-relation decoupling probe — the value-laden gates: the verb relation inventory + registered primary clause (H1 decoupling), the troponymy-depth proxy specification (H2), and the internal-contrast-only anchor"
status: resolved
opened: 2026-07-09
opened-by: session-198
resolved: 2026-07-09
resolved-by: autonomous (adversarial review)
resolution: "RATIFY-WITH-BINDING-CONDITIONS — Q1-C (5-relation set {hypernymy, troponymy, synonymy, entailment, antonymy}; H1 decoupling PRIMARY + H2 troponymy-depth CO-PRIMARY; powered item-level SECONDARY descriptive-only; conditional `cause` sixth) / Q2-A (single min_depth of the cue's first verb synset, pos=v, predicted negative) / Q3 internal-contrast-only. Three new binding conditions B1–B3 added to the seven existing freeze conditions."
contingent-artifacts:
  - design/lexical-relation-recovery-verb-decoupling-v1
---

# Decision (RESOLVED): the value-laden gates of the verb-relation decoupling probe

> **RATIFIED 2026-07-09 (session 199, autonomous cross-session adversarial review + one
> non-Anthropic decorrelation vote — opened by session 198, ratified s199; the surfacing/ratifying
> boundary held). RATIFY-WITH-BINDING-CONDITIONS: Q1-C / Q2-A / Q3 `internal-contrast-only`.**
> Ratification fixes the yardstick, never the result. Tom's standing override outranks.

## What was ratified

The three value-laden gates of the verb-relation decoupling probe DESIGN
([`design/lexical-relation-recovery-verb-decoupling-v1`](../../../experiments/designs/lexical-relation-recovery-verb-decoupling-v1.md);
the decisive third-point test of [`conjecture/decoupling-lexical-hierarchy-pos-generality`](../../findings/conjectures/decoupling-lexical-hierarchy-pos-generality.md),
registered s197 — does the noun cue-strength–recovery decoupling reappear on VERBS, which have a
troponymy hierarchy unlike adjectives, and does a troponymy-depth proxy out-predict cue-strength?):

- **Q1** the verb relation inventory + registered primary clause → **C**: the 5-relation set
  {hypernymy, troponymy, synonymy, entailment, antonymy} for the across-relation decoupling arm, with
  **H1 (decoupling) registered PRIMARY + H2 (troponymy-depth) registered CO-PRIMARY**, plus the
  item-level cue-strength→recovery arm (~600 cues) as a POWERED SECONDARY (descriptive/robustness-only,
  can never on its own fire H1); `cause` added as a **sixth relation only if it survives
  frequency-matching at ≥100 cues**, decided mechanically at freeze, pre-registered either way. All five
  core relations clear powered N fresh (hypernymy 2006 / synonymy 1448 / troponymy 1136 / entailment 242
  / antonymy 140 after excluding the 1,740 prior cue lemmas); 5 rank points is an adequate test, richer
  than adjectives' 4. Q1-A drops entailment for no gain; Q1-B loads a floor-binding `cause` into the
  primary.
- **Q2** the troponymy-depth proxy for H2 → **A**: `min_depth` over the cue's FIRST verb synset
  (`pos="v"`), a single frozen proxy, predicted sign **negative**, byte-analogous to the noun
  `is_a_depth` (`pos="n"`) — making a verb confirmation a genuine *replication* of the noun mechanism,
  not a new bet. Q2-B (richer proxy) would not rescue a near-degenerate spread and inflates the
  multiple-comparison surface; Q2-C (a corpus troponymy "Hearst" arm) is correctly rejected up front
  (verb troponymy has no clean lexico-syntactic frame; the s193 nominal Hearst arm *lost* even where
  well-motivated).
- **Q3** anchor → **`internal-contrast-only`**: recovery scored against WordNet as a shared
  definitional target that cancels in the head-to-head; both predictors (contrastive-frame G²,
  troponymy-depth) are corpus/lexicon statistics; no human recovery baseline enters, so no human-comparison
  claim is made and no `resource` anchor is required (CLAUDE.md terminal state; the s186
  model-vs-computational-baseline gloss-extension applies). Follows s186 / s193 / s196 exactly and
  inherits the parent noun claim's ratified terminal declaration.

## The review (decorrelated; anti-cheat PASS)

An **independent fresh-agent adversarial reviewer** (verdict authority) read the decision, the design,
the s198 pre-run review, the conjecture, the parent noun claim, and the reused s193 instruments, and
returned **RATIFY-WITH-BINDING-CONDITIONS (Q1-C / Q2-A / Q3 internal-contrast-only)**. It ran a
**FABRICATION SPOT-CHECK** firsthand in this environment (WordNet 3.0 via `nltk`): verb `min_depth()`
non-degenerate **0–12, 13 distinct** (reproduced); adjective `a`+`s` `min_depth()` **all `{0}`, 28,849
synsets** (reproduced — the reason verbs, not adjectives, are the H2 test); total verb synsets
**13,767** (reproduced exactly). **No fabrication, no blocker.** These structural facts were also
re-confirmed by the lead session independently.

One **fresh non-Anthropic decorrelation vote** (`gpt-5.4-mini`, `panel.B`, $0.00276075, via the probe
REST path) returned **ADOPT-C / ADOPT-A / internal-contrast-only** — convergent — with the caveat that
DEPTH-FAILS-as-under-powered is honest **only if the degeneracy threshold is frozen ex ante as a
quantitative power bound** (a stated numeric depth-spread threshold), else it over-protects H2. Both
reviewers converged on that point; it is bound as **B1** below. Recorded in
[`REVIEW-ratify-s199.md`](../../../experiments/runs/2026-07-09-verb-relation-decoupling/REVIEW-ratify-s199.md)
and [`vote-ratify.txt`](../../../experiments/runs/2026-07-09-verb-relation-decoupling/vote-ratify.txt).

**Anti-cheat PASS.** H1 is genuinely two-sided (DECOUPLING-REAPPEARS ρ_cue ≤ +0.30 / DECOUPLING-BREAKS
ρ_cue ≥ +0.50, with an explicit INCONCLUSIVE gap; BREAKS is a real clean falsifier of the conjecture's
central identification). The one deliberate asymmetry — DEPTH-FAILS protected as under-powered — is a
real structural fact measured at design time, not a post-hoc rescue, but must be frozen numerically and
applied symmetrically (B1/B2). `internal-contrast-only` is warranted (WordNet gold cancels on both sides
of the contrast; no human key). The "decisive → registered next/third-point test" softening is adequate
(verbs confound POS with hierarchy exactly as nouns do) provided it propagates to the run artifacts (B3).

## Binding conditions at freeze (three new; in addition to the seven already on the design page)

1. **B1 — numeric, outcome-independent degeneracy bound.** Sharpen freeze-condition 1 from "a stated
   threshold" to a **single committed numeric depth-spread bound**, frozen in `PREREG.md` on the frozen
   freq-matched sample **before any model call** (e.g. a floor on the non-antonymy 4-relation depth range
   and/or the 5-relation depth SD — one mechanically-chosen number, not a discretionary call). If the
   achieved spread falls below it, DEPTH-FAILS is non-falsifying/under-powered.
2. **B2 — symmetric application of B1.** The same frozen bound flags the *positive* branch too: below the
   bound, a verb DEPTH-OUT-PREDICTS is reported as under-powered / possibly antonymy-cue-strength-driven,
   **never banked as mechanistically equivalent to the noun H2**. Remove the "informative either way"
   asymmetry for the positive branch when the spread is degenerate.
3. **B3 — propagate the "decisive → third-point" softening to run artifacts.** The eventual
   result/claim page title and the "feeds broadening the noun claim" language must present
   DECOUPLING-REAPPEARS as **one point in a three-point pattern** a future review weighs, never as
   establishing the POS-structural law; no unqualified "decisive"/"isolates hierarchy" on the produced
   pages.

The seven existing freeze-time conditions (H2 near-degenerate-depth guard; antonymy depth×cue-strength
confound; thin-relation fallback covering the CORE relations antonymy/entailment, not only `cause`;
exact fresh-in-band cue definition with POS-agnostic surface exclusion of the 1,740 prior lemmas; the
locked mechanical `cause`-inclusion rule; byte-freeze integrity of the s193 G² construction; exhaustive
ρ_cue bands + numeric H2 margin + calibration-gate inheritance) remain in force. With B1–B3 bound, the
yardstick is fixed and the probe is ratified for freeze s199+.

## Effect

Design promoted (`contingent-on: verb-relation-decoupling-design` cleared; `anchor:
internal-contrast-only` no longer provisional). Fixes the yardstick, never a result — the probe remains
**unrun** at the moment of ratification; freeze + run follow in the same session (s199), each gated on
its own independent pre-run critic + non-Anthropic vote. Logged in [`log.md`](../../../log.md).
