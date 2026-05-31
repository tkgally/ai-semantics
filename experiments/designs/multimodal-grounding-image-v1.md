---
type: design
id: multimodal-grounding-image-v1
title: multimodal grounding image probe v1 — does showing the depicting picture move a VLM's graded sense-relatedness behavior TOWARD the WiC binary same/different signal, keyed to where the two senses are visually distinct?
meaning-senses:
  - grounded
  - grounded.perceptual
  - referential.sense
  - distributional
  - human-comparison
status: run
anchor: resource/wordnet-sense-inventory
contingent-on:
  - multimodal-image-anchor
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: operationalizes
    target: conjecture/multimodal-lexical-grounding-divergence
  - rel: depends-on
    target: resource/wic-word-in-context
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/symbol-grounding-problem
  - rel: depends-on
    target: concept/embodied-cognition
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Experiment design v1 — multimodal grounding (the image-input wedge)

> **RECONCILIATION NOTE (2026-05-31, as RUN).** The probe was built, frozen, and run per
> [`experiments/runs/2026-05-31-multimodal-grounding-image-v1/PREREG.md`](../runs/2026-05-31-multimodal-grounding-image-v1/README.md).
> Two things changed from this draft and the **PREREG is authoritative** where they differ:
> (1) **Anchor:** the realized anchor is **WordNet-synset-keyed *constructed* minimal pairs**
> ([`resource/wordnet-sense-inventory`](../../wiki/base/resources/wordnet-sense-inventory.md)), **not**
> WiC — WiC's actual items under-covered clean visually-distinct homonyms (bat/crane/mouse absent as WiC
> nouns). The same/different gold is the author's synset assignment (verified distinct synsets), not a
> per-item human label — weaker than WiC, stated as such. (2) **Scope:** the realized set is **12 pairs /
> 2 strata / 144 calls** (distinct-F homonyms + same-T controls); the §3/§6 "~16 pairs / ~192 calls /
> VWSD-considered / third abstract-F stratum" text below is the *draft* plan — the abstract-F stratum was
> dropped to v2 (abstract senses can't be faithfully depicted). Read §3/§6 as design rationale, the
> PREREG as what ran.
>
> **Status: run.** This document specifies the probe; the orchestrator
> built + froze (sha256) + ran it. It operationalizes **predictions 2–3**
> of [`conjecture/multimodal-lexical-grounding-divergence`](../../wiki/findings/conjectures/multimodal-lexical-grounding-divergence.md)
> — the first probe in the project that actually sends image input to the panel. Prediction 1
> (the $0 text-side Lancaster moderation) already ran as a NULL
> ([`result/lexical-perceptual-grounding-moderation-v1`](../../wiki/findings/results/lexical-perceptual-grounding-moderation-v1.md)),
> which **lowers the prior** on this probe finding an effect — that is the honest backdrop, not a reason not to run.
>
> **Governance.** [`decisions/resolved/multimodal-panel-and-grounding-theory`](../../wiki/decisions/resolved/multimodal-panel-and-grounding-theory.md)
> is **ratified** per Tom's decision-2 this round: **Q1→A** (keep the existing 3-family image-capable
> panel — `anthropic/claude-sonnet-4.6` / `openai/gpt-5.4-mini` / `google/gemini-3.5-flash`),
> **Q2→A** (Lyre gradual-grounding + `grounded.perceptual`; Harnad/Barsalou as sharper foils),
> **Q3→B GO** (open the image probe). `contingent-on` stays set until Tom ratifies the *result*;
> ratifying the anchor fixes the yardstick, not the outcome.

## 0. The one-line claim under test

For a target word used in two sentence contexts, does **adding a small picture depicting each
usage's referent** move the panel's graded sense-relatedness rating **toward the independent human
WiC binary same/different-sense label** — relative to the *same model family's text-only* rating on
the same pair — and is that movement **concentrated in the subset whose two senses have visually
distinct referents** (homonyms like *bat*, *crane*, *seal*, *pitcher*) and **negligible for
visually-non-distinct / abstract pairs**? The text-only condition is the **null to beat**. Two
first-class nulls: **redundancy** (image ≈ text) and **distraction** (image moves *away* from the
human signal).

