from utils import load_model
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score

def evaluate(model,X_test,y_test):
    preds = model.predict(X_test)

    rmse = root_mean_squared_error(preds,y_test)
    mae = mean_absolute_error(preds, y_test)
    r2 = r2_score(preds, y_test)

    return {
        'root mean square error': rmse,
        'mean absoulute error' : mae,
        'r2 score' : r2
    }