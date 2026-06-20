# PRE-REGISTRATION (FROZEN) — let-alone FORCED-DECOMPOSITION (uptake-inducing) probe

> **FROZEN 2026-06-20 (session 60, UTC).** A FRESH independent pre-run critic returned
> **GO** (all 8 adversarial checks PASS; single-manipulated-variable diff confirmed
> byte-level [common prefix 337 chars = intro + 3 verbatim 0/1/2 definition lines, only
> the trailing instruction differs]; no gold/answer leak; no demonstration items; no new
> decision owed; shas verified == sessions 57/58; parser target-blind; verdict map +
> uptake manipulation-check pre-registered incl. the honest "uptake-not-induced ->
> method-null" branch; no shortcut surface; budget fits). One non-blocking note: gpt's
> session-58 "16/24 bare" is precisely 15 answers at 8 tokens + 1 at 14 tokens
> (descriptive motivation only; feeds no verdict — the analyzer uses the >=30-token uptake
> proxy). The draft below is the frozen pre-registration.

## 1. Question

Session 58's working-surface probe
([`result/scivetti-let-alone-working-surface-v1`](../../../wiki/findings/results/scivetti-let-alone-working-surface-v1.md))
found that the phrasal scalar **let-alone**'s session-57 forced-single-token near-chance
failure is **substantially an output-channel artifact for 2 of 3 models**: claude
(0.542→0.792) and gemini (0.667→0.917) each lifted ~25 points on the *same items* to the
≈0.90 human baseline once *offered* a working surface. But **gpt-5.4-mini did not recover**
(0.458→0.375) — and the verifier found *why*: it **largely declined the offered surface**
(16/24 bare one-token `FINAL: N` answers, median 8 completion tokens, 0 reasoning tokens).
So gpt's persistence is **channel-NOT-TAKEN-UP**, not a clean channel-controlled survival.

[`essay/output-channel-confound`](../../../wiki/findings/essays/output-channel-confound.md)
was sharpened in session 59 — its body now states (subsection *"Offering a channel is not
exercising it: uptake as a control condition"*) that a clean **trigger-(b)** test (a serial
negative that *survives* a widened channel) must **vary the channel actually USED, not
merely the channel offered; verify uptake model-by-model; read a declined surface as
inconclusive (channel-not-taken-up), never a survival.** The session-58 result page names
the remedy explicitly: *"the clean (b) test now needs an arm that induces uptake (few-shot
demonstrations of working the scale, or a forced-decomposition prompt)."*

**So:** when gpt is FORCED to externalize the working steps on the same 24 let-alone items,
does its accuracy (a) **lift** toward the baseline — meaning the let-alone failure was an
output-channel artifact for gpt too — or (b) **persist** near chance with uptake genuinely
induced — the first clean firing of trigger (b): a serial negative surviving an
actually-exercised wide channel? This is the lowest-governance-risk uptake arm the essay
prescribes.

## 2. Design — uptake-inducing, single manipulated variable

The **only** changed variable vs the session-58 baseline is the **response format**:
session 58 *offered* a free-form working surface; this run *requires* the working steps
via a construction-neutral, answer-blind 3-step decomposition scaffold.

| | session 58 (baseline: offered) | this run (forced) |
|---|---|---|
| output instruction | "Think it through step by step. Then ... `FINAL: <0,1,2>`" | "You MUST show your work. Before answering write out three numbered steps — 1. PREMISE (paraphrase) / 2. HYPOTHESIS (paraphrase) / 3. LINK (does the premise force the hypothesis true / open / false, and why) — only THEN `FINAL: <0,1,2>`" |

Everything else is **held byte-identical** to sessions 57/58:

- **Items:** the SAME 24 let-alone + 30 comparative-correlative test items (subset
  sha256 `9be31a8fea8d7f16`; full-set sha `1c5cffb18c5ef78e` == sessions 57/58's, verified
  by `prep.py --check` — same corpus, re-cloned upstream @ `82699473`). Gold NOT shown.
- **0/1/2 label definitions:** the three definition lines of the system prompt are
  **copied verbatim** from session-57/58 `NLI_SYS`.
- **Scoring:** 3-way NLI label vs the same per-item gold, vs the ≈0.90 native-speaker
  baseline. (Does NOT change WHAT is scored — only HOW the label is produced.)
- **Panel:** A claude-sonnet-4.6 / B gpt-5.4-mini / C gemini-3.5-flash, temperature 0.
- **Reasoning-effort knob HELD CONSTANT:** gemini stays `effort: minimal` — so the
  contrast isolates the **output channel** (uptake), not the reasoning budget.

**The scaffold is construction-neutral and answer-blind.** It names no construction, no
scale, no let-alone semantics. Step 3 only restates the same 0/1/2 trichotomy already in
the verbatim definitions ("force true / leave open / force false" = entailment / neutral /
contradiction), so it adds **no information** — it forces the *general* entailment check to
be **externalized**. There are **no demonstration items** (forced decomposition, NOT
few-shot), so no scoring leak / gold leak is possible. The scaffold applies identically to
the comp-correlative control.

**Cells.** let-alone (n=24) — the TARGET; comparative-correlative (n=30) — a CEILING
CONTROL (forced-format 1.0/0.9/1.0; offered-surface 1.0/0.967/1.0) that guards against
"the scaffold broke the instrument."

## 3. No new operationalization decision owed

