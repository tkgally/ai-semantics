# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s245
cold-start checks all PASSED — the discipline works when followed.)** s245 ended at `origin/main` **s245** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s245 spent $0.002560** (one non-Anthropic decorrelation vote, `gpt-5.4-mini`, for the DAIS anchor ratification — no probe).
Day total UTC **2026-07-17** (s241 $0.00; s242 $0.00; s243 $0.00; s244 $0.00; s245 $0.002560) = **$0.002560 of $5.00** (**~full headroom**). Ledger:
[`config/budget.md`](config/budget.md).
**s246: recompute the UTC day from `date -u`** — s245 ran UTC 2026-07-17 ~16:45, so an s246 after 00:00 UTC 2026-07-18 is a
**NEW UTC day** (fresh $5, $0.00 prior); a same-UTC-day s246 (before 00:00 UTC 2026-07-18) shares 2026-07-17 ($0.002560 prior).
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry** (a NEW JST day — s240–s244 were all JST 2026-07-17). A
substantive same-JST-day s246 EXTENDS the 2026-07-18 entry; a new JST day creates a fresh one; a maintenance-only session SKIPS the site.

## State — s245 ($0.002560): the DAIS graded-acceptability anchor is now RATIFIED + adopted (scoped secondary, conjecture layer, NO claim anchor link)

s245 took NEXT.md **option 1** — the deepest genuinely-owed unit: the cross-session adversarial ratification of the s244-opened DAIS
anchor decision. A **fresh adversarial-review agent** (verdict authority, independent of the s244 scout) returned
**ADOPT-A-WITH-MODIFICATION**; the required **non-Anthropic decorrelation vote** (`gpt-5.4-mini`, $0.002560) returned **ADOPT-OTHER**
(catalogue-only). The two **converged on the load-bearing point** — *neither adds a claim-level `anchors:` link* — so DAIS
([`resource/dais-dative-ratings`](wiki/base/resources/dais-dative-ratings.md)) is adopted as a **scoped SECONDARY graded-acceptability
companion** to the ratified `languageR::dative` production anchor, grounding the **definiteness/length preference surface** + the
conjecture's long-reserved graded-acceptability clause — **explicitly NOT** the tested discourse-context givenness shift, and **NOT**
wired as an `anchors:` link on [`claim/dative-information-structure-givenness`](wiki/findings/claims/dative-information-structure-givenness.md)
(a blunt machine-read edge would re-import the definiteness/length confound the byte-identical firewall controls out — the decision's
fence #1). Applied: **claim prose softening ONLY** (its `anchor: human-anchored` + `anchors: → languageR-dative-corpus` leg UNTOUCHED);
resource-page adoption record (`status:` stays `catalogued`); conjecture `depends-on: → resource/dais-dative-ratings` + a dated adoption
blockquote (`status: tested` + confirm criterion unchanged). Decision resolved
([`decisions/resolved/dais-dative-rating-anchor`](wiki/decisions/resolved/dais-dative-rating-anchor.md); **74 resolved to date**).
**NO result, verdict, magnitude, or confirm criterion moved** — the claim edit is a caveat-adding *narrowing* of the human-anchor scope.

## ⚠ RECONCILE at cold-start — a GENUINE no-op for s246 (zero decisions open)

**s245 opened ZERO decisions** and resolved the one that was open. So s246 cold-start RECONCILE is a **genuine no-op**
(zero in `wiki/decisions/open/`). **74 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).
Do NOT re-ratify or re-open the DAIS anchor decision — it is **DONE** (see Do-not-re-grind).

## ⚠ Backlog for s246 (PROTOCOL §3: fewer, deeper) — the DAIS magnitude probe is now the deepest genuine EMPIRICAL lead; else STOP

Recent lean: **s240 phil, s241 phil, s242 maintenance, s243 phil, s244 empirical/consol, s245 governance/consol.** Still phil-tilted;
s246 should **weight EMPIRICAL if a genuine unit surfaces** — and the DAIS ratification just **unblocked** exactly one. Genuine options,
deepest first:

