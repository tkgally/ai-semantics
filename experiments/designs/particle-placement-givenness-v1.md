---
type: design
id: particle-placement-givenness-v1
title: "Verb-particle placement object-givenness probe (A5, third sibling) — does the panel's joined/split preference shift in the human definite→split direction, and does it survive a byte-identical discourse-givenness firewall? FROZEN s225 (ratified + certified)"
meaning-senses:
  - constructional
  - inferential
  - distributional
status: frozen
anchor: human-anchored
contingent-on: []
created: 2026-07-14
updated: 2026-07-14
links:
  - rel: operationalizes
    target: conjecture/particle-placement-givenness
  - rel: depends-on
    target: resource/particle-placement-givenness-human-anchor
  - rel: depends-on
    target: source/kim-2016-particle-placement
  - rel: depends-on
    target: result/dative-information-structure-powered
  - rel: anchors
    target: resource/particle-placement-givenness-human-anchor
---

# Design v1 (FROZEN s225) — verb-particle placement object-givenness probe (program A5, third sibling)

**Status:** FROZEN (s225) — **ratified** [`decisions/resolved/particle-placement-anchor-and-indicator`](../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
(ADOPT-WITH-MODIFICATION Q1-A / Q2-(i) / Q3 human-anchored on the direction; binding conditions R1–R7),
Arm-2 parallelism independently certified **CERTIFY-A** (R2/R3), and frozen at
[`PREREG.md`](../runs/2026-07-14-particle-placement-givenness/PREREG.md) (sha-pinning `stimuli.json` +
`freq_control.json`) before any finding-bearing call. No probe ran in the opening session (s224); freeze +
run are s225 (the genitive s217→s218 pattern). Mirrors the dative
([`result/dative-information-structure-powered`](../../wiki/findings/results/dative-information-structure-powered.md))
and genitive ([`design/genitive-alternation-animacy-v1`](genitive-alternation-animacy-v1.md)) patterns; the
freeze + run follow ratification (the genitive s217→s218 pattern).

## The question (one sentence)

The dative line showed the panel tracks a discourse-structural soft constraint (givenness) in the human
production direction on the *ditransitive* frame; this design tests whether the **same information-
structural constraint** — object givenness — governs a **different production alternation**, English
**verb-particle placement** (joined *picked up the book* vs split *picked the book up*; definite/given
object → split, per Kim et al. 2016 / Gries 1999), **in the human direction**, and crucially whether that
shift **survives a byte-identical discourse-givenness firewall** or is merely the model reading off which
order-string it has seen more often.

## The instrument (port of the validated dative/genitive graded-forced-choice, Q2-(i))

Given a verb-particle proposition with the **verb + particle + object head-noun held fixed**, the model
distributes **100 points** by naturalness between the two orders of the *same* proposition:

- **joined (V-Prt-DO):** *picked up the box*
- **split (V-DO-Prt):** *picked the box up*

split-pref = split_points / (split_points + joined_points) ∈ [0,1]. The split↔A/B mapping is
**counterbalanced** (every item run with split = option A and split = option B) and the parser is
**target-blind** (keys on reply position, not on which option is the split order). Same panel
([`config/models.md`](../../config/models.md)), temperature 0, graded `FINAL:` line, cluster-bootstrap-
over-frames intervals — all inherited byte-parallel in shape from the frozen dative/genitive instruments.

## The two arms (where the givenness manipulation lives)

The focal constraint is **object information-status (givenness)**, operationalized two ways — the
anchor-exact definiteness contrast (confoundable) and the byte-identical discourse-givenness firewall
(shortcut-immune). This is the design's structural advantage over the genitive: the firewall's scored
strings are **fully byte-identical**, tighter than the genitive's nonce arm (which still varied the
possessor string).

**Arm 1 — definiteness (anchor-exact human-direction contrast; confoundable, NOT the decisive leg).** One
*frame* = a fixed verb+particle+head-noun; the object determiner is varied indefinite (*a box*) vs definite
(*the box*), everything else byte-identical. The scored orders (joined/split) differ only in particle
position within a condition; between conditions only the determiner (a/the) differs.

