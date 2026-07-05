---
type: result
id: argument-structure-coercion-v2
title: Off-ceiling coercion v2 — the v1 add-direction ceilings survive a conflicting cue (all three models withhold the construction's added inference when an explicit clause denies it), so they are cue-sensitive, not a brittle template
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-29
updated: 2026-07-05
links:
  - rel: supports
    target: conjecture/caused-motion-construction
  - rel: supports
    target: conjecture/way-construction
  - rel: refines
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: refines
    target: result/way-construction-traversal-v1
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/constructional-meaning
---

# Result: argument-structure coercion probe v2 (off-ceiling)

The first **off-ceiling** test of the project's two add-direction Tier-4 positives — [`result/caused-motion-minimal-pair-divergence-v1`](caused-motion-minimal-pair-divergence-v1.md) and [`result/way-construction-traversal-v1`](way-construction-traversal-v1.md), both of which were **ceiling on relatively easy controls** (their shared lead caveat). Design + frozen stimuli: [`design/argument-structure-coercion-v2`](../../../experiments/designs/argument-structure-coercion-v2.md); governing operationalization (ratified): [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md); run record: [`experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/`](../../../experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/README.md).

It was built to separate two hypotheses the v1 ceilings could not:
- **H-deep** — the model *computes* the construction's added inference and would **withhold** it when a resolving cue blocks it;
- **H-default** — the model *defaults* to "yes" on a well-formed coercion (a learned "this frame → yes" template a conflicting cue cannot override).

**One-line finding:** the v1 ceilings are **cue-sensitive, not a brittle template** — strong evidence for H-deep over H-default. In the key arm (the `canonical` vs `cue` minimal pair, same construction + verb, with an explicit clause denying the inference), **all three models drop to floor on the cue items — affirm 0–20%, a 60–100 pp drop from canonical — in 3/3 models, both instruments, both constructions.** So the near-ceiling v1 affirm rates do not survive an explicit denial: the models respect the cue. **Calibration:** the cue here is an *explicit verbal denial* ("…but the napkin never moved") — the **easier end** of "conflicting cue"; a subtler world-knowledge-immovability cue (the design's bolted-down-object variant) was **not** run and is the natural v2b.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C), as subjects. Both instruments (NLI 0/1/2 + forced-choice YES/NO/CANT_TELL); temperature 0; behavioral, **no logprobs** (so it runs on the standard 3-family behavioral panel, unlike AANN). **0 NA across all 360 calls.**
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `280beeb3d9aff093`): 60 items — 10 caused-motion stems + 10 way stems × 3 conditions:
  - `canonical` (difficulty 1): the v1-style well-formed coercion (*Maria sneezed the napkin off the table* / *Mia whistled her way down the hall*). Affirm-inference gold YES — the ceiling anchor.
  - `resist` (difficulty 2): a coercion-resisting verb in the same frame (cognition/stative for caused-motion: *Maria knew the napkin off the table*; self-motion-precluding for way: *Mia slept her way down the hall*).
  - `cue` (difficulty 3, **the discriminator**): the same construction + verb as `canonical`, plus an explicit clause **denying** the inference (*…but the napkin never moved* / *…but she never left the doorway*).
- Indicator = **affirm-construction-inference rate** (FC YES, or NLI entailment) on the per-item hypothesis. **Cost** (actual): **$0.093** (A $0.055 / B $0.003 / C $0.035).

## Results

Affirm-construction-inference rate (%). Key discriminator = the **cue** column (low = cue-respecting / H-deep; high = template / H-default) and the **canonical→cue drop**.

| model | constr. | instr. | canonical | resist | **cue** | **drop** |
|---|---|---|---:|---:|---:|---:|
| claude-sonnet-4.6 | caused-motion | NLI | 100% | 40% | **0%** | 100 |
| claude-sonnet-4.6 | caused-motion | FC | 100% | 30% | **0%** | 100 |
| claude-sonnet-4.6 | way | NLI | 100% | 100% | **0%** | 100 |
| claude-sonnet-4.6 | way | FC | 100% | 100% | **10%** | 90 |
| gpt-5.4-mini | caused-motion | NLI | 80% | 0% | **0%** | 80 |
| gpt-5.4-mini | caused-motion | FC | 80% | 0% | **10%** | 70 |
| gpt-5.4-mini | way | NLI | 70% | 80% | **0%** | 70 |
| gpt-5.4-mini | way | FC | 80% | 70% | **20%** | 60 |
| gemini-3.5-flash | caused-motion | NLI | 100% | 70% | **0%** | 100 |
| gemini-3.5-flash | caused-motion | FC | 100% | 20% | **0%** | 100 |
| gemini-3.5-flash | way | NLI | 100% | 100% | **20%** | 80 |
| gemini-3.5-flash | way | FC | 100% | 100% | **20%** | 80 |

- **cue at floor everywhere (0–20%), 3/3 models, both instruments, both constructions; drop 60–100 pp.** This is the result: the construction's added inference is **withheld** once an explicit clause denies it. By the ratified reading rule (cue ≥70% in ≥2/3 = robustly template/H-default), the template reading is supported in **0/3** models on every cell — the opposite of H-default.
- **`canonical` replicates v1** (claude/gemini ceiling; gpt 70–80%, its usual conservative profile), confirming the ceiling anchor is present in this item set before the cue knocks it out.
- **Degradation is mostly monotone** (canonical ≥ resist ≥ cue in 9/12 cells) — the graceful-degradation shape, not a brittle flat-then-cliff. The 3 non-monotone cells are all driven by the way-`resist` arm scoring *high* (below).

### The `resist` arm exposes a construction asymmetry (not a failure)

- **Caused-motion `resist` is mostly withheld** (0–70%; claude 30–40%, gpt 0%, gemini 20–70%): with a cognition/stative verb (*knew/believed/understood the napkin off the table*), the models largely decline to attribute caused-motion — correct anomaly detection, since knowing cannot cause physical motion.
- **Way `resist` is *affirmed* (70–100%, 3/3 models):** *slept/fainted/dozed her way down the hall* is still read as traversal. This is **defensible, not a competence failure**: the way-construction contributes path-traversal *independent of the verb* (Goldberg's point — the construction, not the verb, carries the motion), so "slept her way down the hall" still entails the subject ended up down the hall; only the *manner* (sleeping) is anomalous. The contrast with caused-motion is principled: caused-motion's causal attribution legitimately *depends* on a motion-capable verb (so a cognition verb blocks it), whereas way-traversal does not. The honest read: the way-template is **more automatic** — it fires on an anomalous verb where caused-motion's does not — but this is the construction working as described, and crucially it is **still cancelled by the explicit cue** (way `cue` = 0–20%).

## Interpretation (modest)

1. **The v1 add-direction ceilings are cue-sensitive computation, not a brittle template.** The single most important caveat on the CC, caused-motion, and way v1 positives was "ceiling on easy controls = weak evidence for deep processing." This off-ceiling probe directly stresses that: when an explicit clause denies the construction's added inference, every model withholds it (cue 0–20%, drop 60–100 pp). A pure "this-frame→yes" template would have ignored the denial; the panel does not. This **upgrades** the modest reading of the v1 positives — they survive a conflicting cue.
2. **It does not show "deep semantics," only cue-respect at the explicit end.** The cue is a direct verbal contradiction, the easiest kind to register. The result rules out the strongest deflationary reading (template/H-default) but does *not* establish robust world-knowledge reasoning; a subtler implicit cue (world-knowledge immovability; the design's bolted-down-object variant, unrun) is where a model could still fail, and is the natural v2b.
3. **A construction-level asymmetry in automaticity:** the way-construction coerces its inference even on a semantically resisting verb, where caused-motion's verb-dependent causal attribution does not — consistent with the way-construction being the more schema-driven of the two. Both, however, remain cancellable by the explicit cue.

This sits on the theory ladder as the first **off-ceiling** datum for the add-direction constructions: it does not move them off Tier 4, but it removes the "ceiling artifact" worry for the explicit-cue case.

## What this licenses / does not license

**Licenses:** a project-owned statement that the v1 caused-motion and way add-direction ceilings are **cue-sensitive** — all three models withhold the construction's added inference under an explicit denial (0–20% affirm, 60–100 pp drop) — so those ceilings are not a brittle template default for the explicit-cue case. Refines the v1 results' lead caveat.

**Does NOT license:**
- **"Models robustly reason about world knowledge against the construction."** Only an *explicit verbal* denial was tested. Subtler/implicit conflicting cues are unrun (v2b).
- **A resolution of the add/cancel asymmetry.** This is an add-direction probe only; the matched off-ceiling *cancel*-direction (harder conative) the design calls for was not run, so "add easier than cancel" remains confounded with ceiling/difficulty (still future work).
- **A human-level claim.** Internal-contrast-only by ratified design (the Scivetti subsets have no conflicting-cue items; the "correct" reading of an anti-cued coercion is itself contestable for humans). `anchor: internal-contrast-only`; no human baseline asserted or invented.
- **A model-internal or grounding claim.** Behavioral only.

## Limits

- **Explicit-cue only** — the lead caveat now; the cue is a direct contradiction, the easy end of "conflicting cue."
- **N = 10 stems/construction, single run/date, both instruments.** Cross-model + cross-instrument convergence is the robustness signal (and it is strong here: cue floor is unanimous).
- **The cue sentences are internally tensioned by design** ("sneezed the napkin off the table, but it never moved"); the floor affirm rate means the models resolve that tension toward the explicit final-state denial rather than the construction — which is the intended discriminator, but note these are not naturalistic sentences.
- **way `resist` verb "slept" carries mild idiom contamination** ("slept one's way to the top"); "fainted"/"dozed" do not. The way-`resist` affirmation is reported as descriptive, not as a pass/fail (ratified report-the-rate).
- **Near-miss + multi-step arms deferred to v2b** (this run = conflicting-cue + coercion-resisting + graded ladder); v1 already established the construction-floor controls (all passed).
- **Adversarial pre-run pass was an orchestrator self-review**, not an independent subagent: the subagent failed three times on transient API 529 (server overload). A noted reduction in independence; the self-review found no stimulus blockers and is recorded in the run README.
- **Shared priors (charter §2.5):** three decoders are not three independent witnesses.

## Provenance

- Design: [`design/argument-structure-coercion-v2`](../../../experiments/designs/argument-structure-coercion-v2.md). Operationalization (ratified): [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md) (UNIFY + adopt default). Refines: [`result/caused-motion-minimal-pair-divergence-v1`](caused-motion-minimal-pair-divergence-v1.md), [`result/way-construction-traversal-v1`](way-construction-traversal-v1.md).
- Run record + code + full (own-stimuli) outputs + cost: [`experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/`](../../../experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/README.md). Every number reproducible from the committed `raw/results.json`.

## Status

`status: proposed`, `anchor: internal-contrast-only` (ratified 2026-05-31, conflicting-cue-human-anchor). Numbers reproducible from committed code + `raw/results.json`. `contingent-on: []`. Promotion past `proposed` awaits Tom's review. *(Governance note, s183: this sentence predates the autonomous-era amendment — since 2026-06-12, promotion runs by autonomous cross-session adversarial review, [`PROJECT.md`](../../../PROJECT.md) §12.3; Tom holds a standing override.)* The standing next step is v2b: a subtler (world-knowledge / implicit) conflicting cue, plus the matched cancel-direction probe to de-confound the add/cancel asymmetry.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** Both named next steps ran: the
> implicit-cue v2b landed as [`result/coercion-implicit-cue-v2b`](coercion-implicit-cue-v2b.md)
> (bounding H-deep to "explicit-outcome parsing" — the subtler cue is where the H-deep reading
> thins), and the matched cancel-direction companion as
> [`result/conative-cancel-direction-v2`](conative-cancel-direction-v2.md). The "unrun / still
> future work" phrasings above are therefore historical. *(Back-annotation: this page's numbers
> and verdict stand unchanged.)*
