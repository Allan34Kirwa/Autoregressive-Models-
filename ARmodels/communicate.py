from ARmodels.iterate import model
from ARmodels.splitdata import y_test
from ARmodels.evaluate import y_pred_wfv
from ARmodels.library import px, pd
# Print out the parameters for your trained model.
print(model.params)

# plot df_pred_test using plotly express.
df_pred_test = pd.DataFrame(
    {"y_test": y_test, "y_pred_wfv": y_pred_wfv}
)
fig = px.line(df_pred_test, labels={"value": "P2"})
fig.show()
