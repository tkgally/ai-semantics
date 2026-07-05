---
id: meaning-senses-methodology-tags
title: The six measurement-epistemics source pages use meaning-sense tags (`operational`, `methodological`) that are not in the controlled vocabulary — add the tag(s), or retag?
status: open
opened: 2026-07-05
opened-by: session-183
contingent-artifacts: []
---

# Decision: undeclared meaning-sense tags on the methodology sources

## Why this is owed (surfaced by the s183 wiki-coherence audit)

[`meaning-senses.md`](../../meaning-senses.md) is the controlled vocabulary, and it instructs:
"If the sense you mean is not in this list, propose an addition in `decisions/open/` rather than
inventing a tag inline." Six `base/sources/` pages nonetheless carry tags the vocabulary does not
declare — `operational` on the five measurement-epistemics ingests (Cronbach & Meehl, Messick,
Campbell & Fiske, Borsboom, Freiesleben) and `methodological` on Hitchcock & Rédei. senselint
only enforces the vocabulary on `findings/` pages, so this passed silently. (The audit also
noted, for the same vocabulary page at a future touch: four documented sub-tags —
`referential.reference`, `referential.externalist`, `grounded.causal`, `grounded.social` — have
zero uses, and senselint accepts any `known-prefix.suffix` string, so sub-tag control is loose.
That observation is recorded in [`maintenance.md`](../../maintenance.md), not decided here.)

The pages are not mis-tagged in spirit: they are sources about **measurement itself** (construct
validity, operationalization), which no current tag covers — the vocabulary describes senses of
*meaning*, and these sources ground the project's *measurement-epistemic* discipline (ideas.md
cluster §II). The question is how to make the letter match the spirit.

## Options

- **A (provisional default).** Add **one** tag to the controlled vocabulary:
  `measurement-epistemic` — "about the measurement of meaning rather than a sense of meaning:
  operationalization, construct validity, instrument competence. Used chiefly on `base/sources/`
  methodology ingests and methodological essays that need no meaning-sense claim." Retag the six
  pages `operational`/`methodological` → `measurement-epistemic` (a mechanical rename; the pages'
  other tags stay). One new tag, no proliferation, and the essays of ideas-cluster §II gain a
  legitimate co-tag where apt.
- **B.** Add both existing strings (`operational`, `methodological`) to the vocabulary as-is.
  Zero retagging, but two near-synonymous tags enter the controlled list, and "methodological"
  invites loose future use.
- **C.** Retag the six pages using only existing vocabulary (e.g. drop the tags entirely — tags
  are optional in `base/`). Cheapest, but loses real information the tags carry (these six pages
  *are* a distinct kind).

## Provisional default

**A** — one purpose-built tag, six mechanical retags, vocabulary page updated in the same
commit. Until ratified, the six pages keep their current tags (harmless: `base/` is outside
senselint's vocabulary enforcement).

## Ratification

Cross-session, per [`PROJECT.md`](../../../PROJECT.md) §12.3: eligible from session 184 —
independent adversarial review + one non-Anthropic panel vote; Tom's standing override outranks.
