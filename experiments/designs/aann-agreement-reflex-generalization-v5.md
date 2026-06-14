---
type: design
id: aann-agreement-reflex-generalization-v5
title: AANN agreement-reflex generalization v5 — does gpt-5.4-mini's singular-agreement reflex (+0.74 v3 / +0.65 v4) replicate on fresh HELD-OUT items, and do claude/gemini show any contrast off the ceiling? Headline = the v4 was/were agreement arm, unchanged; with a DESCRIPTIVE-ONLY count-noun ceiling diagnostic
meaning-senses:
  - constructional
  - functional-vs-formal
  - distributional
status: "drafted — NOT RUN; design only (no model calls made)"
contingent-on: []
created: 2026-06-14
updated: 2026-06-14
links:
  - rel: operationalizes
    target: conjecture/aann-construction
  - rel: depends-on
    target: result/aann-inferential-v4
  - rel: depends-on
    target: result/aann-inferential-v3
  - rel: depends-on
    target: decisions/resolved/aann-inferential-operationalization
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
---

# Experiment design v5 — AANN agreement-reflex generalization (does the singular reflex replicate on fresh held-out items, and across the panel?)

> **⚠️ DRAFT — DESIGN ONLY — NOT RUN. No model calls have been made.** This is a design-writing
> artifact. **No probe has run; no v5 number exists anywhere** in this design, the stimuli, or the
> code; the cost figures are **ESTIMATES for a not-run experiment, labelled as such.** The v5 probe
> may run **only after** a **fresh independent pre-run critic** reviews this design *plus* a frozen
> `PREREG.md` *plus* the frozen `stimuli.json`, and returns GO. The run, if it happens, stays
> **`anchor: internal-contrast-only`** (within-model contrast; no human-comparison claim).

## Why v5 exists

NEXT.md backlog item 2(a): **does gpt-5.4-mini's singular-agreement reflex generalize across the
panel and to held-out items?** This *reuses the v2 form-instrument family; no new decision.*

The reflex, established by the prior two runs: in the AANN frame (*A beautiful three days ___ what we
needed*) gpt-5.4-mini picks singular *was*; in the bare-plural control (*Three beautiful days ___ what
we needed*) it picks plural *were* — an agreement **shift**. The two prior results, quoted **verbatim**
(no new numbers invented):

- [`result/aann-inferential-v3`](../../wiki/findings/results/aann-inferential-v3.md): "**+0.739 · CI
  [0.57, 0.91] · POSITIVE**" — "it picks singular *was* for the AANN frame (0.96) but plural *were*
  for the matched control (0.22 *was*), a +0.74 shift with a CI well clear of zero."
- [`result/aann-inferential-v4`](../../wiki/findings/results/aann-inferential-v4.md): "**+0.652**
  CI[0.43,0.87] · **POS**" — "raw 'was' rate, AANN / bare-plural ctrl: 0.957 / 0.304"; "The
  grammaticalized reflex **replicates v3** (v3: +0.74; v4: +0.65)."

And the other two models, quoted verbatim from v4: "**claude-sonnet-4.6 and gemini-3.5-flash** … the
agreement reflex is **flat at ceiling** (both pick singular *was* for the AANN **and** the bare-plural
control … exactly as in v3)" — "raw 'was' rate, AANN / bare-plural ctrl: 1.00 / 1.00" for both. So the
contrast was **uninformative** (structurally blind) for them, **not** a demonstrated failure.

Two questions remain open after v3/v4, both about **generalization**, and both answerable with the
**same instrument, run unchanged on fresh items**:

1. **Replication on held-out items.** v3 and v4 reused the *same* base adjective×measure-noun items.
   Does gpt's reflex **replicate on fresh held-out items** it has not been probed on in this line — or
   was the v3/v4 effect tied to those particular items?
2. **Panel generalization off the ceiling.** claude and gemini sat at the AANN/bare-plural ceiling
   (both pick *was* for both frames). Held-out items give a *second* sample: do they **still** sit at
   ceiling (confirming the v3/v4 reading that the contrast is structurally blind for them), or do they
   show any off-ceiling contrast on fresh items?

