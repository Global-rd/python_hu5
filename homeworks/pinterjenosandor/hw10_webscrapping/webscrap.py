from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


#the site what we try to scrap
url = "http://quotes.toscrape.com"
#request the page html content by request
response = requests.get(url)

if response.status_code == 200:
  print("Downloaded\n")
  bsscrap = BeautifulSoup(response.text, "html.parser")
  datas = [] #empty list for data collecting
  top_tags = bsscrap.find_all("span", class_="tag-item") #find all "span" element what have "tag-item" class

  #print("Top 10 tag:\n")
 

  for tag_i, tag_item in enumerate(top_tags, start=1): #make numbering for tags
    #time.sleep(0.5) #rest a little,
    tag_a = tag_item.find("a") #find the link in the html code
    tag_name = tag_item.text.strip()
    tag_url = url + tag_a["href"] #extend the url with the tag, example: http://quotes.toscrape.com/tag/books/
    print(f"***{tag_i}.{tag_name.upper()}***") #print tag item wit id
    tag_response = requests.get(tag_url)
    #print(tag_url)


    if tag_response.status_code == 200:
      tag_bsscrap = BeautifulSoup(tag_response.text, "html.parser") #retrive the content
      quotes= tag_bsscrap.find_all("div", class_="quote") #all data collect
      #print(quotes)


      for quote_i, quote in enumerate(quotes, start=1):
        quote_text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        numbering = f"{tag_i}.{quote_i}" 
        print(f"{numbering} | {tag_name} - {quote_text} - from: {author}")
        datas.append({
              "nr.": numbering,
              "tag": tag_name,
              "author": author,
              "quote": quote_text
            })
    print()
    time.sleep(0.5)
  

  df = pd.DataFrame(datas)
  try:
    df.to_csv("top_10.csv", index=False, encoding="utf-8-sig") #export top ten to CSV
    print(f"Done!{len(datas)} line(s) saved to top_10.csv")
  except PermissionError:
    df.to_csv("top_10_new.csv", index=False, encoding="utf-8-sig") #export top ten to CSV, when error
    print(f"Error was on saving, we saved {len(datas)} line(s) to new file name: top_10_new.csv")

else:
  print(f"Error occured at downloading. Status code: {response.status_code}")