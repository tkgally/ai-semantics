# PROTOCOL.md — per-run discipline

This is the script every run follows. Charter: `PROJECT.md` §7. Conventions: `CLAUDE.md`.

Every run is an independent cloud session with a fresh context and a fresh clone of the default branch. **All continuity lives in the repo.** Unmerged work is invisible to the next run.

## 1. Read (cold start)

1. `NEXT.md` — what state the project is in, what the next concrete action is, what is blocked.
2. `wiki/index.md` — catalog of typed pages. Do not read individual pages until you know which ones the next action needs.
3. `decisions/open/` — list filenames; read only those that touch the next action.
4. Selectively read the pages the next action depends on (the `links:` graph is your guide).

Do not load the whole wiki. Do not re-read `PROJECT.md` unless you need to re-ground; re-ground when the unit feels off-charter.

## 2. Reconcile decisions

For each file in `decisions/open/`:
- If Tom has added a `resolution:` block or moved it to `resolved/`, apply it:
  - Move/keep the page in `decisions/resolved/` with date and rationale.
  - Find every page with that decision id in `contingent-on:` and either (a) promote it (remove from `contingent-on`, upgrade language from provisional to settled) or (b) retire it if the ratified decision contradicts it.
- Otherwise leave it; if it still blocks the unit, re-flag in `NEXT.md`.

## 3. Pick

Take the single next bounded unit named in `NEXT.md`. It must fit comfortably in one context window. If it does not, split it: write the split back into `NEXT.md` as numbered subunits, do unit 1, and hand off.

If `NEXT.md` is empty or stale, do not invent ambitious work. Pick the most tractable open conjecture or open question whose human anchor is in-repo, and proceed.

## 4. Do

Execute the unit. Charter and `CLAUDE.md` bind. Two specific failure modes to watch:

- **Quietly tuning the operationalization until a null becomes positive.** If you find yourself adjusting the indicator after seeing results, stop — that is an operationalization gate (§8 charter). Queue it.
- **Citing a resource by existence, not by content.** If you cite Universal Dependencies or PropBank in support of a claim, the page must show the specific feature/annotation that bears on the claim.

## 5. Verify (before commit)

Run, in order:

1. **senselint** — every new/changed `wiki/findings/` page has front-matter, declares ≥1 `meaning-senses` entry, uses a tag from `wiki/meaning-senses.md`, and does not present anything still in `contingent-on:` as settled. Until `tools/senselint.py` exists, do this by hand.
2. **provenance** — every new claim/result cites at least one in-repo `source` or `resource` page that actually bears on it. Exact quotes are matched against the source page's verbatim content.
3. **human-anchor** — every empirical claim about LLM meaning has an `anchors:` link to a `resource`, OR a queued `decisions/open/` entry that says the anchor question is unresolved.
4. **index hygiene** — `wiki/index.md` lists every new typed page.

If any check fails, fix or queue (do not commit-and-promise-to-fix).

## 6. Commit and merge to the default branch

```
git add -A
git commit -m "<short imperative summary>

<longer body referencing the unit + any decisions queued>"
git push -u origin <branch>
# open PR; merge to main as soon as CI (when it exists) is clean
```

The next run clones the default branch fresh. Unmerged work is invisible and will be redone. This is mandatory.

## 7. Hand off

Rewrite `NEXT.md` from scratch:

- **State:** one sentence — where the project is right now.
- **Next concrete action:** the single bounded unit the next run should pick up. Include filenames it needs.
- **Blocked pending Tom:** list any `decisions/open/` ids that are gating promotion of work.

Append one dated line to `log.md`:

```
2026-05-28  scaffold: bootstrapped repo per PROJECT.md §11; panel candidates queued; first conjectures drafted.
```

Stop cleanly. Do not start another unit in the same session.

## Failure-mode checklist (post-mortem prompts)

If something went wrong, before the next unit, ask:

- Did I read more than I needed?
- Did I conflate two senses of "meaning"?
- Did I cite a resource I had not actually checked?
- Did I retune an indicator after seeing a null?
- Did I promote a contingent finding without a `decisions/resolved/` entry?
- Did I leave work uncommitted or unmerged?

Each "yes" is a defect worth logging.
