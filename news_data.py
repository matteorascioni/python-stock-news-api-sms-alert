import requests

APY_KEY = "Your news API_KEY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"

news_params = {
    "qInTitle": COMPANY_NAME, 
    "sortBy": "relevancy",
    "apiKey": APY_KEY,
}

response = requests.get(url=NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
data = response.json()["articles"]
three_articles = data[:3]