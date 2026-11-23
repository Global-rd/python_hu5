import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://quotes.toscrape.com/"

driver = webdriver.Chrome()
driver.get(BASE_URL)

tag_elements = driver.find_elements(
    By.CSS_SELECTOR, ".tag-item a"
)

top_tags = []

for element in tag_elements:
    top_tags.append(element.text)

print("Top 10 tags:")

for tag in top_tags:
    print(tag)
all_quotes = []

for tag in top_tags:
    page = 1

    while True:
        url = f"{BASE_URL}tag/{tag}/page/{page}/"
        driver.get(url)

        print(f"Scraping tag: {tag} - Page: {page}")

        quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")

        for quote in quotes:
            author = quote.find_element(By.CSS_SELECTOR, ".author").text
            text = quote.find_element(By.CSS_SELECTOR, ".text").text

            all_quotes.append({
                "tag": tag,
                "author": author,
                "quote": text
            })

        next_button = driver.find_elements(By.CSS_SELECTOR, ".next a")

        if not next_button:
            break

        page += 1

print(f"Total quotes collected: {len(all_quotes)}")
driver.quit()
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["tag", "author", "quote"]
    )

    writer.writeheader()
    writer.writerows(all_quotes)

print("CSV file successfully generated!")