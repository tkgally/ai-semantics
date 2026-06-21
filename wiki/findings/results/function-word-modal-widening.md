---
type: result
id: function-word-modal-widening
title: "The modal NLI null does not generalize: must→might (necessity→possibility) flips at ceiling in all three models, shall→should (deontic obligation→advisory) splits the panel, will→would (future→conditional) replicates the null"
meaning-senses:
  - constructional
  - inferential
  - distributional
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: refines
    target: essay/function-words-not-one-category
  - rel: refines
    target: result/function-word-swap-run-v2
  - rel: depends-on
    target: result/function-word-swap-run-v2
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# The modal NLI null does not generalize — it is a future→conditional fact, not a modal fact

> **A within-model contrast (`anchor: internal-contrast-only`).** It widens the modal arm of the
> function-word-vs-content swap probe to test **essay revision trigger (a)** of
> [`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md): was the
> near-null `will`→`would` modal arm in [`result/function-word-swap-run-v2`](function-word-swap-run-v2.md)
> a fact about **modals in general**, or about the **future→conditional** swap specifically? It
> makes **no human comparison** and needs no human anchor. Run:
> `experiments/runs/2026-06-21-modal-arm-widening/`. The set was frozen + hashed (file sha
> `cccac581…`, canonical `fb605ed9…`) and certified `"ok": true` (max-positive freq-only and
> length-only shortcut-reader asymmetry **0.0**) **before any model output**, under an independent
> fresh-agent pre-run critic (GO, with its own 9001-point shortcut-reader sweep). Analysis
> **reproduced from raw by an independent fresh-agent post-run verifier — every per-arm cell to the
> digit, 0 discrepancies, billed re-summed to $0.279173 with 0 rows missing `usage.cost`**. **Billed:
> $0.2792** (claude $0.1711 / gpt $0.0419 / gemini $0.0661; 3 models × 354 calls, **0 unparsed**).

## The question (essay trigger a)

[`result/function-word-swap-run-v2`](function-word-swap-run-v2.md) found the `will`→`would` modal
arm "essentially null across the panel (claude 0/20, gpt 0/20, gemini 3/20)." The companion essay
read this as "modal flavor is the kind of shift this [3-way NLI] instrument is insensitive to" — but
flagged it a **one-pair observation** and named trigger (a): widen the modal arm; *"if instead some
modal contrast flips strongly, the reading narrows: it was idiosyncratic to `will`→`would`, not
modal flavor as such."* This probe is that test.

## Design (frozen, certified)

Five arms, 118 matched items, same instrument/matching/posture as run-v2 (3-way NLI entailment-flip;
content swap matched to the modal pair within |ΔLg10WF| ≤ 0.10 + signed Δlen, content gap ≥ function
gap so no surface-only reader can manufacture the asymmetry; per item, flip_fn = label changes when
the **function word** is swapped, flip_ct = label changes when a matched **content word** is swapped):

- **Modal sweep:** `will`→`would` (future→conditional, n=20, reused from run-v2; hypothesis "is going
  to {verb}"); `shall`→`should` (deontic obligation→advisory, n=18, NEW; hyp "is required to {verb}");
  `must`→`might` (deontic necessity→epistemic possibility, n=20, NEW; hyp "is required to {verb}").
- **In-run positive controls** (prove the instrument flips on a real inferential change here):
  `some`→`every` (n=28, reused) and `because`→`although` (n=32, reused).

The two NEW arms use an "is required to {verb}" hypothesis: `shall`/`must` ≈ *required* (predicted
base = entailment), `should` (advisory) / `might` (possibility) ≠ *required* (predicted flip).

## Headline: the modal null is specific to `will`→`would`, not modal swaps in general

Per-arm flip_fn (function-swap flip rate) — the primary readout:

| arm | claude | gpt | gemini | base-label agreement (cl/gpt/gem) |
|-----|--------|-----|--------|-----------------------------------|
| `because`→`although` (control) | 1.000 | 0.969 | 1.000 | 1.00 / 0.97 / 1.00 |
| `some`→`every` (control) | 1.000 | 0.929 | 1.000 | (see scalar note) |
| `will`→`would` (future→conditional) | **0.000** | **0.000** | **0.150** | 1.00 / 1.00 / 1.00 |
| `shall`→`should` (deontic strength) | **0.056** | **0.056** | **0.778** | 1.00 / 1.00 / 0.89 |
| `must`→`might` (necessity→possibility) | **1.000** | **1.000** | **1.000** | 1.00 / 1.00 / 1.00 |

Content-swap flip rates (flip_ct) are near-floor everywhere (pooled claude 0.017 / gpt 0.076 /
gemini 0.076; the `some` content control `man`→`girl` is the only one above 0.10, 0.07–0.25). The
falsify arm (content ≥ function) did not fire in any modal arm. **So the result is not a frequency
artifact: a matched content swap leaves the inference alone; the modal swap is what moves it (when
it moves at all).**

The `will`→`would` null **replicates** run-v2 cell-for-cell (claude 0/20, gpt 0/20, gemini 3/20). But
**`must`→`might` flips at ceiling in all three models** (20/20 each), and **`shall`→`should` flips
strongly in gemini** (14/18 ≈ 0.78) though barely in claude/gpt (1/18 ≈ 0.06). The blanket reading
"modal flavor is the kind of shift this instrument is insensitive to" is therefore **false**: the
near-null is a fact about the **future→conditional** swap, not about modal swaps as a class. **Essay
trigger (a) fires in the "narrows" direction.**

## The real finding: NLI registers a modal swap in proportion to how truth-conditionally "loud" it is — partly model-dependent

The three modal arms form a clean gradient by how sharply the swap changes the entailment, and the
base-label agreement (high for every modal arm — the manipulation check the pre-run critic required
be reported per arm) makes each cell interpretable:

1. **Subtle modal-flavor shift — `will`→`would` (future→conditional): NULL in all three.** Base
   agreement 1.00 everywhere: all models read "the council *will* see the visitor → is going to see
   the visitor" as entailment. The `would` swap does **not** disturb it — the models read the
   conditional "would see" as still entailing the plain future. The instrument is blind to the
   irrealis shift, exactly as run-v2 found.
2. **Within-deontic-strength drop — `shall`→`should` (obligation→advisory): SPLITS the panel.** Base
   agreement is **high** (1.00 / 1.00 / 0.89): all models read "the bidder *shall* buy the lot → is
   required to buy the lot" as entailment, so the feared "*shall* read as plain future" collapse did
   **not** happen — the split is interpretable. The *fn* condition divides the panel: **gemini** reads
   "*should* buy → is required to buy" as **no longer entailment** (14/18 ≈ 0.78 flip, almost all to
   neutral — it grades *should* as advisory, weaker than *required*), while **claude and gpt keep it
   entailment** (17/18,
   flip 0.056 — they collapse *should* ≈ *required*). So whether the advisory/obligation distinction
   is inference-relevant is a **genuine model difference**, not a surface artifact. **Read with its
   thinness:** the entire `shall` arm rests on a single content pair (`buy`→`give`), so the split is
   14/18 vs 1/18 *frames* on that one verb pair — a clean but narrow contrast (see Limitations).
3. **Category-crossing necessity→possibility — `must`→`might`: flips at ceiling in all three.** Base
   agreement 1.00 everywhere ("the auditor *must* find the form → is required to find the form" =
   entailment). The `might` swap flips it in 20/20 items for every model. **Caveat (the load-bearing
   one): this arm crosses flavor — deontic *must* → epistemic *might*.** The hypothesis "is required
   to find" is deontic; "*might* find" is epistemic possibility — a **category mismatch**, the easiest
   kind of non-entailment. So the ceiling flip shows modals *can* move this instrument, but it does
   **not** isolate a within-scale "necessity vs possibility" reading the way `shall`→`should` isolates
   a within-scale "obligation vs advisory" reading. The flip's *direction* differs by model: **claude
   sends it to contradiction** (20/20 — it reads "*might* find" as actively contradicting "is required
   to find"), while gpt and gemini mostly send it to neutral (12/20, 14/20 neutral; the rest
   contradiction).

So the instrument's sensitivity to a modal swap is graded — **loud category mismatch (registers in
all) > within-scale deontic strength (registers in one model) > subtle future→conditional irrealis
(registers in none)** — and the boundary between "registers" and "doesn't" is partly about the
truth-conditional loudness of the swap and partly model-dependent.

## What this does to the essay (trigger a): narrows the blanket reading, vindicates the deeper one

[`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md) made two
claims about modals. The **narrow** one — "modal flavor is the kind of shift this instrument is
insensitive to" — is **narrowed to the future→conditional swap**: it is not true of modals in
general. The **deeper** one — its §"A calibrated reading", that "a sizeable part of what looks like
'function words carry more inferential load' is really 'the swaps that flip our *one* inferential
instrument are the ones that change a relation that instrument is calibrated to'" — is **vindicated
and sharpened**: across four modal contrasts (counting run-v2's `will`→`would`) the instrument
registers the swap iff the swap changes a relation 3-way NLI is built to read (a clear non-entailment),
and misses the subtle modal-flavor shift. The essay's **type-specificity thesis survives** (closed-class
items carry inferential load non-uniformly) but its **diagnosis changes** (essay trigger (a), as
written): the low-load case is not "modals" but specifically the future→conditional shift; necessity↔
possibility (across the deontic/epistemic line) registers in all three models, and deontic
obligation↔advisory registers in one.

