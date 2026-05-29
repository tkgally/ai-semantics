---
id: lexical-sense-gradience-anchor
title: Which human-rated resource should anchor the lexical sense-gradience conjecture — and is graded usage-similarity (Usim) the right one?
status: resolved
resolved: 2026-05-29
resolution: "Option B — anchor on a DIFFERENT graded set, NOT Usim. Ratified by Tom 2026-05-29. Usim is retired as the candidate anchor: this session's inspection verified its scale (5-point) and counts (34 lemmas / 1530 pairs / 3 annotators) from primary sources, but the released file is not currently fetchable (Box 404 / mirror 503) and carries no explicit data license — so it fails the fetchability + license preconditions. The conjecture's monotonicity clause still needs a GRADED, RELEASED, LICENSED usage/sense-similarity resource; the specific set is to be IDENTIFIED + VERIFIED by a follow-on run before it is the in-repo anchor. Leading candidates (none yet verified in-repo): DWUG / Diachronic Word Usage Graphs (Schlechtweg et al.; graded 4-point usage-similarity judgments in the Usim tradition; CC BY; on Zenodo/GitHub) and CoSimLex (SemEval-2020 Task 3; graded word similarity in context; released). WiC (binary, CC BY-NC 4.0) remains the discrete cross-check. Until a specific graded set is verified + mirrored, the conjecture stays `proposed`/anchor-pending-identification and may not promote a result; this is a build/verify task, not a re-decision (Tom has fixed the DIRECTION: a different graded set, not Usim)."
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

## Update 2026-05-29 — the requested Usim inspection ran (surfacing, not resolving)

The inspection that Option A was made contingent on has now been done (results folded into [`resource/wic-graded-usage-similarity`](../../base/resources/wic-graded-usage-similarity.md)). Findings, from primary sources actually retrieved:

- **Scale + counts now VERIFIED** (ACL 2009 PDF `aclanthology.org/P09-1002.pdf`, HTTP 200; Erk guidelines page, HTTP 200): the graded scale is **1 – completely different, 2 – mostly different, 3 – similar, 4 – very similar, 5 – identical** (+ "Cannot Decide"); **Usim = 34 lemmas, 45 sentence-pairs/lemma = 1530 pairs, 3 native-British-English annotators, LEXSUB source**. (This corrects the page's earlier "~11 lemmas / ~430 items" figures, which actually describe the companion **WSsim** set.)
- **Two ratification preconditions remain UNMET:** (i) **fetchability** — the advertised release file (`utexas.box.com/.../…lywbnl.tgz`) returns **HTTP 404** and the McCarthy mirror **HTTP 503**; no working public mirror found 2026-05-29. (ii) **license** — no formal data license exists, only an email-courtesy request on Erk's page; the ACL paper's CC BY-NC-SA 3.0 licenses the *publication*, not the dataset.

So the **intellectual fit is confirmed** (graded scale grounds the monotonicity clause WiC cannot) but **access/licensing is the standing blocker**. This does not resolve the decision. It sharpens the choice for Tom: ratify Option A *pending a successful re-fetch + license confirmation* (e.g., emailing Erk), or fall toward **Option C** (queue a wanted-resource request) to unblock the conjecture sooner without that dependency. The resource page `status` stays `external-only` until the file is actually fetched and licensed.

## Notes for the resolver

Tom: a one-line ratification is enough — "Usim + WiC, pending inspection", "use WSsim instead", or name a specific graded dataset. Reminder: the conjecture's prediction 2 (polysemy-vs-homonymy intermediate regime) needs a polysemy/homonymy stratification layered on whatever anchor is chosen; that is a build step, not a property of any released ratings, and should be frozen with the item set before any probe runs (a separate operationalization gate the conjecture's *Notes* flags).