> shift₁(frame) = mean(split-pref | definite object) − mean(split-pref | indefinite object)

Human direction ⇒ shift₁ > 0 (definite object pulls preference toward split). **Confound:** because the
determiner differs across conditions, a positive shift₁ could be a shadow of the higher surface frequency
of definite-object split-order strings; and "a box" vs "the box" also differ in **genericity, specificity,
and scope**, not only surface frequency (s224 critic SHOULD-FIX 3) — the frozen covariate nets only
frequency, so shift₁ carries residual confounds no covariate targets. So shift₁ alone does **not** license
a constructional reading. **Role (s224 pre-run critic B2 + SHOULD-FIX 1 — de-muddled):** Arm 1 matches the
human anchor *exactly* (Kim et al.'s DET direction is about the determiner), so it establishes that the
panel shows the anchored direction *at all*; it is **not** the decisive/CONFIRM-bearing leg — that is Arm
2. To avoid a *false-negative machine* (a noisy a/the effect vetoing a clean firewall positive), Arm 1 is
**not** a hard CI-LB gate: CONFIRM requires only that Arm 1 be **directionally consistent** (point estimate
same sign as the human direction), while Arm 2 carries the decisive CI-LB > 0 requirement (see the CONFIRM
rule below). A clean firewall positive with an under-powered Arm 1 is recorded as "CONFIRM, firewall-borne",
not collapsed to WEAK.

**Arm 2 — discourse-givenness firewall (byte-identical scored strings, LOAD-BEARING shortcut control),
with a THREE-condition design that also dissociates referential givenness from lexical priming (s224
pre-run critic B-crit-1).** The object string is held **byte-identical** (*the box*) across all
conditions; information status is manipulated only in a **preceding discourse context**. The two scored
order-strings (*picked up the box* / *picked the box up*) are **byte-identical across every condition**,
so no scored-string statistic can move the shift. The three context conditions:

- **GIVEN:** the object referent is previously mentioned and topical/accessible (discourse-old).
- **NEW-MENTIONED:** the object **noun appears** in the context at matched frequency/recency, but as a
  **non-coreferential / referentially-new** entity (lexically primed, information-structurally new).
- **NEW:** the object is unmentioned, first introduced by the scored sentence.

The **decisive information-structural contrast** is GIVEN vs **NEW-MENTIONED**:

> shift₂(frame) = mean(split-pref | GIVEN) − mean(split-pref | NEW-MENTIONED)

Human direction ⇒ shift₂ > 0. A secondary descriptive contrast GIVEN − NEW is also reported.

**Why the three-condition firewall is needed (B-crit-1).** Byte-identity of the *scored* strings kills
every scored-string shortcut (always-split / always-joined / string-frequency / determiner-collocation →
shift = 0 by construction). But it moves one channel **into the context**: because discourse-givenness is
*created by mentioning the referent*, a two-condition GIVEN-vs-NEW firewall confounds referential givenness
with **mere lexical priming / recency of the object noun** — a model with only a shallow "the noun was just
in context → split feels natural" heuristic, and **no** information-structural representation, scores a
positive GIVEN−NEW shift. The **NEW-MENTIONED** condition holds lexical priming/recency of the object noun
*constant* with GIVEN and varies only its referential/topical status, so a positive **GIVEN − NEW-MENTIONED**
shift cannot be the lexical-recency heuristic — it is referential information structure. The two-condition
GIVEN−NEW contrast is kept only as a descriptive comparison, **not** the CONFIRM leg.

**Fallback (B-crit-1 option B, if NEW-MENTIONED authoring proves infeasible at freeze):** run the
two-condition firewall but **rescope the CONFIRM claim** from "information-structure / givenness tracking"
to "the panel **integrates discourse context** in the human direction", explicitly logging the
lexical-recency heuristic as an alternative this arm does not exclude. Option A (the third condition) is
the honest close and the default; the fallback keeps the claim calibrated if A cannot be built cleanly.

**Context-authoring matching constraint (freeze condition (viii), BLOCKER B1).** GIVEN, NEW-MENTIONED, and
NEW contexts are matched on discourse genre, **clause count, sentence type(s), verb lemmas,
punctuation/formatting, and overall length**, differing **only** in the intended prior-mention /
referential-status manipulation; the object mention (in GIVEN and NEW-MENTIONED) must **not** front, cleft,
topicalize, passivize, or heavy-NP-shift the object (no syntactic-scaffolding leak). This parallelism gates
the whole CONFIRM and is **independently certified** before freeze by a non-authoring agent / the
non-Anthropic panel vote (s224 SHOULD-FIX 2), not only the lead-agent self-audit. If it cannot be
guaranteed, Arm 2 is contaminated and the run **defers** (a NO-GO on the firewall never relaxes the
control). **Felicity note (SHOULD-FIX 4):** a definite *the box* in the NEW context can be mildly
infelicitous (accommodation), so shift could ride felicity not givenness — licensed via bridging where
needed, and monitored; the GIVEN vs NEW-MENTIONED decisive contrast (both mention the noun) largely
sidesteps this.

**Arm 3 — length (convergent-validity leg, SECONDARY).** A short object (*the box*) vs a long object (*the
box we found in the attic*), verb+particle+head-noun fixed. shift₃ = split-pref(short) − split-pref(long),
human direction ⇒ shift₃ > 0. Corroboration that the panel tracks the construction's soft constraints
(the second named human direction), not one arm's confound; not the focal contrast.

## The load-bearing shadow control (Q2 crux)

Unlike the genitive — where the shadow control was a rare/nonce-possessor arm plus a weak corpus covariate
— particle-placement givenness affords a **strictly byte-identical firewall** (Arm 2), which is the
cleanest possible shortcut control: no scored-string statistic can produce a non-zero shift₂. The CONFIRM
therefore rests on **Arm 2**, not on a corpus covariate. A frozen surface covariate is reported as weak
corroboration only:

- **Frozen surface-collocation covariate (corroboration, one exact sha'd recipe).** From a license-
  verified corpus (**UD English-EWT**, CC BY-SA 4.0, in-scope — the genitive covariate corpus; LICENSE
  verified firsthand), a per-item **split-order marginal rate** for the verb+particle (how often that
  particle-verb appears split vs joined), frozen before any call; `analyze.py` reports the definiteness
  shift's residual over it. As with the genitive, particle-placement instances are sparse in a small
  corpus, so this covariate is expected **near-vacuous** and is stated as such — it is corroboration, and
  CONFIRM rests on Arm 2 (which needs no corpus). Power bounded by corpus size, stated honestly.

**Pre-registered CONFIRM-vs-SHADOW rule (fix the adjudication ex ante; s224 critic SHOULD-FIX 1 — the
asymmetric gate).** The **firewall shift₂ (GIVEN − NEW-MENTIONED)** is the decisive, necessary, primary
leg: **shift₂ bootstrap CI lower bound > 0 (≥2/3 models)** is required for any CONFIRM. The definiteness
arm is a consistency check, **not** a hard veto: Arm 1 need only be **directionally consistent** (shift₁
point estimate same sign, human direction). Register before freeze:

- **Full CONFIRM:** shift₂ CI-LB > 0 (≥2/3) **AND** shift₁ CI-LB > 0 (≥2/3).
- **CONFIRM, firewall-borne:** shift₂ CI-LB > 0 (≥2/3) **AND** shift₁ directionally consistent but its CI
  does not clear zero (Arm 1 under-powered) — a genuine positive carried by the clean firewall, recorded
  as such, **not** collapsed to WEAK.
- **SHADOW:** the definiteness shift₁ is present but the **firewall shift₂ (GIVEN − NEW-MENTIONED) does not
  clear zero** (≥2/3) → the definiteness effect is a surface-string/lexical shadow, not information
  structure.

**Gate–hedge dependency (state in PREREG).** If B-crit-1 **Option A** (the NEW-MENTIONED condition) is
built, shift₂ is trustworthy alone → the above asymmetric rule holds. If only the **Option B** fallback
(two-condition GIVEN−NEW firewall) is built, the AND-gate on shift₁ is **retained** as the hedge against
the lexical-recency residual, and the CONFIRM claim is rescoped to "integrates discourse context in the
human direction."

## Primary quantities + 95% CIs (cluster bootstrap over frames)

**(1)** definiteness shift₁ (split-pref definite − indefinite), pp; **(2)** fraction of frames with shift₁
> 0; **(3)** **discourse-givenness firewall shift₂ = GIVEN − NEW-MENTIONED** (byte-identical scored strings,
priming-controlled; the decisive shortcut-immune leg) + the descriptive GIVEN − NEW contrast; **(4)** length
shift₃ (convergent leg); **(5)** shift₁ residual over the frozen surface-collocation covariate
(corroboration); plus per-model split-pref by condition. Deliverable = point estimate + CI, not a threshold
pass.

## Verdict frame (pre-registered, symmetric — a null is first-class)

- **CONFIRM (human-direction):** the firewall shift₂ (GIVEN − NEW-MENTIONED) CI-LB > 0 (≥2/3) **AND** shift₁
  directionally consistent (full CONFIRM if shift₁ CI-LB > 0 too; "CONFIRM, firewall-borne" if shift₁ is
  directionally consistent but under-powered) → a human-anchored production-side information-structure
  positive on a third construction; a particle-placement row for the shadow-depth table; cross-construction
  generalization of the dative's givenness effect. *(Under the Option-B fallback: rescoped to "the panel
  integrates discourse context in the human direction.")*
- **SHADOW / ATTENUATED:** shift₁ > 0 but the **firewall shift₂ (GIVEN − NEW-MENTIONED) does not clear
  zero** (≥2/3) → a distributional/lexical shadow (surface-string frequency or object-noun lexical-recency
  priming), not information-structure tracking; a first-class negative for the shadow-depth reading.
- **WEAK:** the firewall shift₂ clears zero but the convergent length leg (shift₃) fails, or the effect does
  not generalize beyond one arm.
- **FALSIFY / REVERSAL:** no givenness shift under the controlled manipulation, or a reversal → the
  cross-construction generality of the information-structural effect is contested; investigate item
  authoring in a **pre-registered v2**, do **not** re-run v1 or retune (s224 SHOULD-FIX 5).

## What this run may / may NOT claim

- **May:** a **within-model, human-direction** claim that the panel's particle-placement preference does /
  does not shift toward the split order for given/definite objects, with magnitudes + intervals, and
  whether that survives the byte-identical discourse-givenness firewall.
- **May NOT:** any claim of **human-level** particle-placement competence; any claim of beating the
  distributional shadow if the firewall arm does not clear it; any per-item human-gradient claim (no
  openly-licensed per-item particle-placement gradient in-repo — verified null; deferred to a scout);
  any cross-linguistic claim.

## N and power (PROTOCOL §4) — stated in bootstrap (frame) units

The bootstrap resampling unit is the **frame** (a fixed verb+particle+head-noun), not the trial. Target
**≥40 frames** with the **byte-identical firewall arm (Arm 2) at least as powered as the definiteness arm
(Arm 1)** — Arm 2 is the load-bearing shortcut control and carries the CONFIRM, so it must not be
under-powered (the genitive lesson: the shortcut-immune arm is where the marginal model leg failed to
replicate at first). Arm 2 now runs **three** context conditions (GIVEN / NEW-MENTIONED / NEW) per frame ×
A/B counterbalance; the decisive contrast (GIVEN − NEW-MENTIONED) must be powered to the frame floor. **N
is reported and powered in frames**, not trials (A/B and conditions are not independent items). Exact frame
count fixed at freeze; stated with rationale in PREREG.

## Freeze conditions (to honor at the run session, after ratification)

- **(i)** items + the single frozen covariate recipe authored + **frozen (sha256) before running** in a
  named sha'd build script (no "and/or" covariate); `probe.py full` refuses unless the exact shas are in
  PREREG (the dative/genitive discipline).
- **(ii)** object **length, type (full lexical NP — no pronouns), concreteness, animacy, VP idiomaticity**
  matched/held constant across the givenness conditions in Arms 1–2; the object string **byte-identical**
  across Arm 2's given/new conditions (verified at build); shortcut-reader certification (always-split /
  always-joined / position / string-frequency → shift 0) — **exact by construction for Arm 2** (identical
  strings), and stated to NOT cover Arm 1's determiner-frequency reader (which the firewall + covariate
  kill, not construction).
