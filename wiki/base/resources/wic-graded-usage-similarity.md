---
type: resource
id: wic-graded-usage-similarity
title: Usim graded usage-similarity ratings (Erk, McCarthy & Gaylord) — with WiC as the binary cross-check
status: external-only
url: https://www.katrinerk.com/graded-sense-and-usage-annotation
url-note: "Erk's graded-sense/usage-annotation page links a download of both the usage-similarity (Usim) and graded-sense (WSsim) datasets; a second mirror, http://www.dianamccarthy.co.uk/downloads/WordMeaningAnno2012/, returned HTTP 503 on 2026-05-29 and could not be inspected this run"
paper: "ACL 2009 https://aclanthology.org/P09-1002/ ; journal version Computational Linguistics 39(3):511-554, 2013 https://aclanthology.org/J13-3001/ (MIT Press https://direct.mit.edu/coli/article/39/3/511/1437/ — paywalled, returned HTTP 403 on 2026-05-29)"
venue: "Usim: Erk, McCarthy & Gaylord, ACL 2009 / Computational Linguistics 2013. WiC cross-check: Pilehvar & Camacho-Collados, NAACL 2019, https://aclanthology.org/N19-1128/"
meaning-senses:
  - distributional
  - referential
  - human-comparison
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: anchors
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# Usim graded usage-similarity ratings (with WiC as the binary cross-check)

This page catalogs a candidate human anchor for the project's first **lexical** finding: the **Usim usage-similarity** ratings of Erk, McCarthy & Gaylord. The load-bearing property — the whole reason this resource is catalogued rather than the more famous WiC — is that Usim carries **graded** (not binary) human judgments of how similar two usages of the same word are. That graded signal is exactly what the gradience hypothesis in [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) needs and what a binary set like WiC cannot supply (see the seed [`open-question/lexical-polysemy-gradience`](../../findings/open-questions/lexical-polysemy-gradience.md), which flags that "WiC alone (binary) underdetermines" the gradience question).

The resource is **not yet mirrored or inspected in-repo** (`status: external-only`); the download/README pages could not be read this run (see *Known limits*). The catalog below is built from the abstracts, the published descriptions, and secondary summaries that were reachable; figures that could not be verified from a primary fetch this run are flagged inline.

## What it is

**Usim (usage similarity).** A human-rated dataset in which annotators judge, on a **graded 5-point scale**, how similar two usages (two sentence contexts) of the *same* target lemma are — without first committing to a discrete sense label. The scale runs from "completely different" usages to "identical" usages, with intermediate points (verified phrasing of the scale endpoints: 1 = completely different … 5 = identical; the exact mid-point wording should be re-confirmed against the primary paper before any item is quoted). The dataset was introduced in:

