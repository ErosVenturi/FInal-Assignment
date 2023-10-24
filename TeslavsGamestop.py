!pip install yfinance==0.2.4 yfinance already installed
import yfinance as yf
import pandas as pd
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head()
tesla_revenue = tesla_data.tail()
tesla_revenue
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()
gme_revenue = gme_data.tail()
gme_revenue
tesla_data.plot(x="Date",y="Close")
gme_data.plot(x="Date", y="Close")
