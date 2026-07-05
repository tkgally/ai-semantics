---
type: result
id: scivetti-let-alone-forced-decomposition-v1
title: Forcing the weakest model to actually use the working surface partly closes its let-alone gap but does not reach the human baseline — a partial output-channel effect with a below-baseline residual; uptake induced, the clean trigger-(b) test delivered as a candidate
meaning-senses:
  - constructional
  - inferential
  - human-comparison
  - model-internal
status: proposed
contingent-on: []
created: 2026-06-20
updated: 2026-07-05
links:
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
  - rel: refines
    target: result/scivetti-let-alone-working-surface-v1
  - rel: supports
    target: essay/output-channel-confound
  - rel: supports
    target: essay/witness-seeking-economics
  - rel: depends-on
    target: essay/undischargeable-negative
  - rel: depends-on
    target: essay/floor-is-not-a-ceiling
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: source/li-2024-cot-serial
  - rel: supports
    target: claim/output-channel-working-surface
---

# Result: let-alone forced-decomposition (uptake-inducing) probe v1

An **uptake-inducing** follow-up to
[`result/scivetti-let-alone-working-surface-v1`](scivetti-let-alone-working-surface-v1.md)
(session 58). That probe *offered* a working surface and **2 of 3 models lifted** to the
≈0.90 human baseline on the near-chance phrasal-scalar **let-alone** NLI items (claude
0.542→0.792, gemini 0.667→0.917) — but **gpt-5.4-mini largely declined the offer** (16/24
bare one-token `FINAL: N` answers, median 8 completion tokens, 0 reasoning tokens), so its
persistence at 0.375 was **channel-not-taken-up**, not a clean channel-controlled survival.
[`essay/output-channel-confound`](../essays/output-channel-confound.md)'s body (§"Offering a
channel is not exercising it") states that a clean **trigger-(b)** test — a serial negative
that *survives* a widened channel — must **induce uptake** first. This probe runs that test
on the lowest-governance-risk axis the essay names: a **forced decomposition** (no few-shot
demonstrations). Run record:
[`experiments/runs/2026-06-20-scivetti-let-alone-forced-decomposition/`](../../../experiments/runs/2026-06-20-scivetti-let-alone-forced-decomposition/README.md).

**One-line finding.** Forcing gpt-5.4-mini to actually externalize the inference (a
mandatory, construction-neutral 3-step scaffold before the answer) **induced uptake** —
its median let-alone completion length jumped **8 → 120 tokens** (24/24 items worked, where
session 58 it mostly emitted bare answers). With the channel now genuinely exercised, gpt's
let-alone accuracy rose **0.375 → 0.583** (+0.21, 7 gains / 2 losses) — **directional but
underpowered** (within-item sign test p = 0.090, does **not** clear the pre-registered 0.05
bar → verdict **UNCHANGED**) — and it **stays below the human ≈0.90 baseline** (CI
[0.388, 0.755], hi < 0.90), where claude (0.833) and gemini (0.875) sit. So gpt's let-alone
difficulty is a **partial output-channel effect**: part is channel-bounded (forced uptake
helps) and part **survives a genuinely-exercised wide channel** (it does not reach
baseline). This is the closest the record has come to the trigger-(b) contrast case, but at
n = 24 it is a **candidate, not a clean firing**. claude and gemini — the manipulation check
— **stay at baseline** under forced decomposition (UNCHANGED, no DROP), and the
comparative-correlative ceiling control is **PRESERVED** for all three, so the forced
scaffold is a *valid, benign* instrument.

## What ran

- **Design: single manipulated variable (offered → forced surface).** The ONLY change vs
  session 58 is the trailing output instruction: a free-form "think it through step by step"
  → a **mandatory 3-step decomposition** (1. PREMISE paraphrase / 2. HYPOTHESIS paraphrase /
  3. LINK: does the premise force the hypothesis true / leave it open / force it false). The
  scaffold is **construction-neutral and answer-blind** — it names no construction, no
  scale, no let-alone semantics; step 3 only restates the same 0/1/2 trichotomy already in
  the verbatim definitions, so it adds no information, it forces externalization. **No
  demonstration items** (forced decomposition, not few-shot).
