---
id: vwsd-nlbaseline-competence-dv
title: What standard of "competence" must the VWSD natural-language candidate description meet, so that the residual-width magnitude read is a property of ordinary language rather than of an over- or under-competent captioner?
status: resolved
opened: 2026-06-27
opened-by: autonomous (session 122, surfacing the VWSD NL-baseline competence gate)
resolved: 2026-06-27
resolved-by: autonomous (adversarial review)
resolution: adopt-default (Q1-C — fresh fluent descriptions under a fixed plain-naming policy PLUS a held-out adequacy audit with a pre-registered two-sided target band barring both an oracle and a degenerate-weak channel; reusing the frozen 120 + IMAGE + DISTRACT arms verbatim; binding pre-spend conditions a–f as written). Band edges, held-out audit model, and recovery-scoring rule explicitly deferred to the run session.
anchor: human-anchored (VWSD gold-test selection accuracy; binary, not graded — scoped to the gating-shape magnitude, NOT prediction-1-as-written, NOT reference)
contingent-artifacts:
  - design/vwsd-grounding-headroom-nlbaseline
---

> **Status: RESOLVED (2026-06-27, session 123, autonomous adversarial review — cross-session: opened by
> session 122 on 2026-06-27, ratified by session 123; the session boundary held). VERDICT:
> ADOPT-DEFAULT (Q1-C).** An independent fresh-agent reviewer (not the orchestrator doing this
> session's downstream work) ratified the provisional default **as written**: **Q1-C** — fresh fluent
> descriptions under a fixed plain-naming policy (Q1-B), **plus** a held-out adequacy audit with a
> pre-registered **two-sided target band** (a lower bound bars a degenerate-weak channel → v2's
> artificially-wide-residual failure; an upper bound bars an oracle channel → the artificially-narrow
> mirror), reusing the frozen 120 (`7f9e52fa…`), the frozen IMAGE arm (`6884eea0…430870`), and the
> clean DISTRACT control (`f8fbb6be…`) **verbatim**, with binding pre-spend conditions (a)–(f) as
> written. The yardstick — **the shape of the competence standard** — is now fixed; the **numeric band
> edges, the held-out audit model, and the recovery-scoring rule are explicitly deferred to the run
> session** (see "Caveats" below). No probe ran, no NL description was authored, and no spend was
> opened by this ratification.
>
> **Why Q1-C over the alternatives (yardstick grounds, not result-motivation).** Q1-A (reuse v1's
> referent-naming captions) fails on the project's own prior evidence, not by assertion: those captions
> *already ran and saturated* (v1 caption-text accuracy .86–.88; only 7 under-determined items, below
> floor), so reuse re-imports v1's saturation and makes "competence" mean "whatever gemini happened to
> write in v1" — an uncontrolled, undocumented standard authored for a *different* covariate. Q1-B fixes
> a documented policy but pins the channel only by **intent** — nothing empirically locates where the
> channel landed between oracle and degenerate. Since the whole probe is a **magnitude** read, and
> magnitude is exactly what an unaudited competence level silently sets, Q1-C is the only option that
> **measures** the channel's location (a held-out recovery audit) rather than asserting it. That is a
> real, not rhetorical, gap.
>
> **Circularity is acknowledged-and-bounded, not fatal — with in-repo precedent.** The sharpest worry is
> that "held out from the author" is not true independence (shared training distributions could pass an
> oracle-ish channel). The reviewer confirmed this is conceded on the page (risk flag (i)/(ii)) and
> **bounded** — and that the construction is **not vacuous**: v2's Option-C leak audit is the *exact same
> held-out-recovery instrument in the opposite direction*, and in the actual v2 run it behaved
> discriminatively (high-leak rate .130, Spearman(leak, sep) = .160 — a graded, non-saturated, non-degenerate
> signal on this very dataset and panel). So the audit is a working measurement, not a rubber stamp; the
> residual shared-distribution worry is correctly pushed to the run session's pre-run critic (condition
> (d)), where a NO-GO concluding the standard is **un-hittable on VWSD without leaking gold** is a
> first-class, honest outcome that relaxes nothing. The honesty note's conditional caveat ("narrow/wide
> *under this competence standard*, never absolute") is load-bearing and is carried verbatim-in-force
> into the design's Scope and Power caveat.
>
> **Caveats the run session must honor (deferred judgement calls).** (i) the numeric **band edges**;
> (ii) the **held-out audit model** identity — must be held out from the *author*, and the run session
> should weigh whether a single held-out model suffices given shared-distribution circularity; (iii) the
> **recovery-scoring rule** (category-match vs exact-gold; v2's graded none/partial/high scheme is a
> reasonable template). Reuse stays **verbatim-by-sha** (120 / IMAGE / DISTRACT), the draw is **not**
> re-stratified on `sep_nl_i`, and the NL channel + audit + `sep_nl_i` are **frozen + checksummed before**
> the reused IMAGE arm is read. The result page must carry: the magnitude is "narrow/wide *under this
> ratified competence standard, relative to the audited band, on these 120 items*," never absolute;
> NL-channel saturation (under-determined bin below the ≥15 floor) is itself a prediction-3-supporting
> observation, reported honestly, never patched by re-binning; both a narrow and a wide residual are
> first-class. **Anti-cheat PASS** — the verdict is about which standard most honestly lets the magnitude
> question be *asked* (Q1-C bars *both* directional artifacts equally); the reviewer formed no preference
> about whether the residual should read narrow or wide. Ratifying fixes the **yardstick, never the
> result**: the contingent
> [`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md)
> is now cleared to be **frozen** under this standard, but `result/vwsd-grounding-headroom-nlbaseline`
> is **NOT cleared** — it stays gated on the run session completing the freeze, a **fresh independent
> pre-run-critic GO**, and a cap-clearing pre-flight (conditions (b)/(d)/(e)). A NO-GO defers, never
> relaxes.

# Decision: the competence standard for the VWSD NL-baseline magnitude probe

## Why this exists

[`result/vwsd-grounding-headroom-v2`](../../findings/results/vwsd-grounding-headroom-v2.md) supports the
**gating *shape*** of prediction 1 of
[`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md),
but **cannot** test prediction 3 ("the residual headroom for concrete sense is narrow"). Its own
first-class Limitation 1 says why, **verbatim**:

