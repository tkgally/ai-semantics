# PREREG — modal second-instrument forced-choice probe (session 72, 2026-06-21)

**Frozen pre-registration.** Fires revision trigger **(c)** of
[`essay/function-words-not-one-category`](../../../wiki/findings/essays/function-words-not-one-category.md):
"a second inferential instrument … the single most decisive trigger." Result is
`internal-contrast-only` (within-model cross-instrument contrast; no human comparison).

## Stimuli freeze

- `stimuli.json` **file** sha256: `a1eb83a8a9f93789ef347a7b08804e567ef0060baf1aa839f7ce0c1377393e40`
- `stimuli.json` **canonical** sha256: `a12b2da0e84b37d9e54c098bec09672886876aa7e851f92d9f78c0ef7e0dc5c8`
- Source (frozen, certified): `2026-06-21-modal-arm-widening/stimuli.json` (file sha16 `cccac581…`,
  canonical sha16 `fb605ed9…`). The will/shall/must **matched** items are reused **verbatim**
  (same sentences, same content controls); only the indicator changes. The frequency/length
  matching is therefore **inherited** (certified in that run) and not re-derived here.
- `certify.py` → `certification.json` `"ok": true` (per-arm n≥15; hedge-position balance ≤1;
  0 modal-lemma leaks in options; 58/58 base–fn single-modal-token diff; 58/58 base–ct same-modal).

## The question

The session-71 NLI run left `will`→`would` near-null (claude 0/20, gpt 0/20, gemini 3/20). Two
readings remain: the **instrument** (3-way NLI) is insensitive to the future→conditional shift, or
the **relation** is genuinely inferentially inert. This probe holds the modal swap **fixed** and
changes the **indicator** to decide between them.

## Indicator (the second instrument)

Single-letter **forced choice** (A/B) between a **STRONG** modal-force paraphrase and a **HEDGE**
one, per arm:

| arm | STRONG (base modal's force) | HEDGE (swapped modal's force) |
|-----|------|------|
| `will`→`would` | "definitely happens or is the case" | "conditional or hypothetical — happening only if certain circumstances hold" |
| `shall`→`should` | "strictly required or mandatory" | "advisable or recommended, but not strictly required" |
| `must`→`might` | "required or certain to occur" | "merely possible or optional — not required and not certain" |

Option strings contain **no modal lemma** (no will/would/shall/should/must/might), so a
modal-blind reader has no surface cue. HEDGE position (A or B) is **counterbalanced ~50/50**
within each arm and **fixed within an item** across base/fn/ct, so a fixed-letter (position-bias)
reader contributes ~0 to the within-item base→fn shift.

**SAME single-token output channel as NLI** (one letter, no working surface): this controls the
output-channel confound the project mapped — any difference from NLI is the *question type*
(graded modal-force preference vs 3-way entailment), not channel width.

Per item × model, 3 calls: `base`, `fn` (modal swapped), `ct` (content swapped, **modal
unchanged**). `picked_hedge ∈ {0,1}` from chosen letter vs `hedge_letter`.

- **PRIMARY (per arm × model):** `mean(shift_fn)` where `shift_fn = picked_hedge(fn) − picked_hedge(base) ∈ {−1,0,1}`.
- **Manipulation check:** `base_strong_pref = mean(1 − picked_hedge(base))` — base should prefer STRONG.
- **Falsify/control:** `mean(shift_ct)` (modal unchanged) predicted ≈ 0; a large `shift_ct` would mean
  the instrument just flips its answer when any word changes (records it, no item re-selection).

## Predictions (registered before the run)

1. **Instrument-validity anchor — `must`→`might`:** `mean(shift_fn)` **strongly positive** in all
   three models (NLI flipped it at ceiling; a sensitive instrument must register it). If even this
   arm nulls, the instrument is insensitive and the `will` null is **uninformative** — reported as such.
2. **Target — `will`→`would`:** the decisive cell. **If `shift_fn` ≈ 0** while `must` is strongly
   positive → the null is **relation-specific**, reproduced across two unrelated instruments
   (strengthens "future→conditional is inferentially inert here"; trigger (c) fires *negative*).
   **If `shift_fn` strongly positive** → the null was **NLI-specific**; the effect **relocates** from
   "type of grammatical relation" to "instrument sensitivity" (vindicates §"A calibrated reading" in
   its strongest form; trigger (c) fires *positive*).
