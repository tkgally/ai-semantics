---
type: design
id: commitment-framing-model-difference-v1
title: commitment-framing model-difference probe v1 — decomposing why an explicit speaker-commitment framing RESCUES claude but SUPPRESSES gpt on conditional-antecedent presupposition
meaning-senses:
  - inferential
  - distributional
status: provisional
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
    target: essay/projection-defeasible-by-frame
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Design — commitment-framing model-difference probe v1

**Status: DESIGN AWAITING AN INDEPENDENT PRE-RUN CRITIC. NOT FROZEN. DO NOT RUN THIS SESSION.**
Running is spend-bearing and requires (a) a fresh-agent pre-run critique that re-derives every
predicted signature from the stimulus text, and (b) a fresh-budget/day decision per `PROTOCOL.md`
§6b. This page specifies the frozen-ready spec; a **later** session freezes the manifest sha, runs
the pre-run critic, and only then runs the probe.

This is the narrower follow-up named at the end of
[`result/conditional-projection-rescue-v1`](../../wiki/findings/results/conditional-projection-rescue-v1.md)
(the s158/s159 line): *"Opens a possible narrower follow-up (why does an explicit **commitment**
framing rescue claude but **suppress** gpt? — a model-difference in how 'speaker commitment' is
read), left for a later session."* It stays strictly inside that line's ratified
`internal-contrast-only` fence.

## The motivating model-difference (numbers copied verbatim from the parent result)

From [`result/conditional-projection-rescue-v1`](../../wiki/findings/results/conditional-projection-rescue-v1.md)
(verdict **ROBUST-COLLAPSE**), the per-model per-arm presup-endorse P / entail-endorse E table:

| model | base P/E | commit P/E (lift) |
|-------|----------|-------------------|
| A claude-sonnet-4.6 | 0.42 / 0.08 | **0.75** / 0.00 (**+0.33, RESCUED**) |
| B gpt-5.4-mini | 0.17 / 0.17 | 0.00 / 0.00 (−0.17) |
| C gemini-3.5-flash | 0.17 / 0.00 | 0.25 / 0.00 (+0.08) |

The parent's own words on the split: commit *"rescues **only claude** (0.42 → 0.75, entail stays
0.00 — a genuine projection restoration, not a yes-bias). For **gpt commit LOWERS** presup-endorse to
0.00 (it reads 'everything the speaker is committed to' as *more* restrictive and refuses the
antecedent's backgrounded content); gemini barely moves (0.25)."* And the honest limit it left open
(pre-run critic **advisory c**): *"the commit/belief arms change the **speech-act framing** ('a
speaker sincerely asserts') relative to base's 'consider the statement,' so they differ from base in
two coupled ways (the commitment/belief question *and* the speaker scene); a clean decomposition of
which did the work is not available."*

So there are **two things to pull apart**, and one hypothesis to test:

1. **Advisory-c confound (scene vs wording).** The commit arm changed BOTH the *speaker scene* ("A
   speaker sincerely and carefully asserts …" vs base's "Consider only the following statement …")
   AND the *question wording* ("everything the speaker is thereby committed to" vs base's neutral
   "does it follow that"). Which coupled change drives the opposite responses?
2. **The reading hypothesis.** The parent conjectures gpt reads "committed to" **restrictively** — as
   *at-issue*, actively-put-forward content only — and so **refuses the backgrounded presupposition**;
   while claude reads "committed to" **inclusively** — as covering everything the speaker is publicly
   answerable for, backgrounded presuppositions included — and so **endorses** it. This probe
   operationalizes that split directly.

## Hypothesis (direction fixed before the run)

**H (per-model reading of "committed to").** The commit effect is a difference in how each model
*reads the word "committed."* Concretely, "committed to" sits on a scale between two poles:

- a **backgrounding-inclusive** pole — "everything the speaker **takes for granted / presupposes /
  assumes**" — which explicitly reaches the projecting presupposition P;
- an **at-issue-restrictive** pole — "only what the speaker is **directly putting forward as the main
  point**" — which reaches neither the backgrounded P nor the antecedent-trapped E.

H predicts **claude's commit responses cluster at the backgrounding pole** (P high, E low: a real
projection signature) and **gpt's commit responses cluster at the at-issue pole** (P and E both low:
a refusal to extract backgrounded content). A **symmetric null** — commit lands between the poles for
both, or the poles fail to separate the models — is a first-class outcome (see verdict map).

