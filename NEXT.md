# NEXT.md

## State

The project is **three-axis**: **grammatical** (live, robust — 11 own-design results), **lexical**
(live: conjecture clauses a+c supported, b a null awaiting the homonymy-enriched test below), and
**multimodal / grounding** (now **two negatives**: the text-side perceptual-moderation null + this
session's image-experiment redundancy null). This session (2026-05-31, **workflow mode**, branch
`claude/blissful-lovelace-Ts4Fp`, **PR #30**) applied Tom's round-of-decisions and ran the project's
**first image-input experiment**.

What landed (2 full waves + 3 independent adversarial passes [pre-run critic + post-run verifier on the
image probe, plus the Wave-1 coherence done by the orchestrator]):

1. **Housekeeping / decisions (Wave 1).** Budget **raised to $20/week** (soft, all-in;
   [`config/budget.md`](config/budget.md)). **Two decisions resolved:**
   [`conflicting-cue-human-anchor`](wiki/decisions/resolved/conflicting-cue-human-anchor.md) (Option A —
   the off-ceiling/bridge/cross-axis results stay **internal-contrast-only**; 8 results promoted,
   `anchor: pending`→ terminal **`anchor: internal-contrast-only`**, senselint + CLAUDE.md extended to
   recognize the terminal state — **no finding changed**) and
   [`multimodal-panel-and-grounding-theory`](wiki/decisions/resolved/multimodal-panel-and-grounding-theory.md)
   (Q1=A panel, Q2=A Lyre grounding, **Q3=B GO** image probe).
2. **The image experiment — a REDUNDANCY NULL (Wave 2).**
   [`result/multimodal-grounding-image-v1`](wiki/findings/results/multimodal-grounding-image-v1.md):
   showing a depicting picture does **not** improve the panel's same/different-synset separation, because
   the **text-only panel already separates them perfectly (AUC=1.000 every cell)**. Lone exception:
   gpt-5.4-mini on the 0–100 scale pushes different-synset pairs ~8 pts toward "unrelated" (Δsep +7.2, CI
   excludes 0, survives the same-referent distraction control); claude shows the opposite micro-wobble.
   12 WordNet-keyed constructed pairs (6 distinct-homonym F + 6 same-T), 24 CC0/PD Wikimedia images
   sha256-frozen **before any model call**, 144 calls, 0 NA, **$0.2286 billed**. New
   [`resource/wordnet-sense-inventory`](wiki/base/resources/wordnet-sense-inventory.md) (WordNet 3.0
   License verbatim). Run: [`experiments/runs/2026-05-31-multimodal-grounding-image-v1/`](experiments/runs/2026-05-31-multimodal-grounding-image-v1/README.md).
3. **Groundwork for all three axes (Wave 1, no API).** New [`resource/wic-word-in-context`](wiki/base/resources/wic-word-in-context.md)
   (WiC verified + sha256-pinned), [`design/lexical-polysemy-homonymy-v3`](experiments/designs/lexical-polysemy-homonymy-v3.md)
   (the clause-(b) test), [`design/multimodal-grounding-image-v1`](experiments/designs/multimodal-grounding-image-v1.md);
   relational pilot sharpened + [`experiments/notes/relational-axis-literature.md`](experiments/notes/relational-axis-literature.md);
   [`experiments/notes/cloud-compute-feasibility.md`](experiments/notes/cloud-compute-feasibility.md).

## Next concrete action (backlog — pick by Tom's decision or run un-gated units)

**THE TOP-PRIORITY UN-GATED UNIT IS READY TO RUN:**

1. **Lexical v3 — the polysemy-vs-homonymy DISCRETENESS test (un-gated; ready; ~$4.2 billed new spend).**
   [`design/lexical-polysemy-homonymy-v3`](experiments/designs/lexical-polysemy-homonymy-v3.md) — the
   clean clause-(b) re-run the DWUG v2 null pointed to. WiC is **fetched + verified + sha256-pinned**
   ([`resource/wic-word-in-context`](wiki/base/resources/wic-word-in-context.md)); the **binary anchor is
   ratified** (Tom decision 3a); the instrument reuses the resolved op-gate. **Remaining work (a full
   wave, deferred this session for context/quality — it is the heaviest unit):** build the
   homonymy-enriched WiC subset (the **judgement-heavy etymological stratification** of ~50+ target words
   with quoted sources — `nltk` WordNet is now installable, so the gate's preferred WordNet
   lexicographer-file rule can replace the etymological fallback; freeze `manifest.csv` +
   `stratification.csv` sha256 **before any call**), run an **independent pre-run stratification critique**
   (it caught `lass`/`prop` mislabels in v2), 30-item billed pre-flight (drop to `durel`-only if it
   projects > $5), run 3,600 calls, **independent post-run verification**, write the result leading with
   the null if N1/N2 hold. This is the cell the grounding nulls *don't* reach (fine polysemy, where text
   may not saturate).
