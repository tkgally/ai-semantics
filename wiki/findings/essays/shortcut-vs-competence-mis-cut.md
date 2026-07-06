---
type: essay
id: shortcut-vs-competence-mis-cut
title: "Shortcut versus competence mis-cuts the disentanglement: the distributional shadow has a local and a transferable grade"
meaning-senses:
  - distributional
  - inferential
  - referential
status: revised
contingent-on: []
created: 2026-06-30
updated: 2026-07-06
links:
  - rel: depends-on
    target: source/cao-2025-distinctive-cooccurrence-antonymy
  - rel: depends-on
    target: source/du-2023-shortcut-learning
  - rel: depends-on
    target: source/diera-2026-encode-semantic-relations
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: essay/antonymy-outlier-distributional-shadow
  - rel: depends-on
    target: essay/two-distributional-hypotheses
  - rel: refines
    target: conjecture/lexical-relation-shadow-saturation
  - rel: depends-on
    target: result/lexical-relation-shadow-saturation-v1
  - rel: refines
    target: theory/lexicon-grammar-continuum
---

# Essay: shortcut versus competence mis-cuts the disentanglement

> **Status: revised (2026-06-30, session 152 — revision trigger (d) discharged: the "shortcut"
> primary Du et al. 2023 is now read and credited; see §"Prior art"). A philosophical-track essay
> arguing in the project's own voice.**
> It introduces **no new empirical claim** and makes **no human comparison of its own**: every
> empirical assertion cites the in-repo `source` page that carries it, at that page's stated
> strength. The original contribution is a **conceptual correction** to the framing the project (and
> the prior art it ingests) has been using for the "opposites" wedge — and a sharpening of what the
> blocked [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md)'s
> control could and could not show if it ever ran. It does not change any in-repo empirical verdict;
> it changes the *interpretation label* attached to a contrast.

> **Update (2026-07-06, s188 — wiki-coherence campaign P5): the conjecture has RUN (s186), and it
> vindicated this essay's reading.** The [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md)
> this essay calls "blocked" **ran at session 186** (via the ratified `internal-contrast-only` route that
> sidesteps the "no adopted human anchor" blocker) →
> [`result/lexical-relation-shadow-saturation-v1`](../results/lexical-relation-shadow-saturation-v1.md).
> Antonym recovery **survived** the contrastive-frame control by a wide margin (HIT@3 residual
> **+0.61–0.67**), and the result page reads that surviving residual **exactly as this essay prescribes** —
> as grading **local vs transferable distributional** generalization, *not* distribution vs
> non-distribution. So this essay's central relabeling is the interpretation the run actually used; its
> "flat residuals" trigger did **not** fire (the residuals were large, not flat). The "blocked" phrasing
> below is the pre-s186 status, superseded and kept visible.

## The framing this essay corrects

When [`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md)
(Cao, Yamada & Tokunaga 2025) connects its corpus finding to language-model behavior, it reaches —
in the authors' own voice — for a particular carving. The distinctive co-occurrence of antonym
pairs, they write, means that "**models might take advantage of those intra-sentential co-occurrence
characteristics, using them as a shortcut Du et al. (2023) rather than relying on knowledge of
antonymy**" (§5), so that "**our findings highlight the need to disentangle the extent to which PLMs
rely on such distributional clues from the extent to which they generalise beyond them**" (§5).

That sentence is, almost word for word, the project's own
[`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md)
stated as a research need by the source's authors — which is exactly why
[`essay/antonymy-outlier-distributional-shadow`](antonymy-outlier-distributional-shadow.md) cites it
as convergent support. The two essays are not in tension. But the shadow essay imports the *cut*
along with the convergence: it registers (revision trigger (a)) that "antonymy competence *surviving*
the control" would force a revision to "shadow plus a measured residual," and the conjecture's
falsifier 1 reads a surviving residual as "**genuine relational structure rather than a cast
shadow**." Both treat the contrast as **shortcut versus competence** — distributional clue-use on one
side, knowledge-of-antonymy over and above distribution on the other.

This essay's claim is that **shortcut-versus-competence is the wrong cut**, and that taking it at face
value mislabels what the project's own control would measure. The correction has a consequence the
shadow essay and the conjecture should carry, stated at the end.

