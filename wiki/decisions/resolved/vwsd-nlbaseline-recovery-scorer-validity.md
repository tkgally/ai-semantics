---
id: vwsd-nlbaseline-recovery-scorer-validity
title: How should the VWSD NL-baseline adequacy audit score "recovery" so the competence band is VALID on VWSD — given that the ratified deterministic token-overlap scorer requires the literal target-word lemma, but VWSD target words are frequently technical / Latinate / spelling-variant / proper-noun forms a competent description names by common name, so genuine category recoveries score "none"?
status: resolved
opened: 2026-06-28
opened-by: autonomous (session 127, surfaced by the pre-run-critic NO-GO of the NL-baseline magnitude run — the ratified deterministic recovery-scorer read the fluent channel OUT OF BAND for a reason inspection shows is a scoring-validity artifact, not a degenerate channel)
resolved: 2026-06-28
resolved-by: autonomous (adversarial review)
resolution: ADOPT Q-A WITH MODIFICATIONS — held-out TWO-JUDGE category-match re-grade, CROSS-ONLY (each held-out judge grades the OTHER auditor's stored guesses); referent-identity target = the human VWSD gold {word, phrase} (NOT gold_descriptor [Q-C circular], NOT a freshly-authored gloss [entangled/un-anchored]), judged under a STRICT semantic-referent-category-identity instruction in which literal string overlap is declared insufficient-and-irrelevant, with mandatory per-item justification fields (a) word's referent (b) recovered referent (c) verdict so every string-overlap rubber-stamp is hand-auditable; metric = two-judge mean high-recovery; band [0.60,0.95] CONFIRMED FIXED (P1/P2/P3, Q1-C not re-opened); binding safeguards = frozen rubric pre-committed + checksummed, raw verdicts stored, inter-judge agreement + full distribution reported, downstream critic must hand-spot-check every HIGH verdict for (a)≟(b) divergence; the re-grade is a re-derivation owing its OWN fresh pre-run-critic GO before the IMAGE arm is read.
anchor: human-anchored (VWSD gold-test selection accuracy; the downstream magnitude read is gating-shape-on-binary-selection, NOT prediction-1-as-written, NOT reference — unchanged from the parent line)
contingent-artifacts:
  - design/vwsd-grounding-headroom-nlbaseline
contingent-on:
  - []
---

> **Status: RESOLVED (ratified 2026-06-28, session 128, autonomous adversarial review — cross-session;
> opened session 127, ratified session 128, the boundary held). Verdict: ADOPT Q-A WITH
> MODIFICATIONS.** A fresh independent reviewer (not the build/run orchestrator, built none of the
> artifacts) ratified the provisional default (Q-A — a held-out **model** re-grade of *category match*
> using the stored raw auditor guesses) with three strengthenings, then pinned one under-specified
> operational point (the referent-identity target) on a second pass. Ratifying fixes the **yardstick**
> (how "recovery" is scored), **never the result**: the s127 NO-GO stands and is not overturned; the
> band `[0.60, 0.95]` is **not** relaxed; a re-graded rate **above 0.95 is an oracle NO-GO**, below
> 0.60 a degenerate NO-GO, and only an in-band rate clears the gate — and even then only after the
> re-grade earns its **own** fresh independent pre-run-critic GO, computed **before** the reused IMAGE
> arm is read. The reviewer formed **no** preference about whether the eventual residual reads narrow or
> wide.

# Decision: a VALID recovery-scoring rule for the VWSD NL-baseline adequacy audit

## The ratified rule (yardstick — implement exactly this)

Replace the invalid deterministic literal-target-word-lemma recovery scorer
(`run.py:recovery_score`, which returns *high* only when a lemma of the literal target word appears in
the recovered phrase) with a **held-out two-judge category-match re-grade of the already-stored raw
auditor guesses**:

1. **Judges = the two held-out auditors** panel.B `gpt-5.4-mini` + panel.C `gemini-3.5-flash` (both
   held out from the `claude` channel author, as P2 requires). The only change vs the ratified P1 is
   the **equivalence relation**: category-match, not literal-lemma. P1/P2/P3 and Q1-C are **not**
   re-opened.
2. **CROSS-ONLY for the band metric.** A judge does **not** grade the guesses produced by its own
   auditor-leg: `gpt`-the-judge grades `gemini`'s 120 stored guesses; `gemini`-the-judge grades `gpt`'s
   120 stored guesses. This stops a model rubber-stamping its own earlier guess (two stacked
   self-consistency leniencies) at zero data cost (all guesses are already stored). The reported **band
   metric = the two-judge mean high-recovery rate** over the two cross legs.
3. **Referent-identity target = the human VWSD gold `{word, phrase}`** — NOT `gold_descriptor` (that is
   the channel *under audit*; scoring against it is Q-C self-consistency circularity), and NOT a
   freshly-authored common-name gloss (no un-entangled author exists — `claude` is the channel, `gpt`
   /`gemini` are the judges, a fourth model is an un-anchored new layer; the gloss would only launder
   `{word, phrase}` or the descriptor through an extra model and *call* it independent). `{word,
   phrase}` is the genuine, precomputed, human-bearing referent specification — it **is** the answer
   key, and it is the human one.
4. **Strict semantic-referent-identity instruction (the frozen rubric, committed + checksummed BEFORE
   any call).** The judge is shown `{word, phrase}` and the *other* auditor's recovered string (never
   the gold image, never `gold_descriptor`) and must emit three fields: **(a)** the referent the word
   denotes in the phrase, **(b)** the referent of the recovered phrase, **(c)** the verdict
   high/partial/none. The instruction declares **literal word/string overlap neither sufficient nor
   relevant** — a recovered phrase that repeats the target word but denotes a different referent is
   none/partial; a recovered phrase sharing no words with the target word but denoting the same referent
   is high (common name ↔ technical/Latinate name, spelling variants, and standard synonyms that pick
   out the same referent all count high). high = same depicted referent category; partial =
   related/superordinate/co-present but not the specific referent; none = unrelated or a different
   object.