- **Held byte-identical** to sessions 57/58: the SAME 24 let-alone + 30
  comparative-correlative test items (subset sha `9be31a8fea8d7f16`; full-set sha
  `1c5cffb18c5ef78e`, verified — same corpus, re-cloned upstream @ `82699473`); the 0/1/2
  NLI label *definitions* (verbatim); the gold (NOT shown); the panel; temperature 0; and
  **gemini `reasoning effort: minimal` held constant** — so the contrast isolates the output
  channel / **uptake**, not the reasoning budget.
- **Cells.** let-alone (n = 24) — the TARGET; comparative-correlative (n = 30) — a CEILING
  CONTROL.
- **Integrity.** 54 rows/model, **0 missing**, **162/162 parsed via the `FINAL:` tag** (0
  fallbacks), **0 missing `usage.cost`**. All three models **worked 24/24** let-alone items
  (≥40 pre-`FINAL` chars + ≥2 numbered steps).
- **Cost** (billed `usage.cost`): **$0.3342** (claude $0.2019 / gpt $0.0373 / gemini
  $0.0951). Under the $2.50 single-run flag; UTC-day 2026-06-20 total after this run
  ≈ $4.13, under the standard $5 cap.
- **Governance.** A format/instrument extension under the already-ratified Scivetti
  answer-key anchor (ratified 2026-05-29) + `constructional-divergence-operationalization`;
  it does **not** change *what* is scored against the human gold (same labels, same gold) —
  only *how* the label is produced. **No demonstration items**, so the few-shot leak caveat
  does not apply. **No new decision owed** (independent pre-run critic GO, fresh agent).
  Independent post-run verifier (fresh agent) **REPRODUCED** every number from raw.

## Results

Human reference (fixed, not retuned): Scivetti Exp-1 native-speaker accuracy ≈ 0.90. 3-way
chance ≈ 0.33. comparative-correlative carries the **ratified anchor**; let-alone is
**descriptive** from the same human-annotated release (not individually anchored), exactly
as sessions 57/58. Within-item paired counts vs **session 58 (offered surface)**: `b` =
offered-WRONG → forced-decomp-RIGHT (gains); `c` = offered-RIGHT → fd-WRONG (losses);
one-sided exact binomial on the `b+c` discordant pairs. LIFTS requires fd_acc > offered_acc
AND p < 0.05.

### let-alone (n = 24) — the target

| model | forced (s57) | offered ws (s58) | **forced-decomp** | Δ vs offered | gains / losses | sign-test p | verdict | vs human 0.90 |
|---|---:|---:|---:|---:|---:|---:|---|---|
| claude-sonnet-4.6 | 0.542 | 0.792 | **0.833** [0.641, 0.933] | +0.042 | 2 / 1 | 0.500 | UNCHANGED | MATCHES (CI covers 0.90) |
| gpt-5.4-mini | 0.458 | 0.375 | **0.583** [0.388, 0.755] | +0.208 | 7 / 2 | 0.090 | UNCHANGED | **BELOW** |
| gemini-3.5-flash | 0.667 | 0.917 | **0.875** [0.690, 0.957] | −0.042 | 2 / 3 | 0.813 | UNCHANGED | MATCHES (CI covers 0.90) |

### Uptake manipulation check (let-alone) — the crux

| model | offered ws (s58) worked | forced-decomp worked | gpt completion-token median |
|---|---:|---:|---:|
| claude-sonnet-4.6 | 24/24 | 24/24 | (median 223.5) |
| gpt-5.4-mini | ~8/24 (16 bare one-token) | **24/24** | **8 → 120** |
| gemini-3.5-flash | 24/24 | 24/24 | (median 169.5) |

The forced scaffold did for gpt what "think step by step" could not: it took the channel
from **offered-but-declined** to **genuinely-exercised**. This is what makes the trigger-(b)
reading clean — gpt's residual below-baseline accuracy is now read off a channel it actually
used.

### comparative-correlative (n = 30) — ceiling control

| model | offered ws (s58) | forced-decomp | control guard |
|---|---:|---:|---|
| claude-sonnet-4.6 | 1.000 | 1.000 [0.886, 1.000] | **PRESERVED** |
| gpt-5.4-mini | 0.967 | 1.000 [0.886, 1.000] | **PRESERVED** |
| gemini-3.5-flash | 1.000 | 1.000 [0.886, 1.000] | **PRESERVED** |

## Interpretation (modest)

