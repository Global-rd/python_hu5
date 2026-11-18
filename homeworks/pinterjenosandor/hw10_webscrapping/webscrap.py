from bs4 import BeautifulSoup
import requests

#the site what we try to scrap
url = "http://quotes.toscrape.com/"

#request the page html content by request
response = requests.get(url)

if response.status_code == 200:
  print("Downloaded\n")

#transfer to BS
  soup = BeautifulSoup(response.text, "html.parser")
  quotes = soup.find_all("span", class_="text")
  authors = soup.find_all("small", class_="author")

  #looping on it and print the first 10 pcs
  for i, (quote, author) in enumerate(zip(quotes[:10], authors[:10]), start=1):
    print(f"{i}. Quote: {quote.text}")
    print(f"   Author: {author.text}")

else:
  print(f"Error occured at downloading. Status code: {response.status_code}")