This is a **format/instrument extension** under the already-ratified Scivetti answer-key
anchor (ratified 2026-05-29, Tom) and the ratified
`constructional-divergence-operationalization` decision. It does **not** alter what is
scored against the human gold (same labels, same gold) — only how the label is produced.
**There are no demonstration items**, so the NEXT.md governance caveat ("few-shot adds
demonstration items, so check whether the demonstrations could leak/alter scoring") does
**not** apply — forced decomposition was named the lower-governance-risk option for exactly
this reason. Precedent: session 58 ("format-only ... no new decision owed"). The pre-run
critic must confirm this judgement. `wiki/decisions/open/` is empty; nothing to ratify.

## 4. Pre-registered analysis & verdict map (frozen in `analyze.py`)

**Q1 — anchored leg (per-construction accuracy under forced decomposition).** Per model,
per construction: accuracy + Wilson 95% CI vs human 0.90. comparative-correlative carries
the **ratified anchor**; let-alone is **descriptive** from the same human release (not
individually anchored), exactly as sessions 57/58.

**Q2 — the headline uptake contrast (internal-contrast-only).** Within-item paired
comparison vs the **session-58 offered-surface** labels (matched by `item_id`):
- `b` = offered-WRONG → forced-decomp-RIGHT (gains); `c` = offered-RIGHT → fd-WRONG (losses).
- One-sided exact binomial (sign) test on the `b+c` discordant pairs.
- Per-(model, construction) verdict:
  - **LIFTS** : fd_acc > offered_acc AND P(X≥b | n=b+c, 0.5) < 0.05
  - **DROPS** : fd_acc < offered_acc AND P(X≥c | n=b+c, 0.5) < 0.05
  - **UNCHANGED** : otherwise.
- Control guard (comp-correlative): **PRESERVED** if its fd Wilson CI contains the
  offered-surface acc; else FLAG.
- Session-57 forced accuracy is also reported per construction for the
  forced→offered→forced-decomp progression (descriptive context, not a verdict input).

**Q3 — the UPTAKE MANIPULATION CHECK (what makes the trigger-(b) reading clean).** On the
target, per model: the fraction of let-alone items "worked" (≥40 pre-`FINAL` chars and ≥2
numbered step markers, from the committed `uptake` field) and the completion-token
distribution, reported alongside session 58's offered-surface uptake (proxied by
completion_tokens ≥ 30, since session 58 has no `uptake` field — its bare answers were ~8
tokens, its worked answers 200+). This is the test that the manipulation *did its job*.

**Pre-committed interpretation (no retuning after seeing results):**
- **gpt's uptake RISES (now mostly works) AND gpt LIFTS** (fd_acc > offered, sign test
  clears) toward the baseline → the let-alone failure was an **output-channel artifact for
  gpt too**; trigger (b) returns **negative** for a depth-1 scalar bound (the channel,
  once *used*, absorbs the serial work); `output-channel-confound` corroborated; the
  session-58 "gpt channel-not-taken-up" hole is **closed in the lift direction**.
- **gpt's uptake RISES (now mostly works) AND gpt stays UNCHANGED** near chance while the
  control stays PRESERVED → the **first clean firing of trigger (b)**: a serial negative
  that **survives a genuinely-exercised wide channel**. Per
  [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md)
  this is still **not** a capability-absence, but it IS the first let-alone result that is
  channel-*controlled* rather than channel-*not-taken-up* — a real, bounded scalar
  difficulty for gpt that the next witness axis (few-shot, train-split items) would probe.
- **gpt's uptake does NOT rise** (the scaffold failed to induce uptake — e.g. gpt still
  emits bare answers despite "you MUST") → the manipulation **failed**; report Q3 as
  uptake-not-induced, give **no** clean trigger-(b) verdict for gpt, and the next arm is
  few-shot. (This is the honest null on the *method*, pre-committed.)
- **claude/gemini** (already lifted under the offered surface): forced decomposition is
  expected to **preserve** their baseline-level accuracy (UNCHANGED or LIFTS vs offered);
  a DROP would FLAG the scaffold as harmful and is reported as such. They are the
  manipulation check that the forced scaffold is a *valid* instrument, not a degrading one.
- If the control **FLAGs** (degrades) for any model → the scaffold changed the instrument
  too much to read the target cleanly for that model; report as instrument-uninterpretable.

n is small (let-alone n=24); the paired design removes between-item variance, so a large
channel effect is detectable, but a small one may not be — stated as a power bound, not
retuned away.

## 5. Cost & integrity

- Pre-flight estimate: **~$0.35–0.50** billed (54 items × 3 models = 162 calls). Forced
  decomposition makes gpt write working it skipped in session 58 (8→~150+ tokens), so gpt
  costs more than session 58's $0.015; claude/gemini ≈ session 58 (they already worked).
  `ABORT_USD = 0.80`; far under the $2.50 single-run flag and the daily cap.
- Budget context: UTC-day 2026-06-20 spend before this run = **$3.791** (sessions
  51+53+57+58). The temporary $10 cap expires 15:00 UTC 2026-06-20; from then the standard
  **$5.00/day** applies. Even at the standard $5 cap the headroom (**$1.209**) covers this
  ~$0.40 run with margin; the run will not take the UTC-day total over $5.
- Integrity: `usage.cost`-summed (0-missing target); parse modes logged (tagged vs
  fallback); unparseable never dropped silently; the `uptake` field (lengths/booleans only)
  committed for the manipulation check. **Recipe-not-corpus:** the response restates the
  unlicensed source text, so full CoT is **gitignored** under `raw/cot/`; the committed
  artifact is `raw/{slot}-labels.json` (item_id + gold + label + parse_mode + uptake +
  content sha256 + usage, NO text).
- Cadence: this draft → FRESH independent pre-run critic GO → commit as `PREREG.md` →
  probe (background) → FRESH independent post-run verifier REPRODUCES from raw → result page.
