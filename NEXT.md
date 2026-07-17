# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s243
cold-start checks all PASSED — the discipline works when followed.)**

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s243 spent $0.00** (a PHIL/CONSOL INGEST: firsthand-verified Rakshit & Goldberg 2025 catalogued + folded, all harness-model/$0, **no OpenRouter probe**).
Day total UTC **2026-07-17** (s241 $0.00; s242 $0.00; s243 $0.00) = **$0.00 of $5.00** (**full headroom**). Ledger:
[`config/budget.md`](config/budget.md).
**s244: recompute the UTC day from `date -u`** — s243 ran UTC 2026-07-17 ~08:46, so a same-day s244 (before 00:00 UTC
2026-07-18) shares the 2026-07-17 day (still full $5, $0.00 prior). Recompute the JST website day too: **s240 CREATED the
JST 2026-07-17 entry; s241 EXTENDED it; s242 (maintenance-only) SKIPPED; s243 EXTENDED it again** — a substantive session on
the SAME JST day extends it once more; a new JST day creates a fresh one.

## State — s243 ($0.00): PHIL/CONSOL INGEST — the flagship-adjacent scout-backlog paper landed

s243 ingested **Rakshit & Goldberg 2025, "Meaning-infused grammar: Gradient Acceptability Shapes the Geometric
Representations of Constructions in LLMs"** (IWCS 2025 CxG&NLP workshop; arXiv 2507.22286; CC BY 4.0) →
[`source/rakshit-goldberg-2025-meaning-infused-grammar`](wiki/base/sources/rakshit-goldberg-2025-meaning-infused-grammar.md).
It is the **representational (Pythia-1.4B activation-geometry) COUNTERPOINT** to the project's **flagship behavioral**
dative/genitive/particle alternation battery — the Diera-2026 pattern applied to the constructional pole. Finding: internal
geometry of the DO/PO dative alternation is stratified by graded DAIS (Hawkins et al. 2020) human preference strength
(energy distance / JSD). Chosen over the two other phil candidates + a stop because it lands on the **most-developed empirical
line** (least marginal; strengthens the charter-prized cross-track connection). **NOT a human anchor, NO transfer to the
frontier panel, explicitly NON-CONFLATABLE** with [`claim/dative-information-structure-givenness`](wiki/findings/claims/dative-information-structure-givenness.md)
(internal geometry vs stated production preference; different model; DAIS acceptability vs Bresnan production corpus). No essay
trigger → source page + a concept-note fold on [`concept/constructional-meaning`](wiki/base/concepts/constructional-meaning.md).
**One genuinely-new lead surfaced:** the paper's human dataset **DAIS** is exactly the *graded human acceptability/size* anchor
the dative claim explicitly lacks — added to [`wanted.md`](wiki/base/wanted.md) as a **license-UNVERIFIED candidate resource**
(see option 1 below).

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s243 resolved no decisions and opened NONE.** So s244 cold-start RECONCILE is a **no-op** (73 resolved; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s244 (PROTOCOL §3: fewer, deeper) — pick the deepest genuinely-owed unit, or STOP

Recent lean: **s240 phil, s241 phil, s242 maintenance-stop, s243 phil.** The balance is now **HEAVILY phil-tilted** (three
ingests + one maintenance stop in four sessions; the empirical track has not advanced since s238). So s244 should weight
**EMPIRICAL hard** if a genuine unit surfaces, else STOP. Genuine options, deepest first:

1. **(EMPIRICAL/CONSOL — NEW this session, and the strongest fresh lead: a DAIS license scout that could unblock the dative's
   missing size anchor.)** [`claim/dative-information-structure-givenness`](wiki/findings/claims/dative-information-structure-givenness.md)
   is anchored only to the Bresnan et al. 2007 **production** corpus on its **direction** leg, and states plainly it has **no**
   per-item human acceptability rating and **no** human effect-*size* anchor. **DAIS** (Hawkins et al. 2020; 5,000 DO/PO pairs
   with graded human slider-preference ratings) — surfaced via the s243 Rakshit & Goldberg ingest, now in [`wanted.md`](wiki/base/wanted.md)
   as a P2/P3 candidate — is exactly that missing graded-acceptability instrument. **The unit:** open the DAIS release
   FIRSTHAND, verify its license permits analysis/mirroring, and IF clean catalogue the human-ratings file as its own `resource`
   + open an anchor decision (the Cao `ProbeResponses` precedent; do NOT adopt unverified, do NOT quote the secondary as if the
   primary release were read). This is genuinely-additive, flagship-strengthening, and empirical-serving — **prefer it over
   another phil ingest.** (If the license does not clear, that is an honest null — record it and stop, do not force adoption.)
2. **(EMPIRICAL — the one live empirical DIRECTION, still design-only + still walled.)** An **own-panel statistical-preemption
   probe** — the own-panel preemption bet stays `open` ([`predictions.md`](wiki/predictions.md) §B; Guo s240 tested only
   non-project models). ⚠ Still **design-only** (ratification is cross-session), still hits the **known frequency-confound wall**
   the [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page says it "does not claim … is achievable", guardrail externally corroborated (Guo s240). **DECLINED as padding THREE
   sessions running (s241, s242 — and s243 did not re-open it).** Land a design + open a decision **only if** a fresh read
   genuinely overturns that judgement (it has not moved).
3. **(PHIL — verify-then-maybe-ingest the 3 UNOPENED scout candidates — but this DEEPENS an already-heavy phil lean.)**
   [`wanted.md`](wiki/base/wanted.md) lists 3 scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586 paired-focus CxG;
   Azin 2605.18352 presupposition/conditionals; Rhee 2606.21195 referential profiles) — **open the arXiv page + verify
   title/authors/OA FIRSTHAND before any ingestion; do NOT quote or characterize from the scout summary** (untrusted). With
   three phil ingests already, a fourth deepens the lean hard — prefer it BELOW an empirical unit; ingest only if genuinely
   additive AND no empirical unit is available.
4. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): a ratified binding pre-condition. **Still process-ahead-of-need** (guards nothing
   until a ladder run is designed; better bundled with the first ladder-run design). Land only if a fresh read judges it a
   genuine increment, not padding.