- **(iii)** the **byte-identical discourse-givenness firewall (Arm 2), three-condition (GIVEN /
  NEW-MENTIONED / NEW)** is the load-bearing shortcut control, with the decisive contrast GIVEN −
  NEW-MENTIONED (priming-controlled); the frozen surface-collocation covariate is corroboration with power
  limits stated honestly; the **pre-registered asymmetric CONFIRM-vs-SHADOW rule** (firewall shift₂ CI-LB>0
  necessary + primary; shift₁ directional-consistency only; full-vs-firewall-borne CONFIRM; gate–hedge
  dependency on whether Option A or B is built) is registered ex ante.
- **(iv)** powered N in **frames** (§4), firewall arm ≥ definiteness arm; pre-flight estimate + post-run
  actual in [`config/budget.md`](../../config/budget.md).
- **(v)** what each outcome may / may not claim — stated above; falsify/shadow arms live, no retuning; a
  pre-run-critic NO-GO on the firewall **defers** the run, never relaxes the control.
- **(vi)** result posture `human-anchored` on the **direction only**, anchored to
  [`resource/particle-placement-givenness-human-anchor`](../../wiki/base/resources/particle-placement-givenness-human-anchor.md);
  the "May NOT: any per-item human-gradient claim" fence stays hard; CONFIRM prose must not imply
  gradient-matching or human-level competence; the anchor is a **direction restatement** (Kim et al. via
  Gries 1999), so no "as strong as the Dubois rating anchor" rhetoric.
