# PROTOCOL.md — per-run discipline

This is the script every run follows. Charter: `PROJECT.md` §7. Conventions: `CLAUDE.md`.

Every run is an independent cloud session with a fresh context and a fresh clone of the default branch. **All continuity lives in the repo.** Unmerged work is invisible to the next run.

## 0. Run modes

There are two modes. **The default, whenever Tom says "continue working on the project" (or anything equivalent), is workflow mode.** Single-unit mode is the fallback for small, surgical, or maintenance tasks.

- **Workflow mode (default).** A multiagent dynamic workflow: an orchestrator plans a *wave* of independent bounded units, fans them out to parallel subagents, runs an adversarial coherence/refutation pass over their combined output, integrates the shared files itself, and verifies. If Tom gave a time budget, it then plans the next wave and repeats until the deadline. See §A.
- **Single-unit mode (fallback).** Take the one next bounded unit from `NEXT.md`, do it, verify, commit. Use this when Tom asks for one specific thing, or when the work is inherently serial. See §B.

Both modes obey the same non-negotiables (§1, §2, §5, §6) and the same charter gates. Workflow mode does **not** relax the gates, the human-anchor discipline, the no-fabrication rule, or the "surface decisions, don't auto-resolve them" rule. It parallelizes *generation*, not *judgement*.

## 1. Read (cold start) — both modes

1. `NEXT.md` — state, the next action(s), what is blocked.
2. `wiki/index.md` — catalog of typed pages. Do not read individual pages until you know which ones the next action needs.
3. `decisions/open/` — list filenames; read only those that touch the next action.
4. Selectively read the pages the next action depends on (the `links:` graph is your guide).

Do not load the whole wiki. Re-ground in `PROJECT.md` only when the unit feels off-charter.

## 2. Reconcile decisions — both modes

For each file in `decisions/open/`:
- If Tom has added a `resolution:` block or moved it to `resolved/`, apply it: move/keep the page in `decisions/resolved/` with date and rationale; find every page with that decision id in `contingent-on:` and either (a) promote it (remove from `contingent-on`, upgrade language from provisional to settled) or (b) retire it if the ratified decision contradicts it.
- Otherwise leave it; if it still blocks the unit, re-flag in `NEXT.md`.

**Never auto-resolve an open decision yourself.** Surfacing is the job; ratifying is Tom's.

---

## §A. Workflow mode

### A1. Plan a wave

From `NEXT.md` plus the open conjectures/open-questions/stubs, assemble a **backlog of independent bounded units** — pieces that touch disjoint files and don't depend on each other's output within the wave. Good units: write a claim/conjecture/theory page; fill a concept stub; deepen a source's provenance; build or extend a tool. Pick 3–6 for the wave (fewer if the budget is small).

Two hard constraints on unit independence:
- **Disjoint writes.** Each subagent creates/edits its *own* files. No two subagents touch the same file. The orchestrator alone edits the shared files (`wiki/index.md`, `NEXT.md`, `log.md`) — never a subagent.
- **No intra-wave dependencies.** If unit B needs unit A's output, they go in different waves.

### A2. Fan out

Launch the wave's subagents in parallel. Every subagent prompt must carry the **house rules**:
- Read `CLAUDE.md`, `PROTOCOL.md` §5, `wiki/meaning-senses.md`, `wiki/index.md`, and the specific dependency pages — first.
- Create only the named new files; do **not** edit `wiki/index.md`, `NEXT.md`, `log.md`, `CLAUDE.md`, `PROTOCOL.md`, `PROJECT.md`, or any file outside the assignment.
- Use only exact, verifiable quotes with provenance. **Never fabricate a quote, page number, or human-annotated resource.** If a fetch fails, report it honestly and change nothing fabricated.
- Respect anchor discipline: a claim/result needs an `anchors:` link to a resource, or `anchor: pending` + a queued `decisions/open/` entry. Never invent an anchor.
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
- If Tom gave an explicit end time and it has not arrived, plan the next wave (A1) — **refill the backlog** with newly-tractable units (a wave often unblocks the next: a filled stub lets a dependent conjecture proceed; a new claim invites its experiment design). Continuous runs end at the *clock*, not when the first backlog empties.
- If no end time was given, stop after one wave and hand off (§7). Do not invent ambitious work to fill time that wasn't requested.
- Stop early regardless if: the backlog has no unit whose human anchor is in-repo or queueable; or the remaining units are all blocked pending Tom; or you would have to fabricate to proceed.

