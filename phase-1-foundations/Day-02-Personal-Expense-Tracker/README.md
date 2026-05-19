# Day 02 — Personal Expense Tracker

## What I built
A command line personal finance tracker that allows users to 
record their daily expenses, organize them by category, and 
generate a financial summary. The system validates all input 
before recording it, ensuring clean and reliable data.

## What I practised
- Importing and using Python modules
- Lists and dictionaries as core data structures
- Functions — separating each action into its own reusable block
- Input validation loops
- Indentation and code structure

## Key concepts I struggled with and conquered

**1. Input validation with while True**
The first version of this program accepted anything the user 
typed — wrong categories, invalid amounts, incorrectly 
formatted dates. It took me hours to figure out how to force 
the program to reject bad input and keep asking until the user 
provides something valid. The solution was combining while True 
with try/except and break — the same defensive programming 
pattern I discovered on Day 01, now applied more deeply across 
multiple input fields including date validation using Python's 
datetime module.

**2. Dictionary accumulation pattern**
To calculate total spending per category I had to build a 
dictionary dynamically from scratch. I start with an empty 
dictionary, then loop through every expense one by one. If the 
category already exists as a key, I add the new amount to the 
existing total. If it does not exist yet, I create it with the 
current amount as the starting value. By the end of the loop 
every category has its correct total — built incrementally, 
one expense at a time. This pattern of building a dictionary 
inside a loop appears constantly in data analysis and I now 
understand exactly why it works.

## What I learned
- A program should always validate input before processing it
- Functions make code easier to read, test and debug
- Separating the menu logic from the action logic keeps 
  everything clean and maintainable
- Wrong indentation in Python causes bugs that can take hours 
  to find — structure matters as much as logic

## What I would improve next time
Add data persistence — right now all expenses are lost when 
the program exits. The next step is saving expenses to a CSV 
file so data survives between sessions. This will be covered 
in Day 05 when I study file handling.

## How to run
python3 main.py