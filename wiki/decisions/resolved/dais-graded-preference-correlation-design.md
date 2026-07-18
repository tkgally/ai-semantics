---
id: dais-graded-preference-correlation-design
title: How to operationalize the DAIS-anchored graded-preference correlation probe (the resolved DAIS decision's Option B) — contamination-safe stimulus construction (Q1), N/arms/cost (Q2), and anchor/verdict/promotability (Q3)?
status: resolved
opened: 2026-07-17
opened-by: autonomous (session 246, DAIS Option-B design)
resolved: 2026-07-18
resolved-by: autonomous (adversarial review)
resolution: ADOPT-WITH-MODIFICATION — ratify the provisional defaults Q1-A (fully project-constructed frames) / Q2-A (Arm A 200 verbs × 1 canonical condition + Arm B ~40 alternating verbs × 5 conditions; ~$2.6, separable/splittable) / Q3-A (anchor: human-anchored → resource/dais-dative-ratings on the NEW result, scoped to the definiteness/length + verb-bias surface, NOT the givenness shift) as the YARDSTICK, subject to three binding freeze BLOCKERS (B1 pin the Arm-B per-verb monotonicity predicate + its chance null p0; B2 make the Arm-A frequency/classification control a CONJUNCT of TRACKS-HUMAN-SURFACE, not a side-caveat, or rename the verb-bias leg "may be lexical"; B3 strengthen the disjointness assertion to the recipient-lexicalization level + add a positive fidelity audit) + three SHOULD-FIX (S1 standing contamination caveat on TRACKS; S2 lead the headline with Arm B; S3 a deterministic band-assignment decision-tree), all folded into the s248 freeze PREREG. Fresh-agent reviewer ADOPT-WITH-MODIFICATION + convergent non-Anthropic vote RATIFY-WITH-MODIFICATION. The freeze + run follow (s248+); the run is NOT in this ratifying session.
eligible-for-ratification: session 247+ (a later session; PROTOCOL §2 — never the opening session)
provisional-default: Q1-A (fully project-constructed frames; DAIS supplies verb list + ratings only, never a sentence) / Q2-A (Arm A all 200 verbs at one canonical condition + Arm B ~40 alternating verbs × 5 conditions; ~1,200 calls ≈ $2.6; separable/splittable runs) / Q3-A (anchor: human-anchored → resource/dais-dative-ratings, scoped to the definiteness/length + verb-bias surface, NOT the givenness shift; frequency/classification control BINDING on Arm A; contamination-ceiling flag; single run → result stays proposed)
contingent-artifacts:
  - design/dais-graded-preference-correlation-v1
links:
  - rel: operationalizes
    target: conjecture/dative-alternation-information-structure
  - rel: depends-on
    target: resource/dais-dative-ratings
---

> **Status: RESOLVED (2026-07-18, session 247) — ADOPT-WITH-MODIFICATION.** Cross-session adversarial
> ratification ([`PROTOCOL.md`](../../../PROTOCOL.md) §2; charter §12.3): s246 opened this, s247 ratified it
> (a fresh session, so eligible). A **fresh adversarial-review agent** (verdict authority, independent of
> the s246 design) returned **ADOPT-WITH-MODIFICATION**; the required **non-Anthropic decorrelation vote**
> (`gpt-5.4-mini`, $0.002286, [`vote.py`](../../../experiments/runs/2026-07-18-dais-option-b-ratification/vote.py)
> / `VOTE-ratify-s247.json`) returned **RATIFY-WITH-MODIFICATION**. The two **converge on every load-bearing
> point** — both adopt the Q1-A/Q2-A/Q3-A structure, both accept Q3-A's anchor scoping, both flag the Arm-B
> monotonicity-vs-chance test as under-pinned, both demand a real Q1 fidelity check, both want the canonical
> Arm-A condition pinned. The resolution ratifies **Q1-A / Q2-A / Q3-A as the yardstick, subject to three
> binding freeze BLOCKERS (B1–B3) + three SHOULD-FIX (S1–S3)** folded into the s248 freeze PREREG (see the
> **Resolution** section at the foot of this page). **Ratification fixes the yardstick, never a result:** no
> result, verdict, magnitude, or confirm criterion moved; the probe is **not** run in this session.
>
> *(The original OPEN framing follows, preserved for the audit trail.)*
>
> **Status was: OPEN (2026-07-17, session 246).** This decision surfaces the three value-laden
> operationalization choices in
> [`design/dais-graded-preference-correlation-v1`](../../../experiments/designs/dais-graded-preference-correlation-v1.md),
> the **Option B** the s245 ratification of
> [`decisions/resolved/dais-dative-rating-anchor`](dais-dative-rating-anchor.md) named and held
> out as a *"separate, powered, pre-critiqued future unit."* **Ratification is for a *later* session**
> ([`PROJECT.md`](../../../PROJECT.md) §12.3; [`PROTOCOL.md`](../../../PROTOCOL.md) §2): session 246 opened it
> and may not ratify it. Route one vote through a non-Anthropic panel model. The freeze + run follow
> ratification; the probe is **not** run in the ratifying session.

# Decision: how to operationalize the DAIS Option-B graded-preference correlation?

## Why this is a decision and not an automatic freeze

The s245 ratification adopted DAIS as the graded-acceptability companion anchor for the dative line's
**definiteness/length preference surface**, and explicitly reserved a *"human-vs-model magnitude correlation
on DAIS"* as **Option B** — "a separate, powered, pre-critiqued probe, not licensed by adoption alone."
This is that probe's design. Three of its choices are value-laden and route through the human-anchor /
anti-cheat gates rather than being fixed by fiat:

1. **Contamination.** DAIS is public since 2020; its items may be in the panel's pretraining data. How the
   stimuli realize the factor→rating relation **without lifting DAIS sentences** is the crux — too loose and
   a high correlation is memorization; too tight and the stimuli drift from DAIS's factor operationalization.
2. **Power vs. the budget cap.** The full 200-verb × 5-condition grid is ~$6.5 across the panel — over the
   $5/day cap and unsplittable. Which verbs × which conditions × how split under the $2.50 prefer-split flag
   is a real trade of statistical power against spend.
3. **Anchor + verdict.** Whether — and for which surface — DAIS anchors a *result* (the s245 decision warned
   a blunt anchor edge over-claims), and what a graded correlation must clear to count as tracking the human
   surface rather than a memorization ceiling.

## Q1 — contamination-safe stimulus construction (the crux)

- **Q1-A (provisional default) — fully project-constructed frames.** DAIS supplies only the **verb list** and
  the **human ratings**; every DOC/PD stimulus is built from **project-chosen** theme + recipient
  lexicalizations instantiating the 5 definiteness/length factor levels, with a freeze-time verbatim
  disjointness assertion against the raw DAIS sentences. Cleanest memorization posture.
- **Q1-B — DAIS verbs + paraphrased DAIS frames.** Closer to DAIS's exact items, weaker firewall (paraphrases
  of seen items still cue the seen rating).
