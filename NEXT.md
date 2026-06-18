# NEXT.md

## State

**Session of 2026-06-18 (thirty-sixth session, empirical) is landed and squash-merged to `main` (PR #TBD).**
A single-unit empirical session — **288 finding-bearing calls + 3 liveness, $0.372384 billed** (`usage.cost`-summed,
0 missing); day total 2026-06-18 ≈ **$1.358 of $5.00**.

It ran the **worked-example-scaffold** witness-seeking re-run of the Option-C order-sensitive composition split
([`result/relational-order-composition-c-worked-example`](wiki/findings/results/relational-order-composition-c-worked-example.md))
— the **first easing of the chaining axis** the figure-to-figure run localized (a new axis; the three prior easings
touched only state-space and read-off). The single manipulated variable was one **worked example** demonstrating the
chaining mechanic (apply move 1 to the start, then move 2 to the result), added to the **byte-identical** fig trials
(same `stimuli.json` sha `975e31bc…88ba`), built with disjoint items/moves and an explicit order so it eased chaining
**without** teaching stamp-resolution (COMP spontaneity preserved).

**HEADLINE — NO WITNESS again, and the scaffold did not help.** claude RESPECTS-ORDER at ceiling (DIRECT 1.000, COMP
64/64); **gemini UNINTERPRETABLE** (DIRECT 0.625) and **gpt UNINTERPRETABLE** (DIRECT 0.156) — neither cleared the
gate. Decisively, shown a worked chain *and* told the order, **gpt still applies only one of the two moves 84.4% of
the time** (up from the fig run's 65.6%; gemini 21.9%, unchanged; claude 0%). So the single-move signature **persists
and intensifies** even when chaining is demonstrated outright → the difficulty is **not** a demonstration/comprehension
gap but chaining **execution** itself. (The numeric DIRECT drops — gpt 0.250→0.156, gemini 0.656→0.625 — are within
**overlapping CIs**: read "no witness", **not** "the scaffold hurt"; a worked example also lengthens the prompt.)
The split now survives **four** instruments (K=6 positional, K=4 positional, K=4 figure-maps, K=4 figure-maps + worked
example), two on-signature. Per [`essay/undischargeable-negative`](wiki/findings/essays/undischargeable-negative.md)
it stays **undischargeable, not closed** (kind-2 instrument-uninterpretable). `anchor: internal-contrast-only`; **no
human comparison.**

**Integration:** independent **pre-run critic GO** (fresh agent: reproduced the byte-identical freeze; recomputed
geometry 0 mismatches; traced rendering 0 position leaks; verified the worked example leaks no trial answer/map,
teaches no stamp-resolution — no digits/round/stamp/recency words — is arithmetically correct, and is the *single*
prompt variable vs the fig run; ruled no new decision owed). Independent **post-run verifier REPRODUCED** every number
with its own Wilson (0 mismatches; 0 missing-cost; sha confirmed; total $0.372384). Updated, by judgement (orchestrator):
the result page (new), [`essay/capability-split`](wiki/findings/essays/capability-split.md) (trigger (b) tested a third
time → worked-example **discharged**; only fewer-steps remains; trigger (c) "four instruments"),
[`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md) (trigger (a) tested → no witness;
trigger (f) tested → **did not fire**, signature persisted/intensified not changed; diagnostic-dividend persist-branch
corroborated), [`wiki/index.md`](wiki/index.md), [`wiki/executive-summary.md`](wiki/executive-summary.md). senselint
**0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify clean. Website (`docs/`): journal
36th entry + home status/"The latest" card + findings follow-up paragraph. Tracks: …emp(34)→phil(35)→**emp(36)**, so the
next session is **due to lean philosophical** (or a cheap mixed unit).

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** (all 28 decisions resolved). Nothing to ratify
unless Tom opens something or leaves an override. Apply any Tom override first, as always.

**Then pick the lean — philosophical is due** (tracks ended on emp(36)). Candidates:

1. **PHILOSOPHICAL (lean is due) — re-examine, don't spawn for its own sake.** The composition witness-search is now
   **suspended across four instruments** and **near its easing floor on the byte-identical line**: with state-space,
   read-off, and chaining-demonstration all discharged, the one remaining implicated axis is **fewer chaining steps**,
   and an order-sensitive *composition* needs **≥ 2** moves — so that axis cannot go lower and remain a composition.
   This is the natural occasion for the unit [`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md)
   **trigger (b)** names: ask whether a **structural bound (kind-3 reach-closure)** exists for *thin-side* two-move
   composition — "an analogous bound for some thin-side composition capability would be new" — i.e., is there an
   argument that **no** easing of two-move non-commuting composition (short of changing the task) could carry a witness
   for these models, given the ≥2-move floor? If a defensible bound exists, the suspension upgrades from budget-based to
   structural (the highest-value terminator in the economics); if not, write the null and say why. **Caution:** a
   structural bound is a claim about *instrument reach*, never *model capacity* — keep it kind-3, never kind-4.
   Alternatively, catalogue the strongest queued open-access source in [`base/wanted.md`](wiki/base/wanted.md)
   (network-permitting).

2. **EMPIRICAL (if a unit pairs, or next empirical lean) — a FRESH axis, not another easing of the same instrument.**
   The byte-identical composition line is at its floor; further marching down it is low-value (and four eased re-runs
   of one instrument are **not** distinct probes — `capability-split` trigger (c)). Genuinely fresh options: a
   **different non-commuting operation pair** (is STEP/FLIP-on-a-ring unusually hard for gemini/gpt, or is two-move
   composition itself the wall? — a fresh pair would be a new instrument, needing its own freeze + critic), or a fresh
   relational horn: **partially-conflicting refinements** (a later turn *partly* conflicts — overwrite/integrate/split?),
   **larger-grid / >3-turn** integration generality, **image referents**, **cross-family dyads**. Grammar reserve: the
   AANN/CxG **cancel-direction / unification-shape Option-B** held in
   [`decisions/resolved/aann-uniqueness-third-construction`](wiki/decisions/resolved/aann-uniqueness-third-construction.md)
   (needs a fresh human anchor first).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty (28 resolved; full changelog in
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Most recent ratification:
  `wiki-frontmatter-ergonomics` (Option D, 30th session).

## Standing-override notes (for Tom, if he looks)

- This session tried the *last* easier version of the "order of operations" test the project had been saving — a
  **worked example** that shows the two struggling models exactly how to do one move and then the other (using
  different shapes so it gives nothing away). It didn't help: the strong model stayed perfect, the other two still
  failed, and one of them did only a single move *even more* often (about 84% of the time) despite being shown how and
  told the order. So the trouble isn't that the models don't understand the task or were never shown the steps — it's
  the bare act of doing two steps in a row. As always this is **not** "the models can't"; it's a budget decision to
  pause this line, now with only one near-impossible easier version left (a task with fewer than two steps stops being
  a two-step task). Two independent reviewers vetted it (one before spending — checking the worked example gives no
  answer away and teaches no shortcut — one reproducing every number after). About 37 cents; the day stays ≈ $1.36 of
  the $5/day cap. Next session leans to writing/philosophy (the tracks alternate), where a natural question is whether
  one can *argue* — not just keep testing — that no easier version of a two-step task could ever crack it.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md) (resolved-decisions
changelog at [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Budget $5/day UTC — check today's
ledger rows in [`config/budget.md`](config/budget.md) before any probe (2026-06-18 day total ≈ **$1.358**; this session
added **$0.372384**). End squash-merged to `main`, website updated. **No decision is open.** Tracks ended **emp(34) →
phil(35) → emp(36)** — a session is **due to lean philosophical**. The relational ladder stands at rung (i) overwrite,
rung (ii) integration (+depth 2), order-sensitive **composition** (**claude only** across the full three-model panel,
robust to **four** instruments — K=6, K=4, K=4 figure-maps, K=4 figure-maps + worked example — the two UNINTERPRETABLE
verdicts surviving both on-signature easings), and **rung (iii) documented structurally closed for text-only stimuli**.
The methodological spine has four essays: `essay/undischargeable-negative` (the logic), `essay/witness-seeking-economics`
(the spending — suspend never close; ease the implicated axis; the diagnostic dividend, **persist branch** now twice
demonstrated), `essay/capability-split` (read splits as splits; trigger (b) discharged on three of four easings, only
fewer-steps left), and `essay/transcript-ceiling` (the structural reach-closure). The composition witness-search is
**suspended across four instruments and near its easing floor** (only **fewer chaining steps** un-eased, which is
bounded below by the ≥2-move definition of a composition) — the natural next move is to ask whether a **structural
bound** retires the rest of the search, or to open a **fresh axis** (different operation pair / fresh relational horn).
