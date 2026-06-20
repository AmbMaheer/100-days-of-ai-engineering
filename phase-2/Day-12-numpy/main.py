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


# 1. Fit a trend line through the revenue data
#    x = day numbers, y = revenue
#    slope, intercept = np.polyfit(days, revenue, 1)
#    Print the slope — what does a positive slope tell you 
#    about the business in plain English?
x = sales_data[:, 0]
y = sales_data[:, 2]
slope, intercept = np.polyfit(x, y, 1)
print(f"Slope: {slope}, Intercept: {intercept}")
#The positive slope indicates that the business's revenue is generally increasing over time, suggesting growth in sales or customer base.

# 2. Predict the next 7 days
#    Using y = mx + b, predict revenue for days 98-104
#    Print each predicted day and its forecasted revenue
predicted_days = np.arange(98, 105)
predicted_revenue = slope * predicted_days + intercept
for day, revenue in zip(predicted_days, predicted_revenue):
    print(f"Predicted Revenue for Day {day}: {revenue:.2f}")

# 3. Predict next 30 days total
#    Sum the predictions for days 98-127
#    Compare this to the actual total revenue of the last 30 
#    recorded days — is the forecast higher, lower, or similar?
actual_total_last_30_days = np.sum(sales_data[-30:, 2])
predicted_total_next_30_days = np.sum(slope * np.arange(98, 128) + intercept)
print(f"Actual Total Revenue for Last 30 Days: {actual_total_last_30_days}")
print(f"Predicted Total Revenue for Next 30 Days: {predicted_total_next_30_days:.2f}")
if predicted_total_next_30_days > actual_total_last_30_days:
    print("The forecast is higher than the actual total revenue of the last 30 days.")
elif predicted_total_next_30_days < actual_total_last_30_days:
    print("The forecast is lower than the actual total revenue of the last 30 days.")
else:
    print("The forecast is similar to the actual total revenue of the last 30 days.")

# 4. Confidence check — residuals
#    For each historical day, calculate the difference between 
#    the ACTUAL revenue and what the trend line PREDICTED for 
#    that same day (this is called a "residual")
#    Calculate the standard deviation of these residuals
#    This tells you how much to trust the forecast —
#    a high residual std means the trend line is a rough guide,
#    not a precise prediction
predicted_revenue_historical = slope * x + intercept
residuals = y - predicted_revenue_historical
residual_std = np.std(residuals)
print(f"Standard Deviation of Residuals: {residual_std:.2f}")


# 5. Build a simple forecast range
#    Predicted next-day revenue ± 1 standard deviation of residuals
#    Print this as: "Tomorrow's revenue is likely between ₦X and ₦Y"
tomorrow_revenue = slope * 105 + intercept
print(f"Tomorrow's revenue is likely between ₦{tomorrow_revenue - residual_std:.2f} and ₦{tomorrow_revenue + residual_std:.2f}")