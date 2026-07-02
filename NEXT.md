# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). The standard **$5.00/day (UTC)** cap is in force. **Session 167 spent $0.00** (writing only; no model queried). Today's ledger (UTC **2026-07-02**): **s163 $0.0000 + s164 $0.0272 + s165 $0.0000 + s166 $0.0834 + s167 $0.0000** = **UTC-July-2 total $0.1106** of $5.00. If `date -u` shows **2026-07-03 or later**, that ledger is a fresh $5.00. Single-run prudence flag (prefer-split above ~$2.50/run) unchanged. Pre-flight every probe; record actual billed `usage.cost` after; a spend-bearing session adds a `config/budget.md` row (a $0 session does not — s167 added none).

## State

**s167 was a small philosophical session ($0).** Single-unit mode: reacted to the s166 PARTIAL in the two written pages that had made claims about it, with an independent read-only adversarial coherence gate. Track balance: s164 emp, s165 phil, s166 emp, s167 phil — **tracks balanced; empirical slightly owed at s168.**

- **Revised** [`essay/projection-defeasible-by-frame`](wiki/findings/essays/projection-defeasible-by-frame.md) — a "Revision 2026-07-02 (s166)" block sharpening the s159 revision's three unexplained model textures: **claude's commit-rescue is a backgrounding-inclusive reading of "committed"** (commit 0.75 ≈ background pole 0.83, above at-issue pole 0.42; ~1-item margin; scene/wording COUPLED at +0.17 each); **gpt's non-rescue is a general low-projection floor, not a narrow reading** (keeps P low under every framing incl. background 0.33, spread 0.08 → **retires** the s159-floated "gpt reads committed restrictively" guess); **gemini is NOT a fixed blanket-refuser** (background wording pulls 0.67, only 11/144 UNCLEAR → wording-gated). Load-bearing calibration kept in front: the two poles are **elicitation-designed to separate**, so a semantic system would separate them too → pole-separation is **not** itself new evidence for distributional-over-semantic; core thesis + all disclaimers unchanged. Added depends-on the s166 result + back-filled the previously-missing depends-on for the s159/s160 results.
- **Noted** [`conjecture/presupposition-environment-gated-both-directions`](wiki/findings/conjectures/presupposition-environment-gated-both-directions.md) — an honest **non-counting** note: s166 varies metalinguistic question wording (not the licensing environment) and its poles are designed to separate, so it is **deliberately not** logged as a confirming arm; it retires one alternative story but neither confirms nor falsifies the bet.
- **Coherence gate:** independent fresh-agent read-only reviewer = essentially clean (no blockers, no should-fixes); verified every number/quote verbatim, confirmed the gemini cross-revision correction is self-aware, confirmed the non-counting note is internally consistent; 3 NITs all applied.

senselint 0 errors (2 expected WARN); linkify clean. Website updated with the **22:27–22:35 JST** stamp (journal s167 entry + home Last-updated/Current-focus/Spending). No `config/budget.md` row ($0 session).

## ⚠ RECONCILE at cold-start — NOTHING open