## What this design is (and is NOT)

- **The headline instrument is the v4 agreement arm, UNCHANGED.** Same was/were forced choice, same
  two conditions (AANN / **bare-plural** control), same single-contrast indicator
  P(was|AANN) − P(was|control), same per-model counterbalancing via `agr_letter_was`, same bootstrap
  machinery. The *only* change is the **items are fresh held-out** combinations, and the agreement
  single contrast is now the **headline** (in v3/v4 it was the load-bearing *sub-probe* of a larger
  paraphrase/NLI design; here it stands alone).
- **No new operationalization, no new decision page.** See the **Gate check** section below: the
  agreement was/were sub-probe is the ratified *load-bearing discriminator* of
  [`decisions/resolved/aann-inferential-operationalization`](../../wiki/decisions/resolved/aann-inferential-operationalization.md)
  (Condition 3); v5 stays squarely inside that ratified instrument class. The freshness change reuses
  the **v2 form-instrument family** (graded acceptability / agreement on novel adjectives) the way the
  v2b held-out gradient run already did. **No `wiki/decisions/open/` entry is required.**

## 1. Construct

The AANN measure-phrase subject (*a beautiful three days*) takes **singular** agreement despite the
plural noun head — the grammaticalized morphosyntactic reflex of the construction's unification
(single-unit) construal. This is the one place the **distributional-shadow** story predicts the
*opposite* of the inferential story: singular agreement on a plural head is **distributionally
dispreferred** in general text, so a model that picks *was* for the AANN subject specifically is
cutting against the local distributional gradient. That is exactly why the agreement contrast was
elevated to the **load-bearing discriminator** in the governing decision, and why it is the right —
and the only — instrument needed for a clean generalization test.

## 2. Scope and freshness (held-out items)

- **Measure-noun classes:** temporal + distance only — the "genuine extents" the v3/v4 line kept
  (object/mass dropped after the v3 repair). 30 held-out items: **18 temporal, 12 distance**.
- **Held-out adjectives (binding exclusion).** None of the 21 adjectives used in v3/v4 may reappear:
  *beautiful, gruelling, glorious, miserable, restful, punishing, memorable, turbulent, sleepless,
  hectic, blissful, brutal, frantic, scenic, muddy, breathtaking, steep, lonely, treacherous,
  dazzling, relentless.* Every v5 adjective is fresh (e.g. *exhausting, joyful, chaotic, harrowing,
  idyllic, festive, serene, dismal, jubilant, sweltering, frigid* for temporal; *winding, rugged,
  gritty, arduous, dusty, slick, craggy, marshy, jagged, boggy, rocky, snowy* for distance), and each
  adjective × measure-noun combination is fresh. The freshness exclusion is asserted in `stimuli.json`
  (`freshness_note`) and is a pre-run-critic check.
- **Evaluatively-loaded adjectives**, the same register as v3/v4, so the items are well-formed AANNs;
  items where world-knowledge *alone* would force singular agreement are avoided at authoring.

## 3. Instrument — the headline agreement arm (v4, unchanged)

Per held-out item, two frames asked as a **was/were forced choice** (single-token A/B pick, the v4
`P_AGR` wording verbatim):

- **AANN frame** — *A {adj} {number} {noun} ___ …* (the singular-agreement environment the
  construction licenses; expected *was*).
- **bare-plural control frame** — *{number} {adj} {noun} ___ …* (the plural control; expected *were*).

**Indicator (per model):** **agreement shift = P(was|AANN) − P(was|bare-plural control).** The was/were
letter position is **counterbalanced per item** (`agr_letter_was` ∈ {A,B}, 15/15 across the 30 items),
and `analyze.py` maps the chosen **letter back to content** so position bias is blocked at the
stimulus level — identical to v4.

## 4. Descriptive-only count-noun ceiling diagnostic (NON-GATING)

A small set (10 items) of **true COUNT-noun bare plurals** — e.g. *Three excited dogs ___ waiting at
the gate* — where the bare plural robustly takes **were**. Asked as the same was/were forced choice.

