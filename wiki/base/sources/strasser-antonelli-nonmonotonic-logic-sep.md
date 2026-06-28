---
type: source
id: strasser-antonelli-nonmonotonic-logic-sep
title: "Strasser & Antonelli, \"Non-monotonic Logic\" (Stanford Encyclopedia of Philosophy) — the monotony property, defeasible inference, and defaults overridden by more specific information"
authors:
  - Strasser, Christian
  - Antonelli, G. Aldo
year: 2024
venue: "The Stanford Encyclopedia of Philosophy (Winter 2024 Edition), Edward N. Zalta & Uri Nodelman (eds.)"
url: https://plato.stanford.edu/entries/logic-nonmonotonic/
access: open-access
meaning-senses:
  - inferential
status: received
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: concept/inferential-meaning
---

# Strasser & Antonelli 2024 — "Non-monotonic Logic" (Stanford Encyclopedia of Philosophy)

## What it is

The Stanford Encyclopedia of Philosophy (SEP) survey entry on **non-monotonic logic**, by **Christian Strasser** and **G. Aldo Antonelli**. First published Tue Dec 11, 2001; substantive revision Sat Nov 23, 2024. SEP is **open-access** (free to read, no paywall). It is a reference-quality survey of the formal study of **defeasible reasoning**: inference in which a conclusion drawn from a body of premises may be *retracted* when further premises are added — the failure of the classical structural property **monotony** (more premises ⇒ at least the same conclusions). The entry organizes the field's families of systems (default logic, circumscription, inheritance networks, the KLM/preferential-semantics program, autoepistemic logic) and the abstract metatheory of non-monotonic consequence relations.

This is a formal-logic / philosophy-of-logic source about a **formal framework**. It makes no claim about LLMs and provides no human-annotated dataset. The project uses it only to fix the formal vocabulary of monotone accumulation vs. defeasance; see *Bearing on this project*.

## A survey/tertiary source, not the primary research (read this first)

This page summarizes the **SEP survey entry**, a *tertiary/survey* source. **All quotes below are reproduced as they appear in the SEP entry by Strasser & Antonelli**, and the project records them at **encyclopedia-survey strength** — at the strength of a reference survey reporting and organizing the field, **not** as a primary ingestion of the founding research papers. The primary literature the survey is *about* — above all **Reiter's "A Logic for Default Reasoning" (1980)** (Default Logic), **McCarthy's circumscription** papers (1980, 1986), **McDermott & Doyle's non-monotonic logic** (1980), and the **Kraus–Lehmann–Magidor (KLM, 1990)** preferential-semantics framework — are journal-/proceedings-walled and are **not in-repo**. So the monotony/non-monotony definition, the notion of defeasible inference, and the specificity-override picture are recorded here at the strength of *a reference survey reporting the field*, with section locators into the SEP entry, **not** at the strength of the founders' own prose. This mirrors how the project has handled other SEP entries (e.g. [`source/janssen-zimmermann-montague-semantics-sep`](janssen-zimmermann-montague-semantics-sep.md)): the entry discharges the *characterization* gap, it does not stand in for the primary texts.

## Provenance and what was verified

Author names (Christian Strasser and G. Aldo Antonelli), first-published date (Tue Dec 11, 2001), and substantive-revision date (Sat Nov 23, 2024) were read from the entry and confirmed against SEP's author/citation information. SEP entries are not paginated; section numbers/names are the locators. The passages below were fetched from the dated **Winter 2024 archived edition** (`https://plato.stanford.edu/archives/win2024/entries/logic-nonmonotonic/`, a frozen URL) on 2026-06-28 and re-fetched to confirm the wording with no ellipses or paraphrase; **every sentence quoted below came back character-for-character identical.** The mathematical symbols (Σ, φ, ⊨, ∪, ′) are reproduced as they appear.

## Key passages (verbatim)

### (a) The field and defeasible reasoning — what NML models (Introduction)

> "Non-monotonic logic (NML) is a family of formal logics designed to model and better understand defeasible reasoning."

> "Reasoners draw conclusions in a defeasible manner when they retain the right to retract these inferences upon the acquisition of further information."

### (b) The monotony property, stated formally (§1 Dealing with the dynamics of defeasible reasoning)

The property classical entailment has and non-monotonic consequence lacks:

> "Monotony: If Σ ⊨ φ then also Σ ∪ Σ′ ⊨ φ."

> "Monotony states that consequence sets are robust under the addition of information: If φ is a consequence of Σ then it is also a consequence of any set containing Σ as a subset."

### (c) Non-monotonicity — adding information can retract a conclusion (§1)

The defining failure: consequences need not survive new (conflicting) premises.

> "they have non-monotonic consequence relations for which consequences may not persist when new information is obtained."

> "the premises support the conclusion defeasibly, e.g., the conclusion may hold in most/typical/etc. cases in which the premises hold."

### (d) Defaults overridden by more specific information (§3.2 Inheritance networks)

The "typically / for the most part" default, and the specificity-override rule that retracts it:

> "In such a network, links of the form A → B represent the fact that, typically and for the most part, As are Bs, and therefore the information about As is more specific than the information about Bs. More specific information overrides more generic information."

