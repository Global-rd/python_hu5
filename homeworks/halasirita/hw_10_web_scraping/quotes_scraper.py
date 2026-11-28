
import quotes_selectors as qs
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By


class QuotesScraper:

    def initialize_webdriver(self):
        self.driver = webdriver.Chrome()

    def get_top_tags(self):
        self.driver.get("https://quotes.toscrape.com/")

        tag_elements = self.driver.find_elements(
            By.CSS_SELECTOR, qs.TOP_TAGS
        )

        tags = []

        for element in tag_elements:
            tags.append(element.text)

        return tags

    def close_webdriver(self):
        self.driver.quit()


    def scrape_page(self, tag, page=1):

        url = f"https://quotes.toscrape.com/tag/{tag}/page/{page}/"
        self.driver.get(url)

        quote_elements = self.driver.find_elements(
            By.CSS_SELECTOR, qs.QUOTE_CONTAINER
        )

        data = []

        for element in quote_elements:

            author = element.find_element(
                By.CSS_SELECTOR, qs.QUOTE_AUTHOR
            ).text

            quote = element.find_element(
                By.CSS_SELECTOR, qs.QUOTE_TEXT
            ).text

            data.append({
                "tag": tag,
                "author": author,
                "quote": quote
            })

        return data


    def scrape_tag(self, tag):

        data = []
        page = 1

        while True:

            page_data = self.scrape_page(tag, page)
            data.extend(page_data)

            print(f"Tag: {tag}, Page: {page}, Quotes: {len(page_data)}")

            next_button = self.driver.find_elements(
                By.CSS_SELECTOR, qs.NEXT_PAGE
            )

            if not next_button:
                break

            page += 1

        return data


    def scrape_all_tags(self):

        tags = self.get_top_tags()
        all_data = []

        for tag in tags:

            tag_data = self.scrape_tag(tag)
            all_data.extend(tag_data)

            print(f"Completed tag: {tag}, Total: {len(tag_data)}")

        return all_data


    @staticmethod
    def load_data_to_csv(data, filepath):

        df = pd.DataFrame(
            data,
            columns=["tag", "author", "quote"]
        )

        df.to_csv(
            filepath,
            index=False,
            encoding="utf-8"
        )


    @staticmethod
    def validate_csv(filepath, data):

        df = pd.read_csv(
            filepath,
            encoding="utf-8",
            dtype=str,
            keep_default_na=False
        )

        expected = pd.DataFrame(
            data,
            columns=["tag", "author", "quote"]
        )

        checks = {
            "Correct columns":
                list(df.columns) == ["tag", "author", "quote"],

            "Correct record count":
                len(df) == len(data),

            "Ten unique tags":
                df["tag"].nunique() == 10,

            "No empty fields":
                not df.replace(
                    r"^\s*$", pd.NA, regex=True
                ).isna().any().any(),

            "No duplicate records":
                df.duplicated().sum() == 0,

            "Data integrity":
                df.equals(expected)
        }

        for name, result in checks.items():
            print(f"{name}: {'PASS' if result else 'FAIL'}")

        if not all(checks.values()):
            raise ValueError("Data validation failed.")
