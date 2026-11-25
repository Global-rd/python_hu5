
from quotes_scraper import QuotesScraper
from pathlib import Path


def main():

    output_path = Path(__file__).resolve().parent / "quotes.csv"

    scraper = QuotesScraper()
    scraper.initialize_webdriver()


    try:
        data = scraper.scrape_all_tags()

        scraper.load_data_to_csv(data, output_path)

        print(f"Total number of quotes: {len(data)}")
        print(f"CSV saved to: {output_path}")

    finally:
        scraper.load_data_to_csv(data, output_path)
        scraper.validate_csv(output_path, data)
        scraper.close_webdriver()


if __name__ == "__main__":
    main()
