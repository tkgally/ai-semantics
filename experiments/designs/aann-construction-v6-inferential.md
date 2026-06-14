# Design — AANN inferential v6: POWERED PANEL REPLICATION of v4 (fresh held-out adjectives, wider N)

**STATUS: design draft, frozen with `PREREG-draft.md` → `PREREG.md` after a fresh
independent pre-run critic GO.** No new decision is opened: v6 runs entirely under
the already-ratified AANN inferential instruments
([`decisions/resolved/aann-inferential-operationalization`](../../wiki/decisions/resolved/aann-inferential-operationalization.md)
+ [`decisions/resolved/aann-inferential-default-coincidence`](../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)),
with the result fixed at **`anchor: internal-contrast-only`** scored against an
explicitly **expert-stipulated** literature key. This is a *replication*, not a new
instrument, so the ratified yardstick already governs it.

## 1. Why v6 exists (the question)

v4 ([`result/aann-inferential-v4`](../../wiki/findings/results/aann-inferential-v4.md))
returned **PARTIAL**: against a distributive-default control (DDC), all three panel
models shifted paraphrase selection toward the unification reading (double-contrast
Δ² = +0.78 / +0.70 / +0.96, net of the lexical cue), but the shift converged across
instruments (paraphrase **+** NLI **+** the grammaticalized singular-agreement reflex)
in **only one model, gpt-5.4-mini** (CONVERGENT-POSITIVE); claude-sonnet-4.6 and
gemini-3.5-flash were PARAPHRASE-ONLY. v4's own binding bounds named the weakness:
**"small N (23 base items), single run, single panel, single date — direction-of-effect,
not magnitude."**

v6 attacks exactly that bound. Two pre-registered questions:

1. **Does the panel-wide paraphrase double-contrast shift hold up when powered?**
   (≥2 of 3 models reach Δ² positivity on a fresh, larger, held-out item set.)
2. **Does gpt-5.4-mini's cross-instrument convergence (paraphrase + NLI + agreement)
   replicate** on fresh held-out adjectives — or was it a small-N / single-date
   artifact?

It is a **clean replication**: the instrument, the parsing, the four arms, the
thresholds, the headroom gate, the verdict map, and the analysis code are **identical
to v4** (`analyze.py` is byte-identical save run name, design path, and the frozen
bootstrap seed). The **only** change is the item set.

## 2. The single change from v4 — the item set

| | v4 | v6 |
|---|---|---|
| Base items | 23 (temporal 13 / distance 10) | **40 (temporal 20 / distance 20)** |
| Adjectives | 21 | **40, all fresh** (disjoint from v4's 21 **and** the agreement-reflex-v5 probe's 30) |
| Calls | 831 (277/model × 3) | **1392 (464/model × 3)** |
| Disputed-key items | 1 (yards edge) | 1 (yards edge — `freezing forty yards`) |

- **Wider N + rebalanced classes.** N nearly doubles (23 → 40), and the distance
  class doubles (10 → 20) so per-class power is symmetric — v4's distance stratum
  carried the largest paraphrase shifts and the smallest N.
- **Fresh held-out adjectives.** All 40 are consonant-initial (so the AANN article
  "a" reads naturally, as in v4) and **disjoint** from every adjective used in the
  AANN inferential line so far (v4 + the v5 reflex probe), asserted mechanically in
  `prep.py`. So a positive here is the construction **generalizing** to a fresh,
  larger adjective inventory — not a re-measurement of the same items.
- The object/mass noun class **stays dropped** (as in v3/v4).

Everything else is v4 verbatim: the three premise frames (AANN / DDC / LCC), the
paraphrase options (U/D), the NLI hypotheses (unification + whole-evaluation), the
agreement (was/were) sub-probe against the **bare-plural** control (Condition N4),
the Tier-0 manipulation check, the seeded A/B counterbalancing, temperature 0, the
per-model token caps, and the parsing rules.

## 3. Binding conditions — re-confirmed for the v6 item set

v6 inherits **all fourteen** binding conditions (six from the default-coincidence
decision, eight from the operationalization decision). Because the instrument and
analysis are unchanged, the only conditions that need re-confirmation are the ones
that touch the **stimuli**. Each is re-asserted in `prep.py`:

