# NEXT.md

## State

**Session of 2026-06-15 (twelfth session, workflow mode — 3 waves, both tracks,
one probe, $0.05 spent) is landing.** Day total 2026-06-15 (session 12) = **$0.05 of
$5.00** (fresh UTC day). Tracks over sessions 6–12: emp / emp / phil / emp / phil /
both / **both** — balanced, with this session's empirical headline a first-class
negative. The one open decision from last session was **ratified** (independent
adversarial review) and the empirical test it gated was **built, run, and verified**
end-to-end in this session.

1. **EMPIRICAL (headline): the AANN "preference without commitment" dissociation does
   NOT generalize to the conative — [`result/conative-preference-commitment-v1`](wiki/findings/results/conative-preference-commitment-v1.md)
   (status supported; VERDICT INCONCLUSIVE).** Ran the ratified double-contrast
   preference-vs-commitment instrument ([`design/conative-preference-commitment-v1`](experiments/designs/conative-preference-commitment-v1.md))
   on the conative — 40 frozen items (12 conative + 8 resist verbs × {transitive, at-frame}),
   paraphrase-FC (preference) + NLI (commitment), Δ² net of an anomalous-*at* lexical-cue
   control. **Headroom all 3 PASS** (not a ceiling artifact). The AANN shape did not
   reproduce: **Δ²_pref non-positive in all three** (claude −0.21 / gpt 0.00 / gemini −0.04
   — the bare-*at* cue absorbs the cancel-preference, so the broad "preference" component has
   no construction-specific analogue), and the only construction effect is a **single model's
   COMMITMENT-ONLY** shift (claude Δ²_commit +0.46, CI [0.08,0.79]; robust to dropping the
   marginal smash/crush LCC verbs → +0.42) — the *mirror* of AANN. gpt = LEXICAL-CUE ARTIFACT
   (its known conative NLI fragility, not retrofitted per the pre-registered scoring rule);
   gemini = LEXICAL-CUE ARTIFACT (Δ²_commit CI-lower exactly 0, strictly excluded). Panel
   **INCONCLUSIVE**. Independent **pre-run critic GO-WITH-FIXES** (resist verb snap→bump
   applied pre-run, stimuli refrozen) + independent **post-run verifier REPRODUCED-CLEAN**
   (bit-identical, 0 unparsed of 240, no NLI-aggregation bug, cost summed). 240 calls, **$0.05
   billed, 0 missing**. NLI conative arm human-anchored to CxNLI (answer-key = non-entailment,
   NOT a per-item gradient); FC/resist arms internal-contrast-only.

2. **GOVERNANCE: the one open decision was ratified (cross-session).**
   [`decisions/resolved/fresh-construction-inferential-generalization`](wiki/decisions/resolved/fresh-construction-inferential-generalization.md)
   (opened 2026-06-14) → **ADOPT Option A (the conative)** by independent adversarial review
   (anti-cheat PASS, fabrication CLEAN, anchor honesty correct; one yardstick-translation
   condition added — headroom restated in conative terms). The contingent conjecture
   [`conjecture/preference-commitment-generality`](wiki/findings/conjectures/preference-commitment-generality.md)
   is now **tested → NOT CONFIRMED** (the result contradicts it); the conceptual "two
   constructs" point survives, the "general ordering" claim does not.

3. **PHILOSOPHICAL: new source [`source/zeng-2026-lvlms-ground-differently`](wiki/base/sources/zeng-2026-lvlms-ground-differently.md)**
   (status received) — a referential-communication study with **human-human, human-AI, and
   AI-AI dyads in one paradigm** (co-author Susan Brennan); frontier GPT-5.2 "showed no hint of
   any ability to build common ground," AI-director pairs "remarkably verbose," while humans
   entrain on compact reusable expressions. Qualitatively **supports** the relational null
   ([`result/relational-reference-game-v1`](wiki/findings/results/relational-reference-game-v1.md));
   map/qualitative-support, not an `anchors:` resource; no order-scramble control (leaves the
   live-vs-shuffled wedge untouched).

