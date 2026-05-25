# Day 06 — Python Libraries and Virtual Environments

## What I built
A script that installs and interrogates three core Python 
libraries — requests, pandas and python-dotenv — printing 
the name, version and purpose of each. Simple in output 
but foundational in what it establishes for every project 
from this point forward.

## What I practised
- Creating and activating a Python virtual environment
- Installing packages from PyPI using pip
- Importing third party libraries
- Reading library documentation
- Generating a requirements.txt file

## Key concepts I struggled with and conquered

**1. Why virtual environments exist**
Every project needs its own isolated environment because 
different projects may depend on different versions of the 
same library. Installing everything globally causes version 
conflicts that break projects silently. One project, one 
virtual environment — this is non-negotiable in professional 
Python development.

**2. __version__ vs importlib.metadata**
My first instinct was to use the __version__ attribute 
directly on each library. This works for requests and pandas 
but fails for python-dotenv because its developers did not 
expose that attribute. The correct universal solution is 
importlib.metadata — a built-in Python module that reads 
version information from the package metadata itself, 
regardless of how the library was written. This is the 
standard approach used in production code.

## What I learned
- pip downloads libraries from PyPI — the central registry 
  where Python developers publish their work
- Virtual environments protect projects from each other
- Not all libraries expose __version__ — importlib.metadata 
  is the reliable universal alternative
- requirements.txt captures the exact library versions a 
  project needs so any machine can reproduce the environment

## What I would improve next time
Build a script that reads requirements.txt automatically, 
checks which libraries are outdated, and prints upgrade 
recommendations — a basic version of what pip-review does.

## How to run
source env/bin/activate
python3 main.py