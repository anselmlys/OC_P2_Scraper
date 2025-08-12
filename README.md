# OC Project 2: Scraper

This project is carried out as part of the OpenClassrooms training program. 
It collects data about the books sold on this website: https://books.toscrape.com/ and save it on a csv file.


## Features
- Scrapes: all books information from a specific category
- Saves data in CSV format


## Installation
1. Clone this repository:
```bash
git clone https://github.com/anselmlys/OC_P2_Scraper.git
```

2. Create and activate virtual environment (in git bash):
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
Scraped CSV file is saved in data/ folder.


## Dependencies

- Python 3.10+
- requests
- beautifulsoup4


## Limitations

- If data is saved multiple times in the same hour, it will create duplicates in csv file.
- If data is saved while the hour changes, this will split the csv file in two.


## Notes

The scraper is designed for educational purposes only.


## Author

Anselmlys