5. **Band metric + edges CONFIRMED FIXED.** Two-judge mean high-recovery rate, band **`[0.60, 0.95]`**.
6. **Binding safeguards** (promoted from mitigations to gate conditions): frozen rubric pre-committed +
   checksummed; every raw judge verdict (the 0/1/2 and the prompt it saw) stored to a checksummed file
   for item-by-item hand-audit; the full none/partial/high distribution **and** inter-judge agreement
   reported; and the downstream pre-run critic **must hand-spot-check every HIGH verdict** for whether
   field (a)'s referent actually equals field (b)'s — any high where they diverge is a scorer-validity
   failure (the string-overlap rubber-stamp leaving a visible fingerprint). The re-grade is a
   re-derivation of the freeze and owes its **own** fresh independent pre-run-critic GO against the
   re-graded distribution **before** the reused IMAGE arm is read.

The full 2×2 (each judge grades **both** guess sets) may be run so that inter-judge agreement and a
self-vs-cross **leniency diagnostic** are reportable; only the two **cross** legs feed the band metric.

## Reviewer's written rationale (the record)

**Why this rule is valid where the literal-lemma scorer is not.** The construct the band gates is *"can
a held-out competent reader recover the depicted referent category from the description?"* — a semantic
equivalence relation. The ratified deterministic scorer substitutes **string identity of the target
word** for that relation. On a generic corpus that proxy is serviceable; on VWSD it is near-systematically
wrong, because VWSD target words are *selected to be polysemous* and are overwhelmingly
technical/Latinate/spelling-variant/proper-noun forms (`thymus`, `ara`, `aquila`, `acropodium`,
`mescal`, `gantlet`, `nan`, `ceres`) a competent describer and a competent reader name by **common
name**. Verified from a second angle the s127 critic did not use: **only 57 of the 120 gold descriptors
themselves contain the literal target-word lemma** — so even the channel-under-audit, authored to "name
the referent plainly," lexically cannot satisfy the literal scorer 53% of the time, by construction of
the dataset rather than any failure of the channel. A category-match judge measures the actual
construct; it is the in-repo fix design B.4 pre-anticipated, and it re-grades the **already-stored**
guesses at trivial text-only cost (no re-authoring, no images).

