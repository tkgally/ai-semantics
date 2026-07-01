---
type: source
id: clark-chalmers-1998-extended-mind
title: "Clark & Chalmers, \"The Extended Mind\" — the parity principle, active externalism, and Otto's notebook"
authors:
  - Clark, Andy
  - Chalmers, David J.
year: 1998
venue: "Analysis 58(1):7–19 (self-archive header: Analysis 58:10-23, 1998)"
url: https://consc.net/papers/extended.html
access: open-access
meaning-senses:
  - grounded
  - referential
status: received
created: 2026-07-01
updated: 2026-07-01
links: []
---

# Clark & Chalmers 1998 — "The Extended Mind"

## What it is

Andy Clark and David J. Chalmers, **"The Extended Mind,"** published in *Analysis*, 1998 — the founding
statement of **active externalism** and the **extended mind** thesis in philosophy of mind. The paper
argues that when a part of the external world is coupled to a biological agent in the right way, that
external part can be a literal constituent of a cognitive process (its most famous illustration is *Otto's
notebook*). It is a work of **philosophy of human/embodied cognition**; it makes **no claim about LLMs or
AI systems**. The project uses it only as an interpretive frame; see *What it grounds*.

**Meaning-senses.** Tagged `grounded` and `referential` per [`meaning-senses.md`](../../meaning-senses.md).
`grounded` is the primary fit: the paper is the canonical statement of cognition as *anchored in and
constituted by* non-linguistic couplings between agent and environment — the family the project's
`grounded` tag names ("Meaning as anchored in non-linguistic experience — perception, action, body, social
embedding"), including its `grounded.causal` sub-distinction (the coupling turns on the external resource's
active causal role in driving the process). `referential` is secondary: the Otto case is about how an
external store fixes *what a belief is about* (the museum's location), which bears on the externalist
tradition the `referential.externalist` sub-tag names ("meaning fixed by causal/social embedding"),
extended here from content to cognitive process. It is **not** tagged `distributional` or `inferential`:
the paper is not about co-occurrence structure or inferential role.

**Provenance.** Quotes below were verified against the author self-archive HTML at
`https://consc.net/papers/extended.html` (David Chalmers' own author page — a legitimate open-access
route), retrieved 2026-07-01. The `.html` fetch succeeded; the `.pdf` fallback was not needed. The HTML is
**unpaginated**, so locators are section names / the ordinal position of list items, not page numbers.
Italicized words in the original are marked with underscores or noted inline.

**Citation-metadata caveat (flag).** The self-archive header renders the venue as **"*Analysis* 58:10-23,
1998"** (author order Andy Clark, then David J. Chalmers — Clark first, confirmed). The widely-cited page
range for the article is **58(1):7–19**; the self-archive's own header gives **10-23**. Both are recorded
above; the discrepancy is a pagination-metadata difference between the self-archive and the standard
citation, not a content difference. The **year (1998)**, **venue (*Analysis*)**, and **author order (Clark,
Chalmers)** are confirmed from the self-archive header. A downstream unit that needs the exact printed page
range should check the journal of record; do not treat either figure as independently verified beyond the
self-archive.

## The typology it provides

### The parity principle

The load-bearing statement of the paper's method — a criterion for when an external process counts as
cognitive. Verbatim (early in the paper, stating the "Parity Principle"; italics as marked):

> "If, as we confront some task, a part of the world functions as a process which, _were it done in the
> head_, we would have no hesitation in recognizing as part of the cognitive process, then that part of the
> world _is_ (so we claim) part of the cognitive process."

### Active vs. passive externalism

The paper distinguishes its view from the classical (Putnam/Burge) externalism about mental content. C&C's
label for their own position (§ "Active Externalism"), verbatim:

> "an _active externalism_, based on the active role of the environment in driving cognitive processes"

And the contrast with the classical view: Putnam's and Burge's externalism turns on features that are
*passive* — "distal and historical" and playing "no role in driving the cognitive process in the
here-and-now" — whereas on C&C's view, verbatim:

> "In these cases, the relevant external features are _active_, playing a crucial role in the here-and-now."

(The characterization of the Putnam/Burge view as "distal and historical" / "passive" is C&C's framing in
the same section; the *active* sentence is the verbatim-confirmed fragment. The surrounding "passive /
distal and historical" phrasing is reported as C&C's framing but was returned to me as adjacent context
rather than confirmed as a single verbatim block — treat that phrase as **not verbatim-verified** below the
one confirmed sentence.)

### Otto and Inga

The paper's central thought experiment: Inga, with normal biological memory, recalls that the museum is on
53rd Street and walks there; Otto, who has Alzheimer's, stores the same information in a notebook he
carries and consults. C&C argue the two cases are parallel. Verbatim:

> "For in relevant respects the cases are entirely analogous: the notebook plays for Otto the same role
> that memory plays for Inga."

And the Otto case as narrated, verbatim:

> "He consults the notebook, which says that the museum is on 53rd Street, so he walks to 53rd Street and
> goes into the museum."

### The four "glue and trust" conditions

To say *when* an external resource counts as part of the cognitive system, C&C list the features of the
Otto case that "make the notion so clearly applicable there." The list is introduced, verbatim:

> "To help understand what is involved in ascriptions of extended belief, we can at least examine the
> features of our central case that make the notion so clearly applicable there."

The four features are given as an ordinal list ("First … Second … Third … Fourth …"). Verbatim opening of
each (in the order they appear in the Otto section):

1. **Constant availability / typically invoked** —
   > "First, the notebook is a constant in Otto's life — in cases where the information in the notebook
   > would be relevant, he will rarely take action without consulting it."
2. **Easily / directly accessible** —
   > "Second, the information in the notebook is directly available without difficulty."
3. **Automatically endorsed on retrieval** —
   > "Third, upon retrieving information from the notebook he automatically endorses it."
4. **Consciously endorsed in the past** —
   > "Fourth, the information in the notebook has been consciously endorsed at some point in the past, and
   > indeed is there as a consequence of this endorsement."

These four conditions are **load-bearing for the project's use** (see below); a later analysis must check a
tool-case against each. (Note on locators: the fetched HTML is unpaginated; a fetch labeled these as
appearing in "Section 5," but the section *number* was supplied by the fetch tool, not independently
confirmed against a canonical section scheme — cite them as "the four features in the Otto/extended-belief
section," which is verbatim-anchored, rather than by a section number.)

## What it grounds in this project (relevance)

This is the **canonical active-externalist / extended-mind account named by trigger (b)** of the essay
[`essay/origo-supplied-not-occupied`](../../findings/essays/origo-supplied-not-occupied.md). That essay
splits an indexical's meaning (`referential`) along Kaplan's character/content seam and isolates a **channel
claim (ii)**: that *every* origo — including a tool-return such as `get_current_time()` — reaches a
text-only model through the **described** channel (text the model conditions on), so a tool "only adds
another *described* channel" and "does not convert a described origo into an occupied one"
([`essay/origo-supplied-not-occupied`](../../findings/essays/origo-supplied-not-occupied.md), "Three claims,
not one").

The essay's pre-registered **trigger (b)** anticipates exactly the account this source supplies:

> "**(b) An extended-mind / active-externalist account on which tool-mediated access constitutes occupying a
> context.** A philosophical account that argues a tool the system reliably queries is *part of* the
> system's context-fixing apparatus … would **weaken claim (ii)** directly: it would deny that a tool-return
> is merely 'another described channel' and re-classify it as constitutive of an occupied origo."
> ([`essay/origo-supplied-not-occupied`](../../findings/essays/origo-supplied-not-occupied.md), Revision
> triggers)

Clark & Chalmers 1998 **is** that account, at **primary-author-self-archive strength**. It supplies the
philosophical lever a later unit will use to press on claim (ii): the parity principle plus the four
conditions give a *criterion* under which a reliably-queried external resource is claimed to be
constitutive of — not merely input to — the cognitive system. If a queried clock/location tool meets the
four conditions, an extended-mind reading would classify the tool-return as **constitutive of an occupied
origo** rather than merely described, which is precisely what would weaken the essay's channel claim (ii).

**The four conditions are the checklist a later analysis must run the tool-case against.** A queried clock:
does it meet (1) constant availability / typically invoked, (2) easy/direct accessibility, (3) automatic
endorsement on retrieval, and (4) past conscious endorsement? That case is *not made here* — this page only
catalogues the criterion. The essay owns any application, and (per its own discipline) a stronger claim
must pass independent adversarial-review ratification.

## Honest bounds

1. **Philosophy of human/embodied cognition, not a claim about LLMs.** The paper concerns coupling between
   biological agents and external resources; it says nothing about machine systems. The project applies it
   as an interpretive frame only; the essay owns the application and makes **no human-vs-LLM empirical
   claim**.
2. **NOT a human anchor.** No dataset, no annotations, no measured human baseline. It cannot ground any
   empirical claim about LLM meaning; it is a map / interpretive frame, not a labeled resource. YAML
   `links:` is empty and no `anchors` relation originates here.
3. **The extended-mind thesis is contested in the literature.** Standard objections include "cognitive
   bloat" worries and the objection that **coupling is not constitution** (a causal coupling between agent
   and resource need not make the resource *part of* the mind). These are stated here as *general,
   uncited* characterizations of the literature — the fetched C&C text was not mined for named critics, and
   no critic name or quote is fabricated. A later unit that wants a specific critique must ingest that
   critic's own text.

## What it cannot ground

- Any empirical claim about what an LLM *is* or *does* — the paper is about human cognition; it provides no
  measurement, no baseline, no annotated data.
- Any claim that a tool-return *is* constitutive of an occupied context for a model. The paper supplies a
  *criterion* (parity + four conditions) applicable to *human* cases; whether it transfers to a text-only
  model's tool-return is an additional argumentative step the source does not take and the project owns.
- The magnitude or direction of any model effect.

## Known limits

- **A primary philosophical paper, not a survey and not a resource.** It argues one position; where the
  literature disagrees is not represented in the paper itself (its critics came later). Treat the parity
  principle and the four conditions as a well-motivated frame, not a settled theorem.
- **Coupling-vs-constitution gap acknowledged as contested** (above); the project should not lean on
  extended-mind constitution as if uncontested.
- **The parity/occupation gap (flag — this matters for the essay).** The parity principle concerns whether
  an external resource is part of a **cognitive process / the cognitive system**. Whether being part of a
  cognitive process is the *same* as **occupying a Kaplanian context of utterance** (an agent, time,
  location, and world, in the sense
  [`source/braun-2015-indexicals-sep`](braun-2015-indexicals-sep.md) §3.2 sets out) is an **additional
  step the source does not itself take.** Clark & Chalmers argue about *cognition/belief*, not about
  *occupying a context of utterance* in Kaplan's sense; equating the two is a move the project would have to
  make and defend. This gap must be surfaced honestly wherever the essay's trigger (b) is pressed — an
  extended-mind account making a resource part of *cognition* does not, without further argument, make the
  model the *agent/time/location* of a context in Kaplan's structured sense.

## Status in wanted.md

New ingestion (2026-07-01). Author order (Clark, then Chalmers), year (1998), and venue (*Analysis*)
confirmed from the self-archive header; all body quotes verified verbatim against the self-archive HTML
recorded above, except the "passive / distal and historical" characterization of the Putnam-Burge view,
which is flagged **not verbatim-verified** (adjacent framing only). Open-access via the author self-archive
confirmed. **Page-range discrepancy** (self-archive "58:10-23" vs. standard "58(1):7–19") recorded and
left unresolved pending the journal of record; not a wish-list item, but a metadata note for any downstream
citation.
