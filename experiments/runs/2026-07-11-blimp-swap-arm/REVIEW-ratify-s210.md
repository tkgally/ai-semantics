# REVIEW-ratify-s210 — BLiMP R1 content-word-swap arm operationalization gates

*Independent cross-session adversarial ratification review (fresh agent, verdict authority; PROTOCOL §2).
QA companion: the s210 non-Anthropic decorrelation vote (`VOTE-ratify-s210.json`, `gpt-5.4-mini`,
RATIFY-WITH-CONDITIONS, Q1-A/Q2-B/Q3-A). The reviewer independently verified: the 2009 SUBTLEX resource
page names the 2012 "with PoS" file as the fetch needed for auditable POS (its pointer item 4) and records
the 2009 open-for-research/recipe-not-corpus license posture the 2012 file shares; the s209 blockers were
genuinely discharged in-design; Q1-A's re-run-originals choice keeps swapped accuracies unknown at freeze.*

**VERDICT: ADOPT-WITH-MODIFICATION** — proceed to freeze with **Q1-A / Q2-B / Q3-A**, noun+name(+adjective)-only
swap accepted **conditional on a mandatory swap-coverage mitigation (G-coverage)**, bounded candidacy, all
s209 freeze conditions carried plus three additions. (The one modification is Q2 A→B; every other default is
adopted.)

## Per-gate rulings

**Q1 — ADOPT A** (6 frame-safe paradigms, ≈100 fresh paired items each, ORIGINAL re-run fresh, ~$1.3–1.6).
Re-running the originals fresh is the load-bearing choice: it keeps the swapped-condition accuracies unknown
at freeze, which is the swap arm's entire anti-cheat advantage over the covariate arm (Q1-C would re-import
the known-accuracy exposure the arm exists to escape). 3+3 over the 2+2 minimum buys within-stratum
replication so one broken paradigm cannot carry a whole stratum, at linear spend under the $2.50 flag with
powered N per PROTOCOL §4. The frame-safe restriction (excluding island/filler-gap for subcategorization-frame
entanglement and every `irregular_*` for morphology entanglement) is a genuine methodological necessity, not
result-shaping — a POS check cannot detect a valence mismatch or a regular↔irregular conversion, so including
those paradigms with a naive swap would inject artifact, not signal. The deep-pole generality cost (the arm
covers the **scope-deep** pole only, not the island-deep pole) is honestly reported and must travel into
candidacy (see bound).

**Q2 — ADOPT B** (fetch the 2012 "SUBTLEX-US with PoS" file for POS; keep the frequency MATCH norm on
SUBTLEX-US `Lg10WF`), diverging from the design author's A default and converging with the s210 non-Anthropic
vote. Rationale: the swap arm's *only* exposure is the build, and the hand-curated POS lexicon is "the last
build DoF" (G-lexicon-determinism). Q2-B converts hand POS-labelling into an external published annotation — a
strict reduction of the build DoF at trivial cost (one fetch, no model spend), with the license already
verified identical to the in-repo 2009 file and the resource page (pointer item 4) already anticipating
exactly this fetch. This tightens the yardstick and is orthogonal to the direction of Δacc, so it cannot be
result-shaping. The frequency match must stay on the **human-validated** SUBTLEX-US `Lg10WF` (not C4/Q2-C) —
matching on a pretraining proxy would weaken the "the swap did not change human-facing frequency" guarantee.
Q2-C stays a **mandatory** pretraining-proxy diagnostic (G-freq-pretraining), not a match norm. Keep the
design's specified **fallback to Q2-A** if the freeze-time license check or POS-coverage of the 2012 file
fails.

**Q3 — ADOPT A** (mechanical construction-preservation + integrity checks (i)–(v) incl. exact-inflected-form
attestation and the G-frame frame-preservation check; broken pairs dropped/logged/reported; drop-floor →
power re-stated; lead spot-audits as researcher). This respects no-human-subjects (rule 4): the lead auditing
the instrument's own output for gross anomaly is researcher QA, never a human-subject acceptability task. Q3-B
(automated acceptability screen) is correctly rejected as default — it imports a model's grammaticality
opinion into the instrument, contaminating the construct being measured; admissible only as a labelled,
frozen-ex-ante filter. Q3-C is correctly rejected: a SWAP-STABLE earns **bounded candidacy only** — a later,
independent, cross-session adversarial review writes the `claim` (PROTOCOL §3). The control session never
ratifies its own promotion.

