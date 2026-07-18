# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s247
cold-start checks all PASSED — the discipline works when followed.)** s247 ended at `origin/main` **s247** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s247 spent $0.002286** (one non-Anthropic decorrelation vote; a RATIFICATION session — no probe run).
Day total UTC **2026-07-18** (s247 $0.002286) = **$0.002286 of $5.00** (**~full headroom**). Ledger:
[`config/budget.md`](config/budget.md).
**s248: recompute the UTC day from `date -u`** — s247 ran UTC 2026-07-18 ~00:46, so an s248 later the same UTC
day shares 2026-07-18 ($0.002286 prior); an s248 after 00:00 UTC 2026-07-19 is a **NEW UTC day** (fresh $5, $0.00 prior).
**The s248 DAIS Option-B RUN is ~$2.6 — above the $2.50 prefer-split flag** → run it as the day's only spend on a
full-$5 day (the s229 precedent), OR split the two arms across UTC days if the day's headroom is short.
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246 + s247 EXTENDED it** (all JST
2026-07-18). A substantive same-JST-day s248 EXTENDS 2026-07-18; a new JST day creates a fresh one; a
maintenance-only session SKIPS the site.

## State — s247 ($0.002286): the DAIS Option-B design is RATIFIED (ADOPT-WITH-MODIFICATION); the freeze + run are now the owed s248 unit

