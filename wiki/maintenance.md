# maintenance.md — wiki coherence & maintenance ledger

**What this is.** The standing record of the **wiki-coherence campaign** (opened 2026-07-05,
session 183, by Tom's standing override): what has been audited, what was fixed and how, what was
*deliberately not* changed, and the per-phase checklists for the sessions that continue it. The
campaign plan lives in [`../continue-prompt.md`](../continue-prompt.md) §5; this page is the
working ledger. When the campaign closes (P5), this page stays as the audit record and future
maintenance accretes here.

---

## The s183 full audit

**Method.** Six parallel read-only auditors over disjoint slices (results ×2; claims + theory +
conjectures + open-questions; essays + [`ideas.md`](ideas.md) + [`predictions.md`](predictions.md); sources + concepts +
`wanted.md`; resources + resolved decisions + top-level surfaces), each checking seven defect
kinds (stale status, stale pointer, contradiction, missing link, repetition, convention drift,
research seeds) against a shared ground-truth brief. All ~370 pages opened; the spine
(claims/theory/conjectures/open-questions), all 50 essays, all 20 resources, and all 17 concepts
were read in full. Orchestrator triage (judgement not parallelized), then five fix agents with
row-exact directives; the orchestrator applied every BLOCKER itself.

**Headline diagnosis.** The wiki's *content* is sound — no measured number, verdict, or claim
scope was found wrong (one off-by-one annotator count aside, recomputed from raw and corrected).
The systemic defect is **back-annotation lag**: pages are written as terminal records and were
almost never revisited when later sessions promoted, replicated, retired, or superseded their
lines — so the s168–s181 promotions, the four powered replications, the two theory second
editions, and several same-day follow-ups were invisible from exactly the pages a reader lands
on first. A second layer: convention drift the schema never pinned down (result-status
semantics; essay status-blockquote upkeep; two undeclared meaning-sense tags; the documented
`anchors` link direction contradicting universal practice).

**Scale.** ~170 distinct issues: 12 BLOCKER (a current reader would be misled about a
finding/status), ~110 SHOULD-FIX, the rest NIT. Plus ~30 research seeds (harvested below).

## The s183 fix tranche — what was done

- **All 12 BLOCKERs fixed by the orchestrator** (dated `Update (2026-07-05, session 183 —
  wiki-coherence pass)` boxes; originals kept visible): the dative v1/v2 gpt-WEAK story
  (reversed at power, s175); CC v1 "not promoted pending Tom's review" (promoted s168, powered
  s169); the conative COMMITMENT-ONLY anomaly (failed replication, retired); the coercion-v2
  "unrun" next steps (both ran); the sense-gradience v1 missing promotion/rep2 pointers; the
  relational "claude-only capability" (dissolved 3/3 under a working surface, s177 claim) and
  "stays proposed" (falsified/retired 06-16); the two live theory v2 editions' "single-run"
  statements (both flags discharged — AANN s178, sense s181 — including the constructional v2's
  own fired trigger); the flagship table's internally-inconsistent honesty box; the
  `tested`-with-no-outcome presupposition conjecture; three concept on-ramps describing promoted
  lines as unrun/unfetched; the VWSD resource page whose last word was "v2 does not yet exist."
- **Batch fixes via five directive-driven fix agents** (each row verified against the cited
  pages before writing): missing update boxes / forward pointers on ~45 result pages; the
  "awaits Tom's review" archaism governance-noted in 13 files (PROJECT.md §12.3); one-time
  edition pointers at first prose citation of superseded theory v1 pages (~25 files, essays +
  results + spine); missing `supports` back-links from founding results to their promoted claims
  (~20 front-matters); concept/source "not in-repo" claims corrected (~15 files); resource pages
  reconciled with their lines' outcomes (DWUG "never downloaded" → two powered runs; scivetti
  probes list through s177; wic/subtlex/lancaster/mahowald pointers); the resources catalog's 5
  missing entries; the essay convention standardization (4 stale blockquotes, 4 status
  normalizations, 2 `updated:` fixes, trigger-site annotations incl. the witness-seeking
  trigger-(a) contradiction).