- **N1 (headroom precondition).** The DDC ("On each of the {num} {noun} {pp}, it was
  {adj}.") is the genuinely-distributive baseline frame; the headroom gate
  (P(uni|DDC) ≤ 0.30 PASS) is read **pre-headline**, per model, exactly as v4. v6
  does not assume v4's headroom held — it is re-checked on the new items, and a
  whole-design HEADROOM-FAIL (< 2 models clear) routes to the Option-B named null,
  identical to v4.
- **N2 (construction-isolating LCC).** Every item carries the LCC ("On each of the
  {num} {adj} {noun} {pp}, {verb}.") with the **same** itemizing cue as the DDC, the
  adjective attributive, and **no AANN span** — asserted in `prep.py`
  (`aann_span not in lcc`, `"{adj} {noun}" in lcc`, both start with "on each of the
  {num} "). The headline is the double contrast Δ² = P(uni|AANN) − P(uni|LCC).
- **N3 (lexical parity).** Paraphrase-option (U/D) lexical-overlap parity against the
  AANN premise is asserted equal for all 40 items; per-item `control_lexical_delta`
  (DDC vs AANN) is recorded (min 1 / max 2 / mean 1.0).
- **N4 (agreement control = bare plural).** Unchanged — the agreement arm contrasts
  AANN vs the **bare-plural** control, never the DDC.
- **N5 / I5 / I6 (expert-stipulated key; disputed flag).** The unification reading is
  the AANN-licensed answer, **expert-stipulated** (the same Solt 2007 / Dalrymple &
  King 2019 / Bylinina & Nouwen 2018 coding as v4; named, not quoted, not in-repo —
  no fabricated quotes). One item (`freezing forty yards`) carries the `key_disputed`
  flag (yards at the edge of Mahowald's distance inventory), so the I6
  disputed-sensitivity recomputation runs live.
- **I4 (under-pressure subset).** 22 items have the distributive paraphrase as the
  locally-fluent continuation (`local_fluency = "distributive"`); their Δ² is
  analysed separately. World-knowledge-forces-unification items were excluded at
  authoring.
- **I7 (named disagreement statistic).** |FC Δ² − NLI Δ²| is reported per model and
  fed to [`open-question/instrument-sensitivity-constructional-inference`](../../wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md),
  flagged ≥ 0.30, never averaged away.
- **I8 (freeze discipline).** Stimuli, `probe.py`, and `analyze.py` are all committed
  **before** any model call; `probe.py` refuses to run without a frozen `PREREG.md`
  and without `analyze.py` present; `analyze.py --selftest` passes (38 checks) at
  freeze.

## 4. Arms, indicator, thresholds, verdict map — identical to v4

See [`design/aann-construction-v4-inferential`](aann-construction-v4-inferential.md)
§3–§6 for the full specification; v6 reuses it unchanged. In brief:

- **Indicator (PRIMARY):** paraphrase double contrast **Δ² = P(uni|AANN) − P(uni|LCC)**;
  "positive" = Δ² ≥ **τ = 0.20** (inclusive) **and** item-level bootstrap 95% CI
  lower bound > 0 (strict), 10,000 resamples, seed **20260614**.
- **Convergent (NLI):** affirm-rate Δ² over the unification + whole-evaluation
  hypotheses (the **both-hypothesis** aggregation v4's post-run verifier fixed to
  spec — carried forward correctly here from the start).
- **Discriminator (load-bearing):** singular-agreement shift P(was|AANN) − P(was|bare
  plural); same τ + bootstrap.
- **Headroom gate (Condition N1):** PASS ≤ 0.30 / MARGINAL ≤ 0.50 / HEADROOM-FAIL >
  0.50, per model, pre-headline; whole-design gate needs ≥ 2 clearers or → Option-B.
- **Tier-0 gate:** ≥ 20/24 AANN-preferred per model; < 2 passers → INSTRUMENT FAILURE.
- **Verdict map:** per-model CONVERGENT-POSITIVE / PARAPHRASE-ONLY /
  PARAPHRASE-PLUS-REFLEX-NO-NLI / LEXICAL-CUE ARTIFACT / NULL; stratum SUPPORTED
  (≥ 2 CONVERGENT-POSITIVE) / PARTIAL (≥ 2 paraphrase-positive, < 2 convergent) /
  LEXICAL-CUE ARTIFACT / NULL / HEADROOM-FAIL → Option-B / INSTRUMENT FAILURE.

**Pre-registered replication expectation (direction only, no magnitude claim):**
if v4 was real, v6 should return **PARTIAL or SUPPORTED** (≥ 2 models paraphrase-
positive) and gpt-5.4-mini should again be **CONVERGENT-POSITIVE**. A drop to NULL,
a LEXICAL-CUE ARTIFACT verdict, or gpt failing to replicate would each be a
first-class result that **weakens** the v4 reading — and is reported as such.

## 5. Anchor discipline (Condition N5/I5)

**`anchor: internal-contrast-only`** — within-model double contrast; **no
human-comparison claim**. Chief-cost statement (verbatim, binding on the result
page): *the v6 can never say "models draw the inference the way humans do" — only
that the construction shifts inferential behaviour relative to a matched control, in
the direction the published semantics predicts.* The expected-inference key is
expert-stipulated, labelled as such everywhere. Mahowald is cited only as measure-noun
class provenance, never as an inference anchor.

## 6. Spend — pre-flight estimate (Condition I8)

1392 calls (464/model × 3). v4 billed **$0.1266 for 831 calls** = **$0.0001524
per call** (billed `usage.cost`, the rate-card undercount already absorbed). At the
same per-call shape, **1392 × $0.0001524 ≈ $0.212** (point estimate); with the one
verbatim retry per unparseable response and variance, **expected ≈ $0.20–0.35
billed**. Well under $1, well under the **$5.00/day UTC** cap
([`config/budget.md`](../../config/budget.md); day total before this run ≈ $0.974).
Single-run **ABORT_USD = $0.75** coded in `probe.py`. Actual billed `usage.cost`
recorded in `raw/cost-log.txt` and the run record after the post-critic run; calls
with missing `usage.cost` are counted and logged, never silently discarded.

## 7. Files

- `experiments/runs/2026-06-14-aann-inferential-v6/prep.py` — stimulus authoring (40
  fresh items; the held-out-adjective + three-frame + parity asserts). No model calls.
- `.../stimuli.json` — frozen materials (seed 20260614).
- `.../probe.py` — panel calls; logic byte-identical to v4; refuses to run without a
  frozen `PREREG.md` + `analyze.py`.
- `.../analyze.py` — frozen analysis; byte-identical to v4 save run name/design
  path/seed; `--selftest` passes (38 checks).
- `.../PREREG-draft.md` → `PREREG.md` (frozen after the fresh pre-run critic GO).
