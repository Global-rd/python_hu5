"""
HÁZI FELADAT 07: Adatok kinyerése és feldolgozása - CoinGecko API 
"""

import requests
import pandas as pd
import numpy as np

URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {"vs_currency": "usd", "per_page": 250}

def extract() -> pd.DataFrame:
    """
    Lekéri a CoinGecko API-ról a 250 legnagyobb kriptovaluta adatait.
    Az API válasz Pandas DataFrame-mé alakítja. 
    Hálózati hiba vagy érvénytelen API-válasz esetén RuntimeError kivételt ad.
    """
    try:
        response = requests.get(URL, params=PARAMS, timeout=30)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Az API válasza nem lista formátumú.")

        return pd.DataFrame(data)
    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            f"Sikertelen adat lekérés: {error}"
        ) from error
    except ValueError as error:
        raise RuntimeError(f"Hibás választ adott az API: {error}") from error


def main() -> None:
    df = extract()

    # 1. Letöltött kriptovaluták száma és market_cap összegzése
    print ("\n-----------------------------------------------------------------------------------------------")
    print(f"Letöltött kriptovaluták száma: {len(df)}")

    summary = df[["market_cap_rank", "name", "market_cap"]]
    print(df[["market_cap_rank", "name", "market_cap"]])

    print ("\n-----------------------------------------------------------------------------------------------")
    print("1. Üres cellák oszloponként:")
    print(df.isna().sum())

    # 2. Teljes market_cap összegzése
    print ("\n-----------------------------------------------------------------------------------------------")
    print("\n2. Teljes market_cap összeg:")
    print(f"{df['market_cap'].sum():,.0f}".replace(",", " "))

    # 3. az első 50 kriptovaluta current_price alapján (legmagasabb ár)
    top50_df = df.sort_values("current_price", ascending=False).head(50).copy()

    # 4. rendezés price_change_percentage_24h szerint csökkenően
    top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)

    # 5. change_direction oszlop létrehozása a price_change_percentage_24h alapján
    change = top50_df["price_change_percentage_24h"]
    top50_df["change_direction"] = np.select([change > 0, change < 0], ["+", "-"], default="0" )

    print ("\n-----------------------------------------------------------------------------------------------")
    print("\n3-5. top50_df:")
    print(
        top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]].to_string()
    )


if __name__ == "__main__":
    main()
