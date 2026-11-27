
# a cookiek kezelése miatt kell a végén az init
from selenium import webdriver #selenium által vezérelt böngésző

# itt állítjuk be hogy milyen böngészőt használjon és milyen módban (fejlesztésnél látjuk, egyébként nem kell)
from selenium.webdriver.chrome.options import Options

# a módja annak, hogyan azonosítjuk az elemeket
from selenium.webdriver.common.by import By

# futni fog egy böngésző. A script ebből próbálja kinyerni az adatokat -> hibák (pl. még nincs ott az adat)
# -> várakoztatás, hibakezelés
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime as dt
import time
import pandas as pd
import quotes_selector as quo



class QuotesSrcraper():
    
    def initialize_webdriver(self):
        options = Options() #itt állítanánk be hogy headless módban legyen vagy sem a böngésző
        self.driver = webdriver.Chrome(options=options)

    def go_to_next_page(self):
        try:
            next_button = self.driver.find_element(By.XPATH, value=quo.NEXT_BUTTON_XPATH)
            next_button.click()
            time.sleep(3)
            return True
        except NoSuchElementException:
            return False

    def get_top_ten_tags(self):
        # elements-et használunk mert többet keresünk
        # megadjuk hogy xpath alapján azonosítjuk
        tag_names = self.driver.find_elements(by=By.XPATH, value=quo.TOP_TEN_TAG_XPATH) # ez így egy html objektum csak -> szöveggé
        #print(tag_names)
        #print(len(tag_names))
        tag_texts = [element.text for element in tag_names]
        print(tag_texts)
        return tag_texts

    def get_top_ten_tag_urls(self, tags):
        tag_urls = []
        
        for tag in tags:
            tag_url = f"https://quotes.toscrape.com/tag/{tag}/"
            tag_urls.append(tag_url)

        return tag_urls

    def scrape_top_teng_tags(self,url):
        self.driver.get(url)
        tags = self.get_top_ten_tags()
        urls = self.get_top_ten_tag_urls(tags)

        all_data = []
        for i in range(len(tags)):
            tag = tags[i]
            url = urls[i]

            data = self.scrape_quotes_data(tag,url)
            all_data.append(data)
        return all_data


    def get_author(self):
        author = self.driver.find_elements(by=By.XPATH, value=quo.AUTHOR_XPATH)
        author_texts = [element.text for element in author]
        
        return author_texts

    def get_quotes(self):
        quote = self.driver.find_elements(by=By.XPATH, value=quo.QUOTE_XPATH)
        quote_texts = [element.text for element in quote]
        return quote_texts

      
    def scrape_quotes_data(self, tag, url):
        print(f"Scraping {url}")
        self.driver.get(url)

        author = []
        quote = []
        

        while True:

            author.extend(self.get_author())
            quote.extend(self.get_quotes())

            if not self.go_to_next_page():
                print("Last page")
                break

        
        return {
            "tag": tag,
            "author": author,
            "quote": quote
            }

  
        
    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data)
        # azért hagytam benne, mert így átláthatóbb számomra az eredmény
        df = df.explode(["author", "quote"])
        df.to_csv(filepath, sep = ",", index=False)

