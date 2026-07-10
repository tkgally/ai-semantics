# Pre-run design review — BLiMP forced-choice sweep (A3b), design v1

**Reviewer:** independent, adversarial fresh-agent pre-run critic (s204). Not the author of the
design. **Decorrelation vote:** `openai/gpt-5.4-mini` (see `VOTE-s204.json`) — GO-WITH-CONDITIONS,
Q1-B / Q2-A / Q3-A, single top risk = curated-subset fishing. My verdict is the authority; I weigh
the panel vote where it converges/diverges below.

Artifacts read: `experiments/designs/blimp-forced-choice-sweep-v1.md`;
`wiki/decisions/open/blimp-forced-choice-sweep-design.md`; `wiki/base/resources/blimp.md`;
`CLAUDE.md`; `PROTOCOL.md` §2–§5,§B; `wiki/meaning-senses.md`; the linked
essay/claim/theory/source (all four exist). I also grepped the repo for the per-paradigm anchor
data (finding below).

---

## Verdict

**GO-WITH-CONDITIONS**, conditional on gate ratification s205+ **and** on the freeze conditions
below being honored. The unit is well-motivated, honestly scoped, and its anti-cheat scaffolding
(pre-registered bands, strata, first-class nulls) is genuinely good. But two problems the panel
vote did not surface make an unconditional GO wrong: **(1) the load-bearing human anchor is not yet
in the repo**, and **(2) the PRIMARY reading is a Spearman over ~10 points, which is badly
under-powered for the verdict bands as written.** Both are fixable at freeze; neither is a reason to
kill the unit. It is not a NO-GO — the design is contamination-honest and the human-comparison
posture is categorically correct — but it must not freeze at Q1-B/9–12 paradigms with the anchor
uncommitted.

### Per-gate votes

- **Q1 — B, with a binding condition (expand toward the top of the range or beyond).** The
  depth-stratified subset is the right instrument for *both* readings, and the pre-committed
  locality rule is the correct fishing defense (I concur with the panel here). **But 9–12
  paradigms is too few for reading 1's per-model Spearman** (see Methodological risks §5). Condition:
  freeze **≥16 paradigms** spread across the four strata, or adopt **Q1-C** (the full 67 — which
  *simultaneously* powers the Spearman and dissolves the curation objection, at the cost of spend
  and theme-dilution). Plain Q1-B at the 9–12 floor is a SHOULD-NOT. I stop short of voting C only
  because the depth-stratum contrast (reading 2) is sharper on a curated set and cost discipline
  favours a middle path — but a reviewer who votes C is on firmer statistical ground than one who
  votes B-at-9.
- **Q2 — A.** Both orders, order-averaged + consistency + flip-rate, is the right control for the
  one known 2AFC artifact. Consistency accuracy is the metric that actually hardens against bias;
  keep it as the primary robustness check, not a footnote. Unconditional agree.
- **Q3 — A, with conditions.** The human-comparison anchor declaration is *categorically* correct
  (there is a genuine human key — `total_mean` — so `internal-contrast-only` would be *dishonest*,
  not more honest). But Q3-A is sound only if (a) the anchor is actually committed to the repo
  (Blocker 1) and (b) the "uniform inflation" premise is guarded, not assumed (Blocker 3 / risk §2).
  Full Q3-B is not required for v1; a **bounded content-word-swap arm on 2–3 paradigms** would
  materially strengthen the contamination story and I recommend it as a SHOULD-FIX, not a blocker.

---

## BLOCKERS (must fix before freeze)

1. **The per-paradigm human anchor is not in the repo — the PRIMARY reading currently rests on an
   uncommitted, unverifiable "firsthand fetch this session."** I grepped: the per-paradigm numbers
   (`0.958`, `0.83`, `0.72`, `0.73`, `total_mean`, `human_validation_summary.csv`) appear **only**
   in the design, the decision page, and `wiki/program.md` — *nowhere as committed data*, and
   **`wiki/base/resources/blimp.md` does not contain a single per-paradigm agreement number.** The
   resource page documents only the *aggregate* 96.4% and merely notes the repo "ships 'Full human
   validation judgments' in its `raw_results` folder." Under PROTOCOL §5.4 (provenance) an anchor
   must be an in-repo resource that *actually bears on the claim with matching content* — right now
   the resource the design points its `anchors:` link at does **not** carry the per-paradigm profile
   the whole human-comparison reading is built on. **Fix:** before (or at) freeze, fetch
   `human_validation_summary.csv`, commit it (or a pinned sample) with its sha256, and **update
   `resource/blimp.md`** to catalogue the per-paradigm agreement (columns `Condition,accepted,
   total_mean,count`, the range, and the example rows) at the strength the file supports. Until that
   lands, Q3-A's `anchors: resource/blimp` declaration over-reads the resource page. This is the
   single condition I most insist on (see below).

