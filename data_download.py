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
    print(f'Среднее значение колонки "Close": {average_close}\n')


def notify_if_strong_fluctuations(data, threshold):
    # Создаю список значений закрытия цен за период
    list_prices_close = data['Close'].tolist()
    # Определяю начальную цену закрытия за период
    initial_float = list_prices_close[0]
    # Определяю минимальную и максимальную цены закрытия за период
    max_float, min_float = max(list_prices_close), min(list_prices_close)
    # Вычисляю изменение цены за период между начальным и минимальным значениями в процентах
    price_change_between_initial_and_minimum = ((min_float - initial_float) / initial_float) * 100
    # Вычисляю изменение цены за период между начальным и максимальным значениями в процентах
    price_change_between_initial_and_maximum = ((max_float - initial_float) / initial_float) * 100
    # Вычисляю разницу в процентах между изменениями цены до минимального значения и до максимального значения
    difference_between_min_max = price_change_between_initial_and_maximum - price_change_between_initial_and_minimum
    if difference_between_min_max > threshold:
        print(f'Порог колебания цены - ({difference_between_min_max}) превышает допустимое значение - ({threshold})\n')


def calculate_rsi_from_yfinance(ticker, window=14):
    data = yf.Ticker(ticker).history(period='1y')
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data


def calculate_macd_from_yfinance(ticker, short_window=12, long_window=26, signal_window=9):
    data = yf.Ticker(ticker).history(period='1y')
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()

    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_window, adjust=False).mean()

    data['MACD'] = macd
    data['Signal Line'] = signal_line
    return data
