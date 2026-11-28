from quotes_scraper import QuotesScraper


def main():

    BASE_URL = "https://quotes.toscrape.com"
    SCRAPED_DATA_PATH = "homeworks\\nandorbarany\\hw_10_web_scraping\\top10_tags_quotes.csv"
    
    scraper = QuotesScraper(BASE_URL)
    scraper.initialize_webdriver()

    # top 10 tags
    tags = scraper.get_top_tags()

    data = []
    for tag in tags:
        tag_data = scraper.scrape_tag(tag)
        data.extend(tag_data)

    scraper.close_webdriver()

    # tag, author, quote oszlopok
    scraper.load_data_to_csv(data=data, filepath=SCRAPED_DATA_PATH)


if __name__ == "__main__":
    main()