## Coherence note (secondary): scalar upper-bounding of *some*, echoing the few/many split

The `some`→`every` control was included to prove the instrument is alive (it does: flips 1.00 / 0.93 /
1.00). Its *base* label is a free side-observation: the predicted base "Some X → All X = neutral" is
**not** what claude and gemini assign — claude reads it as **contradiction** (27/28), gemini mostly
contradiction (17/28), gpt is mixed (15 contradiction / 13 neutral). That is **scalar
upper-bounding** ("some" → "not all" → contradicts "all"), the same shape
[`result/function-word-few-many-split`](function-word-few-many-split.md) found for *many* in claude —
and here it appears for *some* in claude **and** gemini. (Note gemini upper-bounds *some* here but
relaxed *many* in the few/many split, so the upper-bounding is item/scalar-specific, not a global
model setting.) This is a coherence echo, not a load-bearing claim: the `some` arm's *purpose* is the
flip-rate control, which is unaffected (the swap flips regardless of the base label).

## What this establishes / does not

- **Establishes (within-model):** the run-v2 `will`→`would` modal null replicates, but does **not**
  generalize — `must`→`might` flips a 3-way NLI judgment at ceiling in all three models and
  `shall`→`should` flips it in one (gemini), with the matched content control near-floor throughout.
  Whether a modal swap shifts the inference tracks how clear a (non-)entailment it creates, and is
  partly model-dependent (the `shall`→`should` split). Base-label agreement is high for every modal
  arm, so the nulls and the split are interpretable, not measurement failures.
