# feladat:
# kiszedni a 10- taget -> listában?
# kiszedni a z idézetek tagjeit, az összes oldalról! -> összehasonlítani
# ez alapaján leszűrni. Amiben szerepel a tag
# csv 3 oszloppal, a felesleges tageket droppolni
# next gombot meg kell keresni

import os
import time
from quotes_scraper import QuotesSrcraper
url = "https://quotes.toscrape.com/"


def main():
    SCRAPED_DATA_PATH = "homeworks/nadudvarivirag/hw_10_web_scraping/scraped_quotes_data.csv" 
    scraper = QuotesSrcraper()
    scraper.initialize_webdriver()

    data = []
    quotes_data = scraper.scrape_quotes_data(url)
    
    data.append(quotes_data)
    

    scraper.load_data_to_csv(data=data, filepath=SCRAPED_DATA_PATH)




if __name__== "__main__":
    main()