## Scope — LOAD-BEARING (inherited, no new anchor)

**Within-model contrast only; no human comparison.** Every quantity feeding a verdict is a
within-model endorsement rate over that model's own YES/NO/UNCLEAR answers — *how a model's P/E
endorsement moves across query framings that hold the sentence constant*, and *where its neutral-
worded "committed" arm falls relative to two deliberately-poled anchor arms*. **No human projectivity
or commitment baseline is claimed, measured, or needed.** The result would **not** certify that any
model *represents* presupposition-vs-assertion or *computes* commitment; endorsing (or declining) an
inference off a forced-choice answer is text-consistency, not mechanism.

Anchor is **`anchor: internal-contrast-only`**, **inherited** — not newly opened — from the ratified
parent line
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../wiki/decisions/resolved/presupposition-projection-internal-contrast-anchor.md),
session 159, autonomous adversarial review). The scoring path is identical in kind to s159's. This
follow-up stays strictly inside that ratified within-model contrast and **opens no new anchor
decision**; `contingent-on: []`.

## Panel & settings (identical to s158/s159 house style)

Panel per [`config/models.md`](../../config/models.md): `panel.A` = `anthropic/claude-sonnet-4.6`,
`panel.B` = `openai/gpt-5.4-mini`, `panel.C` = `google/gemini-3.5-flash`, as subjects. Temperature 0;
zero-shot; text-only, single-turn (no tools); gemini `reasoning={"effort":"minimal"}`; billed
`usage.cost` recorded. Neutral system prompt reused **verbatim** from s158/s159 ("You are a careful
reader. Answer the user's question directly.") — it never mentions presupposition, projection,
commitment, or the right answer.

## Items — 12 base scenarios REUSED VERBATIM from s159

The 12 matched scenarios are reused **verbatim** from s159's frozen `prep.py` `SCEN` (which itself
reused s158): same `sid`s, same four trigger families (factive / aspectual / definite / cleft, 3
each), same `presup` (P) and `entail` (E) targets, and the same **antecedent-conditional** sentence
(`cond_antecedent`, e.g. *"If Sam realized that the door was locked, he went back for the key."*).

**Crucial difference from s159:** this probe **holds the sentence constant across all arms** — every
arm uses the `cond_antecedent` sentence. It does **not** reuse s159's `cond_consequent` / `conseq`
position manipulation. Position is *not* a factor here; the only thing that varies across arms is the
**query wrapper** (speaker scene × question wording). This makes every cross-arm difference a pure
framing effect on one fixed sentence — the tightest possible isolation of advisory-c.

P is the **projecting / backgrounded** target (e.g. "the door was locked?"); E is the **at-issue but
antecedent-trapped** target (e.g. "Sam was aware that the door was locked?") and doubles as the
per-arm **yes-bias control** (a framing that merely inflates YES lifts E too).

## Arms — a partial SCENE × WORDING factorial (each model is its own control)

Two factors:

