import constants
import reader
from logistic_regression import LogisticRegression
from multiclass import MulticlassOVR

import pickle


if __name__ == "__main__":
    X_train, y_train = reader.read_fold(constants.DATASET_PATH + "Fold1/train.txt")

    model = MulticlassOVR(LogisticRegression)
    model.fit(X_train, y_train)

    with open("models/model_ovr.pkl", "wb") as f:
        pickle.dump(model, f)
