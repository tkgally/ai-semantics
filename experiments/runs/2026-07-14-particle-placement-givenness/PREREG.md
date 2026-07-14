# PREREG — verb-particle placement object-givenness probe (program A5, third sibling, session 225)

**Frozen 2026-07-14 (session 225), after ratification + independent certification, before any finding-
bearing model call.** Ratified design:
[`decisions/resolved/particle-placement-anchor-and-indicator`](../../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
(ADOPT-WITH-MODIFICATION Q1-A object givenness / Q2-(i) graded forced-choice + the byte-identical
three-condition discourse-givenness firewall / Q3 human-anchored on the direction; + binding freeze
conditions R1–R7 and the s224 freeze conditions (i)–(x)). Conjecture:
[`conjecture/particle-placement-givenness`](../../../wiki/findings/conjectures/particle-placement-givenness.md).
Human anchor: [`resource/particle-placement-givenness-human-anchor`](../../../wiki/base/resources/particle-placement-givenness-human-anchor.md)
(Kim et al. 2016, CC BY 4.0, a **direction restatement** via Gries 1999) — **direction/sign only**
(definite/given object → split).

## Frozen artifacts (sha256 — `probe.py full` refuses unless both appear here)

- `stimuli.json`      : `0b63e2529ed03c3eb5ccb8d9d96db97198a3f4043a3b6ded67cc12d101d166c9`
- `freq_control.json` : `cd472475cfae6f03862cd12ffc9421cd085d8abca831e2cccf1edd7a42da20d7`

Built by `build_items.py` (certification PASS) and `build_cooc_particle.py`. The covariate corpus is
**UD English-EWT** (CC BY-SA 4.0, LICENSE verified firsthand s218; in scope under the s168 UD-treebank
rule); per-file sha256 recorded in `freq_control.json.corpus_meta` (train `d68e061…`, dev `39239e0…`,
test `fa024f4…`).

## Design (one paragraph)

Graded forced-choice (port of the byte-frozen dative/genitive instrument): hold verb + particle + object
head-noun fixed, distribute 100 points by naturalness between the **JOINED** order (*Nadia picked up the
box*) and the **SPLIT** order (*Nadia picked the box up*); split-pref = split_pts/(split_pts+joined_pts).
The resampling unit is the **frame** (a fixed verb+particle+object-head-noun). **40 frames**, three arms:
Arm 1 definiteness (2 conditions), Arm 2 discourse-givenness firewall (3 conditions), Arm 3 length (2
conditions); each × A/B counterbalance. **560 trials × 3 models = 1,680 calls.**

## The three arms + the shadow control (the crux — Q2, R1–R4)

- **Arm 1 — definiteness (anchor-exact, CONFOUNDABLE, NOT decisive).** *a box* vs *the box*, everything
  else byte-identical; shift1 = split-pref(definite) − split-pref(indefinite); human direction shift1 > 0.
  Confound: the determiner differs, so shift1 could be a surface-frequency shadow (and *a*/*the* also
  differ in genericity/specificity/scope — s224 SHOULD-FIX 3). **Role (R4):** a consistency check only —
  directional consistency required (a reversal blocks CONFIRM), NOT a hard CI-LB gate.
- **Arm 2 — discourse-givenness FIREWALL (byte-identical scored strings; LOAD-BEARING; carries the
  CONFIRM).** The object string is held **byte-identical** (*the {noun}*) across three context conditions;
  information status is manipulated only in a single preceding discourse sentence: **GIVEN** (referent
  evoked + topical), **NEW-MENTIONED** (object noun mentioned in a gnomic/generic clause that introduces
  no token — noun primed, referent new), **NEW** (noun absent). Because the two scored order-strings are
  **byte-identical across all three conditions**, any scored-string reader (always-split / always-joined /
  string-frequency / determiner-collocation / position) yields shift = 0 **by construction** (certified).
  **DECISIVE contrast = GIVEN − NEW-MENTIONED** (Option A, ratified default), which holds the object noun's
  lexical priming/recency constant and isolates **referential** information structure (s224 B-crit-1). The
  descriptive **GIVEN − NEW** contrast is also reported.
- **Arm 3 — length (convergent-validity leg, SECONDARY, NON-GATING — R5).** *the box* vs *the box {heavy
  postmodifier}*; shift3 = split-pref(short) − split-pref(long); human direction shift3 > 0 (short → split,
  long → joined, end-weight). Feeds the WEAK adjudication only; never enters the CONFIRM gate, not blended
  into the givenness legs.
- **Frozen surface-collocation covariate (corroboration, near-vacuous — R1/R7).** Per-(verb+particle)
  marginal SPLIT-order rate from UD-EWT (`freq_control.json`); `analyze.py` reports the definiteness
  shift's residual over it (OLS intercept b0) **and the covariate's own predictive validity (b1, R²)**.
  UD-EWT is small and transitive particle-verb tokens sparse: **16/38 stimulus verb+particle pairs have
  any corpus token**, corpus base split rate 0.42 — so this covariate is **weak corroboration**, and
  CONFIRM rests on Arm 2 (which needs no corpus). Stated plainly.

## Independent certification (freeze (ix), R2/R3) — the load-bearing gate

The Arm-2 context parallelism was **independently certified by a non-authoring fresh agent** →
**CERTIFY-A** (`REVIEW-ratify-s225.md` records the ratification; the parallelism certification verdict is
summarized here and in the run README). It certified: **R2(a)** GIVEN and NEW-MENTIONED match the object
noun's mention count (1/1) and recency (second token, one sentence prior) — the coreferential pronoun
*it* in GIVEN adds referent activation, not noun lexical priming; **R2(b)** GIVEN's episodic existential
makes the referent discourse-given/topical while NEW-MENTIONED's gnomic modal introduces no discourse
referent (noun primed, referent new) — the decisive contrast isolates referential givenness; **R2(c)** no
structural-priming leak (the noun appears only as subject of an intransitive/copular clause; no fronting/
clefting/topicalization/passive/heavy-NP; no particle near the object; certified mechanically too);
**R3** the definite scored object is comparably felicitous in GIVEN (anaphoric) and NEW-MENTIONED
(mild accommodated first-mention) — accommodation cost is the processing *signature* of non-givenness,
not a rival construct, and is mild/natural. Advisory (non-blocking) authoring notes on the surface
naturalness of a few nouns (`valve`, `drawer`, `branch`, `thread`) in the generic frame were recorded;
because the scored strings are byte-identical across conditions these **cannot** bias the decisive
contrast, so the certified set is frozen as-is and the notes are disclosed as a v2 consideration.

## Pre-registered ASYMMETRIC verdict (R4 — symmetric outcome frame; a null is first-class)

Per model: **cond_fw** (firewall shift2 GIVEN−NEW-MENTIONED > 0 AND bootstrap 95% LB > 0 — necessary +
primary); **arm1_consistent** (shift1 point estimate > 0, human direction); **arm1_reversal** (shift1 < 0
— blocks CONFIRM); **cond_fw_strong** (shift1 > 0 AND its 95% LB > 0 — full vs firewall-borne);
**cond_len** (shift3 > 0 AND 95% LB > 0). Panel (≥2/3 models):

- **CONFIRM (human-direction):** cond_fw (≥2/3) **AND** arm1_consistent (≥2/3) **AND** not arm1_reversal
  (≥2/3). **Full CONFIRM** if cond_fw_strong (≥2/3) too; else **CONFIRM, firewall-borne** (a genuine
  positive carried by the clean byte-identical firewall with an under-powered Arm 1) → a human-anchored
  production-side information-structure positive on a third construction; a particle-placement row for the
  shadow-depth table; cross-construction generalization of the dative's givenness effect. **Interpretation
  fence (R1):** framed narrowly directional — byte-identity + NEW-MENTIONED exclude scored-string
  shortcuts and object-noun lexical recency, but do **not** exclude the panel reproducing the human
  context→order joint distribution from pretraining; the claim asserts distributional tracking **in the
  human direction**, not information-structural competence beyond that. No "distributional shadow
  defeated." A "CONFIRM, firewall-borne" is scoped to "integrates referential discourse-givenness in the
  human direction" and must not be written as confirming the Kim et al. *determiner* effect specifically.
- **SHADOW / ATTENUATED:** shift1 > 0 (≥2/3) but cond_fw FAILS (<2/3) → the definiteness effect is a
  surface-string/lexical shadow, not information structure (a first-class negative for the shadow-depth
  reading).
- **WEAK:** cond_fw (≥2/3) but cond_len FAILS (<2/3) → firewall positive without the convergent length leg.
- **FALSIFY / REVERSAL:** cond_fw fails AND shift1 not > 0 at ≥2/3 (or Arm 1 reverses at ≥2/3) → the
  cross-construction generality is contested; investigate item authoring in a **pre-registered v2**, do
  **not** re-run v1 or retune (s224 SHOULD-FIX 5).

## Primary quantities + 95% CIs (nonparametric bootstrap over frames)

(1) definiteness shift1 + fraction of frames > 0 + sign test (consistency check); (2) **firewall shift2 =
GIVEN − NEW-MENTIONED** (the decisive shortcut-immune leg) + descriptive GIVEN − NEW; (3) length shift3
(convergent leg); (4) covariate-adjusted intercept b0 + covariate b1/R² (its predictive validity); (5)
per-condition mean split-pref (calibration). Point estimate + interval, not a threshold pass.

## What this run may / may NOT claim (R1, R6)

- **May:** a within-model, human-direction claim that the panel's particle-placement preference does / does
  not shift toward the split order for given/definite objects, with magnitudes + intervals, and whether
  that survives the byte-identical discourse-givenness firewall.
- **May NOT:** any claim of **human-level** particle-placement competence; "distributional shadow
  defeated" (R1 — the byte-identical firewall + NEW-MENTIONED exclude scored-string shortcuts + lexical
  recency, not pretraining joint-distribution mimicry); any per-item human-gradient claim (no openly-
  licensed per-item particle-placement gradient in-repo — verified null; deferred to a scout); any
  cross-linguistic claim; no "as strong as the Dubois rating anchor" rhetoric (the Kim et al. anchor is a
  direction restatement, grounding the sign only — R6).

## N and power (PROTOCOL §4)

Bootstrap unit = the **frame**; 40 frames. Arm 2 (firewall) has 6 trials/frame (3 conditions × A/B) ≥ Arm
1 (definiteness) 4 trials/frame — the load-bearing arm is at least as powered as the confoundable arm
(freeze (iv), R7). N reported in frames, not trials.

## Budget (pre-flight)

1,680 calls, short forced-choice. At observed dative/genitive forced-choice prices (~$0.30 for ~800
calls) ≈ **$0.35–0.65** billed; pre-registered hard stop **$1.30** (`common.HARD_STOP_USD`), below the
$2.50 single-run flag and the $5/day UTC cap. UTC-2026-07-14 spend before this run: s224 $0.003934 +
s225 ratify vote $0.003591 = **$0.007525** (~$4.99 headroom). Actuals from the returned `usage.cost`.

## Anti-cheat

Item set + covariate frozen (shas above) before any finding-bearing call; no retuning after seeing
outputs. A null / SHADOW / FALSIFY is a first-class result. The predictions.md bet is registered at this
freeze, before the run (never pre-filled with an outcome). A FALSIFY/reversal triggers a pre-registered
v2, never a v1 re-run. The probe did not run in the opening session (s224) or the ratifying step (s225
ratification); the freeze + run are this session (s225), the genitive s217→s218 pattern.
