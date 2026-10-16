import pandas as pd

practice_prices = {
    "AAPL": [100.0, 102.0, 101.0],
    "MSFT": [200.0, 198.0, 202.0],
    "JPM": [150.0, 151.0, 153.0],
}

dates = pd.to_datetime([
    "2026-10-05",
    "2026-10-06",
    "2026-10-07",
])

prices = pd.DataFrame(practice_prices, index=dates)
prices.index.name = "Date"

print(prices)
print(prices.shape)
print(prices.dtypes)
print(prices["AAPL"])

print(prices[["JPM", "MSFT"]])
print(prices.loc["2026-10-07"])
print(prices.loc["2026-10-06", "AAPL"])

previous_price = prices.loc["2026-10-05", "AAPL"]
current_price = prices.loc["2026-10-06", "AAPL"]
daily_return = (current_price / previous_price) - 1
print(f"AAPL daily return: {daily_return:.2%}")

daily_returns = prices.pct_change(fill_method=None)
print(daily_returns)
print(f"{daily_returns.loc["2026-10-07", "AAPL"]:.2%}")

total_returns = (prices.iloc[-1] / prices.iloc[0]) - 1
print(total_returns)

weights = pd.Series({
    "AAPL": 1 / 3,
    "MSFT": 1 / 3,
    "JPM": 1 / 3,
})
weighted_returns = total_returns * weights
portfolio_return = weighted_returns.sum()
print("Weighted return contributions:") 
print(weighted_returns)
print(f"Portfolio return: {portfolio_return:.2%}")
print()

initial_investment = 3000
portfolio_profit = initial_investment * portfolio_return
ending_value = initial_investment + portfolio_profit
print(f"Portfolio profit: {portfolio_profit:,.2f}")
print(f"Ending value: {ending_value:,.2f}")
print()

initial_allocations = initial_investment * weights
stock_profits = initial_allocations * total_returns
print(initial_allocations)
print(stock_profits)
print(f"Total stock profits: ${stock_profits.sum():.2f}")

ending_allocations = initial_allocations + stock_profits
ending_weights = ending_allocations / ending_allocations.sum()
print(f"\n{ending_allocations}")
print(ending_weights)
print(ending_weights.sum())

shares = initial_allocations / prices.iloc[0]
print(f"\n{shares}")

holding_values = prices * shares
portfolio_values = holding_values.sum(axis=1)
print(f"\n{holding_values}")
print(portfolio_values)

portfolio_daily_returns = portfolio_values.pct_change(fill_method=None)
print(f"\n{portfolio_daily_returns}")
print(f"{portfolio_daily_returns.loc["2026-10-07"]:.2%}")

valid_returns = portfolio_daily_returns.dropna()
growth_factors = 1 + valid_returns
compounded_return = growth_factors.prod() - 1
print(f"\nCompounded Return: {compounded_return:.2%}")

cumulative_returns = (
    portfolio_values / portfolio_values.iloc[0]
) - 1
print(f"\n{cumulative_returns}")

portfolio_summary = pd.DataFrame({
    "Portfolio Value": portfolio_values,
    "Daily Return": portfolio_daily_returns,
    "Cumulative Return": cumulative_returns,
})
print(f"\n{portfolio_summary}")
