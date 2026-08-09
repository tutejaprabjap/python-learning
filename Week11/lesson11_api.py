import requests


API_BASE_URL = "https://api.frankfurter.dev/v2"


def get_exchange_rate(base_currency, target_currency):
    url = (
        f"{API_BASE_URL}/rate/"
        f"{base_currency.upper()}/{target_currency.upper()}"
    )

    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data["rate"]


    except requests.Timeout:
        print("The exchange-rate service took too long to respond.")
        return None

    except requests.HTTPError:
        print("The exchange-rate service returned an HTTP error.")
        return None

    except KeyError:
        print("The API response did not contain a rate.")
        return None

    except requests.RequestException:
        print("The exchange-rate request failed.")
        return None

    if isinstance(rate, bool) or not isinstance(rate, (int, float)):
        print("The exchange rate is not a int or a float.")
        return None

    if rate <= 0: 
        print("The exchange rate must be greater than zero.")
        return None

    return rate


base_currency = "USD"
target_currency = "EUR"

exchange_rate = get_exchange_rate(base_currency, target_currency)

if exchange_rate is not None:
    print(
        f"1 {base_currency} = "
        f"{exchange_rate} {target_currency}"
    )