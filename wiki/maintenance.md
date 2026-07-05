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
- **Two decisions queued** (ratifiable from s184):
  [`decisions/open/result-status-upgrade-semantics`](decisions/open/result-status-upgrade-semantics.md)
  and [`decisions/open/meaning-senses-methodology-tags`](decisions/open/meaning-senses-methodology-tags.md).
- **One number corrected from raw:** sense-gradience v1's two-annotator count is 152/200 (n≥3 =
  48), not 151; the v1 page and run README carry dated corrections (rep2's "(v1: 48/200)" was
  right).

## What was deliberately NOT changed (and why)

- **No mass retargeting of theory-v1 references.** Most are quote-provenance citations; the v1
  banners route readers; the edition-citation convention (now in CLAUDE.md) is the durable fix.
- **No essay merges** (standing s182 fence: the essay web is load-bearing; the additive
  [`ideas.md`](ideas.md) is the map).
- **No result-status flips.** The ~10 `supported`-at-creation result pages stand untouched
  pending the queued decision — normalizing them now would apply a default in the session that
  opened it.
- **No `anchor:` field normalization.** Two live value styles coexist (`human-anchored` ×5 —
  including the s175 flagship — vs `resource/<id>` ×14); both are readable, senselint accepts
  both; recorded here as benign variance.
- **Superseded pages' bodies byte-untouched** (banners verified correct).
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

## Deferred to P2 (the SHOULD-FIX remainder)

- Apply whichever option the two queued decisions ratify (per-page status-normalization notes;
  the meaning-senses tag change + vocabulary edit).
- `updated:` dates on a handful of spine pages whose newest in-page box postdates the field but
  which no s183 row touched (auditor C's truncated-NIT list; low value, zero risk).
- `operationalizes: design/...` front-matter targets point outside the wiki type system
  (senselint tolerates); decide whether to bless or rehome at the next senselint touch.
- The remaining "pending Tom's review" archaisms inside old status boxes of pages no fix row
  touched (way/conative conjecture boxes were fixed; a final grep-sweep at P2 catches stragglers).
- Barwise & Perry 1983 wanted.md entry (kratzer source points at a nonexistent entry) — being
  handled by fix agent 3; verify landed, else do at P2.
- Spot-check that every fix agent's inserted relative link survives `linkify --check` (P1 exit
  gate re-runs it; re-verify at P2 cold-start).
- `homonym-meaning-dominance-norms` front-matter now reads `status: scouting` (the F27 vocabulary
  normalization) while its body records the data fetched + used firsthand (s94) — a one-word
  status re-grade (`catalogued` or `verified`) is plausibly owed; decide at P2 with the page open.

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

- **P2** — ratify + apply the two decisions; the Deferred list above; re-verify agent links.
- **P3** — program B6 note-sweep (~10 pages; create `findings/notes/`); orphan cures
  (kratzer/zeng verified linked; any remaining zero-inbound sources listed then linked or
  marked peripheral).
- **P4** — concept on-ramp deepening (each of the 17 concepts points at the current findings
  bearing on it — polysemy/relational/constructional/multimodal-compositionality/grounding/
  inferential-meaning/deflationary done or partially done s183; the rest checked); ideas-harvest
  triage (Tier 1 → formed pages or backlog rows; Tiers 2–3 kept here with one-line dispositions).
- **P5** — spot re-audit (fresh agent, sampled pages incl. every s183-fixed BLOCKER); close this
  ledger with a dated summary; delete [`continue-prompt.md`](../continue-prompt.md) §5; log the closure.

## Ledger

| Date | Session | What happened |
|------|---------|---------------|
| 2026-07-05 | s183 | Campaign opened (Tom-directed). Full six-slice audit (~370 pages, ~170 issues, 12 BLOCKERs); orchestrator fixed all BLOCKERs; five fix agents applied the batch tranche; exec-summary regenerated (B4 ticked); predictions.md completed; program.md reconciled; CLAUDE.md conventions corrected/documented; 2 decisions queued; this ledger + the continue-prompt §5 plan written. $0. |
