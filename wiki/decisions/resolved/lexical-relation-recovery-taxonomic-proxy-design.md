---
id: lexical-relation-recovery-taxonomic-proxy-design
title: "Fresh relation-recovery / taxonomic-proxy probe (H1 + H2) — the four value-laden gates: level of analysis for H2 (anti-goalpost), the fresh control corpus, the second pre-registered proxy arm, and the internal-contrast-only anchor"
status: resolved
opened: 2026-07-08
opened-by: session-192
contingent-artifacts:
  - design/lexical-relation-recovery-taxonomic-proxy-v1
resolved: 2026-07-08
resolved-by: autonomous (adversarial review)
resolution: "RATIFY-WITH-CHANGES — Q1-C (across-relation n=6 rank PRIMARY + sole verdict-of-record; item-level ~700–900 cue-depth regression POWERED SECONDARY, strictly descriptive/robustness-only, can never fire H2 or upgrade an across-relation H2-loss); Q2-B (C4 PRIMARY and verdict-bearing — a CHANGE from the provisional default Q2-C; full English Wikipedia demoted to an optional same-family sensitivity arm) — the fresh ratifier and the non-Anthropic vote both ruled full Wikipedia too close to s186's encyclopedic register to be a strong H1 falsifier, and C4's web register the genuine decorrelation (and, under ~30 GB disk, the tractable one via bounded streaming shards); Q3-A (IS-A path depth PRIMARY + a corpus Hearst-frame definitional-density proxy as a SECOND pre-registered arm, multiple-comparison rule: H2 fires only if a NAMED proxy wins in its PRE-REGISTERED direction, a Hearst-only win reported qualified/weaker); Q4 internal-contrast-only (recovery scored vs WordNet as a shared target that cancels in the head-to-head; predictors are corpus/lexicon statistics; no human baseline — terminal declaration ratified). Fresh reviewer RATIFY-WITH-CHANGES + non-Anthropic vote CONVERGED on all four gates including C4-primary. Six freeze-time conditions (recorded on the design) + three ratifier riders bind the freeze. Fixes the yardstick, not the result; nothing frozen or run at ratification."
---

# Resolution (2026-07-08, session 193, autonomous cross-session adversarial review)

> **RATIFIED: RATIFY-WITH-CHANGES** — **Q1-C** (the across-relation n=6 rank test is the *sole
> verdict of record* for both H1 and H2; the powered ~700–900-item cue-depth regression is a
> descriptive/robustness secondary that can never on its own fire H2 or upgrade an across-relation
> H2-loss); **Q2-B — C4 PRIMARY** (a **change** from the design's provisional default Q2-C; full
> English Wikipedia is demoted to an *optional* same-family sensitivity arm); **Q3-A** (IS-A path
> depth `min_depth` primary, predicted sign **negative**, + a corpus Hearst-frame definitional-density
> proxy as a second pre-registered arm, with a multiple-comparison rule — H2 fires only if a *named*
> proxy wins in its *pre-registered* direction, and a Hearst-only win is reported as qualified/weaker,
> never equal-status); **Q4 `internal-contrast-only`** (recovery is scored against WordNet as a shared
> definitional target that cancels in the head-to-head; both predictors are corpus/lexicon statistics;
> no human recovery baseline enters, so no `resource` anchor is required — CLAUDE.md terminal state,
> the s186 model-vs-computational-baseline gloss-extension applies). Opened by session 192; ratified
> session 193 (the surfacing/ratifying boundary held). `resolved-by: autonomous (adversarial review)`.
> Tom's standing override outranks if he ever rules otherwise.

**How it was ratified.** Independent fresh-agent adversarial review (a different agent from the s192
orchestrator that drafted the design) **plus** one non-Anthropic decorrelation vote
(`openai/gpt-5.4-mini`, cutoff-aware preamble; PROTOCOL §2 decorrelation rule,
[`vote-ratify.txt`](../../../experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/vote-ratify.txt),
$0.002346). **Both converged on Q1-C / Q2-B / Q3-A / Q4 internal-contrast-only** — including the one
change from the provisional defaults, **Q2 → B (C4 primary)**. Full review at
[`REVIEW-ratify-s193.md`](../../../experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/REVIEW-ratify-s193.md).

