from datetime import date
from pathlib import Path
import csv


def save_csv(dictionary, category):
    try:
        Path("data").mkdir(parents=True, exist_ok=True)

        current_datetime = date.today().strftime('%y%m%d')
        file_name = "data/"+category+"_"+current_datetime+".csv"
        file_path = Path(file_name)
        file_existence = file_path.is_file()

        with open(file_name, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=dictionary.keys())

            if file_existence == False:
                writer.writeheader()

            writer.writerow(dictionary)

    except PermissionError as errp:
        print("Permission Error", {errp})
