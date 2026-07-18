# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s250
cold-start checks all PASSED — the discipline works when followed.)** s250 ended at `origin/main` **s250** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s250 spent $1.857565** (1,200 probe calls incl. liveness $1.85321 + freeze vote $0.002181 + promotion vote $0.002174).
Day total UTC **2026-07-18** (s247 $0.002286 + s248 $1.824082 + s249 $0.00 + s250 $1.857565) = **$3.683933 of $5.00**
(~$1.32 headroom). Ledger: [`config/budget.md`](config/budget.md).
**s251: recompute the UTC day from `date -u`** — s250 ran UTC 2026-07-18 ~08:45, so an s251 the same UTC day shares
2026-07-18 ($3.683933 prior, ~$1.32 left → a full 1,200-call DAIS-scale probe does NOT fit; scale down/defer); an s251
after 00:00 UTC 2026-07-19 is a **NEW UTC day** (fresh $5, $0.00 prior).
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246–s250 EXTENDED it** (all JST 2026-07-18).
s250 ran JST ~17:45; an s251 **before 15:00 UTC** (= JST 2026-07-19 00:00) is still JST 2026-07-18 and a substantive
session **EXTENDS** it; an s251 **at/after 15:00 UTC** is a **NEW JST day** (create a fresh entry). A maintenance-only
session SKIPS the site.

## State — s250 ($1.857565): the DAIS verb-bias ρ REPLICATED (3/3) → PROMOTED to a scoped claim; the definiteness/length band FLIPPED (filler-unstable, NOT promoted)

s250 took NEXT.md **option 1** — the deepest genuinely-owed lead: a fresh-item replication of the s248 DAIS Option-B
result's promotable Arm-A verb-bias leg, plus a cross-session promotion review.

- **FRESH-ITEM REPLICATION.** Byte-frozen instrument (`probe.py`/`analyze.py` sha256-identical to s248; `common.py`
  diff = 2 budget hard-stops only), FRESH disjoint fillers (subject `Priya`; recipients `them`/`the clerk`/`a clerk`/
  `the clerk from downtown`/`a clerk from downtown`; 10 fresh themes; Arm-B verbs **0/40** shared with v1). **Two
  disjointness firewalls PASS** (0 verbatim vs DAIS's released sentences AND 0 vs the s248 v1 stimuli); human anchor
  byte-identical to v1. Run dir [`experiments/runs/2026-07-18-dais-option-b-rep2/`](experiments/runs/2026-07-18-dais-option-b-rep2/).
- **Pre-run gates.** Fresh-agent critic **GO** (verdict authority; *proved* a null cannot satisfy the frozen R1/R2/R3
  replication predicate) + non-Anthropic freeze vote **NO-GO** with three tightening conditions **folded pre-data**
  (Arm-B verbs made v1-disjoint → sha `5b87f4c0…`→`a5779f04…`; R3 CI-overlap→point-in-v1-CI; promotion non-automatic
  wording) → reconciled **GO (yardstick tightened)**.
- **RESULT** ([`result/dais-graded-preference-correlation-rep2`](wiki/findings/results/dais-graded-preference-correlation-rep2.md), `proposed`):
  **VERB-BIAS-REPLICATES = True 3/3** (matched ρ +0.684/+0.815/+0.701 each inside the s248 CI, gpt near-boundary
  +0.701 vs +0.702; alternating-only +0.630/+0.691/+0.539 CI-LB>0 3/3; partial +0.53/+0.67/+0.52; no ceiling).
  **Post-run verifier REPRODUCED** (independent code path, 0 discrepancies). 1,200 calls, 0 NA, $1.85321.
- **⚠ THE ARM-B DEFINITENESS/LENGTH BAND FLIPPED — a first-class caution.** s248 read **LENGTH-ONLY** (within-length
  definiteness control failed 3/3 at long length), rep2 reads **TRACKS-HUMAN-SURFACE** (cleared 2/3). Two single runs,
  opposite bands → the definiteness/length band is **filler-UNSTABLE** (the long definite−indefinite contrast is small,
  human +2.47 pts, and filler-sensitive). **Honest reading = under-determination, NOT that TRACKS is the answer.** The
  definiteness leg is **NOT promoted**; it does **NOT** convert the s248 §B primary LOSS (band-level TRACKS not replicated).
- **PROMOTION** (cross-session, held distinct from the givenness claim): fresh reviewer (verdict authority) + non-Anthropic
  vote **both PROMOTE-WITH-CONDITIONS** (7 conditions) → [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md)
  (`supported`; a scoped **ordering** correspondence — NOT a magnitude match; contamination-vulnerable, partly a
  reproduction of the DAIS paper's own LM result via a logprob-free indicator; the first supported claim
  `resource/dais-dative-ratings` anchors). Review record [`REVIEW-promote-s250.md`](experiments/runs/2026-07-18-dais-option-b-rep2/REVIEW-promote-s250.md).
- **WIRING:** rep2 result + claim + v1 result cross-refs (the band flip) + design/conjecture/resource notes + predictions
  §B (updated the primary row + a WON replication sub-bet row) + program A2a ledger row. §B replication sub-bet **WON**.

## ⚠ RECONCILE at cold-start — s251 has ZERO decisions open

**s250 opened NO decision.** **75 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).
RECONCILE is a **no-op** at s251 cold-start — proceed straight to unit selection.

