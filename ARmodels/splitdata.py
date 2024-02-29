from ARmodels.DataFrame import y

# Setting cutoff point for 95% of the data.
cutoff_test = int(len(y) * 0.95)

# Splitting time series data into training and testing subsets.
y_train = y.iloc[:cutoff_test]    # my training data
y_test = y.iloc[cutoff_test:]   # my test data

# Confirming the integrity of the time series split.
y_train = y.iloc[:cutoff_test] # My training data