- **Purpose.** It tests whether claude/gemini (which sit at the AANN/quantity ceiling, both picking
  *was*) **can** pick *were* for a genuine count plural — isolating whether their ceiling is
  **notional-singular-for-quantity-subjects** (a duration/amount subject pulls singular regardless of
  the article cue, as v3/v4 read it) rather than a **blanket "always picks was."** If a ceiling model
  picks *were* near-universally here, its AANN/bare-plural ceiling is the *quantity-subject* reading,
  not an inability to choose *were* at all.
- **It is DESCRIPTIVE-ONLY and NEVER verdict-bearing.** It enters **no branch** of the frozen verdict
  tree (§6). `analyze.py` computes it in a function (`analyze_diagnostic`) flagged
  `descriptive_only: true` / `never_verdict_bearing: true`, and the selftest asserts it never appears
  in the verdict basis. This is marked clearly here, in `PREREG-draft.md`, and in `analyze.py`.

## 5. Tier-0 manipulation check (gating, mirrors v4's discipline)

12 clearly grammatical-vs-ungrammatical was/were pairs with **unambiguous singular/plural subjects**
(*The dog ___ asleep* → *was*; *The dogs ___ asleep* → *were*), 6 singular + 6 plural, the
correct-answer letter balanced 6/6 and the was-position balanced 6/6 and uncorrelated with subject
number. This confirms each model **reads the was/were task at all**.

- **Pass:** ≥ 10/12 correct per model (inclusive); > 25% missing = instrument failure.
- **Pre-declared failure consequence:** a model failing Tier-0 has its agreement numbers reported
  **descriptively only** and is **excluded** from a verdict-bearing category — its cell resolves to
  INCONCLUSIVE-CELL (it does not count as REPLICATES / GENERALIZES / FAILS). If the **reflex-bearer
  (gpt)** fails Tier-0, the overall verdict is **INCONCLUSIVE**.

## 6. Frozen verdict map (ordered if/else as CODE in `analyze.py`, with an explicit final else)

All thresholds are **pinned in `PREREG-draft.md`** and **baked in `analyze.py`** before any data;
none may be set or retuned from any pilot output. **Bar τ = +0.30** (inclusive), with a
PREREG-seeded **item-level bootstrap 95% CI** whose **lower bound must exceed 0** for a "positive"
shift; a degenerate zero-width CI (an all-ceiling cell) carries **no inferential weight**. **Ceiling
threshold = 0.85** (control was-rate). **Item floor = 8** gated items per verdict-bearing cell.

**Per the reflex-bearing model (gpt-5.4-mini, slot B):**

- **REPLICATES** if the held-out agreement shift ≥ τ (+0.30) **and** bootstrap CI-lower > 0.
- else **FAILS-TO-REPLICATE.**

**Per claude (A) / gemini (C):**

- **CEILING-UNINFORMATIVE** if the control "was"-rate ≥ 0.85 (the discriminator is structurally blind,
  as in v3/v4 — both AANN and bare-plural pull singular agreement, so the contrast has no room to show;
  this is **not** a failure).
- else **GENERALIZES-TO-PANEL** if the shift ≥ τ and CI-lower > 0.
- else **NO-REFLEX.**

(Any cell below the item floor, or whose model failed Tier-0, resolves to **INCONCLUSIVE-CELL** and is
kept out of the positive branches.)

**Overall verdict (exhaustive, with an explicit final else):**

- **REFLEX-GENERALIZES-TO-PANEL** — ≥ 1 of {claude, gemini} GENERALIZES-TO-PANEL (this outranks gpt's
  own outcome: a panel finding stands regardless).
- else **REFLEX-IS-GPT-SPECIFIC-AND-REPLICATES** — gpt REPLICATES and neither other model generalizes
  (both at ceiling or no-reflex): the reflex is gpt-specific and robust to held-out items.
- else **REFLEX-FAILS-TO-REPLICATE** — gpt FAILS-TO-REPLICATE and neither other model generalizes.
- else **INCONCLUSIVE** — the final else (e.g. gpt's cell did not resolve to REPLICATES /
  FAILS-TO-REPLICATE because of a Tier-0 failure or item-floor breach, and no other model generalizes).