3. **Secondary — `shall`→`should`:** does the NLI panel-split (gemini 0.78 vs claude/gpt 0.06)
   reproduce, dissolve, or invert under a different instrument? (rests on one content pair `buy`→`give`,
   read narrowly.)
4. **Control:** `mean(shift_ct)` ≈ 0 in every arm × model.

No item is re-selected, and no option wording is changed, after any output is seen.

## Governance: no new decision owed (surfaced for the critic to rule on)

The instrument **class** was pre-registered by trigger (c) itself ("a graded paraphrase-preference,
a forced-choice continuation, a scalar-quantity questionnaire") in an **earlier** session
(`essay/function-words-not-one-category`, session 71). Running one is **executing a named plan**, not
opening a methodological fork. The result is `internal-contrast-only` — it makes **no human-anchor
claim** (it is a within-model contrast *between two instruments*), so no `resource` anchor is owed and
no human-comparison decision is at stake. The specific option wordings, the shift measure, and the
counterbalancing are **frozen design choices** subject to this pre-run critic, exactly as the
modal-arm-widening run surfaced its per-arm count-gate relaxation for the critic rather than opening a
decision page. **If the critic judges a `wiki/decisions/open/` entry is owed, this is NO-GO** and the
run defers.

## Pre-flight budget

58 items × 3 conditions × 3 models = **522 finding-bearing calls** + 3 liveness. Single-token A/B is
cheap (NLI run-v2: 1,914 calls = $0.502 → ~$0.00026/call → ~$0.14 here). Estimate **~$0.10–0.25
billed**. `ABORT_USD` = $0.80 (probe.py). UTC-2026-06-21 headroom at session start: $5.00 − $2.747 =
**$2.253**. Record actual billed `usage.cost` after.

## Pipeline

(1) `build.py` → `stimuli.json` (done); (2) `certify.py` → `"ok": true` (done); (3) **independent
fresh-agent pre-run critic** GO/NO-GO; (4) record GO + sha here; (5) `probe.py liveness` then
`probe.py full`; (6) `analyze.py` + **independent fresh-agent post-run verifier**; (7) write the
result page, fire essay trigger (c), update theory.

---

PRE-RUN CRITIC: GO

Independent fresh-agent pre-run critic (2026-06-21, session 72) reproduced the build byte-for-byte
(canonical sha256 `a12b2da0e84b37d9e54c098bec09672886876aa7e851f92d9f78c0ef7e0dc5c8`, file sha256
`a1eb83a8a9f93789ef347a7b08804e567ef0060baf1aa839f7ce0c1377393e40` — both match), re-ran
`certify.py` to `"ok": true`, and returned **GO** with **no BLOCKERs**. It confirmed: (a) no
option-wording cue (length, lexical, position) can manufacture a spurious positive `shift_fn`
because the shift is within-item with identical options at base/fn; (b) the channel is genuinely
matched to the NLI run (both single-token, no working surface), so a divergence is attributable to
question type; (c) **no decision is owed** — the forced-choice indicator is named in the ratified
`decisions/resolved/function-word-anchor-design` Q2(i) ("graded forced-choice rate") AND essay
trigger (c), and the result is `internal-contrast-only`; (d) the freeze guard works and
`internal-contrast-only` is the correct anchor state.

Three SHOULD-FIX disclosures (carried into the result page + post-run verifier brief; not design
changes):
1. **`will`-arm fairness asymmetry.** Standalone `would` is genuinely irrealis out of context and
   the HEDGE option explicitly names "conditional or hypothetical," so this instrument is
   structurally *more* disposed to register `will`→`would` than NLI was. A `will`-positive must be
   reported as "a forced-choice instrument that names the irrealis reading registers the shift,"
   not as "the relation is robustly inferential across instruments."
2. **`base_strong_pref` is a per-arm interpretation gate.** If base does not prefer STRONG in an
   arm, that arm's `shift_fn` is uninterpretable — report it as such, do not read the shift as signal.
3. **`shall` thinness carries over.** All 18 `shall` items rest on the single content pair
   `buy`→`give` (inherited from the source run); the secondary `shall` reading stays narrow.
