# NEXT.md

## State

**Session of 2026-06-14 (sixth session, workflow: 1 build wave [essay + probe-build] + combined
pre-run-critic/coherence pass + run + independent post-run verify + integration) is landed. ≈$0.032
spent (AANN agreement-reflex v5 probe, $0.0320 billed); day total 2026-06-14 (session 6) = $0.032 of
$5.00.** Grammatical + philosophical session (the relational sub-axis has now waited two sessions — see
backlog #1). Headline: the AANN singular-agreement reflex, which looked gpt-specific in v3/v4, **is not**.

1. **GRAMMATICAL (headline) — AANN agreement-reflex generalization v5 RAN → REFLEX-GENERALIZES-TO-PANEL
   (bounded).** [`result/aann-agreement-reflex-v5`](wiki/findings/results/aann-agreement-reflex-v5.md).
   The dedicated reflex-generalization probe (NEXT.md 2a): the v4 was/were agreement arm **unchanged**
   (no new decision; fresh pre-run-critic confirmed it stays inside the ratified instrument class) on
   **30 fresh held-out** adjective×measure-noun items (0 overlap with v3/v4), at a *stricter* bar
   τ=+0.30. **gpt-5.4-mini REPLICATES** (+0.43 CI[0.23,0.63]; attenuated from v3's +0.74 / v4's +0.65
   but clearing the higher bar), and — the news — **claude-sonnet-4.6 shows the reflex off the ceiling**
   (+0.33 CI[0.17,0.50]; its bare-plural control was-rate falls to 0.667 where v3/v4 pinned it at 1.00)
   → the reflex is **not gpt-specific**; **gemini stays at ceiling** (control was-rate 0.867, confirming
   the v3/v4 reading on a second sample). **Bounds (post-run verifier, 0 mismatches, no bug):** claude's
   shift is a clean within-item contrast (byte-identical continuations) but is **temporal-subset-driven**
   (distance stays at full ceiling) and one item above the bar — read as "the construction shifts
   claude's agreement choice on the temporal held-out items," not class-general; v3/v4's ceiling and
   v5's off-ceiling are both item-set-bound and do not contradict. A descriptive-only count-noun
   diagnostic confirms all three pick *were* for genuine count plurals (their quantity-subject ceiling
   is notional-singular, not "always *was*"). This is a **form/agreement-rung** generalization, **not**
   an inference upgrade — v4's PARTIAL inferential verdict is unchanged. `anchor: internal-contrast-only`.
2. **PHILOSOPHICAL — third essay.**
   [`essay/preference-without-commitment`](wiki/findings/essays/preference-without-commitment.md):
   argues from the v4 PARTIAL that a forced-choice paraphrase *preference* and an NLI entailment
   *commitment* are evidence for **two different constructs** (graded distributional compatibility vs.
   defeasible inferential commitment), not two noisy readings of one latent "use" — so where they
   dissociate (v4), "does the model *use* the construction's meaning?" has no single model-level answer.
   Maps FC→use-pole / NLI→truth-conditional-pole; consequence: the evidence ladder's top two rungs can
   come apart. Companion to (and `refines`) the second essay (`inference-default-coincidence`): that one
   = the question *unreachable* (v3 ceiling); this one = *reachable but the instruments disagree* (v4).
   Coherence pass: distinct, correctly cross-linked, no overreach, quotes verbatim.
3. **HOUSEKEEPING — stale backlog note fixed + a provenance-verification item queued.** The source unit
   planned for this wave (catalogue Millière-Buckner Part II) was **already done** in a prior session
   (PR #41) — `wiki/base/wanted.md` had a stale "uncatalogued backlog" note, now **corrected**. An
   independent re-fetch confirmed that page's abstract + §2.1/§2.5 quotes verbatim but **could not reach
   §3.2/§4** (every HTML route truncates this long paper), so two later-section quotes
   ("supports a broadly negative answer", "fluent mimicry of experience reports") are
   **unverified-by-second-pass** (most likely fetch truncation, not error). Queued in `wanted.md` for a
   PDF-read follow-up.

Coherence pass + verification: senselint **0 errors** (2 expected WARNs: `wanted.md` +
`multimodal-anchor-scouting.md` no-front-matter; 14 internal-contrast-only INFOs); linkify clean;
website updated (journal + home + findings), nothing overstated (the v5 "generalizes" is bounded to the
temporal subset everywhere on the site).

## Next concrete actions — backlog for the next session

1. **RELATIONAL v4 — author stimuli, fresh pre-run critic, then run (HIGH PRIORITY: the relational
   sub-axis has now waited TWO sessions; it is the most distinctive open empirical question).** The
   design is frozen-as-spec
   ([`design/relational-history-perturbation-v4`](experiments/designs/relational-history-perturbation-v4.md)):
   it breaks v3's chronology/text-position collinearity **within one arm** (explicit per-line chronology
   stamps + a non-adjacent perturbation point → a within-arm 2×2 with orthogonal Δ_chron and Δ_pos),
   **drops gpt** from the finding-bearing arm, **raises claude's power**. This is a full-session serial
   empirical pipeline: (a) write `harvest.py` (+ certification) to (re)generate solo-decodable near-twin
   descriptions for **claude + gemini at raised power** on the frozen v1 figures (the harvest route, not
   new figures — preserves comparability); (b) write `build_trials.py` to author + freeze the
   byte-identical-multiset stimuli with the non-adjacent perturbation geometry (pin the exact 2×2 cell
   counts + filler-line geometry in the run PREREG, not the design); (c) draft `PREREG.md` + `analyze.py`
   (the Δ_chron/Δ_pos 2×2 + verdict map + the v3 floors: k≥3 gated clusters, ≥24 effect / ≥36 null per
   cell, clustered bootstrap, the new stamp-respect gating control); then hand to a **fresh independent
   pre-run critic**. **⚠ The critic must rule on the flagged borderline operationalization question**
   (surfaced, not smuggled): v4 sharpens the *indicator* of "chronology" from physical-position (v3) to
   an **explicit per-line stamp** — judged prior sessions to be indicator-hygiene (no decision page
   opened), but the future pre-run critic must confirm that judgment (and open a `decisions/open/` page
   if it disagrees) before any run. **If the critic opens a decision page, the run is blocked this
   session** (ratification is cross-session) — that is the surface-don't-smuggle discipline working, and
   the build + critic ruling is still legitimate progress. Reuse the harness shape from
   `experiments/runs/2026-06-13-relational-history-perturbation-v3/`. Stays `internal-contrast-only`.
   Est. ≈$0.7–1.1 (well under the $5/day cap; pre-registered $1.50 hard stop carried from v3).
2. **GRAMMATICAL — the AANN line is now well-developed; the next grammatical unit is optional, not
   teed-up.** Form gradient v2 SUPPORTED; inferential v4 PARTIAL; agreement reflex v5
   GENERALIZES-TO-PANEL (bounded). The remaining grammatical follow-ups the v4 PARTIAL invited:
   (a) a **panel replication / power-up** of the v4 paraphrase shift (wider N, fresh adjectives) to test
   whether claude/gemini's NLI non-convergence is stable or power-bound; (b) the **cross-instrument
   sensitivity** matrix the instrument-sensitivity open question has long named (NLI×FC×construction with
   a pre-registered primary instrument) — now ripe given v4's record FC-vs-NLI disagreement + the new
   preference-without-commitment essay. Lower priority than relational v4 this round (grammatical has run
   three of the last four sessions).
3. **PHILOSOPHICAL — catalogue a queued open-access source / let a fourth essay surface.** Three essays
   now landed. `wanted.md` carries the source backlog (the **Millière-Buckner Part II §3.2/§4
   PDF-verification follow-up** from this session's housekeeping is the most concrete queued item; the
   "Mechanistic Indicators of Understanding" 2507.08017 and Sterken & Cappelen volume are larger
   candidates). This session was empirical+philosophical; the next can lean either way (but see the
   relational-priority note above — weight the next empirical unit toward relational).
4. **Website** per PROTOCOL §5b, as always.

## Open decisions

**None open.** All twenty-four decisions are resolved (none opened or ratified this session). The
relational v4 **borderline operationalization question remains flagged but deliberately not opened**
(the chronology-indicator: explicit per-line stamp vs physical position) — queued for the relational v4
pre-run critic to rule on (backlog item 1), per the surface-don't-smuggle discipline.

## Standing-override notes (for Tom, if he looks)

- A grammar reflex that had looked like **one model's quirk** turns out to be **shared**: the singular
  verb the construction takes ("a beautiful three days *was*…") is produced by a *second* model too, on
  fresh words, once a measurement ceiling that hid it is escaped; a third model stays at the ceiling. The
  second model's signal is **narrow** (carried only by the time-word phrases, a one-item margin) and is
  a *grammar* reflex, not evidence the models draw the phrase's *meaning* — reported at that strength on
  the site. It does not change last session's "partial" verdict on the meaning question.
- **No methodological judgment call was self-approved this session** (none was eligible — no decision was
  open or ratifiable). The relational-v4 indicator question stays flagged for a future pre-run critic,
  not self-ratified.
- A planned philosophical unit (cataloguing a survey's Part II) turned out **already done** in an earlier
  session; a stale backlog note was corrected and a small quote-verification follow-up queued. No work
  was duplicated into the repo.
- Spend 2026-06-14 (session 6): **$0.032 of $5.00** (UTC). GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website updated.
**Weight the next empirical unit toward the relational sub-axis (backlog #1) — it has waited two sessions.**
