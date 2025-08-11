from pathlib import Path
import csv

from extract import get_book_information


def main():
    url = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'

    book_information = get_book_information(url)

    #Sauvegarde les info du livre dans un fichier CSV
    Path("data").mkdir(parents=True, exist_ok=True)

    with open('data/data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=book_information.keys())
        writer.writeheader()
        writer.writerow(book_information)


if __name__ == "__main__":
    main()