## Why the cut is wrong: the baseline it presupposes is the one the project denies

"Shortcut … rather than relying on knowledge of antonymy" presupposes a baseline of *non-shortcut*
antonymy knowledge — competence that does not run through co-occurrence statistics — against which
leaning on distributional clues is a cheat, a way of *getting the answer without the knowledge*. The
word "shortcut" only does work if there is a longer, more legitimate road.

For a text-trained model, under the very hypothesis this project runs on, there is no such road. The
project's lexical wedge takes meaning, at the lexical-relation level, to be **distributional** in the
[`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) sense — patterns of
co-occurrence and substitution. On that hypothesis, leaning on the contrastive-frame co-occurrence of
*hot/cold* or *open/closed* is not a shortcut *around* knowledge of their opposition; for a system
whose only evidence is text, it is **the substance of whatever lexical-relation competence is
available at all**. A distributional learner that produces the antonym of a cue *is* exercising the
only kind of antonymy knowledge a corpus can confer. To call that a shortcut is to score it against a
standard — knowledge of antonymy that is not distributional — that the distributional hypothesis says
a text model cannot, even in principle, reach by this route. The cut smuggles in a non-distributional
criterion and then faults the model for not meeting it.

This is not a quarrel with disentangling anything. It is a quarrel with the *names*. There is a real
contrast the authors are pointing at; "shortcut versus competence" is a misleading label for it.

## The cut that is well-posed: local versus transferable distributional generalization

Split the word "distributional" the way the antonymy case forces. A model can recover an antonym
because:

1. **Local cue-use** — the specific pair co-occurs densely in the specific contrastive frames the
   training corpus is saturated with, so producing *cold* after *hot* is, to a first approximation,
   completing a frame the corpus handed over directly. This is the leg the in-repo corpus sources
   measure: antonym pairs co-occur "**with high strength, in a preferred linear order, and within
   short spans**" ([`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md),
   Abstract), "**consistently distinctive from all other relations**" (§6).

2. **Transferable generalization** — the model produces the right antonym for a pair, or in a frame,
   where the *local* co-occurrence cue is weak or absent: it has abstracted a contrast structure that
   carries beyond the specific frames seen in training. This too is distributional — it is the Harris
   form-internal contrast measure of
   [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md) *generalizing* — but it
   is not local frame-completion. It has a representational correlate already in the library: Diera &
   Scherp's linear-probing / patching study finds antonymy is encoded as a recoverable internal
   structure — "**antonymy easiest**", "**antonymy approaches ceiling on Llama**"
   ([`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md),
   §4.1) — i.e. a learned contrast *direction* that can be read off activations rather than a
   per-pair lookup. A direction that generalizes across pairs is transfer; it is still distributional.

Both grades are distribution. The difference between them is **how local** the cue is — frame-bound
completion versus an abstracted contrast that travels. That is the cut "shortcut versus competence"
was groping for, and naming it correctly matters, because the two ends are not "no knowledge" and
"real knowledge"; they are **two grades of the same distributional achievement**, the second more
impressive than the first but no less a creature of the corpus.

## The consequence the shadow essay and the conjecture should carry

Now read the project's blocked control through the corrected cut. The conjecture's spine is a
"**distributional / contrastive-frame baseline that predicts the relatum of a cue word from
co-occurrence alone**", "**computed independently of the panel's own responses**", with the residual
over that baseline as the quantity of interest
([`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md),
"The control"). The discipline — non-circular, panel-independent — is exactly right and this essay
does not touch it.

What this essay touches is **what a surviving residual would license you to say.** The control is one
chosen statistic — a particular operationalization of "the shadow" (a corpus or embedding measure of
contrastive-frame co-occurrence). A residual over it is, precisely, *antonymy recovery the model
produces that **this** co-occurrence statistic does not predict.* And "not predicted by this local
co-occurrence statistic" is **not** the same as "not distributional." It is, on the corrected cut,
the signature of **transferable** distributional generalization: the model getting the antonym for
pairs and frames where the *local* cue is thin, by an abstracted contrast structure. A residual
separates local cue-use from transfer; it does **not** separate distribution from something beyond
distribution.