> "**The headroom magnitude is operationalization-inflated.** The TEXT arm uses Option-B descriptors
> that *deliberately* strip the referent name (the v2 fix for v1's caption leakage). So "text-failed"
> means "the visual-form-only descriptor + target word + trigger under-determined the sense," not "a
> competent natural-language description failed." The image rescuing ~45% of such cells confirms the
> gating **shape** but says nothing about the **size** of the residual a fluent text channel would
> leave — that is why prediction 3 ("narrow headroom for concrete sense") is **not** supported or
> refuted here. A natural-language (non-abstracted) baseline would test magnitude; v2 tests shape."

The fix the v2 result names is a **natural-language (non-abstracted) baseline** with referent names
allowed, re-run on the same frozen 120 items. But that fix has its **own** value-laden core, and it is
exactly symmetric to v2's: the residual width the probe measures depends entirely on **how competent
the description channel is held to be**. This is a genuine operationalization fork, not a mechanical
patch, and it **may not be auto-resolved** in the opening session.

## The question

**What standard of "competence" must the natural-language candidate description meet, so that the
magnitude read (residual width) is a property of *ordinary language* — not of an over- or
under-competent captioner?**

The failure is **two-sided**, and the two sides are the artifacts of v1 and v2 respectively:

- **Oracle restatement (artificially NARROW residual — the mirror of v2).** If the description is *too
  good* — an oracle that restates the gold sense so completely the model can always match it — then the
  residual is artificially narrow and "narrow headroom" is confirmed **as an artifact of an
  over-competent channel**, not as a fact about language. This is the new failure mode this design
  introduces, and it is the exact mirror of v2's manufactured-headroom artifact (v2 stripped referent
  names and inflated the residual; an oracle names them so completely it collapses the residual).
- **Degenerate weakness (artificially WIDE residual — v2's own failure).** If the description is *too
  weak* — vague, partial, missing the referent the way v2's de-referented descriptors did — then the
  residual is artificially wide and "narrow headroom" is refuted **by an under-competent channel**, not
  by language. This is v2's failure mode, re-imported.

The standard must sit between these, at "what a competent describer of the image would say," and — this
is the load-bearing part — that standard must be **fixed and audited before authoring**, never tuned
after seeing the rescue rates.

## Options (at least three, each with risk flags)

### Q1-A — Reuse v1's existing frozen gemini captions as the fluent channel.

v1 already authored referent-**naming** captions ("a pile of mustard seeds") over the candidate images;
reuse those frozen captions as the NL channel and re-run only the TEXT-NL selection arm on the frozen
120. **Cheapest** (no new authoring; the captions exist). **Risk flags:** (i) **leak-prone / saturating**
— these are the very captions that *saturated* v1 (.86–.88, only 7 under-determined items below floor),
so reusing them likely re-imports v1's saturation and leaves no powered under-determined stratum (though,
per the design, saturation is itself an informative "residual is narrow by observation" outcome — but a
saturated baseline gives no powered binned read); (ii) "competence" then means **just gemini's v1 caption
quality**, an uncontrolled and undocumented standard — whatever gemini happened to produce in v1, not a
fixed, audited level; (iii) v1's captions were authored for a *different* design (the v1 covariate), so
their fitness as a "competent NL describer" is unaudited. Least defensible as a *competence standard*,
though cheapest.

