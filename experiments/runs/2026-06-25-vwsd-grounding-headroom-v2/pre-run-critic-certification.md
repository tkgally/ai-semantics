# Pre-run critic certification (condition e) — session 108

**VERDICT: GO-WITH-CONDITIONS** — the day-1 text-only freeze is sound, every day-1 number
reproduces exactly, the freeze is genuinely pre-image; the run is authorized for the next
fresh-UTC-day execution session **subject to the three binding conditions in §Binding conditions
below** (gemini floor elevation as a first-class per-model caveat; the 0-intermediate-band gap
foregrounded; DISTRACT null reported and credited first). This is a fresh, independent review — I
did not build this experiment. **A GO does not authorize spend today** (UTC 2026-06-25 has ≈$0.28
headroom remaining); it authorizes the next fresh-UTC-day execution session.

I ran only the offline `analyze.py` and checksum/JSON tools. I made **no** model/API call and
**spent nothing**.

---

## Independent reproduction (offline)

I confirmed by inspection that `analyze.py` imports only `json`, `os`, `collections` — no network,
no API. Re-running `python3 analyze.py` regenerates the README's "Day-1 RESULTS" block **exactly**:

- TEXT (descriptor) accuracy: claude **0.750** (90/120) / gpt **0.725** (87/120) / gemini **0.808**
  (97/120). MATCH.
- `sep_i` distribution `{0: 16, 1/3: 19, 1: 85}` → under-determined (sep≤1/3) = **35**, intermediate
  (2/3) = **0**, saturated (sep=1) = **85**. MATCH. Both reported bins clear ≥15.
- Option-A FLOOR: pooled **0.122** Wilson[0.092, 0.160]; claude **0.092** Wilson[0.052,0.157] /
  gpt **0.117** Wilson[0.071,0.186] / gemini **0.158** Wilson[0.104, 0.234]. MATCH.
- Leak distribution **154 / 20 / 26** (n=200), high-leak rate **0.130**;
  Spearman(leak_i, sep_i) over the 120 = **0.160**. MATCH.
- Parse integrity: text 360 calls / 0 fails; floor 360 calls / 0 fails. (Condition d's truncation
  worry did not bite the text-only arms; it remains live only for the not-yet-run claude IMAGE arm.)

**Every finding-bearing number reproduces from the committed raw JSON.** No discrepancy.

---

## Checksum investigation (condition 2 — covariate genuinely pre-frozen)

`sha256sum frozen/descriptors.json frozen/run_items.json raw/text.json`:

- `run_items.json` = `7f9e52fa…` — **MATCHES** NEXT.md / log.md. ✓
- `raw/text.json` = `3a9dfcbf…` — **MATCHES** NEXT.md / log.md. ✓
- `frozen/descriptors.json` = `26616a55…` — does **NOT** match the `afe74f82…` recorded in
  NEXT.md / log.md.

**Finding: the freeze is SOUND; the recorded `afe74f82…` is a stale pre-leak snapshot, not
tampering.** I verified this three ways:

1. **log.md line 179 (s107)** records `frozen/descriptors.json sha afe74f82…` at the moment
   `descriptor-full` finished, and *then* describes running `leak-full`, which "adds leak{} to
   frozen/descriptors.json." So the recorded sha is the descriptor-only file; the leak audit ran
   afterward and re-wrote the file.
2. **run.py** confirms the mechanism: `descriptor-full` freezes `{policy, generator, descriptors,
   leak:{}}` (the `load_desc` default seeds `leak:{}`; the descriptor pass never populates it).
   `leak-full` then loads that object, **only writes into `desc["leak"][...]`** (the descriptor
   text in `desc["descriptors"]` is never touched), and re-freezes. So `leak-full` is purely
   additive to the load-bearing descriptor phrases.
