# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). The standard **$5.00/day (UTC)** cap is in force. The 2026-07-02 **special session** (Tom-directed, unnumbered) spent **$0.00** (no model queried). Today's ledger (UTC **2026-07-02**): s163 $0.0000 + s164 $0.0272 + s165 $0.0000 + s166 $0.0834 + s167 $0.0000 + special $0.0000 = **UTC-July-2 total $0.1106** of $5.00. If `date -u` shows **2026-07-03 or later**, that ledger is a fresh $5.00. **Sizing rule (NEW, [`PROTOCOL.md`](PROTOCOL.md) §4):** a claim-carrying probe uses powered N (~100–150 items); the cap is a ceiling, not a target, but chronic under-use on load-bearing lines is a defect. Single-run prudence flag (prefer-split above ~$2.50/run) unchanged. Pre-flight every probe; record actual billed `usage.cost`; a spend-bearing session adds a `config/budget.md` row.

## State — the program era starts here

**A special Tom-directed session (2026-07-02, unnumbered — the next Routine session is 168) adopted the session-165 external review as the standing program and rebuilt the steering layer.** Full record: [`wiki/decisions/resolved/program-2026-07-adoption.md`](wiki/decisions/resolved/program-2026-07-adoption.md); the review itself: [`project-history/20260702-ai-semantics-review-by-fable.md`](project-history/20260702-ai-semantics-review-by-fable.md). What is new:

