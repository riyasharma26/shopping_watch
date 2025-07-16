from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def predict_price_trend(price_data):
    """
    Use linear regression on historical price data to predict future price.
    Returns dict with predicted min expected price.
    """

    if len(price_data) < 3:
        # Not enough data to predict
        return {"min_expected_price": price_data['price'].min()}

    price_data = price_data.sort_values('date')
    price_data['timestamp'] = price_data['date'].apply(lambda x: x.timestamp()).values.reshape(-1,1)
    prices = price_data['price'].values

    model = LinearRegression()
    model.fit(price_data['timestamp'].values.reshape(-1,1), prices)

    # Predict price 7 days into the future
    future_timestamp = price_data['timestamp'].max() + 7*24*3600
    predicted_price = model.predict([[future_timestamp]])[0]

    min_price = min(predicted_price, price_data['price'].min())
    return {"min_expected_price": min_price}
