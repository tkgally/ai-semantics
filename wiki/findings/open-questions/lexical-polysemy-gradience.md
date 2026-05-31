---
type: open-question
id: lexical-polysemy-gradience
title: Does LLM lexical-sense behavior exhibit the graded polysemy lexicographers document, or collapse to discrete senses?
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: open
created: 2026-05-29
updated: 2026-05-31
links:
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
  - rel: refines
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/lexical-polysemy-homonymy-v2
  - rel: depends-on
    target: result/lexical-polysemy-homonymy-v3
  - rel: depends-on
    target: resource/wic-word-in-context
  - rel: depends-on
    target: resource/wordnet-sense-inventory
  - rel: depends-on
    target: resource/dwug-usage-graphs
---

# Open question: graded polysemy vs. discrete sense in LLMs

> **Update / what landed (2026-05-31) — largely answered by the lexical line; one sub-arm stands as a powered null.** This seed question spawned [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md), which has since been tested across three results. The headline (hypotheses 1 vs 2 below): **graded-sense tracking IS present, not a collapse to discreteness.** [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md) found every panel model's graded sense-relatedness rating **monotonic in the human DURel median** (Spearman 0.60–0.83, in/above the human inter-annotator range ≈0.69), and this monotonicity **survives a context-similarity control** — so hypothesis 3 (the **distributional shadow**) is ruled out as the whole story (clauses a + c). The **distinctive sub-question** — whether the model treats homonymy as a *separate discrete regime* beyond graded distance (hypothesis 2 as a positive prediction, conjecture clause b) — is **not established**: [`result/lexical-polysemy-homonymy-v2`](../results/lexical-polysemy-homonymy-v2.md) found it untestable at the DWUG anchor (only 3 clean homonym lemmas; bimodality precondition unmet), and [`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md), run on a homonymy-enriched WiC noun subset, returned a **powered null** on the discreteness-separation test (rating separates same/different equally well for homonyms and polysemes, AUC diff ≈ 0). The one positive — homonym different-sense pairs floored more — **cannot be distinguished from plain graded distance** (a single continuous relatedness axis, with homonyms further out, predicts exactly this; the discreteness/graded-distance confound is intrinsic to a lemma-level WiC contrast). So the model behaves as a **graded sense tracker with no demonstrated extra discrete homonymy regime** — consistent with the lexicographer's gradience picture, but the bimodal "discrete floor for homonyms vs intermediate band for polysemy" is *not* shown. **Kept open** (Tom's call, 2026-05-31), though largely addressed: the core graded-vs-discrete question this page poses is resolved in the graded direction with a real human anchor; the residual discrete-regime sub-arm is tracked on the conjecture/result pages as a powered null (not falsified). The over-/under-splitting arm (model sense inventory vs a human inventory) was deliberately **not** carried by the conjecture and remains untouched. (Status note: Tom elected 2026-05-31 to keep this question **open** rather than "answered", because the distinctive discrete-regime sub-arm is a *powered null, not a positive resolution* — so the question is held live for a future clause-(b) test on a graded, homonymy-enriched anchor.)

## The question

Every finding in this project so far is **grammatical / constructional**. The charter scopes the project to "lexical *and* grammatical meaning" ([`PROJECT.md`](../../../PROJECT.md) §1) and names a standing asset the field underuses: "a lexicographer's tolerance for fine-grained polysemy and sense-distinction … The debate tends to be coarse; the gradiness is the point." The lexical axis is currently empty. This question opens it on exactly that asset.

Lexicographers treat word sense as **graded**: the senses of a polysemous word (*paper* = material / newspaper / academic article; *run* across dozens of related uses) shade into one another, with bridging contexts where two senses are co-present and judgments are genuinely intermediate — unlike homonymy (*bank* = riverside / financial), where senses are discrete and unrelated. The question: **does an LLM's in-context sense behavior reproduce this gradience, or does it collapse polysemy toward discreteness (treating related senses as either identical or as sharply separate as homonyms)?** And does the model's implicit sense inventory align with, over-split, or under-split a human sense inventory?

This is a `distributional`-vs-`referential.sense` question: distributional structure gives sense-in-context for free (different contexts → different neighborhoods), but whether that structure carries the *graded* sense relations a lexicographer documents — Frege's `Sinn` at fine grain — is exactly the contested boundary ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), [`concept/referential-meaning`](../../base/concepts/referential-meaning.md)).

## Why it matters

- It is the project's first **lexical** wedge, complementing the constructional wedge, and the one place the lexicographer asset the charter highlights is directly in play.
- It is tractable with existing human-annotated resources (below), so it does not require new human-subject data (charter §8).
- The gradience framing is a genuine contribution angle: most LLM word-sense work uses *discrete* sense inventories (WordNet synsets) and asks for classification accuracy; the lexicographically interesting question — whether the model tracks **graded** relatedness and bridging contexts — is comparatively under-probed.

## What a serious answer would look like

A design that distinguishes three hypotheses:
1. **Graded-sense tracking** — the model's same-sense / different-sense behavior is *monotonic in human-rated sense relatedness*: intermediate for bridging/polysemous contexts, high for same-sense, low for homonyms. (The lexicographer's picture.)
2. **Discrete-sense collapse** — behavior is near-binary, with polysemous-but-related uses treated as sharply same or different, no intermediate regime distinguishing polysemy from homonymy.
3. **Distributional shadow** — apparent sense-tracking reduces to context-similarity (the two contexts' overall lexical overlap), not to sense relatedness per se — the lexical analogue of the constructional `distributional` null that runs through this repo.

Discriminating moves: hold context-similarity roughly constant while varying sense relatedness (polysemy vs. homonymy vs. same-sense) so hypothesis 3 is separable from 1; include **bridging contexts** (engineered to be sense-ambiguous) and test for an intermediate regime; compare the model's induced sense splits against a human sense inventory for over-/under-splitting.

## Human anchors (now mostly in-repo)

The candidate anchors this page originally listed as "none in-repo yet" have since been catalogued and used (anchor decision resolved 2026-05-29 → Option B; see the conjecture):

- **WiC — Word-in-Context** (Pilehvar & Camacho-Collados 2019): human **binary** same-sense/different-sense labels (lexicographer-inventory-derived) for a target word across two contexts. **Now in-repo and verified:** [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md) (CC BY-NC 4.0; 7,466 items, 50/50 balanced; negatives **homonymy-enriched** — closest-polyseme pairs pruned). It anchored the clause-(b) discreteness test [`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md). Binary, **not** graded — it grounds same/different separation, never a graded monotonicity claim.
- **Graded usage-similarity data** — the resource type bearing on hypothesis 1 (gradience). **Now in-repo:** [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) (DWUG, Schlechtweg et al.; CC BY-ND 4.0; graded 4-point DURel judgments) was the ratified Option-B graded anchor and grounds the v1 monotonicity result. The originally-named Usim (Erk, McCarthy & Gaylord) was *retired* as the anchor — its content fit but its released file is unfetchable / unlicensed (catalogued at [`resource/wic-graded-usage-similarity`](../../base/resources/wic-graded-usage-similarity.md)). **Still genuinely wanted:** a *second* graded, fetchable, licensed usage-similarity set — CoSimLex was evaluated and **rejected on design fit** (it rates *different-word* pairs in context, not two usages of the *same* lemma), so DWUG remains the sole graded anchor and a homonymy-enriched *graded* set (which neither DWUG nor WiC supplies) is the open want for a clean clause-(b) test that holds graded distance constant.
- **WordNet** (sense inventory) for the over-/under-splitting comparison. **Now in-repo:** [`resource/wordnet-sense-inventory`](../../base/resources/wordnet-sense-inventory.md) (Princeton WordNet 3.0; permissive license; 117,659 synsets). **SemCor / OntoNotes** (sense-tagged corpora) are still **not** in-repo; the over-/under-splitting arm was never carried by the conjecture and remains unprobed.

The chosen resources were catalogued by the feature that actually bears (the charter's verify-content-not-existence rule), and the anchor decision was opened and resolved — so this page is no longer waiting on an anchor for its central arm. The one still-genuinely-wanted asset is a **graded, homonymy-enriched** set (above), which would let a future run separate a discrete homonymy regime from plain graded distance — the confound that left clause (b) a powered null.

## Relation to the existing wedge

- It is the **lexical counterpart** of the constructional `distributional`-vs-`constructional` tension ([`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md)): there the null is n-gram frequency; here it is context-similarity. Both ask whether a `distributional` shadow explains apparent meaning-tracking.
- It does **not** touch the relational axis ([`open-question/relational-meaning-pilot`](relational-meaning-pilot.md)); it is `model-internal` plus `human-comparison`.
- It did spawn the project's first lexical `conjecture` — [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md), stated almost exactly as anticipated here ("monotonic in human-rated sense relatedness, with an intermediate regime for polysemy absent for homonymy") — now tested (see the Update block above).

