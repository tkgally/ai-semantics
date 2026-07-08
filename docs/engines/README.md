# Music Engines

Two self-contained, browser-based **generative-music engines**. Each one composes a fresh
piece from a text *seed* and performs it live with the Web Audio API — **no samples, no
external libraries, no network calls**. Open any `.html` file directly in a browser (or start
at [`index.html`](index.html) for the gallery) and press play.

| # | Engine | Style | File | Version |
|---|--------|-------|------|---------|
| 01 | **Tonal Classical** | through-composed chamber miniature | [`engine-01-tonal-classical.html`](engine-01-tonal-classical.html) | v0.2.0 |
| 02 | **Lo-Fi Chillhop** | swung, looping boom-bap beat | [`engine-02-lofi-chillhop.html`](engine-02-lofi-chillhop.html) | v0.1.0 |

Every engine is deterministic: the same seed + settings always produce the same piece. Each has
a feedback panel that exports a small JSON object (rating + comment + the settings that produced
the take) so listening notes can be captured and fed back into the next version.

---

## Engine 01 — Tonal Classical (v0.2.0)

A miniature for a small chamber ensemble: a singing melody over an Alberti / broken-chord
accompaniment and a bass line, using diatonic harmony and functional cadences, in an
**intro + rounded ternary (A B A′) + coda** shape. The A material literally returns in A′
(lightly ornamented), which is what makes it read as *composed* rather than random.

### What changed from v0.1.0 (the feedback)

The first take was rated 3/5 with three specific notes. All three are addressed:

1. **"Faint static / clipping … at the end of the very last note."**
   The audio path is now click-free *by construction*:
   - No `exponentialRampToValueAtTime(0, …)` anywhere (ramping a gain to exactly zero is the
     classic Web Audio click). Every note's release decays toward a −80 dB floor via
     `setTargetAtTime`, and its oscillators are **stopped only after they are inaudible**.
   - A master **limiter** (`DynamicsCompressor`) plus headroom keeps summed voices from clipping.
   - The whole piece ends on a gentle **master fade** across the reverb tail, so the final note
     can never be truncated into a click.

   Verified by rendering the full piece through an `OfflineAudioContext` and analyzing the
   samples: peak stays ≈ 0.32 (no clipping), the largest sample-to-sample step in the entire
   render is ≈ 0.02 (no discontinuities), and the final 100 ms is exactly silent.

2. **"Articulation / timing … sounds mechanical. More humanness."**
   The performance layer is now humanised (all seeded, so still deterministic):
   - **Micro-timing** jitter per note, reduced on strong beats.
   - **Velocity shaping**: metric accents (downbeats lean in), a raised-cosine **phrase arc**,
     and agogic emphasis on longer notes.
   - **Rubato**: the tempo eases at phrase ends, with a real **ritardando** through the coda.
   - **Articulation** varies (legato melody vs. lighter, detached accompaniment).
   - **Chords are rolled** a few milliseconds rather than struck dead-flat.
   - Gentle **vibrato** eases in on longer melody notes.

3. **"Quite slow at the starting tempo."**
   Default tempo is now **132 bpm** (was 118), with a wider slider range and livelier
   sixteenth-note accompaniment figures.

### Controls
`seed · tempo · mode (major/minor) · tonic · reverb · volume`

---

## Engine 02 — Lo-Fi Chillhop (v0.1.0)

The deliberate contrast to Engine 01. Where the classical engine is through-composed with
rubato, this one **grooves and loops**:

- **Synthesized drums** — kick (pitch-swept sine + beater click), a soft dusty snare
  (noise + tonal body), and hats — no samples.
- A warm **electric-piano** (Rhodes-ish: sine + fast bell "tine" + tremolo + tape wobble)
  comping **jazz 7th / 9th voicings**.
- A round **sub-bass** with syncopated pushes and approach notes into each chord.
- **Vinyl crackle** — continuous hiss + seeded pops baked into one looping buffer.
- Groove is carried by **swing** (shuffled off-beats), **laid-back timing** (snare and keys
  sit slightly behind), and a **sidechain pump** that ducks the music bus on each kick.
- A master low-pass gives the muffled lo-fi warmth; the same limiter + tail-fade discipline as
  Engine 01 keeps it click- and clip-free.

Arrangement: `intro → loop A → B (brighter, with a fill) → A → outro`.

### Controls
`seed · tempo · mood (mellow/warm) · root · swing · vinyl · reverb · volume`

---

## Feedback JSON

Each engine's **Copy / Download feedback JSON** button emits an object like this (Engine 01):

```json
{
  "engine": "tonal-classical",
  "version": "0.2.0",
  "seed": "tvc4pn",
  "bpm": 132,
  "mode": "major",
  "tonic": "C4",
  "reverb": 0.28,
  "volume": 0.62,
  "rating": "4",
  "comment": "…",
  "form": "intro + rounded ternary (A B A′) + coda",
  "key": "C major",
  "submittedAt": "2026-07-08T04:00:00.000Z"
}
```

Engine 02 uses the same shape and adds its groove-specific fields (`swing`, `vinyl`); its `mode`
is `mellow` / `warm` and `tonic` is a pitch class (e.g. `"C"`).

---

## Notes

- **Determinism.** A seed fully determines the composition *and* the humanised performance
  (composition and performance use separate seeded PRNG streams derived from the seed).
- **Browser support.** Any modern browser with the Web Audio API. Audio starts on the first
  play click (a user gesture), per browser autoplay rules.
- **No dependencies.** Everything — synthesis, reverb impulse response, and vinyl texture — is
  generated at runtime; each file is fully offline-capable.
