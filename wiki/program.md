# program.md — the standing program (adopted 2026-07-02)

**What this is.** The project's medium-term working program: the layer between the charter
([`PROJECT.md`](../PROJECT.md), which says *why* and *under what rules*) and [`NEXT.md`](../NEXT.md) (which says *what next
session*). Adopted 2026-07-02 by Tom's standing override
([`decisions/resolved/program-2026-07-adoption`](decisions/resolved/program-2026-07-adoption.md))
from the session-165 external review
([`project-history/20260702-ai-semantics-review-by-fable.md`](../project-history/20260702-ai-semantics-review-by-fable.md)
— read it when an item's rationale is unclear; it is the argued version of this page).

**How sessions use this page.** Read it at cold start, right after [`NEXT.md`](../NEXT.md). Draw bounded
units from the open items below — [`NEXT.md`](../NEXT.md) names the immediate picks, this page holds the
full slate. When a session lands an artifact that advances an item, tick it here (`[x]`, with
the session and artifact) in the same commit. Program items are *direction, not license*:
every existing gate still binds — frozen designs, pre-run critics, post-run verifiers, anchor
discipline, cross-session ratification, the anti-cheat rule. Changing the program itself (not
ticking items) takes a queued decision or Tom.

**The diagnosis in one line** (review Part I): the verification culture is excellent and must
not change, but the loop was spending most of its effort on process and micro-probes while
its claims layer starved — the program points the same discipline at bigger game.

---

## Flagship deliverable: the shadow-depth table

One artifact to build toward across the empirical items: **a table with one row per probed
phenomenon, each row a measured residual-over-matched-distributional-control with its CI**,
ordered along the shadow-depth axis proposed in
[`essay/shadow-depth-cross-cuts-grain`](findings/essays/shadow-depth-cross-cuts-grain.md).
It converts the continuum reading into measurement, unifies five weeks of results, and is
maximally modest: every row is a within-model contrast against a named control, human-anchored
where anchors exist. Rows accumulate as A1/A2 items land; assembling the table (a `result` or
`theory` page) becomes its own unit once ≥2 new controlled rows exist.

## A. Empirical program

- **A1a `[x]` Presupposition distributional control.** Design + run the matched
  surface-cue control the shadow-depth essay names as owed: doppelgänger items (trigger
  word-forms in frames carrying the cue without the presuppositional structure) and
  cue-scrambled variants, so "environment-gated = surface-cue-following" is *tested* the way
  the comparative-correlative's beater status was, not read. Normal freeze/critic/verifier
  gates. **DESIGN landed s172** ([`design/presupposition-doppelganger-control-v1`](../experiments/designs/presupposition-doppelganger-control-v1.md);
  D1 cue-matched non-trigger substitution as the powered residual + D2 descriptive; pre-run critic →
  GO-WITH-CONDITIONS, non-Anthropic vote weighed). Two BLOCKERS **applied this session** (B1: a positive
  residual does *not* license "beats the distributional shadow" — a verb-sensitive surface-cue account
  reconstructs a D1 residual, so the honest prize is the **null**; B2: null/positive not epistemically
  symmetric). **RATIFIED + RUN s173** ([`decisions/resolved/presupposition-doppelganger-control-design`](decisions/resolved/presupposition-doppelganger-control-design.md),
  RATIFY-WITH-NIT; non-Anthropic vote dissented REJECT and was rebutted). → [`result/presupposition-doppelganger-control-v1`](findings/results/presupposition-doppelganger-control-v1.md):
  **VERDICT BEATS-DOPPELGANGER** (pooled +0.78/+0.47/+0.94) but **under-licensed** (B1) — word-form-keyed,
  surface-cue-reconstructable, the essay's revision trigger does **not** fire, the corner does **not** move to the
  beater side, the clean flat null did not obtain; post-run verifier REPRODUCED (0 discrepancies). Revised
  [`essay/shadow-depth-cross-cuts-grain`](findings/essays/shadow-depth-cross-cuts-grain.md) +
  [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md) in-page; anchor decision opened
  ([`decisions/resolved/presupposition-doppelganger-internal-contrast-anchor`](decisions/resolved/presupposition-doppelganger-internal-contrast-anchor.md), ratified s174 → `internal-contrast-only`).
  Froze+ran honoring critic conditions **S1** (drop the definite family from the powered residual),
  **S2** (per-family primary), **S3** (true residual-N ≈64/model, not 128), **S4** (threshold sensitivity).
- **A1b `[ ]` Antonymy shadow-saturation probe.** Run
  [`conjecture/lexical-relation-shadow-saturation`](findings/conjectures/lexical-relation-shadow-saturation.md)
  in its internal-contrast form now — the corpus-side controls are already in-repo (Justeson &
  Katz; Cao co-occurrence data); only the human-compared form stays blocked on its unlicensed
  anchor. **[Corrected s183, per the s182 scout (this page's 2026-07-05 s182 ledger row): the
  corpus-side control *data* are NOT in-repo — only the source-page summaries are. The
  internal-contrast control must be built from scratch (WordNet relation pairs + a co-occurrence
  baseline from in-repo SubTLEX-US or a corpus; `nltk`/WordNet + `numpy` install cleanly), and
  scoring "recovery" without a human gold is the value-laden crux — so A1b is a fresh design +
  decision-trail unit first, run only after cross-session ratification.]**
- **A1c `[x]` Shadow-depth table v1** (s171 → [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md);
  four beater rows — CC covariation, dative info-structure, AANN gradient, sense gradience — each a residual over a
  named distributional control with a 95% CI, plus the antonymy/presupposition corners as marked readings/bets;
  $0, adversarial coherence pass SAFE-TO-LAND. Row-inclusion + presentation choices surfaced as
  [`decisions/resolved/shadow-depth-table-row-inclusion`](decisions/resolved/shadow-depth-table-row-inclusion.md)
  — **ratified s172 (adopt-A on all three; anchor-discipline + modesty PASS); `contingent-on` cleared, table stands as v1**).
- **A2a Powered confirmations (standing habit, now [`PROTOCOL.md`](../PROTOCOL.md) §4).** Any line about to
  carry a claim gets a fresh-item powered re-run at ~100–150 items (~10× founding-era counts;
  still ≲$1 at observed prices) so the claim states a magnitude with an interval, not a
  threshold-pass. Flagship positives owed one each, one at a time:
  sense gradience **`[x]`** (s181 → [`result/lexical-sense-gradience-rep2`](findings/results/lexical-sense-gradience-rep2.md);
  the LAST owed A2a re-run — byte-frozen v1 instrument [`analyze.py` sha-identical; `probe.py` differs only in the input-path constant, `diff`-verified] on **200 fresh DWUG pairs drawn disjoint from v1** [0 shared pairs, asserted + re-verified; 61/357 usages recombine — pair-disjoint, not usage-disjoint], seed 20260705; 1,800 calls **$0.68507**, 0 NA; pre-run critic **NO-GO on B1** [frozen probe read v1's input filename → silent-join hazard] **fixed + smoke-tested before spend** + non-Anthropic vote GO-WITH-CONDITIONS + verifier **REPRODUCED [0 discrepancies, max diff 0.0005/24 stats]**; **REPLICATES 3/3** — every base ρ within v1's CI [durel 0.715/0.528/0.808, cont 0.739/0.631/0.801], topic-partial shadow-beater survives 3/3 both framings; gpt weakest/most-elicitation-sensitive [ordinal 0.528, partial 0.392, down but positive/non-collapsing]; [`claim/lexical-sense-gradience`](findings/claims/lexical-sense-gradience.md) **single-run flag discharged** for the direction/agreement core — NOT usage-independent, NOT a twice-powered independent magnitude. Cost note: gemini $0.174 here vs $2.606 in v1 — the DWUG instrument is **not** reliably >$2.50) · dative information-structure **`[x]`** (s175 → [`result/dative-information-structure-powered`](findings/results/dative-information-structure-powered.md);
  100 fresh disjoint main items, PANEL CONFIRM **3/3 at power**, verifier-REPRODUCED; magnitude+interval attached to
  [`claim/dative-information-structure-givenness`](findings/claims/dative-information-structure-givenness.md) — claude +0.316 [0.298,0.334] / gemini +0.524 [0.506,0.542] / gpt +0.056 [0.039,0.074];
  gpt's v2 WEAK did **not** hold at power (clears zero, recovers v1 +0.056); ~9× spread reproduces) · AANN gradient **`[x]`** (s178 → [`result/aann-behavioral-gradient-rep2`](findings/results/aann-behavioral-gradient-rep2.md);
  second-date fresh-item powered re-run, 408 anchored items **disjoint from v2 (0 shared)** on the byte-frozen v2 instrument + byte-identical human anchor, 1,782 calls $0.3092, 0 missing; pre-run critic GO + non-Anthropic vote GO-WITH-CONDITIONS + verifier **REPRODUCED**; **anchored gradient replicates 3/3** cell ρ 0.692/0.702/0.735 all CIs overlap v2, frequency- and noun-class-guarded; conjecture-level **SUPPORTED via A+C** — gpt Tier-0-excluded 18/24 this occasion [genuine, marginal objects/evaluative items] though its graded gradient is undiminished; the claim's single-run lead caveat **discharged** for the graded gradient) ·
  CC covariation **`[x]`** (s169 → [`result/comparative-correlative-covariation-powered`](findings/results/comparative-correlative-covariation-powered.md);
  136 fresh disjoint items, MAGNITUDE-CONFIRMED, verifier-REPRODUCED — construction-isolation gap ≈87pp
  [lb ≈78], inverse-flip 97–100%, no atypical collapse, 3/3; magnitude+interval attached to
  [`claim/comparative-correlative-covariation`](findings/claims/comparative-correlative-covariation.md)) ·
  environment-gated presupposition `[ ]`.
- **A2b `[ ]` Grounding-magnitude probe via a different instrument.** The highest-information
  unrun probe in the repo: image/vision referents, genuinely unrun ("costs money" — ~$3–4,
  the best purchase available; the grounded cell has a confirming-direction shape datum and an
  untested magnitude). Needs a fresh design + decision trail; the VWSD fluent-channel route is
  closed and stays closed. **[Corrected s183, per the s130 deeper scout + the s182 backlog check
  ([`open-question/grounding-magnitude-instrument`](findings/open-questions/grounding-magnitude-instrument.md)):
  the magnitude is UN-INSTRUMENTABLE with in-repo resources, and an in-house build is barred by
  the no-human-subjects rule — so the realistic A2b unit is a license-checked SCOUT for an
  externally released graded-image fine-polysemy sense set, not a design/run.]**
- **A3a `[x]` (scouted s168) Re-anchor the presupposition line to human projection data.** Scout +
  license-check (never adopt unverified): **CommitmentBank**, **MegaVeridicality** (White &
  Rawlins), the **Tonhauser/Degen projection-variability datasets**, **NOPE**. If adoption
  succeeds, the conditional-antecedent collapse becomes interesting in either direction
  (human ratings dip too → the panel tracks human projection variability; they don't → a
  quantified model–human divergence). Open the anchor decision with the scout results.
  **Done s168:** [`resource/presupposition-projection-human-anchor-scouting`](base/resources/presupposition-projection-human-anchor-scouting.md)
  — **all four datasets license-UNVERIFIED** (no `LICENSE` file in any repo; NOPE's only license
  string is arXiv paper-only CC BY-SA). Anchor decision opened
  ([`decisions/resolved/presupposition-projection-human-anchor`](decisions/resolved/presupposition-projection-human-anchor.md),
  default: adopt none yet, re-scout licenses; CommitmentBank the strongest target *if* a later
  session verifies its terms — the only candidate covering the antecedent-of-conditional).
  **Ratified s169** (ADOPT-A: adopt none yet; the fresh reviewer reproduced the license null).
- **A3b `[ ]` BLiMP forced-choice sweep.** The resource sits idle: 67k human-validated minimal
  pairs, CC-BY, already cataloged. A selected-paradigm sweep (determiner–noun agreement near
  AANN; NPIs; quantifiers) is cheap and human-agreement-anchored. Design + critic first.
- **A3c `[ ]` Lancaster norms $0 re-analysis.** Cross sensorimotor strength with the existing
  lexical results — flagged by the base survey as available without an API call. **[Scope note,
  s183: a moderated re-analysis against the v1 sense-gradience result already ran 2026-05-30 —
  [`result/lexical-perceptual-grounding-moderation-v1`](findings/results/lexical-perceptual-grounding-moderation-v1.md),
  clean null. This item is scoped to crossing the norms with the *post-v1* lexical results (rep2,
  polysemy/homonymy, bridging) — a session that re-runs the v1 cross duplicates done work.]**
- **A4a `[x]` models.md truth-up** (special session 2026-07-02 — panel marked battle-tested).
- **A4b `[ ]` Within-family size ladders on flagship instruments** — **UNBLOCKED s168**
  ([`decisions/resolved/scale-ladder-subjects`](decisions/resolved/scale-ladder-subjects.md)
  ratified ADOPT-A). Does shadow-beating grow, shrink, or hold with capability? Converts the
  standing "single-panel, n=3" caveat into a measured dimension. **Binding first sub-step (the
  ratification condition):** add a mechanical `ladder: true` front-matter field + a senselint check
  forbidding any `supports`/`anchors` link from a ladder-flagged page into a panel-v1 claim/result —
  *no ladder result page may be written before that gate lands*. Riders: "clean first runs" =
  execution-clean, not result-clean; correlated siblings never pooled with the cross-family panel.
- **A4c `[x]` Panel v2 — DECIDED s168 as a sequenced hold**
  ([`decisions/resolved/panel-v2-refresh`](decisions/resolved/panel-v2-refresh.md) ratified ADOPT-A).
  Panel-v1 stays primary for **all** lines; the v2 question re-opens (then decided B-vs-C on
  evidence) the moment **ladder data lands OR `scale-ladder-subjects` is rejected** — the re-open
  trigger is written into [`config/models.md`](../config/models.md) and [`NEXT.md`](../NEXT.md). The
  non-Anthropic vote dissented toward "refresh now"; the fresh reviewer weighed and rebutted it.
- **A4d `[ ]` Logprob supplementary lane** — **UNBLOCKED s168**
  ([`decisions/resolved/logprob-supplementary-lane`](decisions/resolved/logprob-supplementary-lane.md)
  ratified ADOPT-A: re-verify then pilot; a premise-change on
  [`decisions/resolved/aann-panel-logprob-blocker`](decisions/resolved/aann-panel-logprob-blocker.md),
  not a re-litigation). **Gated on:** a $0 live logprob re-verification **recorded with its date in
  [`config/models.md`](../config/models.md) before any pilot**; every logprob-lane result carries a
  senselint-enforced `logprob-lane`/`verdict-bearing:false` contract; never echo/prompt-logprob
  surprisal; pilot only on an already-frozen battery (A3b BLiMP the natural target).
- **A5 `[ ]` Production-side alternation battery.** Extend the dative pattern (the
  best-designed result, anchored to a human *production* direction): free generation scored by
  frozen parsers — given/new manipulations → produced alternant; genitive alternation,
  particle placement, locative alternation, each with published human corpus studies to anchor
  direction. Start with one sibling as a calibrated second row.
- **A6 `[ ]` Cross-linguistic replication scout.** Same-construction/different-surface-statistics
  replication (e.g. the comparative correlative's Japanese counterpart) is one of the strongest
  charter-compatible levers against the distributional-shadow null. Scout open, license-checked
  resources first (UD treebanks in-scope; open Japanese norms exist); one flagship construction.

## B. Consolidation program

- **B1 `[~]` Claims promotion (first landed s168).** Procedure now in [`PROTOCOL.md`](../PROTOCOL.md) §3. Candidates the review
  judged already earned on the corpus's own standards (one promotion review each,
  cross-session, adversarial): CC covariation **`[x]`** (s168 → [`claim/comparative-correlative-covariation`](findings/claims/comparative-correlative-covariation.md),
  `supported`, scoped directional/ordering; magnitude deferred to the A2a powered re-run) ·
  sense-gradience/ungraded-commitment pair **`[x]`** (s176 → [`claim/lexical-sense-gradience`](findings/claims/lexical-sense-gradience.md),
  `supported`, scoped **direction/agreement, single-run-flagged** — the sense-gradience beater; the ungraded-commitment half was
  already promoted s77 → [`claim/lexical-graded-scale-ungraded-commitment`](findings/claims/lexical-graded-scale-ungraded-commitment.md),
  so the **pair is complete**) · AANN behavioral gradient **`[x]`** (s176 → [`claim/aann-behavioral-gradient`](findings/claims/aann-behavioral-gradient.md),
  `supported`, scoped **Tier-2 gradient tracking, single-run**; overall held-out replication holds but is **noun-class-dependent —
  temporal stratum negative** [v2b]; distinct from the Tier-0 form claim and the Tier-4 inferential line) ·
  dative information-structure **`[x]`** (s174 → [`claim/dative-information-structure-givenness`](findings/claims/dative-information-structure-givenness.md),
  `supported`, scoped **2/3** directional/ordering — claude+gemini robust, gpt WEAK; magnitude deferred to the A2a powered re-run) ·
  output-channel/working-surface **`[x]`** (s177 → [`claim/output-channel-working-surface`](findings/claims/output-channel-working-surface.md),
  `supported`, scoped **methodological + task/panel/date-indexed** — a forced terse channel can mask a serial-inference
  capability, format-only working surface flips the verdict, replicated across two task families + three geometry axes,
  with the bridging-context boundary control and gpt's non-uptake/partial-residual third state kept explicit; human-anchored
  leg to Scivetti CxNLI, composition legs internal-contrast per their own ratified pages) ·
  environment-gated presupposition `[ ]`.
- **B2 `[x]` Theory second editions — both done (s177 constructional, s179 situating).**
  [`theory/constructional-meaning-in-llms`](findings/theory/constructional-meaning-in-llms.md)
  (a changelog) **`[x]`** (s177 → [`theory/constructional-meaning-in-llms-v2`](findings/theory/constructional-meaning-in-llms-v2.md);
  the repo's **first `supersedes` edition** — old page `status: superseded` with a banner, kept visible; position restated
  around the four promoted beater claims + the powered re-runs + the shadow-depth table; links pruned 50+ → 33) and
  [`theory/situating-llm-meaning`](findings/theory/situating-llm-meaning.md)
  (caveat-saturated) **`[x]`** (s179 → [`theory/situating-llm-meaning-v2`](findings/theory/situating-llm-meaning-v2.md);
  the second `supersedes` edition, following the s177 convention exactly — new `-v2` page, `rel: supersedes` first in `links:`,
  old page `status: superseded` + banner after H1, body byte-untouched; position restated around the five promoted claims,
  the two powered magnitudes [dative 3/3, CC], the cross-date-replicated AANN gradient the old page's revision hook awaited,
  and the flagship shadow-depth table; **no cell relocated** — the map is better-anchored, not bolder; one new unplaced seed logged
  [form-ceiling wobbles while the graded gradient holds]; fresh-agent adversarial coherence pass **no BLOCKERS**, 1 SHOULD-FIX + 1 NIT fixed; $0):
  rewrite each as a clean edition stating the current position; archive the old page under a `supersedes` link. Standing rule
  (PROTOCOL §3): >3 update boxes forces an edition.
- **B3 `[~]` Essay-family merges + an ideas index.** **Ideas index DONE `[x]`** (s182 →
  [`ideas.md`](ideas.md); the ~50 essays sorted into **12 genuinely distinct contributions** [8
  substantive + 4 methodological], two-line abstract + member essays each; 5 parallel read-only
  extractors → orchestrator synthesis [judgement not parallelized] → adversarial coherence pass
  **NO BLOCKERS**; $0). The **merges are deprioritized** on an s182 finding: the named families are
  **not redundant clutter but a densely cross-referenced web** (undischargeable-negative alone is
  cited by ~30 pages; each family member carries its own [`predictions.md`](predictions.md) bets +
  revision triggers cited by name), so destructive merges are high-churn / low-reader-gain — the
  **additive index delivers B3's goal** (surface the distinct ideas) without disturbing the graph.
  Revisit a merge only for a genuinely-redundant, lightly-cited draft pair (none found among the
  four families): undischargeable-negative family `[~ deprioritized]`; summary-hides-variation
  `[~ deprioritized]`; sense-commitment `[~ deprioritized]`; thin-update `[~ deprioritized]`.
  New-essay bar in PROTOCOL §3.
- **B4 Reading surfaces.** index.md slimmed + generated `[x]` (special session 2026-07-02,
  `tools/build-index.py`); executive summary relabeled a checkpoint digest `[x]` — **full
  regeneration DONE `[x]`** (s183, wiki-coherence campaign P1 →
  [`executive-summary.md`](executive-summary.md) rewritten current through the six promoted
  claims, four powered replications, both theory second editions, the flagship table, and the
  honest negatives; the next regeneration is owed at the next consolidation *checkpoint*, not on
  a fixed clock); public home-page "latest" repaired `[x]`; models.md `[x]`.
- **B5 `[x]` Prediction ledger.** [`predictions.md`](predictions.md) seeded `[x]`; **back-fill
  sweep DONE** (s180 → the full historical sweep: all 18 conjectures, 50 essays, 8 theory pages
  read via parallel extractors, each bet quoted verbatim with status taken only from on-page
  text, integrated and adversarially re-verified [no BLOCKERs, 2 SHOULD-FIX applied]). Rebuilt
  as three sections — §A resolved bets (the calibration record; dozens of past predictions with
  their landed outcomes), §B open project-runnable bets, §C standing revision triggers *not*
  scored (external-contingent / self-discipline), with the scope rule and dedup/co-registration
  convention documented on-page. $0.
- **B6 `note` page type.** Type + lint mapping added `[x]`; **reclassification sweep owed
  `[ ]`**: ~10 result pages that contain no measurement ($0 build gates, calibration NO-GOs,
  re-analyses) become `note` pages (create `wiki/findings/notes/` with the first one; each
  reclassification states why; links updated).

## C. Process rules (where each now lives)

- **C1 Fewer, deeper.** Prefer larger bounded units; a powered run beats several micro-probes;
  a session with nothing substantive owed does a light check and stops — [`PROTOCOL.md`](../PROTOCOL.md) §0/§A1.
- **C2 Website cadence — ruled by Tom:** one journal entry per JST day, no clock stamps —
  [`PROTOCOL.md`](../PROTOCOL.md) §5b.
- **C3 `[x]` Close the founding open questions** (s170 → closure argued in
  [`theory/lexicon-grammar-continuum`](findings/theory/lexicon-grammar-continuum.md) § "Closing the two
  founding open-questions"; both open-questions marked `answered`).
  [`open-question/constructional-vs-frequency-confound`](findings/open-questions/constructional-vs-frequency-confound.md)
  answered by the shadow-control apparatus (matched same-material control + measured residual; worked
  exemplar the CC ≈87pp gap, closed-weight bound stated); and
  [`open-question/distributional-vs-inferential-constructional`](findings/open-questions/distributional-vs-inferential-constructional.md)
  answered *thinly* by the shadow-depth positioning (inferential role secured 1/3 models via cross-instrument
  convergence; boundary a shadow-depth gradient; residual thread re-homed, not re-filed as a founding question).
- **C4 Instrument stopping rule** — [`PROTOCOL.md`](../PROTOCOL.md) §3.
- **C5 Decorrelated review votes** — [`PROTOCOL.md`](../PROTOCOL.md) §2/§A3.

## D. Levers held by Tom (information, not requests — the project never asks)

- **D1 Cadence:** Routine frequency is set outside the repo; the review recommends fewer,
  longer sessions (C1 lets the project meet him halfway).
- **D2 Surprisal lane:** one Together/Fireworks-class API key would un-terminate the cleanest
  graded instrument (per-token surprisal; the frozen AANN Option-A design; open-weight family
  decorrelation). Feasibility preserved in
  [`decisions/resolved/cloud-compute-path`](decisions/resolved/cloud-compute-path.md). Dormant;
  nothing waits on it.
- **D3 Ratify the queued subject decisions** at will (the three under `decisions/open/`);
  otherwise the normal cross-session process handles them. **[Discharged: all three were ratified
  autonomously s168; `decisions/open/` has been empty since — the lever that remains live for Tom
  is the panel-v2 re-open trigger recorded in [`config/models.md`](../config/models.md).]**
- **D4 Paywalled ingestion:** the OA-reachable literature is near-exhausted;
  [`wiki/base/wanted.md`](base/wanted.md) documents each unreachable primary (Goldberg 1995/2006, Kaplan, the
  Sterken & Cappelen volume, …). A small batch would raise the philosophical track's ceiling.

## What must not change (review Part III — binding)

The modesty/anti-cheat/null-writing discipline; freeze-before-run, independent pre-run
critics, recompute-from-raw verifiers; cross-session adversarial ratification with Tom's
standing override; page typing, typed links, meaning-sense tagging, senselint/linkify gates;
the two-track structure; the site's plain-language honesty; the refusal to fabricate around
unreachable resources. Every program item above is compatible with these; several (A1, B5,
B6, C4) extend them.

## Status ledger

| Date | Item | What landed |
|------|------|-------------|
| 2026-07-05 (s182) | B3 | **Ideas index built — the B3 "the ideas" sub-item; the merges deprioritized.** → [`ideas.md`](ideas.md): an additive reading index sorting the ~50 essays into **12 genuinely distinct contributions** (8 substantive positions on meaning + 4 methodological/measurement-epistemic disciplines), a two-line abstract + member essays (anchor first) each; **all 50 essays map to exactly one primary cluster** (coherence-pass verified). Workflow mode: 5 parallel read-only extractors over all 50 essays → orchestrator synthesis (judgement not parallelized) → 1 read-only adversarial coherence pass (**NO BLOCKERS**; 1 SHOULD-FIX [presence-is-not-balance filed by topic in §4 is also cluster-12's "Messick's two threats" material — cross-referenced in both] + 1 NIT [cluster-1 pole-split hedge tightened] applied). Wired into the [`index.md`](index.md) standing-refs header; stale header theory links retargeted to the **-v2** second editions. **The finding that re-scoped B3:** the named merge families are **not redundant clutter but a load-bearing, densely cross-referenced web** — [`essay/undischargeable-negative`](findings/essays/undischargeable-negative.md) is the single most-cited essay (~30 pages), the reading-discipline essays a dozen-plus each, each carrying its own [`predictions.md`](predictions.md) bets + revision triggers cited elsewhere → destructive merges are high-churn / low-value; the **additive index is the B3 lever**, merges deprioritized. Also recorded for the empirical backlog: **A2b** grounding-magnitude is un-instrumentable in-repo (an *external* resource is owed, not a design); **A1b** antonymy has no in-repo control data (a *build-from-scratch* design is owed; `nltk`/`numpy` install cleanly). $0 (no probe, no votes); website rolled up (JST 2026-07-05 entry extended to s179–s182). |
| 2026-07-05 (s181) | A2a | **Lexical sense-gradience cross-date re-run — the LAST owed A2a re-run; single-run flag discharged (replicates 3/3).** → [`result/lexical-sense-gradience-rep2`](findings/results/lexical-sense-gradience-rep2.md): the byte-frozen v1 sense-gradience instrument (`analyze.py` sha-identical; `probe.py` differs only in the single input-path constant, `diff`-verified) on **200 fresh DWUG EN pairs drawn disjoint from v1** (seed 20260705; every v1 pair excluded pre-sampling → **0 shared pairs**, asserted + independently re-verified; 61/357 usages recombine — **pair-disjoint, not usage-disjoint**), fresh date, DWUG archive sha identical to v1. Workflow mode: independent fresh-agent **pre-run critic → NO-GO on B1** (the frozen `probe.py` read v1's input filename, risking a silent v1-preds/rep2-gold join on colliding `lx-{level}-{idx}` ids) **→ fixed** (point the single `FULLTEXT` constant at the rep2 items) **+ smoke-tested before spend** (ids match manifest, 1-item live call parses all framings, $0.002) + one non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`, **GO-WITH-CONDITIONS**, all conditions honored); `probe.py` **1,800 calls, 0 NA, 0 missing cost**; independent fresh-agent **post-run verifier REPRODUCED** (0 discrepancies, max abs diff 0.0005/24 stats; disjointness + anti-cheat independently confirmed). **VERDICT REPLICATES 3/3**: every base ρ within v1's 95% CI, all CIs overlap (durel 0.715/0.528/0.808, cont 0.739/0.631/0.801), topic-partial shadow-beater survives 3/3 both framings (0.60/0.39/0.66 durel); gpt weakest/most-elicitation-sensitive (ordinal 0.528, partial\|topic 0.392 — down from v1, still positive/non-collapsing). [`claim/lexical-sense-gradience`](findings/claims/lexical-sense-gradience.md) **single-run flag discharged** for the direction/agreement core (NOT usage-independent, NOT a twice-powered independent magnitude); shadow-depth-table row + [`predictions.md`](predictions.md) shadow-beaters bet (now **fired-for both halves**) updated. **$0.68507 billed** (day UTC 2026-07-05, fresh $0.00 prior; far below v1's $3.134 — gemini's reasoning burn was an anomaly). Website rolled up (JST 2026-07-05 entry extended to s179–s181). |
| 2026-07-05 (s180) | B5 | **Prediction-ledger back-fill sweep — DONE.** [`predictions.md`](predictions.md) rebuilt from a handful of seeded rows into the full scored ledger. Workflow mode: 5 parallel read-only extractors (3 essay slices + conjectures + theory) swept all 18 conjectures, 50 essays, 8 theory pages, each registered bet returned with a verbatim on-page quote and status taken *only* from on-page text; orchestrator integrated (judgement not parallelized), a fresh read-only adversarial verifier re-checked every §A status + a quote/number/link sample against source pages → **no BLOCKERs**, 2 SHOULD-FIX applied (a `fired-against`→`discharged` relabel on the doppelgänger trigger to match the essay's own status word; a two-topics (d) double-registration collapsed). Structured as **§A resolved bets** (the calibration record — ~50 predictions with their landed outcomes, including the honest losses: commutativity falsified, cross-level dissolution, ambiguity kind-reading retracted, cross-axis ordering disconfirmed), **§B open project-runnable bets**, **§C standing triggers not scored** (external-contingent + self-discipline, named per page). Scope rule (what earns a scored row) + one-row-per-bet dedup/co-registration convention documented on-page. $0 (no probe, no votes); website rolled up (JST 2026-07-05 entry extended to cover s179–s180). |
| 2026-07-05 (s179) | B2 | **Second theory second edition — the `situating-llm-meaning` philosophical map.** → [`theory/situating-llm-meaning-v2`](findings/theory/situating-llm-meaning-v2.md): the repo's **second `supersedes` edition** (s177 convention followed exactly — new `-v2` page with `rel: supersedes` first in `links:`; old page → `status: superseded` + banner after H1, body byte-untouched, history visible). The caveat-saturated first edition (>3 update boxes, and it pre-dated the AANN line entirely) restated cleanly around what now exists: the **five promoted claims** (CC, dative, sense-gradience, AANN, output-channel/working-surface), the **two powered magnitudes** (dative 3/3 at N=100; CC ≈87 pp), the **cross-date-replicated AANN gradient** the old page's revision hook explicitly awaited, and the flagship [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md) as the measured backbone of the "beats but does not escape the shadow" verdict. The honest headline: folding in a week of stronger evidence **relocated no cell** — the synthesis location (model-internal, thin-inferential, use-based, graded, narrow, compositional at the construction grain; not referential/grounded/relationally-constituted/thickly-inferential) is unchanged, only better-anchored. One genuinely new observation logged **without placing it**: the AANN cross-date wrinkle that a model's coarse binary form-ceiling can be *more* fragile at the margin than its graded sensitivity (a possible essay/in-page-revision seed, flagged for a later session against the PROTOCOL §3 bar). Fresh-agent adversarial coherence pass: **no BLOCKERS** (every load-bearing number verified against its source; conventions confirmed; superseded body byte-untouched); 1 SHOULD-FIX (stale "more capable decoders" dative framing) + 1 NIT (Tier-0 floor 22→23/24) both fixed. B2 complete. $0 (no probe, no votes); website rolled up (JST 2026-07-05 journal entry). |
| 2026-07-04 (s178) | A2a | **AANN gradient powered re-run — the owed cross-date replication.** → [`result/aann-behavioral-gradient-rep2`](findings/results/aann-behavioral-gradient-rep2.md): the byte-frozen v2 instrument (probe.py/analyze.py sha-verified) on **408 fresh anchored items drawn disjoint from v2 (0 shared surface items)**, against the **byte-identical human anchor**, seed 20260704; 1,782 calls, **$0.3092 billed, 0 missing**; fresh-agent pre-run critic **GO** + one non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`) **GO-WITH-CONDITIONS** ($0.002071, all 3 conditions honored) + fresh-agent post-run verifier **REPRODUCED (0 discrepancies)**. **The frequency- and noun-class-guarded anchored gradient replicates cross-date 3/3** — cell ρ **0.692 [0.603,0.762] / 0.702 [0.617,0.770] / 0.735 [0.658,0.795]**, every CI overlapping v2, partial-ρ\|Zipf 0.687/0.690/0.722 — discharging the claim's single-run lead caveat for the **graded gradient**. Conjecture-level **SUPPORTED replicates via A+C**, with an honest new wrinkle: **gpt-5.4-mini's Tier-0 manipulation check dropped to 18/24** (genuine, clean misses, all on the marginal *objects + negative-evaluative* items) → **Tier-0-excluded from the support count** even though its graded gradient is undiminished (0.702, CI overlaps v2) — the coarse binary form-ceiling can wobble at the margin while the graded gradient holds. Held-out overall positive re-passed 3/3 (same items, 2nd date); temporal hole reproduced for A, C. [`claim/aann-behavioral-gradient`](findings/claims/aann-behavioral-gradient.md) update box + Bounds amended; shadow-depth table AANN row updated. No predictions.md row owed (conjecture already `tested`). Day UTC 2026-07-04 (Tom's $10 grant): probe $0.3092 + vote $0.002071 + liveness $0.000495. |
| 2026-07-04 (s177) | B1, B2 | **Two deep consolidation/theory units.** (1) **B1 fifth promotion** → [`claim/output-channel-working-surface`](findings/claims/output-channel-working-surface.md): the output-channel/working-surface line promoted (cross-session, independent, adversarial review + one non-Anthropic decorrelation vote, **PROMOTE WITH NARROWER SCOPE — narrowings adopted**, $0.0038655). Scoped **methodological, task/panel/date-indexed**: a forced terse output channel can mask a serial-inference capability; a format-only working surface flips the verdict, replicated across **two task families** (relational composition; let-alone scalar NLI, the latter human-anchored to the Scivetti CxNLI ≈0.90 baseline) and **three geometry axes**; the bridging-context null is carried as the boundary control (the effect is computation-specific, not universal), and gpt's non-uptake vs. partial channel-controlled residual (0.636 [0.466,0.778], 5/5 runs < 0.90) is kept as an explicit third state. 5 of 6 B1 candidates now promoted (environment-gated presupposition remains). (2) **B2 first theory second edition** → [`theory/constructional-meaning-in-llms-v2`](findings/theory/constructional-meaning-in-llms-v2.md): the repo's **first `supersedes` edition** (convention set: new `-v2` page with `rel: supersedes` first in `links:`; old page → `status: superseded` + banner, body untouched, history visible). Position restated cleanly around the four promoted beater claims + powered magnitudes + the flagship table; dative updated to the powered 3/3/~9× truth; AANN single-run + temporal-fail caveats carried; links pruned 50+ → 33. Coherence pass caught **1 BLOCKER** (v2 froze the gpt let-alone story at its June state, contradicting the sibling claim — fixed + cross-linked) + 2 SHOULD-FIX + NITs (fixed) → SAFE-TO-LAND. Also reconciled the stale DWUG anchor-contingency box (s176 flag). $0.0038655 (one vote), UTC 2026-07-04. |
| 2026-07-04 (s176) | B1 (+ flagship A1c) | **Claims layer for the flagship shadow-depth table COMPLETED** — the two remaining beater rows promoted (each a cross-session, independent, adversarial promotion review [`PROTOCOL.md §3`], **plus one non-Anthropic decorrelation vote each** via the probe REST path, both **PROMOTE-SCOPED** convergent, votes $0.003639): [`claim/lexical-sense-gradience`](findings/claims/lexical-sense-gradience.md) (single powered run **N=200**, **direction/agreement scope, single-run-flagged** — the sense-gradience beater; with the ungraded-commitment half already promoted s77, the B1 "pair" is complete) and [`claim/aann-behavioral-gradient`](findings/claims/aann-behavioral-gradient.md) (single powered run + a **partial** held-out replication — temporal stratum uniformly negative [v2b]; **Tier-2** gradient tracking, kept distinct from the **Tier-0** form ceiling and the **Tier-4** inferential PARTIAL line). Fresh-agent adversarial **coherence pass** caught **1 BLOCKER** (a verbatim quote misattributed to the result page — actually the conjecture's, and recontextualized; **fixed**) + 4 NITs (**fixed**) → SAFE-TO-LAND. [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md) refreshed in-place: **all four** beater rows (CC, dative, AANN, sense-gradience) now cite `claim` pages; Honesty box 2 updated (the stale "dative 2/3, others proposed" line corrected). Consolidation lean, no probe; **$0.003639** (two votes), UTC 2026-07-04. |
| 2026-07-04 (s175) | A2a | **Owed dative powered re-run landed** → [`result/dative-information-structure-powered`](findings/results/dative-information-structure-powered.md): 100 fresh disjoint main items + 12 control (0 shared items/contexts with v1/v2); byte-frozen v1/v2 instrument; certification PASS; fresh-agent pre-run critic **GO**, non-Anthropic vote NO-GO **weighed and rebutted** (its GO-condition — frozen roster + fixed panel rule — already met by the standing panel + byte-identical frozen verdict map); post-run verifier **REPRODUCED** (0 doc-pref mismatches; gpt's borderline CONFIRM robust across 50 seeds). **PANEL CONFIRM 3/3 at power**; magnitude+interval attached to [`claim/dative-information-structure-givenness`](findings/claims/dative-information-structure-givenness.md) — claude +0.316 [0.298,0.334] / gemini +0.524 [0.506,0.542] / gpt +0.056 [0.039,0.074]. **gpt's v2 WEAK did NOT hold at power** (clears zero, recovers its v1 +0.056 — v2's +0.018 dip was founding-N item noise); **order-of-magnitude spread reproduces** (~9.3× = v1's 9×, not v2's 27×), firming [`essay/concordant-verdict-hides-spread`](findings/essays/concordant-verdict-hides-spread.md) trigger (c) (predictions row updated). Billed $4.324 (finding-bearing), day's only spend, spanned the UTC midnight boundary. |
| 2026-07-03 (s174) | RECONCILE, B1, phil | **Ratified `presupposition-doppelganger-internal-contrast-anchor`** (s173-opened) → **ADOPT A (`internal-contrast-only`)**; autonomous adversarial review (fresh agent traced the full `analyze.py`/`prep.py` scoring path — no human key enters, anti-cheat orthogonal to the BEATS/SATURATED/MIXED verdict) + one non-Anthropic vote **CONVERGED** on A. [`result/presupposition-doppelganger-control-v1`](findings/results/presupposition-doppelganger-control-v1.md) anchor `pending → internal-contrast-only`, `contingent-on` cleared. **B1 dative promotion** → [`claim/dative-information-structure-givenness`](findings/claims/dative-information-structure-givenness.md) (the twice-observed givenness beater; `supported`, **2/3** direction-only, magnitude deferred to A2a); the flagship [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md) dative row now cites the claim. **Philosophical** → [`essay/under-licensed-middle`](findings/essays/under-licensed-middle.md): the under-licensed middle as a property of the **instrument** — a word-varying matched control can reach only {saturated, under-licensed}, never a clean beater, so "beater" and "under-licensed middle" are outputs of two different instruments; new falsifiable bet (the cleft construction-grain battery) registered in [`predictions.md`](predictions.md). Fresh-agent coherence pass NO-BLOCKERS (quote integrity + governance verified vs. code). $0.0013 (one non-Anthropic vote). |
| 2026-07-03 (s173) | RECONCILE, A1a | **Ratified `presupposition-doppelganger-control-design`** (RATIFY-WITH-NIT; autonomous adversarial review + one non-Anthropic vote that **dissented REJECT and was weighed and rebutted**; design `contingent-on` cleared). **A1a FROZEN + RUN** → [`result/presupposition-doppelganger-control-v1`](findings/results/presupposition-doppelganger-control-v1.md): the matched surface-cue doppelgänger control (22 scenarios, 594 calls, honoring S1–S4). **VERDICT BEATS-DOPPELGANGER** (pooled +0.78/+0.47/+0.94; per-family factive 3/3, aspectual 3/3, cleft 2/3 with gpt control-failing; robust across all 9 S4 cutoffs) — but **UNDER-LICENSED** (B1/B2): word-form-keyed, surface-cue-reconstructable, so it does **not** beat the distributional shadow and does **not** move the corner to the beater side; the clean flat null did **not** obtain. Pre-run critic GO + non-Anthropic GO-WITH-NIT; post-run verifier REPRODUCED (0 discrepancies). Revised [`essay/shadow-depth-cross-cuts-grain`](findings/essays/shadow-depth-cross-cuts-grain.md) + [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md) in-page. Anchor decision opened (`presupposition-doppelganger-internal-contrast-anchor`, s174+). $0.107 ($0.103 probe + votes/pre-flight). |
| 2026-07-03 (s172) | RECONCILE, A1a | **Ratified `shadow-depth-table-row-inclusion`** (adopt-A ×3; autonomous adversarial review + non-Anthropic vote; anchor-discipline + modesty PASS; table `contingent-on` cleared, stands as v1). **A1a design landed** → [`design/presupposition-doppelganger-control-v1`](../experiments/designs/presupposition-doppelganger-control-v1.md) (matched surface-cue doppelgänger control; pre-run critic GO-WITH-CONDITIONS; two BLOCKERS applied this session — a positive residual does *not* license "beats the shadow", the **null** is the diagnostic prize; S1–S4 carried to the freezing session). Opened [`decisions/resolved/presupposition-doppelganger-control-design`](decisions/resolved/presupposition-doppelganger-control-design.md) (s172, ratified s173). Freeze+run owed next. $0.006 (two panel votes). |
| 2026-07-03 (s171) | A1c | **Flagship shadow-depth table v1 assembled** → [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md): five weeks of results as one measured object sorted by shadow-depth. Four beater rows (residual over a named distributional control + 95% CI, at both grains: CC ≈87pp internal-contrast; dative within-item shift 2/3; AANN partial-ρ\|freq human-anchored; sense gradience partial-ρ\|topic human-anchored) beside two saturated corners marked as readings/bets (presupposition, antonymy — controls owed). No new measurement, no new human comparison, no cross-row magnitude comparison. Row-inclusion/presentation surfaced as [`decisions/resolved/shadow-depth-table-row-inclusion`](decisions/resolved/shadow-depth-table-row-inclusion.md) (ratified s172); table `contingent-on` it. $0; fresh-agent adversarial coherence pass → SAFE TO LAND (2 NITs fixed). |
| 2026-07-02 | adoption | Program adopted (Tom); institutional layer built (special session): program page, PROTOCOL §3–§4, generated index, note type, predictions.md seed, models.md truth-up, site repairs, three subject decisions queued. |
| 2026-07-02 (s170) | C3 | **Both founding open-questions closed** (`answered`): the frequency-confound and the distributional-vs-inferential questions (both 2026-05-28) consolidated into [`theory/lexicon-grammar-continuum`](findings/theory/lexicon-grammar-continuum.md)'s new closure section. Q1 answered by the shadow-control apparatus (matched same-material control + measured residual; CC ≈87pp exemplar; closed-weight bound kept honest); Q2 answered *thinly* — inferential role secured 1/3 models via cross-instrument convergence, boundary a shadow-depth gradient, residual thread re-homed. Philosophical/consolidation unit; $0. |
| 2026-07-02 (s169) | A2a, A3a | **A2a first powered confirmation landed:** CC covariation → [`result/comparative-correlative-covariation-powered`](findings/results/comparative-correlative-covariation-powered.md) (136 fresh disjoint items on the byte-frozen v1 instrument; MAGNITUDE-CONFIRMED; pre-run critic + non-Anthropic vote GO, post-run verifier REPRODUCED 0 discrepancies). Construction-isolation assertion gap ≈87pp [95% CI lb ≈78], inverse-flip 97–100%, no atypical collapse, 3/3 — magnitude+interval attached to the CC claim (was direction-only). $0.531 billed. **A3a decision RATIFIED:** the s168-opened human-projection-anchor decision → resolved ADOPT-A (adopt none yet; all four datasets still license-unverified — fresh reviewer reproduced the null via GitHub HTML repo pages; non-Anthropic vote converged). |
| 2026-07-02 (s168) | A4b/A4c/A4d, A3a, B1 | All three queued subject decisions **ratified** (autonomous adversarial review + non-Anthropic votes): scale-ladder ADOPT-A (A4b unblocked, mechanical `ladder` flag owed first), panel-v2 ADOPT-A sequenced-hold with re-open trigger (A4c decided), logprob-lane ADOPT-A (A4d unblocked, re-verify-then-pilot). **A3a** presupposition human-projection-anchor scout landed ($0): all 4 datasets license-UNVERIFIED → anchor decision opened (adopt none yet). **B1** first claims-promotion review landed: CC covariation → [`claim/comparative-correlative-covariation`](findings/claims/comparative-correlative-covariation.md) (`supported`, scoped directional; magnitude deferred to A2a). |
