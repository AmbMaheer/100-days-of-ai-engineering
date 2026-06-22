# Day 14 — Multi-Product Sales Engine

## What I built
A command line multi-product analytical engine for Elite Data Sim 
that simulates 97 days of randomised transaction logs across three 
tiered products. The engine extracts total revenue and profit per 
product, calculates average daily units sold, and performs 
time-series aggregation — weekly resampling and rolling averages — 
all split by product using groupby().

## What I practised
- Generating reproducible random transaction data with np.random.seed(42)
- Structuring multi-product business data with dictionaries for price/cost lookup
- Vectorised profit calculation across the whole DataFrame
- groupby() to split analysis by product before aggregating
- Combining groupby() with resample() and rolling() for per-product time series
- pd.pivot_table() to reshape data into a business-readable comparison table

## Key concepts I struggled with and conquered

**1. Verifying output instead of trusting an autocomplete guess**
My first draft had comments stating specific revenue and unit 
numbers per product that were never actually printed or checked — 
VS Code's AI autocomplete suggested plausible-sounding conclusions 
and I accepted them without running the code to confirm. When I 
added real print() statements, the average daily units numbers 
were wrong (autocomplete guessed 30GB=2.5, 60GB=3.2, 120GB=1.8; 
actual output was 120GB=3.2, 30GB=2.8, 60GB=3.4). The revenue and 
profit rankings happened to match by coincidence. The lesson: a 
comment stating a number is a claim about reality, and it needs 
to come from something I actually looked at, not from whatever 
looked plausible enough to autocomplete.

**2. Why grouping before rolling matters**
Running .rolling(7) directly on the revenue column without 
grouping by product first would average together 7 consecutive 
ROWS, not 7 days of any single product — since the raw data has 
products interleaved day after day, a window could mix 120GB, 
30GB, and 60GB rows into one meaningless average. The same 
misalignment risk from Day 13 (NumPy arrays losing their 
positional meaning) shows up again here in a different form: 
without grouping, the rolling window loses its CATEGORY meaning 
instead of its date meaning. df.groupby('product')['revenue'].rolling(7) 
fixes this by calculating a separate, correctly-windowed rolling 
average for each product independently.

## What I learned
- np.random.seed(42) fixes the random number generator's starting 
  point, so the same "random" data is produced every time the 
  script runs — without it, debugging is impossible because the 
  data changes on every run and you can never tell if a fix 
  actually worked or the numbers just changed by chance
- groupby() splits a DataFrame by category before any aggregation 
  runs, so .sum(), .mean(), or .rolling() apply separately within 
  each group instead of mixing categories together
- pd.pivot_table() turns a long multi-index Series into a wide, 
  human-readable table — rows as time periods, columns as 
  categories — which is the format a business owner actually 
  wants to look at, not a stacked index
- A comment describing output is only valid if I have personally 
  seen that output printed and checked it against the code that 
  produced it

## What I would improve next time
Build the version of this engine that doesn't just describe what 
already happened across multiple products, but forecasts what 
each product's revenue will look like next week — extending the 
Day 12 trend-line approach to work per-product instead of for 
one combined revenue stream.

## How to run
python3 main.py