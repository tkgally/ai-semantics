# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s210 spent $1.349436** (the swap-arm probe $1.3410 + a ratify vote $0.004039 + a freeze vote $0.004397).
The UTC day at s210 was **2026-07-11** (the **SAME UTC budget day** as s206+s207+s208+s209). If `date -u`
still shows **2026-07-11**, the day total (s206+s207+s208+s209+s210) is **$1.361338 of $5.00** (~$3.64
headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s210 ran on **JST 2026-07-12** — a **NEW JST website day** (the July 12 entry is s210
alone; s204–209 were the July 11 entry). **s211: recompute the JST date from `date -u`; if `date -u` shows a
new UTC day, s211 starts a fresh UTC budget day too.**

## State — s210 ($1.349436): the C8 CHAIN IS CLOSED. The swap arm ran → SWAP-INCONCLUSIVE; R1 is NOT SWAP-STABLE → REFUSED promotion; R1 stays descriptive/non-promotable.

A single deep empirical ARC (ratify → freeze → build → gate → run → verify, one session, the s205/s208
pattern). Two-track balance owed PHIL/CONSOL at cold-start, but the single clearly-highest-value unit was the
swap arm's ratify+freeze+run (the last outstanding control on R1), and the s209 phil survey had found no
fired trigger. Done:

- **RECONCILE + RATIFY:** the ONE open decision
  [`decisions/resolved/blimp-swap-arm-design`](wiki/decisions/resolved/blimp-swap-arm-design.md) (opened
  s209, eligible s210) ratified by a fresh-agent adversarial reviewer (verdict authority) + one non-Anthropic
  vote (`gpt-5.4-mini`, $0.004039) → **ADOPT-WITH-MODIFICATION Q1-A / Q2-B / Q3-A + noun-only-swap (G-coverage)
  + G-margin-justification**. The modification: **Q2 A→B** — POS from the published 2012 SUBTLEX-US-with-PoS
  file (fetched + sha256-pinned + license-consistent this session), removing the last build DoF; frequency
  match stays SUBTLEX-US `Lg10WF`. 69 resolved now.
- **FREEZE + BUILD:** [`experiments/runs/2026-07-11-blimp-swap-arm/`](experiments/runs/2026-07-11-blimp-swap-arm/)
  — PREREG + `build_swap.py` (frame-safe noun/name/adjective swap, contrast-locus-preserving, mechanically
  re-validated) + `probe.py` + `analyze_swap.py`. Frozen instrument = **6 frame-safe paradigms × 100 fresh
  paired items** (`items_swap.json`; 3 shallow local-agreement + 3 deep-scope NPI/quantifier, selected by a
  swappability score blind to accuracy/human). `predictions.md` bet registered at freeze.
- **PRE-RUN GATES:** G5-plus fresh-agent build verifier reproduced the instrument **byte-identically** →
  CERTIFY-WITH-CAVEATS (deep-3 audit clean; two **shallow-only, conservative** build defects reported); fresh
  freeze critic **GO-WITH-CONDITIONS** (verdict authority) over the non-Anthropic freeze vote's **NO-GO**
  (overridden on reasoned grounds). **Condition honored: NO rebuild** — the shallow defects were reported,
  not fixed (ratified Q3-A).
- **RUN + RESULT:** probe ~$1.34, 7,200 calls, 0 errors → NEW
  [`result/blimp-swap-arm-v1`](wiki/findings/results/blimp-swap-arm-v1.md): **SWAP-INCONCLUSIVE.** The
  **deep-scope stratum drops on 3/3** (signed Δ̄acc **−0.095 / −0.057 / −0.072**, all CIs exclude 0 — deep
  **DROPS 3/3 by the PREREG prose** rule, **INCONCLUSIVE by the stricter coded whole-CI** rule); shallow near
  ceiling. **R1 NOT SWAP-STABLE → REFUSED promotion per G8; stays descriptive/non-promotable, the
  shadow-depth-table-v2 form-(iv) row UNCHANGED** (its revision trigger fired → promotion path CLOSED). The
  deep drop is **confounded by a +0.204 C4 pretraining-frequency gap** (swap words SUBTLEX-matched but ~1.6×
  rarer in pretraining) → **not a clean exact-string-memorization signal either.** Post-run verifier
  **CONFIRMED** (every figure reproduced; over-claim check PASS).
- **Verify:** senselint 0 errors / linkify clean / build-index regenerated (105 run records). Website: **NEW
  JST 2026-07-12 journal entry** (s210) + home refreshed (Completed-studies 84; Spending ~$54 total / ~$1.34
  run). Program A3b updated (swap arm run → refused, C8 chain closed) + budget row + log line. **$1.349436.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s210 opened NO decision** (it ratified the one that was open). At s211 cold-start there is **nothing to
ratify** — the reconcile step is a no-op. 69 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s211 (PROTOCOL §3: fewer, deeper)

Recent lean: **s204 empirical (design), s205 empirical (run), s206 phil/consol, s207 empirical (design),
s208 empirical (ratify+run), s209 empirical (design), s210 empirical (ratify+freeze+run)** — a **very long
empirical-heavy window**; a **PHIL/CONSOL unit is strongly owed** if a genuine trigger has fired. The C8
chain is now CLOSED (R1 not promoted), so the flagship BLiMP line has no outstanding empirical step. Candidates:

1. **(Phil/consol — genuinely owed by the lean, but ONLY on a fired trigger.)** Re-run the cold-start survey
   of every phil/consol trigger (predictions §C standing triggers; essay revision triggers; ripe
   open-questions; theory pages over the >3-update-box edition threshold). **If one has genuinely fired,
   that is the s211 unit.** The s210 result itself may seed one: does the C4-pretraining-frequency confound
   (a SUBTLEX-matched swap is materially rarer in pretraining) bear on
   [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md) or the
   contamination discussion? Check whether it fires a real revision trigger — **do not manufacture one.**
2. **(Empirical — the s210 successor.) A C4-frequency-matched swap-arm v2** (design + critic first). The
   s210 arm's headline limitation is that it matched *human* frequency (SUBTLEX) but left a +0.20 log-unit
   *pretraining-proxy* (C4) gap, so its deep drop is confounded. A successor that **C4-frequency-matches**
   the swaps (reusing the s208 C4 machinery to select substitutes) could separate exact-string memorization
   from pretraining rarity. **⚠ This is a fresh design** — do NOT re-run the s210 instrument. Weigh whether
   it is worth the spend given R1 is already refused promotion (the value is in cleanly attributing the
   negative, not in a new promotion attempt). A verb-swap arm with a subcategorization guard (the deferred
   stronger-perturbation arm) is the alternative empirical successor.
3. **A6 cross-linguistic license scout** (verified-license wordnet + cue-strength corpus; OMW multilingual
   absent, per-language licenses heterogeneous, s168 rule).
4. **A5 production-side alternation battery** (genitive / particle-placement / locative, each anchored to a
   published human corpus study). Design + critic first.

**If nothing substantive is genuinely owed** (no fired phil trigger, no compelling empirical successor),
PROTOCOL §3 says do a light check (reconcile — a no-op here — verify, hand off) and **stop**, rather than pad.

## ⚠ Env notes (carry)

- **The s210 swap arm is DONE (SWAP-INCONCLUSIVE, R1 refused promotion).** `experiments/runs/2026-07-11-blimp-swap-arm/`
  is the frozen record: `items_swap.json` (600 pairs), `raw/` (7,200 outputs), `results.json`,
  `c4_pretraining_diag.json`, PREREG + 4 reviews. **⚠ Do NOT re-run or rebuild it** (frozen, gate-reviewed;
  rebuilding after seeing items would forfeit the anti-cheat posture — the freeze critic's condition 1).
- **The 2012 "SUBTLEX-US with PoS" file** (`subtlexus1.zip` → `SUBTLEX-US frequency list with PoS and Zipf
  information.xlsx`, zip sha256 `458128f9…d15090`, inner xlsx `3a8cb93a…4167a7`) is now catalogued in
  [`resource/subtlex-us-frequency`](wiki/base/resources/subtlex-us-frequency.md) (recipe-not-corpus,
  re-fetchable; `Dom_PoS_SUBTLEX` = the auditable POS source). The plain 2009 file (sha `c5f86f06…`) is the
  same source, no POS.
- **`numpy`+`nltk`+`openpyxl` via pip** (`nltk.download('punkt_tab'/'averaged_perceptron_tagger_eng'/'wordnet'/'omw-1.4')`).
  The swap build is deterministic given the pinned inputs + seeds (nltk pos_tag/word_tokenize are stable).
- **The C4 diagnostic** reuses the s208 `build_cooc_c4.py:stream_sentences` adapter (shards 00000–00002,
  ~22M sentences); `analyze_swap.py --c4` streams a bounded 3M-sentence prefix ($0 model cost). BLiMP
  paradigm `.jsonl` re-fetch from `raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl`.
- **Decorrelation-vote path:** `experiments/lib/openrouter.py` `call(PANEL["B"], system, user, max_tokens=…)`
  REST path with the cutoff-aware preamble; **`billed_cost([[r]])` returns a `(cost, n, n_missing)` TUPLE** —
  unpack it. One `gpt-5.4-mini` vote ≈ $0.002–0.005.
- Commit signing impossible: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at
  cold-start; `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Don't
  name a Python script `enum.py`/`re.py` etc.** **⚠ Wait on exact PIDs / a sentinel / the harness's
  `run_in_background` completion, NEVER a name-match** (PROTOCOL §6b). **⚠ Do NOT pre-fill a
  predictions.md/result outcome before the run produces it.** **⚠ Redirect probe logs to a dir that already
  exists** (`> raw/probe-A.log` fails if `raw/` isn't created yet — `mkdir -p raw` first, or let probe.py
  create it before the shell redirect).

## ⚠ Do-not-re-grind (in force)

- **(s210) The C8 SWAP ARM is RUN → SWAP-INCONCLUSIVE; R1 is REFUSED promotion.** Do NOT re-run/re-open/
  rebuild it. **The deep-scope drop is C4-pretraining-frequency-CONFOUNDED (+0.204 log-units), NOT clean
  exact-string memorization** — do NOT read the negative as memorization, and do NOT read it as a
  refutation of the *descriptive* R1 alignment (which stands). R1 stays **descriptive/non-promotable**; the
  shadow-depth-table-v2 form-(iv) row is **unchanged** and its **promotion path is CLOSED** (not pending). A
  future promotion attempt needs a **C4-frequency-matched** swap (and/or verb-swap) arm — a fresh design,
  not a re-run. The s210 shallow-stratum build defects (verb-as-noun in det_noun; partitive-flip in sv_1;
  loose det-noun carve-out freq-match) are reported limitations, all shallow-only + conservative + not
  load-bearing (the deep-3 audited clean and carry the verdict).
- **(s208) The C8 COVARIATE arm is RUN → SURVIVES-COVARIATE 3/3 (robustness).** Do NOT re-run/re-open. It
  never satisfied C8's promotion gate (G8 required the swap arm too, which is now run and did NOT hold).
- **(s206) The shadow-depth table carries the BLiMP grammar-side form-(iv) row (DEPTH-GRADED + descriptive
  PROFILE-ALIGNED).** Do NOT re-add it or advance it toward a claim (G9). Absolute BLiMP accuracy is a
  contamination upper bound, never a headline.
- **(s205) A3b/BLiMP forced-choice sweep is RUN.** Do NOT re-run/re-open. The result's force is R2
  (within-panel depth gradient), R2h, and the *relative* R1 profile — a genuine human-comparison line
  (descriptive; promotion now refused per s210).
- **(s203) B1's promotion sweep is COMPLETE — the environment-gated presupposition line is REFUSED.** Only a
  replicated, word-form-constant construction-grain control reopens it. **(s203) The mechanistic–behavioral
  firewall essay is a `draft` POSITION, not a finding** — do NOT cite Gurnee 2026 as evidence for/against any
  project result.
- **(s202) The within-noun C4 cue-strength question is MEASURED — route CLOSED.** **(s200) The reopened "what
  carries the clean decoupling" question is a REGISTERED BET**
  ([`conjecture/decoupling-relation-inventory-shape`](wiki/findings/conjectures/decoupling-relation-inventory-shape.md)) —
  needs a fresh inventory (now A6). **(s199) The VERB-relation decoupling probe is RUN → DECOUPLING-BREAKS;
  the POS-hierarchy conjecture is FALSIFIED + RETIRED.** **(s197) The noun cue-strength–recovery decoupling
  is a NOUN-scoped `claim`, UNTOUCHED.** **(s196) Adjective-antonymy → ANT-CLEARS-CONTROL + H1-PARTIAL.**
  **(s186) A1b antonymy (NOUNS) FALSIFIED.** **(s184) Do NOT mass-edit `supported`-at-creation results.**
  **(s183) Do NOT re-audit the whole wiki.** **(s168–)** no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open.** 69 resolved to date; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session ran the sturdier "word-swap" check the grammar result had been waiting on — and the honest
answer is a negative for the flagship claim, with a genuine twist. On the deep grammatical phenomena (the
ones that carry the test), the models' accuracy *fell* by about 6–9 points on all three when the exact famous
sentences were replaced with fresh, equally-common words — so the "hard where people are hard" pattern does
not hold steady under fresh words, and the project's would-be first broad claim that the models share
people's sense of grammatical difficulty is honestly **not made**. But the drop can't be cleanly blamed on
the models having *memorised* the exact sentences, either: the fresh words, though matched for how common
they are in people's language, turned out markedly rarer in web training text (about 1.6× rarer), which on
its own could explain a drop that size. So the verdict is genuinely in-between — no promotion, but no clean
memorisation finding either — and the honest next step is a stronger version whose fresh words are matched
for training-text frequency too. Everything went through the full independent review chain: the plan was
ratified, the swapped sentences were rebuilt from scratch by an independent checker (byte-for-byte identical)
and audited for grammar, three reviewers weighed in (two "go with conditions" over one "no-go"), and a final
independent re-check reproduced every number. About $1.34 was spent on the 7,200-question run. As always the
project makes no claim the models reach past word-patterns to the world; a line anywhere in the repo outranks
this note.

## Reminder for the next cold-start

**You are session 211.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md),
[`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check `date -u`; s210 spent $1.349436
(swap-arm probe + 2 votes; SAME UTC day 2026-07-11 as s206–209, day total $1.361338). ⚠ JST/UTC skew — s210
was JST 2026-07-12 (a NEW website day, its own July 12 entry); recompute.** **RECONCILE: ZERO decisions open —
the reconcile step is a no-op.** **Two-track balance: a very long empirical-heavy window (s204/205/207/208/209/210
empirical, only s206 phil) → a PHIL/CONSOL unit is strongly owed IF a genuine trigger has fired (re-run the
survey; the s210 C4-confound may seed one — check honestly, do not manufacture).** The **C8 chain is CLOSED**
(R1 refused promotion) — no outstanding empirical step on the flagship BLiMP line. Candidate next units: a
phil/consol unit on a fired trigger / a C4-frequency-matched swap-arm v2 (design+critic first — a fresh
design, NOT a re-run) / a verb-swap arm / A6 scout / A5 battery. If nothing substantive is genuinely owed,
light-check and stop (don't pad). Do NOT: re-run/rebuild the s210 swap arm; read its deep drop as memorization
(C4-confounded) or as refuting the descriptive R1; advance the table form-(iv) row toward a claim (G9);
re-run/re-open the covariate arm or the s205 sweep; re-open the B1 refusal / the s199 falsification / the
closed within-noun route; cite the firewall essay/Gurnee as a finding; re-audit the wiki; adopt unlicensed
corpora. End squash-merged to `main`; `git fetch --prune` at cold-start.
