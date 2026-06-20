# Dative-alternation information-structure probe — ACTIVE BUILD SPEC (ratified)

**Status: operationalization RATIFIED 2026-06-20 (session 50, ADOPT MODIFIED) —
[`decisions/resolved/dative-anchor-and-indicator`](../../../wiki/decisions/resolved/dative-anchor-and-indicator.md).**
This is now the **active build spec**, no longer contingent. The binding
build-session conditions from the ratification are folded in below (see "Binding
conditions (ratified)"). Stimuli construction, freezing, and certification proceed
under those conditions; the run is gated by an independent pre-run critic's GO/NO-GO.

## Binding conditions (ratified 2026-06-20 — all must hold before any spend)

- **(a) Within-pair length variance = 0** — recipient and theme word-lengths are
  identical across the two phrasings (DOC vs PD) compared within a pair.
- **(b) Length-matched given/new control arm of ≥12 pairs**, of which **≥6** are
  cases where information structure predicts the *longer* constituent first — so the
  *short-before-long* and *given-before-new* predictions come apart (opposite
  orderings).
- **(c)** Across the full set, recipient/theme length distributions do **not** differ
  between given-condition and new-condition items (report it; exact matching or a
  non-significant difference).
- **(d) ≥30** controlled minimal-pair items for the main contrast, plus the control
  arm (b), plus a **neutral both-new baseline**.
- **(e) Analysis ordering is binding:** the corpus-licensed **within-model preference
  shift** is the sole confirm/weak/falsify-bearing **primary** test; the
  human-gradient correlation is **secondary** and may strengthen a confirm or
  characterize a weak result but may never convert weak→confirm nor rescue a failed
  primary test.
- **(f) Falsify arm is live** — a flip with the length confound but not with
  information structure (the control arm) is a falsification, recorded as such, with
  no retuning; a pre-run-critic NO-GO defers the run, never relaxes the control.
- **(g) Resource-promotion gate** — `languageR::dative` is mirrored + row-inspected
  (3263×15, factor levels confirmed firsthand) + promoted `external-only`→`catalogued`
  before the corpus-gradient secondary analysis may cite it; the predicted-probability
  surface is computed from inspected data (or Bresnan et al.'s reported model), not
  asserted.
- **Validity guard:** the discourse context establishing givenness must be
  load-bearing — the *same* two phrasings must flip preference *only* because the
  context changed; report the neutral both-new baseline so a context-insensitive
  shallow preference is detectable.
- **Pre-run certification:** an independent pre-run critic certifies, against the
  frozen stimuli, that **no length-only and no position-only reader beats chance** on
  the information-structure contrast — GO/NO-GO before any spend.

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
