import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import quotes_selectors as qs


class QuotesScraper:
    def __init__(self):
        self.base_url = "https://quotes.toscrape.com/"
        self.driver = None

    def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def get_top_tags(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, qs.TOP_TAGS_XPATH))
        )
        tag_elements = self.driver.find_elements(By.XPATH, qs.TOP_TAGS_XPATH)
        tags = [tag.text.strip() for tag in tag_elements]
        print(f"Found top {len(tags)} tags: {tags}")
        return tags

    def scrape_quotes_for_tag(self, tag):
        tag_quotes = []
        page = 1

        while True:
            url = f"{self.base_url}tag/{tag}/page/{page}/"
            print(f"Scraping: {url}")
            self.driver.get(url)

            quote_elements = self.driver.find_elements(By.CLASS_NAME, qs.QUOTE_BLOCK_CLASS_NAME)

            # Ha nincs több idézet az oldalon, elértük a pagination végét
            if not quote_elements:
                break

            for quote_el in quote_elements:
                quote_text = quote_el.find_element(By.CLASS_NAME, qs.QUOTE_TEXT_CLASS_NAME).text
                author = quote_el.find_element(By.CLASS_NAME, qs.QUOTE_AUTHOR_CLASS_NAME).text

                tag_quotes.append({
                    "tag": tag,
                    "author": author,
                    "quote": quote_text
                })

            page += 1

        return tag_quotes

    def close_webdriver(self):
        if self.driver:
            self.driver.quit()

    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False, encoding="utf-8")
        print(f"Saved {len(data)} rows to {filepath}")