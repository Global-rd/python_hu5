import quotes_selectors as qs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd


class QuotesScraper:

    def __init__(self, base_url):
        self.base_url = base_url

    def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def close_webdriver(self):
        self.driver.quit()

    # main page -> aztán return top 10 tag names
    def get_top_tags(self, timeout=10):
        print(f"Collecting the top 10 tags from {self.base_url}")
        self.driver.get(self.base_url)

        tag_elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, qs.TOP_TAGS_XPATH))
        )
        tags = [element.text for element in tag_elements]
        print(f"Top 10 tags: {tags}")
        return tags

    def build_tag_url(self, tag, page_number):
        return f"{self.base_url}/tag/{tag}/page/{page_number}/"

    # list of dicts (tag, author, quote)
    def scrape_page(self, tag, page_number, timeout=10):
        url = self.build_tag_url(tag, page_number)
        print(f"Scraping {url}")
        self.driver.get(url)

        try:
            quote_elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, qs.QUOTE_CLASS_NAME))
            )
        except TimeoutException:
            print(f"No quotes found on {url}, skipping..")
            return []

        page_data = []
        for quote_element in quote_elements:
            text = quote_element.find_element(by=By.CLASS_NAME, value=qs.QUOTE_TEXT_CLASS_NAME).text
            author = quote_element.find_element(by=By.CLASS_NAME, value=qs.QUOTE_AUTHOR_CLASS_NAME).text
            page_data.append({
                "tag": tag,
                "author": author,
                "quote": text.strip("“”"),    # levágja azokat a ronda izéket
            })
        return page_data

    # ha van next page button -> True
    def has_next_page(self):
        next_buttons = self.driver.find_elements(by=By.XPATH, value=qs.NEXT_BUTTON_XPATH)
        return len(next_buttons) > 0
    
    # összes oldal per tag
    def scrape_tag(self, tag):
        tag_data = []
        page_number = 1

        while True:
            page_data = self.scrape_page(tag, page_number)
            tag_data.extend(page_data)

            if not self.has_next_page():
                break
            page_number += 1

        print(f"Tag '{tag}': {len(tag_data)} quotes on {page_number} page(s)")
        return tag_data

    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data, columns=["tag", "author", "quote"])
        df.to_csv(filepath, index=False)
        print(f"{len(df)} rows written to {filepath}")
