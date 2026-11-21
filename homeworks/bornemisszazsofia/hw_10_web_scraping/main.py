from quotes_scraper import QuotesScraper


def main():
    
    SCRAPED_QUOTES_FILE_PATH = "homeworks/bornemisszazsofia/hw_10_web_scraping/scraped_top_ten_tag_quotes.csv"
    
    scraper = QuotesScraper()
    
    scraper.initialize_webdriver()

    quotes_data = scraper.scraper_quotes_data(scraper.url)

    scraper.load_data_to_csv(data=quotes_data, filepath=SCRAPED_QUOTES_FILE_PATH)

    scraper.driver.quit()



if __name__ == "__main__":
    main()