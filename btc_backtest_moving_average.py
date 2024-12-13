import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# Step 1: Download Historical Bitcoin Data
# -----------------------------------
data = yf.download('BTC-USD', start='2020-01-01', end='2023-01-01')

# -----------------------------------
# Step 2: Calculate Moving Averages
# -----------------------------------
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['SMA200'] = data['Close'].rolling(window=200).mean()

# -----------------------------------
# Step 3: Generate Buy/Sell Signals
# Buy signal when SMA50 > SMA200, Sell when SMA50 < SMA200
# Signal = 1 (long position), 0 (no position)
# Position = difference of Signal to identify buy/sell events
# -----------------------------------
data['Signal'] = 0
data['Signal'][200:] = (data['SMA50'][200:] > data['SMA200'][200:]).astype(int)
data['Position'] = data['Signal'].diff()

# -----------------------------------
# Step 4: Simulate Trading
# We start with $10,000 and go "all-in" on buy signals, and fully sell on sell signals.
# -----------------------------------
initial_cash = 10000
cash = initial_cash
btc_held = 0
portfolio_values = []

for i in range(len(data)):
    price = data['Close'].iloc[i]
    
    # Buy signal: Position = 1 means we moved from 0 to 1 (Cross above)
    if data['Position'].iloc[i] == 1:
        # Buy BTC with all available cash
        if cash > 0:
            btc_held = cash / price
            cash = 0
    
    # Sell signal: Position = -1 means we moved from 1 to 0 (Cross below)
    elif data['Position'].iloc[i] == -1:
        # Sell all BTC held
        if btc_held > 0:
            cash = btc_held * price
            btc_held = 0
    
    # Track portfolio value: cash + (btc_held * current_price)
    portfolio_values.append(cash + btc_held * price)

data['Portfolio'] = portfolio_values

# -----------------------------------
# Step 5: Evaluate Performance
# -----------------------------------
final_portfolio_value = data['Portfolio'].iloc[-1]
profit_loss = final_portfolio_value - initial_cash
max_drawdown = (data['Portfolio'] - data['Portfolio'].cummax()).min()

print(f"Final Portfolio Value: ${final_portfolio_value:.2f}")
print(f"Total Profit/Loss: ${profit_loss:.2f}")
print(f"Maximum Drawdown: ${max_drawdown:.2f}")

# -----------------------------------
# Step 6: Visualization
# -----------------------------------
plt.figure(figsize=(12,8))

# Subplot 1: Bitcoin Price and SMAs
plt.subplot(2, 1, 1)
plt.title('Bitcoin Price with SMA Crossover Strategy')
plt.plot(data['Close'], label='BTC-USD Price', alpha=0.6)
plt.plot(data['SMA50'], label='50-Day SMA', color='red')
plt.plot(data['SMA200'], label='200-Day SMA', color='green')
plt.legend(loc='upper left')

# Subplot 2: Portfolio Value
plt.subplot(2, 1, 2)
plt.title('Portfolio Value Over Time')
plt.plot(data['Portfolio'], label='Portfolio', color='orange')
plt.xlabel('Date')
plt.ylabel('Portfolio Value ($)')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
