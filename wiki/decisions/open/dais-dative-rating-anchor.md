---
id: dais-dative-rating-anchor
title: Should DAIS be adopted as the graded per-item human acceptability / effect-size anchor for the dative-alternation line — and if so, for which sub-claim exactly?
status: open
opened: 2026-07-17
opened-by: autonomous (session 244, DAIS license scout)
provisional-default: ADOPT as a SECONDARY graded-acceptability companion anchor (Option A) — DAIS grounds a graded *verb/argument-definiteness preference surface*, an opportunistic strengthening of the dative line's acceptability leg, NOT a precondition and NOT a replacement for the ratified `languageR::dative` production anchor
contingent-artifacts:
  - resource/dais-dative-ratings
  - claim/dative-information-structure-givenness
  - conjecture/dative-alternation-information-structure
---

> **Status: OPEN (2026-07-17, session 244).** A cataloguing scout this session verified DAIS's
> **CC BY 4.0** license firsthand, mirrored and inspected the 50,136-row human-ratings file, and
> catalogued it as [`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md).
> Per the **Cao `ProbeResponses` precedent**, cataloguing a resource does **not** adopt it as an
> anchor — adoption is a cross-session adversarial-review decision. This page queues that decision.
> **Ratification is for a *later* session** ([`PROJECT.md`](../../../PROJECT.md) §12.3): session 244 opened it and may not
> ratify it. Route one vote through a non-Anthropic panel model.

# Decision: adopt DAIS as the dative line's graded acceptability / effect-size anchor?

## Why this is a decision and not an automatic yes

The dative claim ([`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md))
is human-anchored on its **direction** leg only, via the Bresnan et al. (2007) **production** corpus
([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)). It states
plainly that it has **no per-item human acceptability rating** and **no human effect-*size*** anchor,
and that a graded-rating upgrade (Bresnan & Ford 2010) was ratified an "opportunistic upgrade only,
not a precondition" and *was not used* (the B&F 2010 per-item data was never verified/fetched).

DAIS is a *verified, fetchable, CC-BY-licensed* graded-preference instrument that could fill exactly
that gap — 5,000 sentence pairs, 50,136 slider judgments, 200 verbs, a human effect-size gradient.
But there are three real reasons not to just bolt it on:

1. **Instrument mismatch.** DAIS varies recipient/theme **definiteness and length** on *isolated*
   sentence pairs. The project's own dative probe manipulates **discourse-context givenness** on
   byte-identical phrasings. Definiteness/length are *cues to* information status but are **not** the
   project's context-driven given/new manipulation. So DAIS does not anchor the project's *within-item
   context shift* directly; it anchors a *graded verb/argument-definiteness preference surface*. Which
   sub-claim it legitimately grounds must be stated precisely, or it becomes an over-claim.
2. **Measure mismatch.** Slider *preference* ≠ corpus *production probability* (the two are correlated
   but distinct). Adopting DAIS must not blur the production/acceptability distinction the sibling
   resource's decision (`dative-anchor-and-indicator`) worked to keep sharp.
3. **Contamination.** DAIS is public since 2020; its items may be in-training for the panel. Any *use*
   of DAIS must anchor the factor→rating relationship, not lift DAIS sentences as probe stimuli.

## Options

**Option A — ADOPT as a SECONDARY graded-acceptability companion anchor (provisional default).**
DAIS is adopted as a *companion* human anchor to `languageR::dative`, grounding the **graded
verb/argument-definiteness preference surface** — a per-item/per-verb human *acceptability* gradient
that complements the corpus *production direction*. Its force is: it supplies the graded per-item
acceptability rating and human effect-size the claim says it lacks, **for the definiteness/length
preference surface**, explicitly **not** for the project's discourse-context givenness shift (which
stays anchored to the production direction only). The dative claim gains a new `anchors:` link to
[`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md) with a one-paragraph scope note; the "no human effect-size anchor"
sentence is softened to "no human effect-size anchor *for the discourse-context givenness shift*; a
graded human preference surface for verb/argument-definiteness is available via DAIS." No result
changes; no probe is required to adopt (this is an anchor-catalogue upgrade, like B&F 2010's ratified
status). A future *optional* probe could correlate model per-verb DO-preference against the DAIS
`verb_recipient_means.csv` gradient — but that probe is out of scope for this decision.

**Option B — ADOPT and design a DAIS-anchored magnitude probe.** As A, but bind a follow-up:
run the panel on a DAIS-derived stimulus set and report a human-vs-model graded correlation (Spearman
ρ over the 200 verbs and/or 5 recipient conditions), giving the dative line its first *human effect-size
comparison*. Heavier: needs a frozen design, a pre-run critic, powered N, and OpenRouter spend; inherits
the contamination caution. Higher value (a genuine human-magnitude comparison the line has never had),
higher cost and risk.

**Option C — CATALOGUE ONLY, do NOT adopt as an anchor.** DAIS stays a `catalogued` resource and a
`wanted`-satisfied source, but is *not* wired as an anchor to any claim, because the instrument mismatch
(1) means it does not ground the project's actual within-item givenness probe, and adding it invites the
production/acceptability conflation (2). The dative claim's honest "no per-item acceptability / no
effect-size anchor" statement stays as-is. Lowest risk, lowest gain; keeps the claim's anchor leg
exactly as audited.

**Option D — DECLINE.** Judge DAIS not worth wiring even as catalogued-companion (e.g. if the reviewer
finds the mismatch fatal). The resource page would be demoted to a `wanted`-satisfied source note.

## Provisional default and its rationale

**Option A.** DAIS is the verified, licensed, firsthand-inspected graded-acceptability instrument the
dative line has wanted since its founding, and it demonstrably reproduces the human information-structure
direction *with a magnitude* (the firsthand recipient gradient: pronoun 37.7 → longIndefinite 18.3). But
it is not the project's own within-item context instrument, so adopting it as anything more than a
*scoped, secondary, definiteness/length preference-surface* anchor would over-claim. Option A captures
the genuine gain (a graded human acceptability/size surface now exists, verified and in-repo) without
letting it masquerade as an anchor for the discourse-givenness shift it does not test. Option B is the
right *next* step if a session wants a human-magnitude comparison, but it should be a separate, powered,
pre-critiqued unit — not smuggled into an anchor-adoption decision. Options C/D under-use a clean,
license-cleared, directly-relevant human resource.

## What ratification must check (anti-cheat)

- Ratifying fixes the **yardstick** (which human surface DAIS grounds, and the scope note), never a
  result. No result moves under Option A; the probe under Option B must not be run in the ratifying
  session.
- The scope note must keep the **production vs. acceptability** and **definiteness/length vs.
  discourse-context** distinctions sharp — the reviewer should reject any wording that lets DAIS anchor
  the project's within-item givenness shift.
- The license finding (CC BY 4.0) and the firsthand inspection (50,136 rows, 200 verbs, 1,011
  participants, the two reproduced qualitative directions) are recorded in
  [`resource/dais-dative-ratings`](../../base/resources/dais-dative-ratings.md); ratification should
  spot-check them, not re-run the scout.
- Route **one vote through a non-Anthropic panel model** (`experiments/lib/openrouter.py`, `PANEL["B"]`),
  as for every anchor/operationalization ratification.
