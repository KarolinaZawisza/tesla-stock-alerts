import requests

def get_stock_data():
    parameters = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': 'TSLA',
        'apikey': 'RFVSHUB6CQ4PPB53'
    }

    alphavantage_api = requests.get('https://www.alphavantage.co/query', params=parameters)
    json_alphavantage = alphavantage_api.json()["Time Series (Daily)"]
    stock_list = [value for (key, value) in json_alphavantage.items()]
    yesterday_data = stock_list[0]
    day_before_yesterday_data = stock_list[1]
    yesterday_closing_price = yesterday_data['4. close']
    day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
    latest_value = yesterday_data['1. open']

    return [yesterday_closing_price, day_before_yesterday_closing_price, latest_value]
