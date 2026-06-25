---
type: source
id: frege-1892-sense-and-reference
title: Über Sinn und Bedeutung (On Sense and Reference)
authors:
  - Frege, Gottlob
year: 1892
venue: "Zeitschrift für Philosophie und philosophische Kritik, N. F., Bd. 100/1 (1892), S. 25–50"
url: https://www.deutschestextarchiv.de/frege_sinn_1892
access: public-domain
meaning-senses:
  - referential
  - referential.sense
  - referential.reference
  - constructional
status: received
created: 2026-06-25
updated: 2026-06-25
links:
  - rel: supports
    target: concept/truth-conditional-and-use-meaning
  - rel: supports
    target: concept/compositionality
  - rel: supports
    target: concept/referential-meaning
---

# Frege 1892 — Über Sinn und Bedeutung (On Sense and Reference)

## What it is

Gottlob Frege's 1892 essay "Über Sinn und Bedeutung," published in the *Zeitschrift für Philosophie und philosophische Kritik*, Neue Folge, Band 100, Heft 1 (1892), pp. 25–50. It is the founding text of the **sense/reference** distinction (`Sinn`/`Bedeutung`) and a root of the truth-conditional tradition in semantics: it argues that an expression carries both a *reference* (`Bedeutung` — the object it picks out) and a *sense* (`Sinn` — the "Art des Gegebenseins," the mode of presentation of that object), that two expressions may share a reference yet differ in sense, that the **reference of a declarative sentence is its truth-value** while its **sense is the thought (`Gedanke`)** it expresses, and that reference is preserved under substitution of co-referring parts (the seed of compositionality). It is a primary philosophy-of-meaning text — **not** a human-labeled empirical resource, and so **not a human anchor**: it grounds the *theory* the project's concept pages characterize, never a result about any model.

Before this page, [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md) and [`concept/compositionality`](../concepts/compositionality.md) both cited Frege 1892 only as "(not in-repo; characterization)." This page is the in-repo primary those two concept pages can now point at for the `Sinn`/`Bedeutung` distinction, the truth-value-as-reference move, and the part-to-whole substitution principle.

## Provenance

