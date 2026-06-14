# NEXT.md

## State

**Session of 2026-06-14 (ninth session, empirical/grammatical track — single focused
empirical unit with independent pre-run critic + independent post-run verifier) is
landed. ≈$0.21 spent; day total 2026-06-14 (sessions 6–9) ≈$1.19 of $5.00.** Per the
eighth session's handoff (weight back to the empirical track, AANN follow-up the most
tractable), this session ran the **powered panel replication of the AANN inferential
v4 PARTIAL result** (NEXT backlog item 1, first bullet).

1. **EMPIRICAL — GRAMMATICAL (headline): AANN inferential v6 → PARTIAL, replicates v4
   cell-for-cell.** [`result/aann-inferential-v6`](wiki/findings/results/aann-inferential-v6.md)
   (status: proposed). Same yardstick as v4 (instrument, thresholds, verdict map, and
   analysis code identical — `analyze.py` byte-identical save run name / design path /
   bootstrap seed, the only logic-touching diffs inside `--selftest`), single change the
   **item set**: 40 fresh hand-authored base items (temporal 20 / distance 20, nearly
   doubling v4's 23 and rebalancing the distance class), all **40 adjectives held-out**
   (mechanically asserted disjoint from v4's 21 *and* the v5-reflex probe's 30). Both
   pre-registered questions answered **yes**: (1) the panel-wide paraphrase
   double-contrast shift **holds up powered** — all three models paraphrase-positive
   (Δ² +0.875 / +0.575 / +0.90, every CI clear of τ=+0.20; headroom PASS all,
   P(uni|DDC) 0 / 0.225 / 0); (2) **gpt-5.4-mini's cross-instrument convergence
   replicates** — CONVERGENT-POSITIVE again (paraphrase + NLI Δ² +0.225 + agreement
   reflex +0.60), claude + gemini again PARAPHRASE-ONLY (NLI null; agreement flat at
   ceiling 1.00/1.00). Verdict **PARTIAL**, per-model categories PARA-ONLY / CONV-POS /
   PARA-ONLY exactly as v4. Removes v4's small-N / single-date / direction-not-magnitude
   caveat (the effect is now stable in **magnitude across two disjoint item sets**); the
   **single-panel** and **expert-stipulated-key** caveats stand. No new decision (ran
   under the already-ratified AANN inferential instruments); `anchor:
   internal-contrast-only`. Fresh pre-run-critic GO (no BLOCKER/SHOULD-FIX; all 14
   conditions PASS; replication fidelity + held-out + anti-cheat verified; selftest 38
   checks) + independent post-run verifier (0 mismatches; confirmed the v4 NLI-
   aggregation bug class is absent here). 1392 calls, $0.2138 billed, 0 missing.

2. **Integration:** conjecture [`conjecture/aann-construction`](wiki/findings/conjectures/aann-construction.md)
   (v6 replication note added; inferential clause unchanged in status, now on firmer
   ground), theory [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md)
   (AANN Tier-4 cell: PARTIAL replicates powered), [`wiki/index.md`](wiki/index.md)
   (result + design catalogued), [`wiki/executive-summary.md`](wiki/executive-summary.md)
   refreshed. Website (`docs/`) updated: journal entry, home status + latest, findings
   AANN bullet. senselint **0 errors**; linkify clean.

## Next concrete actions — backlog for the next session

**Two-track note:** the last four sessions were empirical / empirical / philosophical /
empirical (sixth AANN-reflex, seventh relational-v4, eighth philosophical, ninth
AANN-v6). The **AANN line is now thoroughly worked** — gradient half SUPPORTED (v2,
v2b), inferential half PARTIAL and now **replicated** (v3→v4→v6), agreement reflex
generalized (v5). **Weight the next session toward the PHILOSOPHICAL track** (it has had
only one of the last four sessions), with a non-AANN empirical fallback. Both are
first-class.

1. **PHILOSOPHICAL (weighted first).** The v6 replication turns a soft empirical fact
   into a firm one: across two disjoint item sets, the AANN construction shifts *which
   paraphrase the models prefer* in all three models, but only **gpt-5.4-mini** carries
   that onto a stricter entailment/agreement *commitment*. That is exactly the subject of
   the fourth-ish essay [`essay/preference-without-commitment`](wiki/findings/essays/preference-without-commitment.md)
   — which can now be **revised to cite a replicated** preference/commitment split (its
   empirical anchor is no longer a single run). Check its revision triggers and update
   in-page. **Or** catalogue a queued source from [`wiki/base/wanted.md`](wiki/base/wanted.md):
   **Sterken & Cappelen (eds.), *Communicating with AI*** (P1; check OA), **Grindrod**
   monograph (P1; verify title/OA), or the **2601.19792** "LVLMs and Humans Ground
   Differently" dyadic-grounding paper (P3, relational-side datapoint). Or a new essay
   where the evidence is now thick (the replicated single-model convergence is a candidate
   subject in its own right: what does it mean that *one* model's inference survives every
   instrument while two stop at preference?).

2. **EMPIRICAL — non-AANN (fallback / if the session leans empirical).** Two tractable
   options, both off the now-saturated AANN axis:
   - **RELATIONAL v5** — the v4 trap (models anchor on **text position**, so a *linear*
     recency probe cannot see a chronology convention) needs a design that **neutralizes
     text-position** (randomize/rotate the decisive line so position carries no
     information, gate on a task that *requires* reading the stamp value) **or** a
     **stamp-comprehension pre-probe** (can these models use an explicit recency stamp at
     all when position is uninformative?). Template:
     `experiments/runs/2026-06-14-relational-history-perturbation-v4/`. Named scope
     extensions remain: image referents, cross-family dyads, live reassignment.
   - **A fresh construction's inferential test** — apply the v4/v6 double-contrast
     instrument design (DDC + LCC + paraphrase/NLI/agreement) to a *different*
     construction whose inference and distributional default plausibly diverge, to test
     whether the "paraphrase-shift-without-commitment, one-model-converges" pattern is
     AANN-specific or general. This would need its own operationalization decision
     (surface it, don't smuggle it).

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

**None open.** All twenty-four decisions remain resolved; **none opened or ratified this
session.** No methodological judgment call required surfacing — v6 is a replication of an
already-ratified-instrument design, with the same frozen yardstick (the anti-cheat point
of a replication is precisely that the yardstick is fixed and cannot be tuned). The
independent pre-run critic (GO) and independent post-run verifier (VERIFIED, 0 mismatches)
are the workflow's generation/judgement split working as intended.

## Standing-override notes (for Tom, if he looks)

- The project's deepest grammar-meaning result — that *a beautiful three days* nudges the
  models toward a "one whole evaluated stretch" reading (a **partial yes**: fully
  convergent across instruments in one of three models, surface-level in two) — was
  **re-run bigger on 40 fresh words and replicated point for point**. The honest upshot:
  the effect's *size*, not just its direction, is now stable across two separate item
  sets, so the earlier "too small / single day" caveat is gone. What remains: still only
  three models (one panel), and still scored against an expert's stipulated key, never
  human inference data — so it can never say the models infer "the way people do."
- **Spend this session ≈ $0.21** (1392 calls, billed `usage.cost`). Day total 2026-06-14
  (sessions 6–9) ≈ $1.19 of $5.00. GitHub Pages serves from `main` `/docs`.
- **No self-approved methodological call this session.** The replication ran under the
  already-ratified instrument; both the pre-run critic and post-run verifier were
  independent fresh agents.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`;
conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md)
then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **Weight the next session toward the PHILOSOPHICAL track (it has had one
of the last four sessions; the AANN empirical line is now thoroughly worked — gradient
SUPPORTED, inferential PARTIAL and replicated, reflex generalized) — with a non-AANN
empirical fallback (relational v5 needs text-position neutralization; or a fresh
construction's inferential probe).**
