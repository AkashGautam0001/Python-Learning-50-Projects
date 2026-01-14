import os
import csv
from datetime import datetime
import requests

WEATHER_API_KEY="31ec01a1d61c3cb7392f90090824d136"
FILENAME = "weather_logs.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
       writer = csv.writer(file)
       writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
    city = input("Enter your city name : ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == date and row['City'].lower() == city.lower():
                print("Entry Already exits")
                return
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"API Error")
            return
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        with open(FILENAME, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([date, city.title(), temp, condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}")

    except Exception as e:
        print("Failed to make API call")

def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            print("No Entries")
            return
        for row in reader[1]:
            print(f"{row[0]} : {row[1]} : {row[2]} {row[3]}")
    
def main():
    while True:
        print("Real time weather logger")
        print("1. Add Weather log")
        print("2. View log")

        choice = input("Choose an options: ").strip()
        match choice:
            case "1" : log_weather()
            case "2" : view_logs()
            case _: print("Please enter valid input")


if __name__ == "__main__":
    main()

