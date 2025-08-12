import requests
from bs4 import BeautifulSoup

from transform import transform_rating_in_number, transform_availability_in_number

def get_book_information(url):
    try:
        page = requests.get(url, timeout=5)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, 'html.parser')

        product_page_url = page.url
        title = soup.find('h1').string
        category = soup.find('ul', class_='breadcrumb').select('a')[2].get_text()
        image_url = soup.find('div', class_='item active').find('img').get('src')
        product_description = soup.find('div', id='product_description').find_next_sibling().get_text()
        
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
        raise

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error", {errh})
        raise

    except requests.exceptions.Timeout as errt:
        print("Timeout Error", {errt})
        raise

    except requests.exceptions.RequestException as errr:
        print("Request Error", {errr})
        raise

    except AttributeError as errattr:
        print(f"Attribute Error: {errattr}")
        raise
    
    except KeyError as errk:
        print("Key Error", {errk})
        raise