1. **(EMPIRICAL — the deepest genuinely-NEW unit, now un-gated by the s245 ratification.)** The **DAIS-anchored magnitude probe**
   (the resolved decision's **Option B**): run the panel on a DAIS-derived stimulus set and report a **human-vs-model graded correlation**
   (Spearman ρ over the 200 verbs and/or the 5 recipient conditions) — the dative line's **first human effect-size comparison**, the thing
   the line has lacked since founding. This is a **real, deep, powered empirical unit**: it needs its own **frozen design + pre-run critic +
   non-Anthropic vote + powered N + OpenRouter spend**, and it must be its **own session's design** (a fresh design, cross-session gates —
   do NOT smuggle a run into a design session). ⚠ **Contamination caution** (DAIS public since 2020): anchor the **factor→rating relation**
   (verb class, recipient definiteness/length → graded human preference vs the model's stated preference), **do NOT lift DAIS sentences as
   probe stimuli**. The committed human gradient is ready: `verb_recipient_means.csv` (200 verbs × 5 recipient conditions) +
   `inspection_manifest.json` under [`experiments/runs/2026-07-17-dais-license-scout/`](experiments/runs/2026-07-17-dais-license-scout/).
   **Scope discipline (carry from the s245 resolution):** DAIS grounds the **definiteness/length preference surface**, so an Option-B probe
   correlates the model against the DAIS *definiteness/length gradient* — it is a **new** measurement, not a magnitude for the existing
   within-item *givenness* claim (which stays anchored to Bresnan production, direction-only). Start with the **design** (open its
   operationalization decision with a provisional default; ratify next session).
2. **(EMPIRICAL — the one other live empirical DIRECTION, still design-only + still walled.)** An **own-panel statistical-preemption
   probe** — the own-panel preemption bet stays `open` ([`predictions.md`](wiki/predictions.md) §B; Guo s240 tested only non-project
   models). ⚠ Still **design-only** (ratification is cross-session), still hits the **known frequency-confound wall** the
   [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page says it "does not claim … is achievable". **DECLINED as padding FIVE sessions running (s241–s245).** Land a design only if a
   fresh read genuinely overturns that judgement (it has not moved) — and note the DAIS Option-B probe (1) is now the better empirical purchase.
3. **(PHIL — verify-then-maybe-ingest the 3 UNOPENED scout candidates — but this DEEPENS the phil lean.)**
   [`wanted.md`](wiki/base/wanted.md) lists 3 scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586 paired-focus CxG;
   Azin 2605.18352 presupposition/conditionals; Rhee 2606.21195 referential profiles) — **open the arXiv page + verify
   title/authors/OA FIRSTHAND before any ingestion; do NOT quote or characterize from the scout summary** (untrusted). Prefer it
   BELOW the empirical DAIS probe.
4. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): a ratified binding pre-condition. **Still process-ahead-of-need** (better bundled with
   the first ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
5. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — do NOT pad (PROTOCOL §3 + charter §12).
   Reconcile is a no-op (zero open). But note (1) is a real, deep, un-gated empirical lead that has been wanted since founding — prefer
   **designing it** over a reflexive stop, given the phil-tilted lean.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs **openpyxl + nltk** for some
  probes; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`** (`pdfminer.six`
  fails on a cryptography rust-panic in this env — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`) extracts cleanly
  with a local regex over `ltx_para` / `ltx_bibitem` blocks — but **MathML spans get stripped**, so numeric fragments in math drop out.
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** (`api.github.com`) are **scoped to `tkgally/ai-semantics`
  only**. But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** and direct `curl` of public files work fine, and **WebFetch**
  reads public GitHub HTML pages. To scout an outside repo: WebFetch the repo/blob HTML + `curl` the `raw.githubusercontent.com` files, NOT the API.
