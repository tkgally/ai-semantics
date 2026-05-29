---
id: aann-stimulus-source
title: Which human-anchored AANN stimulus set should ground the AANN probe?
status: open
opened: 2026-05-28
opened-by: lead-agent
contingent-artifacts:
  - conjecture/aann-construction
  - design/aann-construction-v1
---

# Decision: AANN stimulus source

## Question

The AANN conjecture ([`wiki/findings/conjectures/aann-construction.md`](../../findings/conjectures/aann-construction.md)) requires a human-anchored stimulus inventory to compare against panel-model behavior. The two candidate human anchors in the current CxG-probing literature both bear on AANN; we need to pick one (or both) as the canonical anchor for the probe, and confirm we can actually inspect what we cite.

## Options

### A. Mahowald (2023, EACL) — *A Discerning Several Thousand Judgments* (provisional default)

- **Stimulus structure** (Mahowald Table 1, p. 2): templatic generation across six noun-category templates × six adjective categories (ambig / qualitative / quant / stubborn / color / human) × a numeral inventory including *three* and *five* for the bulk of human experiments.
- **Human ratings**: MTurk acceptability ratings on a 1–10 scale, 126 raters × 3 critical sentences in Experiment 1 (378 ratings total); larger sets in Experiments 2 and 3.
- **Release**: code and data at `https://github.com/mahowak/aann-public` — confirmed-by-page-inspection in this session (the README lists `generate_sentence_templates/`, `aann-sents/`, `mturk_data/`, `mturk_generation/`, `gpt3_data/`).
- **Cataloguing**: [`wiki/base/resources/mahowald-2023-aann-stimuli.md`](../../base/resources/mahowald-2023-aann-stimuli.md) (`status: external-only` until a future run mirrors the repo and inspects file contents).
- **Why provisional default**: cleanest item-level match to the conjecture's predictions; data and code public; the four-way degenerate-variant design (switched order / no modifier / singular noun / no article) gives ready-made licit/illicit contrasts.

### B. Weissweiler et al. (2022/2023, CxG-probing line)

- **What**: Weissweiler, Hofmann, Köksal, and Schütze's CxG-probing papers cover AANN among other constructions in a broader CxG-probing toolkit.
- **Why consider**: aligns with the project's stated wedge of the Weissweiler / Tayyar Madabushi line; potentially richer in cross-construction comparison.
- **Caveat**: not yet inspected in this session; the AANN-specific stimulus structure and any released ratings need confirmation.

### C. Both — Mahowald as primary, Weissweiler as cross-check

- Run primarily against Mahowald's item set (which has documented human ratings and a public release), and use the Weissweiler line as a secondary independent anchor on the subset of items both lines cover.
- Cost: roughly doubles probe count if both lines are run in full; halves it if Weissweiler is used only as a sanity check on Mahowald's high-confidence contrasts.

## Provisional default (in force until Tom ratifies)

**Option A**: Mahowald (2023). Reason: (i) the item-level human ratings exist and are publicly released; (ii) the degenerate-variant design is directly usable as the licit/illicit minimal-pair backbone of the design; (iii) the paper's templatic structure makes it straightforward to define held-out adjectives.

The design ([`experiments/designs/aann-construction-v1.md`](../../../experiments/designs/aann-construction-v1.md)) is written against Option A and marked `contingent-on: aann-stimulus-source`.

## What would change the default

- If Weissweiler's AANN stimuli are confirmed to include item-level human ratings on a comparable scale (and code/data are public), then Option C becomes attractive: it gives an independent second anchor for free.
- If the Mahowald repo turns out to not contain the MTurk ratings in usable form, fall back to a fresh acceptability-anchor decision (and [`wiki/base/wanted.md`](../../base/wanted.md) queues a request to Tom for direct correspondence with the author).

## Notes for the resolver

Tom: a one-line ratification ("default stands" / "switch to C" / "switch to B and fetch the Weissweiler stimuli first") is enough. If switching, name the alternative paper precisely so the resource page can be retargeted.
