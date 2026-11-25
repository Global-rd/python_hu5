from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import quote_selector as qs
import pandas as pd

class QuoteScraper:

    url = 'http://quotes.toscrape.com/'

    def __init__(self):
        self.driver = None

        
    def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def _quote_elements(self):
        return self.driver.find_elements(By.XPATH, qs.QUOTE_XPATH)

    def get_top_tags(self):
        self.driver.get(self.url)
        return [
            (tag.text, tag.get_attribute('href'))
            for tag in self.driver.find_elements(By.XPATH, qs.TOP_TAGS_XPATH)
        ]

    def get_quote_tags(self, url):
        self.driver.get(url)
        return [
            ", ".join(tag.text for tag in quote.find_elements(By.XPATH, qs.QUOTE_TAG_XPATH))
            for quote in self._quote_elements()
        ]

    def get_quote_authors(self, url):
        self.driver.get(url)
        return [
            quote.find_element(By.XPATH, qs.QUOTE_AUTHOR_XPATH).text
            for quote in self._quote_elements()
        ]

    def get_quote_texts(self, url):
        self.driver.get(url)
        return [
            quote.find_element(By.XPATH, qs.QUOTE_TEXT_XPATH).text
            for quote in self._quote_elements()
        ]

    def go_to_next_page(self):
        next_buttons = self.driver.find_elements(By.XPATH, qs.NEXT_PAGE_XPATH)
        if not next_buttons:
            return False
        next_buttons[0].click()
        return True

    def quotes_data(self, url=None):
        if url is not None:
            self.driver.get(url)
        return [
            (
                ", ".join(tag.text for tag in quote.find_elements(By.XPATH, qs.QUOTE_TAG_XPATH)),
                quote.find_element(By.XPATH, qs.QUOTE_AUTHOR_XPATH).text,
                quote.find_element(By.XPATH, qs.QUOTE_TEXT_XPATH).text,
            )
            for quote in self._quote_elements()
        ]

    def scrape_quotes(self):
        top_tags = self.get_top_tags()
        quotes_by_author_and_text = {}

        for tag_name, tag_url in top_tags:
            self.driver.get(tag_url)
            while True:
                for _, author, text in self.quotes_data():
                    quotes_by_author_and_text.setdefault((author, text), set()).add(tag_name)
                if not self.go_to_next_page():
                    break

        return [
            (
                ', '.join(tag_name for tag_name, _ in top_tags if tag_name in matching_tags),
                author,
                text,
            )
            for (author, text), matching_tags in quotes_by_author_and_text.items()
        ]

    @staticmethod
    def load_quotes_to_csv(data, filepath):
        df = pd.DataFrame(data, columns=['Quote Tag', 'Quote Author', 'Quote Text'])
        df.to_csv(filepath, index=False)