3. **Decisive reconstruction (my own check):** I rebuilt the descriptor-only object
   `{policy, generator, descriptors, leak:{}}` from the current committed file and hashed it with
   the same `json.dumps(..., indent=2, sort_keys=True)` the freeze uses. It hashes to
   **`afe74f82f506e8cc11208e7ebd9a22fda11a9ca1612dea5c2b5bb2b081123fd7`** — i.e. the recorded
   `afe74f82…` **exactly**. This proves the 1889 descriptor phrases are **byte-identical** to what
   was frozen before the leak step, and that `26616a55…` is simply that same descriptor set **plus**
   the 200-entry `leak{}` field.

Both the descriptor authoring and the leak audit are **TEXT-ONLY** and ran **before any image arm**
(no `raw/image.json` / `raw/distract.json` exist). The freeze of the load-bearing covariate is
genuinely pre-image. **Recommendation for the execution session (not a blocker): update the recorded
sha in NEXT.md/log.md to the post-leak `26616a55…`, or record both, so the committed checksum matches
the committed file.** This is a bookkeeping nit, not a freeze defect.

---

## Descriptor inspection (independent spot-check)

I read the descriptors directly, including all 26 high-leak (score-2) items and a sample of score-0
and score-1 items.

- **The v1 failure mode is genuinely fixed.** v1's canonical leak ("a pile of mustard seeds") now
  reads "a dense cluster of small round yellowish and dark brown particles," and the held-out gpt
  recovers "mixed spices" — scored **0 (no leak)**. The B.1 visual-form policy is being honored:
  descriptors name shape/colour/layout, not the referent noun.
