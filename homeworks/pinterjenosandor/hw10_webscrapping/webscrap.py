from bs4 import BeautifulSoup
import requests

#the site what we try to scrap
url = "http://quotes.toscrape.com/"
#request the page html content by request
response = requests.get(url)

if response.status_code == 200:
  print("Downloaded\n")
  bsscrap = BeautifulSoup(response.text, "html.parser")

  top_tags = bsscrap.find_all("span", class_="tag-item") #find all "span" element what have "tag-item" class

  print("Top 10 tag:\n")
  for i, tag in enumerate(top_tags, start=1):
    print(f"{i}. {tag.text.strip()}")
else:
  print(f"Error occured at downloading. Status code: {response.status_code}")