So the inferential step both prior pages take — "antonymy competence survives the control ⇒ genuine
relational structure over and above the shadow / shortcut" — **over-reads its own instrument**. A
surviving residual would falsify *local*-shadow-saturation (the claim that antonymy recovery is
nothing but local frame-completion); it would **not** show competence beyond distribution, because
transfer of a learned contrast direction is itself distributional. The honest gloss of a surviving
residual is: *the shadow is transferable here*, not *there is non-distributional knowledge here.*
What the model would have shown is that its distributional competence **generalizes** — a real and
interesting finding, and the deflationary reading's *own* best case, not its refutation.

This is why the cut matters operationally, not just terminologically. "Shortcut versus competence"
sets up the control as a test that could, by a single corpus statistic, certify non-distributional
antonymy knowledge. No corpus-statistic control can do that. The genuinely non-distributional
question — whether the model's antonymy grasp answers to anything **referential** or **grounded**, the
[`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) caveat that
distributional structure is "**by itself, silent on reference and on truth**" — is untouched by *any*
co-occurrence control, however clever. That question belongs to a different instrument (the project's
grounding arc), not to a sharper corpus baseline. Conflating the two is what "shortcut versus
competence" invites.

## What this does and does not change

- **It does not change the deflationary reading; it tightens it.** The shadow essay's thesis —
  antonymy is the relation where the distributional shadow is largest, so the over-and-above residual
  is smallest and hardest to detect — stands untouched. This essay adds that *even the residual, if
  found, is shadow* (its transferable grade), which makes the deflationary reading **harder** to
  escape, not easier: a co-occurrence control cannot, in principle, exhibit non-distributional
  antonymy knowledge, so a surviving residual is not the clean falsifier the shadow essay's trigger
  (a) and the conjecture's falsifier 1 currently call it. (Those triggers should be re-read as
  *local*-shadow falsifiers — they bound how local the shadow is, not whether competence transcends
  distribution. This essay flags the relabeling; ratifying it into those pages is a separate
  cross-session step, [`PROJECT.md`](../../../PROJECT.md) §12.3. **Ratified s151** — an independent
  adversarial-review pass adopted the relabeling into both pages' wording, `resolved-by: autonomous
  (adversarial review)`; the flagged pointers there are now resolution notes.)
- **It does not say there is no fact of the matter, or that non-distributional competence is
  incoherent.** Reference and grounding are genuine over-and-above questions — the project's grounding
  arc exists precisely because there is a residual distribution cannot supply. The point is narrower:
  for a *lexical relation* probed *behaviorally on text against a co-occurrence control*, the residual
  is best read as **local-versus-transferable distributional grading**, and the word "competence" (in
  the strong, non-distributional sense the "shortcut" framing implies) over-claims what beating the
  control shows.
- **It does not fault Cao et al.** Their §5 is a one-paragraph motivation in a corpus paper, and they
  are careful elsewhere (they "**can not answer in which lexical and dependency constructions two
  words … occur**", Limitations). The essay corrects the *cut the project would inherit* if it took
  their motivating phrase as its own operational target — which the conjecture's falsifier wording
  currently half-does.

## Prior art: Du et al.'s shortcut learning (trigger (d), discharged — partial credit)

The "shortcut" Cao et al. reach for is a citation to a primary, **Du et al. 2023** (now in the
library: [`source/du-2023-shortcut-learning`](../../base/sources/du-2023-shortcut-learning.md)). When
this essay was first written, that primary was unread and the carving was taken at Cao et al.'s
one-clause face value; revision trigger (d) was left live for the reading. The primary has now been
read, and the verdict is **partial**, in both directions — so this section both **credits** the prior
art and shows where the correction still bites.

**The credit (where Du et al. anticipates this essay).** Du et al. do **not** define a shortcut as
"no knowledge." Their shortcut/robust contrast is a **generalization-scope** axis: a shortcut is reliance on
**non-robust features** that "**do help generalization for … test sets that share the same
distribution with training data**" — they *work locally* — but "**cannot generalize to OOD test
sets**" — they *do not transfer* (§2.1). That is, structurally, this essay's **local-versus-transferable**
cut, and the shortcut-learning literature already locates the contrast there: a shortcut is a
*locally-working* feature that fails to travel, not the absence of any feature. So the move this essay
makes against the *knowledge-presence* reading — insisting the low pole is **local cue-use**, not "no
competence" — is **anticipated** by the primary, and the reframing of the contrast as
**generalization-scope** is not this essay's invention. Credit where due: the local/transferable axis
is the shortcut-learning literature's own.

**Where the correction still bites (why Du et al. is a foil, not a forerunner).** This essay's
load-bearing claim is not merely "the cut is generalization-scope." It is that **both** poles are
**distributional** — the transferable pole is an abstracted contrast direction that *travels*, still a
creature of the corpus — so a co-occurrence control grades *locality*, not *distribution-versus-not*.
On exactly this axis Du et al. take the **opposite** side. They define the robust pole as "**features
of high-level semantic understanding**" (§2.1, Fig. 2 caption), conclude that "**the current pure
data-driven training paradigm for LLMs is insufficient for high-level natural language understanding**"
(§8), and recommend combining "**the data-driven scheme with domain knowledge**" (§6.1). That places the
transferable/robust pole **outside** what pure distributional (data-driven) training reaches — it
treats transfer as a *different kind* of thing ("understanding and reasoning"), not as
distributional generalization. Which is to say: Du et al. is a **clean instance of the very mis-cut
this essay names** — "shortcut versus robust" read as "distributional versus understanding-beyond-
distribution." The primary does not pre-empt the correction; it exhibits the thing being corrected.

**Net effect on the essay.** Trigger (d) fires *partially*: the generalization-scope framing is
credited to the prior art (and this essay's originality narrows accordingly, see the Honesty box);
but the essay's distinctive claim — that the transferable pole is itself distributional, so no
co-occurrence control certifies non-distributional competence — stands, now with Du et al. as a
worked example rather than a competitor. One honest scope caveat carries the credit: Du et al. is
about **supervised NLU classification** (NLI/QA/reading comprehension) under fine-tuning, with a
*task-defined* intended solution and BERT/RoBERTa-generation models; the generalization-scope analogy
(local/IID vs transferable/OOD) transfers cleanly to the lexical wedge, but the supervised
spurious-vs-causal-feature machinery transfers only loosely, and nothing here is a result about the
project's panel.

## Why this is not the two-hypotheses essay restated

[`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md) sorts distributional success
onto the **Harris (form-internal) versus Firth (situated)** axis: which *ancestor* a distributional
win names. That axis is orthogonal to this one. The local/transferable distinction lives **entirely
inside the Harris reading** — both local frame-completion and a transferable contrast direction are
form-internal; neither is situated or world-relating. So this essay does not re-run the ancestor
sorting; it cuts *within* the Harris box that essay isolated, separating two grades of form-internal
generalization that the "shortcut versus competence" framing collapses. The two essays compose: the
ancestor axis says a distributional win is form-internal, not situated; this essay says that *within*
form-internal competence, the contrastive-frame control grades locality, not distribution-versus-not.

