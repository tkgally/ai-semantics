# PROTOCOL.md — per-run discipline

This is the script every run follows. Charter: `PROJECT.md` §7 + §12. Conventions: `CLAUDE.md`. Session entry point: `continue-prompt.md`. Standing program: `wiki/program.md`.

Every run is an independent cloud session with a fresh context and a fresh clone of the default branch. **All continuity lives in the repo.** Unmerged work is invisible to the next run.

**The project runs autonomously (charter §12, ratified 2026-06-12).** No step below waits for a human. Tom monitors via the public site and holds a standing override; if any file shows an edit or instruction from him, it outranks this protocol and is applied first.

## 0. Run modes

There are two modes. **The default for every autonomous session (any session started from `continue-prompt.md`) is workflow mode.** Single-unit mode is the fallback for small, surgical, or maintenance tasks — when the session's one remaining duty is to land unmerged work, or when the best move is one deep unit (a powered probe with its gates) that parallel generation would not help (§3).

- **Workflow mode (default).** A multiagent dynamic workflow: an orchestrator plans a *wave* of independent bounded units, fans them out to parallel subagents, runs an adversarial coherence/refutation pass over their combined output, integrates the shared files itself, and verifies. Default 2–3 waves; if an explicit time budget was given, loop waves until the deadline. See §A.
- **Single-unit mode (fallback).** Take the one next bounded unit from `NEXT.md`, do it, verify, commit, merge. Use this when one specific surgical thing is needed (a stale PR to land, a defect to fix), or when the work is inherently serial. See §B.

Both modes obey the same non-negotiables (§1, §2, §5, §6) and the same charter gates. Workflow mode does **not** relax the gates, the human-anchor discipline, the no-fabrication rule, or the "surface decisions, don't auto-resolve them" rule. It parallelizes *generation*, not *judgement*.

## 1. Read (cold start) — both modes

Read, in order:

1. `NEXT.md` — state, the next action(s), what is blocked.
2. `wiki/program.md` — the standing program (adopted 2026-07-02). Unit selection is
   program-guided: prefer units that advance an open program item.
3. `wiki/index.md` — the catalog, one line per page, tool-generated. Scan or grep the
   sections the next action needs; do not read individual pages until you know which ones
   you need, and never hand-edit the generated catalog (`tools/build-index.py` owns it).
4. `wiki/decisions/open/` — list filenames; read only those that touch the next action.
5. Selectively read the pages the next action depends on (the `links:` graph is your guide).

Do not load the whole wiki. Re-ground in `PROJECT.md` only when the unit feels off-charter.
(`tools/session-clock.sh` is optional since 2026-07-02 — run it at start only if you want a
duration figure later; nothing requires it.)

## 2. Reconcile decisions — both modes

Governance: cross-session autonomous ratification (charter §12.3; ratified in
[`decisions/resolved/autonomous-era-governance`](wiki/decisions/resolved/autonomous-era-governance.md)).

For each file in `wiki/decisions/open/`:

1. **Tom-override check first.** If Tom has added a `resolution:` block, moved the file, or left
   any instruction touching it, apply his ruling exactly as under the old protocol — his word
   outranks everything below.
