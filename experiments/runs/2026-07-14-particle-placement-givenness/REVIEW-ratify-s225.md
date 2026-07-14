# Ratification review record — A5 third sibling (verb-particle placement givenness), s225

**Decision ratified:** [`decisions/resolved/particle-placement-anchor-and-indicator`](../../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
(opened s224, ratified s225 — cross-session, PROJECT.md §12.3). **VERDICT: ADOPT-WITH-MODIFICATION**
(Q1-A object givenness / Q2-(i) graded forced-choice + the byte-identical three-condition discourse-
givenness firewall / Q3 human-anchored on the direction), subject to binding freeze conditions R1–R7.

Two independent reviewers: a fresh-agent adversarial ratification reviewer (verdict authority,
independent of the s225 freeze/run) and one non-Anthropic decorrelation vote (`gpt-5.4-mini`,
$0.003591, `VOTE-ratify-s225.json`). The vote is INPUT the fresh reviewer weighed, not the ratification.

## Non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.003591) → **REJECT**

- **Q1 (ADOPT-WITH-MODIFICATION):** givenness defensible, but the "short object" length leg is a
  different phenomenon (construct purity); keep givenness primary, demote shortness to an ancillary
  sanity-check, not a co-equal leg.
- **Q2 (REJECT):** the byte-identical firewall blocks *string-frequency* leakage but not "discourse-
  heuristic leakage from the context itself: salience, topical persistence, pronoun-availability, local
  coherence, recently-mentioned-entity effects." NEW-MENTIONED helps but is "not a full control unless
  you also show the model is not just reacting to mentionedness + recency + discourse prominence." Also:
  the asymmetric CONFIRM rule "reads like it is set up to ratify a positive while demoting the covariate
  to near-vacuous corroboration." Residual channel: a model with no information-structural competence
  could exploit discourse salience from NEW-MENTIONED vs NEW, or learn "given-context → split" from
  pretraining-style discourse statistics.
- **Q3 (ADOPT-WITH-MODIFICATION):** "human-anchored on the direction" honest only with a strong caveat
  that the anchor is literature-backed directionality, not a license-verified fresh annotation source;
  tighten wording to "internal-contrast probe with external corroboration of direction."

## Fresh-agent ratification reviewer (verdict authority) → **ADOPT-WITH-MODIFICATION**

The reviewer weighed the vote in full and decomposed the crux (Q2), sorting every point into
*design-change-required* / *fence-condition* / *already-handled*:

- **Q1 → adopt default (already handled).** Length is *already* Arm 3, "convergent-validity leg,
  SECONDARY," outside the CONFIRM gate. The requested demotion is the design's existing posture.
  Decisive add: **only givenness affords the byte-identical firewall** — switching the focal constraint
  to length would forfeit the shortcut-immune leg, the design's sole rigor advantage over the genitive.
  Choosing givenness makes a positive *harder* to earn (anti-cheat-clean).
- **Q2 → adopt default; no design change; fences R1–R4.** The vote's "discourse salience/topical
  persistence/referential prominence" is **the target construct** (givenness = referential discourse-
  accessibility; Chafe/Prince/Gundel) — a **category error** to call it a shortcut. **Lexical recency /
  mentionedness** is a genuine shortcut, closed by construction by **NEW-MENTIONED** (GIVEN and
  NEW-MENTIONED match mention count/recency; decisive GIVEN−NEW-MENTIONED cannot be recency). The
  **deep joint-distribution mimicry** (reproducing the human context→order mapping from pretraining) is
  the standing distributional-shadow limit of the whole program, handled by **fencing the claim**
  (R1, the genitive-R5 analog), not by a design change. The **asymmetric CONFIRM rule** rests the
  necessary CI-LB gate on the byte-identical shortcut-immune arm and demotes the confoundable determiner
  arm to a consistency check — the *correct* direction for rigor (a symmetric AND-gate would let the
  noisy arm veto the clean one, a false-negative machine); the covariate was declared near-vacuous
  *honestly and up front*. Reinforced by R4.
- **Q3 → adopt default; not internal-contrast-only; fence R6.** The substantive caveat (anchor is a
  restatement, not a fresh annotation source) is *already* freeze condition (vi). Relabelling to
  `internal-contrast-only` would **under-claim** a genuine CC-BY-4.0, textbook-robust, ICE-GB-
  corroborated native-speaker *direction* (per CLAUDE.md that terminal state declares *no* human-
  comparison claim). The genitive sibling resolved the identical question the same way. Honest close:
  human-anchored on the sign, restatement caveat kept prominent, human leg framed as external
  corroboration of the direction.

