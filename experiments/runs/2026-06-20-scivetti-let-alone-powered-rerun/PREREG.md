# PRE-REGISTRATION (FROZEN) — POWERED let-alone forced-decomposition re-run (trigger-(g))

> **FROZEN 2026-06-20 (UTC, JST June 21).** A FRESH independent pre-run critic returned
> **GO** (all 9 adversarial checks PASS; no blocking issues): instrument byte-identical to
> session 60 (both 909 chars); disjointness independently re-verified (0 shared
> premise/hypothesis pairs, 0 shared premises, 3 distinct source sentences; the 1-example
> train split a strict subset, so **33 is the ceiling** of available human-annotated
> let-alone N); all four shas re-asserted by `prep.py --check`; no gold/answer leak, no
> demonstration items, scaffold answer-blind; no new decision owed (`wiki/decisions/open/`
> empty); the partial-witness exemption legitimately invoked (session 60 left a directional
> +0.21, not a null); verdict map exhaustive (16/16 inputs, METHOD-NULL reachable) and not
> gerrymandered; budget $0.39 of $0.875 headroom, abort guard cumulative + working; honesty
> constraints bind. Two non-blocking notes (a benign STAYS-PARTIAL label on the unlikely
> gpt-exceeds-baseline case; coarse abort granularity) — neither affects this run's
> reachable outcomes; the frozen+GO'd code is left untouched. The draft below is the frozen
> pre-registration.

## 1. Question

Session 60
([`result/scivetti-let-alone-forced-decomposition-v1`](../../../wiki/findings/results/scivetti-let-alone-forced-decomposition-v1.md))
forced uptake of a working surface on the phrasal-scalar **let-alone** NLI items and found a
**partial witness**: gpt-5.4-mini genuinely took up the channel (median completion tokens
8 → 120, 24/24 items worked) and its let-alone accuracy rose to **0.583** (+0.21 over the
session-58 *offered* surface) — but the lift was **underpowered** (within-item sign test
p = 0.090, n = 24, 9 discordant pairs → verdict UNCHANGED) and it **stayed below** the
≈0.90 human baseline (Wilson CI [0.388, 0.755], hi < 0.90), where claude (0.833) and gemini
(0.875) sit. So part of gpt's let-alone gap is channel-bounded and part **survives a
genuinely-exercised wide channel** — the closest the record has come to
[`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md)
**trigger (b)** (a serial negative surviving a widened channel), but at n = 24 a
**candidate, not a clean firing**.

[`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md)
§"The partial witness" names the correct continuation: a **powered re-run of the same
axis** (more items), **exempt** from the parent essays' "more of the same probe cannot"
caution **because** session 60 left a directional *signal*, not a null — powering a signal
resolves *power*, not the existence question a clean non-witness already answers.

**So:** with the forced-decomposition instrument **held byte-identical** and the let-alone
target **enlarged** with the only additional human-annotated let-alone items in the upstream
release (the disjoint TRAIN split), does gpt's below-baseline residual **HOLD** at higher
power (a cleaner trigger-(b) channel-controlled residual), **DISSOLVE** to baseline (an
output-channel artifact after all), or **STAY PARTIAL** (a power bound at the ceiling of
available human-anchored items)?

## 2. Design — same instrument, enlarged item set (the powered axis)

The **only** changed variable vs session 60 is the **item set**: the let-alone target grows
**24 → 33** (24 test + 9 **disjoint** train items). The forced-decomposition response format
is held **byte-identical** (`probe.py`'s `NLI_SYS_DECOMP` is copied verbatim from session
60; programmatically diff-checked equal).

| | session 60 (forced-decomp, 24 LA test) | this run (forced-decomp, 33 LA = 24 test + 9 train) |
|---|---|---|
| instrument | 3-step decomposition scaffold, `FINAL:` tag | **identical** (byte-for-byte) |
| let-alone items | 24 test (8/8/8) | 24 test + **9 train** (3/3/3), combined 33 (11/11/11) |
| control | 30 comp-corr test | **identical** 30 comp-corr test |
| panel / temp / gemini effort | A/B/C, temp 0, gemini minimal | **identical** |

**The 9 train items are DISJOINT from the 24 test items** — 0 shared (premise, hypothesis)
pairs and 0 shared premises (3 distinct source sentences), asserted in `prep.py`
(`assert_structure`). They are the **only** additional let-alone items in the upstream
release (the 1-example train split is a strict subset of these 9), so **33 is the ceiling**
of available human-anchored let-alone N — an honest, stated power bound, not a tunable knob.

**Cross-checks (provenance).** `prep.py` re-asserts the 390-item full-set sha
`1c5cffb18c5ef78e` (== sessions 57/58/60) and the 54-item session-57/58/60 subset sha
`9be31a8fea8d7f16` (24 LA test + 30 CC), so the test corpus and control are provably
identical to the prior runs; the new train items carry their own sha `6b0c8d82536f25e6`.
Frozen run-set sha `1b87dc871e4ec8dd` (63 items).

## 3. No new operationalization decision owed

