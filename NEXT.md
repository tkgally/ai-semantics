# NEXT.md

## State

The project is **three-axis**: **grammatical** (live, robust — 11 own-design results), **lexical**
(live: clauses a+c supported; clause **b** — the distinctive polysemy-vs-homonymy *discreteness* bet —
now a **powered null** at the WiC anchor), and **multimodal / grounding** (two negatives). This session
(2026-05-31, **workflow mode**, branch `claude/ai-semantics-workflow-3LT7F`, **PR #31**) applied Tom's
rulings and **ran the top-priority lexical v3** plus a bridge-confound cleanup.

What landed (4 waves + 4 independent adversarial passes [2 pre-run critics + 2 post-run verifiers] +
2 cataloging/evidence subagents; ~$1.92 billed, all under the $20/week cap):

1. **Decisions (Wave 0, $0).** Per Tom: **resolved** [`multimodal-image-anchor`](wiki/decisions/resolved/multimodal-image-anchor.md)
   (Option A stands — 3 contingent artifacts promoted, no finding changed) +
   [`relational-fetchable-anchor`](wiki/decisions/resolved/relational-fetchable-anchor.md) (Option A —
   Hawkins catalog-able; Brennan & Clark 1996 → `wanted.md`). **Kept open** (Tom: no key added):
   [`aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) +
   [`cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md). Dashboard: 18 resolved / 2 open.
2. **LEXICAL V3 — clause (b) POWERED NULL (Wave 1, $1.430 billed).**
   [`result/lexical-polysemy-homonymy-v3`](wiki/findings/results/lexical-polysemy-homonymy-v3.md): on a
   homonymy-enriched WiC noun subset (11 homonym vs 11 polyseme lemmas, 161 items, WiC **binary** anchor),
   the panel's graded rating separates WiC same/different **equally well for homonyms and polysemes**
   (AUC diff ≈ 0, every permutation p 0.73–0.96; AUC 0.78–0.91 both strata). The one positive (homonym-F
   floored more) **can't be separated from plain graded distance**, is half-driven by one lemma (`case`),
   partly a gemini scale-quirk, CI-fragile. So the distinctive lexical bet (b) is **not established** —
   now via a powered test. By-product: the bare WordNet lexicographer rule **over-calls homonymy ~6:1**.
   966 calls, 0 NA; pre-run stratification critic + post-run verifier (every figure reproduced).
3. **Hawkins tangrams resource (Wave 2, $0).** [`resource/hawkins-tangrams`](wiki/base/resources/hawkins-tangrams.md)
   — fetched + sha256-verified, recipe-not-corpus posture, derived entrainment curve committed; the
   relational pilot's human **convergence baseline** (the live-vs-shuffled measure is *not* anchored by it).
4. **BRIDGE V2 — partial de-confounding (Wave 3, $0.220 billed).**
   [`result/coercion-sense-modulation-v2`](wiki/findings/results/coercion-sense-modulation-v2.md): the
   non-coercing transitive control settles v1's sense-vs-surface confound — **partially**. A small,
   **fine-scale-only, fragile** sense-specific residual survives (isolation gap cont +13.6/+6.1/+1.9,
   ≈0 on the 4-pt scale, 3–4/8 verbs) **plus a real surface component** → v1's gap was a *mix* (mostly
   sense for claude, mostly surface for gemini). Refined v1 + the lexicon-grammar theory page.

## Next concrete action (backlog — all remaining units are GATED or low-motivation)

The two named **un-gated** units (lexical v3, bridge v2) are **done**. What remains:

1. **Relational pilot** — now has a fetchable human convergence baseline
   ([`resource/hawkins-tangrams`](wiki/base/resources/hawkins-tangrams.md)), the design is sharpened
   ([`open-question/relational-meaning-pilot`](wiki/findings/open-questions/relational-meaning-pilot.md)),
   and the literature gate is discharged. **GATED on Tom's "Decision 9"** (whether to run the two-AI
   iterated-reference-game pilot at all) — it is a large multi-agent build and the *novel*
   live-vs-shuffled trajectory measure is not anchored by Hawkins (only the convergence baseline is).
   If Tom green-lights it, this is the project's most distinctive next experiment.
2. **AANN probe** — **GATED**: needs per-token surprisal (no 3-family OpenRouter logprob path). A real
   cloud path exists (Together echo-logprobs, <$1) but needs a **`TOGETHER_API_KEY`** (decision
   [`cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md)). If Tom adds the key, run the
   Option-A surprisal on one small model (flag the no-cross-family caveat).
3. **Image probe v2** (finer/abstract senses, or VWSD as a genuinely-multimodal anchor) — **un-gated but
   low-motivation**: lexical v3 showed the text-only panel separates senses at ceiling even for the
   *homonymy-enriched* case (AUC 0.78–0.91), echoing the image-v1 redundancy null — so there's **no
   headroom signal** to justify the spend. Worth it only if Tom wants the grounding axis pushed into
   genuinely-multimodal territory (VWSD), not as a text-saturation re-run.

Run `python3 tools/senselint.py` (0 errors) + `python3 tools/linkify.py` before every commit. Claims
modest; **nulls first-class**. New probes import [`experiments/lib/openrouter.py`](experiments/lib/openrouter.py)
(billed `usage.cost`); **freeze + commit stimuli (sha256) before any probe call**; ≥1 independent pre-run
critic + ≥1 post-run verifier per finding-bearing probe. **Budget:** $20/week soft, all-in; gemini
reasoning tokens dominate every multi-call run (v3 gemini $1.227 of $1.430). Spent this session ≈ **$1.92**.

## Blocked / pending Tom (2 open decisions + 1 open question, all non-blocking)

- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — AANN
  held (no 3-family logprob panel); paired with cloud-compute-path.
- [`decisions/open/cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md) — add a
  `TOGETHER_API_KEY` to unblock the AANN Option-A surprisal (<$1)? Tom: not yet.
- **Relational "Decision 9"** (open-question, not a `decisions/` file) — run the two-AI iterated-reference
  pilot? Anchor + literature now ready; needs Tom's go-ahead (it's the big, distinctive build).

## Reminder for the next cold-start

Charter `PROJECT.md`; schema `CLAUDE.md`; run discipline `PROTOCOL.md` ("continue working" ⇒ workflow
mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md) first, then `wiki/index.md`**;
reconcile `wiki/decisions/open/` (2 open, both the non-blocking AANN/compute pair). The project is
**three-axis**: grammatical (robust), lexical (a+c supported; **b a powered null** — the distinctive
discreteness bet not established, and the discreteness/graded-distance confound is intrinsic to a
lemma-level WiC contrast), multimodal/grounding (two negatives + the lexicon-grammar bridge now partly
de-confounded). **No un-gated, in-anchor, worth-the-spend experiment is currently teed up** — the next
substantive moves are Tom's calls (relational Decision 9; the AANN key). Un-gated maintenance/writing
(theory consolidation, source-PDF re-verification of pending quotes) remains possible if no green-light.
