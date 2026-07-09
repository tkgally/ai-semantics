# Promotion review — the NOUN cue-strength–recovery decoupling (s197)

**Procedure:** PROTOCOL §3 (claims promotion), program item B1. Cross-session, independent, adversarial
pass by a **fresh agent** (produced none of the underlying s186/s193/s196 work) + one **non-Anthropic
decorrelation vote** (`gpt-5.4-mini`, probe REST path; PROTOCOL §2/§A3). Verdict authority: the fresh
reviewer. The vote is QA input — convergence is comfort, divergence is signal weighed in writing.

**Object reviewed:** should the **noun** cue-strength–recovery decoupling (H1) — twice-replicated across
two corpus families ([`result/lexical-relation-shadow-saturation-v1`](../../../wiki/findings/results/lexical-relation-shadow-saturation-v1.md)
s186 Simple English Wikipedia; [`result/lexical-relation-recovery-taxonomic-proxy-v1`](../../../wiki/findings/results/lexical-relation-recovery-taxonomic-proxy-v1.md)
s193 C4) — become a standing `claim`, or stay a `result` (a written refusal being a legitimate outcome)?
The narrower question NEXT.md route 1 poses: the **cross-POS** claim is blocked (s196 H1-PARTIAL on
adjectives); does a **noun-scoped** claim clear the §3 bar?

## Verdicts

- **Fresh-agent reviewer: PROMOTE-NOUN-SCOPED** — a nouns-only claim covering **H1 only** (the decoupling
  as a within-distributional absence, stated at n=6-Spearman strength, corroborated by the powered
  item-level arm). **H2 (IS-A depth) explicitly EXCLUDED** (single-run, 2/3, between-relation, Hearst
  co-arm lost — does not clear the replication bar). s196 cited as a *characterized POS boundary* (a
  bound), not a disconfirmation.
- **Non-Anthropic vote (`gpt-5.4-mini`): REFUSE** ($0.0027465) — "the standing-unit bar is higher than a
  replicated *absence of association*; the core is a twice-agreeing **n=6** rank-correlation null; the
  item-level arm is within-cue and the positive replacement (IS-A depth) is thin, so there is no stable
  promoted-positive anchor to absorb the absence; 'cue-strength does not rank-predict recovery for nouns'
  is too close to a descriptive result." Future-promotion path it names: a third independent noun run for
  a tighter aggregate, or a replicated positive replacement.

## Divergence, weighed (orchestrator, s197)

Adopted the fresh reviewer's **PROMOTE-NOUN-SCOPED**. The vote is a *higher-threshold* argument, not a
claim of factual error, and it is honored rather than overridden silently:

1. **It is not "absence at low power."** The near-zero holds at **two grains** — the pre-registered n=6
   across-relation Spearman (3/3, twice, two corpus families) **and** the powered item-level arm (n≈687,
   ρ≈0 on nouns). The vote treated the item-level arm as "not the same claim"; for an *absence* claim it
   is corroboration, and the claim discloses it as robustness color, never as the verdict.
2. **The §3 bar this project sets is met on nouns** — *replicated (fresh items + fresh corpus family) +
   survived its controls* (the residual-arm calibration caveat does not touch the decoupling, a direct
   comparison of two measured rankings). The vote argues for a bar above §3.
3. **It compounds as a framework correction**, not a bare null: it breaks the `contrastive-frame
   cue-density ≈ shadow-depth` identification the lexical pole leaned on. The claims layer already holds
   gap/bound/negative claims (`constructional-divergent-form-generalization-gap`,
   `dative-pronominality-partial-reach`, `formal-competence-aann-ceiling`), so an absence is admissible.
4. **The dissent is honored by the claim's narrowness** — nouns-only, H1-only, no invented interval, H2
   held out, internal-contrast, "does not rank-predict" (not "irrelevant"). The vote's future-work path is
   recorded on the claim as the strengthening route (third noun run; a replicated positive replacement; or
   the verb-troponymy test).

**Anti-cheat:** promotion fixes the yardstick (the frozen near-zero-Spearman map + the ratified
internal-contrast fence), never the result. No motivation to reach a particular outcome; the divergent
vote was weighed on the merits, and the promotion is confined to what two 3/3 replications + a powered
item ρ≈0 license.

## Output

- **New:** [`claim/lexical-relation-recovery-cue-strength-decoupling`](../../../wiki/findings/claims/lexical-relation-recovery-cue-strength-decoupling.md)
  (`supported`, nouns-only, H1-only, `anchor: internal-contrast-only`).
- Underlying results stay `status: proposed` (support migrates to the claim layer per the ratified
  result-status discipline); each gets a one-line dated consolidation note.
- Essay [`cue-strength-recovery-decoupling`](../../../wiki/findings/essays/cue-strength-recovery-decoupling.md)
  s196 box updated (cross-POS blocked; noun-scoped H1 promoted s197). `predictions.md` row updated.
- Companion philosophical unit: [`conjecture/decoupling-lexical-hierarchy-pos-generality`](../../../wiki/findings/conjectures/decoupling-lexical-hierarchy-pos-generality.md)
  (the general POS-structural bet; verbs the decisive test).

**Vote artifacts:** `vote-promote.py`, `vote-promote.txt` (this dir).
