# Day 12 — Revenue Forecaster (NumPy Foundations Capstone)

## What I built
A command line revenue forecasting engine for Elite Data Sim 
using pure NumPy. It fits a linear trend line through 97 days 
of historical revenue, forecasts the next 7 and 30 days, 
measures forecast reliability using residual analysis, and 
produces a confidence range for next-day revenue.

## What I practised
- np.polyfit() to fit a straight line (y = mx + b) through 
  historical data
- Using the fitted slope and intercept to predict future values
- Comparing forecasted totals against actual historical totals
- Calculating residuals (actual minus predicted) to measure 
  how much a model misses by
- np.std() applied to residuals as a confidence measure
- Using the terminal directly to navigate and activate virtual 
  environments instead of relying on VS Code's file explorer

## Key concepts I struggled with and conquered

**1. Linear regression with raw NumPy**
np.polyfit(x, y, 1) fits a straight line by finding the slope 
and intercept that minimise the squared error between the 
line and the actual data points. Once fitted, any future day 
number can be plugged into y = mx + b to get a forecast. This 
is the same underlying math that scikit-learn's LinearRegression 
will do later, just without the wrapper.

**2. Residuals as an honesty check on the model**
A model can produce a forecast and look confident while 
actually being unreliable. Calculating the residual (actual 
revenue minus what the line predicted, for every historical 
day) and taking its standard deviation revealed that day-to-day 
noise in this business (≈₦6,342) is nearly three times larger 
than the entire 30-day trend contribution from the slope 
(≈₦2,200). A forecast range that wide is barely more useful 
than a guess — the code is correct, but the model is too 
simple for this dataset.

## What I learned
- A positive slope means revenue trends upward over time, but 
  the SIZE of the slope relative to the noise in the data 
  determines whether that trend is actually meaningful
- np.polyfit() returns coefficients in order from highest 
  degree to lowest — for a straight line, that is [slope, intercept]
- Residual standard deviation is a direct measure of how much 
  to trust a forecast — small residuals mean the line fits 
  well, large residuals mean real-world noise dominates
- A straight line cannot model revenue that is choppy and 
  irregular day to day; this business's pattern looks more 
  cyclical/lumpy than linear, which a simple trend line cannot 
  capture

## What I would improve next time
Explore matplotlib to visualise the actual revenue, the fitted 
trend line, and the forecast range together on one chart. 
Seeing the spread of residuals visually would make the model's 
limitations immediately obvious rather than something inferred 
purely from a standard deviation number.

## How to run
python3 main.py