from ARmodels.library import AutoReg
from ARmodels.splitdata import y_train
from ARmodels.library import mean_absolute_error

# Fitting AutoRegressive Model (lags=26) to training data.
model = AutoReg(y_train, lags=26).fit()

# Check how many null predictions are there by counting the number of null values 
model.predict().isnull().sum()

# Drop null predictions
model.predict().dropna()

# Evaluating training Mean Absolute Error (MAE) for model performance.
y_pred = model.predict().dropna()
training_mae = mean_absolute_error(y_train.iloc[26:], y_pred)
print("Training MAE:", training_mae)

# Use y_train and y_pred to calculate the residuals for your model
y_train_resid = model.resid
y_train_resid.head()