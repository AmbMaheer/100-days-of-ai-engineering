from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np


# Use the 97-day sales_data from Day 12
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

X = sales_data[:, 0].reshape(-1, 1)  # Day numbers as features
y = sales_data[:, 2]  # Revenue as target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=14, shuffle=False)
#shuffle=False ensures that the last 14 days are held back for testing, preserving the time series order.
#shuffle=True would randomly select days for training and testing, which is like is filling the gaps istead of
#preicting the future based on the past. This would not be a valid test of the model's predictive power.

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred = linear_model.predict(X_test)
print("Predictions for the last 14 days:", [f"{v:,.2f}" for v in y_pred])
result = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (Test Set): {result:<10.2f} Naira")

data_std = np.std(y - linear_model.predict(X))
print(f"Residual Std (All Data): {data_std:,.2f} Naira")
#  The test error is higher than the residual std, and it's expected because the model is trained 
# on past data and tested on future data, which may have different patterns or trends. The residual 
# std represents the variability of the model's predictions on the training data, while the test 
# error reflects how well the model generalizes to unseen data.