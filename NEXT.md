# NEXT.md

## State

The project is **three-axis**: **grammatical** (live, robust — 11 own-design results), **lexical**
(live: clauses a+c supported; clause **b** — the distinctive polysemy-vs-homonymy *discreteness* bet —
a **powered null** at the WiC anchor), and **multimodal / grounding** (two negatives). **None of that
changed this session.**

This session (2026-05-31, **workflow mode**, branch `claude/ai-semantics-wiki-consolidation-UQBue`,
**PR #32**) was a **documentation / consolidation pass only — no experiments, no model/panel calls,
$0 billed.** It improved the wiki itself: consistency, provenance depth, and currency. **No finding was
created, changed, promoted, or retired.** Two open decisions were reconciled per PROTOCOL §2 and left
**open** (Tom added no ruling/key): the held AANN/compute pair.

What landed (2 consolidation waves + recon + 2 independent read-only adversarial coherence passes):

1. **Theory consolidation (Wave 1).** Refreshed both theory pages to fully absorb the latest results.
   [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md): fixed an
   internal contradiction (body said bridge v2 ran while the status section still listed it + lexical v3
   as *open* triggers) — now reflects clause (b) = powered null (v3), bridge = partial/fragile
   de-confounding (v1→v2), grounding = two bounded negatives; YAML links/date synced.
   [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md):
   discharged the stale "first lexical probe runs" trigger; brought the lexical/grounding cross-references
   current (pointing to the continuum page for depth). The grammatical evidence-ladder + 11-result core
   was already current and was left intact.
2. **Provenance hardening (Wave 1).** Re-verified the flagged quotes on **8 source pages** against
   fetchable copies, verbatim — **upgrading only on a real fetch, keeping honest flags where paywalled/
   scanned**. Notably: [`source/harnad-1990-symbol-grounding`](wiki/base/sources/harnad-1990-symbol-grounding.md)
   had **three paraphrased/truncated body quotes corrected to exact arXiv text** (one approximate flag
   retired); [`source/yuksekgonul-2023-aro`](wiki/base/sources/yuksekgonul-2023-aro.md) had a **factual
   error fixed** (per-model scores are in Figure 1/appendix, not "Table 1" = the perturbations list);
   Winoground Table-3 figures verified + no-IAA-statistic confirmed; Barsalou's secondary-source flag
   **correctly kept** (primary PDFs are text-less scans). Scivetti/Weissweiler/Mahowald re-verified.
3. **Consistency sweep + catalog grooming (Waves 1–2).** Reconciled the **index.md** entries that lagged
   the 2026-05-31 promotions (7 results + the multimodal conjecture + 5 design lines now read
   `anchor: internal-contrast-only` / `contingent-on: []`); synced [`resources/index.md`](wiki/base/resources/index.md)
   to add the 4 missing resource entries (Lancaster, WordNet, WiC, Hawkins) + a scouting-notes line;
   added **Brandom** to [`wanted.md`](wiki/base/wanted.md) (it backed `concept/inferential-meaning` but
   was uncited there). Refreshed two stale **open-questions**:
   [`open-question/lexical-polysemy-gradience`](wiki/findings/open-questions/lexical-polysemy-gradience.md)
   → **answered** (graded-sense tracking present + beats the shadow; discrete-regime sub-arm a powered
   null, flagged not buried), and
   [`open-question/instrument-sensitivity-constructional-inference`](wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md)
   → stays **open** but now characterized by CC-v3 / caused-motion-v2c / the disagreement re-analysis;
   and the [`conjecture/multimodal-lexical-grounding-divergence`](wiki/findings/conjectures/multimodal-lexical-grounding-divergence.md)
   → **tested** (predictions 1–3 ran, all negative; only prediction 4 unrun).

Concept stubs were audited and found **complete** — no filler was added. Verification on every commit:
`python3 tools/senselint.py` (0 errors) + `python3 tools/linkify.py` (clean).

## Next concrete action (substantive backlog — all GATED on Tom)

The wiki-improvement backlog is **exhausted** (the consolidation is done; nothing un-gated and
worth-the-spend remains to *write*). The substantive next moves are the researcher's calls — unchanged
from the prior session:

1. **Relational pilot** — has a fetchable human convergence baseline
   ([`resource/hawkins-tangrams`](wiki/base/resources/hawkins-tangrams.md)), a sharpened design
   ([`open-question/relational-meaning-pilot`](wiki/findings/open-questions/relational-meaning-pilot.md)),
   and the literature gate discharged. **GATED on Tom's "Decision 9"** (whether to build/run the two-AI
   iterated-reference-game pilot at all). The *novel* live-vs-shuffled trajectory measure is not anchored
   by Hawkins (only the convergence baseline is). If green-lit, this is the most distinctive next experiment.
2. **AANN probe** — **GATED**: needs per-token surprisal (no 3-family OpenRouter logprob path). A real
   cloud path exists (Together echo-logprobs, <$1) but needs a **`TOGETHER_API_KEY`**
   ([`decisions/open/cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md)). If Tom adds the key,
   run the Option-A surprisal on one small model (flag the no-cross-family caveat).
3. **Image probe v2 / VWSD** (genuinely image-native) — **un-gated but low-motivation**: the text-only
   panel separates senses at ceiling even on the homonymy-enriched set, so there's no headroom signal to
   justify spend on a text-saturated re-run. Worth it only to push the grounding axis into image-native
   territory.

If no green-light arrives, further un-gated maintenance/writing is largely done — the next session would
have little non-filler consolidation left and should either wait for a Tom decision or do a fresh
end-to-end re-verification of source quotes.

## Blocked / pending Tom (2 open decisions + 1 open question, all non-blocking)

- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — AANN
  held (no 3-family logprob panel). Tom (reaffirmed): HOLD AANN, do other work.
- [`decisions/open/cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md) — add a
  `TOGETHER_API_KEY` to unblock the AANN Option-A surprisal (<$1)? Tom: not yet.
- **Relational "Decision 9"** (open-question, not a `decisions/` file) — run the two-AI iterated-reference
  pilot? Anchor + literature ready; needs Tom's go-ahead (the big, distinctive build).

## Reminder for the next cold-start

Charter `PROJECT.md`; schema `CLAUDE.md`; run discipline `PROTOCOL.md` ("continue working" ⇒ workflow
mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md) first, then `wiki/index.md`**;
reconcile `wiki/decisions/open/` (2 open, the non-blocking AANN/compute pair). The project is
**three-axis**: grammatical (robust), lexical (a+c supported; **b a powered null**), multimodal/grounding
(two negatives + a partly de-confounded lexicon–grammar bridge). **No un-gated, in-anchor,
worth-the-spend experiment is currently teed up** — the next substantive moves are Tom's (relational
Decision 9; the AANN key). This session's contribution was making the wiki internally consistent and its
provenance honest, not new findings.
