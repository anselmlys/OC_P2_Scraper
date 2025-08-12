from pathlib import Path
import csv


def save_csv(dictionary):
    try:
        Path("data").mkdir(parents=True, exist_ok=True)

        with open('data/book_information.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=dictionary.keys())
            writer.writeheader()
            writer.writerow(dictionary)
    except PermissionError as errp:
        print("Permission Error", {errp})