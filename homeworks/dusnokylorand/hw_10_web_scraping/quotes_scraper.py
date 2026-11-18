import os
from selenium.webdriver.chrome.service import Service

import csv
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

BASE_URL = "https://quotes.toscrape.com/"


def get_top_tags(driver):
    driver.get(BASE_URL)

    tag_elements = driver.find_elements(
        By.CSS_SELECTOR,
        ".tag-item a.tag"
    )

    top_tags = []

    for element in tag_elements:
        top_tags.append(element.text)

    return top_tags


def scrape_quotes_for_tag(driver, tag):
    results = []
    page_number = 1

    while True:
        url = f"{BASE_URL}tag/{tag}/page/{page_number}/"
        driver.get(url)

        quote_elements = driver.find_elements(
            By.CLASS_NAME,
            "quote"
        )

        if not quote_elements:
            break

        for quote_element in quote_elements:
            quote_text = quote_element.find_element(
                By.CLASS_NAME,
                "text"
            ).text

            author = quote_element.find_element(
                By.CLASS_NAME,
                "author"
            ).text

            results.append(
                {
                    "tag": tag,
                    "author": author,
                    "quote": quote_text,
                }
            )

        try:
            driver.find_element(
                By.CSS_SELECTOR,
                "li.next a"
            )

            page_number += 1

        except NoSuchElementException:
            break

    return results


def save_to_csv(data):
    output_path = Path(__file__).with_name("quotes.csv")

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:

        fieldnames = [
            "tag",
            "author",
            "quote",
        ]

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(data)

    print(
        f"\nCSV file successfully created: {output_path}"
    )


def main():
    driver_path = os.getenv("CHROMEDRIVER_PATH")

    if driver_path:
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
    else:
        driver = webdriver.Chrome()

    all_quotes = []

    try:
        top_tags = get_top_tags(driver)

        print("Top 10 tags:")
        print(top_tags)

        for tag in top_tags:
            print(
                f"\nScraping tag: {tag}"
            )

            tag_quotes = scrape_quotes_for_tag(
                driver,
                tag,
            )

            all_quotes.extend(
                tag_quotes
            )

            print(
                f"Collected quotes: {len(tag_quotes)}"
            )

        save_to_csv(all_quotes)

        print(
            f"\nTotal collected rows: {len(all_quotes)}"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    main()