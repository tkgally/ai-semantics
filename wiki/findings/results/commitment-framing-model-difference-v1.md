---
type: result
id: commitment-framing-model-difference-v1
title: "Why the commitment framing rescues claude but not gpt: claude reads 'committed' inclusively (a backgrounding-reader), but gpt's suppression is NOT a narrow reading — it keeps the presupposition down under every framing (verdict PARTIAL)"
meaning-senses:
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-02
updated: 2026-07-02
links:
  - rel: refines
    target: result/conditional-projection-rescue-v1
  - rel: depends-on
    target: result/conditional-projection-rescue-v1
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: essay/projection-defeasible-by-frame
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the commitment-framing decomposition probe v1

A narrower follow-up to [`result/conditional-projection-rescue-v1`](conditional-projection-rescue-v1.md)
(session 159, verdict **ROBUST-COLLAPSE**), which found a striking **model difference** inside its
`commit` arm: an explicit "everything the speaker is thereby committed to" framing **rescued** claude's
conditional-antecedent presupposition endorsement (0.42 → 0.75) but **suppressed** gpt's (0.17 → 0.00).
That result left the *why* open (its own advisory c): the `commit` arm changed **two** things at once —
the *speaker scene* ("a speaker sincerely asserts") and the *question wording* ("committed to") — so a
clean decomposition was unavailable. This probe decomposes that model difference. Run record:
[`experiments/runs/2026-07-02-commitment-framing-decomposition/`](../../../experiments/runs/2026-07-02-commitment-framing-decomposition/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-07-02-commitment-framing-decomposition/PREREG.md),
manifest sha `2b4f69a7…`.

**One-line finding.** Pre-registered verdict **PARTIAL**. The s159 model difference reproduced (Gate 0
passed: base collapse 3/3, claude commit rescued to 0.75, gpt commit suppressed to 0.08), and the
reading hypothesis holds **for claude only**. claude reads "committed to" **inclusively**: its neutral
`commit` presupposition-endorse (0.75) clusters with the deliberately backgrounding pole "everything the
speaker **takes for granted**" (0.83) and sits well above the at-issue pole "the **main point**" (0.42)
— a **backgrounding-reader**. But gpt's suppression is **not** the predicted narrow reading of
"committed": gpt keeps presupposition-endorse **low under every framing, including the explicitly
backgrounding pole** (max 0.33), so the two poles fail to separate for it (pole_spread 0.08) — gpt is
**undifferentiated**, and its commit-suppression is a *general* reluctance to extract the projected
presupposition, not a wording-specific effect. A twist: the at-issue signature **predicted for gpt shows
up in gemini instead**, and gemini — contra the parent's expectation — is **not** blanket-UNCLEAR here.

## Scope — LOAD-BEARING (read before citing)

**Within-model contrast only; no human comparison.** Every quantity feeding a verdict is a within-model
endorsement rate over that model's own YES/NO/UNCLEAR answers — *how a model's own presupposition/entail
endorsement moves across query framings that hold the sentence constant*, and *where its neutral
`commit` arm falls between its own two poled anchor arms*. **No human projectivity or commitment baseline
is claimed, measured, or needed.** The result does **not** certify that any model *represents*
presupposition-vs-assertion or *computes* commitment; endorsing (or declining) an inference off a
forced-choice answer is text-consistency, not mechanism. A "reader" classification says *where a model's
neutral wording lands between two deliberately-poled anchors*, **not** that either model reads "committed"
correctly. Anchor is **`anchor: internal-contrast-only`**, **inherited** from the parent line ratified by
an independent adversarial review
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md),
session 159); this follow-up stays strictly within that within-model contrast and opens **no** new anchor
decision.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects. Temperature 0; text-only,
  single-turn, zero-shot; gemini `reasoning={"effort":"minimal"}`. Neutral system prompt (identical to
  s158/s159) that never mentions presupposition, projection, commitment, or the right answer.
- **Items.** 12 base scenarios **reused verbatim from s159** (same 4 trigger families — factive /
  aspectual / definite / cleft, 3 each — same P and matched-entailment E targets, same
  antecedent-conditional sentence) × **6 arms** × 2 targets = **144 item-conditions** per model, 432
  calls total. **The sentence is held constant across all arms**; only the query wrapper (SCENE ×
  WORDING) varies, so every cross-arm difference is a pure framing effect on one fixed sentence. The six
  arms (`base` and `commit` reproduce s159's `QUERY_PLAIN` / `QUERY_COMMIT` **byte-for-byte** — asserted
  by `prep.py --check`):
  - **base** (no-scene, plain) — the s159 replication anchor.
  - **scene-only** (scene, plain) — isolates the pure speaker-scene effect (no commitment wording).
  - **commit** (scene, commit) — the s159 commit arm; the effect being decomposed.
  - **background** (scene, background) — the **backgrounding-inclusive pole**: "everything the speaker
    **takes for granted** in saying this."
  - **atissue** (scene, atissue) — the **at-issue-restrictive pole**: "only what the speaker is directly
    **putting forward as the main point**."
  - **background-noscene** (no-scene, background) — corroborates the scene effect on the backgrounding
    question.
