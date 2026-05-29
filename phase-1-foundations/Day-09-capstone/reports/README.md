# Day 09 — Phase 1 Capstone: Daily Intelligence Report

## What I built
A fully automated daily intelligence report system that 
combines every concept from Days 01 through 08 into one 
program. It loads real Elite Data Sim sales data from a 
CSV file, runs a complete financial analysis using pandas, 
fetches live exchange rates from an API, converts total 
revenue into USD, EUR and GBP, generates a terminal bar 
chart of monthly trends, and saves a timestamped report 
file automatically. This is the culmination of Phase 1.

## What I practised
- Importing and orchestrating multiple custom modules
- Loading and analysing CSV data with pandas
- Fetching live data from an external API using requests
- Securing API keys with python-dotenv
- Cross-currency conversion using base currency arithmetic
- Generating dynamic terminal bar charts with proportional scaling
- Writing timestamped files with os.makedirs and datetime
- Using if __name__ == "__main__" correctly
- Debugging return value mismatches between modules

## Key concepts I struggled with and conquered

**1. Orchestrating multiple modules cleanly**
The biggest challenge was not any single concept but 
making four separate modules work together without mixing 
their responsibilities. main.py must contain zero 
calculations — every number in the report comes from a 
function in analysis.py, forecaster.py or currency.py. 
When a number was wrong the debugging process required 
tracing back through the chain of function calls to find 
exactly where the logic broke. This is how real production 
debugging works.

**2. Return value unpacking**
profit_summary() returns three values — total profit, 
average profit per sale, and profit by package as a tuple. 
Assigning the result to a single variable and then trying 
to format it as a number caused a crash. The fix was 
unpacking all three return values correctly:
total_profit, avg_profit, profit_by_pkg = analysis.profit_summary(sales_data)
Understanding what a function returns before using it is 
a discipline this project made concrete.

**3. Dynamic bar chart generation**
Building a proportional bar chart in the terminal required 
figuring out a scaling factor — dividing each month's 
revenue by a constant to determine how many block 
characters to print. Getting the scale right so the chart 
is readable without overflowing the terminal required 
experimentation. This is a simplified version of the 
normalisation logic used in real data visualisation.

**4. Virtual environment navigation across multiple projects**
With nine project folders each having their own virtual 
environment, activating the correct interpreter in VS Code 
required learning to use Python: Select Interpreter 
manually rather than relying on automatic detection. 
This is a practical skill that becomes essential when 
managing multiple projects professionally.

## What I learned
- A program that combines multiple modules is only as 
  clean as the boundaries between them — when each module 
  does exactly one job, debugging becomes a process of 
  isolating which module produced a wrong value
- Reading your own function signatures before calling them 
  prevents the majority of integration bugs
- The if __name__ == "__main__" guard is not optional 
  in any script that might be imported elsewhere
- Saving output to a timestamped file turns a one-time 
  script into a reusable business tool

## What I would improve next time
Replace the terminal bar chart with matplotlib visualisations 
— a bar chart for monthly revenue and a pie chart for 
package breakdown. Add a 30-day forecast section using 
the forecaster module from Day 03. These two additions 
would make this a complete business intelligence tool 
rather than a financial summary.

## How to run
Create a .env file with your API key:
EXCHANGE_API_KEY=your_key_here

Then run:
source env/bin/activate
python3 main.py