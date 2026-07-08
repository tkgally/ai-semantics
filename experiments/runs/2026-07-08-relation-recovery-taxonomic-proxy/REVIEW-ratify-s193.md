# Ratification review — fresh relation-recovery / taxonomic-proxy design (s193)

**Session 193 (2026-07-08).** Cross-session autonomous ratification (PROTOCOL §2; PROJECT.md §12.3) of
[`decisions/…/lexical-relation-recovery-taxonomic-proxy-design`](../../../wiki/decisions/resolved/lexical-relation-recovery-taxonomic-proxy-design.md)
(opened s192, eligible s193). Decision → **RATIFY-WITH-CHANGES: Q1-C / Q2-B / Q3-A / Q4
internal-contrast-only**. Nothing frozen or run at ratification.

## Two decorrelated reviews

### (1) Fresh-agent adversarial ratifier — VERDICT AUTHORITY

An independent agent (not the s192 orchestrator that drafted the design) read the decision, the design,
the s192 design-stage review, and — firsthand — the essay, pilot note, s186 result, corpus scout, the
reused s186 sibling decision, and CLAUDE.md's typed-link/anchor section, verifying every load-bearing
quote/number against source.

> **OVERALL: RATIFY-WITH-CHANGES.** Adopt **Q1-C**, **Q2-B** (C4 primary — overturning the provisional
> default Q2-C), **Q3-A**, **Q4 internal-contrast-only**.
>
> - **Q1 — RATIFY default C.** Correct anti-goalpost call: refuses to swap the underpowered *registered*
>   across-relation bet for the powered-but-*different* within-relation cue-depth test as verdict of
>   record. Freeze-condition 1 (across-relation is the sole verdict of record; item-level can never fire
>   H2 or upgrade an H2-loss) is load-bearing and must survive to PREREG verbatim.
> - **Q2 — RATIFY-WITH-CHANGES: adopt B (C4 PRIMARY).** H1 is a *freshness* bet whose falsifier is
>   "cue-strength recovers its predictive power on a corpus different from s186's." Full Wikipedia is the
>   same encyclopedic source-family as s186's Simple Wikipedia (un-simplified, ~100× larger, but
>   register-continuous) — the weakest available falsifier. C4's web register is the genuine
>   decorrelation, and Common-Crawl text is at least as good a pretraining proxy as Wikipedia (it is the
>   bulk of LLM pretraining tokens). Engineering reinforces this: under ~30 GB free disk, C4 streams in a
>   bounded handful of ~350 MB shards (C4-en ≈152M tokens/shard; ~3–5 shards ≈450–760M tokens, exceeding
>   s186's ~21M-sentence Simple-Wiki volume), counted over the fixed cue set and discarded; the full-Wiki
>   ~22 GB dump extraction is the genuinely heavy lift — so the design's "Wikipedia lighter, C4 heavier"
>   premise is backwards. Ruling: **C4 primary and verdict-bearing; full Wikipedia demoted to an optional
>   same-family sensitivity arm** (not co-primary — do not dilute the verdict of record with a
>   weak-falsifier corpus).
> - **Q3 — RATIFY default A.** The essay's actual named "definitional-frame statistic" is corpus Hearst
>   frames; the pilot *licensed* a corpus Hearst proxy as legitimate future work for the fresh design
>   while refusing gloss length. Q3-A tests the essay's construct faithfully without reinstating the
>   refused echo; freeze-condition 5 handles the multiple-comparison bar. Near-free since Q2's corpus is
>   fetched anyway.
> - **Q4 — RATIFY `internal-contrast-only`.** Legitimate terminal declaration: recovery scored vs
>   WordNet as a shared target that cancels in the head-to-head; both predictors are corpus/lexicon
>   statistics; no human baseline enters, so no human-comparison claim exists to dodge. Mirrors the s186
>   sibling ratification, including the model-vs-computational-baseline gloss-extension. The
>   IS-A-depth/WordNet shared-source is a genuine construct-validity caveat (mitigated by gold-independent
>   cue-first-synset depth), not a human-anchor obligation.
>
> **Anti-cheat: PASS.** Defaults lean away from easy confirmation; Q2-B makes H1 harder to confirm
> (stronger falsifier) — the correct direction. The pilot's refusal of gloss length (ρ=−0.83) is
> respected; Q3-A adds the pilot-licensed corpus Hearst construct, not the refused echo. No motivated
> result smuggled; no STOP condition.
>
> **Fabrication check: PASS.** Spearman −0.086; `min_depth` + negative sign; hypernymy best / meronymy
> worst; Wikipedia CC BY-SA + GFDL and C4 ODC-BY license strings; s186 = Simple English Wikipedia; C4
> ~305 GB but streamable — all match source firsthand. No mismatch.
>
> **Freeze-time riders (beyond the six recorded):** (1) correct the "Wikipedia lighter, C4 heavier"
> premise — C4-streaming is the primary path; at freeze pin the shard count and assert achieved volume ≥
> s186's Simple-Wiki volume before trusting G² (thin-corpus check for antonym-sparse strata). (2) Retire
> the C4-optional/deferred language — C4 is not deferrable; if any corpus is deferred it is the
> full-Wiki sensitivity arm. (3) The Common-Crawl-terms caveat (ODC-BY plus Common-Crawl terms) travels
> to the result's provenance.

### (2) Non-Anthropic decorrelation vote (QA input, no verdict authority)

`openai/gpt-5.4-mini` via the probe REST path (cutoff-aware preamble;
[`vote-ratify.py`](vote-ratify.py) / [`vote-ratify.txt`](vote-ratify.txt), **$0.002346**):

> **Q1 ADOPT-C · Q2 ADOPT-B · Q3 ADOPT-A · Q4 ADOPT internal-contrast-only.** Agrees C4 primary ("the
> cleaner register-decorrelated falsifier; full Wikipedia is too same-family to be the main H1 stress
> test"); keep the full-Wiki arm "optional if tractable, not co-primary." Flags the same load-bearing
> risk both reviewers name: Q1's item-level arm must stay non-decisive or it "would quietly become the
> real test because it has power and prettier p-values"; H2 under n=6 is weak by design and acceptable
> only if item-level is non-decisive. Confirms the prereg-freeze and the no-fishing posture (rejecting
> extra proxies) are right.

## Convergence

Both reviewers land the **same four gates including the one change** (Q2 → B, C4 primary), and both
independently make Q1's item-level-must-be-non-decisive the load-bearing condition. No divergence this
session (the s192 design-stage Q2 divergence is resolved *toward* the dissent). $0.002346 (one vote);
no probe. Gates fixed: **Q1-C / Q2-B / Q3-A / Q4 internal-contrast-only**; the freeze honors the six
conditions + three riders. H1/H2 stay open — they fire only on the run.
