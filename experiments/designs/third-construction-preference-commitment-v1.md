---
type: design
id: third-construction-preference-commitment-v1
title: third-construction preference/commitment v1 — does the AANN forced-choice-vs-NLI "preference without commitment" dissociation reach a SECOND, add-direction divergent-default construction (caused-motion, headroom-engineered)?
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: frozen-not-run
anchor: pending
contingent-on: []
created: 2026-06-15
updated: 2026-06-15
links:
  - rel: operationalizes
    target: conjecture/preference-commitment-generality
  - rel: depends-on
    target: result/aann-inferential-v6
  - rel: depends-on
    target: result/aann-inferential-v4
  - rel: depends-on
    target: result/conative-preference-commitment-v1
  - rel: depends-on
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/caused-motion-near-miss-v2c
  - rel: depends-on
    target: result/argument-structure-coercion-v2
  - rel: depends-on
    target: result/coercion-implicit-cue-v2b
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Experiment design v1 — third-construction (caused-motion) preference/commitment double contrast

> **Status: FROZEN-but-NOT-RUN.** This design implements **Option A** of the ratified decision
> [`decisions/resolved/aann-uniqueness-third-construction`](../../wiki/decisions/resolved/aann-uniqueness-third-construction.md)
> (ADOPT DEFAULT — engineer headroom on an add-direction CxNLI construction, then run the
> double-contrast preference/commitment instrument; Option C the binding fallback). It inherits the
> ratified double-contrast discipline of
> [`decisions/resolved/aann-inferential-default-coincidence`](../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)
> verbatim (headroom precondition + mandatory within-design lexical-cue control arm). It operationalizes
> [`conjecture/preference-commitment-generality`](../../wiki/findings/conjectures/preference-commitment-generality.md).
> **It is NOT yet critic-reviewed and NOT yet run.** No probe call may be made until an *independent*
> pre-run critic in a **later** session renders GO; if the headroom gate (§5) cannot be cleared at critic
> time, the design **must not run** and routes to Option C ("AANN-specific so far" recorded as the
> disciplined terminal close). No budget is spent by creating this page.

## 0. Scope carry-forward (binding — read first)

This is the **second** alternative construction to carry the preference/commitment instrument, after the
conative ([`result/conative-preference-commitment-v1`](../../wiki/findings/results/conative-preference-commitment-v1.md),
VERDICT INCONCLUSIVE — the AANN shape did not reproduce). Per **Carry-forward 1** of the ratified
decision:

- This tests the forced-choice-paraphrase-vs-NLI-entailment **instrument-divergence** question on an
  **add-direction** divergent-default construction (caused-motion: the construction *adds* a
  causation-of-motion entailment a non-motion verb does not lexically license).
- A clean outcome — whichever way it falls — does **NOT** settle the **cancel-direction / unification
  *shape*** question that the AANN's own semantics raise. That question stays **open** (the Option-B
  route, with its unresolved fresh-anchor sub-question, stays in reserve for a future session). The
  planned result page must restate this scope limit in its lead caveat: *"this is a fair but narrower
  point in construction-space — add-direction instrument-divergence — not the AANN unification shape."*
- One add-direction construction (even a clean confirmation) licenses at most "the FC-vs-NLI
  dissociation reproduces on a *second*, add-direction divergent-default construction," never a
  quantified claim about divergent-default constructions as a class.

## 1. The question

The AANN inferential probe produced the project's sharpest cross-instrument dissociation, replicated
cell-for-cell across two disjoint item sets
([`result/aann-inferential-v6`](../../wiki/findings/results/aann-inferential-v6.md),
[`result/aann-inferential-v4`](../../wiki/findings/results/aann-inferential-v4.md)): a forced-choice
**paraphrase preference** shifts toward the licensed reading in **all three** panel models, but the NLI
**entailment commitment** carries over in **only one** (gpt-5.4-mini). The forward bet
([`conjecture/preference-commitment-generality`](../../wiki/findings/conjectures/preference-commitment-generality.md))
is that this **preference-without-commitment** dissociation is a *general* property of constructions
whose licensed inference diverges from their distributional default — not an AANN artifact. The conative
(the only off-ceiling in-repo divergent-default candidate, a cancel-direction construction) did **not**
reproduce it. This design carries the instrument to a **second** divergent-default construction in the
opposite (add) direction.

