---
type: open-question
id: grounding-magnitude-instrument
title: "What instrument could test the grounding-headroom MAGNITUDE (prediction 3) now that the VWSD competence-audited fluent channel is blocked?"
meaning-senses:
  - grounded.perceptual
  - referential.sense
  - distributional
status: open
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: result/vwsd-grounding-headroom-nlbaseline-regrade-v1
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v2
  - rel: depends-on
    target: resource/things-data-triplets
  - rel: depends-on
    target: resource/vwsd-semeval-2023
  - rel: depends-on
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: resource/wic-graded-usage-similarity
---

# Open question: what instrument tests the grounding-headroom *magnitude* now that the VWSD fluent channel is blocked?

> **Why this page exists.** [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
> makes a *gating shape* bet (prediction 1) and a *magnitude* bet (prediction 3: for concrete sense the
> residual the text distribution leaves under-determined is **empirically narrow**). The gating shape now
> has confirming-direction VWSD evidence ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md),
> session 121, 3/3 models in direction, distraction-controlled). The **magnitude** does not — and the
> instrument designed to measure it on VWSD is **blocked**. This is a **scoping** page: it states the
> magnitude question precisely, derives the requirements a valid magnitude instrument must satisfy from
> the block that stopped VWSD, and assesses the in-repo candidate resources against those requirements. It
> does **not** commit to running anything and ratifies nothing. NO model is run; nothing is spent.

## The question, sharply

The v2 run confirmed the gating *shape* but could not read the magnitude, because its under-determined
stratum was **partly manufactured** by a deliberately de-referenced descriptor channel: the v2 TEXT arm
used Option-B descriptors that *strip the referent name* (the fix for v1's caption leakage), so
"text-failed" meant "the visual-form-only descriptor under-determined the sense," not "a competent
natural-language description failed" ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md),
Limitations 1). The +.324 / .453-rescue residual is therefore real as a *shape* signal but says nothing
about how *wide* the residual a fluent channel would leave actually is. That is exactly the magnitude
prediction 3 is about.

The successor designed to fix this — a **competence-audited fluent description channel**, where the text
channel is a natural-language referent-naming description whose competence is *certified* before the
image arm is read — was built and frozen but **deferred at the adequacy-audit gate** at session 127, then
re-graded under a ratified valid scorer at session 128 and **still blocked**: the fluent channel's strict
held-out referent-recovery is **0.438**, below the ratified `[0.60, 0.95]` competence floor, and a fresh
independent critic verified that 0.438 is a *valid* low rate, not a scorer artifact
([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).
The block has a two-horned cause the run could not separate: either the model-authored channel genuinely
under-recovers the specific sense, **or** VWSD's polysemous targets make *specific*-referent recovery
from a description alone intrinsically hard (a held-out reader recovers "a horse show," not "the Appendix
Quarter Horse"). Either way, on VWSD the competence-audited-fluent-channel route to the magnitude is
**blocked under the ratified standard**.

So the question:

> **What instrument could test prediction 3's MAGNITUDE — how *wide* the grounding headroom is for
> concrete lexical sense — given that the VWSD competence-audited fluent channel cannot be certified
> competent on the target items?** Is there an in-repo (or in-repo-scouted) resource on which the text
> channel can be *certified competent on the specific target items*, and which also carries the graded
> human signal a magnitude/degree question wants, so that the size (not just the sign) of the residual can
> be read honestly?

This is a live, tractable scoping question. It is **not** a commitment to a re-run and — per the
do-not-re-grind discipline the regrade page records — **not** a rescue of VWSD: a re-attempt owes a
genuinely *new* instrument, not a re-grade or re-prompt of the blocked one.

## What a valid magnitude instrument must satisfy (requirements, derived from the VWSD block)

The block teaches four requirements. Each is read off a cited result/decision, not imagined:

- **(a) A certified-competent text/description channel on the *specific target items*.** This is the
  failure mode that blocked VWSD: the fluent referent-naming channel's strict held-out referent-recovery
  was 0.438, below the `[0.60, 0.95]` floor, a *valid* rate not a scorer artifact
  ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).
  A magnitude read requires that the text channel be *demonstrably able* to name/identify the target sense
  on the items used — otherwise "text-failed" conflates "text under-determines" with "the channel can't
  speak the target," and the residual's size is uninterpretable.
- **(b) A graded human signal.** Prediction 3 is about *magnitude / degree*, so a binary selection gold is
  weak: it gives the sign of a residual, not its width on a human scale. v2's headline limit is exactly
  this — VWSD gold is **binary correct-image**, not "a graded human relatedness gradient"
  ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), "Does NOT establish";
  [`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md), Known limits: "binary gold,
  not a graded relatedness signal"). A magnitude instrument wants a per-item graded human signal to read Δ
  *against*.
- **(c) Image-native or fine-polysemy material where the senses are perceptually distinguishable.** The
  conjecture's positive cell is where **visual contrast is present but text separability is not** — fine
  polysemy and perceptually-subtle senses ([`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md),
  "What this sharpens"). The material must let an image carry sense-relevant signal, or there is nothing
  for grounding to move.
