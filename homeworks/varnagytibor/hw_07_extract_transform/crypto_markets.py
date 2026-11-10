import requests
import pandas as pd

#hogy a printelt táblák ne törjenek "..."-ra
pd.set_option("display.width", 200)
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", None)

URL = "https://api.coingecko.com/api/v3/coins/markets"

#a két kötelező/szükséges paraméter: milyen pénznemben kérjük az árat, és hány darabot egy oldalon
#(a per_page maximuma 250, és alapból market cap szerint csökkenő a sorrend -> 1 hívás elég)
PARAMETERS = {"vs_currency": "usd",
              "per_page": 250}


def extract_markets(url: str, parameters: dict) -> pd.DataFrame:
    """Lehúzza a CoinGecko /coins/markets endpointról az adatot, és DataFrame-et ad vissza."""
    response = requests.get(url=url, params=parameters, timeout=30)
    response.raise_for_status()  #ha nem 200-as a válasz (pl. 429 rate limit), hibát dob
    return pd.DataFrame(response.json())


def get_change_direction(change) -> str:
    """'+', '-' vagy '0' a 24 órás árváltozás előjele alapján."""
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"


def main():
    df = extract_markets(URL, PARAMETERS)
    print(f"Lehúzott kriptovaluták száma: {len(df)}\n")

    #1. üres cellák száma oszloponként
    print("1. Üres cellák oszloponként:")
    print(df.isnull().sum())
    print()

    #2. a teljes market cap összege
    total_market_cap = df["market_cap"].sum()
    print(f"2. Teljes market cap: {total_market_cap:,.0f} USD\n")

    #3. az első 50 kriptovaluta current_price alapján (a legdrágábbak)
    top50_df = df.nlargest(50, "current_price").copy()
    print("3. top50_df (current_price szerint):")
    print(top50_df[["name", "symbol", "current_price"]])
    print()

    #4. rendezés price_change_percentage_24h szerint csökkenő sorrendbe
    top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)
    print("4. top50_df price_change_percentage_24h szerint csökkenőben:")
    print(top50_df[["name", "current_price", "price_change_percentage_24h"]])
    print()

    #5. change_direction oszlop: "+", "-" vagy "0"
    #(ha a változás hiányzik (NaN), az egyik összehasonlítás sem igaz -> "0" lenne, ezért külön kezelem)
    top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(
        lambda change: get_change_direction(change) if pd.notna(change) else None
    )
    print("5. top50_df a change_direction oszloppal:")
    print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])


if __name__ == "__main__":
    main()
