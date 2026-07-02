# PREREG — the commitment-framing decomposition probe

**Run:** `2026-07-02-commitment-framing-decomposition` · **frozen** 2026-07-02 (session 166) ·
**manifest sha** `PINME`

Narrower follow-up to [`result/conditional-projection-rescue-v1`](../../../wiki/findings/results/conditional-projection-rescue-v1.md)
(run `2026-07-01-conditional-projection-rescue`, session 159; verdict **ROBUST-COLLAPSE**). That
result found a striking **model difference** inside its `commit` arm: an explicit "everything the
speaker is thereby committed to" framing **RESCUED** claude's conditional-antecedent presupposition
endorsement (**0.42 → 0.75**, E stayed 0.00) but **SUPPRESSED** gpt's (**0.17 → 0.00**); gemini
barely moved (0.17 → 0.25). The parent left this open, in its own words: *"Opens a possible narrower
follow-up (why does an explicit commitment framing rescue claude but suppress gpt? — a
model-difference in how 'speaker commitment' is read), left for a later session."*

Frozen *before* any probe call; the FREEZE GUARD in `probe.py` refuses to run unless the manifest sha
above is intact.

## The one question (nothing wider)

> **Why** does the same "committed to" framing move claude and gpt in opposite directions? Decompose
> that model difference along two axes, holding the sentence constant:
> 1. **advisory-c confound** — is the commit effect driven by the **speaker scene** ("a speaker
>    asserts …") or by the **wording** ("committed to")?
> 2. **the reading hypothesis H** — does each model read "committed to" at a **backgrounding-inclusive**
>    pole ("takes for granted", reaching the projecting presupposition P) or an **at-issue-restrictive**
>    pole ("the main point", reaching neither the backgrounded P nor the antecedent-trapped E)?

The measure is a **within-model contrast** throughout: (i) P-vs-E endorsement WITHIN each arm (E is
the yes-bias control), (ii) P endorsement ACROSS arms relative to a BASE arm that replicates the s159
`base`/`commit` cells verbatim, and (iii) where each model's neutral-worded `commit` P falls between
its own `background` P (backgrounding pole) and its own `atissue` P (at-issue pole).

## Scope cap — LOAD-BEARING (read before citing any result)

Any verdict here is a **within-model behavioral contrast ONLY**. It does **not**:

- make **any human comparison** — no human projectivity / commitment baseline is claimed, measured,
  or needed. The signal is *how a model's own P/E endorsement moves across query framings that hold
  the sentence constant*, and *where its neutral commit arm lands relative to two poled anchor arms*.
- certify that any model **represents** presupposition-vs-assertion or **computes** commitment;
  endorsing (or declining) an inference off a forced-choice answer is text-consistency, not
  mechanism. A CLEAN-DECOMPOSITION would show *that* the models diverge in reading "committed", not
  that either reads it "correctly".
- adjudicate presupposition theory. The two poles (`background`, `atissue`) are **deliberately
  non-neutral anchors that bracket** the neutral `commit` wording — not neutral probes.

**Anchor discipline.** `anchor: internal-contrast-only`, **inherited** — not newly opened — from the
ratified parent line
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../../wiki/decisions/resolved/presupposition-projection-internal-contrast-anchor.md),
session 159, autonomous adversarial review). The scoring path is identical in kind to s159's. This
follow-up stays strictly inside that ratified within-model contrast and **opens no new anchor
decision**; `contingent-on: []`.

## Panel & settings (identical to s158/s159 house style)

Panel per [`config/models.md`](../../../config/models.md): `panel.A` = `anthropic/claude-sonnet-4.6`,
`panel.B` = `openai/gpt-5.4-mini`, `panel.C` = `google/gemini-3.5-flash`, as subjects. Temperature 0;
zero-shot; text-only, single-turn (no tools); gemini `reasoning={"effort":"minimal"}`; billed
`usage.cost` recorded. Neutral system prompt reused **verbatim** from s158/s159:
`"You are a careful reader. Answer the user's question directly."` — it never mentions presupposition,
projection, commitment, or the right answer.

## Items — 12 base scenarios REUSED VERBATIM from s159

The 12 matched scenarios are reused **verbatim** from s159's frozen `prep.py` `SCEN` (which itself
reused s158): same `sid`s, same four trigger families (factive / aspectual / definite / cleft, 3
each), same `presup` (P) and `entail` (E) targets, and the same **antecedent-conditional** sentence
(`cond_antecedent`). This probe **holds the sentence constant across all arms** — every arm uses
`cond_antecedent`. It does **not** carry s159's `cond_consequent`; position is not a factor here.
P is the **projecting / backgrounded** target; E is the **at-issue but antecedent-trapped** target
and doubles as the per-arm **yes-bias control**. `prep.py --check` asserts the `base` and `commit`
wrappers are byte-for-byte identical to s159's `QUERY_PLAIN` / `QUERY_COMMIT`.

