# Fresh-agent PRE-RUN CRITIC verdict — particle-placement REP2 (s228)

Fresh agent with GO/NO-GO authority; read PREREG, `build_items.py`, byte-frozen `analyze.py`/`common.py`,
v1 PREREG + v1 result. Weighed the non-Anthropic decorrelation vote (`gpt-5.4-mini`, `VOTE-critic-s228.json`,
**NO-GO**) as input, not a veto. Edited nothing.

## VERDICT: **GO-WITH-CONDITIONS** (all conditions are POST-RUN disclosure; no pre-run change required or permitted)

The decorrelation vote's NO-GO ("reused verb+particle pairs → the shared lexical frame carries the effect
→ only a partial item-extension") is **declined on the merits**: it misdiagnoses where the effect lives.

- **(a) Pair identity is differenced out in the decisive arm.** The load-bearing statistic is the
  within-frame `shift2 = mean(split-pref|GIVEN) − mean(split-pref|NEW-MENTIONED)`, where the verb+particle
  pair, the noun, and the entire scored order-string are byte-identical across the three conditions
  (`build_items.emit()`; certification checks (1)+(2): 7 scored-string readers each yield within-frame
  shift2 = 0, max_abs < 1e-9). A pair's baseline split-propensity is a per-frame constant that enters both
  means identically and cancels in the subtraction (`analyze.frame_shifts`). So pair-level bias — the thing
  the vote says "carries the effect" — contributes **zero** to shift2 by construction. The vote's concern is
  about the *level* of split-preference, not the *difference* the firewall reads. (Arms 1/3 are not
  string-immune but are non-gating and cannot manufacture a CONFIRM, which requires cond_fw.)
- **(b) The pairs MUST be reused.** `analyze.py` (sha `fd77c639…`) + `freq_control.json` (sha `cd472475…`)
  are byte-frozen; any pair outside v1's 38-pair set would KeyError the covariate or force a re-freeze —
  breaking the byte-frozen-instrument discipline that DEFINES an A2a replication. Holding the instrument
  byte-identical while freshening everything that varies (all 48 nouns/objects/contexts/subjects fresh, all
  triples disjoint) is the same standard genitive-rep2 (reused gloss templates + possessum inventory) and
  dative-powered met. A genuine replication, not a partial item-extension.
- **(c) The 10 recurring pairs (f39–f48, each re-using one of f01–f38 with a fresh noun+context): 10
  clusters of 2 + 28 singletons.** The only real residual: the frame-level bootstrap is **mildly
  anti-conservative** under intra-pair correlation (effective N between 38 and 48 → CIs slightly narrow → a
  small bias TOWARD cond_fw). Small and bounded (paired frames have different nouns + contexts → low
  intra-pair correlation; v1 had the identical mechanism at 2 recurrences). **Shrinking to ≤40 unique-pair
  frames is REJECTED** — it would undo the enlargement (the run's whole purpose), reduce power (making a
  positive replication *less* likely), and break the byte-frozen bootstrap. Handle by disclosure + a
  supplementary robustness read, not a fix.
- **(d) Other cheat-surfaces checked — none reaches CONFIRM:** noun choice cancels within-frame (firewall);
  duplicate-pair selection criterion is linguistic ("flexible/both-orders"), and re-pairing with a fresh
  noun+context means v1 firewall magnitude does not transfer through pair identity; DECISIVE leg, verdict
  rule, RNG seed, thresholds all byte-frozen; enlargement is arm-uniform (all frames emit 4+6+4 trials,
  firewall trials/frame 6 ≥ definiteness 4); HARD_STOP 3.50→3.80 the sole common.py delta (pure cost gate).
  SHADOW/WEAK/FALSIFY remains fully reachable (gpt a pre-named SHADOW; enlargement powers, does not guarantee).

## Conditions (ALL post-run disclosure in `result/particle-placement-givenness-rep2`; NONE before the run)

1. Disclose the pair-reuse structure (48 frames / 38 distinct pairs / 10 pairs twice with fresh noun+context)
   and its variance implication: the frame bootstrap (byte-frozen from v1) is mildly anti-conservative under
   intra-pair correlation, more so than v1 (10 vs 2 recurrences) → affects interval WIDTH only, not point
   estimates; CONFIRM rests on the within-frame firewall where pair identity differences out.
2. Report a supplementary (non-decisive) robustness read from the raw jsonl — e.g. firewall shift2 restricted
   to the 38 unique-pair frames, or a pair-clustered resample — as a disclosed sensitivity note that does NOT
   replace the pre-registered frame-bootstrap verdict and must not relabel the outcome.
3. State the duplicate-pair selection criterion ("flexible/both-orders-natural," NOT v1-outcome-based) and
   note the firewall differences out pair identity, so pair-selection cannot import v1 firewall magnitude.
4. Keep the byte-frozen covariate caveat (near-vacuous, R²≤0.02, duplicated x for recurring pairs, non-gating).

**Do not** touch `stimuli.json`, `analyze.py`, `freq_control.json`, the bootstrap, or the frame count before
running. Run the frozen instrument as-is on the next full-$5 UTC day per the resume protocol.
