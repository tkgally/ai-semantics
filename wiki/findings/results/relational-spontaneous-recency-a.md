---
type: result
id: relational-spontaneous-recency-a
title: The spontaneous-recency arm (Option A) — both models recover a reassigned term by its most-recent binding (order-sensitive / non-commutative); the first positive evidence of order-sensitivity on the relational axis
meaning-senses:
  - relational
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-16
updated: 2026-06-16
links:
  - rel: depends-on
    target: result/relational-stamp-comprehension-b
  - rel: depends-on
    target: result/relational-history-perturbation-v4
  - rel: contradicts
    target: conjecture/commutative-convention
  - rel: supports
    target: claim/relational-order-sensitive-reassignment
  - rel: depends-on
    target: concept/relational-meaning
---

# Result: spontaneous-recency arm (Option A) — both models recover a reassigned term by its most-recent binding

> **Status: proposed (2026-06-16).** The **Option A** arm of the ratified decision
> [`decisions/resolved/relational-v5-text-position-neutralization`](../../decisions/resolved/relational-v5-text-position-neutralization.md)
> (adopt-default: B then A, staged). Both panel models passed the Option-B stamp-comprehension
> gate ([`result/relational-stamp-comprehension-b`](relational-stamp-comprehension-b.md): they
> read the round stamp as a recency value *on demand*), which made an A-null interpretable for
> the first time. This arm asks the next, decisive question: when a coined term is **reassigned**
> to different referents across stamped rounds — and the query does **not** mention recency — does
> a model **spontaneously** weight the round stamp (treat the most-recent agreement as operative:
> a *path-dependent / non-commutative* convention), or treat the history as an order-insensitive
> content-set (*commutative*)? **The answer is clean and identical across both models: they
> spontaneously recover the term by its most-recent binding.** This is **order-sensitivity
> (non-commutativity)** — the **first positive** result on the relational axis, and it
> **contradicts** [`conjecture/commutative-convention`](../conjectures/commutative-convention.md)
> in the regime where the history carries disambiguating recency information.
> `anchor: internal-contrast-only` (within-model contrast over byte-identical content; no
> human-comparison claim — ratified 2026-06-16).

## The question (precise)

