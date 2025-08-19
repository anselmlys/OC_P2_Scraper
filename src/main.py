from threading import Thread
from queue import Queue
import time

from pipeline import get_category_urls, get_book_urls, get_all_book_information, save_csv_and_images


def main():
    start = time.time()

    url_to_scrape = 'https://books.toscrape.com/'
    queue1 = Queue()
    queue2 = Queue()
    queue3 = Queue()

    thread_category = Thread(target=get_category_urls, args=(url_to_scrape, queue1))
    thread_book = Thread(target=get_book_urls, args=(queue1, queue2))
    thread_information = Thread(target=get_all_book_information, args=(queue2, queue3))
    thread_load = Thread(target=save_csv_and_images, args=(queue3,))

    thread_category.start()
    thread_book.start()
    thread_information.start()
    thread_load.start()

    thread_category.join()
    thread_book.join()
    thread_information.join()
    thread_load.join()

    end = time.time()
    print(f'Execution time: {end-start}')


if __name__ == "__main__":
    main()