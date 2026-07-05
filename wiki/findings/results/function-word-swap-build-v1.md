---
type: result
id: function-word-swap-build-v1
title: Function-word swap probe — build v1 is a NO-GO; faithful frequency+length matching starves the matched set to ~66 clean items (well below the ≥200 target), and the the→a determiner swap admits no frequency-matched content control at all
meaning-senses:
  - constructional
  - distributional
  - inferential
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-21
updated: 2026-07-05
links:
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: refines
    target: conjecture/function-word-substitutability
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Function-word swap probe — build v1: a certified NO-GO (matching starves the set)

> **This is a BUILD / feasibility result, not a model result. No model was called ($0).** It
> records what the build session learned trying to construct the frozen, certified
> minimal-pair set the ratified
> [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)
> requires for [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md).
> It makes **no claim about LLM behavior** (anchor: `internal-contrast-only` in the sense that
> it asserts nothing requiring a human comparison). It forced the decision
> [`decisions/resolved/function-word-count-vs-matching`](../../decisions/resolved/function-word-count-vs-matching.md),
> **resolved 2026-06-21 (session 68, adversarial review)**. Run:
> `experiments/runs/2026-06-21-function-word-vs-content-swap/`.
>
> **Correction (2026-06-21, session 68 adversarial review).** An earlier version of this page
> said the v1 set was "sound on every matching/shortcut-reader/integrity check" and "fails only
> the count." That **overstated** it. `certification.json` records `"ok": false` with **three**
> fails: (e) ≥200 count, (e) **≥4-class span** (only 3 viable classes survive — adjective is
> dead), **and (i) the freq-only-reader check** (`max POSITIVE threshold asymmetry ≤ 0.12` =
> FALSE, 0.1212 at θ=1.25, because the `because`-arm content gap 1.335 sits below the function gap
> 1.406). The set passes minimal-pair integrity, the length-only-reader check (asymmetry 0.0), and
> the no-leak check; it does **not** pass every shortcut-reader check. Both extra failures are
> fixable in build-v2 and are now binding conditions of the resolved decision.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The widened build-v2 ran the same day
> (2026-06-21): [`result/function-word-swap-run-v2`](function-word-swap-run-v2.md) reached 206
> certified matched items (inventory-widening per the resolved decision, certification `"ok": true`
> before any model output) and returned **CONFIRM 3/3** — function-word swaps flip NLI far more than
> frequency+length-matched content-word swaps. The conjecture
> [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md)
> is now `tested`.
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## What was attempted

The probe operationalizes the conjecture as an **entailment-flip contrast**: build minimal
pairs where a **function-word swap** (`because`→`although`, `some`→`every`, `will`→`would`) is
applied in the premise only, and a **frequency+length-matched content-word swap** is applied
consistently in both premise and hypothesis; then ask whether each swap flips a 3-way NLI
judgment, and compare the function-swap flip rate to the content-swap flip rate. The matching
(binding conditions of the ratified decision) requires each content control to sit within
**|ΔLg10WF| ≤ 0.10** of its function word at **both** ends (mirrored within-pair spread) and to
match its **length**. The full pipeline was written — `build.py` (assembly + matching),
`certify.py` (shortcut-reader + integrity certification), `probe.py` (the NLI instrument,
reused verbatim from the CxNLI line), `analyze.py` (flip-rate contrast + bootstrap) — and the
set was frozen and certified **before any model output**.

## The finding (three matching facts, one decision)

**1. A length-only reader forces a *signed +1* content length-match — which is what starves the
supply.** Every named function swap lengthens the word by exactly one character
(`because`→`although`, `some`→`every`, `will`→`would`). The build's first certification pass
showed that if content swaps are length-neutral (Δ0), a **length-only reader reproduces the
entire function>content asymmetry** (asymmetry 0.46) — flagging all +1 function swaps and no Δ0
content swaps. Binding condition (i) forbids this, so content swaps must also be uniformly +1
(after the fix, length-only asymmetry = **0.0 exactly**). But requiring content swaps to be
frequency-matched at both ends **and** +1 in length **and** coherent collapses the supply.

