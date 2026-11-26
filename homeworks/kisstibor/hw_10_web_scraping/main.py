"""Házi feladat 10: Web Scraping:
Idézeteinek összegyűjtése https://quotes.toscrape.com/ oldalról és CSV-be mentése. """

import os
from quotes_scraper import QuotesScraper


def main():
    url = "https://quotes.toscrape.com/"
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quotes.csv")
    scraper = QuotesScraper()
    scraper.initialize_webdriver()

    try:
        tags = scraper.get_top_tags(url)
        data = []
        for tag, tag_url in tags:
            data.extend(scraper.scrape_tag(tag, tag_url))

        scraper.load_data_to_csv(data, output_path)
        print(f"Elmentve: {len(data)} idézet, {output_path}")
    finally:
        scraper.driver.quit()


if __name__ == "__main__":
    main()
