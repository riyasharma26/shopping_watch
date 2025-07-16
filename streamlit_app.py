import streamlit as st
from utils.scraper import scrape_product_info
from utils.tracker import load_price_history, save_price
from utils.predictor import predict_price_trend
import pandas as pd

st.set_page_config(page_title="Wishlist Price Tracker", page_icon="🛍️")

st.title("🛍️ Wishlist Price Tracker")
st.write("Enter a product URL to track price history and get buying advice.")

url = st.text_input("Product URL")

if url:
    with st.spinner("Fetching product info..."):
        try:
            product_name, price, image_url = scrape_product_info(url)
            st.image(image_url, width=200)
            st.markdown(f"### {product_name}")
            st.metric("Current Price", f"${price:.2f}")

            # Save current price to data store
            save_price(url, product_name, price)

            # Load historical data and show chart
            price_data = load_price_history(url)
            if not price_data.empty:
                st.line_chart(price_data.set_index('date')['price'])

                # Predict price trend and recommend
                prediction = predict_price_trend(price_data)

                if price <= prediction['min_expected_price']:
                    st.success("✅ Buy now — price is likely at its lowest!")
                else:
                    st.warning("⏳ Wait — price might drop soon.")

            else:
                st.info("No price history yet. Check back later!")

        except Exception as e:
            st.error(f"Error fetching product info: {e}")
