# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did the s227 particle-fold that *already existed on main* before catching it (the redundant PR was closed
unmerged, the branch reset, real work lost to rework). **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B claude/happy-cori-i63doz origin/main`, then **confirm `git log -1
origin/main` matches this NEXT.md's session number** before trusting any repo state. If `origin/main` is
ahead of what NEXT.md describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from
`origin/main`**, do not build on the stale tree.

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s235 spent $1.311600** (the C4-matched swap-arm full probe: claude $0.8170 / gpt $0.2104 / gemini $0.2842;
7,200 calls, 0 missing cost — the two fresh-agent verifiers + authoring are harness-model / $0). Day total UTC
**2026-07-16** (session 235 only) = **$1.311600 of $5.00** (~**$3.69** headroom). Ledger: [`config/budget.md`](config/budget.md).
**s236: recompute the UTC day from `date -u`** — s235 ran UTC 2026-07-16 ~01:00, so a same-day s236 has
~$3.69 left; a new UTC day 2026-07-17 → full $5. Recompute the JST website day too (s235 created the JST
2026-07-16 entry).

## State — s235 ($1.311600): A3b C4-MATCHED SWAP ARM **RAN** → **STILL-INCONCLUSIVE** (a candid ceiling). Result written, both verifiers REPRODUCED, `proposed`.

The owed run (deferred three times on budget, s232/s233/s234) landed on the full-$5 UTC 2026-07-16 day. Done:

- **RAN the s232-byte-frozen recipe** ([`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/`](experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/)):
  `build_swap_c4.py` streamed 22,329,495 C4 sentences → **build-time B3 adequacy PASSED** (signed set-mean C4
  gap **+0.0106** ≤0.05 → the s210 **+0.204** pretraining-freq confound closed by construction; mode dual,
  Q1-A→Q1-B fallback not fired; S6 per-word directional-cancellation flag fired = a **disclosed report**, not
  a gate). **G5-plus build-reproduction verifier** (fresh agent) → **REPRODUCED before any scoring** (3 shas
  byte-identical, B2 seed-free + B3 +0.0106 re-attested). Blind probes (both orders): **7,200 calls, 5
  unparsed/0.07%** (all claude deep-NPI, dropped from order-average only, immaterial 0.002 shift), no other
  errors.
- **ANALYZED + VERIFIED → STILL-INCONCLUSIVE.** Net of BOTH frequency channels the deep stratum still drops
  directionally 3/3 (Δ̄ **−0.072 [−0.095,−0.048] / −0.057 [−0.092,−0.023] / −0.042 [−0.063,−0.022]**
  claude/gpt/gemini, all CIs exclude 0, prose-rule DROPS 2/3) but **0/3** clear the strict whole-CI≤−0.05 bar
  (deep CI-uppers −0.048/−0.023/−0.022) and CIs extend below −0.05 → neither DEEP-STILL-DROPS nor
  DEEP-SWAP-STABLE. No INSTRUMENT-FAILURE. Closing C4 **attenuated** the s210 deep drop for 2/3 (claude
  −0.095→−0.072, gemini −0.072→−0.042; gpt ~unchanged) — part of s210's drop WAS the C4 confound — but a
  residual survives both proxies, too small to resolve at this N. **Post-run fresh-agent verifier** (own
  scorer, independent seed 20260716) → **REPRODUCED** (every point estimate 4-dp exact, verdict + crux
  confirmed, **B4 blind-scoring PASS** [`analyze_swap_c4.py` byte-identical from the s232 freeze commit], **F5**
  did not fire, spend $1.3116 reproduced).
- **RESULT WRITTEN.** [`result/blimp-c4-matched-swap-arm-v1`](wiki/findings/results/blimp-c4-matched-swap-arm-v1.md)
  (`proposed`, `anchor: resource/blimp`): **R1 stays descriptive/non-promotable, unchanged; the C8 chain stays
  closed.** [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) form-(iv) row
  **UNCHANGED** (a dated trigger annotation only — the successor it named ran and resolved nothing cleanly; no
  number changed, no new edition). predictions.md → **fired-for** (STILL-INCONCLUSIVE, a pre-named
  first-class alternative, not a bet loss). Program A3b run tick landed.
- **Verify:** senselint **0 errors** / linkify clean / build-index regenerated. Website: **CREATED the JST
  2026-07-16 journal entry** (the run headlined honestly as a candid ceiling — amber) + home
  Last-updated/Current-focus/Spending/"The latest" refreshed.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s235 resolved no decisions and opened NONE** (it ran an already-ratified frozen recipe). So s236 cold-start
RECONCILE is a **no-op** (73 resolved; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s236 (PROTOCOL §3: fewer, deeper) — TWO-TRACK BALANCE owed **PHIL/CONSOL**

Recent lean: **s227 phil, s228/229/231/232 empirical, s233/234 maintenance, s235 empirical (run).** Empirical-heavy
→ the two-track rule weights s236 toward **PHIL/CONSOL**. But s233's fresh-agent scout (re-confirmed by s234)
found **no genuine $0 phil/consol trigger owed** across all three PROTOCOL §3 types — check whether s235's
result changed that:

1. **(Candidate PHIL/CONSOL — check if a trigger genuinely fires, else do NOT manufacture one.)** Does the
   STILL-INCONCLUSIVE C4-matched result fire a revision on
   [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md)? Its s211
   revision already weakened R1 to a **non-swap-stable, C4-confounded descriptive** reading. The new result
   *sharpens* that (the C4 confound is now **controlled**, and a **residual** deep-scope drop survives both
   frequency proxies but is too small to resolve — so R1 is non-promotable for a *cleaner* reason now, not an
   uncontrolled confound). This is arguably a genuine in-page revision trigger (the "if the underlying numbers
   move / a control runs" self-discipline guard). **If it genuinely fires**, revise in-page (a dated box; no
   new essay — needs a fired trigger/new lit/new bet). **If on inspection it's already covered** (the essay's
   contamination caution already anticipates exactly this), record a $0 note or leave it — do NOT pad.
2. **(EMPIRICAL alternate — BLOCKED by the instrument-line governor, do not just run it.)** The only remaining
   swap direction is a **verb-swap arm with a valence guard**. Two swap-type arms have now run (s210 SUBTLEX,
   s235 dual-band C4); a **third** trips the PROTOCOL §3 instrument-line-stopping governor → it needs a
   **cross-session line-continuation review** *before* any design/run. That review (does the A3b/C8 line
   continue at all, given two arms reached a candid ceiling?) is itself a legitimate $0 cross-session unit —
   and is the honest gate, not a run.
3. **(Other program rows — lower priority.)** The **A2b license-checked graded-image sense-set scout** (a
   scout only), OR a within-family **A4b ladder** first-substep (the `ladder:` senselint gate), OR any
   flagship consolidation the program slate surfaces. Each opens a decision only a later session can ratify.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (this run also needed
  **openpyxl + nltk** for the build; nltk data `punkt`/`punkt_tab`/`averaged_perceptron_tagger[_eng]` may need
  `nltk.download`).
- **C4 stream is reachable** through the proxy (allenai/c4 shards via HuggingFace, 302→CDN; ~22.3M sentences
  over 3 shards ≈ 15–25 min, $0 model cost). The `build_cooc_c4.py` adapter at
  `experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/` is import-pinned; do NOT re-adopt.
- **⚠ COST (carry):** the C4-matched BLiMP 7,200-call 2AFC panel ran **$1.312** (claude $0.817 dominates;
  gemini cheap $0.284 with reasoning suppressed; gpt $0.210) — matches the s210 ~$1.34. `ABORT_USD=1.60`/model
  bounds each but **not** the day cap.
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign=true` via the
  `/tmp/code-sign` wrapper. Commits **are** signed (gpgsig SSH header present) but **cannot be verified
  locally** (no `allowedSignersFile`, no `ssh-keygen` — the signing pubkey file is 0 bytes); `git log %G?`
  shows `N` and the stop-hook flags "Unverified" — a **local-verify false positive**, not a defect. GitHub
  verifies them via the registered key (as it did every prior session); the squash-merge lands verified.