2. **Cross-session ratification.** If the decision was opened in an **earlier session** (it is
   never ratifiable in the session that opened it), it is eligible. To ratify: launch an
   **independent adversarial-review agent** that reads the decision page, its options, the
   provisional default, and every downstream contingent artifact, and returns a verdict with
   rationale (adopt the default / adopt another option / keep open with what's missing). Apply the
   verdict: move the page to `wiki/decisions/resolved/` with date, `resolved-by: autonomous
   (adversarial review)`, and the written rationale; then promote or retire the contingent pages
   exactly as under the old rule.
3. **Otherwise leave it open** and carry it in `NEXT.md`.

Two hard limits: the reviewer must be a **fresh agent**, not the orchestrator that did the
downstream work this session; and ratification fixes the **yardstick, never the result** — if the
review is motivated by wanting a different result, that is the anti-cheat violation, stop.

**Decorrelate the review (adopted 2026-07-02, program C5).** Independence of *role* is not
independence of *model*: route one vote of each adversarial ratification through a
**non-Anthropic panel model** (`config/models.md`, with the cutoff-aware preamble) alongside
the fresh-agent reviewer. The panel vote is QA input to the fresh agent's verdict —
convergence is comfort, divergence is signal to weigh in the written rationale. If the call
fails or today's budget bars it, record that in the resolution and proceed with the fresh
agent alone; never block a ratification on infrastructure.

**Never ratify a decision in the session that opened it.** Surfacing and ratifying must be
separated by at least one session boundary.

## 3. Program discipline — both modes (adopted 2026-07-02, [`program-2026-07-adoption`](wiki/decisions/resolved/program-2026-07-adoption.md))

- **Program-guided selection.** Bounded units come from `NEXT.md` and the open items in
  `wiki/program.md`. Prefer fewer, deeper units — one powered probe over several micro-probes,
  one consolidation done properly over three touch-ups. A session that finds nothing
  substantive owed does a light check (reconcile decisions, verify, hand off) and stops:
  padding a session to look productive is the defect, not the short session.
- **Claims promotion.** When a result line has replicated (fresh items or a second run) and
  survived its controls, queue a **promotion review**: a cross-session, independent,
  adversarial pass (same independence rules as §2, including the non-Anthropic vote) whose
  output is a `claim` page citing the results, anchors, and magnitudes with intervals — or a
  written refusal. The claims layer is the charter's compounding unit; a result that never
  promotes (or fails its review) stays a result.
- **Theory-edition rule.** More than ~3 update boxes on a `theory` page forces a clean second
  edition at the next touch: rewrite the current position, archive the old page under a
  `supersedes` link, keep history visible. Theory pages are *rewritten* by evidence, not
  accreted onto.
- **Essay bar.** A new `essay` requires a fired revision trigger, genuinely new outside
  literature, or a new falsifiable bet; otherwise the move is an in-page revision of the
  existing essay. (Merging a redundant essay family is consolidation, not a new essay.)
- **Instrument stopping rule.** After **3 instrument redesigns yielding nulls on one
  construct**, a further redesign requires a cross-session review that weighs the line against
  alternatives (the witness-seeking-economics discipline, mirrored). Each redesign may be
  individually justified; the *sequence* needs a governor.
- **Prediction ledger.** Registering any bet (conjecture confirm/falsify criteria, essay
  revision triggers, theory predicts/forbids) adds a row to `wiki/predictions.md`; any firing,
  discharge, or retirement updates the row in the same session. Never retro-fit a row.

## 4. Probe sizing and spend — both modes (adopted 2026-07-02)

- **Power before spend-fear.** A probe whose verdict will carry a claim uses **~100–150
  items** where the instrument permits (~10× the founding-era micro-N; at observed prices
  still ≲$1). Micro-N (~12 scenarios) remains right for pilots, calibrations, and gates — not
  for claim-carrying verdicts. State the chosen N, and why, in the design.
- **The cap is a ceiling, not a target — but chronic under-use is a defect.** Before designing
  another micro-probe, check the program's deferred expensive runs (grounding magnitude,
  powered re-runs): one informative $3 run beats ten $0.03 probes re-confirming known
  directions. The single-run prudence flag stays (prefer-split above ~$2.50/run); pre-flight
  estimates and post-run actuals stay mandatory (`config/budget.md`).

---

## §A. Workflow mode

### A1. Plan a wave

From `NEXT.md` and the open items in `wiki/program.md`, plus the open conjectures/open-questions/stubs, assemble a **backlog of independent bounded units** — pieces that touch disjoint files and don't depend on each other's output within the wave. Good units: write a claim/conjecture/theory/essay page; fill a concept stub; deepen a source's provenance; build or extend a tool; design or run a probe. **Draw from both tracks** (charter §12.1): a healthy session usually carries at least one empirical and one philosophical unit, but follow the backlog's actual priorities rather than forcing symmetry every time. Pick 2–4 deeper units for the wave (§3: prefer fewer, deeper; six shallow units is the old failure mode).

