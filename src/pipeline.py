from extract import get_all_categories, get_all_books_by_category, get_book_information
from load import save_csv, download_image


def get_category_urls(url, queue1):
    category_urls = get_all_categories(url)
    for category_url in category_urls:
        queue1.put(category_url)
    
    queue1.put(None)


def get_book_urls(queue1, queue2):
    while True:
        category_url = queue1.get()
        
        if category_url == None:
            queue2.put(None)
            break

        book_urls_by_category = get_all_books_by_category(category_url)
        for book_url in book_urls_by_category:
            queue2.put(book_url)


def get_all_book_information(queue2, queue3):
    while True:
        book_url = queue2.get()

        if book_url == None:
            queue3.put(None)
            break

        book_information = get_book_information(book_url)
        queue3.put(book_information)


def save_csv_and_images(queue3):
    while True:
        book_information = queue3.get()

        if book_information is None:
            break
        
        save_csv(book_information, book_information['category'])
        download_image(book_information['category'], 
                        book_information['universal_product_code'],
                        book_information['image_url'])
