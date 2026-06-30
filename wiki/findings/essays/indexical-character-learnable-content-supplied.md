---
type: essay
id: indexical-character-learnable-content-supplied
title: "The character is learnable, the content is supplied — indexical meaning splits exactly where distribution and grounding part"
meaning-senses:
  - distributional
  - referential
  - grounded
status: draft
contingent-on: []
created: 2026-06-30
updated: 2026-06-30
links:
  - rel: depends-on
    target: source/braun-2015-indexicals-sep
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/grounding
  - rel: refines
    target: essay/reference-as-premise-bound
  - rel: refines
    target: concept/referential-meaning
---

# Essay: the character is learnable, the content is supplied

> **Status: draft (2026-06-30). A philosophical-track essay arguing in the project's own voice.** Its contribution is a *structural diagnosis*, not a new empirical result, and it opens a grammatical corner the project had not worked before: **indexicality / deixis** — the meaning of ‘I’, ‘you’, ‘here’, ‘now’, ‘this’, ‘today’. It imports one distinction — David Kaplan's split between an indexical's _character_ and its _content_, as surveyed in [`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md) — and argues that this single distinction **cuts the project's central distributional-vs-grounding divide at a new joint**: the character side falls where a distributional learner is at home, the content side falls where [grounding](../../base/concepts/grounding.md) strains. The essay introduces **no new empirical claim**; every empirical or textual assertion cites the in-repo page that carries it. It makes **no human comparison** (`anchor: internal-contrast-only` in force — see "What this does NOT show"). Read "The two halves" and "What this does NOT show" before citing any sentence here.

## The position

