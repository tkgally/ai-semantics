# PREREG — multimodal-grounding-image-v1 (frozen before any finding-bearing model call)

**Frozen: 2026-05-31.** Operationalizes predictions 2–3 of
`conjecture/multimodal-lexical-grounding-divergence`. Design: `design/multimodal-grounding-image-v1`.
Governance: `decisions/resolved/multimodal-panel-and-grounding-theory` (Q3=B GO) +
`decisions/open/multimodal-image-anchor`. **The headline is scoped throughout to the binary
same/different-sense human signal — there is no graded human score here.**

## Anchor (realized) — DEVIATION from the design's default, surfaced

The design's default anchor was *WiC's* binary labels with a WiC-keyed image set. On building, **WiC's
actual sentence items badly under-cover clean visually-distinct homonyms** (bat/crane/mouse absent as
WiC nouns; most WiC noun-F items use abstract/non-prototypical senses), which would leave the
prediction-3 "visually-distinct" stratum weak. So the realized v1 anchor is **Tom's explicitly
authorized option (b): a small CONSTRUCTED minimal-pair set keyed to an EXISTING human sense
inventory — Princeton WordNet** (Fellbaum 1998; the same inventory WiC itself is built from). Each
item's same/different label = same vs different WordNet noun **synset** (verified via `nltk` WordNet,
synset ids recorded in `items.csv`). WiC remains the anchor for the *text-only* lexical-v3. This
deviation is recorded in `decisions/open/multimodal-image-anchor` and the result page. The human
signal is the WordNet sense distinction (binary); **the image is a designed manipulation, not a human
judgment.**

## Items (12 pairs, frozen in items.csv) — 2 strata

- **distinct-F (6):** visually-distinct homonyms, two DIFFERENT synsets → gold = **different**.
  `bat` (mammal bat.n.01 / club bat.n.05), `crane` (bird crane.n.05 / machine crane.n.04),
  `bank` (river bank.n.01 / financial bank.n.02), `pitcher` (vessel pitcher.n.02 / player pitcher.n.01),
  `mouse` (rodent mouse.n.01 / device mouse.n.04), `seal` (mammal seal.n.09 / stamp seal.n.02).
- **same-T (6):** SAME synset, two contexts + **two DIFFERENT photos** of that referent → gold = **same**.
  `bank`/`crane`/`mouse`/`pitcher`/`seal`/`bat`. This is the **surface-similarity / distraction
  control**: if the image condition rates these *less* related (driven by photo dissimilarity, not
  sense), that is distraction contamination, reported explicitly.

**Scope limit, stated up front:** the purest prediction-3 negative cell — *different-sense but NOT
visually distinct* (abstract F-pairs) — is **deferred to v2**, because abstract senses cannot be
faithfully depicted and attaching a misleading image would violate the depiction-faithfulness gate.
v1 therefore tests prediction 2 (does the image improve T/F separation) + the distraction control
(does it spuriously split same-sense pairs), not the full abstract-F moderator. Honest under-claim.

## Conditions, instrument (frozen)

- **TEXT-ONLY** vs **IMAGE+TEXT**: identical panel, identical instrument; the **user prompt is
  byte-identical** across conditions (see `run.py` FRAMINGS). The only difference is two attached
  images (`images=[{detail:"low"}×2]`) in image+text. A fixed clause in the **system prompt**
  (constant across both conditions) states that *if* images are attached they depict Context 1/2 in
  order — present in both conditions, operative only when images are sent.
- **Instrument (both framings, reused from the lexical program):** DURel 4-pt (4 Identical / 3 Closely
  Related / 2 Distantly Related / 1 Unrelated) **and** a 0–100 scale. Temperature 0, greedy, number
  parsed by first-in-range regex.
- **Panel:** `anthropic/claude-sonnet-4.6` (claude), `openai/gpt-5.4-mini` (gpt),
  `google/gemini-3.5-flash` (gemini). Within-family text-vs-image contrast.
