# PREREG — forced-decomposition repeated-runs (K=5) decline-axis resolver

**Frozen before any run (session 88, 2026-06-23).** This file fixes the design and the
verdict-reading rule **before** any model is queried, so the verdict cannot be tuned to a
desired outcome after seeing results.

## What and why

The NEXT.md backlog-3 resolver for the **session-82 vs 82b disagreement**: two routine
sessions ran independent forced-decomposition gpt re-runs of the *same* frozen instrument
for the same slot. Session 82 (PR #128) read gpt's **bridging %UNCLEAR at 8.3 % (2/24)
→ MIXED/WEAK**; the concurrent session 82b read **0.0 % (0/24) → channel-CONTROLLED null**.
They disagree by ~2 of 24 bridging items — at or under the documented ~12 % temp-0 label
jitter ([`essay/point-estimate-is-a-draw`](../../../wiki/findings/essays/point-estimate-is-a-draw.md)).

This runs the **byte-identical** frozen instrument (sha `dceafa9d…`) **K=5** times at
temperature 0 and reads the **de-noised** majority-vote / range on the decline axis.

It is a **noise-floor measurement**, the licit same-instrument re-run
([`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md)
threaded needle: re-running to *measure the floor* is licit; re-running to "firm a null"
buys nothing). It makes **no new human-comparison claim** beyond pinning the magnitude of
the already-reported, descriptive (DWUG-anchored, usage-similarity-capped) gpt leg.

## Frozen design

- **Instrument:** the forced-decomposition `instrument.json`, sha
  `dceafa9d976cb47c71505d0e6f6f8df205595ccfcd6942f4c96dbffc02e97d42`. The driver
  `repeated_probe.py` imports the frozen probe and reuses `build_systems()` / `load_items()`
  / `run_single()` **verbatim** (fail-closed on any sha drift), so every call is
  byte-identical to session 82. Reasoning held constant (`gpt {"enabled": False}`), temp 0.
- **Model:** gpt-5.4-mini only (the disputed leg). claude/gemini are not re-run (their legs
  answered under the offered surface; not in dispute).
- **Framings:** `c_third` (DECLINE — the disputed axis) + `b_conf` (CONFIDENCE — the other
  commitment instrument the MIXED/WEAK-vs-null verdict combines). **Position (`b_rel`) and
  the topic control are NOT re-run** — position replicates CI-strict between the clear
  classes across all three channels in session 82, so it is not in dispute; skipping it
  keeps the resolver targeted and cheap. (Documented as a scope choice, not a finding.)
- **K = 5** independent temp-0 draws per item per framing (88 items × 2 framings × 5 =
  **880 calls**). Each call is an independent HTTP request; nothing cached/deduped.
- **Items:** the same frozen 88 (bridging 24 / clear-same 29 / clear-different 35; dwug 48 +
  wic 40), staged recipe-not-corpus via the v1 `prep.py` + `map_wic_fulltext.py`.
- **Committed raw is sanitized at write time** (no `raw`/`final_seg`; only labels, counts,
  usage) — DWUG is CC BY-ND, WiC CC BY-NC.

## Verdict-reading rule (FIXED before running)

Primary object: per-run **bridging %UNCLEAR** (the 5 draws) and the **de-noised
majority-vote** bridging decline = fraction of bridging items whose label is `UNCLEAR` in
**> K/2** runs.

1. **Jitter check (symmetric, descriptive).** Report the K-draw range on bridging decline
   and whether it spans the s82 (8.3 %) and s82b (0.0 %) point estimates. If both fall
   inside the observed range, the s82↔s82b disagreement is **confirmed to be run-to-run
   temp-0 jitter** at the documented floor.

2. **De-noised commitment verdict (the resolution):**
   - **NULL / channel-CONTROLLED** (s82b vindicated) **iff** the de-noised majority-vote
     bridging decline is ~0 (**≤ 1/24**) **and** is **not** robustly elevated over the
     de-noised clear-class decline (its lemma-clustered bootstrap lower bound does **not**
     exceed the max clear-class majority decline). Reading: the s82 2/24 elevation was
     reading jittery items; gpt's commitment posture de-noises to "no robust decline crack."
   - **MIXED/WEAK** (s82 survives) **iff** the de-noised majority-vote bridging decline is
     robustly elevated over the clear classes (clustered lower bound > max clear-class
     majority decline). Reading: a real, if thin, decline elevation survives de-noising.
   - **INDETERMINATE at this K** otherwise (small modal decline whose clustered CI does not
     cleanly separate from the clear classes) — report the band, do not force a label.
   The CONFIDENCE axis (`b_conf`) is reported alongside: pooled bridging−clear-same
   difference with a clustered CI; CI **including 0** == "no robust crack" (the posture both
   s82 and s82b already agreed on; a robust crack would be a new, separately-reported datum).

3. **Clear-class precondition (per run):** clear-class decline < 20 % and mean confidence
   > 70 on every run; otherwise the instrument did not read cleanly that run (flag it).

## Anti-cheat declaration

- The rule above is fixed **before** any run; the analyzer encodes it; the verdict is read
  off `analysis.json` mechanically.
- This re-run **measures the noise floor**; it does not alter *what* is scored, only *how
  many times*. The load-bearing facts both s82 and s82b already agree on (uptake induced,
  the graded SCALE replicates, **no clean graded-commitment positive**) are **not** in
  dispute and are not re-litigated.
- Outcomes are reported **symmetrically**: a NULL de-noising (the more likely outcome given
  2/24 sits at the jitter floor) and a MIXED/WEAK survival are equally publishable; neither
  is the "hoped-for" result. No human-comparison claim is added either way.
- Governance: a same-instrument, same-item, repeat-count-only re-run under the **already
  ratified** lexical bridging-context gates — **no new decision owed**. Requires an
  independent fresh-agent **pre-run critic GO** + budget pre-flight before the spend-bearing
  run, and an independent fresh-agent **post-run verifier**.