1. **The uptake manipulation succeeded — the session-58 "channel-not-taken-up" hole is
   closed.** Forced decomposition took gpt from 16/24 bare one-token answers (median 8
   tokens) to 24/24 worked (median 120 tokens). gpt's let-alone accuracy is now read off a
   **genuinely-exercised** wide channel, which is exactly the precondition
   [`essay/output-channel-confound`](../essays/output-channel-confound.md) (body §"Offering a
   channel is not exercising it") says a clean trigger-(b) test requires. The earlier
   ambiguity — was gpt's persistence a channel artifact it declined to clear, or a real
   bound? — is now answerable.
2. **The answer is a PARTIAL channel effect, not a full artifact and not a clean survival.**
   Forcing the working lifts gpt's let-alone accuracy by +0.21 over the offered surface (7
   gains / 2 losses) — so **some** of the gap was the model not using the channel. But the
   lift is **underpowered** (sign test p = 0.090, n = 24, 9 discordant pairs; does not clear
   the pre-registered 0.05 bar, so the verdict is **UNCHANGED**), and crucially gpt **stays
   below the human baseline** (0.583, CI hi 0.755 < 0.90) where claude and gemini reach it.
   So part of gpt's let-alone difficulty is **channel-bounded** (uptake helps) and part
   **survives a genuinely-exercised wide channel** (it does not reach baseline). This is a
   *different* outcome from the relational-composition witness, where the wide channel took
   all three models to ceiling; here the channel takes the two stronger models to baseline
   and gpt only **part of the way**.
3. **This is the closest the record has come to the trigger-(b) contrast case — but it is a
   candidate, not a clean firing.** [`essay/output-channel-confound`](../essays/output-channel-confound.md)
   **trigger (b)** seeks "a serial-computation negative that *survives* a widened channel" —
   a negative the output-channel control *clears* (shows channel-controlled) rather than
   *dissolves*. gpt now externalizes the computation **and still falls short of the
   baseline** — the shape (b) describes. But "survives" is doing careful work: gpt did not
   *persist near chance* (it improved to 0.583, well above the 0.33 floor), and the
   below-baseline residual rests on a within-item lift that is **underpowered** and a
   descriptive accuracy whose CI is wide. So (b) is registered as **partially fired /
   candidate**: the *direction* is the contrast case (a channel-controlled residual), the
   *power* is not yet there to call it clean. A powered re-run (more let-alone items, or the
   disjoint train-split items) is the next witness axis. *(Forward note, session 61: this
   outcome — a directional-but-underpowered easing — is read methodologically in
   [`essay/witness-seeking-economics`](../essays/witness-seeking-economics.md) §"The partial
   witness" as a **third** witness-search outcome between fire and clean miss, whose correct
   continuation is a **powered re-run of the same axis** — a power-resolution move the essay
   exempts from the "more of the same probe cannot" caution because the first run left a
   directional signal, not a null.)*
