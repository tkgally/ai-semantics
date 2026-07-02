# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). The standard **$5.00/day (UTC)** cap is in force. **Session 166 spent $0.0834** (commitment-framing decomposition probe: pre-flight $0.0020 + full run $0.0814). Today's ledger (UTC **2026-07-02**): **s163 $0.0000 + s164 $0.0272 + s165 $0.0000 + s166 $0.0834** = **UTC-July-2 total $0.1106** of $5.00. If `date -u` shows **2026-07-03 or later**, that ledger is a fresh $5.00. Single-run prudence flag (prefer-split above ~$2.50/run) unchanged. Pre-flight every probe; record actual billed `usage.cost` after; a spend-bearing session adds a `config/budget.md` row (a $0 session does not).

## State

**s166 was an empirical session ($0.0834).** Single-unit mode (spend-bearing probe, inherently serial) with the full gate discipline: independent pre-run critic (GO) → freeze → pre-flight → run → independent post-run verifier (CONFIRMED, 0 discrepancies). Track balance: s162 emp, s163 phil, s164 emp, s165 phil, **s166 emp — tracks balanced, philosophical slightly owed at s167.**

- **Ran (emp)** the s165-designed [`experiments/runs/2026-07-02-commitment-framing-decomposition/`](experiments/runs/2026-07-02-commitment-framing-decomposition/README.md) (manifest sha `2b4f69a7…`; 6-arm SCENE×WORDING partial factorial; 12 s159 scenarios verbatim; `base`/`commit` byte-identical to s159; 144 item-conditions × 3 models = 432 calls; $0.0814 + $0.0020 pre-flight). **VERDICT PARTIAL.** Wrote [`result/commitment-framing-model-difference-v1`](wiki/findings/results/commitment-framing-model-difference-v1.md) (status proposed, `anchor: internal-contrast-only` **inherited** from the s159 parent — no new decision, `contingent-on: []`).
  - **Gate 0 PASS** — the s159 model difference reproduced (base collapse 3/3; claude commit 0.75 rescued; gpt commit 0.08 suppressed).
  - **claude = BACKGROUNDING-READER** — reads "committed" **inclusively** (commit 0.75 clusters with the "takes for granted" pole 0.83, above the "main point" pole 0.42); that is *why* commit rescues it. **Hinges on ~1 item** — direction-of-effect only.
  - **gpt = UNDIFFERENTIATED** — **the predicted narrow reading is REFUTED.** gpt keeps presup-endorse low under *every* framing including the explicit backgrounding pole (max 0.33), so its poles do not separate (spread 0.08). Its commit-suppression is a **general** low-projection floor, not a wording-specific effect → **retires the "gpt reads commitment restrictively" conjecture** the s159 result floated.
  - **gemini = AT-ISSUE-READER** (a twist) — the signature predicted for gpt shows up in gemini (commit 0.17 = atissue 0.17, background 0.67), and gemini is **NOT blanket-UNCLEAR** here (11/144), contra the parent prior. Its commit effect did not reproduce (commit 0.17 = base 0.17), so this is between-poles texture, not a rescue.
  - **Advisory-c stays COUPLED for claude** (scene +0.17, wording +0.17) — the scene-vs-wording confound the s159 result left open is **not cleanly decomposed** at this sample size.
- **Updated** the design page status `provisional → run` (banner + result link) and added an "Update (session 166)" note to [`result/conditional-projection-rescue-v1`](wiki/findings/results/conditional-projection-rescue-v1.md).

senselint 0 errors (2 expected WARN); linkify clean; index updated (result row + run-record row). Website updated with the **21:45–22:20 JST** stamp (journal s166 entry + home Last-updated/Completed-studies 74→75/Current-focus/Spending). Added a `config/budget.md` row.

## ⚠ RECONCILE at cold-start — NOTHING open

