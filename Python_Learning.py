import csv

lists = [["Top Gun", "Risky Business", "Minority Report"],
         ["Titanic", "The Revenant", "Inception"],
         ["Training Day", "Mon on File", "Flight"]]

with open("st.csv", "w", newline="") as f:
    w = csv.writer(f,delimiter=",")
    for list in lists:
        w.writerow(list)