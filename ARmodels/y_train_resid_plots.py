from ARmodels.library import plt, plot_acf
from ARmodels.iterate import y_train_resid

# Creating a line plot using pandas.
fig, ax = plt.subplots(figsize=(15, 6))
y_train_resid.plot(ylabel="Residual Value", ax=ax);

# Creating a histogram using plotly express.
y_train_resid.hist()
plt.xlabel("Residual Value")
plt.ylabel("Frequency")
plt.title("AR(26), Distribution of Residuals");

# Creating an ACF plot for y_train_resid
fig, ax = plt.subplots(figsize=(15, 6))
plot_acf(y_train_resid, ax=ax);