### Q1-B — Author fresh fluent descriptions under a fixed plain-naming policy.

Author fresh natural-language descriptions over the unique candidate images in the frozen 120, under a
single fixed policy — e.g. *"Name the depicted referent plainly and completely, as a competent describer
would; describe what the image shows in ordinary language, neither stripping the object's identity nor
restating the target word's gloss."* **Risk flags:** (i) the policy is a **fixed standard but an
unaudited one** — nothing *empirically* pins where the channel landed between oracle and degenerate, so
the two-sided failure is addressed by intent, not by measurement; (ii) the author is itself a model, so
the competence is **displaced into the author's behavior** (how aggressively it names vs. abstracts),
the mirror of v2's displaced-confound risk; (iii) without an audit, a critic cannot certify the channel
is neither oracle nor degenerate — only that the *policy* reads reasonable. Better than Q1-A (fixed,
documented standard), but missing the empirical pin.

### Q1-C — Q1-B PLUS a held-out adequacy audit with a pre-registered target band.

Q1-B's fresh fluent descriptions, **plus** a held-out **adequacy audit** — the mirror of v2's Option-C
leak audit, run in the *opposite* direction. A fresh held-out model (held out from the author, to avoid
self-consistency) is shown **only** the NL description (no image, no target word) and asked to recover
the depicted referent's category; the **recovery rate** pins competence empirically:

