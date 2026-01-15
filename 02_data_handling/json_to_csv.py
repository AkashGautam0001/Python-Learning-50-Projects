import json
import csv
import os

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except:
            print("Invalid JSON format")

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    fieldname = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    
    print(f"Converted {len(data)} record to {output_file} ")

def main():
    print("Converting JSON to CSV ..")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()