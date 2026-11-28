from pathlib import Path

from quotes_scraper import QuotesScraper

# A CSV mindig a main.py mellé kerül, bárhonnan is indítjuk
OUTPUT_PATH = Path(__file__).parent / "top10_tag_quotes.csv"


def main():
    scraper = QuotesScraper(headless=False)  # látszik a Chrome-ablak

    try:
        scraper.initialize_webdriver()
        data = scraper.scrape_top_tags()
    finally:
        # Hiba esetén is bezárjuk a böngészőt
        scraper.close()

    df = scraper.save_to_csv(data, OUTPUT_PATH)

    print("\nQuotes per tag:")
    print(df["tag"].value_counts().to_string())


if __name__ == "__main__":
    main()
