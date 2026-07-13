---
type: resource
id: genitive-animacy-human-anchor
title: Genitive-alternation possessor-animacy direction — native-speaker acceptability anchor (Dubois et al. 2023)
status: catalogued
url: https://doi.org/10.1017/langcog.2023.51
license: CC BY 4.0 (via source/dubois-2023-genitive-animacy)
citation: "Dubois, T., Grafmiller, J., Paquot, M. & Szmrecsanyi, B. (2023). Animacy effects in the English genitive alternation. Language and Cognition, 1–23. https://doi.org/10.1017/langcog.2023.51"
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: depends-on
    target: source/dubois-2023-genitive-animacy
---

# Genitive-alternation possessor-animacy — human acceptability anchor

## What it is

A **human-labelled direction fact** for the English genitive alternation, taken from the native-speaker
half of [`source/dubois-2023-genitive-animacy`](../sources/dubois-2023-genitive-animacy.md) (Dubois,
Grafmiller, Paquot & Szmrecsanyi 2023, *Language and Cognition*, CC BY 4.0): **25 native speakers**
rated the acceptability of the two genitive variants (s-genitive *nature's beauty* vs of-genitive *the
beauty of nature*) across contexts on a graded scale (neutral midpoint 50), and their ratings were
compared against corpus-based production models.

The asset this catalogues is the **direction and rank of the possessor-animacy constraint**, verbatim
from the source:

> "…possessor animacy, which captures the tendency for animate possessors to favour the s-genitive and
> inanimate possessors to prefer the of-genitive."

> "…animacy is normally the strongest constraint of the genitive alternation (Rosenbach, 2014)…"

with the five-level animacy scheme (Zaenen et al. 2004): **animate** (humans/animals/entities
represented as human — *god's plan*) · **collective** · **inanimate** · **locative** · **temporal**.

## What it can ground

The conjecture [`conjecture/genitive-alternation-animacy`](../../findings/conjectures/genitive-alternation-animacy.md)
predicts that panel LLMs' genitive-variant preferences shift in the **human-rated animacy direction**
(animate possessor → s-genitive; inanimate → of-genitive). This resource supplies the exact human-side
signal that prediction needs:

- The **direction** is a native-speaker acceptability fact (not merely a corpus frequency): humans
  *rate* animate-possessor s-genitives more acceptable and inanimate-possessor of-genitives more
  acceptable, holding the possessum fixed.
- The **covariates the design must hold constant** are named in the same source: **possessor length**,
  **possessum length**, **final sibilancy of the possessor**, **definiteness**, structural persistence,
  lexical density (see the source page). A clean animacy probe neutralizes these so any preference shift
  is attributable to animacy, not to a confounded surface feature.
- The **human anchor's shape** — a graded acceptability rating with midpoint 50 — is *broadly* the graded
  shape the project's validated forced-choice indicator produces (the dative instrument distributes 100
  points by naturalness). Note the task structures are **not identical**: Dubois rated each variant
  *separately*, whereas the primary indicator is a *forced-choice split* — so the anchor licenses the
  effect's **direction/sign**, not a per-item magnitude match (the design registers a separate-rating
  sensitivity check that mirrors Dubois' actual task).

## What it cannot ground on its own

- **A per-item human gradient** to regress the panel against. The paper reports the aggregate
  rating↔corpus concordance and mixed-effects coefficients; the per-item native-speaker ratings and the
  Trinity Lancaster Corpus rows are **not** shown to be openly licensed (TLC is a controlled research
  corpus). So the direction is anchorable now; a *per-item gradient* secondary is contingent on a
  separate license-verified dataset scout (queued in the open design decision) — mirroring the dative
  line, where the corpus production surface was the primary and per-item ratings an opportunistic
  upgrade only.
- **A surface-frequency-vs-animacy separation.** The direction fact alone does not certify that a
  panel's animate→s-genitive shift is animacy-driven rather than a shadow of the higher corpus
  frequency of animate-possessor s-genitive strings; that separation is the probe's **load-bearing
  control** (a frozen corpus surface-frequency covariate and/or a typical-vs-atypical possessor split),
  surfaced in the open design decision, not something this resource settles.
- **Model representations** — only a behavioural probe.
- **Cross-linguistic** claims — the s-genitive/of-genitive alternation in this form is English-specific.

## Known limits / cautions

- **Acceptability rating, not production.** The native-speaker anchor is a *judgment* task (what
  speakers rate as natural), complemented in the source by a corpus *production* model. The right
  anchor for a graded-forced-choice naturalness indicator is the rating direction; a production-gradient
  cross-check is the secondary, contingent leg.
- **Animacy is confounded with frequency in natural data.** Animate possessors are both (a) preferred in
  the s-genitive by humans and (b) more frequent as s-genitive strings — so a probe must dissociate the
  two, or it measures the shadow rather than the constraint. This is the operationalization crux the
  open decision fences off.
- **Contamination.** The paper's example items may sit in training data; a clean probe uses **synthetic
  minimal pairs** built to the animacy scheme (the source anchors the *animacy → variant* relation, not
  specific items), as the dative and AANN held-out designs did.
