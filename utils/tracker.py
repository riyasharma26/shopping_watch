import os
import pandas as pd
from datetime import datetime

DATA_FILE = "data/price_data.csv"

def save_price(url, product_name, price):
    if not os.path.exists('data'):
        os.makedirs('data')

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([{
        "url": url,
        "product_name": product_name,
        "price": price,
        "date": date
    }])

    if os.path.isfile(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_csv(DATA_FILE, index=False)

def load_price_history(url):
    if not os.path.isfile(DATA_FILE):
        return pd.DataFrame()

    df = pd.read_csv(DATA_FILE)
    df['date'] = pd.to_datetime(df['date'])
    return df[df['url'] == url].sort_values('date')
