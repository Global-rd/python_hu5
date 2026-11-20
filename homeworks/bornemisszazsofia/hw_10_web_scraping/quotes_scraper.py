import quotes_tags_selector as selector

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



class QuotesScraper:

    url = "https://quotes.toscrape.com"

    def initialize_webdriver(self):
        options= Options()
        self.driver = webdriver.Firefox(options=options)
        
    def get_quotes_tag(self):
        tag_names = self.driver.find_elements(by=By.XPATH, value=selector.TOP_TEN_TAG_XPATH)
        tags = [element.text for element in tag_names]
        
        return tags

    def get_tag_urls(self, tags):
        tags_urls = []
        for tag in tags:
            tag_url = f"{self.url}/tag/{tag}/"
            tags_urls.append(tag_url)
        
        return tags_urls

    def go_to_next_page(self):

        try:
            next_button = self.driver.find_element(by=By.XPATH, value=selector.NEXT_PAGE_XPATH)
            next_button.click()
            return True

        except NoSuchElementException:
            return False

    def get_quotes_text(self):
        quotes_text = self.driver.find_elements(by=By.XPATH, value=selector.QUOTES_TEXT_XPATH)
        quotes = [element.text for element in quotes_text]

        return quotes
    
    def get_quotes_author(self):
        author_name = self.driver.find_elements(by=By.XPATH, value=selector.AUTHOR_NAME_XPATH)
        authors = [element.text for element in author_name]
        
        return authors

    def scraper_quotes_data(self, url, timeout=10):
        self.driver.get(url)

        quotes_data = []

        tags = self.get_quotes_tag()
        tags_url = self.get_tag_urls(tags)

        for tag, tag_url in zip(tags, tags_url):
            self.driver.get(tag_url)
            while True:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_all_elements_located((By.XPATH, selector.QUOTES_TEXT_XPATH))
                )
                authors = self.get_quotes_author()
                quotes = self.get_quotes_text()

                if len(authors) != len(quotes):
                    print("Error: Number of authors and quotes do not match.")

                for author, quote in zip(authors, quotes):
                    quotes_data.append({
                                        "tag": tag,
                                        "author": author,
                                        "quote": quote
                                        })
                if not self.go_to_next_page(tag):
                    break

        return quotes_data

    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