- Katrin Erk, Diana McCarthy & Nicholas Gaylord, *Investigations on Word Senses and Word Usages*, ACL 2009 (https://aclanthology.org/P09-1002/), and developed in the journal version,
- Katrin Erk, Diana McCarthy & Nicholas Gaylord, *Measuring Word Meaning in Context*, Computational Linguistics 39(3):511–554, 2013.

Scope figures (from a secondary summary, **not** verified against a primary fetch this run — flagged for re-check): on the order of ~11 lemmas, with 50 sentences for eight of them (sampled from SemCor and SemEval-3) and 10 sentences each for three more (from the lexical-substitution data), giving roughly 430 usage-pair items, each rated by **three** annotators. The companion **WSsim** dataset in the same release has annotators rate the applicability of *each WordNet sense* to a usage on a graded scale (rather than picking one winner), which is the second graded signal in the release.

The paper's headline finding — that these graded annotations **weaken the case for clear-cut sense boundaries** — is itself the lexicographic gradience claim the conjecture proposes to test in an LLM. (Abstract not quotable verbatim this run; see *Known limits*. Citing the finding here is by paraphrase, flagged as needing a verbatim quote once a primary source page is created.)

**WiC (Word-in-Context), the binary cross-check.** Pilehvar & Camacho-Collados, NAACL 2019 (https://aclanthology.org/N19-1128/). Each instance gives a target word (a noun or verb) in two sentence contexts; the task is a **binary** judgment:

> "The task is to identify if the occurrences of *w* in the two contexts correspond to the same meaning or not." (pilehvar.github.io/wic, task description; verbatim)

with labels **T** (same meaning) / **F** (different). It is expert-curated from Wiktionary, WordNet and VerbNet, and is released under **CC BY-NC 4.0** (verified from pilehvar.github.io/wic, 2026-05-29). WiC is the cleanest *binary* same/different-sense behavioral target — but it is binary by design, so it can ground the discrete-collapse contrast and a same/different baseline, **not** the gradience (monotonicity-in-relatedness) prediction.

## What it can ground — and the specific feature that bears

This is the key section (charter rule: cite a resource by the *feature* that bears, not by existence).

- **Usim grounds the gradience prediction.** Because Usim ratings are a **continuous-ish 5-point graded human judgment of usage similarity**, they let one ask whether an LLM's same/different-sense behavior (or a representational similarity signal) is **monotonic in the human-rated similarity** of two usages — the load-bearing test for hypothesis 1 (graded-sense tracking) in [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md). This is the property no binary set has.
- **WiC grounds the discrete contrast and a same/different baseline.** Its binary T/F labels anchor the discrete-sense behavior (hypothesis 2) and give a clean, large, well-known reference point for a same/different-sense behavioral probe.
- **Both are `human-comparison` anchors** for a `distributional`-vs-`referential.sense` question: usage similarity / same-meaning judgments are human `referential.sense` (Fregean mode-of-presentation) signals, and the conjecture's null is that LLM behavior reduces to context-similarity (`distributional`).

Together they let the conjecture's **discriminating control** be set up: hold context-similarity roughly constant while letting human-rated sense relatedness vary (Usim's graded scale supplies the relatedness axis; a separate context-overlap measure supplies the distributional axis), so the distributional-shadow hypothesis is separable from genuine sense-relatedness tracking.

## What it cannot ground

- **Reference / extension.** Like every resource in-repo, these carry no human-agreed *extension* or reference relation (see [`concept/referential-meaning`](../concepts/referential-meaning.md) on the standing reference-anchor gap); they bear on `referential.sense`, not `referential.reference`.
- **Over-/under-splitting against a full sense inventory.** That comparison needs a discrete sense inventory (WordNet) and a sense-tagged corpus (SemCor / OntoNotes), which are on the resources shortlist ([`index.md`](../../index.md)) but not catalogued here. Usim deliberately *avoids* committing to a discrete inventory, so it cannot by itself answer the over-/under-splitting question; WSsim (sense applicability) is the closer instrument for that.
- **Polysemy-vs-homonymy contrast out of the box.** Usim rates usage similarity but does not itself tag which pairs are polysemy vs. homonymy; building that contrast requires adding a polysemy/homonymy stratification (e.g., from a dictionary or from WordNet sense-relatedness), which is an extra annotation step, not a property of the released ratings. The conjecture should treat that stratification as work-to-be-done, not as given by this resource.

## Known limits

- **External-only; not inspected this run.** The Erk graded-sense download page (katrinerk.com) was reachable as a landing page but the actual data/README was not opened; the McCarthy mirror (dianamccarthy.co.uk/.../WordMeaningAnno2012/) returned **HTTP 503** and the MIT Press journal page returned **HTTP 403** on 2026-05-29. So the **license** of the Usim data, the exact file format, and the precise lemma/item counts were **not verified from a primary source this run**. Treat the scope figures (~11 lemmas, ~430 items, 3 annotators, SemCor/SE-3/LEXSUB sources) as **provisional pending in-repo inspection**; they come from a secondary summary.
- **No verbatim abstract quote secured.** The "weakens the case for clear-cut sense boundaries" finding is paraphrased, not quoted verbatim, because the abstract could not be fetched cleanly. A future run should secure a verbatim quote + locator before this finding is cited in a `claim`/`result`.
- **Small N.** Usim is on the order of hundreds of items over ~11 lemmas; any per-lemma graded claim carries wide uncertainty. It is a *gradience-signal* anchor, not a large-coverage benchmark.
- **WiC is binary.** Re-stated because it is the trap the seed warns about: do not use WiC to ground the gradience (monotonicity) claim; use it for the binary/discrete contrast only.
- **Two graded sub-datasets, distinct roles.** Usim (usage-pair similarity) and WSsim (per-sense applicability) are different instruments; a probe should name which it uses. This page anchors primarily on **Usim** (usage similarity) as the cleanest graded usage-relatedness signal.

## Pointer for next visit

1. Inspect the actual Usim release (retry the katrinerk.com download and the dianamccarthy.co.uk mirror; check the license and file format) and **mirror into `experiments/data/usim/`** (not the wiki) if the license permits; otherwise work against it in place.
2. Verify the scope figures (lemma count, item count, annotator count, source corpora) and the **exact 5-point scale wording** character-for-character; replace the provisional figures above and secure a verbatim abstract quote for the "clear-cut sense boundaries" finding.
3. Decide and queue the **anchor decision** for [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md): is Usim (graded) the ratified gradience anchor, with WiC as the binary cross-check, or is a different graded set preferred? (The conjecture currently marks its anchor as a candidate, not ratified.)
4. Add WordNet + SemCor/OntoNotes as their own resource page(s) if/when the over-/under-splitting arm of the conjecture is pursued.
