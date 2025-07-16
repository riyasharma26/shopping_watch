import requests

SERPAPI_KEY = "8131d215f5e25047542f39e3a960352422921727f17d669193f763d85a9c9c9d"

def search_amazon_products(keyword):
    """
    Use SerpApi to search Amazon by keyword and return product list.
    """
    params = {
        "engine": "amazon",
        "k": keyword,
        "amazon_domain": "amazon.com",
        "api_key": SERPAPI_KEY
    }

    response = requests.get("https://serpapi.com/search.json", params=params)
    if response.status_code != 200:
        raise Exception(f"SerpApi search failed: {response.status_code}")

    data = response.json()
    results = data.get("organic_results", [])

    products = []
    for r in results:
        if "title" in r and "price" in r and "link" in r:
            price_str = r["price"].get("raw", "$0.00")
            try:
                price = float(price_str.replace("$", "").replace(",", ""))
            except:
                continue
            products.append({
                "title": r["title"],
                "price": price,
                "link": r["link"],
                "image": r.get("thumbnail")
            })

    return products
