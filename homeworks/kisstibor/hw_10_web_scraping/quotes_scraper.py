"""Selenium-alapú idézetgyűjtés és az eredmény mentése CSV-fájlba."""

import quotes_selectors as selectors
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class QuotesScraper:
    """A kiemelt címkék és a hozzájuk tartozó idézetek feldolgozója.
    Az adatgyűjtő metódusok előtt meg kell hívni az initialize_webdriver
    metódust. A létrehozott böngészőt a hívónak kell bezárnia.
    """

    def initialize_webdriver(self):
        """Elindítja a Chrome-böngészőt a Selenium WebDriverrel."""
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def get_top_tags(self, url):
        """Visszaadja a főoldalon található tíz kiemelt címkét és URL-jüket.
        Args:
            url: A főoldal címe.
        Returns:
            A címkenevekből és URL-ekből álló párok listája.
        Raises:
            ValueError: Ha nem pontosan tíz érvényes címke található.
            TimeoutException: Ha a címkék nem jelennek meg időben.
        """
        self.driver.get(url)
        tag_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, selectors.TOP_TAGS_XPATH))
        )
        tags = [(element.text.strip(), element.get_attribute("href")) for element in tag_elements]
        if len(tags) != 10 or any(not name or not url for name, url in tags):
            raise ValueError("A főoldalon nem található pontosan 10 érvényes kiemelt címke.")
        return tags

    def get_quote_author(self, quote_element):
        """Visszaadja az átadott idézetelem szerzőjének nevét."""
        author = quote_element.find_element(by=By.CLASS_NAME, value=selectors.AUTHOR_CLASS_NAME)
        return author.text

    def get_quote_text(self, quote_element):
        """Visszaadja az átadott idézetelem szövegét."""
        quote_text = quote_element.find_element(by=By.CLASS_NAME, value=selectors.QUOTE_TEXT_CLASS_NAME)
        return quote_text.text

    def scrape_tag(self, tag, url):
        """Összegyűjti egy kiemelt címke idézeteit az összes lapról.
        Args:
            tag: A feldolgozott kiemelt címke neve.
            url: A címke első oldalának címe.
        Returns:
            Szótárak listája, amelyek kulcsai: tag, author és quote.
            A tag értéke minden sorban az átadott kiemelt címke.
        Raises:
            ValueError: Ha a következő oldal hivatkozásából hiányzik az URL.
            TimeoutException: Ha az idézetek nem jelennek meg időben.
        """
        data = []
        while url:
            print(f"Címke: {tag}, oldal: {url}")
            self.driver.get(url)
            quote_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, selectors.QUOTE_CLASS_NAME))
            )
            for element in quote_elements:
                author = self.get_quote_author(element)
                quote_text = self.get_quote_text(element)
                data.append({
                    "tag": tag,
                    "author": author,
                    "quote": quote_text,
                })

            next_links = self.driver.find_elements(by=By.XPATH, value=selectors.NEXT_PAGE_XPATH)
            if next_links:
                url = next_links[0].get_attribute("href")
                if not url:
                    raise ValueError("A következő oldal hivatkozásából hiányzik az URL.")
            else:
                url = None
        return data

    @staticmethod
    def load_data_to_csv(data, filepath):
        """Az idézeteket UTF-8 BOM-os CSV-fájlba menti indexoszlop nélkül.
        Args:
            data: Az idézeteket tartalmazó szótárak listája.
            filepath: A kimeneti CSV-fájl útvonala.
        """
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
