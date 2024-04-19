import yfinance as yf
from pprint import pprint


def fetch_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=15):
    data['Moving_Average'] = data['High'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(stock_data):
    average_close = stock_data['Close'].mean()
    print(f'Среднее значение колонки "Close": {average_close}')


