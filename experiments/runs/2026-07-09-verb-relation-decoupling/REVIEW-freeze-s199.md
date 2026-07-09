# REVIEW — s199 FREEZE, verb-relation decoupling probe (2026-07-09)

Pre-run FREEZE check (PROTOCOL §A3) of the FROZEN artifacts (built before any model call): an
**independent fresh-agent freeze critic (verdict authority)** + one **non-Anthropic decorrelation vote**
(`panel.B`, via the probe REST path — QA input, not authoritative). The gates are already ratified
(s199, Q1-C/Q2-A/Q3 internal-contrast-only); this checks that the frozen code + numbers honor the
anti-cheat fence and the ten binding conditions (seven design-page + B1–B3).

## Verdict: GO (spend ~$0.40 on the run). The non-Anthropic NO-GO is OVERRULED on the merits.

The fresh-agent critic (verdict authority) re-ran `prep.py` (reproduced byte-identical: sha256 match;
per-relation N 130/130/130/130/130/126; B1 CORE-4 range 0.277, `depth_degenerate=true`), independently
recomputed the 1,740-lemma prior union (0 overlap, all 6 relations, case-sensitive + lowercased),
confirmed `_assert_frozen_g2()` passes (byte-identical G² vs s193; the s193 source hash in
`FREEZE-HASHES.json` matches the live file), confirmed every threshold is a frozen module constant read
by `analyze.py` from the frozen files (no threshold derived from model output), and confirmed the frozen
control cue-strength reproduces PREREG exactly (antonymy 0.0923 / troponymy 0.0487 / synonymy 0.0308 /
hypernymy 0.0207 / cause 0.0106 / entailment 0.0051). **No anti-cheat leak.**

## The non-Anthropic freeze vote — NO-GO (weighed, disclosed, overruled)

`panel.B` (`openai/gpt-5.4-mini`, $0.003033) returned **NO-GO**, its central concern that defining the
B1 degeneracy bound on the **CORE-4** non-antonymy set — which excludes the mechanically-included shallow
`cause` — is "borderline cherry-picking" and "too easy to game in presentation." Secondary points: the
Hearst-arm drop is a "material design subtraction"; the byte-freeze is "asserted, not auditable"; the
disjointness needs a frozen normalization rule. Full text in [`vote-freeze.txt`](vote-freeze.txt).

**Overruled, on the merits (fresh-agent critic):**

1. **Direction is anti-gaming, not gaming.** CORE-4 range 0.277 < 0.50 → DEGENERATE → H2 under-powered
   **symmetrically** (B2). The cause-inclusive range 0.741 would be NON-degenerate. Excluding `cause`
   therefore makes a potential **DEPTH-OUT-PREDICTS (a verb confirmation of the noun mechanism) get
   flagged under-powered and NOT banked** — i.e. it makes a *confirming* H2 result look **WEAKER**. A
   gaming move maximizes apparent strength; this minimizes it. Conservative, not self-serving.
2. **CORE-4 is the ratifier's stated B1 verbatim** — "a floor on the non-antonymy **4-relation** depth
   range." The 5-relation core is {antonymy, synonymy, hypernymy, troponymy, entailment}; non-antonymy-4
   = the CORE-4 backbone. `cause` is the conditional sixth, deliberately outside the fixed backbone, so a
   shallow mechanically-included `cause` cannot manufacture non-degeneracy.
3. **The timeline is legitimate.** The lead first computed the range over all non-antonymy relations
   (incl. cause) → 0.741, then switched to CORE-4 → 0.277 **to align with the ratified written
   definition**, moving the verdict toward MORE-conservative/under-powered. Aligning to the ratifier's
   condition in the anti-gaming direction is correct behavior, not cherry-picking.
4. **Transparency adequate.** `items.json` + PREREG record all three numbers (verdict-driving CORE-4
   0.277, cause-inclusive 0.741, full-set SD 0.304) and name the driver.
5. **Hearst-drop is a RATIFIED Q2-C structural exclusion**, pre-registered — not a post-hoc subtraction.
6. **Auditability now airtight.** `FREEZE-HASHES.json` pins sha256 of all 9 frozen artifacts + the s193
   source; byte-freeze is a **computational-identity** assertion (stronger than a text diff); disjointness
   uses the same lowercased single-word normalization the pipeline uses, against the exact frozen lists.

## Conditions to honor at result-writing (not blockers)

- **B2 in prose:** whatever H2 returns (DEPTH-FAILS or DEPTH-OUT-PREDICTS), report it **under-powered**
  and never as noun-equivalent (analyze.py sets this automatically from the frozen flag; keep it in prose).
- **B3 framing:** present DECOUPLING-REAPPEARS as one point in a three-point pattern; no unqualified
  "decisive"/"isolates hierarchy" on the produced pages.
- **Carry the construct caveats:** all-sense gold vs first-synset depth; hypernymy gold-size confound
  (median 10 vs antonymy 1); corpus-as-pretraining-proxy.
- **Git anchor:** commit the frozen artifacts before/with the run so the freeze has a git anchor (done).
