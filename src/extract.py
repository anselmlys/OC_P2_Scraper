from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

from transform import transform_rating_in_number, transform_availability_in_number


def get_all_book_information(url, queue):
    all_book_urls = []

    category_urls = get_all_categories(url)

    for category_url in category_urls:
        book_urls_by_category = get_all_books_by_category(category_url)
        all_book_urls.extend(book_urls_by_category)

    for book_url in all_book_urls:
        book_information = get_book_information(book_url)
        queue.put(book_information)

    queue.put(None)


def get_all_categories(url):
    '''Extract the URL of each category'''

    try:
        categories_urls = []

        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')

        categories = soup.find('ul', class_='nav nav-list').ul.find_all('li')
        for categorie in categories:
            category_relative_url = categorie.a.get('href')
            category_url = urljoin(page.url, category_relative_url)
            categories_urls.append(category_url)

        return categories_urls
    
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", {errc})

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error", {errh})

    except requests.exceptions.Timeout as errt:
        print("Timeout Error", {errt})

    except requests.exceptions.RequestException as errr:
        print("Request Error", {errr})

    except AttributeError as errattr:
        print(f"Attribute Error: {errattr}")
        print(f"Problematic page:\n{page.url}\n")


def get_books_from_page(url):
    '''Extract all books URLs from a specific page of a category'''

    try:
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')

        books_details = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        books_urls_from_page = []
            
        for book_detail in books_details:
            book_relative_url = book_detail.find('h3').a.get('href')
            book_url = urljoin(page.url, book_relative_url)
            books_urls_from_page.append(book_url)

        return books_urls_from_page
    
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", {errc})

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error", {errh})

    except requests.exceptions.Timeout as errt:
        print("Timeout Error", {errt})

    except requests.exceptions.RequestException as errr:
        print("Request Error", {errr})

    except AttributeError as errattr:
        print(f"Attribute Error: {errattr}")
        print(f"Problematic page:\n{page.url}\n")


def check_if_next_page(url):
    '''Check if there is a next page and return the html under next_bouton'''

    try:
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        next_bouton = soup.find('li', class_='next')
        
        return next_bouton
    
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", {errc})

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error", {errh})

    except requests.exceptions.Timeout as errt:
        print("Timeout Error", {errt})

    except requests.exceptions.RequestException as errr:
        print("Request Error", {errr})


def get_all_books_by_category(url):
    '''Extract all book URLs of a category'''

    books_urls = get_books_from_page(url)
    next_bouton = check_if_next_page(url)

    while next_bouton:
        next_relative_url = next_bouton.a.get('href')
        next_url = urljoin(url, next_relative_url)
        books_urls.extend(get_books_from_page(next_url))
        next_bouton = check_if_next_page(next_url)

    return books_urls


def get_book_information(url):
    '''Get all book information from a book page'''

    try:
        page = requests.get(url, timeout=5)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'html.parser')

        product_page_url = page.url
        title = soup.find('h1').string
        category = soup.find('ul', class_='breadcrumb').select('a')[2].get_text()
        image_relative_url = soup.find('div', class_='item active').find('img').get('src')
        image_url = urljoin(page.url, image_relative_url)
        description_zone = soup.find('div', id='product_description')
        if description_zone:
            product_description = description_zone.find_next_sibling().get_text()
        else:
            product_description = 'ND'

        rating_in_text = soup.find('p', class_='star-rating').get('class')[1]
        review_rating = transform_rating_in_number(rating_in_text)

        trs = soup.find_all('tr')
        table = {}

        for tr in trs:
            th = tr.find('th').string
            td = tr.find('td').string
            table[th] = td

        number_available = transform_availability_in_number(table)

        book_information = {
            'product_page_url': product_page_url,
            'universal_product_code': table['UPC'],
            'title': title,
            'price_including_tax': table['Price (incl. tax)'],
            'price_excluding_tax': table['Price (excl. tax)'],
            'number_available': number_available,
            'product_description': product_description,
            'category': category,
            'review_rating': review_rating,
            'image_url': image_url
            }
        
        return book_information    

    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", {errc})

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error", {errh})

    except requests.exceptions.Timeout as errt:
        print("Timeout Error", {errt})

    except requests.exceptions.RequestException as errr:
        print("Request Error", {errr})

    except AttributeError as errattr:
        print(f"Attribute Error: {errattr}")
        print(f"Problematic page:\n{product_page_url}\n")
    
    except KeyError as errk:
        print("Key Error", {errk})

