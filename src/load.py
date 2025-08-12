from datetime import date
from pathlib import Path
import csv


def save_csv(dictionary):
    try:
        Path("data").mkdir(parents=True, exist_ok=True)

        current_date = date.today().strftime('%y-%m-%d')
        file_name = "data/book-information_"+current_date+".csv"

        with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=dictionary.keys())
            writer.writeheader()
            writer.writerow(dictionary)
    except PermissionError as errp:
        print("Permission Error", {errp})