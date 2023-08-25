from polygon import RESTClient
import pandas as pd

# Import DotEnv #
import os
from dotenv import load_dotenv

import datetime as dt
import plotly.graph_objects as go
from plotly.offline import plot

# Load the .env 
load_dotenv()

# Assign the API key to a variable 
API_KEY = os.getenv('polygon_api_key')

# Create a REST client
client = RESTClient(API_KEY)

counter = 0
tickers = []
for t in client.list_tickers(market='stocks',limit=1000):
    tickers.append(t.ticker)
    counter += 1
    
exchanges = pd.DataFrame(client.get_exchanges(asset_class='stocks', locale='us'))
exchangeList = list(set(exchanges.mic))
exchangeList.remove(None)

usTickers = []
for x in exchangeList:
     for t in client.list_tickers(market='stocks',exchange=x, active=False, limit=1000):
        usTickers.append(t.ticker)
            
finalTickerList = set(usTickers)

#for y in finalTickerList:
#   dataRequest = client.get_aggs(ticker=str(y), multiplier=1, timespan= 'day', from_= '2023-08-01', to='2023-08-23')
#   print(y,dataRequest)

snapshot = client.get_snapshot_all(market_type='stocks',include_otc=False)
print(snapshot.ticker)

