
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def main():
    options = Options()
    driver = webdriver.Chrome(options=options)

    driver.get("https://quotes.toscrape.com/")

    tags = driver.find_elements(By.CLASS_NAME, "tag-item")

    top_tags = []

    for tag in tags:
        tag_link = tag.find_element(By.CLASS_NAME, "tag")
        top_tags.append(tag_link.text)

    all_quotes_data = []

    for tag in top_tags:
        tag_url = f"https://quotes.toscrape.com/tag/{tag}/"

        print("\nFeldolgozás:", tag)

        driver.get(tag_url)

        tag_quote_count = 0

        while True:
            quotes = driver.find_elements(By.CLASS_NAME, "quote")

            for quote in quotes:
                quote_text = quote.find_element(By.CLASS_NAME, "text")
                author = quote.find_element(By.CLASS_NAME, "author")

                quote_data = {
                    "tag": tag,
                    "author": author.text,
                    "quote": quote_text.text
                }

                all_quotes_data.append(quote_data)
                tag_quote_count += 1

            next_page = driver.find_elements(
                By.XPATH, "//li[@class='next']/a"
            )

            if next_page:
                next_page[0].click()
            else:
                break

        print("Összes kinyert idézet:", tag_quote_count)

    print("\nÖsszes kinyert rekord:", len(all_quotes_data))

    driver.quit()

    df = pd.DataFrame(all_quotes_data)

    df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")

    print("\nCSV fájl sikeresen elmentve: quotes.csv")


if __name__ == "__main__":
    main()
