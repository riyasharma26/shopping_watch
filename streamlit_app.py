import streamlit as st
import pandas as pd
from utils.scraper import search_amazon_products
from utils.tracker import save_price, load_price_history
from utils.predictor import predict_price_trend

st.set_page_config(page_title="Amazon Wishlist Tracker", page_icon="🛍️")
st.title("🛍️ Amazon Wishlist Tracker")

query = st.text_input("Search for a product")

if query:
    try:
        products = search_amazon_products(query)

        if not products:
            st.warning("No results found.")
        else:
            for i, product in enumerate(products[:5]):
                with st.container():
                    cols = st.columns([1, 3])
                    if product["image"]:
                        cols[0].image(product["image"], width=80)
                    with cols[1]:
                        st.subheader(product["title"])
                        st.write(f"💲 {product['price']}")
                        if st.button("Track this", key=f"track_{i}"):
                            save_price(product["link"], product["title"], product["price"])
                            st.success("Tracking started!")

                            # Show chart
                            history = load_price_history(product["link"])
                            if not history.empty:
                                st.line_chart(history.set_index("date")["price"])
                                prediction = predict_price_trend(history)

                                if product["price"] <= prediction["min_expected_price"]:
                                    st.success("✅ Buy now — price is likely at its lowest!")
                                else:
                                    st.warning("⏳ Wait — price might drop soon.")

    except Exception as e:
        st.error(f"Error: {e}")