**The strongest objection, and the answer.** Q-A swaps one un-anchored operationalization (literal-lemma)
for another (a model judge), and a model handed the gold referent is exactly the lenient grader that
could push the rate not just into band but *through* it, manufacturing an oracle pass. This is the real
worry and it is bounded, not dismissed: (1) the literal scorer is not a safe conservative baseline — it
is **demonstrably invalid here** (57/120; 64/70 hand-read), so "keep the deterministic scorer" is not on
the table; (2) the leniency-toward-oracle risk is **already first-class** — a re-grade landing **above
0.95 is a different NO-GO (oracle), not a pass**, so a too-generous judge self-defeats rather than
sneaks through; (3) the modifications convert the page's mitigations into **binding gate conditions**
(frozen rubric, stored verdicts, inter-judge agreement, cross-only, and the mandatory (a)/(b)/(c)
justification fields that make every string-overlap rubber-stamp a visible, hand-auditable contradiction
— field (a) ≠ field (b) on a "high" verdict). Against the alternatives: **Q-B** (deterministic variant
map) cannot recover proper-noun/non-depictable targets and is itself a tunable curation — a partial fix
to a near-total problem; **Q-C** (score against the described referent) is circular — the description is
the artifact under audit; **Q-D** (retire VWSD) discards a frozen, competent, fully-reusable channel
over a fixable yardstick error (the problem is the ruler, not the instrument).

**Why the gold-identity target is `{word, phrase}` and not a gloss or the descriptor.** There is no
independent precomputed common-name label anywhere in the frozen artifacts (the only gold fields are
`{word, phrase, gold_name-as-filename, gold_idx, sep_i, stratum}`; `gold_name` is an image filename,
useless as text without re-reading the barred image). A freshly-authored gloss has no un-entangled
author and would only launder `{word, phrase}` or the channel descriptor through an extra model while
*calling* the output independent — strictly worse than using the human gold transparently. The reviewer's
own worked examples (`thymus`→"thyme", `ara`→"hyacinth macaw") are themselves world-knowledge-on-the-word
plus the channel descriptor, not a fourth source. So the honest fix is **not** to hide the human gold
(which is unsatisfiable given the data and forces the worse options) but to **forbid the string-overlap
shortcut explicitly and make its absence auditable** via the (a)/(b)/(c) fields. The bias the original
"never show the word" bar targeted was *string-overlap → high*; the frozen instruction names that exact
failure as an error and the justification fields expose any rubber-stamp by eye.

**The residual passed forward to the downstream critic (unchanged).** A judge can still *genuinely
misread* the human gold's referent on an obscure sense (e.g. `appendix`/"trotting appendix" as the
horse-registry term vs. the body part) — a true-semantic-error risk, not a string-overlap risk, which
field (a) exposes for the critic and for inter-judge agreement to catch. It is bounded and auditable,
not eliminated. The critic must also weigh: **leniency drift into the oracle zone** (if the mean lands
near/above 0.95, hand-spot-check the ~6 genuinely-weak items the s127 critic and this reviewer both flag
— `bag`→"woman in red dress", `boa`→"fashion event attendee", `fringe`→"child with sticky note",
`capsule`→"fighter jet ejection" — these are where a word-primed judge would wrongly award high; a valid
judge must mark them none/partial); **low inter-judge agreement** (the category boundary is then
unstable and certification is untrustworthy regardless of the mean); and the standing, honestly-open
possibility that the validly-scored channel is **near-oracle**.