## 1. Anchor — WiC binary same/different labels (the human signal), image as the manipulation

**Human anchor: WiC (Word-in-Context), Pilehvar & Camacho-Collados 2019** — referenced by the
sibling-created page `resource/wic-word-in-context` (path
`wiki/base/resources/wic-word-in-context.md`, in creation this wave; it will exist after
integration). WiC gives a target word (noun/verb) in two sentence contexts with a **binary** human
label: **T** = same meaning, **F** = different meaning; expert-curated from Wiktionary/WordNet/VerbNet;
released **CC BY-NC 4.0** (per the catalogued WiC facts; see also the verified WiC summary in
[`resource/wic-graded-usage-similarity`](../../wiki/base/resources/wic-graded-usage-similarity.md),
which records the verbatim task wording and the CC BY-NC 4.0 license). WiC's binary label is the
**independent human signal**; this design adds **two depicting images** as the *manipulation*.

**Why WiC, and why this is honest about its scope (anchor-honesty gate):**

- WiC is an **imperfect-but-real existing human resource**, used here exactly per Tom's directive
  option 1 (real human resource, claim scoped accordingly) *and* option 2 (image-paired stimulus set
  keyed to an existing human sense inventory) — the images key onto WiC's own items, so no new human
  sense inventory is invented.
- **The image is a designed variable, not a human judgment.** Whether the two referents "look
  distinct" is set by the design (§3 stratification), not by any annotator. The human anchor is
  WiC's same/different label only. No human label is fabricated.
- **Scope every claim to WiC's BINARY signal**, never to graded DURel correlation. The DV below uses
  a DURel-style *graded* instrument (to stay comparable to the lexical program), but the human anchor
  it is scored against is **binary** — so the confirmable statement is "the image condition's ratings
  separate WiC-T from WiC-F pairs better than text-only," not "the image condition correlates better
  with a graded human relatedness score" (there is no graded human score here).
- **Reuse, not divergence.** WiC is the *same* binary cross-check named for the text-only lexical
  program (lexical-sense-gradience-v1 §6 P5; lexical v3, the sibling subagent's homonymy-enriched
  unit). Using WiC here lets the text-only-vs-image axis integrate with the text-only lexical axis on
  a shared anchor.

**What WiC does NOT supply (and the design must respect):** (i) no graded relatedness (it is binary —
so the headline statistic is a *separation* of two label classes, not a correlation); (ii) no visual
distinctness tag (the §3 stratification adds it as a designed variable); (iii) no images (sourced in
§2); (iv) no reference/extension signal (`referential.sense` only, not `referential.reference`).

**Anchor alternative considered and NOT chosen (surfaced, see Return + §9):** VWSD /
SemEval-2023-Task-1 (Visual Word Sense Disambiguation) is a *genuinely multimodal human-built*
resource — it pairs an ambiguous word + minimal context with a gold image among ~10 candidates. It is
attractive because the human signal is already image-linked. It is **not** chosen as the v1 default
for three reasons: (a) its gold is a *retrieval* answer key (pick the right image), not a
same/different-sense *relatedness* signal, so it does not slot into the project's DURel-style
relatedness instrument without redesign; (b) it tests "can the model pick the depicting image," a
*discriminative/retrieval* behavior, which is exactly the discriminative-vs-generative gap the
conjecture's Notes warn against conflating with the generative panel's relatedness rating; (c) its
image licenses (sourced from web search engines) are a patchwork. It is **recommended as a future
v2 axis** (a genuinely-multimodal human anchor) in the Return, not fabricated into v1. THINGS triplet
data is likewise object-concept similarity, not word-sense, and is logged as a separate-claim anchor
in [`base/resources/multimodal-anchor-scouting.md`](../../wiki/base/resources/multimodal-anchor-scouting.md).

## 2. Image sourcing — the crux (verified reachable this wave)

