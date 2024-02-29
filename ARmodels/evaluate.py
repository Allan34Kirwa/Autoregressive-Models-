from ARmodels.splitdata import y_test,y_train
from ARmodels.iterate import model
from ARmodels.library import mean_absolute_error, pd, px, AutoReg

# Your code here


# Displaying the first few rows of the test dataset.
y_test.head()

# Displaying the last few observations in the test dataset.
y_test.tail()

# Earliest timestamp in the test data index.
y_test.index.min()

# Maximum index value in the test set (y_test).
y_test.index.max()

# Evaluating test Mean Absolute Error (MAE) for model performance.
y_pred_test = model.predict(y_test.index.min(), y_test.index.max())
test_mae = mean_absolute_error(y_test, y_pred_test)
print("Test MAE:", test_mae)

# Create a DataFrame from a dictionary using pandas.
df_pred_test = pd.DataFrame(
    {"y_test": y_test, "y_pred": y_pred_test}, index=y_test.index
)

# Previewing the first few rows of the predicted test dataframe.
df_pred_test.head()

# Create a line plot in plotly express.
fig = px.line(df_pred_test, labels={"value": "P2"})
fig.show()

# Perform walk-forward validation for your model for the entire test set y_test
# %%capture

y_pred_wfv = pd.Series()
history = y_train.copy()
for i in range(len(y_test)):
    model = AutoReg(history, lags=26).fit()
    next_pred = model.forecast()
    y_pred_wfv = y_pred_wfv.append(next_pred)
    history = history.append(y_test[next_pred.index])
    pass

# Comparing lengths of test and walk-forward validation predictions.
len(y_test) == len(y_pred_wfv)

# Calculate the test mean absolute error for your model.
test_mae = mean_absolute_error(y_test, y_pred_wfv)
print("Test MAE (walk forward validation):", round(test_mae, 2))