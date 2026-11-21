import os
import csv
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# 1. Böngésző elindítása és a főoldal megnyitása
driver = webdriver.Chrome()
base_url = "https://quotes.toscrape.com/"
driver.get(base_url)

# 2. A Top 10 tag nevének összegyűjtése
tag_elements = driver.find_elements(By.CSS_SELECTOR, "span.tag-item a.tag")
top_tags = [tag.text for tag in tag_elements]

print(f"Megtalált Top 10 tag: {top_tags}")

scraped_data = []

# 3. Végigmegyünk a Top 10 tag-en és az oldalaikon (pagination)
for tag in top_tags:
    page = 1
    while True:
        # URL manipulálása a tag és az oldalszám alapján
        url = f"{base_url}tag/{tag}/page/{page}/"
        driver.get(url)

        # Idézet blokkok megkeresése az oldalon
        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        # Ha nincs több idézet az oldalon, kilépünk a ciklusból és jöhet a következő tag
        if not quotes:
            break

        for q in quotes:
            quote_text = q.find_element(By.CLASS_NAME, "text").text
            author = q.find_element(By.CLASS_NAME, "author").text

            # Eredeti tag, szerző és idézet mentése
            scraped_data.append({"tag": tag, "author": author, "quote": quote_text})

        # Ellenőrizzük, van-e "Next" gomb (lapozás)
        try:
            driver.find_element(By.CSS_SELECTOR, "li.next a")
            page += 1
        except NoSuchElementException:
            # Ha nincs "Next" gomb, elértük az adott tag utolsó oldalát
            break

driver.quit()

# 4. Adatok mentése CSV fájlba (közvetlenül a .py fájl mellé)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_dir, "top_10_tags_quotes.csv")
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["tag", "author", "quote"])
    writer.writeheader()
    writer.writerows(scraped_data)

print(
    f"Kész! Összesen {len(scraped_data)} idézet lementve a(z)"
    f" '{csv_filename}' fájlba."
)