- **Top-level surfaces:** [`executive-summary.md`](executive-summary.md) fully regenerated
  (program **B4** ticked — it had been ~59 sessions stale and self-contradictory);
  [`predictions.md`](predictions.md) completed (the missing under-licensed-middle cleft-battery
  §B row; two essays named in §C; one mis-filed contingency regrouped); [`program.md`](program.md) item bodies
  reconciled with its own ledger rows (A1b, A2b, A3a, A3c, D3, B4); the [`index.md`](index.md) header now
  leads the syntheses with the flagship table; `multimodal-anchor-scouting.md` got the
  front-matter it predated (clearing the one undocumented senselint WARN).
- **Conventions documented in [`CLAUDE.md`](../CLAUDE.md)** (same-commit rule): the `anchors`
  link direction corrected (the doc had it backwards); the **edition-citation convention**
  (quotes cite the edition they quote; only as-if-current prose gets a pointer; no mass
  retargeting); the **essay status discipline** (front-matter authoritative; blockquote restates
  it; content-changing revision ⇒ `revised`; fired triggers annotated at the trigger).
- **Two decisions queued** (ratifiable from s184; **both ratified ADOPT-A + resolved s184**):
  [`decisions/resolved/result-status-upgrade-semantics`](decisions/resolved/result-status-upgrade-semantics.md)
  and [`decisions/resolved/meaning-senses-methodology-tags`](decisions/resolved/meaning-senses-methodology-tags.md).
- **One number corrected from raw:** sense-gradience v1's two-annotator count is 152/200 (n≥3 =
  48), not 151; the v1 page and run README carry dated corrections (rep2's "(v1: 48/200)" was
  right).

## What was deliberately NOT changed (and why)

- **No mass retargeting of theory-v1 references.** Most are quote-provenance citations; the v1
  banners route readers; the edition-citation convention (now in CLAUDE.md) is the durable fix.
- **No essay merges** (standing s182 fence: the essay web is load-bearing; the additive
  [`ideas.md`](ideas.md) is the map).
- **No result-status flips.** The ~13 `supported`-at-creation result pages stand untouched
  pending the queued decision — normalizing them now would apply a default in the session that
  opened it.
- **No `anchor:` field normalization.** Two live value styles coexist (`human-anchored` ×5 —
  including the s175 flagship — vs `resource/<id>` ×14); both are readable, senselint accepts
  both; recorded here as benign variance.
- **Superseded pages' bodies byte-untouched** (banners verified correct).
- **One typed-link deletion, recorded here** (the campaign's only removal outside the sanctioned
  classes): [`conjecture/aann-construction`](findings/conjectures/aann-construction.md) carried a spurious `refines →
  open-question/relational-meaning-pilot` edge (no reciprocal relationship; the pilot page says
  the constructional conjectures do not touch the relational axis) — deleted s183 rather than
  annotated, because a wrong machine-graph edge has no historical value a note would preserve.
- **Resolved decision pages untouched** (archival; only the changelog index's over-claim about
  `resolved-by` fields was softened).

## Known benign variances (documented; revisit only if they start costing readers)

- `anchor: human-anchored` vs `anchor: resource/<id>` (above).
- One essay ([`presupposition-environment-gated`](findings/essays/presupposition-environment-gated.md))
  carries `anchor: internal-contrast-only` in essay front-matter — informative, nonstandard for
  the type, harmless.
- Four documented meaning-sense sub-tags have zero uses, and senselint accepts any
  `known-prefix.suffix` string — sub-tag control is loose (note for the next vocabulary touch;
  see also the queued tags decision).
- Expected senselint residue is now exactly what CLAUDE.md documents: **1 WARN** (`wanted.md`,
  by design) + contingent-page INFOs.
- Result pages use two update-record shapes (dated boxes vs inline bracketed notes); both are
  dated and attributable — not worth normalizing.

## Deferred to P2 (the SHOULD-FIX remainder) — **CLEARED s184 (2026-07-06)**

**P2 status (s184):** both decisions ratified ADOPT-A (fresh reviewer + non-Anthropic vote
converged on each) and applied; the remainder below cleared. Details in the ledger row.

