from ARmodels.splitdata import y_train
from ARmodels.library import mean_absolute_error

# Calculating baseline Mean Absolute Error (MAE) for (y_train) in time series
y_train_mean = y_train.mean()
y_pred_baseline = [y_train_mean] * len(y_train)
mae_baseline = mean_absolute_error(y_train, y_pred_baseline)

# Displaying Mean P2 Reading & Baseline MAE for comparison.
print("Mean P2 Reading:", round(y_train_mean, 2))
print("Baseline MAE:", round(mae_baseline, 2))