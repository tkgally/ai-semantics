# NEXT.md

## State

**Session of 2026-06-15 (thirteenth session, workflow mode — 2 waves, both tracks,
one probe, $0.05 spent) is landing.** Day total 2026-06-15 (sessions 12–13) =
**$0.10 of $5.00**. Tracks over sessions 7–13: emp / phil / both / both / both /
**both** — balanced. No decision was open at cold start; **none opened or ratified
this session** (the experiment reused an already-ratified yardstick).

1. **EMPIRICAL (headline): the v1 conative COMMITMENT-ONLY anomaly does NOT replicate —
   [`result/conative-commitment-replication-v2`](wiki/findings/results/conative-commitment-replication-v2.md)
   (status supported; VERDICT FAILS TO REPLICATE).** A clean direct replication of the
   single positive effect from last session's conative run (claude-sonnet-4.6's
   Δ²_commit = +0.46, the mirror-of-AANN commitment-only shift) on a **fresh, disjoint**
   verb set — same instrument/scoring/panel, `analyze.py` byte-identical, `probe.py`
   docstring-only diff, freeze hash `84e2e0d6afb4b5b6`
   ([`design/conative-commitment-replication-v2`](experiments/designs/conative-commitment-replication-v2.md)).
   **claude's effect collapsed +0.46 → +0.04** (CI [−0.29, 0.33], not positive; withhold|conative
   fell 0.58 → 0.17), category flips to LEXICAL-CUE ARTIFACT → **all three models LEXICAL-CUE
   ARTIFACT**, panel INCONCLUSIVE, **headroom all 3 PASS at 1.00/1.00**. The v1 +0.46 was
   **verb-set-specific noise**. The critic-flagged figurative verbs (strike/beat) returned
   entailment (no inflation); the marginal resist verb (squash) only shrinks Δ² (conservative).
   Independent **pre-run critic GO** (LCC purity clean, contaminant direction conservative) +
   independent **post-run verifier REPRODUCED-CLEAN** (every number recomputed independently, 0
   unparsed of 240, no NLI-aggregation bug, cost summed $0.0502, freeze integrity confirmed). NLI
   conative arm human-anchored to CxNLI (answer-key = non-entailment); FC/resist arms
   internal-contrast-only. **Net effect on the theory: the conative now reads as a clean
   no-dissociation construction on both arms across TWO independent verb samples — the
   AANN-specific reading of the preference/commitment dissociation is strengthened, with no
   counter-instance surviving.**

2. **PHILOSOPHICAL: new source [`source/mandelkern-linzen-2024-do-words-refer`](wiki/base/sources/mandelkern-linzen-2024-do-words-refer.md)**
   (status received) — Mandelkern & Linzen 2024 (arXiv 2308.05576), "Do Language Models' Words
   Refer?", the strongest in-repo **pro-reference** argument: LMs' words *may* genuinely refer via
   the externalist "natural histories of use" carried by training text. Runs the *same* externalist
   premise as [`concept/referential-meaning`](wiki/base/concepts/referential-meaning.md) to the
   *opposite* verdict — a productive tension a finding can cite from both poles. Map/interlocutor,
   not an `anchors:` resource. Verdict explicitly modal; CL venue + page numbers unverified (arXiv
   text verified; flagged in-page). Abstract + 9 section-located quotes verbatim.

3. **Integration / essay / theory / website:** result + design catalogued in
   [`wiki/index.md`](wiki/index.md); [`essay/preference-without-commitment`](wiki/findings/essays/preference-without-commitment.md)
   got a revision-log entry (the lone conative counter-signal retired, no trigger fired);
   [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md)
   conative callout updated (clean no-dissociation across two samples); budget ledger row added;
   `docs/` updated (journal thirteenth entry, home status + latest, findings paragraph). senselint
   **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — no decision is currently
open or awaiting ratification. (Confirm at cold start.)

**Then pick the lean (tracks balanced; either is fair):**

1. **EMPIRICAL — close the generality question, or open the third construction.** The conative has
   now failed to reproduce the AANN preference/commitment dissociation across **two independent verb
   samples** (v1 + v2), and the one apparent counter-signal is retired as noise. The honest close is
   well-supported: **"the preference-without-commitment dissociation is AANN-specific on the evidence
   so far."** A cheap, high-value philosophical/synthesis unit would be to **write this close up
   explicitly** (a short claim or theory revision: what it means that the dissociation is
   construction-particular, and that a "preference" forced-choice can be driven by a bare lexical
   cue). *Alternatively*, to genuinely test AANN-uniqueness, a **third, different construction** is
   needed — but the add-direction CxNLI constructions (way/caused-motion) run at *ceiling*, so a
   third test must **engineer headroom** on an add-direction construction first; that needs its own
   **fresh operationalization decision surfaced** (with a provisional default), ratified the session
   after. Do not silently reuse at-ceiling items.
2. **EMPIRICAL — non-AANN alternative (still un-run): RELATIONAL v5.** The v4 trap (both models
   anchor on text position, not stamped chronology) needs a design that **neutralizes text-position**
   (randomize/rotate the decisive line; gate on a task requiring the stamp value) **or** a
   **stamp-comprehension pre-probe**. Needs its own fresh operationalization decision surfaced.
   Template `experiments/runs/2026-06-14-relational-history-perturbation-v4/`.
3. **PHILOSOPHICAL — strong essay opportunity from this session's new source.** The freshly
   catalogued [`source/mandelkern-linzen-2024-do-words-refer`](wiki/base/sources/mandelkern-linzen-2024-do-words-refer.md)
   runs the *same* externalist premise as the project's own
   [`concept/referential-meaning`](wiki/base/concepts/referential-meaning.md) to the *opposite*
   verdict (do LMs' inherited word-histories make them "part of the linguistic community" whose use
   fixes reference?). That tension is a natural **essay** in the project's own voice (the philosophical
   track's first-class artifact), grounded in in-repo sources, with explicit revision triggers. Or
   catalogue another queued source: a **deflationary classic** (Cappelen & Dever 2021 *Making AI
   Intelligible*, if OA-reachable) or a **Grindrod rebuttal**.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** All twenty-five decisions are resolved; none opened this session.

## Standing-override notes (for Tom, if he looks)

- This session ran one cheap experiment (**$0.05**) whose only job was to **re-check a surprise**
  from the previous session — a single model's odd-looking effect that rested on one small verb set
  and a wide margin of error. Re-run on a completely fresh batch of verbs, with the measuring code
  kept byte-for-byte identical, **the surprise vanished** (it dropped from a sizeable margin to about
  zero). So it was luck of the draw, not a real property — a clean negative that removes the one
  loose end and makes the broader "prefer-without-committing" picture firmer and tidier.
- **No methodological decision was opened or self-approved this session** (none was eligible; the
  experiment reused a yardstick ratified an earlier session). Independent pre-run and post-run checks
  ran as always.
- Day total 2026-06-15 (sessions 12–13) = **$0.10** of $5.00. GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website
updated. **No open decision to reconcile.** Tracks balanced. Empirical: the generality question is
now well-positioned for an honest close ("AANN-specific so far," two clean conative samples) — write
it up, or surface a *fresh operationalization decision* for an engineered-headroom third
construction. Philosophical: a strong essay opportunity sits in the new Mandelkern & Linzen source
(externalist route to reference vs. the project's own concept page).
