---
type: source
id: azin-2026-presupposition-conditionals
title: "Presupposition and Reasoning in Conditionals: A Theory-Based Study of Humans and LLMs"
authors:
  - Azin, Tara
  - Yu, Yongan
  - Singh, Raj
  - Jouravlev, Olessia
year: 2026
venue: "Proceedings of CoNLL 2026 (colocated with ACL 2026), to appear; arXiv 2605.18352"
url: https://arxiv.org/abs/2605.18352
access: open-access
meaning-senses:
  - inferential
  - distributional
  - human-comparison
status: received
created: 2026-07-18
updated: 2026-07-18
links:
  - rel: refines
    target: concept/inferential-meaning
  - rel: supports
    target: essay/projection-defeasible-by-frame
---

# Azin, Yu, Singh & Jouravlev 2026 — Presupposition and Reasoning in Conditionals

## What it is

A four-author cognitive-science / computational-linguistics paper (to appear, CoNLL 2026) that runs a
**parallel behavioral study comparing human judgments and LLM predictions** on presupposition
projection in conditionals. Its target is the **proviso problem** (Geurts 1996): how a presupposition
*triggered in the consequent* of a conditional is interpreted — either **unconditionally** ("*If John
flies to London, his sister will pick him up* presupposes that John has a sister") or **conditional on
the antecedent** — and how that reading is modulated by the **relevance** of the antecedent to the
presupposed content. The authors build a small **normed dataset** of conditional sentences that crosses
antecedent–presupposition relevance (relevant / somewhat relevant / irrelevant) with proposition
probability (low / mid / high) derived from a norming study, collect **likelihood ratings from 120
human participants and four LLMs** on a matched 0–7 scale, and additionally probe each model's
chain-of-thought with a theory-informed checklist inside an **LLM-as-a-Judge** framework.

Two headline results: (1) **humans "integrate probabilistic and pragmatic cues"** whereas **"LLMs show
variable alignment with human patterns"** — the models' Spearman correlations with the human ranking
are weak-to-moderate at best (see below); (2) a **dissociation** — the model **best aligned** with
human ratings (Qwen2.5-7B-IT) has the **lowest** compliance with the pragmatic-reasoning checklist,
while models with more theory-consistent reasoning (the proprietary models) deviate *more* from human
ratings — from which the authors conclude that LLM "performance on such tasks may result from
**surface pattern matching rather than pragmatic competence**."

This is an **external empirical, human-vs-LLM** study on a **partially-overlapping model set** (GPT-5,
Gemini-2.5-flash, and two small open-source instruct models — Llama-3.1-8B, Qwen2.5-7B — **not** the
project's frontier panel, and with **no claude subject**; claude-haiku-4-5 appears only as the
LLM-as-a-Judge scorer). Like [`source/guo-2026-statistical-preemption`](guo-2026-statistical-preemption.md),
[`source/mosolova-2025-wsi-unsolved`](mosolova-2025-wsi-unsolved.md) and
[`source/rakshit-goldberg-2025-meaning-infused-grammar`](rakshit-goldberg-2025-meaning-infused-grammar.md),
it is catalogued as a **companion / counterpoint source, NOT a human anchor, with no transfer to the
frontier panel**. Its value here is (i) external corroboration, on a distinct conditional-presupposition
configuration, of the reading that LLM presupposition behavior looks like surface-cue-following rather
than computed pragmatics — resonant with [`essay/projection-defeasible-by-frame`](../../findings/essays/projection-defeasible-by-frame.md)
and [`essay/shortcut-vs-competence-mis-cut`](../../findings/essays/shortcut-vs-competence-mis-cut.md);
and (ii) a **new candidate human-projection dataset** for the project's long-open projection-anchor gap
([`resource/presupposition-projection-human-anchor-scouting`](../resources/presupposition-projection-human-anchor-scouting.md),
program item A3a) — recorded there as candidate 5, **license UNVERIFIED**, **not adopted** (see "What
it cannot ground").

## ⚠ Configuration caveat — the proviso cell is NOT the project's headline cell

**Read before wiring.** The project's headline conditional finding
([`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md),
[`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md)) is the
collapse of projection when the presupposition trigger sits in the **antecedent** of a conditional
("*If* [trigger], …"). Azin et al. study the **proviso** configuration: the trigger sits in the
**consequent** ("If A, [trigger]…"), and the question is whether that consequent-triggered
presupposition is read unconditionally or gets *conditionalized on the antecedent*, modulated by A–p
relevance. These are **adjacent but structurally distinct** cells of "conditional presupposition
projection." So this paper is a **companion** on the same broad phenomenon, **not** an item- or
environment-matched corroboration of the project's antecedent collapse, and **must not** be cited as
though it replicated that specific result. (The project's own `conseq`-position arm in
`conditional-projection-rescue-v1` is the closer analogue, but it manipulates trigger position, not
antecedent relevance, and is not the proviso task.)

## Provenance

Title, full author list (Azin & Singh & Jouravlev — Carleton University, Dept of Cognitive Science; Yu
— McGill / Mila), venue ("To appear in the Proceedings of CoNLL 2026, colocated with ACL 2026"), and
the **abstract** were fetched and verified firsthand against the arXiv abstract page
(https://arxiv.org/abs/2605.18352) on 2026-07-18; the abs page declares the license
**CC BY 4.0** (`creativecommons.org/licenses/by/4.0/`, verified in the page source; the string "License:
CC BY 4.0" also appears in the HTML full text). Body quotes were extracted from the arXiv HTML
rendering (https://arxiv.org/html/2605.18352) and each load-bearing string below was confirmed
character-for-character present in a local fetch of that HTML. Locators are the paper's own section
numbers (§-numbers, not pages — the CoNLL camera-ready is not yet in the ACL Anthology). **MathML note:**
per the standing arXiv-HTML caveat, numeric fragments inside math spans are duplicated in a LaTeX
fallback (`ρ = 0.25 \rho=0.25`), so the correlation coefficients below **were** recoverable and are
quoted; the **per-model MAE values** live in a figure (Figure 3) and were **not** text-recoverable, so
MAE is reported only qualitatively (direction as stated in prose), not with specific numbers.

## Abstract (verbatim)

> "Presupposition projection in conditionals is central to theories of meaning and pragmatics, yet it
> remains largely unevaluated in large language models. We address this gap through a parallel
> behavioral study comparing human judgments and LLM predictions on a normed dataset of conditional
> sentences that controls the relation between the antecedent and the projected presupposition. We
> collect likelihood ratings from 120 participants and four LLMs under matched contextual conditions.
> Results show that humans integrate probabilistic and pragmatic cues in their judgment, whereas LLMs
> show variable alignment with human patterns. Using a linguistically motivated checklist within an
> LLM-as-a-Judge framework, we further evaluate model reasoning. We observe models that best match
> human ratings often lack coherent pragmatic reasoning, while models with stronger reasoning produce
> less human-like judgments. These findings suggest that LLMs' performance on such tasks may result
> from surface pattern matching rather than pragmatic competence. Our findings highlight the importance
> of benchmarks grounded in linguistic theory for comparing humans and models."

## The proviso target (verbatim; §1)

> "proviso problem (Geurts, 1996) in presupposition projection, which concerns how presuppositions
> triggered in the consequent of conditionals are interpreted. In some cases, the presupposition is
> clearly understood as unconditional (e.g., If John flies to London, his sister will pick him up
> presupposes that John has a sister). In other cases, however, the presupposition may be understood
> either unconditionally or conditional on the antecedent (e.g., If John is a scuba diver, he will
> bring his wetsuit)."

## Dataset and design (verbatim; §3)

> "90 sentences based on 30 base propositions, each instantiated in three variants that manipulate the
> logical and probabilistic relationship between A and p."

> "four norming conditions: a baseline condition measuring Pr(p∣c) and three conditional criteria
> measuring Pr(p∣A,c) with high, mid, and low A–p relevance antecedents."

The presupposition triggers are **possessive pronouns** ("his, her, their"; stated in the Limitations).
The dataset and code are released at `https://github.com/proviso-bench/Presupposition-and-Reasoning-in-Conditionals`
(Footnote 2) — **license unverified this session** (see below).

## Human study (verbatim; §3.2)

> "120 participants were retained after applying the exclusion criteria (see Appendix A for details)."

Native English speakers recruited via **Prolific**; ratings on a **0–7 Likert scale** ("0 = very
unlikely, 7 = very likely"); a with-context and a without-context condition (60 participants each), all
rating the 90 items. **Both human participants and LLMs receive identical instructions.**

## LLM results (verbatim; §4.3)

The four subject LLMs are **GPT-5, Gemini-2.5-flash, Llama-3.1-8B-Instruct, and Qwen2.5-7B-Instruct**
(all instruction-tuned), each producing a Likert judgment plus chain-of-thought. Item-level alignment
with the human ranking (Spearman ρ):

> "without context: ρ = 0.25, p = .016; with context: ρ = 0.38, p < .001" (Qwen2.5-7B-IT — the
> strongest aligner)

> "Llama3.1-8B-Instruct also showed consistent moderate alignment (without context: ρ = 0.21 …)"

> "Gemini-2.5-flash showed meaningful alignment only when context was provided (ρ = 0.26, p = .013).
> GPT-5 did not show significant overall correlations in either condition."

MAE (Figure 3, reported qualitatively — specific values not text-recoverable): the prose states
**"Llama3.1-8B-Instruct achieved the lowest overall error"** and that the MAE ordering "mirrored" the
correlation pattern. **Note the ceiling:** even the best aligner sits at ρ ≈ 0.25–0.38 — weak-to-moderate,
not strong; the largest models (GPT-5) align *least*.

## The reasoning dissociation (verbatim; §4.4)

> "Qwen2.5-7B-IT is most closely aligned with human Likert ratings across all conditions. However, the
> reasoning results in Table 3 reveal a paradox: Qwen2.5-7B-IT shows the lowest average compliance with
> our theory-informed checklist."

> "This pattern suggests that smaller models approximate human-like response distributions by relying
> on surface-level lexical associations and distributional world knowledge, without consistently
> implementing the formal pragmatic constraints underlying the proviso problem."

> "models that best match human ratings often lack coherent pragmatic reasoning, while models with
> stronger reasoning produce less human-like judgments. These findings suggest that LLMs' performance
> on such tasks may result from surface pattern matching rather than pragmatic competence." (Abstract /
> §4.4)

## What this bears on in-repo

- **[`essay/projection-defeasible-by-frame`](../../findings/essays/projection-defeasible-by-frame.md) —
  `supports` (external, distinct configuration).** The essay's thesis is that the project's conditional
  presupposition behavior is better described as a **frame-conditioned distributional / surface
  regularity** than as a computed presupposition/assertion split — read strictly as a *within-model*
  contrast on the project's panel. Azin et al. supply **independent external evidence pointing the same
  way** on a *different* conditional-presupposition cell (the proviso configuration, human-compared):
  models' human-alignment tops out at ρ ≈ 0.38, the best aligner is the one with the *worst* pragmatic
  reasoning, and the authors' own reading is "surface pattern matching rather than pragmatic
  competence." This is convergent motivation, **not** a replication — the configuration caveat above
  bounds the strength. It does **not** fire any of the essay's revision triggers (those are the
  project's own rescue probe, fired s159, and movement in the project's own result numbers), so the
  essay is **not revised**; the support link records external convergence only.
- **[`essay/shortcut-vs-competence-mis-cut`](../../findings/essays/shortcut-vs-competence-mis-cut.md) —
  thematic echo, NOT a trigger.** The "surface pattern matching rather than pragmatic competence"
  framing rhymes with that essay's warning against a shortcut-vs-competence cut. But that essay's
  revision triggers are specifically about **lexical co-occurrence controls for antonymy**; a
  presupposition-projection paper does not fire them, and Azin's "surface vs competence" is used
  descriptively, not as the mis-cut the essay dissects. Recorded here as resonance only; that essay is
  untouched.
- **[`resource/presupposition-projection-human-anchor-scouting`](../resources/presupposition-projection-human-anchor-scouting.md)
  (program A3a) — a NEW candidate anchor, license UNVERIFIED, NOT adopted.** The proviso-bench release
  is the first *designed, normed, human-rated* conditional-presupposition dataset the project has
  surfaced with the same graded-human-judgment shape the scout wants — added there as **candidate 5**
  with its exact configuration and its unverified license. Cataloguing ≠ adoption (the Cao
  `ProbeResponses` / DAIS precedent): any future adoption is a separate cross-session ratified anchor
  decision, and the configuration caveat means it would anchor the **proviso** question, not the
  project's antecedent-collapse headline.
- **[`concept/inferential-meaning`](../concepts/inferential-meaning.md) — `refines`.** A data point on
  the recurring tension the concept page carries: an ostensibly **inferential** competence (presupposition
  projection) probed behaviorally comes out looking like distributional / world-knowledge pattern-matching
  rather than rule-governed pragmatics — here shown against a *human* baseline, externally.

## What it can ground

- A citation that, in a **human-vs-LLM parallel study on the proviso problem** (presupposition triggered
  in a conditional's consequent, with antecedent–presupposition relevance and proposition-probability
  systematically varied), **humans integrate probabilistic and pragmatic cues** while **LLMs show only
  weak-to-moderate, variable alignment** (best Spearman ρ ≈ 0.25–0.38 for a small open model; **GPT-5
  shows no significant correlation**), and a **dissociation** in which the best human-aligner has the
  worst pragmatic-reasoning-checklist compliance — verbatim as above, on the stated (non-project) model
  set.
- A citation for the **"surface pattern matching vs pragmatic competence"** reading of LLM
  presupposition behavior, from an independent lab, on a distinct configuration — external company for
  the project's frame-conditioned-distributional description of its own conditional collapse.

## What it cannot ground

- **A human anchor (this session).** The proviso-bench dataset's **license is UNVERIFIED** — the repo's
  `LICENSE`, `LICENSE.md`, and `LICENSE.txt` returned **HTTP 404 on both `main` and `master`** in a
  firsthand raw-file check on 2026-07-18 (the GitHub landing page returned 403 through the proxy, so the
  repo's API license field could not be read). The **CC BY 4.0** verified above covers the **arXiv
  paper**, *not* the released data (the NOPE / Cao precedent: paper license ≠ data license). So the
  dataset is **not adopted**; it joins the A3a scout as a license-unverified candidate only.
- **Any claim about the project's frontier panel.** The subjects are GPT-5, Gemini-2.5-flash,
  Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct — **not** the project's panel in
  [`config/models.md`](../../../config/models.md), and **no claude subject** (claude-haiku-4-5 is only
  the LLM-as-a-Judge scorer). No transfer to claude/gemini/gpt-as-subjects is established.
- **Corroboration of the project's antecedent-of-conditional collapse.** Different structural cell
  (proviso / consequent-trigger vs antecedent-trigger). It corroborates a *broad direction* on
  conditional presupposition, not the specific project result — see the configuration caveat.
- **A mechanism claim.** The LLM-as-a-Judge checklist scores *reasoning-step text*, not internal
  computation; "surface pattern matching" is the authors' behavioral reading, not a demonstrated
  mechanism.

## Known limits

- **To appear, CoNLL 2026** (peer-reviewed venue; arXiv v1 at fetch time). Abstract + license verified
  firsthand against the arXiv abs page; body quotes confirmed present in the arXiv HTML full text.
  Locators are §-numbers (no camera-ready pagination yet). Per-model MAE numbers are figure-only and
  not quoted.
- **Small stimulus set and single trigger type.** 90 sentences / 30 base propositions; the triggers are
  **possessive-pronoun** presuppositions only (authors' Limitations) — a narrow trigger inventory
  relative to the project's factive / aspectual / definite / cleft / temporal / focus / quantifier set.
- **Model set is small-open + two proprietary**, English only; the correlations are item-level Spearman
  on a 90-item ranking — modest N by the project's powered-probe standard.

## Status in wanted.md

Firsthand-verified to exist at s249 (arXiv abstract + author list + venue + CC BY 4.0 license
char-checked; dataset-repo license 404-checked firsthand). Was listed among the three unopened
s240-scout candidates (P3, UNVERIFIED). Catalogued 2026-07-18 (session 249) as a **companion /
counterpoint source** on conditional presupposition projection and a **candidate (unadopted) A3a
anchor**; the orchestrating session records it RECEIVED in [`wanted.md`](../wanted.md) and
[`index.md`](../../index.md). The other two scout candidates (Scivetti et al. 2026 paired-focus CxG;
Rhee 2026 referential profiles) remain UNVERIFIED-and-unopened.
</content>
</invoke>