**Source: Wikimedia Commons API**, `https://commons.wikimedia.org/w/api.php`. Prefer
**Public-Domain / CC0**, then CC-BY/CC-BY-SA with recorded attribution. **Verified end-to-end this
wave** (2026-05-31) with a custom User-Agent `ai-semantics-research/0.1 (tomgally@gmail.com)`:

1. **Search for a depicting image** (namespace 6 = File):
   `action=query&list=search&srnamespace=6&srsearch=<referent terms>&srlimit=N`.
   *Verified:* `srsearch=Pipistrellus bat flying` returned 308,748 hits, top results incl.
   `File:Haeckel Chiroptera.jpg` (snippet shows **"Creative Commons Public Domain Mark 1.0"**) and
   CC-BY-SA 4.0 bat photos — i.e. the search surfaces both PD and CC candidates for the *flying-mammal*
   sense of *bat*, which is what disambiguating that homonym needs.
2. **Retrieve url + license + author + size** for a chosen file:
   `action=query&titles=File:<name>&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=<W>`.
   *Verified:* for `File:Big-eared-townsend-fledermaus.jpg` the API returned
   `LicenseShortName=Public domain`, `License=pd`, `UsageTerms=Public domain`,
   `Artist="PD-USGov, exact author unknown"`, `AttributionRequired=false`, original size 617×375, and
   a `thumburl`. **Fetching that exact `thumburl` returned a valid JPEG** (magic bytes `\xff\xd8`,
   15,034 raw bytes → 20,048 base64 chars at the 330px thumb the API served).

   **Important verified gotcha (must be handled at build time):** `iiurlwidth=256` returned a
   **330px** thumb for this file — Commons rounds the requested width *up* to the next standard thumb
   size available for that file, and the width is file-dependent. **Always fetch the exact
   `thumburl` string the API returns** (do not hand-construct a `NNNpx-` slug — a hand-built
   `200px-…` slug returned an HTML error page in testing). Then **apply a local deterministic
   downscale + recompress** (Pillow: longest side ≤ 256px, JPEG quality ≈ 35–50, strip metadata) so
   the frozen artifact has a *hard, reproducible* size/quality bound regardless of what thumb width
   Commons served. The downscaled file (not the Commons thumb) is what gets sha256-frozen and sent.

**Per-image manifest (frozen before any model call).** For each of the ~24–40 images record:
`item_id`, `target_word`, `wic_context_id`, `sense_gloss`, `commons_file_title`, `source_page_url`
(`https://commons.wikimedia.org/wiki/File:<name>`), `original_thumburl`, `license_short`
(e.g. `Public domain` / `CC0` / `CC BY 4.0` / `CC BY-SA 4.0`), `usage_terms`, `artist`,
`attribution_required`, `orig_w`, `orig_h`, `final_w`, `final_h`, `jpeg_quality`,
`sha256_downscaled`. The manifest + an `ATTRIBUTION.md` (author + license + source URL per image, for
the CC-BY/BY-SA ones) are committed; the small downscaled JPEGs are committed too (PD/CC0/CC-BY all
permit redistribution — this is the cleanest-license image path the project has, unlike the gated
Winoground/Flickr sets dropped in the scouting note). **Freeze rule:** the manifest's
`sha256_downscaled` set is pinned in `PREREG.md` **before** any `call()`; if any image is re-fetched
the sha changes and the run is invalid.

**Alternatives if Commons coverage is thin for a referent:** **THINGSplus** CC0 images (1,854
license-free object concepts) or **Openverse** (`api.openverse.org`, aggregates CC/PD). Commons is the
primary because it was verified reachable + returns machine-readable license metadata in one call;
the others are fallbacks recorded in the manifest's `source` field if used. Do **not** use any image
whose license cannot be read programmatically and recorded.

**Image-token cost control (the gemini driver — see §6):** downscale to ≤256px longest side + low
JPEG quality, send via the harness `images=` path as a `data:image/jpeg;base64,…` data URI with
`detail:"low"` (the `call(..., images=[{"url":dataURI,"detail":"low"}])` shape the harness already
supports). At ~15 KB/image the base64 payload is ~20 KB/image; two images/pair is the per-call image
budget. Prefer the data-URI (frozen local bytes) over a hot Commons URL so the run is reproducible and
not dependent on Commons uptime at call time.

