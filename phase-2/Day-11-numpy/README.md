# Day 11 — Trend Engine (NumPy Foundations)

## What I built
A command line financial trend analysis engine for Elite Data 
Sim using pure NumPy. It calculates a 7-day moving average of 
revenue, cumulative revenue over time, day-over-day change, 
percentile-based performance categorisation, and merges new 
weekly data into the existing dataset — all using vectorised 
array operations instead of loops.

## What I practised
- Extracting columns from a 2D NumPy array into named variables
- Vectorised arithmetic across entire arrays (broadcasting)
- np.convolve() for calculating a moving average
- np.argmax() and np.argmin() for finding extreme values and 
  their positions
- np.diff() for calculating day-over-day change
- np.cumsum() for running totals
- np.percentile() for statistical thresholds
- np.vstack() for combining arrays vertically

## Key concepts I struggled with and conquered

**1. Reading documentation vs learning by example**
Official documentation is precise but assumes you already 
know the shape of the problem. For functions like np.cumsum() 
and np.vstack(), I found it faster to watch a short video 
showing the function solve a real problem first, then return 
to the documentation to understand the parameters in depth. 
Documentation answers "what does this do" — examples answer 
"why would I use this."

**2. The convolution output length formula**
I initially could not predict how many elements a moving 
average array would have compared to the input. The actual 
relationship is output_length = input_length - window_size + 1. 
With 90 days and a 7-day window, that gives 84 valid positions 
where the window fits completely inside the data. This is not 
just a NumPy detail — it is the same formula used to calculate 
output size when a filter scans across data in convolutional 
neural networks, which I will encounter again in later phases.

## What I learned
- np.convolve() with a window of equal weights (np.ones(7)/7) 
  is mathematically how a moving average is calculated — each 
  point is the mean of the 7 values inside the sliding window
- np.cumsum() returns a running total at every position, while 
  np.sum() collapses the entire array into a single number — 
  they answer completely different questions
- Combining new data into an existing dataset with np.vstack() 
  is straightforward as long as both arrays have the same 
  number of columns

## What I would improve next time
Visualise these results as a graph instead of printed rows of 
numbers. A moving average is meant to reveal a trend, and a 
trend is far easier to see on a line chart than to read from 
a list of numbers. This is a natural next step once matplotlib 
is introduced.

## How to run
python3 main.py