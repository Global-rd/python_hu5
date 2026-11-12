"""Fetch and transform the top 250 cryptocurrency market records."""

import pandas as pd
import requests


API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {"vs_currency": "usd", "per_page": 250}
REQUIRED_COLUMNS = {
    "name",
    "market_cap",
    "current_price",
    "price_change_percentage_24h",
}


def fetch_markets() -> pd.DataFrame:
    """Get the market-cap-ranked first page with one public API request."""
    response = requests.get(API_URL, params=PARAMS, timeout=30)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, list) or len(data) != 250:
        raise ValueError("The API did not return 250 cryptocurrency records.")

    markets_df = pd.DataFrame(data)
    missing_columns = REQUIRED_COLUMNS.difference(markets_df.columns)
    if missing_columns:
        raise ValueError(f"Missing API columns: {', '.join(sorted(missing_columns))}")
    return markets_df


def change_direction(change: float) -> str | None:
    """Label a known 24-hour price change without mislabeling missing data."""
    if pd.isna(change):
        return None
    if change > 0:
        return "+"
    if change < 0:
        return "-"
    return "0"


def main() -> None:
    try:
        markets_df = fetch_markets()
    except (requests.RequestException, ValueError) as error:
        print(f"Could not load market data: {error}")
        raise SystemExit(1) from error

    print("Missing values by column:")
    print(markets_df.isna().sum().to_string())

    markets_df["market_cap"] = pd.to_numeric(
        markets_df["market_cap"], errors="coerce"
    )
    markets_df["current_price"] = pd.to_numeric(
        markets_df["current_price"], errors="coerce"
    )
    markets_df["price_change_percentage_24h"] = pd.to_numeric(
        markets_df["price_change_percentage_24h"], errors="coerce"
    )

    total_market_cap = markets_df["market_cap"].sum(min_count=1)
    print(f"\nTotal market capitalization (USD): {total_market_cap:,.0f}")

    # Select the 50 highest-priced coins from all 250 records.
    top50_df = markets_df.nlargest(50, "current_price").copy()
    top50_df = top50_df.sort_values(
        "price_change_percentage_24h", ascending=False, na_position="last"
    )
    top50_df["change_direction"] = top50_df[
        "price_change_percentage_24h"
    ].map(change_direction)

    print("\n50 highest-priced cryptocurrencies, sorted by 24-hour change:")
    print(
        top50_df[
            ["name", "current_price", "price_change_percentage_24h",
             "change_direction"]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
