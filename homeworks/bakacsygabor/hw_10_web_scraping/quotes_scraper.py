"""Collect every quote for the site's ten featured tags with Selenium."""

import csv
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_FILE = Path(__file__).with_name("top_ten_tag_quotes.csv")
WAIT_SECONDS = 15


def scrape_quotes(driver: webdriver.Chrome) -> list[dict[str, str]]:
    """Visit each featured tag and follow all of its pagination links."""

    driver.get(BASE_URL)
    wait = WebDriverWait(driver, WAIT_SECONDS)
    tag_links = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tag-item a.tag"))
    )
    top_tags = [(link.text.strip(), link.get_attribute("href")) for link in tag_links]
    if len(top_tags) != 10 or any(not name or not url for name, url in top_tags):
        raise RuntimeError("Could not find exactly ten featured tags.")

    rows: list[dict[str, str]] = []
    for tag, first_url in top_tags:
        next_url = first_url
        visited: set[str] = set()
        while next_url:
            if next_url in visited:
                raise RuntimeError(f"Repeated pagination link for tag {tag}: {next_url}")
            visited.add(next_url)
            driver.get(next_url)
            quotes = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".quote"))
            )
            for quote in quotes:
                rows.append(
                    {
                        "tag": tag,
                        "author": quote.find_element(By.CSS_SELECTOR, ".author").text.strip(),
                        "quote": quote.find_element(By.CSS_SELECTOR, ".text").text.strip(),
                    }
                )

            next_links = driver.find_elements(By.CSS_SELECTOR, "li.next a")
            next_url = next_links[0].get_attribute("href") if next_links else None
        print(f"Collected {len(visited)} page(s) for {tag}.")
    return rows


def main() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    with webdriver.Chrome(options=options) as driver:
        rows = scrape_quotes(driver)

    with OUTPUT_FILE.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["tag", "author", "quote"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} rows to {OUTPUT_FILE.name}.")


if __name__ == "__main__":
    main()