- **Of the 26 high-leak items, only 3** ("card", "field", "blue") literally contain the target word
  string in the descriptor text — and those are mild (e.g. "a rectangular off-white **card** with
  fine black cursive script"; "blue-green veins" → gpt infers "blue cheese"). The descriptor
  generator largely held the no-naming line.
- **The other 23 high-leak items are NOT textual referent-naming.** They are cases where the
  descriptor honestly names visual form but the form is **intrinsically near-diagnostic** — e.g.
  cardamom's "pale green, ribbed, oval pods … split open to reveal … reddish-brown angular elements"
  lets gpt recover "cardamom pods" from shape alone; Neptune's "large, smooth blue sphere with faint
  white horizontal streaks." This is the residual the design's B.2 honesty note and the resource's
  own "mustard seeds, whose visual form is itself near-diagnostic" caveat anticipate.

**My own view:** because the deterministic `leak_i` scorer counts *any* recovery of the target word
as high-leak — including recovery from a clean descriptor of a visually-diagnostic form — the 13%
figure is, if anything, a **conservative over-estimate** of textual referent-naming. The genuine
text-leak rate (descriptor literally names the referent) is ~3/200 in this sample. The audit
honestly characterizes the residual; it does not flatter the descriptors.

---

## The five condition-(e) checks

### (1) Does Option-B honestly measure under-determination and NOT re-leak the referent? — **PASS**

The leak audit is credible (see descriptor inspection). The descriptors name form, not referent; the
v1 caption-leak is removed. `leak_i` high-leak rate **0.130** is acceptably low, and most of it is
visually-diagnostic form rather than textual naming. The TEXT arm is **not saturated** (.725–.808 vs
v1's .86–.88), which is the whole point of v2 — it leaves real text-failed headroom for the image arm
to act on. Spearman(leak_i, sep_i) = **0.160** is **weak** (well below the 0.4 "strong → residual-
contamination warning" threshold and even below the 0.25 "moderate" band), so regressing leak out
would not gut sep, and the Option-C circularity warning does **not** fire. leak_i is carried as a
reported covariate, not the baseline, exactly as designed. *(Caveat the execution session must keep:
the leak-audit's own validity is a later-session ratification per design B.4; carrying it as a
reported covariate — never regressing it out — honors that.)*

### (2) Is the covariate genuinely pre-frozen? — **PASS**

See the checksum investigation. Descriptors + leak_i + the TEXT covariate (`raw/text.json`,
`frozen/run_items.json`) are all checksummed and committed, and **no image/distract raw file exists**.
The `descriptors.json` sha discrepancy is a stale pre-leak record, not tampering — proven by exact
reconstruction of `afe74f82…`. The freeze is sound and pre-image.

### (3) Do the strata clear ≥15 and are they non-degenerate? — **PASS WITH A FOREGROUNDED GAP**

Under-determined **35 ≥ 15** and saturated **85 ≥ 15** both clear the floor (v1 failed at 7<8), so
the **binned interaction is creditable** next session. However, the seeded fill-saturated-first draw
left **0 intermediate (2/3) items**, so the continuous `sep_i` companion has a genuine **gap at 2/3**
(the distribution is `{0:16, 1/3:19, 1:85}` — there are also no 2/3 items in the pool draw because
the binned floor was filled saturated-first). I weighed whether a critic should demand an intermediate
band and DEFER:

- The **test of record is the binned image-rescue contrast** (text-failed vs text-succeeded cells),
  which depends only on the two clearing bins, not on a populated 2/3 band. The binned read is
  creditable.
- The **continuous Spearman/OLS slope is explicitly a descriptive companion only** (mechanical-ceiling
  caveat), so the 2/3 gap weakens a read that is already non-load-bearing.
- The draw rule was **fixed before the covariate was scored** (`draw_stratified.py`, seed 20260625),
  so the empty 2/3 band is a property of the frozen rule, **not** post-hoc retuning.

I therefore do **not** rule this a DEFER, but the gap is a real limitation: the gating *shape* is
read across a **bimodal** sep distribution (under-determined vs saturated, nothing between), so the
result cannot speak to a *graded* sep→rescue trend, only to the two-bin contrast. This must be
foregrounded (binding condition 2 below). It is consistent with — and does not exceed — the design's
"strata view" + "mechanical-ceiling" framing.

### (4) Does the Option-A floor arm sit at/near chance? — **THE LIVE QUESTION; PASS WITH A BINDING CAVEAT (not NO-GO)**

Pooled **0.122** Wilson[0.092, 0.160] includes 0.10. claude **0.092** clean; gpt **0.117** near-clean
(lower bound 0.071 < 0.10). **gemini 0.158 Wilson[0.104, 0.234], lower bound 0.104 > 0.10 — marginally
above chance.** The design names an above-chance Option-A floor a NO-GO trigger, so I weighed this
hard and did **not** relax the design to force a GO.

My ruling: **it is NOT disqualifying, but it is a binding first-class caveat on any gemini result.**
Reasons:

- The elevation is **marginal and model-specific**: lower bound 0.104 is **0.004 above** chance, on
  19/120 vs an expected 12/120 — a handful of items. The pooled read (.122 Wilson[.092,.160]) and
  two of three models (claude clean, gpt near-clean) are at/near chance, so the **instrument as a
  whole is not compromised**; only gemini shows a small label/position prior doing covert work.
- The floor arm's role is to confirm the linguistic context *alone* does not leak gold. For gemini
  it leaks a *little*. The honest consequence is **not** to void the run but to (a) read the gating
  interaction **pooled and per-model**, (b) treat gemini's per-model image-rescue numbers against
  gemini's own elevated floor (≈.158), not against bare chance, and (c) state the elevation as a
  first-class caveat wherever a gemini-specific claim is made.
- Disqualifying the whole run on a 0.004-above-chance, single-model floor bound — when pooled and the
  other two models are clean — would be over-reading a marginal CI edge, not honoring the design. The
  design's NO-GO trigger is for a floor that is *meaningfully* above chance such that "the whole
  instrument is suspect"; here the instrument is sound in pooled and 2/3 models, and the gemini
  elevation is small and bounded.

This is the load-bearing call, and it is **GO-WITH-CONDITIONS, not NO-GO** — but conditional on the
gemini floor being carried as a first-class caveat (binding condition 1).

### (5) Is the DISTRACT control adequate? — **PASS (as designed; arm not yet run)**

The DISTRACT arm (ten images, no target word/trigger, "pick the most prototypical/canonical/everyday
image") is the correct word-ablation control: it isolates image-intrinsic salience from the
word→sense→image mapping. The design mandates it be **reported and credited FIRST**, and that no
IMAGE lift counts as headroom unless it survives DISTRACT (gold-selection ≈ IMAGE rate with no word ⇒
salience, the distraction null). v1's analogous control ran clean (pooled .093 ≈ chance). As specified
the control is adequate: a surface-dissimilarity-only reader that picks by salience would score on
DISTRACT and be caught. The one binding requirement is procedural — it must actually be reported first
(binding condition 3). I cannot verify the arm's *result* because it has not run; I certify the
**design** of the control is adequate.

---

## Binding conditions (the execution session MUST honor these)

1. **Gemini floor elevation is a first-class caveat.** Gemini's Option-A floor is .158
   Wilson[.104,.234], lower bound > chance. Any gemini-specific image-rescue / gating claim must (a)
   be read against gemini's own ≈.158 floor, not bare chance .10; (b) carry the floor elevation as a
   first-class, foregrounded caveat in the result page; and (c) be reported alongside the pooled and
   per-model reads so the marginal, model-specific nature is explicit. The pooled and claude/gpt
   reads (floor at/near chance) carry the primary weight.

2. **Foreground the 0-intermediate-band gap.** The frozen draw has `sep_i ∈ {0, 1/3, 1}` only — **no
   2/3 band**. The result must state plainly that the gating shape is read across a **bimodal**
   separability distribution (under-determined vs saturated, nothing between), that the binned
   image-rescue contrast — not a graded sep→rescue slope — is the test of record, and that the
   continuous Spearman/OLS companion is doubly weakened (mechanical ceiling + the 2/3 gap) and stays
   descriptive-only.

3. **DISTRACT null reported and credited FIRST.** No IMAGE-arm accuracy lift counts as grounding
   headroom unless it survives the word-ablated DISTRACT control. The DISTRACT gold-selection rate
   (vs chance .10, per-model and pooled) must be reported and credited **before** the gating
   interaction, per design condition (c).

Plus the design's already-binding execution-session obligations, restated as I am bound to honor the
design and relax nothing: **re-measure claude's raised-`max_tokens=512` IMAGE per-call cost** in a
small preflight before committing the image arm (condition d — do not run on the stale ~3× placeholder);
**day-split** so each UTC day stays under the $5 cap and each sub-batch under the $2.50 prudence flag
(condition f); keep **images out of git**; **do not re-derive** the frozen day-1 artifacts (descriptors,
leak_i, run_items, text covariate). Carry all four VWSD resource caveats (binary gold, limited annotator
independence, image-redistribution unconfirmed, gold-split-only) verbatim-in-force, and keep leak_i a
reported covariate (never regressed out), per design B.4.

---

## What this verdict authorizes

A **GO-WITH-CONDITIONS** authorizes the **next fresh-UTC-day execution session** to run the IMAGE arm
(then the DISTRACT arm, DISTRACT null reported first), under the three binding conditions above and the
design's standing conditions (d) and (f). It does **NOT** authorize any spend today: UTC 2026-06-25 is
already at ≈$4.725 of $5.00 (~$0.28 headroom), far short of even one IMAGE sub-batch. The
`result/vwsd-grounding-headroom-v2` does not exist and stays not-cleared until the image/distract arms
run, a fresh post-run verifier reproduces the finding-bearing numbers, and the result is written under
these caveats.

This certification fixes nothing about the *result*: a flat interaction remains "no detectable gating
OR underpowered," and a lift that does not survive DISTRACT is the distraction null, not headroom. The
GO reflects only that the day-1 yardstick is sound, honestly frozen, and reproducible — not any wish
for a particular outcome.
