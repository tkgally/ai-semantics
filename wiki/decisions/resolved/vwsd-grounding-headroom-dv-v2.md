---
id: vwsd-grounding-headroom-dv-v2
title: What is the v2 NON-CAPTION text baseline for the VWSD grounding-headroom probe, given that v1's gemini-authored candidate captions named the referent and so contaminated the per-item separability covariate the gating interaction reads?
status: resolved
opened: 2026-06-25
opened-by: autonomous (session 104, surfacing the VWSD v2 non-caption-baseline gate)
resolved: 2026-06-25
resolved-by: autonomous (adversarial review)
resolution: adopt-default (Q1 Option B sense-neutral visual-form descriptor as the separability baseline + Option-A chance-floor calibration arm + Option-C leakage-audit covariate; Q2 stratified draw clearing a re-stated per-stratum floor with the covariate frozen per-model pre-image and day-split if over cap; Q3 v1 narrow human-anchored posture unchanged; binding pre-spend conditions a–f including new (d) raised claude image-arm max_tokens — all as written)
anchor: human-anchored (VWSD gold-test selection accuracy; binary, not graded — scoped to the gating shape, NOT prediction-1-as-written, NOT reference)
contingent-artifacts:
  - conjecture/distributional-saturation-grounding-headroom
  - design/vwsd-grounding-headroom-v2
  - result/vwsd-grounding-headroom-v2
---