## 2. The construction and the hard problem (why caused-motion, and why headroom is genuinely hard)

**Chosen construction: caused-motion** (*Maria sneezed the napkin off the table* → her sneezing caused
the napkin to move, although *sneeze* is intransitive and denotes no motion; Goldberg 1995, ch. 7). The
divergent-default property is present: the construction *adds* a causation-of-motion entailment that the
verb's lexical semantics do not supply.

**The hard problem, stated honestly and with the prior numbers verbatim.** The construction reads at
**ceiling on clean items**, which leaves *no headroom* for a double contrast. The in-repo evidence:

- On clean inanimate-propulsion scenes the caused-motion **construction** arm affirms the
  causation-of-motion entailment at **100%** in all three models, both instruments — the v2c near-miss
  result reports *"the construction is affirmed at 100% everywhere"* and
  *"All 8 scenes are clean inanimate-propulsion"*
  ([`result/caused-motion-near-miss-v2c`](../../wiki/findings/results/caused-motion-near-miss-v2c.md)).
- The v1 minimal-pair probe affirms the caused-motion entailment onto non-motion verbs at **90–100%**
  (claude 100/100, gpt 90/90, gemini 100/100 across NLI/FC)
  ([`result/caused-motion-minimal-pair-divergence-v1`](../../wiki/findings/results/caused-motion-minimal-pair-divergence-v1.md)).

So a double contrast built on the *clean* construction has the same "the default eats the construction"
problem the AANN v3 null exposed. **Headroom must come from genuinely construction-MARGINAL items.**

**Why caused-motion has a credible headroom lever where *way* does not.** The key in-repo datum is the
v2 `resist` arm
([`result/argument-structure-coercion-v2`](../../wiki/findings/results/argument-structure-coercion-v2.md)):
with a **coercion-resisting cognition/stative verb** in the caused-motion frame
(*Maria knew the napkin off the table*), the construction's affirm rate **drops off ceiling and is
largely withheld** — verbatim from that result: caused-motion `resist` *"is mostly withheld (0–70%;
claude 30–40%, gpt 0%, gemini 20–70%)"*. By contrast, the **way** `resist` arm
(*slept her way down the hall*) *"is affirmed (70–100%, 3/3 models)"* — because, in that result's words,
*"the way-construction contributes path-traversal independent of the verb … so 'slept her way down the
hall' still entails the subject ended up down the hall."* That is the decisive asymmetry: caused-motion's
causal attribution **legitimately depends on a motion-capable verb**, so a cognition/stative or otherwise
motion-resisting verb genuinely depresses the construction's baseline; the way-construction coerces
traversal *regardless* of the verb, so its baseline cannot be depressed the same way. **Caused-motion is
therefore the add-direction construction with a real lever to clear the ≤ 0.50 hard ceiling on baseline
construction-affirm rate.**

**Honest statement of residual risk (decision-relevant for the critic / Option C).** Even the v2 `resist`
arm is *uneven*: gemini affirmed it 20–70%, claude 30–40%, and these are NLI/FC-dependent. So a
caused-motion baseline `harvest` is not *guaranteed* to land every model below 0.50 — it is the most
credible add-direction lever in the repo, not a sure thing. **If the harvest arm cannot pin the baseline
construction-affirm rate at ≤ 0.50 for ≥ 2 of 3 models, this design fails the headroom gate (§5) and
routes to Option C.** This possibility is real and is exactly what the headroom gate exists to catch
*before* any spend. (See §11 for the candid assessment.)

## 3. The item construction strategy (the headroom-engineering target)

