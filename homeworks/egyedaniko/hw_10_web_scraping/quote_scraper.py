# Idézetek gyűjtése a tíz legnépszerűbb tag alapján

from pathlib import Path
from urllib.parse import quote as encode_tag

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://quotes.toscrape.com"

# A fájlok mindig a program mellé kerülnek.
OUTPUT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = OUTPUT_DIR / "top10_quotes.csv"


def scrape_quotes():
    # A hiba keresése közben látható böngészőt használunk.
    options = Options()

    # Később ezt visszakapcsolhatod a háttérben futtatáshoz.
    # options.add_argument("--headless=new")

    print("Chrome indítása...", flush=True)

    driver = webdriver.Chrome(options=options)
    all_quotes = []

    try:
        driver.set_page_load_timeout(45)
        wait = WebDriverWait(driver, 30)

        print("Főoldal megnyitása...", flush=True)
        driver.get(BASE_URL)

        print(
            f"Betöltött oldal: {driver.current_url}",
            flush=True,
        )

        # Csak a Top Ten tags oldalsáv címkéit keressük.
        print("A top 10 tag keresése...", flush=True)

        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".tag-item .tag")
            )
        )

        tag_elements = driver.find_elements(
            By.CSS_SELECTOR,
            ".tag-item .tag",
        )

        # A neveket még az oldal elhagyása előtt eltároljuk.
        top_tags = [
            element.text.strip()
            for element in tag_elements[:10]
        ]

        if (
            len(top_tags) != 10
            or len(set(top_tags)) != 10
            or not all(top_tags)
        ):
            raise ValueError(
                "Nem található tíz különböző, nem üres top tag."
            )

        print(
            f"Top 10 tags: {', '.join(top_tags)}",
            flush=True,
        )

        for tag in top_tags:
            # Az URL-ben kódolt, a CSV-ben eredeti tagnevet használunk.
            encoded_tag = encode_tag(tag, safe="")
            page_url = f"{BASE_URL}/tag/{encoded_tag}/"

            page_number = 1
            visited_pages = set()

            while page_url:
                # Védelem az ismétlődő lapozási linkek ellen.
                if page_url in visited_pages:
                    raise ValueError(
                        f"Ismétlődő lapozási link: {page_url}"
                    )

                visited_pages.add(page_url)

                print(
                    f"Feldolgozás: {tag}, "
                    f"{page_number}. oldal – {page_url}",
                    flush=True,
                )

                driver.get(page_url)

                # Megvárjuk az idézetek megjelenését.
                wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, ".quote .text")
                    )
                )

                quote_blocks = driver.find_elements(
                    By.CLASS_NAME,
                    "quote",
                )

                for block in quote_blocks:
                    quote_text = block.find_element(
                        By.CLASS_NAME,
                        "text",
                    ).text.strip()

                    author = block.find_element(
                        By.CLASS_NAME,
                        "author",
                    ).text.strip()

                    all_quotes.append(
                        {
                            "tag": tag,
                            "author": author,
                            "quote": quote_text,
                        }
                    )

                print(
                    f"Begyűjtve ezen az oldalon: "
                    f"{len(quote_blocks)} idézet.",
                    flush=True,
                )

                # Ha van Next link, követjük. Egyébként kész a tag.
                next_links = driver.find_elements(
                    By.CSS_SELECTOR,
                    "li.next a",
                )

                if next_links:
                    page_url = next_links[0].get_attribute("href")

                    if not page_url:
                        raise ValueError(
                            "A következő oldal linkje üres."
                        )
                else:
                    page_url = None

                page_number += 1

    except WebDriverException:
        # A hibás oldal címét is kiírjuk.
        print(
            "\nBöngészőhiba történt. "
            "Megpróbálom elmenteni az oldal képét és HTML-jét.",
            flush=True,
        )

        # A diagnosztika hibája ne fedje el az eredeti hibát.
        try:
            print(
                f"Az aktuális oldal címe: {driver.current_url}",
                flush=True,
            )

            driver.save_screenshot(
                str(OUTPUT_DIR / "scraping_error.png")
            )

            (OUTPUT_DIR / "scraping_error.html").write_text(
                driver.page_source,
                encoding="utf-8",
            )

            print(
                "Diagnosztikai fájlok: scraping_error.png "
                "és scraping_error.html",
                flush=True,
            )

        except (WebDriverException, OSError) as diagnostic_error:
            print(
                f"A diagnosztika mentése nem sikerült: "
                f"{diagnostic_error}",
                flush=True,
            )

        raise

    finally:
        # Hiba esetén is megpróbáljuk bezárni a böngészőt.
        try:
            driver.quit()
        except WebDriverException:
            print(
                "A böngésző bezárása nem sikerült.",
                flush=True,
            )

    return all_quotes


def main():
    try:
        rows = scrape_quotes()

        if not rows:
            raise ValueError("Egyetlen idézet sem került begyűjtésre.")

        df = pd.DataFrame(
            rows,
            columns=["tag", "author", "quote"],
        )

        # Ugyanaz az idézet több különböző tag alatt is megmarad.
        df = df.drop_duplicates(
            subset=["tag", "author", "quote"]
        )

        # Csak a teljes adatgyűjtés után mentjük a CSV-t.
        df.to_csv(
            OUTPUT_FILE,
            index=False,
            encoding="utf-8-sig",
        )

        print(
            f"\nSikeres mentés: {len(df)} sor.",
            flush=True,
        )
        print(f"CSV helye: {OUTPUT_FILE}", flush=True)

        print("\nSorok száma tagenként:")
        print(df.groupby("tag").size().to_string())

    except TimeoutException as error:
        print(
            "\nTimeoutException: az oldal betöltése vagy "
            "a keresett elemek megjelenése nem történt meg időben."
        )
        print(
            "Ha létrejött, nyisd meg a scraping_error.png fájlt "
            "a program mappájában."
        )
        raise SystemExit(1) from error

    except (WebDriverException, ValueError, OSError) as error:
        print(
            f"\nSikertelen adatgyűjtés vagy mentés:\n"
            f"{type(error).__name__}: {error}"
        )
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
