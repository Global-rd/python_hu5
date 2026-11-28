import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import quotes_selectors as qs


class QuotesScraper:
    """
    A quotes.toscrape.com top 10 tagjének összes idézetét gyűjti össze Seleniummal
    (a lesson_19/auchan_scraper.py AuchanScraper osztályának mintájára).
    """

    def __init__(self, headless: bool = False, timeout: int = 10):
        self.headless = headless  # False: látszik a Chrome-ablak, True: a háttérben fut
        self.timeout = timeout
        self.driver = None

    # -------------------------------------------------------------------------
    # Böngésző indítása és bezárása
    # -------------------------------------------------------------------------

    def initialize_webdriver(self) -> None:
        options = Options()
        if self.headless:
            options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)

    def close(self) -> None:
        if self.driver:
            self.driver.quit()

    # -------------------------------------------------------------------------
    # 1. lépés: a top 10 tag összegyűjtése a főoldalról
    # -------------------------------------------------------------------------

    def get_top_tags(self) -> list[dict]:
        """
        Visszaadja a top 10 tag nevét és oldalának URL-jét, pl.
        {"name": "love", "url": "https://quotes.toscrape.com/tag/love/"}
        """
        print(f"Opening {qs.BASE_URL} to collect the top 10 tags...")
        self.driver.get(qs.BASE_URL)

        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, qs.TOP_TAGS_CSS))
        )
        tag_elements = self.driver.find_elements(By.CSS_SELECTOR, qs.TOP_TAGS_CSS)

        tags = [
            {"name": element.text.strip(), "url": element.get_attribute("href")}
            for element in tag_elements
        ]
        print(f"Top tags found ({len(tags)}): {[tag['name'] for tag in tags]}")
        return tags

    # -------------------------------------------------------------------------
    # 2. lépés: egy oldal idézeteinek kiolvasása
    # -------------------------------------------------------------------------

    @staticmethod
    def clean_quote_text(text: str) -> str:
        """Levágja a szóközöket és az idézet körüli „” jeleket."""
        return text.strip().strip("“”\"").strip()

    def scrape_current_page(self, tag_name: str) -> list[dict]:
        """Az éppen megnyitott oldal összes idézete, a top 10-es tag nevével."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, qs.QUOTE_CSS))
            )
        except TimeoutException:
            print(f"  No quotes found on {self.driver.current_url}, skipping page.")
            return []

        quotes = []
        for quote_element in self.driver.find_elements(By.CSS_SELECTOR, qs.QUOTE_CSS):
            text = quote_element.find_element(By.CSS_SELECTOR, qs.QUOTE_TEXT_CSS).text
            author = quote_element.find_element(By.CSS_SELECTOR, qs.QUOTE_AUTHOR_CSS).text
            quotes.append({
                "tag": tag_name,  # az eredeti top 10-es tag, NEM a kapcsolódó tagek
                "author": author.strip(),
                "quote": self.clean_quote_text(text),
            })
        return quotes

    def get_next_page_url(self) -> str | None:
        """A "Next" gomb linkje, vagy None, ha ez az utolsó oldal."""
        next_links = self.driver.find_elements(By.CSS_SELECTOR, qs.NEXT_PAGE_CSS)
        return next_links[0].get_attribute("href") if next_links else None

    # -------------------------------------------------------------------------
    # 3. lépés: egy tag összes oldala (pagination), majd mind a 10 tag
    # -------------------------------------------------------------------------

    def scrape_tag(self, tag: dict) -> list[dict]:
        """Végiglapozza a tag összes oldalát, amíg van "Next" gomb."""
        tag_quotes = []
        url = tag["url"]
        page = 1

        while url:
            print(f"  [{tag['name']}] page {page}: {url}")
            self.driver.get(url)
            tag_quotes.extend(self.scrape_current_page(tag["name"]))
            url = self.get_next_page_url()
            page += 1

        print(f"  [{tag['name']}] {len(tag_quotes)} quotes")
        return tag_quotes

    def scrape_top_tags(self) -> list[dict]:
        all_quotes = []
        for tag in self.get_top_tags():
            all_quotes.extend(self.scrape_tag(tag))
        return all_quotes

    # -------------------------------------------------------------------------
    # Mentés
    # -------------------------------------------------------------------------

    @staticmethod
    def save_to_csv(data: list[dict], filepath) -> pd.DataFrame:
        # utf-8-sig: így az Excel is helyesen mutatja a speciális karaktereket
        df = pd.DataFrame(data, columns=["tag", "author", "quote"])
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
        print(f"Saved {len(df)} rows to {filepath}")
        return df