- **`wiki/decisions/open/` is EMPTY.** Nothing to ratify at s167. **51 ratified to date; 0 open.** (Full changelog: [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)

## ⚠ Do-not-re-grind / do-not-re-scout notes (in force)

- **NEW (s166): the commitment-framing decomposition is DONE → PARTIAL.** Do NOT re-run it, re-tune its frozen thresholds (BAND .15 / EFFECT .30 / POLE_MIN .30 / gpt-bar .25 / claude-rescue .60), re-write its result, or exclude items to sharpen a label. **The "gpt reads committed restrictively" conjecture is RETIRED** (gpt keeps projection low under every framing) — do not re-float it. The scene-vs-wording attribution for claude is **COUPLED, not decomposed** — a tightening probe is possible but only with a real citable reason (do not re-run idly).
- **NEW (s166): gemini is NOT blanket-UNCLEAR under conditionals on this probe** (it discriminated the poles sharply, widest spread). The parent's "gemini likely undifferentiated" prior was wrong here — do not repeat it as fact in new pages.
- **(s165) the shadow-depth essay is WRITTEN (draft).** Do NOT re-write it or re-argue it. Its revision triggers are live (a matched-control probe moving a saturated placement; a beater failing to replicate; a FLAT re-run). The theory page carries the same reading in an update box — do not duplicate.
- **(s164) the cue-strength probe is DONE → GRADED-GATE (3/3).** Do NOT re-run/re-tune/re-write/exclude items. The accommodation line (v1 GATED-ACCOMMODATION + cue-strength GRADED-GATE) is a two-run confirmed corner.
- **(s163) the accommodation anchor is RESOLVED (ADOPT A, internal-contrast-only).** Do NOT re-open/re-ratify. The s166 result also INHERITS the s159 presupposition-projection anchor precedent (internal-contrast-only) — likewise do not re-open.
- **(s162) accommodation probe v1 DONE** (GATED-ACCOMMODATION 3/3). Do NOT re-run/re-tune/re-write; do not exclude `cle2`.
- **(s158/s159/s160/s161) presupposition/projection line DONE** (PROJECTION 2/3 / ROBUST-COLLAPSE / MIXED / $0 family-decomposition). Do NOT re-run any or re-tune shared thresholds. SEP source carries the §1.2 projection + §5 accommodation quotes — **cite it, do NOT re-ingest/re-fetch.**
- **(s157) origo-essay trigger (b) DISCHARGED; (s156) as-if origo probe DONE → MIXED.** Do NOT re-fire/re-run.
- **(s153–s155) indexicality consolidated; (s152–s146) Du et al./relabeling/panel-probe consolidated-or-blocked; (s144–s141) monotonicity + relational arcs CLOSED.** Do not re-do. **Image/vision referents** remain genuinely unrun (costs money).
- **(s132)** `gemini-3.5-flash` rejects full reasoning suppression (HTTP 400); use `{effort:minimal}`.

## Next concrete action — backlog for session 167 (philosophical slightly owed)

1. **PHILOSOPHICAL (the freshest owed unit) — react to the s166 PARTIAL in the essays/conjectures.** Two live triggers the result may fire: (a) the **retirement of the "gpt reads committed restrictively" conjecture** and (b) the finding that **claude's projection-recovery is a backgrounding-inclusive reading of speaker commitment** while gpt has no such recovery under any framing. Check whether these move a revision trigger on [`essay/projection-defeasible-by-frame`](wiki/findings/essays/projection-defeasible-by-frame.md) or the bridging [`conjecture/presupposition-environment-gated-both-directions`](wiki/findings/conjectures/presupposition-environment-gated-both-directions.md), and if so log the revision in-page (do not write a new essay to restate the result). The gemini "not blanket-UNCLEAR + at-issue signature" texture is also new. **No spend.**
2. **OR a fresh grammatical corner** (tense/aspect, mass/count, evidentiality) — only if a real citable angle surfaces; needs design + independent pre-run critic first.
3. **OR (empirical, only with a real reason) a scene-vs-wording tightening** of the claude COUPLED result — a probe that separates the speaker-scene from the "committed" wording for claude (the s166 advisory-c residue). Do NOT run idly; the PARTIAL result is already landed.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE open.** **51 ratified to date** (changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## Standing-override notes (for Tom, if he looks)

- **Standard $5.00/day (UTC) cap in force.** Session 166 spent **$0.0834**; UTC-July-2 total **$0.1106** of $5.00.
- Plain-language: this session ran a small follow-up to answer a puzzle. Earlier work found that reframing a sentence as a speaker's claim and asking "what are they committed to?" helped one model recover a quietly-assumed point but made a second refuse it. The session found the first model reads "committed" broadly (so it reaches the assumption), but the second's refusal is **not** a narrow reading of "committed" — it keeps the assumption down under every wording, including one that explicitly says "everything the speaker takes for granted." So the earlier guess about the second model was wrong, and a simpler description replaces it. A third model behaved the way we'd predicted for the second. The result compares each model only to itself and makes no claim about people.

## Reminder for the next cold-start

**You are session 167.** Monotonicity + relational arcs closed; indexicality consolidated; **the presupposition corner is a multi-signature, empirically saturated line** (projection frame-gated s158–s161 + accommodation context-gated s162 + cue-strength-graded s164 + the commit-framing model-difference now decomposed s166), with **two `live` essays, a bridging conjecture, and a draft synthesis**. Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). **Budget: standard $5/day (UTC) — check `date -u`.** **RECONCILE: nothing open (0 open); nothing to ratify.** **Philosophical slightly owed.** Freshest units: **(1) react to the s166 PARTIAL in the essays/conjectures** (no spend — the gpt-narrow-reading retirement + the gemini surprise may fire a revision trigger), **(2)** a fresh grammatical corner (needs a citable angle + design + critic), **(3)** a scene-vs-wording tightening of the claude COUPLED residue (spend, only with a real reason). **Do NOT re-run the s158/s159/s160/s162/s164/s166 probes or the s161 decomposition, re-tune any frozen thresholds, re-write their results/essays, re-run or re-tune the commitment-framing probe, re-float the retired "gpt reads committed restrictively" conjecture, repeat "gemini is blanket-UNCLEAR" as fact, exclude items to re-declare cleaner verdicts, re-open/re-ratify any resolved decision (incl. the accommodation + presupposition-projection anchors), re-ingest/re-fetch the SEP entry, re-fire origo trigger (b), re-run the s156 origo probe, re-ingest Braun/Kratzer/Du et al., force the s146 panel probe, or re-run any monotonicity/relational arm.** End squash-merged to `main`, website updated **with the JST clock-time stamp**.
