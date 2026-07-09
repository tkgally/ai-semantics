# PREREG — VERB-relation decoupling probe (H-verb-1 + H-verb-2)

**Frozen s199, 2026-07-09, BEFORE any model call.** Design:
[`design/lexical-relation-recovery-verb-decoupling-v1`](../../designs/lexical-relation-recovery-verb-decoupling-v1.md).
Gates RATIFIED s199:
[`decisions/resolved/verb-relation-decoupling-design`](../../../wiki/decisions/resolved/verb-relation-decoupling-design.md)
— **Q1-C / Q2-A / Q3 internal-contrast-only**, with three additional binding conditions **B1–B3** on top
of the seven design-page freeze conditions. This file freezes the item set, the control, the depth proxy
(spec + predicted sign), the corpus, the verdict map with numeric thresholds, the B1 numeric degeneracy
bound, and the anti-cheat fence. Nothing below may be touched after recovery is observed.

## The question (nothing wider)

On a **fresh** relatum-production probe over WordNet **verb** relations, run on the panel against a
contrastive-frame G² control byte-frozen from the s193 `build_cooc_c4.py` (only the cue POS and candidate
pool V changing to verbs), with a **troponymy-depth proxy pre-registered before recovery is observed**:
**(H-verb-1)** does across-relation recovery rank **decouple** from contrastive-frame cue-strength on
verbs (near-zero or negative ρ_cue, the noun band) — confirming "hierarchy ⇒ decoupling" out of nouns —
or does cue-strength **regain** predictive power (clearly positive ρ_cue, the adjective band),
**falsifying** the conjecture's central identification despite the verified verb hierarchy? **(H-verb-2)**
does a pre-registered troponymy-depth proxy (`min_depth` of the cue's first verb synset; predicted sign
**negative**) **out-predict** contrastive-frame cue-strength for recovery rank, ≥2/3 models? **Internal-
contrast only** (Q3): recovery is scored against WordNet, a shared target that cancels in the head-to-head;
both predictors are corpus/lexicon statistics; no human baseline enters.

## Frozen artifacts (built + committed BEFORE any model call)

- **`items.json`** (`prep.py`, SEED 20260709): FRESH cue verbs per relation, **POS-agnostic-surface
  DISJOINT** from the **1,740** committed prior cue lemmas (s186 nouns + s193 fresh nouns + s196
  adjectives; asserted 0 overlap, all relations — freeze-condition 4). Each cue carries its word-form
  gold relatum set (relata() the verb parallel of s186) **and** its `trop_depth`
  (`wn.synsets(cue,'v')[0].min_depth()`; Q2-A). Frequency band Lg10WF ∈ [2.0, 4.5], matched to
  **antonymy's** fresh per-bin profile (the binding relation, freeze-condition 3). **ACHIEVED per-relation
  N (freeze finding):**

  | relation | N | Lg10WF median | mean trop-depth | gold median |
  |---|---|---|---|---|
  | antonymy | 130 | 2.979 | 1.577 | 1 |
  | synonymy | 130 | 2.982 | 2.208 | 4 |
  | hypernymy | 130 | 2.986 | 2.192 | 10 |
  | troponymy | 130 | 2.955 | 2.431 | 6 |
  | entailment | 130 | 2.933 | 2.154 | 2 |
  | cause | 126 | 2.795 | 1.690 | 2 |

  **776 verdict-bearing cues.** trop-depth resolved 100%. **`cause` INCLUDED** as a 6th relation by the
  **mechanical rule (freeze-condition 5): achieved matched-N = 126 ≥ CAUSE_MIN (100)** → the arm is
  6-point. All CORE relations clear the thin-relation floor (CORE_FLOOR 80; freeze-condition 3).

- **`vocab.json`** (`prep.py`): the control's candidate pool V = all single-word SubTLEX **verbs**
  (Lg10WF ≥ 2.0), |V| = 2,645.

- **`control.json` / `counts.json`** (`build_cooc_c4.py`): the contrastive-frame G² control on **C4**.
  **Freeze-condition 6 (byte-freeze integrity):** `signed_g2` + `compute_control` produce **byte-identical
  output** to the s193 `build_cooc_c4.py` (verified by assertion — a battery of inputs + a synthetic
  `compute_control` case; K, FRAME_WIN, CONNECTIVES identical); only the **cue POS (→verbs)** and
  **candidate pool V (→verbs)** change. The s193 nominal **Hearst arm is DROPPED** (Q2-C rejected — verb
  troponymy has no clean corpus frame; the single H2 vehicle is the structural depth proxy). Corpus: C4
  (`allenai/c4` en) shards **00000–00002** (the s193-frozen set), streamed and discarded; volume asserted
  ≥ s186's 21.3M sentences / ~320M tokens. ODC-BY (+ Common-Crawl terms — travels to the result
  provenance).