2. **Bridge v2 — non-coercing transitive control (un-gated; new stimuli + one cheap probe).** Settles the
   coercion-v1 sense-vs-surface confound ([`result/coercion-sense-modulation-v1`](wiki/findings/results/coercion-sense-modulation-v1.md)).
3. **Relational pilot** — design is sharpened; needs a fetchable human convergence anchor (see decision
   `relational-fetchable-anchor`) or the ratified C&W-G 1986 fetch. Un-anchored design work is done.
4. **Image probe v2** — a finer/abstract-sense set (where text does *not* saturate) and/or VWSD as a
   genuinely-multimodal anchor; only worth it if v3 or a finer set suggests headroom.

Run `python3 tools/senselint.py` (0 errors) + `python3 tools/linkify.py` before every commit. Claims
modest; **nulls first-class**. New probes import [`experiments/lib/openrouter.py`](experiments/lib/openrouter.py)
(billed `usage.cost`; image-capable via `images=`); **freeze + commit stimuli (sha256) before any probe
call.** **Budget:** $20/week soft; gemini reasoning + image tokens dominate — keep images small/low-detail.
Spent this session ≈ **$0.23** (image probe + liveness).

## Blocked / pending Tom (4 open decisions, all non-blocking — one-liner each)

- [`decisions/open/multimodal-image-anchor`](wiki/decisions/open/multimodal-image-anchor.md) — the image
  probe's realized anchor was a **WordNet-keyed constructed set** (WiC under-covered clean visual
  homonyms). Default A stands; "fine" / "redo with WiC/VWSD" is enough.
- [`decisions/open/cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md) — add a
  `TOGETHER_API_KEY` to unblock the AANN Option-A surprisal (<$1)? Default A (open CAP-1 if Tom adds a key).
- [`decisions/open/relational-fetchable-anchor`](wiki/decisions/open/relational-fetchable-anchor.md) —
  may we catalog the Hawkins tangrams corpus (no SPDX license; authors' "open corpus" statement) under the
  DWUG recipe-not-corpus posture? Default A.
- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — AANN
  held; now paired with `cloud-compute-path` (a real path exists if a key is added).

## Reminder for the next cold-start

Charter `PROJECT.md`; schema `CLAUDE.md`; run discipline `PROTOCOL.md` ("continue working" ⇒ workflow
mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md) first, then `wiki/index.md`**;
reconcile `wiki/decisions/open/` (4 open, all non-blocking). The project is **three-axis**: grammatical
(robust), lexical (a+c supported; b the ready next experiment — **lexical v3**), multimodal/grounding
(**two negatives** — text-side moderation null + image redundancy null; fine polysemy untouched). The
single clearest next unit is **lexical v3** — fully designed, WiC verified, anchor ratified; it is a full
disciplined wave (build+stratify+freeze+critic+3,600-call run+verify), deferred this session only for
context/quality, **not blocked**.
