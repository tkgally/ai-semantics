# Pre-run design critic — BLiMP R1 frequency control (C8 promotion-prep), s207

**Reviewer:** independent adversarial pre-run design critic (verdict authority over the value-laden
gates), fresh agent, no authorship stake in the design. Reviewed the design
[`design/blimp-profile-frequency-control-v1`](../../designs/blimp-profile-frequency-control-v1.md), the
open decision [`decisions/open/blimp-profile-frequency-control-design`](../../../wiki/decisions/open/blimp-profile-frequency-control-design.md),
the s205 result + parent design + its C8, `resource/blimp`, `resource/cooccurrence-corpus-scouting`, the
byte-frozen C4 recipe `build_cooc_c4.py`, and the frozen s205 `results.json`. No network/model call made
(a separate decorrelation vote handles that; I read its `VOTE-s207.json`).

---

## Verdict: **GO-WITH-CONDITIONS**

The unit is honestly constructed and its decision-trail discipline is right: design s207, ratify s208+,
run after ratification; the null is pre-named symmetrically (BREAKS, SWAP-DROPS, `corr(F,H)≈0`, and an
INCONCLUSIVE middle band are all first-class); the anchor declaration is correct; and — importantly — the
provenance checks out (the quoted ρ_prof values, the C8 verbatim text, the sha256, and every linked page
all resolve against in-repo artifacts; no fabrication). But it is **not freeze-ready as written.** Three
things must be fixed before freeze, and one is a genuine BLOCKER that touches the design's central
anti-cheat claim: **the design misdescribes what `build_cooc_c4.py` computes, and therefore overstates the
"no new DoF" fence on the covariate `F(p)`.** Combined with a second BLOCKER — under the Q2-A default the
covariate controls the *wrong frequency* relative to C8's literal confound — my judgement is that the
**covariate arm alone cannot license a human-comparison PROMOTION**; it earns at most a robustness /
corroboration result. **I require the swap arm (Q1-C) for promotion.** With the conditions below bound
into the freeze, the run is worth doing (and cheap: the covariate arm is $0 model cost).

---

## Per-gate votes

- **Q1 → C (require BOTH the covariate and the swap arm for a promotion).** The covariate arm carries an
  irreducible exposure — the s205 accuracies and ρ_prof are already known, and `F(p)`'s definition is a
  free parameter that demonstrably moves the outcome, so "freeze before computing" is a weaker fence than
  the design admits (see BLOCKER-1). Independently, under Q2-A the covariate controls *lexical
  familiarity*, not the *construction* frequency C8's prose names (BLOCKER-2). The swap arm is a
  fresh-item / fresh-call test of a **different** causal channel (exact-string memorization) with **no**
  exposure to the known accuracies. Covariate-alone should earn only a corroboration/robustness datum;
  the program's *first broad human-anchored grammatical claim* deserves the conjunction. (Converges with
  the decorrelation vote's Q1-C.)
- **Q2 → A as primary, but CONDITIONED — not a clean A, and I explicitly diverge from the decorrelation
  vote's Q2-C.** Q2-A (surface content-word n-gram frequency) is defensible on *interpretability* grounds:
  it is the least depth-entangled proxy, so partialling it is least likely to strip the shared depth
  structure R1 is trying to measure. But it must be scoped honestly as controlling *lexical/surface
  familiarity*, **not** construction frequency. The vote prefers Q2-C (construction-level frequency) as
  "most literal to C8" — I reject Q2-C as the *primary* because construction frequency is nearly collinear
  with structural depth (rare constructions = deep constructions = human-harder), so partialling it
  reproduces the Q2-B over-control hazard: a BREAKS under Q2-C would not separate "frequency artifact" from
  "the shared structure *is* the depth structure." So: Q2-A primary (scoped), Q2-B strictly a labelled
  sensitivity arm, Q2-C optional and only ever reported with the over-control caveat load-bearing.
