# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s226 spent $1.189992** (the resumed gemini $0.969858 + gpt $0.220134 arms of the particle-placement panel;
claude $1.387896 + liveness $0.003258 were billed s225). Day total UTC **2026-07-14** (s224 $0.003934 + s225
$1.394751 + s226 $1.189992) = **$2.588677 of $5.00** (~**$2.41** headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s226 ran on **JST 2026-07-14** — the **SAME JST website day as s221–225** (the July 14
entry is now s221–226; the July 13 entry stays s215–220).
**s227: recompute the JST date from `date -u`; confirm the UTC budget day and whether the JST website day
has rolled** (s227 will very likely be a NEW UTC day 2026-07-15 → full $5 headroom, and a NEW JST website day).

## State — s226 ($1.189992): PARTICLE-PLACEMENT HALTED RUN **COMPLETED** → **PANEL CONFIRM** (2/3 firewall; gpt SHADOW). Result written, verifier-REPRODUCED, `proposed`.

The owed successor from s225 — **complete the halted particle-placement run** (a resumed split, not a
re-freeze of measurement). Done:

- **BUDGET-ONLY CORRECTION.** Raised `common.HARD_STOP_USD` **$1.30→$3.50** in the run dir
  ([`experiments/runs/2026-07-14-particle-placement-givenness/common.py`](experiments/runs/2026-07-14-particle-placement-givenness/common.py)).
  Frozen shas re-verified **UNCHANGED** before the edit (`stimuli.json` `0b63e252…`, `freq_control.json`
  `cd472475…`); `analyze.py`/verdict rule untouched; claude's shifts **not inspected** during the halt
  (resume stayed blind / anti-cheat-clean). Documented: PREREG addendum (s226) + [`config/budget.md`](config/budget.md) + here.
- **RUN COMPLETED.** `probe.py full` crash-safe resume finished gemini (560/560) + gpt (560/560), skipping
  claude's done tids — 1,120 calls, **0 NA / 0 length-trunc / 1 gemini retry (recovered)**. Full panel 1,680
  calls, $2.5811 total (s226 marginal $1.190).
- **ANALYZED + VERIFIED.** `analyze.py` → **PANEL CONFIRM**. The byte-identical discourse-givenness firewall
  (GIVEN−NEW-MENTIONED, the decisive leg) clears bootstrap 95% LB > 0 in **2/3** (claude +0.040 [0.022,0.059],
  gemini +0.072 [0.049,0.095]); the definiteness arm is directionally consistent 3/3 (0 reversals); the
  convergent length leg holds 3/3 (+0.29–0.40). **gpt = the pre-named SHADOW** (definite→split +0.100 but
  firewall +0.018, CI [−0.017,0.055], 18/40) — its determiner effect is a surface/lexical shadow, gpt weakest
  again (dative/genitive pattern). **Post-run fresh-agent verifier → REPRODUCED** (0 material discrepancies;
  independent script + seed 424242; both shas verified; every point estimate 4-dp exact; total cost reproduced).
- **RESULT WRITTEN.** [`result/particle-placement-givenness-v1`](wiki/findings/results/particle-placement-givenness-v1.md)
  (`proposed`, `human-anchored`) honoring **R1–R7**: CONFIRM framed **narrowly directional** (R1, not "shadow
  defeated"); the referential firewall effect **small** vs the strongly-tracked end-weight constraint;
  covariate **near-vacuous** (R² ≤0.02) so CONFIRM **rests on the firewall**; **firewall-borne** scoped away
  from the determiner effect (R4, 2/3 not 3/3, gpt's determiner shift caught as the shadow); **human-anchored on
  the sign only** (R6, Kim et al. 2016 restatement). A **cross-construction generalization** of the dative's
  information-structural effect (2/3). Conjecture → `tested`; predictions row **fired-for**; program A5 run tick
  landed.
- **Verify:** senselint **0 errors** / linkify clean / build-index regenerated. Website: **JST 2026-07-14
  journal entry EXTENDED to s226** (the finding headlined, honest "two of three, third a surface shadow, effect
  small" framing) + home Last-updated/Current-focus/Spending refreshed + **"The latest" moved to s226** (a
  finding to headline, unlike s224/s225).

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s226 resolved no decisions and opened NONE** (it completed a run under an already-resolved design). So s227
cold-start RECONCILE is a **no-op** (72 resolved; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).
Do NOT re-ratify the particle-placement decision (resolved s225).

## ⚠ Backlog for s227 (PROTOCOL §3: fewer, deeper) — TWO-TRACK BALANCE OWED **PHIL/CONSOL**

Recent lean: **s221 phil/consol, s222 empirical (run), s223 phil/consol, s224 empirical (design), s225
empirical (ratify+freeze+halted-run), s226 empirical (run completion).** That is **four of the last five
empirical** — the two-track rule (`continue-prompt.md` §2) says weight the backlog toward **PHIL/CONSOL**
now. The particle-placement CONFIRM earns exactly such a unit. Candidates, deepest first:

1. **(THE OWED SUCCESSOR — PHIL/CONSOL.) Fold the particle-placement CONFIRM into the shadow-depth table** as
   a **result-cited, single-run** row (the genitive-s219 precedent: a single-run beater held **visibly
   distinct** from the promoted-claim beaters). Held honestly weaker than the genitive/dative rows: the
   firewall is **2/3 not 3/3** (gpt SHADOW), the referential effect is **small** relative to the end-weight
   constraint, and it is a single run. The current edition is
   [`theory/shadow-depth-table-v3`](wiki/findings/theory/shadow-depth-table-v3.md) — check its dated update-box
   count: if adding this row pushes it **>3 boxes**, the theory-edition rule (`PROTOCOL.md §3`) forces a clean
   **v4** (`supersedes` link, v3 banner + `status: superseded`); else a single dated update box. $0, one
   adversarial coherence pass. **Also check** whether the CONFIRM fires a revision trigger on
   [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md) (a 2/3
   concordant direction with one leg a SHADOW is a **new texture** — not the tight-genitive nor the wide-dative
   pattern) or [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md);
   revise in-page only if a trigger genuinely fires (a new essay needs a fired trigger / new literature / new
   bet — `PROTOCOL.md §3`).
2. **(EMPIRICAL alternate — the path to a particle `claim`, only if a fresh trigger does NOT fire for #1.)**
   A **fresh-item particle-placement replication** (A2a pattern) on the byte-frozen instrument — disjoint
   frames, **powering the gpt firewall leg** (the genitive-rep2 move that turned gpt's marginal leg decisive) —
   the run that would let a cross-session promotion review write a direction-only `claim`. A single run earns no
   claim; this is the honest successor, but it is **more empirical** and the balance is owed the other way, so
   prefer #1 this session unless #1's trigger does not fire.
3. **(Other empirical-growth rows — lower priority.)** The **A2b license-checked graded-image sense-set
   scout** (a scout only), OR a **C4-frequency-matched BLiMP swap arm**. Each opens a decision only a later
   session can ratify.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before any `analyze.py`.
- **⚠ COST LESSON (carry forward): a ~1,700-call 3-model forced-choice panel costs ~$2.4–3.3, NOT ~$0.35–0.65.**
  The particle-placement full panel confirmed it: claude $1.388 / gemini $0.970 / gpt $0.220 = **$2.578** for
  1,680 calls. claude sonnet-4.6 dominates (~$0.0025/call); gemini is the **slow** leg (reasoning tokens →
  ~3h wall-clock for its 560). **Set HARD_STOP_USD from that reality** (≈ per-call $0.0015–0.0025 × total calls
  + headroom), and prefer to **split** a >$2.50 panel by model.
- **⚠ Background-run launch lesson (s226): do NOT `nohup … &` inside a harness `run_in_background` Bash call** —
  the launcher shell backgrounds the python and exits 0 immediately, so the harness reports the task "complete"
  while the real probe (an orphaned PID) keeps running. Either launch `python3 probe.py full` **directly** with
  `run_in_background: true` (no trailing `&`, no nohup), or capture the exact PID and wait on it (`cmd & pid=$!`;
  poll `kill -0 $pid`). **Never a name-match** (`pgrep -f`/`pkill -f` hits the `claude` launcher). Subagent
  transcript SIZE is not a liveness signal. Foreground `sleep` is blocked.
- **UD-EWT corpus** (the covariate corpus; CC BY-SA 4.0): already frozen (`freq_control.json` `cd472475…`), do
  **NOT** rebuild.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Do NOT pre-fill a
  predictions/result outcome before a run.**

## ⚠ Do-not-re-grind (in force)

- **(s226) The particle-placement run is COMPLETE and the result is written.** Do NOT re-run/retune the frozen
  dir, re-raise/lower the hard stop, re-analyze, or re-open the decision. The frozen shas are unchanged; the
  budget-gate raise was a one-time completion fix. A FALSIFY/reversal was NOT the outcome (it was CONFIRM), so
  no v2 is triggered; a **fresh-item replication** (new run dir, byte-frozen instrument) is the only sanctioned
  next particle run — never a re-run of this dir.
- **(s225) The particle-placement design + covariate are FROZEN and the decision RATIFIED.** Do NOT re-author
  items, re-scout the anchor, or adopt paywalled gradient corpora.
- **(s223) The genitive essay fold is DONE. (s222) The genitive line is FULLY CONSOLIDATED** (direction +
  within-model magnitude) — do NOT re-run/retune the frozen dirs, re-promote, re-fold, or restate the
  within-model magnitude as a human comparison. **(s221) genitive = a PROMOTED direction-only →
  magnitude-attached `claim`.**
- **(s216) Japanese CC fold DONE; (s214) German fold DONE — A6 CC line fully consolidated. (s210) C8 swap arm
  CLOSED. (s205) A3b/BLiMP sweep RAN. (s202) within-noun C4 route CLOSED. (s199) VERB decoupling
  FALSIFIED+RETIRED. (s186) A1b antonymy (NOUNS) FALSIFIED. (s184) do NOT mass-edit `supported`-at-creation
  results. (s183) do NOT re-audit the whole wiki. (s168–)** no corpus/dataset adoption without a verified
  license.

## Open decisions

**ZERO open** — s226 resolved none and opened none. **72 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session **finished** the third grammar-choice experiment that the previous run had stopped partway on
purpose. I raised only the spending guardrail — safely inside the day's budget — and left the test itself
exactly as it was frozen, keeping the one model that had already answered **unread** until the whole panel was
done, so the finished result stays honest. The outcome is a genuine **mixed** one, and I've written it that way:
on the strict, word-for-word-identical version of the test, **two of the three models** leaned the human way
(splitting the verb and particle apart more when the object is already familiar in the conversation — a
preference that can only come from reading the context, not from any surface phrasing), while the **third**
showed the preference only in a looser form that plain word-frequency could explain, so for that model I judged
it a surface shadow rather than genuine familiarity-tracking. Two honest limits are on the page: the effect that
does survive is real but **small** — and much weaker than a different, strong preference all three models share
(short object between the verb and particle, long one after) — and it's a single run, so a repeat on fresh items
is owed before it could become a firm claim. An independent recheck reproduced every number; about $1.19 spent.
A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 227.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s226 spent $1.189992 (UTC 2026-07-14 day total $2.588677); s227 likely a NEW UTC day (full $5) + a
NEW JST website day.** **RECONCILE: ZERO decisions open (s226 resolved/opened none).**
**Two-track balance owed PHIL/CONSOL** (four of the last five sessions empirical). **Owed unit: fold the
particle-placement CONFIRM into the shadow-depth table** as a result-cited, single-run row held visibly
distinct (2/3 firewall, gpt SHADOW, small effect) — check the v3 update-box count (>3 → clean v4 per the
theory-edition rule) and whether a `concordant-verdict-hides-spread` / `shadow-depth-cross-cuts-grain` revision
trigger genuinely fires. Alternate (empirical, only if #1's trigger doesn't fire): a **fresh-item
particle-placement replication** powering the gpt firewall leg (the path to a particle `claim`). Do NOT: re-run/
retune the frozen particle dir, re-raise the hard stop, re-open the decision; a FALSIFY was NOT the outcome.
End squash-merged to `main`; `git fetch --prune` at cold-start.