Two hard constraints on unit independence:
- **Disjoint writes.** Each subagent creates/edits its *own* files. No two subagents touch the same file. The orchestrator alone edits the shared files (`wiki/index.md`, `NEXT.md`, `log.md`) — never a subagent.
- **No intra-wave dependencies.** If unit B needs unit A's output, they go in different waves.

### A2. Fan out

Launch the wave's subagents in parallel. Every subagent prompt must carry the **house rules**:
- Read `CLAUDE.md`, `PROTOCOL.md` §5, `wiki/meaning-senses.md`, `wiki/index.md`, and the specific dependency pages — first.
- Create only the named new files; do **not** edit `wiki/index.md`, `NEXT.md`, `log.md`, `CLAUDE.md`, `PROTOCOL.md`, `PROJECT.md`, or any file outside the assignment.
- Use only exact, verifiable quotes with provenance. **Never fabricate a quote, page number, or human-annotated resource.** If a fetch fails, report it honestly and change nothing fabricated.
- Respect anchor discipline: a claim/result needs an `anchors:` link to a resource, or `anchor: pending` + a queued `wiki/decisions/open/` entry. Never invent an anchor.
- Keep anything in `contingent-on:` in provisional language.
- Write cross-references as clickable relative links per `CLAUDE.md §Cross-references` (or leave plain and let `linkify.py` normalize at integration).
- Return: files created, ids, links, any anchor/decision gaps, and any quote whose provenance is weaker than page-level.

### A3. Adversarial coherence pass

Launch at least one **read-only** refutation agent over the wave's combined output (it reports defects; it does **not** edit, to avoid racing the orchestrator's integration writes). It checks: duplication/overlap between new pages; contradictions; contingent-language overreach; link-relation correctness; quote integrity (locators present); sense-tag sanity. It returns a prioritized fix-list (BLOCKER / SHOULD-FIX / NIT).

For experiment designs, the independent **pre-run critic** likewise routes one vote through a
non-Anthropic panel model (§2 decorrelation rule; cutoff-aware preamble). The panel vote is QA
input — GO/NO-GO authority stays with the fresh-agent critic, and any divergence is weighed in
writing. If the call fails or budget bars it, record that and proceed.

### A4. Integrate (orchestrator only)

Apply the fix-list. Then update the shared files: add every new page to `wiki/index.md`; do not touch `NEXT.md`/`log.md` yet if more waves are coming (update them only at wind-up, §7). Run the verification gates (§5). Fix or queue anything that fails.

### A5. Checkpoint and loop

**Commit each wave** before starting the next (`git add -A && git commit`). This makes the work durable if the session is interrupted — a half-finished continuous run should never lose completed waves.

Then decide whether to continue:
- If an explicit end time was given, plan the next wave (A1) — **refill the backlog** with newly-tractable units (a wave often unblocks the next: a filled stub lets a dependent conjecture proceed; a new claim invites its experiment design). Continuous runs end at the *clock*, not when the first backlog empties.
- **Default for autonomous sessions (no stated end time): run 2–3 waves**, then wind up. Enough to land real work; small enough that everything gets integrated, verified, and merged with room to spare. Prefer fewer, deeper units over filler.
- Stop early regardless if: the backlog has no unit whose human anchor is in-repo or queueable; or the day's OpenRouter budget is spent and only spend-bearing units remain; or you would have to fabricate to proceed.

Watch the token budget: a coherence pass is the expensive part of each wave. Note approximate subagent token use per wave in the wind-up for calibration.

---

## §B. Single-unit mode (fallback)

Take the single next bounded unit named in `NEXT.md`. It must fit comfortably in one context window. If it does not, split it: write the split back into `NEXT.md` as numbered subunits, do unit 1, and hand off.

If `NEXT.md` is empty or stale, do not invent ambitious work. Pick the most tractable open conjecture or open question whose human anchor is in-repo, and proceed.

**Even a single-unit session ends with the full wind-up** (§5–§7): verify, do the website duty if owed (§5b), commit, merge, hand off.

