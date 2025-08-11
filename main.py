import re
import requests
from pathlib import Path
import csv
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

all_books = {}

#Extrait product_page_url
product_page_url = page.url

#Extrait le titre du livre
title = soup.find('h1').string

#Create a dictionnary to stock the book info in all_books
all_books[product_page_url] = {'title': title}

#Extrait category du livre
category = soup.find('ul', class_='breadcrumb').select('a')[2].get_text()

#Extrait l'url de l'image
image_url = soup.find('div', class_='item active').find('img').get('src')

#Extrait la description du livre
product_description = soup.find('div', id='product_description').find_next_sibling().get_text()

#Extrait de review_rating
#Le rating se fait sur 5, à voir s'il faut convertir dans le futur
rating_in_text = soup.find('p', class_='star-rating').get('class')[1]
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

#Extrait le tableau "Product Information"
trs = soup.find_all('tr')
table = {}

for tr in trs:
    th = tr.find('th').string
    td = tr.find('td').string
    table[th] = td

#Retire texte de la donnée "Availability"
availability = re.sub("[^0-9]", "", table['Availability'])
        
#Ajoute les info collectées au dictionnaire du livre
all_books[product_page_url]['category'] = category
all_books[product_page_url]['image_url'] = image_url
all_books[product_page_url]['product_description'] = product_description
all_books[product_page_url]['review_rating'] = review_rating
all_books[product_page_url]['number_available'] = availability

all_books[product_page_url]['universal_product_code'] = table['UPC']
all_books[product_page_url]['price_including_tax'] = table['Price (incl. tax)']
all_books[product_page_url]['price_excluding_tax'] = table['Price (excl. tax)']

#Ajoute product_page_url dans le dictionnaire pour pouvoir accéder à l'info
all_books[product_page_url]['product_page_url'] = product_page_url


#Sauvegarde les info du livre dans un fichier CSV
Path("data").mkdir(parents=True, exist_ok=True)

with open('data/data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=all_books[product_page_url].keys())
    writer.writeheader()
    writer.writerow(all_books[product_page_url])