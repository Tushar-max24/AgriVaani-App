# govt_market.py
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DATA_GOV_API_KEY = os.getenv("DATA_GOV_API_KEY")

DATASET_ID = "9ef84268-d588-465a-a308-a864a43d0070"

_cached_data = []
_last_fetch_date = None

def normalize_state_name(state: str) -> str:
    """Normalize state names to match API's expected format."""
    state_mapping = {
        'karnatka': 'Karnataka',
        'mumbai': 'Maharashtra',
        'bombay': 'Maharashtra',
        'delhi': 'NCT of Delhi',
        'tamilnadu': 'Tamil Nadu',
        'westbengal': 'West Bengal',
        'andhrapradesh': 'Andhra Pradesh',
        'arunachalpradesh': 'Arunachal Pradesh',
        'madhyapradesh': 'Madhya Pradesh',
        'uttarpradesh': 'Uttar Pradesh',
        'uttarakhand': 'Uttarakhand',
        'tamil nadu': 'Tamil Nadu',
        'west bengal': 'West Bengal',
        'andhra pradesh': 'Andhra Pradesh',
        'arunachal pradesh': 'Arunachal Pradesh',
        'madhya pradesh': 'Madhya Pradesh',
        'uttar pradesh': 'Uttar Pradesh',
    }
    normalized = state_mapping.get(state.lower().strip(), state)
    return normalized

def fetch_govt_prices(state=None, limit=100):
    url = f"https://api.data.gov.in/resource/{DATASET_ID}"
    params = {
        "api-key": DATA_GOV_API_KEY,
        "format": "json",
        "limit": limit,
    }

    if state:
        # Normalize the state name
        state = normalize_state_name(state)
        params["filters[state]"] = state
        print(f"🔍 Fetching data for state: {state}")

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        records = data.get("records", [])
        print(f"📊 Found {len(records)} records")
        if not records and state:
            print(f"⚠️ No data found for state: {state}")
            print(f"   API Response: {data}")
        
        govt_prices = []
        for r in records:
            govt_prices.append({
                "crop": r.get("commodity"),
                "price": int(r.get("modal_price", 0)),
                "quantity": "1 Quintal",
                "state": r.get("state"),
                "district": r.get("district"),
                "market": r.get("market"),
                "source": "govt",
            })
        return govt_prices
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Status Code: {e.response.status_code}")
            print(f"   Response: {e.response.text}")
        return []


def get_cached_govt_data(state=None, limit=100):
    global _cached_data, _last_fetch_date

    today = datetime.now().date()

    if _last_fetch_date != today or state:
        _cached_data = fetch_govt_prices(state=state, limit=limit)
        _last_fetch_date = today

    return _cached_data

