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

- **A1a `[ ]` Presupposition distributional control.** Design + run the matched
  surface-cue control the shadow-depth essay names as owed: doppelgänger items (trigger
  word-forms in frames carrying the cue without the presuppositional structure) and
  cue-scrambled variants, so "environment-gated = surface-cue-following" is *tested* the way
  the comparative-correlative's beater status was, not read. Normal freeze/critic/verifier
  gates.
- **A1b `[ ]` Antonymy shadow-saturation probe.** Run
  [`conjecture/lexical-relation-shadow-saturation`](findings/conjectures/lexical-relation-shadow-saturation.md)
  in its internal-contrast form now — the corpus-side controls are already in-repo (Justeson &
  Katz; Cao co-occurrence data); only the human-compared form stays blocked on its unlicensed
  anchor.
- **A1c `[x]` Shadow-depth table v1** (s171 → [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md);
  four beater rows — CC covariation, dative info-structure, AANN gradient, sense gradience — each a residual over a
  named distributional control with a 95% CI, plus the antonymy/presupposition corners as marked readings/bets;
  $0, adversarial coherence pass SAFE-TO-LAND. Row-inclusion + presentation choices surfaced as
  [`decisions/open/shadow-depth-table-row-inclusion`](decisions/open/shadow-depth-table-row-inclusion.md)
  — table `contingent-on` it, pending cross-session ratification).
- **A2a Powered confirmations (standing habit, now [`PROTOCOL.md`](../PROTOCOL.md) §4).** Any line about to
  carry a claim gets a fresh-item powered re-run at ~100–150 items (~10× founding-era counts;
  still ≲$1 at observed prices) so the claim states a magnitude with an interval, not a
  threshold-pass. Flagship positives owed one each, one at a time:
  sense gradience `[ ]` · dative information-structure `[ ]` · AANN gradient `[ ]` ·
  CC covariation **`[x]`** (s169 → [`result/comparative-correlative-covariation-powered`](findings/results/comparative-correlative-covariation-powered.md);
  136 fresh disjoint items, MAGNITUDE-CONFIRMED, verifier-REPRODUCED — construction-isolation gap ≈87pp
  [lb ≈78], inverse-flip 97–100%, no atypical collapse, 3/3; magnitude+interval attached to
  [`claim/comparative-correlative-covariation`](findings/claims/comparative-correlative-covariation.md)) ·
  environment-gated presupposition `[ ]`.
- **A2b `[ ]` Grounding-magnitude probe via a different instrument.** The highest-information
  unrun probe in the repo: image/vision referents, genuinely unrun ("costs money" — ~$3–4,
  the best purchase available; the grounded cell has a confirming-direction shape datum and an
  untested magnitude). Needs a fresh design + decision trail; the VWSD fluent-channel route is
  closed and stays closed.
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
- **A3b `[ ]` BLiMP forced-choice sweep.** The resource sits idle: 67k human-validated minimal
  pairs, CC-BY, already cataloged. A selected-paradigm sweep (determiner–noun agreement near
  AANN; NPIs; quantifiers) is cheap and human-agreement-anchored. Design + critic first.
- **A3c `[ ]` Lancaster norms $0 re-analysis.** Cross sensorimotor strength with the existing
  lexical results — flagged by the base survey as available without an API call.
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
  sense-gradience/ungraded-commitment pair `[ ]` · AANN behavioral gradient `[ ]` ·
  dative information-structure `[ ]` · output-channel/working-surface `[ ]` ·
  environment-gated presupposition `[ ]`.
- **B2 `[ ]` Theory second editions.**
  [`theory/constructional-meaning-in-llms`](findings/theory/constructional-meaning-in-llms.md)
  (a changelog) `[ ]` and
  [`theory/situating-llm-meaning`](findings/theory/situating-llm-meaning.md)
  (caveat-saturated) `[ ]`: rewrite each as a clean edition stating the current position;
  archive the old page under a `supersedes` link. Standing rule (PROTOCOL §3): >3 update boxes
  forces an edition.
- **B3 `[ ]` Essay-family merges + an ideas index.** Merge into one canonical essay each (with
  kept-visible history): the undischargeable-negative family (6) `[ ]`; the
  summary-hides-variation trio `[ ]`; the sense-commitment knot `[ ]`; the thin-update quartet
  `[ ]`. Then curate a short "the ideas" index (the ~10 genuinely distinct contributions,
  two-line abstracts) `[ ]`. New-essay bar now in PROTOCOL §3.
