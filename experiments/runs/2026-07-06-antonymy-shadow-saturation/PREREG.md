# PREREG — A1b antonymy shadow-saturation probe v1 (FROZEN 2026-07-06, session 186)

**Committed BEFORE any model call.** Program A1b. Design:
`experiments/designs/lexical-relation-shadow-saturation-v1.md`. Gates ratified s185:
`wiki/decisions/resolved/antonymy-internal-contrast-scoring.md` (Q1-C / Q2-A / Q3
internal-contrast-only). Conjecture: `wiki/findings/conjectures/lexical-relation-shadow-saturation.md`.

This freezes the item set, the distributional control, the scoring, the verdict map, and the
spend cap. The verdict outcomes — CONFIRMS, SHADOW-SATURATED-FLAT (null), INVERTED, MIXED — are
all named here in advance; no threshold is tuned after seeing model output.

## The question (internal-contrast, no human comparison — Q3)

Over six WordNet **noun** relations, on the panel, against a **contrastive-frame co-occurrence
(G²) distributional control**: is **antonymy the relation whose model relatum-recovery is least
separable from the control** (smallest residual), while meronymy/hyponymy keep a larger residual;
and does the across-relation ranking of raw recovery track the corpus cue-strength ranking, with
antonymy on top of both? The force is a **model-vs-distributional-baseline within-instrument
contrast** — no human-comparison claim, so `anchor: internal-contrast-only` (Q3, ratified).

## POS decision (frozen)

**Nouns only.** WordNet's taxonomic relations (hypernymy/hyponymy/holonymy/meronymy) exist only
for nouns; adjectives carry only antonymy/synonymy, so a **six-relation** cross-relation ranking
is inherently nominal. Antonymy's J&K "home" POS is adjectives — so the **adjective-antonymy
replication is named future work**, not run here. One POS ⇒ no cross-POS pooling (scope cap 4).

## Items (frozen in `items.json`, seed 20260706)

