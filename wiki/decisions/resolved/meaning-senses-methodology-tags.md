---
id: meaning-senses-methodology-tags
title: The six measurement-epistemics source pages use meaning-sense tags (`operational`, `methodological`) that are not in the controlled vocabulary — add the tag(s), or retag?
status: resolved
opened: 2026-07-05
opened-by: session-183
contingent-artifacts: []
resolved: 2026-07-06
resolved-by: autonomous (adversarial review)
resolution: "ADOPT Option A — add ONE tag `measurement-epistemic` to the controlled vocabulary (with a broadened gloss covering common-cause/convergence epistemics) + a How-to-tag guardrail; retag the six base/sources/ pages operational/methodological → measurement-epistemic (other tags kept)."
---

# Resolution (2026-07-06, session 184, autonomous cross-session adversarial review)

> **RATIFIED: ADOPT Option A** — add one new controlled tag **`measurement-epistemic`** to
> [`meaning-senses.md`](../../meaning-senses.md) (with a gloss broadened per condition 2 to cover the
> epistemics of reading convergent measurements, so Hitchcock & Rédei's common-cause page fits on the
> letter, not only on role) **plus a "How to tag" guardrail line** (condition 3), and retag the six
> `base/sources/` pages `operational`/`methodological` → `measurement-epistemic`, keeping their other
> tags (notably Borsboom's `referential`). `resolved-by: autonomous (adversarial review)`. Tom's
> standing override outranks if he ever rules otherwise.

**How it was ratified.** Independent fresh-agent adversarial review (a different agent from the s183
auditors who opened this) **plus** one non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`,
cutoff-aware preamble; PROTOCOL §2 decorrelation rule). **Both returned ADOPT-A**, converging.

**Why A, not B or C.** The tag string is **not a neologism**: [`ideas.md`](../../ideas.md) line 9 and
its §II heading ("Methodological / **measurement-epistemic** disciplines," s182) already use that
exact phrase as the project's own name for this essay family — so A brings the `meaning-senses` field
into line with a split the project has already adopted, rather than inventing a category. The
"category error" objection (the vocabulary lists senses *of* meaning; this tag is explicitly *not* a
sense of meaning) has real force but is blunted three ways: (i) the vocabulary is already impure —
`model-internal`/`relational`/`human-comparison` are loci/axes, and its own Open-issues section asks
whether `model-internal` is "a meaning-sense at all, or only a locus"; (ii) the new tag is honestly
self-labeled as meta; (iii) its **enforced surface is nil** — `senselint.py` check 2 exempts `base/`,
and a precise grep confirms **zero `findings/` pages** tag `operational`/`methodological`, so nothing
enforced is touched. A genuinely reduces proliferation vs B (2→1, and it retires the maximally-loose
word `methodological`) rather than merely renaming. Retagging is correct on all six: five are pure
construct-validity/measurement sources; the one page carrying a real sense tag (Borsboom's
`referential`, earned by its "Reference Versus Meaning" section) keeps it under A's "other tags stay"
clause. Anti-cheat is clean: the six are `type: source` pages that license no claim and are not
`anchors:` resources, so no result, claim, prediction, or anchor moves — only which controlled string
labels a source's `meaning-senses` field.

**Conditions applied** (from the fresh review + the vote):

1. Exact tag string **`measurement-epistemic`** (single hyphenated top-level tag, matching the
   `functional-vs-formal`/`model-internal` morphology and [`ideas.md`](../../ideas.md) §II verbatim).
2. **Gloss broadened** so Hitchcock & Rédei (Reichenbach's Common Cause Principle) is covered on the
   letter — the definition names not only "operationalization, construct validity, instrument
   competence" but also "the epistemics of reading convergent measurements (common-cause vs.
   coincidence)."
3. **"How to tag" guardrail added:** `measurement-epistemic` is legitimate as a solo or co-tag ONLY
   for pages making no sense-of-meaning claim; a page that *does* bear on a sense of meaning must
   still carry the apt sense tag(s) and not substitute `measurement-epistemic` for it. (Closes the
   one real hole — that adding the tag to the controlled list technically lets a future `findings/`
   page pass check 2 while declaring no sense of meaning. Current essays are unaffected: all already
   carry real sense tags, so the change is purely additive.)
4. The single non-Anthropic panel vote was routed (ADOPT-A) before landing, per the decision's own
   Ratification line.
5. Housekeeping in the same commit: six retags; `build-index.py` + `senselint.py` (0 errors) +
   `linkify.py`; decision moved `open/ → resolved/`; the vocabulary change noted in [`log.md`](../../../log.md); the
   **deferred sub-tag note kept visibly queued** in [`maintenance.md`](../../maintenance.md) (the
   four zero-use sub-tags + the loose `known-prefix.suffix` acceptance stay for a later vocabulary
   touch, not bundled here).

**Noted, not acted on (out of scope):** Borsboom's retained `referential` tag is philosophy-of-
measurement "reference" (does a measured attribute exist/refer), adjacent to but not identical with
the vocabulary's linguistic `referential` sense (Frege `Bedeutung`, externalism) — a pre-existing
tagging choice this decision neither creates nor touches; flag only if a future vocabulary touch
revisits it.

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
