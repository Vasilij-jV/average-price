import data_download as dd
import data_plotting as dplt
from pprint import pprint


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet "
        "Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
        "с начала года, макс.")

    enter_ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    enter_period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    ticker = enter_ticker
    period = enter_period
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # calculates and displays the average closing price of shares for a given period
    dd.calculate_and_display_average_price(stock_data)

    # fluctuations_price
    threshold = 5
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Exporting object DataFrame in file
    # Тест, проверяющий создание нового файла в 'export_test.py'
    filename = 'save_dataframe.csv'
    dplt.export_data_to_csv(stock_data, filename)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()