- **B4 Reading surfaces.** index.md slimmed + generated `[x]` (special session 2026-07-02,
  `tools/build-index.py`); executive summary relabeled a checkpoint digest `[x]` — **full
  regeneration owed `[ ]`** at the first consolidation session; public home-page "latest"
  repaired `[x]`; models.md `[x]`.
- **B5 Prediction ledger.** [`predictions.md`](predictions.md) seeded `[x]`; **back-fill sweep
  owed `[ ]`** (collect every registered bet: theory predicts/forbids, essay revision
  triggers, conjecture criteria — verify each against its page; no unverified rows).
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
  otherwise the normal cross-session process handles them.
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
| 2026-07-03 (s171) | A1c | **Flagship shadow-depth table v1 assembled** → [`theory/shadow-depth-table-v1`](findings/theory/shadow-depth-table-v1.md): five weeks of results as one measured object sorted by shadow-depth. Four beater rows (residual over a named distributional control + 95% CI, at both grains: CC ≈87pp internal-contrast; dative within-item shift 2/3; AANN partial-ρ\|freq human-anchored; sense gradience partial-ρ\|topic human-anchored) beside two saturated corners marked as readings/bets (presupposition, antonymy — controls owed). No new measurement, no new human comparison, no cross-row magnitude comparison. Row-inclusion/presentation surfaced as [`decisions/open/shadow-depth-table-row-inclusion`](decisions/open/shadow-depth-table-row-inclusion.md); table `contingent-on` it. $0; fresh-agent adversarial coherence pass → SAFE TO LAND (2 NITs fixed). |
| 2026-07-02 | adoption | Program adopted (Tom); institutional layer built (special session): program page, PROTOCOL §3–§4, generated index, note type, predictions.md seed, models.md truth-up, site repairs, three subject decisions queued. |
| 2026-07-02 (s170) | C3 | **Both founding open-questions closed** (`answered`): the frequency-confound and the distributional-vs-inferential questions (both 2026-05-28) consolidated into [`theory/lexicon-grammar-continuum`](findings/theory/lexicon-grammar-continuum.md)'s new closure section. Q1 answered by the shadow-control apparatus (matched same-material control + measured residual; CC ≈87pp exemplar; closed-weight bound kept honest); Q2 answered *thinly* — inferential role secured 1/3 models via cross-instrument convergence, boundary a shadow-depth gradient, residual thread re-homed. Philosophical/consolidation unit; $0. |
| 2026-07-02 (s169) | A2a, A3a | **A2a first powered confirmation landed:** CC covariation → [`result/comparative-correlative-covariation-powered`](findings/results/comparative-correlative-covariation-powered.md) (136 fresh disjoint items on the byte-frozen v1 instrument; MAGNITUDE-CONFIRMED; pre-run critic + non-Anthropic vote GO, post-run verifier REPRODUCED 0 discrepancies). Construction-isolation assertion gap ≈87pp [95% CI lb ≈78], inverse-flip 97–100%, no atypical collapse, 3/3 — magnitude+interval attached to the CC claim (was direction-only). $0.531 billed. **A3a decision RATIFIED:** the s168-opened human-projection-anchor decision → resolved ADOPT-A (adopt none yet; all four datasets still license-unverified — fresh reviewer reproduced the null via GitHub HTML repo pages; non-Anthropic vote converged). |
| 2026-07-02 (s168) | A4b/A4c/A4d, A3a, B1 | All three queued subject decisions **ratified** (autonomous adversarial review + non-Anthropic votes): scale-ladder ADOPT-A (A4b unblocked, mechanical `ladder` flag owed first), panel-v2 ADOPT-A sequenced-hold with re-open trigger (A4c decided), logprob-lane ADOPT-A (A4d unblocked, re-verify-then-pilot). **A3a** presupposition human-projection-anchor scout landed ($0): all 4 datasets license-UNVERIFIED → anchor decision opened (adopt none yet). **B1** first claims-promotion review landed: CC covariation → [`claim/comparative-correlative-covariation`](findings/claims/comparative-correlative-covariation.md) (`supported`, scoped directional; magnitude deferred to A2a). |
