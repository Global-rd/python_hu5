
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

    def get_author(self):
        author = self.driver.find_elements(by=By.XPATH, value=quo.AUTHOR_XPATH)
        author_texts = [element.text for element in author]
        
        return author_texts

    def get_quotes(self):
        quote = self.driver.find_elements(by=By.XPATH, value=quo.QUOTE_XPATH)
        quote_texts = [element.text for element in quote]
        return quote_texts

    def get_quote_tags(self):
        quote_tags = self.driver.find_elements(by=By.XPATH, value=quo.QUOTE_TAGS_XPATH)
        quote_tags_texts = [element.text for element in quote_tags]
        
        return quote_tags_texts
    
    def compare_tags(self, top_ten_tags, quotes_tags):
        result = []
        for tag_list in quotes_tags:
            tags = tag_list.split()

            for tag in tags:
                if tag in top_ten_tags:
                    result.append(tag)
        return result

    
    def scrape_quotes_data(self, url):
        print(f"Scraping {url}")
        #ezzel navigálunk konkrétan az url-re
        try:
            self.driver.get(url)
            time.sleep(3)
        except TimeoutException:
            print("Time out")

        all_authors = []
        all_quotes = []
        all_matching_tags = []
        top_ten_tags = self.get_top_ten_tags()

        


        while True:
            # Aktuális oldal
            author = self.get_author()
            quote = self.get_quotes()
            quote_tags = self.get_quote_tags()

            print("Aktuális oldal idézetei:", len(quote))
            
            matching_tags = self.compare_tags(top_ten_tags=top_ten_tags, quotes_tags=quote_tags)
            

            # "Segéd" printek nekem
            #print("Top ten tags:", top_ten_tags)
            #print("Quote tags:", quote_tags)
            #print("Matching tags:", matching_tags)

            # Listák feltötltése
            all_authors.extend(author)
            all_quotes.extend(quote)
            all_matching_tags.extend(matching_tags)

            print("Eddig összegyűjtött idézetek:", len(all_quotes))

            # Lapozás
            if not self.go_to_next_page():
                print("Last page")
                break

        
        return {
            "matching_tags": all_matching_tags,
            "author": all_authors,
            "quote": all_quotes
            }

  
        
    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df = df.explode(["matching_tags","author", "quote"])
        df.to_csv(filepath, sep = ",", index=False)

