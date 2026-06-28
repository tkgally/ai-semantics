# Pre-run critic certification — VWSD NL-baseline magnitude probe

**Critic:** fresh, independent agent (NOT the build/run orchestrator), per the frozen design's
"Pre-run critic gate (binding)" and the parent decision's binding condition (d).
**Date:** 2026-06-28. **Scope:** GO/NO-GO against the frozen NL-baseline design plus the observed
`sep_nl_i` + adequacy-audit distributions, *before* the reused IMAGE arm's rescue rate is read.

## VERDICT: NO-GO

## Band check
- Independently recomputed from `frozen/nl_descriptors.json` (`audit` block): gpt high-recovery
  41/120 = 0.342; gemini 41/120 = 0.342; **two-auditor mean high-recovery = 0.342**.
- Ratified band (`decisions/resolved/vwsd-nlbaseline-audit-params`, FIXED): `[0.60, 0.95]`.
- **0.342 is mechanically OUT OF BAND, below the lower bound 0.60.** The band is fixed and was not
  relaxed or re-tuned. A held-out recovery rate outside `[L, U]` is, by both resolved decisions, a
  pre-run-critic NO-GO that defers the run and relaxes nothing.

## Independent diagnosis (scorer artifact vs real degeneracy)
Inspected all 70 gpt-"none" items by hand (the gemini "none" set is near-identical, 69). The
deterministic `recovery_score` (run.py:159) returns *high* only when a **lemma of the literal target
word** appears in the recovered phrase; otherwise *none*. There is no semantic/category match. On
independent reading of each item's recovered phrase against the gold descriptor's depicted referent,
**roughly 64 of the ~70 none-items are faithful category recoveries mis-scored as none** because the
recovered common name does not contain the literal target-word lemma — the lemma is technical/Latinate
(thymus→thyme, ara→macaw, aquila→eagle, viola→violet, ling→heather, acropodium→broom, flageolet→bean),
a spelling variant (mescal→mezcal, gantlet→gauntlet, sty→stye, manakin→mannequin), a synonym/slang
(supporter→jockstrap, brace→suspenders, circle→roundabout, shot→injection, mike→microphone,
lumber→bats, mouse→black-eye, torch→spotlight), a proper noun (nan→Nan River, ceres→Roman goddess,
aurora→Sleeping Beauty, anapurna→Durga), or a non-depicted sense where the auditor faithfully named
the image anyway. Only ~6 are even arguably weak, and even those recovered the *scene* correctly while
missing the specific sense-bearing object (e.g. bag, feather boa, butterfly-stroke name). The 0.342 is
therefore overwhelmingly a **scorer-validity artifact**, NOT a degenerate-weak channel. The channel
appears to be naming referents competently; the deterministic literal-lemma scorer cannot see it.

## Disposition
**DEFER + surface a NEW open decision to ratify a VALID recovery-scoring rule** (e.g. a held-out model
re-grade of *category match* using the stored raw guesses, per design B.4's standing flag that the
deterministic recovery-scorer's validity is itself a later-session ratification) BEFORE any re-attempt.
The NO-GO relaxes nothing: the magnitude read is deferred, and **the reused IMAGE arm MUST NOT be read
and the band MUST NOT be relaxed this session**. Critically — the diagnosis that the 0.342 is a scorer
artifact does NOT license proceeding: under the fixed band the observed mean is out of band regardless
of *why*, and the correct, honest move is to fix the yardstick (a valid scorer) in a later session, not
to wave the run through on a sympathetic reading. Re-grading the audit is a re-derivation that re-opens
the freeze and so must itself be ratified cross-session before it can clear a future critic.

## Anti-cheat: PASS
- **Freeze held.** `frozen/nl_descriptors.json` (descriptors + audit) and `raw/text_nl.json` (sep_nl_i
  source) are frozen + checksummed. Reused arms verbatim-by-sha: items `7f9e52fa…`, IMAGE
  `6884eea0…`, DISTRACT `f8fbb6be…`. No results/rescue output exists; `analyze.py` scores the RESULT
  sections only after a GO (README + script header). The IMAGE rescue rate has not been computed.
- **No backdoor.** The builder's "scorer artifact" reading is recorded as a diagnosis, not used to
  smuggle the run through: the README still states the out-of-band rate is a NO-GO, and no magnitude
  artifact was produced. I did not let the diagnosis relax the gate.
- **Neutrality.** I formed NO preference about whether the eventual residual reads narrow or wide; this
  verdict turns only on the fixed band and the scorer's validity, not on the magnitude it would yield.

## Written certification (for the run-dir record)
This is a NO-GO. Independently recomputed, the two-auditor mean high-recovery rate is 0.342, which
falls outside the ratified, fixed adequacy band `[0.60, 0.95]` — below the lower bound — so by both
resolved decisions the magnitude read is deferred and no condition is relaxed. On hand inspection of
all ~70 "none"-scored items, roughly 64 are faithful category recoveries that the deterministic
literal-target-word-lemma scorer marks "none" because the competently recovered common name (or the
auditor's faithful naming of a non-depicted sense) does not contain the exact target lemma; only about
six are even arguably weak, and those recovered the scene correctly. The most defensible reading is
that the 0.342 reflects a scorer-validity artifact rather than a degenerate-weak channel — but that
diagnosis changes nothing about the disposition: under the fixed band the rate is out of band whatever
its cause, and the honest next step is to surface and ratify (cross-session) a valid recovery-scoring
rule — a held-out model re-grade of category match against the stored raw guesses, per design B.4 —
before any re-attempt. The reused IMAGE arm is NOT to be read, the band is NOT to be relaxed, and both
a narrow and a wide residual remain first-class for any future, validly-scored attempt. The freeze
discipline held (descriptors + audit + sep_nl_i frozen and checksummed before any IMAGE result was
read; reused arms verbatim-by-sha; DISTRACT credited first by design), and the critic formed no
preference about the eventual residual width.
