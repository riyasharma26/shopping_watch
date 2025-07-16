import requests

SERPAPI_KEY = "8131d215f5e25047542f39e3a960352422921727f17d669193f763d85a9c9c9d"

def scrape_product_info(asin):
    """
    Uses SerpApi to get Amazon product info by ASIN.
    """

    params = {
        "engine": "amazon_product",
        "amazon_domain": "amazon.com",
        "asin": asin,
        "api_key": SERPAPI_KEY
    }

    response = requests.get("https://serpapi.com/search", params=params)

    if response.status_code != 200:
        raise Exception(f"SerpApi request failed: {response.status_code}")

    data = response.json()
    if "error" in data:
        raise Exception(data["error"])

    title = data.get("title", "Unknown Product")
    price_str = data.get("price", {}).get("raw", "$0.00")
    price = float(price_str.replace("$", "").replace(",", ""))
    image_url = data.get("images", [None])[0]

    return title, price, image_url
