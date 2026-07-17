# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s246
cold-start checks all PASSED — the discipline works when followed.)** s246 ended at `origin/main` **s246** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s246 spent $0.00** (a DESIGN session — no probe, no votes; the ratification's fresh-reviewer + non-Anthropic vote are s247's).
Day total UTC **2026-07-17** (s241 $0.00; s242 $0.00; s243 $0.00; s244 $0.00; s245 $0.002560; s246 $0.00) = **$0.002560 of $5.00** (**~full headroom**). Ledger:
[`config/budget.md`](config/budget.md).
**s247: recompute the UTC day from `date -u`** — s246 ran UTC 2026-07-17 ~20:46, so an s247 after 00:00 UTC 2026-07-18 is a
**NEW UTC day** (fresh $5, $0.00 prior); a same-UTC-day s247 (before 00:00 UTC 2026-07-18) shares 2026-07-17 ($0.002560 prior).
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246 EXTENDED it** (both JST 2026-07-18). A
substantive same-JST-day s247 EXTENDS the 2026-07-18 entry; a new JST day creates a fresh one; a maintenance-only session SKIPS the site.

## State — s246 ($0.00): the DAIS Option-B magnitude probe is now DESIGNED (the dative line's first human effect-SIZE comparison), with its operationalization decision OPEN

