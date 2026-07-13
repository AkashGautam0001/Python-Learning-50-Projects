import requests
import csv
import os
from datetime import datetime

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

CSV_FILE = "crypto_prices.csv"

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        write = csv.writer(file)
        if not file_exists:
            write.writerow(["timestamp", ""])