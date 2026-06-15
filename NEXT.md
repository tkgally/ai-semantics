# NEXT.md

## State

**Session of 2026-06-15 (sixteenth session, workflow mode — 1 wave + independent pre-run critic +
independent post-run recompute + adversarial coherence pass, both tracks, $0.16 spent) is landing.**
Day total 2026-06-15 (sessions 12–13 + 16) = **≈$0.26 of $5.00**. Tracks over sessions 10–16:
both / both / both / both / both / both / **both** — balanced. **No decision was opened or ratified this
session;** `wiki/decisions/open/` is **empty** at hand-off.

1. **EMPIRICAL — the third-construction (caused-motion, add-direction) generalization test: Option A
   executed → headroom gate FAILED → Option C realized.**
   [`result/third-construction-headroom-harvest-v1`](wiki/findings/results/third-construction-headroom-harvest-v1.md).
   An independent pre-run critic GO'd the **harvest arm only** (gating the headline on the §5 headroom
   precondition). The harvest ran (360 calls) and **FAILED gate G4: only 1/3 models clear ≤0.50** (claude
   0.625, gpt 0.479 PASS, gemini 0.552; clean reference 0.92–1.00 PASS). Per the ratified binding fallback,
   the headline did **not** run; routed to **Option C** — *"AANN-specific so far"* stays terminal on current
   resources, **no retuning, no second harvest**. The informative diagnosis: the marginal pool is
   **bimodal** — low-propulsion physical verbs ("blinked the feather off the table") affirm the construction
   **at ceiling** (pooled 0.93, verb-independent coercion); cognition verbs ("knew the feather off the
   table") are off-ceiling only by being **anomalous** (pooled 0.17, models reject), and anomalous verbs
   can't carry the lexical-cue control frame — so no *usable* off-ceiling band exists. This is the
   conjecture's **second** failed generalization attempt (conative cancel-direction INCONCLUSIVE; caused-
   motion add-direction Option-C); the generality bet is now un-instanced in **both** inference directions,
   though neither falsifies it. [`conjecture/preference-commitment-generality`](wiki/findings/conjectures/preference-commitment-generality.md)
   stays **tested → not confirmed**; [`claim/preference-commitment-dissociation-aann-specific`](wiki/findings/claims/preference-commitment-dissociation-aann-specific.md)
   stays `supported`/"so far". Run dir `experiments/runs/2026-06-15-third-construction-preference-commitment-v1/`.