## Status: open — largely addressed (history below)

*This section is retained for the record; the question's standing is in the Update block at the top — kept **open** per Tom (2026-05-31), though its central arm is resolved.*

When this page was written it was queued, not active — pending a word-sense-disambiguation / usage-similarity literature read and a fetched, graded, licensed anchor. Both happened: the anchor decision was resolved (Option B → DWUG for the graded arm, WiC as the binary cross-check), the resources were catalogued and verified, and the conjecture's three clauses were probed (v1, v2, v3). Framing the question — fixing the three hypotheses and the context-similarity control — was the deliverable here; the resolution is recorded above and on the conjecture/result pages.

## Residual / pointers for any follow-on

- The one un-probed seed arm is **over-/under-splitting** (model sense inventory vs a human inventory) — never carried by the conjecture; it would need SemCor/OntoNotes (still not in-repo) alongside the now-in-repo [`resource/wordnet-sense-inventory`](../../base/resources/wordnet-sense-inventory.md).
- The clause-(b) discrete-regime sub-arm is a **powered null**, not a falsification; a cleaner test would need a **graded, homonymy-enriched** set that holds human graded distance constant across strata (the intrinsic confound WiC's lemma-level labels cannot remove). That is the standing want, not a defect of the work done.
- The representation-locus variant (graded sense *representations*, small-model lane) remains deferred on local compute; v1–v3 are all behavioral.