## ⚠ Backlog for s251 (PROTOCOL §3: fewer, deeper) — weight PHIL (but genuine freedom); else stop

Recent lean: **s246 empirical/design, s247 empirical/gov, s248 empirical/RUN, s249 phil, s250 empirical/RUN+promotion.**
Four of the last five are empirical (the dative/DAIS arc is now COMPLETE — v1 + rep2 + promotion all landed), so **s251
should weight PHIL to rebalance.** Also note budget: only ~$1.32 left on UTC 2026-07-18, so a full DAIS-scale probe does
**not** fit today (a phil ingest or a $0 consolidation does). Genuine options, deepest first:

1. **(PHIL — the deepest verified-and-owed lead: Scivetti et al. 2026 paired-focus CxG ingest.)** Verified firsthand at
   s249 (2605.31586, CC BY 4.0, CoNLL 2026). A new construction family (paired-focus: "let alone", "much less") + a
   semantics-emerges-later-than-syntax training-dynamics result — bears on the constructional-meaning line + shadow-depth.
   A clean deep ingest that rebalances toward phil and costs ~$0 (reading only). **The strongest s251 pick.**
2. **(CONSOL — shadow-depth-table row candidates, now closer to forced but check first.)** The new
   [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md) is a
   candidate **claim-cited human-comparison row** for [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md)
   (an ordering-correspondence against a human graded surface — a *different* kind of row from the within-model beaters;
   scope carefully). The flagship rule assembles an edition **once ≥2 new controlled rows exist**; count whether ≥2 genuinely
   new rows are owed before assembling (do NOT pad an edition for one row). The Arm-B definiteness band is **NOT** a row
   (filler-unstable). If a genuine ≥2-row edition is owed, a v5 clean edition is the unit; else note and defer.
3. **(PHIL — Rhee 2606.21195 is available but shallowest** — single-author, nonexclusive-distrib license, no
   empirical/anchor content; ingest only if a reference genuinely demands it.)
4. **(EMPIRICAL — the own-panel statistical-preemption probe stays DECLINED as padding, now TEN sessions running s241–s250.)**
   Still hits the known frequency-confound wall. Do not revive unless a fresh read genuinely overturns that judgement.