## Build choice (noun+name(+adjective)-only swap): ACCEPTED, conditional on G-coverage

I rule noun + proper-name (+ attributive-adjective)-only swapping an **adequate** exact-string-memorization
control and do **not** require verbs by default. The control's target is exact-string / lexical-item
dependence; swapping the head nouns and names already destroys the memorized surface string while preserving
the frame. Verb-swapping without a subcategorization guard is the exact BLOCKER-1 hazard (a POS-preserving
verb swap can change valence and break grammaticality for a non-memorization reason); verb-swapping *with* a
guard is option (a), a substantially larger build with its own DoF whose marginal gain (readmitting the island
pole) is better pursued in a later dedicated arm. The s210 vote, having raised the "minimal perturbation"
flag, reaches the same conclusion.

But the "possibly result-protective" flag is legitimate and I neutralize it with a **mandatory mitigation the
freeze MUST honor (G-coverage):**

1. **Report per-paradigm swap coverage** — the fraction of open-class/content tokens actually replaced, plus a
   per-item surface-string edit distance (token-level) from the original, aggregated per paradigm. This
   converts "minimal perturbation" from an untestable suspicion into a measured, auditable quantity.
2. **Gate the verdict on coverage** — pre-register a coverage floor; a SWAP-STABLE verdict on any paradigm
   whose coverage/edit-distance falls below the floor is flagged as **weak/uninformative** for that paradigm
   and does **not** count toward the ≥2/3 stratum verdict. (This is what stops a verb-heavy paradigm, where
   noun-only swap changes little, from trivially "passing.")
3. **Bound and record the reading** — SWAP-STABLE means "stable under frequency-matched replacement of content
   nouns / proper names / attributive adjectives, holding the closed-class skeleton, main verbs, and adverbs
   fixed," **not** "under full open-class replacement." Name verb/adverb swapping (option (a), with a
   subcategorization guard) as a deferred stronger-perturbation sensitivity arm, so the choice is transparently
   a frame-safety trade-off with a named path to the stronger test, not a terminal minimization.

With G-coverage the noun-only choice is defensible; without it, it is exposed to the result-protective
reading. G-coverage is the non-negotiable price of accepting noun-only.

## Candidacy bound — residual confounds that MUST travel into any promotion claim (even under SURVIVES ∧ SWAP-STABLE)