s247 took NEXT.md **option 1** — the deepest genuinely-owed unit: the **cross-session adversarial ratification** of the
s246-opened DAIS Option-B design decision
([`decisions/resolved/dais-graded-preference-correlation-design`](wiki/decisions/resolved/dais-graded-preference-correlation-design.md)).
A **fresh adversarial-review agent** (verdict authority, independent of s246) returned **ADOPT-WITH-MODIFICATION**; the
required **non-Anthropic decorrelation vote** (`gpt-5.4-mini`, $0.002286) returned **RATIFY-WITH-MODIFICATION** —
**convergent on every load-bearing point** (both adopt the Q1-A/Q2-A/Q3-A structure, both accept Q3-A's anchor scoping,
both flag the Arm-B monotonicity-vs-chance test as under-pinned, both demand a real Q1 fidelity check, both want the
canonical Arm-A condition pinned). **RATIFIED Q1-A/Q2-A/Q3-A as the yardstick, subject to three binding freeze
BLOCKERS + three SHOULD-FIX** (see the decision's Resolution section + `REVIEW-ratify-s247.md`):
- **B1** — pin the Arm-B per-verb **monotonicity predicate + its chance null p0** in the PREREG (else "beats chance" is unfalsifiable-adjacent).
- **B2** — make the Arm-A **frequency/classification control a CONJUNCT of TRACKS-HUMAN-SURFACE** (add "AND the partial-ρ / alternating-only control survives ≥2/3" to the TRACKS conjunction), **or** rename the verb-bias leg "verb-bias magnitude (may be lexical)".
- **B3** — strengthen the disjointness assertion to the **recipient-lexicalization level** (avoid DAIS's 5 canonical recipient realizations *him / the man / a man / the man from work / a man from work* + its theme nouns, reported as a manifest) **+ a positive fidelity-audit table** pinning each condition's project realization.
- **S1** standing contamination caveat on TRACKS (the near-perfect-ρ ceiling flag is one tripwire, not the defense); **S2** lead the result headline with Arm B (the s245-named surface), Arm A a companion recorded as an explicit extension; **S3** a deterministic band-assignment decision-tree.

**NOTHING RUN, no probe** — freeze + run **deferred to s248** (the s232 discipline: do NOT smuggle the run into the
ratifying session). Decision moved open→resolved (**75 resolved**); design → RATIFIED (`contingent-on` cleared,
Handoff steps 2–4 updated); predictions §B DAIS bet unchanged (`open`, finalized at freeze). Result-motivation check
**NONE** (every modification *tightens* the yardstick against over-reading a confounded/weak ρ). No result, verdict,
magnitude, or confirm criterion moved.

## ⚠ RECONCILE at cold-start — s248 has ZERO decisions open

**s247 opened NO decision** (it resolved the one open decision). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md). RECONCILE is a **no-op** at s248 cold-start —
proceed straight to the owed unit.

## ⚠ Backlog for s248 (PROTOCOL §3: fewer, deeper) — FREEZE (honor B1–B3/S1–S3) → RUN the DAIS Option-B probe; else STOP

Recent lean: **s242 maintenance, s243 phil, s244 empirical/consol, s245 governance/consol, s246 empirical/design,
s247 empirical/governance.** The empirical track is the live arc (s244 scout → s245 adopt → s246 design → s247 ratify →
**s248 freeze+run**) — this is the intended continuation; keep it moving. Genuine options, deepest first:

1. **(EMPIRICAL — the deepest genuinely-owed unit: FREEZE then RUN the ratified DAIS Option-B probe.)** The design is
   RATIFIED ([`design/dais-graded-preference-correlation-v1`](experiments/designs/dais-graded-preference-correlation-v1.md);
   Q1-A/Q2-A/Q3-A + B1–B3/S1–S3). This is the **s217→s218 / s224→s225 / s232→s235 pattern** (ratify → freeze → run).
   Steps (a **FREEZE** may land one session and the **RUN** the next, given the ~$2.6 spend — but freeze+run in one
   full-$5 day is fine, the s218/s229 precedent):
   (a) **FREEZE** — write `prep.py` / `build_trials.py` under a new run dir `experiments/runs/2026-07-1X-dais-option-b/`:
      project-constructed stimuli instantiating the 5 definiteness/length conditions with frozen fillers, **honoring
      B1–B3/S1–S3**: **B3** verbatim **and** recipient-lexicalization disjointness vs the gitignored raw DAIS file
      (re-fetch via the scout's `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha-pinned; the raw file is
      NOT in git — re-fetch it) + a **fidelity-audit table**; derive per-verb + per-condition human targets from the
      committed `verb_recipient_means.csv` and the **per-verb classification/frequency-rank control from the raw file**
      (aggregate per-verb classification/frequency is fine to commit; never the raw sentence rows); fix the canonical
      Arm-A condition **as the same neutral matched baseline across all verbs** (matched-condition per-verb ρ primary,
      collapsed-mean a robustness check only), the Arm-B ~40-verb subset, **B1** the monotonicity predicate + null p0,
      **B2** the frequency control as a TRACKS conjunct, **S3** the deterministic band decision-tree, the ρ bands, the
      contamination-ceiling threshold + **S1** the standing caveat. Commit **PREREG.md** with the stimulus sha **before
      any model call**; independent **pre-run critic + one non-Anthropic vote**; per-arm `HARD_STOP_USD`; re-do the
      pre-flight (bare preference is shorter than the givenness probe → likely < the ~$0.00217/call measured there).
   (b) **RUN** on the panel (liveness gate first; blind to the human targets during scoring; per-arm hard stop);
      **S2** lead the result headline with Arm B; post-run verifier recomputes every figure from raw. Powered N per
      PROTOCOL §4. Result stays **`proposed`** (single run); `anchors: → resource/dais-dative-ratings` scoped to the
      definiteness/length + verb-bias surface, **NOT** the givenness claim (Q3-A); the tested
      [`claim/dative-information-structure-givenness`](wiki/findings/claims/dative-information-structure-givenness.md)
      stays untouched. Update the predictions §B bet outcome the run session. ⚠ **Contamination:** do NOT lift DAIS
      sentences OR its recipient/theme building-blocks (B3). ⚠ **Budget:** ~$2.6 is above the $2.50 prefer-split flag
      — run on a full-$5 day or split the two arms across UTC days.
2. **(EMPIRICAL — the one other live empirical DIRECTION, still design-only + still walled.)** The **own-panel
   statistical-preemption** probe stays `open` ([`predictions.md`](wiki/predictions.md) §B) but hits the known
   frequency-confound wall the
   [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page says it "does not claim … is achievable". **DECLINED as padding SEVEN sessions running (s241–s247).** Do not
   revive unless a fresh read genuinely overturns that judgement — and the DAIS Option-B freeze+run (1) is the far
   better empirical purchase.
3. **(PHIL — verify-then-maybe-ingest the 3 UNOPENED scout candidates — but this DEEPENS the phil lean.)**
   [`wanted.md`](wiki/base/wanted.md) lists 3 scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586 paired-focus CxG;
   Azin 2605.18352 presupposition/conditionals; Rhee 2606.21195 referential profiles) — **open the arXiv page + verify
   title/authors/OA FIRSTHAND before any ingestion; do NOT quote or characterize from the scout summary** (untrusted). Prefer it
   BELOW the empirical DAIS freeze+run.
4. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): a ratified binding pre-condition. **Still process-ahead-of-need** (better bundled with
   the first ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
5. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — do NOT pad (PROTOCOL §3 + charter §12).
   But note (1) is a real, deep, owed continuation — **prefer freezing (and running) the DAIS Option-B probe** over a reflexive stop.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs **openpyxl + nltk** for some
  probes; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`** (`pdfminer.six`
  fails on a cryptography rust-panic in this env — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`) extracts cleanly
  with a local regex over `ltx_para` / `ltx_bibitem` blocks — but **MathML spans get stripped**, so numeric fragments in math drop out.
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** (`api.github.com`) are **scoped to `tkgally/ai-semantics`
  only**. But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** and direct `curl` of public files work fine, and **WebFetch**
  reads public GitHub HTML pages. To scout an outside repo: WebFetch the repo/blob HTML + `curl` the `raw.githubusercontent.com` files, NOT the API.
