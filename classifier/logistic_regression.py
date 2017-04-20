import metrics
import numpy as np


def sigmoid(z):
    return 1. / (1. + np.exp(-z))


class LogisticRegression:
    """
    Implements a logistic regression binary classifier.
    """
    def __init__(self):
        self.w = None

    def fit(self, X_train, y_train, lr=0.01, n_epochs=1000):
        """
        Fit a model to the training data.
        :param X_train: Training instances (n_samples x n_features)
        :param y_train: Training targets (n_samples)
        :param lr: Learning rate -- the gradient descent step
        :param n_epochs: Number of epochs
        """
        self.w = np.zeros((X_train.shape[1],))

        for i_epoch in range(n_epochs):
            print("Epoch {:d}/{:d}".format(i_epoch + 1, n_epochs))
            dLoss_dw = X_train.T.dot(sigmoid(X_train.dot(self.w)) - y_train)
            self.w -= lr * dLoss_dw

    def decision_function(self, X):
        """
        Returns the value of the decision function.
        In this classifier this is equal to the probability of the positive class.
        :param X: Instances to make a prediction for (n_samples x n_features)
        :return: Value of the decision function (n_samples)
        """
        return sigmoid(X.dot(self.w))

    def predict(self, X):
        """
        Predicts labels for the given instances.
        :param X: Instances to make a prediction for (n_samples x n_features)
        :return: Predicted labels (n_samples)
        """
        z = self.decision_function(X)
        return (z > 0.5).astype(float)

    def score(self, X_test, y_test):
        """
        Makes and evaluates a prediction. Returns the prediction accuracy (higher is better).
        :param X_test: Test instances (n_samples x n_features)
        :param y_test: Test targets (n_samples)
        :return: Prediction accuracy
        """
        y_pred = self.predict(X_test)
        return metrics.accuracy_score(y_test, y_pred)
