import os

import requests



QUOTE_URL = "https://finnhub.io/api/v1/quote"
PROFILE_URL = "https://finnhub.io/api/v1/stock/profile2"


def get_stock_quote(symbol, api_key):
    params = {
        "symbol": symbol,
        "token": api_key,
    }

    try:
        response = requests.get(QUOTE_URL, params=params, timeout=10)
        response.raise_for_status()
        quote_data = response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error requesting stock data: {error}.")
        return None
    except requests.exceptions.JSONDecodeError:
        print("Error: Finnhub returned invalid JSON data.")
        return None


    current_price = quote_data.get("c")
    previous_close = quote_data.get("pc")
    daily_change = quote_data.get("dp")

    prices = (current_price, previous_close)

    if any(
        isinstance(price,bool)
        or not isinstance(price,(int,float))
        or price <= 0
        for price in prices
    ):
        return None

    if isinstance(daily_change,bool) or not isinstance(
        daily_change,(int,float)
    ):
        return None

    return {
        "current_price": current_price,
        "previous_close": previous_close,
        "daily_change": daily_change
    }


def get_company_name(symbol, api_key):
    params = {
        "symbol": symbol,
        "token": api_key,
    }

    try:
        response = requests.get(PROFILE_URL, params=params, timeout=10)
        response.raise_for_status()
        profile_data = response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error requesting stock data: {error}.")
        return None
    except requests.exceptions.JSONDecodeError:
        print("Error: Finnhub returned invalid JSON data.")
        return None

    name = profile_data.get("name")

    if not isinstance(name, str):
        return None

    name = name.strip()

    if not name:
        return None

    return name
    


def main():
    api_key = os.getenv("FINNHUB_API_KEY")

    if not api_key:
        print("Error: FINNHUB_API_KEY is not configured.")
        return

    symbol = input("Enter a stock symbol: ").strip().upper()

    if not symbol:
        print("Error: Stock symbol cannot be empty.")
        return

    quote = get_stock_quote(symbol, api_key)

    if quote is None:
        print(f"Error: No valid quote was found for {symbol}.")
        return

    name = get_company_name(symbol, api_key)

    if name is None:
        print(f"Error: No valid name was found for {symbol}")
        return

    print(f"\nStock Quote: {name} ({symbol})")
    print(f"Current price: ${quote['current_price']:.2f}")
    print(f"Previous close: ${quote['previous_close']:.2f}")
    print(f"Daily change: {quote['daily_change']:.2f}%")


if __name__ == "__main__":
    main()