The tree is exhaustive: every combination of per-model categories maps to exactly one overall label,
the final `else` catching anything the three substantive branches do not. `analyze.py --selftest`
exercises every branch (REPLICATES / FAILS / both-ceiling / GENERALIZES / NO-REFLEX, and all four
overall labels including the generalize-outranks-gpt-fail case).

Every outcome — including REFLEX-FAILS-TO-REPLICATE, every CEILING-UNINFORMATIVE cell, and
INCONCLUSIVE — is a **first-class result.** A held-out failure to replicate would be a genuine,
publishable-in-repo null (it would weaken the v3/v4 reflex claim); a ceiling-uninformative outcome for
claude/gemini would *confirm* the v3/v4 structural-blindness reading on a second item sample.

## 7. Anchor discipline (`internal-contrast-only`)

The v5 result will carry **`anchor: internal-contrast-only`** — its force is the **within-model**
AANN-vs-bare-plural agreement shift (does the construction shift the singular-agreement choice relative
to a matched bare-plural control). **No human-comparison claim is made**, and **no in-repo resource
anchors agreement-reflex behavior**: there is no human dataset of AANN-subject agreement judgments in
the repo, so a human-comparison claim is impossible and is not attempted. This terminal state carries
forward from the governing decision
([`decisions/resolved/aann-inferential-operationalization`](../../wiki/decisions/resolved/aann-inferential-operationalization.md),
which ratified `internal-contrast-only` for this AANN inferential line; precedent
[`decisions/resolved/conflicting-cue-human-anchor`](../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)).

