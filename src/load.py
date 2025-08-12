from datetime import datetime
from pathlib import Path
import csv


def save_csv(dictionary):
    try:
        Path("data").mkdir(parents=True, exist_ok=True)

        current_datetime = datetime.now().strftime('%y-%m-%d_%Hh')
        file_name = "data/books-info_"+current_datetime+".csv"
        file_path = Path(file_name)
        file_existence = file_path.is_file()

        with open(file_name, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=dictionary.keys())

            if file_existence == False:
                writer.writeheader()

            writer.writerow(dictionary)

    except PermissionError as errp:
        print("Permission Error", {errp})
