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
])

# 1. 7-day moving average of revenue
#    Calculate this WITHOUT a loop using np.convolve()
revenue = sales_data[:, 2]
moving_avg_7d = np.convolve(revenue, np.ones(7)/7, mode='valid')
print(f"Length of moving_avg_7d: {len(moving_avg_7d)}")  # Should be 84, since the first 6 days don't have a full 7-day window
print(f"7-day Moving Average of Revenue (first 5 values): {moving_avg_7d[:5]}")
#    The output array is shorter than the input array because the 'valid' mode of convolution only computes the average for positions where the full 7-day window fits within the original revenue array.


# 2. Cumulative revenue
#    At any point, how much has the business earned so far?
cumulative_revenue = np.cumsum(revenue)
print(f"Cumulative Revenue at Day 30: {cumulative_revenue[29]}, Day 60: {cumulative_revenue[59]}, Day 90: {cumulative_revenue[89]}")


# 3. Day-over-day change
#    How much did revenue change from one day to the next?
day_over_day_change = np.diff(revenue)
biggest_jump = np.max(day_over_day_change)
biggest_drop = np.min(day_over_day_change)
jump_day = np.argmax(day_over_day_change) + 1
drop_day = np.argmin(day_over_day_change) + 1
print(f"Biggest Jump: {biggest_jump} (Day {jump_day}), Biggest Drop: {biggest_drop} (Day {drop_day})")

# 4. Percentile analysis
#    What revenue amount represents a "good day" vs a "bad day"?
percentiles = np.percentile(revenue, [25, 50, 75])
good_day_threshold = percentiles[2]
bad_day_threshold = percentiles[0]
great_days = np.sum(revenue > good_day_threshold)
slow_days = np.sum((revenue < bad_day_threshold) & (revenue > 0))
print(f"25th Percentile: {percentiles[0]}, 50th Percentile: {percentiles[1]}, 75th Percentile: {percentiles[2]}")
print(f"Great Days: {great_days}, Slow Days: {slow_days}")

# 5. Combine today's data with a new week
#    Pretend you just got 7 more days of sales:
new_week = np.array([
    [91, 4, 14000, 8400], [92, 3, 10500, 6300], [93, 5, 17500, 10500],
    [94, 2, 7000, 4200],  [95, 6, 21000, 12600], [96, 0, 0, 0],
    [97, 7, 24500, 14700]
])
#    Combine it with the original sales_data using np.vstack()
combined_data = np.vstack([sales_data, new_week])
#    Confirm the new array has 97 rows using .shape
print(f"Combined Data Shape: {combined_data.shape}")