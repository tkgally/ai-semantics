# NEXT.md

## State

Bootstrapped (2026-05-28). The repository now has the schema (`CLAUDE.md`), the run discipline (`PROTOCOL.md`), the controlled meaning-sense vocabulary (`wiki/meaning-senses.md`), six concept stubs in `wiki/base/concepts/`, four founding conjectures in `wiki/findings/conjectures/`, one open question (`wiki/findings/open-questions/relational-meaning-pilot.md`), a prioritized reading list (`wiki/base/wanted.md`), a resource catalogue skeleton, a chosen panel with calibration record (`config/models.md`, `experiments/runs/2026-05-28-panel-calibration/`), and a starting budget (`config/budget.md`).

No experimental claim is yet on the books. `findings/claims/`, `findings/results/`, `findings/theory/` are empty by design.

## Next concrete action

**Move the AANN conjecture from `proposed` to `designed` by writing the first experiment design.**

Why AANN first:

- It is the most-tractable of the four founding conjectures: one construction, one English-only stimulus family, a ready-made human anchor (the Weissweiler / Tayyar Madabushi line).
- The bootstrap calibration probe already surfaced a cross-model divergence on AANN (gpt-5.4-mini gave the compositional reading; the others gave the constructional one — see `experiments/runs/2026-05-28-panel-calibration/README.md`). This is a free hint that there is signal to find.
- The probe code is already a starting template for the real probe.

Files the next run will need:

- `wiki/findings/conjectures/aann-construction.md`
- `wiki/base/concepts/constructional-meaning.md`
- `experiments/runs/2026-05-28-panel-calibration/` (template + caveats)
- `config/models.md` (panel slugs + reasoning-token caveats)
- `config/budget.md` (pre-flight cost check)

Deliverables for the next unit:

1. `experiments/designs/aann-construction-v1.md` — formal design page: construct (AANN as form-meaning pairing), indicator (surprisal / acceptability contrast between licit and illicit AANN instantiations + held-out adjectives), method, **named human anchor** (Weissweiler stimulus list, catalogued as a `resource`), predictions (re-stated from the conjecture), falsification criteria.
2. `wiki/base/resources/weissweiler-aann-stimuli.md` — the resource page for the anchor (charter §2.4: cite *content*, not existence). If the actual stimulus list cannot be located and confirmed in this session, write the resource page as `status: external-only` with a clear pointer to where it lives and what feature of it grounds the claim, and write the anchor question as `decisions/open/aann-stimulus-source.md` rather than guessing.
3. **Operationalization gate.** Write `decisions/open/aann-operationalization.md` proposing the indicator (surprisal vs. inferential probe vs. acceptability rating) and the threshold for "tracks the construction." Provisional default: continuation-likelihood contrast on licit vs. minimally-illicit pairs, threshold = ≥20 percentile-points separation on ≥2 of 3 panel models. Downstream artifacts marked `contingent-on: aann-operationalization` until Tom ratifies.

Do **not** run the actual probe in the next session. Design → gate-queue → hand off. The probe run is the session after that.

## Blocked pending Tom

- None blocking the next action. Two queueable decisions will land in `decisions/open/` as part of the next unit:
  - `aann-stimulus-source.md` (which human-anchored AANN stimulus list to cite, and confirmation that we can actually inspect it).
  - `aann-operationalization.md` (what counts as evidence the model "tracks the construction").
- Charter-level points worth Tom's attention when convenient (no run depends on these yet):
  - The candidate panel was chosen on a single liveness probe. After the first real probe-run, propose either confirming or rotating.
  - `wiki/base/wanted.md` lists the founding reading list. Goldberg 1995 / 2006, Sterken & Cappelen volume, and Grindrod's recent monograph are P1; the rest can wait.

## Reminder for the next cold-start

Charter is `PROJECT.md`. Schema is `CLAUDE.md`. Run discipline is `PROTOCOL.md`. Read `wiki/index.md` before opening individual pages. **Commit and merge to the default branch** before stopping.
