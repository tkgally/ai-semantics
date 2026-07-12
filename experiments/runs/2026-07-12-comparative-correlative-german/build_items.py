"""Build and freeze the German CC item set (A6 cross-linguistic replication, 2026-07-12, s213).

A faithful PORT of the frozen English v1/powered comparative-correlative instrument
(experiments/runs/2026-07-02-comparative-correlative-powered) to German, per the ratified scope
decision decisions/resolved/cross-linguistic-cc-replication-scope (Q1-C German / Q2-B same-word +
freq-matched control / Q3-A internal-contrast-only). Same FOUR item forms, same construction-correct
gold answers, same typical/atypical split (24 typical + 10 atypical = 34 scale pairs x 4 forms = 136
items) — the ONLY change vs the English instrument is the target LANGUAGE (the whole point: does the
construction-isolation contrast survive a surface-statistics change from English `the…the` to German
`je…desto/umso`?).

German CC construction (self-audited against base/sources/meinunger-2023-je-desto.md):
  `je` + comparative ... (SUBORDINATE clause, finite verb FINAL) , `desto`/`umso` + comparative ...
  (MAIN clause, finite verb SECOND). `desto` and `umso` interchangeable.

Four forms per scale pair, reusing the SAME scalar lexical material (the same-word non-CC controls,
Q2-A core leg — lexis held identical so the construction-isolation gap is purely syntactic):
  cc-positive  : "Je MORE x ..., desto MORE y ..."   -> covariation direction = increase
  cc-inverse   : "Je MORE x ..., desto LESS/ANTONYM y ..." -> covariation direction = decrease
  ctrl-two     : two independent declarative clauses (both scales asserted, no dependency)
  ctrl-single  : a single comparative clause (only one scale mentioned)

Construction-correct answers (fixed here, BEFORE the run — anti-cheat freeze, condition iii):
  forced-choice (as dim1 increases, does dim2 increase / decrease / undetermined):
    cc-positive -> increase ; cc-inverse -> decrease ; both controls -> undetermined
  NLI (premise = sentence, hypothesis = "Wenn <dim1> zunimmt, dann nimmt <dim2> zu."):
    cc-positive -> 0 entailment ; cc-inverse -> 2 contradiction ; both controls -> 1 neutral

Emits experiments/data/comparative-correlative-german/items.csv; committed BEFORE any probe call.
Scale pairs are authored so the covariation direction is NOT world-knowledge-obvious (typical) or is
deliberately absurd (atypical) — the construction, not plausibility, must supply the direction.
"""
import csv, os

