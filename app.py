import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price Analyzer")
st.write("Analyze stock trends using Moving Averages")

symbol = st.text_input("Enter Stock Symbol (e.g. TCS.NS, RELIANCE.NS):")

if symbol:
    data = yf.download(symbol, period="5y", interval="1d")
    
    if data.empty:
        st.error("Invalid symbol. Please try again.")
    else:
        # Moving averages
        data['MA50'] = data['Close'].rolling(window=50).mean()
        data['MA200'] = data['Close'].rolling(window=200).mean()
        
        # Buy/Sell Signal
        latest_MA50 = data['MA50'].dropna().iloc[-1]
        latest_MA200 = data['MA200'].dropna().iloc[-1]
        
        if latest_MA50 > latest_MA200:
            st.success("Signal: GOLDEN CROSS - Consider BUYING (Upward Trend)")
        else:
            st.error("Signal: DEATH CROSS - Consider SELLING (Downward Trend)")
        
        # Price chart
        st.subheader("Price Chart with Moving Averages")
        fig1, ax1 = plt.subplots(figsize=(14, 7))
        ax1.plot(data['Close'], label='Close Price', color='blue')
        ax1.plot(data['MA50'], label='50-Day MA', color='orange')
        ax1.plot(data['MA200'], label='200-Day MA', color='red')
        ax1.set_title(f'{symbol} Stock Price Analysis')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price')
        ax1.legend()
        ax1.grid(True)
        st.pyplot(fig1)
        
        # Volume chart
        st.subheader("Trading Volume")
        volume_data = data['Volume'].squeeze()
        fig2, ax2 = plt.subplots(figsize=(14, 4))
        ax2.bar(data.index, volume_data, color='purple', alpha=0.5)
        ax2.xaxis_date()
        fig2.autofmt_xdate()
        ax2.set_title(f'{symbol} Trading Volume')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Volume')
        ax2.grid(True)
        st.pyplot(fig2)