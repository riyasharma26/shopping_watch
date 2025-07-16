import streamlit as st
import pandas as pd
from utils.scraper import scrape_product_info
from utils.tracker import load_price_history, save_price
from utils.predictor import predict_price_trend

st.set_page_config(page_title="Amazon Price Tracker", page_icon="🛍️")
st.title("🛍️ Amazon Price Tracker")

asin = st.text_input("Enter Amazon ASIN (e.g., B09G3HRMVB)")

if asin:
    try:
        title, current_price, image_url = scrape_product_info(asin)
        st.image(image_url, width=200)
        st.subheader(title)
        st.metric("Current Price", f"${current_price:.2f}")

        # Track and store price
        fake_url = f"https://www.amazon.com/dp/{asin}"
        save_price(fake_url, title, current_price)

        # Load and show price history
        price_data = load_price_history(fake_url)
        if not price_data.empty:
            st.line_chart(price_data.set_index('date')['price'])

            prediction = predict_price_trend(price_data)

            if current_price <= prediction['min_expected_price']:
                st.success("✅ Buy now — price is likely at its lowest!")
            else:
                st.warning("⏳ Wait — price might drop soon.")
        else:
            st.info("No price history yet. Try again tomorrow!")

    except Exception as e:
        st.error(f"Error: {e}")
