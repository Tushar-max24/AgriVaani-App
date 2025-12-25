import requests

API_KEY = "1e11716e7ff2403a9d27d0007028d295"
BASE_URL = "https://newsapi.org/v2/everything"

def get_agri_news():
    params = {
        "q": "agriculture farming india",
        "language": "en",
        "apiKey": API_KEY,
        "pageSize": 10
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    news_list = []
    for article in data["articles"]:
        news_list.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        })

    return news_list
