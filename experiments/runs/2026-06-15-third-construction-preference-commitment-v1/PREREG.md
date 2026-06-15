# PREREG — caused-motion third-construction preference/commitment HARVEST arm

**Run:** `2026-06-15-third-construction-preference-commitment-v1`
**Design:** `experiments/designs/third-construction-preference-commitment-v1.md` (FROZEN)
**Decision:** `wiki/decisions/resolved/aann-uniqueness-third-construction.md` (Option A; binding fallback C)
**Frozen pre-run.** This pre-registration is for the **HARVEST/baseline arm only** (design §5, gate
G1–G4). The headline preference/commitment arms are **gated** on the harvest clearing G2 for ≥ 2/3 models
and are NOT authorized by this document.

## Authorization

An **independent pre-run critic** (fresh agent, 2026-06-15) rendered **GO-FOR-HARVEST**:
- numbers-integrity PASS (every prior-art figure the design quotes verified verbatim against its result page);
- all six inherited guardrails present (add-direction scoping; hard Option-C fallback; anchor split;
  lexical-cue double-contrast control; symmetric verdict map; anti-cheat against retrofitting gpt's NLI fragility);
- anti-cheat PASS (the guardrails bias against a free positive); freeze discipline sound.
- **Authorized:** the harvest arm only (~288–360 calls). **Gate:** G2 = baseline marginal-construction
  affirm ≤ 0.50 (target ≤ 0.30), ≥ 2/3 models, with G3 clean-reference ≥ 0.85. **A harvest FAIL routes to
  Option C** ("AANN-specific so far" terminal), **no retuning, no second harvest.**

## Frozen before any model call

- `candidates.json` — 24 marginal verbs (12 M1 cognition/stative + 12 M2 low-propulsion physical) + 6
  clean propulsion reference verbs × 2 rotating light-inanimate objects = 60 items. sha256[:16] =
  `79aa83e4c2a79a53`. Frozen by `prep.py` (no model calls; all asserts PASS).
- Selection rule (frozen in `candidates.json.selection_rule`): retain a marginal verb iff its pooled
  baseline affirm ≤ 0.50 (target ≤ 0.30); require ≥ 10 retained or G4 FAIL. Only this *post-harvest*
  selection is data-driven; the rule itself is pre-registered.
- Instruments: paraphrase forced-choice (affirm = construction reading C) + NLI entailment (affirm = label 0),
  temperature 0, gemini `reasoning: {effort: minimal}`. NLI_SYS + parsers reused verbatim from the conative run.

## Gate evaluation (pre-registered, deterministic)

`harvest.py` computes per-model G1 (marginal affirm), G3 (clean affirm), G2 (≤ 0.50), G4 (≥ 2/3), and the
per-verb subset. The headline is authorized iff G4 PASS **and** ≥ 10 verbs retained. The verdict is written
to `harvest.json` regardless of outcome; a FAIL is a first-class Option-C finding.

## Outcome (recorded post-run)

**G4 FAIL — 1/3 models clear G2** (claude 0.625 FAIL, gpt 0.479 PASS, gemini 0.552 FAIL; clean arm
0.92–1.00 PASS G3). **Routed to Option C; headline NOT run.** Independent recompute from `raw/*.json`
(separate code path) reproduced every figure. See `wiki/findings/results/third-construction-headroom-harvest-v1.md`.
