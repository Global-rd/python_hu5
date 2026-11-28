from pathlib import Path

from quote_scraper import QuoteScraper


def main():
    scraper = QuoteScraper()

    try:
        scraper.initialize_webdriver()
        quotes_data = scraper.scrape_quotes()
        output_path = Path(__file__).resolve().with_name('scraped_quotes.csv')
        scraper.load_quotes_to_csv(data=quotes_data, filepath=output_path)
    finally:
        if scraper.driver is not None:
            scraper.driver.quit()


if __name__ == '__main__':
    main()

    