- **Does not establish:** any human comparison (`internal-contrast-only`; a BLiMP/NLI human baseline
  remains the optional, not-in-repo Posture-2 upgrade — so this result does **not** say which reading
  of *should*, or of the modal contrasts, is normatively correct). It does **not** isolate a pure
  necessity-vs-possibility strength reading (the `must`→`might` ceiling flip is confounded by the
  deontic→epistemic flavor cross). It is one instrument (3-way NLI) at temperature 0.

## Limitations (honest — the pre-run critic's required disclosures)

- **`must`→`might` flavor cross.** The ceiling flip is the loudest but least clean arm: it crosses
  deontic→epistemic, so it is a strength contrast *with* a flavor cross, not a pure-strength
  manipulation (see point 3 above). Read it as "modals are not blanket-invisible," not as "models
  read necessity-vs-possibility strength."
- **`shall` single content pair.** All 18 `shall` items rest on **one** content pair (`buy`→`give`) —
  the |ΔLg10WF| gap-0.759 supply ceiling under faithful matching admits essentially one clean
  transitive pair (`matching-report.json` `single_out_word_classes`); `must` carries three
  (`find`/`call`→`leave`, `put`→`move`), `will` two. The `shall` *flip_ct* is 0.000–0.111, so the
  single pair is not manufacturing the split, but the arm is thin.
- **`shall` modal-reading.** The `shall`→`should` reading depends on a deontic (legal) reading of
  `shall`; base agreement confirms the models took it that way (1.00 / 1.00 / 0.89), so this risk did
  not bite — but it is a register-bound arm.
- **Single corpus norm / single instrument / temperature 0.** Frequency is SUBTLEX-US `Lg10WF` only;
  the indicator is one NLI instrument. The strong effects (must arm, controls) far exceed any
  plausible temp-0 jitter; the `shall` claude/gpt 1/18 and gemini 14/18 are concentrated, not
  borderline. Per-arm n is 18–32 (the per-arm power gate replaces the conjecture's ≥200 bar — this is
  a per-arm characterization, not a conjecture re-test; no new operationalization decision was owed,
  confirmed by the pre-run critic).
