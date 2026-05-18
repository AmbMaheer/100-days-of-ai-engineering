# Day 01 — Currency Converter

## What I built
A command line currency converter that converts between 
Nigerian Naira, US Dollar and Euro using fixed exchange rates.

## What I practised
- Variables and data types
- User input and type conversion
- Conditionals (if/elif/else)
- While loops for input validation
- Try/except for error handling

## Key concept I struggled with and conquered
**Input validation loop using while True.**

This pattern keeps the program running and asking for 
correct input instead of crashing when a user types 
something wrong. It took me hours to figure this out.

The pattern looks like this:

while True:
    try:
        value = float(input("Enter amount: "))
        if value <= 0:
            print("Must be greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input. Enter a number.")

The three parts that make it work:
- while True — keeps looping forever until we say stop
- continue — goes back to the top of the loop when input is wrong
- break — exits the loop only when input is valid

In professional terms this is called defensive programming
— writing code that expects users to make mistakes and 
handles them gracefully instead of crashing. Programs 
that never crash on bad input are called robust.

## What I learned
A program should never crash because of user input.
Always validate before using. The while True + break 
pattern is the standard Python way to enforce this.

## What I would improve next time
Connect to a live exchange rate API instead of fixed rates.

## How to run
python3 main.py