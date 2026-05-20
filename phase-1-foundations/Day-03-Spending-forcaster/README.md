# Day 03 — Spending Forecaster

## What I built
A command line spending forecaster that analyses historical 
expense data and predicts future financial behaviour. Unlike 
a basic expense tracker, this program answers the question 
every person managing money actually wants answered — 
"how much will I spend next month?"

## What I practised
- For loops and while loops
- List comprehensions and dictionary comprehensions
- String slicing to extract months from date strings
- Sorting data chronologically using sorted() with lambda
- datetime module for date arithmetic
- Breaking logic into focused, reusable functions

## Key concepts I struggled with and conquered

**1. List comprehensions**
A compact and Pythonic way to build a new list from an 
existing one in a single line. Instead of writing a for loop 
with append, you write the logic inline. I used this to 
extract dates and calculate totals across the expense list. 
This pattern appears constantly in data science code.

**2. Trend analysis using list slicing**
To determine whether spending in a category is going up or 
down, I sort all expenses chronologically, then split each 
category's amounts into two halves using slicing. If the 
second half total is higher than the first, the trend is 
rising. If lower, it is falling. This is a simplified version 
of the same logic used in real financial time-series analysis.

**3. Daily average forecasting**
Instead of assuming every month has the same number of days, 
I calculate the exact number of days covered by the data 
using datetime arithmetic — subtracting the earliest date 
from the latest. I then divide total spending by actual days 
tracked to get a true daily average, and multiply by 30 to 
forecast the next month. This is more accurate than simply 
averaging monthly totals.

## What I learned
- Real financial insight comes from comparing data over time, 
  not just summarising it
- Sorting data before analysing it is often a required first 
  step that is easy to forget
- A savings verdict means more than a raw number — context 
  turns data into decisions
- Using average monthly expense instead of total expense for 
  savings calculation gives a more honest and useful result

## What I would improve next time
Connect this forecaster to the expense tracker from Day 02 
so it analyses real recorded data instead of hardcoded 
expenses. The ultimate version would read from a CSV file 
saved by the tracker — closing the loop between recording 
and forecasting. This will be possible after Day 05 when I
covere file handling.

## How to run
python3 main.py