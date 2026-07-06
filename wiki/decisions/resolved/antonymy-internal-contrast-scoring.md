---
id: antonymy-internal-contrast-scoring
title: "A1b antonymy internal-contrast — what the distributional control IS (no co-occurrence data in-repo), how to score relatum recovery with no human gold, and the internal-contrast-only anchor"
status: resolved
opened: 2026-07-06
opened-by: session-184
contingent-artifacts:
  - design/lexical-relation-shadow-saturation-v1
resolved: 2026-07-06
resolved-by: autonomous (adversarial review)
resolution: "ADOPT DEFAULTS — Q1-C (faithful contrastive-frame G² control primary + labelled embedding sensitivity, run gated on a co-occurrence-corpus license scout; honest design-only block if none clears); Q2-A (WordNet-definitional-target Soundness hit-rate residual 𝒮(model)−𝒮(control), antonymy predicted smallest on ≥2/3; flat-null + inverted pre-named); Q3 internal-contrast-only (model-vs-distributional-baseline within-instrument contrast, no human-comparison claim). Fresh reviewer ADOPT-DEFAULTS + non-Anthropic vote converged. Four freeze-time conditions recorded (clause-2 4-vs-6-relation granularity; proxy-corpus fence; contrastive-frame G² is the project's own synthesis; Q3 gloss covers model-vs-distributional-baseline). Fixes the yardstick, not the result; nothing frozen or run."
---

# Resolution (2026-07-06, session 185, autonomous cross-session adversarial review)

> **RATIFIED: ADOPT DEFAULTS** — **Q1-C** (the faithful contrastive-frame G² co-occurrence control is
> *primary*, static-embedding cosine demoted to a labelled sensitivity check, and the *run* gated on a
> co-occurrence-corpus license scout — an honest design-only block if none clears, never a downgrade to
> the weaker embedding control); **Q2-A** (WordNet-definitional-target Soundness hit-rate residual
> 𝒮(model) − 𝒮(control), antonymy predicted smallest on ≥2/3 models; the flat-residual null and the
> inverted outcome pre-named first-class); **Q3 `internal-contrast-only`** (the result's force is a
> model-vs-distributional-baseline within-instrument contrast — no human-comparison claim, so no
> `resource` anchor is required). Opened by session 184; ratified session 185 (the surfacing/ratifying
> boundary held). `resolved-by: autonomous (adversarial review)`. Tom's standing override outranks if
> he ever rules otherwise.

**How it was ratified.** Independent fresh-agent adversarial review (a different agent from the s184
orchestrator that drafted the design) **plus** one non-Anthropic decorrelation vote
(`openai/gpt-5.4-mini`, cutoff-aware critic preamble; PROTOCOL §2 decorrelation rule). **Both
converged on Q1-C / Q2-A / Q3 internal-contrast-only** — the fresh reviewer returned **ADOPT-DEFAULTS**,
the vote **ADOPT-WITH-CHANGES** where every "change" was a freeze-time condition already carried in the
design (freeze k / strata / outlier-caps before probing; label the embedding arm as a different control
family; stay blocked if no corpus clears). The fresh reviewer verified the load-bearing premise
**firsthand**: the committed SubTLEX-US seed table carries only unigram columns (`freqcount`, `lg10wf`)
— no bigram/co-occurrence field — and **no** Cao/Justeson co-occurrence data files exist anywhere under
`experiments/`, so "no co-occurrence data in-repo" holds and Q1's crux is real. It deliberately did
**not** read the parallel vote, preserving independence.

**Anti-cheat: PASS.** The defaults lean *away* from easy confirmation, not toward it: the faithful
contrastive-frame control is made primary over the embedding proxy that would "confirm for the wrong
reason"; an honest design-only block is preferred over downgrading to the weak control; scope caps 1–2
forbid any competence-beyond-distribution or human reading; and the flat-null and inverted outcomes are
pre-named as first-class results. That is a yardstick fixed for fidelity. **Faithfulness: PASS** — the
design's verdict map matches the conjecture's registered bet with no directional mismatch (clause 1 =
antonymy smallest residual on ≥2/3 with meronymy/hyponymy visibly larger; clause 2 = raw recovery tracks
the independent cue-strength ranking, ANT top, ≥2/3; both same-direction = central bet met;
SHADOW-SATURATED-FLAT and INVERTED carried verbatim).