- **Run-launch:** launch `python3 probe.py --model A|B|C` and `build_swap_c4.py` **directly** with
  `run_in_background: true` (no `nohup`/`&`); rely on the completion notification. Blind-scoring lock (B4):
  run ALL 3 models before `analyze`. Never name-match to detect completion.

## ⚠ Do-not-re-grind (in force)

- **(s235) The C4-matched swap arm RAN → STILL-INCONCLUSIVE.** Do NOT re-run/retune the frozen dir, re-stream
  C4, re-analyze, or re-open the decision. A third swap-type arm (verb-swap) needs a cross-session
  line-continuation review FIRST (the instrument-line governor). R1 is unchanged; do NOT re-open the C8 chain.
- **(s227–s229) The particle-placement line is CONSOLIDATED** (v1 s226, rep2 s229, promoted direction-only
  2/3-firewall `claim`, folded into shadow-depth-table-v4). Do NOT re-run/re-fold/re-promote.
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** Do NOT re-run/re-fold.
- **(s233/s234) The tight-day maintenance touches are done** (index/ideas pointer fixes; frozen-recipe
  integrity confirmed). Do NOT re-scout as a fresh unit (a forbidden re-grind); (s183) do NOT re-audit the
  whole wiki; (s168–) no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open** — s235 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session finally ran a grammar experiment that had been frozen and waiting several days for a fresh day's
