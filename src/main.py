from extract import get_book_information, get_all_books_by_category, get_all_categories
from load import save_csv, download_image


def main():
    url_to_scrape = 'https://books.toscrape.com/'
    all_books_urls = []
    all_books_information = []

    categories_urls = get_all_categories(url_to_scrape)
 
    for category_url in categories_urls:
        books_urls_by_category = get_all_books_by_category(category_url)
        all_books_urls.extend(books_urls_by_category)

    for book_url in all_books_urls:
        book_information = get_book_information(book_url)
        all_books_information.append(book_information)
    
    for book_information in all_books_information:
        save_csv(book_information, book_information['category'])

    for book_information in all_books_information:
        download_image(
            book_information['category'],
            book_information['universal_product_code'], 
            book_information['image_url']
            )


if __name__ == "__main__":
    main()