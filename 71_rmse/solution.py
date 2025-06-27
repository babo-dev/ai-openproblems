import numpy as np


def rmse(y_true, y_pred):
    assert len(y_true) == len(y_pred), "Input arrays must have the same length"
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    squared_errors = (y_true - y_pred) ** 2
    mean_squared_error = np.mean(squared_errors)
    rmse_res = np.sqrt(mean_squared_error)
    return round(rmse_res, 3)
