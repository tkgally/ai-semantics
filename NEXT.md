# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). The standard **$5.00/day (UTC)** cap is in force. **s184 spent $0.002774** (two non-Anthropic ratification votes), booked to **UTC 2026-07-06**. So if `date -u` still shows **2026-07-06**, the day stands at **$0.002774 of $5.00** (~**$5.00** headroom); if **2026-07-07+**, a **fresh $5.00**. Ledger: [`config/budget.md`](config/budget.md). Sizing rule ([`PROTOCOL.md`](PROTOCOL.md) §4): claim-carrying probes use powered N (~100–150 items); prefer-split above ~$2.50/run. Cost caveats: non-Anthropic votes via `experiments/lib/openrouter.py` ~$0.001–0.004/vote with `max_tokens=~500`; the A1b antonymy probe pre-flights at **≈$0.8–1.6** (short outputs) but is **not runnable until its decision ratifies + a co-occurrence corpus is scouted** (see below).

## State — s184 ($0.002774): both s183 decisions ratified (ADOPT-A); campaign P2 done; A1b antonymy design landed + decision queued; form-ceiling-wobble seed placed

Workflow mode, 2 waves + a coherence pass. **Wave 1 (RECONCILE + P2):** both s183-opened decisions **ratified ADOPT-A** — each by an independent fresh-agent adversarial review **and** one non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`), **converging on both**:

1. [`decisions/resolved/result-status-upgrade-semantics`](wiki/decisions/resolved/result-status-upgrade-semantics.md) → **ADOPT-A**. The event-based result/theory status-transition rule is now documented in [`CLAUDE.md`](CLAUDE.md) ("Result and theory status discipline"): status moves only on a recorded dated event; **mechanical-gate** results may be created `supported`, **reading-bearing** results rest at `proposed` with `supported` living on the **claim layer**; result `status` is declared **non-ranking / possibly-stale until normalized**; theory `draft → live` deferred to each page's next substantive touch. **No result mass-edited; no theory flipped to `live`** (option A's no-mass-edit clause — the ~15 `supported`-at-creation pages normalize at each next touch).
2. [`decisions/resolved/meaning-senses-methodology-tags`](wiki/decisions/resolved/meaning-senses-methodology-tags.md) → **ADOPT-A**. Added `measurement-epistemic` to [`meaning-senses.md`](wiki/meaning-senses.md) (broadened gloss + How-to-tag guardrail); retagged the six `base/sources/` methodology pages (Borsboom keeps `referential`).

**Campaign P2 cleared** (the ledger's Deferred-to-P2 list): `operationalizes: design/<id>` blessed in CLAUDE.md; one pending-Tom straggler (way-construction) governance-noted; `homonym-meaning-dominance-norms` regraded `scouting → verified`; 7 touched pages' `updated:` bumped; spine lag-scan found only citation-date false positives; linkify clean; senselint 0 errors. **P2 ticked** in [`continue-prompt.md`](continue-prompt.md) §5 + [`wiki/maintenance.md`](wiki/maintenance.md).

**Wave 2 (empirical + philosophical):**
- **A1b antonymy internal-contrast — DESIGN landed** ([`design/lexical-relation-shadow-saturation-v1`](experiments/designs/lexical-relation-shadow-saturation-v1.md)), **nothing frozen, nothing run.** Three value-laden gates opened as [`decisions/open/antonymy-internal-contrast-scoring`](wiki/decisions/open/antonymy-internal-contrast-scoring.md) (**eligible s185**): Q1 the distributional control (**the design confirmed SubTLEX-US is unigram-only — no co-occurrence data in-repo — so the contrastive-frame control must be fetched from a license-verified corpus or substituted by an embedding proxy, gated on a scout**), Q2 the no-human-gold recovery scoring (default: WordNet-definitional target + model-vs-control hit-rate residual), Q3 the `internal-contrast-only` anchor; plus a frame-ablation arm (needs no external corpus). Conjecture/predictions/program forward-pointers added.
- **Philosophical — form-ceiling-wobble seed placed** as an in-page revision (a "third texture") on [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md): a coarse **binary** indicator can be more fragile than the **graded** one it summarizes, because of measurement grain — not intrinsic formal fragility, and distinct from `point-estimate-is-a-draw`'s jitter (this is genuine signal). situating-v2's "unplaced seed" note updated to point at it.

## ⚠ RECONCILE at cold-start — 1 decision open, eligible s185

Opened s184 (by the A1b design; **never ratifiable in the opening session — s185+ may ratify**, PROTOCOL §2: fresh adversarial reviewer + one non-Anthropic vote):

- [`decisions/open/antonymy-internal-contrast-scoring`](wiki/decisions/open/antonymy-internal-contrast-scoring.md) — the three gates of the A1b probe (Q1 control / Q2 scoring / Q3 anchor). Provisional defaults: Q1-C (faithful contrastive-frame control primary + embedding sensitivity, gated on a license scout), Q2-A (definitional-target hit-rate residual), Q3 internal-contrast-only. Ratifying this = the first half of the s185 A1b unit.

## ⚠ Campaign state (Tom-directed; read `continue-prompt.md` §5 + `wiki/maintenance.md` before campaign work)

- **P1 `[x]` (s183); P2 `[x]` (s184).** **P3 next:** program **B6** note-sweep (~10 measurement-free result pages → `wiki/findings/notes/`; create the dir with the first one; each reclassification states why) + the orphan-source cures the ledger lists. P4 = concept on-ramp deepening + ideas-harvest triage; P5 = close-out (spot re-audit, delete continue-prompt §5).
- **P3 pairs well with the A1b ratify+run** (the campaign rule allows sharing a session with an owed empirical unit) — but A1b's *run* is gated on the corpus scout, so s185 may be: ratify the A1b decision + run the corpus/license scout (if Q1-A/C) OR do P3 while the scout is pending.

## ⚠ Empirical backlog

- **A1b antonymy** — design landed s184. **s185: ratify [`decisions/open/antonymy-internal-contrast-scoring`](wiki/decisions/open/antonymy-internal-contrast-scoring.md)** (fresh reviewer + non-Anthropic vote), then per Q1: **run a license scout for a co-occurrence corpus** (own resource page + verified license; never adopt unverified — s168 discipline) before freezing. Freeze `prep.py` (WordNet items, frequency-matched, outlier-capped) → PREREG → pre-run critic + vote → run (powered N ~120–150 cues, ≈$0.8–1.6). Design: [`design/lexical-relation-shadow-saturation-v1`](experiments/designs/lexical-relation-shadow-saturation-v1.md).
- **A2b grounding magnitude** = external-resource **SCOUT only** (un-instrumentable in-repo; [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)). Ledger Tier-1 seed #4 (RAW-C/SAW-C license scout) is the adjacent text-side scout.
- **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is legitimate (the s173 doppelgänger left it under-licensed).

## ⚠ Env notes (carry)

- `nltk`/WordNet + `numpy` install cleanly via `pip install nltk numpy` + `nltk.download('wordnet')` (tested s182; WordNet 3.0 License verified in-repo — [`resource/wordnet-sense-inventory`](wiki/base/resources/wordnet-sense-inventory.md)). **SubTLEX-US is unigram-only** (no co-occurrence/bigram data; the 51M-word source corpus is not in-repo) — confirmed s184. openrouter MCP flaky — use the probe REST path for votes (`max_tokens=~500`). Commit signing impossible (cosmetic): set `user.email noreply@anthropic.com` + `user.name Claude`; the authoritative commit is the squash-merge. Long probes: `run_in_background: true`; **never name-match waits** (PROTOCOL §6b). `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main` if the branch is gone.

## ⚠ Do-not-re-grind (in force)

- **(s184) Do NOT mass-edit the ~15 `supported`-at-creation result pages** — the ratified rule normalizes them at each page's *next touch* (no sweep). Do NOT flip theory pages to `live` except at a genuine substantive touch. Do NOT run A1b before its decision ratifies + a co-occurrence corpus is license-scouted.
- **(s183) Do NOT re-audit the whole wiki** — work from [`wiki/maintenance.md`](wiki/maintenance.md)'s lists. Do NOT mass-retarget theory-v1 references (edition-citation convention governs).
- **(s182) No B3 destructive essay merges** (load-bearing web; [`wiki/ideas.md`](wiki/ideas.md) is the map). **(s181) All four flagship A2a re-runs DONE** — no re-runs/re-promotions; a full-scope sense-gradience magnitude edition needs a usage-independent re-run + a human effect-size anchor (neither in hand). **(s179) Cite the theory -v2s.** **(s170) Founding questions stay closed.** **(s168–)** no A3a/corpus dataset adoption without a verified DATA license.

## Next concrete actions — backlog for session 185 (PROTOCOL §3: fewer, deeper)

1. **RECONCILE ($0):** ratify [`decisions/open/antonymy-internal-contrast-scoring`](wiki/decisions/open/antonymy-internal-contrast-scoring.md) (fresh adversarial reviewer + non-Anthropic vote); fix Q1/Q2/Q3; if Q1-A/C, this unblocks the corpus scout.
2. **EMPIRICAL — A1b toward a run:** run the **license scout** for a co-occurrence corpus (own resource page + verified license). If a corpus clears, freeze `prep.py` + PREREG + pre-run critic + vote, then run (powered N ~120–150). If none clears, record the block and lean on the frame-ablation arm (needs no external corpus) or defer the run.
3. **CONSOLIDATION — campaign P3** (program B6 note-sweep + orphan cures) — a good deep unit if A1b's run is scout-gated; pairs with the A1b ratification.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md): substantive session → extend **today's** JST entry (check `TZ=Asia/Tokyo date`); a pure-ratification/scout session still records the ratification in the day's entry (Ruling 1).

## Open decisions

**One** — `antonymy-internal-contrast-scoring` (s184-opened, **eligible s185**). 61 resolved to date (2 landed s184; [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## Standing-override notes (for Tom, if he looks)

- This session settled the two small record-keeping questions the housekeeping audit had queued last week — what a "status" label on a result page may mean, and how to tag a few methodology sources — each checked by a fresh reviewer and, separately, by an outside-company model, both agreeing. It also designed (but did not run) a new experiment on whether a model's grasp of opposites is genuine or an echo of how often opposites appear together in text; writing it surfaced that the word-pair data it needs isn't in hand and must be built from a fresh licensed text collection first, so that choice is queued for review before any run. And it placed the "coarse yes/no vs fine graded" observation the previous day had flagged. Under a cent spent. If you want the maintenance campaign paced differently, a line anywhere in the repo outranks the plan.

## Reminder for the next cold-start

**You are session 185.** Entry [`continue-prompt.md`](continue-prompt.md) (note its **§5 campaign section**); charter [`PROJECT.md`](PROJECT.md) (§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§3–§4); conventions [`CLAUDE.md`](CLAUDE.md) (note the **s184 result/theory status discipline** + the `measurement-epistemic` tag); program [`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check `date -u`; s184 spent $0.002774** (2026-07-06). **RECONCILE: 1 decision open, eligible s185** (`antonymy-internal-contrast-scoring`). Most-owed: **ratify the A1b decision + the corpus license scout** (toward the s185 run), pairing with **campaign P3** if the run is scout-gated. Do NOT: mass-edit `supported`-at-creation results, flip theory to `live` outside a substantive touch, run A1b pre-ratification/pre-corpus-scout, re-audit the wiki, mass-retarget theory-v1 refs, B3 merges, A2a re-runs, founding-question re-opens, unlicensed corpus/dataset adoption. End squash-merged to `main`; `git fetch --prune` at cold-start.
