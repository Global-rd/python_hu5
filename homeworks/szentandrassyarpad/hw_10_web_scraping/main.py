from quote_scraper import QuoteScraper
import pprint
import pandas as pd
from pathlib import Path

def main():
    scraper = QuoteScraper()
    scraper.initialize_webdriver()
    tag_urls = scraper.get_tag_urls("https://quotes.toscrape.com")
    quotes_list = []
    authors_list = []
    tags_list = []
    
    for tag_url in tag_urls:
      
        quote_dict = scraper.get_quotes(tag_url["tag"], tag_url["url"])
        quotes_list.extend(quote_dict.get("quotes"))
        authors_list.extend(quote_dict.get("authors"))
        tags_list.extend(quote_dict.get("tags"))
    
    df = pd.DataFrame(
        {
            "tag" : tags_list,
            "author" : authors_list,
            "quote" : quotes_list            
        }
    )
    
    script_dir = Path(__file__).resolve().parent 
    file_path = script_dir /"quotes.csv"
    # A , és ; is bekevar, és idézőjeleket rak mondatok köré, ezért a tab az elválasztó
    df.to_csv(file_path, sep="\t", index=False)

if __name__ == "__main__":
    main()
