# Day 10 — Financial Data Engine (NumPy Foundations)

## What I built
A command line financial analysis engine for Elite Data Sim 
using pure NumPy. It calculates total and average revenue/profit, 
daily profit margins, active vs zero-sales days, best and worst 
performing days, weekly revenue totals, and period-over-period 
growth — all using vectorised array operations instead of loops.

## What I practised
- Importing and using NumPy arrays
- Extracting columns from a 2D array into named variables
- Vectorised arithmetic across entire arrays (broadcasting)
- Boolean indexing and masking
- np.argmax() and np.argmin() for finding extremes
- Reshaping arrays and understanding shape compatibility
- np.std() for measuring data variability

## Key concepts I struggled with and conquered

**1. Reshaping requires exact divisibility**
Reshaping a 90-day array into weeks of 7 does not work 
directly because 90 is not divisible by 7. NumPy requires 
the total element count to match exactly between the original 
and reshaped array. The fix was slicing to the first 84 days 
(12 complete weeks) using revenue[:84].reshape(12, 7), 
leaving the remaining 6 days as an incomplete final week 
to handle separately if needed.

**2. np.where() evaluates both branches always**
I used np.where(revenue != 0, profit / revenue, 0) to avoid 
dividing by zero, but a RuntimeWarning still appeared. The 
reason is that np.where() calculates BOTH the true and false 
results for every element before selecting which one to keep — 
it does not skip the division, it just discards the bad result 
afterward. The correct fix is np.divide() with a where 
parameter, which prevents the unsafe operation from running 
at all rather than running it and throwing away the result.

## What I learned
- NumPy operations apply to entire arrays at once through 
  broadcasting — no loops needed for simple arithmetic
- A warning is not the same as a wrong answer, but it signals 
  an operation that could fail in different circumstances — 
  it should be fixed properly, not ignored
- Reshaping is a structural operation, not a magic one — the 
  array dimensions must multiply out exactly
- Standard deviation reveals consistency: a high std on daily 
  revenue means the business has unpredictable, lumpy sales 
  rather than steady daily income — useful for knowing how 
  much cash buffer the business needs

## What I would improve next time
Handle the leftover 6 days from the reshape instead of 
discarding them — perhaps as a partial 13th week. Also 
explore using percentiles to identify what counts as an 
unusually good or bad day, rather than just looking at the 
single best and worst.

## How to run
python3 main.py