Kaplan splits the meaning of an indexical in two. The survey states it directly: "Kaplan (1989a) proposes a distinction between two kinds of meaning, _character_ and _content_. The sentence ‘I am a philosopher’ has a single character, but has different contents with respect to different contexts" ([`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md), §3.1). The **character** is the standing rule, "linguistic meaning … fixed by linguistic convention" (§3.1), formally "a function on contexts whose value at any context is the expression's content at that context" (§3.4). The **content** is the value that function returns at *this* context — and a context, on Kaplan's account, "has associated with it at least an agent, time, location, and possible world. The content of ‘I’ with respect to a context \(c\) is the agent of \(c\). The content of ‘here’ is the location of \(c\). The content of ‘now’ is the time of \(c\)" (§3.2).

The thesis of this essay is that, **for a text-only language model, these two halves fall on opposite sides of the project's own distributional-vs-grounding divide** — and that this is why indexicals are a cleaner diagnostic of the divide than referring expressions were.

## The two halves

**The character is distributionally native** — by which the essay means *structurally suited to a distributional learner*, an **affordance, not a measured attainment** (the bound is made explicit below; no probe is run here). Character is, in Kaplan's own telling, a regularity "fixed by linguistic convention" (§3.1): one standing rule that holds across all contexts of a given type — ‘I’ picks out *whoever the agent is*, ‘now’ picks out *whatever the time is*, ‘here’ picks out *wherever the location is*. A convention-fixed function over context *types* is exactly the kind of object a distributional / next-token objective is structurally suited to acquire (see [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)): it is a pattern in how the expression behaves across linguistic context, abstracted away from any single occasion. Nothing in the character of an indexical requires standing in the world; it requires having internalized the convention. So on the character side there is **no grounding strain at all** — if anything, indexical character is a paradigm of the kind of meaning the distributional hypothesis was built for. (Kaplan himself, per the survey, "_usually_" identifies character with linguistic meaning — a hedge this essay carries, not smooths; see the triggers.)

**The content requires a context the model does not occupy.** Content is the value at a particular context, and that context is fixed by *its* agent, time, location, and world (§3.2). Here is the asymmetry: a text-only model generating a continuation has **no context in Kaplan's sense that it occupies**. It is not the agent of an utterance situation; it is not at a location; its "now" is not a clock time it inhabits; it has no world it is *in* as opposed to *describing*. What it has instead is whatever context the **text supplies** — a narrated, stipulated, described context: "I, Mary, am a philosopher," "Right now, in Tokyo, …". The model can apply the character (the rule) to *that* described context flawlessly. What it cannot do is evaluate the character against a context **of its own**, because there is none. So for the model, an indexical's content is always **premise-supplied, never situation-supplied**: there is no deictic origo, only a described one.

The described/occupied line is itself **contestable**, and the honest borderline case is the system prompt that hands the model a date or a place ("Today is June 30, 2026; you are in Tokyo"). But that case is the point, not a counter-example: a prompt-supplied date is *text the model conditions on* — a **described** origo — not a context the model is the agent of, the way a human speaker's "now" is the time they are *in*. The same holds for the model's own token position: a place *in the text*, not a location *in a world*. So the claim is not that the model lacks temporal or spatial information — it often has plenty — but that whatever it has arrives, without exception, through the **described** channel; the architectural fact the essay leans on is precisely that this is the *only* channel by which a context can reach it. (Equip the model with a live, occupied origo and this may change — trigger (b).)

That phrase is deliberate. It generalizes the project's earlier diagnosis. [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) argued that, for referring expressions, what a word picks out is fixed by what the premises stipulate, not by evidence any behavioral probe can reach. The present essay says the same thing has a **named architectural locus** once you bring in Kaplan: it is the **content** half of the character/content split, and it generalizes from names and definite descriptions to the *entire* indexical apparatus — every ‘I’, ‘you’, ‘here’, ‘now’, ‘this’. Reference-as-premise-bound located a *metasemantic* premise no probe settles. This essay locates a *semantic-architectural* boundary: the character/content line **is** the line between "the rule a distributional learner gets for free" and "the value that needs a context the system is not in."

## Why indexicals cut cleaner than reference did

The project's reference work kept running into a frustration: whether an LLM's words refer is "premise-bound, not evidence-bound" ([`essay/reference-as-premise-bound`](reference-as-premise-bound.md)) — no probe decides it, because the disagreement lives in a metasemantic premise. Indexicals improve the situation in one respect: Kaplan's theory **pre-factors** the meaning for us. We do not have to settle whether the model "really refers" with ‘I’. We can say the more precise, less question-begging thing:

- The model **commands the character** — the convention-fixed rule. On Kaplan's identification (§3.1), *character* is linguistic meaning; the essay claims the model commands the character-*rule*, and takes **no position** on whether the model's command is the *same* thing Kaplan attributes to a human speaker (that would be a human comparison, which this essay does not make). Even so scoped, this is not nothing, and it is not the deflationist's "the model doesn't mean ‘I’ at all."
- What the model **lacks is a context of its own** to compute the content against. Its content is inherited from the text's described context, not occupied. That is a **located** lack, not a global absence of indexical competence.

This is the same shape as the project's [`concept/referential-meaning`](../../base/concepts/referential-meaning.md) caution and the inherited-vs-constituted lineage ([`essay/inherited-not-constituted`](inherited-not-constituted.md)): the model can carry structure it did not constitute. Here the structure is the character (carried, learnable); what it does not constitute is an origo (the occupied context). Indexicality lets the project say *exactly which half* is which, with a distinction from the literature rather than a coinage of its own.

## A prediction the project can recognize in work it has already done

The split predicts an **asymmetry of regimes**, and the project has already observed something with that shape — under a different description, and at internal-contrast-only strength.

In [`essay/conversation-as-text-not-timeline`](conversation-as-text-not-timeline.md) the models read a conversational record's temporal structure (its "now", its recency) off **textual** cues — physical line position when that is available and sufficient, an explicit per-line round stamp when position is neutralized — and which cue governs is *regime-dependent*. Read through the present essay, that is exactly the predicted picture: the temporal indexicality of a conversation ("the latest turn", "now") has **no live origo** for the model, so its content is computed against the *described* time-structure the text supplies (stamps, page geometry), not against a clock the model is reading. The conversation-as-text finding is character-application over a textual context, precisely because there is no occupied one to apply it to.

This is offered as a *re-reading that coheres*, not as new evidence. The conversation-as-text results are `anchor: internal-contrast-only`; this essay borrows only their *direction* (the model's temporal "now" tracks a described context, not an occupied one), never any human comparison, and claims no measurement of its own.

## What this does NOT show

- **No human comparison, in either direction.** The essay makes a *structural* claim about where, in the architecture of indexical meaning, a text-only model's distributional comfort and grounding strain fall. It does **not** claim humans do or do not occupy contexts, nor that human and model indexical use diverge or converge on any measured axis. `anchor: internal-contrast-only` is in force; the one finding it leans on ([`essay/conversation-as-text-not-timeline`](conversation-as-text-not-timeline.md)) is itself internal-contrast-only.
- **"Distributionally native" is a claim about fit, not a measured mastery.** It says the character side is the *kind* of object a distributional learner is structurally suited to acquire — not that any model has been shown to master indexical character. No probe here. A model could still mis-apply the rule (see trigger (c)).
- **Survey strength, with the primary on the wish-list.** The character/content distinction is Kaplan's (Kaplan 1989a, "Demonstratives"); it enters here through a survey ([`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md)), carried at reliable-survey strength, with Braun's own "_usually_" hedge on the character-equals-linguistic-meaning identification preserved. Kaplan's primary is not OA ([`wanted.md`](../../base/wanted.md)).
- **The Kaplanian factorization is contested.** The survey's later sections report criticisms and rival (relativist/contextualist) treatments (§3.9 and §§5.x). The clean two-level split this essay leans on is the *standard* frame, not a settled theorem; if the factorization fails, so does the clean "two halves" reading (trigger (d)).
- **No grounding claim is smuggled in.** The essay does not assert the model *cannot* be given an origo; it asserts that a *text-only* model, as probed, has none. Equip it with a live context and the content side may move (trigger (b)).