- ✅ **Apply the two ratified decisions.** Both ADOPT-A. *Result-status:* the event-based
  transition rule documented in [`../CLAUDE.md`](../CLAUDE.md) ("Result and theory status
  discipline") — mechanical-gate vs reading-bearing sort; `supported` for reading-bearing lines
  lives on the claim layer; gate pages may be *created* `supported`; result `status` declared
  non-ranking/possibly-stale until normalized; theory `draft → live` deferred to each page's next
  substantive touch. **No result page mass-edited; no theory page flipped to `live` this
  maintenance session** (per option A's no-mass-edit clause). *Meaning-senses tags:*
  `measurement-epistemic` added to [`meaning-senses.md`](meaning-senses.md) (gloss broadened to
  cover common-cause/convergence epistemics; How-to-tag guardrail added) + the six `base/sources/`
  pages retagged (Borsboom keeps `referential`). Resolved pages:
  [`decisions/resolved/result-status-upgrade-semantics`](decisions/resolved/result-status-upgrade-semantics.md),
  [`decisions/resolved/meaning-senses-methodology-tags`](decisions/resolved/meaning-senses-methodology-tags.md).
- ✅ **`updated:` date sweep.** The 7 pages P2 substantively touched (way-construction + 6 retagged
  sources) bumped to 2026-07-06. The spine (theory/claims) lag-scan found **no genuine
  update-box lags** — the two heuristic hits were citation/event dates in prose
  (`relational-order-sensitive-reassignment`'s "attempted 2026-06-20" narrative; a 1-day
  cxg-page citation), not lagging update boxes. Confirms auditor C's "low value" read.
- ✅ **`operationalizes: design/...` targets — BLESSED.** 11 findings pages carry an
  `operationalizes → design/<id>` link (senselint already tolerates it). Documented as a blessed
  exception in [`../CLAUDE.md`](../CLAUDE.md) (Typed links): a conjecture/result is operationalized
  by its frozen `experiments/designs/` design; all other typed-link targets stay in-wiki.
- ✅ **"pending Tom's review" grep-sweep.** Only one genuine straggler
  ([`conjecture/way-construction`](findings/conjectures/way-construction.md)'s tested-box) lacked a
  note — governance-noted s184. The other 14 hits already carry the s183 governance note/correction
  (indexical uses "Governance *correction*", which the s183 grep missed).
- Barwise & Perry 1983 wanted.md entry — **DONE s183** (the kratzer pointer now resolves).
- ✅ **linkify `--check`** re-verified clean at the P2 verification gate.
- ✅ **`homonym-meaning-dominance-norms` regraded** `scouting → verified` (its own blockquote
  records the norms fetched from OSF and used firsthand s94, licenses verified verbatim — matching
  the WordNet resource's `verified` grade); dated regrade note added.

## Ideas harvest — research seeds surfaced by the audit (P4 triages; do not silently drop)

**Tier 1 — strongest: cheap, on-mission, or directly unblocking (P4 should formalize the best
as open-questions/backlog items):**

1. **Frame-ablation instrument for A1b antonymy** (design input to the *queued* item): make the
   Justeson–Katz parallel contrastive frame the manipulated variable — antonymy recovery with
   the frame present vs structurally suppressed. *(sources: justeson-katz-1991 +
   cao-2025-distinctive-cooccurrence)*
2. **$0 cross-task per-model gate-clearance tabulation** — the descriptive table
   capability-split trigger (c) explicitly awaits; pure re-analysis. *(essay/capability-split)*
3. **Sense "wug-test" — regular-polysemy productivity on nonce nouns** (animal-for-meat,
   container-for-contents): productivity separates a stored sense list from a pattern; nothing
   in-repo tests lexical sense productivity. *(source/falkum-vicente-2015 + concept/polysemy)*
4. **RAW-C / SAW-C license scout** — a graded, usage-independent text-side sense-relatedness
   anchor; exactly the missing ingredient for a full-scope sense-gradience magnitude edition.
   *(multimodal-anchor-scouting §3)*
5. **Graded privativity probe** (*fake gun* suppresses 3/3, *toy violin* fails 3/3, *plastic
   apple* borderline → a gradient instrument anchorable to human typicality norms).
   *(monotonicity-c2-battery-v1)*
6. **Targeted quant×temporal AANN cell probe** — the one cell where every model inverts the
   human gradient ("a scant three days"); the reanalysis named the decider and nobody ran it.
   *(aann-temporal-why-reanalysis)*
7. **Heterogeneous (cross-family) dyads in the reference game** — claude-director ×
   gemini-matcher: if convention recovery degrades across families, coordination depended on the
   shared distributional substrate. *(source/zeng-2026 + the relational line)*
8. **Kratzer→origo discharge ($0 revision unit)** — the topic-situation vs utterance-situation
   seam sharpens the described-vs-occupied origo distinction; also cures the kratzer orphan.
   *(source/kratzer-2021-situations-sep)*
9. **Norm-instrument disagreement case study ($0)** — the two human word-balance norms disagree
   11/11 on shared words; a ready-made instrument-sensitivity object for the measurement track.
   *(homonym-meaning-dominance-norms, s94 note)*

**Tier 2 — good, needs a scout or a design decision first:** human-anchored scalar-implicature
divergence (van Tiel scalar-diversity / VAQUUM license scouts; the few→many split is
twice-observed); Bresnan & Ford 2010 per-item ratings scout (a human dative effect-*size*
anchor — concordant-verdict trigger (b)); preemption-vs-productivity probe (named on the
statistical-preemption theory page, never designed); coercion-under-depiction (the one unrun
prediction of the tested multimodal conjecture); frontier-panel replication of the Cao
six-relation battery (internal-contrast form); pair-level homonymy resource scout (the v3
discreteness test's missing ingredient); human order/path-sensitivity anchor scout (the
relational synthesis's IOU); cross-instrument jitter table (K≈5 re-runs on 2–3 instruments —
point-estimate trigger (b)); behavioral projectivity re-ranking of the SEP trigger taxonomy
(manner adverbs non-projective, *only* projects cleanly).

**Tier 3 — recorded textures and method seeds (cite when relevant; no unit owed):** gpt's
length-modulated givenness wrinkle (twice-reproduced, reported-not-read); measure-class-dependent
notional agreement (v5 vs v6 item-set tension); within-flavor modal-strength pair (deontic
must→may isolating strength from flavor); defeasance-vs-NLI-labeling disambiguation for the
cancel arms; frame-axis vs item-axis gradience cross-test; specific-referent effability
(description vs acquaintance — the regrade result's philosophical residue); THINGS
representational-alignment axis; elicitation-axes exhaustibility taxonomy (a new licit
terminator for witness searches); cross-model decorrelation as a frequency-confound
discriminator (the continuum closure's "unexploited avenue"); SemCor/OntoNotes over-/under-
splitting arm.

## Phase checklists

- **P2 `[x]` (s184)** — both decisions ratified ADOPT-A + applied; the Deferred list above cleared;
  agent links re-verified. Paired with the A1b antonymy design (the campaign rule permits sharing a
  session with an owed empirical unit). Next: **P3** (program B6 note-sweep + orphan cures).
- **P3 `[x]` (s185)** — program B6 note-sweep **done** (12 pages → `findings/notes/`, dir created;
  each a dated history-preserving reclassification box, no finding changed, sole-support guardrail
  clear; 4 finding-bearing borderlines kept as results); orphan cures done (kratzer/zeng
  re-confirmed linked; `barrie-tornberg-2025-data-leakage` ← [`source/ashery-2025-llm-conventions`](base/sources/ashery-2025-llm-conventions.md),
  `mahowald-2023-aann-judgments` ← [`conjecture/aann-construction`](findings/conjectures/aann-construction.md); `strasser-antonelli-nonmonotonic-logic-sep`
  left **peripheral** — its two-essay trigger-(d) tension is a finding-adjacent question for a future
  session, out of maintenance scope). Adversarial coherence pass **CLEAN (zero BLOCKERs)**. Paired
  with the A1b ratify + corpus scout. Next: **P4**.
- **P4** — concept on-ramp deepening (each of the 17 concepts points at the current findings
  bearing on it — polysemy/relational/constructional/multimodal-compositionality/grounding/
  inferential-meaning/deflationary done or partially done s183; the rest checked); ideas-harvest
  triage (Tier 1 → formed pages or backlog rows; Tiers 2–3 kept here with one-line dispositions).
- **P5** — spot re-audit (fresh agent, sampled pages incl. every s183-fixed BLOCKER); close this
  ledger with a dated summary; delete [`continue-prompt.md`](../continue-prompt.md) §5; log the closure.

## Ledger

| Date | Session | What happened |
|------|---------|---------------|
| 2026-07-06 | s185 | **P3 done** (program B6 note-sweep + orphan cures; paired with the A1b decision ratification + corpus scout). **12 result pages → `note`** (`type: note`, `status: recorded`), moved to `wiki/findings/notes/` (dir created): the build/feasibility gates (`forced-both-lexical-build-attempt-v1/v2`, `function-word-swap-build-v1`, `addarm-headroom-calibration-v1`, `monotonicity-c1-completion-calibration-v1`, `-generalization-b2-nogo-v1`, `-c2-privative-calibration-v1`), the two VWSD NL-baseline deferrals (`-audit-v1`, `-regrade-v1`), and the three $0 re-analyses (`cross-axis-lexical-constructional-ordering-v1`, `instrument-disagreement-reanalysis-v1`, `projection-trigger-inventory-family-decomposition-v1`). Each carries a dated reclassification box; **every measured value byte-identical** (coherence pass word-diffed all 12: only type/status/updated/box/links changed). Sole-support guardrail **clear** (no `claims/` page cites any of the 12). **4 finding-bearing borderlines kept as results** (conservative bias): `aann-temporal-why-reanalysis` (a $0 re-analysis, but human-anchored to Mahowald with a *new* model-vs-human divergence), `monotonicity-causative-progressive-cancel-v1` (measured suppression, not a buildability gate), `lexical-perceptual-grounding-moderation-v1` (human-anchored NULL), `function-word-few-many-split` (a new interpretive-mechanism finding). ~40 files' inbound links rewritten (`result/<id> → note/<id>` in front-matter targets, prose labels, and paths — incl. superseded theory v1, path-only). Orphan cures as in the P3 checklist above. **Adversarial coherence pass: CLEAN, zero BLOCKERs** (2 cosmetic NITs, no action). $0 (no model calls in P3). |
| 2026-07-06 | s184 | **P2 done** (paired with the A1b antonymy design). Both s183-opened decisions **ratified ADOPT-A** — fresh adversarial reviewer + one non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`) **converged on each** ($0.002774 for the two votes). *result-status-upgrade-semantics:* event-based transition rule documented in CLAUDE.md (mechanical-gate vs reading-bearing sort; `supported` lives on the claim layer for reading-bearing lines; gate pages may be created `supported`; status non-ranking/possibly-stale until normalized; theory draft→live deferred to next substantive touch) — **no result mass-edited, no theory flipped to `live`** (option A's no-mass-edit clause). *meaning-senses-methodology-tags:* `measurement-epistemic` tag added (broadened gloss + How-to-tag guardrail) + six `base/sources/` retags. Deferred-to-P2 remainder cleared: `operationalizes: design/<id>` **blessed** in CLAUDE.md; one pending-Tom straggler (way-construction) noted; `homonym-meaning-dominance-norms` regraded `scouting → verified`; 7 touched pages' `updated:` bumped; spine lag-scan found only citation-date false positives; linkify clean. $0.002774 (two ratification votes). |
| 2026-07-05 | s183 | Campaign opened (Tom-directed). Full six-slice audit (~370 pages, ~170 issues, 12 BLOCKERs); orchestrator fixed all BLOCKERs; five fix agents applied the batch tranche; exec-summary regenerated (B4 ticked); predictions.md completed; program.md reconciled; CLAUDE.md conventions corrected/documented; 2 decisions queued; this ledger + the continue-prompt §5 plan written. Fresh-agent adversarial coherence pass over the full diff → **SAFE-TO-LAND after patch** (1 BLOCKER — an invented meta-number in the regenerated exec summary — + 11 SHOULD-FIX + 12 NIT, **all applied**, including the NITs the reviewer offered to defer). $0. |
