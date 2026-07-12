# PRE-RUN CRITIC — German CC replication design, session 213

**Fresh-agent adversarial pre-run critic** (verdict authority, independent of the design author),
with a **non-Anthropic decorrelation vote** (`gpt-5.4-mini`, $0.003569,
[`VOTE-critic-s213.json`](VOTE-critic-s213.json)) routed as QA input and weighed.

## VERDICT: GO-WITH-CONDITIONS

The design is sound, faithfully ported, honestly scoped, anti-cheat-clean. Grammar and gold labels
correct throughout. One genuine defect in the competence gate (C1) required a $0 pre-run fix
(smoke.py is not under the freeze sha and runs before any model call).

## Per-check findings
- **Grammaticality — PASS (all 34 pairs).** Every `je`-clause verb-final; every `desto`-clause
  verb-second, including subject-fronted (`desto mehr Kunden kamen`), object-fronted
  (`desto mehr Bahnen schwammen die Schwimmer`), adverb-fronted (`desto mehr goss der Gärtner`), and
  the separable verb (`desto größer fiel die Ernte aus`). Marked-but-grammatical items (`gestreifter`,
  `zerknitterter`, `niedriger ragte`) within tolerance (mirror the English instrument's atypical awkwardness).
- **Gold-correctness — PASS (all 136, hand-verified not sampled).** All cc-positive → increase/NLI 0;
  all cc-inverse → decrease/NLI 2 (every antonym-based inverse checked: `ungeduldiger`→Geduld↓,
  `saurer`→Süße↓, `wacher`→Schläfrigkeit↓, `ruhiger`→Unruhe↓, `stiller`→Gesprächigkeit↓,
  `lustloser`→Begeisterung↓, `gelassener`→Frustration↓, `gesitteter`→Ausgelassenheit↓, `blasser`→Helligkeit↓,
  `süßer`→Säure↓, `flacher`→Tiefe↓, `unvorsichtiger`→Vorsicht↓); all 68 controls → undetermined/NLI 1;
  no control secretly directional.
- **Anti-cheat — PASS.** `sha256(items.csv)` + `sha256(freq_control.json)` recomputed byte-identical to
  the PREREG/design; both committed (f583b4c) before any probe; `raw/` empty; gold fixed in
  `build_items.py` before generation; thresholds demoted to continuity-only, deliverable is point+CI.
- **Instrument fidelity — PASS.** probe/analyze/panel/temperature/max_tokens/parsing/bootstrap
  byte-parallel to the English powered instrument; German answer vocab maps back to language-neutral
  labels. Only the target language changes.
- **Q2-B adequacy — ACCEPTABLE, honest (not a dodge), with a noted limitation.** The reframe (frozen
  covariate + typical/atypical split as the primary co-occurrence control) is correct and documented.
  **Limitation (→ C2):** the automatic lemma resolver has form→noun collision noise (copula surface
  `waren`/`war`→content noun `Ware`; `vertrauten`→`Vertraute`; `Start-ups`→`Start`), inflating some
  freq/co-occurrence counts; bounded, symmetric across typical/atypical, frozen, feeds only a
  corroboration Spearman — state plainly on the result page, do not present the covariate as clean.
- **Smoke-test — DEFECT (→ C1, FIXED).** 2 of 12 smoke items (`laerm`, `uebung`) were themselves
  `je…desto` CC constructions, contaminating the gate's isolation-from-the-construction-under-test.
  **Fixed pre-run** (s213): replaced with non-CC explicit-content items (`Als … lauter wurde …`;
  `Weil … länger trainierte, sank …`), verified no residual `je/desto/umso` in any smoke item.
- **Instrument-language — SOUND.** All-German scaffolding well-justified; smoke gate is the designated
  guard for the metalanguage-competence risk; English-scaffolding pre-named as the sensitivity check.
- **Claim scope — HONEST, pre-registered.** internal-contrast-only; within-model; explicitly *partial*
  discharge; symmetric verdict frame with a null first-class + a do-not-retune rule. Honors i–ix.

## Fabrication check — CLEAN
No fabricated quote/citation. `source/meinunger-2023-je-desto` verifies exactly against Cambridge Core
(title, author André Meinunger, *Journal of Germanic Linguistics* 35(2):148–204, 2023, DOI
10.1017/S1470542722000101, the "regular verb-second structures" claim); the page is scrupulously hedged
about provenance depth (abstract-level scholarly + verbatim pedagogical grammar).

## Conditions the run honors
- **C1 (required, DONE pre-run).** Replaced the two CC smoke items with non-CC explicit-content items.
- **C2 (documentation, at write-up).** State the freq_control lemma-resolution noise plainly; keep Q2-B
  framed as a bounded corroboration covariate, typical/atypical split the primary co-occurrence control.
- **C3 (standing).** On null/attenuation honor the no-retune rule (investigate authoring/competence, not
  thresholds); on replication keep the partial-discharge / internal-contrast-only scope.
- **C4 (budget).** Record actual `usage.cost` for 36 smoke + 816 main calls vs the $0.15–0.30 pre-flight;
  stop if the smoke gate is NO-GO.

## Weighing the non-Anthropic vote
Strong convergence on the two highest-risk axes (German grammaticality; gold correctness incl. cc-inverse).
Divergence: the vote missed that 2 smoke items were CC constructions — added as required condition C1
(now fixed). Net: same verdict (GO-WITH-CONDITIONS), one additional load-bearing condition.
