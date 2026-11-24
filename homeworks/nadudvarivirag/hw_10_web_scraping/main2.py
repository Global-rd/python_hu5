import os
import time
from quotes_scraper2 import QuotesSrcraper
url = "https://quotes.toscrape.com/"


def main():
    SCRAPED_DATA_PATH = "homeworks/nadudvarivirag/hw_10_web_scraping/scraped_quotes_data2.csv" 
    scraper = QuotesSrcraper()
    scraper.initialize_webdriver()

    top_ten_tags = scraper.get_top_ten_tags(url)
    print("top ten tags:" , top_ten_tags)

    data = []

    #url összeállítása
    #https://quotes.toscrape.com/tag/friends/
    for tag in top_ten_tags:
        tag_url = f"{url}tag/{tag}/"

        # az adott tag url-jét adom át
        quotes_data = scraper.scrape_quotes_data(tag_url, top_ten_tags)
    
        data.extend(quotes_data)
    

    scraper.load_data_to_csv(data=data, filepath=SCRAPED_DATA_PATH)




if __name__== "__main__":
    main()