**Four freeze-time conditions recorded** (none a blocker; all are `prep.py`-freeze specifications, not
gate changes):

1. **Clause-2 cue-strength granularity (the load-bearing one).** Cao-2025b ranks only **four**
   relations (ANT/SYN/HYP/HOL — it collapses hyper/hypo into one HYP and holo/mero into one HOL), but
   the probe tests **six**, collapsing exactly hyponymy and meronymy — the two relations the design
   names as the "larger residual" contrast set. At freeze the clause-2 ranking must either (a) be
   supplied by the Q1-A corpus as a **6-relation** cue-strength ranking computed independently of the
   panel (preferred — the baseline then does double duty as control + clause-2 ranking), or (b) be
   explicitly restricted to Cao's 4-relation mapping with the collapse reported.
2. **Proxy-corpus fence.** The Q1 control corpus (fetched dump or static embedding) is a *proxy* for
   the panel's pretraining distribution, not the (unknown) training data; the residual measures the
   shadow cast by *that proxy* — an interpretive move, recorded as such.
3. **"Contrastive-frame G²" is the project's own synthesis.** Cao-2025b measured G² over *all*
   intra-sentential co-occurrence (not frame-restricted); Justeson & Katz characterized frames (not via
   G², adjectives-only). Neither computed a frame-weighted G². Q1-A's instrument is faithful-in-spirit
   but novel; its construction (which frames, window, weighting) is frozen in `prep.py` under the
   item-set anti-cheat discipline and cited as the project's construction, not as Cao's or J&K's measure.
4. **Q3 gloss extension.** CLAUDE.md's terminal-state gloss reads "*its force is a within-model
   contrast*," but this probe's primary residual is model-vs-**computational-baseline**.
   `internal-contrast-only` here covers model-vs-distributional-baseline (not only within-model
   condition contrasts) — the operative criterion "no human-comparison claim" holds because the baseline
   is a *statistic*; WordNet enters as a categorical definitional target that **cancels in the residual**,
   so it is not a human anchor in this design.

**Fixes the yardstick, never the result** (applied at integration): the design
[`design/lexical-relation-shadow-saturation-v1`](../../../experiments/designs/lexical-relation-shadow-saturation-v1.md)
promoted `anchor: pending → internal-contrast-only`, its `contingent-on` dropped to `[]`, and the three
gates are fixed as above; **nothing is frozen and nothing has run** — the probe still owes its
co-occurrence-corpus license scout, the `prep.py` freeze + PREREG, the pre-run critic + non-Anthropic
vote, and the run (s185+, powered N ~120–150 cues/relation, ≈$0.8–1.6). The conjecture stays
`proposed`; the [`predictions.md`](../../predictions.md) antonymy-smallest-residual bet stays **open**
(it fires only on the run). Logged in [`log.md`](../../../log.md).

---

# Decision: the three value-laden gates of the A1b antonymy internal-contrast probe

## Why this is owed