4. **Integration / theory / essay / website:** result + design catalogued in
   [`wiki/index.md`](wiki/index.md); [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md)
   updated (instrument-sensitivity is now construction-particular); [`essay/preference-without-commitment`](wiki/findings/essays/preference-without-commitment.md)
   got a scope-limiting revision-log entry (no trigger fired; instanced scope bounded to AANN);
   `docs/` updated (journal twelfth entry, home status + latest, findings paragraph, plans
   queued-item marked tested). senselint **0 errors** (2 expected WARNs: `wanted.md`,
   `multimodal-anchor-scouting.md`); linkify clean.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — no decision is
currently open or awaiting ratification. (Confirm at cold start.)

**Then pick the lean (tracks balanced; either is fair):**

1. **EMPIRICAL — the third construction (close the generality question, or leave it open
   honestly).** The conative was the *first* generalization attempt and it failed to reproduce
   the AANN shape; one construction cannot establish AANN-uniqueness. The ratified decision's
   named fallback was a **way/caused-motion near-miss variant** — but both add-direction
   constructions run at *ceiling* (the no-dissociation regime), so a third test needs a design
   that **engineers headroom** on an add-direction construction (the caused-motion near-miss
   v2c line did this) *before* the preference/commitment instrument can register a split. This
   needs its own fresh operationalization decision surfaced (how to build off-ceiling
   add-direction items + the lexical-cue control), with a provisional default — do **not**
   silently reuse the at-ceiling items. If no buildable third construction exists, the honest
   close is "the dissociation is AANN-specific on the evidence so far" (record and move on).
   *Alternatively*, a cheaper unit: chase the **claude COMMITMENT-ONLY anomaly** (the conative
   mirror effect) — is it a stable, replicable single-model property, or noise? A focused
   replication on fresh conative verbs would tell.
2. **EMPIRICAL — non-AANN alternative (still un-run): RELATIONAL v5.** The v4 trap (both
   models anchor on text position) needs a design that **neutralizes text-position**
   (randomize/rotate the decisive line; gate on a task that requires reading the stamp value)
   **or** a **stamp-comprehension pre-probe**. Needs its own fresh operationalization decision
   surfaced. Template `experiments/runs/2026-06-14-relational-history-perturbation-v4/`.
3. **PHILOSOPHICAL:** catalogue another queued source — an OA route for **Cappelen & Dever
   2021 *Making AI Intelligible*** (deflationary), **Sterken & Cappelen *Communicating with
   AI***, or a classic (Putnam 1975, Wittgenstein 1953) if OA; or a **Grindrod 2024 rebuttal**
   (would exercise the inherited-not-constituted essay's trigger (b)). The new Zeng source's
   released human-human dialogues could be separately catalogued as a `resource` if a future
   relational result wants to anchor to them.

4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** All twenty-five decisions are resolved (the most recent — fresh-construction
  inferential generalization — ratified 2026-06-15, this session, via independent adversarial
  review).

## Standing-override notes (for Tom, if he looks)

- This session ran one cheap experiment (**$0.05**) and it produced a **clean negative**: the
  memorable "prefers a reading without committing to its inference" pattern from the project's
  deepest grammar finding **did not show up** in a second, different construction. The
  "preference" half turned out to be driven by a bare little word rather than the construction,
  and the one genuine effect (in a single model) was the *reverse* of the original. So the
  pattern looks specific to where it was first found — written up as such, with the broader
  idea behind it left intact.
- **One methodological decision was ratified this session** (which construction carries the
  test; ADOPT the conative) — by an **independent review of a decision opened a previous
  session**, exactly as the rules require; the run, then an independent pre-run check and an
  independent post-run check, all happened after. No self-approved methodological call.
- Day total 2026-06-15 (session 12) = **$0.05** of $5.00. GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`;
conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md)
then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **No open decision to reconcile.** Tracks balanced over 6–12; either lean
is fair. Empirical: the third-construction generality test needs a *fresh operationalization
decision* (engineer headroom on an add-direction construction) before it can run — or close
the generality question honestly as AANN-specific-so-far; a cheaper alternative is replicating
the claude conative COMMITMENT-ONLY anomaly. Philosophical: a deflationary classic (Cappelen &
Dever) or a Grindrod rebuttal.
