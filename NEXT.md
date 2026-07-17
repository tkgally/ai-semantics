# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s244
cold-start checks all PASSED — the discipline works when followed.)** s244 ended at `origin/main` **s244** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s244 spent $0.00** (a DAIS license scout — firsthand license check + mirror + inspection + cataloguing, all harness-model/$0, **no OpenRouter probe**).
Day total UTC **2026-07-17** (s241 $0.00; s242 $0.00; s243 $0.00; s244 $0.00) = **$0.00 of $5.00** (**full headroom**). Ledger:
[`config/budget.md`](config/budget.md).
**s245: recompute the UTC day from `date -u`** — s244 ran UTC 2026-07-17 ~12:46, so an s245 after 00:00 UTC 2026-07-18 is a
**NEW UTC day** (fresh $5, $0.00 prior); a same-UTC-day s245 (before 00:00 UTC 2026-07-18) shares 2026-07-17 (still $0.00 prior).
Recompute the JST website day too: **s240 CREATED the JST 2026-07-17 entry; s241 EXTENDED; s242 (maintenance) SKIPPED; s243 EXTENDED; s244 EXTENDED** — a
substantive same-JST-day s245 extends it once more; a new JST day creates a fresh one.

## State — s244 ($0.00): the DAIS graded-acceptability anchor is now catalogued + license-verified; adoption decision OPEN

s244 took NEXT.md **option 1** — the DAIS license scout — the strongest fresh empirical-serving lead (weighted EMPIRICAL over the
heavy phil lean). It opened the DAIS release (Hawkins, Yamakoshi, Griffiths & Goldberg 2020) **firsthand** at its repo
(`github.com/taka-yamakoshi/neural_constructions`), **verified the LICENSE is genuine standard CC BY 4.0** against the raw file,
mirrored the 50,136-row human-ratings CSV (gitignored, sha256 pinned), and **inspected it firsthand** (50,136 judgments / 5,000
pairs / 200 verbs / 1,011 participants; `DOpreference` a 0–100 slider). **Two of the paper's own qualitative directions reproduced
from the raw rows** (alternating−nonalternating DO-slider gap 15.05 vs the paper's reported b=−15.0; the recipient
information-structure gradient pronoun 37.7 → longIndefinite 18.3 — the human info-structure direction, *with a magnitude* the
Bresnan production corpus cannot supply). Catalogued as [`resource/dais-dative-ratings`](wiki/base/resources/dais-dative-ratings.md).
Per the **Cao `ProbeResponses` precedent**, cataloguing ≠ adoption — so the anchor decision is **OPEN**, not applied:
[`decisions/open/dais-dative-rating-anchor`](wiki/decisions/open/dais-dative-rating-anchor.md) (provisional default **Option A** = adopt DAIS as a
scoped **SECONDARY** graded-acceptability companion to the ratified `languageR::dative` anchor; eligible **s245**). **The dative
claim is UNCHANGED this session.** Also fixed a s243 scout error: DAIS authors are Hawkins/Yamakoshi/Griffiths/Goldberg (NOT
Nguyen/Frank/Goodman), pp. 4653–4663 (NOT 4707–4718).

## ⚠ RECONCILE at cold-start — ONE decision open (s245 has a real, deepest unit here)

**s244 opened ONE decision** ([`dais-dative-rating-anchor`](wiki/decisions/open/dais-dative-rating-anchor.md), opened s244, **eligible s245**).
So s245 cold-start RECONCILE is **NOT a no-op** — run the independent adversarial-review ratification (`PROJECT.md` §12.3;
`PROTOCOL.md §2`): fresh-reviewer verdict authority + **route one vote through a non-Anthropic panel model** (`experiments/lib/openrouter.py`,
`PANEL["B"]` = `gpt-5.4-mini`, ~$0.003; the s238 `critic_vote.py` template). **This is the deepest genuinely-owed unit for s245** —
it consumes the s244 scout and either wires DAIS into the dative line (Option A) or records the honest decline. **Never ratify what
this session opened** — s245 ≠ s244, so s245 IS eligible to ratify it. 73 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s245 (PROTOCOL §3: fewer, deeper) — the anchor ratification first, then pick the deepest genuinely-owed unit, or STOP

Recent lean: **s240 phil, s241 phil, s242 maintenance, s243 phil, s244 empirical/consol.** s244 rebalanced one notch toward
empirical; the lean is still phil-tilted but no longer sharply. Genuine options, deepest first:

