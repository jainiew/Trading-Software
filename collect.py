# background process to download data from api
import database as db
import requests
import sys
# from config import alphavantage_api_key, finnhub_api_key
import time

# args = sys.argv[1:]
# ticker, interval = args


# drop any existing tables
db.delete()
# create new table
db.create_table()

# ----- source 1 -----
# download data once
ticker = 'IBM'
interval = '5'
alphavantage_api_key = 'demo'
q = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}min&apikey={alphavantage_api_key}"

response = requests.get(q)
data = response.json()
for key in data.keys():
    if key.startswith('Time'):
        # get all dates from keys
        times = list(data[key])
        for t in times:
            # Example JSON: {'1. open': '135.3100', '2. high': '135.3100', '3. low': '135.3100', '4. close': '135.3100', '5. volume': '364'}
            # Example time: 2021-04-09 18:25:00
            open = data[key][t]['1. open']
            high = data[key][t]['2. high']
            low = data[key][t]['3. low']
            close = data[key][t]['4. close']
            # insert into database
            db.insert(ticker, t, float(open), float(high), float(low), float(close))

# ----- source 2 -----
# download data given interval
# https://finnhub.io/docs/api/quote
# q = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={finnhub_api_key}"
# while True:
#     r = requests.get(q)
#     data = r.json()

#     open = data['o']
#     high = data['h']
#     low = data['l']
#     close = data['c']
#     t = data['t'] # UTC ?
#     db.insert(ticker, t, float(open), float(high), float(low), float(close))
#     time.sleep(int(interval))