- **(d) The de-referencing trap avoided.** The magnitude must **not** be manufactured by stripping referent
  names to create the residual; that is precisely what inflated v2's residual and made it a shape-only
  read ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), Limitations 1).
  The under-determination must arise from the *material* (genuinely fine/abstract senses), not from
  crippling the text channel.

Requirements (a) and (b) are in tension on VWSD: its polysemous targets are technical/variant/proper-noun
forms a fluent description names by common name (the diagnosed reason the channel falls below floor), and
its gold is binary. An instrument that satisfies both at once is what is being scouted.

## In-repo candidate assessment

Each candidate is read against (a)–(d), strictly per what its in-repo page says. No candidate's readiness
is overstated; "scouting, not a typed resource" and "partial fit" caveats are carried.

### THINGS-data behavioral triplets — the scouted "graded multimodal" candidate

[`resource/things-data-triplets`](../../base/resources/things-data-triplets.md) (`status: scouted`) was
scouted (session 99 in the scouting note; page created 2026-06-24) as the candidate **graded** multimodal
anchor — "the future graded-image resource" the v2 ratification envisaged.

- **(b) graded human signal: YES.** It carries a **graded** (continuous embedding from ~4.7M judgments),
  **multi-rater**, **human** similarity signal over depicted objects with images attached — "genuinely a
  'graded-image resource'" on the modality + gradedness axes (resource page, "What it can ground").
- **(c) image-native / perceptually distinguishable: PARTLY.** Images attach, but —
- **(a)/(d) and the decisive gap — construct mismatch: NO, does not cleanly fit.** The resource page's own
  load-bearing verdict: THINGS triplets measure **whole-object similarity** (odd-one-out among three
  *objects*), which is "a **different construct** from the conjecture's graded *word-sense relatedness*."
  It "carries **no** same-word, different-sense pairs" — it samples disambiguated object concepts, "not
  ambiguous word forms," so there is no within-word polysemy structure for the magnitude Δ to be computed
  over. The page explicitly records it as **partial / does-not-cleanly-fit**, the right *shape* of signal
  (graded + image) on the **wrong axis** (object similarity, not word-sense relatedness), and says: "Do
  not promote THINGS as the conjecture-1 graded anchor."
- **Unresolved caveats the page forces:** its CC0 license is **stated-but-not-primary-verified** (OSF node
  `node_license = null`); the **base THINGS images are academic-use-only / publication-restricted** —
  image stimuli must come from THINGSplus (PD/CC0) or Wikimedia PD/CC0, never the base set.
- **Verdict:** **not the magnitude anchor.** It could legitimately anchor a *different* claim
  (representational alignment of object-concept geometry), or serve as **scaffolding** — a stimulus source
  / similarity prior for *building* a future graded sense set — but the graded *sense-relatedness* labels
  would still have to come from a DURel-style instrument it does not provide.

### VWSD (SemEval-2023) — the now-blocked instrument, for contrast