The full German text was fetched on **2026-06-25** from the **Deutsches Textarchiv (DTA)** edition (https://www.deutschestextarchiv.de/frege_sinn_1892), a validated diplomatic transcription of the journal original. The DTA page is JavaScript-gated; the plain-text export was downloaded with `curl` (setting the `verified=1` cookie the site sets via script) from `https://www.deutschestextarchiv.de/book/download_txt/frege_sinn_1892`, and every quote below was matched character-for-character against that extracted text.

**Pagination and orthography.** The DTA text carries inline page markers of the form `[journal/image]` — e.g. `[25/0021]` marks the start of journal page 25 (the article's first page), `[29/0025]`, `[34/0030]`, etc. The locators below are the **original journal page numbers** (25–50) read directly from those markers, which match the conventional citation pagination. The transcription is **diplomatic**: it preserves the 1892 Fraktur orthography, including the **long-s `ſ`** (so "Sinn" appears as "Sinn" but "iſt", "ſein", "Bedeutung der Beſtandtheile", etc.) and the soft-hyphen mark `¬` at line breaks. Quotes below are reproduced **verbatim from the DTA text including the long-s `ſ`**; where a line-break hyphen `¬` falls inside a quoted span it has been silently closed up (the only normalization applied), and that is flagged. A modern-orthography gloss (ſ→s) is given alongside each quote so a reader need not parse Fraktur.

**Access / license.** The *work itself* is **public domain** (Frege died 1925; published 1892). The DTA transcription is released by the Deutsches Textarchiv (BBAW) under a CC license for the markup/edition; the underlying text is PD. Access status is recorded as `public-domain` for the work. No English translation is quoted here: the standard English renderings (Max Black; Geach & Black, *Translations from the Philosophical Writings of Gottlob Frege*, 1952) are **likely still in copyright**, so to stay safe this page **quotes only the PD German original and supplies the project's own glosses** rather than reproducing a copyrighted translation. The glosses are this page's paraphrase, not a quoted published translation.

## Key passages (verbatim German, with journal-page locators and own-gloss)

### 1. The puzzle: `a=a` vs. `a=b` and the Morning-/Evening-Star problem (p. 25)

The essay opens on identity (`Gleichheit`, which Frege uses for `Identität`), and the cognitive-value gap between `a=a` and `a=b`. (Long-s preserved; one `¬` line-break hyphen in "Er¬/kenntnis" closed up.)

> "a=a und a=b ſind offenbar Sätze von verſchiedenem Erkenntniswerte: a=a gilt a priori und iſt nach Kant analytiſch zu nennen, während Sätze von der Form a=b oft ſehr wertvolle Erweiterungen unſerer Erkenntnis enthalten und a priori nicht immer zu begründen ſind." (p. 25)

*Gloss:* "a=a and a=b are evidently sentences of differing cognitive value: a=a holds a priori and, after Kant, is to be called analytic, whereas sentences of the form a=b often contain very valuable extensions of our knowledge and cannot always be established a priori." This is the problem the sense/reference distinction is introduced to solve.

### 2. Sense as "Art des Gegebenseins" (mode of presentation) (pp. 26–27)

Frege locates the difference between `a=a` and a true `a=b` not in the object but in *how the object is given* by the sign — and names that the **sense** of the sign:

> "Eine Verſchiedenheit kann nur dadurch zu Stande kommen, daß der Unterſchied des Zeichens einem Unterſchiede in der Art des Gegebenſeins des Bezeichneten entſpricht." (p. 26)

*Gloss:* "A difference [in cognitive value] can come about only through the difference of the sign corresponding to a difference in the mode of presentation [`Art des Gegebenseins`] of the thing designated."

He then introduces the term `Sinn` for this:

> "Es liegt nun nahe, mit einem Zeichen (Namen, Wortverbindung, Schriftzeichen) außer dem Bezeichneten, was die Bedeutung des Zeichens heißen möge, noch das verbunden zu denken, was ich den Sinn des Zeichens nennen möchte, worin die Art des Gegebenſeins enthalten iſt." (pp. 26–27; `¬` in "Wortver¬/bindung" and "Gegeben¬/ſeins" closed up)

*Gloss:* "It is natural now to think of there being connected with a sign (name, combination of words, written mark), besides that which the sign designates, which may be called the reference [`Bedeutung`] of the sign, also what I should like to call the sense [`Sinn`] of the sign, wherein the mode of presentation is contained."

### 3. The Morning Star / Evening Star: shared reference, distinct sense (p. 27)

The canonical example — `Abendſtern` (Evening Star) and `Morgenſtern` (Morning Star) name the same body (Venus) yet differ in sense:

> "Es würde die Bedeutung von „Abendſtern“ und „Morgenſtern“ dieſelbe ſein, aber nicht der Sinn." (p. 27)

*Gloss:* "The reference of 'Evening Star' and 'Morning Star' would be the same, but not the sense."

### 4. Sense can exist without a reference; reference is the object itself (pp. 27–30)

A grammatically well-formed name always has a sense, but need not have a reference:

> "Die Worte „der von der Erde am weiteſten entfernte Himmelskörper“ haben einen Sinn; ob ſie aber auch eine Bedeutung haben, iſt ſehr zweifelhaft." (p. 28)

*Gloss:* "The words 'the heavenly body most distant from the Earth' have a sense; but whether they also have a reference is very doubtful." Frege gives "die am wenigſten convergente Reihe" ("the least convergent series," p. 28) as an expression with a sense and provably *no* reference. And on what the reference of a name *is*:

> "Die Bedeutung eines Eigennamens iſt der Gegenſtand ſelbſt, den wir damit bezeichen; die Vorſtellung, welche wir dabei haben, iſt ganz ſubjectiv; dazwiſchen liegt der Sinn, der zwar nicht mehr ſubjectiv wie die Vorſtellung, aber doch auch nicht der Gegenſtand ſelbſt iſt." (p. 30)

*Gloss:* "The reference of a proper name is the object itself which we designate by it; the idea [`Vorstellung`] we have of it is wholly subjective; between the two lies the sense, which is indeed no longer subjective like the idea, but is yet not the object itself." (Note the three-way distinction: reference / sense / subjective idea — the sense is **objective and shareable**, "gemeinſames Eigenthum von Vielen," common property of many, p. 29.)

### 5. A sentence's sense is the thought (`Gedanke`); its reference is its truth-value (pp. 32–34)

Turning from names to whole declarative sentences (`Behauptungssatz`), Frege asks whether the **thought** a sentence contains is its sense or its reference, and settles it via the same substitution test that fixed the Morning/Evening Star case — swapping a co-referring part with a different sense changes the thought but must not change the sentence's reference:

> "Ein ſolcher Satz enthält einen Gedanken *). Iſt dieſer Gedanke nun als deſſen Sinn oder als deſſen Bedeutung anzuſehen?" (p. 32)

*Gloss:* "Such a sentence contains a thought [`Gedanke`]. Is this thought now to be regarded as its sense or as its reference?" His footnote `*)` fixes `Gedanke`: not the subjective act of thinking but "deſſen objectiven Inhalt, der fähig iſt, gemeinſames Eigenthum von Vielen zu ſein" (p. 32) — "its objective content, which is capable of being the common property of many." He concludes the thought is the *sense*, because it changes when a co-referring name is swapped:

> "Der Gedanke kann alſo nicht die Bedeutung des Satzes ſein, vielmehr werden wir ihn als den Sinn aufzufaſſen haben." (p. 32; `¬` in "viel¬/mehr" closed up)

*Gloss:* "The thought, accordingly, cannot be the reference of the sentence; rather we shall have to take it as the sense." What remains constant under such substitution — and so is the sentence's *reference* — is its truth-value:

> "So werden wir dahin gedrängt, den Wahrheitswerth eines Satzes als ſeine Bedeutung anzuerkennen. Ich verſtehe unter dem Wahrheitswerthe eines Satzes den Umſtand, daß er wahr oder daß er falſch iſt[.] [...] Ich nenne der Kürze halber den einen das Wahre, den andern das Falſche." (p. 34)

*Gloss:* "We are therefore driven to acknowledge the truth-value [`Wahrheitswert`] of a sentence as its reference. By the truth-value of a sentence I understand the circumstance that it is true or that it is false. [...] For brevity I call the one the True [`das Wahre`], the other the False [`das Falsche`]." This is the move that makes a sentence's semantic value its truth-value — the seed of truth-conditional semantics. Frege ties the drive from sense to reference explicitly to the pursuit of truth: "Das Streben nach Wahrheit alſo iſt es, was uns überall vom Sinne zur Bedeutung vorzudringen treibt." (p. 33) — "It is the striving for truth that drives us always to advance from the sense to the reference."

### 6. Compositionality / substitution-salva-veritate (pp. 35–36)

The part-to-whole principle: the reference (truth-value) of a sentence is unchanged when a part is replaced by a co-referring expression of different sense — Frege cites Leibniz's *salva veritate* — and he transfers the whole/part relation to the level of reference:

> "Wenn unſere Vermuthung richtig iſt, daß die Bedeutung eines Satzes ſein Wahrheitswerth iſt, ſo muß dieſer unverändert bleiben, wenn ein Satztheil durch einen Ausdruck von derſelben Bedeutung, aber anderm Sinne erſetzt wird. Und das iſt in der That der Fall. Leibnitz erklärt gradezu: „Eadem sunt, quae sibi mutuo substitui possunt, ſalva veritate“." (p. 35)

*Gloss:* "If our conjecture is right that the reference of a sentence is its truth-value, then this must remain unchanged when a part of the sentence is replaced by an expression with the same reference but a different sense. And that is indeed the case. Leibniz states outright: 'Things are the same as each other, of which one can be substituted for the other without loss of truth.'" Frege then explicitly applies the whole/part relation to reference, calling a word's reference a part of the sentence's reference — while flagging the move as "anfechtbar" (contestable):

> "Ich habe nämlich das Verhältniß des Ganzen und des Theils vom Satze auf ſeine Bedeutung übertragen, indem ich die Bedeutung eines Wortes Theil der Bedeutung des Satzes genannt habe[.]" (pp. 35–36)

*Gloss:* "I have, namely, transferred the relation of whole and part from the sentence to its reference, by calling the reference of a word a part of the reference of the sentence." This is the precise sense in which Frege grounds the **principle of compositionality** that [`concept/compositionality`](../concepts/compositionality.md) attributes to him: sense and reference of the whole are determined by, and decompose into, those of the parts under their mode of combination.

## Bearing on this project

- **[`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md).** That page's pole (a) opens: "Frege's distinction between sense and reference (`Über Sinn und Bedeutung`, 1892) gave the referential side its modern shape, with `Bedeutung` as the truth-relevant semantic value of an expression." This page supplies the verbatim primary for exactly that: `Bedeutung` of a sentence *is* its `Wahrheitswert` (p. 34), and the sense is the `Gedanke` (p. 32). The concept page's "Honest gaps" section listed Frege 1892 among the "not in-repo" truth-conditional lineage; that gap is now closed for Frege specifically (Tarski/Davidson/Montague/Wittgenstein remain not-in-repo).
- **[`concept/compositionality`](../concepts/compositionality.md).** That page attributes the principle of compositionality to Frege "(the principle of compositionality and the `Sinn`/`Bedeutung` distinction, 1892; *not in-repo; characterization*)." The substitution-*salva-veritate* passage (p. 35) and the whole/part transfer to reference (pp. 35–36) are the in-repo primary for that attribution. Caveat to carry forward: Frege does **not** state a general "meaning of the whole is a function of the meanings of the parts" slogan in those words; what is verbatim here is the *substitution-preserves-reference* principle and the whole/part transfer (which he himself flags as "anfechtbar," contestable). The modern compositionality-principle formulation is a later systematization; cite Frege for the substitution principle and the `Sinn`/`Bedeutung` machinery, not for the slogan verbatim.
- **[`concept/referential-meaning`](../concepts/referential-meaning.md) and the `referential` meaning-sense.** [`meaning-senses.md`](../../meaning-senses.md) defines `referential` as "Frege's `Bedeutung`," with sub-tags `referential.sense` ("Frege's `Sinn`: mode of presentation") and `referential.reference` ("what the expression picks out"). This page is the verbatim source for both: `Sinn` as "Art des Gegebenſeins" (pp. 26–27) and `Bedeutung` as "der Gegenſtand ſelbſt" (p. 30).

## What it can ground

- The verbatim `Sinn`/`Bedeutung` distinction (pp. 26–27), the Morning/Evening Star example (p. 27), sense-without-reference (p. 28), reference-as-object (p. 30), sentence-reference-as-truth-value (p. 34), sentence-sense-as-thought (p. 32), and the substitution-*salva-veritate* / whole-part-of-reference compositionality thread (pp. 35–36) — for any page needing the founding formulation rather than a paraphrase.
- The historical-conceptual point that on Frege's picture **meaning is a world-relation** (reference to an object, truth-value of a sentence), with sense as an objective, shareable mode of presentation between sign and object — the referential pole the project contrasts against distributional and use accounts.

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models.** The essay predates all of it by a century; it grounds the *theory* a model may or may not instantiate, never a result about a model. **It is not an `anchors:` resource** — it is not a human-labeled empirical asset (no treebank, sense inventory, acceptability norm, or annotation).
- **A human-comparison anchor.** A `source` page supplies theory/provenance, not a human yardstick; citing it does not discharge any empirical claim's human-anchor obligation.
- **The modern slogan of compositionality verbatim.** See the caveat above: Frege states substitution-salva-veritate and a whole/part transfer to reference (which he himself calls contestable), not the textbook "function of the meanings of the parts" formula.

## Known limits

- **Diplomatic Fraktur transcription.** Quotes preserve the 1892 long-s `ſ`; a citing session quoting at length should re-verify against the DTA text or the journal scan, especially around the closed-up `¬` line-break hyphens (flagged per quote). The DTA edition is a validated transcription of the journal original, but it is a transcription, not the page image.
- **No English-translation quotes.** The standard Black / Geach-&-Black translations are likely in copyright; this page deliberately quotes only the PD German and gives its own glosses. The glosses are the project's paraphrase and should not be cited as a published translation.
- **`Bedeutung` is conventionally translated "reference" but literally "meaning"/"significance."** Frege's technical use is the referent/semantic-value; the project follows the standard "reference" rendering and flags that the German word's ordinary sense is broader, to avoid the unqualified-"meaning" lint trap.
- The essay's later sections (indirect/oblique reference `ungerade Rede`, subordinate clauses `Nebensätze`) are summarized only in passing here; this page captures the sense/reference core, the truth-value move, and the compositionality thread, not the full theory of clausal embedding (pp. 36–50).