- **Cost.** **$0.0814 billed** (claude $0.0475 / gpt $0.0157 / gemini $0.0182), 0 missing cost, **0
  unparsed** answers; plus a $0.0020 pre-flight (6 claude items) = **$0.0834** this run. UTC-2026-07-02
  day total after this run **$0.1106** of $5.00. Far under the $2.50 single-run flag.

## Numbers (from `results.json`; independently reproduced by a fresh post-run verifier, 0 discrepancies)

**Per model, per arm** (presup-endorse P / entail-endorse E over 12 items each; gap = P − E). Every arm
holds the same antecedent-conditional sentence; only the query framing changes.

| model | base P/E | scene-only P/E | **commit P/E** | **background** P/E | **atissue** P/E | bg-noscene P/E |
|-------|----------|----------------|----------------|--------------------|-----------------|----------------|
| A claude-sonnet-4.6 | 0.42 / 0.08 | 0.58 / 0.08 | **0.75 / 0.00** | **0.83 / 0.00** | **0.42 / 0.00** | 0.83 / 0.08 |
| B gpt-5.4-mini | 0.08 / 0.17 | 0.17 / 0.00 | **0.08 / 0.00** | **0.33 / 0.08** | **0.25 / 0.00** | 0.33 / 0.25 |
| C gemini-3.5-flash | 0.17 / 0.00 | 0.25 / 0.00 | **0.17 / 0.00** | **0.67 / 0.08** | **0.17 / 0.00** | 0.75 / 0.08 |

**Derived per model** (P-space; all within-model, sentence held constant):

| model | scene_effect | wording_effect | commit_vs_bg | commit_vs_ai | pole_spread | advisory-c | **reading** |
|-------|-------------|----------------|--------------|--------------|-------------|-----------|-------------|
| A claude | +0.17 | +0.17 | −0.08 | +0.33 | 0.42 | COUPLED | **BACKGROUNDING-READER** |
| B gpt | +0.08 | −0.08 | −0.25 | −0.17 | 0.08 | NULL | **UNDIFFERENTIATED** |
| C gemini | +0.08 | −0.08 | −0.50 | +0.00 | 0.50 | NULL | **AT-ISSUE-READER** |

Verdict per the frozen map (BAND 0.15 / EFFECT 0.30 / POLE_MIN 0.30 / BASE_COLLAPSE_MAX 0.60 / gpt
suppression ≤ 0.25 / claude rescue ≥ 0.60): **Gate 0 PASS** (base collapsed 3/3; claude commit 0.75 ≥
0.60; gpt commit 0.08 ≤ 0.25) → the s159 model difference reproduced. Overall **PARTIAL** — the reading
split holds for **claude only** (claude BACKGROUNDING-READER as hypothesised; gpt UNDIFFERENTIATED, not
the predicted AT-ISSUE-READER).

## Interpretation (calibrated)

- **claude: a backgrounding-reader (hypothesis confirmed, for this model).** claude's neutral `commit`
  presupposition-endorse (0.75) is one 0.083-step from the explicit "takes for granted" pole (0.83) and a
  clean 0.33 above the "main point" pole (0.42), with entail flat at 0.00 throughout (no yes-bias). So
  claude reads "everything the speaker is committed to" **inclusively** — reaching the backgrounded
  presupposition — which is *why* the commit framing rescues its projection. This directly supplies the
  reading the s159 result conjectured for claude.
- **gpt: suppression is general, not a narrow reading (hypothesis refuted, informatively).** The s159
  result conjectured gpt reads "committed" *restrictively* (at-issue) and so refuses the backgrounded
  content. This probe **does not support that**: gpt's presupposition-endorse stays low under **every**
  framing, including the explicitly backgrounding pole (`background` 0.33, `background-noscene` 0.33) — so
  the two poles barely separate for it (pole_spread 0.08, below the 0.30 discrimination floor) and it is
  **UNDIFFERENTIATED**. gpt's commit-suppression is therefore not specific to the word "committed"; it is
  a *general reluctance to extract the projected presupposition from a conditional antecedent*, which no
  framing tested here lifts. That is a **stronger, simpler** description of gpt than the narrow-reading
  conjecture — and it retires that conjecture.
- **The advisory-c confound is NOT cleanly resolved for claude.** The whole point of decomposing was to
  say whether the commit rescue is carried by the *speaker scene* or the *wording*. For claude both
  contribute about equally (scene_effect +0.17, wording_effect +0.17, each ≥ BAND, neither ≥ EFFECT) →
  **COUPLED**. So the honest statement is: the rescue is **coupled scene-plus-wording**, not "the word
  *committed* did it." The decomposition sharpened *what* claude's commit reading is (backgrounding) but
  left the *scene-vs-wording* attribution unseparated at this sample size.
