# NEXT.md

## State

The AANN conjecture is `designed` (2026-05-28). The first experiment design exists at `experiments/designs/aann-construction-v1.md`, operationalizing the conjecture via a continuation-likelihood contrast against Mahowald 2023's published AANN stimuli and MTurk acceptability ratings. The human anchor is catalogued at `wiki/base/resources/mahowald-2023-aann-stimuli.md` (status: `external-only` — the public release at `github.com/mahowak/aann-public` was confirmed by reading the README and the paper, but not yet mirrored locally). Two operationalization decisions are queued for Tom (see below). No probe has been run.

`findings/claims/`, `findings/results/`, `findings/theory/` are still empty by design.

## Next concrete action

**Reconcile the two open AANN decisions; if both are ratified by Tom in `decisions/resolved/`, prepare the probe — mirror the Mahowald repo, lock the held-out adjective list, write the probe code. If either decision is still open, do *not* run the probe; pick the most tractable unblocked alternative instead.**

Step-by-step (next session):

1. **Reconcile decisions first.** Check `decisions/open/` and `decisions/resolved/`:
   - `aann-stimulus-source.md` — provisional default: Mahowald 2023.
   - `aann-operationalization.md` — provisional default: continuation-likelihood contrast (Option A), threshold T1, ≥30 held-out adjectives per category.
   If Tom has ratified, move both to `decisions/resolved/` with date and rationale, then drop them from `contingent-on:` on the conjecture and the design (and rewrite any provisional language as settled).
2. **If both decisions are ratified, do the probe-prep unit:**
   - Mirror `https://github.com/mahowak/aann-public` into `experiments/data/aann/aann-public/`. Check license first; if not present, leave a `LICENSE-CHECK.md` note and proceed read-only.
   - Promote `wiki/base/resources/mahowald-2023-aann-stimuli.md` from `external-only` to `catalogued` after inspecting actual file contents against the page's summary; correct any divergences.
   - Lock the held-out adjective list. Commit `experiments/data/aann/held-out-adjectives.txt` *before* writing the probe; freeze with at least 30 adjectives per Mahowald category, chosen from outside Mahowald's slot-filler superset.
   - Write `experiments/runs/<run-date>-aann-probe-v1/probe.py` mirroring the calibration probe's structure, including reasoning-token mitigation for Gemini. Do a 5-item dry run per panel model to confirm logprob availability (Option A vs. Option B fallback per model) before going wide.
   - Pre-flight cost check per `config/budget.md` against the actual measured token counts from the dry run.
   - **Do not run the full probe in the same session as the dry run.** Hand off to the *following* session for the full run + evaluation.
3. **If either decision is still open**, pick the next tractable unit instead:
   - Most tractable: catalogue the public OA papers in `wiki/base/wanted.md` P1 (Piantadosi & Hill 2022; Bender & Koller 2020; Lyre 2024; one Weissweiler CxG-probing paper) into `wiki/base/sources/` so a future run citing them has provenance pages. None of these requires Tom.
   - Or: write the `way`-construction design (analogous to the AANN one), which has independent open decisions but parallel structure. This is the **second-tractable** founding conjecture per the original NEXT-after-bootstrap.

Files the next run will need:

- `decisions/open/aann-stimulus-source.md`
- `decisions/open/aann-operationalization.md`
- `wiki/findings/conjectures/aann-construction.md`
- `experiments/designs/aann-construction-v1.md`
- `wiki/base/resources/mahowald-2023-aann-stimuli.md`
- `config/models.md`, `config/budget.md`
- `experiments/runs/2026-05-28-panel-calibration/probe.py` (as a template)

## Blocked pending Tom

- `decisions/open/aann-stimulus-source.md` — ratify Mahowald 2023 as primary anchor (default), or switch to Weissweiler-as-primary / Mahowald + Weissweiler combination.
- `decisions/open/aann-operationalization.md` — ratify continuation-likelihood contrast + T1 threshold (default), or switch to Mahowald-prompt replication / paraphrase probe, or tighten the threshold to T2.

Charter-level points worth Tom's attention when convenient:

- Panel is still on a single liveness probe; confirm or rotate after first real probe-run.
- `wiki/base/wanted.md` P1 list is unchanged; nothing about the AANN probe currently depends on a paywalled item being fetched.

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md`. Read `wiki/index.md` before opening individual pages. **Reconcile `decisions/open/` first.** **Commit and merge to the default branch before stopping.**
