import requests
from bs4 import BeautifulSoup

def scrape_product_info(url):
    """
    Scrape product name, price, and image from the URL.
    Note: This example works with Amazon product pages.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to load page")

    soup = BeautifulSoup(response.content, 'html.parser')

    # Get product title
    title_tag = soup.find(id="productTitle")
    if not title_tag:
        raise Exception("Could not find product title")
    product_name = title_tag.get_text().strip()

    # Get price
    price_tag = soup.find(id="priceblock_ourprice") or soup.find(id="priceblock_dealprice")
    if not price_tag:
        raise Exception("Could not find product price")
    price_str = price_tag.get_text().strip().replace('$', '').replace(',', '')
    price = float(price_str)

    # Get image
    img_tag = soup.find(id="landingImage") or soup.find("img", {"id": "imgBlkFront"})
    if img_tag and img_tag.has_attr('src'):
        image_url = img_tag['src']
    else:
        image_url = None

    return product_name, price, image_url
