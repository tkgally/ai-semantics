# NEXT.md

## State

**Eight of nine open decisions were ratified by Tom (2026-05-29)** in an interactive walkthrough; they now live in [`wiki/decisions/resolved/`](wiki/decisions/resolved/). The headline consequence: **two probes are now ratified end-to-end (anchor + operationalization) and can actually be RUN** — the project moves from *designing* to *running its first probe*.

Resolved:
- **AANN** — anchor = Mahowald 2023; operationalization = continuation-likelihood contrast (Option A) + prompted-acceptability fallback + threshold T1 + held-out adjectives locked pre-run. → [`design/aann-construction-v1`](experiments/designs/aann-construction-v1.md) is ready to run.
- **Scivetti bundle** (caused-motion, conative, way, comparative-correlative) — all anchored to the **Scivetti CxNLI dataset**. During the walkthrough Tom located the de-anonymized repo ([github.com/melissatorgbi/beyond-memorization](https://github.com/melissatorgbi/beyond-memorization)); it was inspected and confirmed to carry **per-item construction labels + a single gold answer per item** (an "answer key" + aggregate ≈0.90/0.83 baseline — *not* a multi-rater gradient). [`resource/scivetti-2025-cxnli-dataset`](wiki/base/resources/scivetti-2025-cxnli-dataset.md) upgraded `external-only → partial`, now `anchors` the four conjectures.
- **constructional-divergence-operationalization** — default (both instruments, 30/70/15-pp thresholds, frozen pre-run). → [`design/comparative-correlative-v1`](experiments/designs/comparative-correlative-v1.md) is ready to run.
- **cxg-probing-anchor** — Option A: the surprisal-validity claim stays AANN-scoped; cross-construction generality stays an explicitly provisional extrapolation.

**Standing steer recorded (PROJECT.md §1/§2, CLAUDE.md rule 6):** keep all claims realistic and modest; the project's purpose is to extend genuine human knowledge and understanding using AI tools — not to produce publishable research or pad a CV. Ratifying an anchor/operationalization fixes the *yardstick*, never the *result* — every ratified conjecture/design here remains **untested/unrun**.

## Next concrete action

Default is **workflow mode** (`PROTOCOL.md §A`). The project is now at the **Run** step of the loop (charter §5.4) for the first time. Priority backlog:

1. **Run the AANN probe** ([`design/aann-construction-v1`](experiments/designs/aann-construction-v1.md)) — fully ratified. Prerequisite: mirror the Mahowald repo (`github.com/mahowak/aann-public`) into `experiments/data/aann/` (license-check first), then execute the read-only continuation-likelihood probe against the panel ([`config/models.md`](config/models.md)), under the budget cap ([`config/budget.md`](config/budget.md)). Record prompts/outputs under `experiments/runs/`. Write the result — **including a null** — and only then update the conjecture/theory. Lock the held-out adjective list before running (charter §8).
2. **Run the comparative-correlative / Scivetti probe** ([`design/comparative-correlative-v1`](experiments/designs/comparative-correlative-v1.md)) — fully ratified. Prerequisite: check the Scivetti repo license, then mirror it into `experiments/data/scivetti/` (or work in place if no license); enumerate the CC subset; run both instruments per the ratified operationalization; compare panel NLI labels to the per-item gold answers + the aggregate ≈0.90/0.83 baseline (not a per-item gradient).
3. **Develop the lexical wedge** ([`open-question/lexical-polysemy-gradience`](wiki/findings/open-questions/lexical-polysemy-gradience.md)) — non-blocked; read the WiC / graded usage-similarity line, then propose a conjecture + catalogue a gradience-bearing sense resource.

Keep claims modest; write nulls as first-class results. Run `senselint.py` (0 errors) + `linkify.py` before commit.

## Blocked pending Tom

- [`decisions/open/relational-anchor-shortlist`](wiki/decisions/open/relational-anchor-shortlist.md) — human dyadic-interaction anchor for the relational-meaning pilot (default: Clark & Wilkes-Gibbs 1986 + Pickering & Garrod 2004 backdrop). **Not yet taken** ("Decision 9" in the walkthrough — the broader two-AI relational experiment — was deferred).

That is the only open decision. Everything else is either ratified or non-blocked.

## Reminder for the next cold-start

Charter: `PROJECT.md` (note the restated **purpose/modesty** principle in §1/§2). Schema: `CLAUDE.md` (now incl. rule 6, modest realistic claims). Run discipline: `PROTOCOL.md` — **"continue working" ⇒ workflow mode**. Read `wiki/index.md` before opening pages. **Reconcile `wiki/decisions/open/` first** (one entry: relational-anchor-shortlist). **The big change this session: the AANN and comparative-correlative probes are ratified and runnable — the next loop turn should RUN one and write the result (null included), not design more.** Mirror the relevant dataset into `experiments/data/` (license-check) before running. Run `senselint.py` (0 errors) + `linkify.py` before each commit; commit and merge to the default branch before stopping.
