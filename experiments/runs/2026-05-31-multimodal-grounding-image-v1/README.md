# Run: 2026-05-31 multimodal-grounding-image-v1 (the project's FIRST image-input probe)

Operationalizes predictions 2–3 of `conjecture/multimodal-lexical-grounding-divergence`:
does showing a small picture depicting each usage move the panel's graded sense-relatedness
behavior **toward** the binary human sense signal, **keyed to where the two senses are
visually distinct**? Design: `experiments/designs/multimodal-grounding-image-v1.md`.

- **Anchor (realized):** constructed minimal pairs keyed to **Princeton WordNet** synsets
  (Tom-authorized option b; WiC's items under-covered clean visual homonyms — see PREREG).
  Claims scoped to the **binary** same/different-synset signal. Image = designed manipulation.
- **Stimuli:** 12 word pairs (6 distinct-homonym F + 6 same-sense T) × 2 conditions
  (text-only / image+text) × 2 framings (DURel 4-pt, 0–100) × 3 models = 144 calls.
- **Images:** 24, Wikimedia Commons PD/CC0/CC-BY(-SA), downscaled ≤256px q40, sha256-frozen
  (PREREG.md). Sources/licenses in `manifest.json` + `ATTRIBUTION.md`. Contact sheet:
  `contact_sheet.png` (visually verified before freeze).
- **Discipline:** stimuli frozen + committed BEFORE any model call; independent pre-run
  critique + post-run number-verification (PROTOCOL §5).

See `PREREG.md` for the frozen indicators/nulls. Result → `result/multimodal-grounding-image-v1`.
