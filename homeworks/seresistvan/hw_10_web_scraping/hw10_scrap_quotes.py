import csv
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

rows = []
with webdriver.Chrome() as driver:
    driver.get("https://quotes.toscrape.com/")
    links = driver.find_elements(By.CSS_SELECTOR, ".tag-item a.tag")
    tags = [(link.text, link.get_attribute("href")) for link in links[:10]]

    for tag, url in tags:
        while url:
            driver.get(url)
            for card in driver.find_elements(By.CSS_SELECTOR, ".quote"):
                author = card.find_element(By.CSS_SELECTOR, ".author").text
                quote = card.find_element(By.CSS_SELECTOR, ".text").text
                rows.append([tag, author, quote])

            next_links = driver.find_elements(By.CSS_SELECTOR, "li.next a")
            url = next_links[0].get_attribute("href") if next_links else None

output = Path(__file__).with_name("quotes.csv")
with output.open("w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["tag", "author", "quote"])
    writer.writerows(rows)