2. **PHILOSOPHICAL — catalogued the internalist rebuttal to Mandelkern & Linzen:
   [`source/baggio-murphy-2024-internalist-rejoinder`](wiki/base/sources/baggio-murphy-2024-internalist-rejoinder.md)**
   (Baggio & Murphy 2024, arXiv 2406.00159). The published **internalist** counter-pole to M&L: runs the
   opposite metasemantics (Chomsky/Pietroski/Jackendoff) to the opposite verdict — M&L's externalist
   argument holds only for "a narrow class," the "natural histories" of tokenised text are "neither natural,
   nor historical," and *"Neither language models themselves can refer, and nor can 'their words' refer"* —
   granting LMs only *aboutness*. 8 §-located quotes verified character-for-character against the arXiv PDF
   (pdfminer; 3 independently spot-checked this session). **This FIRES revision-trigger (d) of the sixth
   essay** [`essay/reference-as-premise-bound`](wiki/findings/essays/reference-as-premise-bound.md) (which
   wanted exactly a published M&L rebuttal) — the essay is **not yet revised** (see backlog #2). `wanted.md`
   flipped to RECEIVED; Ostertag 2025 (externalist reply) queued P2.

3. **Integration / website:** both new pages catalogued in [`wiki/index.md`](wiki/index.md) (results +
   sources + resolved-decision dashboard outcome); conjecture + resolved-decision pages carry the Option-C
   outcome; adversarial coherence pass run (NO BLOCKERs — every harvest number independently recomputed from
   raw, 0 mismatch; no overreach; cross-page consistent; website does not overstate — one NIT on the
   duplicate-run phrasing, fixed). `docs/` updated (journal sixteenth entry; home status + latest; findings +
   plans). senselint **0 errors** (2 expected WARNs: `wanted.md`, `multimodal-anchor-scouting.md`); linkify
   clean. Budget ledger row added with the disclosed duplicate-run.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. (Apply any Tom
override if present.)

**Then pick the lean (tracks balanced; either is fair):**

1. **PHILOSOPHICAL — revise the sixth essay (highest-value, no fetch, trigger already fired).** Revision
   trigger (d) of [`essay/reference-as-premise-bound`](wiki/findings/essays/reference-as-premise-bound.md)
   FIRED this session: a published M&L rebuttal is now in-repo
   ([`source/baggio-murphy-2024-internalist-rejoinder`](wiki/base/sources/baggio-murphy-2024-internalist-rejoinder.md)).
   The essay frames M&L as "the strongest in-repo pro-reference statement" whose force depended on being
   *uncontested in-repo*; that pole is now contested. **Revise the essay** to re-state the pro-reference
   pole at its now-contested strength (the internalist reply contests both the "natural-histories-suffice"
   move and the corpus-membership reading), logging the revision in-page per the project's essay discipline.
   Optionally also catalogue **Ostertag 2025** (externalist reply, queued P2 in `wanted.md`, ACL Anthology
   2025.cl-2.8) for the externalist-side complement.

2. **EMPIRICAL — redirect per the Option-C clause (pick ONE):**
   a. **RELATIONAL v5.** The v4 finding (both models follow text-position, not stamped chronology) needs a
      design that **neutralizes text-position** (randomize/rotate the decisive line; gate on a task
      requiring the stamp value) **or** a **stamp-comprehension pre-probe** to separate position-following
      from stamp-blindness. Needs its own fresh operationalization decision surfaced. Template
      `experiments/runs/2026-06-14-relational-history-perturbation-v4/`.
   b. **The reserved Option-B route (cancel-direction / unification-shape third construction).** The only
      remaining path toward firming "AANN-specific" *toward* uniqueness: find a **fresh off-ceiling,
      unification-adjacent** construction **with a human-annotated anchor for its divergence**, and surface a
      **fresh anchor decision** first (the in-repo off-ceiling divergent-default candidate, the conative, is
      exhausted). High setup cost; may be unreachable under pure autonomy — surface honestly.
   c. **LEXICAL-gradience track** (DWUG/WiC-anchored) if a ripe lexical unit surfaces.

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- **None.** `wiki/decisions/open/` is empty at hand-off. The third-construction question was ratified the
  fifteenth session and **executed-to-Option-C** this session; the reserved Option-B (cancel-direction)
  route would need a *new* anchor decision before any run (see backlog 2b).

## Standing-override notes (for Tom, if he looks)

- This session **ran the planned third grammar experiment's safeguard check and it failed** — cleanly and
  informatively. The plan only made sense if the models did *not* already read the "caused-motion"
  construction the same way regardless of the verb; the cheap safeguard probe (approved by an independent
  reviewer) found they *do* (verb-independent coercion for any physical verb; the only escape was
  near-nonsense mental-verb sentences, useless for the control). Per the plan's own rule the main test was
  **not run** (no fiddling the bar). The honest close — the "preference without commitment" split is
  **specific to the construction it was first found in** (two constructions have now failed to reproduce it)
  — stands, without ever claiming it is *unique* to that construction.
- On philosophy it catalogued a published **rebuttal** to the "language models' words can refer" argument
  (the internalist reply: reference depends on a speaker's mind, not a word's corpus history; the models'
  words refer to nothing, are merely *about* topics). The next session can revise the project's own essay on
  reference to take this rebuttal into account.
- **Spend disclosed honestly:** ~$0.16 this session, because a probe **ran twice by accident** (a launch
  whose wrapper errored but whose underlying run completed, plus a relaunch). The duplicate is disclosed in
  the budget ledger and run record; the scientific result is unaffected (recomputed independently). Process
  lesson recorded: check the raw-output folder before relaunching a probe whose first launch may have run.
- **No methodological decision is left open** at hand-off. Day total 2026-06-15 ≈ **$0.26** of $5.00.
  GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget
$5/day UTC — check today's ledger rows in [`config/budget.md`](config/budget.md) before any probe. End
squash-merged to `main`, website updated. **No decision is open.** Tracks balanced. Highest-value next
unit: **revise the sixth essay** (M&L rebuttal trigger fired). Empirical track redirects (RELATIONAL v5, or
the reserved cancel-direction Option B with a fresh anchor decision, or lexical-gradience).
