# Day 16 — Scikit-learn: My First Real Model

## What I built

A revenue forecasting model for Elite Data Sim built with scikit-learn 
instead of raw NumPy. It trains a LinearRegression model on the first 
83 days of data, predicts the held-back final 14 days it never saw 
during training, and scores its own accuracy using mean_absolute_error 
— then compares that honest test-set error against the Day 12 
residual std that was computed by fitting on the entire dataset at once.

## What I practised

* Importing and using scikit-learn's estimator interface 
  (LinearRegression, mean_absolute_error, train_test_split)
* Reshaping a 1D feature array into the 2D shape scikit-learn requires
* Splitting time-ordered data with shuffle=False instead of the 
  default random shuffle
* Training a model only on a training set, then predicting on data 
  it has never seen, to get an honest measure of accuracy
* Comparing a proper test-set error against a same-data residual std 
  to judge whether the comparison itself is fair

## Key concepts I struggled with and conquered

**1. shuffle=False vs shuffle=True — fitting a gap vs predicting the future**
My first run used shuffle=True and produced predictions that looked 
more realistic — jagged, varied — and I initially judged that as 
"more accurate" because it resembled real sales data. The actual 
mean_absolute_error told a different story: shuffle=True scored 
worse (7,429.76) than shuffle=False (6,681.72), despite looking more 
convincing. The reason is that shuffling lets the model train on days 
scattered across the entire 97-day range, including days chronologically 
after the ones being "predicted." That isn't forecasting — it's filling 
in a gap in the middle of data the model has already mostly seen. 
shuffle=False forces the model to train only on the past (days 1-83) 
and predict only the future relative to that training, which is the 
only honest simulation of a real forecasting situation.

**2. A crash with a clear lesson: formatting an array like a single number**
print(f"{y_pred:,.2f}") threw TypeError: unsupported format string 
passed to numpy.ndarray.__format__ because y_pred is an array of 14 
values, not one number — Python's format spec only knows how to format 
a single value. Any time this exact error appears again, the fix is 
to format each element individually (a list comprehension or np.round) 
rather than applying the spec to the whole array directly.

**3. Test error vs residual std — direction matters**
The test-set MAE (6,681.72) came out higher than the Day 12 residual 
std computed on the full dataset (6,345.44). That direction is 
expected and healthy, not a warning sign — the residual std was 
computed by a model that had already seen and fit every point, while 
the test MAE measures performance on 14 days the model genuinely 
never touched during training. A test error somewhat higher than the 
full-data residual means the model generalises reasonably; a test 
error dramatically higher would be the actual red flag.

## What I learned

* Every scikit-learn model follows the same fit() → predict() pattern, 
  regardless of which algorithm sits underneath it
* X (features) must be 2D even with a single column; y (target) stays 1D
* train_test_split's shuffle parameter must be False for any time-ordered 
  data — shuffling destroys the past/future structure the test is 
  supposed to simulate
* A prediction that visually resembles real data is not the same as 
  a prediction that is numerically accurate — mean_absolute_error is 
  the actual judge, not visual resemblance

## What I would improve next time

Today's model only predicted 14 days that were already inside the 
recorded dataset — the model never had to forecast genuinely unseen 
future dates. Next step is predicting forward into real unseen time, 
such as the next 90 days beyond day 97, and visualising the actual 
data, the fitted line, and the forecast together using matplotlib, 
rather than reading raw numbers off the terminal.

## How to run

python3 main.py