## Frozen predictor vectors (pre-recovery — legitimate to state; NO model data existed when computed)

- **Troponymy-depth (H2 proxy, predicted NEGATIVE), per relation:** antonymy 1.577 · cause 1.690 ·
  entailment 2.154 · hypernymy 2.192 · synonymy 2.208 · troponymy 2.431.
- **Cue-strength (contrastive-frame G² soundness, H1 predictor), per relation** (frozen in `control.json`
  from the C4 stream + the frozen gold, before any model call): antonymy **0.0923** · troponymy 0.0487 ·
  synonymy 0.0308 · hypernymy 0.0207 · cause 0.0106 · entailment 0.0051 (mean control-frame soundness
  0.0347 — non-degenerate, top-3 produced for ~every cue).

**Note the confound made explicit (condition 2 / B2):** **antonymy is BOTH the highest-cue-strength
relation (0.0923) AND the shallowest-depth relation (1.577)** — its contrastive frames literally *are*
antonym frames — so on verbs ρ_cue-positive and ρ_depth-negative are **aligned** through antonymy (the
reverse of the noun case, where low-cue-strength hypernymy was taxonomically central and *disaligned*
them). This is exactly why the frozen depth spread is DEGENERATE (B1) and H2 is under-powered
symmetrically (B2). H1 is unaffected: cue-strength's rank {antonymy > troponymy > synonymy > hypernymy >
cause > entailment} is a well-defined predictor independent of depth.

## B1 — the NUMERIC degeneracy bound (the s199 ratifier's binding condition; frozen pre-recovery)

