# Dative-alternation information-structure probe — DESIGN SPEC (contingent, NOT RUN)

**Status: design draft. No stimuli built, no certification, no model calls, $0
spent.** This directory holds the *design specification* for the probe that opens
the dative line; it is **contingent on**
[`wiki/decisions/open/dative-anchor-and-indicator`](../../../wiki/decisions/open/dative-anchor-and-indicator.md)
and must not be built, certified, or run until that decision is ratified by a later
session's independent adversarial review. Building stimuli here now would freeze a
design around an unratified value-laden choice and force a re-freeze — so this file
is a plan, not an instrument.

## Question

Does the panel's preference between the double-object construction (DOC,
*Mary gave John the book*) and the prepositional dative (PD, *Mary gave the book to
John*) track the **information-structure** constraint humans show — given/old
material before new; pronominal recipients strongly favoring DOC — rather than a
shallow surface cue (theme/recipient length)?

Conjecture: [`conjecture/dative-alternation-information-structure`](../../../wiki/findings/conjectures/dative-alternation-information-structure.md).
Human anchor: [`resource/languageR-dative-corpus`](../../../wiki/base/resources/languageR-dative-corpus.md)
(Bresnan et al. 2007), with Bresnan & Ford (2010) ratings as a candidate convergent
anchor (see the decision).

## Indicator (provisional default — pending ratification)

Logprob-free **graded forced-choice production preference**: a controlled discourse
context establishes which referents are given vs. new (and their pronominality),
then the model is shown the two phrasings of the *same* ditransitive proposition and
distributes 100 points (or rates each on a fixed scale) by naturalness. Surprisal /
continuation-likelihood is **not** available (no panel prompt-logprobs — see
[`decisions/resolved/aann-panel-logprob-blocker`](../../../wiki/decisions/resolved/aann-panel-logprob-blocker.md)),
which is why the indicator is behavioral.

## Stimulus schema (provisional)

Synthetic minimal pairs (not lifted from the corpus → contamination defense), built
to the corpus factor structure:

- **Manipulated:** information status of recipient vs. theme (`given`/`new`,
  crossed with `pronominal`/`nonpronominal` for the recipient).
- **Held constant within a pair:** the verb, the lexical content, **the length of
  recipient and theme**, and animacy — so a within-pair preference shift cannot be
  read off length or animacy.
- **The anti-shortcut control (binding):** a length-matched given/new contrast.
  Because given material is shorter in natural corpora, a model that merely prefers
  *short-before-long* would mimic information-structure sensitivity; the design must
  include matched-length given/new pairs so that the two predictions come apart, and
  the pre-run critic must certify that **no length-only reader** beats chance on the
  information-structure contrast.

## Conditions (sketch, ≥30 items per the conjecture's confirm bar)

1. Recipient given+pronominal / theme new → human surface strongly DOC.
2. Theme given+pronominal / recipient new → human surface shifts toward PD.
3. Length-matched given/new control (the dissociation arm).
4. A neutral baseline (both new, matched length) to locate the model's default.

## Analysis (pre-registered before any run)

- **Primary (corpus-licensed):** within-model preference *shift* across conditions
  1 vs. 2 (and the control arm 3), with length and animacy held constant — does the
  model move toward DOC/PD in the human direction? This is what the corpus anchor
  licenses (it has no per-item rating, only an aggregate production-probability
  surface).
- **Secondary (anchor-dependent):** monotonic correlation between the model's
  per-condition preference and the human signal (corpus-model predicted PP/NP
  probability for that factor configuration; or B&F per-item ratings if that anchor
  is adopted), across ≥30 items, in ≥2 of 3 panel models = **confirm**; preference
  present but not tracking the human gradient = **weak**; preference flips with the
  length confound but not with information structure (control arm) = **falsify**
  (these map the conjecture's own confirm/weak/falsify criteria).
- Verdict scored against an explicitly stated key; the result is **human-anchored**
  (not `internal-contrast-only`).

## Pre-flight budget (estimate only — not authorized until ratification)

~30–60 items × {graded preference} × 3 models, single short structured outputs.
By the panel's measured per-call cost on comparable single-output probes
(~$0.0001–0.0002/call), a ~60-item run is well under $0.25 billed — comfortably
inside the $5/day cap. The build session does the real pre-flight and records the
actual `usage.cost`.

## Build-session checklist (after ratification)

1. Apply the ratified anchor + indicator + control decisions.
2. Mirror + inspect + checksum `languageR::dative` (promote the resource page
   `external-only` → `catalogued`); verify B&F 2010 data if Option B/C adopted.
3. Build synthetic stimuli; freeze; run the certification (no length-only or
   position-only reader beats chance on the information-structure contrast).
4. Independent pre-run critic (GO/NO-GO) → run → independent post-run verifier.
5. Record actual billed cost; write the result page with a human-anchor link.
