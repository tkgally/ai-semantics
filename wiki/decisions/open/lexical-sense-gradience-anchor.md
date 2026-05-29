---
id: lexical-sense-gradience-anchor
title: Which human-rated resource should anchor the lexical sense-gradience conjecture — and is graded usage-similarity (Usim) the right one?
status: open
opened: 2026-05-29
opened-by: orchestrator
contingent-artifacts:
  - conjecture/lexical-sense-gradience
---

# Decision: lexical sense-gradience anchor

## Question

[`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) — the project's first **lexical** conjecture — claims an LLM's same/different-sense behavior is *monotonic in human-rated usage similarity*, with an intermediate regime for polysemy absent for homonymy, separable from a context-similarity shadow. The monotonicity clause needs a **graded** (not binary) human sense/usage-relatedness resource as its anchor. None is in-repo. This decision picks the anchor (and queues the fetch/inspection).

The load-bearing property the anchor must have: **graded** per-pair human judgments of usage/sense relatedness. A binary same/different set (WiC) cannot ground monotonicity — it can only ground the discrete cross-check.

## Options

### A. Usim graded usage-similarity (Erk, McCarthy & Gaylord), with WiC as binary cross-check (provisional default)

- **What:** the Usim usage-similarity ratings (graded 5-point human judgments of how similar two usages of a target lemma are), catalogued at [`resource/wic-graded-usage-similarity`](../../base/resources/wic-graded-usage-similarity.md); WiC (Pilehvar & Camacho-Collados 2019, binary, CC BY-NC 4.0) as the discrete cross-check.
- **Grounds:** the monotonicity prediction (Usim's graded scale) + the binary baseline (WiC).
- **Limits (real, must be cleared before ratification):** the Usim resource is `external-only` — its **license, exact scale wording, and item counts were not verified from a primary source** this run (the download/journal pages 503'd / 403'd / were paywalled on 2026-05-29). Usim also does **not** tag pairs as polysemy vs. homonymy, so prediction 2 needs an added stratification step. Small N (~hundreds of items, ~11 lemmas, provisional).

### B. A different graded sense resource

- E.g. the companion **WSsim** (graded per-WordNet-sense applicability, same release) for the over-/under-splitting framing; or a SemEval graded-sense / lexical-substitution set; or a more recent graded word-in-context dataset if one with released per-item graded human ratings is identified.
- **Why consider:** if Usim's license/availability cannot be confirmed, or if the over-/under-splitting arm is preferred over the monotonicity arm.

### C. Defer and queue a wanted-resource request

- If neither A nor B is confirmed graded-and-licensed, hold the conjecture at `proposed`/`anchor: pending` and add a [`base/wanted.md`](../../base/wanted.md) request for a released graded usage-similarity / sense-relatedness dataset (existing released ratings only — no new human-subject collection, charter §8).

## Provisional default (in force until Tom ratifies — conjecture stays untested)

**Option A** (Usim as the graded gradience anchor, WiC as the binary cross-check), **contingent on a future run actually inspecting the Usim release** to confirm (i) its license, (ii) the exact graded scale, (iii) item/lemma/annotator counts, and (iv) that the data is fetchable. If that inspection fails (license unclear or data unreachable), fall back to Option B or C. Until inspected and ratified, the conjecture carries `contingent-on: lexical-sense-gradience-anchor` and may not promote a result.

Rationale: Usim is the cleanest in-literature graded usage-similarity signal and directly grounds the monotonicity clause that WiC cannot; but its in-repo provenance is currently too thin to ratify outright.

## Notes for the resolver

Tom: a one-line ratification is enough — "Usim + WiC, pending inspection", "use WSsim instead", or name a specific graded dataset. Reminder: the conjecture's prediction 2 (polysemy-vs-homonymy intermediate regime) needs a polysemy/homonymy stratification layered on whatever anchor is chosen; that is a build step, not a property of any released ratings, and should be frozen with the item set before any probe runs (a separate operationalization gate the conjecture's *Notes* flags).
