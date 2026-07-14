---
type: resource
id: particle-placement-givenness-human-anchor
title: English particle-placement object-givenness direction — native-speaker corpus anchor (Kim et al. 2016 / Gries 1999)
status: catalogued
url: https://aclanthology.org/Y16-3005/
license: CC BY 4.0 (via source/kim-2016-particle-placement)
citation: "Kim, H.-E., Lee, G.-H. & Lee, Y. (2016). A Correlation Analysis of English Particle Placement of Three East Asian EFL Learners' Writings. PACLIC 30: Posters, 347–354. https://aclanthology.org/Y16-3005/"
created: 2026-07-14
updated: 2026-07-14
links:
  - rel: depends-on
    target: source/kim-2016-particle-placement
---

# English particle placement — object-givenness (definiteness) human-direction anchor

## What it is

A **human-labelled direction fact** for the English verb-particle (particle-placement) alternation —
the joined order *picked up the book* (V-Prt-DO) vs the split order *picked the book up* (V-DO-Prt) —
taken from [`source/kim-2016-particle-placement`](../sources/kim-2016-particle-placement.md) (Kim, Lee &
Lee 2016, PACLIC 30, **CC BY 4.0**), whose CC-licensed text states the native-speaker direction (a
restatement of Gries 1999's synthesis of the descriptive/corpus literature, corroborated on the paper's
own native-speaker ICE-GB corpus).

The asset this catalogues is the **direction of the object information-status (definiteness/givenness)
constraint**, verbatim from the source:

> "If the determiner of DO is indefinite (such as a or an), native speakers tend to choose construction0
> rather than construction1. If the determiner of DO is definite (such as the), native speakers prefer to
> use construction1 rather than construction0."

with the construction mapping the source fixes: **construction0 = the JOINED order** (V-Prt-DO),
**construction1 = the SPLIT order** (V-DO-Prt). So the human direction is: **definite / discourse-given
direct object → split order; indefinite / new object → joined order.** Definiteness is the grammaticalized
marker of the object's discourse-givenness, so this is the same information-structural constraint the
dative line tested (given material placed earlier), on a new construction.

A **second, convergent** direction the same source anchors (used as a corroboration leg, not the focal
contrast):

> "If the DO is long, native speakers tend to choose construction0 rather than construction1. If the DO
> is short, however, the native speakers tend to use construction1 rather tahn [sic] construction0."

→ **short object → split; long/heavy object → joined** (the end-weight / domain-minimization constraint).

## What it can ground

The conjecture [`conjecture/particle-placement-givenness`](../../findings/conjectures/particle-placement-givenness.md)
predicts that panel LLMs' particle-placement preferences shift in the **human direction** (given/definite
object → split order). This resource supplies the human-side signal that prediction needs:

- The **direction** is a native-speaker fact (definite/given object → split), license-verified and
  textbook-robust.
- The **covariates a clean probe must hold constant** are named in the same source's factor inventory:
  object **length** (avoid confounding givenness with weight), object **type** (avoid pronouns —
  pronominal objects are near-categorically split, a categorical not graded contrast), **concreteness**,
  **animacy**, and **VP idiomaticity**. A clean givenness probe neutralizes these so any preference shift
  is attributable to information status.
- The **shape** the project's validated graded-forced-choice indicator produces (distribute 100 points by
  naturalness between the two orders) is a preference contrast; the anchor licenses the effect's
  **direction/sign**, not a per-item magnitude match.

## What it cannot ground on its own

- **A per-item human gradient** to regress the panel against. The source reports aggregate monofactorial
  correlation coefficients on writing corpora, not a per-item human-rated gradient, and releases no
  openly-licensed per-item data file. So the direction is anchorable now; a per-item gradient is
  contingent on a separate license-verified dataset scout (**verified null 2026-07-14**: the classic
  gradient corpora — Gries 2003; Grafmiller & Szmrecsanyi 2018 — are paywalled / carry no verifiable open
  license and are not adopted) — mirroring the dative and genitive lines, where the direction was the
  adopted primary and a per-item gradient an unrealized upgrade.
- **A surface-frequency-vs-givenness separation.** The direction fact alone does not certify that a
  panel's definite→split shift is information-structural rather than a shadow of the higher corpus
  frequency of definite-object split-order strings; that separation is the probe's **load-bearing
  control** (a byte-identical discourse-givenness firewall arm + a frozen surface-collocation covariate),
  surfaced in the open design decision, not something this resource settles.
- **Model representations** — only a behavioural probe.
- **Human-*level* competence** — only whether the panel tracks the human *direction*.

## Known limits / cautions

- **Provenance is a direction restatement, not a fresh rating experiment.** Unlike the genitive's Dubois
  anchor (25 native raters), this anchor is a CC-licensed restatement of the established native-speaker
  direction (via Gries 1999), corroborated on the paper's own native ICE-GB corpus. The direction is
  robust and uncontroversial, but the anchor grounds only the **sign** — recorded here and in the open
  decision as a modesty caveat the ratification must weigh.
- **Definiteness vs discourse-givenness.** The verbatim anchor is about the object's **determiner**
  (a/the); the probe's shortcut-immune firewall arm manipulates **discourse-givenness** with the object
  string held byte-identical. These are two operationalizations of the same information-status construct
  (definiteness marks givenness); the one-step link is stated openly in the design, and the anchored
  direction is the definiteness one.
- **Avoid pronominal objects.** Pronoun objects are near-obligatorily split (*pick it up*, not
  *?pick up it*) — a categorical grammatical fact, not the graded soft preference under test. The probe
  uses **full lexical NP** objects only.
- **Contamination.** The source's example items may sit in training data; a clean probe uses **synthetic
  minimal pairs** built to the construction (the source anchors the *givenness → order* relation, not
  specific items), as the dative / genitive / AANN held-out designs did.
