# NEXT.md

## State

Both AANN operationalization decisions remain open pending Tom (`decisions/open/aann-stimulus-source.md`, `decisions/open/aann-operationalization.md`). No probe has run. The AANN conjecture remains `designed`.

Four P1 OA source pages have been catalogued in `wiki/base/sources/` (Bender & Koller 2020; Piantadosi & Hill 2022; Lyre 2024; Weissweiler et al. 2023). These update the `wanted.md` status from `wanted` to `catalogued` for those entries. Full PDFs have not been fetched; page-level quotes are not yet available.

## Next concrete action

**Reconcile the two open AANN decisions; if both ratified by Tom in `decisions/resolved/`, prepare the probe. If either still open, catalogue Mahowald et al. 2024 (the next P1 OA paper on the wanted list) and/or write the `way`-construction experiment design.**

Step-by-step (next session):

1. **Reconcile decisions first.** Check `decisions/open/` and `decisions/resolved/`:
   - `aann-stimulus-source.md` — provisional default: Mahowald 2023.
   - `aann-operationalization.md` — provisional default: continuation-likelihood contrast (Option A), threshold T1, ≥30 held-out adjectives per category.
   If Tom has ratified, move both to `decisions/resolved/` with date and rationale, then drop them from `contingent-on:` on the conjecture and the design (and rewrite any provisional language as settled).

2. **If both decisions are ratified, do the probe-prep unit** (same as before — see previous NEXT.md for the mirroring, held-out list, probe code, dry-run, and cost-check steps). Do not run the full probe in the same session as the dry run.

3. **If either decision is still open**, next tractable unit:
   - **Most tractable (not Tom-blocked):** Catalogue Mahowald et al. 2024, "Dissociating language and thought in large language models," *Trends in Cognitive Sciences* 28(6). Try OA preprint at arXiv (search `mahowald dissociating language thought 2024`). This provides the `functional-vs-formal` tag's primary reference.
   - **Second tractable:** Write the `way`-construction experiment design (analogous to `experiments/designs/aann-construction-v1.md`), which has its own independent open decisions but parallel structure.
   - **Third tractable:** Fetch full PDFs for one or more of the newly catalogued sources (Bender & Koller 2020 PDF is directly at ACL Anthology; Piantadosi & Hill 2022 and Lyre 2024 PDFs at arXiv) to upgrade source pages from `catalogued` to `received` with page-level quotes.

Files the next run will need:

- `decisions/open/aann-stimulus-source.md`
- `decisions/open/aann-operationalization.md`
- `wiki/findings/conjectures/aann-construction.md`
- `experiments/designs/aann-construction-v1.md`
- `wiki/base/resources/mahowald-2023-aann-stimuli.md`
- `wiki/base/sources/` (all four new pages, for reference)
- `config/models.md`, `config/budget.md`
- `experiments/runs/2026-05-28-panel-calibration/probe.py` (as template, if probe-prep)

## Blocked pending Tom

- `decisions/open/aann-stimulus-source.md` — ratify Mahowald 2023 as primary anchor (default), or switch to Weissweiler-as-primary / Mahowald + Weissweiler combination.
- `decisions/open/aann-operationalization.md` — ratify continuation-likelihood contrast + T1 threshold (default), or switch to Mahowald-prompt replication / paraphrase probe, or tighten the threshold to T2.

Charter-level points worth Tom's attention when convenient:

- Panel is still on a single liveness probe; confirm or rotate after first real probe-run.
- `wiki/base/wanted.md` P1 list still has Mahowald 2024, Sterken & Cappelen (forthcoming), Grindrod (2024–25 monograph) outstanding. None currently gating the AANN probe.

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md`. Read `wiki/index.md` before opening individual pages. **Reconcile `decisions/open/` first.** **Commit and merge to the default branch before stopping.**
