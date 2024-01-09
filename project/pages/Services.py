import streamlit as st
import os
from PIL import Image
DEFAULT_WIDTH = 80
st.set_page_config(layout="wide")
st.write("# Our Service")
folders = ["photos"]
# create a list of image paths
image_paths = []
for folder in folders:
    for file in os.listdir(folder):
        if file.endswith('.jpg'):
            image_paths.append(os.path.join(folder, file))

# create a list of images
images = []
for path in image_paths:
    image = Image.open(path)
    images.append(image)

# use st.slider to select
index = st.slider('Select an image index', 0, len(images)-1)

# set size for image slider
image_width = st.slider(
    label="Change Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%", key="image_uploader"
)
width = max(image_width, 0.01)
side = max((100 - width) / 2, 0.01)
_, container, _ = st.columns([side, image_width, side])
container.image(images[index])


VIDEO_DATA = "videos/genshin.mp4"
# st.set_page_config(layout="wide")
video_width = st.slider(
    label="Change Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%", key="video_upload"
)
width = max(video_width, 0.01)
side = max((100 - width) / 2, 0.01)


_, container, _ = st.columns([side, video_width, side])
container.video(data=VIDEO_DATA)

import pandas as pd
import requests

# Retrieve real-time cryptocurrency prices from Binance API
def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

# Store the retrieved data in a DataFrame
def get_crypto_data():
    symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "DOGEUSDT"]
    prices = []
    for symbol in symbols:
        price = get_crypto_price(symbol)
        prices.append(price)
    data = {"Symbol": symbols, "Price": prices}
    df = pd.DataFrame(data)
    return df

# Create a web application that displays the data in a user-friendly format
def main():
    st.title("Cryptocurrency Price Checker")
    st.write("Real-time cryptocurrency prices retrieved via the Binance API")
    df = get_crypto_data()
    chart_width = st.slider(
    label="Change Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%", key="crypto_price_checker"
    )
    width = max(chart_width, 0.01)
    side = max((100 - width) / 2, 0.01)

    _, container, _ = st.columns([side, width, side])
    container.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    main()
