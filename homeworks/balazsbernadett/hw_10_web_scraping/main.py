from quotes_scraper import QuotesScraper


def main():
    SCRAPED_DATA_PATH = "homeworks/balazsbernadett/hw_10_web_scraping/scraped_quotes_data.csv"

    scraper = QuotesScraper()
    scraper.initialize_webdriver()

    top_tags = scraper.get_top_tags()
    data = []

    for tag in top_tags:
        tag_data = scraper.scrape_quotes_for_tag(tag)
        data.extend(tag_data)

    scraper.close_webdriver()
    scraper.load_data_to_csv(data=data, filepath=SCRAPED_DATA_PATH)


if __name__ == "__main__":
    main()