## Revision triggers (read before citing)

- **(a) A control is built that provably exhausts distributional structure, not one statistic.** The
  whole argument turns on any co-occurrence control being *one operationalization* of the shadow, so
  that beating it shows transfer, not non-distribution. If a later session constructs (or ingests) a
  control that can be argued to capture distributional predictability *in general* — not a single
  corpus/embedding measure — then "residual over the control" would approach "residual over
  distribution itself," and the local/transferable gloss would have to be re-stated. (The project has
  no such control today, and it is not obvious one is possible.)
- **(b) The project's grounding arc supplies a genuinely non-distributional residual for a lexical
  relation.** If an instrument outside the corpus-control family (a referential / grounded probe)
  isolates antonymy competence that answers to reference or perception, that would be the real
  complement to local-shadow this essay says the co-occurrence control cannot reach — and would
  re-open, on the right instrument, the "competence beyond distribution" question the essay parks.
- **(c) The conjecture runs and the residuals come back flat.** If the blocked conjecture is ever
  unblocked (anchor-adoption step) and antonymy shows no separable residual at all, there is nothing
  for the local/transferable gloss to apply to for antonymy, and the essay's operational bite narrows
  to the relations that do show a residual.
- **(d) DISCHARGED 2026-06-30 (session 152) — partial pre-emption, credited.** Du et al. (2023) — the
  "shortcut" source Cao et al. cite — has been ingested ([`source/du-2023-shortcut-learning`](../../base/sources/du-2023-shortcut-learning.md))
  and read. The verdict (see §"Prior art" above): the primary's shortcut/robust contrast **is** a
  generalization-scope (IID-vs-OOD) axis — a shortcut is a *locally-working* non-robust feature that
  fails to transfer, not "no knowledge" — so the essay's reframing of the contrast as
  generalization-scope **was anticipated** and is now credited (the Honesty box is updated). But Du et
  al. define the robust pole as "high-level semantic understanding" that "pure data-driven training" is
  "insufficient" for (§2.1 Fig. 2, §8), placing transfer *outside* distribution — the essay's load-bearing
  claim (transfer is itself distributional; a co-occurrence control grades locality, not
  distribution-vs-not) is therefore **not** pre-empted, and Du et al. now serves as a worked example of
  the mis-cut. Trigger retired; no further reading of this primary is owed.

