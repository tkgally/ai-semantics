# NEXT.md

## State

Three AANN decisions remain open pending Tom (`decisions/open/aann-stimulus-source.md`, `decisions/open/aann-operationalization.md`). One new decision open: `decisions/open/way-construction-anchor.md` (provisional default: Option A — Goldberg 1995 examples as seed, anchor: pending). The AANN conjecture remains `designed`; the way-construction conjecture is now also `designed` (this session). Five P1 OA source pages catalogued in `wiki/base/sources/`. Full PDFs not fetched; page-level quotes pending.

## Next concrete action

**Fetch full PDFs for one or more catalogued sources to upgrade from `catalogued` to `received` with page-level quotes.** Priority candidates:

1. **Bender & Koller 2020** — PDF at ACL Anthology: `https://aclanthology.org/2020.acl-main.463.pdf`
2. **Lyre 2024** — PDF at arXiv: `https://arxiv.org/pdf/2402.10992`
3. **Mahowald et al. 2024** — PDF via DOI 10.1016/j.tics.2024.01.011 (CC BY 4.0, open access)

For each PDF fetched: (a) extract 3–5 verbatim page-level quotes most relevant to the source page's stated contribution to the project; (b) add the quotes to the source page under a `## Key passages` section with exact page numbers; (c) upgrade `status: catalogued` to `status: received`; (d) update `wiki/index.md` entry.

Step-by-step (next session):

1. Reconcile open decisions first. Check `decisions/open/` — if any of the three decisions have been ratified, apply them (see §Blocked pending Tom).
2. If decisions still open, proceed with PDF fetch.
3. Fetch Bender & Koller 2020 PDF first (smallest, most foundational for `grounded` tag reasoning).
4. Extract key passages; update `wiki/base/sources/bender-koller-2020-climbing.md`.
5. If context permits: repeat for Lyre 2024.
6. Update `wiki/index.md` for each upgraded source.
7. Commit and merge.

Files the next run will need:

- `decisions/open/aann-stimulus-source.md`
- `decisions/open/aann-operationalization.md`
- `decisions/open/way-construction-anchor.md`
- `wiki/base/sources/bender-koller-2020-climbing.md`
- `wiki/base/sources/lyre-2024-semantic-grounding.md`
- `wiki/base/sources/mahowald-2024-dissociating.md` (if fetching that PDF)
- `wiki/index.md`

## Blocked pending Tom

- `decisions/open/aann-stimulus-source.md` — ratify Mahowald 2023 as primary anchor (default), or switch.
- `decisions/open/aann-operationalization.md` — ratify continuation-likelihood contrast + T1 threshold (default), or switch.
- `decisions/open/way-construction-anchor.md` — ratify Option A (Goldberg 1995 examples as seed, anchor: pending), or supply corpus annotation (Option B), or identify published inference data (Option C). "Option A stands" is sufficient.

Charter-level points worth Tom's attention when convenient:

- Panel is still on a single liveness probe; confirm or rotate after the first real probe-run.
- `wiki/base/wanted.md` P1 list still has Sterken & Cappelen (forthcoming) and Grindrod (2024–25 monograph) outstanding; neither is gating any active probe.

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md`. Read `wiki/index.md` before opening individual pages. **Reconcile `decisions/open/` first.** **Commit and merge to the default branch before stopping.**
