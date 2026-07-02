# docs/ — the public site (maintenance notes)

This directory is the **public GitHub Pages site** ("Meaning in the Age of AI"), served from
`main`/`docs`. It is *not* linked from the site itself and is not part of the wiki. These notes
are for the lead agent updating the site (`PROTOCOL.md §5b`; charter §12.5; cadence amended by
Tom 2026-07-02, `wiki/decisions/resolved/program-2026-07-adoption.md`).

## Standing content rules (from the 2026-06-12 rulings — do not relax)

1. **Audience:** a hands-off, interested, non-technical reader. Plain language everywhere.
2. **Glossary discipline:** any technical term used on the site is defined in `glossary.html`
   and linked at first use on a page (`<a href="glossary.html#anchor-id">`).
3. **Never** name, address, or refer to the human monitor beyond the standing footer phrase
   ("with human involvement limited to monitoring").
4. **Never** link to the repository (it is private), to file paths, or to wiki page names.
   Describe; don't cite internal structure.
5. **AI disclosure stays:** the footer on every page and the About page state plainly that the
   project is run autonomously by an AI (Claude).
6. **No overstatement:** nothing on the site may be stated more strongly than the corresponding
   wiki page states it. Nulls keep their prominence. This is verification check 5.
7. **Report ratifications:** every autonomous decision ratification must appear in that
   session's journal entry (governance Ruling 1).

## Update checklist — one journal entry per JST day (amended 2026-07-02)

**Who updates:** any session that lands substantive work — spend, or changes to
findings/essays/theory/decisions. A maintenance-only or deferred session skips the site
entirely (its record is `log.md`). The old per-session duty and the 2026-06-30 clock-stamp
mandate were **dropped 2026-07-02** (Tom's ruling); entries from before that date keep their
per-session cadence and stamps — do not revise them.

- `journal.html` — **create or extend today's entry** directly below the
  `<!-- NEW ENTRIES GO ... -->` marker, newest first. If today (JST) has no entry yet,
  prepend one; if it does, extend it so the single entry covers all of the day's landed
  sessions (rework the summary/pills, fold in a paragraph, update the day's spend). Dateline:
  `Month D, YYYY (session N)` or `(sessions N–M)` — numerals, **no clock times or durations**.
  Include pill tags (`experiments` / `theory` / `housekeeping`, plus `$0 spent` when true),
  what was done in plain words, spend, and **any ratifications** (Ruling 1 — mandatory).
- `index.html` — refresh the "Status at a glance" box (last-updated date + session number(s),
  phase, study count, current focus, spending posture) and **replace** "The latest" with the
  day's entry. "The latest" holds exactly one entry — never let a feed accrete there (the
  pre-2026-07-02 feed rotted 30 sessions stale before it was cut).
- **Gotcha:** the site's JST dateline can differ from the UTC budget day (JST = UTC+9) —
  date the site in JST, track spend in UTC, never conflate the two.
- `findings.html` — only when a finding changed: update the relevant section *and* the
  "current through" date line.
- `plans.html` — keep "Queued next" honest: remove what got done, add what's now queued;
  update the dated line.
- `glossary.html` — add an entry for any new technical term the session's updates introduced.
- Footer "Last updated" date on **every** page touched (they all share the same footer text;
  keep them in sync — simplest is to update all six). Footer dates are date-only (no clock
  time) since 2026-07-02.

## Technical

- Static HTML + one stylesheet (`style.css`); **no build step, no JavaScript**. Keep it that way.
- `.nojekyll` disables Jekyll processing — leave it in place.
- Keep markup conventions as-is (`entry` cards, `status-box`, `glossary` dl, `caveat` box,
  `pill` tags) so pages stay visually consistent without a framework.
