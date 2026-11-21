"""
A következő URL-ről https://quotes.toscrape.com selenium segítségével scrape-eld le
a top 10 tag összes idézetét (figyelj a pagination-re is). A végeredmény a következő
oszlopokból álló .csv file kell legyen, benne a lescrape-elt adattal:
- tag (az eredeti tag a top 10-ből, nem a kapcsolódó tag-ek)
- author
- quote
Csak a top 10 tag-hez tartozó idézeteket scrape-eld le. Tipp: először gyűjtsd össze a
tag-ek neveit, így tudod manipulálni az url-t.
"""

import quotes_selectors as qs
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# bongeszo
driver = webdriver.Chrome(options=Options())

# DataFrame, amibe gyujtjuk az idezeteket
df = pd.DataFrame(columns=["tag", "author", "quote"])

try:
  # megnyitjuk az oldalt
  driver.get("https://quotes.toscrape.com")

  # kigyujtjuk a tag-eket
  tags = driver.find_elements(by=By.XPATH, value=qs.TAGS_LIST)

  # loop-olunk a tag-eket es navigalunk az adott tag-re
  for tag in [tag.text for tag in tags]:

    driver.get(f"https://quotes.toscrape.com/tag/{tag}")

    # a lapozo miatt egy while, amibol akkor lepunk ki, ha nincs tobb oldal
    while True:

      quotes = driver.find_elements(by=By.XPATH, value=qs.QUOTES_LIST)

      # osszegyujtjuk az idezeteket
      for quote in quotes:

        quote_text = quote.find_element(by=By.CSS_SELECTOR, value="span.text").text
        quote_author = quote.find_element(by=By.CSS_SELECTOR, value="span:nth-of-type(2) > small").text

        df.loc[len(df)] = {
          "tag": tag,
          "author": quote_author,
          "quote": quote_text,
        }

      # van-e kovetkezo oldal, ha nincs, akkor ez egy ures tombot ad vissza
      next_page = driver.find_elements(By.CSS_SELECTOR, value="nav > ul > li.next > a")

      # ha van, akkor oda megyunk tovabb, ha nincs, akkor kilepunk a while-bol es jon a kovetkezo tag
      if next_page:
        driver.get(next_page[0].get_attribute("href"))
      else:
        break

finally:
  # bongeszo close
  driver.quit()

# idezetek CSV-be
df.to_csv("quotes.csv", index=False, encoding="utf-8")