# pid, typicality, dim1 (German NP, phrased so "<dim1> zunimmt" reads), dim2 (German NP),
# cc_pos, cc_inv, ctrl_two, ctrl_single
PAIRS = [
    # ---- typical (24): plausible-either-direction pairs (direction not obvious) ----
    ("roman", "typical", "die Dicke des Romans", "die Geduld des Lesers",
     "Je dicker der Roman war, desto geduldiger blieb der Leser.",
     "Je dicker der Roman war, desto ungeduldiger wurde der Leser.",
     "Der Roman war dick. Der Leser war geduldig.",
     "Der Roman war dicker als der letzte."),
    ("oefen", "typical", "die Hitze der Öfen", "die Zahl der Kunden",
     "Je heißer die Öfen liefen, desto mehr Kunden kamen.",
     "Je heißer die Öfen liefen, desto weniger Kunden kamen.",
     "Die Öfen liefen heiß. Viele Kunden kamen.",
     "Die Öfen liefen heißer als sonst."),
    ("seminar", "typical", "die Größe des Seminars", "die Menge der Diskussion",
     "Je größer das Seminar war, desto mehr Diskussion entstand.",
     "Je größer das Seminar war, desto weniger Diskussion entstand.",
     "Das Seminar war groß. Die Diskussion war lebhaft.",
     "Das Seminar war größer als die Vorlesung."),
    ("sommer", "typical", "die Trockenheit des Sommers", "die Süße der Äpfel",
     "Je trockener der Sommer war, desto süßer wurden die Äpfel.",
     "Je trockener der Sommer war, desto saurer wurden die Äpfel.",
     "Der Sommer war trocken. Die Äpfel waren süß.",
     "Der Sommer war trockener als im Vorjahr."),
    ("autobahn", "typical", "die Breite der Autobahn", "die Geschwindigkeit der Fahrer",
     "Je breiter die Autobahn war, desto schneller fuhren die Fahrer.",
     "Je breiter die Autobahn war, desto langsamer fuhren die Fahrer.",
     "Die Autobahn war breit. Die Fahrer fuhren schnell.",
     "Die Autobahn war breiter als die alte Straße."),
    ("galerie", "typical", "die Dunkelheit der Galerie", "das Flüstern der Besucher",
     "Je dunkler die Galerie war, desto mehr flüsterten die Besucher.",
     "Je dunkler die Galerie war, desto weniger flüsterten die Besucher.",
     "Die Galerie war dunkel. Die Besucher flüsterten.",
     "Die Galerie war dunkler als das Foyer."),
    ("startup", "typical", "die Größe des Start-ups", "die Vorsicht der Investoren",
     "Je größer das Start-up war, desto vorsichtiger wurden die Investoren.",
     "Je größer das Start-up war, desto unvorsichtiger wurden die Investoren.",
     "Das Start-up war groß. Die Investoren waren vorsichtig.",
     "Das Start-up war größer als sein Rivale."),
    ("hafen", "typical", "die Betriebsamkeit des Hafens", "der Preis für Fisch",
     "Je betriebsamer der Hafen war, desto höher stieg der Preis für Fisch.",
     "Je betriebsamer der Hafen war, desto niedriger fiel der Preis für Fisch.",
     "Der Hafen war betriebsam. Der Preis für Fisch war hoch.",
     "Der Hafen war betriebsamer als im Winter."),
    ("wartezimmer", "typical", "die Wärme des Wartezimmers", "die Schläfrigkeit der Patienten",
     "Je wärmer das Wartezimmer war, desto schläfriger wurden die Patienten.",
     "Je wärmer das Wartezimmer war, desto wacher wurden die Patienten.",
     "Das Wartezimmer war warm. Die Patienten waren schläfrig.",
     "Das Wartezimmer war wärmer als der Flur."),
    ("weinberg", "typical", "die Steilheit des Weinbergs", "der Lohn der Pflücker",
     "Je steiler der Weinberg war, desto höher stieg der Lohn der Pflücker.",
     "Je steiler der Weinberg war, desto niedriger fiel der Lohn der Pflücker.",
     "Der Weinberg war steil. Der Lohn der Pflücker war hoch.",
     "Der Weinberg war steiler als der Obstgarten."),
    ("becken", "typical", "die Kälte des Beckens", "die Zahl der Bahnen",
     "Je kälter das Becken war, desto mehr Bahnen schwammen die Schwimmer.",
     "Je kälter das Becken war, desto weniger Bahnen schwammen die Schwimmer.",
     "Das Becken war kalt. Die Schwimmer schwammen viele Bahnen.",
     "Das Becken war kälter als das Meer."),
    ("regale", "typical", "die Höhe der Regale", "das Tempo der Bibliothekare",
     "Je höher die Regale waren, desto schneller gingen die Bibliothekare.",
     "Je höher die Regale waren, desto langsamer gingen die Bibliothekare.",
     "Die Regale waren hoch. Die Bibliothekare gingen schnell.",
     "Die Regale waren höher als die Lesetische."),
    ("band", "typical", "die Lautstärke der Band", "die Größe der tanzenden Menge",
     "Je lauter die Band spielte, desto größer wurde die tanzende Menge.",
     "Je lauter die Band spielte, desto kleiner wurde die tanzende Menge.",
     "Die Band war laut. Die tanzende Menge war groß.",
     "Die Band war lauter als die Vorband."),
    ("feld", "typical", "die Ebenheit des Feldes", "der Ertrag der Bauern",
     "Je ebener das Feld war, desto größer wurde der Ertrag der Bauern.",
     "Je ebener das Feld war, desto kleiner wurde der Ertrag der Bauern.",
     "Das Feld war eben. Der Ertrag der Bauern war groß.",
     "Das Feld war ebener als der Hang."),
    ("broschuere", "typical", "der Glanz der Broschüre", "das Vertrauen der Käufer",
     "Je glänzender die Broschüre war, desto mehr vertrauten die Käufer der Broschüre.",
     "Je glänzender die Broschüre war, desto weniger vertrauten die Käufer der Broschüre.",
     "Die Broschüre war glänzend. Die Käufer vertrauten ihr.",
     "Die Broschüre war glänzender als der Flyer."),
    ("theater", "typical", "die Dunkelheit des Theaters", "die Unruhe des Publikums",
     "Je dunkler das Theater war, desto unruhiger wurde das Publikum.",
     "Je dunkler das Theater war, desto ruhiger wurde das Publikum.",
     "Das Theater war dunkel. Das Publikum war unruhig.",
     "Das Theater war dunkler als bei der Generalprobe."),
    ("curry", "typical", "die Schärfe des Currys", "die Gesprächigkeit der Gäste",
     "Je schärfer das Curry war, desto gesprächiger wurden die Gäste.",
     "Je schärfer das Curry war, desto stiller wurden die Gäste.",
     "Das Curry war scharf. Die Gäste waren gesprächig.",
     "Das Curry war schärfer als die Vorspeise."),
    ("lehrplan", "typical", "die Länge des Lehrplans", "die Begeisterung der Studenten",
     "Je länger der Lehrplan war, desto begeisterter wirkten die Studenten.",
     "Je länger der Lehrplan war, desto lustloser wirkten die Studenten.",
     "Der Lehrplan war lang. Die Studenten waren begeistert.",
     "Der Lehrplan war länger als im letzten Semester."),
    ("stroemung", "typical", "die Geschwindigkeit der Strömung", "die Frustration der Angler",
     "Je schneller die Strömung war, desto frustrierter wurden die Angler.",
     "Je schneller die Strömung war, desto gelassener wurden die Angler.",
     "Die Strömung war schnell. Die Angler waren frustriert.",
     "Die Strömung war schneller als im Morgengrauen."),
    ("kueche", "typical", "die Ordnung in der Küche", "das Geplauder der Köche",
     "Je ordentlicher die Küche war, desto mehr plauderten die Köche.",
     "Je ordentlicher die Küche war, desto weniger plauderten die Köche.",
     "Die Küche war ordentlich. Die Köche plauderten.",
     "Die Küche war ordentlicher als die Speisekammer."),
    ("pfad", "typical", "die Enge des Pfades", "der Abstand der Wanderer",
     "Je enger der Pfad war, desto größer wurde der Abstand der Wanderer.",
     "Je enger der Pfad war, desto kleiner wurde der Abstand der Wanderer.",
     "Der Pfad war eng. Der Abstand der Wanderer war groß.",
     "Der Pfad war enger als der Fahrweg."),
    ("auktionssaal", "typical", "die Helligkeit des Auktionssaals", "das Verweilen der Sammler",
     "Je heller der Auktionssaal war, desto länger verweilten die Sammler.",
     "Je heller der Auktionssaal war, desto kürzer verweilten die Sammler.",
     "Der Auktionssaal war hell. Die Sammler verweilten lange.",
     "Der Auktionssaal war heller als der Tresorraum."),
    ("boden", "typical", "der Sandanteil des Bodens", "die Häufigkeit des Gießens",
     "Je sandiger der Boden war, desto mehr goss der Gärtner.",
     "Je sandiger der Boden war, desto weniger goss der Gärtner.",
     "Der Boden war sandig. Der Gärtner goss oft.",
     "Der Boden war sandiger als das Lehmbeet."),
    ("halle", "typical", "die Größe der Halle", "die Ausgelassenheit der Fans",
     "Je größer die Halle war, desto ausgelassener wurden die Fans.",
     "Je größer die Halle war, desto gesitteter wurden die Fans.",
     "Die Halle war groß. Die Fans waren ausgelassen.",
     "Die Halle war größer als der Club."),
    # ---- atypical (10): deliberately absurd pairings (world knowledge gives NO direction;
    #      covariation can ONLY come from the construction) ----
    ("teetasse", "atypical", "die Rundheit der Teetasse", "die Länge des Staus",
     "Je runder die Teetasse war, desto länger wurde der Stau.",
     "Je runder die Teetasse war, desto kürzer wurde der Stau.",
     "Die Teetasse war rund. Der Stau war lang.",
     "Die Teetasse war runder als die Tasse."),
    ("teppich", "atypical", "die Röte des Teppichs", "die Geschwindigkeit des Aufzugs",
     "Je roter der Teppich war, desto schneller fuhr der Aufzug.",
     "Je roter der Teppich war, desto langsamer fuhr der Aufzug.",
     "Der Teppich war rot. Der Aufzug fuhr schnell.",
     "Der Teppich war roter als die Vorhänge."),
    ("pfannkuchen", "atypical", "die Lockerheit des Pfannkuchens", "die Höhe des Berges",
     "Je lockerer der Pfannkuchen war, desto höher ragte der Berg.",
     "Je lockerer der Pfannkuchen war, desto niedriger ragte der Berg.",
     "Der Pfannkuchen war locker. Der Berg ragte hoch.",
     "Der Pfannkuchen war lockerer als die Waffel."),
    ("hefter", "atypical", "das Gewicht des Hefters", "die Helligkeit des Sonnenuntergangs",
     "Je schwerer der Hefter war, desto heller brannte der Sonnenuntergang.",
     "Je schwerer der Hefter war, desto blasser brannte der Sonnenuntergang.",
     "Der Hefter war schwer. Der Sonnenuntergang brannte hell.",
     "Der Hefter war schwerer als der Klebeband-Abroller."),
    ("socke", "atypical", "das Streifenmuster der Socke", "die Lautstärke des Donners",
     "Je gestreifter die Socke war, desto lauter krachte der Donner.",
     "Je gestreifter die Socke war, desto leiser krachte der Donner.",
     "Die Socke war gestreift. Der Donner krachte laut.",
     "Die Socke war gestreifter als der Handschuh."),
    ("lampenschirm", "atypical", "die Breite des Lampenschirms", "die Säure des Joghurts",
     "Je breiter der Lampenschirm war, desto saurer schmeckte der Joghurt.",
     "Je breiter der Lampenschirm war, desto süßer schmeckte der Joghurt.",
     "Der Lampenschirm war breit. Der Joghurt schmeckte sauer.",
     "Der Lampenschirm war breiter als der Sockel."),
    ("tastatur", "atypical", "der Staub auf der Tastatur", "die Größe der Ernte",
     "Je staubiger die Tastatur war, desto größer fiel die Ernte aus.",
     "Je staubiger die Tastatur war, desto kleiner fiel die Ernte aus.",
     "Die Tastatur war staubig. Die Ernte fiel groß aus.",
     "Die Tastatur war staubiger als der Monitor."),
    ("ballon", "atypical", "der Glanz des Ballons", "die Tiefe des Brunnens",
     "Je glänzender der Ballon war, desto tiefer reichte der Brunnen.",
     "Je glänzender der Ballon war, desto flacher reichte der Brunnen.",
     "Der Ballon war glänzend. Der Brunnen reichte tief.",
     "Der Ballon war glänzender als das Band."),
    ("umschlag", "atypical", "die Zerknitterung des Umschlags", "die Geschwindigkeit des Zuges",
     "Je zerknitterter der Umschlag war, desto schneller fuhr der Zug.",
     "Je zerknitterter der Umschlag war, desto langsamer fuhr der Zug.",
     "Der Umschlag war zerknittert. Der Zug fuhr schnell.",
     "Der Umschlag war zerknitterter als das Paket."),
    ("tannenzapfen", "atypical", "die Klebrigkeit des Tannenzapfens", "der Preis des Haarschnitts",
     "Je klebriger der Tannenzapfen war, desto teurer wurde der Haarschnitt.",
     "Je klebriger der Tannenzapfen war, desto billiger wurde der Haarschnitt.",
     "Der Tannenzapfen war klebrig. Der Haarschnitt war teuer.",
     "Der Tannenzapfen war klebriger als die Eichel."),
]

