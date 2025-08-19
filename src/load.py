from datetime import date
from pathlib import Path
import csv
import requests


def save_csv(dictionary, category):
    try:
        Path("data").mkdir(parents=True, exist_ok=True)

        current_datetime = date.today().strftime('%y%m%d')
        filename = "data/"+category+"_"+current_datetime+".csv"
        file_path = Path(filename)
        file_existence = file_path.is_file()

        with open(filename, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=dictionary.keys())

            if file_existence == False:
                writer.writeheader()

            writer.writerow(dictionary)

    except PermissionError as errp:
        print("Permission Error", {errp})


def download_image(category, book_upc, image_url):
    try:
        Path("media").mkdir(parents=True, exist_ok=True)

        category_folder = 'media/'+category
        Path(category_folder).mkdir(parents=True, exist_ok=True)

        image_data = requests.get(image_url).content
        filename = 'media/'+category+'/'+book_upc+'.jpg'

        with open(filename, 'wb') as image:
            image.write(image_data)

    except PermissionError as errp:
        print("Permission Error", {errp})
