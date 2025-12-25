import requests
import os
from dotenv import load_dotenv

load_dotenv()

DATA_GOV_API_KEY = os.getenv("DATA_GOV_API_KEY")

BASE_URL = "https://api.data.gov.in/resource"
RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"


def fetch_govt_prices(limit=100):
    print("🔍 Fetching govt prices...")
    print("🔑 DATA_GOV_API_KEY:", DATA_GOV_API_KEY)

    url = f"{BASE_URL}/{RESOURCE_ID}"

    params = {
        "api-key": DATA_GOV_API_KEY,
        "format": "json",
        "limit": limit
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        print("🔍 Status Code:", response.status_code)
        response.raise_for_status()

        data = response.json()
        records = data.get("records", [])
        print("🔍 Records count:", len(records))

        govt_prices = []

        for item in records:
            govt_prices.append({
                "crop": item.get("commodity"),
                "price": float(item.get("modal_price", 0)),
                "quantity": "1 Quintal",
                "state": item.get("state"),        # ✅ CRITICAL
                "district": item.get("district"),
                "market": item.get("market"),
                "source": "govt"
            })

        return govt_prices

    except Exception as e:
        print("❌ Govt API error:", e)
        return []