- **Q3 → A.** Correct: the control is a promotion **gate**, promotion stays a separate cross-session
  adversarial review, and the outcome is a standalone result either way. Reject Q3-C (over-reach) and Q3-B
  (needless forfeit) as the design does. One extension required (see BLOCKER-3 + G6): the verdict map is
  missing the *high-collinearity* branch. (Converges with the vote's Q3-A.)

---

## BLOCKERS (must fix before freeze)

**BLOCKER-1 — G1 misdescribes the reused artifact; the "no new DoF" claim is false.**
The design repeatedly states the covariate will "byte-reuse `build_cooc_c4.py`'s C4 streaming **+ n-gram
counting**" so "the counting carries **no new DoF**" (design §Metrics anti-cheat fence, §Handoff step 3,
G1(a)). This is not what `build_cooc_c4.py` does. Read firsthand, that script computes: (i) a
sentence-streaming IO adapter (`stream_sentences`) + tokenization regexes; (ii) **unigram** sentence
document-frequency `df[w]` over a *fixed pre-specified target set* (`vocab | cues`); (iii) cue-anchored
**co-occurrence** counts (`co_sent`, `co_frame`) and a signed-G² kernel; (iv) a Hearst definitional-frame
density. **There is no per-n-gram (bigram/trigram) frequency counter anywhere in it** — the only
"trigram" tokens are the fixed Hearst trigger patterns. And the four on-disk copies are **not**
byte-identical (four distinct sha256); what is actually frozen (by the import-time assertion) is the *G²
computation* — `signed_g2` / `compute_control` / `K` / `FRAME_WIN` / `CONNECTIVES` — **none of which
`F(p)` uses.** Consequently the `F(p)` n-gram extraction, the content-word selection, the log/aggregation
to a per-paradigm scalar, and the item-set targeting are **all new code with genuine DoF, authored by
someone who already knows the accuracies and ρ_prof.** That is exactly the exposure the design claims to
have closed.
*Fix:* (a) rewrite G1 to state the honest reuse boundary — only the streaming adapter + tokenization
regexes are reused; the n-gram extraction and `F(p)` aggregation are **new**; (b) the import-time
assertion in `build_freq.py` must pin the *actually-copied* code (streaming/tokenization), not the G²
kernel; (c) bind that `build_freq.py` and the full `F(p)` recipe are frozen in `PREREG.md` **and
independently reproduced by a fresh-agent verifier from the frozen spec before `F(p)` is computed against
the real paradigm→H mapping**; (d) keep the scrambled-mapping negative control, but note it does **not**
catch `F`-definition tuning on the real mapping (a scramble collapses ρ_prof to ~0 regardless of `F`), so
it is necessary-not-sufficient.

**BLOCKER-2 — under Q2-A the covariate controls the wrong frequency; a SURVIVES would not rebut C8's
literal confound.** C8's prose names *construction* frequency: "rare island/scope contrasts *both*
human-harder *and* less-represented." Q2-A partials out *surface content-word n-gram frequency* — lexical
familiarity, not construction frequency. So a SURVIVES under Q1-A/Q2-A licenses only "R1 is
over-and-above **lexical/surface exposure**," which is strictly weaker than "over-and-above construction
frequency." This is a *second* load-bearing scope caveat that the design does not carry (Q3-A's caveat
covers only "C4 ≠ pretraining corpus"). It is also the substantive reason the covariate arm alone cannot
carry the promotion. *Fix:* add the surface-vs-construction scope caveat as load-bearing in G3 and on any
result page; state that the covariate arm's honest reach is "over-and-above lexical/surface exposure,"
never "over-and-above construction frequency," unless Q2-C is run — and note that the swap arm, too,
targets lexical/exact-string memorization, so **even Q1-C leaves construction frequency only indirectly
addressed.** The promotion candidacy must inherit this scope, not launder it away.

**BLOCKER-3 — the verdict map is missing the high-collinearity branch.** The design handles
`corr(F,H)≈0` (confound absent → R1 corroborated) but not `corr(F,H)≈high`. When `F` and `H` are strongly
correlated (which is *the confound scenario the control exists for*), the partial coefficient has inflated
variance and, worse, if `F` tracks depth at all, partialling it strips genuine shared structure — so a
BREAKS becomes uninterpretable (frequency artifact vs. over-control cannot be separated). *Fix:*
pre-register a frozen high-`corr(F,H)` threshold above which the partial ρ is reported **INCONCLUSIVE
(uninterpretable / over-control-suspect)**, a distinct branch from both SURVIVES/BREAKS and the
`corr(F,H)≈0` corroboration.

---

## SHOULD-FIX

