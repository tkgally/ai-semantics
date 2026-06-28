# VWSD grounding-headroom NL-baseline probe — the MAGNITUDE follow-up

Run dir for the frozen design
[`design/vwsd-grounding-headroom-nlbaseline`](../../designs/vwsd-grounding-headroom-nlbaseline.md),
under the ratified competence standard
[`decisions/resolved/vwsd-nlbaseline-competence-dv`](../../../wiki/decisions/resolved/vwsd-nlbaseline-competence-dv.md)
(ADOPT-DEFAULT Q1-C) with the three deferred numbers ratified session 127
[`decisions/resolved/vwsd-nlbaseline-audit-params`](../../../wiki/decisions/resolved/vwsd-nlbaseline-audit-params.md)
(ADOPT-DEFAULTS):

- **P1** — recovery scored **graded none/partial/high**; band metric = the **high-recovery rate**.
- **P2** — NL **author = panel.A `claude-sonnet-4.6`**; **held-out auditors = panel.B `gpt-5.4-mini`
  + panel.C `gemini-3.5-flash`** (both held out from the author); band on the **two-auditor mean**.
- **P3** — two-sided target band **`[0.60, 0.95]`** on the high-recovery rate.

It answers the first-class **Limitation 1** of
[`result/vwsd-grounding-headroom-v2`](../../../wiki/findings/results/vwsd-grounding-headroom-v2.md):
v2 tested the gating **shape** with a *de-referented* (visual-form-only) text channel, so it could not
read the **magnitude** of the residual a *fluent, referent-naming* channel leaves (prediction 3,
"narrow headroom"). This run authors that fluent channel and reads the magnitude.

## What is NEW spend vs REUSED verbatim

The **only** new text channel is a competent natural-language description that **names** the depicted
referent (v1 named + saturated; v2 barred naming + manufactured headroom; this is the fluent middle).
New spend = (i) NL descriptor authoring, (ii) the TEXT-NL selection arm, (iii) the held-out adequacy
audit. The frozen items, the IMAGE arm, and the DISTRACT control are **reused verbatim by sha** (they
are properties of the items + images + models, not of the text channel):

- `frozen/run_items.json` — the v2 frozen stratified N=120, sha256 **`7f9e52fa…`** (verbatim).
- `raw/image.json` — the v2 IMAGE arm (s112), sha256 **`6884eea0…430870`** (verbatim, reused).
- `raw/distract.json` — the v2 DISTRACT word-ablated control (s121), sha256 **`f8fbb6be…`** (verbatim,
  reused; **credited FIRST** — no image lift counts as headroom unless it survives this clean null).

## Files

- `run.py` — the harness (desc / text / audit arms; reused-arm shas verified at read time).
- `analyze.py` — scores the FREEZE sections (sep_nl_i, strata, adequacy audit + band) and, only after
  a pre-run-critic GO, the RESULT sections (DISTRACT first, magnitude read, rescue rate).
- `frozen/nl_descriptors.json` — the NL descriptions (1158 unique candidate images) + the adequacy
  audit; frozen + checksummed **before** the reused IMAGE arm is read.
- `raw/text_nl.json` — the TEXT-NL selection arm (120 × 3), the source of sep_nl_i.
- `raw/descriptor_calls.json`, `raw/audit_calls.json` — full call ledgers (billed `usage.cost`).
- Images are **OUT of git** (`.gitignore`; redistribution unconfirmed) — fetched at runtime into
  `$VWSD_IMAGES` (572MB resized EN zip, sha `b9f2f1e1…af8f`).

## Discipline (anti-cheat)

The audit band was **ratified before any NL description was authored** (s127, independent review). The
NL descriptions + adequacy audit + `sep_nl_i` are **frozen + checksummed before** the reused IMAGE arm
is read (no retuning). A fresh independent **pre-run critic** must GO against the observed sep_nl_i +
audit distributions before the magnitude read; a held-out high-recovery rate outside `[0.60, 0.95]` is
a **NO-GO that defers and relaxes nothing**. Both a narrow and a wide residual are pre-registered as
first-class; the magnitude is always *"narrow/wide under THIS competence standard, on these 120
items,"* never absolute.

## Results

*(filled in after the run by the executing session — see the journal/log and
`result/vwsd-grounding-headroom-nlbaseline` if it was cleared, or the deferral note if the pre-run
critic returned NO-GO.)*
