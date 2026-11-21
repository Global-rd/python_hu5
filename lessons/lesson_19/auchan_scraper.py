import auchan_selectors as auch

import requests
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime as dt
import pandas as pd


class AuchanScraper:

    def __init__(self):
        self._cookies_accepted = False

    def get_urls_from_sitemap(self, sitemap_url):

        print(f"Requesting all product urls from Auchan's sitemap: {sitemap_url}")

        response = requests.get(sitemap_url)

        #print(response.text[:1000])

        if response.status_code == 200:
            sitemap_tree = ET.ElementTree(ET.fromstring(response.content))
            root = sitemap_tree.getroot()

            namespace = {'ns': "http://www.sitemaps.org/schemas/sitemap/0.9"}

            urls = []

            for url in root.findall('ns:url', namespace):
                loc = url.find('ns:loc', namespace)
                if loc is not None:
                    urls.append(loc.text)
            print(f"Total urls: {len(urls)}")
            return urls
        else:
            print(f"Failed to retrieve sitemap: {response.text}")
            return []


    def initialize_webdriver(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    def accept_cookies(self, timeout=10):

        try:
            accept_button = WebDriverWait(self.driver, timeout).until(
               EC.element_to_be_clickable((By.XPATH, auch.COOKIE_ACCEPT_BUTTON))
            )
            accept_button.click()
            self._cookies_accepted = True
        except TimeoutException:
            print("Cookies panel not found, or not clickable, skipping..")

    def get_product_hierarchy(self):

        category_names = self.driver.find_elements(by=By.XPATH, value=auch.CATEGORY_HIERARCHY_XPATH)
        print(category_names)
        print(len(category_names))
        category_texts = [element.text for element in category_names[4::2]]

        return {
            "category_level1": category_texts[0],
            "category_level2": category_texts[1],
            "category_level3": category_texts[2],
            "category_level4": category_texts[3] if len(category_texts) > 3 else None,
        }

    def get_product_name(self):
        product_name = self.driver.find_element(by=By.XPATH, value=auch.PRODUCT_NAME_XPATH)
        return product_name.text

    def get_product_price(self):
        product_price = self.driver.find_element(by=By.CLASS_NAME, value=auch.PRODUCT_PRICE_CLASS_NAME)
        return int(product_price.text.replace(" Ft", "").replace(" ", ""))


    def scrape_product_data(self, url):
        print(f"Scraping {url}")
        self.driver.get(url)
        if not self._cookies_accepted:
            self.accept_cookies()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, auch.CATEGORY_HIERARCHY_XPATH))
        )
        product_hierarchy = self.get_product_hierarchy()
        product_name = self.get_product_name()
        product_price = self.get_product_price()

        return {
            "product_name": product_name,
            **product_hierarchy,
            "product_price": product_price,
            "url": url,
            "scrape_timestamp": dt.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def write_urls_to_file(urls, file_name):
        with open(file_name, "w") as file:
            for url in urls:
                file.write(url + "\n")
        print(f"URLs has been written to {file_name}")

    @staticmethod
    def read_urls_from_file(file_name):
        urls = []

        with open(file_name, "r") as file:
            for line in file:
                url = line.strip()
                if url:
                    urls.append(url)
        return urls

    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)