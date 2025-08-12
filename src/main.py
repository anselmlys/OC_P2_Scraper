from extract import get_book_information, get_all_book
from load import save_csv


def main():
    category_url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

    books_urls = get_all_book(category_url)
    for book_url in books_urls:
        book_information = get_book_information(book_url)
        save_csv(book_information)


if __name__ == "__main__":
    main()