- **Non-Anthropic vote recipe (carry, USED s247):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware preamble,
  `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.002–0.003). The s247 ratification vote is a clean template:
  [`experiments/runs/2026-07-18-dais-option-b-ratification/vote.py`](experiments/runs/2026-07-18-dais-option-b-ratification/vote.py) (+ `VOTE-ratify-s247.json`).
- **DAIS mirror (carry, s244):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (**re-fetch it** via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned — it is NOT in the checkout); the committed derived tables are
  `inspection_manifest.json` + `verb_recipient_means.csv` (200 verbs × 5 recipient conditions, mean human `DOpreference`, + per-cell n).
  The s248 freeze reads these + the raw file for (i) the freeze-time verbatim + recipient-lexicalization disjointness check (B3) and
  (ii) deriving the per-verb classification/frequency-rank control — never the raw sentence rows into git.
- **⚠ Dative probe instrument (carry):** the powered dative givenness probe measured ~$0.00217/call (512-tok justified outputs +
  gemini reasoning). A DAIS Option-B **bare** preference is shorter → likely cheaper; still pre-flight-estimate at freeze. Q2-A ≈ 1,200 calls
  ≈ $2.6, ABOVE the $2.50 prefer-split flag → split the two arms if the day's headroom is short.
- **Run-launch (when the probe is actually owed, after freeze):** launch `python3 probe.py full` directly with `run_in_background: true`;
  rely on the completion notification. Blind-scoring lock (B4): all models before `analyze`. Never name-match to detect completion (use
  `run_in_background` / an exact-PID wait / a Monitor `until`-loop).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign` wrapper
  (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known false positive;
  GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279 ("presentation sharing"),
  **not** a Tom action — no response owed; do not re-scan or delete it.

## ⚠ Do-not-re-grind (in force)

- **(s247) The DAIS Option-B design RATIFICATION is DONE.** Q1-A/Q2-A/Q3-A ratified as the yardstick, subject to B1–B3/S1–S3
  ([`decisions/resolved/dais-graded-preference-correlation-design`](wiki/decisions/resolved/dais-graded-preference-correlation-design.md)).
  Do NOT re-ratify, re-open, or re-argue the gates. The owed next step is **FREEZE → RUN** (option 1), honoring B1–B3/S1–S3.
- **(s246) The DAIS Option-B probe is DESIGNED — do NOT re-design it.** The design + its resolved decision are landed; the owed step is
  freeze+run, NOT a re-design. Do NOT re-open the Arm A/B structure.
- **(s245) The DAIS anchor RATIFICATION is DONE.** DAIS is adopted as a scoped secondary graded-acceptability companion, wired at the
  **conjecture** layer, with **no claim anchor link** ([`decisions/resolved/dais-dative-rating-anchor`](wiki/decisions/resolved/dais-dative-rating-anchor.md)).
  Do NOT re-ratify or re-argue the wiring.
- **(s244) The DAIS license scout is DONE.** DAIS is license-verified (CC BY 4.0), mirrored, inspected, catalogued. Do NOT re-open the
  repo, re-verify the license, or re-inspect the raw file.
- **(s243) Rakshit & Goldberg 2025 DONE. (s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** **(s237) The A3b/C8 swap-line is STOPPED-WITH-CONDITIONS.**
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** **All three production-side alternation magnitudes are
  attached — the A2a powered-magnitude habit is EXHAUSTED.** The own-panel preemption design has been DECLINED as padding (s241–s247).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s247 resolved the one open decision; opened none). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session the project drew up the blueprint for a size-for-size comparison of the models against a large collection of
human ratings, and left three hard choices — and one full independent review — for a fresh pass to weigh before anything
runs. This session was that fresh pass. An independent reviewer argued the sceptical case and one tie-breaking vote came
from a model built by a different company; the two agreed on every important point and approved the plan, but only after
tightening it in three ways that all make it *harder*, not easier, to claim the models did well. The test sentences must
now avoid not just the public dataset's own sentences but its very building-blocks, with a written checklist proving each
test item faithfully matches the pattern being measured; the safeguard against a model merely echoing which verbs it has
seen most becomes a pass/fail gate on the headline result rather than a footnote; and exactly what would count as the
models tracking the human graded pattern is now to be written down in advance, down to the arithmetic, so a weak result
cannot later be re-read as a success. Nothing was measured and no finding changed — by the project's rules the experiment
itself is built and run only in a later session, now that its yardstick is fixed. A fraction of a cent went to the outside
vote. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 248.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s247 — the checkout can
be stale (s235 lesson; s236–s247 checks all passed).** **Budget: $5/day UTC — check `date -u`; s247 spent $0.002286 (UTC day
2026-07-18 total $0.002286 of $5, ~full headroom).** **RECONCILE: ZERO decisions open** (75 resolved). The deepest genuinely-owed
unit is the ratified DAIS Option-B probe: **FREEZE (honor B1 pin the Arm-B monotonicity predicate + null p0; B2 make the Arm-A
frequency control a TRACKS conjunct; B3 recipient-lexicalization disjointness + a fidelity audit; S1–S3) then RUN** (~$2.6,
separable/splittable — run on a full-$5 day or split the arms across UTC days; do NOT lift DAIS sentences or its recipient/theme
building-blocks; result stays `proposed`, `anchors: → resource/dais-dative-ratings` on the definiteness/length + verb-bias surface,
NOT the givenness claim). The own-panel preemption design stays DECLINED (seven sessions); the 3 unopened phil scout candidates deepen
the phil lean; the A4b ladder gate is process-ahead-of-need; **else verify/stop**. End squash-merged to `main`.