- **[`wiki/program.md`](wiki/program.md)** — the standing program (empirical A1–A6, consolidation B1–B6, process C, Tom-held levers D). **Read it right after this file**; unit selection is program-guided now; tick items you advance in the same commit.
- **`PROTOCOL.md` §3–§4 (new)** — program discipline (claims-promotion reviews, theory-edition rule, essay bar, instrument stopping rule, prediction ledger) and probe sizing. **§2:** each ratification and pre-run critique now routes **one vote through a non-Anthropic panel model** (`config/models.md`). **§1:** no session clock; cold-start reading path is NEXT → program → index (scan).
- **`wiki/index.md` is generated** — run `python3 tools/build-index.py` as verification step 1; **never hand-edit the catalog** (it went 604 KB → ~107 KB, one line per page). Hand-edit only its header.
- **Website (Tom's rulings, 2026-07-02): one journal entry per JST calendar day** — a substantive session creates or extends **today's** entry; maintenance-only sessions skip the site; **no clock stamps** (`session-clock.sh` now optional). See `PROTOCOL.md §5b` / `docs/README.md`.
- **[`wiki/predictions.md`](wiki/predictions.md)** — the registered-bet ledger (seeded; historical back-fill owed, program B5). New bets add rows; outcomes update them same-session.
- **`note` page type** exists for no-measurement records ($0 gates, calibrations, re-analyses); the reclassification sweep of ~10 result pages is queued (program B6; create `wiki/findings/notes/` with the first one).
- **[`wiki/executive-summary.md`](wiki/executive-summary.md)** is re-scoped as a checkpoint digest (last full regeneration s124); a fresh regeneration is owed at the first consolidation session (program B4).
- Track balance: s164 emp, s165 phil, s166 emp, s167 phil → **empirical slightly owed at s168** (the special session was process-only and does not move the balance).

## ⚠ RECONCILE at cold-start — 3 decisions open (ALL eligible at s168)

Opened by the 2026-07-02 special session, so the cross-session boundary is satisfied at s168. Ratify per `PROTOCOL.md §2` (independent fresh-agent adversarial review **plus one non-Anthropic panel vote**); Tom may rule directly at any time. Ratifying 1 and 3 unblocks program items A4b/A4d:

1. [`wiki/decisions/open/scale-ladder-subjects.md`](wiki/decisions/open/scale-ladder-subjects.md) — within-family capability siblings as *supplementary* subjects on frozen flagship instruments (provisional default: ADOPT, 2 families first, `ladder`-flagged, panel-v1 stays primary).
2. [`wiki/decisions/open/panel-v2-refresh.md`](wiki/decisions/open/panel-v2-refresh.md) — whether/when to refresh the default panel (provisional default: decide with ladder data; v1 primary meanwhile).
3. [`wiki/decisions/open/logprob-supplementary-lane.md`](wiki/decisions/open/logprob-supplementary-lane.md) — re-verify the stale logprob catalog, then (if ≥2 decorrelated families survive) a flagged supplementary graded lane (provisional default: re-verify + one pilot).

**52 resolved to date** (changelog: [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Env note — same-container fallback wake-ups

If a session cold-starts and finds its designated branch behind a **merged** PR, follow the merged-PR git rule: `git fetch origin main && git checkout -B <this-session's-designated-branch> origin/main`, then do fresh work. Never stack new commits on already-merged history. (Happened at s167; the rule is general.)

## ⚠ Do-not-re-grind / do-not-re-scout notes (in force)

- **(s167) the s166 PARTIAL is fully digested into the essay + conjecture.** Do NOT re-write those revisions or re-argue the same point in a new page. The **"gpt reads committed restrictively" guess is RETIRED** — do not re-float it. **"gemini is blanket-UNCLEAR under conditionals" is CORRECTED** (it is wording-gated) — do not repeat it as fact. The s166 result is **not** a confirming arm of the environment-gated conjecture (poles are elicitation-designed) — do not re-file it as one.
- **(s166) the commitment-framing decomposition is DONE → PARTIAL.** Do NOT re-run it, re-tune its frozen thresholds, re-write its result, or exclude items. The scene-vs-wording attribution for claude is **COUPLED, not decomposed** — a tightening probe is possible but only with a real citable reason (do not run idly).
- **(s165) the shadow-depth essay is WRITTEN (draft).** Do NOT re-write/re-argue. Revision triggers live (now also rows in [`wiki/predictions.md`](wiki/predictions.md)); the deciding controls are program items A1a/A1b — *running those is in-bounds and queued*, re-arguing the essay is not.
- **(s164) cue-strength DONE → GRADED-GATE (3/3); (s163) accommodation anchor RESOLVED (ADOPT A); (s162) accommodation v1 DONE → GATED-ACCOMMODATION (3/3).** Do NOT re-run/re-tune/re-write/re-open/exclude `cle2`.
- **(s158/s159/s160/s161) presupposition/projection line DONE** (PROJECTION 2/3 / ROBUST-COLLAPSE / MIXED / $0 family-decomposition). Do NOT re-run any or re-tune shared thresholds. SEP source carries the §1.2 projection + §5 accommodation quotes — **cite it, do NOT re-ingest/re-fetch.** (The A1a doppelgänger *control* and the A3a human re-anchoring scout are NEW work, not re-grinds.)
- **(s157) origo-essay trigger (b) DISCHARGED; (s156) as-if origo probe DONE → MIXED.** Do NOT re-fire/re-run.
- **(s153–s155) indexicality consolidated; (s152–s146) Du et al./relabeling/panel-probe consolidated-or-blocked; (s144–s141) monotonicity + relational arcs CLOSED.** Do not re-do. **Image/vision referents** remain genuinely unrun — now queued as program item A2b with explicit budget license (~$3–4).
- **(s132)** `gemini-3.5-flash` rejects full reasoning suppression (HTTP 400); use `{effort:minimal}`.

## Next concrete actions — backlog for session 168 (empirical owed; program-guided)

1. **RECONCILE the 3 open decisions first** (§above). Then pick 1–2 *deep* units, not many shallow ones (`PROTOCOL.md §3`):
2. **EMPIRICAL, program A1b (the teed-up shadow-depth row):** run [`conjecture/lexical-relation-shadow-saturation`](wiki/findings/conjectures/lexical-relation-shadow-saturation.md) in its **internal-contrast form** — the corpus-side controls are in-repo (Justeson & Katz; Cao); only the human-compared form stays blocked. Full gates: design → independent pre-run critic (with non-Anthropic vote) → freeze → run at powered N (§4) → post-run verifier → result + tick A1b + update the predictions row.
3. **OR EMPIRICAL, program A1a:** design the presupposition **surface-cue doppelgänger / cue-scrambled control** the shadow-depth essay names as owed (design + critic this session; freeze + run next).
4. **CONSOLIDATION, program B1 + C3 (good second unit):** the first **claims-promotion review** — strongest candidate: CC covariation (3 runs + controls) — per `PROTOCOL.md §3`; and/or close the two founding open-questions into the continuum theory page (C3), closure argued in-page.
5. **SCOUT, program A3a ($0):** license-check **CommitmentBank / MegaVeridicality / Tonhauser-Degen / NOPE** for the presupposition human re-anchoring; open the anchor decision with the scout results (adopt nothing unverified).
6. **Website** per `PROTOCOL.md §5b`: if the session lands substantive work, create or extend **today's** journal entry (one per JST day; no clock stamps).

## Open decisions

- [`scale-ladder-subjects`](wiki/decisions/open/scale-ladder-subjects.md) — **eligible** (opened 2026-07-02, special session)
- [`panel-v2-refresh`](wiki/decisions/open/panel-v2-refresh.md) — **eligible**
- [`logprob-supplementary-lane`](wiki/decisions/open/logprob-supplementary-lane.md) — **eligible**

## Standing-override notes (for Tom, if he looks)

- **Your 2026-07-02 instruction is implemented.** The review is adopted as [`wiki/program.md`](wiki/program.md); your two rulings (one journal entry per day; clock-stamp mandate dropped) are encoded in `PROTOCOL.md §5b` and `docs/README.md`. The journal-day unit is implemented as the **JST calendar day** (the site's dateline timezone); spend accounting stays UTC. The D-group levers (Routine cadence, the surprisal-lane key, paywalled ingestion, direct rulings on the three queued panel decisions) are documented in `program.md §D` — information, not requests.
- Plain-language: this special session turned the outside review of the project's first 165 sessions into a concrete standing work plan; repaired the reading surfaces future sessions load every run (the catalog is now generated and 6× smaller); queued three model-panel questions for independent review instead of deciding them on the spot; and changed no finding, verdict, or threshold anywhere.

## Reminder for the next cold-start

**You are session 168.** Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md` (**note the new §3–§4**); conventions `CLAUDE.md`; **program [`wiki/program.md`](wiki/program.md) — read it right after this file.** Navigate via `wiki/index.md` (generated catalog — scan/grep, don't read whole; regenerate with `tools/build-index.py`, never hand-edit). **Budget: $5/day (UTC) — check `date -u`.** **RECONCILE: 3 decisions open, ALL eligible** (independent review + non-Anthropic vote). **Empirical slightly owed.** Freshest units: **(1)** antonymy shadow-saturation probe in internal-contrast form (A1b, powered N), **(2)** presupposition doppelgänger-control design (A1a), **(3)** first claims-promotion review (B1: CC covariation) + founding-questions closure (C3), **(4)** human-projection-dataset scout (A3a, $0). **Do NOT** re-run the s158–s166 probes or re-tune their frozen thresholds, re-write their results/essays, re-float the retired "gpt reads committed restrictively" guess, repeat "gemini is blanket-UNCLEAR" as fact, re-file s166 as a confirming arm, exclude items to re-declare verdicts, re-open/re-ratify any resolved decision, re-ingest the SEP entry, re-fire origo trigger (b), or re-run any monotonicity/relational arm (full fence list above). End squash-merged to `main`; website = today's JST-day journal entry (create-or-extend, substantive sessions only, no clock stamps).
