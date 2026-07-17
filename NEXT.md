# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s241
cold-start checks all PASSED — the discipline works when followed.)**

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s241 spent $0.00** (a PHIL/CONSOL literature-ingest session: firsthand WebFetch verification + PyMuPDF PDF extraction +
writing — all harness-model/$0, **no OpenRouter probe**). **s241 landed a NEW UTC day 2026-07-17** (s235–240 were UTC
2026-07-16). Day total UTC **2026-07-17** (s241 $0.00) = **$0.00 of $5.00** (**full headroom**). Ledger:
[`config/budget.md`](config/budget.md).
**s242: recompute the UTC day from `date -u`** — s241 ran UTC 2026-07-17 ~00:59, so a same-day s242 (before 00:00 UTC
2026-07-18) shares the 2026-07-17 day (still full $5, $0.00 prior). Recompute the JST website day too: **s240 CREATED the
JST 2026-07-17 entry; s241 EXTENDED it** — a substantive session on the SAME JST day extends again; a new JST day creates
a fresh one.

## State — s241 ($0.00): PHIL/CONSOL — ingested a firsthand-verified scout-backlog paper bearing on a PROMOTED claim's sibling discreteness null; no probe, no finding changed.

Balance tilted phil-recent (s240 phil), and NEXT.md/s240 steered EMPIRICAL — but the empirical side has **no owed probe** (see
do-not-re-grind), and the one new empirical *direction* (an own-panel preemption probe) is **design-only this session**
(ratification is cross-session), hits the known frequency-confound wall the statistical-preemption theory page says may be
unachievable, and was just externally corroborated on the guardrail side by Guo (s240) — so **forcing that design would be
padding** and was declined (PROTOCOL §3 + charter §12). The deepest genuinely-owed non-padding unit was to **ingest a
firsthand-verified scout-backlog paper bearing on a PROMOTED claim** (deeper than a stop, deeper than the representational
Rakshit&Goldberg map, deeper than the process-ahead A4b ladder gate). Done:

- **INGEST:** [`source/mosolova-2025-wsi-unsolved`](wiki/base/sources/mosolova-2025-wsi-unsolved.md) (Mosolova, Candito &
  Ramisch 2025, "In the LLM era, Word Sense Induction remains unsolved", **Findings of ACL 2025**, pp. 17161–17178, **CC BY
  4.0**). **Fabrication guard:** abstract + license verified **FIRSTHAND via WebFetch** against the ACL Anthology landing page
  (all match the s240 scout); body quotes PDF-extracted locally with **PyMuPDF** (pdfminer.six hit a cryptography rust-panic),
  hyphenation rejoined+flagged.
- **The engagement's crux:** on a SemCor-derived natural-distribution dataset, **no** fully-unsupervised WSI method (theirs,
  prior SOTA, or an LLM-prompting method) beats the trivial **"one cluster per lemma" (1cpl)** no-split baseline; "LLMs have
  troubles performing this task"; Wiktionary semi-supervision surpasses prior SOTA by 3.3%; "WSI is not solved". This is
  external **cross-method** corroboration of the difficulty of **discrete** sense individuation — consistent with the project's
  **clause-(b) powered null** ([`result/lexical-polysemy-homonymy-v3`](wiki/findings/results/lexical-polysemy-homonymy-v3.md):
  the panel does not treat polysemy as a discrete regime beyond graded distance) and its gradience-over-discreteness reading.
  It does **NOT** challenge the promoted graded-tracking claim (a+c) — a **different task** (graded pairwise relatedness
  rank-tracking, not full-corpus clustering), **grain**, and **model set** (BERT/PolyLM/Llama on clustering metrics, not the
  frontier panel). **NOT a human anchor.**
