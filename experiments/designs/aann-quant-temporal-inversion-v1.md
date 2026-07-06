---
type: design
id: aann-quant-temporal-inversion-v1
title: "AANN quant×temporal inversion — class-vs-lexical widening probe (v1): is the one panel-wide model-vs-human inversion cell (humans rate 'a scant three days' HIGHEST, every model LOWEST) the whole quantity-adjective class or a few items? DESIGN, NOT FROZEN — one open decision (anchor scope + class-vs-lexical threshold)"
meaning-senses:
  - constructional
  - human-comparison
status: "RATIFIED + FROZEN s189 (design s188; decision ratified s189 ADOPT-WITH-CHANGES [Q1-C human-N-gated / Q2-B primary / Q3-A]; run + result follow in the same session — see experiments/runs/2026-07-06-aann-quant-temporal-inversion/)"
anchor: "hybrid (Arm 1 anchored → resource/mahowald-2023-aann-stimuli; Arm 2 internal-contrast-only)"
contingent-on: []
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: operationalizes
    target: open-question/aann-quant-temporal-inversion
  - rel: refines
    target: result/aann-temporal-why-reanalysis
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: result/aann-temporal-heldout-v2b
  - rel: depends-on
    target: claim/aann-behavioral-gradient
  - rel: depends-on
    target: conjecture/aann-construction
---

# Design v1 — AANN quant×temporal inversion: class effect or lexical effect?

