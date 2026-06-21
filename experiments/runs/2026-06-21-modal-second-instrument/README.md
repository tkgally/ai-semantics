# Modal second-instrument forced-choice probe (session 72, 2026-06-21)

**The decisive test of essay revision trigger (c)** of
[`essay/function-words-not-one-category`](../../../wiki/findings/essays/function-words-not-one-category.md):
is the `will`→`would` NLI null the **instrument's** insensitivity or the **relation's** subtlety?

## What this run does

Reuses the **frozen, certified** will/shall/must modal items from
[`2026-06-21-modal-arm-widening`](../2026-06-21-modal-arm-widening/) **verbatim** and swaps the
indicator from **3-way NLI entailment-flip** to a **single-letter forced-choice modal-force
preference** (STRONG vs HEDGE paraphrase). Same single-token output channel (controls the
output-channel confound); different question type. Measures the within-item base→fn preference
**shift**. `must`→`might` is the instrument-validity anchor (NLI flipped it at ceiling), `will`→`would`
the target null, `shall`→`should` the panel-split check, content-swap the falsify control.

Full design, predictions, freeze shas, and the no-new-decision argument: **`PREREG.md`**.

## Files

`build.py` (assembles `stimuli.json` from the frozen modal arms + forced-choice options) ·
`stimuli.json` · `certify.py` → `certification.json` (instrument shortcut/leak checks; matching
inherited) · `probe.py` (forced-choice instrument; freeze guard; `ABORT_USD`=$0.80) · `analyze.py`
(per-arm × model shift + bootstrap CIs) · `raw/` (per-model outputs after the run).

## Pipeline

`build.py` → `certify.py` (`"ok": true`) → **independent pre-run critic GO** → freeze `PREREG.md` →
`probe.py liveness` → `probe.py full` → `analyze.py` + **independent post-run verifier** → result page.
