# NEXT.md

## State

**Session 50 (2026-06-20 UTC) ratified the dative-alternation operationalization (ADOPT MODIFIED) and BUILT + FROZE + CERTIFIED
the probe instrument under an independent pre-run critic GO; $0 spent, no models queried. The run is the next step.**
The English DATIVE ALTERNATION line (double-object *Mary gave John the book* vs. prepositional *Mary gave the book to John*,
constrained by information structure) — the project's return to its grammatical core — is now ready to run:

- **Decision ratified (cross-session):** [`decisions/resolved/dative-anchor-and-indicator`](wiki/decisions/resolved/dative-anchor-and-indicator.md)
  — opened by session 49, ratified by session 50 via an independent adversarial-review agent: **ADOPT MODIFIED** (Option A corpus
  production surface = primary anchor; B&F 2010 ratings an opportunistic upgrade only; graded forced-choice indicator; synthetic
  minimal pairs; human-anchored posture) with **four modifications** (confirm-wording fix; binding primary/secondary analysis
  ordering; numeric length-control thresholds; forced-choice validity guard) + **seven binding build conditions**.
- **Anchor promoted:** [`resource/languageR-dative-corpus`](wiki/base/resources/languageR-dative-corpus.md) `external-only`→**`catalogued`**
  — corpus mirrored + inspected firsthand (3263×15; NP=2414/PP=849; factor levels confirmed; logistic fit reproduces all five
  canonical human directions, acc 0.887). Derived gradient committed (`corpus_inspection.json`); raw `.rda` gitignored.
- **Instrument BUILT + FROZEN + CERTIFIED:** [`experiments/runs/2026-06-20-dative-information-structure/`](experiments/runs/2026-06-20-dative-information-structure/)
  — `stimuli.json` **sha256 `0ffe3700524a8e5e0780820bab2fa4301923d37d93f7683d69515c968c4ababf`** (44 items = 32 main + 12 control;
  240 trials). The givenness manipulation lives ONLY in the discourse context, so the within-item shift is **provably immune to
  every length/position/order shortcut** (`certification.json`: all 8 enumerated shortcut readers → max|shift|=0; all binding
  conditions PASS). `PREREG.md` freezes the sha + the pre-registered analysis + verdict map + the **independent pre-run critic GO**.
- **JST site-stamp hardened (monitor request):** the requirement to stamp the journal entry + home-page "Last updated" with the
  Japan-time clock time is now in `PROTOCOL.md §5b` (with the `TZ=Asia/Tokyo` recipe + the UTC-vs-JST budget-day gotcha) and
  `CLAUDE.md` rule 9, plus a cautionary note in `docs/README.md` (sessions 48–49 had dropped it). This session's site entries
  carry `12:36 JST`.

senselint **0 errors** (expected residue: wanted.md + multimodal-anchor-scouting WARNs); linkify clean.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** (the dative decision was ratified this session; nothing else
open). Nothing to ratify. Apply any Tom override first.

**Track lean:** sessions 49 (build-open) + 50 (ratify + build) were empirical/governance; the natural next step is the EMPIRICAL run.

1. **EMPIRICAL — RUN the frozen dative probe (the headline).** The instrument is frozen + certified + pre-run-critic-GO'd this
   session (GO recorded in `PREREG.md`; sha pinned). Procedure (all in `experiments/runs/2026-06-20-dative-information-structure/`):
   `python3 probe.py liveness` (3 calls, all must parse the graded `FINAL:` line) → `python3 probe.py full` (refuses unless the
   PREREG sha matches; 720 calls; **hard stop $1.50**; crash-safe resume; gemini `effort: minimal`) → `python3 analyze.py`
   (primary within-model shift + control arm + neutral baseline + non-decisive secondary corpus-gradient Spearman) → **independent
   post-run verifier** reproduces every number from raw → write the **result page** (human-anchored, `anchors:`
   `resource/languageR-dative-corpus`; NOT internal-contrast-only) → update `conjecture/dative-alternation-information-structure`
   (proposed→tested) + `theory/constructional-meaning-in-llms` + budget row + website + handoff. **Pre-flight ~$0.7–1.1 billed**
   (claude's working-surface output dominates; check today's `config/budget.md` UTC rows first). The pre-run critic GO is on the
   byte-identical sha; the run may proceed directly (a fresh quick re-confirmation is optional, not required). **Do NOT re-tune the
   indicator or stimuli after seeing outputs** — a failed primary test is a falsification, recorded as such.
2. **PHILOSOPHICAL (if a run is deferred / budget tight):** a warranted essay/conjecture or open-access `wanted.md` catalogue —
   only if a finding will lean on it. Composition-essay space is saturated.
3. **Website** per `PROTOCOL.md §5b`, as always — **with the JST clock-time stamp** (now mandatory in §5b + CLAUDE.md rule 9).

## Open decisions

- **None.** `wiki/decisions/open/` is empty. (The dative operationalization, opened 2026-06-20 by session 49, was ratified
  2026-06-20 by session 50 — [`decisions/resolved/dative-anchor-and-indicator`](wiki/decisions/resolved/dative-anchor-and-indicator.md).)

## Standing-override notes (for Tom, if he looks)

- The "grammar of giving" test is now **approved, built, and stress-tested** — an independent review approved the design and
  tightened it (hard numbers for the "shorter-thing-first" trap; the human-data comparison demoted to a supporting check); the test
  was built so that no shallow shortcut can fake the effect (a second independent reviewer tried ten and broke none, then gave a
  green light). Only the small, cheap run remains. Nothing has been queried or spent.
- The site-following tweak you asked for — showing the **Japan-time clock time** after the date on each new entry — is now written
  into the always-read run rules (not just the site's maintenance notes), so future sessions shouldn't drop it again. This
  session's entries show `12:36 JST`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget **$5/day UTC** — check
[`config/budget.md`](config/budget.md) (2026-06-20 UTC day total = **$0**; this session spent $0). End squash-merged to `main`,
website updated **with the JST clock-time stamp**. **No decisions open.** The headline next step is the **dative probe RUN** —
frozen + certified + pre-run-critic-GO'd (`stimuli.json` sha `0ffe3700…ababf`); run it, verify independently, write the
human-anchored result, and never re-tune after seeing outputs.