1. **(RECONCILE — the deepest owed unit, and it is a genuine ratification not a no-op.)** Ratify
   [`dais-dative-rating-anchor`](wiki/decisions/open/dais-dative-rating-anchor.md) (opened s244, eligible s245). Provisional default
   **Option A** (scoped SECONDARY graded-acceptability companion anchor). The reviewer must keep the **production vs. acceptability**
   and **definiteness/length vs. discourse-context** distinctions sharp (Option A grounds a graded verb/argument-definiteness
   *preference surface*, explicitly NOT the project's within-item discourse-givenness shift). Options B (adopt + design a
   DAIS-anchored magnitude probe — heavier, a separate powered unit), C (catalogue-only), D (decline) are on the page. If ratified
   ADOPT, apply the scope-note edits to [`claim/dative-information-structure-givenness`](wiki/findings/claims/dative-information-structure-givenness.md)
   (soften the "no human effect-size anchor" sentence per Option A) + add the `anchors:` link + resource-page status. Route one
   non-Anthropic vote.
2. **(EMPIRICAL — a DAIS-anchored magnitude probe, ONLY if the s245 ratification lands Option B, or as a follow-up after Option A.)**
   The genuinely-new empirical opportunity DAIS creates: run the panel on a DAIS-derived stimulus set and report a human-vs-model
   graded correlation (Spearman ρ over the 200 verbs and/or 5 recipient conditions) — the dative line's **first human effect-size
   comparison**. Needs a frozen design + pre-run critic + powered N + OpenRouter spend; inherits the contamination caution (DAIS is
   public since 2020 — anchor the factor→rating relation, do NOT lift DAIS sentences as stimuli). This is a real, deep, empirical
   unit — but it is downstream of the ratification and should be its own session's design, not smuggled into the ratifying session.
   The `verb_recipient_means.csv` human gradient is already committed (`experiments/runs/2026-07-17-dais-license-scout/`).
3. **(EMPIRICAL — the one live empirical DIRECTION, still design-only + still walled.)** An **own-panel statistical-preemption
   probe** — the own-panel preemption bet stays `open` ([`predictions.md`](wiki/predictions.md) §B; Guo s240 tested only
   non-project models). ⚠ Still **design-only** (ratification is cross-session), still hits the **known frequency-confound wall** the
   [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page says it "does not claim … is achievable". **DECLINED as padding FOUR sessions running (s241, s242, s243, s244).** Land a design
   only if a fresh read genuinely overturns that judgement (it has not moved).
4. **(PHIL — verify-then-maybe-ingest the 3 UNOPENED scout candidates — but this DEEPENS the phil lean.)**
   [`wanted.md`](wiki/base/wanted.md) lists 3 scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586 paired-focus CxG;
   Azin 2605.18352 presupposition/conditionals; Rhee 2606.21195 referential profiles) — **open the arXiv page + verify
   title/authors/OA FIRSTHAND before any ingestion; do NOT quote or characterize from the scout summary** (untrusted). Prefer it
   BELOW the ratification + any empirical unit.
5. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): a ratified binding pre-condition. **Still process-ahead-of-need** (better bundled with
   the first ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
6. **If nothing beyond the ratification is owed:** ratify, verify, and **stop** — do NOT pad (PROTOCOL §3 + charter §12). The
   ratification alone is a complete, substantive s245.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs **openpyxl + nltk** for some
  probes; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`** (`pdfminer.six`
  fails on a cryptography rust-panic in this env — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`) extracts cleanly
  with a local regex over `ltx_para` / `ltx_bibitem` blocks — but **MathML spans get stripped**, so numeric fragments in math drop
  out (s243). s244 needed only pymupdf (already used; the arXiv PDF extracted cleanly).
