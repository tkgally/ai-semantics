---
type: design
id: blimp-swap-arm-v1
title: "BLiMP R1 content-word-swap arm (C8 promotion-prep, Q1-C's second required control) — does the panel's grammatical difficulty profile survive replacing the exact BLiMP surface strings with novel frequency-matched content words? DESIGN, not frozen; three gates open"
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: draft
anchor: resource/blimp
contingent-on:
  - []
created: 2026-07-11
updated: 2026-07-11
links:
  - rel: operationalizes
    target: result/blimp-forced-choice-sweep-v1
  - rel: depends-on
    target: result/blimp-profile-frequency-control-covariate-v1
  - rel: depends-on
    target: design/blimp-profile-frequency-control-v1
  - rel: depends-on
    target: resource/blimp
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
---

# Design v1 — BLiMP R1 content-word-swap arm (program A3b, C8 promotion-prep, the swap half of Q1-C)

> **RATIFIED + FROZEN + RUN (2026-07-11, s210).** Gates ratified ADOPT-WITH-MODIFICATION **Q1-A / Q2-B /
> Q3-A** (+ G-coverage, G-margin-justification;
> [`decisions/resolved/blimp-swap-arm-design`](../../wiki/decisions/resolved/blimp-swap-arm-design.md)),
> frozen + built (G5-plus verifier reproduced the build byte-identically), gate-reviewed (freeze critic
> GO-WITH-CONDITIONS), run (~$1.34, 7,200 calls), verifier-checked. **Outcome: SWAP-INCONCLUSIVE — R1 is
> NOT SWAP-STABLE → REFUSED promotion** ([`result/blimp-swap-arm-v1`](../../wiki/findings/results/blimp-swap-arm-v1.md)).
> The deep-scope stratum dropped on 3/3 (Δ̄acc −0.06 to −0.09, CIs exclude 0) but the drop is confounded by
> a +0.20 C4 pretraining-frequency gap, so it is neither SWAP-STABLE nor a clean memorization signal. The
> honest successor is a **C4-frequency-matched** swap arm.

**A design + decision-trail unit — the content-word-swap behavioral control that binding condition **G8** of
the ratified C8 design names as *required for a human-comparison PROMOTION* of reading R1. Status: DESIGN —
three operationalization gates open, ratifiable s210+.** This page operationalizes the **swap arm** of the
already-ratified Q1-C (both arms) on
[`decisions/resolved/blimp-profile-frequency-control-design`](../../wiki/decisions/resolved/blimp-profile-frequency-control-design.md).
It does **not** re-open Q1-C / Q2-A / Q3-A / G8 (all ratified s208) — those fixed *that* the swap arm is
required and *why*; this design fixes **how** the swap arm is built and scored. Per PROTOCOL §3/§A1 and the
A3b/A1b precedent (design one session, ratify the next, run after ratification): **design s209, ratifiable
s210+, freeze + run after ratification.** A control that opens value-laden operationalization choices is not
run in the session that opens it.

> **Where this sits in the C8 chain.** R1 = **PROFILE-ALIGNED** (per-model Spearman of per-paradigm
> forced-choice accuracy vs BLiMP per-paradigm human agreement, ρ_prof **+0.606 / +0.543 / +0.628**, all
> CIs > 0, n = 40) — "the panel is grammatically hard where humans are hard." The s208 **covariate arm**
> returned **SURVIVES-COVARIATE 3/3** (partial ρ_prof·F +0.572 / +0.510 / +0.606, all CIs exclude 0) — a
> **ROBUSTNESS / CORROBORATION** result, not a promotion, because per **G8** the covariate arm alone
> (which reuses the already-known s205 accuracies and controls only a **surface-lexical** frequency proxy)
> cannot license a human-comparison promotion. **G8 requires the swap arm for a promotion.** This design is
> that swap arm. **SURVIVES-COVARIATE ∧ SWAP-STABLE → R1 becomes a promotion-review candidate** — the
> program's first broad human-anchored grammatical-competence claim. **SWAP-DROPS → R1 is refused
> promotion**; the shadow-depth table's form-(iv) row keeps **only DEPTH-GRADED**; the honest reading
> becomes "the panel's grammatical profile rides at least partly on exact-string / lexical-item
> memorization of the BLiMP items."

