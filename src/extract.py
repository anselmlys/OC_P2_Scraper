import re
import requests
from bs4 import BeautifulSoup


def get_book_information(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_page_url = page.url
    title = soup.find('h1').string
    category = soup.find('ul', class_='breadcrumb').select('a')[2].get_text()
    image_url = soup.find('div', class_='item active').find('img').get('src')
    product_description = soup.find('div', id='product_description').find_next_sibling().get_text()
    rating_in_text = soup.find('p', class_='star-rating').get('class')[1]

    trs = soup.find_all('tr')
    table = {}

    for tr in trs:
        th = tr.find('th').string
        td = tr.find('td').string
        table[th] = td

    #Le rating se fait sur 5, à voir s'il faut convertir dans le futur
    rating_in_text = rating_in_text.lower()

    match rating_in_text:
        case "zero":
            review_rating=0
        case "one":
            review_rating=1
        case "two":
            review_rating=2
        case "three":
            review_rating=3
        case "four":
            review_rating=4
        case "five":
            review_rating=5
        case _:
            review_rating="ND"

    #Retire texte de la donnée "Availability"
    availability = re.sub("[^0-9]", "", table['Availability'])

    #Create a dictionnary to stock the book info in all_books
    book_information = {'title': title}
            
    #Ajoute les info collectées au dictionnaire du livre
    book_information['product_page_url'] = product_page_url
    book_information['category'] = category
    book_information['image_url'] = image_url
    book_information['product_description'] = product_description
    book_information['review_rating'] = review_rating
    book_information['number_available'] = availability

    book_information['universal_product_code'] = table['UPC']
    book_information['price_including_tax'] = table['Price (incl. tax)']
    book_information['price_excluding_tax'] = table['Price (excl. tax)']

    return book_information
