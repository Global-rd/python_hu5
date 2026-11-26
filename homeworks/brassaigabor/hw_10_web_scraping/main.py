from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv

# --------------------------------------------------
def datas_to_csv(datas):
    # CSV file name
    csv_filename = "./quotes.csv"

    # Define the field names (headers)
    fieldnames = ["tag", "author", "quote"]

    # Writing to CSV
    with open(
        csv_filename,
        mode='w',
        newline='',
        encoding='utf-8-sig'
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # oszlop nevek
        writer.writerows(datas)  # adatok

# ------------------------------------------------
def get_quote(url, driver, tag):
    driver.get(url)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.quote")
        )
    )
    elements = driver.find_elements(By.CSS_SELECTOR, "div.quote")
    quotes_data = []

    for i in elements:
        quotes = i.find_element(By.CSS_SELECTOR, 'span.text')
        authors = i.find_element(By.CSS_SELECTOR, 'small.author')
        quotes_data.append(
            {
            "tag" : tag,
            "author" : authors.text,
            "quote" : quotes.text,
            }
        )
#    return quotes_data

# ------------- main -----------------------------
def main():
    BASE_URL = "https://quotes.toscrape.com/"
    driver = webdriver.Chrome()
    try:
        driver.get(BASE_URL)
        elements = driver.find_elements(By.CSS_SELECTOR, ".tags-box a.tag")

        # ------ tag-ek osszegyujtese ----------------
        tops = {}
        for i in elements:
            # --- tag, url ---
            tops[i.text] = i.get_attribute('href')
#        print(tops)
        print(f"Talált tagek száma: {len(tops)}")

        # ----- tag-hez tartozo lap megnyitasa -----------
        quotes_data = []
        for tag, url in tops.items():
    #        print(tag, url)
            current_url = url
            while current_url:
                quotes_data.extend(get_quote(current_url, driver, tag))
                next_pages = driver.find_elements(By.CSS_SELECTOR, "li.next a")
                if next_pages:
                    current_url = next_pages[0].get_attribute('href')
                else:
                    current_url = None
    finally:
        driver.quit()

    if quotes_data:
        datas_to_csv(quotes_data)
    else:
        print("Nem sikerült idézeteket gyűjteni!")

# ------------------------------------------
if __name__ == "__main__":
    main()