[`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md) is
linked **only as stimulus-class provenance** (the AANN measure-noun classes — temporal/distance — the
items reuse). Mahowald's MTurk data are 1–10 **acceptability** ratings; no human there was asked an
agreement question, so the resource is **CLASS PROVENANCE ONLY**, never an inference/agreement anchor.
The expected-agreement **key** (singular *was* = AANN-licensed; plural *were* = bare-plural ordinary)
is **EXPERT-STIPULATED** — the design author's coding of the published AANN semantics (Solt 2007
unit-coercion; Dalrymple & King 2019; Bylinina & Nouwen 2018 — named as the analyses the stipulation
rests on, **not** quoted, **not** in-repo). It is a scoring key, **not** behavioral-human data; the
agreement *shift* is a within-model contrast that does not even depend on the key (it compares the
model to itself across two frames).

**Chief-cost statement (verbatim, binding on the result page):** *the v5 can never say "models pick
the singular agreement the way humans do" — only that the construction shifts the within-model
singular-agreement choice relative to a matched bare-plural control, in the direction the published
AANN semantics predicts.*

## 8. Gate check — why this is inside the ratified instrument class (NO new decision)

The single value-laden call in any AANN probe is the operationalization of the construction's
meaning into an indicator; that call was **already made and ratified** by
[`decisions/resolved/aann-inferential-operationalization`](../../wiki/decisions/resolved/aann-inferential-operationalization.md)
(autonomous adversarial review, 2026-06-13). Its **Condition 3** names the **grammaticalized singular/
plural agreement sub-probe** the **load-bearing discriminator**, controlled by the **bare plural**.
v5 uses **exactly that instrument**, **unchanged** — same frames, same control, same indicator, same
counterbalancing. The freshness change (held-out adjectives) reuses the **v2/v2b form-instrument
family**, which the v2b held-out gradient run already established as a within-class generalization
move (novel-adjective generalization of a ratified acceptability/agreement instrument). Therefore:

- **No new operationalization decision is taken** — v5 does not pick a *new* indicator; it re-runs a
  ratified one on a fresh item sample.
- **No `wiki/decisions/open/` entry is required** — there is no open operationalization or
  human-anchor question. The anchor (`internal-contrast-only`) was ratified for this line.
- The freeze + fresh-pre-run-critic gate **still binds** (CLAUDE.md run discipline): the critic checks
  freshness (no v3/v4 adjective reused), the agreement-arm fidelity (control = bare plural; indicator =
  the single shift), the diagnostic's descriptive-only fencing, Tier-0 balance, and the frozen verdict
  tree — but this is a **materials/PREREG review**, not a new operationalization ratification.

So v5 is `contingent-on: []`: it adds no contingency, because it introduces no new decision.

## 9. Cost — ESTIMATE only (for a NOT-RUN experiment)

**This estimate is for a run that has NOT happened. No model calls have been made.** Geometry (frozen
in `stimuli.json`):

| Arm | Items × frames × models | Calls |
|---|---|---|
| `agreement` (headline) | 30 held-out × 2 frames × 3 | 180 |
| `diagnostic` (descriptive-only) | 10 count-noun × 1 × 3 | 30 |
| `tier0` | 12 pairs × 1 × 3 | 36 |
| **Total** | | **246** (82/model × 3) |

**Pre-flight dollar ESTIMATE from v4's measured billed rate.** v4 ran 831 calls for **$0.1266 billed**
= **~$0.00015 per call** (billed `usage.cost`). At the same per-call shape (single-token A/B picks),
**246 × ~$0.00015 ≈ $0.037**; allowing for the one verbatim retry per unparseable response and
variance, **expected ≈ $0.03–0.06 billed.** This lands **far under $1** and **far under the $5.00/day
UTC budget cap** ([`config/budget.md`](../../config/budget.md)). A single-run **ABORT_USD = $0.25**
flag is coded in `probe.py` (well under the day cap). **These are estimates for a not-run experiment;
the actual billed `usage.cost` would be recorded after the later, post-critic run — which has not
occurred.**

## 10. Run protocol (later session, after a fresh pre-run-critic GO)

1. `stimuli.json` is **already frozen** (hand-authored, no model calls): 30 held-out items (18 temporal
   / 12 distance), 10 count-noun diagnostics, 12 Tier-0 pairs, with counterbalancing.
2. A **fresh independent pre-run critic** (not this design's author) reviews this design + `PREREG.md`
   + `stimuli.json`: freshness (no v3/v4 adjective), agreement-arm fidelity (bare-plural control,
   single-shift indicator), the descriptive-only fencing of the diagnostic, Tier-0 balance, the frozen
   verdict tree, anti-cheat. The orchestrator freezes `PREREG.md` only on **GO**.
3. `probe.py`: all calls via [`experiments/lib/openrouter.py`](../lib/openrouter.py) (`usage: include`);
   refuses to run without `PREREG.md` **and** `analyze.py`; per-slot max_tokens + gemini
   `reasoning:{effort:"minimal"}`; one verbatim retry per unparseable response then missing;
   billed-cost logging; ABORT_USD = $0.25.
4. `analyze.py` computes the agreement shift + bootstrap CI + the frozen verdict tree (with the
   diagnostic kept descriptive-only) and writes `results.json`; an independent post-run verifier
   recomputes every number from raw before any result page is written.
5. Result page (later session, post-run) `wiki/findings/results/aann-agreement-reflex-v5.md`,
   `anchor: internal-contrast-only`, carrying the §7 chief-cost statement verbatim.

## 11. What this design does NOT do / NOT RUN (named null)

- **It has NOT run.** No model calls, no v5 numbers, no result page. The probe may run only after a
  fresh independent pre-run-critic GO on this design + a frozen PREREG + the frozen stimuli.
- **No human-comparison claim** anywhere (anchor `internal-contrast-only`); it cannot, and does not,
  claim a model picks the singular agreement *the way humans do*. No in-repo resource anchors agreement
  behavior; the Mahowald resource is **class provenance only**.
- **The count-noun diagnostic carries no verdict weight** — it is descriptive characterisation of the
  ceiling, fenced out of every verdict branch in code.
- **No new decision, no new operationalization, no threshold retuning** — v5 reuses the ratified
  agreement instrument unchanged; τ, the ceiling threshold, the floors, and the bootstrap seed are
  fixed pre-data in `PREREG-draft.md`.
- **It does not re-open the paraphrase/NLI inferential question** — v5 is *only* the agreement-reflex
  generalization test. The broader inferential verdict stays where v4 left it (PARTIAL); this probe
  asks the narrower, cleaner generalization question the v4 reflex result raised.