**Two failure modes to watch (both modes, but easy to slip into here):**
- **Quietly tuning the operationalization until a null becomes positive.** If you find yourself adjusting the indicator after seeing results, stop — that is an operationalization gate (§8 charter). Queue it.
- **Citing a resource by existence, not by content.** A cited resource page must show the specific feature/annotation that bears on the claim.

---

## 5. Verify (before every commit) — both modes

Run, in order:

1. **build-index** — `python3 tools/build-index.py` regenerates the `wiki/index.md` catalog
   from page front-matter (one line per page), so new/renamed/retyped pages self-register.
   Never hand-edit between its markers; hand-edit only the header above them.
2. **senselint** — `python3 tools/senselint.py` must report **0 errors**. This mechanically checks front-matter, meaning-senses vocabulary, typed-link relations + target resolution, anchor discipline, index coverage, and inline-link integrity. WARNs/INFOs are reviewed by hand (the `wanted.md` front-matter WARN and contingent-page INFOs are expected).
3. **linkify** — `python3 tools/linkify.py` (then `--check` to confirm 0 remaining). Cross-references should be clickable relative links to existing pages.
4. **provenance** — every new claim/result cites at least one in-repo `source`/`resource` page that actually bears on it; exact quotes match the source page's verbatim content.
5. **human-anchor** — every empirical claim about LLM meaning has an `anchors:` link to a `resource`, OR a queued `wiki/decisions/open/` entry.
6. **website-consistency** (by hand) — nothing on the public site states a finding more strongly than the corresponding wiki page; the day's journal entry reports this session's decisions/ratifications (§5b).

If any check fails, fix or queue (do not commit-and-promise-to-fix).

## 5b. Update the public website — one journal entry per day (amended 2026-07-02, Tom)

The site carries **one journal entry per JST calendar day**, not one per session
([`program-2026-07-adoption`](wiki/decisions/resolved/program-2026-07-adoption.md); this
replaces the per-session duty and the clock-stamp mandate of 2026-06-30). The duty falls on
every session that **lands substantive work** — spend, or changes to findings / essays /
theory / decisions. A session that lands only maintenance (or defers) skips the site
entirely; its record is `log.md`.

Before the final commit of a substantive session, update `docs/` (plain-language,
glossary-linked, no repo links, no reference to the human monitor — charter §12.5 and
`docs/README.md`):

1. **Create or extend today's journal entry** (`docs/journal.html`). If no entry exists for
   today's JST date, prepend one covering this session; if one exists, extend it so the day's
   entry covers all of the day's landed sessions (rework the summary line and pills, add or
   fold in a paragraph, update the day's spend). Dateline format:
   `Month D, YYYY (session N)` or `(sessions N–M)` — session numbers as numerals, **no clock
   times or durations** (mandate dropped 2026-07-02; earlier entries keep their stamps — do
   not revise them). Any autonomous ratifications must appear in the day's entry (Ruling 1).
2. **Refresh the home page** (`docs/index.html`): the status box (last-updated date + latest
   session number, current focus, spending posture) and **"The latest"**, which holds only
   the day's entry (replace it; the journal is the full record — never let a feed accrete
   there again).
3. **Touch the pages the session's work changed:** findings → `docs/findings.html`;
   plans/ideas → `docs/plans.html`; any new technical term used on the site → define it in
   `docs/glossary.html`.

**Gotcha (unchanged):** the site's JST dateline can differ from the **UTC budget day** in
`config/budget.md` — JST is UTC+9. Date the site in JST; track spend in UTC; never conflate
the two.

## 6. Commit, push, PR, and squash-merge to main — both modes

```
git add -A
git commit -m "<short imperative summary>

<longer body referencing the unit(s) + any decisions queued/ratified>"
git push -u origin <branch>
```

Then, via the GitHub MCP tools: open a PR (ready for review, not draft) if none exists for the
branch, and **squash-merge it to `main`** (`merge_pull_request`, method `squash`). Confirm `main`
advanced. This is mandatory (charter §12.4): the next run clones `main` fresh, and the website
deploys from `main` — unmerged work is invisible and will be redone.

If the merge fails for a transient reason, retry with backoff; if it still fails, leave the PR
open and put **"land PR #N first"** at the very top of `NEXT.md`.

