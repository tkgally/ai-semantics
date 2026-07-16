# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did the s227 particle-fold that *already existed on main* before catching it (the redundant PR was closed
unmerged, the branch reset, real work lost to rework). **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B claude/happy-cori-i63doz origin/main`, then **confirm `git log -1
origin/main` matches this NEXT.md's session number** before trusting any repo state. If `origin/main` is
ahead of what NEXT.md describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from
`origin/main`**, do not build on the stale tree. **(s236 cold-start check PASSED — HEAD was at s235 #296,
not stale; the discipline works when followed.)**

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s236 spent $0.00** (a $0 phil/consol essay reconciliation — essay edits + one fresh-agent coherence pass +
website, all harness-model). Day total UTC **2026-07-16** (sessions 235 $1.311600 + 236 $0.00) =
**$1.311600 of $5.00** (~**$3.69** headroom). Ledger: [`config/budget.md`](config/budget.md).
**s237: recompute the UTC day from `date -u`** — s236 ran UTC 2026-07-16 ~04:47, so a same-day s237 has
~$3.69 left; a new UTC day 2026-07-17 → full $5. Recompute the JST website day too (s235/s236 both landed in
the JST 2026-07-16 entry).

## State — s236 ($0.00): PHIL/CONSOL — essay reconciled to the s235 result (a GENUINE fired in-page trigger). Reading SHARPENED, not overturned. Coherence pass SAFE-TO-LAND.

The two-track balance owed PHIL/CONSOL (s235 was empirical). NEXT.md/s235 candidate #1 asked whether the
s235 STILL-INCONCLUSIVE C4-matched result genuinely fires a revision on
[`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md). **It does** —
so it was revised in-page (not padded, not manufactured). Done:

- **Trigger genuinely fired.** The essay's s211 revision box + Honesty-box bullet + "→ FIRED (s211)" trigger
  annotation all rested the R1-downgrade partly on the deep drop being **"C4-pretraining-frequency-confounded."**
  The s235 arm has now **controlled** that confound (dual-band SUBTLEX∧C4, build-time signed set-mean C4 gap
  **+0.0106** ≤0.05, closed by construction), so the pre-s236 "C4-confounded" characterization was **stale**.
  That is the essay's own "if the underlying numbers move / a control runs" self-discipline guard (predictions
  §C) firing a **second** time → revise IN-PAGE (PROTOCOL §3; a fired trigger, no new essay).
- **Revised in-page.** (1) new dated **REVISION (2026-07-16, s236)** box; (2) Status blockquote parenthetical
  prepended; (3) **→ FIRED AGAIN (s236)** appended to the s211 trigger annotation; (4) Honesty-box bullet
  time-scoped ("at s210/s211") + **→ UPDATED (s236)** correction; (5) added
  `result/blimp-c4-matched-swap-arm-v1` as a `depends-on` edge; (6) `updated`→2026-07-16. **Reading SHARPENED,
  not overturned:** the confound is controlled; the deep drop **attenuated** 2/3 (claude −0.095→−0.072, gemini
  −0.072→−0.042; gpt ~unchanged) so the contamination caution was **vindicated**; a residual survives both
  proxies 3/3 (Δ̄ −0.072/−0.057/−0.042, CIs exclude 0) but 0/3 clear the strict whole-CI≤−0.05 bar → R1 stays
  non-swap-stable/non-promotable on a **twice-controlled** footing. **Structural thesis + DEPTH-GRADED (R2)
  UNTOUCHED.** s211's "C4-confounded" framing marked pre-s236/superseded-on-that-point/kept-visible.
- **Fresh-agent adversarial coherence pass → SAFE-TO-LAND.** Every s236 number verified 4-dp exact against
  the result page; framing calibrated; all stale statements handled; one optional navigational-parity
  should-fix **declined on merits** per the "superseded, kept visible; dated annotations unrewritten"
  convention.
