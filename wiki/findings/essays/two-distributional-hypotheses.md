---
type: essay
id: two-distributional-hypotheses
title: Two distributional hypotheses — which ancestor an LLM's distributional competence actually names
meaning-senses:
  - distributional
  - referential
  - grounded
status: draft
contingent-on: []
created: 2026-06-24
updated: 2026-06-24
links:
  - rel: depends-on
    target: source/harris-1954-distributional-structure
  - rel: depends-on
    target: source/firth-1957-synopsis
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: source/piantadosi-hill-2022-meaning-without-reference
---

# Essay: two distributional hypotheses

> **Status: draft (2026-06-24). A philosophical-track essay arguing in the project's own voice.** It introduces **no new empirical claim**: every empirical assertion inside it cites the in-repo page that carries it, and the original part is the argument — a sorting of which founding statement of the distributional tradition an LLM's distributional competence actually instantiates. The historiographic premise (Harris's distribution is form-internal; Firth's "collocation" is one mode of meaning among several, always situated in a "context of situation") is **secondary-sourced**: it comes via Brunila & LaViolette 2022 as carried by [`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md), and is used as historiography, never as a primary reading of Firth — no one in this project has read the Firth primary. **Revision trigger:** if a later session reaches the Firth primary and finds the form-internal / situated divergence overstated by the secondary, revise or retract the essay's premise and re-state the sorting accordingly; likewise revisit if the project ever catalogues a contrary reading of either founding text.

## The position

"The distributional hypothesis" is cited as one idea with two founding fathers, Firth and Harris. This essay argues it is **two distinct ideas**, and that the difference is not antiquarian housekeeping — it bears directly on what an LLM's distributional competence does and does not show. The bounded thesis: the next-token / embedding objective instantiates the **Harris** reading almost exactly, and does **not** instantiate the **Firth** reading; so a distributional success names the Harris ancestor precisely and leaves the Firth (situated) and the [`source/bender-koller-2020-climbing`](../../base/sources/bender-koller-2020-climbing.md) (world-relation) questions exactly where they were. The essay re-labels the grounding question with a sharper ancestor; it does not resolve it.

## The two hypotheses, kept apart

The two statements are routinely bundled, but the in-repo sources record a real divergence between them.

**Harris's is form-internal.** Harris 1954 states the distributional hypothesis as a within-language contrast measure. The central line, read from the primary scan, is:

> "if we consider words or morphemes A and B to be more different in meaning than A and C, then we will often find that the distributions of A and B are more different than the distributions of A and C. In other words, difference of meaning correlates with difference of distribution." ([`source/harris-1954-distributional-structure`](../../base/sources/harris-1954-distributional-structure.md), p. 156)

The Harris source page draws the consequence the project cares about: this correlation is "between *meaning difference* and *distribution difference*, a within-language contrast, not a theory of how expressions hook onto the world" ([`source/harris-1954-distributional-structure`](../../base/sources/harris-1954-distributional-structure.md), §"Bearing on this project"). The "company" Harris's elements keep is other linguistic elements — "environments," in his own idiom — and nothing else. His hypothesis is **form-internal by construction**: it relates distributions to distributions and reads a contrast in distributional `meaning` off the difference.

**Firth's, on the secondary reading, is situated.** The Firth line that NLP made its slogan is reliably *attributed* — carried by [`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md) via Brunila & LaViolette 2022, with the Firth primary **not consulted**:

> "You shall know a word by the company it keeps" (quoted via Brunila & LaViolette 2022, attributing it to Firth's Synopsis at p. 11; [`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md), §"The famous line")

But the same secondary records that for Firth "meaning by collocation" was only **one mode of meaning among several**, that collocation was no "mere juxtaposition" but "an order of mutual expectancy" (quoted via Brunila & LaViolette 2022, `Firth, 1957c, 12`; [`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md), §"Meaning by collocation"), and — the load-bearing point — that Firth's "collocation" is "always situated in a broader 'context of situation'" ([`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md), §"Bearing on this project"). Firth's "company," on this reading, includes the situational and cultural surround, not only neighboring tokens. As that source page puts it, his notion is "*less* form-internal than the embedding tradition that quotes him" ([`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md), §"Bearing on this project").

So the two hypotheses differ at exactly the seam the project's whole enquiry runs along: one stays inside linguistic form; the other reaches out, by Firth's own framing, to the situation in which the form is used.

## Which one the objective instantiates

This is the essay's original move: ask which ancestor a next-token predictor actually descends from, and the answer is unambiguous on the in-repo record.

The objective is trained on **form alone**. It conditions a distribution over the next token on the preceding tokens; its only data are the linguistic environments themselves. That is the Harris picture, almost line for line: "difference of meaning correlates with difference of distribution" is the within-language contrast a substitution-similarity or neighborhood measure reads off an embedding space, and the Harris source page already traces that lineage — his "measure how similar are the selection approximations of any two words" is, "read forward, the vector-space neighborhood / substitution-similarity measure the project uses as a distributional indicator" ([`source/harris-1954-distributional-structure`](../../base/sources/harris-1954-distributional-structure.md), §"Bearing on this project"). The concept page states the instantiation directly: the view "is instantiated in word embeddings and the next-token-prediction objective: a model trained to predict context implicitly encodes distributional structure" ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)). What the objective encodes is Harris's contrast measure at scale.