## 3. Items and stratification (frozen with the manifest)

**Target pool:** a small subset of **WiC noun items** with concrete, visually-depictable referents.
Two strata, the prediction-3 moderator (a **designed** variable):

- **VISUALLY-DISTINCT stratum (the discriminating cell).** WiC **F**-labelled (different-sense) pairs
  that are **genuine homonyms whose two senses have visually distinct referents**: *bat* (flying
  mammal vs sports implement), *crane* (bird vs machine), *bank* (river edge vs financial building),
  *seal* (animal vs stamp/wax), *pitcher* (jug vs baseball player), *mouse* (rodent vs computer
  device), etc. Each context gets an image depicting **that context's referent**, so the F-pair is
  shown two visibly different pictures. This is where vision should add the sense-distinguishing
  signal the text under-determines.
- **NON-DISTINCT / control stratum.** (a) WiC **T**-labelled (same-sense) pairs of the same concrete
  nouns — both contexts depict the *same* referent (two pictures that look alike); the image should
  *not* push these apart. (b) WiC **F**-pairs whose two senses are **not** visually distinct
  (abstract or perceptually-similar senses, e.g. metaphorical/extended uses with no contrasting
  depiction). Prediction 3 says the image advantage is **negligible** here.

**Counts (kept deliberately small — see §6):** ~**12–20 word pairs** total, balanced across the
strata (target ≈ 6–8 visually-distinct F-pairs, ≈ 4–6 same-sense T-pairs, ≈ 4–6 non-distinct
F-pairs). Each pair → **2 images** → **~24–40 images**. Each pair is run in **both conditions**
(text-only, image+text) × **~2 instrument framings** (4-pt + 0–100, §4) × **3 models**. Item ids,
WiC source ids, sense glosses, the visual-distinctness label, and the image manifest are all frozen
in `items.csv` + the manifest before any call.

## 4. Conditions, instrument, and DV

**Two conditions, single factor toggled (modality):**

- **TEXT-ONLY** — the two WiC context sentences (target word marked) + the DURel-style graded
  relatedness prompt. Identical to the lexical program's instrument. No image.
- **IMAGE+TEXT** — the *same* sentences + the *same* prompt + the two depicting images attached via
  `images=`. **The prompt text is byte-identical across conditions** so modality is the only toggle
  (no extra wording that could itself shift the rating).

**Instrument (held identical across conditions, reused from the lexical program):** present the two
usages of the target word; elicit a graded sense-relatedness rating on **both** framings — the
**verbatim 4-point DURel scale** (4 Identical / 3 Closely Related / 2 Distantly Related / 1 Unrelated)
and a **0–100** continuous framing — temperature 0, logprob-free greedy parse. (Both framings because
the lexical program repeatedly found framing-specific fragility, esp. gpt-5.4-mini.)