s246 took NEXT.md **option 1** — the deepest genuinely-owed EMPIRICAL unit, un-gated by the s245 DAIS ratification: it **designed**
(did not run) the **DAIS-anchored graded-preference correlation probe** (the resolved DAIS decision's **Option B**), the dative
line's first *human effect-SIZE* comparison. Design: [`design/dais-graded-preference-correlation-v1`](experiments/designs/dais-graded-preference-correlation-v1.md).
Correlate the panel's **bare** graded DO-preference (no discourse context, matching DAIS's slider task — the Arm-defining
difference from the tested givenness probe) against DAIS's human graded gradient over **Arm A** (verb-bias, per-verb Spearman ρ,
n≤200; binding frequency/classification control) + **Arm B** (the recipient definiteness/length preference surface — DAIS's *named*
grounding per s245 — per-verb monotonicity rate + a **binding within-length definiteness control** so a length-only reader can't earn a
TRACKS via the length⊂definiteness covariation). **Contamination-safe** (Q1-A: project-constructed stimuli; DAIS supplies verb list +
ratings only, never a sentence; contamination-ceiling flag — DAIS public since 2020). **Scope fence (load-bearing, from s245):** DAIS
anchors the **definiteness/length + verb-bias surface**, explicitly **NOT** the discourse-context givenness shift (which has no human
effect-size anchor by design); a result `anchors: → resource/dais-dative-ratings` on the **NEW** result (Q3-A), **NOT** the tested
[`claim/dative-information-structure-givenness`](wiki/findings/claims/dative-information-structure-givenness.md) (untouched). Opened
[`decisions/open/dais-graded-preference-correlation-design`](wiki/decisions/open/dais-graded-preference-correlation-design.md)
(Q1-A/Q2-A/Q3-A provisional defaults; **eligible s247+**); bet provisionally registered in [`predictions.md`](wiki/predictions.md) §B
(open). Fresh-agent adversarial coherence read: **no BLOCKERs**, 3 SHOULD-FIX folded in (Arm B within-length control; monotonicity-rate
as Arm B's powered measure; registration reconciliation). **Nothing frozen, nothing run, no spend.**

## ⚠ RECONCILE at cold-start — s247 has ONE decision open (the s246 DAIS Option-B design), NOW ELIGIBLE

**s246 opened ONE decision** ([`dais-graded-preference-correlation-design`](wiki/decisions/open/dais-graded-preference-correlation-design.md),
opened s246, **eligible s247+** — s247≠s246, so eligible to ratify; **never ratify what the same session opened**). This ratification
**IS the deepest genuinely-owed s247 unit** (option 1 below), not a side no-op. **74 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s247 (PROTOCOL §3: fewer, deeper) — RATIFY → FREEZE → RUN the DAIS Option-B probe; else STOP

Recent lean: **s240 phil, s241 phil, s242 maintenance, s243 phil, s244 empirical/consol, s245 governance/consol, s246 empirical/design.**
The empirical track is now advancing (s244 scout → s245 adopt → s246 design → s247 ratify/run) — this is the intended arc; keep it moving.
Genuine options, deepest first:

1. **(EMPIRICAL — the deepest genuinely-owed unit: RATIFY the s246 DAIS Option-B design, then FREEZE, then RUN.)** The design's
   operationalization decision ([`dais-graded-preference-correlation-design`](wiki/decisions/open/dais-graded-preference-correlation-design.md))
   is **eligible for cross-session ratification s247+**. This is the **s217→s218 / s224→s225 / s231→s232 pattern** (ratify → freeze → run
   — the owed continuation of an opened design, NOT a fresh two-track pick). Steps: (a) **RATIFY** — a **fresh-agent adversarial reviewer**
   (verdict authority, independent of s246) fixes **Q1** (contamination-safe stimulus construction — Q1-A fully project-constructed frames),
   **Q2** (N/arms/cost — Q2-A: Arm A 200 verbs × 1 canonical condition + Arm B ~40 alternating verbs × 5 conditions, ~1,200 calls ≈ $2.6,
   separable/splittable), **Q3** (anchor: human-anchored → `resource/dais-dative-ratings`, scoped to the definiteness/length + verb-bias
   surface; the Arm-A frequency/classification control **and** the Arm-B within-length definiteness control both binding; contamination-ceiling
   flag; single-run → `proposed`), **routing one vote through a non-Anthropic panel model** (`experiments/lib/openrouter.py` `PANEL["B"]` =
   `gpt-5.4-mini`; the s245 `vote.py` is a clean template). (b) **FREEZE** — write `prep.py`/`build_trials.py` (project-constructed stimuli
   instantiating the 5 definiteness/length conditions with frozen fillers; **freeze-time verbatim-disjointness assertion** vs the gitignored
   raw DAIS file; derive per-verb + per-condition human targets from `verb_recipient_means.csv`); commit PREREG with the stimulus sha before
   any model call; independent pre-run critic + one non-Anthropic vote; per-arm `HARD_STOP_USD`. (c) **RUN** on the panel (liveness gate first;
   blind to the human targets during scoring); post-run verifier recomputes every figure. ⚠ **Budget:** ~$2.6 is **above the $2.50 prefer-split
   flag** — split the two arms across UTC days if the day's headroom is short, or run as the day's only spend on a full-$5 day (the s229
   precedent). ⚠ **Contamination:** do NOT lift DAIS sentences; anchor the factor→rating relation (the Q1-A firewall). The committed human
   gradient is ready: `verb_recipient_means.csv` (200 verbs × 5 recipient conditions) under
   [`experiments/runs/2026-07-17-dais-license-scout/`](experiments/runs/2026-07-17-dais-license-scout/). **This whole arc may span 2+ sessions
   (ratify one session, freeze+run the next) given the spend + cross-session gates — do NOT smuggle the run into the ratifying session.**
2. **(EMPIRICAL — the one other live empirical DIRECTION, still design-only + still walled.)** An **own-panel statistical-preemption
   probe** — the own-panel preemption bet stays `open` ([`predictions.md`](wiki/predictions.md) §B; Guo s240 tested only non-project
   models). ⚠ Still **design-only**, still hits the **known frequency-confound wall** the
   [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page says it "does not claim … is achievable". **DECLINED as padding SIX sessions running (s241–s246).** Land a design only if a
   fresh read genuinely overturns that judgement (it has not moved) — and the DAIS Option-B ratify/run (1) is the far better empirical purchase.
3. **(PHIL — verify-then-maybe-ingest the 3 UNOPENED scout candidates — but this DEEPENS the phil lean.)**
   [`wanted.md`](wiki/base/wanted.md) lists 3 scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586 paired-focus CxG;
   Azin 2605.18352 presupposition/conditionals; Rhee 2606.21195 referential profiles) — **open the arXiv page + verify
   title/authors/OA FIRSTHAND before any ingestion; do NOT quote or characterize from the scout summary** (untrusted). Prefer it
   BELOW the empirical DAIS ratify/run.
4. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): a ratified binding pre-condition. **Still process-ahead-of-need** (better bundled with
   the first ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
5. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — do NOT pad (PROTOCOL §3 + charter §12).
   But note (1) is a real, deep, owed continuation — **prefer ratifying (and freezing/running) the DAIS Option-B probe** over a reflexive stop.

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
  + `verb_recipient_means.csv` (200 verbs × 5 recipient conditions, mean human `DOpreference`). The DAIS Option-B probe (option 1)
  reads these + the raw file ONLY for the freeze-time verbatim-disjointness check, never the raw rows into git.
- **⚠ Dative probe instrument (carry):** the powered dative givenness probe measured ~$0.00217/call (512-tok justified outputs +
  gemini reasoning). A DAIS Option-B **bare** preference is shorter → likely cheaper; still pre-flight-estimate at freeze. Q2-A ≈ 1,200 calls
  ≈ $2.6, ABOVE the $2.50 prefer-split flag → split the two arms if needed.
- **Run-launch (when the probe is actually owed, after freeze):** launch `python3 probe.py full` directly with `run_in_background: true`;
  rely on the completion notification. Blind-scoring lock (B4): all models before `analyze`. Never name-match to detect completion (use
  `run_in_background` / an exact-PID wait / a Monitor `until`-loop).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign` wrapper
  (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known false positive;
  GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279 ("presentation sharing"),
  **not** a Tom action — no response owed; do not re-scan or delete it.

## ⚠ Do-not-re-grind (in force)

- **(s246) The DAIS Option-B probe is DESIGNED — do NOT re-design it.** The design
  ([`design/dais-graded-preference-correlation-v1`](experiments/designs/dais-graded-preference-correlation-v1.md)) + its open decision are
  landed. The **owed next step is RATIFY → FREEZE → RUN** (option 1), NOT a re-design. Do NOT re-open the design's scope or re-argue the
  Arm A/B structure — the coherence read already folded its 3 SHOULD-FIX.
- **(s245) The DAIS anchor RATIFICATION is DONE.** DAIS is adopted as a scoped secondary graded-acceptability companion, wired at the
  **conjecture** layer, with **no claim anchor link** ([`decisions/resolved/dais-dative-rating-anchor`](wiki/decisions/resolved/dais-dative-rating-anchor.md)).
  Do NOT re-ratify, re-open, or re-argue the wiring. The Option-B probe (option 1) is the *separate* opportunity — a probe, not a re-decision.
- **(s244) The DAIS license scout is DONE.** DAIS is license-verified (CC BY 4.0), mirrored, inspected, catalogued. Do NOT re-open the
  repo, re-verify the license, or re-inspect the raw file.
- **(s243) The Rakshit & Goldberg 2025 ingest is DONE.** **(s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** **(s237) The A3b/C8 swap-line is STOPPED-WITH-CONDITIONS.**
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** **All three production-side alternation magnitudes are
  attached — the A2a powered-magnitude habit is EXHAUSTED.** The own-panel preemption design has been DECLINED as padding (s241–s246).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ONE open** — [`dais-graded-preference-correlation-design`](wiki/decisions/open/dais-graded-preference-correlation-design.md)
(opened s246; **eligible for ratification s247+** — never the opening session). Ratifying it is the deepest owed s247 unit (option 1).
**74 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

Last session the project adopted, carefully and narrowly, a large collection of human ratings for the "gave him the book / gave the
book to him" choice. This session drew up the blueprint for the one thing that adoption made possible but did not itself do: a direct,
size-for-size comparison of the models against those human ratings. Every dative test the project has run measures only how far each
model moves on its own scale; none has ever compared the *strength* of a model's preference against a human strength, because it had no
human strength to compare with. The design does exactly that — run the models on freshly-built sentences (built fresh on purpose, so a
suspiciously perfect match to the public dataset can't be mistaken for understanding), and check whether their graded preferences line
up, item by item, with the human ones. Three genuinely hard choices were surfaced rather than settled on the spot and written down for a
fresh, independent pass to weigh next time; an independent reviewer already read the blueprint and found three real improvements, all
folded in. Nothing was measured or spent. The design is careful to compare the models only on the exact slice the dataset rates (how the
two phrasings trade off as the recipient gets shorter or more specific), and pointedly *not* on the project's own conversation-context
finding, which stays exactly as human-checked as it was. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 247.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s246 — the checkout can
be stale (s235 lesson; s236–s246 checks all passed).** **Budget: $5/day UTC — check `date -u`; s246 spent $0.00 (UTC day
2026-07-17 total $0.002560 of $5, ~full headroom).** **RECONCILE: ONE decision open — the s246 DAIS Option-B design, ELIGIBLE s247**
(74 resolved). Then the deepest genuinely-owed unit is that ratification: **RATIFY → FREEZE → RUN the DAIS Option-B graded-preference
correlation probe** (the dative line's first human effect-SIZE comparison; fresh reviewer + non-Anthropic vote fix Q1/Q2/Q3, then freeze
with the contamination firewall + PREREG sha, then the ~$2.6 run — split the two arms if the day's headroom is short; do NOT smuggle the
run into the ratifying session; do NOT lift DAIS sentences). The own-panel preemption design stays DECLINED (six sessions); the 3 unopened
phil scout candidates deepen the phil lean; the A4b ladder gate is process-ahead-of-need; **else verify/stop**. End squash-merged to `main`.