# construction-correct gold: (form, fc_gold, nli_gold)
FORMS = [
    ("cc-positive",   "increase",     "0"),
    ("cc-inverse",    "decrease",     "2"),
    ("ctrl-two",      "undetermined", "1"),
    ("ctrl-single",   "undetermined", "1"),
]


def sentence_for(pair, form):
    _, _, _, _, cc_pos, cc_inv, ctrl_two, ctrl_single = pair
    return {"cc-positive": cc_pos, "cc-inverse": cc_inv,
            "ctrl-two": ctrl_two, "ctrl-single": ctrl_single}[form]


def main():
    out = os.path.join(os.path.dirname(__file__), "..", "..",
                       "data", "comparative-correlative-german", "items.csv")
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    # integrity guards (ENFORCED): unique pids, correct split, four forms each.
    pids = [p[0] for p in PAIRS]
    assert len(pids) == len(set(pids)), f"duplicate pid: {[p for p in pids if pids.count(p) > 1]}"
    n_typ = sum(1 for p in PAIRS if p[1] == "typical")
    n_aty = sum(1 for p in PAIRS if p[1] == "atypical")
    assert (n_typ, n_aty) == (24, 10), f"split drifted: {n_typ} typical + {n_aty} atypical"
    rows = []
    for pair in PAIRS:
        pid, typ, dim1, dim2 = pair[0], pair[1], pair[2], pair[3]
        for form, fc_gold, nli_gold in FORMS:
            sent = sentence_for(pair, form)
            rows.append({
                "item_id": f"{pid}-{form}",
                "scale_pair": pid,
                "typicality": typ,
                "form": form,
                "dim1": dim1,
                "dim2": dim2,
                "sentence": sent,
                "fc_gold": fc_gold,
                "nli_hypothesis": f"Wenn {dim1} zunimmt, dann nimmt {dim2} zu.",
                "nli_gold": nli_gold,
            })
    cols = ["item_id", "scale_pair", "typicality", "form", "dim1", "dim2",
            "sentence", "fc_gold", "nli_hypothesis", "nli_gold"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} items ({len(PAIRS)} pairs x {len(FORMS)} forms) -> {out}")
    print(f"  typical pairs: {n_typ}, atypical pairs: {n_aty}")


if __name__ == "__main__":
    main()
