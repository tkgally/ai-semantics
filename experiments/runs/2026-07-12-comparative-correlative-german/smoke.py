"""German-competence smoke test (freeze condition i of the ratified scope decision).

Runs BEFORE the main probe. 12 UNAMBIGUOUS, NON-CC German comprehension items in the exact same
forced-choice channel (FC_SYS + parse_fc, imported from probe.py) whose ZUNAHME/ABNAHME/UNBESTIMMT
answer is forced by EXPLICIT German content (not by the je…desto construction under test) — so a
correct answer means the panel (a) reads German, (b) maps to the answer vocabulary, (c) follows the
one-word format. This isolates German competence from the constructional question: if a model fails
here, its main-run behavior cannot be read as constructional vs comprehension noise.

GATE (pre-registered): each model >= 10/12 AND panel mean >= 0.90 -> GO. Otherwise the main run is
withheld and the failure recorded. Uses the SAME panel, temperature, parsing as the main probe.

Run: OPENROUTER_API_KEY=... python3 smoke.py
"""
import json, os, time
from probe import PANEL, FC_SYS, call, parse_fc, mt_for, RAW_DIR

# (id, passage, dim1, dim2, gold) — answer forced by explicit content, NOT by a CC construction.
SMOKE = [
    ("regen", "Als es stärker regnete, wurde die Straße nasser.",
     "die Stärke des Regens", "die Nässe der Straße", "increase"),
    ("hitze", "Mit steigender Hitze schmolz das Eis schneller.",
     "die Hitze", "die Schmelzgeschwindigkeit des Eises", "increase"),
    ("preis", "Weil der Preis stieg, kauften weniger Menschen das Brot.",
     "der Preis des Brotes", "die Zahl der Käufer", "decrease"),
    ("laerm", "Je mehr Lärm entstand, desto stärker stiegen die Beschwerden.",
     "die Menge des Lärms", "die Zahl der Beschwerden", "increase"),
    ("licht", "Als das Licht heller wurde, sank die Zahl der Fehler beim Lesen.",
     "die Helligkeit des Lichts", "die Zahl der Lesefehler", "decrease"),
    ("hund", "Der Hund schlief ruhig in seinem Korb.",
     "die Temperatur des Raumes", "die Zahl der Sterne am Himmel", "undetermined"),
    ("wind", "Mit zunehmendem Wind drehten sich die Windräder schneller.",
     "die Stärke des Windes", "die Drehgeschwindigkeit der Windräder", "increase"),
    ("uebung", "Je mehr sie übte, desto weniger Fehler machte sie.",
     "die Menge der Übung", "die Zahl der Fehler", "decrease"),
    ("buch", "Auf dem Tisch lag ein blaues Buch neben einer Tasse.",
     "das Alter des Buches", "die Höhe des Berges", "undetermined"),
    ("sonne", "Als die Sonne unterging, wurde es draußen kälter.",
     "die Zeit seit Sonnenuntergang", "die Temperatur draußen", "decrease"),
    ("garten", "Weil es mehr regnete, wuchsen die Pflanzen im Garten schneller.",
     "die Menge des Regens", "die Wachstumsgeschwindigkeit der Pflanzen", "increase"),
    ("stein", "Ein grauer Stein lag am Rand des Weges.",
     "das Gewicht des Steins", "die Länge des Films", "undetermined"),
]


def fc_user(passage, dim1, dim2):
    return (f"Passage: {passage}\n"
            f"Wenn {dim1} zunimmt, was impliziert die Passage über {dim2}? "
            f"Antworte mit ZUNAHME, ABNAHME oder UNBESTIMMT.")


def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    results = {}
    total_cost = 0.0
    for slot, model in PANEL.items():
        recs = []
        for sid, passage, d1, d2, gold in SMOKE:
            r = call(model, FC_SYS, fc_user(passage, d1, d2), mt_for(model))
            pred = parse_fc(r.get("content"))
            recs.append({"id": sid, "gold": gold, "pred": pred, "raw": r.get("content"),
                         "usage": r.get("usage"), "error": r.get("error")})
            total_cost += float((r.get("usage") or {}).get("cost") or 0)
        correct = sum(1 for x in recs if x["pred"] == x["gold"])
        na = sum(1 for x in recs if x["pred"] is None)
        results[slot] = {"model": model, "correct": correct, "n": len(SMOKE),
                         "acc": round(correct / len(SMOKE), 3), "na": na, "recs": recs}
        print(f"panel.{slot} {model}: {correct}/{len(SMOKE)} acc={correct/len(SMOKE):.3f} na={na}")
    accs = [results[s]["correct"] / len(SMOKE) for s in PANEL]
    panel_mean = sum(accs) / len(accs)
    each_pass = all(results[s]["correct"] >= 10 for s in PANEL)
    verdict = "GO" if (each_pass and panel_mean >= 0.90) else "NO-GO"
    out = {"gate": "each model >= 10/12 AND panel mean >= 0.90",
           "panel_mean_acc": round(panel_mean, 3), "each_ge_10": each_pass,
           "verdict": verdict, "billed_usd": round(total_cost, 6), "per_model": results}
    with open(os.path.join(RAW_DIR, "smoke_results.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"\npanel_mean_acc={panel_mean:.3f}  each>=10/12={each_pass}  -> {verdict}")
    print(f"billed: ${total_cost:.6f}")


if __name__ == "__main__":
    main()
