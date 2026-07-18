# Fresh-agent adversarial ratification review — DAIS Option-B graded-preference correlation design (s247)

**Procedure.** Cross-session adversarial ratification (`PROTOCOL.md` §2; charter §12.3): a **fresh
adversarial-review agent** (general-purpose subagent, verdict authority, independent of the s246 design)
read the open decision + the full design + the s245 resolved DAIS-anchor decision + the DAIS resource
page + the tested givenness claim + the dative conjecture + CLAUDE.md typed-links/anchor discipline, and
spot-checked the committed human gradient (`verb_recipient_means.csv` + `inspection_manifest.json`). One
**non-Anthropic decorrelation vote** (`gpt-5.4-mini` = `PANEL["B"]`, cutoff-aware preamble; `vote.py` →
`VOTE-ratify-s247.json`, $0.002286) was cast as advisory QA. s247 ≠ s246, so s247 is eligible to ratify.
Ratifying fixes the **yardstick** (stimulus posture, N/arms, anchor scope, verdict bands), never a result;
the probe is **not** run in this session.

## Fresh-reviewer verdict: ADOPT-WITH-MODIFICATION

Adopt **Q1-A / Q2-A / Q3-A** as the yardstick, **conditioned on three BLOCKERS being folded into the
freeze PREREG**; if they are not, the bands must not be frozen as-is. Human gradient reproduced as cited
(pronoun 37.74 > shortDef 30.50 > shortIndef 25.15 > longDef 20.78 > longIndef 18.31; alternating 33.97
vs non-alternating 18.92).

- **Q1: A.** Fully project-constructed frames is the correct contamination posture (Q1-C lifting is the
  drawn fence; Q1-B paraphrases still cue memorized ratings). But the freeze mechanic as written is
  near-vacuous — a "no full DOsentence/PDsentence string verbatim" assertion passes trivially once the
  theme changes, and proves little about the real channel (per-verb/per-construction bias memorization,
  not sentence reuse). → see BLOCKER 3.
- **Q2: A.** The 600+600 split at ~$2.6, per-arm HARD_STOP, splittable across UTC days (particle
  precedent) buys the right power cheaply. Fixing Arm A at one canonical condition is sound **provided**
  the matched-condition correlation (model-shortDefinite vs human-shortDefinite per verb) is primary and
  the collapsed-mean version is an explicit robustness check only. n≈40 for Arm B is adequate — the issue
  is the unpinned monotonicity null (BLOCKER 1), not the N.
- **Q3: A.** Anchoring the NEW result (`anchors: → resource/dais-dative-ratings`) and NOT the givenness
  claim is exactly the s245 fence; `anchors`-on-result → resource is CLAUDE.md-correct; the
  `anchor: pending → human-anchored` transition with the decision named in `contingent-on:` is compliant.
  Q3-B (internal-contrast) would under-claim a genuine human-vs-human-rating comparison.

## BLOCKERS (binding — must be folded into the freeze PREREG before any model call)

- **B1 — Pin the per-verb monotonicity predicate AND its chance baseline p0 before any call.** "Arm B
  monotonicity rate beats chance" is unfalsifiable-adjacent until frozen: exact-human-rank-order gives
  p0 = 1/120 (trivially beaten by a handful of verbs); a coarse trend test gives p0 ≈ 0.5. The PREREG must
  fix (a) the per-verb monotone-in-human-direction predicate and (b) the null p0 it is binomially tested
  against — else "beats chance" can be re-read as success at will.
- **B2 — Make the Arm-A frequency/classification control a CONJUNCT of TRACKS-HUMAN-SURFACE, not a
  side-caveat.** As written, TRACKS requires only raw Arm-A ρ CI-LB > 0 (+ the two Arm-B conditions), with
  the binding frequency control listed separately — so a model reproducing only the alternating/
  non-alternating *lexical subcategorization* split (memorizable, not graded information structure) could
  earn the flagship "tracks the human graded verb-bias surface" label with the control never surviving.
  Either add "**AND** the partial-ρ / alternating-only control survives ≥2/3" to the TRACKS conjunction,
  or rename the verb-bias leg to "verb-bias magnitude (may be lexical)" so TRACKS cannot be claimed on the
  confounded raw ρ.
- **B3 — Strengthen the disjointness assertion + add a fidelity audit.** (a) Disjointness at the
  **recipient-lexicalization** level too — explicitly avoid DAIS's five canonical recipient realizations
  (*him / the man / a man / the man from work / a man from work*, paper ex. 3) and its theme nouns,
  reported as a manifest; (b) a **positive fidelity audit** — a frozen human-readable table pinning each of
  the 5 conditions' project realization so "faithful to the factor level" is auditable and the drift-fence
  is real, not asserted.

## SHOULD-FIX (fold into the freeze)