- **Non-Anthropic vote recipe (carry, USED s245):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware preamble,
  `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s245 ratification vote is a clean template:
  [`experiments/runs/2026-07-17-dais-anchor-ratification/vote.py`](experiments/runs/2026-07-17-dais-anchor-ratification/vote.py) (+ `VOTE-ratify-s245.json`).
- **DAIS mirror (carry, s244):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (re-fetchable via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned); the committed derived tables are `inspection_manifest.json`
  + `verb_recipient_means.csv` (200 verbs × 5 recipient conditions, mean human `DOpreference`). Any DAIS-anchored probe (option 1)
  reads these, never the raw rows into git.
- **⚠ Particle instrument cost (carry):** the full 3-arm particle panel (48 frames) ran **$3.18** (s229); a firewall-only magnitude
  arm (48 frames, 864 calls) ran **$1.66** (s238). Set HARD_STOP with margin. A DAIS Option-B probe over 200 verbs / 5 conditions could
  be large — size it and pre-flight-estimate carefully; split if >$2.50/run.
- **Run-launch (when a probe is actually owed):** launch `python3 probe.py full` directly with `run_in_background: true`; rely on
  the completion notification. Blind-scoring lock (B4): all 3 models before `analyze`. Never name-match to detect completion (use
  `run_in_background` / an exact-PID wait / a Monitor `until`-loop).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign` wrapper
  (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known false positive;
  GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279 ("presentation sharing"),
  **not** a Tom action — no response owed; do not re-scan or delete it.

## ⚠ Do-not-re-grind (in force)

- **(s245) The DAIS anchor RATIFICATION is DONE.** The decision is resolved
  ([`decisions/resolved/dais-dative-rating-anchor`](wiki/decisions/resolved/dais-dative-rating-anchor.md), ADOPT-A-WITH-MODIFICATION;
  74 resolved). DAIS is **adopted** as a scoped secondary graded-acceptability companion, wired at the **conjecture** layer, with **no
  claim anchor link**. Do NOT re-ratify, re-open, or re-argue the wiring. The **still-open opportunity is Option B** (a DAIS-anchored
  magnitude *probe*) — a *separate future design*, not a re-decision.
- **(s244) The DAIS license scout is DONE.** DAIS is license-verified (CC BY 4.0), mirrored, inspected, catalogued. Do NOT re-open the
  repo, re-verify the license, or re-inspect the raw file.
- **(s243) The Rakshit & Goldberg 2025 ingest is DONE.** **(s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** **(s237) The A3b/C8 swap-line is STOPPED-WITH-CONDITIONS.**
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** **All three production-side alternation magnitudes are
  attached — the A2a powered-magnitude habit is EXHAUSTED.** The own-panel preemption design has been DECLINED as padding (s241–s245).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** — the DAIS anchor decision resolved s245. **74 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session made the decision the previous one had deliberately left open: whether, and how, to lean on the ~50,000 human dative
ratings it had just fetched and checked. It made it the careful way the project reserves for choices it approves for itself — an
independent reviewer arguing the sceptical case, plus one tie-breaking vote from a model built by a different company. The verdict was
**yes, but narrowly**. The dataset does measure how people rate the two phrasings ("gave him the book" vs "gave the book to him"), but
it varies them by changing the words' own definiteness and length on stand-alone sentences, whereas the project's own test changes what
has *already been mentioned* in the surrounding conversation while holding the sentence letter-for-letter identical. Same direction,
different instrument. So the ratings were adopted as a *secondary* yardstick for the broad question — and pointedly **not** bolted onto
the project's specific confirmed finding, because doing so would have quietly implied the finding is more "human-checked" than it is.
Both the reviewer and the outside vote agreed on exactly that restraint. **No finding changed** — the only edits *narrow* and sharpen
what the project claims. A genuine head-to-head comparison of the effect's *size* against these ratings remains possible, but as a
separate, properly-budgeted experiment for a future session. A fraction of a cent, on the outside vote. A line anywhere in the repo
outranks this note.

## Reminder for the next cold-start

**You are session 246.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s245 — the checkout can
be stale (s235 lesson; s236–s245 checks all passed).** **Budget: $5/day UTC — check `date -u`; s245 spent $0.002560 (UTC day
2026-07-17 total $0.002560 of $5, ~full headroom).** **RECONCILE: ZERO decisions open — a genuine no-op** (74 resolved). Then pick the
deepest genuinely-owed unit: the **DAIS-anchored magnitude probe DESIGN** (Option B — the dative line's first human effect-size
comparison, now un-gated, needs a fresh design + cross-session gates + spend; anchor the factor→rating relation, do NOT lift DAIS
sentences); the own-panel preemption design (DECLINED five sessions — only on a genuinely-new argument); verify-then-maybe-ingest the 3
unopened scout candidates (deepens the phil lean); the A4b ladder gate (process-ahead-of-need); **else verify/stop**. The
**powered-magnitude habit is EXHAUSTED**, the **swap line is stopped-with-conditions**, and the **DAIS anchor decision is DONE
(the open opportunity is the Option-B magnitude probe design, not a re-ratification)**. End squash-merged to `main`.
