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
        if np.random.rand() > 0.3:  # not every product sells every day
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


print(df.groupby('product')['revenue'].sum())
# The 120GB product earns the most overall, likely due to its higher price point and
# potentially higher profit margin compared to the 30GB and 60GB products.


print(df.groupby('product')['units'].mean().round(1))
# The average daily units sold per product are approximately:
# - 120GB    3.2
# - 60GB     2.8
# - 30GB     3.4


df['profit'] = df['revenue'] - df['cost']
profit_by_product = df.groupby('product')['profit'].sum()
print(profit_by_product)
# The product with the best profit is the 120GB product, which also has the best
# revenue. This is business-relevant because it indicates that the 120GB product
# is not only generating the most sales but also contributing the most to the 
# company's bottom line, making it a key focus for marketing and inventory decisions.


weekly_revenue_per_product = df.groupby('product')['revenue'].resample('W').sum()
print(weekly_revenue_per_product)
# The two levels of the index are 'product' and 'date' (resampled to
# weekly frequency). The 'product' level indicates which product the 
# revenue corresponds to, while the 'date' level indicates the week for which the revenue is aggregated.


average_revenue_per_product = df.groupby('product')['revenue'].rolling(7).mean()
print(average_revenue_per_product)
# The window grabs whatever 7 rows are physically adjacent, full stop, with no awareness 
# of what's in them. And groupby('product') runs first, splitting the table into separate 
# mini-tables — one all-120GB, one all-30GB, one all-60GB — so that by the time .rolling(7) runs, 
# the "7 adjacent rows" it's grabbing are guaranteed to be 7 rows of the same product, not a mix

pivot_table = pd.pivot_table(df, index=df.index.to_period('W'),
columns='product', values='revenue',
aggfunc='sum')
print(pivot_table)