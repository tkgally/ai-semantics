# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). The standard **$5.00/day (UTC)** cap is in force. **s183 spent $0.00** (wiki-coherence campaign P1 — no probe, no votes). The day's only spend remains **s181's $0.689661**, booked to **UTC 2026-07-05**. So if `date -u` still shows **2026-07-05**, the day stands at **$0.689661 of $5.00** (~**$4.31** headroom); if **2026-07-06+**, a **fresh $5.00**. Ledger: [`config/budget.md`](config/budget.md). Sizing rule ([`PROTOCOL.md`](PROTOCOL.md) §4): claim-carrying probes use powered N (~100–150 items); prefer-split above ~$2.50/run. Cost caveats: DWUG instrument not reliably expensive (s181 $0.685); non-Anthropic votes via `experiments/lib/openrouter.py` ~$0.001–0.004/vote with `max_tokens=~500`.

## State — s183 (Tom-directed, $0): the wiki-coherence campaign opened; P1 done — full audit + fix tranche + regenerated executive summary

**Session 183 ran on Tom's standing override** (wiki polish & coherence instead of a regular unit; multi-session plan requested). Workflow mode: 6 parallel read-only auditors over all ~370 pages → orchestrator triage (~170 issues, 12 BLOCKERs) → orchestrator fixed every BLOCKER + 5 directive-driven fix agents applied the batch tranche → adversarial coherence pass over the diff. Highlights:

1. **Diagnosis:** the findings are sound (no wrong number/verdict/scope; one off-by-one annotator tally recomputed from raw and corrected — v1 sense-gradience 152/200 two-annotator, n≥3=48). The systemic defect was **back-annotation lag**: result/concept/resource pages never learned their lines were later promoted/replicated/retired/superseded. Both live theory v2 editions still said "single-run" where their own named triggers had fired (s178/s181) — fixed with dated update boxes.
2. **Fixed** (history-preserving, all dated s183): ~45 results back-annotated; 13 "awaits Tom's review" archaisms governance-noted (PROJECT.md §12.3); ~25 one-time edition pointers at as-if-current theory-v1 cites; ~20 missing `supports` back-links to promoted claims; concepts/resources reconciled (polysemy, relational-meaning, constructional-meaning, DWUG, VWSD, scivetti, resources catalog +5 entries); essay convention standardized (4 stale blockquotes, 4 status normalizations, trigger-site annotations incl. the witness-seeking trigger-(a) contradiction); [`wiki/executive-summary.md`](wiki/executive-summary.md) **fully regenerated** (program **B4 ticked** — was ~59 sessions stale); [`wiki/predictions.md`](wiki/predictions.md) completed (missing under-licensed-middle cleft §B row + 2 essays named in §C); [`wiki/program.md`](wiki/program.md) item bodies reconciled (A1b/A2b/A3a/A3c/D3); `CLAUDE.md` corrected (`anchors` direction was documented backwards) + 2 conventions documented (edition citations; essay status discipline); `multimodal-anchor-scouting` front-matter added (senselint residue now exactly the documented 1 WARN).
3. **Campaign records:** plan in [`continue-prompt.md`](continue-prompt.md) **§5** (phases P1–P5; P1 `[x]`); live ledger [`wiki/maintenance.md`](wiki/maintenance.md) (what was fixed / deliberately not changed / deferred-to-P2 / **~30-seed ideas harvest** in 3 tiers). Website: today's JST entry extended to s179–183 (housekeeping section), home status + plans.html updated.

## ⚠ RECONCILE at cold-start — 2 decisions open, BOTH ELIGIBLE at s184

Opened s183 (by the audit; never ratifiable in the opening session — **s184+ may ratify**, PROTOCOL §2: fresh adversarial reviewer + one non-Anthropic vote each):

1. [`decisions/open/result-status-upgrade-semantics`](wiki/decisions/open/result-status-upgrade-semantics.md) — what `status: supported` on a RESULT page means / who flips it (default A: event-based transitions; deprecate supported-at-creation; theory v2s may go `live` at next touch). ~10 pages' statuses untouched pending this.
2. [`decisions/open/meaning-senses-methodology-tags`](wiki/decisions/open/meaning-senses-methodology-tags.md) — the 6 methodology sources' undeclared tags (default A: one new `measurement-epistemic` tag + 6 mechanical retags + vocabulary edit).

Ratifying + applying these = the first half of campaign **P2**.

## ⚠ Campaign state (Tom-directed; read `continue-prompt.md` §5 + `wiki/maintenance.md` before campaign work)

- **P1 `[x]` (s183).** P2 next: ratify/apply the two decisions + the ledger's "Deferred to P2" list (small: date bumps, a governance-phrase grep-sweep, `operationalizes: design/...` target-type call, link re-verify). **P2 is light — pair it with the A1b design** (the campaign rule allows sharing a session with an owed empirical unit).
- P3 = program B6 note-sweep + orphan cures; P4 = concept on-ramp deepening + ideas-harvest triage; P5 = close-out (spot re-audit, delete continue-prompt §5).

## ⚠ Empirical backlog (unchanged from s182 in substance; program.md item bodies now say this too)

