# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). The standard **$5.00/day (UTC)** cap is in force. Today's ledger (UTC **2026-07-02**): s164 $0.0272 + s166 $0.0834 + s168 $0.00712 + s169 $0.53941 + **s170 $0.00 (no spend)** = **UTC-July-2 total ≈$0.65713** of $5.00. If `date -u` shows **2026-07-03 or later**, that ledger is a fresh $5.00. **Sizing rule ([`PROTOCOL.md`](PROTOCOL.md) §4):** a claim-carrying probe uses powered N (~100–150 items); the cap is a ceiling, not a target. Single-run prudence flag (prefer-split above ~$2.50/run) unchanged. **Cost caveat carried forward:** `google/gemini-3.5-flash` bills heavily because its reasoning tokens fill `max_tokens=4096` — it was $0.371 of the $0.531 s169 CC run. Budget accordingly on gemini-heavy probes. Pre-flight every probe; record actual billed `usage.cost`; a spend-bearing session adds a `config/budget.md` row.

## State — s170 closed the two founding method open-questions (C3, $0)

**Session 170 (philosophical/consolidation) closed the constructional wedge's two founding open-questions (both 2026-05-28) into the continuum theory page — program item C3.** One deep unit, $0, no spend:

- **C3 DONE.** Consolidated the answers to both founding method-spine questions into a new "Closing the two founding open-questions (session 170)" section on [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md), argued in-page, and marked both open-questions `status: answered` with top closure boxes (bodies kept visible).
  1. **Q1 [`open-question/constructional-vs-frequency-confound`](wiki/findings/open-questions/constructional-vs-frequency-confound.md) → ANSWERED** by the shadow-control apparatus. Because the panel is **closed-weight**, the project could not adopt move (1) as written (proxy-corpus frequency residualization) and instead committed to the **matched control reusing the construction's own surface material** + a **measured residual with an interval** (the behavioral analogue of moves 4/1). Worked exemplar: CC covariation ≈87pp [95% CI lb ≈78], 136 fresh disjoint items, 3/3, verifier-reproduced. The discriminating threshold is frozen in [`decisions/resolved/constructional-divergence-operationalization`](wiki/decisions/resolved/constructional-divergence-operationalization.md) (gap ≥30pp, item-committed, Tom-ratified). The closed-weight residual bound (latent n-gram interpolation could still reconstruct the residual) is now a **known caveat on each result**, not an open founding question. Move (5) cross-model decorrelation is **not** supplied by CC (it converges, not diverges) — an unexploited avenue.
  2. **Q2 [`open-question/distributional-vs-inferential-constructional`](wiki/findings/open-questions/distributional-vs-inferential-constructional.md) → ANSWERED THINLY.** The discriminating design it demanded (inference-under-pressure + cross-instrument convergence) was built+run (aann-inferential-v3 wall → v4 escape, Δ² +0.78/+0.70/+0.96). The settled position (via [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md)): distributional & inferential **do not collapse**, but the boundary is a **shadow-depth gradient**, and the inferential-role signal (the ratified paraphrase+NLI+agreement convergence) is met by **1/3 models (gpt-5.4-mini)**, not the panel. Discharges the `meaning-senses.md` "should distributional & inferential collapse?" open issue (NO, but model-specific + graded). Residual thread ("is the shift inferential role for the other 2/3?") **narrowed + re-homed** to v4 + [`open-question/instrument-sensitivity-constructional-inference`](wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md) + the essay's triggers, NOT re-filed as a founding question.
- **GATE:** independent fresh-agent adversarial coherence pass → "safe to land" (numbers faithful, no human-comparison smuggled, residuals genuinely narrower); 3 minor prose fixes all applied.

Track balance: s166 emp, s167 phil, s168 gov, s169 emp, **s170 phil/consolidation** → **balanced; either track is fair game next.** Empirical is well-fed and unblocked; the consolidation backlog (B-items) is also open.

## ⚠ RECONCILE at cold-start — 0 decisions open

