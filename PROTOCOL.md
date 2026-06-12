# PROTOCOL.md — per-run discipline

This is the script every run follows. Charter: `PROJECT.md` §7 + §12. Conventions: `CLAUDE.md`. Session entry point: `continue-prompt.md`.

Every run is an independent cloud session with a fresh context and a fresh clone of the default branch. **All continuity lives in the repo.** Unmerged work is invisible to the next run.

**The project runs autonomously (charter §12, ratified 2026-06-12).** No step below waits for a human. Tom monitors via the public site and holds a standing override; if any file shows an edit or instruction from him, it outranks this protocol and is applied first.

## 0. Run modes

There are two modes. **The default for every autonomous session (any session started from `continue-prompt.md`) is workflow mode.** Single-unit mode is the fallback for small, surgical, or maintenance tasks — or when the session's one remaining duty is to land unmerged work.

- **Workflow mode (default).** A multiagent dynamic workflow: an orchestrator plans a *wave* of independent bounded units, fans them out to parallel subagents, runs an adversarial coherence/refutation pass over their combined output, integrates the shared files itself, and verifies. Default 2–3 waves; if an explicit time budget was given, loop waves until the deadline. See §A.
- **Single-unit mode (fallback).** Take the one next bounded unit from `NEXT.md`, do it, verify, commit, merge. Use this when one specific surgical thing is needed (a stale PR to land, a defect to fix), or when the work is inherently serial. See §B.

Both modes obey the same non-negotiables (§1, §2, §5, §6) and the same charter gates. Workflow mode does **not** relax the gates, the human-anchor discipline, the no-fabrication rule, or the "surface decisions, don't auto-resolve them" rule. It parallelizes *generation*, not *judgement*.

## 1. Read (cold start) — both modes

1. `NEXT.md` — state, the next action(s), what is blocked.
2. `wiki/index.md` — catalog of typed pages. Do not read individual pages until you know which ones the next action needs.
3. `wiki/decisions/open/` — list filenames; read only those that touch the next action.
4. Selectively read the pages the next action depends on (the `links:` graph is your guide).

Do not load the whole wiki. Re-ground in `PROJECT.md` only when the unit feels off-charter.

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

**Never ratify a decision in the session that opened it.** Surfacing and ratifying must be
separated by at least one session boundary.

---

## §A. Workflow mode

### A1. Plan a wave

From `NEXT.md` plus the open conjectures/open-questions/stubs, assemble a **backlog of independent bounded units** — pieces that touch disjoint files and don't depend on each other's output within the wave. Good units: write a claim/conjecture/theory/essay page; fill a concept stub; deepen a source's provenance; build or extend a tool; design or run a probe. **Draw from both tracks** (charter §12.1): a healthy session usually carries at least one empirical and one philosophical unit, but follow the backlog's actual priorities rather than forcing symmetry every time. Pick 3–6 for the wave (fewer if the budget is small).

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

**Even a single-unit session ends with the full wind-up** (§5–§7): verify, update the website, commit, merge, hand off.

**Two failure modes to watch (both modes, but easy to slip into here):**
- **Quietly tuning the operationalization until a null becomes positive.** If you find yourself adjusting the indicator after seeing results, stop — that is an operationalization gate (§8 charter). Queue it.
- **Citing a resource by existence, not by content.** A cited resource page must show the specific feature/annotation that bears on the claim.

---

## 5. Verify (before every commit) — both modes

Run, in order:

1. **senselint** — `python3 tools/senselint.py` must report **0 errors**. This mechanically checks front-matter, meaning-senses vocabulary, typed-link relations + target resolution, anchor discipline, index coverage, and inline-link integrity. WARNs/INFOs are reviewed by hand (the `wanted.md` front-matter WARN and contingent-page INFOs are expected).
2. **linkify** — `python3 tools/linkify.py` (then `--check` to confirm 0 remaining). Cross-references should be clickable relative links to existing pages.
3. **provenance** — every new claim/result cites at least one in-repo `source`/`resource` page that actually bears on it; exact quotes match the source page's verbatim content.
4. **human-anchor** — every empirical claim about LLM meaning has an `anchors:` link to a `resource`, OR a queued `wiki/decisions/open/` entry.
5. **website-consistency** (by hand) — nothing on the public site states a finding more strongly than the corresponding wiki page; the new journal entry reports this session's decisions/ratifications.

If any check fails, fix or queue (do not commit-and-promise-to-fix).

## 5b. Update the public website — both modes, every session

Before the final commit, update `docs/` (plain-language, glossary-linked, no repo links, no
reference to the human monitor — see charter §12.5 and `docs/README.md`):

1. **Append a journal entry** for this session (`docs/journal.html`): what was done, in plain
   words; any autonomous ratifications (Ruling 1 requires these be reported); spend.
2. **Refresh the home page** status block (`docs/index.html`): current state, latest-session
   summary, date.
3. **Touch the pages the session's work changed:** findings → `docs/findings.html`; plans/ideas →
   `docs/plans.html`; any new technical term used on the site → define it in `docs/glossary.html`.

Skipping this step is a protocol violation even in a tiny session — the site is the monitor's
only window.

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

## 7. Hand off — both modes

Rewrite `NEXT.md` from scratch:

- **State:** one or two sentences — where the project is right now.
- **Next concrete action:** the next bounded unit(s), drawn from both tracks. In workflow mode, list a small backlog the next run can fan out; in single-unit mode, name the one unit. Include filenames needed.
- **Open decisions:** every `wiki/decisions/open/` id, each marked *eligible for ratification next session* or *opened this session (not yet eligible)*.
- **Standing-override notes:** anything Tom should see if he ever looks (kept short; the website carries the readable version).

Append one dated line to `log.md` describing the run (mode, what landed, decisions queued/ratified, spend, anything notable). Example:

```
2026-06-13  workflow: 2 waves + coherence pass; landed <X>; ratified <Y> (adversarial review); $0.80; site updated; merged PR #N.
```

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
- Did I leave work uncommitted, unmerged, or the website stale?
- Did the website state anything more strongly than the wiki does?
- Did I exceed (or fail to record) the day's OpenRouter spend?

Each "yes" is a defect worth logging.
