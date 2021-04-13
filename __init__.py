# api key for alphavantage
alphavantage_api_key = "key1"
finnhub_api_key = "key2"


ticker = ''
interval = ''
api_key = alphavantage_api_key # finnhub_api_key
request = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}min&apikey={alphavantage_api_key}"
