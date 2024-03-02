import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
import quandl

class BitcoinPriceAnalyzer:
    def __init__(self):
        # Initialize Quandl API key (replace with your own key)
        quandl.ApiConfig.api_key = "n8WW2NvmWYZBERZFPNfz"

    def fetch_bitcoin_data(self):
        # Fetch historical Bitcoin price data
        btc_usd_price_kraken = quandl.get("BCHARTS/KRAKENUSD")
        return btc_usd_price_kraken

    def plot_bitcoin_prices(self, btc_data):
        btc_trace = go.Scatter(x=btc_data.index, y=btc_data['Weighted Price'])
        layout = go.Layout(title="Bitcoin Price Chart", xaxis=dict(title="Date"), yaxis=dict(title="Price (USD)"))
        fig = go.Figure(data=[btc_trace], layout=layout)
        py.iplot(fig)

if __name__ == "__main__":
    analyzer = BitcoinPriceAnalyzer()
    btc_data = analyzer.fetch_bitcoin_data()
    analyzer.plot_bitcoin_prices(btc_data)