**What this is.** A frozen-*to-be* forward probe operationalizing
[`open-question/aann-quant-temporal-inversion`](../../wiki/findings/open-questions/aann-quant-temporal-inversion.md):
is the single panel-wide model-vs-human inversion cell — **quantity adjectives × temporal nouns**
("a scant three days", "a mere two weeks"), where humans rate **highest** of the four adjective
classes and every panel model rates **lowest** — a property of the **whole quantity-adjective class**
or of **a few lexical items** (*scant*/*mere*)? It **reuses the byte-frozen v2b graded-acceptability
instrument**; the only newly-assembled artifact is the **item set**.

> **Status: DESIGN, NOT FROZEN (s188, 2026-07-06).** One value-laden gate is routed to
> [`decisions/open/aann-quant-temporal-inversion-design`](../../wiki/decisions/open/aann-quant-temporal-inversion-design.md):
> **Q1** (anchor scope: anchored-narrow / wide-unanchored / hybrid), **Q2** (the class-vs-lexical
> scoring threshold), **Q3** (the non-quant reference baseline that *defines* "inversion"). Nothing
> here is frozen; no `prep.py` exists yet; **no model call is made this session and nothing is
> spent.** Per [`PROJECT.md`](../../PROJECT.md) §12.3 the decision is **opened this session and is not
> ratifiable until a later session**; the probe **freezes and runs only after it ratifies**. Anything
> depending on the decision stays provisional and carries the decision id in `contingent-on:`.
>
> **Reviewed s188 → GO-WITH-CONDITIONS.** A fresh-agent pre-run critic (no fabrication — every cited
> figure verified against source) + a convergent decorrelated non-Anthropic vote returned **2 PREREG
> blockers** (B1 per-modifier noun-balance; B2 verdict-map NULL-vs-CLASS/LEXICAL precedence) + 10
> SHOULD-FIX, all **binding on the freeze/run session** (see the *Design-review record* at the foot of
> this page and `experiments/runs/2026-07-06-aann-quant-temporal-inversion/REVIEW-design-s188.md`). Two
> body framings are **scoped there**: "byte-frozen instrument / only the item set is new" (S10 — the §6
> verdict logic is *also* new code, frozen + self-tested in the PREREG) and "item-matched" (S3 — Arm 1 is
> a per-modifier gradient comparison unless items are restricted to Mahowald's exact tuples at freeze).

---

## 1. The finding this sharpens (reproduced verbatim, cited)

The AANN construction ("a beautiful three days", *article–adjective–adjective/numeral–noun*) carries a
human acceptability gradient over adjective × noun classes
([`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md),
Experiment-2, 1–10 MTurk scale). The temporal noun class fails to replicate that gradient held-out; a
$0 re-analysis ([`result/aann-temporal-why-reanalysis`](../../wiki/findings/results/aann-temporal-why-reanalysis.md))
located the *negative sign* in **one cell — quantity adjectives × temporal nouns** — which humans rate
**highest** of the four adjective classes and every model rates **lowest**:

| adjective class (× temporal) | human mean | claude | gpt | gemini |
|---|---|---|---|---|
| neg | 7.57 | 49.4 | 40.2 | 75.0 |
| pos | 8.02 | 50.6 | 37.5 | 70.0 |
| ambig | 8.25 | 55.0 | 50.6 | 84.3 |
| **quant** | **8.45 (highest)** | **43.0 (lowest)** | **30.1 (lowest)** | **68.8 (lowest)** |

*(Table reproduced from [`result/aann-temporal-why-reanalysis`](../../wiki/findings/results/aann-temporal-why-reanalysis.md),
H4. Exact unrounded model class-cell means from that run's `results.json` — claude 43.00 / gpt 30.05 /
gemini 68.75 on quant; human quant mean 8.4508, n = 193 ratings; the other human means 8.2526 / 7.5673
/ 8.0183, from the frozen v2 `human_class_means.csv`.)* **Dropping the quant cell**, the remaining
three-class ranking (neg < pos < ambig) flips **positive for all three models** (claude **+1.00**,
gpt **+0.50**, gemini **+0.50** — same source). A frequency artifact is ruled out (H3); small inventory
limits precision but not direction (H2). So this is a **clean, localized, panel-wide model-vs-human
inversion** — the sharpest handle in the AANN line on where the model gradient does not merely compress
but **reverses** relative to humans (`constructional` × `human-comparison`).

**The confound the located inversion carries (why widening is needed).** The re-analysis's quant×temporal
model means come from the **v2b held-out temporal arm**, whose quant adjectives are **project-assigned,
held-out** items *(ample, lavish, negligible, respectable, skimpy, towering, colossal, modest, scant,
sizable* — verified in `experiments/runs/2026-06-13-aann-temporal-heldout-v2b/stimuli.json*)*, scored
against Mahowald's **anchored** quant-class human mean (8.45), whose adjectives are a **different**
lexical set *(mere, staggering, whopping, hefty, paltry, meager, extra, measly, substantial,
record-setting* — [`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md),
Table 1). So the located inversion is (a) a comparison across two disjoint quant lexical sets and (b)
rests on only 10 held-out quant adjectives on 5 nouns. Whether the inversion is the **class** or **a few
items** — and whether it even survives Mahowald's *own* attested quant set — is exactly what this probe
is built to separate.

## 2. The question, sharply

> Is the quant×temporal inversion (humans-high / models-low) a property of the **whole
> quantity-adjective class**, or is it carried by **a few lexical items**? Does it **persist** when the
> quantity-modifier set and the temporal-noun set are widened beyond the thin v2b inventory? The **null
> is first-class**: if the inversion does not reproduce on the widened set, the temporal class's negative
> sign was an **inventory artifact** of the specific held-out quant adjectives — written as such.

## 3. Instrument — REUSE the v2b graded-acceptability instrument (byte-frozen); only the item set is new

The re-analysis's handoff is explicit that **the instrument is settled**: *"Neither [decider] requires
re-litigating the instrument: Tier-0 and framing-robustness already pass in v2b, so the inversion is the
models' graded behavior, not an artifact"*
([`result/aann-temporal-why-reanalysis`](../../wiki/findings/results/aann-temporal-why-reanalysis.md),
*What would decide it*). This design honors that: it changes **only the stimuli**.

**Byte-frozen, reused unchanged from [`design/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md)
/ `experiments/runs/2026-06-13-aann-temporal-heldout-v2b/`:**

- **`probe.py`** — the primary indicator `P100` (prompted **0–100 graded acceptability**, integer-only,
  *"Respond with ONLY the integer"*), the `P4` 4-point framing, the `PT0` Tier-0 forced-choice prompt,
  the system prompt (*"You are a careful native-speaker judge of English acceptability."*), the parsing
  (`parse_int`: full-string bare integer first, else the **last** in-range token; one verbatim retry
  then missing), the per-slot settings (**temperature 0**; `max_tokens` 64 for A/B, 512 for C;
  `google/*` at `reasoning:{"effort":"minimal"}` per [`config/models.md`](../../config/models.md)), the
  billed-cost logging, and the `PREREG`/`analyze.py`-must-exist run guards.
- **`analyze.py`** — the Spearman conventions, the 10,000-resample percentile bootstrap CI, the Tier-0
  gate (≥ 20/24, parsing the last standalone A/B), and the 4-point framing-fragility caveat (ρ < 0.50 or
  NaN ⇒ fragility caveat, never gate-bearing). Scoring logic is copied, then extended only by the new
  per-modifier decomposition of §6 (declared here, frozen in a `PREREG` before any call).

**Newly assembled (the only new thing): the item set (`stimuli.json`), built by a fresh `prep.py`
(no model calls).** Because the instrument is unchanged, the run inherits v2b's settled Tier-0 +
framing-robustness status. Confirming that status from the frozen v2b record:

- **Tier-0 passed 3/3 in v2b** (`results.json`: `tier0_passers = ["A","B","C"]`; claude 23/24). This is
  the instrument's manipulation check (does the model prefer licit AANN to its degenerate variants).
- **Framing-robustness passed under the v2 instrument** (0–100 vs 4-point item-level ρ **0.93 / 0.82 /
  0.82**, [`claim/aann-behavioral-gradient`](../../wiki/findings/claims/aann-behavioral-gradient.md),
  *Grounds* table).

Following v2b's discipline, **Tier-0 and the 4-point framing arm are re-run fresh this occasion** (they
are not inherited across occasions), byte-identical, as per-occasion instrument checks — so the inversion
read stands on a *this-occasion* clean instrument, not an assumed one.

## 4. Item design — widen the quant×temporal cell so CLASS and ITEM are separable

The class-vs-item question needs **many quantity modifiers, each on several temporal noun/template
combinations**, so we can *count how many modifiers invert* rather than read one mean. Structure (subject
to the freeze specifics the decision fixes):

- **Quantity modifiers, K ≈ 20**, deliberately spanning Mahowald's attested set **and** beyond it, and
  balanced across the two quantity-polarity subtypes:
  - **~10 Mahowald-anchored quant adjectives** (his Exp-2 `quant` class, Table 1): *mere, staggering,
    whopping, hefty, paltry, meager, extra, measly, substantial, record-setting* — **these carry
    item-level human ratings** in `mturk_data/adjexp_turk.csv` and form the anchored arm (Arm 1).
  - **~10 widened, beyond-Mahowald modifiers**: *scant, bare, skimpy, negligible, modest, ample, solid,
    full, good, whole* (drawn from the re-analysis handoff — *"more scant/mere/measly/paltry/good-type
    quantity modifiers"* — and the OQ's *"scant, mere, measly, paltry, good, full, whole, solid, bare"*).
    **No human rating** (internal-contrast; Arm 2).
  - **Quantity-polarity subtype** (a pre-registered *descriptive* stratum, §6): *small/diminishing*
    modifiers giving the idiomatic "only X" reading (*mere, paltry, meager, measly, scant, bare, skimpy,
    negligible, modest*) vs *large/augmentative* (*staggering, whopping, hefty, substantial, ample,
    solid, full, good, whole, record-setting, extra*). This matters because "a scant/mere three days"
    ("only three days") may be a **subtype** signature, not the whole class — and the v2b held-out set
    was heavy on large-magnitude/size adjectives (*towering, colossal, sizable, ample*), a candidate
    reason it inverted.
- **Temporal nouns (all 5 Mahowald):** *days, hours, weeks, months, years*; **numerals** *three*/*five*
  (Mahowald's bulk numerals); **templates** the 3 Mahowald temporal frames recovered in v2b (*"The
  family spent X in London" / "The diplomat worked X in Nairobi" / "The tourish stayed X in Papua New
  Guinea"* — the upstream *tourish* typo retained for instrument continuity, as in v2b; held-out items
  make no item-level human comparison so it carries no anchor risk).
- **~6 items per modifier** (seeded rotation across the 5 nouns × 3 templates × 2 numerals, class- and
  template-balanced, deterministic seed frozen in `stimuli.json` as in v2b) ⇒ **≈ 120 quant items**.
- **Non-quant reference cells (Mahowald's own ambig/pos/neg temporal adjectives), ~4 each × ~3 items ≈
  36 anchored items**, to define the model's non-quant temporal baseline **B_m** (§6) *on the same
  occasion* and to reproduce the exact four-class comparison of the re-analysis table (Q3 fixes whether
  the baseline is this fresh reference or v2b's frozen non-quant ratings).

**Main arm ≈ 156 items** (120 quant + 36 reference). **Powered N justification (PROTOCOL §4):** the
verdict is a *per-modifier* count over the quant set, so power lives in the **modifier count (K ≈ 20)**
and the items-per-modifier (~6); 120 quant items is ~10× the founding-era micro-N and ~7.5× the v2b
held-out quant cell (16 items), which is exactly the "too thin to read" inventory the widening relieves.

**Frequency control (inherited):** widened and reference adjectives are Zipf-matched per class to the
Mahowald class median within ±0.5 (v2b's `prep.py` procedure, mechanically asserted in `stimuli.json`),
so raw acceptability differences are not a unigram-frequency artifact — H3 was already ruled out and stays
ruled out here.

## 5. Human anchor + scope caveat (the operationalization crux → the decision)

- **Arm 1 (anchored, human-comparison).** Mahowald's **own** quant adjectives × temporal are items
  Mahowald **actually rated** (`mturk_data/adjexp_turk.csv`, item ids `{adjective}-{numeral}-{noun}-sent-
  {nounclass}-{template}`, 1–10 `answer`). So Arm 1 is an **item-matched model-vs-human** comparison —
  *stronger* than v2b's held-out gradient-replication — and it `anchors:` →
  [`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md).
  Per-modifier human means are **computed at freeze** from `adjexp_turk.csv`; modifiers with too few
  ratings to estimate a stable per-modifier mean (threshold frozen in `PREREG`) enter only the
  class-level comparison, not the per-modifier one. **No human rating is invented**: only ratings present
  in the resource enter, and only the in-repo class means (quant 8.45 etc.) are quoted here.
- **Arm 2 (widened, internal-contrast).** Beyond-Mahowald modifiers carry **no human rating by
  construction**, so they are read as **within-model** contrasts (against B_m) and as gradient-replication
  against the anchored quant-class ordering — never as a fresh human measurement.
- **The trade-off is the crux.** *Anchored-but-narrow* (Arm 1 only) is fully human-anchored but may be
  too thin to separate class from item; *wide-but-partly-unanchored* (Arm 2) is wide enough but
  internal-contrast on the new items. The **hybrid** carries both, reported separately. Which scope the
  freeze adopts is **Q1 of
  [`decisions/open/aann-quant-temporal-inversion-design`](../../wiki/decisions/open/aann-quant-temporal-inversion-design.md)**
  (provisional default: **C, hybrid**). Until it ratifies, the anchor structure above is provisional and
  the design carries `anchor: pending`.

## 6. Pre-registered scoring + verdict thresholds (frozen in advance; NULL first-class)

All statistics, the modifier list, K, the reference set, B_m, and the thresholds are **frozen in the
`PREREG` before any model call**; the indicator is **not tuned after seeing which modifiers invert**
(PROTOCOL §B anti-cheat). Per-model reads, panel verdict by the **≥ 2-of-3 rule over Tier-0-passing
models** (v2b semantics: a Tier-0 failure ⇒ that model reported descriptively, never counted).

**Per-modifier inversion indicator (widened set — the class-vs-lexical primary).** For quant modifier
*j* and model *m*, `A_m(j)` = mean 0–100 acceptability over *j*'s temporal items; `B_m` = the model's
non-quant temporal baseline (mean over the ambig+pos+neg reference items; Q3 fixes its source). Modifier
*j* **inverts** for *m* iff `A_m(j) < B_m` (the quant cell's defining property is that it sits *below*
all three non-quant cells). Let `p_m` = fraction of the K quant modifiers that invert.

- **CLASS effect (per model):** `p_m ≥ 0.70` (the drag is broad). *(X = 0.70 provisional; Q2.)*
- **LEXICAL effect (per model):** `p_m ≤ 0.30` **and** removing the bottom-3 modifiers lifts the pooled
  quant-cell mean to ≥ B_m (the cell inversion disappears without a few items). *(Y = 0.30 provisional;
  Q2.)*
- **MIXED / SUBTYPE:** 0.30 < `p_m` < 0.70, **or** the inverting modifiers are predominantly one
  quantity-polarity subtype — reported descriptively as **SUBTYPE** (small-quantity vs large-quantity).
- **Panel verdict** = the category holding for **≥ 2/3** Tier-0-passing models.

**Anchored per-modifier model-vs-human (Arm 1 — the human-comparison leg).** Over Mahowald's own quant
modifiers with a stable human mean, report (i) the per-modifier **sign** of model-low/human-high, (ii)
the Spearman between `{A_m(j)}` and the human `{H(j)}`, and (iii) whether the anchored quant **class**
still sits **lowest** for models while **highest** for humans (direct reproduction of the §1 table). If
most of Mahowald's *own* quant modifiers show model-low/human-high, the inversion is a **class** property
even within the attested set — the strongest, fully-anchored form of the answer.

**NULL (first-class, pre-named).** If the widened quant-cell mean is **not** the lowest of the four
adjective-class cells for ≥ 2/3 models — i.e. the quant cell no longer sits below the non-quant baseline
once the modifier set is widened — then the located inversion was an **artifact of the thin v2b held-out
quant sample**; the temporal class's negative sign **dissolves**. Written as a clean, useful negative
(the OQ's *"if the inversion does not reproduce on the widened set, that dissolves the temporal class's
negative into an inventory artifact"*).

**Secondary / descriptive (no gates):** the quantity-polarity subtype split; the per-noun structure (the
re-analysis noted per-noun ρ negative for short-span *days/hours*, positive for *years*); the four-class
table reproduction; the pooled item-grain model-vs-human rank agreement on Arm 1; a *tourish*-template
sensitivity recompute (v2b semantics).

## 7. Cost pre-flight (config/budget.md)

**Reference runs:** v2b (this exact instrument) billed **$0.0793** for 432 calls; the powered rep2 re-run
of the AANN gradient billed **$0.3092** for 1,782 calls; v2 measured per-model arm costs A $0.1934 / B
$0.0476 / C $0.0715. Using v2b's **measured billed per-call rates per arm** (held-out 0–100: A $0.000331,
B $0.000080, C $0.000115; Tier-0: A $0.000263, B $0.000068, C $0.000221; 4-point: A $0.000355, B $0.000083,
C $0.000114):

| Arm | Items × models | Calls | A | B | C |
|---|---|---|---|---|---|
| main 0–100 (156 items) | 156 × 3 | 468 | $0.0516 | $0.0125 | $0.0179 |
| Tier-0 (24 pairs) | 24 × 3 | 72 | $0.0063 | $0.0016 | $0.0053 |
| 4-point robustness (40 subsample) | 40 × 3 | 120 | $0.0142 | $0.0033 | $0.0046 |

**~660 calls; point estimate ≈ $0.117; expected ≈ $0.10–0.20 billed** (v2b came in at the low end of its
estimate). `ABORT_USD = $0.40` coded in `probe.py` (scaled up from v2b's $0.30 for the ~1.5× larger N).
Comfortably under the **$2.50 single-run** prudence flag and the **$5.00/day** cap. The design spends
**$0 this session** (freeze-before-run); the run is a later session. **Cheaper-companion note:** the v2/
rep2 anchored arms already rated Mahowald's *own* quant×temporal items, so a **$0 re-analysis** of that
frozen raw is a legitimate first look at Arm 1's per-modifier decomposition; the forward probe still
runs, to (a) supply the genuinely-new widened Arm 2 and (b) put both arms on one comparable occasion (a
second date for the anchored cell).

## 8. Gates carried to the freeze/run session

Per PROTOCOL §A3 / §2 (decorrelation) and §5:

1. **Freeze:** `prep.py` builds and freezes `stimuli.json` (modifier list, K, reference set, seed, Zipf
   audit, per-modifier human-mean inclusion threshold, subtype labels — all before any call); `PREREG`
   committed with the §6 statistics and thresholds; `analyze.py` written and self-tested; `probe.py`
   refuses to run before `PREREG` + `analyze.py` exist (v2b guards, inherited).
2. **Freeze-stage independent pre-run critic** (a fresh agent, not the design author) returns GO/NO-GO,
   **plus one non-Anthropic decorrelation vote** (`panel.B`/`panel.C`, cutoff-aware preamble) as QA input
   — divergence weighed in writing; if the call fails or budget bars it, record and proceed.
3. **Run** the panel via `experiments/lib/openrouter.py` (`usage: include`), billed-cost logged,
   missing-cost counted, `$0.40` abort.
4. **Post-run recompute-from-raw verifier** (independent) reproduces every figure before any wiki edit.
5. **Ledger + predictions:** actual billed recorded in [`config/budget.md`](../../config/budget.md); the
   class-vs-lexical bet gets a `wiki/predictions.md` row at freeze, scored the run session.

## 9. What this design does not do

No new construction, no inferential arm, no re-litigation of the v2b instrument, no change to the AANN
gradient claim's overall verdict, and **no invented human rating** — Arm 2's widened items make no human
claim. It sharpens exactly one cell: the quant×temporal inversion, decomposed into class vs item. It is
`model-internal` graded behavior set against a human gradient (Arm 1) plus a within-model contrast (Arm
2); it does not touch the relational axis. **Contingent on**
[`decisions/open/aann-quant-temporal-inversion-design`](../../wiki/decisions/open/aann-quant-temporal-inversion-design.md);
nothing is truly frozen until it ratifies.

## Design-review record (s188 — GO-WITH-CONDITIONS)

Two decorrelated design-stage reviews (PROTOCOL §A3); full detail in
`experiments/runs/2026-07-06-aann-quant-temporal-inversion/REVIEW-design-s188.md`.

- **Fresh-agent pre-run critic (authoritative): GO-WITH-CONDITIONS** — "one freeze-pass away from being
  genuinely informative." **No fabrication:** every cited figure verified against source (model means
  43.0/30.05/68.75; human quant mean 8.4508 n=193; framing ρ; Tier-0 3/3; the quant-drop flip).
- **Non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`, QA): NO-GO** ($0.00304875), **convergent** in
  substance (verdict-map precedence, Q2 threshold, B_m definition, arm firewall, subtype clause). Higher
  severity weighed; handled as the freeze conditions below, not design-landing blockers.

**PREREG blockers (fix before the freeze/run session):** **B1** every modifier gets an identical
noun×numeral×template frame (or balanced Latin square), asserted per-modifier — 6 items cannot balance 5
nouns and per-noun ρ differs in sign, so an unbalanced noun-mix would corrupt `p_m`. **B2** freeze
NULL-vs-CLASS/LEXICAL precedence (evaluate NULL on the cell mean first; else CLASS/LEXICAL/MIXED on `p_m`).

**SHOULD-FIX (freeze; S1–S2 at the data-reclone step):** S1 gate Arm 1's per-modifier human leg on a
reclone + per-modifier rating-N check (`adjexp_turk.csv` is gitignored; only class means are committed — if
N is thin Arm 1 degrades to the class-level comparison, weakening Q1-C's premise, and that must be said);
S2 use what Mahowald's humans actually saw ("tourist" vs the v2b "tourish" typo) on anchored items + make
the exclusion recompute gate-bearing; S3 relabel "item-matched" as a per-modifier gradient comparison
unless items are restricted; S4 define inversion as `A_m(j) < min(non-quant class means)`, not the pooled
mean; S5 freeze K to an exact integer and tie the drop-count to ⌈Y·K⌉; S6 make subtype either a thresholded
verdict bucket or purely descriptive (not both); S7 report the genuinely-new Arm-2 subset separately +
document each modifier's source + justify/reverse the large-magnitude v2b drop; S8 enumerate the exact K=20
with a closed documented source per modifier; S9 wire a per-modifier Zipf partial. **NITs:** N1 Q3-A is a
structural four-class reproduction on a new occasion, not the same cells; N2 sourcing-consistency of the
framing-ρ figures. These conditions are recorded on the open decision as ratification inputs.
