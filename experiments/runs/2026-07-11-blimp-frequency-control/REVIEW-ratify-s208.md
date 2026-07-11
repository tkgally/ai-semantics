# Ratification review — BLiMP R1 frequency control (C8 promotion-prep), s208

Independent adversarial ratification reviewer (fresh agent, verdict authority; did NOT author the design
or any downstream artifact). Read PROTOCOL §2–3, the open decision, the full design, REVIEW-design-s207 +
VOTE-s207, the downstream result + frozen results.json + human anchor, and `build_cooc_c4.py` firsthand.
Paired with one non-Anthropic decorrelation vote (`gpt-5.4-mini`, VOTE-ratify-s208.json, $0.003099;
RATIFY-WITH-CONDITIONS, Q1-C / Q2-A / Q3-A, G8=Y).

## 1. OVERALL: RATIFY-WITH-MODIFICATION
Gates honestly constructed; null pre-named symmetrically; provenance + anchor CLEAN; s207 blockers
genuinely discharged in-design. Adopt Q1-C (over the Q1-A default; converging with both prior reviewers),
keep Q2-A (surface-scoped) primary, keep Q3-A, adopt G8 as BINDING, add ONE freeze condition (G9) on
staging/labeling. The covariate-only staging is coherent and honest under G8 — fixing the higher
(both-arms) promotion bar now, then running the cheap half as an explicitly-demoted robustness datum, is
the anti-cheat-conservative reading of C8, not a lowered one.

## 2. Per-gate ruling
- Q1 = C. Two independent reviewers converged; reasons non-redundant: the covariate arm carries an
  irreducible reuse-of-known-accuracies exposure (G1′) AND, under Q2-A, controls only surface-lexical
  familiarity — strictly weaker than C8's literal "corpus-frequency covariate for each construction." The
  swap arm tests a different causal channel (exact-string memorization), fresh items/calls, no accuracy
  exposure. The program's first broad human-anchored grammatical claim deserves the conjunction.
- Q2 = A primary, honestly scoped (surface-lexical); Q2-B sensitivity-only; REJECT the vote's Q2-C-as-
  primary. The critic's collinearity argument is decisive: construction frequency is near-collinear with
  depth (rare = deep = human-harder), so partialling it reproduces the Q2-B over-control hazard — a BREAKS
  under Q2-C could not separate "frequency artifact" from "the shared structure IS the depth structure."
- Q3 = A (promotion gate; standalone result either way; cross-session promotion review writes the claim),
  with the G6 collinearity branch and both G3′ caveats load-bearing.

## 3. G8: ADOPT-BINDING
Covariate arm alone = robustness/corroboration only; Q1-C swap arm required for any human-comparison
PROMOTION. Over-determined by (i) residual definitional-DoF exposure of an accuracy-known author (G1′) and
(ii) the surface-vs-construction scope gap (G3′). Promotion candidacy requires SURVIVES ∧ SWAP-STABLE.

## 4. Staging ruling: YES — coherent and honest.
Ratifying Q1-C RAISES the promotion bar to both arms before either runs, and G8 forecloses reading a
covariate SURVIVES as C8-satisfied. Yardstick fixed ahead of data; covariate arm's honest ceiling
(robustness only) fixed by G8 not chosen after outcome; running the free arm first is correct budget
discipline. The one hazard (a later reader mistaking the interim covariate result for a satisfied
promotion gate) is closed by G9.

## 5. Anti-cheat verdict: ADEQUATE (robustness/corroboration only; NOT promotion — which G8 forbids).
PREREG-before-compute + fresh-agent independent reproduction of build_freq.py from the frozen spec before
F(p) meets the paradigm→H mapping + scrambled-mapping negative control (necessary-not-sufficient) + frozen
collinearity guard + G7 single-primary-F/no-post-hoc-tuning fences the residual exposure proportionately
to a demoted robustness datum. Not fatal precisely because G8 caps the covariate arm below promotion.

## 6. Provenance check (independently confirmed)
- (a) ρ_prof +0.606/+0.543/+0.628 — CONFIRMED (results.json 0.6062679/0.5431747/0.6277811).
- (b) build_cooc_c4.py has NO n-gram frequency counter — CONFIRMED firsthand (only stream+tokenize;
  unigram df over a fixed target set; cue co-occurrence + signed-G² kernel; Hearst via fixed pattern
  membership). Import assertion pins the G² kernel, which F(p) does not use. F(p) is genuinely new code
  with DoF; G1′ correction accurate; s207 BLOCKER-1 correctly raised + discharged.
- (c) C8 verbatim — CONFIRMED, with a clarifying note: the design's block quote is verbatim to the parent
  design's binding C8 ("…a pre-registered corpus-frequency covariate FOR EACH CONSTRUCTION partialled from
  ρ_prof…"). The resolved-decision resolution-field summary paraphrases and drops "for each construction,"
  but the binding text names *construction* frequency — which STRENGTHENS the ruling (Q2-A must be honestly
  under-scoped per G3′; covariate arm alone cannot satisfy the promotion gate per G8). No fabrication.

## 7. Added freeze condition
G9 (NEW — staging/labeling honesty). When the covariate arm is run without the swap arm, its result page
must (a) be typed/titled as a ROBUSTNESS / CORROBORATION result, (b) state on its face that C8's promotion
gate is NOT satisfied and the Q1-C swap arm is the outstanding requirement, (c) carry both G3′ caveats,
(d) NOT advance the shadow-depth table's form-(iv) row toward a claim. Plus a G7 sharpening: F(p) fixed to
a single zero-post-freeze-latitude recipe; the fresh-agent verifier certifies that property and runs the
external-benchmark proxy-validity audit BEFORE any partial outcome is inspected. All other freeze
conditions (G1′, G2, G3′, G4′, G5, G6, G7, G8) adopted as recorded on the design.