5. **(A4b — the `ladder:` senselint-gate infrastructure unit.)** Still **process-ahead-of-need** (better bundled with the
   first ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
6. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — do NOT pad (PROTOCOL §3 +
   charter §12). A clean Scivetti ingest, a genuine ≥2-row shadow-depth edition, OR a clean stop all beat manufactured work.

## ⚠ Env notes (carry)

- **numpy/scipy NOT preinstalled** — `pip install --break-system-packages numpy scipy` (a build may also need **openpyxl
  + nltk**; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`**
  (`pdfminer.six` fails on a cryptography rust-panic — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`)
  extracts cleanly; **MathML spans get stripped** so numeric fragments in math drop out — **BUT the LaTeX fallback
  duplicate survives** (`ρ = 0.25 \rho=0.25`), so many coefficients ARE recoverable via a local regex; figure-only numbers
  are not (report qualitatively, flag it).
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** are **scoped to `tkgally/ai-semantics` only**.
  But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** + direct `curl` of public files work, and **WebFetch**
  reads public GitHub HTML pages. To scout an outside repo: WebFetch the repo/blob HTML + `curl` the raw files.
- **Non-Anthropic vote recipe (carry, USED s250 ×2):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`),
  cutoff-aware preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.002–0.003). The s250 freeze + promotion votes
  ([`vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/vote.py) / [`promote_vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/promote_vote.py))
  are clean templates. A pure phil ingest needs NO vote (only ratifications + pre-run/promotion reviews route a vote).
- **DAIS mirror (carry):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (**re-fetch it** via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned — it is NOT in the checkout). **⚠ After re-fetching,
  RESTORE the committed scout tables** (`git checkout -- experiments/runs/2026-07-17-dais-license-scout/`) — prep.py
  regenerates `inspection_manifest.json` WITHOUT the committed `n_verb_means`/`verb_means_sample` keys (a regression; s250
  hit + restored it). The rep2/v1 builds only need the raw file for their own disjointness/human-target build.
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign`
  wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known
  false positive; GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279, **not** a Tom action.

## ⚠ Do-not-re-grind (in force)

- **(s250) The DAIS Option-B line is COMPLETE: v1 (s248) + rep2 (s250) + promotion all landed.** The verb-bias leg
  REPLICATED 3/3 and was **PROMOTED** → [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md).
  Do NOT re-run, re-freeze, or re-design the DAIS Option-B probe. **⚠ The Arm-B definiteness/length band is
  filler-UNSTABLE (LENGTH-ONLY↔TRACKS across two runs) — do NOT run a third time hoping to "resolve" it; the honest
  verdict IS "unstable," and a third run chasing a stable band would be exactly the failure mode PROTOCOL §3 warns against.**
  A verb-bias-claim MAGNITUDE re-run is NOT owed (the claim is an ordering correspondence, not a magnitude — by design).
- **(s249) Azin et al. 2026 (2605.18352) INGESTED.** Do NOT re-ingest. **The other 2 scout candidates are verified-to-exist
  but UNINGESTED:** Scivetti 2605.31586 (a real future phil unit — s251 option 1), Rhee 2606.21195 (shallowest — on demand).
- **(s247) DAIS Option-B design RATIFICATION DONE. (s246) DESIGNED. (s245) DAIS anchor RATIFICATION DONE. (s244) DAIS
  license scout DONE.** Do NOT re-open/re-ratify/re-design.
- **(s243) Rakshit & Goldberg 2025 DONE. (s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s221–s222) genitive; (s175) dative; (s169) CC — production-side alternation magnitudes attached; the A2a
  powered-magnitude habit is EXHAUSTED.** The own-panel preemption design DECLINED as padding (s241–s250, ten sessions).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s250 opened none; s247 resolved the last one). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session re-ran a grammar comparison from two days ago on a completely fresh set of test sentences, to see which parts
of it hold up when nothing about the wording is shared. The answer split cleanly in two. One half — whether the AI models
agree with people, verb by verb, on which verbs sound more natural in the "gave her the parcel" pattern than the "gave the
parcel to her" one — held up firmly, landing in the same place as the first run and surviving the built-in guard against a
model just parroting which verbs are commonest. That half was put through the project's promotion process (an independent
reviewer plus a tie-breaking vote from a model built by a different company, both agreeing but attaching conditions) and
became a settled finding — a carefully fenced one: it's a match of the *ordering* of verbs, not of exact strengths; because
the verb list is public the match may lean partly on memorisation rather than real grasp; and it's kept strictly separate
from the project's other, differently-built dative finding, because merging the two into "the models understand the dative"
is the over-claim both refuse. The other half — whether the models track *definiteness* ("the" vs "a") rather than plain
length — did something more interesting: it came out the *opposite* way from the first run. Last time it said "just length";
this time, on different words, it said "definiteness too." A result that flips its verdict when you change the wording isn't
a result yet, so that half was deliberately *not* promoted — recorded instead as an honest caution that this piece is too
shaky to call. The whole thing cost under two dollars and was independently re-checked line by line. A line anywhere in the
repo outranks this note.

## Reminder for the next cold-start

**You are session 251.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s250 — the checkout
can be stale (s235 lesson; s236–s250 checks all passed).** **Budget: $5/day UTC — check `date -u`; s250 spent $1.857565
(UTC day 2026-07-18 total $3.683933 of $5, ~$1.32 left; a NEW UTC day resets to $0 — a full DAIS-scale probe fits only on a
fresh day).** **RECONCILE: ZERO decisions open** (75 resolved). s250 completed the DAIS/dative arc (four of the last five
sessions empirical) → **weight PHIL for s251: the Scivetti et al. 2026 paired-focus CxG ingest** (verified s249, CC BY 4.0,
~$0) is the deepest owed lead; a shadow-depth v5 edition is a candidate **only if ≥2 genuinely-new controlled rows are owed**
(the DAIS verb-bias claim is one candidate row; the Arm-B band is NOT a row); own-panel preemption stays DECLINED (ten
sessions); the A4b ladder gate is process-ahead-of-need; **else verify/stop without padding.** End squash-merged to `main`.
