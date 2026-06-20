# PRE-REGISTRATION (draft) — let-alone working-surface format probe

**Run:** `2026-06-20-scivetti-let-alone-working-surface`
**Date drafted:** 2026-06-20 (session 58, UTC)
**Status:** DRAFT — must pass a FRESH independent pre-run critic GO, then be committed
as `PREREG.md` before any model call (the probe's freeze guard enforces this).

## 1. Question

Session 57's Scivetti answer-key probe
([`result/scivetti-cxnli-answer-key-v1`](../../../wiki/findings/results/scivetti-cxnli-answer-key-v1.md))
found the phrasal scalar **let-alone** at near-chance for all three panel models
(claude 0.542 / gpt 0.458 / gemini 0.667; 3-way chance ≈ 0.33), while the
argument-structure constructions sat at or near the ≈0.90 human baseline. That probe
used a **forced single-token** NLI channel ("Output a single digit 0, 1, or 2 and
nothing else").

The project's own methodological spine says a forced-format near-chance negative must
have its **output channel** varied before it can be trusted as anything stronger than a
channel-bounded, instrument-relative effect-null:

- [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md):
  a behavioral negative is never a capability-absence; it is a kind-1 effect-null / kind-2
  instrument-uninterpretable result, and "more of the same probe cannot" change its status —
  only a **witness-seeking** probe (an easier/different elicitation) can.
- [`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md):
  names the **output channel** (forced single token vs. a working surface) as the
  privileged, cheap axis to vary before trusting any forced-format negative.
- [`essay/floor-is-not-a-ceiling`](../../../wiki/findings/essays/floor-is-not-a-ceiling.md):
  the relational-composition saga is the direct precedent — a four-instrument near-chance
  "split" (gpt DIRECT 0.156, gemini 0.656) **dissolved** into panel-concordance the moment
  a working surface was permitted (gpt→0.969, gemini→1.000), reasoning-effort held constant.

**So:** is let-alone's near-chance a robust difficulty, or an artifact of the forced
single-token channel? This is the high-value witness-seeking probe the essays prescribe.

## 2. Design — format-only, single manipulated variable

The **only** changed variable vs the session-57 baseline is the **response format**:

| | session 57 (baseline) | this run |
|---|---|---|
| output instruction | "Output a single digit 0, 1, or 2 and nothing else." | "Think it through step by step. Then, on the final line, output your answer in exactly this format: `FINAL: <0, 1, or 2>`" |

Everything else is **held byte-identical** to session 57:

- **Items:** the SAME 24 let-alone + 30 comparative-correlative test items (subset
  sha256 `9be31a8fea8d7f16`; full-set sha `1c5cffb18c5ef78e` == session 57's, verified by
  `prep.py --check` — same corpus, re-cloned upstream @ `82699473`). Gold NOT shown.
- **0/1/2 label definitions:** the three definition lines of the system prompt are
  **copied verbatim** from session-57 `NLI_SYS`.
- **Scoring:** 3-way NLI label vs the same per-item gold, vs the ≈0.90 native-speaker
  baseline. (Does NOT change WHAT is scored — only HOW the label is produced.)
- **Panel:** A claude-sonnet-4.6 / B gpt-5.4-mini / C gemini-3.5-flash, temperature 0.
- **Reasoning-effort knob HELD CONSTANT:** gemini stays `effort: minimal` — so the
  contrast isolates the **output channel**, not the reasoning budget (exactly as the
  2026-06-19 working-surface witness re-run did).

**Cells.** let-alone (n=24) — the TARGET; comparative-correlative (n=30) — a CEILING
CONTROL (forced-format 1.0/0.9/1.0 in session 57) that guards against "the working
surface broke the instrument."

## 3. No new operationalization decision owed

This is a **format/instrument extension** under the already-ratified Scivetti answer-key
anchor (ratified 2026-05-29, Tom) and the ratified
`constructional-divergence-operationalization` decision. It does **not** alter what is
scored against the human gold (same labels, same gold) — only how the label is produced.
Precedent: the 2026-06-19 working-surface re-run was logged "format-only ... no new
decision owed." The pre-run critic must confirm this judgement. `wiki/decisions/open/` is
empty; nothing to ratify.

## 4. Pre-registered analysis & verdict map (frozen in `analyze.py`)

**Q1 — anchored leg (per-construction accuracy under the working surface).**
Per model, per construction: accuracy + Wilson 95% CI vs human 0.90.
comparative-correlative carries the **ratified anchor**; let-alone is **descriptive**
from the same human release (not individually anchored), exactly as session 57.

**Q2 — the headline format contrast (internal-contrast-only).** Within-item paired
comparison vs the session-57 forced-format labels (matched by `item_id`):
- `b` = forced-WRONG → working-surface-RIGHT (gains); `c` = forced-RIGHT → ws-WRONG (losses).
- One-sided exact binomial (sign) test on the `b+c` discordant pairs.
- Per-(model, construction) verdict:
  - **LIFTS** : ws_acc > forced_acc AND P(X≥b | n=b+c, 0.5) < 0.05
  - **DROPS** : ws_acc < forced_acc AND P(X≥c | n=b+c, 0.5) < 0.05
  - **UNCHANGED** : otherwise.
- Control guard (comp-correlative): **PRESERVED** if its ws Wilson CI contains the
  forced-format acc; else FLAG.

**Pre-committed interpretation (no retuning after seeing results):**
- If let-alone **LIFTS** toward the argument-structure/control level in ≥2 of 3 models
  while the control stays PRESERVED → the forced-format near-chance was substantially a
  **channel artifact**; the witness fires; `essay/output-channel-confound` /
  `floor-is-not-a-ceiling` are corroborated; the "scalar-phrasal competence-absence"
  reading is **refuted** (a witness flips a negative to a presence). The session-57
  result page's "let-alone failure is the robust signal" caveat is revised accordingly.
- If let-alone is **UNCHANGED** (stays near-chance) while the control stays PRESERVED →
  the failure **survives** the privileged channel manipulation; it is a more robust
  (kind-1) instrument-relative effect-null, and the scalar-phrasal locus becomes the
  first real candidate for a content-type difficulty on the constructional ladder — but
  still **not** a capability-absence (undischargeable-negative discipline: the next
  witness axis would be few-shot / a different framing / the train-split items).
- If the control **FLAGs** (degrades) → the instrument changed too much to read the
  target cleanly; report as instrument-uninterpretable, no target verdict.

n is small (let-alone n=24); the paired design removes between-item variance, so a large
channel effect (cf. the relational saga's 0.156→0.969) is detectable, but a small one may
not be — this is stated as a power bound, not retuned away.

## 5. Cost & integrity

- Pre-flight estimate: **~$0.15–0.35** billed (54 items × 3 models = 162 calls + 3
  liveness; working-surface CoT makes claude the cost driver, as in the dative/witness
  runs). `ABORT_USD = 0.80`; far under the $2.50 single-run flag and the daily cap.
- Budget context: UTC-day 2026-06-20 spend before this run = $3.475 (temp $10 cap through
  15:00 UTC; standard $5 thereafter). Even at the standard $5 cap the headroom ($1.525)
  covers this run.
- Integrity: `usage.cost`-summed (0-missing target); parse modes logged (tagged vs
  fallback); unparseable never dropped silently. **Recipe-not-corpus:** the working-surface
  CoT restates the unlicensed source text, so full CoT is **gitignored** under `raw/cot/`;
  the committed artifact is `raw/{slot}-labels.json` (item_id + gold + label + parse_mode +
  content sha256 + usage, NO text).
- Cadence: this draft → FRESH independent pre-run critic GO → commit as `PREREG.md` →
  probe (background) → FRESH independent post-run verifier REPRODUCES from raw → result page.
