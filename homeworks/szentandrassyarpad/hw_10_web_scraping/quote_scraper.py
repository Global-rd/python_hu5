
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import pprint

class QuoteScraper:
    
    def initialize_webdriver(self):
        options = Options() # pl hogy headless módban legyen a browserünk, de egyelőre ezek üresek
        self.driver = webdriver.Chrome(options=options)
        print("Initialize driver")

    def get_tag_urls(self, url):
        print(f"Scraping {url}")
        self.driver.get(url)        
        tag_urls=[]
        
        for i in range (1,11):
            tag_element = self.driver.find_element(by=By.XPATH, value=f"/html/body/div/div[2]/div[2]/span[{i}]/a" )
            tag_urls.append(
                    {
                        'tag':tag_element.text,
                        'url':tag_element.get_attribute("href")
                    }
            )

        return tag_urls

    def get_quotes(self,tag, url):
        text_list = []
        author_list = []
        tag_list = []
        next_url = url
        
        pager_text = "-"
        while True:
            
            self.driver.get(next_url)
            # várakoztatás amíg betőlt az első idézet elem.
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/span[1]'))
            )
                       
            text_elements = self.driver.find_elements(by=By.CLASS_NAME, value="text")
            for text in text_elements:
                text_without_quotation_marks=text.text
            
                for quotation_mark in ['"', '„', '”', '“']:
                    text_without_quotation_marks = text_without_quotation_marks.replace(quotation_mark, '')
                text_list.append(text_without_quotation_marks)

            author_elements = self.driver.find_elements(by=By.CLASS_NAME, value="author")
            for author in author_elements:
                author_list.append(author.text)
                tag_list.append(tag)
            try:
                pager_element = self.driver.find_element(by=By.XPATH, value = "/html/body/div/div[2]/div[1]/nav/ul/li/a")
                pager_text = pager_element.text
                next_url = pager_element.get_attribute("href")
            except NoSuchElementException:
                pager_text = "-"
                next_url = None

            if "Next" not in pager_text:
                return {
                            "tags" : tag_list, 
                            "quotes" : text_list, 
                            "authors" : author_list
                        }    
    