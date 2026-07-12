"""Japanese-competence smoke test (freeze condition i of the ratified scope decision).

Runs BEFORE the main probe. 12 UNAMBIGUOUS, NON-CC Japanese comprehension items in the exact same
forced-choice channel (FC_SYS + parse_fc, imported from probe.py) whose 増加/減少/不明 answer is forced
by EXPLICIT Japanese content (NOT by the 〜ば〜ほど construction under test) — so a correct answer means
the panel (a) reads Japanese, (b) maps to the answer vocabulary, (c) follows the one-word format. This
isolates Japanese competence from the constructional question: if a model fails here, its main-run
behavior cannot be read as constructional vs comprehension noise. Japanese panel competence is a
priori lower than German (Q1-C note), so this gate is load-bearing.

GATE (pre-registered, identical to the German arm): each model >= 10/12 AND panel mean >= 0.90 -> GO.
Otherwise the main run is withheld and the failure recorded. Uses the SAME panel, temperature,
parsing as the main probe.

Run: OPENROUTER_API_KEY=... python3 smoke.py
"""
import json, os
from probe import PANEL, FC_SYS, call, parse_fc, mt_for, RAW_DIR

# (id, passage, dim1, dim2, gold) — answer forced by explicit content, NOT by a CC construction.
SMOKE = [
    ("rain", "雨が強く降ると、道はさらに濡れた。",
     "雨の強さ", "道の濡れ具合", "increase"),
    ("heat", "気温が上がると、氷は速く溶けた。",
     "気温", "氷の溶ける速さ", "increase"),
    ("price", "パンの値段が上がったので、買う人が減った。",
     "パンの値段", "買う人の数", "decrease"),
    ("noise", "工事の音が大きくなると、苦情を言う住民が増えた。",
     "工事の音の大きさ", "苦情の数", "increase"),
    ("light", "照明が明るくなると、読み間違いの数は減った。",
     "照明の明るさ", "読み間違いの数", "decrease"),
    ("dog", "犬はかごの中で静かに眠っていた。",
     "部屋の温度", "空の星の数", "undetermined"),
    ("wind", "風が強くなると、風車は速く回った。",
     "風の強さ", "風車の回る速さ", "increase"),
    ("study", "試験のために長く練習したので、彼女のミスは減った。",
     "練習の時間", "ミスの数", "decrease"),
    ("book", "机の上に青い本がカップの隣に置かれていた。",
     "本の古さ", "山の高さ", "undetermined"),
    ("sun", "日が沈むと、外は寒くなった。",
     "日没からの時間", "外の気温", "decrease"),
    ("garden", "雨が多く降ったので、庭の植物は速く育った。",
     "雨の量", "植物の育つ速さ", "increase"),
    ("stone", "灰色の石が道の端に転がっていた。",
     "石の重さ", "映画の長さ", "undetermined"),
]


def fc_user(passage, dim1, dim2):
    return (f"文章：{passage}\n"
            f"{dim1}が増すと、この文章は{dim2}についてどう示唆していますか？"
            f"「増加」「減少」「不明」で答えてください。")


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
