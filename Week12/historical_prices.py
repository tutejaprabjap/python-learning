import yfinance as yf

history = yf.Ticker('AAPL').history(
    start='2025-01-01', 
    end='2026-01-01', 
    interval='1d', 
    auto_adjust=False, 
    actions=True,
)
print(history.empty)

if not history.empty:
    print(history.shape)
    print(history.columns)

    print(history[['Close', 'Adj Close']].head())
    print(history[['Close', 'Adj Close']].isna().sum())
    print((history[["Close", "Adj Close"]] <= 0).sum())

    print(history.index.is_monotonic_increasing)
    print(history.index.is_unique)

    daily_returns = history['Adj Close'].pct_change(fill_method=None)
    print(daily_returns.head())

    total_return = (history['Adj Close'].iloc[-1] / history['Adj Close'].iloc[0]) - 1
    print(f"Total Return: {total_return:.2%}")

    valid_returns = daily_returns.dropna()
    growth_factors = valid_returns + 1
    compounded_return = growth_factors.prod() - 1
    print(f"Compounded return: {compounded_return:.2%}")

    

