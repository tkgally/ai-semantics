# NEXT.md

## State

The project is **three-axis**: **grammatical** (live, robust — 11 own-design results), **lexical**
(live: conjecture clauses a+c supported, b a null awaiting a homonymy-enriched anchor), and
**multimodal / physical-AI** (opened 2026-05-30). This session (2026-05-30, **workflow mode**,
branch `claude/dreamy-galileo-u2Ipf`, PR #29) ran the multimodal axis's **first probe-bearing unit**
— the **$0 Lancaster perceptual-grounding moderation** of the existing DWUG lexical result
(prediction 1 of [`conjecture/multimodal-lexical-grounding-divergence`](wiki/findings/conjectures/multimodal-lexical-grounding-divergence.md),
decision Q3 default A, standing delegation). It produced the project's **first `grounded`-tagged
result — a NULL**.

What landed (one full wave + two independent adversarial passes [pre-write critic + post-run
verifier], all fixes applied):

1. **Anchor fetched + catalogued.** The **Lancaster Sensorimotor Norms** (Lynott et al. 2020,
   **CC BY 4.0**) aggregate CSV downloaded + **sha256-pinned** (OSF `rwhs6`/`48wsc`,
   `445d363f…`; full CSV gitignored, derived 42-lemma join table committed). New typed resource
   [`resource/lancaster-sensorimotor-norms`](wiki/base/resources/lancaster-sensorimotor-norms.md).
   42/43 DWUG EN lemmas covered (`lass` absent).
2. **The result — a NULL** ([`result/lexical-perceptual-grounding-moderation-v1`](wiki/findings/results/lexical-perceptual-grounding-moderation-v1.md)).
   A word's perceptual groundedness (`Max_strength.perceptual`) does **not** predict how well a
   text-only model tracks its graded DWUG senses. Pre-registered primary cells (durel × 3 models):
   every Δρ = ρ_HIGH − ρ_LOW negative (−0.05 / −0.27 / −0.04); the lone CI excluding zero
   (gpt-5.4-mini, −0.27) runs the **wrong** way. Confounds (pairs/lemma, annotator-count, spread)
   all clear; **inherently underpowered** (21 lemmas/side, compressed range 2.44–4.95) → null reads
   as "no detectable moderation OR unresolvable," not a falsification. **Lowers the prior** on the
   image predictions (2–4) per the conjecture's own null clause; does **not** reach the image-vs-text
   *redundancy* null (that needs an actual image probe). Cost **$0.00**.
3. **Discipline.** Inputs frozen (sha256) before any model-rating × perceptual quantity; independent
   pre-write critic caught a normalization **BLOCKER** (fixed pre-run) + forced the power /
   collinearity (perceptual≈visual ρ 0.85) / multiple-comparison disclosures + an n≥3 robustness pass;
   independent post-run verifier reproduced **every** figure to ±0.0001. `PREREG.md` + run record in
   [`experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/`](experiments/runs/2026-05-30-lancaster-perceptual-moderation-v1/README.md).

## Next concrete action (backlog — pick by Tom's decision or run un-gated units)

The cheapest high-value $0 multimodal unit is **done**. The next multimodal step (the genuine image
probe) is **gated on a value-laden Tom decision** (Q3-B); the rest of the standing backlog is un-gated
but needs **new API spend**.

1. **Multimodal predictions 2–3 — the first IMAGE probe (genuinely multimodal; new spend). GATED.**
   (a) A liveness ping through the now-image-capable harness (tiny synthetic image + "what colour?",
   all 3 models; ~$0.001; freeze the 1-line stimulus + sha256). (b) An image-paired graded-sense set
   (target words depicted in two usages, with genuinely cross-sense, visually-distinct homonym pairs)
   rated with vs without the image, against a human sense signal. **Needs Tom's Q3-B** (opening the
   image-input probe is the surfaced, value-laden direction-setting call) + a new design doc + budget
   + an image anchor (THINGS-data, CC0, scouted). The prediction-1 null *lowered* the prior on this
   but did **not** falsify it — the word-level Lancaster proxy is blunter than prediction 3's
   *sense-level* perceptual-distinguishability moderator, so a sharp image test is still warranted.
2. **Bridge v2 — non-coercing transitive control (un-gated; new stimuli + one cheap probe).** Settles
   the coercion-v1 sense-vs-surface confound ([`result/coercion-sense-modulation-v1`](wiki/findings/results/coercion-sense-modulation-v1.md)).
   The cleanest un-gated runnable unit (governed by ratified gates, internal-contrast-only).
3. **Lexical v3 — homonymy-enriched anchor (un-gated; needs a new graded set with matched cross-sense
   homonym/polysemy pairs + new API).** The clean clause-(b) test the DWUG-EN null
   ([`result/lexical-polysemy-homonymy-v2`](wiki/findings/results/lexical-polysemy-homonymy-v2.md))
   pointed to. (Multimodal prediction 3 is a second route to the same question, via vision.)
4. **WiC binary cross-check** (conjecture prediction 5; needs WiC fetched + a cheap probe).
5. **AANN small-model lane** (held by Tom — needs local compute). **Relational pilot** — needs Clark &
   Wilkes-Gibbs 1986 fetched (Tom's library) + a multi-agent-LLM literature read.

Run `python3 tools/senselint.py` (0 errors) + `python3 tools/linkify.py` before every commit. Claims
modest; **nulls first-class**. New probes import [`experiments/lib/openrouter.py`](experiments/lib/openrouter.py)
(billed `usage.cost`; image-capable via `images=`); **freeze + commit stimuli (sha256) before any
probe call.** **Budget watch:** gemini reasoning + image tokens dominate multi-call cost — keep images
small/low-detail.

## Blocked / pending Tom (3 open decisions, all non-blocking)

- [`decisions/resolved/multimodal-panel-and-grounding-theory`](wiki/decisions/resolved/multimodal-panel-and-grounding-theory.md)
  — **direction-setting, non-blocking.** Q1 panel (default A: existing 3-family, image first), Q2
  grounding theory (default A: Lyre gradual + `grounded.perceptual`, Harnad/Barsalou as foils), Q3
  anchor class (default A = the Lancaster $0 moderator, **now DONE → null**; **B = the THINGS image
  probe, the live next call**; C = hold multimodal for text lexical v3). With Q3-A done, the live
  question is **whether to open the image probe (Q3-B) now** — the value-laden call. A one-liner each
  is enough.
- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) —
  AANN held (Tom's call); clean path needs local compute. Not blocking.
- [`decisions/resolved/conflicting-cue-human-anchor`](wiki/decisions/resolved/conflicting-cue-human-anchor.md)
  — low-priority; pending human anchor for internal-contrast-only off-ceiling/bridge results. A
  one-liner closes it.

## Reminder for the next cold-start

Charter `PROJECT.md` (purpose/modesty §1/§2); schema `CLAUDE.md`; run discipline `PROTOCOL.md`
("continue working" ⇒ workflow mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md)
first, then `wiki/index.md`**; reconcile `wiki/decisions/open/` (3 open, all non-blocking). The project
is **three-axis**: grammatical (live, robust), lexical (a+c supported, b a null), multimodal (base
layer + first conjecture + feasibility + **now the first `grounded`-tagged result, a $0 NULL**). The
harness is image-capable but **no image probe has run yet** — the panel is verified able to take
images; opening that probe is the surfaced Q3-B decision. The next un-gated new-spend unit is
**bridge-v2**.