> **This unit is HUMAN-ANCHORED, not internal-contrast-only.** R1 is a genuine human-comparison line
> (per-paradigm human agreement is the key). The swap arm tests the **validity** of that comparison against
> the sub-confound the covariate arm cannot reach — that the alignment is driven by having *seen the exact
> BLiMP strings* (contamination-as-validity-threat, the s204 critic's distinction), not by shared
> grammatical-difficulty structure. `anchor: resource/blimp` throughout; never internal-contrast-only.

---

## Why this unit is owed now

1. **It is the single outstanding requirement for the highest-value open claim.** The C8 chain has exactly
   two gates between the s205 run and a promotion of R1: the covariate arm (**run s208 → SURVIVES**) and the
   swap arm (**this design**). R1 is the program's one live path to a *broad* human-anchored
   grammatical-competence claim; the swap arm is the last thing owed. Nothing else in the backlog is as close
   to a compounding claim (the design-page assessment carried since s207).
2. **The two-track balance leaves no genuine phil/consol unit to prefer.** A cold-start survey of every
   phil/consol trigger (predictions §C standing triggers, essay revision triggers, ripe open-questions, and
   theory pages over the >3-update-box edition threshold) returned **four honest nulls** — no
   philosophical/consolidation unit has a genuinely fired, unacted trigger (the recent BLiMP line correctly
   fired none; the firewall essay already handled Gurnee 2026 as mutual non-entailment; every over-threshold
   theory page already has its second edition). With no genuine phil unit to do and padding forbidden
   (PROTOCOL §3, "prefer a real trigger over padding"), the highest-value empirical continuation is the
   honest pick.
3. **It is cheap and its anti-cheat posture is the covariate arm's exact complement.** Fresh items + fresh
   calls ⇒ the swapped-condition accuracies are **unknown at freeze**, so — unlike the covariate arm, whose
   sharpest exposure was reusing the already-known s205 accuracies (G1′) — the designer **cannot tune the
   swap to hit a target**. The residual DoF (which paradigms, which swap words, the re-validation rule) is
   frozen in PREREG and independently verifier-reproduced from the recipe before any item is scored. Cost is
   ~$0.3–0.5 (below), well under the $2.50 prefer-split flag.
4. **G8 is symmetric.** A **SWAP-DROPS** outcome — accuracy collapses once the exact strings are replaced —
   is a first-class negative that *refuses* the program its would-be flagship claim and hardens the honest
   reading that the panel's grammatical profile is (at least partly) BLiMP-string memorization. The bands are
   pre-registered identically for SWAP-STABLE and SWAP-DROPS; that symmetry is the whole point.

## The sub-confound the swap arm targets (why the covariate arm is not enough)

R1 says: the panel is grammatically hard **where humans are hard** (ρ_prof > 0). Two distinct confounds
could manufacture that alignment; C8 named both and G8 requires both controlled:

- **Construction / surface frequency** (the covariate arm's target, run s208): frequent local-agreement
  constructions are plausibly both human-easy and heavily represented in pretraining; rare island/scope
  contrasts both human-harder and less represented. The covariate partialled a **C4 surface-lexical
  frequency proxy** from ρ_prof → **SURVIVES**. But it reaches only surface-lexical familiarity, not
  construction frequency (G3′), and it inherits the known-accuracy exposure.
- **Exact-string / lexical-item memorization** (the swap arm's target, *this* design): BLiMP is public and
  contamination-bounded (absolute accuracy 0.87–0.94 = an upper bound). If the panel is right on the frozen
  BLiMP items partly because it has **seen those exact sentences (or their close lexical neighbours)**, then
  ρ_prof partly measures *which paradigms were better memorized*, not shared grammatical-difficulty
  structure. Replacing the open-class content words with **novel, frequency-matched** ones — holding the
  grammatical minimal contrast constant — removes the exact strings while leaving the *construction* intact.
  If per-paradigm accuracy is **stable** under swap, the profile does not ride on exact-string memorization.

**What a SWAP-STABLE does and does not license (G3′ travels).** SWAP-STABLE rules out *exact-string /
lexical-item memorization* as the driver. It does **not** control **construction** frequency (a
content-swapped island is still a rare *construction*) — that is the covariate arm's job, and even the two
arms together reach construction frequency only *indirectly*. The promotion candidacy carries **both** the
covariate arm's G3′ caveats and this caveat into the claim review; it launders nothing away.

## GATE Q1 — paradigm & item selection (accuracy-blind AND human-agreement-blind)

The parent design fixes **≥2 shallow + ≥2 deep** paradigms. The value-laden operationalization choices are
**how many**, **which**, and **what the ORIGINAL baseline is**. All selection references **only** BLiMP
structural metadata (`paradigm_meta.json` `linguistics_term`/`field`, the s205 depth strata) and a
**swappability** criterion — **never** the s205 accuracies and **never** the human-agreement values.

- **Q1-A (provisional default, hardened for frame-safety — s209 BLOCKER-1) — 3 shallow + 3 deep = 6
  **frame-safe** paradigms, chosen by a deterministic swappability rule; ORIGINAL condition = ≈100 fresh
  paired items/paradigm re-run fresh this session.** BLOCKER-1: POS-preservation does **not** preserve
  grammaticality where the open-class word is entangled with the contrast — a `filler_gap_dependency` /
  `island_effects` item's gap is licensed by the **main verb's subcategorization frame** (swap a transitive
  verb for an intransitive one and the good member becomes ungrammatical for an argument-structure reason,
  undetected by a POS check), and an `irregular_*` agreement item's contrast turns on **irregular** plural
  morphology (man/men → swapping to a regular-plural noun silently converts it to an easier regular test).
  **So the swappable set is restricted to frame-safe paradigms:** shallow-3 from the **regular**
  `determiner_noun_agreement` (1/2) + `regular_plural_subject_verb_agreement` (1/2) paradigms; deep-3 from
  `npi_licensing` ∪ `quantifiers`, where the licensor (negation / `only` / a quantifier) is **closed-class**
  and content-swap is frame-safe. `island_effects` / `filler_gap_dependency` and every `irregular_*`
  paradigm are **excluded from the swappable set**, and the **deep-pole generality cost is reported** (the
  swap arm covers the **scope-deep** pole, not the island-deep pole). Within each restricted stratum, select
  by a **frame-safe swappability score** (count of open-class positions replaceable without touching the
  contrast locus *and* without frame entanglement), ties by paradigm UID alphabetical — computed from item
  *structure*, blind to accuracy and human agreement. The more-general **option (a)** — a
  subcategorization-tagged verb lexicon + same-frame substitution + an irregular↔irregular guard, which
  would let the island pole back in — is the alternative the ratifier may prefer (recorded on the decision).
  The **ORIGINAL** condition is a **fresh, seeded ≈100-pair subsample** per paradigm from its 1,000, each
  with a swapped counterpart, **re-run fresh this session** (not reused from the s205 `results.json`), so
  Δacc is a **within-run paired** quantity under identical conditions — removing both the known-accuracy
  exposure and any "the panel drifted since s205" concern, and giving G-power the N the equivalence test
  needs. **Corrected cost:** 6 × 100 × 2 conditions × 2 orders × 3 models = **7,200 calls ≈ $1.3–1.6** at the
  s205 economics — **under the $2.50 prefer-split flag** (the s209 critic's 15,840 estimate double-counted).
- **Q1-B — the ≥2 + ≥2 minimum (4 paradigms).** Cheapest (~$0.2–0.35); but a single paradigm's swap
  breaking would carry a whole stratum, since the verdict is per-stratum. Rejected as default for lack of
  within-stratum replication.
- **Q1-C — reuse the s205 frozen original accuracies as the baseline (do not re-run originals).** Halves the
  call count, but re-introduces the covariate arm's known-accuracy exposure into the comparison baseline and
  cannot rule out cross-session drift. Rejected as default (the swap arm's whole value is its freedom from
  that exposure).

**Why value-laden.** More paradigms buy within-stratum replication at linear spend; re-running originals
buys a clean paired within-run Δ at 2× calls but removes the known-accuracy exposure the swap arm exists to
escape. The default spends the modest extra to keep the arm's anti-cheat advantage intact.

## GATE Q2 — the swap operationalization (THE CRUX): frequency-balancing norm + POS/morphology-preserving substitution

The swap is only a valid control if the replaced words are (a) **novel** (not the BLiMP originals),
(b) **frequency-matched** (so a Δacc is not a frequency drop in disguise — the very confound the covariate
arm controls must not sneak back in through the swap), and (c) **POS- and morphology-preserving** (so the
grammatical minimal contrast survives, G5). Three operationalizations differ on the frequency norm and how
POS is supplied.

- **Q2-A (provisional default) — SUBTLEX-US `Lg10WF` banding + a frozen, hand-curated, POS-labelled content
  lexicon.** For each swappable open-class position, replace the original lemma with a novel word of the
  **same POS**, matched **within ±0.10 `Lg10WF`** (the psycholinguistically standard log-frequency scale),
  re-inflected to the original's morphological features (number/tense/person), drawn **deterministically
  (seeded) from the full eligible in-band, POS-(and frame-)matched set** of a **frozen frequency-banded
  content lexicon** the freeze session curates from SUBTLEX-US `Lg10WF` bands and labels by POS — the **only
  human DoF is membership** (junk removal via a published closed-class stoplist rule, verifier + stoplist
  auditable), **never per-item hand-assignment** (G-lexicon-determinism, s209 critic condition), committed +
  sha256-pinned. Reuses the license-verified
  [`resource/subtlex-us-frequency`](../../wiki/base/resources/subtlex-us-frequency.md) (recipe-not-corpus;
  the resource page already names "a candidate open-class content-control band within ±0.10 Lg10WF" as its
  intended use and flags that the plain 2009 file **carries no POS**, so the POS labelling is a curation
  step, a DoF frozen in PREREG). *Strength:* matches on the **human-validated** frequency norm (the measure
  best predicting human lexical-processing latencies), so a Δacc cannot be a human-frequency artifact.
  *Weakness:* the hand-curated POS lexicon is a researcher DoF (mitigated by G5-plus: frozen + verifier-
  reproduced before scoring).
- **Q2-B — the 2012 "SUBTLEX-US with PoS" file, fetched + license-checked, for auditable POS selection.**
  Replaces the hand-curation with the published POS-tagged frequency list (Brysbaert, New & Keuleers 2012),
  removing the POS-labelling DoF. *Cost:* a fresh fetch + license verification of a **not-yet-in-repo** file
  (the s168 rule: no adoption without a verified license) — a build dependency that may fail the
  license check, in which case fall back to Q2-A.
- **Q2-C — C4 log-frequency banding (reuse the s208 frozen C4 machinery).** Match swap words on the **same
  C4 proxy** the covariate arm used, so the swap and covariate arms are balanced on one corpus family.
  *Weakness:* C4 is a *proxy for pretraining*, not a human-frequency norm, and carries the training-proxy
  caveat; matching the swap on it, rather than on the human-validated SUBTLEX-US, weakens the "the swap did
  not change human-facing frequency" guarantee. Rejected as default; admissible as a **labelled sensitivity
  cross-check** only.

**The substitution recipe (fixed at freeze regardless of Q2 choice).** Per minimal pair `(good, bad)`:
1. **Locate the contrast locus** — the token(s) that differ between `good` and `bad` (the number target, the
   NPI marker `ever`/`certainly`, the wh/complementizer, the verb inflection). **Never swapped, never
   touched.**
2. **Identify swappable open-class positions** — common nouns, main-verb lemmas, adjectives, adverbs, and
   proper names **outside** the contrast locus **that are not frame-entangled with it** (G-frame). Closed-class
   items (determiners, auxiliaries, complementizers, negation, quantifiers, wh-words, prepositions) are **held
   exactly**. Where the contrast is carried by an open-class word's *inflection* (the head noun's number in
   det–noun agreement, the verb's inflection in subject–verb agreement), the **lemma is swapped but the
   inflectional feature is preserved** — and, per BLOCKER-1, only within the **frame-safe paradigm set** (Q1):
   the paradigms where the contrast rides on a closed-class licensor, never one where a swapped verb's
   **subcategorization frame** licenses a gap (island/filler-gap) or a swapped noun's **irregular** morphology
   carries the contrast (both excluded from the swappable set at Q1).
3. **Replace** each swappable lemma with a novel, POS-matched, frame-matched, frequency-matched word (Q2),
   re-inflected to the original features. The functional skeleton and the contrast locus are byte-identical to
   the original except for the open-class lemmas.

**Why grammaticality is preserved by construction *within the frame-safe set* (and where it is NOT — BLOCKER-1).**
Because the swappable set is **restricted to frame-safe paradigms** (Q1) and only frame-unentangled open-class
lemmas are swapped (POS + morphology preserved) with the functional skeleton + contrast locus untouched, the
**good stays grammatical and the bad stays ungrammatical for the same structural reason**. This is **not** true
in general: in gap-bearing paradigms (island/filler-gap) the main verb's subcategorization frame licenses the
gap, so a POS-preserving verb swap can *destroy* the dependency — POS is too coarse a grain — which is exactly
why those paradigms are excluded at Q1 (or, under option (a), scored only with a subcategorization-tagged
same-frame lexicon). The residual risks *within* the frame-safe set are (i) **selectional / semantic anomaly**
(an implausible verb–object pairing) — which BLiMP items already tolerate (many are semantically odd but
grammatical), so it does not by itself void a pair, but an *egregious* anomaly that could independently depress
acceptability is caught by Q3; (ii) a swap that accidentally creates a within-item agreement coincidence or a
real homograph collision — caught by the Q3 mechanical integrity check + the G-frame frame-preservation check. **Why value-laden:** SUBTLEX-US (human-validated) vs C4 (pretraining-proxy) as
the match norm changes what a stable-vs-dropped result *means*; hand-curated vs fetched POS trades a DoF
against a license-check build. The default matches on the human norm and accepts the curation DoF under a
verifier gate.

## GATE Q3 — grammaticality re-validation without human subjects (G5) + the honest promotion scope

The no-human-subjects rule (CLAUDE.md rule 4) means re-validation is **rule-based / mechanical**, never a
new human acceptability judgement. What counts as an adequately re-validated swapped pair, and what does a
SWAP-STABLE (with the s208 SURVIVES) license?

- **Q3-A (provisional default) — mechanical construction-preservation + integrity check; a broken pair is
  dropped, logged, reported; the lead spot-audits a sample as researcher, not subject.** A swapped pair is
  admitted iff, mechanically: (i) every swapped token matches its original's **POS** and **morphological
  features**; (ii) the **contrast locus is byte-identical** to the original's (the good/bad difference is
  exactly the original target and nothing else); (iii) every swapped word is a **real English word** whose
  **exact inflected form is corpus-attested** (in the frozen lexicon / SUBTLEX-US) within the ±0.10 `Lg10WF`
  band (the vote's exact-inflected-form attestation); (iv) the swap introduces **no new token-level agreement
  coincidence** (a mechanical check that no swapped noun/verb accidentally satisfies the contrast the pair is
  meant to violate); (v) **frame-preservation (G-frame):** the swap leaves every argument-structure /
  subcategorization relation that could license or block the contrast unchanged — enforced structurally by
  the Q1 frame-safe paradigm restriction, and checked mechanically (no swapped verb changes valence class; no
  swapped noun changes the regular/irregular morphology class carrying an agreement contrast). A pair failing
  any check is **dropped, logged, and reported** (never silently repaired); if drops reduce a paradigm below a
  pre-registered floor (e.g. < 60 usable pairs at the ≈100 target) the paradigm is dropped and power
  re-stated. The lead **spot-audits a fixed-size random sample** of admitted pairs for gross
  selectional anomaly **as the researcher running the instrument** (documented, not a human-subject
  acceptability task); an audit-flagged systematic anomaly pattern is reported as a limitation, not
  silently fixed. **Promotion scope (bounded — both s209 reviewers).** SWAP-STABLE ∧ (s208)
  SURVIVES-COVARIATE → R1 becomes a **bounded promotion-review candidate** (a later, separate, cross-session
  adversarial review writes the `claim`; this run earns candidacy, never ratifies — PROTOCOL §3 / the B1
  procedure). **The candidacy is explicitly bounded** to "R1's profile alignment is **not explained by
  exact-string / lexical-item memorization or the tested surface frequency proxy**" — it is **not** a
  construction-frequency-controlled nor a template-difficulty-controlled reading (the critic's ceiling note:
  the shallow stratum sits near ceiling so the deep-3 carry the real test, and residual construction /
  item-template familiarity is reached by neither arm). The bound + both G3′ caveats travel into the claim
  review. SWAP-DROPS → R1 refused promotion, table form-(iv) row keeps **only DEPTH-GRADED**.
- **Q3-B — add an automated acceptability screen (a frozen parser / an off-panel LLM acceptability filter)
  to drop semantically anomalous swaps.** Tighter, but the screen is itself a DoF and an off-panel LLM
  acceptability judgement risks importing a model's grammaticality opinion into the instrument. Admissible as
  a **labelled, reported** filter only if frozen ex ante; rejected as the default (mechanical POS/morphology
  preservation already preserves the *grammatical* contrast, which is what the arm tests — semantic oddity is
  a BLiMP-inherited property, not a new confound).
- **Q3-C — treat SWAP-STABLE as itself writing the R1 claim this session.** Rejected: promotion is always a
  separate, cross-session, adversarial review (PROTOCOL §3); the control session earns candidacy, never
  ratifies.

**Why value-laden.** Whether re-validation is purely mechanical + a researcher spot-audit (Q3-A) or adds an
automated acceptability screen with its own DoF (Q3-B), and whether a SWAP-STABLE earns candidacy (Q3-A) or
writes the claim (Q3-C, over-reach). The default keeps re-validation mechanical (respecting no-human-subjects
and not importing a model's acceptability opinion) and promotion cross-session.

## Metrics + verdict map (direction fixed at freeze; band PINNED here, not inherited-by-assertion — G-metric)

Let `acc_orig(m,p)` and `acc_swap(m,p)` = model m's order-averaged forced-choice accuracy on paradigm p's
original vs swapped items (both re-run fresh this session, both orders, position-bias-netted, exactly the
s205 Q2-A elicitation). `Δacc(m,p) = acc_swap(m,p) − acc_orig(m,p)`.

> **The parent ratified an *illustrative* band (s209 BLOCKER-2).** The parent design writes the swap-arm
> band as "**e.g.** |Δacc| ≤ 0.05" — illustrative, not a pinned yardstick — and a **mean-of-absolute-Δ**
> aggregation is **upward-biased under sampling noise** (at 30 items/paradigm the per-paradigm Δ SE ≈ 0.065,
> so under a *true* Δ=0 the expected `mean|Δ|` ≈ 0.05, right at the band → a stable panel can land
> INCONCLUSIVE from noise alone). So the **aggregation + band are a live operationalization DoF pinned here
> (G-metric), not inherited by assertion**, and the metric is a **signed CI / equivalence** test, not
> mean-of-absolutes.

- **SWAP-STABLE (G-metric — a TOST-style equivalence)** iff the **per-model, per-stratum signed
  stratum-mean Δ** has a **bootstrap CI that sits *within* ±0.05** on **both** the shallow and deep strata
  for **≥2/3** models — the per-paradigm profile is statistically equivalent-to-unchanged under swap, i.e.
  does not depend on exact-string memorization. **SWAP-DROPS** iff the signed stratum-mean Δ ≤ **−0.05 with
  its CI excluding 0** within a stratum on ≥2/3 — the exact strings were load-bearing, a first-class
  negative. **SWAP-INCONCLUSIVE** otherwise (a CI that neither fits within ±0.05 nor clears −0.05 — the
  honest under-power landing, pre-registered). Report per-model, per-paradigm signed Δacc with bootstrap CIs
  and the frozen s205 elicitation's both-order diagnostics (position-lock rate, ans1_rate) and the
  **INSTRUMENT-FAILURE** guard carried verbatim from the s205 PREREG.
- **Power (G-power sharpened — BLOCKER-2).** To make the equivalence test meaningful the paired item set is
  **expanded to ≈100 fresh paired items/paradigm** (per-paradigm Δ SE → ~0.03), pinned in PREREG with the
  per-model per-stratum Δ CI power stated; the shallow stratum sits near ceiling (s205 local accuracy
  0.98–0.99, near-zero headroom) so it is close to automatically within-band — **the deep-3 carry the real
  test** (reinforcing G-frame: those three must be frame-safe, and adequately powered).
- **Combined promotion verdict (G8, inherited):** promotion candidacy requires **SURVIVES-COVARIATE (s208) ∧
  SWAP-STABLE (this run)**; either a BREAKS-covariate (already excluded — s208 SURVIVED) or a SWAP-DROPS
  refuses promotion. The stricter conjunction is deliberate — a claim armored against both the frequency and
  the exact-string sub-confounds is the only one worth the program's first broad grammatical claim.
- **Pre-named nulls (first-class):** SWAP-DROPS (R1 rides on exact-string memorization); SWAP-INCONCLUSIVE
  (mixed across strata); an INSTRUMENT-FAILURE void; a paradigm dropped for too many broken-pair drops. Each
  is pre-registered and reported, never silently dropped.
- **Anti-cheat fence (PROTOCOL §B).** The paradigm selection rule + swappability score, the frozen
  frequency-banded POS lexicon (Q2), the substitution recipe, the re-validation checks + drop floor, the
  SWAP-STABLE/DROPS bands (inherited), and the elicitation (s205-frozen prompt + both orders) are **all
  frozen in `PREREG.md` before any swapped item is built or scored**, and the swap-build code is
  **independently reproduced by a fresh-agent verifier from the frozen recipe before any item is scored**
  (G5-plus). Because the swapped-condition accuracies are **unknown at freeze**, the swap arm has **no
  known-accuracy exposure** — its DoF is entirely in the *build*, fenced by the verifier reproduction.

## Panel & settings

Panel = the three [`config/models.md`](../../config/models.md) slots (`panel.A/.B/.C`), temperature 0,
zero-shot, single-turn, **both presentation orders** (the s205 Q2-A control), `google/*` reasoning
suppressed/capped (config Caveat 1), the **exact s205 forced-choice prompt** (frozen in that run's
`probe.py`), `usage.cost` recorded via [`experiments/lib/openrouter.py`](../lib/openrouter.py). Never
hardcode slugs.

## Cost (pre-flight estimate)

- **Default (Q1-A, 6 frame-safe paradigms, N≈100 for the equivalence test — BLOCKER-2):** 6 × 100 items ×
  2 conditions (orig + swap) × 2 orders × 3 models = **7,200 calls ≈ $1.3–1.6** at the s205 per-call
  economics (7,200 s205 calls billed $1.33; claude the largest share; gemini reasoning suppressed). Hard
  per-model `ABORT_USD ≈ 1.0` in `probe.py` at freeze. **Under the $2.50 prefer-split flag → no split** (the
  s209 critic's 15,840-call / $2–3.5 estimate double-counted).
- **Q1-B (4 paradigms):** ~$0.2–0.35. **Q2-B** adds a one-time fetch + license-check of the 2012
  SUBTLEX-US-with-PoS file (no model cost). **Q2-C sensitivity cross-check** adds no model cost (C4
  streaming compute only).
- **This design session (s209):** the only spend is **one non-Anthropic decorrelation vote**
  (`gpt-5.4-mini` via the probe REST path, ~$0.002–0.004) as QA to the fresh-agent design critic.

## Scope cap — LOAD-BEARING (read before citing any result this design produces)

1. **Controls R1 only, and only the exact-string / lexical-item memorization sub-confound.** It does **not**
   touch R2 (DEPTH-GRADED, within-panel — already verdict-bearing) or R2h (TRACKS-DIP), and does **not**
   control **construction** frequency (the covariate arm's target; even both arms reach construction
   frequency only indirectly — G3′ travels).
2. **SWAP-STABLE means "not driven by memorizing the exact BLiMP strings," never "grammatical competence."**
   Absolute accuracy stays a contamination upper bound; the swap removes *exact* strings, not the models'
   broader exposure to English grammar.
3. **The frequency-match is only as good as the norm + the ±0.10 band.** Under Q2-A the match is on
   SUBTLEX-US (human-validated) `Lg10WF`; a residual per-word frequency gap within the band is reported.
4. **Acceptability, not inference; behavioral 2AFC, not logprob; the s205 elicitation** — all s205 scope
   caps carry unchanged.
5. **n = 3 models; per-model, per-stratum Δacc, never pooled.**

## What each outcome feeds

- **SWAP-STABLE (with s208 SURVIVES-COVARIATE):** R1 becomes a promotion-review candidate — the program's
  first broad human-anchored grammatical-competence claim (carrying **both** the covariate arm's C4/surface
  caveats and this arm's "exact-string only, not construction frequency" caveat); the shadow-depth table's
  form-(iv) row hardens from descriptive toward a claim. A `predictions.md` row (registered at **freeze**)
  fires-for.
- **SWAP-DROPS:** a first-class negative — the panel's grammatical difficulty profile rides at least partly
  on exact-string / lexical-item memorization; R1 stays descriptive; the table's form-(iv) row keeps **only
  DEPTH-GRADED**; the honest reading against
  [`essay/shadow-depth-cross-cuts-grain`](../../wiki/findings/essays/shadow-depth-cross-cuts-grain.md) is
  sharpened. No revision trigger fires from the design itself; the run's outcome may.
- **SWAP-INCONCLUSIVE:** neither promotion nor refusal; the arm is reported and the line notes what a
  cleaner instrument would need.

## Handoff (what s209 did, and what remains)

1. **s209:** wrote this design; opened the decision
   ([`decisions/open/blimp-swap-arm-design`](../../wiki/decisions/open/blimp-swap-arm-design.md); Q1–Q3,
   provisional defaults **Q1-A / Q2-A / Q3-A**); ran the design pre-run critic (fresh agent, verdict
   authority → **GO-WITH-CONDITIONS**, provenance + anchor **CLEAN**, two blockers + one condition + one
   added diagnostic) + one non-Anthropic decorrelation vote (`gpt-5.4-mini`, **GO-WITH-CONDITIONS**, Q1-A /
   Q2-A / Q3-A, $0.004603; recorded under
   [`experiments/runs/2026-07-11-blimp-swap-arm-design/`](../runs/2026-07-11-blimp-swap-arm-design/) —
   [`REVIEW-design-s209.md`](../runs/2026-07-11-blimp-swap-arm-design/REVIEW-design-s209.md),
   [`VOTE-s209.json`](../runs/2026-07-11-blimp-swap-arm-design/VOTE-s209.json)). **The two blockers are
   discharged in-design this session** (BLOCKER-1 frame-safety → Q1 frame-safe restriction + G-frame;
   BLOCKER-2 metric → G-metric equivalence test + G-power N≈100), plus G-lexicon-determinism and the added
   G-freq-pretraining diagnostic. **Nothing frozen, nothing run.**
2. **Ratify (s210+):** a fresh reviewer + one non-Anthropic vote fix Q1–Q3 (never the opening session).
3. **Freeze (after ratification):** write `build_swap.py` (the substitution recipe + the frozen
   frequency-banded POS lexicon, sha256-pinned, deterministic seeded selection; contrast-locus + frame
   detection from the frozen BLiMP items) + `probe.py` (the s205 elicitation, both orders, `ABORT_USD`) +
   `analyze_swap.py` (per-model, per-stratum signed Δacc + bootstrap CIs + the both-order diagnostics + the
   C4 pretraining-proxy cross-check); fix the lexicon + bands + re-validation checks in `PREREG.md`
   **before any swapped item is built or scored**; the swap-build is **independently reproduced by a
   fresh-agent verifier before scoring** (G5-plus); independent pre-run freeze critic + one non-Anthropic
   vote; register the `predictions.md` bet at freeze.
4. **Run (after freeze):** the swap arm (~$1.3–1.6); post-run verifier recomputes every figure from the
   frozen items + the fresh swap build.

## Freeze-time conditions (bind the freeze session)

From this design's own anti-cheat analysis + the s207/s208 C8 lineage + the s209 pre-run critic + vote
(both discharged in-design this session).

- **G5-plus (anti-cheat — the swap arm's build is its only exposure).** The swap-build code is frozen in
  PREREG and **independently reproduced by a fresh-agent verifier from the recipe before any item is
  scored**; the frequency-banded POS lexicon is committed + sha256-pinned; the contrast-locus detection is
  validated against the frozen s205 items (every detected locus matches the good/bad diff). Because swapped
  accuracies are unknown at freeze, there is **no known-accuracy exposure** — but a builder could still bias
  the lexicon, so the verifier reproduction is load-bearing.
- **G-frame (grammaticality-preservation ≠ POS-preservation — s209 BLOCKER-1).** The swappable set is
  **restricted to frame-safe paradigms** (Q1: regular det–noun + regular subject–verb agreement shallow;
  `npi_licensing` ∪ `quantifiers` deep — closed-class licensor), **excluding** island/filler-gap
  (subcategorization-frame-entangled) and every `irregular_*` paradigm (morphology-entangled); the
  deep-pole generality cost (scope-deep covered, island-deep not) is **reported**. A mechanical
  **frame-preservation admission check** (no swapped verb changes valence class; no swapped noun changes the
  regular/irregular morphology class carrying a contrast) is in the Q3 admission rule. Option (a) — a
  subcategorization-tagged same-frame verb lexicon that readmits the island pole — is the ratifier's
  alternative.
- **G-metric (the band is pinned, not inherited — s209 BLOCKER-2).** SWAP-STABLE is a **TOST-style
  equivalence** (per-model per-stratum signed stratum-mean Δ **bootstrap CI within ±0.05** on both strata,
  ≥2/3); SWAP-DROPS is signed Δ ≤ **−0.05 with CI excluding 0**; else SWAP-INCONCLUSIVE. Replaces the
  parent's illustrative "e.g. |Δacc| ≤ 0.05" mean-of-absolutes (noise-biased toward INCONCLUSIVE). Pinned in
  PREREG.
- **G3′ travels.** Every SWAP-STABLE/DROPS statement carries "controls exact-string / lexical-item
  memorization, **not** construction frequency" — the swap arm does not, alone or with the covariate arm,
  license a "construction-frequency-controlled" reading; the promotion candidacy is **bounded** accordingly.
- **G-freq (no human-frequency confound re-introduced).** The swap must be frequency-matched (±0.10 `Lg10WF`
  under Q2-A); report the achieved per-word frequency-gap distribution, and if the swap set's mean frequency
  differs materially from the originals', that is a limitation on the Δacc reading (a frequency drop, not a
  memorization signal).
- **G-freq-pretraining (the seam between the two arms — s209 critic's added condition).** SUBTLEX-US is a
  **human-facing** norm, not the models' pretraining distribution, so a SUBTLEX-matched substitute can be
  materially rarer in **pretraining** — a Δacc could be a pretraining-frequency drop in disguise. At freeze,
  report the swap set's **C4 (pretraining-proxy) log-frequency distribution against the originals'** (reuse
  the s208 C4 pipeline; streaming compute, **no model cost**); a material difference is a load-bearing
  limitation on any SWAP-DROPS reading and travels into the candidacy alongside G3′. (Q2-C repurposed from
  optional to a **mandatory diagnostic**.)
- **G-lexicon-determinism (the lexicon is the last build DoF — s209 critic condition).** The per-position
  substitute is chosen **deterministically (seeded) from the full eligible in-band, POS-and-frame-matched
  set**; the only human DoF is **membership** (junk removal via a published stoplist rule), verifier +
  stoplist auditable — never per-item hand-assignment.
- **G-power (sharpened — s209 BLOCKER-2).** N is **expanded to ≈100 fresh paired items/paradigm** (per-paradigm
  Δ SE → ~0.03) so the equivalence test is meaningful, pinned in PREREG with the per-model per-stratum Δ CI
  power stated; the shallow stratum is near ceiling so **the deep-3 carry the real test**; if broken-pair
  drops reduce usable pairs below the floor, re-state power and downgrade to descriptive / SWAP-INCONCLUSIVE
  if it falls too low.
- Carry the standard fences: PREREG committed before any swap build or model call; independent pre-run
  critic + one non-Anthropic vote at freeze; `ABORT_USD`; `predictions.md` row at freeze; the s205
  INSTRUMENT-FAILURE guard verbatim.
