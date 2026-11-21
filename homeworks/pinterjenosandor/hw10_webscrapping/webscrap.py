from bs4 import BeautifulSoup
import requests
import pandas as pd


#the site what we try to scrap
url = "http://quotes.toscrape.com/"
#request the page html content by request
response = requests.get(url)

if response.status_code == 200:
  print("Downloaded\n")
  bsscrap = BeautifulSoup(response.text, "html.parser")
  datas = [] #empty list for data collecting
  top_tags = bsscrap.find_all("span", class_="tag-item") #find all "span" element what have "tag-item" class

  print("Top 10 tag:\n")
  for i, tag in enumerate(top_tags, start=1):
    tag_name = tag.text.strip()
    print(f"{i}. {tag_name}") #print top ten
    #dictonary from the top ten
    datas.append({
      "nr.": i,
      "tag": tag_name,
    })
  df = pd.DataFrame(datas)
  df.to_csv("top_10.csv", index=False) #export top ten to CSV


else:
  print(f"Error occured at downloading. Status code: {response.status_code}")