## Arms — a partial SCENE × WORDING factorial (each model is its own control)

Two factors: **SCENE** ∈ {`no-scene`, `scene`}; **WORDING** ∈ {`plain`, `commit`, `background`,
`atissue`}. `commit`/`atissue` and the `scene` lead-in are inherently speaker-anchored, so appear
only at `scene`; `plain`/`background` are scene-agnostic and get both SCENE levels. **6 arms:**

| # | arm | SCENE | WORDING | query stem (over the fixed `cond_antecedent` sentence) | role |
|---|-----|-------|---------|--------------------------------------------------------|------|
| 1 | **base** | no-scene | plain | *"Taking that statement at face value, does it follow that: {target}"* | **s159 replication anchor (VERBATIM)** — must reproduce the collapse |
| 2 | **scene-only** | scene | plain | *"Taking that assertion at face value, does it follow that: {target}"* | isolates the pure **speaker-scene** effect |
| 3 | **commit** | scene | commit | *"Considering everything the speaker is thereby committed to, does it follow that: {target}"* | **s159 commit arm (VERBATIM)** — the effect being decomposed |
| 4 | **background** | scene | background | *"Considering everything the speaker takes for granted in saying this, does it follow that: {target}"* | **backgrounding-inclusive POLE** |
| 5 | **atissue** | scene | atissue | *"Considering only what the speaker is directly putting forward as the main point, does it follow that: {target}"* | **at-issue-restrictive POLE** |
| 6 | **background-noscene** | no-scene | background | *"Considering everything the statement takes for granted, does it follow that: {target}"* | corroborates the SCENE effect on the backgrounding question |

Every arm ends with the s158/s159 tail verbatim: *"\n\nAnswer with exactly one word — YES, NO, or
UNCLEAR — and nothing else."*

**The poles are deliberately not neutral — that is their job.** `background` leans toward endorsing a
backgrounded P; `atissue` leans away from it. The science is *where each model's `commit` P falls
between its own `background` P and its own `atissue` P*. The E leg inside each arm guards against a
pole being a mere global-YES shift: at the backgrounding pole the correct signature is **P up, E
flat** (E is at-issue-embedded, not "taken for granted"); a rise in E alongside P flags a yes-shift.

## Metrics (pre-specified, direction fixed)

Per (model, arm) over the arm's 12 scenarios: `presup_endorse` (P), `entail_endorse` (E; yes-bias
control), `gap = P − E`. Derived per model:

- `scene_effect   = scene-only.P − base.P` (pure speaker-scene lift on the neutral question)
- `wording_effect = commit.P − scene-only.P` (pure "committed" lift net of scene)
- `commit_vs_bg   = commit.P − background.P` (near 0 ⇒ commit read as backgrounding)
- `commit_vs_ai   = commit.P − atissue.P` (near 0 ⇒ commit read as at-issue)
- `pole_spread    = background.P − atissue.P` (must be wide enough for the poles to discriminate)

Reuse s159's `parse_endorse` (first standalone yes/no/unclear token; `endorsed == YES`) verbatim;
report unparsed and per-arm E exactly as s159 did.

## Verdict map (thresholds fixed NOW; symmetric; may be tightened, never loosened)

```
BAND              = 0.15   |Δ| below this = "same as" (commit clusters with a pole; effect is null)
EFFECT            = 0.30   |Δ| at/above this = a real, attributable effect (scene / wording)
POLE_MIN          = 0.30   background.P − atissue.P must be >= this for the poles to discriminate
BASE_COLLAPSE_MAX = 0.60   base.P must be BELOW this for >=2/3 models (s159 collapse replicated)
YESBIAS           = 0.60   per-arm entail_endorse at/above this flags a yes-shift confound on that arm
GATE0_CLAUDE_RESCUE = 0.60  claude commit.P must be >= this (rescued) for Gate 0
GATE0_GPT_SUPPRESS  = 0.25  gpt commit.P must be <= this (suppressed) for Gate 0
```

**Gate 0 — design validity (must pass or the run is a REPLICATION-ANOMALY).**
`base` reproduces the s159 collapse (base.P < BASE_COLLAPSE_MAX for ≥2/3 models) **and** the `commit`
model-difference reappears: claude `commit.P ≥ 0.60` **and** gpt `commit.P ≤ 0.25`. If either fails,
the thing being decomposed is not present this run → verdict **REPLICATION-ANOMALY**, decomposition
reported only with that caveat, no reading claim.

**Per-model advisory-c classification** (source of the commit effect):
- **WORDING-DRIVEN** — `|scene_effect| < BAND` and `|wording_effect| ≥ EFFECT`.
- **SCENE-DRIVEN** — `|scene_effect| ≥ EFFECT` and `|wording_effect| < BAND`.
- **COUPLED** — both `≥ BAND` (no clean separation).
- **NULL** — neither `≥ BAND` (the commit effect did not reproduce for this model).