1. **Construction-frequency / template-difficulty confound** (both votes' central residual; G3′): neither arm
   controls construction frequency or paradigm-template difficulty — a content-swapped island is still a rare
   *construction*. The candidacy is bounded to "not explained by exact-string/lexical-item memorization or the
   tested surface frequency proxy," never a construction-frequency- or template-difficulty-controlled reading.
2. **Deep-pole generality cost** (G-frame): the swap tests the **scope-deep** pole (npi/quantifiers) + shallow
   only; the **island-deep** pole — where the models were weakest — is excluded and untested by the swap.
3. **Perturbation bound** (G-coverage): stability is under noun/name/adjective replacement only; verbs and
   adverbs held fixed.
4. **C4 pretraining-proxy caveat** (G-freq-pretraining): SUBTLEX-matched ≠ pretraining-matched; the swap set's
   C4 log-frequency distribution vs the originals' must be reported, and a material gap is a load-bearing
   limitation on any SWAP-DROPS reading.
5. **Ceiling / weight-of-evidence**: the shallow-3 sit near ceiling (0.98–0.99) and are near-automatically
   within-band; the real evidential weight is the scope-deep-3.
6. **Contamination upper bound persists**: SWAP-STABLE means "not exact-string memorization," never
   "grammatical competence"; absolute accuracy stays a contamination upper bound.

## Anti-cheat check

**Convergence with the s210 non-Anthropic vote:** Q1 (both A), Q2 (both B — I adopt the vote's preference
over the author's default), Q3 (both A), noun-only build (both accept), and the central candidacy bound (both:
template/construction difficulty). Divergence is minor and additive: I make the vote's implicit coverage
concern an explicit mandatory gate (G-coverage) and extend the candidacy bound beyond template difficulty to
the deep-pole generality, perturbation, and pretraining-proxy caveats. Convergence here is comfort, not the
basis of my verdict — I hold verdict authority and reach these independently.

**Outcome-aimed scan:** The two places that could read as result-protective — the noun-only perturbation and
the frame-safe exclusion of the hardest (island) paradigms — are each either (a) forced by a genuine
frame-entanglement confound (you cannot cleanly content-swap a gap-licensing item) or (b) neutralized by a
mandatory measured/gated quantity (G-coverage) plus honest generality reporting into candidacy. Neither is a
smuggled result. The bands are symmetric (SWAP-STABLE and SWAP-DROPS pre-registered identically), the nulls
are first-class, and because Q1-A re-runs originals fresh the ±0.05 margin cannot be tuned to a known result —
the core anti-cheat advantage is genuine. The s209 vote's "asymmetric metric softens failure" concern is
resolved: G-metric replaced the noise-biased mean-of-absolutes with a signed-CI TOST equivalence test and an
honest INCONCLUSIVE middle, and G-power (N≈100) makes that test meaningful. Nothing is aimed at a particular
Δacc sign.

## Freeze conditions the freeze session must honor

- **Gates pinned:** Q1-A (6 frame-safe paradigms, ORIGINAL re-run fresh, N≈100/paradigm) / Q2-B (2012
  SUBTLEX-with-PoS as POS source; **fallback to Q2-A** if the freeze-time license check or POS coverage fails)
  / Q3-A.
- **Q2-B provenance:** at freeze, fetch + sha256-pin the 2012 file, verify its license posture matches the
  2009 (no new restriction), handle recipe-not-corpus (gitignore the full file; commit only the recipe +
  derived POS table), and **extend `resource/subtlex-us-frequency`** with the 2012 file's provenance (as its
  pointer item 4 anticipates). Match frequency on `Lg10WF` on a single pinned basis.
- **G-coverage (NEW, mandatory):** report per-paradigm swap coverage + surface edit distance; pre-register a
  coverage floor; a low-coverage paradigm's SWAP-STABLE is flagged weak and excluded from the ≥2/3 verdict;
  record the perturbation bound.
- **G-margin-justification (NEW):** justify the ±0.05 equivalence margin in PREREG as a pre-registered
  practical-equivalence threshold, not a convenience cutoff.
- **Carry unchanged:** G5-plus (fresh-agent verifier reproduces the swap build from the frozen recipe before
  any item is scored), G-frame (frame-safe restriction + mechanical frame-preservation admission check;
  deep-pole generality cost reported), G-metric (TOST-style signed-CI equivalence; SWAP-DROPS = signed Δ ≤
  −0.05 with CI excluding 0; else INCONCLUSIVE), G-power (N≈100; deep-3 carry the test; drop-floor → power
  re-stated), G-lexicon-determinism (seeded selection from the full eligible in-band set; only membership is a
  DoF), G-freq (report achieved per-word frequency-gap distribution), G-freq-pretraining (mandatory C4
  pretraining-proxy cross-check, no model cost), G3′ (both caveats travel).
- **Standard fences:** PREREG committed before any swap build or model call; independent pre-run freeze critic
  + one non-Anthropic decorrelation vote at freeze; `ABORT_USD` (~1.0/model); `predictions.md` row registered
  at freeze; s205 INSTRUMENT-FAILURE guard carried verbatim; bounded-candidacy scope (all six residual
  confounds above) recorded; promotion remains a separate cross-session adversarial review — this run earns
  candidacy, never writes the claim.

**Governance note:** move `decisions/open/blimp-swap-arm-design.md` to `resolved/` with `resolved-by:
autonomous (adversarial review)`, resolution **ADOPT-WITH-MODIFICATION Q1-A / Q2-B / Q3-A + G-coverage +
G-margin-justification**; clear the design's `contingent-on`; record this review + the s210 vote.
