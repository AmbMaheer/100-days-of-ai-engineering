# Day 05 — Program Memory

## What I built
A major system upgrade to the command-line applications built
on Day 02 (Personal Expense Tracker) and Day 04 (Financial
Calculator). I implemented persistent data storage using CSV
files and event logging. Previously, all data was lost in RAM
the moment the program exited. Now, transactions are permanently
saved and retrieved across sessions, and financial calculations
are securely recorded in a permanent, growing log file.

## What I practised
-File handling in Python (open(), read, write, and append modes)
-Using the built-in csv module to safely format and parse data
-Implementing event logging to maintain an audit trail of calculations
-Refactoring existing code to support multi-user data filtering
-Navigating and interpreting official Python documentation

## Key concepts I struggled with and conquered
**1. Reading official Python documentation on python.org**
Previously, when I got stuck on a concept, my first instinct
was to search for a YouTube tutorial or ask an AI for a direct
explanation. Today, I forced myself to rely on the official
Python documentation to understand file handling and modules.
While it was intimidating at first, I learned how to properly
navigate technical docs. I realized that while videos are good
for quick fixes, official documentation offers the most detailed,
authoritative explanations and is ultimately the best way to
deeply master a language.

**2. Refactoring logic for multi-user support**
Changing the Day 02 logic to require a username completely
shifted how the program handles data. I had to figure out how
to avoid "The Overwrite Bug"—if the program only loaded one
user's data from the CSV, saving it back would accidentally
delete everyone else's data. I learned that the system must
load all records into memory in the background, filter what
is displayed based on the active username, and then safely
save the entire dataset back to the CSV.

## What I learned
-The difference between file modes is critical: "w" (write)
is destructive and wipes the file, while "a" (append) is
essential for continuous logging without data loss.

-Using the built-in csv module is vastly superior to manually
splitting strings with commas, as it automatically protects
against edge cases (like users typing commas in their input).

-Adding new features (like user profiles) often requires
completely rethinking the underlying data structure, such as
adding a new column to an existing CSV format.

## What I would improve next time
I would implement a more robust authentication system, perhaps
requiring a simple PIN or password alongside the username.
Additionally, I would like to add a feature that allows users
to view or search their calculation logs directly from the
calculator's main menu, rather than having to open the .log
text file manually.


## How to run
python3 main.py