import numpy as np


def accuracy_score(y_test, y_pred):
    """
    Returns the accuracy score.
    :param y_test: True labels (n_samples)
    :param y_pred: Predicted labels (n_samples)
    :return: Accuracy
    """
    return np.sum((y_pred == y_test).astype(float)) / len(y_test)


def mean_absolute_error(y_test, y_pred):
    """
    Calculates the mean absolute error.
    :param y_test: True labels (n_samples)
    :param y_pred: Predicted labels (n_samples)
    :return: Mean absolute error
    """
    return np.mean(np.abs(y_pred - y_test))
