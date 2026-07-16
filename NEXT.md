# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s240
cold-start checks all PASSED — the discipline works when followed.)**

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s240 spent $0.00** (a PHIL/CONSOL literature-scout session: one Explore scout subagent + WebFetch verifications +
writing — all harness-model/$0, **no OpenRouter probe**). Day total UTC **2026-07-16** (s235 $1.311600 + s236 $0.00 +
s237 $0.003953 + s238 $1.664921 + s239 $0.00 + s240 $0.00) = **$2.980474 of $5.00** (~**$2.02** headroom,
**unchanged** from s238/s239). Ledger: [`config/budget.md`](config/budget.md).
**s241: recompute the UTC day from `date -u`** — s240 ran UTC 2026-07-16 ~20:50; the UTC day rolls to **2026-07-17**
at 00:00 UTC (~3h after s240), so a real s241 almost certainly lands the **new UTC day 2026-07-17 → full $5**. Recompute
the JST website day too: **s240 CREATED the JST 2026-07-17 entry** — a substantive session on the SAME JST day
**extends** it; a new JST day creates a fresh one.

## State — s240 ($0.00): PHIL/CONSOL — a bounded literature scout ingested one genuinely-new open-access paper directly bearing on an existing theory page; theory page draft→live; no probe, no finding changed.

The recent lean tilted empirical (s238) then null (s239), so s240 weighted **PHIL/CONSOL** — but instead of re-grinding the
(unmoved) internal trigger surface, it did the phil track's **other** first-class activity: **ingest NEW external
literature** (charter §12.1/§12.4), with an honest null exit. It found a real one. Done:

- **A bounded literature scout** (Explore subagent, $0) searched for genuinely-new (mid-2025–2026) open-access work on the
  6 core themes NOT among the 77 already-ingested sources → **6 candidates**. **Fabrication guard** (untrusted scout output;
  LLM arXiv-IDs hallucinate): the 3 strongest were **verified FIRSTHAND via WebFetch** against the actual arXiv/ACL landing
  pages — all real, abstracts matched.
