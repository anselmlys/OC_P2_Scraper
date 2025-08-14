# OC Project 2: Scraper

This project is carried out as part of the OpenClassrooms training program. 
It collects data about the books sold on this website: https://books.toscrape.com/ and save it on csv file. It also collects all the book images in jpg format.


## Features
- Scrapes books data from all categories:
    - product page url
    - universal product code
    - title
    - price including tax
    - price excluding tax
    - number available
    - product description
    - category
    - review rating
    - image url
    - image
    
- Saves book information in separate CSV files per category.
- Saves images in jpg format organized in folders by category.


## Installation
1. Clone this repository:
```bash
git clone https://github.com/anselmlys/OC_P2_Scraper.git
```

2. Create and activate virtual environment:
```bash
python -m venv env
. env/Scripts/activate
```

3. Install dependencies:
```bash
pip install requests
pip install beautifulsoup4
```


## Usage
Run the scraper with:
```bash
python main.py
```
CSV files are saved in data/ folder and jpg are saved in media/ folder.


## Dependencies

- Python 3.10+
- requests
- beautifulsoup4


## Limitations

- If data is saved multiple times in the same day, it will create duplicates in csv file.
- If data is being saved during day change, this will split in two the currently open csv file.


## Notes

The scraper is designed for educational purposes only.


## Author

Anselmlys