- **A1b antonymy** = fresh **design + decision-trail** unit (control built from scratch: WordNet relation pairs + co-occurrence baseline from in-repo SubTLEX-US; `nltk`/WordNet + `numpy` install cleanly; the value-laden crux is scoring "recovery" **without** a human gold). Design s184, ratify + run s185. The maintenance ledger's Tier-1 seed #1 (frame-ablation instrument, from the Justeson–Katz parallel-frame finding) is **design input** for it.
- **A2b grounding magnitude** = external-resource **SCOUT only** (un-instrumentable in-repo; [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)). The ledger's Tier-1 seed #4 (RAW-C/SAW-C license scout) is the adjacent text-side scout.
- **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is legitimate (the s173 doppelgänger left it under-licensed).

## ⚠ Env notes (carry)

- `nltk`/WordNet + `numpy` install cleanly via pip (tested s182). openrouter MCP flaky — use the probe REST path for votes (`max_tokens=~500`). Commit signing impossible (cosmetic): set `user.email noreply@anthropic.com` + `user.name Claude`; the authoritative commit is the squash-merge. Long probes: `run_in_background: true`; **never name-match waits** (PROTOCOL §6b). `git fetch --prune` at cold-start; `git checkout -B <branch> origin/main` if the branch is gone.

## ⚠ Do-not-re-grind (in force)

- **(s183) Do NOT re-audit the whole wiki** — P1 is done; work from [`wiki/maintenance.md`](wiki/maintenance.md)'s lists. Do NOT flip the ~10 `supported`-at-creation result statuses before the decision ratifies. Do NOT mass-retarget theory-v1 references (edition-citation convention in `CLAUDE.md` governs; the v1 banners route readers).
- **(s182) No B3 destructive essay merges** (load-bearing web; [`wiki/ideas.md`](wiki/ideas.md) is the map). **(s181) All five flagship A2a re-runs DONE** — no re-runs/re-promotions; a full-scope sense-gradience magnitude edition needs a usage-independent re-run + a human effect-size anchor (neither in hand). **(s179) Cite the theory -v2s;** never restate situating-v2 as a verdict flip. **(s170) Founding questions stay closed.** **(s168–)** no A3a dataset adoption without a verified DATA license.

## Next concrete actions — backlog for session 184 (PROTOCOL §3: fewer, deeper)

1. **RECONCILE + campaign P2 ($0):** ratify the two s183 decisions (fresh adversarial reviewer + non-Anthropic vote each); apply what ratifies; clear the ledger's Deferred-to-P2 list; tick P2 in `continue-prompt.md` §5 + the maintenance ledger.
2. **EMPIRICAL DESIGN ($0) — A1b antonymy internal-contrast:** the whole-session deep unit if P2 is done quickly (they pair well). Decision trail for: relation set, item source, co-occurrence baseline construction, and the no-human-gold recovery scoring. Freeze nothing; open the design decision for s185 ratification.
3. **CONSOLIDATION ($0) — campaign P3** (program B6 note-sweep, ~10 measurement-free result pages → `wiki/findings/notes/`) — if P2+A1b don't fill the session; otherwise s185+.
4. **PHILOSOPHICAL ($0) — place the form-ceiling-wobble seed** (in-page revision candidate on [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md) or [`essay/point-estimate-is-a-draw`](wiki/findings/essays/point-estimate-is-a-draw.md); check the PROTOCOL §3 essay bar — most likely an in-page revision, not a new essay). Still unplaced; the situating-v2 revision hook lists it.
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md): substantive session → extend **today's** JST entry (check `TZ=Asia/Tokyo date`); pure P2 bookkeeping + ratifications = the ratifications must appear in the day's entry.

## Open decisions

**Two** — both s183-opened, both **eligible s184**: `result-status-upgrade-semantics`, `meaning-senses-methodology-tags` (see RECONCILE above). 59 resolved to date ([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## Standing-override notes (for Tom, if he looks)

- This session did what you asked on 2026-07-05: it audited the whole wiki (about 370 pages, six independent readers, every flag verified before any change), fixed the places a reader could be misled — the findings themselves all checked out; what lagged was the paperwork around them — rewrote the plain-language executive summary from scratch, harvested about thirty future-research ideas into one place, and wrote the multi-session continuation plan into `continue-prompt.md` §5 with a public ledger at `wiki/maintenance.md`. Two small bookkeeping rules the audit surfaced were queued for independent review next session rather than settled today, per the project's own discipline. Nothing was spent. If you want the campaign paced differently (e.g. all phases before any new experiments, or the reverse), a line anywhere in the repo outranks the plan as written.

## Reminder for the next cold-start

**You are session 184.** Entry [`continue-prompt.md`](continue-prompt.md) (note its **§5 campaign section**); charter [`PROJECT.md`](PROJECT.md) (§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§3–§4); conventions [`CLAUDE.md`](CLAUDE.md) (note the s183 additions: edition citations, essay status discipline, corrected `anchors` direction); program [`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), and now [`wiki/maintenance.md`](wiki/maintenance.md) (campaign ledger). **Budget: $5/day UTC — check `date -u`; s183 spent $0** (2026-07-05 stands at ~$4.31 headroom if still that day). **RECONCILE: 2 decisions open, both eligible.** Most-owed: **campaign P2 + A1b design** (pair them). Do NOT: re-audit the wiki, flip result statuses pre-ratification, mass-retarget theory-v1 refs, B3 merges, A2a re-runs, theory re-editions, founding-question re-opens, unlicensed A3a adoption. End squash-merged to `main`; `git fetch --prune` at cold-start.