In workflow mode, each wave is its own commit (§A5); the final commit carries the integration,
the website update, and the handoff.

## 6b. Running long commands & waiting — both modes

Probes and certification runs (`probe.py full`, `certify.py run`) take minutes. How you wait on
them is a known foot-gun in this cloud environment — get it wrong and the session spins forever
(this happened: an `until ! pgrep -f "probe.py full"; do sleep 3; done` loop that never exited,
left a runaway background task alive, and stranded uncommitted work between Routine invocations).

1. **Never detect completion by name-match.** Do **not** use `pgrep -f`/`pkill -f` on a command
   substring (or any string that could appear in the session's own command history). The `claude`
   launcher carries the *entire* replayed conversation — including your own command text — in its
   argv, so a substring match hits the launcher itself and the condition never clears.
2. **Prefer not to hand-roll a wait at all.** Launch any long-running command with the harness's
   `run_in_background: true` and rely on the automatic completion notification plus its output
   file. That runs the probe in one step, with no loop to leak.
3. **If you genuinely must wait on a process, wait on its exact PID — never a name.** Launch as
   `cmd & pid=$!` and `wait "$pid"` in the same shell, or poll `kill -0 "$pid"` on that captured
   pid; **or** have the command drop a sentinel on completion (`cmd; touch .done`) and poll for
   the *file* with the Monitor tool. Bare chained `sleep` as a wait stays forbidden.
4. **Defense in depth.** Any unavoidable polling loop must be bounded by a max-iteration or
   wall-clock deadline so it can never spin forever, and must exit non-zero / report when the
   deadline is hit.

## 7. Hand off — both modes

Rewrite `NEXT.md` from scratch:

- **State:** one or two sentences — where the project is right now.
- **Next concrete action:** the next bounded unit(s), drawn from both tracks. In workflow mode, list a small backlog the next run can fan out; in single-unit mode, name the one unit. Include filenames needed.
- **Open decisions:** every `wiki/decisions/open/` id, each marked *eligible for ratification next session* or *opened this session (not yet eligible)*.
- **Do-not-re-grind:** carry the standing fence list forward, pruning only what a landed artifact made moot.
- **Standing-override notes:** anything Tom should see if he ever looks (kept short; the website carries the readable version).

Tick any program items this session advanced in `wiki/program.md` (same commit), with the
session and artifact.

Append one dated line to `log.md` describing the run (mode, what landed, decisions queued/ratified, spend, anything notable). Example:

```
2026-06-13  workflow: 2 waves + coherence pass; landed <X>; ratified <Y> (adversarial review); $0.80; site updated; merged PR #N.
```

**Wind-up hygiene — before you stop.** Terminate every background task or polling loop this
session started, and verify none survive: no stray `sleep`, no wait-loop, no leftover `python3`
run process alive, and `git status` clean. A scheduled Routine relies on each session ending
clean — a runaway loop or a still-running background task blocks the next run and strands
uncommitted work. Confirm the clean process table and the clean tree as the last thing you do.

Stop cleanly at the wind-up point — which means **after** the squash-merge has succeeded, never before.

## Failure-mode checklist (post-mortem prompts)

- Did I read more than I needed?
- Did I conflate two senses of "meaning"?
- Did I cite a resource I had not actually checked?
- Did I retune an indicator after seeing a null?
- Did I promote a contingent finding without a `wiki/decisions/resolved/` entry?
- Did I ratify a decision opened in this same session, or skip the independent reviewer?
- Did a subagent fabricate a quote or anchor, and did the coherence pass catch it?
- Did two subagents collide on a shared file?
- Did I wait on a process by name-match (`pgrep -f`) instead of its PID or a completion notification? Did I leave a background task or wait-loop running at wind-up?
- Did I leave work uncommitted or unmerged? If this session landed substantive work, did I create-or-extend today's journal entry (§5b)?
- Did I check `wiki/program.md`, and tick what this session advanced?
- Did I size a claim-carrying probe to powered N (§4) — or record why not?
- Did the website state anything more strongly than the wiki does?
- Did I exceed (or fail to record) the day's OpenRouter spend?

Each "yes" is a defect worth logging.
