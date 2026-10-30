import requests

def extract_data():
    """
    A function to get the data thru API with specific parameters in json format.
    """

    url = "https://api.coingecko.com/api/v3/coins/markets"
    parameters = {"vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 250}

    response = requests.get(url=url, params=parameters).json()
    return response