**The one change from the provisional defaults — Q2 (Wikipedia-primary → C4-primary).** The design
defaulted to Q2-C (full English Wikipedia primary + C4 sensitivity arm). Both the s192 design-stage
non-Anthropic vote **and** this session's fresh ratifier + its decorrelation vote judged that a
H1-REPLICATES verdict on **full English Wikipedia** would be a weak fresh test: it is the *same
encyclopedic source-family* as s186's Simple English Wikipedia (un-simplified and ~100× larger, but
register-continuous), so it leaves the core alternative — that the decoupling is corpus/register-specific
— largely untested. **C4's web register is the genuine decorrelation**, and (contra the design's
"Wikipedia is the best pretraining proxy" rationale) Common-Crawl-family text is at least as good a
pretraining proxy — it is the bulk of LLM pretraining tokens. The engineering constraint reinforces
rather than opposes the methodology: under the run environment's **~30 GB free disk**, C4 is
**streamable in a bounded handful of ~350 MB shards** (counted over the fixed cue set and discarded),
while the full-Wikipedia dump (~22 GB compressed, heavy extraction) is the genuinely heavy lift — so
the design's "Wikipedia lighter, C4 heavier" premise was **backwards**. C4 is both the stronger
falsifier and the tractable one. Ruling: **C4 primary and verdict-bearing; full Wikipedia demoted to
an optional same-family robustness arm**, not co-primary (diluting the verdict of record with a
weak-falsifier corpus is the wrong direction).

**Anti-cheat: PASS.** The defaults lean *away* from easy confirmation: Q1-C refuses to swap the
underpowered *registered* across-relation bet for the powered-but-*different* item-level test as the
verdict of record; every proxy spec, predicted sign, ρ-band and threshold is frozen in PREREG before
any model call; H1-BREAK, H2-LOSE, both-null, and an across-vs-item-level divergence are all pre-named
first-class outcomes. The Q2 → B change makes H1 **harder** to confirm (a stronger falsifier) — the
correct anti-cheat direction. The pilot's principled refusal of the gloss-length exploratory maximum
(ρ = −0.83, the top correlate, deliberately not frozen) is respected — Q3-A adds the pilot-*licensed*
corpus Hearst construct, not the refused WordNet gloss echo. Ratification fixes the yardstick, never
the result.

**Fabrication check: PASS.** The fresh ratifier verified the load-bearing quotes/numbers firsthand
against the source pages: the across-relation Spearman **−0.086** (s186 result); IS-A depth `min_depth`
+ **negative** predicted sign (pilot note); **hypernymy best-recovered / meronymy worst** (s186 clause
2); the Wikipedia CC BY-SA + GFDL and C4 ODC-BY license strings (corpus scout); **s186 = Simple
English Wikipedia**. No mismatch.

## Freeze-time conditions (six, recorded on the design; bind the s193 freeze)

Carried verbatim from the s192 pre-run design review (all are PREREG/`prep.py` specifications, not
gate rewrites):

1. **Q1 verdict-of-record binding.** PREREG states as a hard commitment that the **across-relation
   (n=6) result is the sole verdict of record for H1 and H2**; the item-level cue-depth arm is
   **descriptive/robustness-only** and can never on its own fire H2 or upgrade an across-relation
   H2-loss. A level-divergence is a pre-named first-class outcome.
2. **Close the ρ_cue band gap.** Exhaustive, mutually-exclusive H1 bands (no uncovered middle) and a
   **numeric** H2 margin for "|ρ_proxy| clearly greater than |ρ_cue|," fixed before any model call.
3. **Q2 register scope-cap + C4.** *Superseded in force by the Q2-B ruling:* C4 is now the primary
   verdict-bearing corpus, so the "Wikipedia-only scope-cap / C4 deferred" language does not apply —
   C4 is not deferrable. If any corpus is deferred for tractability it is the full-Wikipedia
   sensitivity arm, reason documented.
4. **Clarify "byte-frozen."** Byte-identity applies to the **G²/co-occurrence computation**
   (`FRAME_WIN`, connective set, K, weighting, `signed_g2`) — verified unchanged against the s186
   `build_cooc.py`; the per-corpus sentence-streaming/IO adapter necessarily changes but must not
   touch any counting/weighting logic.
5. **Q3 multiple-comparison rule + Hearst sign.** IS-A depth primary, Hearst-frame proxy secondary;
   freeze the Hearst construction and its theory-set predicted sign before any corpus counting on the
   fresh cues; a Hearst-only H2 win (IS-A depth loses) is reported as qualified/weaker, not
   equal-status H2-WINS.
6. **Disjointness + fresh-N reporting.** Exclude the exact committed 780 s186 cue lemmas with asserted
   per-relation 0-overlap; report the achieved fresh per-relation N (antonymy expected ~100, capped by
   WordNet nominal sparsity).

## Ratifier riders (three, added s193; bind the freeze)

1. **Correct the fetch-tractability premise (ties to Q2-B).** Rewrite the design's "Wikipedia lighter,
   C4 heavier" line: C4-streaming is the **primary** path. At freeze, pin the exact number of C4 shards
   streamed and **assert the achieved token/sentence volume ≥ s186's Simple-Wikipedia volume** before
   any G² is trusted (a thin-corpus check for the antonym-sparse strata, where G² is least stable).