**Dependent variable / reading rule (scoped to WiC's BINARY label):**

- **Primary (prediction 2 — movement toward the human signal).** Per model × framing, compute the
  **separation** between WiC-**F** (different-sense) and WiC-**T** (same-sense) pairs in the model's
  relatedness rating — e.g. ΔR = mean(rating | T) − mean(rating | F), and/or AUC of rating
  discriminating T vs F. Prediction 2 ⇒ **separation is larger in IMAGE+TEXT than in TEXT-ONLY**
  (F-pairs rated *lower / nearer "Unrelated"* once their distinct pictures are shown), i.e. the image
  condition aligns *better* with the binary human label. Report the per-pair paired difference
  (image − text rating) and its sign relative to the WiC label; **report-the-estimate with a CI**
  (cluster bootstrap over word pairs), **no pass bar**.
- **Discriminating (prediction 3 — the moderator).** The image-minus-text improvement in T/F
  separation is **concentrated in the VISUALLY-DISTINCT F-subset** and **≈0 in the non-distinct /
  same-sense strata**. The reportable contrast is Δ(separation gain)_{distinct} −
  Δ(separation gain)_{non-distinct}; prediction 3 ⇒ positive. **This is the load-bearing clause:**
  an *undifferentiated* image effect (prediction 2 alone, uniform across strata) does **not**
  establish grounding — it would read as a generic prompt-perturbation (the falsify-the-shape case).

**The two nulls are first-class (write the null first):**

- **Redundancy null:** image+text ≈ text-only separation within noise → "a fluent text model already
  had the sense distinction from the sentences; the picture is redundant." Given the prediction-1
  NULL already lowered the prior, **this is the most likely outcome and must be reported as a clean,
  informative bound**, not a failure.
- **Distraction null:** image+text separation < text-only, OR F-pairs rated *more* related when shown
  two surface-different pictures (the image dragging the rating toward image surface-similarity rather
  than sense) → image input is not automatically grounding in the meaning-relevant sense (the
  Harnad/Barsalou caveat made concrete).

## 5. Circularity / confound controls

1. **The image must not inject information beyond the sentence (no leakage that isn't grounding).**
   Each image depicts **only** the referent the sentence already names — *bat the mammal* for the
   "the bat flew out of the cave" context, *bat the implement* for "he swung the bat." It adds a
   *perceptual rendering* of what the text already disambiguates, not a new fact. **Guard, discussed
   honestly:** if the picture trivially shows two visibly different objects for an F-pair, a model
   could score "different" from *image surface dissimilarity alone* without any sense computation —
   that is **not** grounding. The design separates these via the prediction-3 moderator (a real
   grounding signal is keyed to sense-distinctness, present in the distinct stratum) AND via the
   **distraction-null / surface-similarity probe** below. A result must keep "the image changed the
   rating in the human direction" separate from "the model is perceptually grounded in the
   theoretical sense" (conjecture Notes).
2. **Surface-image-similarity control (against the distraction null driving the effect).** Include
   **same-sense (WiC-T) pairs** whose two depicting images are themselves *visually different photos
   of the same referent* (e.g. two different river banks). If the model rates these *less* related
   under image+text (driven by photo dissimilarity, not sense), that is surface-similarity
   contamination — detectable as a spurious T-pair separation increase. Report it explicitly.
3. **Instrument identical across conditions** (§4) — modality is the only toggle; the prompt wording,
   scale, temperature, and parse are byte-identical, so any condition difference is attributable to
   the image, not to prompt drift.
4. **Depiction faithfulness is pre-registered + frozen.** Each image's `sense_gloss` ↔ image mapping
   is fixed in the manifest before any call; no image is swapped after seeing model output.
5. **Within-family contrast.** Text-vs-image is compared **within the same model family** (the
   harness sends the same family with/without images), isolating "does grounding change behavior"
   from "does this model differ" — the cleanest design the feasibility note endorsed.

## 6. Pre-flight cost, ceiling, and the liveness micro-ping (do this FIRST)

**Cost drivers (verified facts):** per the feasibility note + the rate card in
[`experiments/lib/openrouter.py`](../lib/openrouter.py) (`RATE_CARD`), `google/gemini-3.5-flash` is
the dominant risk on **two** axes simultaneously — (a) it burns the visible-output budget on
**reasoning tokens** under a small cap (harness defaults google/* to `max_tokens=4096`), and (b) it
bills a **separate per-image-token** line (catalog `img 1.50/Mtok`; Anthropic/OpenAI fold image into
prompt tokens). Every prior probe found gemini billed **~14–15× its rate-card estimate**
(`usage.cost` is the source of truth via `billed_cost()`). **So: keep images ≤256px + `detail:"low"`,
and treat the rate-card number as a floor, not the bill.**

**Order of operations (mandatory):**

1. **Liveness micro-ping FIRST (~$0.001, not a finding).** Send **one tiny synthetic solid-colour
   PNG** (frozen, sha256'd) as a base64 data URI + "What colour is this image?" to all **3 models**
   via the `images=` path. Confirm all three round-trip a sensible answer and that `usage.cost` is
   populated for image calls. This verifies the end-to-end `images=` plumbing the feasibility note
   flagged as *not yet liveness-verified* before any spend on the real set.
2. **Pre-flight estimate on 1 real pair × 3 models × 2 framings × 2 conditions** (~12 calls), read the
   **actual** `billed_cost()`, and extrapolate to the full grid before committing.

**Full-grid size:** ~16 pairs × 2 conditions × 2 framings × 3 models ≈ **~192 calls** (image+text
calls carry ~2 small images each). **Proposed cost ceiling: $3.00** for the full run (hard stop;
abort + report if the pre-flight extrapolation exceeds it). This sits inside the raised **$20/week
soft** budget with wide margin and matches the order of the comparable lexical runs
(lexical-sense-gradience-v1 was $3.13 billed, gemini-reasoning-heavy, text-only — adding small
low-detail images should not multiply that more than ~1.5–2× given the tiny image payloads). If
gemini image-token cost surprises on pre-flight, the fallback is to **drop to the 4-pt framing only**
(halves calls) before dropping models (keeping 3-family decorrelation).

## 7. Indicators frozen, no retuning

The strata, the visual-distinctness labels, the image↔sense mapping, the two framings, the
separation statistic (ΔR / AUC), the prediction-3 moderator contrast, and the two null definitions are
**all frozen in `PREREG.md` before any model-rating quantity is computed**. No threshold is tuned
after the run. A redundancy or distraction null is reported **as the result**, not retuned around
(charter §6). The headline is scoped to WiC's binary label throughout.

## 8. Harness, build/freeze/run pipeline

- Reuses the build→freeze→probe→analyze pattern of the lexical probes. New `build_items.py` selects
  the WiC subset, sources + downscales + sha256-freezes the images (§2), and emits `items.csv` +
  `manifest.json` + `ATTRIBUTION.md`. New `run.py` calls `call(model, system, user, images=…)` for
  the image+text condition and `call(model, system, user)` (no images) for text-only — byte-identical
  prompts. New `analyze.py` computes the per-model × framing T/F separation, the image−text paired
  differences, the prediction-3 moderator contrast, and the cluster-bootstrap CIs.
- `OPENROUTER_API_KEY` from env; temperature 0; `usage:{include:true}` already baked into the harness
  so `billed_cost()` records actual spend.
- **Adversarial pre-run critique** (≥1, independent) and **post-run number-verification** (≥1,
  independent) per PROTOCOL §5, as every finding-bearing probe gets.

## 9. Handoff hooks / open items the orchestrator must resolve before running

1. **WiC fetch + license confirm.** The sibling-created `resource/wic-word-in-context` page must be
   integrated and WiC actually fetched; confirm the **CC BY-NC 4.0** terms permit the analysis use
   (non-commercial research — fine for this project) and that the chosen WiC subset's items carry the
   noun-sense glosses needed for the §3 image mapping. WiC ships sentences + binary labels but **not**
   per-sense glosses for every item — the gloss may need to be read from the WiC item's Wiktionary/
   WordNet source; record provenance.
2. **Image manifest + freeze.** Source ~24–40 images via the verified Commons path (§2), downscale,
   sha256-freeze, write `ATTRIBUTION.md`. **Freeze before any model call.**
3. **Liveness micro-ping** (§6) before the real run.
4. **Surface the sub-decision below to Tom** (recommended — see Return), do not self-resolve it.

**Recommended new sub-decision to surface (do not auto-resolve):** *Is WiC's BINARY label an
adequate human anchor for a graded image-grounding instrument, or should v1 instead use the
genuinely-multimodal VWSD/SemEval-2023-Task-1 human resource?* The design's provisional answer is
**WiC** (real human resource + reuses the lexical-axis anchor + cleanly scoped to a binary
separation), with **VWSD recommended as a v2 axis**. But "binary anchor for a graded DV" and
"constructed image set vs an existing genuinely-multimodal human set" are both value-laden anchor
choices the charter says to surface. This belongs in `wiki/decisions/open/` as a sub-question of
`multimodal-panel-and-grounding-theory` (Q3 follow-on), opened by the orchestrator at integration.
