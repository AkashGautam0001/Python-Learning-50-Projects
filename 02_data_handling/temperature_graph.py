import csv
from collections import defaultdict
import matplotlib.pyplot as plot

FILENAME = "weather_lgs_for_graph.csv"

def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row["Date"])
                temps.append(row["Temperature"])
                conditions[row["Condition"]] += 1
            except:
                continue
    
    if not dates:
        print("No data is avaiable")
        return
    # plot.figure(figsize=(10,7))
    # plot.plot(dates, temps, marker="o")
    # plot.title("Temperature over time")
    # plot.xlabel("Date")
    # plot.ylabel("Temperature")
    # plot.grid(True)
    # plot.show()

    plot.figure(figsize=(7,5))
    plot.bar(list(conditions.keys()), list(conditions.values()), color="skyblue")
    plot.title("Temperature Conditions")
    plot.xlabel("Condition")
    plot.ylabel("Frequency")
    plot.grid(True)
    plot.show()


visualize_weather()







