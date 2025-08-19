from threading import Thread
from queue import Queue

from pipeline import get_category_urls, get_book_urls, get_all_book_information, save_csv_and_images


def main():
    url_to_scrape = 'https://books.toscrape.com/'
    queue1 = Queue()
    queue2 = Queue()
    queue3 = Queue()
    thread_number_per_worker = 10

    category_thread = Thread(target=get_category_urls, args=(url_to_scrape, queue1))
    category_thread.start()

    book_thread = Thread(target=get_book_urls, args=(queue1, queue2))
    book_thread.start()

    information_threads = []
    for _ in range(thread_number_per_worker):
        information_thread = Thread(target=get_all_book_information, args=(queue2, queue3))
        information_thread.start()
        information_threads.append(information_thread)
    
    load_threads = []
    for _ in range(thread_number_per_worker):
        load_thread = Thread(target=save_csv_and_images, args=(queue3,))
        load_thread.start()
        load_threads.append(load_thread)

    category_thread.join()
    book_thread.join()

    for _ in range(thread_number_per_worker):
        queue2.put(None)

    for information_thread in information_threads:
        information_thread.join()

    for _ in range(thread_number_per_worker):
        queue3.put(None)

    for load_thread in load_threads:
        load_thread.join()


if __name__ == "__main__":
    main()