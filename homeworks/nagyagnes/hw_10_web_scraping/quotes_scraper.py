import quotes_selectors as qs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd


class QuotesScraper:

    # Selenium: Chrome indítása
    def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    # 1. lépés: top 10 tag nevének összegyűjtése
    def get_top_tags(self):
        self.driver.get("https://quotes.toscrape.com/")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, qs.TOP_TAGS_XPATH)
            )
        )

        tag_elements = self.driver.find_elements(
            by=By.XPATH,
            value=qs.TOP_TAGS_XPATH
    )

        tags = [element.text for element in tag_elements]

        return tags

    # idézet szövege az idézetdobozon belül
    def get_quote_text(self, quote_element):
        quote_text = quote_element.find_element(
            by=By.XPATH,
            value=qs.QUOTE_TEXT_XPATH
        )
        return quote_text.text

    # idézet szerzője az idézetdobozon belül
    def get_quote_author(self, quote_element):
        author = quote_element.find_element(
            by=By.XPATH,
            value=qs.QUOTE_AUTHOR_XPATH
        )
        return author.text

    # 2. lépés: egy tag összes idézete, lapozással
    def get_quotes(self, tag):
        quotes = []
        page = 1
        while True:
            # URL a tag nevéből és az oldalszámból
            url = f"https://quotes.toscrape.com/tag/{tag}/page/{page}/"
            self.driver.get(url)
            print(url)
        #url = f"https://quotes.toscrape.com/tag/{tag}/"
        #self.driver.get(url)

            quote_elements = self.driver.find_elements(
                by=By.XPATH,
                value=qs.QUOTE_CONTAINER_XPATH
            )
            # lapozás vége: üres oldal
            if not quote_elements:
                break

            for quote_element in quote_elements:
                quote_text = self.get_quote_text(quote_element)
                author = self.get_quote_author(quote_element)

                # csv oszlopok: tag (az eredeti top 10-es), author, quote
                quote_data = {
                    "tag": tag,
                    "author": author,
                    "quote": quote_text
                }
                quotes.append(quote_data)
            page += 1
        return quotes

    # 3. lépés: mentés .csv-be
    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)