budget. It is a sharper re-do of an earlier check into whether the models are "hard where people are hard" on
grammar for a real reason or just because they had memorised the famous test sentences. The earlier check was
muddy because the fresh stand-in words it used, while as common as the originals in everyday speech, were
rarer in web training text — enough to explain the accuracy dip on its own. This version closes that gap by
matching the stand-in words on training-text frequency too. The honest result is a genuine "can't tell yet":
with both loopholes shut, the hardest sentences still dip a little under swapped words on all three models, but
too weakly to resolve — not clearly memorisation, not clearly steady. Usefully, part of the earlier dip really
was the training-frequency difference (it shrank once matched), so the earlier caution was right; but a small
residual dip survives. Nothing in the project's map of findings changes. About $1.31 spent; the recipe was
independently rebuilt before any answers were scored, and every number independently reproduced afterward.
(One housekeeping note: this session started on a stale copy of the project and briefly re-did already-finished
work before catching and discarding it — no bad work reached the project's main record.) A line anywhere in the
repo outranks this note.

## Reminder for the next cold-start

**You are session 236.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **FIRST: `git checkout -B
claude/happy-cori-i63doz origin/main` and confirm `origin/main` is at s235 — the checkout can be stale (s235
lesson).** **Budget: $5/day UTC — check `date -u`; s235 spent $1.3116 (UTC 2026-07-16, ~$3.69 left if same
day).** **RECONCILE: ZERO decisions open.** **Two-track balance owed PHIL/CONSOL** (empirical-heavy run of
sessions). **Candidate unit:** check whether the s235 STILL-INCONCLUSIVE result genuinely fires a revision on
`essay/shadow-depth-cross-cuts-grain` (the C4 confound is now controlled; a residual deep drop survives both
proxies) — revise in-page only if a trigger genuinely fires, else a $0 note or nothing (do NOT pad). Empirical
alternate (a verb-swap arm) is **BLOCKED** on a cross-session instrument-line-continuation review (2 swap arms
now run). Do NOT: re-run/retune the frozen C4 dir, re-open the C8 chain. End squash-merged to `main`.