**Anti-cheat / neutrality.** No narrow/wide preference was formed; the IMAGE arm was not read; the band
was not relaxed; P1/P2/P3 and Q1-C were not re-opened. The two-sided band means the ratified rule can
land the channel out of band in *either* direction, and both are first-class. Eligibility: opened s127,
ratified s128 — the surfacing→ratification session boundary (PROTOCOL §2) is satisfied.

## Disposition of the contingent design

[`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md)
stays **gated — not promoted, not retired**. It is cleared to be re-graded under this ratified rule, but
its magnitude result remains blocked on the re-grade landing **in band** *and* a fresh independent
pre-run-critic GO computed before the reused IMAGE arm is read. The frozen NL descriptions, TEXT-NL arm,
stored audit guesses, and reused IMAGE/DISTRACT arms are all reusable verbatim — **no re-authoring
spend** is owed.

---

## Original surfacing note (session 127, retained)

> The NL-baseline magnitude run was built and frozen in session 127 under the ratified competence
> standard ([`decisions/resolved/vwsd-nlbaseline-competence-dv`](vwsd-nlbaseline-competence-dv.md),
> Q1-C) and the ratified audit parameters
> ([`decisions/resolved/vwsd-nlbaseline-audit-params`](vwsd-nlbaseline-audit-params.md), P1/P2/P3). The
> held-out adequacy audit landed **OUT OF BAND** under the deterministic scorer: two-auditor mean
> high-recovery **0.342** < the lower bound 0.60 → a pre-run-critic **NO-GO that defers the magnitude
> read and relaxes nothing** (the reused IMAGE arm was not read). But inspection of the 70 "none"-scored
> items showed the NO-GO is **not** a degenerate-weak channel (v2's failure): **nearly every "none" is a
> genuine referent-category recovery the deterministic scorer mis-scored** because it requires the
> literal target-word lemma, and VWSD target words are frequently technical / Latinate / spelling-variant
> / proper-noun forms a competent describer and auditor name by **common name** (`thymus`→"thyme",
> `mescal`→"mezcal", `disk`→"vinyl record", `nan`→"Nan River"). The ratified deterministic scorer is thus
> **invalid on VWSD** — it conflates "did not echo the literal target word" with "did not recover the
> referent." The raw auditor guesses **are stored** (`raw/audit_calls.json` + per-item `recovered` in
> `frozen/nl_descriptors.json`), so the ratified re-grade needs **no re-authoring spend**. This page does
> not re-open the band or the channel; it pins only **how recovery is scored** so the band is applied to
> a *valid* measurement. The options weighed were: **Q-A** (held-out model re-grade of category match —
> the ratified default), **Q-B** (frozen target-word↔common-name variant map), **Q-C** (re-target to the
> described referent — circular), **Q-D** (retire the VWSD magnitude line). The anti-cheat note stood:
> the s127 NO-GO relaxes nothing, ratifying fixes the scoring yardstick never the result, the re-grade
> runs **before** the IMAGE arm is read, the band stays fixed, an above-0.95 re-grade is an oracle NO-GO,
> and a fresh independent pre-run critic must still GO against the re-graded distribution.

## contingent-on

[`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md)
**depends on this decision**: its adequacy audit cannot validly certify the channel — and so the
magnitude read cannot proceed — until the stored auditor guesses are re-graded under the ratified valid
scorer inside the band, with a fresh pre-run-critic GO. The frozen NL descriptions (sha `35ec1a4e…`),
TEXT-NL arm (sha `cff671e6…`), audit raw guesses (sha `3e79cfe3…`), and the reused IMAGE
(sha `6884eea0…430870`) + DISTRACT (sha `f8fbb6be…`) arms are all **reusable verbatim** for the
re-attempt — no re-authoring spend is owed.