The between-relation troponymy-depth spread is **near-degenerate** on verbs (the s198 critic's catch).
B1 requires a **single committed numeric bound**, computed on the **frozen freq-matched sample** before
any model call, decided outcome-independently. As ratified, the bound is on the **non-antonymy CORE-4
mean-depth range** {synonymy, hypernymy, troponymy, entailment} — the fixed backbone, independent of the
mechanical `cause` decision:

> **`DEGEN_MAX_RANGE = 0.50`.** The depth spread is **DEGENERATE** iff the non-antonymy CORE-4 mean-depth
> range < 0.50. Rationale (pre-committed, not tuned): at a within-relation depth SD ≈ 2 and N ≈ 130, one
> standard error of a relation mean ≈ 0.18, so a 4-relation range must clear ≈ 2.5–3 SE (≈ 0.5) to be a
> real, above-sampling-noise depth test.

**FROZEN VERDICT (on the frozen sample): DEGENERATE.** Achieved non-antonymy CORE-4 range = **0.277**
(troponymy 2.431 − entailment 2.154) < 0.50. [Transparency: the cause-inclusive non-antonymy range is
0.741 and the full-set depth SD is 0.304 — both recorded in `items.json`, neither drives the verdict; the
non-degeneracy of the wider set rides on `cause` (1.69) and antonymy (1.577), and antonymy's shallow depth
is **confounded** with its high contrastive-frame cue-strength.]

**B2 — symmetric application.** Because the spread is DEGENERATE, H2 is under-powered **symmetrically**:
a **DEPTH-FAILS** is reported UNDER-POWERED / **non-falsifying** (does NOT fire conjecture-falsifier-2),
**AND** a **DEPTH-OUT-PREDICTS** is flagged UNDER-POWERED — **not banked as mechanistically equivalent to
the noun H2** (possibly antonymy/cause-driven). `analyze.py` applies this automatically from the frozen
`b1_depth_spread.depth_degenerate` flag.

## Panel & elicitation (byte-identical to s186/s196 neutral arm)

Panel = [`config/models.md`](../../../config/models.md) `panel.A/.B/.C` (never hardcode slugs).
Temperature 0, zero-shot, single-turn, neutral system prompt; `google/*` gets
`reasoning={"effort":"minimal"}`. NEUTRAL prompt scaffold + `parse_words` + the antonymy/synonymy GLOSS
lines byte-identical to s186 `probe.py`; the verb-specific gloss lines are the POS parallel. **Two arms:**
neutral (all 6 relations) + an **antonymy frame-ablation** arm (antonymy only; the corpus-free hedge
against a calibration-gate refire, condition 7 — descriptive, bears on the antonymy-shadow reading, not
on H1/H2). `ABORT_USD = 1.50`. Every call records `usage.cost`.

## Metrics

- **Recovery 𝒮** (per relation) = mean raw **Soundness** (Cao precision-over-produced). **HIT@3** =
  gold-size-insensitive co-primary.
- **Cue-strength** (per relation) = mean 𝒮(control top-3, frame variant).
- **ρ_cue / ρ_depth** = across-relation Spearman (**tie-naive** — the authoritative s186/s193 pipeline) of
  recovery against each predictor, **per model**.

## Verdict map (FROZEN; direction fixed; exhaustive bands)

**Verdict of record = the ACROSS-RELATION result** (Q1-C). The item-level cue/depth regression is
**descriptive/robustness-only, NON-DECISIVE**.

**H-verb-1 (the registered decoupling) — exhaustive, mutually-exclusive bands on primary (soundness) ρ_cue:**
- **DECOUPLING-REAPPEARS** iff ρ_cue **≤ +0.30** on **≥2/3** models (near-zero or negative; the noun band).
- **DECOUPLING-BREAKS** iff ρ_cue **> +0.50** on **≥2/3** models (cue-strength recovers its predictive
  power despite the verified verb hierarchy — the clean falsifier of the conjecture's central
  identification, fires conjecture-falsifier-1).
- **H1-INCONCLUSIVE** otherwise (the (+0.30, +0.50] gap or no ≥2/3 majority) — pre-named first-class,
  broken by the powered item-level arm.

**H-verb-2 (troponymy-depth; predicted NEGATIVE) — numeric margin, THEN the B1/B2 under-power gate:**
- Depth **wins** for a model iff **|ρ_depth| − |ρ_cue| ≥ 0.20** AND ρ_depth is **negative**.
- **DEPTH-OUT-PREDICTS** iff depth wins on **≥2/3**; **DEPTH-FAILS** otherwise.
- **B1/B2 gate (frozen DEGENERATE):** a DEPTH-FAILS is reported **under-powered/non-falsifying**; a
  DEPTH-OUT-PREDICTS is reported **under-powered, not noun-equivalent**. Neither is read as
  mechanistically equivalent to the noun H2 (condition 2: antonymy depth×cue-strength confound).

**Pre-named nulls (first-class):** ρ_cue in the INCONCLUSIVE band with the item-level arm also ambiguous;
or DECOUPLING-REAPPEARS but DEPTH-FAILS (decoupling without the named mechanism — but under-powered on
verbs, so uninformative about mechanism); or the across-relation and item-level arms **diverge** (reported,
not resolved by fiat).

**n = 3 models; orderings, not coefficients; VERBS only. No pooling across models or POS.**

## What each outcome feeds (B3 softening applied — a THIRD point, never the established law)

- **DECOUPLING-REAPPEARS:** "hierarchy ⇒ decoupling" gains its first out-of-noun confirmation — **one
  point in a three-point pattern** (nouns + adjectives + verbs) a future review would weigh toward
  broadening the noun claim; NOT the established POS-structural law, and NOT an isolation of hierarchy
  (verbs confound POS with hierarchy as nouns do). Still `internal-contrast-only`, within-distribution.
- **DECOUPLING-BREAKS:** a POS that *has* a hierarchy still shows cue-strength predicting recovery — the
  sharpest result; the conjecture's central identification collapses. First-class negative.
- **H2 (either branch):** under-powered on verbs by B1/B2 — informative only weakly; never noun-equivalent.
- **A [`predictions.md`](../../../wiki/predictions.md) probe row** is registered at freeze (co-registered
  with the s197 conjecture bet, not double-scored); outcome updated the run session.

## Anti-cheat fence (PROTOCOL §B; the ten conditions)

The fresh disjoint cue sets, the band [2.0,4.5] outlier cap, k=3, the relation inventory (incl. the
mechanical `cause`-inclusion rule + the CORE thin-relation floor), the troponymy-depth proxy spec + its
predicted negative sign, the ρ_cue bands, the ρ_depth margin, and the **B1 numeric degeneracy bound**
(0.50 on the non-antonymy CORE-4 range) are **all frozen here BEFORE any model call**. No band, proxy, or
threshold is touched after recovery is seen. DECOUPLING-BREAKS, DEPTH-FAILS/DEPTH-OUT-PREDICTS (both
under-powered by B1/B2), and the nulls are pre-named first-class. The G² computation is byte-frozen vs
s193 (condition 6). `internal-contrast-only` — recovery scored vs WordNet, a shared target that cancels;
predictors are corpus/lexicon statistics; no human baseline.

**Construct-validity scope caveats (carried to the result, not gates):** (a) gold is all-sense while the
depth proxy is first-synset (byte-identical to the noun run); (b) hypernymy gold median ≈ 10 vs antonymy's
≈ 1 — a gold-size confound, mitigated by the HIT@3 co-primary, disclosed; (c) the corpus is a proxy for
the panel's pretraining distribution (fence carried).
