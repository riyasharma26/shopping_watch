# Wishlist Price Tracker

A Streamlit app to track price history of wishlist items and recommend when to buy.

## Features

- Enter product URL (supports Amazon currently)
- Scrapes product name, price, and image
- Tracks price history over time
- Predicts price trend and advises whether to buy now or wait
- Visualizes price history in charts

## Setup

1. Clone the repo  
```
git clone https://github.com/your-username/wishlist-price-tracker.git
cd wishlist-price-tracker
```

2. Install dependencies  
```
pip install -r requirements.txt
```

3. Run the app  
```
streamlit run streamlit_app.py
```

## Notes

- Currently supports Amazon product pages only.
- Price data is saved locally in `data/price_data.csv`.

## Contributing

Feel free to submit pull requests or open issues!
