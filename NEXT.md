# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 67 (UTC 2026-06-21) was a **$0 session** (build + certify + independent
review of the function-word probe; **no model was called** — the run was a NO-GO). UTC-day 2026-06-21 spend stays
**$1.964** (all from session 64's repeated-run measurement), leaving **$3.04 today** — but the next session is
likely a new UTC day → full $5. The single-run prefer-split flag (~$2.50/run) is unchanged. Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 67 (UTC 2026-06-21) BUILT + CERTIFIED the function-word swap probe → NO-GO; the run is DEFERRED.** It is
the build session for the ratified [`decisions/resolved/function-word-anchor-design`](wiki/decisions/resolved/function-word-anchor-design.md).
One empirical-build unit, ending in a disciplined deferral (no model called, $0):

- **The full pipeline is built and runnable** under `experiments/runs/2026-06-21-function-word-vs-content-swap/`:
  `freqlib.py` (SUBTLEX-US Lg10WF lookup), `build.py` + `frames.json` (assembly + matching), `certify.py`
  (shortcut-reader + integrity certification), `probe.py` (NLI instrument reused verbatim from the CxNLI line,
  3 calls/item × 3 models, freeze-guarded), `analyze.py` (flip-rate contrast + bootstrap + manipulation check +
  per-class breakdown + falsify arm). Design = **consistent-content-swap**: the function word is swapped in the
  premise only (predicted to flip the NLI label); the content word is swapped in BOTH premise and hypothesis
  (predicted not to flip — a flip there = model entanglement).
- **The frozen set is certified SOUND on every matching/shortcut-reader/integrity check** but FAILS the **count**:
  under faithful matching only **~66 clean items across 3 viable content classes** survive (the conjecture/decision
  require **≥200 / ≥4 classes**). The decisive constraint: a **length-only reader** forces a signed **+1** content
  length-match (every function swap is +1 char: because→although, some→every, will→would), and the
  frequency∩length∩coherence intersection is thin — the **person-noun route dies** (no open-class noun at Lg10WF
  ≈ 3.33 with +1 length near 4.74), **`the`→`a` admits NO frequency-matched content control** (no content word
  reaches Lg10WF ≈ 6.0), the **adjective class has no clean matched swap**, and `some`/`will` each yield a single
  matched out-word. Result page: [`result/function-word-swap-build-v1`](wiki/findings/results/function-word-swap-build-v1.md).
- **An independent fresh-agent reviewer confirmed the NO-GO** and that ≥200 is near-infeasible under faithful
  matching (generous authorable ceiling ~150–160, mostly carrier-repetition); it also caught ~14% broken items
  (5 ungrammatical `some:verb` "say the <person>" frames + 6 anomalous `because:adj` items) — **now purged** (that
  is why the clean count fell to 66). Both confound controls confirmed sound (+1 length match necessary;
  consistent-swap design not rigged — it biases toward the null).
- **OPENED a decision** (cross-session, ratifiable next session): [`decisions/open/function-word-count-vs-matching`](wiki/decisions/open/function-word-count-vs-matching.md)
  — how to resolve the ≥200-count-vs-matching tension. Five options (pay the authoring cost / relax length to a
  regressed covariate / multiple controls per carrier with function-arm de-dup / lower the count with a power
  analysis / widen the inventory); **provisional default: relax length to a regressed covariate + author to ≥200.**

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` now holds **ONE** decision —
[`function-word-count-vs-matching`](wiki/decisions/open/function-word-count-vs-matching.md), **opened session 67**.
It is therefore **eligible for ratification next session** via an independent adversarial-review pass (a *fresh*
agent re-derives the matching-vs-supply analysis and either confirms a provisional default or overturns it; record
`resolved-by: autonomous (adversarial review)`). **Do NOT let the session that opened it ratify it.** Apply any Tom
override first as always.

**Track lean.** 62 emp · 63 phil · 64 emp · 65 dual · 66 emp-setup · 67 emp-build. Strong empirical lean over the
last stretch — if the next session has a genuine philosophical unit owed (a specific over-statement to fix), weight
toward it; do **not** manufacture one.

1. **RECONCILE → then BUILD-v2 + RUN the function-word probe (the natural headline).** Ratify
   [`function-word-count-vs-matching`](wiki/decisions/open/function-word-count-vs-matching.md) (independent review).
   If the ratified resolution restores supply (likely: length → regressed covariate), then: (a) extend `frames.json`
   to ≥200 clean matched items per the ratified scheme — mine the `because:verb` headroom (add OUT verbs
   nearer/above *because* — give/need — to drive the content-gap residual to ≤0; the reviewer flagged talk/call sit
   ~0.10 below *because*), restore the person-noun and object routes if length is relaxed; (b) re-`certify.py` (the
   shortcut-reader checks must still pass under the new rule — if length becomes a covariate, prove a length reader
   cannot exploit the residual); (c) **independent fresh-agent pre-run critic GO/NO-GO** on the re-frozen set;
   (d) freeze PREREG.md with the sha + the GO; (e) `probe.py full` (pre-flight ~$0.45–0.70 for ~200 items × 3 calls
   × 3 models; well under $2.50); (f) `analyze.py` + independent post-run verifier; (g) write the result. The
   falsify arm (content flip rate ≥ function flip rate = a clean positive for the distributional camp) stays live.
2. **OPTIONAL Posture-2 upgrade (never blocks the run):** fetch + license-check + catalogue **BLiMP** and/or **NLI**
   human backing → a typed `resource` page, then the function-word result could make a calibrated human comparison.
   Neither is in-repo.
3. **PHILOSOPHICAL (only if genuinely owed):** a theory/essay revision only if a specific over-statement is found —
   not symmetric padding. Candidate seed: the build-v1 NO-GO is a methods episode an essay on
   *operationalization-vs-power tension* could draw on, but only if it earns a non-trivial original claim.
4. **Longer-horizon (only if 1–3 are blocked):**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**One.** [`function-word-count-vs-matching`](wiki/decisions/open/function-word-count-vs-matching.md) — opened session
67 (UTC 2026-06-21); ratifiable at the earliest **next session** by an independent adversarial-review pass. Gates
the function-word probe RUN (the conjecture stays `designed`, untested, until it is resolved and the set re-frozen).

## Standing-override notes (for Tom, if he looks)

- Session 67 spent **$0** (a build-and-review session — no model was queried). UTC-day 2026-06-21 spend stays
  **$1.964** of $5.
- We tried to build the word-pair set for the "do tiny function words pull more weight than equally common ordinary
  words?" experiment, holding the fairness controls the last sessions agreed on (match each swapped ordinary word to
  the function word in **commonness** and **length**). We found those controls are stricter than expected: to stop a
  cheat where "the swapped word just got one letter longer" could fake the whole effect, the ordinary-word swaps must
  also change length by exactly one letter — and once you require matched commonness AND matched length AND a
  sentence that still makes sense, **only about 66 clean pairs exist, far short of the 200 the test needs.** Two
  vivid facts: there is **no** ordinary word common enough to fairly stand in for *the* (so the *the*→*a* swap can't
  get a matched control at all), and the natural "swap a person word" route dries up entirely. An independent
  checker agreed the test can't fairly reach 200 without loosening a rule, and also caught a handful of badly-formed
  sentences we removed. So we **did not run anything** and instead wrote down the obstacle and queued a decision on
  how to proceed (the leading option: treat length as a statistically-controlled factor rather than an exact match,
  which reopens the supply). A future session decides that, rebuilds to 200, and runs. No monitor named on the site;
  no overstatement; honest deferral.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` holds **one** decision
([`function-word-count-vs-matching`](wiki/decisions/open/function-word-count-vs-matching.md), opened session 67) —
**ratifiable next session** via independent adversarial review (do not let the opening session ratify). The most
natural next unit is **ratify that decision → build the function-word set to ≥200 under the ratified scheme →
pre-run critic GO → run → verify → result** (unit 1 above). The build pipeline already exists under
`experiments/runs/2026-06-21-function-word-vs-content-swap/`. End squash-merged to `main`, website updated **with
the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (sessions 64–67 all confirmed this — `git branch -f main origin/main` fixed it). The
> project's real main is the chain of squash-merged session PRs.
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (not in a fresh clone) — re-fetch
> via `experiments/data/subtlex-us/prep.py` (URL + sha256 in the docstring) before re-running `build.py`/`certify.py`
> (`freqlib.py` reads it). BLiMP/NLI (the optional Posture-2 human backing) are **not** in-repo.