- **S1 — Standing contamination caveat on TRACKS, not only above the ceiling threshold.** DAIS verb bias
  is literally what the source paper showed neural LMs partly capture, and per-verb bias is memorizable
  under Q1-A even with disjoint sentences; a moderate-but-clean-looking ρ is still contamination-vulnerable.
  The CONTAMINATION-CEILING flag (near-perfect ρ only) is one tripwire, not the contamination defense — the
  real defenses are the controls + Q1-A + "pattern not magnitude." Make the caveat standing.
- **S2 — Lead the result headline with Arm B, not Arm A's big-n ρ.** Arm B (definiteness/length + the
  within-length control) is the s245-named surface and the confound-cleaner test; Arm A (verb-bias) is
  well-powered but the most lexical/memorizable and only a defensible *extension* of the s245 scope to the
  paper's headline verb-bias construct. Flagship reading = Arm B; Arm A is the companion, recorded as an
  explicit (honest, non-fence-breaching) extension.
- **S3 — Freeze a deterministic band-assignment decision-tree** (arm-A-clears? → within-length-clears? →
  monotonicity-clears?) so two readers derive the same label from the same numbers; the current whole-panel
  labels can overlap (verb-bias-present + length-counting maps ambiguously to LENGTH-ONLY vs
  VERB-BIAS-ONLY).

## Scope-fence check: PASS

The design produces no magnitude for the givenness shift, states the fence in its load-bearing section and
mandates it in the result's opening blockquote, anchors DAIS only to the surface DAIS measures, and leaves
the givenness claim's `anchors: → languageR-dative-corpus` untouched. **One residual to guard:** the
self-description "the dative line's first human effect-SIZE comparison" must never appear **unscoped** on
the result page or the website rollup, and must not sit adjacent to the givenness magnitudes in a way that
implies those are now human-anchored.

## Anti-cheat check: FAIL as-written, PASS once B1 + B2 are folded

Two pre-commitment holes let a weak/confounded result be re-read as success: (i) "beats chance" has no
pinned null (B1), and (ii) TRACKS can be earned without the binding frequency control surviving (B2). Fix
both in the PREREG and the check passes; the rest of the anti-cheat frame (PREREG sha-pin before any call;
all bands/thresholds/fillers/canonical-condition frozen; both arms frozen before Arm A runs so a UTC split
is not a peek-then-tune; blind scoring; post-run recompute) is sound.

## Non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.002286): RATIFY-WITH-MODIFICATION

- **Q1: MODIFY** — keep the verbatim-disjointness firewall, but require DAIS-faithful factor-instantiation
  checks on recipient class/length/definiteness balance and item-level verb comparability; else full
  project-construction risks measuring your own filler design more than DAIS's surface. *(Converges with
  B3 — the fidelity audit.)*
- **Q2: MODIFY** — Arm A at 200×1 is sound only if the canonical condition is pre-registered as the same
  neutral baseline across all verbs; Arm B at ~40 verbs is thin for a monotonicity-rate claim against
  chance — either raise the alternating-verb count or downgrade Arm B to exploratory. *(Converges with the
  reviewer's Q2 matched-condition-primary point and with B1 — the under-pinned monotonicity null.)*
- **Q3: A.** *(Converges with the reviewer.)*
- **OVERALL: RATIFY-WITH-MODIFICATION.**

## Convergence / divergence weighed

The two independent checks **converge on every load-bearing point**: both adopt the Q1-A/Q2-A/Q3-A
*structure* (neither rejects), both accept Q3-A's anchor scoping, both flag the **Arm-B monotonicity-vs-chance
test as under-pinned** (reviewer B1 pins the predicate + null; vote calls it "thin, raise verbs or downgrade
to exploratory"), both demand a **real Q1 fidelity/faithfulness check** (reviewer B3; vote Q1-MODIFY), and
both want the **canonical Arm-A condition pinned as a matched baseline** (reviewer Q2; vote Q2). They
**diverge** only on the Arm-B remedy: the vote floats "downgrade to exploratory" as an option, while the
reviewer (authority) keeps Arm B — indeed makes it the flagship (S2) — and closes the thinness by **pinning
the binomial null** (B1). The resolution takes the reviewer's authority: **keep Arm B, pin its predicate +
null p0**; the vote's thinness concern is honored by the pinned null + adequate N, not by demotion. No
option is attractive for making a finding look stronger — the modifications uniformly *tighten* the
yardstick against over-reading a confounded/weak ρ.

## Resolution applied (s247)

**ADOPT-WITH-MODIFICATION — ratify Q1-A / Q2-A / Q3-A as the yardstick, subject to three binding freeze
BLOCKERS (B1–B3) + three SHOULD-FIX (S1–S3), all to be folded into the s248 freeze PREREG.** The freeze +
run follow (s248+); the run is **not** in this ratifying session. Fixes the yardstick, never a result.