- Six relations, **N=130 cue nouns each** (equal; antonymy's in-band pool is 233, so no
  sub-power cap was needed — the design's antonymy-capped clause did not bind). ~10× founding-era
  N (PROTOCOL §4 powered-N; applied per relation, the residual unit).
- Cue frequency band **Lg10WF ∈ [2.0, 4.5]** (SubTLEX-US). Upper bound is the **outlier cap** —
  it drops the very-highest-frequency iconic pairs (man/woman etc., Lg10WF>4.5) Cao-2025b flags as
  G² outliers, so the ranking is not one-pair-driven.
- **Frequency-matched** across all six relations to a common Lg10WF profile (the antonymy
  distribution, the binding/sparsest relation) by stratified per-bin sampling: per-relation Lg10WF
  medians 3.005–3.015, identical [2.0, 4.5] range — so raw-recovery differences are not a unigram
  artifact.
- Gold = **word-form level** (Cao's task granularity), aggregated over all senses of the cue;
  relata single-word, SubTLEX Lg10WF ≥ 1.5. Max pairwise cue overlap across relations = 11.
- **Gold-relation rule (frozen; fix found via pre-run smoke test, before any scored data):**
  antonymy/synonymy/holonymy/meronymy = **direct (one-hop)** WordNet relata; **hypernymy and
  hyponymy = transitive closure (depth ≤ 4)** — the prompts invite ANY more-general category /
  specific kind, and the model naturally gives valid multi-hop relata (admiration→feeling→emotion),
  so direct-only would unevenly under-credit the inherently-chained taxonomic relations vs one-hop
  antonymy. This makes gold-set sizes differ by relation (a real WordNet fan-out property: antonymy
  mean≈1.1, hyponymy mean≈24, max 486). Two guards below neutralize any size artifact.

**Gold-size guards (both pre-registered, before any model call):**
- The **residual** (𝒮(model) − 𝒮(control)) scores model AND control against the *same* gold per
  relation, so the fan-out effect is present in both terms and largely cancels — the residual is
  the model's *advantage over blind co-occurrence*, size-controlled by construction. A large gold
  set *raises* the control's 𝒮 too, which *lowers* that relation's residual — i.e. transitive
  hyponymy biases hyponymy toward a *small* residual, which is *against* the conjecture
  (it predicts hyponymy keeps a *large* residual). So the size choice is conservative, not
  confirmation-seeking.
- A **size-matched sensitivity** re-runs the residual ranking on only cues with |gold| ≤ 5 across
  all six relations, so the cross-relation ranking is checked on a gold-size-comparable subset.
  Reported alongside the primary. Per-relation gold sizes are reported in full.

## The distributional control (Q1-C, frozen in `control.json`)

Corpus: **Simple English Wikipedia** full dump (`simplewiki-latest-pages-articles.xml.bz2`),
**CC BY-SA 4.0 + GFDL** — the Wikimedia license the s185 scout verified firsthand for English
Wikipedia (`wiki/base/resources/cooccurrence-corpus-scouting.md`). Recipe-not-corpus: the dump is
gitignored, re-fetchable via `build_cooc.py`. 21,307,378 sentence-units; candidate pool
**V = 6,810 open-class content nouns** (SubTLEX Lg10WF≥2.0, ≥3 chars, function-word stoplist
applied — so blind co-occurrence is ranked over the content-noun space the model's relata live in,
not flooded by function-word homographs).

- **PRIMARY control — contrastive-frame G²** (condition 3: the project's own synthesis, not
  Cao's nor J&K's measure). Dunning (1993) signed log-likelihood over co-occurrence **restricted
  to a symmetric/contrastive frame** — cue and candidate within ≤4 tokens with a coordinating /
  contrastive connective between them (and/or/nor/but/versus/than/to/from/neither/either/…), or
  immediately adjacent (conjoined). For each cue the control ranks all of V by signed G², takes
  **top-k=3**.
- **SENSITIVITY control — sentence-level G²** (Cao's all-intrasentential method): same Dunning
  form over any same-sentence co-occurrence. Reported side-by-side to show whether the residual
  ranking is control-choice robust.
- **DEFERRED sensitivity — static-embedding cosine (Q1-B).** A documented omission: the ratified
  decision makes it "only a labelled sensitivity check," and the primary corpus G² is built, so
  deferring the third sensitivity is a scope cut, not a downgrade to the weaker control.

**Proxy-corpus fence (condition 2):** Simple English Wikipedia is a *proxy* for the panel's
(unknown) pretraining distribution; the residual measures the shadow cast by *this proxy*.

## Elicitation (frozen in `probe.py`)

Panel = `config/models.md` slots A/B/C, temperature 0, zero-shot, single-turn; `google/*` gets
`reasoning={"effort":"minimal"}`. k=3 relata per cue.

- **neutral (frame-suppressed):** all six relations, plain relation gloss ("Give up to 3 single
  English words, each the opposite of / a synonym of / a more general category that a … is a kind
  of / …"). The 𝒮(model) that enters the **primary residual**.
- **frame (frame-present):** antonymy ONLY — three symmetric contrastive frames ("X versus ___",
  "neither X nor ___", "from X to ___"), the essay's antonymy-cuing signature. Enters the
  **frame-ablation arm** only.

## Scoring (Q2-A + a gold-size-insensitive companion, frozen in `analyze.py`)

Two per-cue scorers (both frozen; the second added at freeze to neutralize the gold-fan-out
confound both pre-run reviewers flagged — antonymy gold≈1 caps precision at 1/3 when the model
volunteers 3 words, mechanically depressing antonymy 𝒮 toward a small residual):

- **Soundness 𝒮** = (produced words in gold) / (words produced) — Cao's precision-over-produced
  (the ratified Q2-A). 0-produced cue → NA (dropped).
- **HIT@3** = 1 if any produced word is in gold else 0 — gold-size-insensitive (a hit is a hit
  regardless of over-production). **Co-primary**, per the reviews.

Both scorers applied identically to model and control (same 3-slot budget, same gold). **residual =
score(model, neutral) − score(control)**, paired per cue, bootstrap 95% CI over cues (B=2000, seed
20260706). Controls: **frame** (contrastive-frame G², mechanism-specific) and **sent**
(all-intrasentential G², relation-agnostic). **Size-matched** view = frame control on |gold| ≤ 5
cues (per-relation n reported). Clause-2 and frame-ablation as before, reported for both scorers.

- **Clause-2 corpus cue-strength** = mean 𝒮(control) per relation (the 6-relation ranking the
  corpus supplies — condition 1 route (a)); reported for BOTH controls (NIT: clause-1 and clause-2
  share the frame control under route (a) — disclosed, not independent). Antonymy predicted top.
- **%gold-in-V reported per relation** (the control can only propose relata that are in V; an
  asymmetry the reviews flagged — reported so its direction is auditable).
- **Frame-ablation (descriptive):** antonymy score(frame) − score(neutral) per model, both scorers.

## Verdict map (FROZEN — no post-hoc tuning)

n=3 models, orderings not coefficients. Per single (control, cue-subset) view the outcome is:
- **antonymy-smallest** iff antonymy has the smallest residual on **≥2/3** models with meronymy
  and/or hyponymy visibly larger;
- **flat** iff antonymy's residual 95% CI overlaps every other relation's on ≥2/3 models;
- **inverted** iff a weakly-cued relation (meronymy/holonymy) has the smallest residual on ≥2/3;
- **mixed** otherwise.

**Six views** (dual scorer × dual control, plus two size-matched): `soundness_frame`,
`soundness_sent`, `soundness_sizematched`, `hit_frame`, `hit_sent`, `hit_sizematched`. Per view the
per-model smallest-residual relation and the antonymy-smallest count (/3) are reported. Headline
(frozen logic in `analyze.py`):

- **CONFIRMS-ROBUST** — antonymy smallest on ≥2/3 models under **all four frame views**
  (soundness+hit × full+size-matched) **AND both sent views** (relation-agnostic — the neutral
  baseline the vote demanded).
- **CONFIRMS-FRAME-SPECIFIC** — robust under the four frame views but **not** the sent views ⇒ the
  panel's antonymy recovery is saturated by the *contrastive-frame* shadow specifically, not by
  generic co-occurrence. Reported as scoped, not a bare confirm.
- **SHADOW-SATURATED-FLAT** — antonymy's hit-frame residual CI overlaps all others on ≥2/3.
- **INVERTED** — the smallest-residual relation (hit-frame) is one of the **two measured
  weakest-cued relations** (bottom-2 by frame cue-strength, computed from the corpus — SHOULD-FIX 5;
  the earlier hard-coded "meronymy/holonymy" gloss was wrong, meronymy is 2nd-strongest cued) on
  ≥2/3.
- **MIXED/NO-MAJORITY** — otherwise.

"Visibly larger" (the CONFIRMS side-condition) is operationalized as **CI-separation**: antonymy
residual CI-upper < meronymy or hyponymy residual CI-lower (reported as a count /3), not left vague.

**Calibration gate (formalizes the vote's SHOULD-FIX):** if mean 𝒮(control) is negligible and the
soundness residual ranking merely reproduces the raw-𝒮(model) ranking (Spearman ≈ 1, reported per
model), the residual arm is reported **descriptively only** — the control explains too little for
the residual to be a separability measure — and weight shifts to clause-2 (corpus cue-strength) and
the frame-ablation arm. Pre-named, not a post-hoc downgrade.

**Pre-registered instrument caveat (named before the run):** the control is blind top-k=3
precision, structurally low in absolute terms (antonymy control 𝒮≈0.077, others 0.010–0.023 —
measured from the corpus with no model involvement). If model recovery is uniformly high, the
residual will approximately track raw recovery, and an INVERTED/MIXED primary verdict is a live,
honest outcome — it would mean the panel's antonym production exceeds *this* weak co-occurrence
control by as much as its other-relation production does, i.e. the model's antonymy competence is
not "saturated" by a top-3 contrastive-frame control. Clause-2 (corpus cue-strength) and the
frame-ablation arm are informative under any primary verdict, and are reported regardless.

## Spend

Pre-flight: 6×130 neutral + 130 antonymy-frame, ×3 models ≈ **2,730 calls**, short outputs →
**≈ $0.4–0.9** projected (cf. s178 AANN 1,782 calls $0.31). `ABORT_USD = 2.50` in `probe.py`
(single-run prudence flag). Post-run: record billed `usage.cost` in `config/budget.md`.

## Registered bet (`predictions.md`)

Antonymy has the **smallest frame-control residual** on ≥2/3 models (clause 1) AND raw recovery
ranking tracks corpus cue-strength with antonymy top (clause 2). Fires on this run; the flat-null
and inverted outcomes are first-class losses.

## Gates remaining before spend

Independent pre-run critic (fresh agent) + one non-Anthropic decorrelation vote (PROTOCOL §A3);
then run; then independent post-run verifier recomputes from raw.