## Bearing on this project / what it can and cannot ground

**It can ground the FORMAL vocabulary** the project's monotonicity-asymmetry framing uses — upgrading that mapping from "analogy only" to "grounded in a survey source":

- **[`conjecture/constructional-monotonicity-asymmetry`](../../findings/conjectures/constructional-monotonicity-asymmetry.md) — the principal connection.** That conjecture casts the recurring add-vs-cancel pattern as a *monotonicity* asymmetry: adding a construction-contributed entailment is **monotone accumulation** (content layered on, nothing retracted), while cancelling a verb's lexical default is a **defeasibility operation** (the default is a defeasible inference the construction overrides). Its *Provenance and what is not claimed* section currently holds that mapping "as analogy" because "no in-repo source treats the LLM-defeasance connection" and flags that "a defeasible-reasoning / non-monotonic-logic reference should be fetched first." This source supplies exactly that reference: the formal definition of **monotony** (§1, passage b) is the property "add only accumulates" instantiates; the **defeasible / retraction-on-new-information** characterization (Introduction and §1, passages a, c) is the property "cancel a default" instantiates; and the **specificity-override of a "typically/for the most part" default** (§3.2, passage d) is the formal analogue of a construction overriding a verb's lexical-default entailment. The conjecture's *formal vocabulary* is now grounded in a citable in-repo survey — the mapping moves from "analogy only" to "grounded in a survey source." (The conjecture's empirical content — *that current LLMs are better at the monotone direction* — is untouched by this source and remains a forward bet.)
- **[`concept/inferential-meaning`](../concepts/inferential-meaning.md).** The entry is about inference relations (consequence, entailment, defeasible support), the inferential sense of meaning; it supplies the monotone-vs-non-monotone distinction that page can reference.
- **[`essay/predictive-objective-favors-accumulation`](../../findings/essays/predictive-objective-favors-accumulation.md).** The essay's "accumulation vs retraction" framing can now cite a formal source for the monotone/non-monotone distinction it leans on; the essay's *original argument* (why a predictive objective would favor accumulation) needs no anchor, but its use of the formal monotonicity vocabulary rests on this survey.

**It cannot ground:**

- **Any empirical claim about LLMs, and no human anchor.** This is a formal-logic survey with no labeled resource. It **grounds the THEORY / framing** (the formal vocabulary the conjecture and essay use), and like other theory-source pages it **never discharges a result's human-anchor obligation**: it cannot serve as the `anchors:` resource for any `claim` or `result` about model behavior. The conjecture's matched-difficulty generalization test still needs its own human anchor (the Scivetti CxNLI dataset, as that page notes); this source does nothing to supply one.
- **The claim that LLM cancellation *is* a non-monotonic inference in the technical sense.** The source defines non-monotonicity for formal consequence relations; whether an LLM's failure to suppress a lexical default is *literally* a non-monotonic consequence operation, versus a distributional-prior effect that merely *resembles* one, is the conjecture's own open question (its *Mechanism* section, labeled speculation), not something this source settles. The page licenses the **vocabulary**, not an identification of mechanism.
- **The primary research.** Reiter's Default Logic (1980), McCarthy's circumscription (1980/1986), McDermott & Doyle (1980), and the KLM preferential-semantics framework (1990) are summarized by this survey but are **not in-repo**; this page carries the survey's characterization of them, not their own prose.

## Honest gaps

- **A survey, not the primaries.** Anything needing the founding formal systems *verbatim* — Reiter's default-rule notation and extension semantics, McCarthy's circumscription as second-order minimization, the KLM rationality postulates (Cautious Monotony, Cut, etc.) as originally stated — still requires the primary papers, which stay on the wanted backlog. This page records only the survey's organizing characterization.
- **No bridge to lexical/constructional defaults.** The entry's "typically / for the most part" defaults are about taxonomic inheritance (birds fly, bats are exceptional), not about a *verb's lexical-aspect default* that a construction defeases. The mapping from "specificity override in an inheritance network" to "the conative frame overriding *kick*'s completed-contact default" is the project's own analogy; the source supplies the *formal* template, not the lexical-semantic application.
- **Does not adjudicate the deflationary reading.** The survey is neutral on cognition; it cannot say whether retraction "works against" a predictive objective (the conjecture's *Mechanism* speculation). That bridge stays the project's own, untested.

## Status in wanted.md

New ingestion (2026-06-28), filling the queued [P3] want for a non-monotonic / defeasible-reasoning reference flagged by [`conjecture/constructional-monotonicity-asymmetry`](../../findings/conjectures/constructional-monotonicity-asymmetry.md) (its *Provenance* note that such a reference "should be fetched first" before the project leans formally on the monotonicity framing). Authors (Christian Strasser, G. Aldo Antonelli), edition (Winter 2024), first-published (Tue Dec 11, 2001) and substantive-revision (Sat Nov 23, 2024) dates verified; the key quotes above are verbatim-confirmed. Open-access confirmed. The **primary literature** — **Reiter 1980** (Default Logic), **McCarthy 1980/1986** (circumscription), **McDermott & Doyle 1980**, **KLM 1990** — remains **not in-repo** and stays on the backlog; this survey is encyclopedia-survey strength and does not replace them.
