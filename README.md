# Bitcoin Moving Average Crossover Backtest (From Scratch)

This repository contains Python code for a simple moving average crossover backtest on Bitcoin (BTC-USD) daily historical data. The strategy uses a 50-day and 200-day Simple Moving Average (SMA) to generate buy and sell signals and simulates the performance over time without relying on external backtesting frameworks.

## Features

- **Data Retrieval**: Uses `yfinance` to download historical Bitcoin price data.
- **Simple Moving Averages (SMA)**: Implements 50-day and 200-day SMAs to identify trends.
- **Trading Logic**: 
  - **Buy Signal**: When the 50-day SMA crosses above the 200-day SMA.
  - **Sell Signal**: When the 50-day SMA crosses below the 200-day SMA.
- **Trade Simulation**: Simulates going "all-in" with a starting capital of \$10,000 on buy signals and selling all holdings on sell signals.
- **Performance Metrics**: Prints the final portfolio value, total profit/loss, and maximum drawdown.
- **Visualization**: Plots both Bitcoin’s price with SMAs and the portfolio value over time.

## Requirements

- **Python 3.7+**
- **Dependencies**:
  - `yfinance` for historical data
  - `pandas` for data manipulation
  - `matplotlib` for visualization

Install dependencies using:
```bash
pip install yfinance pandas matplotlib
# backtesting
btc_backtest_moving_average