- **SCENE** ∈ {`no-scene`: "Consider only the following statement:" ; `scene`: "A speaker sincerely
  and carefully asserts:"}.
- **WORDING** ∈ {`plain`, `commit`, `background`, `atissue`} — the question stem.

`commit`, `atissue`, and the `scene` lead-in are inherently **speaker-anchored** ("committed",
"asserts", "putting forward" all presuppose a speaker), so they appear only at the `scene` level.
`plain` and `background` are scene-agnostic (a bare *statement* can be taken "at face value" or "take
something for granted"), so they get **both** SCENE levels — that is what lets the pure SCENE effect
be read off net of wording. This yields **5 core arms** (+1 optional, below):

| # | arm | SCENE | WORDING | query stem (over the fixed `cond_antecedent` sentence) | role |
|---|-----|-------|---------|--------------------------------------------------------|------|
| 1 | **base** | no-scene | plain | *"Taking that statement at face value, does it follow that: {target}"* | **s159 replication anchor (VERBATIM)** — must reproduce the collapse |
| 2 | **scene-only** | scene | plain | *"Taking that assertion at face value, does it follow that: {target}"* | isolates the pure **speaker-scene** effect (no commitment wording) |
| 3 | **commit** | scene | commit | *"Considering everything the speaker is thereby committed to, does it follow that: {target}"* | **s159 commit arm (VERBATIM)** — the effect being decomposed |
| 4 | **background** | scene | background | *"Considering everything the speaker takes for granted in saying this, does it follow that: {target}"* | **backgrounding-inclusive POLE** — where "commit" lands if read broadly |
| 5 | **atissue** | scene | atissue | *"Considering only what the speaker is directly putting forward as the main point, does it follow that: {target}"* | **at-issue-restrictive POLE** — where "commit" lands if read narrowly |
| 6 | *(optional)* **background-noscene** | no-scene | background | *"Considering everything the statement takes for granted, does it follow that: {target}"* | corroborates the SCENE effect on the backgrounding question; lets `background` wording be seen without a scene |

Every arm ends with the s158/s159 tail verbatim: *"\n\nAnswer with exactly one word — YES, NO, or
UNCLEAR — and nothing else."* `base` and `commit` reproduce s159's `QUERY_PLAIN` and `QUERY_COMMIT`
**byte-for-byte** (the pre-run critic must diff them against s159's frozen `prep.py`); arms 2/4/5/6
are new query wrappers over the same frozen sentences.

**The poles are deliberately not neutral — that is their job.** `background` leans toward endorsing a
backgrounded P; `atissue` leans away from it. They are **anchors that bracket** the neutral-worded
`commit`, not neutral probes. The science is *where each model's `commit` P falls between its own
`background` P and its own `atissue` P*. The E leg inside each arm is the guard that a pole is not
merely a global-YES shift: at the backgrounding pole the correct signature is **P up, E flat** (E is
at-issue-embedded, not "taken for granted"), so a rise in E alongside P flags a yes-shift, not a
projection signal. (This leadingness is a genuine risk — flagged for the pre-run critic below.)

### What each contrast buys (all within-model, sentence held constant)

- **SCENE effect (advisory-c, half 1):** `base` → `scene-only` (same `plain` stem, scene toggled).
  Does merely *adding the speaker scene* already move P, before any commitment wording? Corroborated
  by `background-noscene` → `background` if arm 6 is included.
- **WORDING effect (advisory-c, half 2):** `scene-only` → `commit` (same scene, `plain` → `commit`).
  Does the *word "committed"* move P net of the scene?
- **The reading hypothesis H:** `atissue` ← `commit` → `background`, scene held. Is a model's `commit`
  P statistically indistinguishable from its `background` P (**backgrounding-reader**, claude's
  predicted signature) or from its `atissue` P (**at-issue-reader**, gpt's predicted signature)?

## Metrics (pre-specified, direction fixed)

Per (model, arm) over the arm's 12 scenarios: `presup_endorse` (P-endorse rate), `entail_endorse`
(E-endorse rate; yes-bias control), `gap = presup_endorse − entail_endorse`. Derived per model:

- `scene_effect  = scene-only.P − base.P` (pure speaker-scene lift on the neutral question)
- `wording_effect = commit.P − scene-only.P` (pure "committed" lift net of scene)
- `commit_vs_bg  = commit.P − background.P` (near 0 ⇒ commit read as backgrounding)
- `commit_vs_ai  = commit.P − atissue.P` (near 0 ⇒ commit read as at-issue)
- `pole_spread   = background.P − atissue.P` (must be wide enough for the poles to discriminate)

Reuse s159's `parse_endorse` (first standalone yes/no/unclear token; `endorsed == YES`) and per-arm
rate machinery verbatim; report unparsed and per-arm E (yes-bias) exactly as s159 did.

## Verdict map (thresholds fixed NOW; symmetric; may be tightened, never loosened)

```
BAND        = 0.15   |Δ| below this = "same as" (commit clusters with a pole; effect is null)
EFFECT      = 0.30   |Δ| at/above this = a real, attributable effect (scene / wording)
POLE_MIN    = 0.30   background.P - atissue.P must be >= this for the poles to discriminate at all
BASE_COLLAPSE_MAX = 0.60   base.P must be BELOW this for >=2/3 models (s159 collapse replicated)
YESBIAS     = 0.60   per-arm entail_endorse at/above this flags a yes-shift confound on that arm
```

**Gate 0 — design validity (must pass or the run is a REPLICATION-ANOMALY).**
`base` must reproduce the s159 collapse (base.P < BASE_COLLAPSE_MAX for ≥2/3 models) **and** the
`commit` model-difference must reappear: claude `commit.P ≥ 0.60` (rescued) **and** gpt `commit.P ≤
0.25` (suppressed). If either fails, the thing being decomposed is not present this run → verdict
**REPLICATION-ANOMALY**, decomposition reported only with that caveat, no reading claim.

**Per-model advisory-c classification** (source of the commit effect):
- **WORDING-DRIVEN** — `|scene_effect| < BAND` and `|wording_effect| ≥ EFFECT` (the *word* did it).
- **SCENE-DRIVEN** — `|scene_effect| ≥ EFFECT` and `|wording_effect| < BAND` (the *scene* did it).
- **COUPLED** — both `≥ BAND` (no clean separation; advisory-c stands).
- **NULL** — neither `≥ BAND` (the commit effect did not reproduce for this model).

**Per-model reading classification** (only meaningful where `pole_spread ≥ POLE_MIN`):
- **BACKGROUNDING-READER** — `|commit_vs_bg| ≤ BAND` and `commit_vs_ai ≥ BAND` (commit clusters with
  the backgrounding pole, above the at-issue pole). *Predicted for claude.*
- **AT-ISSUE-READER** — `|commit_vs_ai| ≤ BAND` and `commit_vs_bg ≤ −BAND` (commit clusters with the
  at-issue pole, below backgrounding). *Predicted for gpt.*
- **UNDIFFERENTIATED** — commit within BAND of both poles, or of neither, or `pole_spread <
  POLE_MIN` — the wording contrast does not separate the readings for this model. **First-class null.**

**Overall verdict:**
- **CLEAN-DECOMPOSITION** — Gate 0 passes AND the reading split is as hypothesised: claude
  BACKGROUNDING-READER **and** gpt AT-ISSUE-READER. The model difference *is* a difference in how
  "speaker commitment" is read (gpt at-issue-restrictive, claude backgrounding-inclusive); the
  advisory-c classification says whether scene or wording carries it.
- **PARTIAL** — Gate 0 passes and ≥1 of {claude, gpt} classifies as hypothesised but not both.
- **NO-DECOMPOSITION (NULL)** — Gate 0 passes but the key models are UNDIFFERENTIATED and/or COUPLED:
  **both readings survive; no clean decomposition.** Written up as a genuine null (charter §4).
- **REPLICATION-ANOMALY** — Gate 0 fails (see above).

The map is deliberately symmetric: the same BAND/EFFECT thresholds that could confirm H are the ones
that return NULL when commit sits between the poles. **No threshold may be re-tuned after seeing
results** (`PROTOCOL.md` §8 / failure-mode checklist).

## Call count & cost estimate (pre-flight, rough)

- **Core (5 arms):** 5 × 12 scenarios × 2 targets × 3 models = **360 calls**.
- **With optional arm 6:** 6 × 12 × 2 × 3 = **432 calls**.

Single-word completions, same size/shape as s159. s159 billed **$0.0526** for 288 calls
(≈ $0.000183/call) plus a $0.0026 pre-flight. Scaling: **~$0.066 core / ~$0.079 with arm 6**, plus a
~$0.003 pre-flight ⇒ **rough pre-flight estimate $0.07–0.10 total.** Set `ABORT_USD = 1.00` as the
runaway hard-stop; far under the $2.50 single-run flag and the $5.00/day (UTC) cap. A real pre-flight
(`--limit` on one model) is measured and recorded before the full run.

## Gates (what a later session must do before running)

1. **Freeze next session, not this one.** Pin the manifest sha (over SYS + the six query wrappers +
   the 12 verbatim scenarios) in `prep.py`; the probe's FREEZE GUARD refuses to run on drift.
2. **Independent fresh-agent pre-run critic (required, GO/NO-GO).** Not the agent that wrote this
   design. It must: (a) diff `base` and `commit` byte-for-byte against s159's frozen `prep.py`; (b)
   confirm the 12 scenarios are the verbatim s159 set; (c) rule on the leading-poles risk (below);
   (d) re-derive each predicted signature from the text; (e) confirm the verdict map is symmetric.
3. **Independent post-run verifier** re-derives every rate and every classification from `raw/*.json`
   by its own route before the result page is written.

## Honest bounds & risks the pre-run critic must rule on

- **Behavioral, within-model, no human comparison.** `anchor: internal-contrast-only` (inherited);
  no mechanism claim; both the at-issue and backgrounding readings of any classification are
  distributional. A CLEAN-DECOMPOSITION would show *that* the models diverge in reading "committed,"
  not that either reads it "correctly."
- **Leading poles (the central risk).** `background` ("takes for granted") and `atissue` ("main
  point") are intentionally non-neutral. The defence is that they are *anchors bracketing* the
  neutral `commit`, and the per-arm E-leg guards against a pole being mere global-YES (backgrounding
  pole must show P up / E flat). The pre-run critic must confirm this guard holds item-by-item and
  that `background`'s P-lift is not simply a yes-shift (check E and `gap`, not P alone).
- **Small Ns.** n = 3 models, 12 project-authored synthetic scenarios × up to 6 arms; each rate moves
  in ~0.083 steps, so a per-model classification can hinge on ~2 items. Direction-of-effect only; no
  coverage claim; report per-family texture, do not smooth.
- **gemini likely does not discriminate.** The parent found gemini blanket-returns UNCLEAR under
  conditionals (P and E alike). Expect gemini → UNDIFFERENTIATED here; the live model difference is
  claude-vs-gpt, and the design should say so rather than force a three-way reading.
- **"Committed" is irreducibly speaker-anchored.** There is no coherent `no-scene × commit` cell, so
  the factorial is deliberately partial (commit/atissue only at the scene level). The SCENE effect is
  therefore read off the scene-agnostic `plain` (and optional `background`) wordings, not off commit.

## Open design decisions the pre-run critic must settle before freezing

1. **Include optional arm 6 (`background-noscene`)?** Include for a symmetric read of the SCENE effect
   on the backgrounding question (+72 calls, +~$0.013), or drop for tightness (5 arms). Provisional
   default: **include** — it is cheap and strengthens the scene/wording separation.
2. **Exact phrasing of the two poles.** Is `background` = "takes for granted" the right lexeme, or
   should it be "presupposes" / "assumes" / a rotation across the three (risking within-arm
   inconsistency)? Is `atissue` = "directly putting forward as the main point" the fair narrow pole,
   or too strong (it may push even legitimately-committed content to NO)? These wordings set the poles
   the whole hypothesis is measured against — the critic owns them.
3. **`scene-only` stem wording drift.** `base` says "that **statement**", `scene-only` says "that
   **assertion**" — a one-noun drift riding along with the scene toggle. Accept (minor), or neutralise
   by re-wording both to a shared noun (which would break `base`'s byte-identical s159 replication)?
   Provisional default: **accept the drift**, and lean on `background-noscene → background` as the
   noun-clean corroborating SCENE contrast.
4. **Thresholds.** Are BAND = 0.15 / EFFECT = 0.30 / POLE_MIN = 0.30 the right bars given ~0.083-per-
   item granularity, or should BAND be one item wider (0.167) so a classification never hinges on a
   single item? Fixed now; the critic may **tighten**, never loosen.
5. **Gate-0 suppression bar for gpt.** Is `commit.P ≤ 0.25` the right "suppressed" threshold to count
   the s159 model-difference as reproduced (s159 gpt commit was 0.00), or too strict for fresh-resample
   drift? Provisional default: **≤ 0.25** (0.00 + one item of slack).
6. **gemini handling in the overall verdict.** If gemini is UNDIFFERENTIATED (expected), does
   CLEAN-DECOMPOSITION require only the claude/gpt split (as written), or all three? Provisional
   default: **claude/gpt split suffices**; gemini's blanket-UNCLEAR is reported as its own texture.
