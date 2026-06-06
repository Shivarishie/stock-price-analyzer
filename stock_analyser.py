import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Get the stock data:
def get_stock_data(symbol):
    stock = yf.download(symbol, period="2y", interval="1d")
    return stock

# Calculate moving avgs
def calculate_moving_averages(data):
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    return data

def generate_signal(data):
    latest_MA50 = data['MA50'].dropna().iloc[-1]
    latest_MA200 = data['MA200'].dropna().iloc[-1]
    
    if latest_MA50 > latest_MA200:
        print("Signal: GOLDEN CROSS - Consider BUYING (Upward Trend)")
    else:
        print("Signal: DEATH CROSS - Consider SELLING (Downward Trend)")

def plot_volume(data, symbol):
    volume = data['Volume'].squeeze()
    plt.figure(figsize=(14, 4))
    plt.bar(range(len(volume)), volume.values, color='purple', alpha=0.5)
    plt.title(f'{symbol} Trading Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)
    plt.show()

# Plot the chart 
def plot_stock(data, symbol):
    plt.figure(figsize=(14,7))
    plt.plot(data['Close'], label='Close price', color='blue')
    plt.plot(data['MA50'], label='50-Day MA', color='orange')
    plt.plot(data['MA200'], label='200-Day MA', color='red')
    plt.title(f'{symbol} Stock Price Analysis')
    plt.xlabel('Data')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main
symbol = input("Enter the Stock Name (eg. TCS.NS, RELIANCE.NS): ")
data = get_stock_data(symbol)
data = calculate_moving_averages(data)
generate_signal(data)
plot_volume(data, symbol)
plot_stock(data, symbol)
