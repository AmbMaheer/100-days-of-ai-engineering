# Day 13 — From Array to Time Series

## What I built
A command-line Python script that takes raw Elite Data Sim
sample data and transforms it into a time-aware Pandas DataFrame
The script automatically generates a calendar date index, performs
weekly and monthly revenue aggregation, calculates a 7-day rolling 
average (with and without minimum periods), and outputs a side-by-side
comparison of daily revenue against its rolling average for the final 10 days.

## What I practised
- `pd.date_range()` to automatically generate and fit
 a chronological timeline to raw data.
- `pd.DataFrame()` to structure raw NumPy arrays into 
a labeled, tabular format.
- `.resample('W').sum()` to aggregate daily revenue data i
nto broader time periods (weekly and monthly).
- `.rolling(window=7).mean()` to calculate moving averages while 
respecting the integrity of the dataframe's index.

## Key concepts I struggled with and conquered

**1. The Alignment Trap: `convolve()` vs. `.rolling()`**
Using NumPy's `convolve()` shrinks a 97-day array down to 91 days. 
If mapped directly back to the original calendar, the data misaligns 
silently—January 1st wrongly inherits the average meant for January 7th, 
shifting every record backward by 6 days. This happens because NumPy 
arrays are entirely unaware of date labels. Pandas' `rolling()` solves 
this by preserving the original array length of 97, injecting `NaN` into 
the first 6 slots to guarantee perfect chronological alignment.

**2. Automating Date Generation**
Looking at the instructions, my first instinct was to add the dates manually. 
However, I realized that hardcoding data is rarely the right approach in programming. 
I checked the Pandas documentation and discovered the `pd.date_range()` function, 
which allowed me to manipulate and generate the entire timeline automatically 
with a single line of code.

## What I learned
- `pd.date_range()` is the proper, scalable way to add dates to existing 
data without manually scattering or hardcoding the actual dataset.
- `.resample()` is a much safer and more flexible tool for handling the 
aggregation of data over time compared to NumPy's `.reshape()`.
- `.rolling()` calculates a moving window while preserving the exact original 
row count by padding the early days with blanks, guaranteeing the timeline never shifts.

## What I would improve next time
I want to focus more deeply on *what* the underlying code does 
mathematically, rather than just writing it to test if a function 
works. Understanding the mechanics beneath the functions helps me 
interpret my output more accurately.

## How to run
python3 main.py