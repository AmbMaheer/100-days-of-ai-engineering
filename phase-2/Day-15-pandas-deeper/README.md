# Day 15 — Period-over-Period Growth Engine

## What I built

A command-line financial intelligence engine for Elite Data Sim that 
calculates month-over-month and quarter-over-quarter growth rates 
across multiple data packages. The engine handles the first-period 
NaN edge case correctly, calculates both raw differences and 
percentage changes, and — critically — includes a structural guard 
that detects when a resampled period (like a quarter) is incomplete 
and withholds the growth metric instead of reporting a misleading 
number.

## What I practised

* Shifting data across an index using `.shift()` to align each 
  period against the one before it
* Calculating fractional growth using `.pct_change()` and converting 
  it to business percentages
* Isolating timelines from a MultiIndex using `.get_level_values()`
* Distinguishing Pandas frequency strings (`'ME'` for resampling 
  timestamps vs `'M'` for building Period boxes)
* Writing a guard clause that compares the data's actual last 
  recorded date against a period's theoretical boundary before 
  trusting any calculation built on that period

## Key concepts I struggled with and conquered

**1. The Box vs. The Pinpoint (`'M'` vs `'ME'`)**
My script crashed with `ValueError: Invalid frequency: ME` when I 
tried `.to_period('ME')`. I had used `'ME'` successfully inside 
`.resample()` to avoid a deprecation warning, but the two commands 
build different things in memory. `.resample('ME')` drops a specific 
Timestamp — a pinpoint — on the exact last day of the month. 
`.to_period('M')` creates a Period — a logical box holding the entire 
month. A box has no single "end," so asking for a "Month-End Box" 
made no sense. `'ME'` is for resampling timestamps; `'M'` is for 
building period boxes.

**2. The MultiIndex Tuple Trap**
Running `.max()` on a grouped index returned a Python tuple — 
`('60GB', Timestamp('2026-04-30'))` — not a single date object, 
because the data was grouped by product first. Tuples are invisible 
to Pandas date operations. The fix was 
`monthly_revenue.index.get_level_values(1).max()`, which ignores the 
product label (Level 0) and extracts only the timeline (Level 1).

**3. A correct calculation is not the same as a true conclusion**
The quarterly report initially showed every single product dropping 
87-93% in the same quarter. The code had no bug — every line executed 
correctly. The actual problem was that Q2 only contained 7 days of 
data out of roughly 90 (the simulation stops at day 97, mid-April), 
so Pandas was comparing a full Q1 against a nearly empty Q2 bucket 
and reporting the resulting ratio as if it were a real collapse. 
The giveaway wasn't the size of the drop — a real shock can hit one 
product hard — it was that three independently-priced, unrelated 
products all dropped by similar magnitude on the exact same date. 
That kind of uniform synchronized failure across unconnected 
categories is the fingerprint of a measurement artifact, not a 
market event. I fixed this by adding a guard that compares 
`df.index.max()` (the last real date in the data) against each 
period's end date, and withholds the growth percentage entirely if 
the period is still incomplete, printing an explicit "INCOMPLETE" 
status instead.

## What I learned

* `np.random.randint(low, high)` is inclusive of the lower bound but 
  exclusive of the upper bound — `randint(1, 6)` never generates 6
* Vectorised Pandas operations push computation down to C-arrays, 
  running column-wide instantly instead of looping row by row
* `groupby('product')` must run before `.shift()` for the same 
  reason it must run before `.rolling()` — without it, the engine 
  shifts one product's revenue directly into another product's row, 
  corrupting the column
* Pandas is a blind calculator — it will compute a percentage change 
  on a 92%-empty bucket exactly as confidently as it computes one on 
  a complete bucket, with no warning that the inputs were unfair

## What I would improve next time

The quarterly guard checks whether the latest quarter is complete 
before reporting growth, but the monthly report still has the exact 
same unguarded problem — April only has 7 days of data out of ~30, 
and the monthly percentage changes for April (-80.95%, -63.77%, 
-56.86%) are exactly as misleading as the original broken quarterly 
numbers were, for the identical reason. The next version needs the 
same incomplete-period guard applied at the monthly level, not just 
the quarterly level — fixing one resampling frequency and leaving 
the other unguarded means the underlying bug is only half-solved.

## How to run

python3 main.py