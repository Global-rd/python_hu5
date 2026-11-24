from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
        options = Options() 
        self.driver = webdriver.Chrome(options=options)

    def go_to_next_page(self):
        try:
            next_button = self.driver.find_element(By.XPATH, value=quo.NEXT_BUTTON_XPATH)
            next_button.click()
            time.sleep(1)
            return True
        except NoSuchElementException:
            return False

    def get_top_ten_tags(self, url):
        self.driver.get(url)
        tags = self.driver.find_elements(
            by=By.XPATH, 
            value=quo.TOP_TEN_TAG_XPATH)
        
        return [tag.text for tag in tags]

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
    
    
    def scrape_quotes_data(self, url, top_ten_tags):
        print(f"Scraping {url}")
        #ezzel navigálunk konkrétan az url-re
        
        self.driver.get(url)
        time.sleep(3)
        
        all_data = []
        

        while True:
            # Aktuális oldal
            author = self.get_author()
            quote = self.get_quotes()
            quote_tags = self.get_quote_tags()

            #print("Aktuális oldal idézetei:", len(quote))
            
             # Idézetenként összehasonlítjuk a tageket
            for i in range(len(quote)):
                tags = quote_tags[i].split()
                print(i)

                matching_tags = [
                    tag for tag in tags
                    if tag in top_ten_tags
                ]
                if matching_tags:
                    for tag in matching_tags:
                        all_data.append({
                            "matching_tags": tag,
                            "author": author[i],
                            "quote": quote[i]
                            })

            if not self.go_to_next_page():
                print("Last page")
                break

        return all_data

 
        
    @staticmethod
    def load_data_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df = df.explode(["matching_tags","author", "quote"])
        df.to_csv(filepath, sep = ",", index=False)