A **same-instrument power extension** under the already-ratified Scivetti answer-key anchor
(ratified 2026-05-29, Tom) and the ratified
[`decisions/resolved/constructional-divergence-operationalization`](../../../wiki/decisions/resolved/constructional-divergence-operationalization.md).
The instrument, label definitions, gold, panel, temperature, and reasoning-effort knob are
all unchanged from session 60; **what is scored against the human gold is unchanged** —
only the item *count* grows, with NEW items drawn from the **same human-annotated release,
same construction, same balance**. Adding within-construction items from the same anchored
resource is the exact move the partial-witness exemption prescribes (essay/witness-seeking-
economics §"The partial witness"). **No demonstration items** (forced decomposition, not
few-shot) → no scoring/gold leak. `wiki/decisions/open/` is empty; nothing to ratify. The
pre-run critic must confirm this judgement and the disjointness.

## 4. Pre-registered analysis & verdict map (frozen in `analyze.py`)

Human reference (fixed, not retuned): Scivetti Exp-1 native-speaker accuracy ≈ 0.90; 3-way
chance ≈ 0.33. comparative-correlative carries the **ratified anchor**; let-alone is
**descriptive** from the same human-annotated release (not individually anchored), exactly
as sessions 57/58/60.

- **Q1 (headline, vs-baseline residual).** Each model's let-alone accuracy on the combined
  33 items + Wilson 95% CI vs 0.90. Trigger-(g) subject = **gpt-5.4-mini**.
- **Q1b (internal replication + generalization).** Per-split accuracy: test (24) vs train
  (9, disjoint); item-by-item label agreement vs session 60's committed 24-item labels (does
  0.583 reproduce? do the fresh disjoint items agree in direction?).
- **Q2 (ceiling control guard).** comp-correlative (30) accuracy + Wilson CI; **PRESERVED**
  iff Wilson LB ≥ 0.80 (near ceiling).
- **Q3 (uptake manipulation check).** let-alone fraction "worked" (≥ 40 pre-`FINAL` chars
  AND ≥ 2 numbered step markers) + completion-token median. **Uptake induced** iff ≥ 80%
  worked. If NOT induced → the channel question is not cleanly posed (METHOD-NULL).

**Verdict map (gpt-5.4-mini let-alone, combined n = 33), frozen:**

| condition | verdict | reading |
|---|---|---|
| uptake induced ∧ control PRESERVED ∧ **CI hi < 0.90** | **CONFIRMS-RESIDUAL** | below-baseline channel-controlled residual HOLDS at higher power → a *cleaner* trigger-(b) case (descriptive + contamination-caveated, **not** "cannot") |
| uptake induced ∧ control PRESERVED ∧ **CI covers 0.90, point ≥ 0.90** | **DISSOLVES** | residual was a small-N artifact → output-channel-artifact reading (like claude/gemini) |
| uptake induced ∧ control PRESERVED ∧ **point < 0.90 but CI hi ≥ 0.90** | **STAYS-PARTIAL** | power bound at the ceiling of available human-anchored items (33); redirect axis |
| uptake NOT induced (< 80% worked) ∨ control BROKEN | **METHOD-NULL** | channel question not cleanly posed this run |

claude/gemini are the **manipulation check**: each EXPECTED at/covering baseline (a benign,
non-degrading scaffold) with control PRESERVED; a DROP in either would flag the larger item
set as having broken the instrument.

**Honesty constraints (binding).** (i) "cannot" is forbidden (undischargeable-negative);
the strongest license is a *candidate/cleaner* channel-controlled residual. (ii) let-alone
items are public → a *match* cannot distinguish learned construction-meaning from memory;
the robust signals are the **uptake jump** and **within-model contrasts**, the absolute
0.90 match inherits the contamination caveat. (iii) the vs-baseline leg is what this run
powers; the session-60 **vs-offered paired** leg is NOT powered here (the 9 new items have
no offered-surface arm) — stated as a limit, not smuggled.

## 5. Cost & stop rule

189 finding-bearing calls (63 × 3) + a small liveness ping. Pre-flight from session 60's
**measured** $0.3342 / 162 calls → ≈ **$0.39** (189/162 scale; claude the CoT driver).
`ABORT_USD = 0.80` per-run flag (under the $2.50 single-run flag). UTC-day 2026-06-20 spend
before this run = **$4.125**; headroom ≈ $0.875 → this run fits with margin. If the abort
trips, partials are written and the run is reported as aborted (no silent completion).

## 6. Integrity commitments

- `prep.py` freezes recipe-only (hashes + counts, NO text); disjointness + balance asserted.
- `probe.py` is the only API caller; freeze guard requires `PREREG.md` + `analyze.py` +
  `prep.py --check` PASS. Records item_id + cxn + split + gold + label + parse_mode + uptake
  (lengths/booleans) + content sha256 + usage. Full CoT → `raw/cot/` (gitignored,
  recipe-not-corpus). Parser **target-blind**; gold NEVER shown.
- A FRESH independent post-run verifier (separate agent) must reproduce every accuracy,
  Wilson CI, the internal-replication agreement, the uptake check, the billed cost, parse
  integrity, the `content_sha256`↔CoT binding, CoT genuineness, and confirm no gold-leak
  path, before the result page is promoted past draft.
