# Day 04 — Financial Calculator Module

## What I built
A two-file command line financial calculator that computes 
profit after tax, Return on Investment, break-even point, 
compound interest, and financial transaction summaries. 
The logic and the interface are completely separated into 
two files — finance.py handles all calculations and main.py 
handles all user interaction.

## What I practised
- Separating logic from interface across two files
- Importing a custom module using import
- Defining functions with default parameters
- Using *args to accept a variable number of arguments
- Input validation with while True and try/except
- Handling edge cases before they cause crashes

## Key concepts I struggled with and conquered

**1. The *args packing and unpacking pattern**
When a function is defined with *args, Python collects all 
arguments passed to it into a tuple. When calling that 
function with a list, the * operator unpacks the list into 
individual arguments before the function repacks them. 
Understanding both directions — packing on the definition 
side and unpacking on the calling side — took time but is 
now clear. This is how Python libraries accept flexible 
numbers of inputs.

**2. Distinguishing income from expenses in summarize_finances**
To separate income from expenses without adding an extra 
parameter, I used the sign of the number — positive values 
are income, negative values are expenses. This is the 
standard convention in accounting and financial software. 
The function uses generator expressions to filter and 
calculate each group independently.

**3. Guarding against empty input**
When a user enters 0 immediately without recording any 
transactions, calling the summary function with no data 
causes unnecessary processing and misleading output. 
The fix was a simple length check before calling the 
function — if no transactions were recorded, return to 
the menu immediately. Stressing a system with empty data 
is a bad practice, especially in financial software where 
a result of zero and no result are two different things.

## What I learned
- Separating logic from interface makes both easier to 
  test, debug and extend independently
- Financial formulas like ROI, break-even and compound 
  interest are just arithmetic — the challenge is 
  translating the formula correctly, not the code itself
- Handling edge cases like division by zero and empty 
  input is not optional in financial systems — wrong 
  output is worse than no output

## What I would improve next time
Integrate this calculator with the expense tracker from 
Day 02 so it reads real recorded transactions automatically 
instead of requiring manual input. The ultimate version 
would monitor transaction data continuously and recalculate 
financial summaries in real time — closer to how actual 
accounting software works.

## How to run
python3 main.py