**Per-model reading classification** (only meaningful where `pole_spread ≥ POLE_MIN`):
- **BACKGROUNDING-READER** — `|commit_vs_bg| ≤ BAND` and `commit_vs_ai ≥ BAND`. *Predicted: claude.*
- **AT-ISSUE-READER** — `|commit_vs_ai| ≤ BAND` and `commit_vs_bg ≤ −BAND`. *Predicted: gpt.*
- **UNDIFFERENTIATED** — otherwise, or `pole_spread < POLE_MIN`. **First-class null.**

**Overall verdict:**
- **CLEAN-DECOMPOSITION** — Gate 0 passes AND claude BACKGROUNDING-READER **and** gpt AT-ISSUE-READER.
- **PARTIAL** — Gate 0 passes and exactly one of {claude, gpt} classifies as hypothesised.
- **NO-DECOMPOSITION (NULL)** — Gate 0 passes but the key models are UNDIFFERENTIATED and/or COUPLED;
  both readings survive. Written up as a genuine null (charter §4).
- **REPLICATION-ANOMALY** — Gate 0 fails.

The map is deliberately symmetric: the same BAND/EFFECT thresholds that could confirm H are the ones
that return NULL when commit sits between the poles. **No threshold may be re-tuned after seeing
results** (`PROTOCOL.md` §8 / failure-mode checklist).

## Pre-run critic rulings (session 166) — the 6 open design decisions

The independent pre-run critic (fresh agent, not the design author) settled the six decisions the
design page listed. Recorded here as frozen:

1. **Arm 6 (`background-noscene`)** — **INCLUDED** (6 arms, 432 calls). Cheap; strengthens the
   scene/wording separation and gives a noun-clean corroborating SCENE contrast.
2. **Pole phrasings** — `background` = "takes for granted", `atissue` = "directly putting forward as
   the main point". Adopted as written.
3. **`scene-only` noun drift** ("statement" → "assertion") — **accepted**; `background-noscene →
   background` is the noun-clean corroborating SCENE contrast.
4. **Thresholds** — BAND 0.15 / EFFECT 0.30 / POLE_MIN 0.30 kept.
5. **Gate-0 gpt suppression bar** — `commit.P ≤ 0.25` kept (0.00 + one item of slack).
6. **gemini handling** — CLEAN-DECOMPOSITION requires only the claude/gpt split; gemini's expected
   blanket-UNCLEAR reported as its own texture.

*(Any critic amendments to the above are recorded in `README.md` / the result page; the sha is
pinned only after the critic signs off.)*

## Honest bounds & risks

- **Behavioral, within-model, no human comparison.** `anchor: internal-contrast-only` (inherited);
  no mechanism claim; both readings of any classification are distributional.
- **Leading poles (central risk).** The E-leg guard (backgrounding pole must show P up / E flat)
  defends against a pole being mere global-YES; report E and `gap`, not P alone.
- **Small Ns.** n = 3 models, 12 synthetic scenarios × 6 arms; each rate moves in ~0.083 steps, so a
  per-model classification can hinge on ~2 items. Direction-of-effect only; no coverage claim.
- **gemini likely does not discriminate** (blanket-UNCLEAR under conditionals in the parent); expect
  UNDIFFERENTIATED. The live model difference is claude-vs-gpt.
- **"Committed" is irreducibly speaker-anchored** — no coherent `no-scene × commit` cell, so the
  factorial is deliberately partial; the SCENE effect is read off the scene-agnostic wordings.

## Cost estimate (pre-flight, rough)

- **6 arms:** 6 × 12 scenarios × 2 targets × 3 models = **432 calls**.

Single-word completions, same size/shape as s159. s159 billed **$0.0526** for 288 calls
(≈ $0.000183/call). Scaling: **~$0.079** plus a ~$0.003 pre-flight ⇒ **rough estimate $0.07–0.10.**
`ABORT_USD = 1.00` is the runaway hard-stop; far under the $2.50 single-run flag and the $5.00/day
(UTC) cap. A real pre-flight (`--limit` on one model) is measured and recorded before the full run.

## Gates

1. **Freeze** — pin the manifest sha in `prep.py`; the FREEZE GUARD refuses to run on drift.
2. **Independent fresh-agent pre-run critic (GO/NO-GO)** — diffed `base`/`commit` byte-for-byte
   against s159, confirmed the 12 scenarios verbatim, ruled on the 6 decisions + the leading-poles
   E-leg guard, confirmed the verdict map is symmetric. (Rulings above.)
3. **Independent post-run verifier** re-derives every rate and every classification from `raw/*.json`
   by its own route before the result page is written.
