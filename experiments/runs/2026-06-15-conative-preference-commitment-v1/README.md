# 2026-06-15 — conative preference/commitment double contrast (v1)

**What this run is.** A frozen behavioral probe testing whether the AANN
*preference-without-commitment* dissociation generalizes to a fresh divergent-default
construction — the **conative** ("Maria kicked **at** the ball" → contact not
guaranteed). Two instruments on 40 frozen items: a paraphrase forced-choice
(PREFERENCE, the weaker signal) and an NLI entailment check (COMMITMENT, the
load-bearing discriminator). Headline = the **double contrast Δ²** (conative minus a
matched anomalous *at*-string control), net of the bare-*at* lexical cue. Runs under
the ratified `decisions/resolved/fresh-construction-inferential-generalization`
(Option A); operationalizes `conjecture/preference-commitment-generality`.

Full spec: `experiments/designs/conative-preference-commitment-v1.md`.

## Files

| file | role |
|---|---|
| `prep.py` | stimulus authoring (NO API); emits `stimuli.json`, asserts parity/LCC/counterbalancing, prints sha256 |
| `stimuli.json` | the 40 frozen items (seed 20260615) |
| `probe.py` | panel calls — paraphrase-FC + NLI, temperature 0, gemini reasoning effort minimal (the ONLY file that calls the API); freeze-guarded; `ABORT_USD = 0.50` |
| `analyze.py` | frozen analysis (double contrast Δ², two-sample item-level bootstrap, headroom gate, verdict map); `--selftest` |
| `PREREG-draft.md` | pre-registration draft (freezes to `PREREG.md` after the independent pre-run-critic GO) |
| `README.md` | this file |

## Stimuli freeze hash

`stimuli.json` sha256[:16] = **3ca3a1d50069f0cd** (post-critic refreeze; 40 items:
12 conative verbs × {transitive_conative, conative} + 8 resist verbs ×
{transitive_resist, resist}; seed 20260615). Re-running `prep.py` reproduces this hash.
(Pre-critic hash was `052781ee6c4d9838`; the independent pre-run critic's GO-WITH-FIXES
swapped resist verb `snap`→`bump` — see PREREG §1.)

## Verified offline

- `python3 prep.py` → 40 items, all asserts PASS, sha256 above.
- `python3 analyze.py --selftest` → `selftest PASS (30 checks)` (realizes a clean
  PARAPHRASE-ONLY model, a CONVERGENT-POSITIVE model, a NULL model, plus the panel
  CONFIRM / FALSIFY-convergence / FALSIFY-null / HEADROOM-FAIL paths; bootstrap runs).
- `probe.py` NOT run (awaiting freeze).

## Pre-flight cost estimate

40 items × 2 instruments × 3 models = **240 calls** (+ small verbatim retry per
unparseable response). Point estimate **≈ $0.037**; expected **≈ $0.04–0.08** billed
(billed `usage.cost`, summed by the shared lib). `ABORT_USD = 0.50`. Well under the
$5.00/day UTC cap.

## Freeze status

**FROZEN — independent pre-run critic returned GO-WITH-FIXES (2026-06-15).** The one
SHOULD-FIX (resist verb `snap`→`bump`, a lexical-cue-control purity defect) was applied
and the stimuli refrozen (hash above); analyze `--selftest` re-passed. `PREREG.md` is
committed; `probe.py` may run. A whole-design HEADROOM-FAIL at analysis routes to the
Option-B fallback, not a headline.