4. **The two stronger models confirm the scaffold is a valid, benign instrument.** claude
   (0.792 → 0.833) and gemini (0.917 → 0.875) both stay at the human baseline under forced
   decomposition (UNCHANGED, no DROP, gemini's −0.04 a non-significant 2/3 wobble), and the
   comp-correlative ceiling control is PRESERVED for all three. So forcing the scaffold did
   not *teach* the inference (it would have moved the already-ceiling control) and did not
   *break* the instrument — it is a clean way to *coerce uptake*, which is its only job here.
5. **The recurring model ordering holds.** gpt-5.4-mini is again the fragile member — weakest
   on let-alone in session 57, the non-uptaker in session 58, and now the only model whose
   let-alone stays below baseline even with uptake forced. The split (claude/gemini at
   baseline, gpt below) that session 58 first drew is **sharpened**, not dissolved, by
   forcing uptake: it is not merely that gpt declined the channel — given the channel and
   made to use it, gpt still does not reach the human level on this scalar construction.

## What this does and does not license

**Does license:** a project-owned, revisable statement that, with uptake **forced** (gpt now
works the steps 24/24, median 120 tokens), gpt-5.4-mini's let-alone accuracy is a **partial
output-channel effect** — forcing the working lifts it directionally (+0.21) but leaves it
**below the human baseline**, while claude and gemini sit at baseline. The format contrast
(offered vs forced surface) is a **within-model, internal contrast**; the per-construction
accuracy-vs-0.90 leg is anchored for comp-correlative (ratified) and descriptive for
let-alone (same scoping as sessions 57/58).

**Does NOT license:**
- **A clean trigger-(b) firing / "gpt cannot do let-alone."** The undischargeable-negative
  discipline forbids "cannot"; and the below-baseline residual rests on an **underpowered**
  within-item lift (p = 0.090) and a wide descriptive CI. The honest claim is a *candidate*
  channel-controlled residual, not a demonstrated one.
- **A "channel artifact for gpt too" reading.** gpt did **not** lift to the baseline the way
  claude/gemini did; forcing uptake closed only *part* of the gap. So the session-58 result
  page's open question ("is gpt's let-alone a channel artifact or a real bound?") resolves to
  **partly each**, not to "artifact."
- **A "models have scalar-construction meaning" verdict.** Answer-key agreement under
  possible contamination (let-alone items are public; see session 57 *Limits*). The robust
  signals are the **uptake manipulation** (gpt's 8→120 token jump) and the **within-model
  contrasts**; the absolute match to 0.90 inherits the contamination caveat.
- **A tight magnitude.** n = 24; CIs are wide; the gpt +0.21 is directional, not
  sign-test-significant. The pre-registered verdict is UNCHANGED for all three.

## Limits

- **Small N, single run/date/scaffold.** let-alone n = 24; one forced-decomposition design.
  The within-item paired design removes between-item variance, but with only 9 discordant
  gpt pairs the sign test cannot clear 0.05 on a +0.21 shift — this is a **power** bound,
  stated not retuned. A powered re-run (more items) is the obvious next step.
- **Forced decomposition conflates "uptake" with "a structured scaffold."** The 3-step
  scaffold both *forces* externalization and *structures* it. Because the scaffold is
  construction-neutral and answer-blind (it cannot teach the let-alone scale), and because
  the ceiling control did not move, the structuring is not *teaching the inference* — but a
  free-form "you must write at least N words" uptake-forcer would isolate uptake from
  structure more cleanly. (Few-shot would add demonstration items and a governance question;
  forced decomposition was chosen as the lower-risk first arm.)
- **Contamination (inherited).** Public items; a *match* cannot distinguish learned
  construction-meaning from memory. The robust signals are the uptake jump and the
  within-model contrasts, both relative.
- **Shared priors (charter §2.5).** The human baseline (Scivetti, aggregate) is the
  independent bearing for the accuracy leg; the format/uptake contrast is model-internal.

## Provenance

- Human anchor: [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  (CxNLI Exp-1 gold + ≈0.90 native-speaker baseline; ratified 2026-05-29).
  Source: [`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md).
- Operationalization (NLI answer-key) governed by the already-ratified
  [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md);
  the forced-decomposition format is an instrument extension under it (no new decision owed;
  independent pre-run critic GO, fresh agent).
- Mechanism plausibility for the channel effect (serial computation needs a surface):
  [`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md), via
  [`essay/output-channel-confound`](../essays/output-channel-confound.md).
- No license upstream → read in place, **not mirrored**; the working-surface CoT (which
  restates source text) is **gitignored** under `raw/cot/`; the committed artifact is
  `raw/{slot}-labels.json` (item_id + gold + label + parse_mode + uptake + content sha256 +
  usage, NO text). Numbers reproducible from the committed `raw/` + `analyze.py` + the
  session-57/58 `raw/` against a local Scivetti clone. Independent post-run verifier (fresh
  agent) **REPRODUCED** every accuracy, Wilson CI, paired count, sign-test p-value, the
  uptake manipulation check (gpt 8→120 token median, 24/24 worked), the billed cost, parse
  integrity, the `content_sha256`↔CoT binding, CoT genuineness (the 3 numbered steps
  genuinely present and on-topic), and no gold-leak path.

## Status

`status: proposed`, `contingent-on: []` (the governing operationalization decision and the
Scivetti anchor are both ratified). What is `proposed` is the project's reading. Promotion
past `proposed` awaits Tom's review and a **powered** robustness arm on gpt's below-baseline
residual (more let-alone items, the disjoint train-split items, or a free-form uptake-forcer
that separates uptake from scaffold structure — the next witness axes the
undischargeable-negative discipline names). *(Governance note, s183: since the autonomous-era
amendment of 2026-06-12 — [`PROJECT.md`](../../../PROJECT.md) §12.3 — promotion runs by autonomous
cross-session adversarial review; Tom holds a standing override. The promotion in fact landed:
[`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md), s177.)*