2. **Retire the C4-optional/deferred language** (condition 3 above): C4 is primary and not deferrable.
3. **Common-Crawl-terms caveat travels to the result page.** The scout's ODC-BY-plus-Common-Crawl-terms
   layer must be recorded on the eventual result's provenance.

**Construct-validity scope caveat (not a gate).** IS-A depth and the recovery-scoring key share a
source (WordNet); mitigated by the pilot's gold-independent cue-first-synset depth ("a property of the
cue, not a restatement of the answer set"). Carry as a scope caveat on the eventual result; Q4 stays
internal-contrast-only.

---

*(The four gate statements Q1–Q4, their options, and the anti-cheat note as opened s192 are preserved
below verbatim for the audit trail.)*

## Gate Q1 — level of analysis for H2 (the anti-goalpost-moving gate; load-bearing)

The essay registered H2 as an **across-relation rank** hypothesis (recovery rank vs proxy rank over the
six relations, head-to-head against cue-strength rank). But **n = 6 relations cannot be a significant
Spearman**, and IS-A depth is a **per-cue** property, so a far more powerful **item-level** test exists
(regress a cue's recovery on its own IS-A depth, N ≈ 700–900). Choosing item-level *alone* silently
redefines H2 after the fact. Options:

- **A — across-relation rank only** (6 points). Faithful to the exact registered bet; underpowered.
- **B — item-level cue-depth regression only** (~700–900 items; powered). Powered, but a **different**
  hypothesis (within-relation cue-depth → recovery), and adopting it alone moves the goalposts.
- **C (RATIFIED) — across-relation rank PRIMARY and verdict-bearing (n = 6, reported with its wide CI),
  PLUS the item-level analysis as a POWERED SECONDARY** reported side-by-side. The head-to-head of
  record stays |ρ(depth, recovery)| vs |ρ(cue-strength, recovery)| across relations, ≥2/3 models; the
  item-level arm buys power and guards an n=6 fluke **without** changing what H2 was registered to
  predict. A **divergence** between the two levels is itself a first-class reported outcome.

## Gate Q2 — the fresh control corpus

H1's falsifier requires a **fresh** test; "a different control corpus" is a named route. s186 used
**Simple English Wikipedia**. Both candidates cleared the s185 license scout firsthand
([`resource/cooccurrence-corpus-scouting`](../../base/resources/cooccurrence-corpus-scouting.md)).
Options:

- **A — full English Wikipedia** (CC BY-SA 4.0 + GFDL). Cleanest license, billions of words; but the
  **same source family** as Simple Wikipedia — the weakest register-decorrelation.
- **B (RATIFIED) — C4** (`allenai/c4`, ODC-BY). Web register, genuinely different; the strongest fresh
  test; streamable so only the fixed cue set is counted. Now the **primary verdict-bearing** corpus.
- **C (provisional default, NOT adopted) — full English Wikipedia PRIMARY + C4 as a labelled
  sensitivity arm.** Overturned: full Wikipedia is too same-family to be the primary H1 falsifier.

## Gate Q3 — the second pre-registered proxy arm (definitional-frame)

- **A (RATIFIED) — IS-A path depth PRIMARY (the pilot's frozen spec) + a corpus Hearst-frame
  definitional-density proxy as a SECOND pre-registered arm.** H2 is satisfied if *any* pre-registered
  proxy out-predicts cue-strength (≥2/3) in its pre-registered direction; both proxies' specs +
  predicted signs frozen **before** recovery; a pre-registered multiple-comparison rule handles the
  second arm.
- **B — IS-A path depth only.** Not adopted (leaves the essay's named definitional-frame candidate
  untested; forgoes a nearly-free arm).
- **C — add ill-behaved candidates** (subtree connectivity, polysemy). **Rejected up front.**

## Gate Q4 — the anchor declaration

- **RATIFIED: `anchor: internal-contrast-only`** — following the s186 Q3 ratification exactly. Recovery
  is scored against WordNet as a **shared definitional target that cancels in the head-to-head**; the
  predictors (contrastive-frame G², IS-A depth, any Hearst proxy) are corpus/lexicon **statistics**; no
  human recovery baseline enters. So the result makes **no human-comparison claim** and no `resource`
  anchor is required (CLAUDE.md terminal state; the s186 gloss-extension applies).

## Anti-cheat note (as opened s192, preserved)

The defaults lean *away* from easy confirmation: Q1-C **refuses** to swap the underpowered registered
bet for the powered-but-different item-level test as the verdict of record; Q2 demands a corpus
*different* from s186's so H1 cannot win by same-corpus artifact; Q3's second arm comes with a
pre-registered multiple-comparison rule; every proxy spec, predicted sign, and threshold is frozen in
PREREG **before** recovery; and the H1-break, H2-lose, and both-null outcomes are pre-named first-class
results. Ratification fixes the yardstick, never the result.
