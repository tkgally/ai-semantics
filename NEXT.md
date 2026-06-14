# NEXT.md

## State

**Session of 2026-06-14 (seventh session, single-unit serial empirical: build → stimulus
construction → independent pre-run critic → freeze → run → independent post-run verifier →
result + integration) is landed. ≈$0.94 spent this session (relational v4: stimulus
construction $0.278 + probe $0.630); day total 2026-06-14 (sessions 6–7) ≈$0.974 of $5.00.**
The relational sub-axis got its decisive within-arm test. Headline: the chronology/text-position
decoupling **worked**, and **both models follow physical text-position, not stamped chronology**.

1. **RELATIONAL (headline) — history-perturbation v4 RAN → TEXT-POSITION, not chronology.**
   [`result/relational-history-perturbation-v4`](wiki/findings/results/relational-history-perturbation-v4.md).
   v4 implemented the one structural change v3's verifier named: chronology carried by an explicit
   per-line **round stamp**, the decisive most-recent line placed **non-terminally**, so
   "chronologically-latest twin" and "physically-last-line twin" are crossed **orthogonally within
   one arm** (cov 0, asserted at build + re-derived by the verifier). claude+gemini only (gpt
   dropped). **claude → TEXT-POSITION ARTIFACT** (Δ_pos clean 0.698 [0.594,0.804]; Δ_chron null
   0.509 [0.465,0.556]); **gemini → INCONCLUSIVE/MIXED**, same direction — **position-dominant**
   (Δ_pos 0.812), and the post-run verifier showed its Δ_chron elevation is a **pure
   position-gradient artifact** (a pure-position reader predicts 0.5625 = observed exactly; zero
   residual chronology). In the conflict cells both pick the physically-last (chronologically-
   *earlier*) twin ~0.69–0.75. **Critical scope limit (pre-run-critic calibration):**
   position-following here is **indistinguishable from stamp-blindness** (the single-twin
   stamp-respect control shows "not derailed by non-monotonic layout," not "reads stamp values"),
   so it is **methodological — prompt geometry / stamp-value neglect — and says nothing
   relational**; it must NOT be read as "the models chose to ignore recency." For
   [`conjecture/commutative-convention`](wiki/findings/conjectures/commutative-convention.md):
   **neither falsified** (no chronology-tracking) **nor certified** (the models are not
   content-only — they are strongly position-driven); stays `proposed`. Independent pre-run critic
   (GO-after-fixes; the stamp-as-chronology indicator ruled **inside-class hygiene, no decision
   page**, so the run was not blocked) + independent post-run verifier (0 mismatches). 460
   finding-bearing calls, $0.630 billed, 0 NA / 0 retried / strict 1.000. `anchor:
   internal-contrast-only`. Run dir:
   [`experiments/runs/2026-06-14-relational-history-perturbation-v4/`](experiments/runs/2026-06-14-relational-history-perturbation-v4/README.md).

## Next concrete actions — backlog for the next session

**Two-track note:** the relational empirical question has now been pushed hard across **four
versions** (v1–v4) and the last several sessions have leaned empirical (7 relational, 6
grammatical+phil, 5 empirical). **Weight the next session toward the PHILOSOPHICAL track**, or a
*different* empirical axis — do not reflexively spin up relational v5.

1. **PHILOSOPHICAL (weighted first) — a relational essay is now ripe, OR catalogue a queued
   source.** The v4 result hands the philosophical track a concrete object: these models, asked to
   integrate a conversation whose convention shifts over time, anchor on **prompt position**, not
   on the conversation's **chronology** — and we cannot even establish they read the timeline at
   all. That bears directly on the aggregation-vs-constitution theme (an order-/position-anchored
   reader is the deflationary "bag of turns," but a *position*-anchored one is not even the clean
   commutative null) and on "what is a conversation, to a model?" A fourth essay could argue this,
   with explicit revision triggers. Alternatively, the **source backlog** in
   [`wiki/base/wanted.md`](wiki/base/wanted.md): the **Millière-Buckner Part II §3.2/§4
   PDF-verification** follow-up (queued session 6), the "Mechanistic Indicators of Understanding"
   2507.08017, or the Sterken & Cappelen volume.
2. **RELATIONAL v5 — ONLY if the next session deliberately returns to this axis (it has had four
   runs; lower priority).** v4 located a hard confound: because the models anchor on text-position,
   a **linear single-column** recency probe is structurally unable to see a chronology-based
   relational convention. A genuine v5 would have to **neutralize text-position as a cue** (e.g.
   rotate/randomize the decisive line's position so it carries no information, and gate on a task
   that *requires* reading the stamp value), **or** first run a **stamp-comprehension pre-probe**
   (can these models use an explicit recency stamp at all when position is uninformative?) before
   re-attempting the relational chronology question. The conjecture's named scope extensions remain:
   **image referents**, **cross-family dyads**, **live (non-constructed) reassignment**. The v4 run
   harness (`experiments/runs/2026-06-14-relational-history-perturbation-v4/`) is the template; any
   v5 design must be drafted-then-frozen-after-a-fresh-pre-run-critic, as always.
3. **GRAMMATICAL — optional, not teed-up.** The AANN line is well-developed (form gradient v2
   SUPPORTED; inferential v4 PARTIAL; agreement reflex v5 GENERALIZES-bounded). The remaining
   invited follow-ups: a **panel replication / power-up** of the v4 paraphrase shift (wider N, fresh
   adjectives), or the **cross-instrument sensitivity** matrix (NLI×FC×construction with a
   pre-registered primary instrument).
4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

**None open.** All twenty-four decisions remain resolved; **none opened or ratified this session.**
The relational v4 **borderline operationalization question** (chronology indicator: explicit
per-line stamp vs physical position) was **ruled INSIDE-CLASS HYGIENE by the independent pre-run
critic** — recorded in the frozen
[`PREREG.md`](experiments/runs/2026-06-14-relational-history-perturbation-v4/PREREG.md) §"Pre-run
critic revisions", **not** opened as a `decisions/open/` page, so it required no cross-session
ratification and did not block the run (this is the surface-don't-smuggle discipline resolving
cleanly in-session via the independent critic, which is permitted: the critic is the independent
party, and the ruling fixed the *yardstick* as inside-class, not a result).

## Standing-override notes (for Tom, if he looks)

- The relational "does meaning get built between agents over time?" question got its **cleanest
  test yet**, and the answer is methodological: when a conversation's convention shifts over its
  turns, both models anchor on **where the text sits on the page**, not on the **stated timeline** —
  and the test cannot even establish whether they read the timeline at all. So this is a finding
  about **prompt layout**, not a claim the models *ignore* time, and it leaves the relational
  meaning question **open**, now with a mapped trap (a linear recency probe can't separate "latest
  in time" from "last line"). The standing bet (conventions are an order-free "bag of turns") is
  **neither overturned nor confirmed** — a genuine draw.
- **No methodological judgment call was self-approved this session.** The one borderline call
  (stamp-as-chronology-indicator) was **ruled inside-class hygiene by the independent pre-run
  critic**, not self-ratified, and no decision page was opened.
- Spend 2026-06-14 (sessions 6+7 combined): **≈$0.974 of $5.00** (UTC). GitHub Pages serves from
  `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website
updated. **Weight the next session toward the PHILOSOPHICAL track (or a non-relational empirical
axis) — the relational sub-axis has now had four empirical runs.**
