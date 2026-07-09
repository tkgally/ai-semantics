# Pre-run FREEZE review — adjective-antonymy replication probe (s196, 2026-07-09)

Frozen artifacts: `PREREG.md`, `prep.py`/`items.json`/`vocab.json`, `build_cooc_c4.py`/`control.json`,
`analyze.py`, `probe.py`. **Nothing run when this review was taken** (no model calls).
PROTOCOL §A3: an **independent fresh-agent pre-run critic** (GO/NO-GO verdict authority) **+ one
non-Anthropic decorrelation vote** (`panel.B`, cutoff-aware preamble). Both reached this session by a
different agent than the freeze author.

## Fresh-agent critic (verdict authority) — GO, no BLOCKERS, FABRICATION-CHECK PASS

Reproduced every load-bearing number in `PREREG.md` from the frozen artifacts (no model calls); audited
scoring/verdict logic against PREREG and against the s186/s193 instruments this byte-freezes; confirmed
both outcome directions are genuinely reachable.

- **Fabrication / faithfulness — all PASS** (recomputed from `items.json` + `control.json`): the
  predictor table exact (antonymy frame-G² 𝒮 0.1214 / sent 0.1487 / HIT@3 0.3643 / 129-of-130;
  synonymy 0.0465/0.0388/0.1240; similar 0.0462/0.0487/0.1154; also-see 0.0615/0.0487/0.1846); **mean
  control-frame soundness 0.0689 ≥ 0.05 → calibration gate CLEARS** (residual arm verdict-bearing);
  achieved N=130/relation, Lg10WF medians + gold sizes match; **0 overlap** with the 707 s186 cues on
  all 4 relations; adjective `min_depth()` a **degenerate constant 0** (H2 correctly not tested); C4
  volume 22.33M sentences / 388M tokens ≥ 21.3M/320M.
- **Instrument-freeze faithfulness — PASS:** `_assert_frozen_g2()` green (`signed_g2` + `compute_control`
  byte-identical to s186; K/FRAME_WIN/CONNECTIVES identical; **no Hearst/hypernym arm leaked**);
  `NEUTRAL`/`FRAME`/`parse_words`/`ask()`/`spearman` byte-identical to s186 at the code level (diffs =
  comments only); `prep.py` implements Q1-C with the correct WordNet calls, POS `a`+`s`, band [2.0,4.5],
  antonymy-profile freq-matching, no `is_a_depth`.
- **Verdict map vs PREREG — EXACT MATCH:** all thresholds (0.30/0.50/0.05/0.10/0.15, MAJ 2); H1 bands
  exhaustive + mutually exclusive (C2); antonymy-shadow RANK+MARGIN rule (C6) relation-agnostic;
  frame-ablation Δ-rule (C8) present; item-level arm locked descriptive-only (C7); residuals paired by
  cue within relation, frame-variant control used, empties dropped per the frozen s186 convention and
  reported.
- **Anti-cheat — PASS:** every threshold frozen before any model call; **ANT-SATURATES is genuinely
  reachable precisely because the control is strong on antonymy (0.36)**, and ANT-CLEARS/MIDDLING + the
  H1 BREAKS/null bands are all first-class; the ≤4-point band asymmetry is disclosed (C4) and barred
  from solely carrying promotion. Nothing reads as tuned toward confirming the decoupling or the s186
  falsification.

**Four NITs (non-blocking; explicitly "do NOT change before running"; carried to the result / verifier):**
1. The calibration gate is single-condition (`mean < 0.05`), whereas s186 used a two-part gate
   (`mean < 0.05 AND median-Spearman ≥ 0.90`); pre-registered as the single-condition form in C3, **moot
   here** (0.0689 clears both) and the *stricter/more conservative* direction — note the divergence in
   the result so it is not read as drift.
2. `probe.py` GLOSS antonymy/synonymy dict lines differ from s186 by whitespace only — the **rendered
   prompt strings are byte-identical**.
3. The item-level SECONDARY Spearman is tie-naive over ~520 heavily-tied points (statistically weak) —
   locked descriptive/non-decisive (C7), acceptable.
4. Watch slot-C (reasoning model) empty-answer counts at analysis time (dropped empties can inflate
   recovery); the frozen convention matches s186 and `empties_neutral` is reported — confirm empties are
   low before reading the residual.

## Non-Anthropic decorrelation vote (`panel.B`, $0.0026715) — GO-WITH-CONDITIONS

Converges (GO). Conditions, all carried to the **write-up**: (1) confirm the gates + panel
inclusion/order were frozen before any model outputs — they were (ratified before any run; the standing
`config/models.md` panel, not selected on preliminary output); (2) **separate confirmatory vs
descriptive claims line-by-line** in the result, especially the control-driven antonymy arm and the
low-power H1 arm; (3) noted the RANK+MARGIN rule "partly bakes in" the expected direction because the
control shows a strong antonymy advantage. **On (3) the direction is actually conservative for
ANT-CLEARS:** antonymy faces the *strongest* control (HIT@3 0.364 vs 0.115–0.185), so its residual is
*harder* to make largest — CLEARS (the s186-falsification-replicates reading) is the harder outcome,
SATURATES the easier one. Recorded verbatim in `vote-freeze.txt`.

## Disposition — GO. Run the panel.

Verdict of record: **GO** (fresh critic authority; non-Anthropic vote converges). No blocker; nothing
changed before running (the four NITs are verifier-awareness items). Two write-up conditions bound: note
the single-condition calibration-gate divergence from s186; separate confirmatory vs descriptive claims.
