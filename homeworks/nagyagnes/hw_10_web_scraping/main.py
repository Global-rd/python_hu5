from quotes_scraper import QuotesScraper


def main():

    SCRAPED_DATA_PATH = "homeworks/nagyagnes/hw_10_web_scraping/scraped_quotes.csv"
    scraper = QuotesScraper()

    scraper.initialize_webdriver()

    # 1. lépés: top 10 tag (quotes_scraper.py-ból)
    tags = scraper.get_top_tags()
    print(tags)

    # 2 lépés: idézetek tag-enként, lapozással (quotes_scraper.py-ból)
    all_quotes = []

    for tag in tags:
        quotes = scraper.get_quotes(tag)
        all_quotes.extend(quotes)

    print(len(all_quotes))

    # 3. lépés: mentés .csv-be (tag, author, quote)
    scraper.load_data_to_csv(data=all_quotes, filepath=SCRAPED_DATA_PATH)


if __name__ == "__main__":
    main()
