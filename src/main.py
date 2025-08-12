from extract import get_book_information
from load import save_csv


def main():
    url = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'

    book_information = get_book_information(url)
    save_csv(book_information)


if __name__ == "__main__":
    main()