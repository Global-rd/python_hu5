import time
from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.parse import urljoin
from pathlib import Path

url = "http://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
  print("Downloaded\n")
  bsscrap = BeautifulSoup(response.text, "html.parser")
  datas = []
  top_tags = bsscrap.find_all("span", class_="tag-item")

  for tag_i, tag_item in enumerate(top_tags, start=1):
    tag_a = tag_item.find("a")
    tag_name = tag_item.text.strip()


    next_pg_url = urljoin(url, tag_a["href"]) #create the starting address as next page url

    quote_i = 0 # start the ID's of quotes from 0 at every new tag

    print(f"***{tag_i}.{tag_name.upper()}***")

    while next_pg_url:
      tag_response = requests.get(next_pg_url)

      if tag_response.status_code == 200:
        tag_bsscrap = BeautifulSoup(tag_response.text, "html.parser")
        quotes = tag_bsscrap.find_all("div", class_="quote")

        for quote in quotes:
          quote_i += 1
          quote_text = quote.find("span", class_="text").text.strip()
          author = quote.find("small", class_="author").text.strip()
          numbering = f"{tag_i}.{quote_i}"
          print(f"{numbering} | {tag_name} - {quote_text} - from: {author}")
          datas.append({
              "nr.": numbering,
              "tag": tag_name,
              "author": author,
              "quote": quote_text,
          })

        next_li = tag_bsscrap.find("li", class_="next")
        next_a = next_li.find("a") if next_li else None
        next_pg_url = urljoin(url, next_a["href"]) if next_a else None
        time.sleep(0.5)
      else:
        break

    print()
    time.sleep(0.5)

  df = pd.DataFrame(datas)
  try:
    df.to_csv(Path(__file__).parent / "top_10.csv", index=False, encoding="utf-8-sig")
    print(f"Done! {len(datas)} line(s) saved to top_10.csv")
  except PermissionError:
    df.to_csv(Path(__file__).parent / "top_10_new.csv", index=False, encoding="utf-8-sig")
    print(f"Error was on saving, we saved {len(datas)} line(s) to new file name:top_10_new.csv")

else:
  print(f"Error occured at downloading. Status code: {response.status_code}")