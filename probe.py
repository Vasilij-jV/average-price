# import yfinance as yf
# import matplotlib.pyplot as plt
#
# # Загружаем данные о ценах акций за один день (сегодня)
# ticker_symbol = 'AAPL'  # Символ тикера для акции (например, AAPL для Apple)
# stock_data = yf.download(ticker_symbol, start='2024-04-9', end='2024-04-10', interval='1m')
#
# # Извлекаем данные о ценах закрытия за каждую минуту торгового дня
# closing_prices = stock_data['Close']
#
# # Создаем график
# plt.figure(figsize=(10, 6))
# closing_prices.plot()
# plt.title('Цены закрытия акций ' + ticker_symbol + ' за день')
# plt.xlabel('Время')
# plt.ylabel('Цена закрытия')
# plt.grid(True)
# plt.show()


import yfinance as yf
import matplotlib.pyplot as plt

# Создаем объект Ticker для нужной акции (например, Apple)
ticker_symbol = 'AAPL'
ticker = yf.Ticker(ticker_symbol)

# Получаем данные о ценах акций за один день
stock_data = ticker.history(period='10800m')

# Извлекаем данные о ценах закрытия за каждый интервал торгового дня (обычно интервалы - это минуты)
closing_prices = stock_data['Close']

# Создаем график
# plt.figure(figsize=(10, 6))
# closing_prices.plot()
# plt.title('Цены закрытия акций ' + ticker_symbol + ' за день')
# plt.xlabel('Время')
# plt.ylabel('Цена закрытия')
# plt.grid(True)
# plt.show()

print(closing_prices)
print(stock_data)