**Anti-cheat check (mandated):** no default is preferred only because it makes a positive likelier —
givenness makes a positive *harder*; the length-arm demotion removes it from the CONFIRM gate; the
asymmetric rule rests on the *cleaner* arm; the human-anchored posture touches only the licensed claim,
not the measurement or gate. The design's rigor advantages cut against an easy positive.

## Binding residual freeze conditions R1–R7 (the s225 freeze honors these)

- **R1 (fence, Q2-deep).** CONFIRM framed narrowly directional — no "distributional shadow defeated."
  State explicitly that byte-identity + NEW-MENTIONED exclude scored-string shortcuts and object-noun
  lexical recency, but do **not** exclude the panel reproducing the human context→order joint
  distribution; the claim asserts distributional tracking **in the human direction**, not
  information-structural competence beyond that.
- **R2 (certification).** The independent, non-authoring Arm-2 certification (freeze (ix)) must
  explicitly certify GIVEN vs NEW-MENTIONED (a) match the object noun's mention count/recency, (b)
  differ **only** in referential/coreferential status, (c) carry **no** structural-priming leak
  (freeze (viii): no fronting/clefting/topicalization/passive/heavy-NP in either mention). Any of
  (a)–(c) uncertifiable ⇒ the run **defers**.
- **R3 (NEW — sharpens SHOULD-FIX 4).** The certifier must additionally verify the definite scored
  object is **comparably felicitous** in GIVEN and NEW-MENTIONED, so shift₂ cannot ride an
  accommodation/processing-difficulty asymmetry. If NEW-MENTIONED can only be built by rendering the
  definite object infelicitous, neutralize it (bridging that does not itself confer givenness), else
  shift₂ is contaminated → defer or fall to the Option-B rescope.
- **R4 (asymmetric rule stays honest).** Firewall shift₂ CI-LB>0 necessary+primary; Arm 1
  directional-consistency only; pre-registered ex ante, not re-tuned. (a) A **reversal** in Arm 1
  (anti-human point estimate) is not "directionally consistent" and blocks CONFIRM → FALSIFY/REVERSAL;
  (b) "CONFIRM, firewall-borne" prose is scoped to "integrates referential discourse-givenness in the
  human direction" and must not be written as confirming the Kim et al. *determiner* effect specifically.
- **R5 (Q1).** Object givenness stays focal; length (Arm 3) stays a SECONDARY convergent leg outside the
  CONFIRM gate, not blended into the givenness measures. Switching the focal constraint to length is
  rejected.
- **R6 (Q3).** Keep `anchor: human-anchored` on the direction only; not internal-contrast-only, not
  Dubois-strength. Restatement caveat prominent in the result's opening blockquote and prose; no
  per-item gradient, no human-level claim, no "as strong as Dubois" rhetoric; human leg framed as
  external corroboration of the direction.
- **R7 (standing).** All s224 freeze conditions (i)–(x), NEW-MENTIONED as the Option-A default
  (Option-B rescope only if A cannot be cleanly built + certified), SHOULD-FIX 1–5, sha-freeze before
  any call, powered-in-frames with Arm 2 ≥ Arm 1, no retuning / FALSIFY→pre-registered-v2, and "a
  pre-run-critic NO-GO on the firewall **defers** the run" remain binding.

## Net

**ADOPT-WITH-MODIFICATION.** The decorrelation vote's REJECT was weighed in full: its convergent core is
either already handled by the s224 hardening (NEW-MENTIONED, asymmetric rule, restatement caveat) or
carried as fence conditions R1–R4/R6; its two design-changing preferences are met in substance (length
non-gating; caveat a freeze condition) while the internal-contrast-only relabel is rejected as an
under-claim on the fresh critic's reasoned grounds. The vote names no fatal defect — a weighed-and-
addressed decorrelation input, its intended function, not a veto. R3 (definite-felicity certification in
NEW-MENTIONED) is the one genuinely new binding requirement added beyond the s224 record. The probe did
not run in this ratifying session. Spend at this step: $0.003591 (one decorrelation vote); the
fresh-agent reviewer and page authoring are harness-model / $0.
