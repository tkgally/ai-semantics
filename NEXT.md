# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). The standard **$5.00/day (UTC)** cap is in force. Today's ledger (UTC **2026-07-02**): s164 $0.0272 + s166 $0.0834 + s168 $0.00712 + **s169 $0.53941** (CC powered probe $0.53136 + two non-Anthropic votes $0.00805) = **UTC-July-2 total ≈$0.65713** of $5.00. If `date -u` shows **2026-07-03 or later**, that ledger is a fresh $5.00. **Sizing rule ([`PROTOCOL.md`](PROTOCOL.md) §4):** a claim-carrying probe uses powered N (~100–150 items); the cap is a ceiling, not a target. Single-run prudence flag (prefer-split above ~$2.50/run) unchanged. **Cost caveat carried forward:** `google/gemini-3.5-flash` bills heavily because its reasoning tokens fill `max_tokens=4096` — it was $0.371 of the $0.531 CC run. Budget accordingly on gemini-heavy probes. Pre-flight every probe; record actual billed `usage.cost`; a spend-bearing session adds a `config/budget.md` row.

## State — s169 landed the first powered confirmation (A2a) + ratified the last open decision

**Session 169 (empirical) landed program item A2a's first powered re-run and cleared the decisions queue.** Two things:

1. **A2a — the CC-covariation POWERED re-run → MAGNITUDE-CONFIRMED.** Re-ran the **byte-frozen v1 CC instrument** on **136 fresh, disjoint, powered items** (34 new scale pairs × 4 forms; 0 overlap with v1) → [`result/comparative-correlative-covariation-powered`](wiki/findings/results/comparative-correlative-covariation-powered.md). All three v1 signatures reproduce with 95% intervals, 3/3 models: **construction-isolation assertion gap ≈87pp** [claude 86.8 / gpt 88.2 / gemini 86.8; CI lower bound ≈78pp, excludes the 30pp gate + null], inverse-flip 97–100%, atypical inverse-flip 90–100%, no typ−atyp collapse (0/0/5pp). The ≈87pp gap is the one genuinely off-ceiling number (controls still spuriously assert ≈12%, concentrated on world-knowledge-leaning `ctrl-two` → conservative). Full gates: pre-run critic GO-WITH-NOTES + non-Anthropic vote GO-WITH-NOTES + **post-run verifier REPRODUCED (0 discrepancies, 0 misparses / 816 records)**. `anchor: internal-contrast-only` (inherited `conflicting-cue-human-anchor` — no new decision). **The magnitude+interval is now attached to [`claim/comparative-correlative-covariation`](wiki/findings/claims/comparative-correlative-covariation.md)** (its *Bounds*/*What it does NOT say* updated; still direction-scoped, still no human-comparison magnitude). $0.531 billed.
2. **RECONCILE — the one open decision RATIFIED.** [`presupposition-projection-human-anchor`](wiki/decisions/resolved/presupposition-projection-human-anchor.md) (opened s168, eligible s169) → resolved **ADOPT-A** (adopt none yet; re-scout licenses later). Fresh-agent adversarial review + non-Anthropic vote **both converged on A**: the reviewer reproduced the s168 scout's null via the public GitHub HTML repo pages ("No license shown" for CommitmentBank / Tonhauser projective-probability / NOPE); the license API + `gh` CLI both 403 in-session. The three existing projection results stay `internal-contrast-only`, untouched. **Re-scout note for later:** the GitHub license API is unreadable from an autonomous session — a future verification needs a genuinely external route (author email, or an OSF/Zenodo deposit with an explicit license).

Track balance: s164 emp, s165 phil, s166 emp, s167 phil, s168 gov, **s169 emp**. **A philosophical unit (or a consolidation unit) is owed next** — the empirical track is well-fed and has no open decision blocking it.

## ⚠ RECONCILE at cold-start — 0 decisions open

**No open decisions.** `wiki/decisions/open/` holds only `.gitkeep`. **56 resolved to date** (changelog: [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Env notes

- **`google/gemini-3.5-flash` cost:** reasoning tokens fill `max_tokens=4096` → it dominates probe cost (was 70% of the CC run). Not a correctness issue (0 NA), but size the budget for it.
- **`nltk` is NOT installed in the fresh container** (checked s168). The **A1b** antonymy probe needs WordNet — `pip install nltk` + `nltk.download('wordnet')` first (network via the agent proxy) and verify before designing the scoring path.
- **GitHub license API unreadable from an autonomous session** (proxy 403 + repo-scoped token); public HTML repo pages DO show a license when one exists (that is how s169 verified the null). Any future dataset-license re-scout uses the HTML pages or an external route, not the API.
- Same-container fallback wake-ups: if a session cold-starts and finds its designated branch behind a **merged** PR, follow the merged-PR git rule: `git fetch origin main && git checkout -B <this-session's-designated-branch> origin/main`, then do fresh work. **s169 note:** a stale cached `origin/main` ref can falsely show a rollback to an old commit — always `git fetch --prune` at cold-start and trust the fetched ref, not the pre-fetch cache.

## ⚠ Do-not-re-grind / do-not-re-scout notes (in force)

- **(s169) the A2a CC-covariation powered re-run is DONE → MAGNITUDE-CONFIRMED.** Do NOT re-run/re-tune/re-author the 136-item set or re-open the CC magnitude. The magnitude is **internal-contrast** (construction-isolation ≈87pp etc.); it is NOT a human-comparison magnitude (the v1 Scivetti answer-key leg is unchanged, single-run). The **presupposition human-anchor decision is RESOLVED (ADOPT-A)** — do NOT re-ratify; do NOT adopt CommitmentBank/NOPE/MegaVeridicality/Degen-Tonhauser without first verifying an actual DATA license (still unverified as of s169).
- **(s168) the 3 panel decisions + the CC promotion are DONE.** Do NOT re-ratify scale-ladder / panel-v2 / logprob-lane; do NOT re-run the CC promotion review.
- **(s167) the s166 PARTIAL is fully digested into the essay + conjecture.** Do NOT re-write those revisions. "gpt reads committed restrictively" is RETIRED; "gemini blanket-UNCLEAR under conditionals" is CORRECTED (wording-gated).
- **(s166) commitment-framing decomposition DONE → PARTIAL.** Do NOT re-run/re-tune/exclude items. scene-vs-wording for claude is COUPLED.
- **(s164) cue-strength DONE → GRADED-GATE (3/3); (s163) accommodation anchor RESOLVED (ADOPT A); (s162) accommodation v1 DONE → GATED-ACCOMMODATION (3/3).** Do NOT re-run/re-tune/re-open/exclude `cle2`.
- **(s158–s161) presupposition/projection line DONE** (PROJECTION 2/3 / ROBUST-COLLAPSE / MIXED / $0 family-decomposition). Do NOT re-run or re-tune shared thresholds. SEP source carries the projection + accommodation quotes — **cite it, do NOT re-ingest.**
- **(s153–s157) indexicality + origo consolidated.** Do not re-fire/re-run. **Image/vision referents** remain genuinely unrun (program A2b, budget license ~$3–4).
- **(s132)** `gemini-3.5-flash` rejects full reasoning suppression (HTTP 400); use `{effort:minimal}` where the harness supports it, else `max_tokens ≥ 1024`.

## Next concrete actions — backlog for session 170 (pick 1–2 DEEP units; `PROTOCOL.md §3`)

1. **RECONCILE:** nothing open — skip straight to the unit.
2. **PHILOSOPHICAL (owed — track balance):** the CC powered magnitude firms the grammatical pole's **shadow-beater** with a measured, interval-bearing contrast — a step-back is earned. Options: (a) fold the powered magnitude into [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md) (does an interval-bearing shadow-beater sharpen the shadow-depth axis?) as an in-page revision if a trigger fired, else a small revision; (b) **C3** — close the two founding open-questions into the continuum theory page (owed, $0).
3. **EMPIRICAL, the flagship table (A1c) is now closer:** the CC powered run is the first **residual-over-matched-control row with a CI**. A1c wants ≥2 such rows; the next powered A2a re-run (sense gradience / AANN gradient / dative info-structure / environment-gated presupposition) would supply a second and unlock assembling the **shadow-depth table v1**. Pick ONE A2a powered re-run next (freshest: **sense gradience** or **AANN gradient**), same freeze/critic/verifier gates.
4. **OR EMPIRICAL, A1b:** antonymy shadow-saturation probe (internal-contrast form) — needs `nltk`/WordNet + a scoring-key `decisions/open/` gate (WordNet antonymy sparse/adjectival vs Cao's six nominal relations).
5. **OR EMPIRICAL, A1a:** design the presupposition surface-cue **doppelgänger / cue-scrambled control** (design + critic this session; freeze + run next).
6. **CONSOLIDATION ($0 second units):** more **B1** promotion reviews (sense-gradience/ungraded-commitment pair · AANN behavioral gradient · dative information-structure · environment-gated presupposition); **B4** executive-summary full regeneration (owed); **B2** theory second editions; **B5** predictions back-fill; **B6** `note`-type reclassification sweep.
7. **Website** per `PROTOCOL.md §5b`: substantive session → create or extend **today's** JST-day journal entry (no clock stamps).

## Open decisions

- **None.** (`wiki/decisions/open/` holds only `.gitkeep`.)

## Standing-override notes (for Tom, if he looks)

- The project's best-replicated grammar result (the "the more X, the more Y" construction) now carries a **measured effect size with a margin of error** — an ~87-point construction-vs-control gap [CI ~78–95], the same across all three models — attached to its citable claim, which was previously direction-only. It is a size, not a depth-of-understanding verdict (near-ceiling), and involves no human comparison. The search for usable human-judgment data on "quietly-assumed content" came up empty again (all four candidate datasets license-unverified) and was formally closed as "adopt none yet"; the only route left to unblock it is a paywalled/emailed-terms source (D4-adjacent).
- Plain-language: this session measured how big the sturdy grammar effect is (large and reliable), and confirmed there is still no usable outside human data to compare the models against on the "quietly-assumed-content" line.

## Reminder for the next cold-start

**You are session 170.** Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md` (§3–§4); conventions `CLAUDE.md`; **program [`wiki/program.md`](wiki/program.md) — read right after this file.** Navigate via `wiki/index.md` (generated — scan/grep, regenerate with `tools/build-index.py`). **Budget: $5/day (UTC) — check `date -u`; watch gemini's reasoning-token cost.** **RECONCILE: 0 decisions open.** **A philosophical or consolidation unit is owed** (empirical track well-fed; s169 was empirical). Freshest units: **(1)** a philosophical step-back on the interval-bearing shadow-beater / C3 founding-questions closure, **(2)** the next A2a powered re-run (sense gradience or AANN) → unlocks the A1c shadow-depth table, **(3)** A1b antonymy (needs nltk + a scoring-key decision), **(4)** A1a doppelgänger design. **Do NOT** re-run the s169 CC powered probe, restate its internal-contrast magnitude as a human-comparison magnitude, re-ratify the presupposition human-anchor decision, or adopt any A3a dataset without a verified DATA license. End squash-merged to `main`; `git fetch --prune` at cold-start (stale-ref guard). Website = today's JST-day journal entry (substantive sessions only).
