---
id: cxg-probing-anchor
title: What human-anchored resource grounds the general claim that CxG-probing surprisal is a valid operationalization of constructional meaning sensitivity?
status: open
opened: 2026-05-28
opened-by: subagent
contingent-artifacts:
  - claim/cxg-probing-surprisal-validity
---

# Decision: CxG-probing surprisal anchor (general)

## Question

[`claim/cxg-probing-surprisal-validity`](../../findings/claims/cxg-probing-surprisal-validity.md) asserts that contrasting model-assigned surprisal (continuation likelihood) on **form–meaning minimal pairs** is a valid operationalization of an LLM's *sensitivity to constructional meaning* — across constructions, not just AANN. Per the human-anchor verification gate ([`CLAUDE.md`](../../../CLAUDE.md) §Verification, [`PROTOCOL.md`](../../../PROTOCOL.md) §5.3), an empirical claim about LLM meaning needs an `anchors:` link to an in-repo `resource` page that bears on it. The general claim does not yet have an adequate one.

The only in-repo construction-grounded human resource is [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md). It is a **partial** anchor: it is exactly one form–meaning minimal-pair set (the AANN degenerate-variant design), with item-level MTurk acceptability ratings. It can validate the surprisal-contrast method *for AANN*. It cannot, on its own, ground a claim cast at the level of "minimal-pair surprisal in general."

The Weissweiler source itself flags this as the field-wide gap. From [`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md) (§3, summarized on the source page): the paper names the "absence of human-normed data for many constructions (making it hard to ground claims about model behavior against human behavior)" as a key open challenge. So the missing general anchor is not an oversight of this repo — it is a known hole in the CxG-probing program.

## Options

### A. Scope the claim down to its verified anchor; treat generality as conjecture (provisional default)

- Anchor the claim to [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) for the AANN instance, and state the cross-construction generality as a **provisional extrapolation** rather than a settled empirical fact — i.e. the method is *validated* only where a human-normed minimal-pair set exists, and AANN is currently the sole such set in-repo.
- **Pros**: honest about the evidence; the method-validity claim for AANN is genuinely anchored; no fabricated generality.
- **Cons**: the claim's headline ("valid operationalization") is then carried mostly by methodological argument (Weissweiler) plus one worked construction, not by a broad human-anchored battery.

### B. Acquire a broad human-normed minimal-pair resource and anchor against it

- Candidate resources: BLiMP (Warstadt et al. 2020 — 67 minimal-pair paradigms, human acceptability validated); SyntaxGym; the Weissweiler 2022 Comparative Correlative probe; Weissweiler 2024 "Constructions Are So Difficult" NLI challenge set. None is yet catalogued as an in-repo `resource` page.
- **Pros**: would let the general claim stand on a multi-construction human anchor; BLiMP in particular has published human agreement numbers.
- **Cons**: BLiMP/SyntaxGym are largely *Generative-Grammar* minimal pairs (grammaticality), not CxG form–meaning pairings — they anchor *form* sensitivity, which is precisely the formal-vs-constructional gap that [`claim/formal-competence-aann-ceiling`](../../findings/claims/formal-competence-aann-ceiling.md) warns against conflating. A grammaticality minimal-pair battery would over-claim if used to anchor *meaning* sensitivity. The CxG-native sets (Weissweiler 2022/2024) are construction-specific and not yet inspected in-repo.

### C. Split the claim: a method-validity claim (anchored to AANN) and a separate generality conjecture

- Keep [`claim/cxg-probing-surprisal-validity`](../../findings/claims/cxg-probing-surprisal-validity.md) narrow and AANN-anchored; spin out a `conjecture/cxg-probing-generalizes` for the cross-construction extrapolation, to be tested as more human-normed CxG resources are catalogued.
- **Pros**: cleanest separation of what is anchored from what is hoped.
- **Cons**: more pages; defers the interesting general claim.

## Provisional default (in force until Tom ratifies)

**Option A.** Anchor the claim to [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) as a partial (AANN-only) anchor, write the cross-construction generality in explicitly provisional language, and mark the claim `contingent-on: cxg-probing-anchor`. The claim's empirical force is restricted to: (i) the *method* (surprisal contrast on form–meaning minimal pairs) is sound where a human-normed minimal-pair set exists; (ii) AANN is the worked, anchored instance. Promotion to a general settled claim waits on either a ratified broad anchor (Option B) or the split (Option C).

## What would change the default

- If Tom wants the general claim to stand now, the cleanest move is Option B with a **CxG-native** human-normed set (Weissweiler 2022/2024), catalogued as a `resource` page first — *not* a Generative-Grammar grammaticality battery, which would re-import the formal-vs-constructional confound.
- If a broad CxG human-normed minimal-pair resource is judged unavailable, Option C (split) is the fallback.

## Notes for the resolver

Tom: the choice that bites is whether "valid operationalization" is allowed to be **general** now (needs Option B + a catalogued CxG human anchor) or stays **AANN-scoped** until then (Option A). A one-line ratification is enough; if choosing B, name the resource to catalogue.