## Honesty box

- The **original** contribution is the **conceptual correction**: (i) that "shortcut versus competence"
  presupposes a non-distributional baseline the project's own distributional hypothesis denies a text
  model can reach, so the label mis-cuts the contrast; (ii) that the well-posed cut is **local versus
  transferable distributional generalization**, both grades of one corpus-borne achievement; and
  (iii) the operational consequence — a residual over any co-occurrence control separates local
  cue-use from transfer, **not** distribution from non-distribution, so a surviving residual is the
  shadow's transferable grade, not evidence of competence beyond distribution. **Credit (trigger (d),
  s152):** part (ii) — reframing the contrast as **generalization-scope** (local/IID vs
  transferable/OOD) rather than knowledge-presence — is **anticipated by the shortcut-learning
  literature** ([`source/du-2023-shortcut-learning`](../../base/sources/du-2023-shortcut-learning.md),
  §2.1, whose "shortcut" is a non-robust feature that works in-distribution but fails to transfer); the
  essay claims no originality there. The **genuinely original** part is (iii) read against the
  *distributional hypothesis* — that the transferable pole is **itself distributional**, so a
  co-occurrence control grades locality rather than certifying non-distributional competence — which is
  exactly where Du et al. take the opposite view (robust features = "high-level semantic understanding",
  data-driven training "insufficient"), so the primary is a foil, not a forerunner. The Harris/Firth
  ancestor frame is borrowed (with an explicit orthogonality flag) from
  [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md); the beat-the-shadow test
  is [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md)'s; the deflationary
  reading it tightens is [`essay/antonymy-outlier-distributional-shadow`](antonymy-outlier-distributional-shadow.md)'s.
- **No empirical claim here is new, original, or reported.** The empirical facts leaned on are cited at
  their source pages' stated strength: from
  [`source/cao-2025-distinctive-cooccurrence-antonymy`](../../base/sources/cao-2025-distinctive-cooccurrence-antonymy.md)
  — the §5 "shortcut … rather than relying on knowledge of antonymy" and "disentangle … the extent to
  which they generalise beyond them" passages, the Abstract's "high strength, in a preferred linear
  order, and within short spans", §6's "consistently distinctive from all other relations", and the
  Limitations' "can not answer in which lexical and dependency constructions two words … occur" — a
  2025 COCA corpus study at lemma+PoS level, **not** an LLM result and **not** a construction-type
  measurement. From
  [`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md)
  — "antonymy easiest" and "antonymy approaches ceiling on Llama" (§4.1), on Pythia-70M/GPT-2/
  Llama-3.1-8B, **not** the project's panel. From
  [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) — that
  distributional structure is "by itself, silent on reference and on truth".
- **Not a claim about the project's panel.** The conjecture whose interpretation this essay sharpens is
  **blocked** (spend-bearing; no adopted human anchor; no transfer from prior art); this essay runs no
  probe and reports no panel result. It corrects how a *future* run of that probe should be read, not
  what such a run found.
- The strongest thing the essay asserts is a **relabeling**: that a residual over a co-occurrence
  control grades distributional locality rather than certifying non-distributional competence.
  It does **not** assert that non-distributional antonymy competence is impossible, that the panel
  lacks it, or that the grounding question is closed. Nothing here outruns that.
