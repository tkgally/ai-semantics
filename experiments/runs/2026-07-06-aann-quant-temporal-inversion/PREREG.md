# PREREG — AANN quant×temporal inversion (class-vs-lexical widening probe), session 189

**Frozen 2026-07-06 (s189) before any model call.** Operationalizes
[`open-question/aann-quant-temporal-inversion`](../../../wiki/findings/open-questions/aann-quant-temporal-inversion.md)
per [`design/aann-quant-temporal-inversion-v1`](../../designs/aann-quant-temporal-inversion-v1.md) and
the ratified decision
[`resolved/aann-quant-temporal-inversion-design`](../../../wiki/decisions/resolved/aann-quant-temporal-inversion-design.md)
(s189 ADOPT-WITH-CHANGES: **Q1-C human-N-gated / Q2-B monotone-primary / Q3-A**). No model call until
this file, `prep.py`, `analyze.py`, and `stimuli.json` are committed and the freeze-stage pre-run critic
(+ one non-Anthropic vote) returns GO.

## The question

Is the one panel-wide AANN model-vs-human inversion cell — **quantity adjectives × temporal nouns**
("a scant three days": humans rate acceptability **highest** of four adjective classes, every panel
model **lowest** — [`result/aann-temporal-why-reanalysis`](../../../wiki/findings/results/aann-temporal-why-reanalysis.md),
H4) — the **whole quantity-adjective class** or **a few lexical items**? Widen the quantity-modifier set
(K=20) and the temporal frame; read how the per-modifier margin below the non-quant baseline is
distributed. **The NULL is first-class:** if the widened quant cell is no longer lowest of the four
classes, the located inversion was an artifact of the thin v2b held-out quant sample.

## Instrument (byte-frozen calling code) + new analysis (self-tested)

`probe.py` is **byte-identical to `../2026-06-13-aann-temporal-heldout-v2b/probe.py` except one line**
(`ABORT_USD` 0.30 → 0.60, for the ~1.5× larger N; `diff` = exactly that line). The prompts (`P100`
0–100 acceptability, `P4` 4-point framing, `PT0` Tier-0 forced choice), the parsing (`parse_int`
last-in-range token; `parse_ab_last`), the per-slot settings (temperature 0; `max_tokens` 64 A/B, 512 C;
`google/*` reasoning effort minimal), the one-retry-then-missing rule, and the `PREREG`+`analyze.py`
run-guards are all unchanged. *(The inherited header docstring's counts ["432 calls", "80 items"] describe
v2b, not this run; the instrument functions are what is frozen, not the comment. This run's counts are
below.)* `analyze.py` is **new code** (the §6 verdict logic) and is **self-tested** (`analyze.py
--selftest` proves CLASS/LEXICAL/MIXED/NULL all reachable + the panel rule) — this is where anti-cheat
scrutiny belongs (design S10).

Tier-0 (manipulation check) and the 4-point framing arm are **re-run fresh this occasion**, byte-
identical, per v2b discipline (not inherited across occasions).

## Item set (`stimuli.json`, built by `prep.py`, no model calls) — 260 main items

**Quant arm — K=20 modifiers × 10 items = 200.** Every modifier gets the **identical** balanced frame
(**B1**): 5 temporal nouns (days, hours, months, weeks, years) × 2 numerals (three, five) = 10 cells;
template = cell_index % 3. Per-modifier: exactly 2 items/noun, 5 items/numeral, template multiset
{4,3,3} — asserted mechanically, so no noun-mix confound corrupts the per-modifier read. The exact K=20,
each with documented source + quantity-polarity (**S8**):

- **Arm 1 (Mahowald-attested `quant`, anchored — human temporal means available):** mere(s),
  staggering(l), whopping(l), hefty(l), paltry(s), meager(s), extra(l), measly(s), substantial(l),
  record-setting(l). *(source: Mahowald 2023 Table 1 `quant` class.)*
- **Arm 2a (genuinely-new — neither Mahowald nor v2b held-out):** good(l), full(l), whole(l),
  solid(l), bare(s). *(source: OQ/handoff widening targets.)*
- **Arm 2b (v2b held-out quant carryover; retains large-magnitude per S7):** scant(s), skimpy(s),
  ample(l), towering(l), colossal(l). *(source: v2b held-out quant.)*

`(s)`=small/diminishing, `(l)`=large/augmentative. Polarity is **descriptive-only** (**S6**), never a
verdict bucket.

**Non-quant reference arm — 4 adjectives × 3 classes × 5 items = 60** (**Q3-A**), rated the **same
occasion** to define each model's non-quant temporal class means. ambig: astonishing, impressive,
remarkable, surprising; pos: beautiful, charming, lovely, soothing; neg: disgusting, hideous, ugly,
uninviting *(committed-v2 temporal class labels)*. **N1:** this is a **structural** four-class
reproduction on a new occasion (~4 adjectives/class), not the committed full-class cells.

**Tier-0** = 24 v2 forced-choice pairs verbatim; **4-point robustness** = 40 items (2 template-spread
quant items/modifier, cells 0 & 5). **972 calls total** (324/model × 3).

## Frozen scoring + verdict (Q2-B monotone primary; NULL-first; MIN baseline)

