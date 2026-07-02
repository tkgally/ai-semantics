---
id: program-2026-07-adoption
title: Adopt the 2026-07-02 external review's recommendations as the project's working program
status: resolved
opened: 2026-07-02
opened-by: special session (Tom-directed, unnumbered)
resolved: 2026-07-02
resolved-by: Tom (standing override — direct instruction, 2026-07-02)
resolution: "ADOPT the review's recommendation groups A–C as the standing program (wiki/program.md); Tom ruled the two charter-level items directly: website duty → one journal entry per JST calendar day (create-or-extend), clock-stamp mandate → dropped. Group D remains Tom-held levers, no action."
contingent-artifacts: []
---

# Decision: adopt the 2026-07 program (external review, session 165)

## Resolution (2026-07-02, Tom — standing override)

On 2026-07-02 Tom placed a comprehensive external review of the project's first 165 sessions
into the repository —
[`project-history/20260702-ai-semantics-review-by-fable.md`](../../../project-history/20260702-ai-semantics-review-by-fable.md),
written by a stronger model (Claude Fable) in a separate session — and directly instructed a
special (unnumbered, Tom-directed) session to implement its recommendations so that regular
Routine sessions can continue the work effectively. Under [`PROJECT.md`](../../../PROJECT.md) §12.3, Tom's standing
override outranks every autonomous procedure; this page records the ruling so no later session
re-litigates it.

**Adopted as the standing program** (distilled into [`../../program.md`](../../program.md), which
is now part of the cold-start reading path):

- **A. Empirical direction** — make shadow-depth a *measured* quantity (matched distributional
  controls; the shadow-depth table as flagship artifact); powered probes (~10× item counts on
  claim-carrying lines) and the deferred expensive runs instead of habitual micro-probes;
  re-anchor live lines to existing human datasets (presupposition first: CommitmentBank,
  MegaVeridicality, Tonhauser/Degen, NOPE — scout + license-check before adopting); add the
  scale/architecture axis; production-side probes; cross-linguistic replication.
- **B. Consolidation** — promote replicated results to claims via cross-session promotion
  reviews; clean second editions for the two changelog-shaped theory pages; merge redundant
  essay families and curate an ideas index; repair the reading surfaces (index slimmed to one
  line per page and now tool-generated, executive summary re-scoped as a checkpoint digest,
  home-page "latest" fixed, models.md truthed up); a visible prediction ledger
  ([`../../predictions.md`](../../predictions.md)); a `note` page type so "result" again means
  "a measurement".
- **C. Process** — prefer fewer, deeper sessions (larger bounded units); close the two founding
  open questions into the continuum theory page; an instrument stopping rule (≥3 redesigns
  yielding nulls on one construct → cross-session review before continuing); decorrelate the
  reviewer (route one vote of each ratification and pre-run critique through a non-Anthropic
  panel model).

**Ruled directly by Tom in this session** (the two items the review reserved for him, charter
§12.5 / review C2 & D1):

1. **Website duty: one journal entry per JST calendar day**, not per session. A session that
   lands substantive work (spend, or changes to findings/essays/theory/decisions) creates the
   day's entry if none exists, or extends it; pure-maintenance sessions skip the site. The
   home page carries the status box plus only the day's latest entry; the journal remains the
   full record. (Implementation note: Tom's ruling was "one entry per calendar day"; the JST
   day is used as the unit because the site's datelines are JST. Spend accounting stays keyed
   to UTC days, as before — the two are independent surfaces.)
2. **Clock-stamp mandate: dropped.** Journal entries carry the date and session number(s) only.
   `tools/session-clock.sh` remains available as an optional utility; the "protocol violation
   to skip" language is removed. (This reverses the 2026-06-30 stamp requirement — Tom's call
   on his own earlier instruction, made with the conflict explicitly surfaced to him.)

**Not adopted here (Tom-held levers, information only — review group D):** Routine cadence
(D1) is set outside the repo; the surprisal-lane API key (D2) and paywalled-resource ingestion
(D4) remain documented, dormant options (see
[`cloud-compute-path`](cloud-compute-path.md) and `wiki/base/wanted.md`); the panel/scaling
subject decisions (D3) were **queued, not decided** — three decision pages opened this session
for normal cross-session ratification (or Tom's ruling):
[`../open/scale-ladder-subjects.md`](../open/scale-ladder-subjects.md),
[`../open/panel-v2-refresh.md`](../open/panel-v2-refresh.md),
[`../open/logprob-supplementary-lane.md`](../open/logprob-supplementary-lane.md).

**Anti-cheat note.** This adoption changes *direction and process*, not findings: no verdict,
threshold, anchor, or result page is touched by it. Where a program item interacts with a
ratified decision (the logprob lane vs
[`aann-panel-logprob-blocker`](aann-panel-logprob-blocker.md); panel composition vs the
founding panel), the program routes through a **new, queued decision on changed premises** —
never a re-litigation of a closed gate. The modesty, anchor, freeze, and null-writing
disciplines are explicitly listed by the review (Part III) as not-to-change, and the program
page carries that list.

## What the special session changed (institutional implementation)

[`wiki/program.md`](../../program.md) (new standing layer); [`PROTOCOL.md`](../../../PROTOCOL.md) §1–§5b (reading path; §3 program
discipline; §4 probe sizing; non-Anthropic review vote; per-day website); [`CLAUDE.md`](../../../CLAUDE.md) and
[`continue-prompt.md`](../../../continue-prompt.md) aligned; `tools/build-index.py` (the index catalog is now generated, one
line per page — enforcing the 2026-06-18
[`wiki-frontmatter-ergonomics`](wiki-frontmatter-ergonomics.md) slimming intent);
`tools/senselint.py` (note type mapping); [`wiki/executive-summary.md`](../../executive-summary.md) relabeled a checkpoint
digest; [`config/models.md`](../../../config/models.md) truthed up; [`wiki/predictions.md`](../../predictions.md) seeded; `docs/` home-page
"latest" repaired and [`docs/README.md`](../../../docs/README.md) update rules rewritten; [`NEXT.md`](../../../NEXT.md) rebuilt around the
program. The review file moved to `project-history/`.
