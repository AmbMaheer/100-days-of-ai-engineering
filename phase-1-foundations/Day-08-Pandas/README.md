# Day 08 — Sales Analysis Engine

## What I built
A two-file sales analysis engine that loads real business 
data from a CSV file and produces a complete financial report 
— total revenue, profit summary, revenue by package, top 
customers, monthly breakdown and busiest month. Built on 
real Elite Data Sim sales data exported from Supabase.

## What I practised
- Loading CSV files into pandas DataFrames with pd.read_csv()
- Converting date strings to datetime using pd.to_datetime()
- Grouping and aggregating data with groupby()
- Sorting results with sort_values() and nlargest()
- Extracting month and year from dates using the .dt accessor
- Adding calculated columns to a DataFrame
- Separating analysis logic from report output across two files

## Key concepts I struggled with and conquered

**1. groupby() and aggregation**
groupby() solves the problem of categorising and summarising 
data without writing complex dictionary loops. It works like 
an instant pivot table — group all sales by package name, 
then call .sum() or .count() and pandas handles everything 
underneath. What took 10 lines of dictionary logic in Day 02 
takes one line in pandas. Understanding that groupby() 
returns a GroupBy object that you then chain an aggregation 
method onto was the key mental shift.

**2. Column name discipline**
pandas is unforgiving with column names — a single typo 
gives you a KeyError that crashes the entire program. I 
learned to always check my actual CSV headers first before 
referencing them in code. The habit of printing 
df.columns at the start of any new dataset is now part 
of how I work.

**3. The .dt accessor**
To extract the month from a datetime column you cannot 
use normal string slicing. pandas provides a .dt accessor 
that unlocks date-specific operations on a datetime Series. 
sales_data['sale_date'].dt.to_period('M') converts each 
date into a year-month period like 2026-03 which can then 
be grouped and sorted chronologically. Finding this in the 
documentation without being told was the turning point of 
the day.

**4. Keeping analysis and interface separated**
main.py contains zero calculations. Every number in the 
report comes from a function in analysis.py. main.py only 
calls functions and formats the output. This separation 
means the analysis engine can be imported into any other 
project — a web app, a dashboard, an API — without changing 
a single line.

## What I learned
- pandas replaces complex for loops with single readable 
  lines — the same logic that took 15 lines in Day 02 
  takes 1 line with groupby()
- Real data analysis always starts with loading, then 
  cleaning, then analysing — in that order
- A DataFrame is not just a table — it is a programmable 
  object with hundreds of built-in methods that understand 
  the shape and type of your data
- Profit calculation belongs in the data layer using actual 
  cost values per row, not as a hardcoded percentage guess

## What I would improve next time
Add matplotlib to visualise the monthly revenue as a bar 
chart and the package breakdown as a pie chart. Numbers 
in a terminal are useful but a chart communicates