import csv

lists = [["トップガン", "リスキービジネス", "マイノリティリポート"],
         ["タイタニック", "レヴナント", "インセプション"],
         ["トレイニングデイ", "マンオンファイア", "フライト"]]

with open("st.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for list in lists:
        w.writerow(list)