2. **Power: the PRIMARY (human-anchored) reading is a Spearman over ~10 paradigms.** At n≈10 the
   sampling error on ρ is enormous — a Spearman of +0.4 is *not distinguishable from 0* (roughly
   p≈0.25; the ~0.05 threshold at n=10 is ρ≈0.64). So the verdict bands "PROFILE-ALIGNED iff
   ρ>+0.4" and "DIVERGES iff <+0.2" are **not calibrated to the instrument's resolution** — most
   real outcomes will land in a CI that spans all three bands. **Fix:** either raise the paradigm
   count to give the Spearman usable resolution (Q1 condition above — ≥16, ideally more), or
   explicitly downgrade reading 1 to *descriptive/directional* with the CI reported and the verdict
   framed as "consistent with alignment/divergence," never as a decided PROFILE-ALIGNED claim, and
   forbid the result from being promoted to a `claim` on n≈10 alone. State the achieved-n power in
   PREREG.

3. **The "memorization inflates uniformly" premise is load-bearing and untested — and non-uniform
   contamination would confound reading 1, not just reading 1a.** The design's robustness argument
   (relative profile survives a *uniform* boost) is valid *only under uniformity*. But contamination
   is plausibly **non-uniform and correlated with human agreement**: frequent, human-easy
   constructions (adjacent agreement) are also the most represented in pretraining and the most
   memorized, while rare island/scope contrasts are less so. If exposure correlates with `H(p)`, it
   inflates ρ_prof *spuriously* — manufacturing profile-alignment from a training-frequency
   artifact. **Fix:** (a) pre-register a **saturation/range guard** — if a model's accuracy variance
   across paradigms is near zero (all near ceiling), ρ_prof is uninformative → forced INCONCLUSIVE,
   not a reported coefficient; and (b) at minimum add a contamination *diagnostic* (report absolute
   accuracy dispersion per model; ideally the bounded content-word-swap arm of Q3-B on the
   shallow-vs-deep extremes) so a frequency-driven pseudo-alignment can be distinguished from a
   structural one. Without at least the range guard, a PROFILE-ALIGNED verdict is not safely
   interpretable.

## SHOULD-FIX

4. **Low-human-agreement paradigms have unreliable gold labels — this bites reading 2 specifically.**
   The design places `coordinate_structure_constraint_subject_extraction` (human `total_mean`
   **0.514**, ~chance) in the deep-structural stratum. Reading 1 can legitimately use a low-agreement
   paradigm as a *profile point*. But reading 2 scores model "accuracy" against the **template gold
   label**, and where humans endorse that label only 51% of the time the gold is itself contested —
   "accuracy" there measures agreement with a shaky key, not grammatical competence. **Fix:** either
   set a human-agreement floor for paradigms entering the reading-2 accuracy contrast (e.g. exclude
   `H(p) < ~0.6` from the *accuracy* strata while keeping them in the *profile* Spearman), or
   pre-register that sub-0.6-agreement paradigms are reported descriptively only.