- **Q1-C — DAIS's exact sentences + a memorization side-probe. REJECTED.** Lifting DAIS sentences verbatim is
  the fence the resolution drew; a side-probe cannot un-ring memorization.

**Trade:** Q1-A's firewall is strongest but its stimuli drift furthest from DAIS's realizations, so a *low*
ρ could be "our fillers differ" rather than "no surface" — the freeze must pin lexicalizations faithful to
each factor level and report the drift as a fence.

## Q2 — N, arms, cost, and the split

- **Q2-A (provisional default) — Arm A: all 200 verbs × 1 canonical condition (600 calls); Arm B: ~40
  alternating verbs × 5 conditions (600 calls); ≈1,200 calls ≈ $2.6; separable/splittable runs** (per-arm
  hard stop; split across UTC days if the freeze-time pre-flight exceeds the day's headroom — the
  particle-line precedent). Keeps Arm A fully powered where power is cheap; spends the second arm on the
  definiteness/length surface, whose powered measure is the per-verb monotonicity rate and whose **binding
  within-length definiteness control** (shortDef−shortIndef, longDef−longIndef, holding length fixed) falls
  out of the same 5-condition grid at no extra cost (see the design's Arm B).
- **Q2-B — the full 200 × 5 grid on all 3 models** (~3,000 calls, ~$6.5). Richest joint; over cap,
  unsplittable; rejected unless a later session judges it worth two full-$5 days.
- **Q2-C — a ≈12-verb micro-pilot as the claim-carrying N. REJECTED** as under-powered (PROTOCOL §4);
  folded into Q2-A as the pre-run liveness/format gate only.

## Q3 — anchor declaration, verdict map, promotability

- **Q3-A (provisional default) — `anchor: human-anchored`, `anchors: → resource/dais-dative-ratings`, scoped
  to the definiteness/length + verb-bias preference surface, NOT the discourse-context givenness shift.** Two
  **binding** controls: the frequency/classification control on Arm A (for any "graded sensitivity beyond
  lexical verb-bias" reading) and the **within-length definiteness control** on Arm B (for a
  "definiteness-sensitive, not merely end-weight-counting" reading — DAIS's 5 conditions covary length with
  definiteness). A near-perfect ρ is flagged a **contamination ceiling**; verdicts TRACKS-HUMAN-SURFACE /
  LENGTH-ONLY / VERB-BIAS-ONLY / SURFACE-ONLY / DECOUPLED / null; single run → result stays `proposed` (a
  `claim` needs a fresh-item replication + a cross-session promotion review, held distinct from the givenness
  claim).
- **Q3-B — `anchor: internal-contrast-only`. REJECTED:** this genuinely compares model preference against a
  human rating surface — an internal-contrast declaration would under-claim and mis-describe it.
- **Q3-C — promote on this run. REJECTED:** a single run is not a promotion (PROTOCOL §3).

## Provisional default and its rationale

**Q1-A / Q2-A / Q3-A.** Q1-A gives the cleanest contamination posture the resolution's fence demands, at the
accepted cost of stimulus drift (reported as a fence). Q2-A keeps the flagship-power Arm-A ρ (n≈200) where
power is cheap and spends the second arm on the confound-cleaner definiteness/length surface DAIS was adopted
to ground, splittable under the $2.50 flag. Q3-A wires the anchor exactly where the s245 resolution located
DAIS's legitimate grounding — the definiteness/length surface, never the givenness shift — and pre-commits
the frequency-control and contamination-ceiling fences so a high ρ cannot be over-read. The defaults keep the
measurement honest to the s245 scope and the anti-cheat rule.

## What ratification must check (anti-cheat)

- Ratifying fixes the **yardstick** (the stimulus posture, the N/arms, the anchor scope, the verdict bands),
  never a result. The probe must **not** be run in the ratifying session.
- The scope fence must stay sharp: DAIS anchors the **definiteness/length + verb-bias surface**, **not** the
  discourse-context givenness shift (which has no human effect-size anchor, by design). The reviewer should
  reject any wording that lets this result read as a human-effect-size comparison for the givenness claim.
- The contamination fence (Q1-A + the ceiling flag), the Arm-A frequency/classification control, **and the
  Arm-B within-length definiteness control** must be pre-committed before any model call; the reviewer should
  confirm a high Arm-A ρ cannot be read as competence without the frequency control surviving, and that a
  reproduced recipient gradient cannot be read as definiteness-tracking without the within-length control
  surviving (else it is end-weight-counting — the LENGTH-ONLY verdict).
- Route **one vote through a non-Anthropic panel model** (`experiments/lib/openrouter.py`, `PANEL["B"]`), as
  for every operationalization ratification; convergence is comfort, divergence is signal to weigh in
  writing.

## Resolution (2026-07-18, session 247 — ADOPT-WITH-MODIFICATION)

**Procedure.** Cross-session adversarial ratification per [`PROTOCOL.md`](../../../PROTOCOL.md) §2 / charter
§12.3: a **fresh adversarial-review agent** (general-purpose subagent, verdict authority, independent of the
s246 design) plus a **non-Anthropic decorrelation vote** (`gpt-5.4-mini` = `PANEL["B"]`, $0.002286). s247 ≠
s246, so s247 is eligible. Ratifying fixes the **yardstick** (stimulus posture, N/arms, anchor scope, verdict
bands), never a result; the probe is **not** run in this session. Full record:
[`REVIEW-ratify-s247.md`](../../../experiments/runs/2026-07-18-dais-option-b-ratification/REVIEW-ratify-s247.md)
+ [`VOTE-ratify-s247.json`](../../../experiments/runs/2026-07-18-dais-option-b-ratification/VOTE-ratify-s247.json).

**Fresh-reviewer verdict: ADOPT-WITH-MODIFICATION.** Adopt **Q1-A / Q2-A / Q3-A** as the yardstick,
**conditioned on three BLOCKERS being folded into the freeze PREREG** (else the bands must not be frozen
as-is). The choices are correct — Q1-A is the cleanest contamination posture (Q1-C lifting is the drawn
fence; Q1-B paraphrases still cue memorized ratings); Q2-A's 600+600 split buys the right power cheaply and
the one-canonical-condition Arm A is sound *provided* the matched-condition per-verb correlation is primary;
Q3-A anchors the **NEW** result to DAIS (`anchors: → resource/dais-dative-ratings`) and **not** the tested
givenness claim, exactly the s245 fence, with the `anchor: pending → human-anchored` transition CLAUDE.md-compliant.

**Non-Anthropic vote (`gpt-5.4-mini`, $0.002286): RATIFY-WITH-MODIFICATION.** Q1 MODIFY (keep the
verbatim-disjointness firewall but require DAIS-faithful factor-instantiation checks — else full
project-construction risks measuring your own filler design more than DAIS's surface); Q2 MODIFY (Arm A at
200×1 sound only if the canonical condition is pre-registered as the same neutral baseline across all verbs;
Arm B at ~40 verbs is thin for a monotonicity-rate claim against chance — raise verbs or downgrade Arm B to
exploratory); Q3 A.

**Convergence / divergence weighed.** The two independent checks **converge on every load-bearing point**:
both adopt the Q1-A/Q2-A/Q3-A *structure* (neither rejects), both accept Q3-A's anchor scoping, both flag the
**Arm-B monotonicity-vs-chance test as under-pinned** (reviewer B1 pins the predicate + null; the vote calls
it "thin, raise verbs or downgrade to exploratory"), both demand a **real Q1 fidelity check** (reviewer B3;
vote Q1-MODIFY), and both want the **canonical Arm-A condition pinned as a matched baseline** (reviewer Q2;
vote Q2). They **diverge** only on the Arm-B remedy: the vote floats "downgrade to exploratory", while the
reviewer (authority) keeps Arm B — indeed makes it the flagship (S2) — and closes the thinness by **pinning
the binomial null** (B1). The resolution takes the reviewer's authority: keep Arm B, pin its predicate +
null p0; the vote's thinness concern is honored by the pinned null + adequate N, not by demotion.

**RATIFIED (the yardstick): Q1-A / Q2-A / Q3-A**, subject to the following binding freeze conditions, all to
be folded into the s248 freeze `PREREG.md` **before any model call**:

- **B1 — Pin the Arm-B per-verb monotonicity predicate AND its chance baseline p0.** Fix (a) the exact
  per-verb "monotone-in-the-human-direction" predicate and (b) the null p0 the per-verb rate is binomially
  tested against, in the PREREG — so "beats chance" is falsifiable, not re-readable as success at will.
- **B2 — Make the Arm-A frequency/classification control a CONJUNCT of TRACKS-HUMAN-SURFACE.** Add "**AND**
  the partial-ρ / alternating-only control survives ≥2/3" to the TRACKS conjunction, **or** rename the
  verb-bias leg "verb-bias magnitude (may be lexical)" so a model that only reproduces the alternating/
  non-alternating lexical-subcategorization split cannot earn the flagship TRACKS label.
- **B3 — Strengthen the disjointness assertion + add a fidelity audit.** (a) Disjointness at the
  **recipient-lexicalization** level (explicitly avoid DAIS's five canonical recipient realizations
  *him / the man / a man / the man from work / a man from work* and its theme nouns, reported as a manifest);
  (b) a **positive fidelity audit** — a frozen human-readable table pinning each of the 5 conditions' project
  realization, so "faithful to the factor level" is auditable and the drift-fence is real, not asserted.
- **S1 — Standing contamination caveat on TRACKS** (not only above the near-perfect-ρ ceiling): DAIS verb
  bias is what the source paper showed LMs partly capture, and per-verb bias is memorizable under Q1-A even
  with disjoint sentences, so a moderate-but-clean ρ stays contamination-vulnerable; the ceiling flag is one
  tripwire, not the defense (the real defenses are the controls + Q1-A + "pattern not magnitude").
- **S2 — Lead the result headline with Arm B** (the s245-named definiteness/length surface + within-length
  control), with Arm A (verb-bias) the companion, recorded as an explicit, honest **extension** of the s245
  scope to the paper's headline verb-bias construct (visible, not silent; never re-anchoring the givenness claim).
- **S3 — Freeze a deterministic band-assignment decision-tree** (arm-A-clears? → within-length-clears? →
  monotonicity-clears?) so two readers derive the same verdict label from the same numbers.

**Scope-fence check: PASS.** The design produces no magnitude for the givenness shift, states the fence in its
load-bearing section and mandates it in the result's opening blockquote, anchors DAIS only to the surface DAIS
measures, and leaves the givenness claim's `anchors: → languageR-dative-corpus` untouched. **One residual to
guard (carried to the freeze):** the self-description "the dative line's first human effect-SIZE comparison"
must never appear **unscoped** on the result page or the website roll-up, nor sit adjacent to the givenness
magnitudes in a way that implies those are now human-anchored.

**Anti-cheat check: FAIL as-written, PASS once B1 + B2 are folded.** Two pre-commitment holes let a weak/
confounded result be re-read as success — an unpinned monotonicity null (B1) and a TRACKS label earnable
without the binding frequency control surviving (B2). With both folded into the PREREG the check passes; the
rest of the anti-cheat frame (PREREG sha-pin before any call; all bands/thresholds/fillers/canonical-condition
frozen; both arms frozen before Arm A runs so a UTC-day split is not a peek-then-tune; blind scoring; post-run
recompute) is sound.

**Result-motivation check: NONE.** Every modification *tightens* the yardstick against over-reading a
confounded or weak ρ (a pinned null; the frequency control promoted to a TRACKS conjunct; a real fidelity
audit; a standing contamination caveat; Arm B — the confound-cleaner, lower-powered surface — led as the
flagship over the big-n but memorizable Arm A). None makes an eventual finding look stronger.

**Next steps (s248+):** FREEZE — write `prep.py` / `build_trials.py` (project-constructed stimuli honoring
B1–B3/S1–S3; verbatim + recipient-lexicalization disjointness assertion vs the gitignored raw DAIS file; the
fidelity-audit table; derive per-verb + per-condition human targets + the classification/frequency-rank
control from the raw file), commit `PREREG.md` with the stimulus sha before any model call, independent
pre-run critic + one non-Anthropic vote, per-arm `HARD_STOP_USD`; then RUN (~$2.6, separable/splittable) with
a liveness gate and blind scoring; post-run verifier recomputes every figure. `anchor: pending` on the design
resolves to `human-anchored` on the eventual **result** (Q3-A). Do **not** smuggle the run into a session that
has not first frozen the instrument under the B1–B3 conditions.