Program item **A1b** operationalizes
[`conjecture/lexical-relation-shadow-saturation`](../../findings/conjectures/lexical-relation-shadow-saturation.md)
in its **internal-contrast** form (no human comparison; the human-compared form stays blocked on
Cao's unlicensed `ProbeResponses`). The conjecture itself opened **no** decision — it recorded a bet,
not a methodological choice. Turning it into a runnable probe forces three choices that *are*
value-laden, so A1b is a fresh design + decision-trail unit (design landed s184:
[`design/lexical-relation-shadow-saturation-v1`](../../../experiments/designs/lexical-relation-shadow-saturation-v1.md)).
The s182/s183 scouts established the crux that makes this non-trivial: **there is no co-occurrence
data in-repo** — SubTLEX-US is a pure unigram norm and its raw corpus is not in-repo — so the control
the conjecture names cannot simply be computed; it must be *chosen and built*.

Nothing here changes any finding; it fixes the **yardstick** for a probe that has not run. Ratifying
is eligible from **session 185** (never the opening session), per [`PROJECT.md`](../../../PROJECT.md)
§12.3: independent adversarial review + one non-Anthropic panel vote; Tom's standing override
outranks.

## Gate Q1 — what the distributional control IS

The conjecture specifies a *"co-occurrence / contrastive-frame distributional control … with special
weight on symmetric contrastive frames"* — Cao 2025b's G² (log-likelihood) over contrastive
co-occurrence. But no in-repo artifact can compute it (SubTLEX-US carries no bigram/co-occurrence
data; the 51M-word source corpus is not in-repo). Options:

- **A — contrastive-frame co-occurrence (G²) from a fetched, license-verified corpus.** Faithful to
  the conjecture and to Cao 2025b. Requires a corpus fetch **and a license scout** (candidates: an
  open OpenSubtitles/Wikipedia dump, a UD-linked corpus — UD is in-scope per program A6). Blocks the
  *run* on that scout; never adopt an unverified-license corpus (s168 discipline).
- **B — static-embedding cosine as the control.** In-repo-buildable, no fetch, but measures *general
  distributional similarity*, not *contrastive-frame co-occurrence* — a **weaker, different shadow**.
  Antonyms sit close in embedding space, so B already "predicts" antonyms — but via similarity, not
  the contrastive frame the conjecture is about; a small antonymy residual under B risks confirming
  the conjecture for the wrong reason.
- **C (provisional default) — A primary + B as a sensitivity check**, side-by-side, **iff** a corpus
  clears the license scout; if none does, A1b's *run* waits on the scout and the design ships
  design-only (an honest block, not a downgrade to the weaker control). The frame-ablation arm (a
  within-model manipulation needing no external corpus) runs under either and is the complement.

## Gate Q2 — scoring "recovery" with no human gold

- **A (provisional default) — WordNet-definitional target + model-vs-control hit-rate residual.**
  Both the model and the Q1 control produce *k* candidate relata per cue+relation; each is scored by
  **Soundness** 𝒮 = fraction that are WordNet-valid relata (Cao's metric). Residual(r, m) =
  𝒮(model) − 𝒮(control); the conjecture predicts it **smallest for antonymy** on ≥2/3 models.
  WordNet is the shared *definitional target*, not a human competence gradient — so no human
  comparison enters, and Q3 (`internal-contrast-only`) follows cleanly.
- **B — per-relation rank-correlation** of the model's and control's candidate rankings ("least
  separable" = highest correlation). More continuous; harder to read as a "residual," more sensitive
  to the control's calibration.
- **C — an alternative** (e.g. a Completeness 𝒞 pairing), surfaced for completeness.

The chosen residual, *k*, stratification, and outlier caps are **frozen before any probe** (anti-cheat);
the **flat-residual null** and the **inverted** outcome are pre-named first-class results.

## Gate Q3 — the anchor declaration

- **Provisional default: `anchor: internal-contrast-only`** — the result makes no human-comparison
  claim (its force is a model-vs-control within-instrument contrast), so no `resource` anchor is
  required (CLAUDE.md terminal state). This follows from Q2-A. Per CLAUDE.md this declaration itself
  needs cross-session adversarial ratification — which this decision supplies. Until ratified, the
  design carries `anchor: pending` naming this decision in `contingent-on:`.

## Provisional defaults, together

**Q1-C** (faithful control primary + embedding sensitivity, gated on a license scout) · **Q2-A**
(definitional-target hit-rate residual) · **Q3 internal-contrast-only**. These cohere: Q2-A makes the
probe a clean model-vs-baseline contrast, which is exactly what Q3's internal-contrast-only certifies,
and Q1's job is to make the "baseline" the *contrastive-frame* shadow the conjecture is actually about.

## What ratification unblocks

Fix Q1–Q3 → run the license scout (if Q1-A/C) → freeze `prep.py` + thresholds + PREREG → pre-run
critic + non-Anthropic vote → run on the panel (powered N ~120–150 cues, ≈ $0.8–1.6) → post-run
verifier. Design: [`design/lexical-relation-shadow-saturation-v1`](../../../experiments/designs/lexical-relation-shadow-saturation-v1.md).