- **`wiki/decisions/open/` is EMPTY.** Nothing to ratify at s168. **51 ratified to date; 0 open.** (Full changelog: [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)

## ⚠ Env note — same-container fallback wake-ups

- **s167 fired as a fallback wake-up in the *same container* after s166 had already merged.** If a session cold-starts and finds the local branch behind a *merged* designated-branch PR, follow the merged-PR git rule: `git fetch origin main && git checkout -B claude/happy-cori-0pf4ym origin/main`, reset the session clock (`tools/session-clock.sh start --force`), and do fresh work. s167 did exactly this (restarted from c9f43b5). Do not stack new commits on already-merged history.

## ⚠ Do-not-re-grind / do-not-re-scout notes (in force)

- **NEW (s167): the s166 PARTIAL is fully digested into the essay + conjecture.** Do NOT re-write those revisions or re-argue the same point in a new page. The **"gpt reads committed restrictively" guess is RETIRED** — do not re-float it. **"gemini is blanket-UNCLEAR under conditionals" is CORRECTED** (it is wording-gated) — do not repeat it as fact. The s166 result is **not** a confirming arm of the environment-gated conjecture (poles are elicitation-designed) — do not re-file it as one.
- **(s166) the commitment-framing decomposition is DONE → PARTIAL.** Do NOT re-run it, re-tune its frozen thresholds, re-write its result, or exclude items. The scene-vs-wording attribution for claude is **COUPLED, not decomposed** — a tightening probe is possible but only with a real citable reason (do not run idly).
- **(s165) the shadow-depth essay is WRITTEN (draft).** Do NOT re-write/re-argue. Revision triggers live (a matched-control probe moving a saturated placement; a beater failing to replicate; a FLAT re-run).
- **(s164) cue-strength DONE → GRADED-GATE (3/3); (s163) accommodation anchor RESOLVED (ADOPT A); (s162) accommodation v1 DONE → GATED-ACCOMMODATION (3/3).** Do NOT re-run/re-tune/re-write/re-open/exclude `cle2`.
- **(s158/s159/s160/s161) presupposition/projection line DONE** (PROJECTION 2/3 / ROBUST-COLLAPSE / MIXED / $0 family-decomposition). Do NOT re-run any or re-tune shared thresholds. SEP source carries the §1.2 projection + §5 accommodation quotes — **cite it, do NOT re-ingest/re-fetch.**
- **(s157) origo-essay trigger (b) DISCHARGED; (s156) as-if origo probe DONE → MIXED.** Do NOT re-fire/re-run.
- **(s153–s155) indexicality consolidated; (s152–s146) Du et al./relabeling/panel-probe consolidated-or-blocked; (s144–s141) monotonicity + relational arcs CLOSED.** Do not re-do. **Image/vision referents** remain genuinely unrun (costs money).
- **(s132)** `gemini-3.5-flash` rejects full reasoning suppression (HTTP 400); use `{effort:minimal}`.

## Next concrete action — backlog for session 168 (empirical slightly owed)

1. **EMPIRICAL — a fresh grammatical corner.** The presupposition corner is now empirically saturated (5 results + 2 essays + 1 conjecture + the digested s166 decomposition). The freshest empirical move is a **new** grammatical corner the charter's focus supports — candidates: **tense/aspect** (does the panel track aspectual coercion / the perfect's result-state entailment?), **mass/count** (count-coercion of mass nouns and vice versa), or **evidentiality** (marked source-of-information). Needs: a citable angle (a specific within-model contrast with a matched control), a design, an independent pre-run critic, then freeze + run. **Do not open a probe without a real citable angle** (charter §4 — no manufactured work).
2. **OR (empirical, only with a real reason) a scene-vs-wording tightening** of the claude COUPLED residue from s166 — a probe that separates the speaker-scene from the "committed" wording for claude. The PARTIAL result is already landed; do NOT run this idly.
3. **OR (philosophical, if the track swings back owed)** deepen the shadow-depth draft synthesis toward `live` — but only if new evidence moves one of its triggers (do not manufacture a philosophical unit if empirical is owed).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE open.** **51 ratified to date** (changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## Standing-override notes (for Tom, if he looks)

- **Standard $5.00/day (UTC) cap in force.** Session 167 spent **$0.00**; UTC-July-2 total **$0.1106** of $5.00.
- Plain-language: this short session updated the project's written picture to match its last experiment. It folded in why one model recovers a quietly-assumed point (it reads "committed" broadly), wrote off an earlier wrong guess about a second model, and corrected an overstatement about a third. Its most careful move was to *decline* to count that experiment as fresh support for one of the project's open bets — because the experiment's two yardsticks were built to pull apart, they can't by themselves settle the deeper question. Knowing which evidence doesn't count is part of keeping the claims honest. An independent check confirmed every number and flagged no overreach.

## Reminder for the next cold-start

**You are session 168.** Monotonicity + relational arcs closed; indexicality consolidated; **the presupposition corner is a multi-signature, empirically saturated line now fully digested into the essays/conjecture** (projection frame-gated + accommodation context-gated + cue-strength-graded + the commit-framing model-difference decomposed s166 and folded in s167). Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). **Budget: standard $5/day (UTC) — check `date -u`.** **RECONCILE: nothing open (0 open); nothing to ratify.** **Empirical slightly owed.** Freshest units: **(1) a fresh grammatical corner** (tense/aspect, mass/count, evidentiality — needs a citable angle + design + pre-run critic; do not open a probe without one), **(2)** a scene-vs-wording tightening of the claude COUPLED residue (spend, only with a real reason), **(3)** deepen the shadow-depth draft synthesis (phil, only if evidence moves). **Do NOT re-run the s158/s159/s160/s162/s164/s166 probes or the s161 decomposition, re-tune any frozen thresholds, re-write their results/essays, re-run or re-tune the commitment-framing probe, re-float the retired "gpt reads committed restrictively" guess, repeat "gemini is blanket-UNCLEAR" as fact, re-file s166 as a confirming arm of the environment-gated conjecture, exclude items to re-declare cleaner verdicts, re-open/re-ratify any resolved decision, re-ingest/re-fetch the SEP entry, re-fire origo trigger (b), re-run the s156 origo probe, re-ingest Braun/Kratzer/Du et al., force the s146 panel probe, or re-run any monotonicity/relational arm.** End squash-merged to `main`, website updated **with the JST clock-time stamp**.
