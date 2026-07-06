# Design-review record — aann-quant-temporal-inversion-v1 (session 188)

Two independent, decorrelated reviews of the **frozen-to-be** design
(`experiments/designs/aann-quant-temporal-inversion-v1.md`). This is a **design-stage** review
(PROTOCOL §A3): the fresh-agent critic holds verdict authority; the non-Anthropic panel vote is QA
input. **No probe ran; the only spend is the one vote.** The conditions below are **binding on the
freeze/run session** (which happens only after the decision
`wiki/decisions/open/aann-quant-temporal-inversion-design.md` ratifies).

## Verdicts

- **Fresh-agent pre-run critic (authoritative): GO-WITH-CONDITIONS.** "A well-built, honest design one
  freeze-pass away from being genuinely informative." **No fabrication** — every cited figure verified
  against in-repo source (model quant×temporal means 43.0/30.05/68.75 vs `results.json`; human quant
  mean 8.4508 n=193 vs `human_class_means.csv`; framing ρ, Tier-0 3/3, quant-drop flip +1.00/+0.50/+0.50
  all confirmed).
- **Non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`, QA): NO-GO** ($0.00304875) —
  **convergent in substance** with the critic (both flag verdict-map precedence, Q2 threshold
  arbitrariness, the B_m baseline definition, the arm firewall, and the subtype clause). The vote's
  higher severity is weighed here: its five points map onto the critic's B2 / S5 / S4 / S3-S7 / S6 and
  are handled as the freeze conditions below, not as design-landing blockers.

Convergence on *which* issues matter is high; the disagreement is only severity framing (blockers vs
fixable conditions). The design is landed as a GO-WITH-CONDITIONS draft; nothing is frozen.

## PREREG blockers (must be fixed in the PREREG before the freeze/run session proceeds)

- **B1 — per-modifier noun-mix confound.** "~6 items per modifier, seeded rotation as in v2b" cannot
  balance 5 temporal nouns and imports v2b's `noun_asymmetry_note`; because per-noun ρ is negative for
  short-span *days/hours* and positive for *years* (`result/aann-temporal-why-reanalysis` H4), a modifier
  drawing more days/hours would invert for **noun-mix**, not lexical, reasons — corrupting `p_m`, the
  class-vs-lexical statistic. **Fix:** give every modifier an *identical* noun×numeral×template frame
  (or a balanced Latin square), asserted per-modifier in `stimuli.json` (e.g. 10/modifier = 2 per noun).
- **B2 — verdict-map NULL-vs-CLASS/LEXICAL precedence unadjudicated.** NULL is gated on the *cell mean*;
  CLASS/LEXICAL on `p_m`; both can fire (≈75% modifiers invert → CLASS, yet a few augmentatives pull the
  mean above neg → NULL). **Fix:** freeze precedence — evaluate NULL first on the cell mean; if not-lowest
  for ≥2/3, verdict = NULL regardless of `p_m`; else evaluate CLASS/LEXICAL/MIXED on `p_m`.

## SHOULD-FIX (resolve at freeze; S1–S2 at the data-reclone step)

- **S1 — Arm 1's per-modifier human means depend on a file not in the repo.** `adjexp_turk.csv` is
  gitignored (`experiments/data/aann-public/`); only class-level `human_class_means.csv` is committed, so
  the 8.45/n=193 is a **pooled** class mean. Per-*modifier* temporal means (what Arm 1's "stronger than
  v2b" claim rests on) are unverified and may be thin (~19 ratings/adjective, distribution unknown).
  **Fix:** freeze gate — reclone the pinned mirror, have `prep.py` report per-modifier temporal rating
  counts, gate Arm 1's per-modifier leg on adequate N; below threshold Arm 1 degrades to the class-level
  comparison (which materially weakens Q1-C's premise and **must be stated**).
- **S2 — the "tourish" typo reaches ANCHORED items.** v2b's "held-out items make no item-level human
  comparison" justification does not transfer to Arm 1 / the Q3-A reference cells (which *are*
  human-compared); v2b's own record shows excluding template-2 flips the verdict category for 2/3 models.
  **Fix:** at freeze check whether Mahowald's rated temporal sentences read "tourist" or "tourish"; use
  what humans saw for anchored arms; make the tourish-exclusion recompute **gate-bearing** for Arm 1.
- **S3 — "item-matched" overclaimed.** The §6 Arm-1 statistic is a per-modifier-mean vs per-modifier-mean
  Spearman over the *model's* generated items, not Mahowald's exact rated tuples. **Fix:** either restrict
  Arm 1 items to Mahowald's exact (adjective×numeral×noun×template) tuples to earn "item-matched," or
  relabel as "per-modifier gradient comparison." *(Design prose corrected s188 to the latter, pending the
  freeze choice.)*
- **S4 — inversion indicator looser than the finding.** `A_m(j) < B_m` uses the pooled non-quant mean, but
  the property is "below **all three** non-quant cells"; pooled ≈51.6 > pos 50.55 > neg 49.35, so "< pooled"
  is easier and biases toward CLASS. **Fix:** define inversion as `A_m(j) < min(non-quant class means)`,
  or justify the pooled choice and note the bias direction. *(Converges with the vote's B_m point.)*
- **S5 — the bottom-3-drop clause is arbitrary and can contradict Y.** If 6 modifiers invert, dropping only
  3 need not lift the cell; "3" is fixed regardless of K. **Fix:** freeze K to an exact integer; tie the
  drop-count to the inverting set (⌈Y·K⌉), not a hard 3. *(Converges with the vote's Q2 point.)*
- **S6 — subtype is descriptive in the decision but verdict-bearing (unthresholded "predominantly") in the
  design §6.** **Fix:** pick one — give "predominantly" a frozen threshold if verdict-bearing, else remove
  SUBTYPE from the verdict map. *(Converges with the vote.)*
- **S7 — Arm 2 is only half-new and curated toward inverters.** 5 of 10 Arm-2 modifiers are v2b held-out
  quant adjectives (scant/skimpy/negligible/modest/ample — the original inverters), while the large-magnitude
  v2b items (colossal/towering/lavish/sizable/respectable) are dropped, biasing Arm 2's `p_m` up. **Fix:**
  report the genuinely-new subset (bare/solid/full/good/whole) separately; document each modifier's source;
  justify or reverse the large-magnitude drop.
- **S8 — the stated inclusion rule doesn't determine the actual list** (skimpy/negligible/modest/ample are
  not OQ-named). **Fix:** enumerate the exact K=20 in the PREREG with a closed, documented source per modifier.
- **S9 — per-modifier frequency not controlled** (the ±0.5 Zipf control is per-class median). **Fix:** wire a
  per-modifier Zipf partial into the inversion read (v2b's `partial_spearman_zipf_adjective_grain` exists).
- **S10 — "byte-frozen instrument; only the item set is new" understates the new analysis surface.** v2b's
  `analyze.py` has no B_m/`p_m`/inversion-count/bottom-drop/reference-arm/subtype logic — the entire §6
  verdict machinery is **new code**, exactly where anti-cheat scrutiny belongs. **Fix:** reframe as "the
  *calling* instrument (`probe.py`: prompts/parsing/settings) is byte-frozen; the item set **and the §6
  verdict logic** are new, frozen in PREREG and self-tested before any call." *(Design prose corrected s188.)*

## NITs

- **N1** — Q3-A's B_m (~4 non-quant adjectives/class) ≠ the §1 table's full-class means; "reproduces the
  four-class table" is a *structural* reproduction on a new occasion, not the same cells — say so.
- **N2** — §3 sources framing ρ from the claim page (0.9288/0.8168/0.8215) rather than v2b's own robustness
  arm (0.9388/0.8783/0.815); both pass — a one-line sourcing note.

## Disposition of the provisional decision defaults (for the ratification session)

- **Q1-C (hybrid): adopt, but condition on S1.** If per-modifier human-N is thin (likely), Q1-C in practice
  becomes "class-level anchor + widened internal-contrast" — closer to B than the design implies. Ratify C
  *with* S1/S2/S3 written in.
- **Q2-A: adopt the family, not the current wording.** Threshold-first + named NULL is the right anti-cheat
  posture but is not runnable until B2 (precedence), S4 (indicator), S5 (bottom-drop/K), S6 (subtype) are
  fixed. Both reviewers push toward a tighter / more monotone primary criterion — the ratification should
  weigh Q2-B (continuous per-modifier dispersion) as the primary read with the 0.70/0.30 count secondary.
- **Q3-A: adopt (right call).** Same-occasion reference is correct; carry the N1 clarification + the S2
  spelling fix onto the anchored reference items.
- **Missing folded choices to surface:** noun/numeral-balance-per-modifier (B1) and tourist-vs-tourish-on-
  anchored-items (S2) are not currently surfaced as freeze choices — add them.

**Bottom line (critic):** fix B1 + B2 as PREREG blockers, resolve S1–S2 at the reclone step, and it is a GO.