- **(vii)** the **convergent length leg (Arm 3)** committed so the WEAK verdict is cleanly adjudicable.
- **(viii) [BLOCKER — s224 pre-run critic B1].** Arm 2 context authoring must close the context→string
  channel: GIVEN and NEW contexts matched on **genre, clause count, sentence type(s), verb lemmas,
  punctuation/formatting, and overall length**, differing **only** in a single controlled prior-mention /
  topical-accessibility manipulation, with **no** fronting / clefting / topicalization / heavy-NP / passive
  cue in the given context's mention. This is the load-bearing shortcut control (is Arm 2 manipulating
  referential givenness, or merely lexical mention / priming / a syntactic-scaffolding leak?). Verified at
  build; if the parallelism cannot be guaranteed, the run **defers** — a NO-GO here never relaxes the
  control. (Full spec in the *Arm 2* section above.)
- **(ix)** lead-agent self-audit of every synthetic item against the construction and the givenness scheme;
  **plus an independent (non-authoring agent / non-Anthropic vote) certification of the Arm-2 GIVEN /
  NEW-MENTIONED / NEW parallelism** before freeze (s224 SHOULD-FIX 2 — the load-bearing gate must not rest
  on author self-audit alone); no attested example sentences lifted (contamination guard).
- **(x)** the **NEW-MENTIONED** third Arm-2 condition (B-crit-1 Option A) is built if the priming-controlled
  parallelism can be guaranteed; else the Option-B fallback (two-condition firewall + rescoped "integrates
  discourse context" claim) is used and stated. Definite-in-NEW felicity licensed via bridging / monitored
  (SHOULD-FIX 4). A FALSIFY/reversal triggers a **pre-registered v2**, never a v1 re-run (SHOULD-FIX 5).

## Budget (pre-flight, for the run session)

Arm 1 (2 conditions) + Arm 2 (3 conditions) + Arm 3 (2 conditions) × ~40 frames × A/B × 3 models ≈
**~900–1,700 calls**. No metalanguage-competence smoke test needed (the task is in English). At observed
dative/genitive prices (~$0.30 for ~800 forced-choice calls) ≈ **$0.35–0.65** billed — well under the
$2.50 single-run flag and the $5/day cap. Actuals from the returned `usage.cost`.

## Pre-run critic (this design session, s224)

An independent fresh-agent pre-run critic (verdict authority for the eventual run) + one non-Anthropic
decorrelation vote (`gpt-5.4-mini`, $0.003934) reviewed this design and the open decision's provisional
defaults. QA input to the s225+ ratification, not a substitute for it. Full record on the open decision
[`decisions/resolved/particle-placement-anchor-and-indicator`](../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
and in [`REVIEW-critic-s224.md`](../runs/2026-07-14-particle-placement-givenness-design/REVIEW-critic-s224.md).

- **Fresh-agent critic → GO-WITH-CONDITIONS.** Anchor mapping verified correct (construction0 = joined,
  construction1 = split; definite→split and short→split cited accurately, not overclaimed); verdict frame
  symmetric; Arm 2 immune to *scored-string* shortcuts. **BLOCKER B-crit-1 (applied above):** byte-identity
  of the scored strings moves one channel *into the context* — because givenness is created by mentioning
  the object, a two-condition GIVEN−NEW firewall confounds referential givenness with **lexical priming /
  recency of the object noun**; a shallow "noun was just in context → split" heuristic scores a spurious
  positive. **Fixed** by the **NEW-MENTIONED** third condition (object mentioned at matched recency but
  referentially new), making GIVEN − NEW-MENTIONED the decisive contrast (Option A), with an Option-B
  rescope fallback. **SHOULD-FIX 1 (applied):** the symmetric AND-gate was a false-negative machine (the
  noisy a/the arm could veto a clean firewall positive) — replaced by the asymmetric rule (firewall shift₂
  necessary+primary; Arm 1 directional-consistency only; full-vs-firewall-borne CONFIRM; gate–hedge
  dependency). **SHOULD-FIX 2–5 (applied):** independent parallelism certification; broadened Arm-1 confound
  disclosure (genericity/specificity/scope); definite-in-NEW felicity via bridging/monitoring; FALSIFY →
  pre-registered v2. **Recommendations:** Q1 **adopt givenness** (only givenness affords the byte-identical
  firewall — switching to length for novelty would forfeit the shortcut-immune leg; flagged as a rigor-loss
  temptation); Q3 **keep human-anchored on the direction/sign only** (internal-contrast-only would
  *under*-claim a genuine license-verified anchor).
- **Non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.003934) → NO-GO**, convergent on the core: it
  independently flagged the Arm-2 context→string leakage (lexical priming / syntactic scaffolding), the
  muddled Arm-1-primary-vs-CONFIRM-on-Arm-2 framing, a preference for length as a cleaner first cut, and a
  push toward internal-contrast-only. The leakage + framing points are **addressed** by B-crit-1 + the
  asymmetric rule; the length and internal-contrast-only preferences were **weighed and not adopted**, on
  the fresh-agent critic's reasoned grounds (the firewall exists only for givenness; the anchor is genuine).
  A NO-GO decorrelation vote weighed-and-addressed is the intended decorrelation function, not a veto.
- **Net:** GO-WITH-CONDITIONS. The design is **hardened this session** (B-crit-1 + SHOULD-FIX 1–5 folded
  into the arms, CONFIRM rule, and freeze conditions), mirroring the A1a/genitive pattern of applying
  blockers to the design and carrying them to the freezing session. Ratifiable + freezable **s225+** once
  the Arm-2 NEW-MENTIONED parallelism is built and independently certified; a pre-run-critic NO-GO on the
  firewall at freeze **defers** the run, never relaxes the control. No probe ran this session.