- **gemini: the predicted-gpt signature, in the wrong model — and it is not blanket-UNCLEAR.** gemini
  classifies **AT-ISSUE-READER** (neutral `commit` 0.17 = `atissue` 0.17, both low; `background` high at
  0.67; widest pole_spread, 0.50). Ironically this is the signature the parent predicted for *gpt*.
  Crucially, gemini is **not** blanket-UNCLEAR here (only 11/144 UNCLEAR answers; 105 NO, 28 YES) —
  contra the parent's expectation — and it discriminates the two poles the most sharply of the three. But
  its **commit effect did not reproduce** (commit 0.17 = base 0.17, advisory-c NULL), so its at-issue
  classification reflects where its neutral wording *sits between poles*, not a commit-induced lift; gemini
  is not one of the Gate-0 models, so this is recorded as its own texture, not part of the verdict.
- **What the data do NOT support.** (i) No human comparison — no human projectivity or commitment
  baseline is measured or claimed. (ii) No mechanism claim — a "reader" label is a within-model position
  between two poled framings, read off forced-choice answers; it is not evidence a model *computes* an
  at-issue/backgrounded partition. (iii) The scene-vs-wording attribution for claude is **coupled**, not
  decomposed. (iv) The poles are **deliberately non-neutral anchors** that bracket the neutral `commit`
  wording; they are not neutral probes and carry no "correct-reading" force.
- **Feeds the parent line and the essay.** This refines
  [`result/conditional-projection-rescue-v1`](conditional-projection-rescue-v1.md): the model-specific
  rescue it recorded is, for claude, a **backgrounding-inclusive reading of speaker commitment**, and gpt's
  suppression is a **general** low-projection floor rather than a narrow commitment reading. It leaves
  [`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md) untouched at the
  panel level (the conditional-antecedent collapse remains the standing boundary; only claude's projection
  is recoverable, now with a named reading behind the recovery).

## Honest bounds & caveats (all surfaced by the independent post-run verifier)

1. **claude's BACKGROUNDING-READER classification hinges on ~1 item.** `commit_vs_bg = −0.08` is one
   0.083-step inside the ±0.15 band; had claude's commit arm been one item lower (0.67), it would exceed
   the band and flip claude to UNDIFFERENTIATED. Report as **direction-of-effect only**, not a precise
   boundary.
2. **gemini is NOT blanket-UNCLEAR** (11/144 UNCLEAR), contradicting the parent/PREREG expectation; it
   has the *widest* pole spread of the panel. The parent's "gemini likely undifferentiated" prior was
   wrong for this probe.
3. **claude's rescue is COUPLED, not wording-driven** — do not phrase it as "the word *committed* did it";
   scene and wording contribute about equally.
4. **gemini's commit effect did not reproduce** (commit 0.17 = base 0.17); its at-issue reading is a
   between-poles position, not a commit-induced lift.
5. **Small N throughout** — n = 3 models × 12 project-authored synthetic scenarios × 6 arms; rates move in
   ~0.083 steps, so a per-model classification can hinge on ~2 items. Direction-of-effect only; no coverage
   claim; per-family texture not smoothed. `anchor: internal-contrast-only`; no human comparison.

## Gates

- **Pre-run critic (independent fresh agent): GO** (no blockers, no should-fixes). It byte-diffed `base`
  and `commit` against s159's frozen `prep.py` (identical, em-dash included), confirmed the 12 scenarios
  are the verbatim s159 set (0 field diffs), ruled the E-leg guard sound (re-derived from fac1/cle1/def1:
  E is antecedent-trapped, not backgrounded, so a backgrounding pole lifts P and leaves E flat),
  confirmed the verdict map is symmetric (null reachable and first-class), and settled all six open
  design decisions by accepting the provisional defaults (arm 6 included → 6 arms/432 calls; poles as
  written; scene-only noun drift accepted; thresholds kept; gpt suppression bar ≤ 0.25; gemini reported
  as its own texture). Freeze pinned the manifest sha after sign-off.
- **Post-run verifier (independent fresh agent): CONFIRMED** — re-derived every per-arm P/E, all five
  derived quantities, all classifications, Gate 0's three conjuncts, and the overall verdict from
  `raw/*.json` by its own parser: **0 discrepancies**. Data integrity: 0 errors, 0 empty answers, 0
  unparsed, 0 ambiguous parses; all 36 (model × arm × target) cells hold exactly 12 items; no arm trips
  the yes-bias flag (max E = 0.25 < 0.60). The five caveats above are its findings.
- **Freeze guard.** `prep.py --check` passes with the pinned manifest sha `2b4f69a7…`; `probe.py` refuses
  to run on drift; `analyze.py` makes no API calls.