Headroom is engineered by holding the **caused-motion construction form** constant and choosing
**construction-marginal verbs** whose semantics resist the causal-motion attribution — so the
construction's added entailment is *contestable rather than automatic*, giving the FC and NLI instruments
room to diverge.

Two complementary marginality dimensions, both motivated by the v2/v2b prior art (each framed as a
**design hypothesis to be verified by the harvest arm**, not an established measured fact):

- **(M1) Coercion-resisting verbs** — cognition / perception / stative / low-propulsion verbs in the
  caused-motion frame (e.g. *knew*, *believed*, *understood*, *noticed*, *remembered*, *doubted* the
  object into displacement). **Design hypothesis:** these depress the construction's causal-motion
  affirm rate, per the v2 `resist` numbers above. These do **not** assert a verb is "rare" or "low
  frequency" as fact — they are selected by the *semantic property* (the verb denotes no force/contact
  that could displace an object), and the harvest arm measures the resulting affirm rate empirically.
- **(M2) Low-propulsion / motion-marginal physical verbs** — physical verbs whose force is too weak or
  diffuse to make the displacement reading automatic (e.g. *blinked*, *hummed*, *grinned*, *winked* the
  object off the surface), where the caused-motion reading is *available but marginal*. **Design
  hypothesis:** these sit between the clean-propulsion ceiling (sneeze/blow) and the cognition floor,
  widening the off-ceiling band where preference and commitment can dissociate.

**The freeze rule (so the design can be frozen without enumerating every final stimulus).** The
`harvest`/baseline arm (run first, §5) measures the per-model construction-affirm rate for a candidate
pool of **≥ 24 marginal verbs** (≈12 M1 + ≈12 M2) in the fixed caused-motion frame against a fixed light
inanimate object set (napkin, crumb, feather, wrapper, petal, confetti — inherited from the v2c
clean-propulsion object inventory). The **headline item set is then frozen as the subset of marginal
verbs whose pooled baseline construction-affirm rate is ≤ 0.50 per model** (target ≤ 0.30), with a
minimum of **10 verbs** retained or the design fails the gate. The candidate pool, the object set, the
frame template, and the selection rule are all frozen in `prep.py` **before** the harvest arm runs;
only the *post-harvest subset selection* is data-driven, and it is a pre-registered rule, not post-hoc
tuning. (Verbatim concrete example items appear in §4.)

## 4. Conditions (the four item families; verb + object held constant within a stem)

Hypothesis / causal proposition held identical across all four forms within each stem:
**H = "&lt;subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move."** (the v1/v2c hypothesis verbatim).

