---
type: essay
id: shortcut-vs-competence-mis-cut
title: "Shortcut versus competence mis-cuts the disentanglement: the distributional shadow has a local and a transferable grade"
meaning-senses:
  - distributional
  - inferential
  - referential
status: draft
contingent-on: []
created: 2026-06-30
updated: 2026-06-30
links:
  - rel: depends-on
    target: source/cao-2025-distinctive-cooccurrence-antonymy
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
  - rel: refines
    target: theory/lexicon-grammar-continuum
---

# Essay: shortcut versus competence mis-cuts the disentanglement

> **Status: draft (2026-06-30). A philosophical-track essay arguing in the project's own voice.**
> It introduces **no new empirical claim** and makes **no human comparison of its own**: every
> empirical assertion cites the in-repo `source` page that carries it, at that page's stated
> strength. The original contribution is a **conceptual correction** to the framing the project (and
> the prior art it ingests) has been using for the "opposites" wedge — and a sharpening of what the
> blocked [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md)'s
> control could and could not show if it ever ran. It does not change any in-repo empirical verdict;
> it changes the *interpretation label* attached to a contrast.

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
  cross-session step, [`PROJECT.md`](../../../PROJECT.md) §12.3.)
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
- **(d) A reading of Du et al. (2023) — the "shortcut" source Cao et al. cite — is ingested and
  defines "shortcut" in a way that already anticipates this distinction.** The essay treats "shortcut"
  as Cao et al. deploy it (an unread secondary use); if the primary turns out to mean by "shortcut"
  something closer to "local cue-use" already, the essay's correction is partly pre-empted and should
  credit it. (Du et al. 2023 is not in the library; this is a flag, not a claim about its contents.)

## Honesty box

- The **original** contribution is the **conceptual correction**: (i) that "shortcut versus competence"
  presupposes a non-distributional baseline the project's own distributional hypothesis denies a text
  model can reach, so the label mis-cuts the contrast; (ii) that the well-posed cut is **local versus
  transferable distributional generalization**, both grades of one corpus-borne achievement; and
  (iii) the operational consequence — a residual over any co-occurrence control separates local
  cue-use from transfer, **not** distribution from non-distribution, so a surviving residual is the
  shadow's transferable grade, not evidence of competence beyond distribution. The Harris/Firth
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