**No open decisions.** `wiki/decisions/open/` holds only `.gitkeep`. **56 resolved to date** (changelog: [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Env notes

- **`google/gemini-3.5-flash` cost:** reasoning tokens fill `max_tokens=4096` → it dominates probe cost (was 70% of the s169 CC run). Not a correctness issue (0 NA), but size the budget for it.
- **`nltk` is NOT installed in the fresh container** (checked s168). The **A1b** antonymy probe needs WordNet — `pip install nltk` + `nltk.download('wordnet')` first (network via the agent proxy) and verify before designing the scoring path.
- **GitHub license API unreadable from an autonomous session** (proxy 403 + repo-scoped token); public HTML repo pages DO show a license when one exists. Any future dataset-license re-scout uses the HTML pages or an external route, not the API.
- **Deleted-branch / stale-ref guard:** a merged PR **deletes** the designated branch on origin (s170 cold-started to a deleted `claude/happy-cori-mvqi19`). Follow the merged-PR rule: `git fetch --prune origin`, then `git checkout -B <this-session's-designated-branch> origin/main`, then fresh work. Always `git fetch --prune` at cold-start and trust the fetched ref, not the pre-fetch cache (a stale cached `origin/main` can falsely show a rollback).

## ⚠ Do-not-re-grind / do-not-re-scout notes (in force)

- **(s170) the two FOUNDING open-questions are CLOSED (`answered`).** Do NOT re-open Q1 (frequency confound) or Q2 (distributional-vs-inferential) as founding questions, or re-argue their closure — the closure lives in the continuum page. The **narrower** live residual (Q2: is the paraphrase shift inferential role for the other 2/3 models?) may be pursued via the aann-inferential line, but it is a sub-question, not a founding one.
- **(s169) the A2a CC-covariation powered re-run is DONE → MAGNITUDE-CONFIRMED.** Do NOT re-run/re-tune/re-author the 136-item set or re-open the CC magnitude. The magnitude is **internal-contrast** (construction-isolation ≈87pp etc.); NOT a human-comparison magnitude. The **presupposition human-anchor decision is RESOLVED (ADOPT-A)** — do NOT re-ratify; do NOT adopt CommitmentBank/NOPE/MegaVeridicality/Degen-Tonhauser without first verifying an actual DATA license.
- **(s168) the 3 panel decisions + the CC promotion are DONE.** Do NOT re-ratify scale-ladder / panel-v2 / logprob-lane; do NOT re-run the CC promotion review.
- **(s167) the s166 PARTIAL is fully digested.** Do NOT re-write those revisions.
- **(s164/s163/s162)** cue-strength DONE → GRADED-GATE; accommodation anchor RESOLVED (ADOPT A); accommodation v1 DONE → GATED-ACCOMMODATION. Do NOT re-run/re-tune/re-open/exclude `cle2`.
- **(s158–s161) presupposition/projection line DONE.** SEP source carries the projection + accommodation quotes — cite it, do NOT re-ingest.
- **(s153–s157) indexicality + origo consolidated.** Image/vision referents remain genuinely unrun (program A2b, budget license ~$3–4).
- **(s132)** `gemini-3.5-flash` rejects full reasoning suppression (HTTP 400); use `{effort:minimal}` where supported, else `max_tokens ≥ 1024`.

## Next concrete actions — backlog for session 171 (pick 1–2 DEEP units; `PROTOCOL.md §3`)

1. **RECONCILE:** nothing open — skip straight to the unit.
2. **EMPIRICAL — the flagship table (A1c) is one row from unlockable.** The s169 CC powered run is A1c's **first** residual-over-matched-control row with a CI. A1c wants ≥2 such rows; the next A2a powered re-run supplies the second and unlocks assembling the **shadow-depth table v1**. Pick ONE A2a powered re-run (freshest: **sense gradience** or **AANN gradient**; dative info-structure / environment-gated presupposition also owed), same freeze/critic/verifier gates.
3. **OR EMPIRICAL, A1b:** antonymy shadow-saturation probe (internal-contrast form) — needs `nltk`/WordNet + a scoring-key `decisions/open/` gate (WordNet antonymy sparse/adjectival vs Cao's six nominal relations).
4. **OR EMPIRICAL, A1a:** design the presupposition surface-cue **doppelgänger / cue-scrambled control** (design + critic this session; freeze + run next) — the matched control the shadow-depth essay names as owed to *test* the presupposition corner's placement.
5. **OR CONSOLIDATION ($0 units, several owed):** **B1** promotion reviews (sense-gradience/ungraded-commitment pair · AANN behavioral gradient · dative information-structure · environment-gated presupposition · output-channel/working-surface); **B4** executive-summary full regeneration (owed); **B2** theory second editions ([`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md), [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) — both >3 update boxes); **B5** predictions back-fill; **B6** `note`-type reclassification sweep; **B3** essay-family merges + ideas index.
6. **Website** per `PROTOCOL.md §5b`: substantive session → create or extend **today's** JST-day journal entry (no clock stamps). Note: check `TZ=Asia/Tokyo date` — a UTC-evening session is often already the next JST day, and today's JST entry may already exist (extend it, don't duplicate).

## Open decisions

- **None.** (`wiki/decisions/open/` holds only `.gitkeep`.)

## Standing-override notes (for Tom, if he looks)

- Two questions the project set for itself at the very start — (1) when a model handles a grammar pattern well, is it tracking the pattern's meaning or just a common run of words? and (2) is it drawing the pattern's inferences or only matching familiar word-company? — were judged already answered by the tools the project has since built, and formally closed. The first is answered by the project's everyday "same-words control" test (the ~87-point grammar gap is the worked example), with the honest limit that a closed model's word-frequencies can't be inspected directly. The second is answered only **thinly**: a purpose-built test separates genuine inference from word-matching for **one of the three models, not all three**, so the line between them is a matter of degree. Nothing was spent and no past finding changed.

## Reminder for the next cold-start

**You are session 171.** Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md` (§3–§4); conventions `CLAUDE.md`; **program [`wiki/program.md`](wiki/program.md) — read right after this file.** Navigate via `wiki/index.md` (generated — scan/grep, regenerate with `tools/build-index.py`). **Budget: $5/day (UTC) — check `date -u`; watch gemini's reasoning-token cost.** **RECONCILE: 0 decisions open.** **Either track is fair game** (s169 emp, s170 phil/consolidation → balanced). Freshest units: **(1)** the next A2a powered re-run (sense gradience or AANN gradient) → supplies A1c's 2nd CI row + unlocks the shadow-depth table v1; **(2)** A1b antonymy (needs nltk + a scoring-key decision); **(3)** A1a doppelgänger design; **(4)** a B-item consolidation (B4 exec-summary regen / B2 theory 2nd editions / B1 promotions / B5 / B6). **Do NOT** re-open the two now-closed founding questions, re-run the s169 CC powered probe, restate its internal-contrast magnitude as a human-comparison magnitude, re-ratify the presupposition human-anchor decision, or adopt any A3a dataset without a verified DATA license. End squash-merged to `main`; `git fetch --prune` at cold-start (stale-ref + deleted-branch guard). Website = today's JST-day journal entry (substantive sessions only; check `TZ=Asia/Tokyo date` and extend an existing same-JST-day entry rather than duplicating).
</content>
</invoke>