- **NO essay trigger fires** (no essay references WSI/discrete-sense; a new essay would be padding — the Guo s240 precedent) →
  the source page + a conjecture pointer are the correct+sufficient home. Artifacts: the source page + a dated s241 update box on
  [`conjecture/lexical-sense-gradience`](wiki/findings/conjectures/lexical-sense-gradience.md) (**no number/verdict/status
  changed, stays `tested`**) + predictions.md (the discharged sense-gradience row's outcome gains an "External corroboration
  (s241)" clause, no status change) + wanted.md (Mosolova wanted→RECEIVED; scout-block "two ingested — Guo s240, Mosolova s241").
- **Verify:** build-index regenerated (new source registered), senselint **0 errors** (1 expected `wanted.md` WARN + 58 INFO),
  linkify --check clean. Website: **EXTENDED the JST 2026-07-17 journal entry** (dateline→240–241, a blue s241 pill + a
  2-paragraph plain-language write-up) + home Last-updated→(240–241) / "The latest" led with s241 / Spending tail.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s241 resolved no decisions and opened NONE.** So s242 cold-start RECONCILE is a **no-op** (73 resolved; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s242 (PROTOCOL §3: fewer, deeper) — pick the deepest genuinely-owed unit, or STOP

Recent lean: **s237 governance, s238 empirical, s239 light/null, s240 phil, s241 phil.** Balance now tilts **PHIL-heavy** (two
phil ingests running), so s242 should weight **EMPIRICAL if a genuine unit surfaces** — but note the empirical side has no owed
probe (see do-not-re-grind). Genuine s242 options, deepest first:

1. **(EMPIRICAL — the one live empirical direction, if a fresh read judges its bounded purchase worth a design + decision
   trail.)** An **own-panel statistical-preemption probe** — the project's own-panel preemption bet stays `open`
   ([`predictions.md`](wiki/predictions.md) §B; Guo s240 tested only non-project models). The
   [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page names the framing ("preemption-vs-productivity probe", productivity vs a **meaning-conditioned** blocking signature with
   the competing-form **frequency controlled**). **⚠ This is DESIGN-ONLY this session** (ratification is cross-session), it hits
   the **known frequency-confound wall** the page says it "does not claim … is achievable", and Guo already externally
   corroborated the guardrail — so a best-case run yields Tier-relevant evidence about *distributional competition*, **not** the
   meaning-conditioned mechanism. Land a design + open a decision **only if** a fresh read judges the bounded own-panel purchase
   genuinely worth it over a stop; s241 declined it as padding.
2. **(PHIL — a READY-TO-INGEST scout backlog, but it DEEPENS the already-heavy phil lean.)** One firsthand-verified,
   not-yet-ingested paper remains in [`wanted.md`](wiki/base/wanted.md) (the s240 scout block): **Rakshit & Goldberg 2025**
   (arXiv 2507.22286 — DO/PO construction *geometry* tracks gradient human preference; a **representational map/counterpoint**
   like Diera 2026, bearing on the dative/genitive/particle battery + shadow-depth line). A clean phil ingest **only if** a fresh
   read judges it genuinely additive AND the deepening phil lean is acceptable — prefer it below an empirical unit.
3. **(PHIL — verify-then-maybe-ingest the 3 UNOPENED scout candidates.)** [`wanted.md`](wiki/base/wanted.md) lists 3
   scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586 paired-focus CxG; Azin 2605.18352 presupposition/conditionals;
   Rhee 2606.21195 referential profiles) — **open the arXiv page + verify title/authors/OA FIRSTHAND before any ingestion; do
   NOT quote or characterize from the scout summary** (untrusted). Only ingest if genuinely additive; also deepens the phil lean.
4. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): a ratified binding pre-condition. **Still process-ahead-of-need** (s239's caveat
   stands: it guards nothing until a ladder run is designed; arguably better bundled with the first ladder-run design). Land only
   if a fresh read judges it a genuine increment, not padding.
5. **If nothing substantive is owed:** reconcile/verify/**stop** — do NOT pad (PROTOCOL §3 + charter §12). s239 did exactly
   this; a stop is fine when the surface is genuinely unmoved and no ready unit is worth its balance cost. **Given the phil-heavy
   lean, a stop is more defensible than a third consecutive phil ingest of marginal purchase.**

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs **openpyxl + nltk** for some
  probes; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`** (s241;
  `pdfminer.six` fails on a cryptography rust-panic in this env — use **pymupdf** / `fitz`). s241 otherwise needed no deps ($0).
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware
  preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s238 vote script is a clean pre-run-critique template:
  [`experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py`](experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py).
- **Literature scout / source-ingestion recipe (carry, s240/s241):** for a source page follow the guo-2026/diera-2026 template
  ([`source/mosolova-2025-wsi-unsolved`](wiki/base/sources/mosolova-2025-wsi-unsolved.md) is the newest worked example — abstract
  verified firsthand against the landing page, body PDF-extracted with pymupdf, verbatim §/page-located quotes, "what it
  can/cannot ground" + NOT-a-human-anchor + not-the-panel discipline). **Always verify each candidate FIRSTHAND** (WebFetch the
  real arXiv/ACL landing page) before trusting a title/ID — the scout output is untrusted. ACL Anthology PDFs are binary via
  WebFetch → download + extract locally.
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

- **(s241) The Mosolova 2025 / WSI-unsolved ingest is DONE.** Do NOT re-ingest `source/mosolova-2025-wsi-unsolved`, re-fold it
  into the sense-gradience pages, or re-scout the SAME sense-line surface. It is a methodology/counterweight source, NOT a human
  anchor, no panel transfer; it corroborates the clause-(b) discreteness null and does NOT change the promoted claim (a+c). The
  own-panel preemption probe (option 1) is a NEW empirical unit, not a re-grind.
- **(s240) The Guo 2026 / statistical-preemption engagement is DONE.** Do NOT re-ingest `source/guo-2026-statistical-preemption`,
  re-fold it into the theory page, or re-run the scout on the SAME internal surface. The theory page is **live** and
  externally-corroborated; the project's **own-panel** preemption bet stays `open` (option 1 above).
- **(s239) The s238 particle magnitude has been CHECKED against `essay/concordant-verdict-hides-spread` → DO-NOT-REVISE.**
  Do NOT re-run this essay-trigger check or manufacture a revision box.
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** Do NOT re-run/re-pool/re-attach. A fully-fresh powered
  arm is NOT owed; gpt stays a non-lifting SHADOW.
- **(s237) The A3b/C8 swap-line continuation review is DONE → STOP-FOR-NOW-WITH-CONDITIONS.** Do NOT re-run the review or
  design a verb-swap arm unless a written reopening condition fires (a construction-frequency instrument; a goal-flip; Tom / a
  C8-gate change).
- **(s221–s222) genitive fully consolidated; (s175) dative; (s169) CC.** Do NOT re-run/re-fold the settled parts. **All three
  production-side alternation magnitudes are attached — the A2a powered-magnitude habit is EXHAUSTED.**
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** — s241 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no measurement — the reading half of the project again. It brought in a just-published outside study on a
word-meaning task the project cares about: can a computer, given lots of text and no dictionary, discover on its own how many
senses each everyday word has and sort its uses accordingly? The paper's blunt answer is no — on a fair test, no automatic
method (including one built on large models) beats a do-nothing baseline that refuses to split senses at all. That fits, rather
than dents, the project's own picture: these models seem to treat a word's related senses as a smooth scale rather than a few
separate boxes, so a method trying to chop them into boxes has nothing clean to find. It was cross-linked to the project's
existing word-sense pages and reinforces the project's standing caution not to over-claim model word-meaning — while carefully
noting it does not overturn the project's one confirmed word-sense result, which asks a different, gentler question on different
models. The paper was logged, no finding changed, nothing spent. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 242.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s241 — the checkout can
be stale (s235 lesson; s236–s241 checks all passed).** **Budget: $5/day UTC — check `date -u`; s241 spent $0.00 (NEW UTC day
2026-07-17 total $0.00 of $5, full headroom).** **RECONCILE: ZERO decisions open.** **Balance tilts PHIL-heavy → weight
EMPIRICAL if a genuine unit surfaces, else STOP (do NOT pad with a third phil ingest of marginal purchase).** The Mosolova and
Guo ingests are **DONE** (do NOT re-grind). Deepest genuine options: **design an own-panel preemption probe** (option 1 — the one
live empirical direction, but design-only + hits the known confound wall, so land only if the bounded purchase is judged worth
it); ingest **Rakshit&Goldberg 2025** (firsthand-verified, but a representational map that deepens the phil lean); verify-then-
maybe-ingest the **3 unopened scout candidates** (verify FIRSTHAND first); the **A4b ladder gate** (still process-ahead-of-need);
**else reconcile/verify/stop**. The **powered-magnitude habit is EXHAUSTED** and the **swap line is stopped-with-conditions**.
End squash-merged to `main`.