Watch the token budget: a coherence pass is the expensive part of each wave. Note approximate subagent token use per wave in the wind-up so Tom can calibrate.

---

## §B. Single-unit mode (fallback)

Take the single next bounded unit named in `NEXT.md`. It must fit comfortably in one context window. If it does not, split it: write the split back into `NEXT.md` as numbered subunits, do unit 1, and hand off.

If `NEXT.md` is empty or stale, do not invent ambitious work. Pick the most tractable open conjecture or open question whose human anchor is in-repo, and proceed.

**Two failure modes to watch (both modes, but easy to slip into here):**
- **Quietly tuning the operationalization until a null becomes positive.** If you find yourself adjusting the indicator after seeing results, stop — that is an operationalization gate (§8 charter). Queue it.
- **Citing a resource by existence, not by content.** A cited resource page must show the specific feature/annotation that bears on the claim.

---

## 5. Verify (before every commit) — both modes

Run, in order:

1. **senselint** — `python3 tools/senselint.py` must report **0 errors**. This mechanically checks front-matter, meaning-senses vocabulary, typed-link relations + target resolution, anchor discipline, index coverage, and inline-link integrity. WARNs/INFOs are reviewed by hand (the `wanted.md` front-matter WARN and contingent-page INFOs are expected).
2. **linkify** — `python3 tools/linkify.py` (then `--check` to confirm 0 remaining). Cross-references should be clickable relative links to existing pages.
3. **provenance** — every new claim/result cites at least one in-repo `source`/`resource` page that actually bears on it; exact quotes match the source page's verbatim content.
4. **human-anchor** — every empirical claim about LLM meaning has an `anchors:` link to a `resource`, OR a queued `decisions/open/` entry.

If any check fails, fix or queue (do not commit-and-promise-to-fix).

## 6. Commit and merge to the default branch — both modes

```
git add -A
git commit -m "<short imperative summary>

<longer body referencing the unit(s) + any decisions queued>"
git push -u origin <branch>
# open PR; merge to the default branch per Tom's stated landing preference for the session
```

The next run clones the default branch fresh. Unmerged work is invisible and will be redone. In workflow mode, each wave is its own commit (§A5); the final commit carries the integration + handoff.

## 7. Hand off — both modes

Rewrite `NEXT.md` from scratch:

- **State:** one or two sentences — where the project is right now.
- **Next concrete action:** the next bounded unit(s). In workflow mode, list a small backlog the next run can fan out; in single-unit mode, name the one unit. Include filenames needed.
- **Blocked pending Tom:** every `decisions/open/` id gating promotion of work.

Append one dated line to `log.md` describing the run (mode, what landed, decisions queued, anything notable). Example:

```
2026-05-29  workflow: 6-unit wave + coherence pass; landed <X>; queued decisions <Y>; senselint clean.
```

Stop cleanly at the wind-up point (or, in workflow mode with a deadline, when the clock arrives).

## Failure-mode checklist (post-mortem prompts)

- Did I read more than I needed?
- Did I conflate two senses of "meaning"?
- Did I cite a resource I had not actually checked?
- Did I retune an indicator after seeing a null?
- Did I promote a contingent finding without a `decisions/resolved/` entry?
- Did a subagent fabricate a quote or anchor, and did the coherence pass catch it?
- Did two subagents collide on a shared file?
- Did I leave work uncommitted or unmerged?

Each "yes" is a defect worth logging.