For quant modifier *j* and **Tier-0-passing** model *m*: `A_m(j)` = mean 0–100 over *j*'s 10 items;
`B_m^min = min` over {ambig, pos, neg} of the model's non-quant temporal **class** mean (**S4** — MIN,
not the pooled mean); `d_m(j) = A_m(j) − B_m^min`.

- **B2 precedence — NULL first.** If the pooled quant-cell mean is **not** the lowest of the four
  adjective-class cells (quant/ambig/pos/neg) for the model → **NULL** for that model, regardless of the
  d-distribution.
- Otherwise read the **shape of {d_m(j)}**:
  - **CLASS** iff `median(d) < 0` **and** `Q3(d) ≤ 0` (wholesale below the lowest non-quant baseline).
  - **LEXICAL** iff `median(d) ≥ 0` **and** pooled quant-cell mean `< B_m^min` (inversion tail-carried).
  - **MIXED** otherwise.
- **Panel verdict** = the category holding for **≥ 2/3 Tier-0-passing models** (else SPLIT).

The cut is **zero = the finding's own baseline**; nothing is tuned. The **0.70/0.30 inversion count +
bottom-drop are computed but descriptive-secondary only** (never verdict-bearing).

**Anchored Arm 1 (human comparison, per-modifier gradient — NOT item-matched, S3).** Over the 10
Mahowald quant modifiers (human-N gate **S1 passed: all 10 clear N≥10; N 11–24, total 193**), report
per-modifier model-low(`A_m(j)<B_m^min`)/human-high(`H(j)>` human min non-quant class mean = **neg
7.5673**) sign, and Spearman(`A_m(j)`, `H(j)`) — flagged noisy (human means over 11–24 singly-rated
items). Anchors → [`resource/mahowald-2023-aann-stimuli`](../../../wiki/base/resources/mahowald-2023-aann-stimuli.md).

**Descriptive-secondary (no gates):** the genuinely-new Arm-2a subset shape reported **separately**
(**S7** — a CLASS verdict must survive {good, full, whole, solid, bare}); the small-vs-large polarity
median-d; the per-modifier Zipf rank-correlation (**S9** — the ±0.5 class-median Zipf *match* is
deliberately **not** enforced on the widened set, which would exclude the natural high-frequency quantity
modifiers good 6.12 / full 5.54 / whole 5.46 the class-vs-lexical test needs; frequency is controlled by
the reported partial, not by exclusion); the **tourish-template-2 exclusion recompute** (**S2** —
**primary = the full set with tourish** [faithful to what Mahowald's raters saw]; the without-template-2
recompute is a **required sensitivity view**, and if it disagrees with the primary the result reports the
split and treats the finding as template-sensitive rather than silently adopting the nicer verdict); the
four-class structural reproduction (N1); bootstrap 95% CIs (10,000 resamples).

**S2 freeze finding (reverses the reviewer's assumed direction):** the "tourish" typo is in Mahowald's
**own** stimuli (`generate_sentence_templates/templates_adj.csv`, `aann-sents/aann_sentences.txt`), so
his MTurk raters saw "tourish" — faithfulness **keeps** it (as v2b did), and the exclusion recompute is
the robustness check.

## Registered bet (→ `wiki/predictions.md`, scored this session)

**The prior:** the re-analysis called the inversion a "clean, localized, panel-wide" effect that "recurs
across the inventory" with per-noun structure. The **pre-registered directional bet:** the widened quant
cell **stays lowest of the four classes for ≥ 2/3 models** (i.e. **not NULL**), and the per-modifier
distribution is **CLASS or MIXED rather than LEXICAL** — the inversion is not carried by scant/mere alone.
A NULL, or a LEXICAL read, is a genuine loss and is written as such. Confidence is **modest** — the
widened Arm 2 includes high-acceptability quantity modifiers (good/full/whole/solid) that may **not**
invert, which would pull toward LEXICAL or MIXED.

## Cost pre-flight

972 calls. Using v2b's measured per-call billed rates by arm (main 0–100: A ~$0.00033, B ~$0.00008,
C ~$0.000115; Tier-0: A ~$0.00026, B ~$0.00007, C ~$0.00022; 4-pt: A ~$0.00036, B ~$0.00008, C
~$0.00011): main 260×3 ≈ $0.137; Tier-0 72 ≈ $0.013; 4-pt 120 ≈ $0.022 → **point estimate ≈ $0.17;
expected $0.15–0.30 billed**. `ABORT_USD = $0.60`. Under the $2.50 single-run flag and the $5.00/day cap
(UTC 2026-07-06 prior spend ≈ $0.4799; ~$4.52 headroom, less this session's ratification vote $0.00233).

## Gates to the run/verify (unchanged discipline)

Freeze-stage pre-run critic (fresh agent) GO/NO-GO + one non-Anthropic decorrelation vote → run
(`python3 probe.py`, 3× parallel per-model) → post-run recompute-from-raw verifier (independent) → a
`result` page (Arm 1 `anchors:` → Mahowald; Arm 2 internal-contrast) refining the re-analysis and bearing
on [`claim/aann-behavioral-gradient`](../../../wiki/findings/claims/aann-behavioral-gradient.md).
