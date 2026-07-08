# Freeze-stage pre-run review (s193)

**Session 193 (2026-07-08).** PROTOCOL §A3 freeze-stage critique of the FROZEN (not-yet-run) FRESH
relation-recovery / taxonomic-proxy probe. `PREREG.md` frozen; `raw/` empty (verified). Decides ~$0.4
of spend. **Outcome: GO** (fresh-agent critic, verdict authority) + one non-Anthropic decorrelation
vote GO-WITH-CONDITIONS (QA, weighed below).

## (1) Fresh-agent pre-run critic — VERDICT AUTHORITY → **GO**

An independent agent (not the freeze author) read PREREG, prep.py, build_cooc_c4.py, analyze.py,
probe.py, the design + resolved decision + pilot, and the s186 instrument; verified every frozen
number firsthand with read-only Bash.

> **OVERALL: GO. No BLOCKER. Anti-cheat PASS. Fabrication check PASS. All five outcomes reachable.**
> - **Six conditions + three riders all honored.** (1) analyze.py: H1/H2 read only the across-relation
>   ρ; the item-level block feeds *only* the `level_divergence` flag + a NON-DECISIVE report — it is
>   *structurally incapable* of moving H1/H2. (2) H1 bands exhaustive/mutually-exclusive (ρ=0.50→PARTIAL),
>   numeric H2 margin ≥0.20. (3) C4 primary; 22.33M sentences / 388.2M tokens ≥ s186. (4) `signed_g2` +
>   `compute_control` character-for-character identical to s186; `_assert_frozen_g2` is a genuine
>   import-and-compare (8-case battery + synthetic `compute_control`), not a trivial pass; only the C4
>   IO adapter differs. (5) IS-A depth primary (neg), Hearst secondary (pos), Hearst-only win →
>   WINS-QUALIFIED. (6) 0 overlap with the s186 cues, 6/6; antonymy reported at achieved 87, total 687.
> - **Anti-cheat PASS; the test is NOT rigged toward H2.** Simulation: if recovery repeats the s186
>   ordering (hypernymy best-recovered), then because hypernymy is one of the *deepest* relations on C4
>   (7.008), ρ_depth = −0.200 with margin 0.057 < 0.20 → **depth H2 LOSES cleanly**, and ρ_hearst is in
>   the wrong direction → Hearst loses too. The a-priori-likely outcome is **H1-REPLICATES + H2-LOSES**;
>   the riskier hypothesis genuinely can fail. Nothing is tunable post-hoc (literal constants matching
>   PREREG).
> - **Verdict-map ↔ code exact match** (0.30 / 0.50 / 0.20 / MAJ 2; signs; tie-naive Spearman
>   byte-identical to s186). **Fabrication PASS**: 707 s186 lemmas, 87/120/687 fresh N, 0 overlap,
>   687/687 depth resolved, the IS-A/cue-strength/Hearst vectors, 22.33M/388.2M — **every number
>   reproduced exactly**. **Construct-validity** (IS-A depth / WordNet shared source) mitigated by the
>   gold-independent cue-first-synset depth, carried as a scope caveat; Q4 internal-contrast-only.
> - **NITs (non-blocking):** (i) the design/condition-6 wording says "780 s186 cue lemmas"; PREREG +
>   prep.py correctly exclude the **707 unique** union (780 = 6×130 slots; a noun serving multiple
>   relations collapses to 707) — the code does the stricter/correct thing; reconcile the wording on the
>   result page. (ii) HIT@3 is reported as a co-primary but the frozen bands run on soundness ρ_cue only
>   (per PREREG) — note on the result page so HIT isn't read as decisive.
> **Recommendation: proceed to run.**

## (2) Non-Anthropic decorrelation vote (QA input, no authority) → GO-WITH-CONDITIONS

`openai/gpt-5.4-mini` ([`vote-freeze.py`](vote-freeze.py) / [`vote-freeze.txt`](vote-freeze.txt),
**$0.002853**): GO-WITH-CONDITIONS. Two "BLOCKER"-labelled asks + minor riders, **weighed**:

- *"Mechanize the verdict map; no interpretive escape hatches (PARTIAL / QUALIFIED)."* — **Already met.**
  The fresh critic confirmed `analyze.py` computes every label mechanically from the frozen constants;
  PARTIAL is a pre-named exhaustive band and QUALIFIED a pre-declared label, not human discretion.
- *"Lock the proxy hierarchy — Hearst strictly ancillary, ideally no H2 claim."* — **Partly met, and the
  stronger version is declined as contradicting the ratified gate.** IS-A depth is already the sole
  full-status H2 test and a Hearst-only win is pre-declared QUALIFIED/weaker (ratified condition 5).
  Downgrading Hearst to *no* H2 claim would contradict ratified **Q3-A** (H2 satisfied if *any*
  pre-registered proxy out-predicts cue-strength). The qualified-status already prevents an equal-status
  Hearst win.
- *"Add an absolute |ρ_proxy| floor beyond the margin"* / *"item-level to an appendix"* / *"hash the
  predictors before scoring."* — The floor is a defensible tightening but the fresh critic (authority)
  judged the frozen margin fair and the test un-rigged, and changing a frozen threshold post-freeze is
  itself a discipline risk; **not adopted**. Item-level is already marked descriptive/non-decisive.
  Predictors were **committed to git (hashed/timestamped) before any model call** — the freeze commit —
  which is exactly the requested discipline.

**Convergence:** both reviewers GO/GO-WITH-CONDITIONS; the vote's substantive asks are already satisfied
by the ratified structure or decline on ratified-gate grounds. **Proceed to run.** $0.002853 (one vote).
