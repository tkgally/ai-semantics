# Pre-run critic — independent fresh-agent review (s215, VERDICT AUTHORITY)

Independent fresh agent (general-purpose), not the design author, audited the **first** frozen
instrument (`items.csv` sha `2d212d92…`) with its own Japanese competence. Verbatim verdict + review
below. It weighed against the non-Anthropic decorrelation vote
([`VOTE-critic-s215.json`](VOTE-critic-s215.json), `gpt-5.4-mini`, NO-GO). Reconciliation: the
verdict-authority GO governs (German-s213 precedent: proceed over a non-Anthropic NO-GO on reasoned
grounds); the vote's one substantive point (a few cc-inverse consequents decrease the named scale
indirectly) was **honored** via condition **C1** — 4 cc-inverse consequents made explicitly
scale-decreasing, gold unchanged, re-frozen to `31597d29…` before any probe call (see the design page's
*Pre-run critic outcome + applied condition (C1)*).

---

## VERDICT: GO

The frozen instrument is grammatically sound, the gold is internally consistent and construction-correct,
the anti-cheat freeze verifies, and the source page is honestly framed. No blockers and no gold errors.

**A. Japanese grammatical fidelity — PASS.** All 34 antecedents `[Pred-ば][Pred]ほど` well-formed
(i-adjectives; na-adjectives field `平らであればあるほど` / kitchen `きれいであればあるほど`; verbs balloon
`光れば光るほど` / pinecone `べたつけばべたつくほど`). All 34 cc-inverse consequents genuinely decrease the
named dim2 (roman 飽きっぽく→辛抱強さ↓, startup 大胆に→慎重さ↓, clinic 目が冴えた→眠気↓, theater 静かに→
ざわめき↓, curry 無口に→おしゃべり↓, current 落ち着いた→苛立ち↓, hall おとなしく→盛り上がり↓, lampshade
甘く→酸っぱさ↓, stapler 淡く沈んだ→明るさ↓; none ambiguous enough to make gold wrong). Controls genuinely
lack 〜ば〜ほど (ctrl-two = two independent declaratives; ctrl-single = one より-comparative on dim1,
dim2 absent) → undetermined correct. No item ungrammatical or misreading-prone enough to corrupt the
measurement.

**B. Gold consistency — PASS.** Machine cross-tab: 34 cc-positive→increase/0, 34 cc-inverse→decrease/2,
34 ctrl-two→undetermined/1, 34 ctrl-single→undetermined/1. Zero deviations. NLI gold normatively correct.

**C. Instrument/probe — PASS (minor notes).** FC_SYS/NLI_SYS accurate; NLI hypothesis frames both scales
in rising sense (required for cc-inverse=contradiction); parsing sound (増加|減少|不明 share no
characters; NLI last-digit [012]; no Arabic digits in stimuli). Out-of-vocab correct answers parse to NA
(conservative), monitored via fc_na/nli_na — identical to English/German arms.

**D. Anti-cheat — PASS.** Live `sha256(items.csv)` matched the design Freeze block exactly; gold fixed in
`build_items.py` before any call; thresholds frozen, "do not retune" stated; verdict frame symmetric,
null first-class.

**E. Fabrication / source honesty — PASS.** `japanese-ba-hodo-cc.md` form facts are standard correct
Japanese grammar; verbatim examples correct; "verified firsthand + academic sources located-not-read"
framing accurate and not over-claiming; correctly disclaims frequency/acquisition/human-processing and
not-a-human-anchor.

**F. Smoke items — PASS (one minor note).** 12 genuinely non-CC items (と-conditionals / plain
declaratives), balanced 5 increase / 4 decrease / 3 undetermined, gold correct; `sun` is the softest but
the ≥10/12 gate tolerates one soft item.

**Minor non-blocking notes (no fix required):** `値段/頻度/雑談 が増す` slightly less idiomatic than
上がる/増える (held constant with the English/German "increases" template); summer 酸っぱい / stapler 淡く
沈んだ antonym-mapping is defensible but the least direct (→ addressed by C1); FC ordering slightly loose
but clear; pool 長く泳いだ faintly duration/distance-ambiguous, reads as distance in context.
