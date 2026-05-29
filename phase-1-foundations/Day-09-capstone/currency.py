import requests
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")
def get_exchange_rates(base_currency, api_key):
    """"Fetches exchange rates for the given base currency using the ExchangeRate-API.
    Args: base_currency (str): The currency for which to fetch exchange rates (e.g., "USD", "NGN", "EUR").
        api_key (str): Your API key for the ExchangeRate-API.
    Returns:
        dict: A dictionary containing the exchange rates for the specified base currency.
    """
    # calls the API and returns a dictionary of rates
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}' 
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # raises error for 4xx and 5xx
        data = response.json()
        return data.get("conversion_rates")
    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your network.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"API error: {e}")
        return None
    
    # example: {"USD": 1, "NGN": 1547.23, "EUR": 0.92}


def convert_currency(amount, from_currency, to_currency, rates):

    """"Converts an amount from one currency to another using the provided exchange rates.
    Args:        amount (float): The amount of money to convert.
    from_currency (str): The currency code of the amount to convert (e.g., "USD", "NGN", "EUR").    
    to_currency (str): The currency code to which the amount should be converted (e.g., "USD", "NGN", "EUR").    
    rates (dict): A dictionary containing exchange rates for various currencies relative to a base currency.  
    Returns:  float: The converted amount in the target currency.   """   
    # uses the fetched rates to convert
    rate = rates.get(to_currency) / rates.get(from_currency)
    amount_in_to_currency = amount * rate
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()


    # returns the converted amount
    return amount_in_to_currency

def show_ngn_rates(rates):
    # shows how much 1 NGN is worth in USD, EUR.
    ngn_to_usd = rates.get("USD") / rates.get("NGN")
    ngn_to_eur = rates.get("EUR") / rates.get("NGN")
    ngn_to_ngn = rates.get("NGN") / rates.get("NGN")
    
    return ngn_to_usd, ngn_to_eur, ngn_to_ngn