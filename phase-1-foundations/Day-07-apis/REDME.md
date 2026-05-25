# Day 07 — Live Currency Converter with Real Exchange Rates

## What I built
A command line currency converter that fetches live exchange 
rates from the ExchangeRate-API and performs real-time 
currency conversions between NGN, USD and EUR. Unlike the 
Day 01 version which used hardcoded rates that go stale 
immediately, this version always reflects the current market 
rate at the moment of conversion.

## What I practised
- Making HTTP GET requests using the requests library
- Parsing JSON responses into Python dictionaries
- Loading API keys securely from a .env file using python-dotenv
- Cross-currency conversion using a base currency as the bridge
- Separating API calls, calculations and interface into 
  distinct functions

## Key concepts I struggled with and conquered

**1. Cross-currency conversion math**
The API returns all rates relative to one base currency — USD. 
To convert NGN to EUR directly you cannot use the rates 
straight from the dictionary. You must go through the base 
currency as a middle step. The formula is:

  converted = amount * (rate_of_target / rate_of_source)

For example, to convert NGN to EUR:
  result = amount * (EUR_rate / NGN_rate)

This works because dividing one rate by another cancels out 
the base currency and gives you the direct conversion factor. 
Writing this on paper before touching the code made the 
implementation straightforward.

**2. Keeping API keys out of code**
Hardcoding an API key directly in a script means anyone who 
sees the code can use your key, exhaust your quota, or rack 
up charges on your account. The correct approach is storing 
the key in a .env file, adding .env to .gitignore, and 
loading it at runtime using python-dotenv and os.getenv(). 
The code never contains the key — only a reference to where 
the key lives.

**3. Real world API responses**
The API does not return just the rates — it returns a nested 
dictionary with metadata, result status and the conversion 
rates buried inside a key called conversion_rates. Learning 
to navigate a real API response by reading the documentation 
first, then using .get() to extract exactly what I need, 
is a foundational skill for working with any external data 
source.

## What I learned
- HTTP GET requests fetch data that already exists on a server
- APIs return JSON which Python's requests library converts 
  automatically into dictionaries using .json()
- API keys are secrets — they belong in .env files, never 
  in source code, never on GitHub
- Reading the official API documentation before writing code 
  saves more time than it costs

## What I would improve next time
Add proper error handling for three failure cases — no 
internet connection which raises a ConnectionError, an 
invalid API key which returns a 401 status, and an 
unrecognised currency code. Currently the program assumes 
everything works. In production software that assumption 
always breaks eventually.

## How to run
Create a .env file with your API key:
EXCHANGE_API_KEY=your_key_here

Then run:
source env/bin/activate
python3 main.py