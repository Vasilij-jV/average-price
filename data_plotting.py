import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


# Экспорт данных в CSV
def export_data_to_csv(data, filename):
    if isinstance(data, pd.DataFrame) and isinstance(filename, str):
        data.to_csv(filename, index=False)


def plot_technical_indicators(data, ticker, indicator):
    plt.figure(figsize=(14, 7))

    if indicator == 'RSI':
        plt.plot(data['RSI'], label='RSI')
        plt.title('RSI Chart for ' + ticker)
    elif indicator == 'MACD':
        plt.plot(data['MACD'], label='MACD', color='blue')
        plt.plot(data['Signal Line'], label='Signal Line', color='red')
        plt.title('MACD Chart for ' + ticker)

    plt.legend()
    plt.savefig(f"{ticker}_{indicator}_chart.png")
    print(f"{indicator} график сохранён, как {ticker}_{indicator}_chart.png")

