from threading import Thread
from queue import Queue
import time

from extract import get_all_book_information
from load import save_csv_and_images


def main():
    start = time.time()

    url_to_scrape = 'https://books.toscrape.com/'
    book_queue = Queue()

    load_thread = Thread(target=save_csv_and_images, args=(book_queue,))
    load_thread.start()

    extract_thread = Thread(target=get_all_book_information, 
                            args=(url_to_scrape, book_queue))
    extract_thread.start()
    
    extract_thread.join()
    load_thread.join()

    end = time.time()
    print(f'Execution time: {end-start}')


if __name__ == "__main__":
    main()