- **Grid:** 12 items × 2 conditions × 2 framings × 3 models = **144 calls** (72 carry 2 images).

## DV / reading rule (frozen, scoped to the BINARY label) — no pass bar, report-the-estimate

- **Primary (prediction 2 — movement toward the human signal).** Per model × framing, the **separation**
  between gold-same (T) and gold-different (F) pairs in the model's relatedness rating:
  `ΔR = mean(rating | same) − mean(rating | different)` (and AUC of rating discriminating same vs
  different). Prediction 2 ⇒ **ΔR larger in IMAGE+TEXT than TEXT-ONLY** (F-pairs pushed toward
  "Unrelated" once their distinct pictures are shown). Report the per-item paired image−text rating
  difference, by stratum, with a **cluster bootstrap CI over the 12 items**. (0–100 ratings used as is;
  4-pt mapped to its own scale; the two framings reported separately.)
- **Distraction control (the surface-similarity guard, load-bearing here).** In the **same-T** stratum
  (two different photos of the same referent), the image condition should **not** lower the relatedness
  rating. If it does (T-pairs rated less related under image), that is photo-dissimilarity contamination
  — reported as the distraction null, not suppressed.
- **Nulls, first-class (write the null):** **Redundancy** (image ≈ text separation within the bootstrap
  CI → "the text already carried the sense distinction"; the most likely outcome given the prediction-1
  null) and **Distraction** (image moves *away* / splits same-sense pairs). Either is reported AS the
  result; no indicator is retuned after seeing ratings.

## Frozen artifacts — sha256 (computed before any finding-bearing call)

`items.csv` (12 items), `manifest.json` (24 images + source/license), `ATTRIBUTION.md`. Images
downscaled locally (≤256px, JPEG q40) from Wikimedia Commons PD/CC0/CC-BY(-SA); per-image source +
license in `manifest.json`/`ATTRIBUTION.md`.

```
024b3a47…  crane-F_1.jpg      03f3236b…  pitcher-T_1.jpg    08ea4c89…  seal-T_1.jpg
0ffe7816…  bank-F_1.jpg       1ccd328d…  crane-T_2.jpg      2547fdcb…  bank-F_2.jpg
36e48f32…  bat-F_2.jpg        476ef165…  pitcher-T_2.jpg    61534a5f…  pitcher-F_2.jpg
69df63b7…  bat-T_2.jpg        6bb379b6…  bank-T_2.jpg       76c557b2…  pitcher-F_1.jpg
776602a9…  seal-F_1.jpg       7c929010…  crane-F_2.jpg      89776dbf…  bat-T_1.jpg
8c329071…  bank-T_1.jpg       9abfae35…  mouse-T_2.jpg      a5133616…  crane-T_1.jpg
ba939051…  mouse-F_1.jpg      bb613556…  mouse-T_1.jpg      bff13629…  mouse-F_2.jpg
c49ed3fd…  seal-F_2.jpg       ebb2e014…  seal-T_2.jpg       eff1c9c1…  bat-F_1.jpg
b4fb9839…  _liveness_red.png (synthetic, liveness only — not a finding)
```
(Full 64-hex digests via `sha256sum images/*.jpg` reproduce these prefixes.)

## Order of operations (mandatory)

1. **Liveness micro-ping** (`run.py liveness`) — synthetic red square + "what colour?" × 3 models;
   confirm the `images=` path round-trips and `usage.cost` populates. Not a finding.
2. **Independent adversarial pre-run critique** over the frozen stimuli + this PREREG; apply
   BLOCKER/SHOULD-FIX fixes and **re-freeze** before any grid call.
3. **Pre-flight** (`run.py preflight`) — 1 item, read billed cost, extrapolate (ceiling **$3.00**).
4. **Full grid** (`run.py full`) → `raw/results.json`.
5. **Independent post-run number-verification** before the result page is promoted.
