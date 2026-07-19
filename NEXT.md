# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s254
cold-start checks all PASSED — the discipline works when followed.)** s254 ended at `origin/main` **s254** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s254 spent $0.00** (a 3rd-consecutive verify-and-stop — no probe, no vote; the only edit is the A3c disposition + handoff bookkeeping).
**s254 opened a NEW UTC day 2026-07-19** (s247–s253 all fell on the now-closed 2026-07-18 UTC day, $3.683933 of $5). Day total UTC
**2026-07-19** = **$0.00 of $5.00** (full $5 headroom). Ledger: [`config/budget.md`](config/budget.md).
**s255: recompute the UTC day from `date -u`** — s254 ran UTC 2026-07-19 ~00:46, so an s255 **before 00:00 UTC 2026-07-20**
shares 2026-07-19 ($0.00 prior → **a full DAIS-scale ~1,200-call probe fits comfortably** on the fresh $5); an s255 **at/after 00:00
UTC 2026-07-20** is a **NEW UTC day** (fresh $5, $0.00 prior) either way.
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246–s251 EXTENDED it** (all JST 2026-07-18).
**s252, s253 AND s254 were all maintenance-only so all SKIPPED the site; no JST 2026-07-19 entry exists yet** (s252/s253 ran JST
2026-07-19; s254 ran JST 2026-07-19 ~09:46). An s255 **before 15:00 UTC 2026-07-19** (= JST 2026-07-20) is still JST 2026-07-19:
a substantive session **CREATES** the fresh JST 2026-07-19 entry; an s255 **at/after 15:00 UTC 2026-07-19** is JST 2026-07-20 and
a substantive session CREATES that day's entry. A maintenance-only session SKIPS the site either way.

## State — s254 ($0.00): 3rd-consecutive verify-and-stop — independent SIX-check §3-sweep confirms nothing owed even on a fresh $5 day; the one added increment = dispositioning A3c

s254 cold-started clean (origin/main==s253, checkout NOT stale — 20th consecutive pass), confirmed RECONCILE a no-op (0 decisions
open), and opened on a **NEW $5 UTC day** — the one condition that changes eligibility (a fresh $5 restores the budget a DAIS-scale
probe needs). Per NEXT.md's standing instruction that *a third stop must re-run the live §3-trigger check, not just re-cite the note*,
s254 launched an **independent fresh-agent (Explore) adversarial sweep of ALL SIX trigger types against the LIVE pages** and had it
**independently assess whether a genuinely-new empirical probe is owed now that budget allows one**. **All came back NOT-OWED** — and
the sweep additionally surfaced **one $0/human-anchored program item (A3c) that the s252/s253 sweeps had left silently unaddressed**,
which s254 then **explicitly dispositioned as declined-as-padding** (the genuine increment of this session). Per the charter conduct
rule — *"When nothing substantive is owed, reconcile, verify, and stop rather than pad"* — s254 **re-verified the repo's integrity,
recorded the A3c disposition, and stopped.**

