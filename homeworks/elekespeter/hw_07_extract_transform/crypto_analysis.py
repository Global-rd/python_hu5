import time

import numpy as np
import pandas as pd
import requests

# =============================================================================
# KONSTANSOK
# =============================================================================
URL = "https://api.coingecko.com/api/v3/coins/markets"

# A feladat szerint 2 paraméter kell:
#   vs_currency: kötelező, milyen pénznemben kérjük az árakat
#   per_page:    alapból 100 elem jön egy oldalon, 250 a maximum
# A sorrend alapból market cap szerint csökkenő, így ez a "250 legnagyobb".
PARAMS = {
    "vs_currency": "usd",
    "per_page": 250,
}

MAX_RETRIES = 3


# =============================================================================
# 1. LÉPÉS: EXTRACT - adatok lekérése az API-ról (lesson_13 alapján)
# =============================================================================

def fetch_markets(url: str, params: dict) -> list:
    """
    Lekéri a kriptovaluták piaci adatait.
    Siker esetén egy listát ad vissza (minden elem egy dictionary),
    hiba esetén üres listát.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, params=params, timeout=30)

            # 429 = Too Many Requests: a nyilvános API percenként korlátozza a hívásokat
            if response.status_code == 429:
                wait = int(response.headers.get("Retry-After", 60))
                print(f"Túl sok kérés ({attempt}. próbálkozás), várakozás {wait} mp...")
                time.sleep(wait)
                continue

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Sikertelen API-hívás: {e}")
            return []
        except ValueError:
            print("A válasz nem érvényes JSON.")
            return []

    print("Többszöri próbálkozás után sem sikerült lekérni az adatokat.")
    return []


# =============================================================================
# 2. LÉPÉS: TRANSFORM - az 5 pandas-feladat (lesson_14 alapján)
# =============================================================================

def count_missing(df: pd.DataFrame) -> pd.Series:
    """
    1. feladat: oszloponként hány üres cella (NaN / None) van.
    Az isna() minden cellára True/False-t ad, a sum() oszloponként összeadja
    (a True 1-nek, a False 0-nak számít).
    """
    return df.isna().sum()


def total_market_cap(df: pd.DataFrame) -> float:
    """2. feladat: a teljes DataFrame market_cap oszlopának összege."""
    return df["market_cap"].sum()


def build_top50(df: pd.DataFrame) -> pd.DataFrame:
    """
    3. feladat: az 50 legmagasabb árú (current_price) kriptovaluta.
    Értelmezés: "current_price alapján" -> ár szerint csökkenő sorrend, első 50.
    A .copy() azért kell, hogy a top50_df önálló DataFrame legyen, és a későbbi
    új oszlop ne adjon SettingWithCopyWarning figyelmeztetést.
    """
    return df.sort_values("current_price", ascending=False).head(50).copy()


def sort_by_24h_change(df: pd.DataFrame) -> pd.DataFrame:
    """4. feladat: rendezés a 24 órás árváltozás (%) szerint, csökkenő sorrendben."""
    return df.sort_values("price_change_percentage_24h", ascending=False)


def add_change_direction(df: pd.DataFrame) -> pd.DataFrame:
    """
    5. feladat: új change_direction oszlop: "+", "-" vagy "0".
    A np.where csak 2 kimenetet ismer (lesson_14: Premium/Standard), ezért
    3 esethez np.select kell: feltételek listája + hozzájuk tartozó értékek.
    Ha az érték hiányzik (NaN), egyik feltétel sem igaz -> "N/A".
    """
    change = df["price_change_percentage_24h"]
    conditions = [change > 0, change < 0, change == 0]
    choices = ["+", "-", "0"]
    df["change_direction"] = np.select(conditions, choices, default="N/A")
    return df


# =============================================================================
# FŐPROGRAM
# =============================================================================

def main():
    data = fetch_markets(URL, PARAMS)
    if not data:
        print("Nincs adat, a program leáll.")
        return

    # A lista minden eleme egy dictionary -> pd.DataFrame(data) (lesson_14)
    df = pd.DataFrame(data)
    print(f"Lekért kriptovaluták száma: {len(df)}")

    # 1. feladat
    print("\n--- 1. Üres cellák oszloponként ---")
    print(count_missing(df))

    # 2. feladat
    print("\n--- 2. Teljes market cap ---")
    print(f"{total_market_cap(df):,.0f} USD")

    # 3. feladat
    top50_df = build_top50(df)
    print("\n--- 3. top50_df: az 50 legmagasabb árú kriptovaluta ---")
    print(top50_df[["name", "symbol", "current_price"]])

    # 4. feladat
    top50_df = sort_by_24h_change(top50_df)
    print("\n--- 4. top50_df rendezve 24 órás változás szerint (csökkenő) ---")
    print(top50_df[["name", "current_price", "price_change_percentage_24h"]])

    # 5. feladat
    top50_df = add_change_direction(top50_df)
    print("\n--- 5. change_direction oszlop ---")
    print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])
    print("\nIrányok darabszáma:")
    print(top50_df["change_direction"].value_counts())


if __name__ == "__main__":
    main()