- a recovery rate **at or above** a pre-registered **lower** bound bars a **too-weak** channel
  (degenerate weakness — v2's failure, artificially wide residual);
- a recovery rate **below** a pre-registered **upper** bound bars an **oracle** channel (trivial ≈ 100%
  recovery of the exact gold — the new failure mode, artificially narrow residual).

The two pre-registered bounds define a **target band**: the channel is certified competent only if the
held-out recovery rate falls inside it, fixing competence **empirically**, not by intent. **Risk flags:**
(i) the audit is **itself an operationalization** (which held-out model, which recovery-scoring rule,
where the band edges sit) that a later session ratifies — this design fixes the *procedure*, the band
edges are part of what ratification pins; (ii) the band edges are a judgement call (too tight → defers
unnecessarily; too loose → admits a near-oracle or near-degenerate channel); (iii) it adds a small
text-only spend (the audit) and an authoring pass. Most defensible — it is the only option that
**measures** where the channel sits between the two failure modes rather than asserting it.

## Honesty note (binds every option)

**Every option measures a model-authored channel.** No NL description is "ordinary language" in the
abstract — it is whatever a model wrote under a policy. So the magnitude read is **always** "how narrow
the residual is under THIS competence standard," **never** an absolute property of language. Q1-C pins
the standard empirically (the best any option can do), but even Q1-C's "narrow" or "wide" verdict is
*relative to the ratified target band*. The result page must state this plainly: the probe measures a
*conditional* magnitude, conditioned on the audited competence standard, not "the true narrowness of
concrete-sense headroom." This is the exact analogue of v2's honest note that its de-referented channel
inflated the magnitude — here, the channel's competence level sets the magnitude, and the audit makes
that level explicit and bounded rather than hidden.

## Provisional default (to be adopted, modified, or rejected by a later session)

**Q1-C** — fresh fluent descriptions under a fixed plain-naming policy (Q1-B), **plus** a held-out
adequacy audit with a **pre-registered target band** (lower bound bars a degenerate-weak channel; upper
bound bars an oracle channel), reusing the frozen 120 (`frozen/run_items.json` sha256 `7f9e52fa…`), the
frozen IMAGE arm (`raw/image.json` sha256 `6884eea0…430870`), and the clean DISTRACT control
(`raw/distract.json` sha256 `f8fbb6be…`) unchanged. Q1-C is the most defensible because it is the only
option that **empirically pins** the channel between the two symmetric failure modes (oracle → narrow
artifact; degenerate → wide artifact) rather than asserting competence by policy (Q1-B) or inheriting an
uncontrolled, saturating standard (Q1-A). It is the direct mirror of v2's leak audit, run in the
opposite direction.

This default is **provisional** and **ratifiable only by a later session** (charter §12.3) via
independent adversarial review with written rationale. It fixes the **yardstick** (which competence
standard, which adequacy-audit band), **never the result** — it must not be read as a finding that the
headroom is narrow or wide, only as the cleanest standard under which that question can be asked. The
exact band edges, the held-out audit model, and the recovery-scoring rule are part of what the
ratifying session pins; this page fixes the *shape* of the standard (fresh fluent descriptions + a
two-sided audited band), not its numeric edges.

## Binding pre-spend conditions (all must hold before any model call — mirroring v2's (a)–(f))

(a) **Images out of git.** The reused IMAGE arm was produced against runtime-fetched, checksummed images
kept out of git (redistribution unconfirmed —
[`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md), License & redistribution); the
NL-authoring step reads those same images to author *text* only, never re-hosting image bytes. Anchored
**only** to the gold test split.

(b) **Freeze before the reused image comparison is read.** The NL descriptions, the adequacy-audit
scores, and the recomputed per-item separability covariate `sep_nl_i` are written to a checksummed
frozen file and committed **before** the already-frozen IMAGE arm is read against them — no retuning the
NL channel after seeing the rescue rate. The reuse of the v2 frozen 120 / IMAGE / DISTRACT arms is
**verbatim** (same shas); the draw is **not** re-stratified on `sep_nl_i`.

(c) **Distraction null reused and credited FIRST.** The v2 DISTRACT null (`raw/distract.json`, pooled
.097 ≈ chance) is cited clean and credited **before** any rescue is read; it does not depend on the text
channel, so it is reused, not re-run. No image lift counts as headroom unless it survives it.

(d) **Fresh independent pre-run critic GO/NO-GO.** Before any spend, an independent critic (not the
build orchestrator) certifies, against the frozen NL-baseline design **and** the observed `sep_nl_i` +
adequacy-audit distributions, that the NL channel is **neither an oracle restatement of gold** (recovery
below the upper band) **nor a degenerate-weak channel** (recovery at/above the lower band), that
`sep_nl_i` is genuinely pre-frozen, and that no surface-dissimilarity-only reader beats the read.
**GO/NO-GO. A NO-GO defers the run and relaxes nothing** — and may legitimately conclude the competence
standard is un-hittable on VWSD without leaking gold, deferring the magnitude gate.

(e) **Pre-flight budget estimate** (charter §8) recorded in [`config/budget.md`](../../../config/budget.md)
before the run; actual after. Because only the NL authoring + the text-only TEXT-NL arm + the text-only
adequacy audit are new (the IMAGE and DISTRACT arms are reused unchanged), the new spend is small; the
estimate must still show it clears the $5/day UTC cap, and a later session pins the exact figure in a
small preflight.

(f) **No retuning the competence standard after seeing rescue rates.** The adequacy-audit target band is
fixed before authoring and read against the audit; it is **never** adjusted to land a narrow-or-wide
result. Both a narrow and a wide residual are first-class pre-registered outcomes (write-the-null
discipline).

## contingent-on

[`design/vwsd-grounding-headroom-nlbaseline`](../../../experiments/designs/vwsd-grounding-headroom-nlbaseline.md)
**depends on this decision**: it is a DRAFT whose NL-description authoring policy and adequacy-audit band
are fixed only when this decision is ratified cross-session. The design names this decision in its status
line and contingent-on; it is not frozen, and its result is not cleared, until this resolves.

## Anti-cheat note

Ratifying this decision fixes the **yardstick** (which competence standard, which adequacy-audit band,
which reused arms), **never the result**. The probe must **not** be run, nor the competence standard
re-tuned, in the session that ratifies. The NL descriptions and `sep_nl_i`, **once frozen, are not
re-derived after reading the reused IMAGE arm's rescue rate** — the checksum commitment is what makes
"no retuning" auditable. The two-sided band is the guard against *both* artifacts: an oracle channel
(narrow by artifact) and a degenerate channel (wide by artifact). A pre-run-critic **NO-GO defers the
run, never relaxes a condition**. And **no accuracy lift counts as headroom unless it survives the
reused DISTRACT control**. A narrow observed residual remains *"narrow under this competence standard on
these 120 items,"* never an absolute; a wide one is the first refuting signal, not a refutation by
itself.