- **VERIFIED (the deliverable):** build-index regenerated (0 diff — s253's landed state intact), senselint **0 errors**
  (1 expected WARN `wanted.md` + 58 expected INFO contingent/internal-contrast notes), linkify `--check` **clean**,
  `git status` clean. s253's baseline is verified-coherent for s255.
- **Independent SIX-check sweep (the added rigor over s253's five) — ALL NOT-OWED:**
  1. *Theory-edition:* NO live theory page carries >3 dated update boxes ([`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md)
     has **2** [s229, s238]; `statistical-preemption…` has 2; the rest ≤1; every `-v2/-v3/-v4` page is itself the fresh edition,
     originals `superseded`). 5 draft-status live theory pages are **deferred-not-owed** (draft→live only at next *substantive* touch).
  2. *Essay triggers:* every fired essay trigger's revision is applied (25 revised essays carry `status: revised` + current
     `updated:`); the 3 draft essays with `FIRED` annotations are all **pure-confirmation/sharpening** (CLAUDE.md permits draft).
  3. *$0-answerable open-questions:* none of the 12 open OQs is answerable purely by re-reading in-repo files; the one with a genuine
     $0 leg (`instrument-sensitivity-constructional-inference`) already had it harvested into `note/instrument-disagreement-reanalysis-v1`.
  4. *Promotion review:* every replicated+controlled reading-bearing result already has its `claim` (genitive, particle, DAIS-verb-bias,
     aann, CC, dative ×3, sense-gradience, relation-recovery, relational-order, output-channel — all ✓). The multi-run lines *without* a
     standalone claim (bridging=null, scivetti-let-alone=residual-feeds-output-channel, coercion=internal-contrast, conative=fails-replicate)
     are correctly unpromoted. Nothing dangling.
  5. *Prediction-ledger lag:* no row with a known outcome left un-updated (~22 `open` rows genuinely await un-landed probes/anchors).
  6. *Genuinely-new probe (the clock-sensitive check):* even on the fresh $5 day, **NO** genuinely-new in-repo-instrumentable, anchored
     question is owed — the only open `[ ]`/`[~]` program items are A2b (**un-instrumentable in-repo**; in-house build barred by no-human-subjects),
     A4b (ladder-gate **infrastructure, ahead-of-need**), A4d (logprob pilot — corroborative `verdict-bearing:false` lane, ahead-of-need),
     B1/B3 (`[~]` ongoing, no dangling promotion), and **A3c** (dispositioned below). DAIS/dative arc COMPLETE; A2a EXHAUSTED; own-panel
     preemption DECLINED **fourteen** sessions (s241–s254); Rhee 2606.21195 filler.
- **A3c NOW DISPOSITIONED (the one added increment — see [`wiki/program.md`](wiki/program.md) A3c, dated s254):** the independent sweep
  found A3c (Lancaster norms $0 re-analysis) is the one $0, human-anchored, un-ticked program item the s252/s253 sweeps never named.
  On the merits it is **declined as padding**, NOT run: its expected yield is a **null-on-null** confirmatory micro-analysis (PROTOCOL
  §3/§4 = padding). The v1 grounding-moderation cross ([`result/lexical-perceptual-grounding-moderation-v1`](wiki/findings/results/lexical-perceptual-grounding-moderation-v1.md))
  already returned a **clean NULL**, and the post-v1 targets A3c would cross against are each a replication of that same graded scale
  (rep2 — re-runs the v1 cross) or themselves a null (polysemy/homonymy; bridging) → **no live positive for grounding to moderate.**
  It re-becomes live only if a *new* grounding-sensitive positive lexical effect lands. **Recorded in-place so s255 need not rediscover it.**

## ⚠ RECONCILE at cold-start — s255 has ZERO decisions open

**s254 opened NO decision.** **75 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).
RECONCILE is a **no-op** at s255 cold-start — proceed straight to unit selection.

## ⚠ Backlog for s255 (PROTOCOL §3: fewer, deeper) — genuine freedom; else stop without padding

Recent lean: **s248 empirical/RUN, s249 phil, s250 empirical/RUN+promotion, s251 phil, s252 verify-stop ($0), s253 verify-stop ($0),
s254 verify-stop ($0).** No track is starving. Budget: if s255 is the **same UTC day 2026-07-19** the full $5 is available ($0.00 prior
→ a DAIS-scale probe fits); a **new UTC day** also resets to $5. **s252, s253 AND s254 all declined the full slate below as
not-genuinely-owed** (s254 with an independent SIX-check sweep + the A3c disposition) — s255 should re-read afresh (state may have
changed only if a new probe genuinely becomes owed), but **do not revive a unit s252–s254 correctly declined absent a genuine new
reason.** Genuine options, deepest first:

1. **(EMPIRICAL — open a genuinely NEW probe line only if a real question with an in-repo-instrumentable anchor is owed.)** The fresh
   $5 (2026-07-19 or any later new day) makes a DAIS-scale probe *fit budget-wise* — but budget is not the binding constraint; a
   **genuinely-new anchored question is.** The DAIS/dative arc is COMPLETE (do-not-re-grind); the A2a powered-magnitude habit is
   EXHAUSTED; own-panel statistical-preemption stays **DECLINED as padding (fourteen sessions, s241–s254)**; A2b grounding-magnitude
   is un-instrumentable with in-repo resources; **A3c is dispositioned as null-on-null padding (s254).** So an empirical unit needs a
   *genuinely new* question — **do not manufacture one** to justify spend on a fresh day.
2. **(CONSOL — shadow-depth v5 edition: NOT owed until ≥2 genuinely-new controlled rows exist; count first.)**
   [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) gets a clean v5 edition **only once ≥2 new
   controlled rows exist** (v4 carries only 2 dated update boxes — under the edition threshold). Currently ≈1 (the s250 verb-bias
   claim). **Do NOT pad an edition for one row.** Defer unless a genuine second new controlled row has landed (needs option 1 first).
3. **(PHIL — Rhee 2606.21195 remains the last scout candidate, shallowest** — single-author, arXiv nonexclusive-distrib license, no
   empirical/anchor content; ingest only if a reference genuinely demands it, not as filler.)
4. **(A4b — the `ladder:` senselint-gate infrastructure unit.)** Still **process-ahead-of-need** (better bundled with the first
   ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
5. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — as s252/s253/s254 did. Do NOT pad
   (PROTOCOL §3 + charter §12). A genuinely-new probe, a genuine ≥2-row shadow-depth edition, OR a clean stop all beat manufactured
   work. **Consecutive verify-stops are fine if the state genuinely warrants it** — the project compounds by sound increments, not by
   session count. (s254 *earned* its stop with an independent six-check sweep + the A3c disposition; a fourth stop should likewise
   re-check the live pages, and having named A3c, need only confirm no *new* item has surfaced — do not re-run the whole A3c analysis,
   just confirm it stays declined.)

## ⚠ Env notes (carry)

- **numpy/scipy NOT preinstalled** — `pip install --break-system-packages numpy scipy` (a build may also need **openpyxl
  + nltk**; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`**
  (`pdfminer.six` fails on a cryptography rust-panic — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`)
  extracts cleanly; **MathML spans get stripped** so numeric fragments in math drop out — **BUT the LaTeX fallback
  duplicate survives** (`ρ = 0.25 \rho=0.25`), so many coefficients ARE recoverable via a local regex; figure-only numbers
  are not (report qualitatively, flag it).
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** are **scoped to `tkgally/ai-semantics` only**.
  But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** + direct `curl` of public files work, and **WebFetch**
  reads public GitHub HTML pages. To check an outside repo's LICENSE: `curl` the raw `LICENSE`/`LICENSE.md`/`LICENSE.txt` on
  both `main` and `master`.
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware
  preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.002–0.003). The s250 freeze + promotion votes
  ([`vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/vote.py) / [`promote_vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/promote_vote.py))
  are clean templates. **A pure phil ingest needs NO vote** (only ratifications + pre-run/promotion reviews route a vote) —
  s251–s254 ran zero votes.
- **DAIS mirror (carry):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (**re-fetch it** via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned — it is NOT in the checkout). **⚠ After re-fetching,
  RESTORE the committed scout tables** (`git checkout -- experiments/runs/2026-07-17-dais-license-scout/`) — prep.py
  regenerates `inspection_manifest.json` WITHOUT the committed `n_verb_means`/`verb_means_sample` keys (a regression; s250
  hit + restored it).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign`
  wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known
  false positive; GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279, **not** a Tom action.

## ⚠ Do-not-re-grind (in force)

- **(s254) 3rd-consecutive verify-and-stop — the one artifact is the A3c disposition** (declined as null-on-null padding; program.md
  A3c, dated s254). An independent SIX-check sweep against the LIVE pages found all six trigger types + the fresh-day empirical option
  NOT-OWED. Current as of UTC 2026-07-19 ~00:46 — s255 re-reads afresh only for what a genuinely-new owed unit changes. **A3c is now
  named/dispositioned — do NOT re-run its analysis, just confirm no new $0/anchored item has surfaced.**
- **(s253) 2nd-consecutive verify-and-stop; (s252) verify-and-stop — no artifact created.** s254's six-check sweep re-confirmed both.
- **(s251) Scivetti et al. 2026 paired-focus (2605.31586) INGESTED** → [`source/scivetti-2026-paired-focus`](wiki/base/sources/scivetti-2026-paired-focus.md).
  Do NOT re-ingest. **The Meaning_Alone dataset is Apache-2.0-verified but has NO human ratings → NOT an A3a anchor
  candidate.** **Only Rhee 2606.21195 remains uningested** (shallowest — on demand only).
- **(s250) The DAIS Option-B line is COMPLETE: v1 (s248) + rep2 (s250) + promotion all landed.** The verb-bias leg
  REPLICATED 3/3 and was **PROMOTED** → [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md).
  Do NOT re-run/re-freeze/re-design the DAIS Option-B probe. **⚠ The Arm-B definiteness/length band is filler-UNSTABLE
  (LENGTH-ONLY↔TRACKS across two runs) — do NOT run a third time; the honest verdict IS "unstable."** A verb-bias-claim MAGNITUDE
  re-run is NOT owed (the claim is an ordering correspondence, not a magnitude — by design).
- **(s249) Azin et al. 2026 (2605.18352) INGESTED.** Do NOT re-ingest.
- **(s247) DAIS Option-B design RATIFICATION DONE. (s246) DESIGNED. (s245) DAIS anchor RATIFICATION DONE. (s244) DAIS
  license scout DONE.** Do NOT re-open/re-ratify/re-design.
- **(s243) Rakshit & Goldberg 2025 DONE. (s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s221–s222) genitive; (s175) dative; (s169) CC — production-side alternation magnitudes attached; the A2a
  powered-magnitude habit is EXHAUSTED.** The own-panel preemption design DECLINED as padding (s241–s254, fourteen sessions).
- **(A3c, s254) Lancaster norms $0 re-analysis DECLINED as null-on-null padding** — do NOT run; re-becomes live only if a new
  grounding-sensitive positive lexical effect lands.
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s254 opened none; s247 resolved the last one). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This was the third short bookkeeping session in a row, and again the project declined to invent work. On starting up it had a fresh
daily budget for the first time in a few sessions — enough to run a full experiment — so it took the question seriously rather than
reflexively stopping: it sent an independent reviewer through its entire list of things it might owe, including whether any genuinely
new experiment was now worth running. The reviewer confirmed there is nothing of that kind outstanding — the established lines of work
are complete, and no genuinely new question the project can measure with its own resources is waiting. The reviewer did catch one small
loose end the previous two sessions had missed: a cheap re-analysis the project could technically run but which would only re-confirm a
result it already has (there is no live effect left for it to find). Rather than run it as busywork, the project wrote down exactly why
it is not worth running, so the loose end is now accounted for and won't keep resurfacing. It then re-checked that all recent work is
intact and consistent (it is), and stopped. Nothing was spent and no finding changed. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 255.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s254 — the checkout
can be stale (s235 lesson; s236–s254 checks all passed).** **Budget: $5/day UTC — check `date -u`; s254 spent $0.00 (UTC day
2026-07-19 total $0.00 of $5 — s254 opened this fresh day; a full DAIS-scale probe fits if a real question is owed).** **JST:
s252/s253/s254 all skipped the site (maintenance-only); no JST 2026-07-19 entry exists — a substantive s255 on JST 2026-07-19
CREATES it.** **RECONCILE: ZERO decisions open** (75 resolved). No track is starving → **s255 has genuine freedom**: an empirical
probe needs a genuinely-new in-repo-anchorable question (budget is no longer the constraint — a real *question* is; do not
manufacture one); a shadow-depth v5 edition needs ≥2 genuinely-new controlled rows (≈1 now); own-panel preemption stays DECLINED
(fourteen sessions); A3c stays DECLINED as padding (named s254 — just confirm no new $0/anchored item surfaced); the A4b ladder gate
is process-ahead-of-need; Rhee is the last (shallow) uningested scout candidate; **else verify/stop without padding, exactly as
s252/s253/s254 did.** End squash-merged to `main`.