[`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md) (`status: catalogued`) is the
image-native instrument the gating shape was confirmed on.

- **(c) image-native: YES** — "sense distinctions are given in the visual modality"; minimal context so the
  image is *necessary* (resource page, "What it can ground").
- **(b) graded human signal: NO** — "binary gold, not a graded relatedness signal … it tests *selection
  accuracy*, not *graded similarity*," and "No inter-annotator agreement is reported."
- **(a) certified-competent fluent channel on the target items: BLOCKED** — the magnitude follow-through's
  fluent channel reads 0.438 strict referent-recovery, below floor, a valid low rate
  ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)),
  with the targets' technical/proper-noun nature a diagnosed contributor.
- **Verdict:** **blocked for magnitude** (it served the gating *shape* fine, and remains the gating-shape
  instrument). Its block is *why* this page exists; it is not a re-attempt target.

### DWUG usage graphs — graded same-word usage proximity, but text-only

[`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (`status: partial`) is the
project's existing graded lexical anchor.

- **(b) graded human signal: YES, the strongest in-repo** — graded, multi-rater, 4-point DURel proximity
  judgments over **usage pairs of the same target word** (9 annotators for EN; ρ .69 / α .61); annotators
  "make frequent use of the intermediate levels of the scale ('2','3') and thus assign graded distinctions
  of word meaning" (resource page, verbatim). This is the **right construct** (same-word sense relatedness)
  THINGS lacks.
- **(a) certified text channel: N/A for the image arm — and (c) image-native: NO.** DWUG is a **text**
  resource: no images, no perceptual material. It cannot supply the disambiguating *image* the conjecture's
  Δ toggles. The prior image probe found DWUG "supplied no clean cross-sense homonym pairs"
  ([`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md),
  "Why this is interesting"), and the resource page notes it does not tag polysemy vs. homonymy out of the
  box.
- **Caveats the page forces:** **CC BY-ND 4.0**, "Republication and redistribution is prohibited" for some
  versions — analysis + verbatim mirror permitted, distributing a modified/augmented version is not; the
  **diachronic** design means within-period pairs must be selected explicitly for a synchronic anchor.
- **Verdict:** **insufficient alone** for a *magnitude* instrument — it is text-only, so it cannot carry the
  image arm (c) at all. It is, however, the in-repo resource that proves the *graded same-word sense-
  relatedness* signal (b) exists and is reusable; a magnitude instrument would need to **add perceptually-
  distinguishable depicted senses** to DWUG-style graded pairs (a build step, not a property of DWUG).

### WiC / Usim graded usage-similarity — graded text signal, no images

[`resource/wic-graded-usage-similarity`](../../base/resources/wic-graded-usage-similarity.md)
(`status: external-only`) catalogs Usim (graded 5-point usage similarity, 34 lemmas / 1530 pairs / 3
annotators) with WiC as the binary cross-check.

- **(b) graded human signal: YES (Usim)** — graded usage-similarity over same-word usage pairs, the same
  DURel tradition; **WiC is binary** and explicitly cannot ground a gradience/magnitude claim (resource
  page: "binary by design").
- **(c) image-native: NO** — text-only, like DWUG.
- **Blocking caveat the page forces:** Usim is `status: external-only` — its released file is **not
  currently fetchable** (Box 404 / mirror 503) and carries **no explicit license**, which is *why* DWUG was
  chosen over it as the gradience anchor. Could not verify Usim's current fetchability from the in-repo
  page beyond "unfetchable as of 2026-05-29."
- **Verdict:** **insufficient** for the same reason as DWUG (text-only, no image arm), and additionally
  **blocked on fetchability/license** for Usim. WiC adds nothing for magnitude (binary). Same role as DWUG:
  evidence that the graded same-word signal (b) exists, not an image-bearing instrument.

### Other scouted multimodal candidates (for completeness)

[`resource/multimodal-anchor-scouting`](../../base/resources/multimodal-anchor-scouting.md) (a *scouting
note, not a typed resource*) catalogs six candidates. Per its own verdicts: **Lancaster Sensorimotor
Norms** are a *text-side word-level* moderator (no images, no usage pairs) — not a magnitude instrument;
**Winoground** and **SNLI-VE** are dropped (license/Getty + gated access; auto-derived labels, 31% neutral
error / unverified license); **NLVR2** and **VALSE** are **binary** image-text benchmarks for a *future
constructional-VLM axis*, not graded sense-relatedness. None of these supplies a graded *word-sense*
relatedness signal with disambiguating images; the note's own graded-multimodal pick is THINGS, assessed
above. So the scouting note adds no new magnitude candidate beyond THINGS.

## Honest bottom line

- **No in-repo resource is a drop-in magnitude instrument.** The requirements (a) certified text channel,
  (b) graded human signal, (c) image-native fine-polysemy material, (d) no de-referencing trap, are not
  jointly met by any catalogued resource. VWSD is image-native but binary and blocked on (a); DWUG/Usim
  carry the graded same-word signal but are **text-only** (no image arm); THINGS is graded + image but the
  **wrong construct** (object similarity, not word-sense relatedness).
- **The single candidate worth a future $0 deeper scout is THINGS — but as *scaffolding*, not as the
  anchor.** Per its own page, THINGS could supply depicted-object stimuli (via THINGSplus PD/CC0) and a
  human similarity prior to **pre-stratify** material for *building* a graded sense set; the graded
  *sense-relatedness* labels would still have to come from a DURel-style instrument (the DWUG-proven signal).
  A future deeper scout would assess whether a fine-polysemy depicted-sense set can be **built** so that the
  text channel can be certified competent on its specific items (requirement (a)) without de-referencing
  (requirement (d)) — i.e. material where under-determination is *intrinsic to the fine senses*, not
  manufactured. That build is the unit a real prediction-3 test would require; the conjecture already names
  "a fine-polysemy image set … **not yet in-repo**" as that unit.
- **None of this rescues VWSD, and a re-attempt owes a genuinely new instrument.** Per the do-not-re-grind
  discipline ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)):
  the VWSD competence-audited-fluent-channel route is blocked under the ratified standard, the 0.438 is a
  *valid* below-floor rate, and "a **different** magnitude instrument … may be needed." This page does not
  re-open VWSD; it scopes what a new instrument would have to be.

## Session-130 deeper scout (update, 2026-06-28)

A $0 open-access scout (full detail + per-candidate provenance ledger in
[`resource/multimodal-anchor-scouting`](../../base/resources/multimodal-anchor-scouting.md), "Session-130
deeper scout") widened the hunt beyond the in-repo candidates above and **confirms, more strongly, that no
resource clears the four requirements** — the two-axis wall holds across the open-access frontier:

- **Graded same-word sense relatedness exists only *text-only*** (fails (c)): newly assessed **RAW-C /
  SAW-C** (Trott & Bergen — graded same-word relatedness, the *right* construct, IAA 0.79, 112 words / 672
  pairs; license + scale endpoints UNVERIFIED) joins DWUG / Usim / WiC in this class. **SID**
  (SemEval-2017-derived, CC BY) is graded but text-only *and* between-word similarity (the CoSimLex
  disqualifier).
- **Graded *image* signals exist only over the *wrong construct*** (fail (b)-as-construct + (d)):
  **Crisscrossed Captions (CxC)** is graded (0–5) + image-native but rates *whole-caption/scene* similarity,
  no within-word sense structure (THINGS's failure mode on scenes); **PiCS** (CC BY 4.0), **MM-MDS**,
  **Carlson-Image RSA**, and the **Mooney-THINGS** visual-ambiguity set are graded + image but rate
  *object-category* similarity or *perceptual* recognizability, not word sense.
- **Sense-tagged image resources are *binary/categorical*** (fail (b)): **BabelPic**, **VisualSem** (both
  BabelNet non-commercial), **VerSe**, and VWSD itself.

**THINGS-as-scaffolding, worked concretely:** a magnitude set *could* be built in principle (THINGSplus
PD/CC0 images + the human similarity prior as a pre-stratifier), but it is **not tractable within this
project's charter** — the spine (within-word polysemy) must be imported from a text resource (THINGS has
none); THINGSplus gives one image per *concept* not per *sense* (so a two-sense design needs Wikimedia
sourcing anyway, making THINGS's image role marginal); and — the fatal blocker — the indispensable
**per-item graded human *sense*-relatedness labels over images** cannot come from THINGS (wrong construct)
and cannot be produced here, because the project runs **no new human annotation** ([`CLAUDE.md`](../../../CLAUDE.md)
always-on rule 4). Scaffolding cannot be promoted to anchor in-house.

**Sharpened bottom line.** The magnitude (prediction 3) is **untested and, on current open resources,
un-instrumentable** — the only route is an **externally-released** graded-image fine-polysemy set (or an
external build) the project could then *ingest*; an in-house build is out of charter reach. No new typed
`resource` page is warranted for the magnitude question. (Two newly-found candidates are catalog-worthy for
*other* axes if those open: **RAW-C / SAW-C** as a second graded *text-side* lexical-gradience anchor
alongside DWUG — pending license verification; **PiCS / CxC** for a future representational-alignment axis
— never for word-sense relatedness.)

## Status: open (scoping only)

This page runs nothing and ratifies nothing. It states the magnitude question, derives the four
requirements from the VWSD block, assesses the in-repo candidates against them, and names THINGS (as
scaffolding, not anchor) as the one candidate worth a future $0 deeper scout — with the explicit caveat
that the graded sense-relatedness labels and a non-de-referenced, certifiable text channel would still
have to be *built*, not read off any existing resource. Prediction 3 ("narrow headroom for concrete
sense") remains **UNTESTED**.