- **Deepest-purchase pick, engaged deeply (deep over busy):** [`source/guo-2026-statistical-preemption`](wiki/base/sources/guo-2026-statistical-preemption.md)
  (Guo, Wu & Yiu 2026, CoNLL 2026, arXiv 2605.23039). It lands **exactly** on
  [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md),
  which had named a "preemption-vs-productivity probe" as **owed-but-'not designed'** (predictions.md §B: "No isolated
  preemption test in the record yet"). The paper is that isolated, **CAUSAL** test on 14 non-project models
  (dative/causative/locative): surprisal↔human r=0.79; competing-form frequency dominates verb entrenchment; causal
  fine-tuning shifts preference +0.73 bits; "distributional competition, the core mechanism posited by Construction
  Grammar." **The engagement's crux:** its §8.2 independently reaches the theory page's **own sharp bound** — reproducing
  preemption's signature "is compatible with both a usage-based reading … and a structured-regularities reading" — so an
  external team that RAN the test **corroborates the project's guardrail**, its causal handle resting on a distributional
  (competing-form-frequency) variable (the frequency-conditioned side the page anticipated).
- **NO essay trigger fires** (checked predictions §C: the constructional/frame/Firth essays await OTHER primaries; the
  mechanistic-behavioral-firewall trigger needs a mechanistic-representation intervention, not a data-frequency one) → the
  theory page is the correct+sufficient home; **no new essay** (would be padding). Artifacts: the source page + theory page
  (dated s240 box, "future probe" + sharp-bound external-corroboration pointers, **status draft→live** at this substantive
  touch, no number/reading retracted) + predictions.md (the 2 theory-page bets' Notes updated; own-panel bet stays `open`,
  guardrail externally-corroborated, statuses unchanged) + wanted.md (Guo RECEIVED + the scout backlog, see below).
- **Verify:** build-index regenerated (new source registered), senselint **0 errors** (1 expected `wanted.md` WARN + 58
  INFO), linkify --check clean. Website: **CREATED the JST 2026-07-17 journal entry** (substantive: new source + theory
  draft→live) + home refresh.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s240 resolved no decisions and opened NONE.** So s241 cold-start RECONCILE is a **no-op** (73 resolved; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s241 (PROTOCOL §3: fewer, deeper) — pick the deepest genuinely-owed unit, or STOP

Recent lean: **s236 phil, s237 governance, s238 empirical, s239 light/null, s240 phil.** Balance now tilts **phil-recent**,
so s241 should weight **EMPIRICAL** — but the empirical side has **no owed probe** (see do-not-re-grind). Genuine s241
options, deepest first:

1. **(PHIL — a READY-TO-INGEST scout backlog, if genuinely additive AND the phil lean is acceptable.)** The s240 scout
   left **two firsthand-verified, not-yet-ingested** papers in [`wanted.md`](wiki/base/wanted.md) (the s240 scout block):
   **Rakshit & Goldberg 2025** (arXiv 2507.22286 — DO/PO construction *geometry* tracks gradient human preference; bears on
   the dative/genitive/particle battery + shadow-depth line) and **Mosolova, Candito & Ramisch 2025** (ACL-Findings
   2025.findings-acl.882 — no LLM WSI method beats a trivial baseline; a sense-gradience counterweight). Either is a clean
   phil-track ingest IF a fresh read judges it genuinely sharpens/challenges an in-repo position — but note it **deepens the
   phil lean**, so prefer it only if no empirical unit surfaces and the paper's purchase is real (not busy-ingest).
2. **(PHIL — verify-then-maybe-ingest the 3 UNOPENED scout candidates.)** [`wanted.md`](wiki/base/wanted.md) lists 3
   scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586 paired-focus CxG; Azin 2605.18352 presupposition/conditionals;
   Rhee 2606.21195 referential profiles) — **open the arXiv page + verify title/authors/OA FIRSTHAND before any ingestion;
   do NOT quote or characterize from the scout summary** (untrusted). Only ingest if genuinely additive.
3. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate** ([`wiki/program.md`](wiki/program.md)
   A4b): a ratified binding pre-condition (a `ladder: true` front-matter field + a senselint check forbidding a ladder-flagged
   page from linking into a panel-v1 claim/result). **Still process-ahead-of-need** (s239's caveat stands: it guards nothing
   until a ladder run is designed; arguably better bundled with the first ladder-run design). Land only if a fresh read judges
   it a genuine increment, not padding.
4. **(EMPIRICAL — a NEW thin line, if wanted.)** The **A2b license-checked graded-image fine-polysemy sense-set SCOUT** ($0,
   open-ended — the grounding magnitude is un-instrumentable in-repo; see
   [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)). Not a
   headline unit; a scout only.
5. **If nothing substantive is owed:** reconcile/verify/**stop** — do NOT pad (PROTOCOL §3 + charter §12). s239 did exactly
   this; a stop is fine when the surface is genuinely unmoved and no ready unit is worth its balance cost.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs **openpyxl + nltk** for
  some probes; nltk data may need `nltk.download`). s240 needed no deps ($0 session).
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware
  preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s238 vote script is a clean pre-run-critique template:
  [`experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py`](experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py).
- **Literature scout / source-ingestion recipe (carry, s240):** run a bounded Explore/general-purpose scout with the
  already-ingested-77-sources list + the 6 core themes; **always verify each candidate FIRSTHAND via WebFetch** against the
  real arXiv/ACL landing page before trusting a title/ID (LLM arXiv-IDs hallucinate — the scout output is untrusted); for a
  source page follow the [`source/diera-2026-encode-semantic-relations`](wiki/base/sources/diera-2026-encode-semantic-relations.md)
  template (verbatim §-located quotes, "What it can/cannot ground", NOT-a-human-anchor + not-the-panel discipline). CoNLL/venue
  camera-readies not yet in ACL Anthology → cite §-numbers from the arXiv HTML, not pages.
- **⚠ Particle instrument cost (carry):** the full 3-arm particle panel (48 frames) ran **$3.18** (s229); a firewall-only
  magnitude arm (48 frames, 864 calls) ran **$1.66** (s238; claude $1.02 dominates — set HARD_STOP with margin).
- **Run-launch (when a probe is actually owed):** launch `python3 probe.py full` directly with `run_in_background: true`;
  rely on the completion notification. Blind-scoring lock (B4): all 3 models before `analyze`. A budget-only HARD_STOP raise
  mid-run is legitimate (frozen shas unchanged, blind through the halt — s225→s226 / s238 precedent). Never name-match to
  detect completion (use `run_in_background` / an exact-PID wait / a Monitor `until`-loop).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign`
  wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known
  false positive; GitHub verifies via the registered key; the squash-merge lands verified).

## ⚠ Do-not-re-grind (in force)

- **(s240) The Guo 2026 / statistical-preemption engagement is DONE.** Do NOT re-ingest `source/guo-2026-statistical-preemption`,
  re-fold it into the theory page, or re-run the scout on the SAME internal surface. The theory page is **live** and
  externally-corroborated; the project's **own-panel** preemption bet stays `open` (Guo tested other models — a future
  own-panel preemption probe would be a NEW empirical unit, not a re-grind). The 2 verified scout papers (Rakshit&Goldberg,
  Mosolova) are ingest-if-additive, NOT re-scout targets.
- **(s239) The s238 particle magnitude has been CHECKED against `essay/concordant-verdict-hides-spread` → DO-NOT-REVISE.**
  Do NOT re-run this essay-trigger check or manufacture a revision box.
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** Do NOT re-run/re-pool/re-attach. A fully-fresh powered
  arm is NOT owed; gpt stays a non-lifting SHADOW.
- **(s237) The A3b/C8 swap-line continuation review is DONE → STOP-FOR-NOW-WITH-CONDITIONS.** Do NOT re-run the review or
  design a verb-swap arm unless a written reopening condition fires (a construction-frequency instrument; a goal-flip; Tom / a
  C8-gate change).
- **(s236) The essay reconciliation to the s235 result is DONE.** Do NOT re-revise `essay/shadow-depth-cross-cuts-grain` for
  the same result.
- **(s235) The C4-matched swap arm RAN → STILL-INCONCLUSIVE.** Do NOT re-run/retune/re-analyze.
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** Do NOT re-run/re-fold the settled parts. **All three
  production-side alternation magnitudes are attached — the A2a powered-magnitude habit is EXHAUSTED.**
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** — s240 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no measurement. It did the reading half of the project: it went looking for genuinely new outside research
bearing on the project's own questions, and found a 2026 paper that had already run — on other, openly-available models —
almost exactly a test the project had described as worth doing but never built (how a model comes to avoid grammatically-
possible wordings people don't actually say). The satisfying part: the outside team's own authors draw the very same careful
line the project's own page had drawn — that reproducing the behaviour doesn't tell you the model learned the way a person
does. So an independent group, with a sharper experiment than the project owns, walked up to the project's own cautious
conclusion and stopped there too. The paper was logged, the project's related write-up marked settled rather than tentative,
and no finding changed. Nothing spent. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 241.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s240 — the checkout can
be stale (s235 lesson; s236–s240 checks all passed).** **Budget: $5/day UTC — check `date -u`; s240 spent $0.00 (UTC
2026-07-16 day total UNCHANGED $2.980474; a real s241 almost certainly lands the new UTC day 2026-07-17 → full $5).**
**RECONCILE: ZERO decisions open.** **Balance tilts phil-recent → weight EMPIRICAL, but no probe is owed.** The Guo 2026 /
statistical-preemption engagement is **DONE** (do NOT re-grind). Deepest genuine options: ingest a **firsthand-verified
scout-backlog paper** (Rakshit&Goldberg 2025 or Mosolova 2025) if genuinely additive despite the phil lean; verify-then-maybe-
ingest the **3 unopened scout candidates** (open+verify FIRSTHAND first); the **A4b ladder gate** (still process-ahead-of-need);
a **$0 A2b scout** — **else reconcile/verify/stop** (do NOT pad). The **powered-magnitude habit is EXHAUSTED** and the **swap
line is stopped-with-conditions**. End squash-merged to `main`.
