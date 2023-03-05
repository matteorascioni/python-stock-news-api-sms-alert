import requests

STOCK = "TSLA"
APY_KEY = "Your alpha vantage API_KEY"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

alpha_vantage_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": APY_KEY,
    "datatype": "json",
    "outputsize": "full",
}

response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=alpha_vantage_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]