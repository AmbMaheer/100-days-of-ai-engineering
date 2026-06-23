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


np.random.seed(42)
dates = pd.date_range(start='2026-01-01', periods=97, freq='D')

products = ['30GB', '60GB', '120GB']
rows = []
for date in dates:
    for product in products:
        if np.random.rand() > 0.3:  
            units = np.random.randint(1, 6)
            price = {'30GB': 2000, '60GB': 3500, '120GB': 6000}[product]
            cost  = {'30GB': 1200, '60GB': 2100, '120GB': 3800}[product]
            rows.append({
                'date': date,
                'product': product,
                'units': units,
                'revenue': units * price,
                'cost': units * cost
            })

df = pd.DataFrame(rows)
df.set_index('date', inplace=True)



monthly_revenue = df.groupby('product')['revenue'].resample('ME').sum()

monthly_revenue_shifted = monthly_revenue.groupby('product').shift(1)
monthly_revenue_change = monthly_revenue - monthly_revenue_shifted
print(monthly_revenue_change)
#Groupby() takes the data and splits it into groups based on the product. 
# This is necessary because we want to calculate the month-over-month change
# for each product separately. If we didn't group by product, the shift would 
# mix up the revenue values from different products, leading to incorrect calculations. 
# By grouping first, we ensure that the shift operation only affects the revenue values 
# within each product group, allowing us to accurately compute the change from one month 
# to the next for each individual product.


monthly_revenue_pct_change = monthly_revenue.groupby('product').pct_change()
monthly_revenue_change_percentage = (monthly_revenue_change / monthly_revenue_shifted) * 100
print(monthly_revenue_change_percentage)



quarterly_revenue = df.groupby('product')['revenue'].resample('QE').sum()
quarterly_revenue_pct_change = quarterly_revenue.groupby('product').pct_change()
last_recorded_date = df.index.max()
print("--- Quarterly Growth Report ---")
for product in products:
    q_series = quarterly_revenue_pct_change.loc[product]
    latest_quarter_end = q_series.index.max()
    if last_recorded_date < latest_quarter_end:
        print(f"{product}: Q2 ({latest_quarter_end.date()}) is INCOMPLETE (Data ends {last_recorded_date.date()}). Growth metric withheld.")
    else:
        growth = q_series.loc[latest_quarter_end] * 100
        print(f"{product}: Q2 ({latest_quarter_end.date()}) Growth = {growth:.2f}%")


print(monthly_revenue_pct_change.loc['30GB'])
# NaN appears in the first row because there is no previous month to compare to.
# Pandas cannot calculate a percentage change from the previous month for the very 
# first month in the data because there is no prior data point to reference. 
# The percentage change is defined as the difference between the current value 
# and the previous value, divided by the previous value. Since there is no previous 
# value for the first month, it is mathematically impossible to compute a percentage 
# change, resulting in a NaN (Not a Number) value. This behavior is consistent with how 
# pandas handles missing or undefined values, ensuring that the output accurately reflects 
# the lack of available data for that calculation.


latest_timestamp = monthly_revenue.index.get_level_values(1).max()
if pd.notna(latest_timestamp):
    current_period = latest_timestamp.to_period('M')
    previous_period = current_period - 1 
    for product in products:
        product_series = monthly_revenue.loc[product]
        product_series.index = product_series.index.to_period('M')
        current_month_revenue = product_series.get(current_period, 0)
        previous_month_revenue = product_series.get(previous_period, 0)
        if previous_month_revenue == 0:
            growth_rate = "N/A (no sales last month)"
        else:
            growth_rate = f"{((current_month_revenue - previous_month_revenue) / previous_month_revenue) * 100:.2f}%"
        print(f"{product}: Revenue ₦{current_month_revenue} this month, {growth_rate} vs last month")