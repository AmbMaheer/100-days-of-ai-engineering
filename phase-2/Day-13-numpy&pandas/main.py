import pandas as pd
import numpy as np

sales_data = np.array([
    [1,  3, 10500, 6300],  [2,  1, 6000, 3800],   [3,  2, 7000, 4200],
    [4,  0, 0, 0],         [5,  4, 12000, 7200],   [6,  2, 7000, 4200],
    [7,  1, 3500, 2100],   [8,  3, 10500, 6300],   [9,  2, 7000, 4200],
    [10, 0, 0, 0],         [11, 5, 16000, 9600],   [12, 2, 7000, 4200],
    [13, 1, 3500, 2100],   [14, 3, 9000, 5400],    [15, 4, 14000, 8400],
    [16, 0, 0, 0],         [17, 2, 7000, 4200],    [18, 3, 10500, 6300],
    [19, 1, 3500, 2100],   [20, 5, 17500, 10500],  [21, 2, 7000, 4200],
    [22, 0, 0, 0],         [23, 3, 10500, 6300],   [24, 4, 14000, 8400],
    [25, 1, 3500, 2100],   [26, 2, 7000, 4200],    [27, 3, 10500, 6300],
    [28, 0, 0, 0],         [29, 5, 17500, 10500],  [30, 3, 10500, 6300],
    [31, 2, 7000, 4200],   [32, 4, 14000, 8400],   [33, 1, 3500, 2100],
    [34, 3, 10500, 6300],  [35, 0, 0, 0],          [36, 5, 17500, 10500],
    [37, 2, 7000, 4200],   [38, 3, 10500, 6300],   [39, 4, 14000, 8400],
    [40, 1, 3500, 2100],   [41, 0, 0, 0],          [42, 6, 21000, 12600],
    [43, 3, 10500, 6300],  [44, 2, 7000, 4200],    [45, 4, 14000, 8400],
    [46, 1, 3500, 2100],   [47, 5, 17500, 10500],  [48, 0, 0, 0],
    [49, 3, 10500, 6300],  [50, 4, 14000, 8400],   [51, 2, 7000, 4200],
    [52, 6, 21000, 12600], [53, 1, 3500, 2100],    [54, 0, 0, 0],
    [55, 5, 17500, 10500], [56, 3, 10500, 6300],   [57, 4, 14000, 8400],
    [58, 2, 7000, 4200],   [59, 6, 21000, 12600],  [60, 0, 0, 0],
    [61, 3, 10500, 6300],  [62, 5, 17500, 10500],  [63, 2, 7000, 4200],
    [64, 4, 14000, 8400],  [65, 1, 3500, 2100],    [66, 0, 0, 0],
    [67, 6, 21000, 12600], [68, 3, 10500, 6300],   [69, 4, 14000, 8400],
    [70, 2, 7000, 4200],   [71, 5, 17500, 10500],  [72, 0, 0, 0],
    [73, 4, 14000, 8400],  [74, 6, 21000, 12600],  [75, 2, 7000, 4200],
    [76, 3, 10500, 6300],  [77, 5, 17500, 10500],  [78, 0, 0, 0],
    [79, 4, 14000, 8400],  [80, 6, 21000, 12600],  [81, 3, 10500, 6300],
    [82, 2, 7000, 4200],   [83, 5, 17500, 10500],  [84, 0, 0, 0],
    [85, 4, 14000, 8400],  [86, 6, 21000, 12600],  [87, 3, 10500, 6300],
    [88, 5, 17500, 10500], [89, 2, 7000, 4200],    [90, 7, 24500, 14700],
    [91, 4, 14000, 8400], [92, 3, 10500, 6300], [93, 5, 17500, 10500],
    [94, 2, 7000, 4200],  [95, 6, 21000, 12600], [96, 0, 0, 0],
    [97, 7, 24500, 14700]
])

# Build a DataFrame with real dates starting from a chosen date
# Use the same 97 days of data from Day 12, but assign real
# calendar dates instead of just day numbers — start anywhere,
# e.g. 2026-01-01
dates = pd.date_range(start='2026-01-01', periods=sales_data.shape[0], freq='D')


# 1. Create the DataFrame
#    Columns: date, units, revenue, cost
#    Set 'date' as the DataFrame's index using pd.to_datetime() 
#    and .set_index()
df = pd.DataFrame(sales_data, columns=['day', 'units', 'revenue', 'cost'])
df['date'] = dates
df.set_index('date', inplace=True)


# 2. Weekly resampling
#    df['revenue'].resample('W').sum()
#    Compare this to your Day 11 manual reshape(12,7).sum(axis=1)
#    Do the totals match? They should — explain in a comment 
#    why resample() is the better tool going forward
weekly_revenue = df['revenue'].resample('W').sum()
# The totals match because both methods aggregate the revenue data over the same time period (weekly). However, resample() is a better tool going forward because it is more flexible and can handle irregular time series data, allows for different aggregation functions, and integrates seamlessly with pandas' time series functionality.

# 3. Monthly resampling
#    df['revenue'].resample('M').sum()
#    df['revenue'].resample('M').mean()
#    Which month had the highest total revenue?
monthly_revenue = df['revenue'].resample('ME').sum()
monthly_mean_revenue = df['revenue'].resample('ME').mean()
highest_revenue_month = monthly_revenue.idxmax()
print(f"Month with highest total revenue: {highest_revenue_month.strftime('%B %Y')} with revenue of {monthly_revenue.max()}")

# 4. Rolling 7-day average — the pandas way
#    df['revenue'].rolling(window=7).mean()
#    Compare the first 5 non-NaN values to your Day 11 
#    np.convolve() output — do they match?
#    Notice: rolling() produces NaN for the first 6 days 
#    instead of just shortening the array. Why is that 
#    actually more honest than what convolve did?
rolling_avg_revenue = df['revenue'].rolling(window=7).mean()
# convolve() shrinks the array from 97 to 91. If you then lined that array 
# up against your original 97 dates, Jan 1 would end up paired with the 
# average that actually belongs to Jan 7 — every date shifts 6 days out 
# of alignment, silently, because NumPy arrays carry no date labels to 
# catch the mismatch. rolling() avoids this entirely by always returning 
# 97 values, marking the first 6 as NaN instead of dropping them.


# 5. Rolling with a minimum period
#    df['revenue'].rolling(window=7, min_periods=1).mean()
#    This fills in early days with a "partial" average 
#    instead of NaN. When would you want this vs. not?
#    You would want this when you want to avoid NaN values in the early days and still have some form of average, even if it's based on fewer data points.
rolling_avg_revenue_min_periods = df['revenue'].rolling(window=7, min_periods=1).mean()

# 6. Combine rolling average with the original data
#    Add the rolling average as a NEW COLUMN in your DataFrame
#    df['revenue_7d_avg'] = df['revenue'].rolling(7).mean()
#    Print the last 10 rows showing both columns side by side
df['revenue_7d_avg'] = df['revenue'].rolling(7).mean()
print(df[['revenue', 'revenue_7d_avg']].tail(10))