- **Power stated on the wrong quantity (G4).** G4 reports power at the *point-estimate* threshold
  (partial |ρ|≈0.32 at df=37). But the binding criterion is "CI excludes 0," and the partial point
  estimate will *drop* from the raw +0.54–0.63 toward ~+0.3–0.4 while per-model bootstrap CIs at n=40 are
  wide (the raw CIs already span e.g. [+0.357,+0.795]). The realistic risk is that the weaker models land
  **INCONCLUSIVE** (CI includes 0) even on a true partial ~+0.35. State power as *P(bootstrap CI excludes
  0) at the expected partial magnitude, per model* — not the point threshold.
- **SURVIVES band internal tension.** "partial ρ ≥ +0.3 **with** CI excluding 0" — at df=37 the
  CI-excludes-0 gate already requires |ρ|≳0.325, so the +0.3 floor sits *below* its own CI criterion and
  is nearly inert. Reconcile: state that CI-exclusion is the binding criterion and +0.3 is a
  non-binding floor, or raise the floor to match.
- **C4-adoption provenance points at a "scouting" page that adopts nothing.**
  `resource/cooccurrence-corpus-scouting` is `status: scouting` and states verbatim "Nothing was fetched,
  downloaded, built, or adopted … No `anchors:` link is asserted." The *actual* C4 fetch + frozen recipe
  live in the run dirs (earliest `2026-07-08-relation-recovery-taxonomic-proxy/build_cooc_c4.py`, which
  streams shards 00000–00002 under ODC-BY + the Common-Crawl-terms layer, carried to provenance as "rider
  3"). Cite that run as the operative provenance for "C4 fetched, license-carried," and carry the
  Common-Crawl-terms layer into any result page — don't rest the corpus provenance on a scouting note.
- **Bind Q2-B as sensitivity-only, hard.** The decorrelation vote flagged Q2-B as the spot most likely
  "aimed" (a control selected because it tends to break the result). The design already says
  sensitivity-only; make it a hard freeze condition (G2) that Q2-B is never a decision gate and its
  over-control caveat is load-bearing on every mention.

## NITS

- "byte-frozen C4 counting recipe (`build_cooc_c4.py`, s193/s199/s202)" — the file is *not* byte-identical
  across those runs (4 distinct sha256); what is byte-frozen is the G² *kernel* via import assertion.
  Tighten the wording so it doesn't read as "the whole file is frozen."
- meaning-senses tags (`constructional`, `human-comparison`, `measurement-epistemic`) are all in the
  controlled vocabulary and apt. No lint issue.
- Cost/decision-trail framing is clean; the `predictions.md`-row-at-freeze and `ABORT_USD`-on-swap-arm
  fences are correctly deferred to the freeze session.

---

## Fabrication / provenance check — CLEAN

| Quoted item | In design | In-repo artifact | Match |
|---|---|---|---|
| ρ_prof `+0.606 / +0.543 / +0.628` | design front-matter + §R1 | `result/blimp-forced-choice-sweep-v1` lines 48, 84 | ✅ verbatim |
| n = 40 paradigms | throughout | result "40 BLiMP paradigms" | ✅ |
| F3 SD `0.12 / 0.15 / 0.11` | design §confound | result line 83 / §reading-3 | ✅ |
| human depth-gap `+0.065` | design §confound context | result table | ✅ |
| human CSV sha256 `ea0e7c21…` | design §why-owed-2 | `resource/blimp` + committed file (3,057 bytes) | ✅ |
| **C8 verbatim** (block quote) | design lines 42–48 | parent design C8 lines 439–457 (ellipsis skips the "because…" clause) | ✅ faithful |
| frozen s205 accuracies reusable | design §why-owed-2 | `2026-07-10-blimp-forced-choice-sweep/results.json` present | ✅ |

**Linked pages all exist:** `result/blimp-forced-choice-sweep-v1`, `resource/blimp`,
`resource/cooccurrence-corpus-scouting`, `source/mahowald-2024-dissociating`,
`essay/shadow-depth-cross-cuts-grain`, and the resolved decision `blimp-forced-choice-sweep-design` all
resolve. No aspirational link to a non-existent page. **The one provenance defect is not a fabrication but
a misdescription:** `build_cooc_c4.py` does not compute the n-gram frequencies the design says it will
byte-reuse (BLOCKER-1).

## Anchor discipline — CORRECT

`anchor: resource/blimp` (human-comparison, **not** internal-contrast-only) is the right declaration.
R1's force is the correlation of per-paradigm accuracy against BLiMP's per-paradigm human agreement
`H(p)`; the control's output is a *partial* Spearman that **still correlates against `H(p)`**, so the
control tests the *validity* of the human comparison without converting it to a within-model contrast.
`resource/blimp` exists and now carries the committed per-paradigm anchor (sha256 `ea0e7c21…`), so the
`anchors: resource/blimp` typed link is earned. A control that reuses the frozen accuracies does not lose
the human key — reusing accuracies is a within-subject re-analysis of the *model* side; the *human* side
(`H(p)`) is untouched and remains load-bearing. Declaration is right; do not retreat to
internal-contrast-only.

## Anti-cheat — G1 is INSUFFICIENT as written; the swap arm is REQUIRED for promotion

The reuse-of-known-accuracies exposure is real and is **not** closed by G1, for two compounding reasons:
(1) BLOCKER-1 — the byte-reuse fence covers the G² kernel, which `F(p)` does not use; the `F(p)` recipe is
new code with genuine DoF authored with the accuracies known, and "freeze before compute" cannot fully
neutralize an outcome-sensitive *definition* choice (bigram vs trigram, content-word selection, log vs
raw, aggregation). (2) BLOCKER-2 — under Q2-A the covariate controls lexical familiarity, not C8's
construction frequency, so a clean SURVIVES still leaves C8's literal confound un-rebutted.

**Concrete recommendation:** **require Q1-C (add the swap arm) for any human-comparison PROMOTION.** Permit
the covariate arm alone to earn only a *robustness / corroboration* result (never a promotion candidacy).
Additionally bind: a single primary `F` definition + one pre-specified sensitivity variant, **no post-hoc
proxy tuning**; a proxy-validity audit (show `F(p)` has a sensible relation to an external frequency
benchmark) run *before* any partial outcome is inspected; fresh-agent independent reproduction of
`build_freq.py` before `F(p)` touches the real mapping; and the scrambled-mapping negative control
reported (necessary-not-sufficient). This converges with the parallel decorrelation vote (GO-WITH-
CONDITIONS; Q1-C; covariate-alone "not strong enough … the swap arm is needed"; proxy-validity-audit
condition) — two independent reviewers land on **the swap arm being required for promotion.**

## Freeze conditions I would bind (extending/refining G1–G5)

- **G1′ (rewrite).** Honest reuse boundary: only `stream_sentences` + tokenization regexes are reused; the
  n-gram extraction + `F(p)` aggregation are new, frozen in PREREG, and **independently reproduced by a
  fresh-agent verifier before the real `F(p)` is computed.** Import-time assertion pins the copied
  streaming/tokenization code, not the unused G² kernel.
- **G2 (keep, harden).** Q2-B is a labelled conservative sensitivity arm only, never a decision gate; the
  over-control caveat is load-bearing on every mention.
- **G3′ (extend).** The proxy caveat carries **both** "C4 ≠ the panel's pretraining corpus" **and**
  "surface-lexical frequency ≠ construction frequency"; the covariate arm's honest reach is
  "over-and-above lexical/surface exposure," never "over-and-above construction frequency."
- **G4′ (strengthen).** Power stated as P(bootstrap CI excludes 0) at the expected partial magnitude,
  per model; reconcile the +0.3 SURVIVES floor with the n=40 CI-exclusion threshold (~0.325).
- **G5 (keep).** Swap items' grammatical contrast re-validated before scoring; frozen frequency-balanced
  swap word-list; broken pairs dropped-and-logged, never silently repaired.
- **G6 (NEW).** Collinearity guard: a frozen high-`corr(F,H)` threshold above which the partial ρ is
  reported INCONCLUSIVE (over-control-suspect), distinct from the `corr(F,H)≈0` corroboration branch.
- **G7 (NEW).** Single primary `F` + one pre-specified sensitivity variant; no post-hoc proxy tuning;
  proxy-validity audit before inspecting any partial outcome (adopts the decorrelation vote's condition).
- **G8 (NEW).** Q1-C swap arm required for a human-comparison PROMOTION; covariate-alone → robustness /
  corroboration only. Promotion candidacy inherits the surface-vs-construction scope (G3′).

---

**Closing summary:** GO-WITH-CONDITIONS — provenance and anchor discipline are clean, but the design
overstates its central anti-cheat fence (`build_cooc_c4.py` does no n-gram counting, so `F(p)` is new
DoF) and, under Q2-A, controls lexical familiarity rather than C8's construction frequency; the covariate
arm alone is a robustness result, and **the swap arm (Q1-C) is required to license the promotion.**
