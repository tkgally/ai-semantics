# Freeze-stage pre-run review — aann-quant-temporal-inversion-v1 (session 189)

Two decorrelated reviews of the **frozen** probe (`prep.py` + `stimuli.json` + `PREREG.md` +
`analyze.py`), PROTOCOL §A3. The fresh-agent critic holds GO/NO-GO authority; the non-Anthropic panel
vote is QA input. Run only on GO.

## Verdicts

- **Fresh-agent pre-run critic (authoritative): GO.** Anti-cheat **PASS**. Verified concretely: the
  instrument is byte-frozen (`diff` v2b/probe.py = exactly the `ABORT_USD 0.30→0.60` line); the
  `analyze.py --selftest` cases are non-degenerate and genuinely force each of CLASS/LEXICAL/MIXED/NULL
  (traced by hand); **all 10 Arm-1 human means recount exactly against `adjexp_turk.csv`** (staggering
  8.3333/N=24, mere 8.875/N=16, record-setting 9.0455/N=22, … total N=193 = the committed class mean's
  n) — **no fabrication**; B1 holds mechanically (all 20 quant modifiers share the identical
  noun[2 each]×numeral[5,5]×template[{4,3,3}] frame); the "tourish" typo is genuinely in Mahowald's own
  `templates_adj.csv` (751 occurrences) so his raters saw it — **S2 faithfulness correct**; the full
  `main()` path runs end-to-end on synthetic raw. **The MIN baseline is the *conservative*
  operationalization of "below all three non-quant cells" — it makes CLASS *harder*, tilting AGAINST the
  author's registered bet**, the correct anti-cheat direction; NULL-first is coded before the shape read;
  the 0.70/0.30 count + bottom-drop are computed but never fed to the classifier (genuinely descriptive);
  Arm-2a deliberately includes high-acceptability large-magnitude modifiers (good/full/whole/solid) that
  plausibly will **not** invert, so NULL/LEXICAL have a real path; all four outcomes reachable.
- **Non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`, QA): NO-GO** ($0.00271275) — **DIVERGENT;
  weighed and largely rebutted.** Its central BLOCKER (revert the MIN baseline to the pooled non-quant
  mean, on the ground that MIN "biases / is tunable") **contradicts the ratified decision and is
  factually backwards**: the ratification chose MIN *because* S4 showed the pooled mean biases *toward*
  CLASS (pooled > min ⇒ "below baseline" is a laxer bar), and MIN has **no researcher degree of freedom**
  (it is a deterministic statistic of the same-occasion reference data, frozen before any call). The
  fresh critic independently confirmed MIN is the conservative, anti-cheat-favorable choice. The vote's
  other points are handled by the frozen design: NULL-first is a clean pre-registered condition proven
  reachable by the self-test; the item-set "neutrality" worry is exactly S7, already addressed (source
  stratification + genuinely-new subset reported separately + a CLASS verdict must survive it — all
  computed in `analyze.py`); the Arm-2 human-language firewall is in place (Arm 2 carries no human
  rating by construction); the tourish recompute is frozen (primary keeps tourish; the exclusion is a
  required sensitivity view, disagreement reported as template-sensitivity, never silently picking the
  nicer verdict). Per PROTOCOL §A3 the GO/NO-GO authority stays with the fresh-agent critic; the
  divergence is recorded here.

## Conditions carried to the run + result (none block spend)

1. **Post-run S7 survival gate (manual interpretive).** `arm2_new_shape` (median_d, all_below_zero over
   {good, full, whole, solid, bare}) is **computed and frozen** but **not enforced on the panel verdict
   in code**. The result-writing session applies it by hand: **if the panel returns CLASS but the
   genuinely-new subset median_d ≥ 0, the CLASS reading is downgraded/qualified** (the class effect does
   not survive the genuinely-new items). Recorded so the interpretive gate is honored.
2. **Arm-1 Spearman reported with its noisy caveat** (human per-modifier means over 11–24 singly-rated
   items; the 10-point rank correlation is underpowered) — already in the PREREG; keep on the result page.
3. **NITs (note if they fire):** `panel_verdict` returns SPLIT with < 2 Tier-0 passers (v2b passed 3/3,
   low risk); the reference arm uses a partial num/template rotation (only class-level means are used, so
   acceptable; the tourish recompute partially covers template sensitivity); the design §5 "item-matched"
   phrase is superseded by the PREREG's "per-modifier gradient — NOT item-matched" (S3; the PREREG
   governs the run).

**Bottom line:** GO. Proceed to run (~972 calls, est. $0.15–0.30, ABORT $0.60), then the post-run
recompute-from-raw verifier and the result page, honoring the two post-run conditions above.
