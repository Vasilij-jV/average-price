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
    # Определяю начальную и конечную цены закрытия за период
    initial_float, final_float = list_prices_close[0], list_prices_close[-1]
    # Определяю минимальную и максимальную цены закрытия за период
    max_float, min_float = max(list_prices_close), min(list_prices_close)
    # Вычисляю изменение цены за период между начальным и конечным значениями в процентах
    price_change_over_the_period = ((final_float - initial_float) / initial_float) * 100
    # Вычисляю разницу цены между минимальным и максимальным значениями в процентах
    price_change_min_max = ((max_float - min_float) / min_float) * 100
    # Вычисляю коэффициент между изменением цены за период и разницой между минимальным и максимальным
    # значениями
    ratio = price_change_over_the_period / price_change_min_max
    if ratio < threshold:
        print(f'Порог колебания цены - ({ratio}) превышает допустимое значение - ({threshold})\n')


