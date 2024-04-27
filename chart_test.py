import unittest
from data_download import calculate_rsi_from_yfinance, calculate_macd_from_yfinance
from data_plotting import plot_technical_indicators
import pandas as pd
import os


class TestTechnicalIndicators(unittest.TestCase):

    def setUp(self):
        self.ticker = 'AAPL'

    def test_rsi_calculation(self):
        data_rsi = calculate_rsi_from_yfinance(self.ticker)
        self.assertIsInstance(data_rsi, pd.DataFrame)
        self.assertTrue('RSI' in data_rsi.columns)

    def test_macd_calculation(self):
        data_macd = calculate_macd_from_yfinance(self.ticker)
        self.assertIsInstance(data_macd, pd.DataFrame)
        self.assertTrue('MACD' in data_macd.columns)
        self.assertTrue('Signal Line' in data_macd.columns)

    def test_rsi_chart_saved(self):
        data_rsi = calculate_rsi_from_yfinance(self.ticker)
        plot_technical_indicators(data_rsi, self.ticker, 'RSI')
        self.assertTrue(os.path.exists(f"{self.ticker}_RSI_chart.png"))

    def test_macd_chart_saved(self):
        data_macd = calculate_macd_from_yfinance(self.ticker)
        plot_technical_indicators(data_macd, self.ticker, 'MACD')
        self.assertTrue(os.path.exists(f"{self.ticker}_MACD_chart.png"))


if __name__ == '__main__':
    unittest.main()
