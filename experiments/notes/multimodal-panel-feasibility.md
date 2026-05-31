# Multimodal panel & harness feasibility (2026-05-30)

Un-gated feasibility scouting for the new **multimodal / physical-AI meaning** axis
(see `wiki/findings/conjectures/` multimodal conjecture and
`wiki/decisions/resolved/multimodal-panel-and-grounding-theory`). The driving question
for the axis: *do multimodal (vision-language) models interpret lexical/grammatical
meaning differently from text-only models?* Before any probe can run we must know
(a) which multimodal models are reachable through the existing OpenRouter harness,
(b) at what cost, with what image-input support, and (c) whether the harness code can
send images at all. This note records that check. It is **infrastructure scouting,
not a finding** — no meaning-claim is drawn here.

## Headline: image input is fully available on the existing decorrelated panel — NO model-family swap needed

This is the **opposite** of the blocker the AANN logprob path hit
(`wiki/decisions/open/aann-panel-logprob-blocker` — only 2 of the panel families
expose logprobs, killing the 3-family decorrelated logprob design). For **image
input**, all three *current* panel families already accept images. The project can run
its first multimodal probe with the **same three-lab decorrelated panel** it uses for
every text probe — preserving family decorrelation (charter §6) across the text↔
multimodal comparison, which is exactly what a clean text-only-vs-VLM contrast wants
(same model families, modality toggled).

## Method

Free GET to `https://openrouter.ai/api/v1/models` (no completion call, $0), 2026-05-30,
filtering `architecture.input_modalities` for `"image"`. 355 models listed; 165 accept
image input. The three current panel slots (`config/models.md`, "Current panel
2026-05-28"):

| Slot | Model | `input_modalities` (verbatim from catalog) | prompt $/Mtok | completion $/Mtok |
|------|-------|---------------------------------------------|---------------|-------------------|
| A | `anthropic/claude-sonnet-4.6` | `text, image, file` | 3.00 | 15.00 |
| B | `openai/gpt-5.4-mini` | `file, image, text` | 0.75 | 4.50 |
| C | `google/gemini-3.5-flash` | `text, image, video, file, audio` | 1.50 | 9.00 (img 1.50) |

Notes:
- **Gemini (slot C) is the broadest**: it lists `audio` and `video` input too, so the
  "where tractable audio/embodied" part of the axis has a single-model on-ramp via the
  *same* harness — but only one of three families would carry audio/video, so an
  audio/video probe would **not** be family-decorrelated (single-model, lower evidential
  weight). Image is the only modality all three families share. **Privilege image first.**
- Image cost on Anthropic/OpenAI is folded into input-token count (catalog `image: None`
  means no separate per-image line item — images are tokenized into the prompt); Gemini
  bills a small separate per-image-token rate (`img 1.50/Mtok`). All three are cheap
  enough that a ~100-item × 3-model image probe is well within the $20/mo budget — image
  *tokens* dominate, so keep images small (see below).

## Harness status

`experiments/lib/openrouter.py` was **text-only** (sent `messages[].content` as a plain
string). Extended 2026-05-30 (this session, un-gated infrastructure): `call()` now takes
an optional `images=` list. When `images` is None the user turn is sent as a plain string
— **byte-for-byte identical to prior behaviour**, so every existing text probe is
unchanged and reproducible. When images are present, the user turn is built as the
OpenAI/OpenRouter multimodal content array (`[{type:text,...}, {type:image_url,
image_url:{url:...}}, ...]`). Each `images` element is either a URL string
(`https://…` or a `data:image/png;base64,…` data URI) or `{"url":..., "detail":...}`.

**Not yet liveness-verified.** The catalog confirms the *modality* is accepted; it does
NOT prove our specific request shape round-trips. The first runnable multimodal action is
a **liveness ping** (see below) before any finding-bearing probe.

## Carry-over caveats (from `config/models.md` + the text probes)

1. **Reasoning-token consumption.** Gemini (and alternates) burn the visible-output
   budget on reasoning tokens under a small cap → set `max_tokens` ≥ 1024 for gemini
   (the harness already defaults google/* to 4096). Budget watch: gemini reasoning
   tokens dominate multi-call cost — this was true for every text probe and will be
   true here, *plus* image tokens.
2. **Image tokens are the new cost driver.** A high-detail image can cost hundreds–
   thousands of prompt tokens per call × 3 models × N items. Use the smallest image that
   preserves the contrast under test (downscale; `detail:"low"` where the contrast does
   not need fine pixels); estimate before committing a run.
3. **Family decorrelation holds for image, not for audio/video.** Keep the headline axis
   on image so all three families participate.

## Recommended first runnable multimodal probe (the handoff)

1. **Liveness ping (infrastructure, ~\$0.001, not a finding).** Send each panel model one
   tiny synthetic image (e.g. a solid-colour PNG as a base64 data URI) + "what colour is
   this image?" Confirm all three return a sensible answer through the extended harness.
   Freeze the 1-line stimulus + sha256 first per probe discipline, even though it is
   plumbing.
2. **Then the first finding-bearing probe**, per the multimodal conjecture's wedge
   (`wiki/findings/conjectures/` + its design doc): the cleanest first contrast is the
   **text-only-vs-image-grounded graded sense / compositionality** wedge — the same
   DURel-style graded-relatedness instrument the lexical program already validated
   (`result/lexical-sense-gradience-v1`), run with vs without a disambiguating image,
   against a human-anchored multimodal resource (see
   `wiki/base/resources/multimodal-anchor-scouting.md`). Build + freeze + sha256 stimuli,
   ≥1 adversarial pre-run critique, ≥1 post-run number-verification, per `PROTOCOL.md` §5.

## What is NOT resolved here (surfaced to Tom)

The *choice of multimodal model panel* (keep the existing 3 vs add a VLM-specialist family)
and *which grounding theory to privilege* (Harnad symbol-grounding vs Barsalou perceptual
symbols vs Lyre gradual-grounding) are value-laden / direction-setting and are surfaced in
`wiki/decisions/resolved/multimodal-panel-and-grounding-theory`, not self-resolved. This note
establishes only the *capability* fact: the existing panel CAN take images.