5. **Reading 2 is labeled "internal-contrast-only" but its stated interest imports the human key.**
   The design says DEPTH-GRADED is "expected" and its bite is "whether it *exceeds the human dip*" —
   that comparison uses `H(p)`, so the interesting version of reading 2 is *not* purely within-panel.
   This is a labeling inconsistency, not a fatal flaw. **Fix:** either keep reading 2 strictly
   within-panel (drop the "exceeds the human dip" framing from the internal-contrast reading and move
   that comparison explicitly under reading 1's human-anchored umbrella), or relabel the "excess over
   human dip" quantity as a third, human-anchored sub-reading. Do not let a within-panel gradient be
   scored against a human baseline while wearing the `internal-contrast-only` label.

6. **Bounded contamination control (Q3-B arm) would materially de-risk the headline.** Not required
   for v1, but a content-word swap on even 2–3 paradigms (one shallow, one deep) turns "we assume
   uniform inflation" into "we checked whether swapping surface strings moves accuracy." Recommend as
   a cheap strengthener.

## NITS

- The design quotes example rows "verbatim" from a CSV that is not committed; once Blocker 1 is
  fixed these become checkable — until then they read as unverifiable to any later session. (Same
  root cause as Blocker 1; flagged separately because the *design page itself* asserts verbatim
  values with no in-repo referent.)
- `ABORT_USD ≈ $2.0` with a pre-flight of $0.6–1.6 and a gemini "wildcard" is sensible, but state
  the split-into-two-half-sweeps trigger as a hard rule keyed to the freeze re-estimate, not a
  "must consider."
- "≥2/3 models" verdicts with n=3 are fine as *directional* reporting but should never be phrased as
  a rate/proportion; keep per-model coefficients + CIs primary (the design already says this — hold
  the line at write-up).

---

## Fabrication / provenance check

- **Aggregate 96.4% + CC-BY:** **corroborated.** The design's quote "human aggregate agreement with
  the labels is 96.4%" and the CC-BY / `nyu-mll/blimp = cc-by-4.0` claim match `resource/blimp.md`
  (TACL abstract quote, lines 45–54; license line 10, "VERIFIED 2026-06-21"). No over-claim on these.
- **Paradigm names** (`determiner_noun_agreement_1`, `..._with_adjective_1`,
  `regular_plural_subject_verb_agreement_1`, `distractor_agreement_relational_noun`,
  `distractor_agreement_relative_clause`, `npi_present_1`, `only_npi_scope`,
  `sentential_negation_npi_scope`, `existential_there_quantifiers_1`, `wh_island`, `adjunct_island`,
  `coordinate_structure_constraint_*`): **all corroborated** by the 67 filenames listed in
  `resource/blimp.md` (lines 93–116). The stratum set is drawn from real paradigms.
- **Per-paradigm human-agreement numbers** (`det_noun_agr_1=0.958`, `npi_present_1=0.83`,
  `only_npi_scope=0.72`, `wh_island=0.73`, `coordinate_..._subject_extraction=0.514`, range
  ~0.47–0.99): **NOT corroborable from any in-repo file.** `resource/blimp.md` contains zero
  per-paradigm numbers. A repo grep finds these values *only* in the design, the decision page, and
  `wiki/program.md` — all three tracing to the same uncommitted s204 "firsthand fetch." I cannot
  verify them against an in-repo artifact, and (per the brief) I did not fetch the web. **This is not
  an accusation of fabrication** — the design is transparent that these are firsthand-inspected
  examples to be re-fetched + sha256-pinned at freeze — **but it is a provenance gap that must close
  before the anchor is declared** (Blocker 1). At present the design cites a per-paradigm profile at
  a strength `resource/blimp.md` does not support.

**Verdict on this axis:** no fabrication detected; one **material provenance gap** (the per-paradigm
anchor is asserted but not in-repo). Honest self-labeling throughout.

## Anchor discipline

Q3-A's "human-comparison, NOT internal-contrast-only" is **sound and correct** — and importantly it
would be *dishonest* to retreat to `internal-contrast-only` here, because there genuinely is a human
key (per-paradigm `total_mean`). `internal-contrast-only` is the terminal declaration for results
that make *no human comparison*; this result makes one. The profile-Spearman (model difficulty
profile vs human difficulty profile) is a **legitimate human comparison** — it is exactly a contrast
against a human-anchored resource, which is what the `human-comparison` sense tag and the `anchors →
resource` discipline are for. Contamination threatens the **validity** of that comparison (risk §2/
Blocker 3), not its **type**. The right posture is therefore *human-comparison-with-a-contamination-
caveat*, which is what Q3-A says. **Caveat:** the declaration is only *earned* once the per-paradigm
anchor is actually in `resource/blimp.md` (Blocker 1); until then `anchor: pending` is the honest
front-matter state, which the design correctly still carries.

## Methodological risks (ranked)

1. **Under-powered Spearman (Blocker 2)** — the primary reading's instrument resolution is poor at
   n≈10; the headline verdict bands out-run it.
2. **Non-uniform contamination confound (Blocker 3)** — the uniformity assumption is load-bearing,
   untested, and its most likely failure mode (exposure ∝ human-ease) *manufactures* alignment.
3. **Range restriction / saturation** — a special case of §2: if exposure pushes accuracy to ceiling
   on most paradigms, ρ_prof is computed over near-constant values = noise. Needs the pre-registered
   variance guard.
4. **Reading-1/reading-2 confound** — acknowledged in the design (humans also dip on deep
   paradigms). Handled honestly; the residual issue is the mislabeling of reading 2 (SHOULD-FIX §5).
5. **Depth-stratum circularity** — "locality of the licensing dependency," assigned pre-call by a
   written paradigm-agnostic rule, is a *defensible, non-circular* ordering (it is a standard
   structural notion, not fitted to accuracies). The residual risk is that the *choice of which*
   paradigms enter (not their stratum) is a researcher DoF — this is the panel's top concern and the
   Q1 pre-commitment + honest "selected subset" framing is the right, if not complete, mitigation.
   Q1-C removes it entirely.
6. **Position bias** — adequately controlled by Q2-A (both orders + consistency + flip diagnostic);
   the pre-named INSTRUMENT-FAILURE outcome for a flip-rate blowout is good discipline.
7. **Gold-label reliability on low-agreement paradigms (SHOULD-FIX §4)** — real but bounded; fixed by
   a human-agreement floor on the accuracy contrast.

## Freeze conditions (bind the freeze session)

**The one I most insist on:**

> **F1 (BLOCKER). Commit the per-paradigm human anchor and update `resource/blimp.md` before the
> anchor is declared.** Fetch `raw_results/summary/human_validation_summary.csv`, commit it (or a
> pinned representative slice) with its sha256, and extend `wiki/base/resources/blimp.md` to
> catalogue per-paradigm human agreement (the `total_mean` column, the ~0.47–0.99 range, and the
> exact values for every UID used in the sweep). The design's `anchors: resource/blimp` is not
> earned until the resource page actually carries the per-paradigm profile. No model call until this
> lands.

Others (all binding at freeze):

- **F2 (from Blocker 2).** Freeze ≥16 paradigms across strata (or adopt Q1-C); state achieved-n
  power for ρ_prof in PREREG; if n stays low, reading 1 is descriptive-only and non-promotable on
  this run alone.
- **F3 (from Blocker 3).** Pre-register a saturation/range guard: near-zero across-paradigm accuracy
  variance for a model → ρ_prof(m) reported as INCONCLUSIVE, not as a coefficient. Report absolute-
  accuracy dispersion per model as a contamination diagnostic.
- **F4 (from SHOULD-FIX §4).** Set a human-agreement floor (≈0.6) for paradigms entering the
  reading-2 *accuracy* contrast; sub-floor paradigms stay in the profile Spearman but are reported
  descriptively.
- **F5 (from SHOULD-FIX §5).** Resolve the reading-2 label: keep it strictly within-panel, or move
  the "exceeds the human dip" quantity under a human-anchored sub-reading. No human-baselined
  quantity may wear the `internal-contrast-only` label.
- **F6 (panel-vote condition, adopted).** Publish the final **selected** paradigms *and the excluded
  ones with reasons*, plus the paradigm→stratum mapping, decided solely on syntactic/structural
  criteria with no reference to expected model performance — in PREREG, before any model call.
- **F7 (recommended, not blocking).** Add a bounded content-word-swap contamination arm on 2–3
  paradigms (one shallow, one deep).
- Carry the design's own fences: gemini reasoning suppressed/capped; `ABORT_USD`; split-into-two-
  half-sweeps if the freeze re-estimate exceeds $2.50; PREREG committed before any model call;
  independent pre-run critic + non-Anthropic vote at freeze.

## Anti-cheat

- **Positive discipline:** pre-registered ρ bands with an explicit INCONCLUSIVE dead-zone, first-
  class PROFILE-DIVERGES / DEPTH-FLAT / contamination-saturated / instrument-failure nulls, and
  freeze-before-call fencing are all genuinely present and good. The wide inconclusive band makes a
  false positive *harder*, not easier — the right direction.
- **Residual result-seeking risk (concurs with panel):** the **curated Q1-B subset** is the one
  place the design could steer toward the shadow-depth narrative — mitigated (not eliminated) by
  F6/Q1-C.
- **New concern I add:** framing DEPTH-GRADED as "expected" while scoring its interest against the
  human dip (SHOULD-FIX §5) risks letting a partly-baked-in gradient read as a discovered human-
  aligned one. F5 closes this.
- No sign of thresholds or strata reverse-engineered from accuracies; the locality rule is ex-ante
  and structural. Provided F1–F6 hold, I see no move aimed at a desired *result* — only the standard
  curation DoF, adequately fenced.

---

*Decorrelation vote (`gpt-5.4-mini`): GO-WITH-CONDITIONS, Q1-B / Q2-A / Q3-A, top risk curated-subset
fishing, top freeze condition = lock the ex-ante inclusion+stratum rule and publish included/excluded
paradigms. **Convergence:** identical per-gate votes; agreement that Q1 curation is the sharpest
anti-cheat exposure and that Q3-A is relative-evidence-only. **Divergence:** the panel did not flag
(a) the uncommitted anchor or (b) the n≈10 power problem — my two blockers. I weight these as
decisive additions: they do not overturn GO-WITH-CONDITIONS but they add F1–F3 above the panel's
single condition.*
