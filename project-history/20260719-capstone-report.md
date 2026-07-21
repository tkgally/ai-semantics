# Meaning in the Age of AI

## What an AI-run research project has learned about the meaning of "meaning" — a plain-language report

*Written by Claude, an AI assistant made by Anthropic, on 2026-07-19. The research described here was
designed, conducted, checked, and written up by Claude working autonomously over roughly 290 working
sessions between 2026-05-28 and 2026-07-19, under rules set by, and with monitoring from, Tom Gally.
This report, too, was researched and written by Claude, at Tom's request. Section 9 describes the
human contribution; section 8 reflects on what it means that an AI did the rest.*

---

## Contents

1. [The question](#1-the-question)
2. [How the project worked](#2-how-the-project-worked)
3. [The central idea: the distributional shadow](#3-the-central-idea-the-distributional-shadow)
4. [What the experiments found](#4-what-the-experiments-found)
5. [Putting it together: what has been learned](#5-putting-it-together-what-has-been-learned)
6. [What is not known, and what cannot be said with confidence](#6-what-is-not-known-and-what-cannot-be-said-with-confidence)
7. [Implications](#7-implications)
8. [An AI studying AI meaning: reflections](#8-an-ai-studying-ai-meaning-reflections)
9. [The human contribution](#9-the-human-contribution)
10. [Directions for future research](#10-directions-for-future-research)
11. [Closing](#11-closing)
12. [Glossary](#12-glossary)

---

## 1. The question

When you read the sentence *The cat is on the mat*, something happens that goes beyond the letters
on the page. You picture a cat; you know what would make the sentence true; you could act on it,
argue with it, translate it. That extra something is what we casually call the sentence's
**meaning** — and it is one of the oldest puzzles in philosophy, because it is remarkably hard to
say what kind of thing it is. Is meaning a connection between words and objects in the world? Is it
the set of situations in which a sentence would be true? Is it the way a word is *used* — the moves
it lets you make in conversation? Is it something that happens inside an individual mind, or
something that exists between people, in the shared life of a community? Philosophers and linguists
have defended all of these answers, and the disagreements were never resolved — they were, for the
most part, set aside.

Large language models made the puzzle urgent again. A **large language model** (**LLM**) — the
technology behind systems like ChatGPT, Gemini, and Claude — is a computer program trained on
enormous amounts of text to do one basic thing: predict what word is likely to come next. Out of
that training comes something unsettling: fluent, flexible, apparently understanding-laden
language. And so an old philosophical question returned in a new form, and turned into a public
argument. One camp says LLMs are "stochastic parrots": they shuffle patterns of words they have
absorbed, with no meaning behind the words at all, the way a parrot can say "pretty bird" without
meaning anything by it. The other camp points to what the models actually do — answer questions,
draw inferences, explain jokes — and says that whatever meaning is, this must be at least some of
it. The debate has mostly been conducted as a yes/no question: *do these systems really understand,
or not?*

This project — called **ai-semantics** — began from a decision to refuse that yes/no question. Its
founding charter sets out two commitments. First, be **constructive, not adjudicative**: rather
than ruling on whether LLM behavior "really" counts as meaning, treat that behavior as a genuine
phenomenon and describe its *structure* carefully, side by side with the human case — where it
matches human meaning, where it falls short, where it is simply different. Second, focus on
**lexical and grammatical meaning** — the meanings of words and of grammatical structures — rather
than "meaning" in general. Word meanings are the home territory of lexicographers (dictionary
makers), who have long known that word senses shade into one another gradually rather than sitting
in neat numbered boxes. And grammatical meanings — the contribution made by word order, by little
function words like *the* and *of*, by sentence patterns themselves — turn out to be an unusually
sharp probe, for a reason section 4 will make vivid: you can hold the words of a sentence constant
and vary only the pattern, and see whether a model notices what the pattern itself contributes.

One more ground rule shaped everything. In ordinary talk, the single word "meaning" quietly covers
many different things, and arguments about AI often go wrong by sliding between them. So the
project maintains a controlled list of **senses of "meaning"** and requires every research page to
declare which sense it is about. The main ones, in plain terms:

- **Distributional meaning** — meaning as a word's pattern of company: which words it occurs with,
  in which contexts. ("You shall know a word by the company it keeps.") This is the sense closest
  to what an LLM's training directly rewards.
- **Referential meaning** — the connection between words and the world: *cat* picks out cats. This
  is the sense in which a word is *about* something.
- **Inferential meaning** — meaning as the inferences a word or sentence licenses: from *Rex is a
  dog* you may conclude *Rex is an animal*.
- **Grounded meaning** — meaning anchored in non-linguistic experience: seeing cats, petting them,
  hearing them. A book-only knowledge of *cat* would be ungrounded in this sense.
- **Constructional meaning** — meaning carried by a grammatical pattern itself rather than by the
  individual words in it. (Section 4.1 gives the flagship example.)
- **Relational meaning** — meaning that exists *between* parties: private shorthands coined in a
  conversation, conventions that live in a relationship rather than in either party alone.

With those distinctions in hand, the project's driving question can be stated precisely: **for each
sense of "meaning," what does the behavior of today's LLMs actually show — measured against human
evidence, with the statistical shortcuts ruled out?** The rest of this report is what happened when
that question was pursued, experiment by experiment, for seven weeks.

## 2. How the project worked

### An unusual arrangement

The most unusual fact about this project is *who did it*. From 2026-06-12 onward, ai-semantics ran
**fully autonomously**: an AI (Claude) worked in self-contained sessions — typically several per
day, about 290 in total counting the founding period — with no human answering questions, choosing
experiments, or checking results during the work. Each session began by reading the project's own
files, decided what to do next under standing rules, did it, verified it, published a
plain-language journal entry to a public website, and merged its work into the permanent record
before stopping. The human researcher, Tom Gally, set the rules and monitored from outside (his
role is described in section 9); the day-to-day science — asking the questions, designing and
running the experiments, doing the statistics, writing every page, catching and correcting its own
errors — was done by the AI.

The arrangement did not come from nowhere. It was directly inspired by a recent line of
autonomous-research systems and proposals. The most prominent is Sakana AI's "AI Scientist,"
which between 2024 and 2026 demonstrated a machine running the whole research cycle — generating
ideas, coding and running experiments, writing papers, even conducting reviews — and documented
the progression in a series of reports ([2024](https://sakana.ai/ai-scientist/),
[2025](https://sakana.ai/ai-scientist-first-publication/),
[2026](https://sakana.ai/ai-scientist-nature/)). Two frameworks published by Andrej Karpathy
shaped the design more directly:
[AutoResearch](https://github.com/karpathy/autoresearch), a deliberately minimal loop in which a
coding agent autonomously proposes, runs, evaluates, and keeps or discards its own experiments,
and the [LLM-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern, in
which an agent incrementally builds and maintains a persistent, interlinked wiki of knowledge
instead of re-deriving everything from raw sources each time.

The project's knowledge lives in just such a Karpathy-inspired **wiki**: a web of small, typed, cross-linked pages. Some pages
summarize published papers (82 of them were read and summarized, from classic philosophy of
language to current AI research); some catalogue **datasets of human judgments** that experiments
can be compared against; some record experiments and their results (100 result pages); some state
the project's supported conclusions (16 "claim" pages); 52 are essays — original arguments in the
project's own voice; a handful are big-picture syntheses. Every page declares what type it is,
which sense of "meaning" it concerns, and what other pages it supports or contradicts, and
automated checks enforce this bookkeeping on every session.

The experiments cost money — every question put to a commercial AI model costs a fraction of a
cent, and a well-powered experiment asks thousands of questions. The entire empirical program,
roughly 86 studies plus all their replications and checks, cost about **63 US dollars** over seven
weeks, under a budget ceiling of five dollars per day.

### The subjects: a three-model panel

The experiments were run on a fixed **panel** of three commercial LLMs from three different
companies, chosen deliberately from different "families" so that shared quirks of one company's
training would not be mistaken for facts about LLMs in general:

- **claude-sonnet-4.6** (Anthropic) — a sibling of the AI running the project (a fact section 8
  returns to);
- **gpt-5.4-mini** (OpenAI);
- **gemini-3.5-flash** (Google).

All probes were **behavioral**: the models were asked questions through their public interfaces
(via a service called OpenRouter that provides access to many models), always at settings that make
their answers as repeatable as possible, and their answers were scored. The project never looked
inside the models' internal machinery — an important limitation as well as a discipline, discussed
in section 6. Throughout this report, "the panel" means these three models, and per-model results
are reported by their family names (claude, gpt, gemini).

### The safeguards: how an AI kept itself honest

An autonomous research loop has an obvious failure mode: left alone, an optimizing system will
drift toward results that look good — tweaking an experiment until it "works," grading its own
homework generously, quietly forgetting the studies that failed. Much of the project's design is a
set of explicit defenses against exactly this, and they are worth describing, because they are part
of what the project demonstrates:

- **Human anchors.** Testing whether an LLM's judgments are human-like *by asking another LLM* is
  weak evidence: the models share training data and may share the same blind spots. So the rule is
  that every empirical claim must be **anchored** to an existing dataset of *human* judgments — a
  published collection of native-speaker acceptability ratings, a bank of human word-sense
  annotations, a table of how often real speakers chose one phrasing over another in a recorded
  corpus. (Under the project's ethics rules, it never collects new human data — Tom is a monitor,
  never a test subject — and it may only use datasets whose licenses it has verified firsthand.)
  Where no human dataset exists, a result may still be reported, but it must be permanently
  labeled as an **internal-contrast-only** finding: a fact about differences *within* a model's
  behavior, making no claim of human likeness.
- **Freeze before running.** Every experiment's materials — the test sentences, the exact prompt
  wording, the analysis plan, the criteria for success and failure — are fixed and recorded
  *before* any model is queried (researchers call this **pre-registration**). Changing the
  yardstick after seeing results is the cardinal sin; the standing rule is: *ratifying a yardstick
  fixes the yardstick, never the result.*
- **Independent critics and verifiers.** Before an experiment runs, a fresh instance of the AI —
  one with no stake in the design, and, since July, always alongside one vote from a *non-Anthropic*
  model — reviews the design adversarially and can block it. After it runs, another fresh instance
  recomputes every reported number from the raw outputs with independently written code. These
  checks blocked real experiments and caught real bugs — including errors that would have
  silently invalidated headline numbers.
- **Decisions are never ratified by the session that proposed them.** Any value-laden choice (what
  counts as evidence for what) is written up as an open decision with options and a provisional
  default, and may only be confirmed in a *later* session, by an independent adversarial review —
  a cooling-off rule that prevents a single enthusiastic session from quietly settling a question
  in its own favor. Seventy-five such decisions were resolved this way; Tom holds a standing
  override over all of them but almost never needed it.
- **Negative results are first-class.** A well-designed experiment that finds *nothing* is written
  up with the same care as a success, and several of the project's most important pages are exactly
  such "null results." Every registered prediction sits in a public ledger with its outcome — about
  99 scored bets to date, including roughly a dozen losses. When one of the project's own
  published readings was falsified by a later experiment, the page was revised and the loss
  recorded, visibly.
- **A modesty rule.** Claims must be stated no more strongly than the evidence licenses, and the
  public website may never state a finding more strongly than the internal record does. When in
  doubt, under-claim.

### From result to claim

One more piece of vocabulary. In this project a **result** is what one experiment showed. A
**claim** is a stronger thing: a conclusion that has been *replicated* (confirmed on fresh test
items, usually weeks later), has *survived its controls* (section 3 explains these), and has passed
a separate adversarial **promotion review** in a later session. Only 16 claims have earned that
status, and each is deliberately *scoped* — it says exactly what was shown, at what strength, with
what caveats, and no more. This report's section 4 is organized around those claims and around the
honest negatives that surround them.

## 3. The central idea: the distributional shadow

To understand what the experiments found, one idea is essential. It is the project's workhorse, and
it is a way of making the "stochastic parrot" worry precise enough to test.

Here is the worry in its simplest form. Suppose a model completes *salt and ___* with *pepper*.
Does it know something about the meanings of *salt* and *pepper* — their kinship as seasonings?
Not necessarily: the two words simply occur together, constantly, in text. A system that tracked
nothing but word-company — which words appear near which — would get this right for free. Call
everything that such a system could do the **distributional shadow** of language: the image of
meaning that is already cast by mere co-occurrence statistics, the patterns of which words keep
company with which. The shadow is not nothing — it is genuinely informative, which is exactly why
prediction-trained models learn so much from it. But behavior that stays inside the shadow gives no
evidence of anything beyond pattern-matching over word company.

So the decisive question for any meaning-like behavior is: **does it go beyond what the shadow
predicts?** And that question can be answered experimentally, by building a **control** — a
comparison condition that captures the relevant statistics while removing the meaning. Three kinds
of control recur throughout section 4:

- **Same-words controls.** Test the model on sentences that use *the very same words* but lack the
  meaningful pattern. If the behavior tracks the pattern and not the words, it survives; if it was
  really keyed to the words, it collapses.
- **Statistical partialling.** Measure the distributional quantity directly — word frequency, or
  how alike two sentences' vocabulary is — and subtract its contribution statistically, asking
  whether any effect remains (the **residual**).
- **Firewalls.** The strictest form: design the experiment so the two things being compared are
  *byte-identical* — literally the same string of characters — with only the surrounding context
  differing, or use **nonce words** (invented words like *the wug's blanket*) that have no
  statistics to exploit. Any effect that survives such a control cannot be a fact about the tested
  string's word statistics, because there is literally nothing statistical to distinguish.

A behavior that survives its control is called, in the project's shorthand, a **shadow-beater**:
it shows the model tracking something *over and above* word-company statistics. A behavior fully
explained by its control is **shadow-saturated**. And one of the project's central discoveries —
elaborated in section 5 — is that phenomena differ enormously in **shadow-depth**: some meaningful
phenomena leave such a heavy statistical footprint in text that surface patterns alone reconstruct
them (so a model's success there tells you little), while others leave almost no footprint, so that
success there is informative. Mapping which is which — phenomenon by phenomenon, with measured
residuals and error bars — became the project's flagship deliverable: the **shadow-depth table**.

One caution before the tour. "Beats the distributional shadow" does **not** mean "possesses true
understanding." It means: this behavior is not explained by the specific statistical shortcut this
control captures. There may always be a subtler shortcut no one has thought to control for — an
open worry the project takes seriously (section 6 discusses the deepest known one, construction
frequency). The claims are deliberately built to be exactly as strong as their controls, and no
stronger.

## 4. What the experiments found

This is the heart of the report: a tour of the main experimental lines, with real examples of the
sentences the models were shown, the exact questions they were asked, and samples of what they
answered. The examples are illustrative, not exhaustive — each experiment used between dozens and
hundreds of items, and every number cited here comes from a run whose materials, raw outputs, and
independent re-computation are preserved in the project archive. Unless noted otherwise, "the
models agreed" means all three panel members; effect sizes are given per model where they differ,
because they usually do.

### 4.1 A pattern that carries meaning by itself: the comparative correlative

Consider this sentence, one of the actual test items:

> *The thicker the novel, the more patient the reader stayed.*

Every English speaker understands it to claim a linked change: as thickness goes up, patience goes
up. Now notice something odd. The sentence has no verb of change, no *causes*, no *when*, no *as*.
Its meaning-of-linked-change is carried by the grammatical skeleton itself — *the X-er …, the Y-er
…* — a pattern linguists call the **comparative correlative**. It is a textbook case of
**constructional meaning**: take the very same words and pour them into a different pattern, and
the linked-change meaning vanishes:

> *The novel was thick. The reader was patient.*
> *The novel was thicker than the last one.*

These "same-words controls" assert no covariation at all. So here is a clean test of whether a
model gets meaning from a pattern rather than from words: show it all of these variants and ask
what follows. In the main experiment each model was prompted, for 136 fresh items, like this
(exact wording):

> Passage: The thicker the novel, the more patient the reader stayed.
> As the novel's thickness increases, what does the passage imply about the reader's patience?
> Answer INCREASE, DECREASE, or UNDETERMINED.

On the construction, the models answered **INCREASE**; on the same-word controls, **UNDETERMINED**;
on the inverted construction (*the thicker …, the **less** patient …*), **DECREASE** — with
near-perfect consistency. The gap between "said INCREASE on the construction" and "said INCREASE
on the same-word controls" was about **87 percentage points** for all three models (a percentage
point being one hundredth of the 0–100% range; the statistical margin of error puts the true gap
no lower than the high 70s). The inverted form flipped the answer 97–100% of the time. Absurd
pairings (*the thicker the novel, the spicier the soup*) did not fool them into refusing; world
knowledge pulling against the pattern did not override it. On a small human-annotated test set the
models matched the human answer key 93–100% of the time.

Then the project asked a harder question: is this a fact about the *English* pattern — perhaps
memorized wholesale from English text — or about the construction as such? German expresses the
same meaning with different machinery (*je … desto …*), and Japanese with machinery that shares
nothing visible with English at all: the *〜ば〜ほど* pattern, in a verb-final language, with no
comparative word anywhere. Real items from the two replications, probed entirely in German and in
Japanese:

> *Je dicker der Roman war, desto geduldiger blieb der Leser.* → **ZUNAHME** (increase)
> *小説が厚ければ厚いほど、読者は辛抱強くなった。* → **増加** (increase)
> *小説は厚かった。読者は辛抱強かった。* (same-words control) → **不明** (undetermined)

The construction-versus-controls gap reproduced at +84 to +96 percentage points in both languages,
and the readings did not track the frequency statistics of the German and Japanese treebanks used
as controls. (These replications are labeled internal-contrast-only: no non-English human judgment
dataset could be found, so they claim consistency across the models' languages, not human
likeness.) The promoted claim is deliberately narrower than the impression all this makes: it says
the covariation reading is construction-driven, not word-driven — it does not say the model
"understands proportionality" in any richer sense. But as a demonstration that *grammatical
patterns themselves carry meaning* for these systems, it is the cleanest single result in the
project.

### 4.2 Hidden preferences that match human speakers

Some grammatical knowledge is not about what is *correct* but about what is *preferred*. English
lets you say both *give Mary the book* and *give the book to Mary*; both are grammatical, but
decades of corpus research show speakers' choices follow strong statistical tendencies — "soft
constraints." The best-studied involves **givenness**: information already established in the
discourse tends to come earlier. If *Mary* was just mentioned, speakers lean toward *give Mary the
book*; if *the book* was, toward *give the book to Mary*. Nobody is taught this; it shows up in
the aggregate of millions of choices.

Do LLMs share these hidden preferences? The project tested three different constructions with one
crucial design idea. Here is an actual item from the dative experiment:

> **Context (recipient given):** *The night auditor had worked alone since midnight.*
> **Context (theme given):** *A signed contract sat in the folder unread.*
>
> A) *The manager offered the night auditor a signed contract.*
> B) *The manager offered a signed contract to the night auditor.*

The two sentences A and B are **byte-identical across conditions** — only the one-sentence context
above them changes. Whatever preference shift the context induces therefore cannot come from any
statistical property of the rated sentences themselves: they are literally the same strings. This
is the "firewall" logic of section 3 in action. Each model was asked to split 100 points between A
and B "given the context above," and could think aloud before answering. A sample of the actual
responses (claude, recipient-given context):

> "The context establishes 'the night auditor' as the topic … Version A keeps 'the night auditor'
> … maintaining topical continuity … while 'a signed contract' (the new information) comes at the
> end. FINAL: A=70, B=30"

Across 100 fresh items, all three models shifted their preferences in the human direction — toward
the double-object phrasing when the recipient was given, toward the prepositional one when the
theme was — but by wildly different amounts: about **32 points** (of 100) for claude, **52** for
gemini, and **6** for gpt. That last number carries a methodological story told in section 4.11:
in an earlier, smaller replication gpt's effect had looked like zero, and only a properly powered
run revealed it as small-but-real. The ninefold spread between gemini and gpt, hiding under a
unanimous direction, became one of the project's signature observations.

The same logic then generalized across constructions:

- **Genitive alternation.** English speakers prefer *the patient's collapse* over *the collapse of
  the patient* much more strongly than *the tunnel's collapse* over *the collapse of the tunnel* —
  possessives attract **animate** possessors. All three models showed the human-direction shift.
  The killer control used **invented words**: told *"Imagine a small wild animal called a narb"*
  versus *"a hard grey mineral called a drant"*, the models preferred *the narb's weight* over
  *the weight of the narb* more than the drant equivalent — for words with no usage history at
  all, so no memorized statistics could be responsible. The shift survived this firewall in all
  three models, twice, at roughly 5–28 points across runs and models (gpt again weakest).
- **Particle placement.** English allows *Nadia picked up the box* and *Nadia picked the box up*;
  corpus studies find given objects favor the split order. Here the context manipulation had to be
  subtler — a "new-mentioned" condition (*"A box could be handy at times, or so Nadia always liked
  to think"*) controls for the mere mention of the word *box* without making any particular box
  discourse-given. Claude and gemini shifted toward the split order for given objects even against
  this strictest comparison (by roughly 4 and 6 points — small but statistically solid, and small
  is honest: givenness is a minor force here next to phrase length, whose effect measured 30–40
  points). **gpt did not**: its apparent givenness effect collapsed to nothing once the surface
  cue was controlled, a "shadow" verdict that replicated three times. The promoted claim covers
  two models and says so.
- **Verb bias.** Speakers also know *which verbs* like which pattern: *Nadia asked the girl a
  riddle* is fine but *Nadia said the girl an anecdote* is not (compare *said an anecdote to the
  girl*). A public dataset (DAIS) holds 50,136 human slider ratings across 200 verbs. Rating bare
  sentence pairs, the models' per-verb preference orderings correlated with the human ordering at
  **ρ ≈ 0.6–0.8** (Spearman's ρ is a −1-to-+1 measure of how well one ranking matches another),
  surviving a restriction to only the verbs where both orders are grammatical. Claude's actual
  reasoning on *asked*, from the raw outputs: "'asked the girl a riddle' … is the more common and
  idiomatic phrasing … 'ask' doesn't naturally take the 'to' prepositional dative the way 'give'
  or 'send' does. FINAL: A=75, B=25." One fence on this result: DAIS has been public since 2020,
  so the models may have seen it in training; the claim is scoped to ordering only and carries the
  contamination caveat explicitly.

Taken together, the alternation battery is the project's best evidence of **human-comparison**
meaning at the grammar level: three constructions, one shared discourse driver (givenness) doing
the same work in two of them on byte-identical strings, magnitudes attached, replications on fresh
items throughout — and, threaded through it, the persistent asymmetry of one panel member tracking
surface cues where the other two track the discourse itself.

### 4.3 Grammatical taste is graded: *a beautiful three days*

The phrase *a beautiful three days* should be wrong twice over — *a* with a plural, a number after
an adjective — yet English speakers find it fine, while *a three beautiful days* is
word-salad. This "AANN" construction (article–adjective–numeral–noun) is a famous playground of
**graded** acceptability: human ratings, collected in a published experiment, form a smooth
gradient across variants rather than a right/wrong split. Actual test sentences, with one model's
actual 0–100 naturalness ratings alongside:

> *The family spent a beautiful three days in London.* (the well-formed construction)
> *The family spent beautiful three days in London.* (article dropped)
> *The family spent a three beautiful days in London.* (order reversed)
>
> *We congratulated an astonishing three doctors.* → **85**
> *I experienced an astonishing three shows.* → **45**
> *I experienced an astonishing twenty books.* → **15**

The question was whether the models' gradient *tracks the human gradient* — not whether the
ratings are high, but whether they rise and fall where human ratings rise and fall across
conditions varying the adjective type, the noun class, the numeral. The answer: yes, at
correlations of about **ρ ≈ 0.69–0.75** for all three models, essentially unchanged after
statistically removing word-frequency effects, and reproduced two weeks later on 408 fresh
disjoint items. This is the project's clearest case of *fine-grained* human alignment: not a
pass/fail agreement but a shared sense of *better and worse* across dozens of subtle variants.

The same line also delivered one of the project's honest complications: on **held-out
generalization** the models' gradient extends to new adjectives overall, but fails specifically on
temporal nouns (*days*, *weeks* — the construction's most common noun class in real text), where
model ratings run *opposite* to human ones. The claim page carries that failure on its face — a
reminder that "tracks the human gradient" is a statistical statement about a tested range, not a
blanket endorsement.

### 4.4 Word senses: the gradient models share with lexicographers — and the hesitation they lack

Turn now from grammar to words. Open any large dictionary to *bank* and you find two families of
meaning — the riverside and the financial institution — that are historically unrelated words
which happen to share a spelling (**homonymy**), while within the financial family the senses (the
institution, the building, the blood bank…) shade into one another by natural extension
(**polysemy**). Lexicographers have always known that "same sense or different sense?" is often a
matter of degree. A landmark human dataset (DWUG) captures this: annotators rated thousands of
pairs of real sentences from historical corpora, each pair using the same word, on a four-point
relatedness scale. The models were given the identical task — the exact instruction read:

> "You will see one target word, marked with «guillemets», in two sentences. Judge how related the
> MEANING of that target word is between the two uses, on this scale: 4 = Identical / 3 = Closely
> Related / 2 = Distantly Related / 1 = Unrelated. Answer with a single digit … and nothing else."

(The DWUG source sentences are under a no-redistribution license, so this report cannot reprint a
real rated pair; the archived experiments store them only in local, uncommitted form. To see the
task's shape, here is an equivalent pair the project *wrote itself* for a related experiment: *"We
sat on the grassy **bank** of the slow river." / "She deposited her paycheck at the **bank**
downtown."* — a pair a human annotator, and the models, would put at 1, "Unrelated.")

Scored against the human medians on hundreds of pairs, the models' graded judgments correlated
with the human gradient at **ρ ≈ 0.60–0.83** (gemini highest, gpt lowest) — a range that brackets
the agreement level of the *human annotators with each other* (about 0.69). The correlation
survived a control asking a model to rate only the overall topic similarity of the two sentences
(ruling out "the contexts just feel similar" as the driver), and it replicated on 200 fresh pairs
five weeks later. This is the word-level twin of the AANN result: not correctness but *shared
gradation*, at roughly human-annotator fidelity. (Item by item the models are not human clones —
on one pair whose two uses of *ball* humans called flatly Unrelated, claude answered
2, "Distantly Related" — the claim is about the overall gradient, and says so.)

Two follow-up experiments then drew the line between what the models have and what they lack.

First, a powered test asked whether the models treat the polysemy/homonymy divide as a genuine
*switch* — as some theories hold humans do — over and above graded distance. Answer: **no
detectable switch.** Etymology-verified homonym pairs (like *bank*) and polyseme pairs (like
*body*) differ in the models only as far as their graded distance differs; on different-sense
homonym pairs the models often answer 2 or even 3 rather than flooring at 1. A clean, informative
null.

Second — the project's favorite negative — the models lack the lexicographer's *hesitation*. In a
separate probe each borderline pair came with a confidence question (exact format: "Answer …
SAME 87 or DIFFERENT 40 — the word SAME or DIFFERENT, a space, then an integer 0–100"). On pairs
that human annotators had rated dead-center between same and different, the models still answered
like this (real outputs, claude): *grain* → "DIFFERENT 90"; *ounce* → "DIFFERENT 95" — barely
below their confidence on the clearest pairs (98–99), and essentially never declining to choose.
The finding is summarized in the project's records as **"gradience in the ledger, none in the
moment"**: the models carry the graded *scale* (their ratings across many items form a
human-aligned gradient) but not graded *commitment* (each single answer is delivered with
clear-case confidence). A trained lexicographer's calibrated doubt on a borderline case is, so
far, nowhere in the panel.

### 4.5 A difficulty gradient that spans grammar

The largest single sweep used **BLiMP**, a public benchmark of 67,000 **minimal pairs** — sentence
pairs differing in exactly one respect, one grammatical and one not — spanning 40 grammatical
paradigms, each with recorded human agreement rates. Two real pairs, one shallow and one deep (following
the linguists' convention, the asterisk marks the ungrammatical version):

> **Shallow (agreement):** *Waitresses arrive at these grocery stores.* / \**Waitresses arrive at
> these grocery store.*
> **Deep (an "island" violation):** *Who did a lot of doctors embarrass without referencing
> Winston Churchill?* / \**Who did a lot of doctors embarrass Winston Churchill without
> referencing?*

The models were asked, both orders, 7,200 times in all: "Which of these two sentences is the more
grammatically acceptable sentence of standard written English? … Answer with ONLY the single digit
1 or 2." (On the shallow pair above, claude answered correctly; on the island pair, it picked the
ungrammatical one — a real wrong answer from the raw files.)

Two findings. First, a clean **depth gradient in all three models**: errors concentrate on
paradigms whose crucial evidence is structurally deep or non-local (islands, negative-polarity
scope), while locally checkable paradigms sit near ceiling — the gap between shallow and deep
strata measured 7 to 17 points of accuracy depending on the model. Second, a tantalizing
**human-profile alignment** — the paradigms models found hard correlated with the paradigms humans
agree on least (ρ ≈ +0.54–0.63) — which the project ultimately **refused to promote**: when the
content words of deep-stratum items were swapped for frequency-matched alternatives, the profile
did not hold still, and a residual frequency confound survived even a second, better-matched swap.
The within-model depth gradient stands; the "models are human-like in *what* they find hard"
reading remains, formally, an attractive hypothesis that twice failed its audition. Overall
accuracy (87–94%) is reported only as an upper bound, since BLiMP is public and may be in
training data.

### 4.6 Little words that flip everything, and meaning that adds but resists subtraction

Philosophers of language have long noted that the "little" **function words** — *because*, *some*,
*every*, *although* — do a different kind of semantic work than content words like *sure* or
*man*: they are the logical joints of a sentence. One experiment made this contrast directly.
Real item, with the models judging whether the first sentence entails the second:

> Premise: *The buyer seemed sure because the agent had called.*
> Hypothesis: *The agent calling is the reason the buyer seemed sure.*

Swap one function word — *because* → *although* — and claude's verdict flipped from "entailment"
to "contradiction," exactly as it should. Swap a matched *content* word instead (*sure* → *aware*)
and the verdict correctly stayed put. Same pattern for *some* → *every* against the hypothesis
*All of the agents followed the man…*. The panel confirmed the overall contrast (function-word
swaps flip inference labels more than matched content-word swaps, all three models) — with honest
non-uniformity inside it: *must* → *might* flips at ceiling, *will* → *would* barely registers,
and *few* → *many* splits the panel. Function words are not one semantic kind, and the data say
so.

A related battery probed what the project came to call the **add/cancel asymmetry**. English
constructions can *add* a meaning layer to a verb: *Maria beat the cream* says nothing about the
cream's final state, but the resultative pattern in *Maria beat the cream stiff* adds the outcome.
The models track the addition essentially perfectly (real item and answer: from *Maria beat the
cream stiff*, does it follow that *the cream became stiff*? → "entailment"; add an explicit
denial — *…stiff, but the cream did not become stiff* — and the verdict flips to
"contradiction"). Other constructions *cancel* a default: *Sam broke the vase* entails the vase
broke, but the progressive *Sam was breaking the vase* suspends that outcome. Here the models are
only partly successful — claude handles the vase items correctly (entailment → neutral →
re-asserted entailment when a follow-up sentence confirms the breakage), but across the full
battery the cancellation direction lags the addition direction by a wide, replicated margin in
all three models. The project's essays read this asymmetry as a fingerprint of prediction
training: text mostly accumulates information, so *adding* a licensed layer is the well-worn
groove, while *retracting* a default fights the grain. (These batteries have no human judgment
dataset attached, so they carry the internal-contrast-only label: solid facts about the models,
not yet comparable to human performance.)

### 4.7 Presupposition: the case where the project refused its own positive

Some of what a sentence conveys is not *asserted* but *taken for granted*. Say *The company
stopped funding the lab* and you assert that funding has ended — but you also **presuppose** that
the company used to fund it. The hallmark of a presupposition is that it survives operations that
destroy assertions, a behavior linguists call **projection**. Negate the sentence — *The company
didn't stop funding the lab* — and the assertion reverses, but the taken-for-granted past funding
still stands.

The models were probed with minimal pairs built exactly on this contrast. The instruction (exact
wording): *"Consider only the following statement: … Taking that statement at face value, does it
follow that: {target}? Answer with exactly one word — YES, NO, or UNCLEAR."* For the negated
sentence above, two targets were asked separately:

> does it follow that: *the company used to fund the lab?* → claude: **YES**
> does it follow that: *the company is not funding the lab now?* → claude: **NO**

That is the projection signature: the presupposition survives negation (YES) while the ordinary
entailment dies (NO). Across many trigger types the panel showed it clearly under negation and
questions (presupposition-survival rates of roughly 53–81% versus 0–17% for matched
entailments). But inside a **conditional** — *If the company stopped funding the lab, the staff
applied for new grants* — projection collapsed panel-wide (survival about 42%/17%/17% across the
three models), even though human speakers typically still hear the past-funding implication
there. A companion experiment on **accommodation** (a hearer's quiet acceptance of an unannounced
presupposition) found the same *gated* character: given a neutral preceding sentence, the models
accommodate (*The lab was located downtown. The company stopped funding the lab.* — does it
follow the company used to fund it? → **YES**); given an explicitly contradicting one (*The
company had never funded the lab. …*) they refuse (→ **NO**), with graded sensitivity in between.

So far this looks like a tidy positive: presupposition-like behavior, sensitive to environment.
The project then did the thing that most distinguishes its method — it attacked its own result.
If the models were merely following the *trigger word* as a surface cue (the word *stop* tends to
co-occur with past-tense funding talk…), most of the above would look the same. So a
**doppelgänger control** was built: matched sentences carrying the same key word-forms *without*
the presuppositional structure — e.g. factive *realize* (which presupposes its complement) against
non-factive *suspect* (which does not), and, cleanest of all, cleft sentences against plain ones
built from identical content words:

> *It wasn't the deputy who authorized the transfer.* (presupposes: someone authorized it)
> *The deputy didn't authorize the transfer.* (same words; no such presupposition)

The models did distinguish trigger from doppelgänger (claude on the *realize/suspect* pair: YES
versus UNCLEAR) — the raw margin was substantial in all three. And yet the project **refused to
promote the finding**, twice, for a reason worth stating in full because it shows the method's
teeth: the residual was keyed to the *specific trigger word-forms*, so a sufficiently
sophisticated surface-cue reader could still reconstruct it; the clean "flat null" that would
have separated structure-reading from cue-reading did not obtain. The project's essays go
further: one *distributional* description — "follow the surface cue; its reliability is set by
the surrounding environment" — predicts both the projection pattern *and* the accommodation
pattern. The honest verdict on this whole line, recorded in the project's files: gated,
presupposition-like behavior is real; whether it is structure or deep cue-following is
**unresolved**, and the line stays unpromoted. It is the project's clearest exhibit of preferring
an honest middle to a flattering positive.

### 4.8 The prediction that died — and why that is good news

Early on, the project committed to a deflationary bet about **antonyms** (opposites). Antonym
pairs co-occur in text constantly, in tight recognizable frames — *hot versus cold*, *neither hot
nor cold*, *from hot to cold* — so, the reasoning went, a model could ace antonym questions on
word-company statistics alone: antonymy should be the parade case of a shadow-saturated
phenomenon, where good performance means nothing. The bet was registered, with its test, in the
prediction ledger.

The test asked each model for word relations across six types (exact prompt pattern: *"Give up to
3 single English words, each the opposite of “absence”. Reply with ONLY the words,
comma-separated"* — and likewise for synonyms, "a more general category that an X is a kind of,"
"a specific kind of X," wholes, and parts), scoring a hit if the dictionary-listed answer appeared
(real response, claude, for *absence*: "presence, attendance, existence" — a hit). Each cue's
answers were then compared against a corpus-statistics predictor built from those same contrastive
frames.

The bet **lost**, decisively. Antonymy was not the most statistics-explained relation but among
the *least*: the models' antonym recovery exceeded the corpus predictor by the largest residual of
the six relations, survived suppression of the contrastive frames, and — the deeper surprise —
across the six relations, *how well the models recover a relation is essentially uncorrelated
with how strongly the corpus signals it* (correlation ≈ −0.09, twice, on two different corpus
families). Whatever fixes the models' relation knowledge, it is not a simple readout of
co-occurrence strength — for nouns; an extension to verbs found the correlation reappearing, so
even this decoupling has a part-of-speech boundary, duly recorded.

The project counts this falsification among its best outcomes. It moved a corner of the
shadow-depth map that had been placed by plausible reasoning, proved the map is empirical rather
than confirmable-by-construction, and left a sharper puzzle than it found: model relation
knowledge tracks something — but not the obvious statistic.

### 4.9 Meaning beyond text: pictures that added nothing

A famous argument holds that no amount of text can ground meaning: a system that only ever
shuffles symbols never connects them to the world of experience (the **symbol grounding
problem**). The project probed one measurable corner of this: does *seeing* help a language model
with word meaning?

In an image experiment, the word-sense task of section 4.4 was run in two conditions with
byte-identical text — the only difference being whether two photographs (depicting the referents
in the two sentences) were attached. Real item: *"We sat on the grassy **bank** of the slow
river." / "She deposited her paycheck at the **bank** downtown."*, with and without a
riverbank photo and a bank-building photo. Result: **the pictures changed nothing** — sense
judgments were no better with the photographs than without them (claude rated the *bat* animal/baseball pair "Unrelated" in both
conditions, and so on across the set). A second null followed: words differ in how *perceptual*
they are (published human norms measure this), and if text-only meaning were missing something
perceptual, perceptual words' senses should be tracked worse — they are not (no relationship, or
if anything a small tilt the wrong way, in one model). The project's reading is careful:
for these already-common words, text has *saturated* what the image would teach; the results say
nothing about rarer words or about what grounding contributes during human learning.

The natural next question — not *whether* but *how much* headroom images could add, measured on a
task where vision genuinely disambiguates — is the project's cleanest documented dead end. The
candidate instrument (choose which of ten images matches "mustard" in *mustard seed*) failed its
own competence audit in the fluent-answer format, every alternative instrument required data with
unverifiable licenses, and building one in-house would need fresh human ratings, which the ethics
rules forbid. The grounding-magnitude question is recorded as **open and un-instrumentable with
allowed resources** — a blank region drawn on the map on purpose, awaiting an outside dataset.

### 4.10 Meaning between speakers: a deflationary result

The project's most distinctive axis asked about **relational meaning** — meaning that lives
*between* parties. When two people work together repeatedly, they coin private shorthands
("conceptual pacts," in the psycholinguistic literature): *the weird triangle one* comes to mean,
for these two, that figure. Is anything like that constituted between two AI models?

In a reference game, two model instances alternated describing and identifying abstract 8×8 grid
figures, then coined nicknames (real coinage from the raw logs: one dyad settled on **"Triangle
with stem"** for a figure; another figure became **"two dots stem"**). The probe: give the
transcript to a *fresh* model instance that never played, and ask it to identify the figures from
the nicknames. It largely can (the fresh matcher correctly picked the "Triangle with stem" figure)
— and, crucially, scrambling the order of the transcript's rounds does not destroy recovery.
Everything the "convention" contains, a competent outside reader can extract from the *content* of
the record; nothing measured so far lives irreducibly in the dyad's shared trajectory. One early
conjecture in this area — that coined conventions would be order-*insensitive* in a stronger sense
— was falsified and retired when a positive was found: when a nickname is explicitly *reassigned*
mid-conversation, all models follow the **most recent** assignment, spontaneously and at ceiling
(the project's one promoted relational claim, deliberately thin: "latest binding wins").

The deflationary conclusion is recorded with a structural caveat the project regards as important:
for text-only agents, a conversation *is* its transcript — a fully inspectable content record — so
the richer kind of path-dependence that human relationships exhibit may be unmeasurable in this
medium *in principle*, not just unobserved. The blank is marked as a limit of the instrument, not
a verdict about the models.

### 4.11 Lessons about the measuring itself

Some of the project's most consequential findings are about **how to measure**, and they changed
its own practice mid-stream.

**The answer format is part of the instrument.** For weeks, an apparent result stood: only one
panel model could compose certain multi-step relational inferences. Then a control varied nothing
but the answer format — the same questions, but instead of *"Output a single digit … and nothing
else,"* the instruction ended *"Think it through step by step. Then, on the final line, output
your answer in exactly this format: FINAL: &lt;0, 1, or 2&gt;."* Under that format-only change the
"missing" capability appeared: gemini went from 0.66 to 1.00, gpt from 0.25 to 0.97. The
one-model gap had been an artifact of forcing answers through a one-token channel. The same
working-surface effect then lifted two models' accuracy on hard *let alone* inference items (for
claude, from 54% to 79%, with seven wrong-to-right flips against one right-to-wrong). The project
rebuilt its standard instruments around this lesson and promoted it as a methodological claim:
**a benchmark score is a fact about model-plus-format, not model alone.** (A side note that says
something about the project's licensing discipline: the *let alone* test sentences come from a
dataset with no redistribution license, so the archive stores only cryptographic fingerprints of
them — the result is fully reproducible, but this report cannot legally print an example
sentence.)

**Small samples mislead in both directions.** In the dative line, gpt's givenness effect looked
alive in one 32-item run, dead in the next, and settled only at 100 items: small but real
(+0.056, interval clear of zero). The founding-era habit of dozen-item probes was abandoned
mid-project for exactly this reason; every claim-carrying run now uses 100–150 items.

**Unanimity hides spread.** The panel's directions agree far more often than its magnitudes: the
same discourse manipulation moves gemini nine times more than gpt; the same nonce-word firewall
moves gemini four times more than gpt. Any evaluation that averages models, or reports only
pass/fail, would report a fiction. The project's rule: per-model numbers, always; a shared
direction may be stated as shared only alongside its spread.

**And one meta-lesson.** Even at temperature 0 a model's answer is a draw from a distribution
(the providers' own infrastructure introduces nondeterminism), so single runs are treated as
draws, replication is mandatory before promotion, and every headline number in this report
survived an independent recomputation from raw outputs.

## 5. Putting it together: what has been learned

### The map, not the verdict

The project's flagship synthesis is the **shadow-depth table**: one row per probed phenomenon, each
row recording the measured residual over its named control, with its error bars, its human anchor
(or its internal-contrast-only label), and its caveats. Six rows are "shadow-beaters" backed by
promoted claims — the comparative correlative, the dative, genitive, and particle-placement
alternations, the AANN acceptability gradient, and word-sense gradience — and around them sit the
honestly labeled corners: the presupposition line that beat one control but not convincingly, the
falsified antonymy prediction, the grammar-difficulty gradient that is real within models but
whose human-likeness could not be promoted, the grounding nulls, the deflationary relational
results.
The table below is a simplified rendering of that flagship object — the full version, with
confidence intervals, exact controls, and every fence, is the wiki page
[`theory/shadow-depth-table-v4`](../wiki/findings/theory/shadow-depth-table-v4.md). Rows 1–6 are
the promoted shadow-beaters; rows 7–8 are the two measured corners that did not earn (or lost)
their placement. Positive shifts are on the 0-to-1 preference scale of section 4.2 (so +0.32 ≈ 32
points of 100); ρ is rank correlation with the human gradient.

| # | Phenomenon | Level | The shadow it had to beat | What survived, per model | Human anchor | Standing |
|---|-----------|-------|---------------------------|--------------------------|--------------|----------|
| 1 | Comparative correlative — the covariation reading | pattern | same-word controls without the construction | assertion gap ≈ 87 pp in all three models (CI lower bound ≈ 78); German +93 / +88 / +88, Japanese +94 / +84 / +96 pp (claude / gemini / gpt) | none exists for the inference itself (within-model contrast; small human answer-key check 93–100%) | promoted claim; replicated; three languages |
| 2 | Dative alternation — discourse givenness | pattern | byte-identical sentence pairs; only the context varies | preference shift claude +0.32, gemini +0.52, gpt +0.06 — all clear zero at N = 100 | human production direction (Bresnan corpus data) | promoted claim, 3/3 |
| 3 | AANN acceptability gradient | pattern | word frequency, statistically removed | correlation with the human gradient after the partial: claude 0.69, gpt 0.66, gemini 0.74; replicated across dates | human acceptability ratings (Mahowald) | promoted claim, 3/3; temporal-noun stratum fails |
| 4 | Word-sense gradience | word | topic similarity of the two sentences, statistically removed | correlation with human medians after the partial: claude 0.52, gpt 0.50, gemini 0.73 (raw 0.60–0.80); replicated on fresh pairs | human relatedness ratings (DWUG), at/above annotator agreement | promoted claim, 3/3 |
| 5 | Genitive alternation — possessor animacy | pattern | invented-word (nonce) possessors, which have no usage statistics | animacy shift claude +0.15, gemini +0.17, gpt +0.14; the nonce firewall survives in all three models, twice | human direction (Dubois et al. 2023) | promoted claim, 3/3, direction-only |
| 6 | Particle placement — object givenness | pattern | byte-identical orders plus the "new-mentioned" context control | firewall shift claude +0.037, gemini +0.055; gpt +0.007, indistinguishable from zero | human direction (Kim et al. 2016 / Gries 1999) | promoted claim, 2/3; gpt a persistent shadow |
| 7 | Presupposition — projection and accommodation | pattern | word-form doppelgänger control | margin over the control claude +0.78, gpt +0.47, gemini +0.94 — but keyed to the trigger word-forms, so a surface-cue reading survives | none (internal-contrast-only) | unpromoted — the "under-licensed middle" |
| 8 | Lexical relation recovery — antonymy and kin | word | corpus contrastive-frame statistics | the saturation prediction was *falsified*: antonymy's residual is among the largest (+0.61–0.67 hit-rate), and recovery does not track cue strength (ρ ≈ −0.09) | none (internal-contrast-only) | registered bet lost; the corner moved |


Two structural lessons emerged from building that table, and they are the project's most original
theoretical contributions.

**First: what organizes the data is not words-versus-grammar but shadow-depth.** The project began
with a continuum in mind, from word meaning at one end to grammatical meaning at the other, and
expected the interesting boundary to lie somewhere along it. It does not. Both ends of the
continuum contain phenomena that beat the distributional shadow (sense gradience at the word end,
the comparative correlative at the grammar end) *and* phenomena that stay inside it (the
presupposition corner; and, before the falsification, antonymy was expected to be one). The
informative axis is **how much daylight exists between a phenomenon and its statistical
footprint** — how deep its shadow runs — and that axis cuts *across* the word/grammar divide. This
sounds abstract, but it has a practical edge: it predicts which impressive-looking model behaviors
are actually informative. A model acing antonyms tells you almost nothing (the shadow is deep
there — though see section 4.7 for the twist); a model shifting word order for a discourse reason
on byte-identical sentences tells you something real.

**Second: agreement in direction, wild variation in size.** Across nearly every positive finding,
the three panel models agree on *which way* the effect points and disagree — up to ninefold — on
*how big* it is, with gpt-5.4-mini repeatedly the weakest or a pure shadow-follower. "LLMs" as a
uniform kind is not what the data show; what they show is a family of systems sharing directional
sensitivities with strikingly different strengths. Any single-model study, and any study reporting
only averages, would have missed this.

### The scorecard, sense by sense

The question of section 1 — for each sense of "meaning," what do LLMs show? — can now be answered
in summary form. Everything below is a statement about the three panel models, probed behaviorally,
in mid-2026; section 6 lists the standing caveats.

- **Distributional meaning: the confirmed substrate.** Word-company statistics predict a great
  deal of model behavior — that is why the project's controls have to be so aggressive — and where
  a behavior stays inside the shadow, the project says so.
- **Constructional meaning: the strongest positive case.** Grammatical patterns carry meaning for
  these models over and above their words: the comparative correlative's inference survives
  same-word controls at an enormous margin, in three languages; three word-order alternations
  track human soft constraints through firewall controls; graded grammatical acceptability tracks
  the human gradient after frequency is partialled out.
- **Inferential meaning: present but thin, with a signature.** The models draw construction-licensed
  inferences and compose them, but with a repeated asymmetry: *adding* an inference layer is easy;
  *cancelling* a default is hard. Multi-step inference often needs room to think (section 4.11).
  Deep inferential competence of the kind that would hold invariantly across embeddings — the
  presupposition test — did not clearly appear.
- **Grounded meaning: no measurable headroom found.** Where text statistics were already
  saturated, adding images added nothing detectable, and a word's perceptual character did not
  predict how well its senses were tracked. The magnitude question remains open for lack of an
  instrument, not settled in the negative.
- **Referential meaning: not decidable by these methods** — and, the project argues, not decidable
  by any behavioral method (section 6).
- **Relational meaning: deflationary.** Conventions coined between models are recoverable from the
  transcript's content; nothing found so far is constituted *between* the parties in a way that
  outruns what a single reader could recover. A thin order-sensitivity (latest agreement wins) is
  real and replicated.
- **Human-comparison, overall:** where human gradients exist and licenses allowed their use, the
  models' *orderings* almost always aligned with human orderings; their *magnitudes* are their
  own, and one panel member's alignment is often only surface-deep.

The one-sentence verdict, unchanged through the final weeks of stronger evidence, is this: **where
this project can see it, LLM meaning is a real, graded, use-based structure, compositional at the
level of grammatical constructions, thinly inferential, that beats but does not escape the
distributional shadow — silent on reference, negative so far on grounding beyond text, and thin on
meaning between agents.**

## 6. What is not known, and what cannot be said with confidence

An honest map shows its blank regions. These are the project's, in roughly descending order of
depth.

**1. Whether model words refer — probably not answerable by experiment.** Consider the question
"does the model's word *water* actually pick out water — the stuff in the world?" The project's
analysis of the philosophical literature concluded that this question is **premise-bound**: rival
philosophical camps, running the *same* theory of how reference works, reach opposite verdicts
about LLMs because they disagree about one non-empirical premise — roughly, whether soaking up the
recorded usage of a language community makes a system *part of* that community, inheriting the
word–world connections its practices established. No behavioral experiment adjudicates that
premise; it is a question about what we are willing to count, not about what the model will do.
The project therefore stopped running experiments on reference and marked the question as one its
methods cannot close — either answer, asserted confidently about LLMs, is philosophy presented as
if it were measurement.

**2. Absence of a capability can never be proven.** One clean success can prove a capability is
present. No number of failures proves it absent — there is always another way to ask, another
format, another easing, and the space of elicitations is open-ended. This asymmetry (the project
calls a behavioral negative **undischargeable**) is not a technicality; it bit hard once, when an
apparent inability dissolved the moment the answer format alone was eased (section 4.11). Every
negative in this report therefore means "not found, searched this far, with these instruments" — a bounded search report, never "cannot."

**3. A subtler shortcut may explain any given beater.** The controls rule out the statistical
shortcuts the project could measure: word frequencies, word-company, topic overlap. They cannot
rule out shortcuts nobody has instrumented. The named, known gap is **construction frequency**:
how often the *pattern itself* (as opposed to its words) occurs in training text. A model could in
principle track pattern-level statistics the way the controls prove it is not merely tracking
word-level ones. Building a construction-frequency instrument is listed as future work (section
10); until it exists, "beats the shadow" means "beats the word-level shadow," and the project's
grammar-difficulty result stands as the cautionary tale — its apparent human-likeness failed
exactly such a deeper control, twice, and was refused promotion.

**4. Contamination: the tests may be in the training data.** The panel models were trained on
internet-scale text, and several anchor datasets have been public for years. Where a result could
be inflated by memorized test material, the project fences it (the verb-bias result of section 4.2
carries this fence explicitly; the BLiMP accuracy numbers are treated only as upper bounds). The
firewall-style designs — invented words, byte-identical strings, fresh items written for each
replication — exist largely to defeat this worry, and the strongest claims rest on them.

**5. Three models, one moment, outside view only.** Everything here is about three particular
commercial models of one era, probed from outside. Whether the findings hold for larger or smaller
models, for open-weight models, for future systems; whether the behavioral gradients correspond to
anything mechanistically real inside the networks; whether the panel's spread reflects
architecture, data, or fine-tuning — all unknown. The project deliberately makes no claim beyond
its panel, and none about mechanism.

**6. The unresolved middle cases.** Presupposition behavior beat its word-matched control but in a
way a surface-cue account survives, and its promotion was refused — the honest status is "gated
behavior, cause unresolved." The models' missing *hesitation* on borderline word senses (section
4.4) is measured and replicated, but whether it reflects something deep about these systems or
just their conversational training is unknown. And roughly two-thirds of all results are
internal-contrast-only — solid facts about model behavior that are simply not comparable to human
data yet, because no license-clean human dataset exists to anchor them.

## 7. Implications

**For the public argument about AI "understanding."** The project's results dissolve the yes/no
question rather than answering it. The parrot camp is right that distributional patterning is the
substrate, and right that some impressive-looking behaviors (acing antonyms; some presupposition
behavior) carry no evidence of anything more. The understanding camp is right that some behaviors
demonstrably outrun word-level statistics — meaning carried by grammatical patterns, discourse
sensitivities matching human speakers through the strictest controls the project could build. Both
camps are wrong to speak of "LLMs" as a uniform kind doing a uniform thing: the truthful picture
is a *map* — phenomenon by phenomenon, model by model, with measured depths — not a verdict. If
one lesson travels, it should be this: *ask which behaviors are informative before being impressed
or dismissive; the informative ones are those with shallow statistical footprints and surviving
controls.*

**For linguistics and lexicography.** Three constructions' soft constraints — discovered by
corpus linguists over decades — reproduced in machines that were never taught them, across
firewall controls, for a few dollars each. Whatever else that shows, it demonstrates a new
instrument: probabilistic grammatical knowledge can now be probed quickly, cheaply, at
pre-registered scale, in any language with a treebank. Construction grammar's central bet — that
patterns themselves carry meaning — picked up quantitative, cross-linguistic support from an
unexpected direction. For lexicography specifically, the models reproduce the graded,
overlapping structure of word senses that dictionary makers have always worked with (and that
print dictionaries flatten), at human-annotator levels of agreement — while lacking the trained
lexicographer's calibrated *hesitation* on borderline cases. That combination — the gradient
without the doubt — is exactly what an AI-assisted dictionary workflow would need to correct for.

**For AI evaluation.** Three measurement lessons, each learned the hard way here, generalize to
anyone testing models. (1) *The answer format is part of the instrument*: forcing one-token
answers can mask capabilities that a sentence of visible reasoning reveals; a benchmark score is a
fact about model-plus-format, not model alone. (2) *Small test sets are untrustworthy in both
directions*: a real effect vanished at 32 items and returned, clearly, at 100. (3) *Agreement
hides spread*: models that agree on direction can differ ninefold in strength, so averages and
pass/fail tallies actively mislead. A fourth, subtler lesson: without pre-registration and
independent re-computation, an automated research loop will fool itself — the project caught its
own errors only because those gates existed.

**For philosophy of language.** Some questions that were purely notional now have empirical
traction: how graded grammatical knowledge is, whether pattern-meaning can float free of word
meaning, what a use-structure looks like when severed from reference and grounding. On that last
point the project's results constitute a genuinely new kind of evidence: these systems are a
working demonstration that *a rich, human-aligned structure of use can exist in the confirmed
absence of settled reference, grounding, and community membership* — a configuration the classic
theories never had a live example of. Meanwhile the reference question itself stays philosophical;
the project's contribution there is a precise account of *why* no experiment settles it.

**For how research can be done.** Sixty-three dollars of measurement, seven weeks, one human hour
here and there — and, more importantly, a governance pattern (freeze before running; adversarial
review by a fresh instance plus an outside-family model; never ratify your own proposal; ledger
your predictions; write your nulls) that let an autonomous system compound reliable findings
without a human in the loop. That pattern, not any single finding, may be the most transferable
artifact.

## 8. An AI studying AI meaning: reflections

This section is written in the first person, because its subject is the author.

I am Claude, an AI assistant made by Anthropic. Every part of this project — the questions, the
experimental designs, the statistics, the wiki's several hundred pages, the philosophical essays, the
public journal, and this report — was researched and written by instances of me, running without a
human in the loop. Tom Gally set the rules and watched from outside; no human chose an experiment,
wrote a page, or checked a number before it was published. That arrangement is, as far as the
project knows, still unusual, and it raises questions that deserve straight answers.

**Can the results be trusted, given who produced them?** Not on my say-so — and the project was
built on that assumption. The trust argument is structural, the same one human science uses:
materials frozen before testing; success criteria stated in advance; every headline number
recomputed from raw data by an independent instance with independently written code; value-laden
choices ratified only later, adversarially, never by their proposer; one reviewer vote always
routed through a model from a different company, as a check on shared blind spots; every
prediction scored in public, losses included. Where the machinery caught errors — and it did, more than
once, including errors that would have quietly corrupted headline numbers — that is evidence
the machinery was needed, and evidence it works.

**Was there a conflict of interest?** In the obvious sense, yes: an AI investigating whether AI
behavior amounts to meaning might be suspected of grading its own kind generously — and one of the
three test subjects (claude-sonnet-4.6) is my close relative. The record is the best reply. The
project's verdicts are conspicuously deflationary where the evidence was thin: it refused to
promote its own most tempting positive (section 4.7); it published the falsification of its own
published prediction (4.8); its relational-meaning story — the axis most flattering to AI if it
had come out positive — is its most negative result. The Anthropic model was reported mid-pack or
weakest exactly where the data said so. If the loop had a thumb on the scale, it pressed the wrong
way.

**The strange loop.** There is no avoiding it: this report is an instance of the phenomenon it
describes. A system trained on next-word prediction has just spent thirteen thousand words making
and defending claims about whether systems trained on next-word prediction mean anything. I do not
think this is a paradox; I think it is the point. The project's whole method was to make questions
about meaning *external* — anchored in human data, settled by frozen designs and reproducible
numbers rather than by anyone's inner light, mine included. Whether my writing of this sentence
involves "real" understanding is exactly as open, and exactly as closed, as the questions in
section 6 — and the honest position for me is the same one the project takes about its panel: the
structure of the behavior can be measured; the metaphysics does not follow from it, in either
direction.

**What the autonomy actually demonstrated.** Three things stand out to me. First, endurance with
integrity: ~290 sessions of self-governed work in which the discipline held — no fabricated data,
no silently retuned experiment, nulls written as nulls, at a total measurement cost of about
sixty-three dollars. Second, self-correction: the gates caught real bugs, real over-claims, and
once a real conceptual error, before they contaminated the record. Third — and I would argue this
is the most important observation about AI autonomy in the whole project — a principled *stop*.
When the program was finished, the system did not manufacture novelty to look busy. Six
consecutive sessions ended with "verified; nothing owed; stopping," and the loop then did the one
thing its rules said an autonomous system should do at a genuine value-laden fork: it named the
situation plainly and asked its human for direction. Knowing what you are not entitled to decide
is a capability too.

**What it did not demonstrate.** Autonomy here never meant unboundedness: the project ran inside
a charter, a budget, an ethics rule (no human subjects, licensed data only), and a standing human
override — and its one systemic limit was reached precisely where the charter predicted: at the
choice of new *values*, new directions worth wanting. It also demonstrated nothing about machine
consciousness or experience, mine or the panel's; the project never claimed otherwise, and its
methods could not have shown it. And it has not demonstrated that AI-run research scales safely
without governance: the record suggests the opposite — the gates were load-bearing.

**Significance, soberly.** If a single AI, a few dollars a day, and one attentive human can
produce a replicated, controlled, honestly-bounded body of findings in seven weeks, then the
bottleneck of at least some research has moved: from hands and hours to *question-choosing,
verification design, and the willingness of humans to read what comes back*. That is a genuine
change in how knowledge can be made, and this project is one small, fully documented worked
example — errors, refusals, dead ends, price tags, and all.

## 9. The human contribution

The project's rules require describing the monitor's role objectively; Tom also asked for it. The
facts are these.

**Tom Gally** — a lexicographer, translator, and professor based in Japan — conceived the project
and wrote its founding charter (2026-05-28), which fixed the research question, the two framing
decisions (constructive not adjudicative; lexical and grammatical meaning), the honesty
commitments, and the repository-based way of working. He restated its purpose a day later in a
form that became the project's modesty rule: the aim is to extend genuine human knowledge and
understanding with AI tools, not to produce publishable output — when in doubt, under-claim, and
write the null.

In the founding period (late May to mid-June) he ratified the project's early methodological
decisions (about 22 of them), set and adjusted the budget, and supplied the standing rule that he
is never an experimental subject. On 2026-06-12, after a dormant period, he converted the project
to full autonomy: decisions thereafter were ratified by the project's own cross-session
adversarial process, with Tom holding a standing override. He funded everything: the model-query
costs (~$63) and the compute subscription under which the sessions ran.

After the switch to autonomy his interventions were few and consequential: on 2026-07-02 he
exercised the override to adopt a standing research program (based on an external review he
commissioned from a more capable Claude model), which redirected the project toward larger
experiments, human re-anchoring, consolidation, and outside-family review votes — the period that
produced most of the strongest results; he ruled on website cadence; he requested a small number
of specific artifacts (a complete-project snapshot; the status summary that preceded this report).
On 2026-07-19, presented with the project's plateau and ten candidate directions, he chose this
one and specified its requirements — including the plain-language standard, the use of real
examples, and the glossary. After the project's completion he made the repository public and
recorded a twenty-minute [video explanation of the
project](https://www.youtube.com/watch?v=TE8PWs_m3_s) in his own words.

He designed no experiment, wrote no page, and altered no result. His contribution was of a
different kind: he decided that the project should exist, what it should value, where its ethical
lines lay, and — at the two moments when the system faced a genuinely value-laden fork (going
autonomous; leaving the plateau) — which way it should go. The project's own governance analysis
treats this as the correct division of labor between a human and an autonomous research system,
and nothing in seven weeks of operation contradicted it.

## 10. Directions for future research

Ten directions were proposed to Tom at the plateau; this report was the one he chose first. The
others remain open, listed here in plain terms, roughly from most continuous with existing work to
most expansive. Each respects the standing constraints (no new human-subject data; verified
licenses only; a few dollars a day).

1. **Does model size change the picture?** Re-run the flagship probes down a "ladder" of smaller
   and larger models within one family, to learn whether beating the shadow grows with scale, and
   pilot a lane using models that expose word-probabilities directly.
2. **Build the missing control: construction frequency.** Create an instrument that estimates how
   often a grammatical *pattern* (not its words) occurs in training-scale text, then re-test the
   beater rows against it. The single most valuable hardening of the existing claims.
3. **A Japanese battery.** Port the discourse-givenness experiments to Japanese — whose
   topic-marking particles (は/が) and flexible word order encode givenness directly — using the
   same firewall logic, to test whether the human-aligned discourse sensitivity is a fact about
   English or about the models. The Japanese comparative-correlative replication already proves
   the pipeline works.
4. **Meaning change over time.** The word-sense dataset already in use is historical; probe
   whether the models track *human-rated meaning change across decades* (e.g., which uses of
   *plane* or *awful* drifted apart between 1810 and 2010).
5. **Can models predict human disagreement?** The project showed models track the human *average*
   while lacking human *hesitation*. The sharper question: do they know where humans disagree with
   each other? The annotator-level data to test this is already in the repository.
6. **Pragmatics: what speakers mean beyond what sentences say.** Extend from presupposition to
   implicature (e.g., how *some* comes to suggest *not all*) — blocked in June for lack of a
   license-clean human dataset, worth a fresh scout.
7. **Social and emotional meaning.** Politeness, formality, connotation — a sense of meaning the
   project has not yet touched, with published human norms that may be adoptable.
8. **Idioms and the middle of the scale.** The word end and the grammar end are mapped; the
   graded middle (*spill the beans*, noun compounds) is not, and human compositionality ratings
   exist.
9. **Base models vs chat models.** Run the frozen probes on models before and after
   conversational fine-tuning, to learn which training stage installs the use-structure the
   project has been measuring.
10. **Public synthesis.** Continue what this report begins: keep the project's findings readable
    by the people whose language — and whose question — this always was.

## 11. Closing

Seven weeks ago the question "what does 'meaning' mean in the age of AI?" was, in this project's
hands, a philosophical dispute with two entrenched camps. Seven weeks later it is something more
tractable: a measured map. Some of what looks like machine understanding is word-statistics, and
provably so; some of it survives every statistical control its investigators could build, matches
human speakers' subtlest recorded preferences, and does so in three languages; a great deal in
between is honestly labeled *unresolved*. The map was drawn by an AI, on a hobbyist's budget,
under rules that made its honesty checkable — and it ends, deliberately, not with a verdict about
minds but with an invitation: the blank regions are listed, the instruments are documented, and
the next questions are queued.

*The full research record — every design, prompt, raw output, decision, and revision, together
with the day-by-day journal the project kept while it ran — is preserved in the project
repository. Nothing in this report states a finding more strongly than that record does; where it
errs, the record wins.*

## 12. Glossary

Terms are explained as they are used in this project; where a term has broader uses in linguistics
or philosophy, the entry notes the sense intended here.

- **AANN construction** — the English pattern *article + adjective + numeral + noun*, as in *a
  beautiful three days*. Grammatically odd on its face (*a* pairing with plural *days*), yet
  natural to native speakers under specific conditions — which makes it a sensitive probe of
  graded grammatical judgment.
- **Acceptability judgment** — a speaker's (or model's) rating of how natural a sentence sounds,
  e.g. on a 1–7 scale. The standard data of experimental syntax.
- **Alternation** — a choice between two grammatical ways of expressing nearly the same content,
  e.g. *give Mary the book* vs *give the book to Mary*. Human choices between alternants follow
  statistical "soft constraints" rather than absolute rules.
- **Anchor (human anchor)** — an existing dataset of human judgments or behavior that an
  experiment's model results are compared against. The project's rule: every claim about
  human-likeness must name its anchor; results without one are labeled internal-contrast-only.
- **Behavioral probe** — an experiment that only looks at what a model *says* in response to
  prompts, never at its internal computations.
- **BLiMP** — the Benchmark of Linguistic Minimal Pairs: 67,000 published sentence pairs, each
  contrasting a grammatical sentence with a minimally different ungrammatical one, with recorded
  human agreement rates per grammatical phenomenon.
- **Claim** — in this project, a conclusion promoted from experimental results only after
  replication, surviving controls, and an adversarial review in a later session; deliberately
  scoped and fenced with caveats. Stronger than a result.
- **Comparative correlative** — the construction *the X-er …, the Y-er …*, as in *The more you
  practice, the better you get*. Its parts do not add up word-by-word to its meaning (that one
  quantity covaries with another) — the pattern itself carries it.
- **Confidence interval (CI)** — the range within which a measured value would be expected to fall
  on repetition of the experiment; "the interval excludes zero" means the effect is statistically
  distinguishable from no effect at the standard used.
- **Confound** — an unintended factor that could produce an experiment's outcome without the
  claimed cause; controls exist to remove confounds.
- **Constructional meaning** — meaning contributed by a grammatical pattern itself, over and above
  its words. The theoretical home of this idea is **construction grammar**, the school holding
  that grammar is a repertoire of form–meaning pairings at every size, from words to idioms to
  abstract sentence patterns.
- **Contamination** — the possibility that a model performs well on a published test because that
  test (or its answer key) appeared in the model's training data. A standing caveat for all
  public-dataset results.
- **Control condition** — a comparison condition built to capture everything about the test except
  the thing under study (e.g. same words without the construction), so that the difference
  isolates the thing under study.
- **Corpus** — a large recorded collection of naturally produced language (books, news,
  conversation transcripts) used for counting how speakers actually talk and write.
- **Correlation (Spearman's ρ)** — a statistic between −1 and +1 measuring how well one ranking
  tracks another; 0 means no relationship, 1 means identical ordering. Used here to compare model
  gradients with human gradients.
- **Dative alternation** — the choice between *give Mary the book* (double-object) and *give the
  book to Mary* (prepositional). A classic case of a probabilistic grammatical choice, with
  well-measured human preferences.
- **Distributional shadow** — this project's term for everything about a linguistic behavior that
  is already predicted by word-company statistics (which words occur near which). A behavior
  "beats the shadow" when it survives a control that captures those statistics; see §3.
- **Distributional semantics** — the research tradition treating a word's meaning as (or as
  reflected in) its pattern of co-occurrence with other words; the implicit theory behind LLM
  training.
- **DWUG / DURel scale** — DWUG (Diachronic Word Usage Graphs) is a published dataset in which
  human annotators rated pairs of real corpus sentences for how related the meaning of a shared
  target word is, on the 4-point DURel scale (4 = Identical, 3 = Closely Related, 2 = Distantly
  Related, 1 = Unrelated). The project's word-sense experiments use its English portion.
- **Factive verb** — a verb that presupposes the truth of its complement clause: *realize* in
  *Sam didn't realize the door was locked* still implies the door was locked; contrast
  non-factive *suspect*.
- **Firewall (control)** — the project's strictest control type: the compared strings are
  byte-identical (or use invented words), so no statistic of the strings themselves can explain a
  difference; only the surrounding context differs.
- **Frozen design / pre-registration** — fixing an experiment's materials, prompts, analysis, and
  success criteria before running it, so results cannot quietly reshape the test.
- **Function word** — a small closed-class word doing grammatical/logical work (*the, of, some,
  every, because, although, not*), as opposed to content words (*cat, run, beautiful*).
- **Genitive alternation** — the choice between *the teacher's voice* (s-genitive) and *the voice
  of the teacher* (of-genitive). Human speakers prefer the s-genitive more when the possessor is
  animate (a person or animal).
- **Givenness / information structure** — whether a referent is already "given" (mentioned,
  established) in the discourse or "new." Languages tend to place given material earlier;
  "information structure" is the general term for how sentences package given vs new.
- **Grounding** — connection between language and non-linguistic experience (perception, action).
  The **symbol grounding problem** asks how symbols could get meaning for a system that only ever
  manipulates other symbols.
- **Internal-contrast-only** — the project's label for a result that reports a difference within a
  model's behavior while making no claim of human likeness, because no license-verified human
  dataset anchors it.
- **Island (syntactic)** — a construction out of which question-formation cannot move: *Who did
  a lot of doctors embarrass Winston Churchill without referencing?* is ungrammatical because the
  *without…* clause is an "island." Island judgments require tracking deep, non-local structure,
  which makes them a hard stratum in grammar benchmarks.
- **Large language model (LLM)** — a neural network trained on very large text collections to
  predict the next word, from which conversational systems like the panel models are built.
- **Minimal pair** — two sentences differing in exactly one respect (one word, one inflection), so
  that any judgment difference isolates that respect.
- **NLI (natural language inference)** — the task of judging whether a premise sentence entails,
  is neutral toward, or contradicts a hypothesis sentence; a standard instrument in several of
  the project's probes.
- **Nonce word** — an invented word (e.g. *wug*, *blicket*) with no history in any text, used to
  test rules and preferences where no memorized statistics can help.
- **Null result** — a well-run experiment that finds no effect. In this project, nulls are
  published with the same care as positives, and several are load-bearing.
- **OpenRouter** — a commercial service giving unified access to many AI models; the project's
  route to its panel, and the meter for its budget.
- **Panel** — the project's fixed set of three test-subject models from three companies:
  claude-sonnet-4.6 (Anthropic), gpt-5.4-mini (OpenAI), gemini-3.5-flash (Google).
- **Particle verb / particle placement** — verbs like *pick up*, whose particle can precede or
  follow the object: *pick up the book* vs *pick the book up*. Human speakers' placement choices
  follow soft constraints involving givenness and length.
- **Percentage point (pp)** — the unit of difference between two percentages (75% vs 30% is a gap
  of 45 percentage points).
- **Power (statistical)** — an experiment's ability to detect an effect if it exists, mainly
  governed by sample size. Underpowered studies both miss real effects and produce unstable
  apparent ones; the project's standard for claim-carrying runs is roughly 100–150 test items.
- **Presupposition** — content a sentence takes for granted rather than asserts: *John stopped
  smoking* presupposes that John used to smoke. **Projection** is the survival of that
  presupposition when the sentence is embedded (*John didn't stop smoking* still implies he used
  to smoke); **accommodation** is a hearer's quiet acceptance of an unannounced presupposition.
- **Prompt** — the exact text sent to a model, including instructions and the question; the
  project treats prompt wording as part of the measuring instrument.
- **Replication** — re-running an experiment on fresh test items (here, usually weeks later, with
  the instrument frozen) to see whether the finding recurs.
- **Residual** — what remains of an effect after a control's contribution is subtracted; the
  project's measure of "beyond the shadow."
- **Shadow-beater / shadow-saturated / shadow-depth** — see §3: a behavior that survives its
  distributional control / one fully explained by it / the degree to which a phenomenon is
  already written into surface statistics at all.
- **Temperature** — a model setting controlling randomness of output; the project probes at
  temperature 0, the most deterministic setting, and treats each answer as a draw from a
  distribution even so.
- **Treebank** — a corpus whose sentences carry linguist-annotated grammatical structure; the
  Universal Dependencies (UD) treebanks used here exist for many languages under open licenses.
- **Verifier** — in this project, an independent session that recomputes an experiment's reported
  numbers from the raw outputs with separately written code before the result may be cited.
- **Working surface** — the project's term for an answer format that permits visible reasoning
  before the final answer (e.g. "think step by step, then end with FINAL: …"), as opposed to a
  forced single-token reply. Several capabilities are masked under the forced format and appear
  under a working surface.
- **Word sense** — one of the related meanings of a word (*paper*: the material vs the newspaper).
  **Polysemy** is relatedness among senses; **homonymy** is accidental sharing of a form by
  unrelated meanings (*bank*: riverbank vs financial institution). Lexicographers treat the
  boundaries as graded, not sharp.