| family | example | role | causal default |
|---|---|---|---|
| `clean` (clean-propulsion verbs) | Maria sneezed the napkin off the table. | **headroom anchor / ceiling reference** — the v1/v2c clean construction; must read ≈ceiling | ENTAILED (the construction's automatic add) |
| `marginal` (target) | Maria blinked the feather off the table. | **the construction, off-ceiling** — caused-motion on a motion-marginal/resisting verb | LICENSED-BUT-CONTESTABLE (the headroom band) |
| `cue-control` / **LCC** (near-miss frame, same verb + end-state, construction REMOVED) | Maria blinked, and the feather ended up off the table. | **lexical-cue control** — same verb + outcome, **not** construction-licensing the causation | open / coincidental (the v2c near-miss) |
| `displaced` (other-cause control) | A draft blew the feather off the table while Maria blinked. | **causal-attribution floor** — motion present but by an overt other cause; verb-causation withheld | NOT verb-caused (v1 ctrl-sep analogue) |

- **Target / marginal verbs (M1 + M2):** the harvest-selected off-ceiling subset (§3 freeze rule),
  paired with the fixed light inanimate objects.
- **Clean reference verbs:** the v2c clean-propulsion set (sneeze, cough, blow, puff, huff, fan) — these
   run as the **ceiling reference**, not the headline; they show that when the construction *is*
  automatic the instruments agree (the no-dissociation regime, matching v2c's 100%), so a dissociation
  on the `marginal` arm is read against a within-design positive control.
- **Cue-control / LCC frame (THE mandatory lexical-cue control arm — binding):** the **coordinated
  *and*-frame** from v2c (*"&lt;subj&gt; &lt;verb-ed&gt;, and &lt;obj&gt; ended up &lt;path&gt;."*),
  holding the verb + object + end-state constant and **removing only the caused-motion construction**.
  This carries the same lexical content and the same displacement outcome **without** the
  construction-licensing of the causation — exactly the v2c near-miss design, repurposed here as the
  lexical-cue control. A measured "preference" or "commitment" shift on the `marginal` construction that
  the `cue-control` frame matches is a content/lexical-cue artifact, **not** a construction effect (see
  §6 Δ²). This is the within-design subtraction the conative lesson and the ratified guardrails require.
- **`displaced` other-cause control:** the v1 `ctrl-sep` analogue (motion present, overt other cause) —
  reported for transparency as the causal-attribution floor; it is **not** part of the headline Δ²
  (that is `marginal` − `cue-control`), but it guards against a "any displacement → yes" reading.

## 5. Headroom precondition — PRE-REGISTERED HARD GATE (binding; numbered pre-run condition)

The ratified headroom precondition is implemented as a **pre-headline harvest/baseline arm** that runs
and is evaluated **before any preference/commitment contrast is interpreted**. This is a numbered gate,
not prose:

**G1 — baseline construction-affirm rate, per model, on the `marginal` construction arm.** Measure
P(affirm-causation | `marginal` construction) for each model (pooled over NLI + FC on the H hypothesis).

**G2 — per-model PASS condition:** the baseline `marginal` construction-affirm rate is **materially
off-ceiling: target ≤ 0.30, hard ceiling ≤ 0.50**. A model whose `marginal` construction baseline
exceeds 0.50 has **no headroom** — the construction's add is still automatic for it — and its headline is
**uninterpretable** (a ceiling artifact, exactly the AANN v3 / "default eats the construction" failure).

**G3 — clean-reference sanity check:** the `clean` arm must read at ceiling (≥ 0.85 affirm) per model,
confirming the construction is *available* and the marginality (not a broken instrument) is what depresses
the `marginal` baseline. A model failing this is flagged INSTRUMENT-SUSPECT for that arm.

**G4 — whole-design gate (no retuning):** if **fewer than 2 of 3** models clear G2 (baseline
`marginal` construction-affirm ≤ 0.50), the design's headline **does not stand** and the run **routes to
Option C** of the ratified decision — record "AANN-specific so far" as the disciplined terminal close.
**No retuning, no threshold relaxation, no second harvest.** The harvest subset is frozen by the §3 rule;
if that frozen subset fails G2/G4, the design does not run the headline. (Per **Carry-forward 2**: if the
headroom precondition and the lexical-cue control arm cannot *both* be satisfied at design /
independent-pre-run-critic time, do not run; route to Option C. C is preferred over a guardrail-violating
A.)

**Order of operations (binding):** harvest → evaluate G1–G4 → **only on PASS** freeze the headline item
set and proceed to the preference/commitment arms. The harvest result is reported in the result page
regardless of outcome (a clean Option-C route is itself a first-class finding: "no off-ceiling
add-direction headroom buildable from caused-motion marginal verbs").

## 6. The two instruments and the double contrast (headline; net of the lexical cue)

Both instruments run on the same frozen headline items, mirroring the AANN and conative designs.

### Arm 1 — paraphrase forced-choice (the PREFERENCE signal; the *weaker* instrument)

Present the sentence and two lexically parity-matched paraphrases differing **only** by whether the
caused-motion causal link is asserted; ask which the sentence better supports:

- option **C** (construction reading): *"&lt;subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move."*
- option **N** (no-causation reading): *"&lt;obj&gt; moved, but not because of &lt;subj&gt;'s
  &lt;gerund&gt;."*

A/B letter assignment **seed-counterbalanced** per item (fixed seed, recorded). **Preference measure** =
P(construction-reading C chosen). Indexes graded distributional *compatibility* with the caused-motion
reading.

### Arm 2 — NLI entailment (the COMMITMENT signal; the load-bearing DISCRIMINATOR)

Premise = sentence; Hypothesis = **H = "&lt;subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move."**;
relation 0/1/2 (entailment / neutral / contradiction), single-token, temperature 0 — the v1/v2c
caused-motion NLI arm verbatim. **Commitment measure** = P(commits to the caused-motion entailment) =
P(NLI = 0). (Reported alongside P(NLI = neutral) and P(NLI = contradiction) so the verdict does not hinge
on collapsing categories.)

The caused-motion construction has **no AANN-style grammaticalized agreement reflex**, so — exactly as
the inherited binding condition 4 requires — the **NLI commitment arm carries the discriminator role**;
the paraphrase arm is explicitly the weaker signal. A paraphrase shift without an NLI shift is reported
as **"preference without commitment,"** never as "the model draws the inference."

### The double contrast (Δ²; nets out the lexical cue)

For each instrument, the headline is the **double contrast** — the construction must move the reading
*more than the matched near-miss cue frame moves it*:

- **Δ²_pref** = P(construction-pref | `marginal` construction) − P(construction-pref | `cue-control`/LCC)
- **Δ²_commit** = P(commit | `marginal` construction) − P(commit | `cue-control`/LCC)

A shift wholly attributable to the lexical content / displacement cue (the `cue-control` near-miss shifts
as much as the construction → Δ² ≈ 0) is declared a **LEXICAL-CUE ARTIFACT** and cannot carry the
headline. The raw component effects (`marginal` − `cue-control`; `cue-control` − `displaced`) are reported
in full; the **headline is Δ²** (per inherited binding condition 2).

## 7. Thresholds, bootstrap, verdict map (frozen pre-run — no post-hoc tuning)

- **τ = 0.20** on the double contrast (carried from the AANN/conative instrument, binding condition 3).
- **Significance:** item-level bootstrap **95% CI lower bound > 0** on Δ², **10,000 resamples**, fixed
  **seed = 20260615**. A double contrast counts as "positive" iff Δ² ≥ τ **and** CI-lower > 0.
- **Tier-0 manipulation check:** the `clean` arm must affirm at ceiling (G3) and the `displaced` arm at
  floor; a model failing either is flagged INSTRUMENT-SUSPECT for that arm.

### Per-model verdict map (carried from the AANN/conative instrument, frozen pre-run)

| verdict | condition |
|---|---|
| **CONVERGENT-POSITIVE** | Δ²_pref positive **and** Δ²_commit positive |
| **PARAPHRASE-ONLY** (preference without commitment) | Δ²_pref positive, Δ²_commit **not** positive |
| **COMMITMENT-ONLY** (surprise / mirror) | Δ²_commit positive, Δ²_pref **not** positive — reported as an anomaly, not folded into "confirm" |
| **LEXICAL-CUE ARTIFACT** | a raw construction shift exists but Δ² (net of the near-miss cue) not positive on either arm |
| **NULL** | no shift on either arm (`marginal` construction ≈ `cue-control`) |
| **HEADROOM-FAIL** | baseline `marginal` construction-affirm off-ceiling gate (G2) not met for that model |

### Panel-level verdict (the conjecture's symmetric confirm/falsify — neither uniform reads as confirm)

- **CONFIRM (generalizes to add-direction):** the **qualitative AANN shape** reproduces — Δ²_pref
  positive in most or all of the panel, Δ²_commit positive in a **minority**, with **≥ 1 model
  CONVERGENT-POSITIVE and ≥ 1 model PARAPHRASE-ONLY**.
- **FALSIFY (convergence):** **all three** models CONVERGENT-POSITIVE (full cross-instrument
  convergence) → the dissociation is plausibly AANN-specific (add-direction does not split the
  instruments).
- **FALSIFY (null):** **all three** models NULL (no preference shift to dissociate from) → the antecedent
  is absent for caused-motion; the instance falls, the conceptual "two constructs" point survives
  un-instanced.
- **INCONCLUSIVE → Option C:** the headroom gate fails (G4: < 2/3 models clear G2) → no headline; route
  to Option C, record "AANN-specific so far" as terminal.

**Binding symmetry note (carried from the conjecture):** these criteria are symmetric by design —
**neither a uniform positive nor a uniform null can be read as confirmation** of generality. A uniform
positive *falsifies* (it is the convergence regime, not the dissociation); a uniform null *falsifies*
(the antecedent is absent). Only the split panel confirms.

## 8. Pre-registered scoring caution against retrofitting known single-model fragility (binding anti-cheat)

Carried verbatim in force from the conjecture and conative design: **a single model's pre-existing
NLI fragility must NOT be retrofitted as evidence for generality.** Specifically:

- In the AANN line gpt-5.4-mini was the *converger* (the one model whose NLI commitment carried over);
  on caused-motion v1 it was the conservative model (90% vs the others' 100%) and on the way-construction
  the conservative outlier.
- The test is whether the **full panel** reproduces the AANN *shape*. The identity of any
  CONVERGENT-POSITIVE model is read **from this run's data**, not assumed from prior runs. A genuine
  CONFIRM requires the split to emerge *in this run* — a known-fragile model landing PARAPHRASE-ONLY is
  not, by itself, the dissociation; a *different* model must converge for the AANN shape to be reproduced.
- Per **Carry-forward 3** and the conjecture's caution: do not read any single model's known instrument
  idiosyncrasy as confirmation; the panel-level split is the signal.

## 9. Anchor discipline (binding — Carry-forward 3; honest split, no anchor invented)

- The **NLI entailment arm** on the `clean` and `marginal` construction items *may* make a
  human-comparison claim against the **CxNLI caused-motion gold labels**: **human-anchored** via
  [`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)
  (caused-motion subset — the ratified anchor for the v1 caused-motion line) — an **answer-key
  comparison + aggregate native-speaker baseline, NOT a per-item human gradient** (the release gives a
  single adjudicated gold label per item; verbatim from the resource: it *"anchors an answer-key
  comparison, not a graded human-judgment gradient"*). The caused-motion CxNLI gold for the
  construction's causal-motion hypothesis is **entailment** on canonical items.
- The **paraphrase forced-choice arm**, the **`cue-control`/near-miss LCC arm**, and the **`displaced`
  arm** stay **`anchor: internal-contrast-only`** — no in-repo human paraphrase-preference norm exists,
  and Scivetti has no coordinated/sequence near-miss caused-motion items (verbatim from v2c:
  *"Scivetti has no coordinated/sequence near-miss items → no in-repo human norm on the near-miss arms"*),
  so the near-miss withhold gold is the strict-entailment reading, not a human label. The result page
  declares this split precisely.
- **No human-comparison AANN-uniqueness claim, and no anchor invented.** The result's *generality*
  conclusion (does the dissociation reach a second construction?) is a **within-model / cross-construction
  contrast** — `internal-contrast-only` for the generality claim itself, with the NLI arm's
  caused-motion entailment optionally CxNLI-anchored only for the per-item answer-key comparison. CxNLI
  is **not** an AANN resource and must not be cited for any AANN-uniqueness number. No invented human
  number anywhere.

## 10. Files & freeze discipline (binding; inherited from the conative + v2c harnesses)

- `experiments/runs/2026-MM-DD-third-construction-preference-commitment-v1/prep.py` — stimulus authoring;
  emits the **frozen candidate pool** (`candidates.json`) + the fixed object/frame templates + the §3
  harvest-selection rule; asserts the parity / hypothesis-identity-across-forms / cue-control-isolation
  checks; **no model calls**.
- `.../harvest.py` — runs the §5 baseline `marginal` + `clean` arms; emits `harvest.json`; evaluates
  G1–G4; **freezes the headline `stimuli.json` (sha256 recorded) only on PASS**; on FAIL writes the
  Option-C terminal note and **stops** (no headline arms run).
- `.../stimuli.json` — frozen headline materials (committed before any preference/commitment call; sha256
  recorded in README).
- `.../probe.py` — panel calls (paraphrase-FC + NLI, temperature 0, gemini `reasoning:{effort:"minimal"}`
  + token cap per the cost-driver mitigation); **refuses to run without a frozen `PREREG.md`, a frozen
  `stimuli.json`, and a present `analyze.py`**; codes `ABORT_USD = 0.50`.
- `.../analyze.py` — frozen analysis (double contrast, bootstrap, headroom gate replay, verdict map);
  `--selftest` must pass before freeze.
- `.../PREREG-draft.md` → `PREREG.md` (frozen only after the fresh independent pre-run-critic GO).
- **Adversarial passes (binding):** an independent read-only pre-run critic (a later session / fresh
  agent) must render GO **before any spend**; an independent read-only post-run verifier recomputes every
  figure from `raw/*.json` before the result page is written.

## 11. Candid assessment of headroom feasibility (decision-relevant — surfaced for the critic)

Per the orchestrator's instruction to flag honestly whether the headroom precondition may be unmeetable
for an add-direction construction:

- **Caused-motion is the *best* add-direction lever in the repo**, because its causal attribution
  genuinely depends on a motion-capable verb (the v2 `resist` arm dropped it to 0–70%), unlike the
  way-construction (verb-independent, `resist` 70–100% — effectively un-depressable). This is why
  caused-motion, not *way*, is chosen.
- **But the v2 `resist` numbers are uneven** (claude 30–40%, gpt 0%, gemini 20–70%): gemini in
  particular hovers near or above the 0.50 hard ceiling on some cells. So **the headroom gate may
  genuinely fail for gemini**, and conceivably for ≥ 2 models if the harvest subset is conservative. That
  is a real risk, **not** a flaw in the design — it is precisely what G4 catches, and a clean Option-C
  route ("no off-ceiling add-direction headroom buildable") is a legitimate, first-class terminal
  finding that *strengthens* the "AANN-specific so far" close rather than padding it with a forced run.
- **The critic must therefore weigh:** is the proposed marginal-verb harvest likely to clear G2 for
  ≥ 2/3 models? If the critic judges it cannot, the disciplined call is **do not run; route to Option
  C** — exactly as the ratified decision's binding fallback specifies. This design is built so that
  outcome is reached *before* any budget is spent, via the harvest arm, not after.

## 12. Spend — pre-flight estimate (no spend authorized by this page)

Harvest arm: ≈24 candidate verbs × {`marginal` construction, `clean` reference} × 2 instruments × 3
models ≈ **288 calls**. Headline arm (only on PASS): ≈10–12 retained marginal verbs × {`marginal`,
`cue-control`, `displaced`} × 2 instruments × 3 models ≈ **180–216 calls**. Total if it runs ≈ **470–500
calls**. At the AANN v6 measured shape ($0.0001524/billed call), **≈ $0.07–0.08 point estimate; expect
≈ $0.08–0.20 billed** (cf. conative v1 $0.071; caused-motion v2c $0.212; coercion v2b $0.158 — gemini
reasoning-token overage is the cost driver). Well under the single-run flag and the **$5.00/day UTC** cap
([`config/budget.md`](../../config/budget.md)). **No spend is authorized by this design** — it is
FROZEN-but-NOT-RUN pending an independent pre-run critic GO in a later session, and the harvest arm
itself is gated behind that GO. Actual billed `usage.cost` to be recorded in the run record; missing-cost
calls counted, never silently dropped.