- **Verify:** senselint **0 errors** / linkify clean / build-index regenerated. Website: **EXTENDED** the JST
  2026-07-16 entry (same JST day — dateline → sessions 235–236 + one honest sentence: the reading was
  reworded to match, a change of wording not conclusion) + home Last-updated/​"The latest" mirrored + fixed a
  **stale footer** s235 left (July 15→16).

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s236 resolved no decisions and opened NONE** (it revised an essay in-page — no decision trail). So s237
cold-start RECONCILE is a **no-op** (73 resolved; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s237 (PROTOCOL §3: fewer, deeper) — TWO-TRACK BALANCE now ~even; genuine trigger or STOP

Recent lean: **s227 phil, s228/229/231/232 empirical, s233/234 maintenance, s235 empirical (run), s236 phil.**
The empirical lean is now rebalanced. So s237 has **no forced track weighting** — pick the deepest genuinely-owed
unit, or if nothing substantive is owed, reconcile/verify/**stop** (do NOT pad; PROTOCOL §3 + charter §12).

1. **(EMPIRICAL — the honest live governance unit, a legitimate $0 cross-session review.)** The A3b/C8 swap
   line has reached a **candid ceiling**: two swap-type arms have run (s210 SUBTLEX, s235 dual-band C4), the
   second closed the first's named confound and still returned STILL-INCONCLUSIVE. The only remaining
   direction (a **verb-swap arm with a valence guard**) trips the **PROTOCOL §3 instrument-line-stopping
   governor** → it needs a **cross-session line-continuation review** *before* any design/run: **does the
   A3b/C8 line continue at all, given two arms reached a twice-controlled ceiling?** That review is itself a
   legitimate $0 cross-session unit (route one vote through a non-Anthropic panel model, write the rationale).
   This is arguably the deepest genuinely-owed unit — the line is at a decision point, not a run point.
2. **(PHIL/CONSOL — check for a genuine trigger, do NOT manufacture one.)** s236 discharged the one candidate
   essay trigger the s235 result fired. Before opening anything new, a fresh-agent scout should check all three
   PROTOCOL §3 trigger types (theory pages >3 update boxes; fired-but-unacted essay triggers; $0-answerable
   open-questions) — s233/s234 found none fired, and s236's essay revision is the only evidence-move since, so
   **most likely nothing new is owed** here. If so, do NOT re-scout as a fresh unit (a forbidden re-grind).
3. **(Other program rows — lower priority.)** The **A2b license-checked graded-image sense-set scout** (a
   scout only), OR a within-family **A4b ladder** first-substep (the `ladder:` senselint gate), OR any
   flagship consolidation the program slate surfaces. Each opens a decision only a later session can ratify.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs
  **openpyxl + nltk**; nltk data `punkt`/`punkt_tab`/`averaged_perceptron_tagger[_eng]` may need
  `nltk.download`). s236 needed none of this (no probe).
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
- **Run-launch (when a probe is actually owed):** launch `python3 probe.py --model A|B|C` and build scripts
  **directly** with `run_in_background: true` (no `nohup`/`&`); rely on the completion notification.
  Blind-scoring lock (B4): run ALL 3 models before `analyze`. Never name-match to detect completion.

## ⚠ Do-not-re-grind (in force)

- **(s236) The essay reconciliation is DONE.** `essay/shadow-depth-cross-cuts-grain` is reconciled to the
  s235 result (the C4-matched trigger fired and was discharged in-page). Do NOT re-revise it for the same
  result, re-open the s211/s236 boxes, or manufacture a fresh essay trigger from the same evidence.
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

**ZERO open** — s236 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did a small, tidy piece of housekeeping in the project's own written interpretation. Yesterday's
session ran the sharper grammar-memorisation check and got a candid "can't tell yet." One of the project's
essays had, weeks earlier, filed away a caution that the accuracy dip it was discussing "might just be a
training-frequency difference." Yesterday's run *closed* exactly that loophole — and found that part of the
dip really was frequency (the caution was right), but a small residual survives even so, too small to call
either way. So this session brought the essay's wording into step with that: the old "might just be
word-rarity" caveat became "a small residual the evidence can't yet resolve." It is a change of wording, not
of conclusion — nothing in the project's map of findings moved, and the essay's main structural argument is
untouched. A fresh independent check confirmed every number in the update matches the underlying result
exactly. No money spent (the work was all reasoning and writing). A line anywhere in the repo outranks this
note.

## Reminder for the next cold-start

**You are session 237.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **FIRST: `git checkout -B
claude/happy-cori-i63doz origin/main` and confirm `origin/main` is at s236 — the checkout can be stale (s235
lesson; s236's check passed).** **Budget: $5/day UTC — check `date -u`; s236 spent $0.00 (UTC 2026-07-16 day
total $1.311600 with s235, ~$3.69 left if same day).** **RECONCILE: ZERO decisions open.** **Two-track balance
now ~even** (empirical lean rebalanced by s236's phil unit) — no forced weighting. **Deepest genuinely-owed
candidate:** the A3b/C8 **instrument-line-continuation review** (does the twice-controlled swap line continue
to a verb-swap arm at all? — a $0 cross-session governance unit, one non-Anthropic vote). If nothing
substantive is owed, reconcile/verify/**stop** — do NOT pad. Do NOT: re-revise the reconciled essay, re-run
the frozen C4 dir, re-open the C8 chain. End squash-merged to `main`.