> **Status: RESOLVED (2026-06-25, session 105, autonomous adversarial review — cross-session: opened
> by session 104 on 2026-06-25, ratified by session 105; the session boundary held). VERDICT:
> ADOPT-DEFAULT.** An independent fresh-agent reviewer (not the orchestrator doing this session's
> downstream work) ratified the page's provisional defaults **as written** — **Q1 Option B** (a
> sense-neutral visual-form candidate descriptor as the separability baseline, paired with **Option A**
> as a mandatory chance-floor calibration arm and **Option C**'s leakage score carried as a reported
> audit covariate on the Option-B descriptors), **Q2** (a stratified draw clearing a re-stated
> per-stratum floor, the separability covariate frozen per-model to a checksummed file before any image
> arm, authoring + arms day-split across UTC if the preflight exceeds the $5/day cap), **Q3** (the v1
> narrow human-anchored posture unchanged — selection accuracy vs human gold, gating-shape-only,
> explicitly **not** prediction-1-as-written and **not** reference, all four VWSD resource caveats
> carried forward), and **binding pre-spend conditions (a)–(f)** including new condition **(d)** (raise
> the claude image-arm `max_tokens` to remove the v1 reasoning-then-truncation bias). No yardstick
> modification was required.
>
> **Quote-integrity PASS.** The reviewer verified char-for-char that the three v1-Limitation quotes
> this page reproduces (caption-leakage contamination; floor-not-met/underpowered; 6 claude
> parse-fails) match [`result/vwsd-grounding-headroom-v1`](../../findings/results/vwsd-grounding-headroom-v1.md)
> exactly (the third honestly elided with "…", the cut not load-bearing), and confirmed v1's own frozen
> numbers (caption-text accuracy .86–.88; sep=1.0 for 40/50 items; only 7 under-determined, below the
> floor of 8) genuinely support the **caption-saturation + separability-contamination** claim — it is
> v1's own first-class Limitation, not an inflation.
>
> **Anti-cheat PASS.** Option B is chosen on **yardstick** grounds — it is the only baseline whose
> covariate measures the conjecture's actual target (linguistic under-determination) with a *per-item
> gradient* (Option A floors at chance and cannot rank items; Option C models rather than removes the
> confound) — and **not** because it makes any probe result likelier; the page's structure makes a
> *spurious positive harder*, which is the correct direction. Conditions (b) freeze-before-image, (c)
> distraction-null-reported-first, (e) fresh pre-run-critic GO/NO-GO (a NO-GO defers, never relaxes),
> and the "no lift counts as headroom unless it survives the distraction control" rule close the
> retuning, distraction-confound, truncation-bias, and budget surfaces. The page correctly forbids
> running or re-tuning the baseline in the ratifying session, and the reviewer attested the verdict is
> motivated by yardstick-correctness, not by wanting any particular result.
>
> **Contingent-artifact disposition.** [`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md)
> stays **`proposed`** — ratifying fixes the *yardstick*, never the *result*; the conjecture remains
> untested. The two `*-v2` artifacts — `design/vwsd-grounding-headroom-v2` and
> `result/vwsd-grounding-headroom-v2` — **still do not exist**: a build session is now **cleared to
> author** `design/vwsd-grounding-headroom-v2` under this resolved gate (Option-B descriptors +
> leak-audit frozen and checksummed; the Option-A floor arm; the stratified draw clearing the
> per-stratum floor; the per-model covariate frozen pre-image; raised claude `max_tokens`), but
> `result/vwsd-grounding-headroom-v2` is **NOT cleared** until the design is frozen, the EN test images
> fetched + checksummed (kept out of git), a **fresh independent pre-run critic returns GO**, and a
> pre-flight budget estimate (subsampled and/or UTC-day-split) clears the $5/day cap. **The probe must
> not be run, nor the non-caption baseline re-derived, in the session that ratified (it was not — no
> probe ran, no spend this session).** Logged in [`log.md`](../../../log.md).
>
> *The text below is the page as opened by session 104, preserved verbatim as the record of the
> options, provisional defaults, and binding conditions the verdict adopts.*
>
> ---
>
> The v1 result it responds to,
> [`result/vwsd-grounding-headroom-v1`](../../findings/results/vwsd-grounding-headroom-v1.md), **did
> run** (session 100) and returned **neither-confirms-nor-falsifies**. This v2 decision is a
> **re-operationalization**, not a re-run: it changes what the separability covariate *means*, so the
> prior decision [`decisions/resolved/vwsd-grounding-headroom-dv`](vwsd-grounding-headroom-dv.md)
> (which fixed the v1 DV) is not enough — a fresh baseline decision was required before any v2 spend.

# Decision: the v2 non-caption text baseline for a VWSD grounding-headroom probe

## Why this exists

The v1 probe **ran** and returned a clean but inconclusive result: it **neither confirms nor
falsifies** the grounding-headroom gating prediction on VWSD. Three v1 limitations drive the need for
a v2, and the first is value-laden — it cannot be auto-resolved.

**Limitation 1 — caption-leakage contamination of the separability covariate (the deepest limit).**
The whole gating geometry is read off a per-item *text-only separability* covariate; v1 computed that
covariate from gemini-authored candidate **captions**, and those captions name the referent. Verbatim
from [`result/vwsd-grounding-headroom-v1`](../../findings/results/vwsd-grounding-headroom-v1.md)
(Limitations, item 1):

> "**Caption-leakage contamination of the separability covariate (the deepest limit, per the
> critic).** The text-only baseline is *"can the model pick gold from a **caption** of each
> candidate,"* and the gemini captions are concrete noun phrases that frequently **name the referent**
> ("a pile of mustard seeds"). So `sep_i` conflates "the target word + phrase determines the sense"
> with "the gold image's caption is descriptive enough to match." The conjecture targets the former;
> the instrument measures a blend. The high caption-text accuracy is therefore **not** clean evidence
> that *language* determines the sense — and the whole gating geometry is only weakly identified even
> setting N aside. This is co-equal with the floor failure."

The consequence was structural: the caption baseline **saturated**, which suppressed the very
interaction the probe exists to read. Verbatim from the same page (Limitations, item 2):

> "**Floor not met / underpowered.** N=50, only 7 under-determined items, ~16 text-failed cells. The
> binned interaction is suppressed and the rescue read is descriptive. A larger, stratified draw (or a
> non-caption text baseline) is needed to test the gating shape."

And the mechanical loss that biased the image arm, verbatim (Limitations, item 3):

> "**6 image parse-fails, all claude, on rare-phrasing items** (retard, amit, bovid bag, sea steamer,
> clocks weed, sharp crease) — claude reasoned aloud and was truncated at `max_tokens=16` before
> emitting a number. ... (a v2 should raise `max_tokens` for claude)."

So the central v2 question is **not** "re-run with more items." It is: **what text do you actually
show the model so that "text separability" measures *linguistic* under-determination — the thing the
conjecture's gating clause is about — rather than caption informativeness?** This is a genuine
operationalization fork: each candidate baseline changes what the covariate means and therefore what
the whole gating interaction tests. That fork is value-laden and is the core this page surfaces; it
**may not be auto-resolved**, and the v1 DV decision does not cover it (v1's baseline was the caption
baseline now shown to be confounded).

The conjecture's own anchor caveats make the stakes explicit — the stratifier must be a *measured,
pre-frozen, per-model covariate*, from
[`conjecture/distributional-saturation-grounding-headroom`](../../findings/conjectures/distributional-saturation-grounding-headroom.md)
(Anchor caveats):

> "Text-only baseline separability is a *measured covariate*, not a human label. ... the covariate
> must be computed and frozen *before* the image condition is run, on pain of retuning the indicator
> after seeing results (the operationalization gate the protocol forbids)."

A confounded covariate, frozen perfectly, is still a confounded covariate. v2 has to fix *what is
measured*, not just *when it is frozen* — which is why this is a fresh value-laden decision, not a
mechanical patch.

## The sub-questions

### Q1 — What is the non-caption text baseline? (the value-laden core)

The covariate must read **linguistic under-determination**: how far the target word + the VWSD trigger
word(s) — the genuine minimal linguistic context VWSD supplies — fix the sense, *independent of* how
richly any candidate is described in words. The fork is in how the candidates are presented in the
text-only condition.

- **Option A — minimal linguistic context, candidates as bare index labels (no descriptive text at
  all).** Show the model only the target word + the trigger word(s) VWSD provides, with the ten
  candidates replaced by neutral *index labels only* ("image 1 … image 10") and **no caption**. The DV
  in the text-only condition is then degenerate by construction — with no candidate description and no
  image, there is nothing for the model to match the linguistic context against. **This option does
  not yield a usable per-candidate text baseline at all**, so it cannot be the separability covariate
  as v1 framed it; its honest role is a *floor calibration* (it should sit at/near chance, confirming
  the linguistic context alone cannot pick gold without *some* candidate signal). **Risk flags:** (i)
  it measures the wrong thing for stratification — it tells you the task is under-determined *globally*
  but gives no *per-item* separability gradient, which is exactly what the interaction needs; (ii) it
  floors accuracy near chance and so cannot rank items. Honest verdict: Option A as a *separability
  covariate* is a non-starter; it is retained only as a calibration arm, not the baseline.

- **Option B — a deliberately sense-neutral candidate descriptor that names visual form WITHOUT
  naming the referent concept.** Author (or machine-generate then human/critic-filter) a candidate
  descriptor that describes *visual form only* — shapes, colors, layout — and is barred from naming
  the depicted concept ("a cluster of small round yellowish particles" rather than "a pile of mustard
  seeds"). Under this baseline, a model that picks gold must do so by mapping the *linguistic context*
  onto *visual form*, not by string-matching the referent name — so `sep_i` would track linguistic
  under-determination rather than caption informativeness. **Risk flags (stated as honestly as v1's
  Q1):** (i) **authoring it is itself value-laden and leak-prone** — the line between "names the
  visual form" and "names the referent" is fuzzy ("a pile of small seeds" already half-names it), and
  every authoring choice could re-introduce the confound it is meant to remove; (ii) the descriptor
  generator is a model, so the confound could be *displaced* (into how aggressively the generator
  abstracts away identity) rather than removed; (iii) it requires a **pre-registered, checksummed
  leak-audit** (e.g. a held-out check that the descriptor does not let a referent-name classifier
  recover the gold) before it can be trusted, and that audit is itself an operationalization choice a
  later session must ratify. This is the highest-fidelity option *if* the leak-audit can be made
  credible, and the costliest to get right.

- **Option C — keep a caption baseline but *control* it: measure per-item caption-referent-naming
  leakage as a covariate and regress it out.** Keep v1's caption baseline, but add a measured
  *leakage* score per item (how strongly the caption names the referent) and report the gating
  interaction **conditioned on / residualized against** that leakage covariate. **Risk flags:** (i)
  **same circularity risk** — if leakage and true linguistic separability are themselves correlated
  (they plausibly are: items whose sense is easy to name in a caption may also be easy to fix from
  context), regressing one out partly removes the other, biasing the interaction toward null; (ii) the
  leakage score is another model-derived construct needing its own validation; (iii) it does not
  *remove* the confound, it *models* it, so the result inherits all the modeling assumptions. It is
  the least disruptive to the v1 pipeline and the least clean.

**Provisional default for Q1 (calibrated, not surveyed):** **Option B** — the sense-neutral
visual-form descriptor — **as the separability baseline**, paired with **Option A as a mandatory
floor-calibration arm** (it must sit at chance to confirm the linguistic context alone does not leak),
**and Option C's leakage score carried as a reported audit covariate** on the Option-B descriptors
(not as the baseline, but as the mechanical check that Option B did not re-leak). The default is B
because it is the only option whose covariate actually measures the conjecture's target (linguistic
under-determination), and the only one that can clear the floor with a *per-item gradient*; A cannot
rank items and C inherits the confound it tries to model. The default is provisional precisely because
**Option B's leak-audit is itself unratified** — a later session may judge the descriptor un-authorable
without leakage and fall back to C-with-explicit-circularity-caveat, or declare the gate un-closable on
VWSD and reserve it (as v1's scope note already reserves prediction-1-as-written) for a future
graded-image resource. No position here binds that judgment.

### Q2 — Stratification + N under the chosen baseline

The baseline in Q1 changes the separability distribution, so the stratified draw must be specified
*after* Q1 is fixed, not before. Carrying v1's binding mods forward
([`decisions/resolved/vwsd-grounding-headroom-dv`](vwsd-grounding-headroom-dv.md), mods 1
and 2):

- **Stratified draw from the 463 EN gold so both strata clear a stated floor.** v1's failure mode was
  exactly that the saturated baseline left only 7 under-determined items, below the floor of 8 (v1
  result, §3). Under a non-caption baseline the saturation should fall, but v2 must not *assume* it
  does: the design must draw a **stratified** sample (over-sampling the predicted under-determined
  band) so the under-determined and saturated strata **each hold ≥ a stated minimum number of EN gold
  items**, with the separability distribution reported, before the interaction is credited (carry mod
  1's numeric-floor discipline forward, re-set for the new baseline).
- **Per-model, frozen pre-image covariate.** The separability covariate is computed **per model, per
  item, and written to a frozen checksummed file before any image condition runs** (carry mod 2
  forward verbatim in force) — "no retuning" stays mechanically auditable. Under Option B this
  *additionally* means the descriptor set and the leakage-audit scores are frozen and checksummed
  before any image arm.
- **Budget-realism subsampling / UTC splitting (charter §8).** v1 was deliberately **budget-bounded to
  a 50-item seeded subset** because a full-EN-set caption/descriptor pass over the candidate images
  did not fit the $5/day cap (the v1 session's handoff note records the full-set caption preflight at
  roughly $7, over cap; that exact figure is a session-100 estimate, not a committed audit number).
  A v2 descriptor-authoring pass over the full set would carry a comparable cost. So a full-N v2 must
  **subsample smartly** (a stratified draw, not the full 463) **or split the authoring + arms across
  UTC days** to stay under the daily cap. This budget constraint interacts with the floor: the draw
  must be large enough to clear both strata's floors *and* small enough (or day-split enough) to fit
  the budget. This is a realism constraint, **not a finding**.

**Provisional default for Q2:** a **stratified draw** sized to clear a re-stated per-stratum floor
(set in the frozen design, certified non-degenerate by the pre-run critic), with the covariate frozen
per-model pre-image, and authoring + arms **day-split across UTC** if the preflight exceeds the cap.
Provisional; a later session sets the exact floor and N once Q1's baseline is fixed.

### Q3 — Anchor posture and honest scope

v2 carries the **same narrow human-anchored posture** v1 ratified
([`decisions/resolved/vwsd-grounding-headroom-dv`](vwsd-grounding-headroom-dv.md), Q3); no
widening:

- **What it establishes:** image-conditioned *selection accuracy* against the human-curated gold image
  (the 463 EN gold-test items; trial 16), in a by-construction text-under-determining task, read as
  the gating **interaction** between per-item (non-caption) separability and image-induced selection
  improvement. **Explicitly NOT prediction-1-as-written** (no graded human relatedness gradient — VWSD
  gold is binary); **NOT reference** (`referential.externalist` untouched).
- **Caveats carried forward verbatim in force**, all from
  [`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md): **binary gold** (no graded
  signal); **limited annotator independence** (English annotators "includ[ed] the authors of this
  paper"; BabelNet-automatic seed; **no inter-annotator agreement reported**); **image redistribution
  unconfirmed** (images stay out of git, fetch-at-runtime only); **anchored only to the gold
  test/trial split** (the 12,869 training instances are silver).

**Provisional default for Q3:** identical narrow posture as v1 — selection accuracy vs human gold,
gating-shape-only, not prediction-1-as-written, not reference; all four VWSD resource caveats carried
forward.

## Provisional default (to be adopted, modified, or rejected by a later session)

- **Q1:** Option B (sense-neutral visual-form candidate descriptor) as the separability baseline, with
  Option A as a mandatory chance-floor calibration arm and Option C's leakage score carried as a
  reported audit covariate on the B descriptors — chosen because B is the only baseline whose covariate
  measures the conjecture's actual target (linguistic under-determination) with a per-item gradient,
  contingent on a credible pre-registered leak-audit.
- **Q2:** a stratified draw from the 463 EN gold sized to clear a re-stated per-stratum floor under the
  Q1 baseline, covariate frozen per-model pre-image, authoring + arms day-split across UTC if the
  preflight exceeds the $5/day cap.
- **Q3:** the v1 narrow human-anchored posture unchanged — selection accuracy vs human gold,
  gating-shape-only, not prediction-1-as-written, not reference, all four VWSD caveats carried forward.

Adopting this default **fixes the yardstick** (which non-caption baseline, which leak-audit, which
strata, which floor, which anchor posture) and **never any result**. It must not be read as a finding
that grounding helps in the residual, nor that a non-caption baseline will fail to saturate — only as
the cleanest VWSD re-operationalization of the conjecture's testable gating structure. This default is
**provisional and ratifiable only by a later session**.

## Binding pre-spend conditions (all must hold before any model call)

Mirroring v1's (a)–(e)
([`decisions/resolved/vwsd-grounding-headroom-dv`](vwsd-grounding-headroom-dv.md)), with
one new condition (d) from v1 Limitation 3:

(a) **Fetch + checksum, images out of git.** The resized EN test images are fetched at runtime,
checksummed, and **kept out of git** — image redistribution is unconfirmed
([`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md), License & redistribution),
so **fetch-at-runtime only, no re-hosting**. Anchor **only** to the gold test/trial split; the
training split is silver and is not an anchor.

(b) **Prereg the DV + the non-caption baseline, frozen to a checksummed file before any image
condition.** The DV (selection-accuracy interaction vs per-item *non-caption* separability), the
chosen non-caption baseline procedure (Q1), the candidate descriptors and their leakage-audit scores,
the stratification and per-stratum floor (Q2), and the analysis ordering (interaction is the test of
record; a bare main-effect lift is descriptive only) are written into
`design/vwsd-grounding-headroom-v2` and **frozen**. The per-model, per-item separability covariate is
written to a **frozen, checksummed file before any image condition runs** — no retuning after seeing
image results; the non-caption baseline, once frozen, is **not re-derived** after image results land.

(c) **Distraction control built in and reported first.** The design carries the **same-referent /
surface-dissimilarity (word-ablated) distraction control** v1 built and the conjecture/resource both
require, and reports the distraction null **before** the interaction is credited; a positive accuracy
lift that does not survive the control is the **distraction null, not headroom**.

(d) **Raise the claude image-arm `max_tokens`** (new, from v1 Limitation 3 — 6 image parse-fails, all
claude, from reasoning-then-truncation at `max_tokens=16`). The v2 design must set the claude image-arm
`max_tokens` high enough that reasoning-then-answer is not truncated before a parseable selection is
emitted, removing the v1 bias (dropped hard items overstated claude image accuracy and understated the
rescue-cell count). This is a build condition, not a sub-question.

(e) **Fresh independent pre-run critic GO/NO-GO.** Before any spend, an independent critic certifies,
against the **frozen** design, that the non-caption baseline honestly measures linguistic
under-determination (not re-leaking the referent name), that the leak-audit is credible, that the
strata clear their floors and are non-degenerate, and that no surface-dissimilarity-only reader beats
the interaction — **GO/NO-GO**. A **NO-GO defers the run and never relaxes any condition.**

(f) **Pre-flight budget estimate** (charter §8) recorded in [`config/budget.md`](../../../config/budget.md)
before the run; actual recorded after. The estimate must show the chosen draw + descriptor-authoring +
three arms fit the $5/day cap (subsampled and/or UTC-day-split per Q2).

## Anti-cheat note

Ratifying this decision fixes the **yardstick** (which non-caption baseline, which leak-audit, which
strata and floor, which anchor posture and scope), **never the result**. The probe must **not** be run,
nor the DV / non-caption baseline re-tuned, in the session that ratifies. The non-caption separability
baseline, **once frozen, is not re-derived after seeing image results** — its commitment to a
checksummed file is what makes "no retuning" auditable. A pre-run-critic **NO-GO defers the run, never
relaxes a condition** (and may legitimately conclude the non-caption baseline is un-authorable without
leakage on VWSD, deferring the gate to a future graded-image resource). And **no accuracy lift counts
as headroom unless it survives the distraction control** — surface dissimilarity reproduces a positive
with zero sense computation. A flat (null) interaction remains *"no detectable gating OR
underpowered,"* never proven absence of headroom.