**2. Under faithful matching, ~66 clean items across only 3 viable content semantic classes
survive — versus the ≥200 / ≥4-class confirm criterion.** The certification passes minimal-pair
integrity, the **length-only-reader** check (asymmetry 0.0), and the no-leak check, but
`certification.json` is `"ok": false` on **three** checks: the **count** (66 < 200), the
**class span** (3 < 4 — adjective dead), **and** the **freq-only-reader** shortcut check
(`(i) max POSITIVE threshold asymmetry ≤ 0.12` = FALSE at 0.1212, θ=1.25 — the frequency residual
the independent-review section item (d) flags, which the earlier version under-counted as merely
"small" while wrongly calling the set sound on every shortcut check).
Specifically:
- The high-yield **person-noun route dies**: no open-class person noun sits at Lg10WF ≈ 3.33
  (to match `although`) with +1 length against a ≈ 4.74 partner.
- The **`the`→`a` determiner swap admits *no* frequency-matched open-class content control** —
  no content word reaches Lg10WF ≈ 6.0 (the resource page
  [`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md) predicted
  exactly this). It can run only as a **function-only characterizing arm** (no contrast).
- The **adjective content class has no clean frequency+length-matched swap** (the only matched
  candidates — *sure*→*tight/empty/heavy* — are semantically anomalous, so a flip would reflect
  oddness, not relation change; removed on the independent reviewer's catch).
- `some` and `will` are intrinsically low-yield: a **single** matched content out-word each
  (`some`: *man*; `will`: *see*), so most of any larger count would be carrier-repetition of a
  handful of swaps, not lexical diversity.

**3. The decision anticipated exactly this** ("over-matching can leave too few items to reach
the ≥200-pair target … a NO-GO defers the run rather than relaxing the matching"). The build is
that deferral, made decidable in — and now **resolved** by (2026-06-21, session 68, adversarial
review) —
[`decisions/resolved/function-word-count-vs-matching`](../../decisions/resolved/function-word-count-vs-matching.md).
The reviewer **overturned** the provisional "relax length to a regressed covariate" default
(length is degenerate in the function arm — every function swap is +1 char, so Δlen ≡ +1 with
zero variance, perfectly collinear with condition; it cannot be regressed out and must stay a
hard freeze-time gate) and adopted **inventory-widening** instead: add new function-word swap
pairs at the **unchanged** ±0.10 frequency tolerance with a per-pair signed-Δlen gate, plus
capped carrier-authoring, also fixing the freq-only residual (point 4 below) and keeping the
≥200/≥4-class bar.

## Independent pre-run review — VERDICT: NO-GO (confirmed, strengthened)

A fresh-agent adversarial reviewer reproduced the build and certification, and independently:
(a) **confirmed ≥200 is near-infeasible under faithful matching** (generous authorable ceiling
~150–160 items, dominated by carrier-repetition of a few swaps — `some:noun_person` has only
*man*, `will` only *see*); (b) **caught ~14% broken items** the session had not fully
coherence-checked (5 ungrammatical `some:verb` "say the <person>" frames; 6 anomalous
`because:adj` items) — **now purged**, which is why the clean count fell to 66; (c) confirmed
**both confound controls are sound** — the +1 length match is genuinely necessary, and the
consistent-content-swap-in-both-premise-and-hypothesis design is not rigged (it biases toward
the null, since preserving the relation predicts a non-flip); (d) flagged a small **frequency
residual** (because content gap 1.34 < function gap 1.41, because the available high-frequency
intransitive verbs *talk/call* sit ~0.10 below *because*) — fixable next build by choosing OUT
verbs nearer/above *because*. **Do not relax the ratified tolerances autonomously; defer.**

## What this does and does not establish

- **Does:** it is a concrete, quantified measurement of the **matching-vs-power tension** the
  decision foresaw — a methods finding about *operationalizing* the function/content contrast
  under a single corpus frequency norm. The determiner-swap result (no frequency-matched content
  control exists for `the`→`a`) is a clean structural fact about closed-class frequency.
- **Does not:** say anything about whether function-word swaps actually shift LLM behavior more
  than content-word swaps — the conjecture
  [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md)
  stays `designed` and **untested**. The build pipeline is complete; build-v2 must widen the
  function-word inventory to reach ≥200 / ≥4 classes and fix the freq-only residual (per the
  resolved decision), then re-freeze + re-certify under a fresh pre-run critic before any run.