It does **not** instantiate the Firth picture, because the situational surround Firth's "company" is said to include is precisely what an isolated, text-trained model never sees. The "context of situation" is not in the token stream; it is the extra-linguistic setting the stream is a projection of. A model with form as its only data has, in [`source/bender-koller-2020-climbing`](../../base/sources/bender-koller-2020-climbing.md)'s terms, "no way to learn" the relation between form and the non-linguistic surround — "a system trained only on form has a priori no way to learn meaning" ([`source/bender-koller-2020-climbing`](../../base/sources/bender-koller-2020-climbing.md), p. 5185). The situated half of Firth's "company" is exactly the half form-only training cannot supply.

## The slogan borrows Firth's words for Harris's idea

Here is the consequence worth recording. When NLP reaches for "you shall know a word by the company it keeps" as the motto for embeddings, it borrows **Firth's words for Harris's idea**. The objective it is captioning is form-internal — Harris's — but the line it quotes belongs to a notion whose "company" was avowedly wider than that. The appropriation does not extend the model to Firth's situated reach; it quietly narrows *Firth* down to exactly the form-internal residue. The Firth source page makes this the explicit caution: "the NLP appropriation of Firth arguably narrows his notion to exactly the form-internal residue that *is* so silent" on reference and truth ([`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md), §"Bearing on this project"); the concept page carries the same observation ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), §"Historiographic caveat"). The slogan is doing rhetorical work it has not earned: it dresses a Harris-shaped competence in a Firth-shaped name, and the name promises a situatedness the competence does not have.

This matters because the borrowed name can make the grounding question look answered when it has only been re-labelled. If "company" is heard in Firth's wider sense, then a model that knows a word by its company sounds as though it has the situation too — and the gap to reference and world quietly closes by equivocation. Read in Harris's sense, which is the sense the objective actually instantiates, no such thing follows: the `distributional` caveat in [`meaning-senses.md`](../../meaning-senses.md) holds in full, that "by itself, distributional structure is silent on reference and on truth."

## What the sorting buys, and what it does not

The payoff is precision, not progress. Naming the Harris ancestor exactly lets a distributional result say what it is — a within-language contrast measure, form-internal — and stop there. It does **not** advance the questions a distributional success leaves open. The concept page already states the boundary the sorting respects: "A distributional success therefore does not settle the formal/functional question, and it does not settle the grounded/ungrounded question" ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), §"Live tension"). The sorting in this essay adds only that the success names its ancestor: it is Harris's contrast that the model instantiates, and Harris's contrast was, on the source page's own reading, never a theory of "how expressions hook onto the world" ([`source/harris-1954-distributional-structure`](../../base/sources/harris-1954-distributional-structure.md), §"Bearing on this project"). So:

- The **Firth (situated)** question — does the model have the "context of situation" that Firth's wider "company" included? — is left exactly where it was. The objective does not reach it; the slogan only borrows its name.
- The **Bender–Koller (world-relation)** question — does form-only training yield the form-to-world relation they define as meaning proper? — is left exactly where it was. A Harris-shaped success is, by Harris's own framing, silent on it.

A distributional success, correctly sorted, is therefore a precise statement of *which* ancestor's competence has been shown, and a precise statement of *which* questions remain untouched. That is the whole of what the essay claims for it.

## The live counter-position (the essay takes no side)

There is a standing rejoinder that a form-internal competence might still be meaningful — [`source/piantadosi-hill-2022-meaning-without-reference`](../../base/sources/piantadosi-hill-2022-meaning-without-reference.md)'s argument that "meaning arises from conceptual role," so that meaning "cannot be determined from a model's architecture, training data, or objective function, but only by examination of how its internal states relate to each other" ([`source/piantadosi-hill-2022-meaning-without-reference`](../../base/sources/piantadosi-hill-2022-meaning-without-reference.md), §Abstract). If inferential-role structure is `meaning` enough, then the form-internal residue need not be a deficit. **This essay takes no side on that.** Its job is upstream of the dispute: to fix *which* distributional hypothesis is on the table when an LLM's distributional competence is at issue. Whether the Harris-shaped competence so named amounts to meaning without reference is the Piantadosi–Hill-versus-Bender–Koller question, and the concept page already records it as "live for every empirical finding in this project that involves an LLM" ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)). The sorting clarifies the terms of that debate; it does not enter it.

## What this essay is not

- **Not a primary reading of Firth.** The Firth half of the premise is secondary-sourced via Brunila & LaViolette 2022, carried by [`source/firth-1957-synopsis`](../../base/sources/firth-1957-synopsis.md); no Firth primary was consulted, and the essay's claims about Firth are claims about that secondary reading. The revision trigger above is armed against exactly this dependency.
- **Not a new empirical claim.** It re-sorts existing in-repo material; it measures nothing. Every empirical assertion cites the page that carries it.
- **Not a resolution of the grounding question.** The sorting re-labels which ancestor a distributional success names; it leaves the Firth (situated) and Bender–Koller (world-relation) questions exactly where it found them, and explicitly declines the Piantadosi–Hill dispute.
- **Not a claim that the slogan-borrowing is anyone's error of fact.** "You shall know a word by the company it keeps" is a real Firth line, reliably attributed; the point is only that the *objective* it captions is Harris-shaped, so the name promises a reach the competence does not have.

## Honesty box

- The essay's *original* contribution is the **sorting**: that "the distributional hypothesis" is two ideas, that the next-token objective instantiates the Harris (form-internal) one and not the Firth (situated) one, and that NLP's Firth slogan therefore borrows Firth's words for Harris's idea — re-labelling, not resolving, the grounding question. The historiographic premise it builds on is secondary-sourced and flagged as such throughout.
- The strongest thing the essay asserts is that a correctly-sorted distributional success **names its ancestor precisely and leaves the situated and world-relation questions untouched.** It does not assert that the Harris-shaped competence is, or is not, meaning in any reference-involving or inferential sense. Nothing here outruns that.
