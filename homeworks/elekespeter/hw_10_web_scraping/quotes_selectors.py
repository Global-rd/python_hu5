# Az oldal elemeinek CSS-szelektorai egy helyen (mint a lesson_19/auchan_selectors.py).
# Ha az oldal szerkezete változik, csak itt kell javítani.

BASE_URL = "https://quotes.toscrape.com/"

# A főoldal jobb oldali "Top Ten tags" dobozának linkjei
TOP_TAGS_CSS = "div.tags-box span.tag-item a.tag"

# Egy idézet blokkja, és azon belül a szöveg és a szerző
QUOTE_CSS = "div.quote"
QUOTE_TEXT_CSS = "span.text"
QUOTE_AUTHOR_CSS = "small.author"

# A lap alján lévő "Next →" gomb linkje (pagination)
NEXT_PAGE_CSS = "li.next a"