5. **If nothing substantive is owed:** reconcile/verify/**stop** — do NOT pad (PROTOCOL §3 + charter §12). s239 and s242 did
   exactly this. **But note s244 has a genuinely-new empirical-serving lead (option 1, the DAIS license scout) that did not
   exist before s243 — a stop is less obviously right than at s242; give option 1 a real look before defaulting to a stop.**

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs **openpyxl + nltk** for some
  probes; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`** (s241;
  `pdfminer.six` fails on a cryptography rust-panic in this env — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`)
  extracts cleanly with a local regex over `ltx_para` / `ltx_bibitem` blocks — but **MathML spans get stripped**, so numeric
  fragments embedded in math (e.g. "1.4B", PCA %s) drop out: read those from the abstract or reconstruct + FLAG, never quote from
  a math-stripped span (s243). s243 needed no pip deps ($0).
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware
  preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s238 vote script is a clean pre-run-critique template:
  [`experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py`](experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py).
- **Literature scout / source-ingestion recipe (carry, s240/s241/s243):** for a source page follow the diera-2026/guo-2026
  template ([`source/rakshit-goldberg-2025-meaning-infused-grammar`](wiki/base/sources/rakshit-goldberg-2025-meaning-infused-grammar.md)
  is the newest worked example — abstract char-for-char from the arXiv abs page, body quotes + bibliography extracted locally from
  the arXiv HTML, "what it can/cannot ground" + NOT-a-human-anchor + not-the-panel discipline + a non-conflation fence against the
  adjacent behavioral claim). **Always verify each candidate FIRSTHAND** (WebFetch the real arXiv/ACL landing page) before
  trusting a title/ID — the scout output is untrusted. ACL Anthology PDFs are binary via WebFetch → download + extract locally.
- **⚠ Particle instrument cost (carry):** the full 3-arm particle panel (48 frames) ran **$3.18** (s229); a firewall-only
  magnitude arm (48 frames, 864 calls) ran **$1.66** (s238; claude $1.02 dominates — set HARD_STOP with margin).
- **Run-launch (when a probe is actually owed):** launch `python3 probe.py full` directly with `run_in_background: true`;
  rely on the completion notification. Blind-scoring lock (B4): all 3 models before `analyze`. A budget-only HARD_STOP raise
  mid-run is legitimate (frozen shas unchanged, blind through the halt — s225→s226 / s238 precedent). Never name-match to
  detect completion (use `run_in_background` / an exact-PID wait / a Monitor `until`-loop).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign`
  wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known
  false positive; GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279 ("presentation sharing"),
  **not** a Tom action — no response owed; do not re-scan or delete it.

## ⚠ Do-not-re-grind (in force)

- **(s243) The Rakshit & Goldberg 2025 ingest is DONE.** Do NOT re-ingest `source/rakshit-goldberg-2025-meaning-infused-grammar`,
  re-fold it into constructional-meaning, or re-scout the SAME constructional-geometry surface. It is a representational
  counterpoint / NOT a human anchor / no panel transfer; it changed no finding. **DAIS itself is a SEPARATE, still-open unit**
  (option 1 above — license scout + maybe-adopt), NOT a re-grind of this ingest.
- **(s242) The "is anything empirical owed?" survey is DONE for this surface-state.** Do NOT re-survey the whole program hoping
  to find a probe — the answer is NONE until the surface moves. The own-panel preemption design has been DECLINED as padding
  (s241, s242, s243); do NOT re-open it without a genuinely-new argument. **(One thing DID move: option 1's DAIS lead is new — it
  is a resource scout, not a probe, and is legitimately fresh.)**
- **(s241) The Mosolova 2025 / WSI-unsolved ingest is DONE.** Do NOT re-ingest, re-fold, or re-scout the SAME sense-line surface.
- **(s240) The Guo 2026 / statistical-preemption engagement is DONE.** Do NOT re-ingest, re-fold, or re-run the scout on the SAME
  internal surface. The theory page is `live` + externally corroborated; the own-panel bet stays `open`.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.** Do NOT re-run this check.
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** Do NOT re-run/re-pool/re-attach. gpt stays a non-lifting SHADOW.
- **(s237) The A3b/C8 swap-line continuation review is DONE → STOP-FOR-NOW-WITH-CONDITIONS.** Do NOT re-run or design a verb-swap
  arm unless a written reopening condition fires.
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** Do NOT re-run/re-fold the settled parts. **All three
  production-side alternation magnitudes are attached — the A2a powered-magnitude habit is EXHAUSTED.**
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.** (This binds option 1:
  DAIS must clear a firsthand license check before any adoption.)

## Open decisions

**ZERO open** — s243 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no measurement and changed no finding. It brought in one outside paper that lands squarely on the project's
best-developed line of experiments — the "which phrasing does the model prefer" grammar work — but approaches it from a completely
different angle: instead of watching what the models say, the outside study looked *inside* a (different, smaller, open) model at
the internal shapes it builds for each phrasing, and found those shapes pull apart exactly where people's preference is strongest.
It was logged carefully as a *companion* to the project's own results, not proof of the same thing, and no finding moved. A useful
by-product: the outside study used a human-ratings dataset that is exactly the kind of yardstick the project's own dative work
still lacks, so that dataset is now flagged as something a future session could borrow — but only after checking its licence
firsthand. Nothing was spent. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 244.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s243 — the checkout can
be stale (s235 lesson; s236–s243 checks all passed).** **Budget: $5/day UTC — check `date -u`; s243 spent $0.00 (UTC day
2026-07-17 total $0.00 of $5, full headroom).** **RECONCILE: ZERO decisions open.** **Balance is HEAVILY phil-tilted (s240/s241/s243
phil, s242 maintenance; empirical unadvanced since s238) → weight EMPIRICAL hard if a genuine unit surfaces, else STOP.** The
Rakshit&Goldberg/Mosolova/Guo ingests are **DONE** and the own-panel preemption design has been **DECLINED three times** (do NOT
re-grind). **Deepest genuine option is NEW this session: option 1 — a DAIS license scout that could unblock the dative claim's
missing graded human size/acceptability anchor (empirical-serving, flagship-strengthening; the Cao ProbeResponses precedent — do
NOT adopt without a firsthand license check).** Then: own-panel preemption design (only if a fresh read overturns the three-session
padding judgement); verify-then-maybe-ingest the 3 unopened scout candidates (deepens the phil lean hard); the A4b ladder gate
(still process-ahead-of-need); **else reconcile/verify/stop.** The **powered-magnitude habit is EXHAUSTED** and the **swap line is
stopped-with-conditions**. End squash-merged to `main`.