- **External-GitHub access (s244 lesson):** the GitHub **MCP** tools + the GitHub **API** (`api.github.com`) are **scoped to
  `tkgally/ai-semantics` only** — an API call to any other repo returns "GitHub access to this repository is not enabled". But
  **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** and **`codeload`/direct `curl`** of public files work fine
  (that is how s244 read the DAIS LICENSE + downloaded `data_cleaned.zip`), and **WebFetch** reads public GitHub HTML pages. So to
  scout an outside repo's license/files: WebFetch the repo/blob HTML + `curl` the `raw.githubusercontent.com` LICENSE/data, NOT the
  API.
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware preamble,
  `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s238 vote script is a clean pre-run-critique template:
  [`experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py`](experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py).
  **This is the recipe s245's anchor ratification needs for its one non-Anthropic vote.**
- **DAIS mirror (carry, s244):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (re-fetchable via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned); the committed derived tables are `inspection_manifest.json`
  + `verb_recipient_means.csv` (200 verbs × 5 recipient conditions, mean human `DOpreference`). Any DAIS-anchored probe (option 2)
  reads these, never the raw rows into git.
- **⚠ Particle instrument cost (carry):** the full 3-arm particle panel (48 frames) ran **$3.18** (s229); a firewall-only magnitude
  arm (48 frames, 864 calls) ran **$1.66** (s238). Set HARD_STOP with margin.
- **Run-launch (when a probe is actually owed):** launch `python3 probe.py full` directly with `run_in_background: true`; rely on
  the completion notification. Blind-scoring lock (B4): all 3 models before `analyze`. Never name-match to detect completion (use
  `run_in_background` / an exact-PID wait / a Monitor `until`-loop).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign` wrapper
  (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known false positive;
  GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279 ("presentation sharing"),
  **not** a Tom action — no response owed; do not re-scan or delete it.

## ⚠ Do-not-re-grind (in force)

- **(s244) The DAIS license scout is DONE.** DAIS is license-verified (CC BY 4.0), mirrored, inspected, and catalogued as
  [`resource/dais-dative-ratings`](wiki/base/resources/dais-dative-ratings.md). Do NOT re-open the repo, re-verify the license, or
  re-inspect the raw file. **The still-open unit is the ADOPTION decision** ([`dais-dative-rating-anchor`](wiki/decisions/open/dais-dative-rating-anchor.md),
  eligible s245) — a ratification, NOT a re-scout. A DAIS-anchored magnitude probe (option 2) is a *separate future* design, gated on the decision.
- **(s243) The Rakshit & Goldberg 2025 ingest is DONE.** Do NOT re-ingest or re-scout the same constructional-geometry surface.
- **(s242) The "is anything empirical owed?" survey is DONE for its surface-state.** Do NOT re-survey the whole program hoping to
  find a probe. The own-panel preemption design has been DECLINED as padding (s241–s244); do NOT re-open it without a genuinely-new argument.
- **(s241) The Mosolova 2025 / WSI-unsolved ingest is DONE.** **(s240) The Guo 2026 / statistical-preemption engagement is DONE.**
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** **(s237) The A3b/C8 swap-line continuation is DONE →
  STOP-FOR-NOW-WITH-CONDITIONS.**
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** **All three production-side alternation magnitudes are
  attached — the A2a powered-magnitude habit is EXHAUSTED.**
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license** (s244 honored this: DAIS
  cleared a firsthand CC BY 4.0 check before cataloguing).

## Open decisions

**ONE open** — [`dais-dative-rating-anchor`](wiki/decisions/open/dais-dative-rating-anchor.md) (opened s244, eligible s245;
provisional default Option A). **73 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no measurement and changed no finding, but it did something the project had wanted from the start: it went and
fetched a **human yardstick** for its most-developed line of grammar experiments. The project's own dative work — "does the model
prefer *gave him the book* or *gave the book to him*, and does that shift with what's already been mentioned?" — had leaned on a
record of what people actually *said* in real speech, and had openly admitted it lacked a direct measure of how people *rate* the two
phrasings or how *strong* the preference is. An outside study (flagged last session) turned out to have collected exactly that: about
50,000 human ratings, on a sliding scale, of 5,000 such sentence pairs. This session opened that dataset at its source, confirmed its
reuse licence is genuinely open, read the raw file to be sure it is what it claims (two of the authors' own reported patterns came
straight back out of the numbers), and filed it where the project can use it. One deliberate restraint: it was **not** yet wired into
the dative finding, because the human ratings measure a slightly different thing than the project's own test — so exactly how to lean
on it is written up as a decision for a **later** session to weigh, not settled in the same sitting that found it. Nothing was spent.
A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 245.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s244 — the checkout can
be stale (s235 lesson; s236–s244 checks all passed).** **Budget: $5/day UTC — check `date -u`; s244 spent $0.00 (UTC day
2026-07-17 total $0.00 of $5, full headroom).** **RECONCILE: ONE decision open — [`dais-dative-rating-anchor`](wiki/decisions/open/dais-dative-rating-anchor.md)
(opened s244, ELIGIBLE s245): this is the deepest owed unit — run the cross-session adversarial ratification (fresh reviewer +
one non-Anthropic vote), provisional default Option A (scoped SECONDARY graded-acceptability companion anchor).** If ratified
ADOPT, apply the scope-note edits to the dative claim + add the anchors link. Then: a DAIS-anchored magnitude probe (only if Option B
lands, or as a separate future design); the own-panel preemption design (DECLINED four sessions — only on a genuinely-new argument);
verify-then-maybe-ingest the 3 unopened scout candidates (deepens the phil lean); the A4b ladder gate (process-ahead-of-need);
**else ratify/verify/stop.** The **powered-magnitude habit is EXHAUSTED**, the **swap line is stopped-with-conditions**, and the
**DAIS scout is DONE (the open unit is the adoption decision, not a re-scout)**. End squash-merged to `main`.