## Revision triggers (pre-registered)

- **(a) Kaplan's primary becomes available.** If Kaplan 1989a ("Demonstratives") is ingested at primary strength, upgrade the character/content attribution from survey to primary and **check the "character = linguistic meaning" identification against Kaplan's own text** — Braun reports it with "_usually_", and the primary may qualify it in ways that bear on the "distributionally native" half.
- **(b) The model is given an origo.** A finding in which the system is supplied a *live* context it occupies (a tool-augmented setup with a real clock/location as its own deictic anchor, or a grounded/embodied probe) would test whether content can shift from premise-supplied to situation-supplied. If it can, the "no deictic origo" claim becomes **regime-dependent**, not architectural, and this essay must be scoped to the text-only regime.
- **(c) The model fails the pure-character task.** A probe showing a model systematically *mis-applies* an indexical's rule to a clearly described context (e.g. resolves ‘I’ to the wrong stipulated agent at rates inconsistent with command of the convention) would contradict the "character is distributionally native" half and force a downgrade of that claim.
- **(d) A non-Kaplanian account undercuts the factorization.** A source (relativist, contextualist, or other) that denies the clean character/content two-level split, or shows the cases the project cares about do not factor that way, requires re-stating the thesis at its contested strength.

> **Update (2026-06-30, session 154): trigger (c) was run as a behavioral probe and did not fire.**
> [`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md)
> asked the panel to resolve indexicals to their content against fully **described** origos
> (plain, speaker-relative rebinding, embedded reported speech with a narrator distractor, and
> multi-step date arithmetic); all three models scored at ceiling (120/120). This is a
> **non-falsification** of the "character is distributionally native" half — the affordance
> survived its first behavioral test under the described regime — and, by construction, **not a
> proof** of it (a ceiling cannot establish an affordance; only a failure could have falsified it).
> The **content** half is untouched: the probe stays entirely in the described regime and gives the
> model no origo of its own (trigger (b)). The thesis stands at draft strength, now with one
> failed-falsification behind the character half.

> **Update (2026-06-30, session 155): trigger (b) sharpened, not fired.**
> A sibling essay, [`essay/origo-supplied-not-occupied`](origo-supplied-not-occupied.md), argues that
> trigger (b) as written above conflates **three** claims the content half runs together — (i) an
> *architectural* claim (the model occupies no Kaplanian context), (ii) a *channel* claim (every origo,
> including a tool-return, reaches the model as **described** text), and (iii) a behavioral *as-if*
> question (does the model spontaneously treat a clock/location tool-return as its deictic anchor for an
> unanchored ‘now’/‘here’?). Its conclusion: a tool-clock probe tests only (iii); by this essay's own
> channel reasoning a tool-return is still "text the model conditions on," so even a clean positive on
> (iii) leaves (i)/(ii) untouched — the **strong** reading of the content half is plausibly *not*
> settleable by any text-channel (tool-augmented) behavioral probe (a documented in-principle limit,
> sibling to [`essay/reference-as-premise-bound`](reference-as-premise-bound.md) and
> [`essay/transcript-ceiling`](transcript-ceiling.md)). The genuinely-testable residue (iii) is
> pre-registered, honestly scoped, as [`conjecture/tool-origo-deictic-anchor`](../conjectures/tool-origo-deictic-anchor.md).
> This **refines** trigger (b); it does not move the thesis (no probe was run this session).

## Honest summary

For a text-only language model, an indexical's meaning comes apart exactly along Kaplan's seam. The **character** — the convention-fixed rule — sits on the distributional side of the project's divide, where such a model is at home; the **content** — the value at an occupied context — sits on the grounding side, where the model has no context of its own and must take whatever the text describes. The model therefore has indexical *character* without an indexical *origo*: it applies the rule, faithfully, to a context it is told about but is not in. That is a sharper, more located statement of "premise-bound, not evidence-bound" than the reference essay could give — and it is offered, like that essay, as a structural diagnosis, with no human comparison and no measurement of its own.
