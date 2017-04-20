import numpy as np
import metrics


def labels_as_ovr(y, cls):
    """
    Converts a multi-label targets vector to binary "one-vs-rest" targets.
    :param y: Targets (n_samples)
    :param cls: Label to select as the positive class
    :return: Binarised targets (n_samples)
    """
    y_ovr = np.zeros_like(y)
    y_ovr[y == cls] = 1.
    return y_ovr


class MulticlassOVR:
    """
    Implements a wrapper for "one-vs-rest" multi-class classification.
    """
    def __init__(self, classifier):
        """
        :param classifier: An uninitialised binary classifier
        """
        self.classifier = classifier
        self.classes = None
        self.models = {}

    def fit(self, X_train, y_train, **kwargs):
        """
        Fits classifiers for the one-vs-rest prediction.
        The number of classifier fitted is equal to the the number of unique classes among the training targets.
        :param X_train: Training instances (n_samples x n_features)
        :param y_train: Training targets (n_samples)
        :param kwargs: Additional arguments for the "fit" method of the classifier
        """
        self.classes = np.sort(np.unique(y_train))

        for i_cls, cls in enumerate(self.classes):
            print("Fitting model {:d}/{:d}".format(i_cls + 1, len(self.classes)))
            classifier = self.classifier()
            y_ovr = labels_as_ovr(y_train, cls)
            classifier.fit(X_train, y_ovr, **kwargs)
            self.models[cls] = classifier

    def decision_function(self, X):
        """
        Returns the decision function for the prediction on X.
        A separate value is reported for each class.
        :param X: Instances (n_samples x n_features)
        :return: Decision function (n_samples x n_classes)
        """
        return np.array([self.models[cls].decision_function(X) for cls in self.classes])

    def predict(self, X):
        """
        Predicts the targets for X using the ensemble of classifiers.
        :param X: Instances (n_samples x n_features)
        :return: Predicted targets (n_samples)
        """
        p = self.decision_function(X)
        return self.classes[np.argmax(p, axis=0)]

    def score(self, X_test, y_test):
        """
        Makes and evaluates a prediction. Returns the prediction accuracy (higher is better).
        :param X_test: Test instances (n_samples x n_features)
        :param y_test: Test targets (n_samples)
        :return: Prediction accuracy
        """
        y_pred = self.predict(X_test)
        return metrics.accuracy_score(y_test, y_pred)
