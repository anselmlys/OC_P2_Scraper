from extract import get_book_information, get_all_book, get_all_categories
from load import save_csv


def main():
    url_to_scrape = 'https://books.toscrape.com/'

    categories_urls = get_all_categories(url_to_scrape)
        
    try:    
        for category_url in categories_urls:
            books_urls = get_all_book(category_url)
            for book_url in books_urls:
                book_information = get_book_information(book_url)
                save_csv(book_information)
    except AttributeError:
        print(f'Stopped at:\n{category_url}: {book_url}')


if __name__ == "__main__":
    main()