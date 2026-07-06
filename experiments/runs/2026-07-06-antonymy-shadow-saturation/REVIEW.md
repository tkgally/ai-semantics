# Pre-run review log — A1b antonymy shadow-saturation probe (s186)

Two independent pre-run reviews (fresh-agent adversarial critic + one non-Anthropic decorrelation
vote, `openai/gpt-5.4-mini`, PROTOCOL §A3). **Both returned NO-GO on round 1.** Every point was
addressed before any spend; a round-2 re-critique was run on the corrected freeze (both reviewers
explicitly required it). No model data was collected during either round.

## Round 1 findings (both NO-GO) → disposition

**Fresh-agent critic (NO-GO):**
1. **[BLOCKER] Control stale vs items** — `control.json` was built against the pre-transitive-closure
   cue set; 322/707 current cues absent, collapsing residual n (hyper 29, hypo 25) vs antonymy 130.
   → **FIXED:** rebuilt `control.json` + `counts.json` against the current `items.json` (full corpus
   re-stream). Coverage re-verified: 0 current cues missing.
2. **[BLOCKER] PREREG contradicts code** (closure gold + GOLD_CAP undocumented). → **FIXED:** PREREG
   now documents the transitive-closure gold rule, the size-matched arm, and the hit@3 companion.
3. **[BLOCKER→interpretation] Gold-size confound tilts toward CONFIRMS** — antonymy gold≈1 caps
   precision at 1/3 when the model volunteers 3, mechanically depressing antonymy 𝒮 → smallest
   residual for a reason unrelated to co-occurrence; %gold-in-V and control-𝒮 asymmetries push the
   same way. → **FIXED:** added **HIT@3** (gold-size-insensitive) as a **co-primary** scorer;
   promoted the **size-matched** (|gold|≤5) residual to co-primary; report per-relation gold sizes +
   %gold-in-V. CONFIRMS now requires antonymy-smallest under all four frame views.
4. **[SHOULD-FIX] `analyze.py` CONFIRMS looser than PREREG** ("visibly larger" not operationalized).
   → **FIXED:** operationalized as CI-separation (antonymy residual CI-upper < meronymy/hyponymy
   CI-lower), reported as a count.
5. **[SHOULD-FIX] INVERTED rationale contradicts control** (meronymy is 2nd-*strongest* cued, not
   weak). → **FIXED:** INVERTED set = the two measured weakest-cued relations (bottom-2 by frame
   cue-strength, computed from the corpus), not a hard-coded gloss.
6. **[NIT] Clause-1 and clause-2 share the frame control** (not independent). → **DISCLOSED** in
   PREREG; clause-2 also reported against the sent control.

**Non-Anthropic vote (NO-GO):**
- **[BLOCKER] Control is antonymy-laden** (contrastive frames specifically cue antonymy → confirm
  for the wrong reason). → **ADDRESSED:** the relation-agnostic **sent** (all-intrasentential) G²
  control is elevated to a required view; **CONFIRMS-ROBUST** demands antonymy-smallest under it too,
  else the result is scoped **CONFIRMS-FRAME-SPECIFIC**. The frame control's antonymy-appropriateness
  is stated transparently as the essay's mechanism, not hidden.
- **[BLOCKER] Gold cardinalities make residuals non-comparable.** → same fix as critic #3 (hit@3 +
  size-matched co-primary).
- **[BLOCKER] Antonymy-smallest partly pre-decided.** → same as its BLOCKER 1; the dual-control +
  hit@3 + size-matched convergence requirement removes the single-control circularity.
- **[SHOULD-FIX] verdict multiplicity / calibration** → calibration gate added (residual reported
  descriptive-only if it merely reproduces raw recovery); headline requires convergence across six
  views rather than one loose threshold.

## Round 2

Re-critique (fresh agent) + re-vote on the corrected freeze recorded below this line at run time.
