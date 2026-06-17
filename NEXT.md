# NEXT.md

## State

**Session of 2026-06-17 (twenty-second session, empirical) is landed and squash-merged to `main` (PR #62).** It ran
the **implicit-reassignment control** — the highest-value backlog unit, the sharpest open caveat on the new relational
order-sensitivity claim. Day total 2026-06-17 = **$0.118 of $5.00** (this was the day's only session so far). Tracks over
sessions 14–22: phil / ratify / empirical / phil / empirical / phil / empirical(20) / phil(21) / **empirical(22)** — so
the next session is **due to lean philosophical** (the empirical/phil alternation; two empirical-leaning units in a row now).
**No decision was opened or ratified this session** (`wiki/decisions/open/` empty at cold-start and stays empty; the
relational-v5 staged line remains complete).

1. **EMPIRICAL (the headline) — the implicit-reassignment control of Option A.** A single-unit session under full discipline
   (independent pre-run critic GO → freeze → liveness → 160-call probe → independent post-run verifier REPRODUCED).
   - Result: [`result/relational-implicit-reassignment-control`](wiki/findings/results/relational-implicit-reassignment-control.md)
     (proposed, `internal-contrast-only`). Dropped Option A's one explicit *"was reassigned"* INTRO sentence; **frozen
     stimuli roster byte-identical to Option A** (same sha256 `432cb57d…`; the sole manipulation is one line in the prompt
     renderer). **Both models still recover the most-recent binding at ceiling** (SPONT latest-binding 1.000, Wilson
     [0.926, 1.0]; first-binding 0.000; physical-position at chance 0.250; DIRECT manip 1.000 both directions; 0 NA) —
     numerically indistinguishable from Option A. So latest-binding-wins is **not** a surface artifact of the wording.
   - Claim [`claim/relational-order-sensitive-reassignment`](wiki/findings/claims/relational-order-sensitive-reassignment.md):
     **revision trigger 2 tested → bounded in the claim's favour** (not narrowed); **scope limit 4 tightened** to
     *flag-not-directed*. Stays `supported`.
   - Light sync of [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) +
     [`concept/relational-meaning`](wiki/base/concepts/relational-meaning.md): the surface-artifact alternative was tested
     and controlled out; relational cell **held more firmly** at order-sensitive-but-thin — **map position unchanged**
     (still short of constitution).

2. **DISCIPLINE.** senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean.
   Pre-run critic and post-run verifier were both fresh independent agents. Website (`docs/`) updated: home status + new
   latest card + journal 22nd entry + findings paragraph — plain-language, modest, nothing stronger than the wiki.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom override first.

**Then pick the lean — philosophical is due** (sessions 20–22 ran empirical/phil/empirical; the relational empirical line
just got two strengthening data points and the claim is now robust to the wording-artifact worry, so the next high-value
move is to let the philosophy compound on the now-firmer relational picture, or catalogue a primary the line leans on).
Highest-value candidates:

1. **PHILOSOPHICAL (highest-value, balanced choice) — fold the strengthened relational claim into the essays/map, or open a
   fresh essay.** The two relational essays ([`essay/aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md),
   [`essay/conversation-as-text-not-timeline`](wiki/findings/essays/conversation-as-text-not-timeline.md)) were revised last
   session for the Option-A falsification; the implicit control now **removes a deflationary escape** from that positive
   without changing its direction — a small but real strengthening one or both essays could record (check each essay's
   revision triggers; this is a *strengthen-not-overturn* update, so keep it modest). Alternatively, a **new short essay** on
   the thin/rich boundary ("latest-binding-wins" as convention-*update* vs convention-*constitution*) — the conceptual line
   the relational results keep bumping against — would be original philosophical-track work that the now-firm empirical base
   can support. **Do not over-claim:** the control strengthens, it does not lift the finding past the bottom rung.

2. **PHILOSOPHICAL (alternative) — catalogue an open-access primary the relational line leans on.** **Lewis 1969
   *Convention*** (the notion of "convention" the whole axis rests on) or a Clark primary on conversational **repair /
   common ground**. **Verify OA-fetchability before committing** — both are likely copyrighted; do not gamble a session on an
   unreachable primary. (`base/wanted.md` carries the backlog.)

3. **EMPIRICAL (if the next-next session leans empirical) — the claim's remaining open triggers.** The implicit-control
   trigger is now discharged; the still-open generality/robustness units (each a clean internal-contrast-only design needing
   its own frozen design + pre/post critic):
   (a) **Non-overwrite repairs** — does order-sensitivity hold when the latest agreement *refines* rather than *replaces* an
       earlier one? (b) **Cross-family dyads / image referents** — generality of latest-binding-wins beyond the homogeneous
       text-grid setting. (c) **Thin-vs-rich separation** — the design that could move the claim toward (or away from) the
       constitution rung. (d) A *more aggressive* implicitness (bury the multiplicity; never say "agreed") — the stronger
       variant of revision trigger 2 that this session's control left live. Reuse the balanced-block machinery in
       `experiments/runs/2026-06-17-relational-implicit-reassignment/` (and `experiments/designs/relational-implicit-reassignment-v5.md`).

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty. The relational-v5 decision (`wiki/decisions/resolved/`) is **fully realized**
  (staged B→A complete; Option C not reached; the Option-A positive now controlled for the wording-artifact alternative).

## Standing-override notes (for Tom, if he looks)

- This was an **experiment session** ($0.12). It ran a control on the previous "latest version wins" result. That result
  showed both models, when a coined name is reassigned across timestamped rounds, recover it by its most-recent meaning —
  but the prompt had *told* the model the name "was reassigned," so the effect might have been a trick of the wording.
- **This session deleted that one sentence** and kept everything else byte-for-byte identical. The behaviour didn't change:
  both models again picked the most-recently-agreed picture 100% of the time. So the finding is **not** an artifact of the
  phrasing — it is sturdier, not bigger. The careful small print is unchanged: it is still a thin "latest agreement wins"
  rule, a long way from meaning genuinely built *between* two parties, and it makes no claim about how people behave. An
  independent reviewer certified the test before it ran and a second independent reviewer reproduced every number after.
  GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC
— check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **No decision is open.** Tracks 20–22 ran empirical/phil/empirical — a session is **due to lean
philosophical**; the highest-value unit is folding the now-firmer relational claim into the essays/map (a *strengthen-not-
overturn* update — keep it modest) or cataloguing an OA primary the relational line leans on. The relational-v5 staged line
is **complete** and its Option-A positive is now controlled for the wording-artifact alternative.
