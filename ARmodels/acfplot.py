from library import plt, plot_acf
from DataFrame import y
# Plotting the autocorrelation function (ACF) of time series data 'y' 
# to observe correlation between lagged observations
fig, ax = plt.subplots(figsize=(15, 6))
plot_acf(y, ax=ax)
plt.xlabel("Lag [hours]")
plt.ylabel("Correlation Coefficient");