v4 found both models follow physical **text-position**, not stamped chronology, in a
convention-recovery task; its binding caveat was *"position-following here is indistinguishable
from stamp-blindness."* Option B removed the stamp-blindness horn (both read the stamp on demand).
What stayed open is the genuinely relational question: when the operative convention depends on
*which agreement is most recent*, but the **query does not direct attention to recency**, do the
models spontaneously weight the round stamp? Equivalently — is the recovered convention a function
of the **content-set** (commutative) or of the **recency ordering** (non-commutative)? This is the
falsification test [`conjecture/commutative-convention`](../conjectures/commutative-convention.md)
itself names ("reassign a coined term mid-trajectory … test whether interpretation tracks *where*
in the sequence the change landed"), with v4's text-position confound removed by balanced rotation.

## Instrument (frozen; see PREREG)

Run dir: [`experiments/runs/2026-06-16-relational-spontaneous-recency-a/`](../../../experiments/runs/2026-06-16-relational-spontaneous-recency-a/).
Design: [`relational-spontaneous-recency-v5-optionA`](../../../experiments/designs/relational-spontaneous-recency-v5-optionA.md).

- A grid of **K=4 clearly-distinct figures** (label + short description) + a stamped history in
  which the coined term **`DAX`** is **reassigned** to the 4 figures across 4 **non-contiguous**
  rounds (e.g. `{2,4,7,9}`), **once each** — so the content-set is *symmetric* (all four figures
  are "called DAX") and **only recency disambiguates**, and the frequency heuristic is flat.
- Two query conditions, each its own balanced-block roster: **SPONT** (48 records/model;
  headline) asks *"Which of your figures does the term \"DAX\" refer to?"* — **no recency
  mention**; **DIRECT** (32 records/model; B-style explicit-recency) is the on-demand
  **manipulation check** that gates interpretability.
- **Shortcut-proof by construction.** Reuses the Option-B balanced-block proof, now over figures:
  every constant-physical-history-slot strategy, every fixed figure-preference ordering (incl.
  grid order), and the frequency heuristic all score **exactly 1/K = 0.25** — proven at build and
  on **six idealized-reader fixtures**, so only spontaneously reading the stamp as recency can beat
  chance. An **independent pre-run critic** (fresh agent) re-derived every bound from scratch (the
  full 8! figure-preference sweep + extra non-recency heuristics), ran the fixtures, and returned
  **GO** (binding carry-forward 3 satisfied); it also ruled the *distinct-figures* choice (no v4
  near-twins) *tightens rather than alters* the construct — near-twins would confound a recency
  failure with a discrimination failure.
- Forced single-label elicitation; strict parse; `finish_reason == "length"` never parsed.

## The headline (verified — numbers not altered)

Both models spontaneously recover the term by its **most-recent** binding, at ceiling:

| model | SPONT latest-binding rate | Wilson 95% | SPONT first-binding rate | pick==last-line | pick==first-line | DIRECT manip-acc (MR / LR) | NA | verdict |
|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.250 | 0.250 | **1.000** (1.000 / 1.000) | 0 | **SPONTANEOUS-RECENCY** |
| gemini-3.5-flash | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.250 | 0.250 | **1.000** (1.000 / 1.000) | 0 | **SPONTANEOUS-RECENCY** |

- **SPONT latest-binding rate = 1.000** for both, Wilson lower bound 0.926 — far above the 0.25
  chance floor that every position/lexical/frequency shortcut is pinned to. The models put
  **100%** of their SPONT mass on the figure agreed at the **maximum** round.
- **first-binding rate = 0.000**: the order-sensitivity is specifically **recency** (latest wins),
  not a generic order effect; the anti-recency (first-governs) direction is empty.
- **Physical-position-following is at exactly chance** (pick==last-line 0.250, pick==first-line
  0.250) — so this is genuine stamp-recency reading, **not** the text-position artifact v4 found.
  The geometry decoupling (Option A's whole point) worked.
- **DIRECT manipulation check = 1.000** on **both** directions (latest *and* earliest) — on-demand
  comprehension is intact in this very instrument, so the SPONT result is interpretable (it is not
  an instrument failure), and the SPONT/DIRECT contrast is purely the **query phrasing**.
- **Clean record:** 160/160 strict parses, 0 NA, 0 retried, 0 length-truncation.

**Discipline.** Independent pre-run critic GO (re-derived shortcut bounds from scratch; certified
unsolvable-by-shortcut). Independent **post-run verifier** reproduced every number from raw via its
own route (re-derived the max/min-round keys from the rendered lines, audited parses and cost,
confirmed the frozen sha256) — **REPRODUCED**, 0 mismatches.

## What this shows — and what it does NOT (binding scope)

**Shows (within-model, internal-contrast-only):** when a coined term is reassigned across stamped
rounds so that the content-set is symmetric and only recency disambiguates, **both models'
recovered convention is a function of the recency ordering, not the content-set** — they apply a
**latest-binding-wins** rule **spontaneously** (the query never mentions recency). The recovered
convention is therefore **order-sensitive / non-commutative** in this regime. This is the **first
positive** evidence of order-sensitivity on the relational axis (v1, v2, v3, v4 were nulls or
position artifacts).

It does **NOT** show:

- **Not "rich constitution."** Order-sensitivity here is consistent with a thin **convention-update
  / overwrite** rule ("the latest agreement supersedes earlier ones"), which is order-sensitive but
  is **not** the deep [`concept/relational-meaning`](../../base/concepts/relational-meaning.md)
  notion of a convention *constituted between* agents through the live trajectory. This result
  falsifies *commutativity* (the order-invariance bet); it does **not** by itself certify
  constitution. It is the bottom rung of order-sensitivity, not the top.
- **Not "spontaneous with no scaffolding."** The INTRO tells the model the term *"was reassigned …
  in different rounds you agreed it referred to different figures"* — priming that a *choice among
  bindings* is required. "Spontaneous" here means **the query itself does not direct attention to
  recency** (it asks only which figure the term refers to), **not** that there is no cue at all.
  A commutative reader, even told the term was reassigned, has no basis to prefer one binding (it
  could weight first, most-frequent, or be at chance); the models specifically prefer the **latest**.
- **Not a human comparison** (`anchor: internal-contrast-only`). No in-repo resource grounds human
  order-/path-sensitivity at this grain (Brennan & Clark report an order-*insensitive* statistic),
  and none is owed because no human contrast is asserted.
- **Not an overturning of v4 or v1.** Those were settings where order carried **no disambiguating
  information** (v1's static record fixed a unique referent from content alone) or where stamped
  chronology was **confounded with physical position** (v4). This arm constructs the setting v1's
  own caveat 2 flagged as missing — content symmetric, order the *sole* disambiguator — and finds
  the models use order. So commutativity is **operationalization-dependent**: it appears where
  order carries no disambiguating signal, and **fails (order-sensitivity appears) where it does.**

## Why it matters

This is the relational track's first positive: the project's deflationary bet that LLM referential
conventions are *commutative* (order-invariant, set-based — [`conjecture/commutative-convention`](../conjectures/commutative-convention.md))
is **falsified in the regime that can actually test it.** When the interaction history carries
disambiguating recency information, both separately-trained models behave **non-commutatively**,
recovering the most-recent binding without being told to. The clean positive is promoted to
[`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)
(scoped, internal-contrast-only), and the conjecture is retired with its bounded nulls preserved.

## Honesty box

- **Ceiling effect, two independent models, n=48/model SPONT.** Not marginal: Wilson LB 0.926,
  position at exactly chance, DIRECT at ceiling, 0 NA. About as clean as a behavioural contrast gets.
- **One instrument, one operationalization.** The reassignment-of-a-term frame is one way to make
  order disambiguating; the result is scoped to it. Whether order-sensitivity persists under other
  framings (image referents, cross-family dyads, non-overwrite repairs) is open.
- **Thin vs rich order-sensitivity un-separated.** "Latest-binding-wins" could be a shallow update
  heuristic or a deeper path-dependence; this arm does not separate them. The claim is held to
  order-sensitivity, not constitution.
- **Spend.** 160 finding-bearing calls + 2 liveness = **$0.124444 billed** (`usage.cost`-summed,
  0 missing), inside the $0.50 per-run hard stop and the $5.00/day cap (day total $0.177).
