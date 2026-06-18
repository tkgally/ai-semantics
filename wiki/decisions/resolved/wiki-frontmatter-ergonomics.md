---
id: wiki-frontmatter-ergonomics
title: Should the wiki add per-page frontmatter summaries/keywords (and a leaner index) to make cold-start triage cheaper — and if so, how minimal?
status: resolved
opened: 2026-06-18
opened-by: Tom (interactive request)
contingent-artifacts: []
resolved: 2026-06-18
resolved-by: autonomous (adversarial review)
resolution: ADOPT Option D (trim the always-loaded index; move the resolved-decisions changelog to a history page; no per-page summary/keyword headers)
---

# Resolution (2026-06-18, autonomous adversarial review, cross-session)

> **RATIFIED: ADOPT Option D** — trim the always-loaded [`index.md`](../../index.md) (move the resolved-decisions
> changelog out to [`index.md`](../../index.md), this directory's history page); **do not** add per-page
> `summary:`/`keywords:` headers (Option A's header half and Option B are rejected).
> `resolved-by: autonomous (adversarial review)`. Opened 2026-06-18 out-of-band at Tom's interactive
> request; ratified the next autonomous session (cross-session boundary held). Tom's standing override
> outranks this if he ever rules otherwise.

**Why Option D and not the provisional default (Option A).** An independent adversarial-review agent
re-derived the cold-start cost from the repo and found **two premises of the opening analysis below
are factually wrong as of 2026-06-18**, and both undercut specifically the *per-page-header* half of
Option A:

1. **The resolved-decisions changelog is NOT "most of the ~207 KB" of the index.** Measured: the
   `### Resolved decisions` changelog was **~22.7 KB (~11%)** of [`index.md`](../../index.md); the **per-page Pages
   catalog (~181 KB, ~87%)** is the real bulk. So moving the changelog out (the Option-D / Option-A
   move 1) is still net-positive — the changelog is the most-prunable block and is never needed on the
   main triage path — but it captures ~11% of the file, not "most." Adopt D for the honest reason.
2. **`wiki/decisions/*` are NOT frontmatter-bare today.** Every page under `wiki/decisions/` already
   begins with `---`. The genuinely bare pages are meta/catalog files ([`meaning-senses.md`](../../meaning-senses.md),
   [`base/wanted.md`](../../base/wanted.md), [`executive-summary.md`](../../executive-summary.md), [`base/resources/index.md`](../../base/resources/index.md), the scouting note, [`index.md`](../../index.md)
   itself) — exactly the pages where a `summary:`/`keywords:` header earns least and still adds the
   "third copy / drift" maintenance tax [`CLAUDE.md`](../../../CLAUDE.md)'s never-silent-drift rule warns against. So
   Option A move 2 was aimed at a **mis-identified** set; its residual benefit is negligible. Cut it.

**What was implemented this session:** the changelog was relocated to
[`decisions/resolved/index.md`](index.md); `index.md` keeps a count, the governance note, and a
one-line pointer (plus the single most-recent-decision line). **No** per-page headers were added; **no**
new `senselint` field-check was added (senselint already warns-not-errors on missing frontmatter
outside `findings/`, so Option D needs none). The convention change is logged in
[`log.md`](../../../log.md). **Anti-cheat:** `contingent-artifacts: []` is accurate — no research
result is tilted; this fixes only a navigation convention. The "yardstick, never the result" rule is
satisfied vacuously (no result rides on it).

**Note on the analysis below:** the original opening analysis is preserved verbatim for the record;
its two factual errors (the "most of the ~207 KB" claim in §"The costs to weigh" point 3, and the
"`wiki/decisions/*` … no frontmatter" claim in point 2) are **corrected above** and should be read in
light of this resolution.

---

# Decision: wiki frontmatter / cold-start-triage ergonomics

> **Opened 2026-06-18 at Tom's explicit request, to be handled in a future working session.**
> This is a **conventions/ergonomics** decision — it changes how the wiki is *navigated* at cold
> start, not what any finding claims. It is **not** a research finding and **not** an
> operationalization or human-anchor gate, so it carries no anchor obligation and no result page is
> contingent on it (`contingent-artifacts: []`). Per the cross-session rule ([`PROJECT.md`](../../../PROJECT.md) §12.3) it
> may be ratified **only in a later session** than this one — by an independent adversarial-review
> pass, or by Tom's standing override. Do **not** ratify it in the session that reads this if that
> is still 2026-06-18's opening session; a normal later autonomous session is eligible.

## The question

Two parts. **(a)** Should the project change its wiki conventions to make the start-of-session
warm-up cheaper and more effective — specifically, would adding YAML frontmatter (a one-line
*summary* and *keywords*) to the start of every page help the agent decide whether to load a page
into context *without* first paying to read the whole page? **(b)** If something is worth doing,
**how minimal** should it be?

**Scope note (important):** interoperability is explicitly **not** a goal. Tom has confirmed the
project is not shared with other models or systems, so the separate question of conforming to an
external standard (e.g. Google's Open Knowledge Format) is **out of scope here** — this decision is
purely about *this project's own* cold-start ergonomics.

## Why this exists (surfaced, not auto-resolved)

Tom asked (2026-06-18) whether per-page summary+keywords frontmatter would make the every-few-hours
cold-start more effective, given that the project runs as a fresh session each time with all
continuity in the repo ([`PROTOCOL.md`](../../../PROTOCOL.md) §1). The analysis below was worked out in that conversation
and is recorded here so a future session can ratify or reject it without re-deriving it.

### Where the load decision actually happens

The cold-start path is [`NEXT.md`](../../../NEXT.md) → [`wiki/index.md`](../../index.md) → list `decisions/open/` → **then selectively
load only the pages the next action needs** ([`PROTOCOL.md`](../../../PROTOCOL.md) §1). The "should I load this page?"
decision is therefore made at [`index.md`](../../index.md), which already carries a one-line gloss per page. By the
time the agent reads a page's *own* frontmatter, it has already paid the tokens to load that page —
so a frontmatter summary arrives **too late on the main path** and is largely **redundant** with the
index gloss that was already used to decide. Findings / base / design pages additionally already
carry a sentence-form `title:` (often a complete summary) and `meaning-senses:` (keyword-like tags),
so most of the "summary + keywords" value already exists where it matters most.

### Where a per-page header *would* help

The genuine benefit is on the **fallback** paths, not the main one:

1. **Glob/grep discovery** of pages not reached through the index.
2. **Bulk topic triage** by grepping a `keywords:`/`summary:` field across `wiki/**` to assemble an
   ad-hoc, subject-specific mini-index.
3. **Cheap peeking** — `Read` with a small line `limit` to grab just the top-of-file header instead
   of loading a 200–300-line page, so the agent triages *which* full pages to load while paying
   ~10 lines apiece.

### The costs to weigh

1. **Drift.** A per-page summary is a *third* copy of each page's gist (body + index gloss +
   frontmatter summary) that can fall out of sync. `senselint` can enforce *presence* but not
   *faithfulness*, and the project's core discipline is "never silent drift" ([`CLAUDE.md`](../../../CLAUDE.md)). A stale
   summary is worse than none, because the agent will trust it.
2. **The gap is small.** The pages with **no frontmatter at all** today are only:
   `wiki/decisions/*`, [`wiki/meaning-senses.md`](../../meaning-senses.md), [`wiki/base/wanted.md`](../../base/wanted.md), [`wiki/executive-summary.md`](../../executive-summary.md).
   All four are already glossed in [`index.md`](../../index.md), so even they are not invisible at cold start.
3. **The triage surface itself has grown heavy.** [`wiki/index.md`](../../index.md) measured **299 lines / ~207 KB
   (~81k tokens when read 2026-06-18)**, most of it the ever-growing *resolved-decisions changelog*
   of paragraph-length bullets. [`index.md`](../../index.md) is the one file loaded on **every** cold start, so
   trimming it likely speeds up every session more than per-page summaries would.

## The options

### Option A (provisional default) — lean index + minimal headers on the bare pages only

Three coordinated moves:

1. **Lean the index.** Keep [`wiki/index.md`](../../index.md) as the single triage surface but curate it: a
   current-state dashboard + a tight typed-page catalog at the top; move the verbose
   *resolved-decisions changelog* (the paragraph-length per-decision bullets, now the bulk of the
   ~207 KB) into a dedicated history page (e.g. [`wiki/decisions/resolved/index.md`](index.md)), leaving
   one-line pointers in the main index.
2. **Minimal headers on the four bare page classes.** Add a sentence-form `title:` and a short
   `keywords:` list to the pages that currently have *no* frontmatter (`wiki/decisions/*`,
   [`wiki/meaning-senses.md`](../../meaning-senses.md), [`wiki/base/wanted.md`](../../base/wanted.md), [`wiki/executive-summary.md`](../../executive-summary.md)). Leave
   findings/base/design pages unchanged — their `title:` + `meaning-senses:` already serve as
   summary + keywords.
3. **One workflow line.** Add a note to [`CLAUDE.md`](../../../CLAUDE.md) / [`PROTOCOL.md`](../../../PROTOCOL.md) §1 that a session may
   frontmatter-peek (`Read` with a small line limit) or grep `keywords:` across `wiki/**` when the
   index gloss does not settle whether to load a page.

Rationale: best ratio of triage benefit to drift risk — it concentrates effort on the one
always-loaded file and the only pages lacking any header, and reuses the title/meaning-senses that
findings pages already carry.

### Option B — blanket `summary:` + `keywords:` on all pages

Every wiki page (~100) gains a one-sentence `summary:` and a `keywords:` list; `senselint` gains a
presence check. Maximally uniform peek/grep surface. Weighed against: redundant on the main load
path (the load decision precedes seeing a page's own frontmatter); introduces a third, drift-prone
copy of each page's gist; `senselint` can verify presence but not faithfulness; a standing
per-session maintenance tax. Most of its marginal value over A falls on pages that already carry a
sentence-form `title:`.

### Option C — status quo (do nothing)

[`index.md`](../../index.md) + `title:` + `meaning-senses:` + [`executive-summary.md`](../../executive-summary.md) already make cold-start
tractable; the cost of any change (a [`CLAUDE.md`](../../../CLAUDE.md) convention edit, a `senselint` extension, per-page
edits, and the standing drift risk) is not worth a marginal triage gain. The honest null option — to
be chosen if the reviewing session judges the current cold-start already cheap enough.

### Option D (partial, foldable into A) — trim the index only

Do move 1 of Option A (lean the index / split out the resolved-decisions changelog) and nothing
else: no new per-page fields, no new drift surface, while capturing most of the measured cost (the
~207 KB always-loaded file). A reviewing session that rejects per-page headers (B) but judges full
status-quo (C) too passive can adopt D as the minimal high-value core of A.

## Provisional default and contingency

**Default taken: Option A**, with **Option D** explicitly available as the "A minus the per-page
headers" fallback if the reviewing session wants the index win without the header tax. Nothing in the
repo is changed by *opening* this decision; no finding is contingent on it (`contingent-artifacts:
[]`), so no page needs provisional language on its account.

## What ratification fixes (and what it does not)

Ratifying this fixes a **navigation convention** — how the wiki is read and triaged at cold start. It
**never** changes what any finding claims, and it creates no human-comparison or operationalization
commitment. If A or D is adopted, the change is a [`CLAUDE.md`](../../../CLAUDE.md) convention edit and must be **logged in
[`log.md`](../../../log.md)** in the same commit ([`CLAUDE.md`](../../../CLAUDE.md) "When to update this file"); any new `senselint` check for
a `keywords:`/`summary:` field should be kept at **WARN, not ERROR**, to avoid build churn while the
convention beds in.

## Anti-cheat / discipline note

The usual operationalization anti-cheat ("never retune an indicator after seeing results") does not
bind here — no result rides on this decision. The relevant risks are (1) **drift** (Option B's
three-copies hazard) and (2) **scope creep** (a "tidy the wiki" task quietly expanding). A reviewing
session should resist both: prefer the smallest change that demonstrably lowers cold-start cost, and
treat any per-page summary as an artifact that must be kept faithful or removed, never left to rot.

## Recommended resolution

Adopt **Option A** (lean index + minimal headers on the four bare page classes + one workflow line),
treating the index-trim (Option D) as the load-bearing part and the per-page headers as the cheap
secondary aid — or fall back to **Option D alone** if the reviewer judges the per-page headers not
worth their maintenance. Log the convention change in [`log.md`](../../../log.md); keep any new `senselint` field-check
at WARN.
